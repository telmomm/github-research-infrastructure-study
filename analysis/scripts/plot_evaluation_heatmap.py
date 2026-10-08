#!/usr/bin/env python3
"""Heat map of the 62 criterion scores by configuration (manuscript 2, free plans).

Reads framework/evaluation/{criteria,scores}.csv and writes manuscript_2/fig_heatmap.svg
(build converts it to PDF with rsvg-convert). Two bands: RM1-RM8 and RM9-RM15.
Ordinal single-hue ramp, validated light->dark; score 0 is an empty outlined cell.
"""
import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EV = os.path.join(ROOT, "framework", "evaluation")
OUT = os.path.join(ROOT, "manuscript_2", "fig_heatmap.svg")

PLAT = [("GH", "GitHub"), ("GL", "GitLab"), ("BB", "Bitbucket"), ("AT", "Bitbucket + Jira + Confl.")]
FILL = {1: "#86b6ef", 2: "#2a78d6", 3: "#0d366b"}
LEGEND = [(3, "3 native"), (2, "2 by convention"), (1, "1 marginal"), (0, "0 absent")]
INK, MUTED, RULE = "#1f1f1d", "#6b6b66", "#b9b8b2"
W, LABEL_W = 468, 102
CELL, GAP, GROUP_GAP, ROW_H, ROW_GAP = 8.0, 1.5, 6.0, 11.0, 1.5
BANDS = [range(1, 9), range(9, 16)]


def read(name):
    with open(os.path.join(EV, name), newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def cell(x, y, score):
    if score == 0:
        return (f'<rect x="{x + .3:.2f}" y="{y + .3:.2f}" width="{CELL - .6:.2f}" height="{ROW_H - .6:.2f}" rx="1" '
                f'fill="#ffffff" stroke="{RULE}" stroke-width="0.6"/>')
    return f'<rect x="{x:.2f}" y="{y:.2f}" width="{CELL:.2f}" height="{ROW_H:.2f}" rx="1" fill="{FILL[score]}"/>'


def main():
    crit = read("criteria.csv")
    score = {(s["criterion_id"], s["platform"]): int(s["score_free"]) for s in read("scores.csv")}
    out, y = [], 16.0
    # legend
    x = LABEL_W
    for s, text in LEGEND:
        out.append(cell(x, 2, s))
        out.append(f'<text x="{x + CELL + 4:.2f}" y="10.4" font-size="7" fill="{INK}">{text}</text>')
        x += CELL + 4 + len(text) * 3.6 + 12
    y += 8
    for band in BANDS:
        x = LABEL_W
        head_y, top = y, y + 5
        for rm in band:
            ids = [c["criterion_id"] for c in crit if c["rm_id"] == f"RM{rm}"]
            width = len(ids) * CELL + (len(ids) - 1) * GAP
            out.append(f'<text x="{x + width / 2:.2f}" y="{head_y:.2f}" font-size="6.6" fill="{MUTED}" text-anchor="middle">RM{rm}</text>')
            out.append(f'<line x1="{x:.2f}" y1="{head_y + 2.2:.2f}" x2="{x + width:.2f}" y2="{head_y + 2.2:.2f}" stroke="{RULE}" stroke-width="0.5"/>')
            for k, cid in enumerate(ids):
                for r, (p, _) in enumerate(PLAT):
                    out.append(cell(x + k * (CELL + GAP), top + r * (ROW_H + ROW_GAP), score[cid, p]))
            x += width + GROUP_GAP
        for r, (_, name) in enumerate(PLAT):
            out.append(f'<text x="{LABEL_W - 6}" y="{top + r * (ROW_H + ROW_GAP) + 7.8:.2f}" font-size="7" fill="{INK}" text-anchor="end">{name}</text>')
        y = top + len(PLAT) * (ROW_H + ROW_GAP) + 16
    h = y - 10
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}pt" height="{h:.0f}pt" viewBox="0 0 {W} {h:.0f}" '
           f'font-family="Helvetica, Arial, sans-serif">\n<rect width="{W}" height="{h:.0f}" fill="#ffffff"/>\n' + "\n".join(out) + "\n</svg>\n")
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(svg)
    print("wrote", os.path.relpath(OUT, ROOT), f"{W}x{h:.0f}")


if __name__ == "__main__":
    main()
