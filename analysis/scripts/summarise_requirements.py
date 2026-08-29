#!/usr/bin/env python3
"""Cross-tabs of the Research Management Requirements Framework (Phase 3).

Input : framework/requirements/requirements_framework.csv
        framework/requirements/lifecycle_requirements_matrix.csv
Output: results/framework/*.csv + results/framework/requirements_summary.md

Standard library only.
"""

import csv
import os
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REQ = os.path.join(ROOT, "framework", "requirements")
OUT = os.path.join(ROOT, "results", "framework")


def read(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main():
    os.makedirs(OUT, exist_ok=True)
    rows = read(os.path.join(REQ, "requirements_framework.csv"))
    mat = read(os.path.join(REQ, "lifecycle_requirements_matrix.csv"))
    stages = [k for k in mat[0].keys() if k != "rm_id"]

    by_cat = Counter(r["category"] for r in rows)
    by_imp = Counter(r["importance"] for r in rows)
    by_att = Counter(r["literature_attention"] for r in rows)
    diff = [r["rm_id"] for r in rows if r["differentiator"].strip().lower() == "yes"]

    ev_studies = Counter()
    for r in rows:
        for s in r["evidence_studies"].split(";"):
            if s.strip():
                ev_studies[s.strip()] += 1
    ev_re = Counter()
    for r in rows:
        for e in r["evidence_re"].split(";"):
            if e.strip():
                ev_re[e.strip()] += 1

    # lifecycle load: sum of applicability weights per stage, and per requirement
    stage_load = {s: 0 for s in stages}
    rm_span = {}
    for m in mat:
        span = 0
        for s in stages:
            v = int(m[s] or 0)
            stage_load[s] += v
            if v >= 2:
                span += 1
        rm_span[m["rm_id"]] = span

    def dump(name, header, items):
        with open(os.path.join(OUT, name), "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(header)
            w.writerows(items)

    dump("rm_by_category.csv", ["category", "count"], sorted(by_cat.items()))
    dump("rm_by_importance.csv", ["importance", "count"], sorted(by_imp.items()))
    dump("rm_by_literature_attention.csv", ["literature_attention", "count"], sorted(by_att.items()))
    dump("rm_evidence_studies.csv", ["study_id", "n_requirements"], ev_studies.most_common())
    dump("rm_evidence_re.csv", ["re_id", "n_requirements"], sorted(ev_re.items()))
    dump("lifecycle_stage_load.csv", ["stage", "sum_applicability"],
         [(s, stage_load[s]) for s in stages])
    dump("rm_lifecycle_span.csv", ["rm_id", "stages_applicable_ge2"],
         sorted(rm_span.items()))

    md = ["# Research Management Requirements Framework — summary\n",
          f"- Requirements: **{len(rows)}** (RM1-RM15)",
          f"- Differentiators (High importance despite weak literature attention): {', '.join(diff)}\n",
          "## By category\n"]
    for k, v in sorted(by_cat.items(), key=lambda kv: -kv[1]):
        md.append(f"- {k}: {v}")
    md.append("\n## By importance\n")
    for k in ["High", "Medium-High", "Medium", "Low-Medium"]:
        if k in by_imp:
            md.append(f"- {k}: {by_imp[k]}")
    md.append("\n## By literature attention\n")
    for k, v in sorted(by_att.items(), key=lambda kv: -kv[1]):
        md.append(f"- {k}: {v}")
    md.append("\n## Lifecycle-stage load (sum of applicability weights, 0-3 per requirement)\n")
    for s in stages:
        bar = "#" * round(stage_load[s] / 2)
        md.append(f"- {s:<12} {stage_load[s]:>3}  {bar}")
    md.append("\n## Most-cited evidence studies\n")
    for s, c in ev_studies.most_common(8):
        md.append(f"- {s}: {c} requirements")
    md.append("")
    with open(os.path.join(OUT, "requirements_summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    print("\n".join(md))


if __name__ == "__main__":
    main()
