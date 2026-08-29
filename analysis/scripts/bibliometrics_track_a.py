#!/usr/bin/env python3
"""Track A bibliometric descriptives (RQ1) — zero-dependency version.

Input : data/processed/corpus.csv   (from build_corpus.py)
Output: results/track_a/*.csv  + results/track_a/track_a_summary.md

Produces everything RQ1 needs without R: annual production, top sources,
country distribution, concept/topic/keyword frequencies, a research-lifecycle
stage-hit profile (to compare against literature/lifecycle_coverage.csv), and a
keyword co-occurrence edge list that VOSviewer or Gephi can render as a map.

The R script (bibliometrics_track_a.R) is the option for publication-quality
thematic maps once an R + bibliometrix stack is available.
"""

import csv
import itertools
import os
import re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CORPUS = os.path.join(ROOT, "data", "processed", "corpus.csv")
OUT = os.path.join(ROOT, "results", "track_a")

STOP_KW = {
    "", "research", "science", "scientific", "study", "analysis", "data", "method",
    "methods", "approach", "system", "systems", "model", "models", "using", "based",
}

# research-lifecycle stage lexicon (lowercase substring match over concepts + abstract)
STAGE_LEX = {
    "idea_question": ["research question", "hypothesis", "ideation", "problem formulation"],
    "planning": ["project management", "research planning", "grant", "proposal", "research design"],
    "literature": ["systematic review", "literature review", "scoping review", "bibliometric"],
    "methods_protocol": ["protocol", "preregistration", "pre-registration", "study design", "methodology"],
    "data_management": ["research data management", "data curation", "data management", "fair data", "metadata"],
    "analysis_workflow": ["scientific workflow", "workflow management", "pipeline", "reproducib", "computational"],
    "provenance": ["provenance", "lineage", "traceability", "audit trail"],
    "dissemination": ["preprint", "repository", "open access", "scholarly communication", "publishing"],
    "outputs_identification": ["persistent identifier", "doi", "orcid", "research information system", "cris"],
    "coordination": ["collaboration", "coordination", "virtual research environment", "science gateway", "team science"],
    "governance": ["research policy", "governance", "sustainability", "funding model", "workforce"],
}


def read_corpus():
    with open(CORPUS, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def split_semi(s):
    return [x.strip() for x in re.split(r";\s*", s or "") if x.strip()]


def concept_names(cell):
    return [re.sub(r":[0-9.]+$", "", c).strip().lower() for c in split_semi(cell)]


def kw_list(row):
    out = []
    for c in split_semi(row.get("keywords", "")):
        c = c.lower().strip()
        if c and c not in STOP_KW and len(c) > 2:
            out.append(c)
    return sorted(set(out))


def write_counter(name, counter, key_header, top=None):
    os.makedirs(OUT, exist_ok=True)
    items = counter.most_common(top) if top else sorted(counter.items(), key=lambda kv: (-kv[1], str(kv[0])))
    with open(os.path.join(OUT, name), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow([key_header, "count"])
        w.writerows(items)


def main():
    rows = read_corpus()
    n = len(rows)

    by_year = Counter(r["publication_year"] for r in rows if r.get("publication_year"))
    by_source = Counter(r["source"] for r in rows if r.get("source"))
    by_type = Counter(r["type"] for r in rows if r.get("type"))
    countries = Counter()
    for r in rows:
        countries.update(split_semi(r.get("countries", "")))
    concepts = Counter()
    topics = Counter()
    keywords = Counter()
    for r in rows:
        concepts.update(concept_names(r.get("concepts", "")))
        topics.update(x.lower() for x in split_semi(r.get("topics", "")))
        keywords.update(kw_list(r))

    # lifecycle stage hits
    stage_hits = []
    for stage, lex in STAGE_LEX.items():
        hits = 0
        for r in rows:
            hay = (r.get("concepts", "") + " " + r.get("abstract", "") + " " + r.get("topics", "")).lower()
            if any(term in hay for term in lex):
                hits += 1
        stage_hits.append((stage, hits, round(100 * hits / n, 1)))

    # keyword co-occurrence edges (author keywords)
    pair_counts = Counter()
    node_counts = Counter()
    for r in rows:
        ks = kw_list(r)
        node_counts.update(ks)
        for a, b in itertools.combinations(sorted(ks), 2):
            pair_counts[(a, b)] += 1
    MIN_EDGE = 3
    MIN_NODE = 5

    os.makedirs(OUT, exist_ok=True)
    write_counter("annual_production.csv", by_year, "publication_year")
    write_counter("top_sources.csv", by_source, "source", top=60)
    write_counter("doc_types.csv", by_type, "type")
    write_counter("countries.csv", countries, "country", top=60)
    write_counter("top_concepts.csv", concepts, "concept", top=80)
    write_counter("top_topics.csv", topics, "topic", top=60)
    write_counter("top_keywords.csv", keywords, "keyword", top=100)

    with open(os.path.join(OUT, "lifecycle_stage_hits.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["stage", "n_works", "pct_of_corpus"])
        w.writerows(sorted(stage_hits, key=lambda x: -x[1]))

    with open(os.path.join(OUT, "coword_nodes.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "label", "weight"])
        for k, c in node_counts.most_common():
            if c >= MIN_NODE:
                w.writerow([k, k, c])

    with open(os.path.join(OUT, "coword_edges.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["source", "target", "weight"])
        for (a, b), c in pair_counts.most_common():
            if c >= MIN_EDGE and node_counts[a] >= MIN_NODE and node_counts[b] >= MIN_NODE:
                w.writerow([a, b, c])

    md = ["# Track A — bibliometric descriptives\n",
          f"- Corpus: **{n}** works",
          f"- Years: {min(by_year)}–{max(by_year)}",
          f"- Distinct sources: {len(by_source)}",
          f"- Works with >=1 parsed country: {sum(1 for r in rows if r.get('countries'))}\n",
          "## Annual production\n"]
    for y in sorted(by_year):
        md.append(f"- {y}: {by_year[y]}")
    md.append("\n## Top 15 sources\n")
    for s, c in by_source.most_common(15):
        md.append(f"- {s}: {c}")
    md.append("\n## Top 15 countries\n")
    for s, c in countries.most_common(15):
        md.append(f"- {s}: {c}")
    md.append("\n## Lifecycle stage-hit profile (compare with literature/lifecycle_coverage.csv)\n")
    for stage, hits, pct in sorted(stage_hits, key=lambda x: -x[1]):
        md.append(f"- {stage}: {hits} ({pct}%)")
    md.append(f"\n## Co-word map inputs\n- nodes (kw freq >= {MIN_NODE}): see coword_nodes.csv"
              f"\n- edges (co-occ >= {MIN_EDGE}): see coword_edges.csv"
              "\n- load both into VOSviewer (Create > Map from network data) or Gephi")
    md.append("")
    with open(os.path.join(OUT, "track_a_summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    print("\n".join(md))


if __name__ == "__main__":
    main()
