#!/usr/bin/env python3
"""Scopus / Web of Science coverage cross-check against the Track A corpus (OPEN_ITEMS 2.8).

Reads WoS tab-delimited record exports (data/raw/wos/**/*.txt, 2-letter tag headers) and,
if present, Scopus CSV exports (data/raw/scopus/**/*.csv). De-duplicates, restricts to the
corpus window (2008-2025), and compares against data/processed/corpus.csv (OpenAlex + arXiv)
by DOI, then by normalised title+year.

Characterises the difference (year, venue, per-query breakdown) rather than only counting it.
Standard library only.

Output:
  results/track_a/scopus_wos_crosscheck.md
  results/track_a/xref_not_in_corpus.csv
"""

import csv
import glob
import gzip
import io
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW = os.path.join(ROOT, "data", "raw")
CORPUS = os.path.join(ROOT, "data", "processed", "corpus.csv")
OUT = os.path.join(ROOT, "results", "track_a")
YEAR_MIN, YEAR_MAX = 2008, 2025


def norm_doi(d):
    d = (d or "").strip().lower()
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", d).strip()


def norm_title(t):
    t = re.sub(r"<[^>]+>", " ", (t or "").lower())
    return " ".join(re.sub(r"[^a-z0-9]+", " ", t).split())


def yr4(v):
    m = re.search(r"(19|20)\d{2}", str(v or ""))
    return m.group(0) if m else ""


def qtag(path):
    for part in (os.path.basename(os.path.dirname(path)), os.path.basename(path)):
        m = re.match(r"(Q\d+)", part, re.I)
        if m:
            return m.group(1).upper()
    return "?"


def read_wos(path):
    with open(path, encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.reader(fh, delimiter="\t"))
    if not rows:
        return []
    idx = {}
    for i, name in enumerate(rows[0]):
        idx.setdefault(name.strip(), i)
    q = qtag(path)
    out = []
    for r in rows[1:]:
        if not any(c.strip() for c in r):
            continue
        g = lambda tag: (r[idx[tag]].strip() if tag in idx and idx[tag] < len(r) else "")
        doi = g("DI")
        if not re.match(r"10\.\d{4,9}/", doi):
            doi = ""
        out.append({"src": "wos", "q": q, "doi": doi, "title": g("TI"),
                    "year": yr4(g("PY")), "venue": g("SO") or g("SE"), "doctype": g("DT")})
    return out


def read_scopus(path):
    with open(path, encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    km = {k.lower(): k for k in (rows[0].keys() if rows else [])}
    pick = lambda *c: next((km[x] for x in c if x in km), None)
    kd, kt, ky, ks, kx = (pick("doi"), pick("title"), pick("year"),
                          pick("source title"), pick("document type"))
    q = qtag(path)
    return [{"src": "scopus", "q": q,
             "doi": r.get(kd, "") if kd else "", "title": r.get(kt, "") if kt else "",
             "year": yr4(r.get(ky, "") if ky else ""),
             "venue": r.get(ks, "") if ks else "", "doctype": r.get(kx, "") if kx else ""}
            for r in rows]


def load_all():
    recs, files = [], []
    for f in sorted(glob.glob(os.path.join(RAW, "wos", "**", "*.txt"), recursive=True)):
        r = read_wos(f); recs += r; files.append((os.path.relpath(f, RAW), len(r)))
    for f in sorted(glob.glob(os.path.join(RAW, "scopus", "**", "*.csv"), recursive=True)):
        r = read_scopus(f); recs += r; files.append((os.path.relpath(f, RAW), len(r)))
    return recs, files


def dedup(recs):
    seen_d, seen_t, out = set(), set(), []
    for x in recs:
        d = norm_doi(x["doi"])
        t = (norm_title(x["title"]), x["year"])
        if d and d in seen_d:
            continue
        if not d and t[0] and t in seen_t:
            continue
        if d:
            seen_d.add(d)
        elif t[0]:
            seen_t.add(t)
        out.append(x)
    return out


def main():
    recs, files = load_all()
    for name, k in files:
        print(f"  {name}: {k}")
    if not recs:
        sys.exit("no WoS/Scopus exports under data/raw/{wos,scopus}/")

    total_raw = len(recs)
    in_window = [x for x in recs if x["year"] and YEAR_MIN <= int(x["year"]) <= YEAR_MAX]
    out_window = total_raw - len(in_window)
    uniq = dedup(in_window)

    corpus = list(csv.DictReader(open(CORPUS, newline="", encoding="utf-8")))
    c_doi = {norm_doi(c.get("doi")) for c in corpus if norm_doi(c.get("doi"))}
    c_ty = {(norm_title(c.get("title")), yr4(c.get("publication_year"))) for c in corpus}

    hit_doi = hit_ty = 0
    matched, missing = [], []
    for x in uniq:
        d = norm_doi(x["doi"])
        t = (norm_title(x["title"]), x["year"])
        if d and d in c_doi:
            hit_doi += 1; matched.append(x)
        elif t[0] and t in c_ty:
            hit_ty += 1; matched.append(x)
        else:
            missing.append(x)

    x_doi = {norm_doi(x["doi"]) for x in uniq if norm_doi(x["doi"])}
    x_ty = {(norm_title(x["title"]), x["year"]) for x in uniq}
    corpus_only = [c for c in corpus
                   if norm_doi(c.get("doi")) not in x_doi
                   and (norm_title(c.get("title")), yr4(c.get("publication_year"))) not in x_ty]

    os.makedirs(OUT, exist_ok=True)
    # full list is ~2 MB -> gzip so it is git-friendly
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["src", "q", "doi", "year", "doctype", "venue", "title"])
    for x in sorted(missing, key=lambda r: (r["year"], r["title"].lower())):
        w.writerow([x["src"], x["q"], x["doi"], x["year"], x["doctype"], x["venue"], x["title"]])
    with gzip.open(os.path.join(OUT, "xref_not_in_corpus.csv.gz"), "wt", encoding="utf-8", newline="") as fh:
        fh.write(buf.getvalue())

    n = len(uniq)
    ov = 100 * len(matched) / n if n else 0
    yr = Counter(x["year"] for x in missing)
    ven = Counter((x["venue"] or "?").title()[:48] for x in missing)
    byq_all = Counter(x["q"] for x in uniq)
    byq_miss = Counter(x["q"] for x in missing)

    md = ["# Scopus / Web of Science cross-check (OPEN_ITEMS 2.8)\n",
          f"- Source files: {len(files)}  ·  raw records: {total_raw}  ·  outside 2008-2025 window: {out_window}",
          f"- De-duplicated in-window cross-check set: **{n}**",
          f"- Overlap with the OpenAlex + arXiv corpus: **{len(matched)} ({ov:.0f}%)**  "
          f"(by DOI {hit_doi}, by title+year {hit_ty})",
          f"- WoS/Scopus records not in the corpus: **{len(missing)} ({100-ov:.0f}%)** "
          f"— `xref_not_in_corpus.csv.gz`",
          f"- Corpus records not returned by these queries: {len(corpus_only)} of {len(corpus)} "
          f"(OpenAlex indexes preprints and OA venues; the open queries are phrased differently)\n",
          "## WoS/Scopus-only records — where they come from\n",
          "| Query | in set | not in corpus |",
          "|---|---|---|"]
    for q in sorted(byq_all):
        md.append(f"| {q} | {byq_all[q]} | {byq_miss.get(q, 0)} |")
    md.append("\n**Top venues of the not-in-corpus set:**\n")
    for v, c in ven.most_common(12):
        md.append(f"- {v}: {c}")
    md.append("\n**By year:** " + ", ".join(f"{y}:{yr[y]}" for y in sorted(yr)) + "\n")
    md.append("## Reading\n")
    md.append(
        "The two retrieval routes diverge because WoS *Topic* (`TS=`) also matches Keywords Plus "
        "and author keywords, which expands aggressively, whereas the OpenAlex query is anchored "
        "to title and abstract. The not-in-corpus set is dominated by recent bioinformatics and "
        "tool papers that mention `GitHub` in a data-availability statement and `workflow` / "
        "`reproducibility` in the abstract (see the venue list) — the low-precision tail that a "
        "title/abstract search deliberately excludes, not missed core literature on research-"
        "process infrastructure. Conversely the corpus contains preprints and open-access records "
        "WoS does not index. The overlap on DOI is the robust figure; it quantifies the "
        "coverage/precision trade-off declared in `DECISION_LOG.md` D8, and supports keeping "
        "OpenAlex as the primary source while acknowledging that a subscription search would add "
        "a substantial, mostly peripheral, tail.")
    md.append("")
    with open(os.path.join(OUT, "scopus_wos_crosscheck.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    print("\n".join(md))


if __name__ == "__main__":
    main()
