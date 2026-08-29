#!/usr/bin/env python3
"""Cross-tabs of the GitHub capability catalogue (Phase 4).

Input : framework/mapping/github_capability_catalogue.csv
        framework/requirements/requirements_framework.csv
Output: results/framework/gc_*.csv + results/framework/capability_summary.md

`candidate_requirements` in the catalogue is a Phase-4 hint, not the Phase-5
scored mapping. This script only tallies coverage so gaps are visible early.
Standard library only.
"""

import csv
import os
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MAP = os.path.join(ROOT, "framework", "mapping")
REQ = os.path.join(ROOT, "framework", "requirements")
OUT = os.path.join(ROOT, "results", "framework")


def read(p):
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def dump(name, header, rows):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)


def main():
    caps = read(os.path.join(MAP, "github_capability_catalogue.csv"))
    reqs = read(os.path.join(REQ, "requirements_framework.csv"))
    rm_ids = [r["rm_id"] for r in reqs]
    rm_name = {r["rm_id"]: r["name"] for r in reqs}

    by_group = Counter(c["feature_group"] for c in caps)
    by_plan = Counter(c["plan_availability"] for c in caps)
    by_cx = Counter(c["practical_complexity"] for c in caps)

    cand_by_rm = defaultdict(list)
    caps_no_rm = []
    for c in caps:
        tokens = [t.strip() for t in c["candidate_requirements"].split(";") if t.strip()]
        if not tokens:
            caps_no_rm.append(c["cap_id"])
        for t in tokens:
            cand_by_rm[t].append(c["cap_id"])

    dump("gc_by_feature_group.csv", ["feature_group", "n_capabilities"],
         sorted(by_group.items(), key=lambda kv: -kv[1]))
    dump("gc_by_plan_availability.csv", ["plan_availability", "n"], sorted(by_plan.items()))
    dump("gc_by_complexity.csv", ["practical_complexity", "n"], sorted(by_cx.items()))
    dump("gc_candidate_coverage.csv", ["rm_id", "name", "n_candidate_capabilities", "capabilities"],
         [[rm, rm_name[rm], len(cand_by_rm.get(rm, [])), " ".join(cand_by_rm.get(rm, []))] for rm in rm_ids])

    gaps = [rm for rm in rm_ids if len(cand_by_rm.get(rm, [])) == 0]
    thin = [rm for rm in rm_ids if 0 < len(cand_by_rm.get(rm, [])) <= 2]

    md = ["# GitHub capability catalogue — summary\n",
          f"- Capabilities catalogued: **{len(caps)}** across {len(by_group)} feature groups",
          f"- Requirements with no candidate capability: {', '.join(gaps) if gaps else 'none'}",
          f"- Requirements with only 1-2 candidate capabilities (watch in Phase 5): {', '.join(thin) if thin else 'none'}\n",
          "## Capabilities per feature group\n"]
    for g, n in by_group.most_common():
        md.append(f"- {g}: {n}")
    md.append("\n## Plan availability\n")
    for k, v in sorted(by_plan.items()):
        md.append(f"- {k}: {v}")
    md.append("\n## Practical complexity\n")
    for k in ["low", "medium", "medium-high", "high"]:
        if k in by_cx:
            md.append(f"- {k}: {by_cx[k]}")
    md.append("\n## Candidate capability count per requirement (Phase-4 hint)\n")
    for rm in rm_ids:
        n = len(cand_by_rm.get(rm, []))
        md.append(f"- {rm} {rm_name[rm]}: {n}")
    md.append("")
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "capability_summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    print("\n".join(md))
    if caps_no_rm:
        print("\nCapabilities with no candidate requirement:", ", ".join(caps_no_rm))


if __name__ == "__main__":
    main()
