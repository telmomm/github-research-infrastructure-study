# Analysis

Scripts that regenerate the study's tables and figures from the versioned datasets.

## Track B (evidence review)

| Script | Input | Output |
|---|---|---|
| `scripts/summarise_track_b.py` | `literature/*.csv` | `results/tb_*.csv`, `results/track_b_summary.md` |

## Framework (Phases 3–4)

| Script | Input | Output |
|---|---|---|
| `scripts/summarise_requirements.py` | `framework/requirements/*.csv` | `results/framework/rm_*.csv`, `requirements_summary.md` |
| `scripts/summarise_capabilities.py` | `framework/mapping/github_capability_catalogue.csv` + `framework/requirements/requirements_framework.csv` | `results/framework/gc_*.csv`, `capability_summary.md` |
| `scripts/coverage_indicators.py` | `framework/mapping/requirement_feature_matrix.csv` + `framework/requirements/*.csv` | `results/framework/coverage_*.csv`, `coverage_summary.md` |
| `scripts/summarise_architecture.py` | `framework/architecture/*.csv` + `framework/mapping/` + `framework/requirements/` | `results/framework/arch_*.csv`, `architecture_summary.md` |
| `scripts/check_template.py` | `template/template_manifest.csv` + `template/github-research-project-template/` + `framework/architecture/` | `results/framework/template_coverage.csv`, `template_summary.md` (exits non-zero on any gap) |
| `scripts/summarise_case_study.py` | `case-study/*.csv` + `framework/architecture/` + `framework/mapping/` | `results/framework/cs_*.csv`, `case_study_summary.md` (exits non-zero on a broken reference) |
| `scripts/evaluation_summary.py` | `case-study/evaluation_scores.csv` + `framework/mapping/requirement_feature_matrix.csv` | `results/framework/eval_*.csv`, `evaluation_summary.md` |
| `scripts/synthesis_check.py` | `analysis/findings.csv` | `results/framework/synthesis_*.csv`, `synthesis_summary.md` (exits non-zero on a missing evidence path) |
| `scripts/summarise_external_validity.py` | `case-study/external_validity_mapping.csv` | `results/framework/external_validity_summary.md` (RM1–RM15 status tally; exits non-zero on a missing RM row) |

## Phase 10 synthesis

`analysis/synthesis.md` (narrative) + `analysis/findings.csv` (32 findings F01–F32, typed and evidence-linked) integrate RQ1–RQ5 for the manuscript.

## Track A (bibliometric corpus, open sources — `DECISION_LOG.md` D8)

Run in order:

| # | Script | Does |
|---|---|---|
| 1 | `scripts/fetch_openalex.py --mailto <email>` | Fetch the primary corpus from the OpenAlex API (15 frozen queries) → `data/raw/openalex/works_<date>.{jsonl,csv}`. `--dry-run` prints counts only. |
| 2 | `scripts/fetch_arxiv.py` | Supplement: arXiv preprints for the version-control / GitHub strand → `data/raw/arxiv/works_<date>.csv`. |
| 3 | `scripts/build_corpus.py` | Merge all `data/raw/` sources, drop repository deposits (`data/raw/exclude_sources.txt`), de-duplicate (DOI → title+year) → `data/processed/corpus.csv`, `data/processed/dedup_report.md`. |
| 4 | `scripts/bibliometrics_track_a.py` | Zero-dependency descriptives → `results/track_a/*.csv`, `results/track_a/track_a_summary.md`, plus `coword_nodes.csv` / `coword_edges.csv` for VOSviewer / Gephi. |
| 4′ | `scripts/bibliometrics_track_a.R` | Optional: `bibliometrix` thematic maps and co-word networks. Needs `install.packages(c("bibliometrix","readr","dplyr","stringr","tidyr","ggplot2"))`. |
| 5 | `scripts/coword_map.py` | `results/track_a/coword_{nodes,edges}.csv` → `coword_map.gexf` (Gephi/VOSviewer) + `manuscript/figures/coword_map.svg`. |
| — | `scripts/query_precision_check.py` | Estimates precision of the broad OpenAlex queries → `results/track_a/query_precision.md`. One-shot. |
| — | `scripts/enrich_crossref.py --mailto <e>` | Crossref DOI/citation match for no-DOI corpus records → `data/processed/corpus_enrichment.csv`. One-shot, network. |
| — | `scripts/scopus_wos_crosscheck.py` | Coverage cross-check of the corpus against WoS (`data/raw/wos/**/*.txt`) + Scopus (`data/raw/scopus/**/*.csv`) exports → `results/track_a/scopus_wos_crosscheck.md`, `xref_not_in_corpus.csv.gz`. One-shot. |

Steps 1–4 are standard-library Python 3 only. Manual Google Scholar spot-check additions go in `data/raw/manual/*.csv` (columns: `title,doi,publication_year,source`; `source=GS`) and are picked up by step 3.

## Running

```
python3 analysis/scripts/summarise_track_b.py
python3 analysis/scripts/fetch_openalex.py --mailto you@example.org
python3 analysis/scripts/build_corpus.py
python3 analysis/scripts/bibliometrics_track_a.py
```
