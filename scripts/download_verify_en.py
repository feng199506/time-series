#!/usr/bin/env python3
"""Download and verify public PDFs for the seed list.

For every seed entry:
  1. pick the PDF URL (arXiv: the exact latest version reported by the arXiv API;
     otherwise the vetted URLs in seed "pdf_candidates");
  2. download into a fresh, empty staging directory (never directly into pdfs/);
  3. check HTTP status, the %PDF- magic header, that pypdf can parse it, and that
     the title is found in the text of the first page(s);
  4. compute SHA256, de-duplicate by identifier and by hash;
  5. move accepted files to pdfs/<year>_<FirstAuthor>_<ShortTitle>_en.pdf.

Nothing behind a paywall, login or captcha is attempted. Requests are rate
limited per host; each URL is tried at most 3 times.

Results go to scripts/download_results_en.json (re-runs skip verified files).

Usage:
  python3 -I scripts/download_verify_en.py <project_dir> <staging_dir> <pypdf_lib_dir>
"""
import hashlib
import json
import re
import shutil
import sys
import tempfile
import time
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

UA = "time_series_literature/1.0 (literature collection; low rate)"
MIN_INTERVAL = {"arxiv.org": 4.0}
DEFAULT_INTERVAL = 3.0
_last = {}

STOP = {"a", "an", "the", "of", "for", "and", "in", "on", "with", "to", "via", "by",
        "is", "are", "from", "at", "as", "its", "do", "how", "much", "can"}


def fold(s):
    s = re.sub(r"[{}\\]", "", s)
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()


def short_title(title):
    title = fold(re.sub(r"<[^>]+>", "", title))
    head = title.split(":")[0].strip()
    if ":" in title and len(head.split()) <= 3:
        words = head.split()
    else:
        words = [w for w in re.findall(r"[A-Za-z0-9]+", title) if w.lower() not in STOP][:4]
    out = "".join(w[:1].upper() + w[1:] for w in re.findall(r"[A-Za-z0-9]+", " ".join(words)))
    return out[:40]


def surname(name):
    return re.sub(r"[^A-Za-z]", "", fold(name).split()[-1]) or "Anon"


def tokens(s):
    return [t for t in re.findall(r"[a-z0-9]+", fold(s).lower()) if t not in STOP and len(t) > 1]


def title_match(title, text):
    """Fraction of title tokens present in the first-page text (whitespace-insensitive)."""
    tt = tokens(re.sub(r"<[^>]+>", "", title))
    blob = re.sub(r"[^a-z0-9]", "", fold(text).lower())
    if not tt:
        return 0.0
    return sum(1 for t in tt if t in blob) / len(tt)


def fetch(url, dest):
    host = urllib.parse.urlparse(url).netloc
    host_key = "arxiv.org" if host.endswith("arxiv.org") else host
    err = ""
    for attempt in range(3):
        wait = MIN_INTERVAL.get(host_key, DEFAULT_INTERVAL) - (time.time() - _last.get(host_key, 0))
        if wait > 0:
            time.sleep(wait)
        _last[host_key] = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/pdf"})
            with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
                shutil.copyfileobj(r, f)
                return {"http_status": r.status, "content_type": r.headers.get("Content-Type", ""),
                        "final_url": r.geturl(), "attempts": attempt + 1}
        except urllib.error.HTTPError as e:
            err = f"HTTP {e.code}"
            if e.code in (401, 402, 403, 404, 451):  # access denied / missing: do not hammer
                return {"http_status": e.code, "error": err, "attempts": attempt + 1}
        except Exception as e:
            err = repr(e)
        time.sleep(10 * (attempt + 1))
    return {"http_status": None, "error": err, "attempts": 3}


def inspect_pdf(path, title):
    import pypdf
    info = {}
    with open(path, "rb") as f:
        head = f.read(1024)
    info["magic_ok"] = head.lstrip().startswith(b"%PDF-")
    if not info["magic_ok"]:
        info["error"] = "not a PDF (magic header missing): " + head[:60].decode("latin-1", "replace")
        return info
    try:
        reader = pypdf.PdfReader(str(path))
        info["pages"] = len(reader.pages)
        text = ""
        for i in range(min(2, len(reader.pages))):
            text += (reader.pages[i].extract_text() or "") + "\n"
        info["first_text_chars"] = len(text)
        info["first_text_head"] = " ".join(text.split())[:300]
        info["title_match"] = round(title_match(title, text), 3)
        letters = [ch for ch in text if ch.isalpha()]
        info["ascii_letter_ratio"] = round(sum(ch.isascii() for ch in letters) / max(1, len(letters)), 3)
        info["parse_ok"] = True
    except Exception as e:
        info["parse_ok"] = False
        info["error"] = "pypdf failed: " + repr(e)[:200]
    return info


def main():
    proj, staging_root, pylib = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
    sys.path.insert(0, pylib)
    seeds = json.loads((proj / "scripts/seed_list_cn.json").read_text())
    meta = json.loads((proj / "scripts/metadata_cache_en.json").read_text())
    res_path = proj / "scripts/download_results_en.json"
    results = json.loads(res_path.read_text()) if res_path.exists() else {}
    pdf_dir = proj / "pdfs"
    staging_root.mkdir(parents=True, exist_ok=True)
    seen_hash = {r["sha256"]: k for k, r in results.items() if r.get("status") == "ok"}

    for s in seeds:
        sid = s["id"]
        if results.get(sid, {}).get("status") == "ok" and (proj / results[sid]["local_path"]).exists():
            continue
        m = meta.get(sid, {})
        ax, cr = m.get("arxiv") or {}, m.get("crossref") or {}
        title = ax.get("title") or cr.get("title") or ""
        authors = ax.get("authors") or cr.get("authors") or ["Anon"]
        year = (ax.get("published") or "")[:4] or str(cr.get("year") or "")
        urls = []
        if ax.get("latest_version"):
            urls.append(("arXiv " + ax["latest_version"], "https://arxiv.org/pdf/" + ax["latest_version"]))
        for u in s.get("pdf_candidates", []):
            urls.append(("candidate", u))
        rec = {"title": title, "tries": []}
        if not urls:
            rec.update(status="link_only", reason="no legal public PDF URL identified")
            results[sid] = rec
            continue
        fname = f"{year}_{surname(authors[0])}_{short_title(title)}_en.pdf"
        for label, url in urls:
            stage = Path(tempfile.mkdtemp(prefix=sid + "_", dir=staging_root))
            dest = stage / "download.bin"
            print(f"{sid} GET {url}", file=sys.stderr)
            t = {"label": label, "url": url, **fetch(url, dest)}
            if t.get("http_status") == 200 and dest.exists():
                t.update(inspect_pdf(dest, title))
                ok = t.get("magic_ok") and t.get("parse_ok") and t.get("title_match", 0) >= 0.8
                if ok:
                    sha = hashlib.sha256(dest.read_bytes()).hexdigest()
                    if sha in seen_hash and seen_hash[sha] != sid:
                        t["error"] = f"duplicate of {seen_hash[sha]} (same SHA256)"
                    else:
                        target = pdf_dir / fname
                        if target.exists() and hashlib.sha256(target.read_bytes()).hexdigest() != sha:
                            t["error"] = f"refusing to overwrite different existing file {fname}"
                        else:
                            shutil.move(str(dest), target)
                            seen_hash[sha] = sid
                            rec.update(status="ok", local_path=f"pdfs/{fname}", sha256=sha,
                                       size=target.stat().st_size, pdf_url=url, version_label=label,
                                       pages=t.get("pages"), title_match=t.get("title_match"))
                elif t.get("magic_ok") and t.get("parse_ok"):
                    t["error"] = f"title not found on first pages (match={t.get('title_match')})"
            rec["tries"].append(t)
            shutil.rmtree(stage, ignore_errors=True)
            if rec.get("status") == "ok":
                break
        if rec.get("status") != "ok":
            rec["status"] = "failed"
            rec["reason"] = "; ".join(f"{t['label']}: {t.get('error') or t.get('http_status')}" for t in rec["tries"])
        results[sid] = rec
        res_path.write_text(json.dumps(results, ensure_ascii=False, indent=1))
    res_path.write_text(json.dumps(results, ensure_ascii=False, indent=1))
    n_ok = sum(r.get("status") == "ok" for r in results.values())
    print(f"done: {n_ok}/{len(results)} ok -> {res_path}")


if __name__ == "__main__":
    main()
