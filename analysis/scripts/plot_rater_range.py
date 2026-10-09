#!/usr/bin/env python3
"""Reference requirement scores against the spread of the returned rating sheets (manuscript 2).

Reads results/evaluation/panel_requirements.csv (written by rater_agreement.py) and writes
manuscript_2/fig_raters.svg (build converts it to PDF with rsvg-convert). Four panels, one
per configuration; each row is a requirement: a grey bar spans the lowest to the highest
sheet, a tick marks their median, a dot marks the reference score.
"""
import csv
import os
import statistics

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "results", "evaluation", "panel_requirements.csv")
OUT = os.path.join(ROOT, "manuscript_2", "fig_raters.svg")

PLAT = [("GH", "GitHub"), ("GL", "GitLab"), ("BB", "Bitbucket"), ("AT", "Bitbucket + Jira + Confl.")]
REF, BAR, INK, MUTED, RULE = "#0d366b", "#b9b8b2", "#1f1f1d", "#6b6b66", "#dedcd6"
W, LABEL_W, PANEL_GAP, ROW_H, TOP = 468, 30, 12.0, 10.0, 34.0


def main():
    with open(SRC, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    raters = [k for k in rows[0] if k.startswith("P")]
    rms = sorted({r["rm_id"] for r in rows}, key=lambda s: int(s[2:]))
    data = {(r["rm_id"], r["platform"]): (float(r["reference"]), [float(r[k]) for k in raters]) for r in rows}
    pw = (W - LABEL_W - PANEL_GAP * (len(PLAT) - 1) - 8) / len(PLAT)
    bottom = TOP + len(rms) * ROW_H
    out = []
    # legend
    out.append(f'<rect x="{LABEL_W}" y="3.5" width="22" height="4" rx="2" fill="{BAR}"/>')
    out.append(f'<line x1="{LABEL_W + 13}" y1="1.5" x2="{LABEL_W + 13}" y2="9.5" stroke="{INK}" stroke-width="1.2"/>')
    out.append(f'<text x="{LABEL_W + 27}" y="8" font-size="7" fill="{INK}">range of the {len(raters)} AI rating sheets, with their median</text>')
    out.append(f'<circle cx="{LABEL_W + 190}" cy="5.5" r="2.6" fill="{REF}" stroke="#ffffff" stroke-width="0.8"/>')
    out.append(f'<text x="{LABEL_W + 197}" y="8" font-size="7" fill="{INK}">reference score</text>')
    for k, rm in enumerate(rms):
        out.append(f'<text x="{LABEL_W - 5}" y="{TOP + k * ROW_H + ROW_H / 2 + 2.4:.2f}" font-size="6.6" fill="{INK}" text-anchor="end">{rm}</text>')
    for j, (p, name) in enumerate(PLAT):
        x0 = LABEL_W + j * (pw + PANEL_GAP)

        def X(v):
            return x0 + v / 3 * pw
        out.append(f'<text x="{x0 + pw / 2:.2f}" y="{TOP - 9:.2f}" font-size="7" fill="{INK}" text-anchor="middle">{name}</text>')
        for v in range(4):
            out.append(f'<line x1="{X(v):.2f}" y1="{TOP - 3:.2f}" x2="{X(v):.2f}" y2="{bottom:.2f}" stroke="{RULE}" stroke-width="0.5"/>')
            out.append(f'<text x="{X(v):.2f}" y="{bottom + 8:.2f}" font-size="6.2" fill="{MUTED}" text-anchor="middle">{v}</text>')
        for k, rm in enumerate(rms):
            ref, vals = data[rm, p]
            y = TOP + k * ROW_H + ROW_H / 2
            lo, hi = min(vals), max(vals)
            out.append(f'<rect x="{X(lo) - 2:.2f}" y="{y - 2:.2f}" width="{X(hi) - X(lo) + 4:.2f}" height="4" rx="2" fill="{BAR}"/>')
            m = X(statistics.median(vals))
            out.append(f'<line x1="{m:.2f}" y1="{y - 3.6:.2f}" x2="{m:.2f}" y2="{y + 3.6:.2f}" stroke="{INK}" stroke-width="1.2"/>')
            out.append(f'<circle cx="{X(ref):.2f}" cy="{y:.2f}" r="2.6" fill="{REF}" stroke="#ffffff" stroke-width="0.8"/>')
    out.append(f'<text x="{LABEL_W + (W - LABEL_W) / 2:.2f}" y="{bottom + 18:.2f}" font-size="6.6" fill="{MUTED}" text-anchor="middle">requirement score (mean of its capability scores, 0 to 3)</text>')
    h = bottom + 23
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}pt" height="{h:.0f}pt" viewBox="0 0 {W} {h:.0f}" '
           f'font-family="Helvetica, Arial, sans-serif">\n<rect width="{W}" height="{h:.0f}" fill="#ffffff"/>\n' + "\n".join(out) + "\n</svg>\n")
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(svg)
    print("wrote", os.path.relpath(OUT, ROOT), f"{W}x{h:.0f}")


if __name__ == "__main__":
    main()
