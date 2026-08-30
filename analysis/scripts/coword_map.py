#!/usr/bin/env python3
"""Render the Track A co-word map (OPEN_ITEMS 2.4).

Input : results/track_a/coword_nodes.csv, coword_edges.csv
Output:
  results/track_a/coword_map.gexf            full graph, Gephi/VOSviewer-ready
  manuscript/figures/coword_map.svg          top-N nodes, deterministic FR layout

Standard library only. No networkx / graphviz.
"""

import csv
import math
import os
import random
import xml.sax.saxutils as sx

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TA = os.path.join(ROOT, "results", "track_a")
FIG = os.path.join(ROOT, "manuscript", "figures")

TOP_N = 28          # nodes in the SVG
EDGE_MIN = 80       # min co-occurrence for an SVG edge (keeps the map legible)
W, H = 1100, 800
ITERS = 600


def read(p):
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def write_gexf(nodes, edges, path):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<gexf xmlns="http://gexf.net/1.3" version="1.3">',
             '<graph mode="static" defaultedgetype="undirected">',
             '<nodes>']
    for n in nodes:
        lines.append(f'<node id={sx.quoteattr(n["id"])} label={sx.quoteattr(n["label"])}>'
                     f'<viz:size xmlns:viz="http://gexf.net/1.3/viz" value="{n["weight"]}"/></node>')
    lines.append('</nodes>')
    lines.append('<edges>')
    for i, e in enumerate(edges):
        lines.append(f'<edge id="{i}" source={sx.quoteattr(e["source"])} '
                     f'target={sx.quoteattr(e["target"])} weight="{e["weight"]}"/>')
    lines.append('</edges></graph></gexf>')
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def fr_layout(ids, adj):
    rnd = random.Random(42)
    # start on a circle so nodes spread out
    pos = {}
    for idx, i in enumerate(ids):
        ang = 2 * math.pi * idx / len(ids)
        pos[i] = [W / 2 + 0.35 * W * math.cos(ang) + rnd.uniform(-5, 5),
                  H / 2 + 0.35 * H * math.sin(ang) + rnd.uniform(-5, 5)]
    k = 1.6 * math.sqrt((W * H) / len(ids))   # ideal spacing
    t = W / 8
    for _ in range(ITERS):
        disp = {i: [0.0, 0.0] for i in ids}
        for a_idx, a in enumerate(ids):
            for b in ids[a_idx + 1:]:
                dx = pos[a][0] - pos[b][0]
                dy = pos[a][1] - pos[b][1]
                d = math.hypot(dx, dy) or 0.01
                rep = k * k / d
                ux, uy = dx / d, dy / d
                disp[a][0] += ux * rep; disp[a][1] += uy * rep
                disp[b][0] -= ux * rep; disp[b][1] -= uy * rep
        for (a, b), w in adj.items():
            dx = pos[a][0] - pos[b][0]
            dy = pos[a][1] - pos[b][1]
            d = math.hypot(dx, dy) or 0.01
            att = d * d / k * (0.15 + 0.35 * w)   # gentle attraction
            ux, uy = dx / d, dy / d
            disp[a][0] -= ux * att; disp[a][1] -= uy * att
            disp[b][0] += ux * att; disp[b][1] += uy * att
        for i in ids:
            dl = math.hypot(*disp[i]) or 0.01
            pos[i][0] += disp[i][0] / dl * min(dl, t)
            pos[i][1] += disp[i][1] / dl * min(dl, t)
            pos[i][0] = min(W - 60, max(60, pos[i][0]))
            pos[i][1] = min(H - 50, max(50, pos[i][1]))
        t *= 0.985
    return pos


def write_svg(nodes, edges, path):
    top = sorted(nodes, key=lambda n: -int(n["weight"]))[:TOP_N]
    keep = {n["id"] for n in top}
    wmax = max(int(n["weight"]) for n in top)
    e_in = [e for e in edges if e["source"] in keep and e["target"] in keep
            and int(e["weight"]) >= EDGE_MIN]
    emax = max((int(e["weight"]) for e in e_in), default=1)
    ids = [n["id"] for n in top]
    adj = {}
    for e in e_in:
        adj[(e["source"], e["target"])] = int(e["weight"]) / emax
    pos = fr_layout(ids, adj)

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="system-ui,Arial,sans-serif">',
           f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
           f'<text x="20" y="30" font-size="15" font-weight="700">Track A co-word map — top {TOP_N} concepts (edge co-occurrence &#8805; {EDGE_MIN})</text>']
    for e in e_in:
        a, b = pos[e["source"]], pos[e["target"]]
        sw = 0.4 + 3.0 * int(e["weight"]) / emax
        out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
                   f'stroke="#b9c3d0" stroke-width="{sw:.2f}" stroke-opacity="0.6"/>')
    for n in top:
        x, y = pos[n["id"]]
        r = 5 + 22 * int(n["weight"]) / wmax
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="#3b6fb0" fill-opacity="0.85"/>')
        out.append(f'<text x="{x:.1f}" y="{y - r - 3:.1f}" font-size="11" text-anchor="middle" '
                   f'fill="#1a1a1a">{sx.escape(n["label"])}</text>')
    out.append("</svg>")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))


def main():
    nodes = read(os.path.join(TA, "coword_nodes.csv"))
    edges = read(os.path.join(TA, "coword_edges.csv"))
    os.makedirs(FIG, exist_ok=True)
    write_gexf(nodes, edges, os.path.join(TA, "coword_map.gexf"))
    write_svg(nodes, edges, os.path.join(FIG, "coword_map.svg"))
    print(f"nodes {len(nodes)}, edges {len(edges)}")
    print(f"  {os.path.join(TA, 'coword_map.gexf')}")
    print(f"  {os.path.join(FIG, 'coword_map.svg')}  (top {TOP_N})")


if __name__ == "__main__":
    main()
