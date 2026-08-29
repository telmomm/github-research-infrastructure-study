#!/usr/bin/env python3
"""Descriptive summaries of the Track B evidence base.

Reads the versioned CSVs under literature/ and writes summary tables to results/.
Standard library only.
"""

import csv
import os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LIT = os.path.join(ROOT, "literature")
OUT = os.path.join(ROOT, "results")


def read(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def write_counter(name, counter, key_header):
    os.makedirs(OUT, exist_ok=True)
    rows = sorted(counter.items(), key=lambda kv: (str(kv[0])))
    with open(os.path.join(OUT, name), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow([key_header, "count"])
        for k, v in rows:
            w.writerow([k, v])
    return rows


def main():
    studies = read(os.path.join(LIT, "included_studies.csv"))
    reqs = read(os.path.join(LIT, "requirements_extraction.csv"))
    life = read(os.path.join(LIT, "lifecycle_coverage.csv"))

    by_year = Counter(s["year"] for s in studies)
    by_strand = Counter(s["strand"] for s in studies)
    by_focus = Counter(s["lifecycle_focus"] for s in studies)
    by_relevance = Counter(s["relevance"] for s in studies)
    by_doctype = Counter(s["doc_type"] for s in studies)

    req_by_rm = Counter(r["rm_mapping"] for r in reqs)
    req_by_attention = Counter(r["literature_attention"] for r in reqs)
    life_by_attention = Counter(l["literature_attention"] for l in life)

    write_counter("tb_studies_by_year.csv", by_year, "year")
    write_counter("tb_studies_by_strand.csv", by_strand, "strand")
    write_counter("tb_studies_by_lifecycle_focus.csv", by_focus, "lifecycle_focus")
    write_counter("tb_studies_by_relevance.csv", by_relevance, "relevance")
    write_counter("tb_studies_by_doctype.csv", by_doctype, "doc_type")
    write_counter("tb_requirements_by_rm.csv", req_by_rm, "rm_mapping")
    write_counter("tb_requirements_by_attention.csv", req_by_attention, "literature_attention")
    write_counter("tb_lifecycle_by_attention.csv", life_by_attention, "literature_attention")

    md = []
    md.append("# Track B descriptive summary\n")
    md.append(f"- Studies (S01-S52): **{len(studies)}**")
    md.append(f"- Requirement rows (RE01-RE17): **{len(reqs)}**")
    md.append(f"- Lifecycle stages assessed: **{len(life)}**\n")
    md.append("## Studies by strand\n")
    for k, v in sorted(by_strand.items(), key=lambda kv: -kv[1]):
        md.append(f"- {k}: {v}")
    md.append("\n## Studies by lifecycle focus\n")
    for k, v in sorted(by_focus.items(), key=lambda kv: -kv[1]):
        md.append(f"- {k}: {v}")
    md.append("\n## Requirement rows by literature attention\n")
    for k, v in sorted(req_by_attention.items(), key=lambda kv: -kv[1]):
        md.append(f"- {k}: {v}")
    md.append("\n## Lifecycle stages by literature attention\n")
    for k, v in sorted(life_by_attention.items(), key=lambda kv: -kv[1]):
        md.append(f"- {k}: {v}")
    md.append("")

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "track_b_summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))

    print("\n".join(md))


if __name__ == "__main__":
    main()
