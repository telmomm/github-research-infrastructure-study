#!/usr/bin/env python3
"""Consistency checks and tallies for the self-referential case study (Phase 8).

Inputs:
  case-study/implementation_record.csv
  case-study/activity_register.csv
  framework/architecture/architecture_components.csv
  framework/mapping/requirement_feature_matrix.csv
Outputs:
  results/framework/cs_*.csv + results/framework/case_study_summary.md

Standard library only. Exits non-zero on a broken internal reference.
"""

import csv
import os
import re
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CS = os.path.join(ROOT, "case-study")
ARCH = os.path.join(ROOT, "framework", "architecture", "architecture_components.csv")
MATRIX = os.path.join(ROOT, "framework", "mapping", "requirement_feature_matrix.csv")
OUT = os.path.join(ROOT, "results", "framework")

# implementation statuses that count as "the component is actually working here"
EXERCISED = {"native", "partial"}


def read(p):
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def toks(s):
    return [t.strip() for t in re.split(r"[;|]", s or "") if t.strip()]


def main():
    impl = read(os.path.join(CS, "implementation_record.csv"))
    reg = read(os.path.join(CS, "activity_register.csv"))
    comps = {c["comp_id"] for c in read(ARCH)}
    matrix = {r["rm_id"]: r for r in read(MATRIX)}

    # --- implementation record checks
    impl_ids = {r["comp_id"] for r in impl}
    missing_comps = sorted(comps - impl_ids)
    unknown_comps = sorted(impl_ids - comps)
    by_status = Counter(r["status"] for r in impl)
    exercised = [r["comp_id"] for r in impl if r["status"] in EXERCISED]

    # RMs served by an exercised component
    rm_served = set()
    for c in read(ARCH):
        if c["comp_id"] in exercised:
            rm_served.update(toks(c["requirements_served"]))
    rm_all = [f"RM{i}" for i in range(1, 16)]
    rm_not_exercised = [rm for rm in rm_all if rm not in rm_served]

    # --- activity register checks
    ids = {r["item_id"] for r in reg}
    by_type = Counter(r["type"] for r in reg)
    by_status_reg = Counter(r["status"] for r in reg)
    bad_links = []
    for r in reg:
        for l in toks(r["linked_to"]):
            if l not in ids:
                bad_links.append((r["item_id"], l))
    rqs = {r["item_id"] for r in reg if r["type"] == "RQ"}
    bad_rq = []
    for r in reg:
        for q in toks(r["serves_rq"]):
            if q and q not in rqs:
                bad_rq.append((r["item_id"], q))
    # every RQ answered or in-progress, every milestone linked to >=1 task
    tasks_by_ms = defaultdict(list)
    for r in reg:
        if r["type"] == "task":
            for l in toks(r["linked_to"]):
                if l.startswith("M"):
                    tasks_by_ms[l].append(r["item_id"])
    ms_no_task = [r["item_id"] for r in reg if r["type"] == "milestone" and not tasks_by_ms.get(r["item_id"])]

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "cs_implementation_status.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["comp_id", "name", "layer", "status"])
        for r in impl:
            w.writerow([r["comp_id"], r["name"], r["layer"], r["status"]])
    with open(os.path.join(OUT, "cs_register_by_type.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["type", "n"])
        w.writerows(sorted(by_type.items()))

    problems = bool(missing_comps or unknown_comps or bad_links or bad_rq or ms_no_task)

    md = ["# Case study — self-referential implementation summary\n",
          f"- Architecture components recorded: {len(impl)} / {len(comps)}",
          f"- Register items: {len(reg)}  ({', '.join(f'{k} {v}' for k, v in sorted(by_type.items()))})\n",
          "## Implementation status\n"]
    for k in ("native", "partial", "config", "retrospective", "planned"):
        if k in by_status:
            ids_k = " ".join(r["comp_id"] for r in impl if r["status"] == k)
            md.append(f"- {k}: {by_status[k]}  ({ids_k})")
    md.append(f"\n- Components exercised (native/partial): {len(exercised)} / {len(impl)} "
              f"— {' '.join(exercised)}")
    md.append(f"- Requirements with **no** exercised component: "
              f"{', '.join(rm_not_exercised) if rm_not_exercised else 'none'}")
    md.append("\n## Register status\n")
    for k, v in sorted(by_status_reg.items()):
        md.append(f"- {k}: {v}")
    md.append("\n## Consistency checks\n")
    md.append(f"- Components missing from implementation_record: {missing_comps or 'none'}")
    md.append(f"- Unknown component ids: {unknown_comps or 'none'}")
    md.append(f"- Register links unresolved: {bad_links or 'none'}")
    md.append(f"- Register serves_rq unresolved: {bad_rq or 'none'}")
    md.append(f"- Milestones with no task: {ms_no_task or 'none'}")
    md.append("")
    with open(os.path.join(OUT, "case_study_summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    print("\n".join(md))
    if problems:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
