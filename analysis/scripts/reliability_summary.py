#!/usr/bin/env python3
"""Inter-coder agreement for the second-coding pass (OPEN_ITEMS 2.7/3.1/5.2/9.1, issue #10).

Input : case-study/reliability_check.csv
Output: results/framework/reliability_summary.md

Reports, per coding unit and pooled:
  - percent exact agreement
  - Cohen's kappa  (nominal for the RE->RM unit)
  - linearly-weighted Cohen's kappa (for the ordinal support-level and
    evaluation-score units)
and a sensitivity note for the single evaluation-score disagreement.

Standard library only.
"""

import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "case-study", "reliability_check.csv")
OUT = os.path.join(ROOT, "results", "framework")

UNIT_NAMES = {
    "A_re_rm": "RE->RM assignment (literature/requirements_extraction.csv)",
    "B_support": "Requirement support level (framework/mapping/requirement_feature_matrix.csv)",
    "C_eval": "Evaluation sub-score (case-study/evaluation_scores.csv)",
}


def cohen_kappa(pairs, weighted=False, max_dist=1):
    """pairs: list of (a, b). weighted=True -> linear weights on |a-b|."""
    cats = sorted({c for p in pairs for c in p})
    idx = {c: i for i, c in enumerate(cats)}
    n = len(pairs)
    if n == 0:
        return None
    row = [0.0] * len(cats)
    col = [0.0] * len(cats)
    obs = 0.0
    for a, b in pairs:
        row[idx[a]] += 1
        col[idx[b]] += 1
        if weighted:
            obs += 1 - abs(_num(a) - _num(b)) / max_dist
        else:
            obs += 1 if a == b else 0
    p_o = obs / n
    row = [x / n for x in row]
    col = [x / n for x in col]
    p_e = 0.0
    for i, ci in enumerate(cats):
        for j, cj in enumerate(cats):
            w = 1 - abs(_num(ci) - _num(cj)) / max_dist if weighted else (1 if i == j else 0)
            p_e += w * row[i] * col[j]
    if p_e >= 1.0:
        return 1.0
    return (p_o - p_e) / (1 - p_e)


def _num(v):
    return float(str(v).replace("RM", ""))


def main():
    with open(SRC, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    units = {}
    for r in rows:
        units.setdefault(r["unit"], []).append(r)

    md = ["# Inter-coder agreement — second-coding pass\n",
          "Independent re-code of every coded decision in the framework "
          "(RE->RM assignment, requirement support levels, evaluation sub-scores) "
          "against the author's codes. Method and caveats: "
          "`case-study/reliability_check.md`. Issue #10; `DECISION_LOG.md` D26.\n",
          "| Unit | n | Exact agree | % agree | Cohen's kappa | Weighted kappa |",
          "|---|---|---|---|---|---|"]

    pooled = []
    for key in ("A_re_rm", "B_support", "C_eval"):
        rs = units[key]
        pairs = [(r["author_code"], r["second_code"]) for r in rs]
        n = len(pairs)
        exact = sum(1 for a, b in pairs if a == b)
        k = cohen_kappa(pairs, weighted=False)
        if key == "A_re_rm":
            kw = "-"
        else:
            md_ = 2 if key == "C_eval" else 3
            kw = f"{cohen_kappa(pairs, weighted=True, max_dist=md_):.3f}"
        md.append(f"| {UNIT_NAMES[key]} | {n} | {exact} | {100*exact/n:.1f}% "
                  f"| {k:.3f} | {kw} |")
        pooled.append((exact, n))

    pe = sum(e for e, _ in pooled)
    pn = sum(n for _, n in pooled)
    md.append(f"| **pooled** | {pn} | {pe} | {100*pe/pn:.1f}% | - | - |\n")

    dis = [r for r in rows if r["agree"] == "0"]
    md.append("## Disagreements\n")
    for r in dis:
        md.append(f"- **{r['item_id']}** ({UNIT_NAMES[r['unit']].split(' (')[0]}): "
                  f"author `{r['author_code']}` vs second `{r['second_code']}`. {r['note']}")
    soft = [r for r in rows if r["boundary"] == "1" and r["agree"] == "1"]
    md.append(f"\n{len(soft)} further codes agreed but were flagged as boundary calls "
              "(recorded in `reliability_check.csv`, column `boundary`).\n")

    md.append("## Sensitivity of the headline evaluation score\n")
    md.append("The one evaluation-score disagreement is **E6 workflow overhead** "
              "(author 2, second coder 1, adjacent). Adopting the stricter code:\n")
    md.append("- E6 (Usability) dimension mean 1.50 -> 1.25")
    md.append("- Overall (mean of 21 sub-scores) 1.86 -> 1.81; "
              "dimension-mean overall 1.86 -> 1.83")
    md.append("- Ranking unchanged: strongest E3/E4/E5, weakest E6; overall still 'high'.\n")

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "reliability_summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    print("\n".join(md))


if __name__ == "__main__":
    main()
