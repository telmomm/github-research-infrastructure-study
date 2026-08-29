#!/usr/bin/env python3
"""Coverage indicators for the requirement-feature mapping (Phase 5).

Inputs:
  framework/mapping/requirement_feature_matrix.csv
  framework/requirements/requirements_framework.csv
  framework/requirements/lifecycle_requirements_matrix.csv
Outputs:
  results/framework/coverage_*.csv
  results/framework/coverage_summary.md

Standard library only.
"""

import csv
import os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MAP = os.path.join(ROOT, "framework", "mapping")
REQ = os.path.join(ROOT, "framework", "requirements")
OUT = os.path.join(ROOT, "results", "framework")

LABELS = {0: "Not supported", 1: "Limited", 2: "Partial", 3: "Direct"}
GROUP_NAMES = {
    "GF1": "Repository & Git", "GF2": "Markdown & documentation", "GF3": "Issues",
    "GF4": "Projects", "GF5": "Milestones", "GF6": "Labels", "GF7": "Discussions",
    "GF8": "Branches", "GF9": "Pull Requests", "GF10": "Actions",
    "GF11": "Releases & tags", "GF12": "Access, identity & meta",
}


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
    m = read(os.path.join(MAP, "requirement_feature_matrix.csv"))
    reqs = {r["rm_id"]: r for r in read(os.path.join(REQ, "requirements_framework.csv"))}
    life = {r["rm_id"]: r for r in read(os.path.join(REQ, "lifecycle_requirements_matrix.csv"))}
    stages = [k for k in next(iter(life.values())).keys() if k != "rm_id"]

    for r in m:
        r["support_level"] = int(r["support_level"])
        r["differentiator"] = reqs[r["rm_id"]]["differentiator"].strip().lower() == "yes"

    n = len(m)
    total = sum(r["support_level"] for r in m)
    mean = total / n

    # distribution
    dist = defaultdict(int)
    for r in m:
        dist[r["support_level"]] += 1
    dump("coverage_distribution.csv", ["support_level", "label", "n", "pct"],
         [[k, LABELS[k], dist[k], round(100 * dist[k] / n, 1)] for k in (3, 2, 1, 0)])

    # per category
    cat = defaultdict(list)
    for r in m:
        cat[r["category"]].append(r["support_level"])
    dump("coverage_by_category.csv", ["category", "n", "mean_support"],
         [[c, len(v), round(sum(v) / len(v), 2)] for c, v in sorted(cat.items(), key=lambda kv: -sum(kv[1]) / len(kv[1]))])

    # differentiators vs rest
    diff = [r["support_level"] for r in m if r["differentiator"]]
    rest = [r["support_level"] for r in m if not r["differentiator"]]
    dump("coverage_differentiators.csv", ["group", "n", "mean_support", "rm_ids"],
         [["differentiators", len(diff), round(sum(diff) / len(diff), 2),
           " ".join(r["rm_id"] for r in m if r["differentiator"])],
          ["all others", len(rest), round(sum(rest) / len(rest), 2), ""]])

    # per requirement
    dump("coverage_by_requirement.csv",
         ["rm_id", "name", "category", "support_level", "support_label", "external_tools_needed"],
         [[r["rm_id"], r["name"], r["category"], r["support_level"], r["support_label"],
           r["external_tools_needed"]] for r in m])

    # external tools
    ext = [r for r in m if r["external_tools_needed"].strip().lower() not in ("", "none")]
    dump("coverage_external_tools.csv", ["rm_id", "name", "external_tools_needed"],
         [[r["rm_id"], r["name"], r["external_tools_needed"]] for r in ext])

    # lifecycle-coverage profile: weighted mean support per stage
    sup = {r["rm_id"]: r["support_level"] for r in m}
    stage_rows = []
    for s in stages:
        num = den = 0.0
        for rm, lr in life.items():
            w = int(lr[s] or 0)
            if w > 0 and rm in sup:
                num += w * sup[rm]
                den += w
        stage_rows.append([s, round(num / den, 2) if den else 0.0, int(den)])
    dump("coverage_lifecycle_profile.csv", ["lifecycle_stage", "weighted_mean_support", "applicability_weight"], stage_rows)

    # RM x feature-group contribution matrix (from contributing_groups)
    gids = list(GROUP_NAMES)
    grid = []
    for r in m:
        cells = {g: 0 for g in gids}
        for tok in r["contributing_groups"].split(";"):
            tok = tok.strip()
            if ":" in tok:
                g, v = tok.split(":")
                if g in cells:
                    cells[g] = int(v)
        grid.append([r["rm_id"]] + [cells[g] for g in gids])
    dump("coverage_group_matrix.csv", ["rm_id"] + gids, grid)
    group_tot = {g: sum(row[i + 1] for row in grid) for i, g in enumerate(gids)}

    md = ["# Requirement-feature coverage — indicators\n",
          f"- Requirements assessed: **{n}**",
          f"- Overall mean support (0-3): **{mean:.2f}**",
          f"- Requirements needing a complementary external tool: **{len(ext)}** ({', '.join(r['rm_id'] for r in ext)})\n",
          "## Support distribution\n"]
    for k in (3, 2, 1, 0):
        md.append(f"- {LABELS[k]} ({k}): {dist[k]}  ({round(100 * dist[k] / n, 1)}%)  "
                  + " ".join(r["rm_id"] for r in m if r["support_level"] == k))
    md.append("\n## Mean support by category\n")
    for c, v in sorted(cat.items(), key=lambda kv: -sum(kv[1]) / len(kv[1])):
        md.append(f"- {c}: {sum(v)/len(v):.2f}  (n={len(v)})")
    md.append(f"\n## Differentiators vs rest\n- differentiators (RM1, RM2, RM5): "
              f"{sum(diff)/len(diff):.2f}\n- all others: {sum(rest)/len(rest):.2f}")
    md.append("\n## Lifecycle-coverage profile (weighted mean support per stage)\n")
    for s, val, w in stage_rows:
        bar = "#" * int(round(val * 6))
        md.append(f"- {s:<12} {val:>4}  {bar}")
    md.append("\n## Feature-group contribution (sum of RM contribution weights)\n")
    for g in sorted(gids, key=lambda x: -group_tot[x]):
        md.append(f"- {g} {GROUP_NAMES[g]}: {group_tot[g]}")
    md.append("")
    with open(os.path.join(OUT, "coverage_summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    print("\n".join(md))


if __name__ == "__main__":
    main()
