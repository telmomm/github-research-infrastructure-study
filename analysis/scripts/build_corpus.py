#!/usr/bin/env python3
"""Merge Track A source exports into one de-duplicated corpus.

Inputs (whichever exist, newest file per source):
  data/raw/openalex/works_*.csv     primary
  data/raw/arxiv/works_*.csv        supplementary
  data/raw/manual/*.csv             snowballing / Google Scholar spot checks
                                    (needs columns: title, doi, publication_year, source; others optional)

Output:
  data/processed/corpus.csv         one row per de-duplicated work
  data/processed/dedup_report.md    counts at each step

De-duplication: exact DOI (normalised), then normalised title + year.
Standard library only.
"""

import csv
import glob
import os
import re
import sys
import datetime as dt

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW = os.path.join(ROOT, "data", "raw")
OUT = os.path.join(ROOT, "data", "processed")

FIELDS = [
    "corpus_id", "source_dataset", "openalex_id", "arxiv_id", "doi",
    "title", "publication_year", "type", "source", "source_type",
    "cited_by_count", "authors", "institutions", "countries",
    "concepts", "topics", "keywords", "abstract", "query_tags",
]


def newest(pattern):
    files = sorted(glob.glob(pattern))
    return files[-1] if files else None


def norm_doi(d):
    d = (d or "").strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    return d


def norm_title(t):
    t = (t or "").lower()
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return " ".join(t.split())


def load(path, dataset):
    if not path:
        return []
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    for r in rows:
        r["source_dataset"] = dataset
    print(f"  {dataset}: {len(rows)} rows  ({os.path.relpath(path, ROOT)})")
    return rows


def main():
    os.makedirs(OUT, exist_ok=True)
    sources = []
    sources += load(newest(os.path.join(RAW, "openalex", "works_*.csv")), "openalex")
    sources += load(newest(os.path.join(RAW, "arxiv", "works_*.csv")), "arxiv")
    for m in sorted(glob.glob(os.path.join(RAW, "manual", "*.csv"))):
        sources += load(m, "manual:" + os.path.splitext(os.path.basename(m))[0])

    if not sources:
        print("no source exports found under data/raw/ — run fetch_openalex.py first", file=sys.stderr)
        sys.exit(1)

    total_in = len(sources)

    # Optional: drop pure data/software-repository deposits (not scholarly documents).
    # One source-name substring per line in data/raw/exclude_sources.txt (case-insensitive).
    excl_fp = os.path.join(RAW, "exclude_sources.txt")
    excluded_repo = 0
    if os.path.exists(excl_fp):
        with open(excl_fp, encoding="utf-8") as fh:
            patterns = [ln.strip().lower() for ln in fh if ln.strip() and not ln.startswith("#")]
        kept = []
        for r in sources:
            src = (r.get("source") or "").lower()
            if any(p in src for p in patterns):
                excluded_repo += 1
            else:
                kept.append(r)
        sources = kept
        print(f"  excluded {excluded_repo} records by data/raw/exclude_sources.txt")
    by_doi = {}
    no_doi = []
    dup_doi = 0
    for r in sources:
        d = norm_doi(r.get("doi"))
        if d:
            if d in by_doi:
                dup_doi += 1
                merge_tags(by_doi[d], r)
            else:
                by_doi[d] = r
        else:
            no_doi.append(r)

    by_title = {}
    dup_title = 0
    kept_no_doi = []
    for r in no_doi:
        key = (norm_title(r.get("title")), str(r.get("publication_year", "")).strip())
        if not key[0]:
            continue
        if key in by_title:
            dup_title += 1
            merge_tags(by_title[key], r)
        else:
            by_title[key] = r
            kept_no_doi.append(r)

    # also drop no-doi rows whose title+year collides with a DOI row
    doi_titlekeys = {(norm_title(r.get("title")), str(r.get("publication_year", "")).strip()) for r in by_doi.values()}
    cross = 0
    final_no_doi = []
    for r in kept_no_doi:
        key = (norm_title(r.get("title")), str(r.get("publication_year", "")).strip())
        if key in doi_titlekeys:
            cross += 1
        else:
            final_no_doi.append(r)

    corpus = list(by_doi.values()) + final_no_doi
    corpus.sort(key=lambda r: (str(r.get("publication_year", "")), norm_title(r.get("title"))))
    for i, r in enumerate(corpus, 1):
        r["corpus_id"] = f"C{i:04d}"

    out_csv = os.path.join(OUT, "corpus.csv")
    with open(out_csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        for r in corpus:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    by_year = {}
    by_src = {}
    for r in corpus:
        by_year[r.get("publication_year", "")] = by_year.get(r.get("publication_year", ""), 0) + 1
        by_src[r.get("source_dataset", "")] = by_src.get(r.get("source_dataset", ""), 0) + 1

    lines = []
    lines.append("# Track A corpus — de-duplication report\n")
    lines.append(f"- Generated: {dt.date.today().isoformat()}")
    lines.append(f"- Input rows (all sources): **{total_in}**")
    lines.append(f"- Removed as data/software-repository deposits (exclude_sources.txt): {excluded_repo}")
    lines.append(f"- Removed as duplicate DOI: {dup_doi}")
    lines.append(f"- Removed as duplicate title+year (no DOI): {dup_title}")
    lines.append(f"- Removed as no-DOI row matching a DOI row on title+year: {cross}")
    lines.append(f"- **Corpus: {len(corpus)}**  ({len(by_doi)} with DOI, {len(final_no_doi)} without)\n")
    lines.append("## By source dataset\n")
    for k, v in sorted(by_src.items()):
        lines.append(f"- {k}: {v}")
    lines.append("\n## By publication year\n")
    for k in sorted(by_year):
        lines.append(f"- {k}: {by_year[k]}")
    lines.append("")
    with open(os.path.join(OUT, "dedup_report.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    print(f"\ncorpus: {len(corpus)} works")
    print(f"  {out_csv}")
    print(f"  {os.path.join(OUT, 'dedup_report.md')}")


def merge_tags(keep, drop):
    a = set(filter(None, str(keep.get("query_tags", "")).replace(",", ";").split(";")))
    b = set(filter(None, str(drop.get("query_tags", "")).replace(",", ";").split(";")))
    keep["query_tags"] = "; ".join(sorted(t.strip() for t in (a | b) if t.strip()))
    if drop.get("source_dataset") and drop["source_dataset"] not in str(keep.get("source_dataset", "")):
        keep["source_dataset"] = keep.get("source_dataset", "") + "+" + drop["source_dataset"]


if __name__ == "__main__":
    main()
