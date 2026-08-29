#!/usr/bin/env python3
"""Consistency checks and cross-tabs for the reference architecture (Phase 6).

Inputs:
  framework/architecture/architecture_components.csv
  framework/architecture/workflows.csv
  framework/architecture/lifecycle_model.csv
  framework/mapping/requirement_feature_matrix.csv
  framework/requirements/requirements_framework.csv
Outputs:
  results/framework/arch_*.csv
  results/framework/architecture_summary.md

Standard library only.
"""

import csv
import os
import re
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARCH = os.path.join(ROOT, "framework", "architecture")
MAP = os.path.join(ROOT, "framework", "mapping")
REQ = os.path.join(ROOT, "framework", "requirements")
OUT = os.path.join(ROOT, "results", "framework")


def read(p):
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def toks(s):
    return [t.strip() for t in re.split(r"[;|]", s or "") if t.strip()]


def dump(name, header, rows):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)


def main():
    comps = read(os.path.join(ARCH, "architecture_components.csv"))
    wfs = read(os.path.join(ARCH, "workflows.csv"))
    life = read(os.path.join(ARCH, "lifecycle_model.csv"))
    matrix = {r["rm_id"]: r for r in read(os.path.join(MAP, "requirement_feature_matrix.csv"))}
    reqs = read(os.path.join(REQ, "requirements_framework.csv"))
    rm_ids = [r["rm_id"] for r in reqs]
    rm_name = {r["rm_id"]: r["name"] for r in reqs}

    by_layer = Counter(c["layer"] for c in comps)

    # RM -> serving components
    served = defaultdict(list)
    for c in comps:
        for rm in toks(c["requirements_served"]):
            served[rm].append(c["comp_id"])
    # RM -> workflows
    wf_by_rm = defaultdict(list)
    for w in wfs:
        for rm in toks(w["requirements"]):
            wf_by_rm[rm].append(w["wf_id"])

    dump("arch_components_by_layer.csv", ["layer", "n"], sorted(by_layer.items()))
    dump("arch_rm_coverage.csv",
         ["rm_id", "name", "support_label", "components", "workflows", "n_components"],
         [[rm, rm_name[rm], matrix.get(rm, {}).get("support_label", ""),
           " ".join(served.get(rm, [])), " ".join(sorted(set(wf_by_rm.get(rm, [])))),
           len(served.get(rm, []))] for rm in rm_ids])

    # component -> RM check (every component serves >=1 RM)
    comp_no_rm = [c["comp_id"] for c in comps if not toks(c["requirements_served"])]
    rm_no_comp = [rm for rm in rm_ids if not served.get(rm)]

    # workflow step / component references resolve
    comp_ids = {c["comp_id"] for c in comps}
    bad_wf_comp = []
    for w in wfs:
        for cid in toks(w["components"]):
            if cid not in comp_ids:
                bad_wf_comp.append((w["wf_id"], cid))

    # lifecycle stages: components active per stage
    stage_rows = []
    for s in life:
        active = toks(s["active_components"])
        bad = [c for c in active if c not in comp_ids]
        stage_rows.append([s["stage"], len(active), " ".join(active), " ".join(bad)])
    dump("arch_lifecycle_components.csv",
         ["stage", "n_active_components", "active_components", "unresolved"], stage_rows)

    # differentiator requirements and how the architecture lifts them
    diff = [r for r in reqs if r["differentiator"].strip().lower() == "yes"]
    lift_rows = []
    for r in diff:
        rm = r["rm_id"]
        conv = [c["comp_id"] + ": " + c["convention"].split(":")[0]
                for c in comps if rm in toks(c["requirements_served"]) and c["convention"].strip()]
        lift_rows.append([rm, rm_name[rm], matrix[rm]["support_label"], " | ".join(conv)])
    dump("arch_differentiator_lift.csv",
         ["rm_id", "name", "phase5_support", "lifting_conventions"], lift_rows)

    md = ["# Reference architecture — summary\n",
          f"- Components: **{len(comps)}** across {len(by_layer)} layers "
          f"({', '.join(f'{k} {v}' for k, v in sorted(by_layer.items()))})",
          f"- Workflows defined: **{len(wfs)}**",
          f"- Lifecycle stages modelled: **{len(life)}**\n",
          "## Consistency checks\n",
          f"- Components with no requirement served: {comp_no_rm or 'none'}",
          f"- Requirements with no serving component: {rm_no_comp or 'none'}",
          f"- Workflow component references unresolved: {bad_wf_comp or 'none'}",
          f"- Lifecycle component references unresolved: "
          f"{[r[0] for r in stage_rows if r[3]] or 'none'}\n",
          "## Requirement -> component coverage\n"]
    for rm in rm_ids:
        md.append(f"- {rm} {rm_name[rm]} [{matrix.get(rm, {}).get('support_label','')}]: "
                  f"{' '.join(served.get(rm, [])) or 'NONE'}")
    md.append("\n## Differentiators — lifting conventions\n")
    for rm, name, sup, conv in lift_rows:
        md.append(f"- {rm} {name} [{sup}]: {conv}")
    md.append("")
    with open(os.path.join(OUT, "architecture_summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    print("\n".join(md))


if __name__ == "__main__":
    main()
