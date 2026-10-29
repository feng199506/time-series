#!/usr/bin/env python3
"""Fetch bibliographic metadata for the seed list.

Sources (all public APIs, no login):
  - arXiv API (export.arxiv.org)    : title, authors, versions, journal_ref, DOI, comment, abstract
  - Crossref REST API               : authoritative metadata for DOIs
  - OpenAlex API                    : open-access locations (pdf_url, host, version, license)
  - DBLP search API                 : conference/journal venue for CS papers known only via arXiv

Output: scripts/metadata_cache_en.json (raw-ish records keyed by seed id).
Requests are rate limited per host and retried at most 3 times.

Usage: python3 -I scripts/fetch_metadata_en.py <project_dir>
"""
import json
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

UA = "time_series_literature/1.0 (literature metadata collection; low rate)"
MIN_INTERVAL = {"export.arxiv.org": 3.5, "api.crossref.org": 1.0,
                "api.openalex.org": 1.0, "dblp.org": 6.0}
_last = {}


def get(url, accept="application/json"):
    host = urllib.parse.urlparse(url).netloc
    for attempt in range(3):
        wait = MIN_INTERVAL.get(host, 2.0) - (time.time() - _last.get(host, 0))
        if wait > 0:
            time.sleep(wait)
        _last[host] = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return 404, b""
            err = f"HTTP {e.code}"
            if e.code == 429:  # back off hard on rate limiting
                time.sleep(30)
        except Exception as e:  # network errors
            err = repr(e)
        print(f"  retry {attempt + 1}/3 {url}: {err}", file=sys.stderr)
        time.sleep(5 * (attempt + 1))
    return None, err.encode()


ATOM = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def arxiv_batch(ids):
    url = ("https://export.arxiv.org/api/query?max_results=200&id_list="
           + ",".join(ids))
    status, body = get(url, accept="application/atom+xml")
    out = {}
    if status != 200:
        print("arXiv API failed", status, file=sys.stderr)
        return out
    root = ET.fromstring(body)
    for e in root.findall("a:entry", ATOM):
        abs_url = e.findtext("a:id", "", ATOM)
        vid = abs_url.rsplit("/abs/", 1)[-1]
        base = vid.split("v")[0] if "v" in vid else vid
        rec = {
            "abs_url": abs_url,
            "latest_version": vid,
            "title": " ".join(e.findtext("a:title", "", ATOM).split()),
            "authors": [a.findtext("a:name", "", ATOM) for a in e.findall("a:author", ATOM)],
            "published": e.findtext("a:published", "", ATOM),
            "updated": e.findtext("a:updated", "", ATOM),
            "abstract": " ".join(e.findtext("a:summary", "", ATOM).split()),
            "comment": e.findtext("arxiv:comment", "", ATOM),
            "journal_ref": e.findtext("arxiv:journal_ref", "", ATOM),
            "doi": e.findtext("arxiv:doi", "", ATOM),
            "primary_category": (e.find("arxiv:primary_category", ATOM).get("term")
                                 if e.find("arxiv:primary_category", ATOM) is not None else ""),
        }
        out[base] = rec
    return out


def crossref(doi):
    status, body = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    if status != 200:
        return {"error": f"status {status}"}
    m = json.loads(body)["message"]
    year = None
    for k in ("published-print", "published-online", "issued"):
        if m.get(k, {}).get("date-parts"):
            year = m[k]["date-parts"][0][0]
            break
    return {
        "title": " ".join((m.get("title") or [""])[0].split()),
        "authors": [" ".join(filter(None, [a.get("given"), a.get("family")])) or a.get("name", "")
                    for a in m.get("author", [])],
        "year": year,
        "container": (m.get("container-title") or [""])[0],
        "volume": m.get("volume", ""), "issue": m.get("issue", ""), "page": m.get("page", ""),
        "type": m.get("type", ""), "url": m.get("URL", ""),
        "abstract": m.get("abstract", ""),
    }


def openalex(doi):
    status, body = get("https://api.openalex.org/works/doi:" + urllib.parse.quote(doi))
    if status != 200:
        return {"error": f"status {status}"}
    w = json.loads(body)
    locs = []
    for loc in w.get("locations", []):
        src = loc.get("source") or {}
        locs.append({"pdf_url": loc.get("pdf_url"), "landing": loc.get("landing_page_url"),
                     "is_oa": loc.get("is_oa"), "version": loc.get("version"),
                     "license": loc.get("license"), "source": src.get("display_name"),
                     "source_type": src.get("type"), "host_org": src.get("host_organization_name")})
    inv = w.get("abstract_inverted_index") or {}
    abstract = ""
    if inv:
        pos = sorted((p, word) for word, ps in inv.items() for p in ps)
        abstract = " ".join(word for _, word in pos)
    return {"id": w.get("id"), "title": w.get("title"), "year": w.get("publication_year"),
            "oa_status": (w.get("open_access") or {}).get("oa_status"),
            "locations": locs, "abstract": abstract}


def dblp(title):
    q = urllib.parse.quote(title)
    status, body = get(f"https://dblp.org/search/publ/api?q={q}&format=json&h=10")
    if status != 200:
        return {"error": f"status {status}"}
    hits = json.loads(body).get("result", {}).get("hits", {}).get("hit", [])
    out = []
    for h in hits:
        i = h.get("info", {})
        out.append({"title": i.get("title"), "venue": i.get("venue"), "year": i.get("year"),
                    "type": i.get("type"), "doi": i.get("doi"), "ee": i.get("ee"),
                    "key": i.get("key")})
    return {"hits": out}


def main():
    proj = Path(sys.argv[1])
    seeds = json.loads((proj / "scripts/seed_list_cn.json").read_text())
    cache_path = proj / "scripts/metadata_cache_en.json"
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}

    ax_ids = [s["arxiv"] for s in seeds if s.get("arxiv") and "arxiv" not in cache.get(s["id"], {})]
    ax = arxiv_batch(ax_ids) if ax_ids else {}
    for s in seeds:
        rec = cache.setdefault(s["id"], {})
        if s.get("arxiv") and "arxiv" not in rec:
            rec["arxiv"] = ax.get(s["arxiv"], {"error": "not returned by arXiv API"})
        doi = s.get("doi") or (rec.get("arxiv", {}).get("doi") or "")
        if doi and "crossref" not in rec:
            print("crossref", s["id"], doi, file=sys.stderr)
            rec["crossref"] = crossref(doi)
        if doi and "openalex" not in rec:
            rec["openalex"] = openalex(doi)
        title = rec.get("arxiv", {}).get("title") or rec.get("crossref", {}).get("title")
        # DBLP only when arXiv itself carries no journal_ref/DOI (venue unknown)
        ax_rec = rec.get("arxiv", {})
        if (s.get("arxiv") and title and "dblp" not in rec
                and not ax_rec.get("journal_ref") and not ax_rec.get("doi")):
            print("dblp", s["id"], file=sys.stderr)
            rec["dblp"] = dblp(title)
        cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=1))
    print(f"done: {len(cache)} records -> {cache_path}")


if __name__ == "__main__":
    main()
