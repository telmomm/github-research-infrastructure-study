#!/usr/bin/env python3
"""Tally the template external-validity mapping (OPEN_ITEMS 8.2 / issue #12).

Input : case-study/external_validity_mapping.csv
Output: results/framework/external_validity_summary.md

Standard library only. Exits non-zero if any RM1-RM15 row is missing.
"""

import csv
import os
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "case-study", "external_validity_mapping.csv")
OUT = os.path.join(ROOT, "results", "framework")


def main():
    with open(SRC, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    ids = {r["rm_id"] for r in rows}
    missing = [f"RM{i}" for i in range(1, 16) if f"RM{i}" not in ids]

    by_status = Counter(r["status"].strip() for r in rows)
    status_rms = defaultdict(list)
    for r in rows:
        status_rms[r["status"].strip()].append(r["rm_id"])

    os.makedirs(OUT, exist_ok=True)
    md = ["# Template external-validity mapping — summary\n",
          "Target: PreMoCir (clinical ML, *Sensors* 26(5):1656, 2026; notebooks Zenodo 10.5281/zenodo.18249069).\n",
          f"- Requirements mapped: **{len(rows)} / 15**",
          f"- Missing rows: {missing or 'none'}\n",
          "## By status\n",
          "| Status | Count | RMs |",
          "|---|---|---|"]
    for st in ("covered", "convention", "external"):
        if st in by_status:
            md.append(f"| {st} | {by_status[st]} | {', '.join(status_rms[st])} |")
    for st in by_status:
        if st not in ("covered", "convention", "external"):
            md.append(f"| {st} | {by_status[st]} | {', '.join(status_rms[st])} |")
    md.append(
        "\n**Reading:** the documentation / decision / version-control / output spine "
        "(covered) transfers directly; the coordination layer (convention) is available "
        "but not exercised retrospectively; restricted data, environments and institutional "
        "governance (external) depend on out-of-repo systems — the same boundary as the "
        "self-referential case. See `case-study/external_validity.md`.\n")
    with open(os.path.join(OUT, "external_validity_summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    print("\n".join(md))
    if missing:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
