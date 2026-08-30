#!/usr/bin/env python3
"""Consistency checks and tallies for the Phase 10 synthesis.

Input : analysis/findings.csv
Output: results/framework/synthesis_*.csv + results/framework/synthesis_summary.md

Verifies that every finding's evidence paths exist, and tallies by RQ / type /
strength. Standard library only. Exits non-zero on a missing evidence path.
"""

import csv
import os
import re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FINDINGS = os.path.join(ROOT, "analysis", "findings.csv")
OUT = os.path.join(ROOT, "results", "framework")

RQS = ["RQ1", "RQ2", "RQ3", "RQ4", "RQ5", "main"]


def read(p):
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main():
    rows = read(FINDINGS)
    os.makedirs(OUT, exist_ok=True)

    missing = []
    for r in rows:
        for ev in re.split(r";\s*", r["evidence"]):
            ev = ev.strip()
            if not ev:
                continue
            path = ev.split()[0].split("#")[0].split(" §")[0].strip()
            # allow "docs/DECISION_LOG.md D16" style — check the file part only
            path = re.sub(r"\s+D\d+$", "", path)
            if not os.path.exists(os.path.join(ROOT, path)):
                missing.append((r["finding_id"], path))

    by_rq = Counter(r["rq"] for r in rows)
    by_type = Counter(r["type"] for r in rows)
    by_strength = Counter(r["strength"] for r in rows)
    rq_type = Counter((r["rq"], r["type"]) for r in rows)

    with open(os.path.join(OUT, "synthesis_by_rq.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["rq", "results", "limitations", "implications", "total"])
        for rq in RQS:
            w.writerow([rq, rq_type[(rq, "result")], rq_type[(rq, "limitation")],
                        rq_type[(rq, "implication")], by_rq[rq]])

    with open(os.path.join(OUT, "synthesis_index.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["finding_id", "rq", "type", "strength", "statement"])
        for r in rows:
            w.writerow([r["finding_id"], r["rq"], r["type"], r["strength"], r["statement"][:120]])

    md = ["# Phase 10 synthesis — summary\n",
          f"- Findings: **{len(rows)}**  (F01–F{len(rows):02d})",
          f"- By type: " + ", ".join(f"{k} {v}" for k, v in sorted(by_type.items())),
          f"- By strength: " + ", ".join(f"{k} {v}" for k, v in sorted(by_strength.items())) + "\n",
          "## By research question\n",
          "| RQ | results | limitations | implications | total |",
          "|---|---|---|---|---|"]
    for rq in RQS:
        md.append(f"| {rq} | {rq_type[(rq,'result')]} | {rq_type[(rq,'limitation')]} | "
                  f"{rq_type[(rq,'implication')]} | {by_rq[rq]} |")
    md.append(f"\n## Evidence-path check\n- Missing paths: {missing or 'none'}")
    md.append("")
    with open(os.path.join(OUT, "synthesis_summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    print("\n".join(md))
    if missing:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
