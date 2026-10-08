#!/usr/bin/env python3
"""Systematic review, step 1: identify candidate secondary studies in the Track A corpus.

Rule (design filter, title only): the title names a secondary-study design.
Records already in the structured-review base (literature/included_studies.csv)
are flagged, not removed. Output: literature/systematic/candidates.csv
"""
import csv
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "literature", "systematic", "candidates.csv")
DESIGN = re.compile(
    r"\b(systematic (literature )?review|scoping review|literature review|narrative review|"
    r"state of the art|survey|taxonomy|bibliometric|mapping study|meta-analysis|review)\b"
)


def norm(d):
    return (d or "").lower().replace("https://doi.org/", "").strip()


def main():
    csv.field_size_limit(10**9)
    with open(os.path.join(ROOT, "data", "processed", "corpus.csv"), newline="", encoding="utf-8") as fh:
        corpus = list(csv.DictReader(fh))
    with open(os.path.join(ROOT, "literature", "included_studies.csv"), newline="", encoding="utf-8") as fh:
        base = {norm(r["doi"]): r["study_id"] for r in csv.DictReader(fh)}
    cand = [r for r in corpus if DESIGN.search(r["title"].lower())]
    cand.sort(key=lambda r: (r["publication_year"], r["title"].lower()))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["cand_id", "corpus_id", "year", "title", "source", "doi", "in_structured_base", "has_abstract", "abstract"])
        for i, r in enumerate(cand, 1):
            w.writerow([f"C{i:03d}", r["corpus_id"], r["publication_year"], r["title"], r["source"], norm(r["doi"]),
                        base.get(norm(r["doi"]), ""), "yes" if r["abstract"].strip() else "no", r["abstract"].strip()])
    print(f"corpus {len(corpus)} -> candidates {len(cand)} "
          f"({sum(1 for r in cand if norm(r['doi']) in base)} already in the structured base, "
          f"{sum(1 for r in cand if not r['abstract'].strip())} without abstract)")


if __name__ == "__main__":
    main()
