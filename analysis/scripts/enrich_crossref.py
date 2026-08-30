#!/usr/bin/env python3
"""Crossref enrichment for Track A corpus records without a DOI (OPEN_ITEMS 2.1).

For each no-DOI corpus record, query Crossref by bibliographic string and, when the
top hit matches on title (token Jaccard >= THRESH) and year (+/- 1), record its DOI,
type and citation count. Writes a SIDE table; corpus.csv is left unchanged so its
provenance stays clean.

Input : data/processed/corpus.csv
Output: data/processed/corpus_enrichment.csv  +  results/track_a/enrichment_summary.md

Usage: python3 analysis/scripts/enrich_crossref.py --mailto you@example.org [--limit 400]
Standard library only.
"""

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CORPUS = os.path.join(ROOT, "data", "processed", "corpus.csv")
OUT_CSV = os.path.join(ROOT, "data", "processed", "corpus_enrichment.csv")
OUT_MD = os.path.join(ROOT, "results", "track_a", "enrichment_summary.md")
THRESH = 0.6


def read(p):
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def toks(s):
    return set(re.findall(r"[a-z0-9]+", (s or "").lower()))


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def query(title, year, mailto):
    q = urllib.parse.urlencode({"query.bibliographic": f"{title} {year}".strip(), "rows": "1"})
    url = f"https://api.crossref.org/works?{q}"
    if mailto:
        url += f"&mailto={urllib.parse.quote(mailto)}"
    req = urllib.request.Request(url, headers={"User-Agent": f"track-a-enrich/1.0 (mailto:{mailto or 'n/a'})"})
    for i in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception:  # noqa: BLE001
            time.sleep(2 ** i)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mailto", default="")
    ap.add_argument("--limit", type=int, default=400)
    args = ap.parse_args()

    rows = read(CORPUS)
    no_doi = [r for r in rows if not (r.get("doi") or "").strip()][: args.limit]
    print(f"no-DOI records: {sum(1 for r in rows if not (r.get('doi') or '').strip())}; processing {len(no_doi)}")

    out = []
    matched = 0
    for i, r in enumerate(no_doi, 1):
        title = r.get("title", "")
        year = (r.get("publication_year", "") or "").strip()
        data = query(title, year, args.mailto)
        time.sleep(0.4)
        hit = None
        if data:
            items = data.get("message", {}).get("items", [])
            if items:
                it = items[0]
                cr_title = " ".join(it.get("title", []) or [])
                sim = jaccard(toks(title), toks(cr_title))
                cr_year = ""
                for k in ("published-print", "published-online", "issued"):
                    dp = it.get(k, {}).get("date-parts", [[None]])
                    if dp and dp[0] and dp[0][0]:
                        cr_year = str(dp[0][0]); break
                year_ok = (not year or not cr_year) or abs(int(year) - int(cr_year)) <= 1
                if sim >= THRESH and year_ok:
                    hit = {
                        "corpus_id": r.get("corpus_id", ""),
                        "matched_doi": it.get("DOI", ""),
                        "crossref_type": it.get("type", ""),
                        "crossref_cited_by": it.get("is-referenced-by-count", ""),
                        "title_sim": round(sim, 2),
                        "crossref_title": cr_title[:160],
                    }
        if hit:
            out.append(hit); matched += 1
        if i % 50 == 0:
            print(f"  {i}/{len(no_doi)}  matched {matched}")

    os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["corpus_id", "matched_doi", "crossref_type",
                                           "crossref_cited_by", "title_sim", "crossref_title"])
        w.writeheader()
        w.writerows(out)

    rate = matched / len(no_doi) if no_doi else 0
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write(
            "# Crossref enrichment (OPEN_ITEMS 2.1)\n\n"
            f"- No-DOI corpus records processed: {len(no_doi)}\n"
            f"- Confident Crossref matches (title Jaccard >= {THRESH}, year +/-1): "
            f"**{matched}** ({rate:.0%})\n"
            f"- Output: `data/processed/corpus_enrichment.csv` (side table; corpus.csv unchanged)\n\n"
            "Most no-DOI records are preprints, reports, or venue types Crossref does not index; "
            "the matched DOIs and citation counts are available for the manuscript's descriptive "
            "statistics but are not merged into the frozen corpus. OpenAlex `cited_by_count` "
            "remains the primary citation field for RQ1.\n")
    print(f"\nmatched {matched}/{len(no_doi)} ({rate:.0%})  ->  {OUT_CSV}")


if __name__ == "__main__":
    main()
