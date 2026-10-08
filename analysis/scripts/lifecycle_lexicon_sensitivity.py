#!/usr/bin/env python3
"""Sensitivity of the Track A lifecycle stage-hit profile to the matching rule.

The primary profile (bibliometrics_track_a.py -> lifecycle_stage_hits.csv) uses
plain lowercase substring matching, which over-counts short terms ("doi" in
"doing", "cris" in "crisis", "grant" in "granted"). This script re-scores the
same lexicon with a word-anchored rule and writes both side by side, so the
manuscript can report whether the stage ranking depends on the rule.

Word-anchored rule: every term must start at a word boundary; the short
acronym-like terms must also end at one ("grant" may take a plural "s").

Output: results/track_a/lifecycle_stage_hits_sensitivity.csv
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CORPUS = os.path.join(ROOT, "data", "processed", "corpus.csv")
OUT = os.path.join(ROOT, "results", "track_a", "lifecycle_stage_hits_sensitivity.csv")

sys.path.insert(0, HERE)
from bibliometrics_track_a import STAGE_LEX  # noqa: E402

CLOSED = {"doi", "cris", "orcid"}


def anchored(term):
    if term in CLOSED:
        return re.compile(r"\b" + re.escape(term) + r"\b")
    if term == "grant":
        return re.compile(r"\bgrants?\b")
    return re.compile(r"\b" + re.escape(term))


def main():
    csv.field_size_limit(10**9)
    with open(CORPUS, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    n = len(rows)
    hay = [
        (r.get("concepts", "") + " " + r.get("abstract", "") + " " + r.get("topics", "")).lower()
        for r in rows
    ]
    out = []
    for stage, lex in STAGE_LEX.items():
        sub = sum(any(t in h for t in lex) for h in hay)
        pats = [anchored(t) for t in lex]
        anc = sum(any(p.search(h) for p in pats) for h in hay)
        out.append((stage, sub, round(100 * sub / n, 1), anc, round(100 * anc / n, 1)))
    out.sort(key=lambda r: -r[1])
    unmatched = sum(not any(any(t in h for t in lex) for lex in STAGE_LEX.values()) for h in hay)

    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["stage", "n_substring", "pct_substring", "n_anchored", "pct_anchored"])
        w.writerows(out)
        w.writerow(["(no theme matched)", unmatched, round(100 * unmatched / n, 1), "", ""])
    for r in out:
        print(f"{r[0]:24s} substring {r[2]:5.1f}%   anchored {r[4]:5.1f}%")
    print(f"no theme matched: {unmatched} ({100 * unmatched / n:.1f}%)  n={n}")


if __name__ == "__main__":
    main()
