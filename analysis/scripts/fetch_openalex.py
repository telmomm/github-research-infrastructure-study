#!/usr/bin/env python3
"""Fetch the Track A primary corpus from the OpenAlex API.

Open, reproducible bibliometric retrieval. Runs a fixed list of queries
(mirroring literature/search_strings.md), pages through results with cursor
pagination, reconstructs abstracts from the inverted index, and writes:

  data/raw/openalex/works_<YYYYMMDD>.jsonl   full records, one JSON per line
  data/raw/openalex/works_<YYYYMMDD>.csv     flattened, one row per work

Standard library only. Polite pool: pass --mailto <email>.

Usage:
  python3 analysis/scripts/fetch_openalex.py --mailto you@example.org
  python3 analysis/scripts/fetch_openalex.py --mailto you@example.org --dry-run   # counts only
"""

import argparse
import csv
import datetime as dt
import json
import os
import sys
import time
import urllib.parse
import urllib.request

BASE = "https://api.openalex.org/works"
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUTDIR = os.path.join(ROOT, "data", "raw", "openalex")

FROM_DATE = "2008-01-01"
TO_DATE = "2025-12-31"
TYPES = "article|review|proceedings-article"

# Query tags -> title_and_abstract.search strings. Quoted phrases are ANDed with
# bare terms by OpenAlex; run several narrow queries and union client-side.
QUERIES = {
    "Q1a": '"research project management" (scientific OR academic OR research)',
    "Q1b": '"research workflow management"',
    "Q1c": '"research workflow" (management OR coordination OR documentation OR provenance)',
    "Q1d": '"research lifecycle" (management OR infrastructure OR platform OR coordination)',
    "Q1e": '"research life cycle" (management OR infrastructure OR platform)',
    "Q1f": '"research process management"',
    "Q1g": '"scientific workflow" (management OR collaboration OR documentation OR provenance)',
    "Q2a": '"research data management" (workflow OR lifecycle OR infrastructure OR platform OR "project management")',
    "Q2b": '"open science" (workflow OR infrastructure OR "project management" OR lifecycle)',
    "Q2c": '"reproducible research" (workflow OR infrastructure OR "project management")',
    "Q3a": 'github (research OR science OR scholarly) (workflow OR "project management" OR reproducibility OR provenance OR collaboration)',
    "Q3b": '"version control" (research OR science OR scholarly) (workflow OR "project management" OR reproducibility OR documentation)',
    "Q4a": '"virtual research environment" (workflow OR lifecycle OR "project management" OR coordination)',
    "Q4b": '"science gateway" (workflow OR lifecycle OR "project management" OR coordination)',
    "Q4c": '"research information system" (workflow OR lifecycle OR coordination OR interoperability)',
}


def build_url(search, cursor, mailto):
    filt = ",".join([
        f"title_and_abstract.search:{search}",
        f"from_publication_date:{FROM_DATE}",
        f"to_publication_date:{TO_DATE}",
        f"type:{TYPES}",
    ])
    params = {"filter": filt, "per-page": "200", "cursor": cursor}
    if mailto:
        params["mailto"] = mailto
    return BASE + "?" + urllib.parse.urlencode(params, safe=":|")


def get(url, tries=5):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "track-a-fetch/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # noqa: BLE001
            wait = 2 ** i
            print(f"  retry {i + 1}/{tries} after {wait}s ({e})", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"failed: {url}")


def abstract_from_index(idx):
    if not idx:
        return ""
    positions = []
    for word, locs in idx.items():
        for loc in locs:
            positions.append((loc, word))
    positions.sort()
    return " ".join(w for _, w in positions)


def flatten(work, tags):
    auth = work.get("authorships", []) or []
    concepts = work.get("concepts", []) or []
    primary = work.get("primary_location") or {}
    source = primary.get("source") or {}
    return {
        "openalex_id": (work.get("id") or "").rsplit("/", 1)[-1],
        "doi": (work.get("doi") or "").replace("https://doi.org/", ""),
        "title": work.get("title") or "",
        "publication_year": work.get("publication_year") or "",
        "type": work.get("type") or "",
        "source": source.get("display_name") or "",
        "source_type": source.get("type") or "",
        "cited_by_count": work.get("cited_by_count") or 0,
        "referenced_works_count": len(work.get("referenced_works", []) or []),
        "language": work.get("language") or "",
        "is_oa": (work.get("open_access") or {}).get("is_oa", ""),
        "oa_status": (work.get("open_access") or {}).get("oa_status", ""),
        "authors": "; ".join(a.get("author", {}).get("display_name", "") for a in auth),
        "institutions": "; ".join(
            sorted({i.get("display_name", "") for a in auth for i in (a.get("institutions") or [])})
        ),
        "countries": "; ".join(
            sorted({i.get("country_code", "") for a in auth for i in (a.get("institutions") or []) if i.get("country_code")})
        ),
        "concepts": "; ".join(f"{c.get('display_name')}:{c.get('score'):.2f}" for c in concepts[:6]),
        "topics": "; ".join(t.get("display_name", "") for t in (work.get("topics") or [])[:3]),
        "keywords": "; ".join(k.get("display_name", k.get("keyword", "")) for k in (work.get("keywords") or [])),
        "abstract": abstract_from_index(work.get("abstract_inverted_index")),
        "query_tags": "; ".join(sorted(tags)),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mailto", default="", help="contact email for the OpenAlex polite pool")
    ap.add_argument("--dry-run", action="store_true", help="print per-query counts, fetch nothing")
    args = ap.parse_args()

    os.makedirs(OUTDIR, exist_ok=True)
    stamp = dt.date.today().strftime("%Y%m%d")
    works = {}          # openalex_id -> raw work
    tags_by_id = {}     # openalex_id -> set of query tags
    counts = {}

    for tag, search in QUERIES.items():
        cursor = "*"
        n = 0
        while cursor:
            data = get(build_url(search, cursor, args.mailto))
            if cursor == "*":
                total = data.get("meta", {}).get("count", 0)
                counts[tag] = total
                print(f"{tag}: {total} results  [{search}]")
                if args.dry_run:
                    break
            for w in data.get("results", []):
                wid = (w.get("id") or "").rsplit("/", 1)[-1]
                works.setdefault(wid, w)
                tags_by_id.setdefault(wid, set()).add(tag)
                n += 1
            cursor = data.get("meta", {}).get("next_cursor")
            time.sleep(0.2)
        if not args.dry_run:
            print(f"  fetched {n} (running unique: {len(works)})")

    if args.dry_run:
        print(f"\nsum of per-query totals (with overlap): {sum(counts.values())}")
        return

    jsonl_path = os.path.join(OUTDIR, f"works_{stamp}.jsonl")
    with open(jsonl_path, "w", encoding="utf-8") as fh:
        for wid, w in works.items():
            w["_query_tags"] = sorted(tags_by_id[wid])
            fh.write(json.dumps(w, ensure_ascii=False) + "\n")

    rows = [flatten(w, tags_by_id[wid]) for wid, w in works.items()]
    rows.sort(key=lambda r: (str(r["publication_year"]), r["title"].lower()))
    csv_path = os.path.join(OUTDIR, f"works_{stamp}.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print(f"\nunique works: {len(works)}")
    print(f"  {jsonl_path}")
    print(f"  {csv_path}")
    print("\nLog per-query counts in literature/search_log.md.")


if __name__ == "__main__":
    main()
