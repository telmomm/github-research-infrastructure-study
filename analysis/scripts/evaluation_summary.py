#!/usr/bin/env python3
"""Tally the Phase 9 evaluation.

Inputs:
  case-study/evaluation_scores.csv
  framework/mapping/requirement_feature_matrix.csv
Outputs:
  results/framework/eval_*.csv + results/framework/evaluation_summary.md

Standard library only.
"""

import csv
import os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CS = os.path.join(ROOT, "case-study")
MATRIX = os.path.join(ROOT, "framework", "mapping", "requirement_feature_matrix.csv")
OUT = os.path.join(ROOT, "results", "framework")

DIMS = {
    "E1": "Requirement coverage", "E2": "Traceability", "E3": "Documentation",
    "E4": "Organization", "E5": "Transparency", "E6": "Usability",
}


def read(p):
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main():
    rows = read(os.path.join(CS, "evaluation_scores.csv"))
    for r in rows:
        r["score"] = float(r["score"])
        r["max"] = float(r["max"])

    per_dim = defaultdict(list)
    for r in rows:
        per_dim[r["dimension"]].append(r)

    basis_count = defaultdict(int)
    for r in rows:
        basis_count[r["basis"]] += 1

    # E1 coverage from the Phase 5 matrix
    m = read(MATRIX)
    lv = defaultdict(int)
    for r in m:
        lv[int(r["support_level"])] += 1
    n = len(m)
    supported = lv[3] + lv[2]
    fully = lv[3]

    os.makedirs(OUT, exist_ok=True)
    dim_rows = []
    for d in ["E1", "E2", "E3", "E4", "E5", "E6"]:
        rs = per_dim[d]
        mean = sum(x["score"] for x in rs) / len(rs)
        dim_rows.append([d, DIMS[d], round(mean, 2), len(rs),
                         round(100 * mean / 2, 0)])
    with open(os.path.join(OUT, "eval_by_dimension.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["dimension", "name", "mean_score_0_2", "n_subdimensions", "pct"])
        w.writerows(dim_rows)

    with open(os.path.join(OUT, "eval_subdimensions.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["dimension", "subdimension", "score", "max", "basis"])
        for r in rows:
            w.writerow([r["dimension"], r["subdimension"], r["score"], r["max"], r["basis"]])

    overall = sum(x["score"] for x in rows) / (2 * len(rows))
    observed = [x for x in rows if x["basis"] == "observed"]
    obs_mean = sum(x["score"] for x in observed) / (2 * len(observed)) if observed else 0

    md = ["# Phase 9 evaluation — summary\n",
          f"- Sub-dimensions scored: **{len(rows)}** across 6 dimensions",
          f"- Overall mean: **{overall*2:.2f} / 2**  ({overall*100:.0f}%)",
          f"- Observed-only mean: {obs_mean*2:.2f} / 2  ({obs_mean*100:.0f}%, n={len(observed)})\n",
          "## By dimension (mean of sub-scores, 0-2)\n",
          "| Dim | Name | Score | % |",
          "|---|---|---|---|"]
    for d, name, mean, _, pct in dim_rows:
        md.append(f"| {d} | {name} | {mean:.2f} | {pct:.0f}% |")
    md.append("\n## E1 requirement coverage (from Phase 5 matrix)\n")
    md.append(f"- Supported (Direct or Partial): **{supported}/{n}** ({100*supported/n:.0f}%)")
    md.append(f"- Fully supported (Direct): {fully}/{n} ({100*fully/n:.0f}%)")
    md.append(f"- Limited: {lv[1]}  ·  Not supported: {lv[0]}")
    md.append("\n## Basis of scores\n")
    for b, c in sorted(basis_count.items(), key=lambda kv: -kv[1]):
        md.append(f"- {b}: {c}")
    md.append("\n## Lowest sub-scores\n")
    for r in sorted(rows, key=lambda x: x["score"])[:5]:
        md.append(f"- {r['dimension']} {r['subdimension']}: {r['score']:.0f}/2 ({r['basis']})")
    md.append("")
    with open(os.path.join(OUT, "evaluation_summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    print("\n".join(md))


if __name__ == "__main__":
    main()
