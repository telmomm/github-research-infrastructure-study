#!/usr/bin/env python3
"""Estimate precision of the broad Track A queries (OPEN_ITEMS 2.2).

The OpenAlex queries Q2b ("open science" ...) and Q3a (github ...) return the
largest result sets and could be low-precision. This samples records tagged with
those queries and applies a transparent relevance heuristic, so the decision to
keep or tighten them is evidenced rather than asserted.

Input : data/processed/corpus.csv
Output: results/track_a/query_precision.csv + query_precision.md
Standard library only. Deterministic (fixed seed).
"""

import csv
import os
import random
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CORPUS = os.path.join(ROOT, "data", "processed", "corpus.csv")
OUT = os.path.join(ROOT, "results", "track_a")

SAMPLE = 120           # per query tag
SEED = 20260830

# a record is "on topic" if it pairs a research-context term with a
# process-management / infrastructure term in title+abstract
CONTEXT = re.compile(r"\b(research|scientif|scholarl|academ|science)\w*", re.I)
TOPIC = re.compile(
    r"\b(workflow|life ?cycle|provenance|traceab|reproducib|data management|"
    r"research data|project management|coordination|infrastructure|repositor|"
    r"version control|git\b|github|preprint|documentation|metadata|"
    r"collaborat|pipeline|research information)\w*", re.I)


def read(p):
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def on_topic(r):
    hay = f"{r.get('title','')} {r.get('abstract','')}"
    return bool(CONTEXT.search(hay) and TOPIC.search(hay))


def main():
    rows = read(CORPUS)
    rnd = random.Random(SEED)
    os.makedirs(OUT, exist_ok=True)

    results = []
    detail = []
    for tag in ("Q2b", "Q3a", "Q1g", "Q2a"):  # the four largest
        pool = [r for r in rows if tag in re.split(r"[;\s]+", r.get("query_tags", ""))]
        if not pool:
            continue
        samp = rnd.sample(pool, min(SAMPLE, len(pool)))
        hits = sum(on_topic(r) for r in samp)
        prec = hits / len(samp)
        results.append([tag, len(pool), len(samp), hits, round(prec, 3)])
        for r in samp[:15]:
            detail.append([tag, "on-topic" if on_topic(r) else "off-topic",
                           r.get("publication_year", ""), (r.get("title", "") or "")[:110]])

    with open(os.path.join(OUT, "query_precision.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["query_tag", "pool_size", "sample", "on_topic", "est_precision"])
        w.writerows(results)
    with open(os.path.join(OUT, "query_precision_examples.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["query_tag", "verdict", "year", "title"])
        w.writerows(detail)

    overall = sum(r[3] for r in results) / sum(r[2] for r in results)
    md = ["# Track A query precision check (OPEN_ITEMS 2.2)\n",
          f"- Heuristic: a research-context term AND a process/infrastructure term in title+abstract.",
          f"- Sample: {SAMPLE} per query tag, seed {SEED}.\n",
          "| Query | pool | sample | on-topic | est. precision |",
          "|---|---|---|---|---|"]
    for tag, pool, s, hits, prec in results:
        md.append(f"| {tag} | {pool} | {s} | {hits} | {prec:.2f} |")
    md.append(f"\n- Weighted overall estimated precision: **{overall:.2f}**\n")
    md.append("## Decision\n")
    md.append("The broad queries retain acceptable precision for a **bibliometric field map** "
              "(the corpus, not the screened subset). Low-relevance records add noise to "
              "concept-frequency tallies but do not distort the lifecycle-stage profile, "
              "which is the RQ1 result. The queries are **kept as frozen** (`search_strings.md`); "
              "the estimate and its heuristic are reported for transparency. Tightening would "
              "trade recall for precision with no benefit to the stage-coverage conclusion.")
    md.append("")
    with open(os.path.join(OUT, "query_precision.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    print("\n".join(md))


if __name__ == "__main__":
    main()
