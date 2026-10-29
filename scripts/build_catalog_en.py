#!/usr/bin/env python3
"""Merge seed list, metadata, venue checks, annotations and download results into
the deliverable tables:

  catalog_cn.csv            structured catalogue (Chinese headers/annotations, English metadata)
  download_failures_cn.csv  failed downloads and link-only entries
  checksums_en.sha256       sha256sum-compatible list of accepted PDFs (run from project root)

Usage: python3 -I scripts/build_catalog_en.py <project_dir>
"""
import csv
import json
import re
import sys
from pathlib import Path

WINDOW_START, WINDOW_END = "2023-10-29", "2026-10-29"

# Venue evidence found by hand on an official page (not in the proceedings indexes).
MANUAL_VENUE = {
    "TS038": ("NeurIPS 2025", "https://papers.neurips.cc/paper_files/paper/2025/hash/"
              "5356603f9c47399adfd372f77a677057-Abstract-Conference.html"),
}
# Version notes that need a human-readable explanation (Chinese, goes into the CSV).
VERSION_NOTES = {
    "TS003": "重大修订：v1（2025-02）标题为 “Beyond the Time Domain: Recent Advances on Frequency Transforms in Time Series Analysis”，后续版本改为现标题；下载为最新版。",
    "TS021": "重大修订：v4 增加带协变量预测评测、消融与局限讨论（据 arXiv comments）。",
    "TS037": "同一模型更早的技术报告为 arXiv:2407.07874（“Toto: Time Series Optimized Transformer for Observability”，2024-07），属不同 arXiv 条目，本库未单独收录/下载；本条为 2025 年论文（新增 BOOM 基准）。",
    "TS048": "重大修订：v1（2025-02）标题以 “Position:” 开头，v2（2026-01）改为现标题并注明 TMLR 接收。",
    "TS050": "v3 为技术报告修订（增加作者、更正参考文献，据 arXiv comments）。",
}
OLD_VERSION = {
    "TS054": ("出版社正式版（Journal of Statistical Software，开放获取）", "2008-07（PDF 首页：July 2008, Vol. 27, Issue 3；精度：月）"),
    "TS055": ("作者主页预印本（robjhyndman.com），非出版社排版版", "2005-11-02（PDF 首页注明日期）"),
    "TS056": ("出版社排版版（JASA 2007 Vol.102 No.477，PDF 首页含 © 2007 ASA），由作者主页（华盛顿大学 Raftery）自存档托管；出版社是否授权该自存档未核实", "2007-03（PDF 首页；精度：月）"),
    "TS057": ("作者主页工作论文/投稿版（robjhyndman.com/papers/cv-wp.pdf，首页注 Preprint submitted），非出版社排版版", "2017-07-23（PDF 元数据创建日期）"),
}


def main():
    proj = Path(sys.argv[1])
    seeds = json.loads((proj / "scripts/seed_list_cn.json").read_text())
    meta = json.loads((proj / "scripts/metadata_cache_en.json").read_text())
    ann = json.loads((proj / "scripts/annotations_cn.json").read_text())
    dl = json.loads((proj / "scripts/download_results_en.json").read_text())
    vc = json.loads((proj / "scripts/venue_check_en.json").read_text())["matches"]

    rows, fails, sums = [], [], []
    for s in seeds:
        sid = s["id"]
        m = meta.get(sid, {})
        ax, cr = m.get("arxiv") or {}, m.get("crossref") or {}
        d = dl.get(sid, {})
        title = re.sub(r"<[^>]+>", "", ax.get("title") or cr.get("title") or "")
        authors = ax.get("authors") or cr.get("authors") or []
        first_pub = (ax.get("published") or "")[:10]
        precision = "日（arXiv v1 提交日，UTC）" if first_pub else "年（仅核实到出版年）"
        if not first_pub:
            first_pub = str(cr.get("year") or "")
        old = s.get("era") == "old"
        if old:
            window = "三年前（补充/基础，不计入近三年）"
        elif len(first_pub) == 10 and WINDOW_START <= first_pub <= WINDOW_END:
            window = "近三年"
        else:
            window = "待核实（日期边界或精度不足）"

        # venue & formal publication
        doi = s.get("doi") or ax.get("doi") or ""
        venue, venue_basis, formal = "", "", ""
        if cr.get("container"):
            venue = cr["container"]
            vol = f", vol. {cr['volume']}" if cr.get("volume") else ""
            pages = f", pp. {cr['page']}" if cr.get("page") else ""
            venue += vol + pages
            venue_basis = "Crossref（DOI 元数据）"
            formal = f"{cr.get('year')}（精度：年，Crossref）"
        elif vc.get(sid):
            v = vc[sid][0]
            venue = v["venue"]
            venue_basis = f"官方论文集索引页标题匹配：{v['index']}"
            formal = f"{re.search(r'20[0-9]{2}', v['venue']).group(0)}（会议年份，精度：年）"
        elif sid in MANUAL_VENUE:
            venue, url = MANUAL_VENUE[sid]
            venue_basis = f"官方论文页：{url}"
            formal = "2025（会议年份，精度：年）"
        else:
            comment = ax.get("comment") or ""
            claim = re.search(r"(NeurIPS|ICLR|ICML|AAAI|AISTATS|TMLR|KDD|VLDB)[^.;,]*", comment)
            if claim:
                venue = f"arXiv 预印本（作者在 arXiv comments 中声明：{claim.group(0).strip()}）"
                venue_basis = "仅 arXiv comments 自述，未在官方页面核实"
                formal = "未核实"
            else:
                venue = "arXiv 预印本"
                venue_basis = "未发现正式发表信息（未核实是否已发表）"
                formal = "未核实/未发现"

        landing = ax.get("abs_url", "").replace("http://", "https://") or (f"https://doi.org/{doi}" if doi else "")
        if ax.get("latest_version"):
            version = f"arXiv {ax['latest_version']}（最新版）"
            version_date = (ax.get("updated") or "")[:10]
        else:
            version, version_date = OLD_VERSION.get(sid, ("", "未核实"))
        vnote = VERSION_NOTES.get(sid, "")

        status = d.get("status", "not_run")
        if status == "ok":
            dl_status = "成功"
            check = (f"通过：HTTP 200；%PDF 文件头；pypdf 可解析（{d.get('pages')} 页）；"
                     f"首页标题词匹配率 {d.get('title_match')}")
            sums.append(f"{d['sha256']}  {d['local_path']}")
        else:
            dl_status = "失败" if status == "failed" else "仅链接"
            check = "未通过/未下载：" + (d.get("reason") or "")
            fails.append({
                "文献编号": sid, "标题": title, "原始页面": landing,
                "尝试的PDF URL": " | ".join(t.get("url", "") for t in d.get("tries", [])),
                "失败原因": d.get("reason", ""),
                "处理建议": "保留原始链接；如需全文请通过机构订阅或作者联系获取，不绕过访问限制",
            })

        summ = ann.get(sid, "")
        rows.append({
            "文献编号": sid, "主题": s["topic"], "子主题": s.get("sub", ""), "时间窗口": window,
            "标题": title, "作者": "; ".join(authors), "首次公开年份": first_pub[:4],
            "首次公开日期": first_pub, "日期精度": precision, "正式发表日期": formal,
            "渠道": venue, "渠道核验依据": venue_basis, "DOI": doi,
            "arXiv ID": s.get("arxiv", ""), "原始页面": landing,
            "PDF URL": d.get("pdf_url", ""), "本地相对路径": d.get("local_path", ""),
            "版本": version, "下载版本日期": version_date, "版本说明": vnote,
            "下载状态": dl_status, "核验状态": check, "SHA256": d.get("sha256", ""),
            "选入理由": s["reason"], "三年前保留理由": s.get("old_reason", ""),
            "内容简介": summ,
            "简介依据": s.get("summary_basis", "摘要（arXiv API / Crossref 返回的摘要）；未读全文，未核实全文结论") if summ else "",
            "阅读优先级": {1: "高", 2: "中", 3: "低"}[s["priority"]],
        })

    with open(proj / "catalog_cn.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    fail_fields = ["文献编号", "标题", "原始页面", "尝试的PDF URL", "失败原因", "处理建议"]
    with open(proj / "download_failures_cn.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fail_fields)
        w.writeheader()
        w.writerows(fails)
    (proj / "checksums_en.sha256").write_text("\n".join(sorted(sums, key=lambda x: x.split()[1])) + "\n")

    recent = [r for r in rows if r["时间窗口"] == "近三年"]
    print(json.dumps({
        "total": len(rows), "recent": len(recent),
        "recent_share": round(len(recent) / len(rows), 3),
        "old": sum(r["时间窗口"].startswith("三年前") for r in rows),
        "pending": sum(r["时间窗口"].startswith("待核实") for r in rows),
        "downloaded": len(sums),
        "recent_downloaded": sum(r["下载状态"] == "成功" for r in recent),
        "failed_or_link_only": len(fails),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
