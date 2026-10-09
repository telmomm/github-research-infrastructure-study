#!/usr/bin/env python3
"""Agreement between the reference scores and the returned rating sheets (manuscript 2).

Reads every completed sheet in framework/evaluation/ratings/ (rater_sheet_evaluator_N.md),
compares it with the reference scores and with the other sheets, and reports how robust
the reference scores are. Partial sheets are accepted; empty cells are skipped.

The five sheets returned on 2026-10-09 were completed by AI assistants, not by people
(framework/evaluation/ratings/README.md). They test whether the scores survive a second
reading of the rubric; they are not human inter-rater reliability.

Outputs (results/evaluation/)
  panel_scores.csv        every cell: reference, five panel scores, panel median, range
  panel_agreement.csv     per rater vs reference, and pairwise
  panel_requirements.csv  requirement means per configuration: reference, each rater, panel median
  panel_strata.csv        agreement with the reference by verification status and by configuration
  panel_gaps.csv          the reference residual gaps: how many sheets also find no native support
  panel_summary.md
"""
import collections
import csv
import glob
import itertools
import os
import re
import statistics

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EV = os.path.join(ROOT, "framework", "evaluation")
OUT = os.path.join(ROOT, "results", "evaluation")
PLAT = ["GH", "GL", "BB", "AT"]
NAME = {"GH": "GitHub", "GL": "GitLab", "BB": "Bitbucket", "AT": "Bitbucket + Jira + Confluence"}
ROW = re.compile(r"^\|\s*\**\s*(RM\d+\.\d+)\b")


def parse(path):
    out = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = ROW.match(line)
            if not m:
                continue
            cells = [c.strip().strip("*") for c in line.strip().strip("|").split("|")]
            for i in range(len(cells) - 3):
                four = cells[i:i + 4]
                if all(re.fullmatch(r"[0-3?]?", c) for c in four) and any(four):
                    out[m.group(1)] = [int(c) if c.isdigit() else None for c in four]
                    break
    return out


def wkappa(a, b):
    """Linearly weighted Cohen's kappa on the 0-3 scale."""
    n = len(a)
    obs = sum(abs(x - y) for x, y in zip(a, b)) / n
    ca, cb = collections.Counter(a), collections.Counter(b)
    exp = sum(ca[i] * cb[j] * abs(i - j) for i in range(4) for j in range(4)) / n ** 2
    return 1 - obs / exp if exp else float("nan")


def alpha_ordinal(units):
    """Krippendorff's alpha, ordinal metric; units = list of lists of ratings (None dropped)."""
    units = [[v for v in u if v is not None] for u in units]
    units = [u for u in units if len(u) >= 2]
    n = sum(len(u) for u in units)
    tot = collections.Counter(v for u in units for v in u)

    def d2(c, k):
        lo, hi = min(c, k), max(c, k)
        return (sum(tot[g] for g in range(lo, hi + 1)) - (tot[lo] + tot[hi]) / 2) ** 2
    do = sum(sum(d2(a, b) for a, b in itertools.permutations(u, 2)) / (len(u) - 1) for u in units) / n
    de = sum(tot[c] * tot[k] * d2(c, k) for c in range(4) for k in range(4)) / (n * (n - 1))
    return 1 - do / de


def main():
    crit = [r for r in csv.DictReader(open(os.path.join(EV, "criteria.csv"), encoding="utf-8"))]
    ids = [c["criterion_id"] for c in crit]
    rms = sorted({c["rm_id"] for c in crit}, key=lambda s: int(s[2:]))
    ref = {(r["criterion_id"], r["platform"]): int(r["score_free"])
           for r in csv.DictReader(open(os.path.join(EV, "scores.csv"), encoding="utf-8"))}
    verified = {(r["criterion_id"], r["platform"]) for r in csv.DictReader(open(os.path.join(EV, "scores.csv"), encoding="utf-8"))
                if r["verification"].startswith("verified")}
    files = sorted(glob.glob(os.path.join(EV, "ratings", "rater_sheet_evaluator_*.md")))
    raters = {}
    for f in files:
        rid = "P" + re.search(r"_(\d+)\.md$", f).group(1)
        p = parse(f)
        raters[rid] = {(i, pl): p[i][k] for i in p for k, pl in enumerate(PLAT)}
        print(rid, "rows parsed", len(p), "missing cells", sum(v is None for v in raters[rid].values()) + 4 * (62 - len(p)))
    R = list(raters)
    cells = [(i, p) for i in ids for p in PLAT]

    med = {}
    with open(os.path.join(OUT, "panel_scores.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["criterion_id", "platform", "reference", "verified"] + R + ["panel_median", "panel_range"])
        for c in cells:
            vals = [raters[r].get(c) for r in R]
            got = [v for v in vals if v is not None]
            med[c] = statistics.median(got) if got else None
            w.writerow([c[0], c[1], ref[c], "yes" if c in verified else ""] + ["" if v is None else v for v in vals]
                       + ["" if med[c] is None else med[c], max(got) - min(got) if got else ""])

    agree = []
    for r in R:
        pairs = [(ref[c], raters[r][c]) for c in cells if raters[r].get(c) is not None]
        a, b = zip(*pairs)
        agree.append([f"reference vs {r}", len(pairs), sum(x == y for x, y in pairs) / len(pairs),
                      sum(abs(x - y) <= 1 for x, y in pairs) / len(pairs), wkappa(a, b), statistics.mean(y - x for x, y in pairs)])
    for r, s in itertools.combinations(R, 2):
        pairs = [(raters[r][c], raters[s][c]) for c in cells if raters[r].get(c) is not None and raters[s].get(c) is not None]
        a, b = zip(*pairs)
        agree.append([f"{r} vs {s}", len(pairs), sum(x == y for x, y in pairs) / len(pairs),
                      sum(abs(x - y) <= 1 for x, y in pairs) / len(pairs), wkappa(a, b), ""])
    pm = [(ref[c], med[c]) for c in cells if med[c] is not None]
    agree.append(["reference vs panel median", len(pm), sum(x == y for x, y in pm) / len(pm),
                  sum(abs(x - y) <= 1 for x, y in pm) / len(pm), "", statistics.mean(y - x for x, y in pm)])
    with open(os.path.join(OUT, "panel_agreement.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["pair", "n", "exact", "within_one", "weighted_kappa", "mean_difference"])
        for a in agree:
            w.writerow([a[0], a[1], f"{a[2]:.3f}", f"{a[3]:.3f}", "" if a[4] == "" else f"{a[4]:.2f}", "" if a[5] == "" else f"{a[5]:+.2f}"])
    alpha6 = alpha_ordinal([[ref[c]] + [raters[r].get(c) for r in R] for c in cells])
    alpha5 = alpha_ordinal([[raters[r].get(c) for r in R] for c in cells])

    def reqmean(src, rm, p):
        v = [src.get((i, p)) for i in ids if i.startswith(rm + ".")]
        v = [x for x in v if x is not None]
        return sum(v) / len(v) if v else None
    sources = dict(reference=ref, **raters, median=med)
    with open(os.path.join(OUT, "panel_requirements.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["rm_id", "platform"] + list(sources))
        for rm in rms:
            for p in PLAT:
                w.writerow([rm, p] + [f"{reqmean(s, rm, p):.2f}" for s in sources.values()])
    overall = {k: {p: statistics.mean(reqmean(s, rm, p) for rm in rms) for p in PLAT} for k, s in sources.items()}
    diffm = {k: {p: statistics.mean(reqmean(s, rm, p) for rm in ("RM1", "RM2", "RM5")) for p in PLAT} for k, s in sources.items()}
    restm = {k: {p: statistics.mean(reqmean(s, rm, p) for rm in rms if rm not in ("RM1", "RM2", "RM5")) for p in PLAT} for k, s in sources.items()}

    def label(x):
        return "D" if x >= 2.5 else "P" if x >= 1.5 else "L" if x >= 0.5 else "N"
    same_label = sum(label(reqmean(ref, rm, p)) == label(reqmean(med, rm, p)) for rm in rms for p in PLAT)
    big = [(c, ref[c], [raters[r].get(c) for r in R]) for c in cells if med[c] is not None and abs(med[c] - ref[c]) >= 1.5]
    ver_dis = [(c, ref[c], med[c]) for c in cells if c in verified and med[c] is not None and abs(med[c] - ref[c]) >= 1]

    L = ["# Second-reading check (AI raters): summary", "",
         f"{len(R)} completed rating sheets ({R[0]}-{R[-1]}), compared with the reference scores. The sheets were",
         "completed by AI assistants; this is a robustness check, not human inter-rater reliability.", "",
         f"- Krippendorff's alpha (ordinal), reference + panel: **{alpha6:.2f}**; panel only: {alpha5:.2f}", "",
         "| Pair | n | Exact | Within one | Weighted kappa | Mean difference |", "|---|---|---|---|---|---|"]
    L += [f"| {a[0]} | {a[1]} | {a[2]:.0%} | {a[3]:.0%} | {'' if a[4] == '' else f'{a[4]:.2f}'} | {'' if a[5] == '' else f'{a[5]:+.2f}'} |" for a in agree]
    L += ["", "## Overall mean (15 requirements) by configuration", "", "| Source | " + " | ".join(NAME[p] for p in PLAT) + " | Ranking |", "|---|---|---|---|---|---|"]
    for k in sources:
        rank = " > ".join(sorted(PLAT, key=lambda p: -overall[k][p]))
        L.append(f"| {k} | " + " | ".join(f"{overall[k][p]:.2f}" for p in PLAT) + f" | {rank} |")
    L += ["", "## Differentiators (RM1, RM2, RM5) vs the other twelve", "", "| Source | " + " | ".join(NAME[p] for p in PLAT) + " |", "|---|---|---|---|---|"]
    for k in sources:
        L.append(f"| {k} | " + " | ".join(f"{diffm[k][p]:.2f} vs {restm[k][p]:.2f}" for p in PLAT) + " |")
    L += ["", f"- Requirement labels unchanged between reference and panel median: {same_label} of 60",
          f"- Cells where the panel median differs from the reference by 1.5 or more: {len(big)}"]
    L += [f"  - {c[0]} {c[1]}: reference {r}, panel {v}" for c, r, v in big]
    L += ["", f"- Verified cells where the panel median differs from the reference by 1 or more: {len(ver_dis)} of {len(verified)}"]
    L += [f"  - {c[0]} {c[1]}: reference {r}, panel median {m}" for c, r, m in ver_dis]
    # agreement by stratum: verified or not, and by configuration
    strata = [("verified cells", [c for c in cells if c in verified]), ("unverified cells", [c for c in cells if c not in verified])]
    strata += [(NAME[p], [c for c in cells if c[1] == p]) for p in PLAT]
    srows = []
    for name, sub in strata:
        ex, w1, md = [], [], []
        for r in R:
            pairs = [(ref[c], raters[r][c]) for c in sub if raters[r].get(c) is not None]
            ex.append(sum(x == y for x, y in pairs) / len(pairs))
            w1.append(sum(abs(x - y) <= 1 for x, y in pairs) / len(pairs))
            md.append(statistics.mean(y - x for x, y in pairs))
        pm = [(ref[c], med[c]) for c in sub]
        srows.append([name, len(sub), min(ex), max(ex), min(w1), max(w1), min(md), max(md),
                      sum(x == y for x, y in pm) / len(pm), statistics.mean(y - x for x, y in pm)])
    with open(os.path.join(OUT, "panel_strata.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["stratum", "cells", "exact_min", "exact_max", "within_one_min", "within_one_max",
                    "mean_difference_min", "mean_difference_max", "exact_vs_median", "mean_difference_vs_median"])
        for a in srows:
            w.writerow([a[0], a[1]] + [f"{x:.3f}" for x in a[2:6]] + [f"{x:+.2f}" for x in a[6:8]] + [f"{a[8]:.3f}", f"{a[9]:+.2f}"])
    L += ["", "## Agreement with the reference by stratum (range over the sheets)", "",
          "| Stratum | Cells | Exact | Within one | Mean difference | Exact vs panel median |", "|---|---|---|---|---|---|"]
    L += [f"| {a[0]} | {a[1]} | {a[2]:.0%}-{a[3]:.0%} | {a[4]:.0%}-{a[5]:.0%} | {a[6]:+.2f} to {a[7]:+.2f} | {a[8]:.0%} |" for a in srows]

    # sensitivity: keep the reference where it was verified, take the panel median elsewhere
    mixed = {c: ref[c] if c in verified else med[c] for c in cells}
    mix_overall = {p: statistics.mean(reqmean(mixed, rm, p) for rm in rms) for p in PLAT}
    L += ["", "## Sensitivity: reference on verified cells, panel median on the rest", "",
          "| " + " | ".join(NAME[p] for p in PLAT) + " | Ranking |", "|---|---|---|---|---|",
          "| " + " | ".join(f"{mix_overall[p]:.2f}" for p in PLAT) + " | " + " > ".join(sorted(PLAT, key=lambda p: -mix_overall[p])) + " |"]

    # what holds in every reading
    readings = ["reference"] + R
    first = collections.Counter(max(PLAT, key=lambda p: overall[k][p]) for k in readings)
    last = collections.Counter(min(PLAT, key=lambda p: overall[k][p]) for k in readings)
    lower = {p: sum(diffm[k][p] < restm[k][p] for k in readings) for p in PLAT}
    native = {k: {p: sum(sources[k].get((i, p)) == 3 for i in ids) for p in PLAT} for k in sources}
    L += ["", f"## What holds across the {len(readings)} readings (reference and {len(R)} sheets)", "",
          "- Highest overall mean: " + ", ".join(f"{NAME[p]} {n}" for p, n in first.most_common()),
          "- Lowest overall mean: " + ", ".join(f"{NAME[p]} {n}" for p, n in last.most_common()),
          "- RM1, RM2 and RM5 score below the other twelve: " + ", ".join(f"{NAME[p]} {lower[p]} of {len(readings)}" for p in PLAT),
          "- Native criteria (score 3) per reading: " + "; ".join(f"{k} " + "/".join(str(native[k][p]) for p in PLAT) for k in sources)]
    for cid, text in (("RM5.1", "decision as a distinct record"), ("RM6.1", "mandatory review"), ("RM14.2", "archive with identifier"), ("RM14.3", "citation metadata used")):
        L.append(f"- {cid} ({text}), sheets scoring 3: " + ", ".join(f"{NAME[p]} {sum(raters[r].get((cid, p)) == 3 for r in R)}" for p in PLAT)
                 + "; reference " + "/".join(str(ref[cid, p]) for p in PLAT))

    # residual gaps of the reference: does each sheet also find no native support?
    gaps = [i for i in ids if max(ref[i, p] for p in PLAT) < 3]
    confirm = {i: sum(max(v for v in (raters[r].get((i, p)) for p in PLAT) if v is not None) < 3 for r in R) for i in gaps}
    per_reading = {k: sum(max(v for v in (sources[k].get((i, p)) for p in PLAT) if v is not None) < 3 for i in ids) for k in sources}
    with open(os.path.join(OUT, "panel_gaps.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["criterion_id", "reference_best", "sheets_also_without_native", "sheets"] + [f"{r}_best" for r in R])
        for i in gaps:
            w.writerow([i, max(ref[i, p] for p in PLAT), confirm[i], len(R)]
                       + [max(v for v in (raters[r].get((i, p)) for p in PLAT) if v is not None) for r in R])
    L += ["", f"## Residual gaps (no configuration native): {len(gaps)} in the reference", "",
          "- Criteria with no native support, per reading: " + ", ".join(f"{k} {n}" for k, n in per_reading.items()),
          "- Reference gaps and the number of sheets that also find no configuration native: "
          + ", ".join(f"{i} {confirm[i]}/{len(R)}" for i in gaps),
          f"- Confirmed by a majority of the sheets: {sum(n * 2 > len(R) for n in confirm.values())} of {len(gaps)}"]

    # cells every sheet scores on the same side of the reference
    side = [(c, ref[c], [raters[r].get(c) for r in R]) for c in cells
            if all(raters[r].get(c) is not None for r in R)
            and (all(raters[r][c] > ref[c] for r in R) or all(raters[r][c] < ref[c] for r in R))]
    L += ["", f"## Cells every sheet scores on the same side of the reference: {len(side)}", "",
          f"Verified {sum(c in verified for c, _, _ in side)}, unverified {sum(c not in verified for c, _, _ in side)}. "
          "The unverified ones are the candidates for adjudication.", ""]
    L += [f"- {c[0]} {c[1]}: reference {r}, sheets {v}" + (" (verified)" if c in verified else "") for c, r, v in side]
    with open(os.path.join(OUT, "panel_summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
