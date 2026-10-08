#!/usr/bin/env python3
"""Platform evaluation (manuscript 2): aggregate criterion scores into requirement support.

Inputs   framework/evaluation/criteria.csv, scores.csv
Outputs  results/evaluation/
           requirement_support.csv   mean and label per requirement x platform, free and best tier
           platform_summary.csv      overall means, label counts, tier-gating delta, verified share
           best_of_breed.csv         per criterion: best free score, who reaches it
           residual_gaps.csv         criteria no platform meets natively on the free tier
           summary.md
Rule (protocol.md): requirement score = mean of its criterion scores (0-3);
Direct >= 2.5, Partial >= 1.5, Limited >= 0.5, otherwise Not supported.
"""
import collections
import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EV = os.path.join(ROOT, "framework", "evaluation")
OUT = os.path.join(ROOT, "results", "evaluation")
PLAT = ["GH", "GL", "BB", "AT"]
NAME = {"GH": "GitHub", "GL": "GitLab", "BB": "Bitbucket", "AT": "Bitbucket + Jira + Confluence"}
DIFF = ("RM1", "RM2", "RM5")


def label(x):
    return "Direct" if x >= 2.5 else "Partial" if x >= 1.5 else "Limited" if x >= 0.5 else "Not supported"


def read(name):
    with open(os.path.join(EV, name), newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def mean(xs):
    xs = list(xs)
    return sum(xs) / len(xs)


def main():
    os.makedirs(OUT, exist_ok=True)
    crit = read("criteria.csv")
    sc = read("scores.csv")
    rms = sorted({c["rm_id"] for c in crit}, key=lambda s: int(s[2:]))
    cell = {(s["criterion_id"], s["platform"]): s for s in sc}
    assert len(cell) == len(crit) * len(PLAT)

    req = {}
    for rm in rms:
        ids = [c["criterion_id"] for c in crit if c["rm_id"] == rm]
        for p in PLAT:
            req[rm, p] = (mean(int(cell[i, p]["score_free"]) for i in ids),
                          mean(int(cell[i, p]["score_best"]) for i in ids))
    with open(os.path.join(OUT, "requirement_support.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["rm_id", "n_criteria"] + [f"{p}_{t}" for p in PLAT for t in ("free", "free_label", "best", "best_label")])
        for rm in rms:
            row = [rm, sum(1 for c in crit if c["rm_id"] == rm)]
            for p in PLAT:
                f, b = req[rm, p]
                row += [f"{f:.2f}", label(f), f"{b:.2f}", label(b)]
            w.writerow(row)

    summ = {}
    with open(os.path.join(OUT, "platform_summary.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["platform", "mean_free_15", "mean_free_core14", "mean_best_15", "direct", "partial", "limited", "not_supported",
                    "differentiators_free", "others_free", "criteria_native_free", "criteria_absent_free",
                    "criteria_gated_by_tier", "cells_verified"])
        for p in PLAT:
            f15 = mean(req[rm, p][0] for rm in rms)
            f14 = mean(req[rm, p][0] for rm in rms if rm != "RM15")
            b15 = mean(req[rm, p][1] for rm in rms)
            labs = collections.Counter(label(req[rm, p][0]) for rm in rms)
            cells = [cell[c["criterion_id"], p] for c in crit]
            summ[p] = dict(f15=f15, f14=f14, b15=b15, labs=labs,
                           diff=mean(req[rm, p][0] for rm in DIFF), rest=mean(req[rm, p][0] for rm in rms if rm not in DIFF),
                           native=sum(c["score_free"] == "3" for c in cells), absent=sum(c["score_free"] == "0" for c in cells),
                           gated=sum(c["score_best"] > c["score_free"] for c in cells),
                           ver=sum(c["verification"].startswith("verified") for c in cells))
            s = summ[p]
            w.writerow([p, f"{f15:.2f}", f"{f14:.2f}", f"{b15:.2f}", labs["Direct"], labs["Partial"], labs["Limited"], labs["Not supported"],
                        f"{s['diff']:.2f}", f"{s['rest']:.2f}", s["native"], s["absent"], s["gated"], s["ver"]])

    bob, gaps = [], []
    for c in crit:
        i = c["criterion_id"]
        best = max(int(cell[i, p]["score_free"]) for p in PLAT)
        who = [p for p in PLAT if int(cell[i, p]["score_free"]) == best]
        bob.append([i, c["rm_id"], c["expected_capability"], best, ";".join(who)])
        if best < 3:
            gaps.append([i, c["rm_id"], c["expected_capability"], best])
    with open(os.path.join(OUT, "best_of_breed.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["criterion_id", "rm_id", "expected_capability", "best_free_score", "reached_by"])
        w.writerows(bob)
    with open(os.path.join(OUT, "residual_gaps.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["criterion_id", "rm_id", "expected_capability", "best_free_score"])
        w.writerows(gaps)
    # weakest-link sensitivity: a requirement is only as supported as its weakest criterion
    weak = {(rm, p): min(int(cell[c["criterion_id"], p]["score_free"]) for c in crit if c["rm_id"] == rm) for rm in rms for p in PLAT}
    with open(os.path.join(OUT, "requirement_weakest_link.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["rm_id"] + PLAT)
        for rm in rms:
            w.writerow([rm] + [weak[rm, p] for p in PLAT])
    combo = {rm: mean(b[3] for b in bob if b[1] == rm) for rm in rms}
    sole = collections.Counter(b[4] for b in bob if ";" not in b[4])

    L = ["# Platform evaluation: summary", "",
         "Free tier, public project. Scores 0-3 per criterion; requirement score is the mean of its criteria.", "",
         "| Platform | Mean (15) | Core 14 | Best tier | Direct | Partial | Limited | Not supp. | Differentiators | Others | Native criteria | Absent | Tier-gated | Cells verified |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for p in PLAT:
        s = summ[p]
        L.append(f"| {NAME[p]} | {s['f15']:.2f} | {s['f14']:.2f} | {s['b15']:.2f} | {s['labs']['Direct']} | {s['labs']['Partial']} | "
                 f"{s['labs']['Limited']} | {s['labs']['Not supported']} | {s['diff']:.2f} | {s['rest']:.2f} | {s['native']}/62 | "
                 f"{s['absent']} | {s['gated']} | {s['ver']}/62 |")
    L += ["", "## Requirement support, free tier", "", "| Req. | " + " | ".join(NAME[p] for p in PLAT) + " | Best of breed |", "|---|" + "---|" * (len(PLAT) + 1)]
    for rm in rms:
        L.append(f"| {rm} | " + " | ".join(f"{req[rm, p][0]:.2f} {label(req[rm, p][0])[0]}" for p in PLAT) + f" | {combo[rm]:.2f} {label(combo[rm])[0]} |")
    L += ["", "## Weakest-link sensitivity (minimum criterion score per requirement, free tier)", "",
          "| Platform | All criteria native (min 3) | Min 2 | Min 1 | Min 0 |", "|---|---|---|---|---|"]
    for p in PLAT:
        k = collections.Counter(weak[rm, p] for rm in rms)
        L.append(f"| {NAME[p]} | {k[3]} | {k[2]} | {k[1]} | {k[0]} |")
    L += ["", f"- Best-of-breed mean (15): **{mean(combo.values()):.2f}**; differentiators {mean(combo[r] for r in DIFF):.2f}",
          f"- Criteria where one platform alone reaches the best score: " + ", ".join(f"{NAME[k]} {v}" for k, v in sole.most_common()),
          f"- Residual gaps (no platform native on the free tier): **{len(gaps)}** of 62 criteria:",
          ""] + [f"  - {g[0]} {g[2]} (best {g[3]})" for g in gaps]
    with open(os.path.join(OUT, "summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
