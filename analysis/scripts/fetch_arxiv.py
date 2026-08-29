#!/usr/bin/env python3
"""Supplementary Track A retrieval from the arXiv API (CS / version-control slice).

arXiv only covers preprints (mainly physics, CS, maths). It is a supplement to the
OpenAlex primary corpus, used so the "GitHub / version control in research" strand
is not under-covered. Writes:

  data/raw/arxiv/works_<YYYYMMDD>.csv

Standard library only (urllib + xml.etree). arXiv asks for <=1 request / 3 s.

Usage:
  python3 analysis/scripts/fetch_arxiv.py
"""

import csv
import datetime as dt
import html
import os
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

API = "http://export.arxiv.org/api/query"
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUTDIR = os.path.join(ROOT, "data", "raw", "arxiv")
NS = {"a": "http://www.w3.org/2005/Atom"}

YEAR_MIN, YEAR_MAX = 2008, 2025

# arXiv search_query blocks. Scoped to the abstract (abs:) / title (ti:) on purpose:
# this is a *supplement* for the "version control / research software" strand, not a
# second primary corpus. `all:github` alone returns tens of thousands of CS papers
# that merely link a repo, so github terms are constrained to co-occur with a topical
# term and (where it helps) a relevant arXiv category.
CATS = "(cat:cs.DL OR cat:cs.SE OR cat:cs.CY OR cat:cs.DC)"
QUERIES = {
    "A1": 'abs:"version control" AND (abs:research OR abs:reproducibility OR abs:"scientific workflow" OR abs:"research software")',
    "A2": f'(ti:github OR abs:github) AND (abs:reproducibility OR abs:reproducible OR abs:"research software" OR abs:"scientific workflow" OR abs:"open science" OR abs:"version control") AND {CATS}',
    "A3": 'abs:"scientific workflow" AND (abs:provenance OR abs:reproducibility OR abs:"workflow management")',
    "A4": 'abs:"research software" AND (abs:sustainability OR abs:reproducibility OR abs:citation OR abs:workflow)',
    "A5": 'abs:"reproducible research" AND (abs:workflow OR abs:infrastructure OR abs:"version control" OR abs:"project management")',
}


def fetch_query(tag, query, page=200, cap=1200):
    out = []
    start = 0
    while start < cap:
        params = {
            "search_query": query,
            "start": start,
            "max_results": page,
            "sortBy": "submittedDate",
            "sortOrder": "ascending",
        }
        url = API + "?" + urllib.parse.urlencode(params)
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                root = ET.fromstring(r.read())
        except Exception as e:  # noqa: BLE001
            print(f"  {tag} start={start} error: {e}", file=sys.stderr)
            time.sleep(5)
            continue
        entries = root.findall("a:entry", NS)
        if not entries:
            break
        for e in entries:
            def txt(path):
                el = e.find(path, NS)
                return html.unescape(el.text.strip()) if el is not None and el.text else ""

            published = txt("a:published")
            year = published[:4]
            if not year.isdigit() or not (YEAR_MIN <= int(year) <= YEAR_MAX):
                continue
            arxiv_id = txt("a:id").rsplit("/", 1)[-1]
            doi_el = e.find("{http://arxiv.org/schemas/atom}doi")
            cats = [c.get("term") for c in e.findall("a:category", NS)]
            out.append({
                "arxiv_id": arxiv_id,
                "doi": doi_el.text.strip() if doi_el is not None and doi_el.text else "",
                "title": " ".join(txt("a:title").split()),
                "publication_year": year,
                "type": "preprint",
                "source": "arXiv",
                "source_type": "repository",
                "authors": "; ".join(
                    (a.find("a:name", NS).text or "").strip()
                    for a in e.findall("a:author", NS)
                ),
                "categories": "; ".join(cats),
                "abstract": " ".join(txt("a:summary").split()),
                "query_tags": tag,
            })
        start += page
        time.sleep(3)
    return out


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    by_id = {}
    for tag, q in QUERIES.items():
        rows = fetch_query(tag, q)
        print(f"{tag}: {len(rows)} in-window results  [{q}]")
        for r in rows:
            prev = by_id.get(r["arxiv_id"])
            if prev:
                prev["query_tags"] = "; ".join(sorted(set(prev["query_tags"].split("; ")) | {tag}))
            else:
                by_id[r["arxiv_id"]] = r

    rows = sorted(by_id.values(), key=lambda r: (r["publication_year"], r["title"].lower()))
    stamp = dt.date.today().strftime("%Y%m%d")
    path = os.path.join(OUTDIR, f"works_{stamp}.csv")
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"\nunique arXiv preprints: {len(rows)}\n  {path}")
    print("Log per-query counts in literature/search_log.md.")


if __name__ == "__main__":
    main()
