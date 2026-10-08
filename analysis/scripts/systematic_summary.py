#!/usr/bin/env python3
"""Systematic review, step 3: flow counts and the requirement-stability test.

Reads literature/systematic/{candidates,screening,extraction}.csv and writes
results/systematic/summary.md and results/systematic/rm_support.csv.
"""
import collections
import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SYS = os.path.join(ROOT, "literature", "systematic")
OUT = os.path.join(ROOT, "results", "systematic")


def read(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main():
    os.makedirs(OUT, exist_ok=True)
    scr = read(os.path.join(SYS, "screening.csv"))
    ext = read(os.path.join(SYS, "extraction.csv"))
    base = read(os.path.join(ROOT, "literature", "included_studies.csv"))
    reasons = collections.Counter(
        r["reason"].split(":")[0] if r["decision"] == "exclude"
        else ("in base" if r["reason"].startswith("already") else "new") for r in scr)
    rm = collections.Counter()
    outside = collections.Counter()
    for r in ext:
        for k in filter(None, r["rm_mapping"].split(";")):
            rm[k] += 1
        if r["outside_framework"]:
            outside[r["outside_framework"]] += 1
    with_challenge = sum(1 for r in ext if r["rm_mapping"] or r["outside_framework"] not in ("", "none stated", "no abstract available"))
    mapped = sum(1 for r in ext if r["rm_mapping"])
    with open(os.path.join(OUT, "rm_support.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["rm_id", "new_studies"])
        for i in range(1, 16):
            w.writerow([f"RM{i}", rm.get(f"RM{i}", 0)])
    L = ["# Systematic screen: summary", "",
         f"- Candidates after title design filter: **{len(scr)}**",
         f"- Excluded: {sum(v for k, v in reasons.items() if k.startswith('E'))} "
         f"({', '.join(f'{k} {v}' for k, v in sorted(reasons.items()) if k.startswith('E'))})",
         f"- Included: {reasons['in base'] + reasons['new']} ({reasons['in base']} already in the structured base, **{reasons['new']} new**)",
         f"- Review total: {len(base)} + {reasons['new']} = **{len(base) + reasons['new']}** studies", "",
         "## Requirement-stability test on the new studies (abstract level)", "",
         f"- New studies reporting a challenge: {with_challenge} of {len(ext)}",
         f"- Mapped to at least one of RM1-RM15: {mapped}",
         "- Themes outside the framework: " + "; ".join(f"{k} ({v})" for k, v in outside.items() if k not in ("none stated", "no abstract available")),
         f"- No challenge stated in abstract: {outside['none stated']}; no abstract: {outside['no abstract available']}", "",
         "| Requirement | New studies |", "|---|---|"]
    L += [f"| RM{i} | {rm.get(f'RM{i}', 0)} |" for i in range(1, 16)]
    with open(os.path.join(OUT, "summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
