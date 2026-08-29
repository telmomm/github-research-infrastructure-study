# Data

Datasets for the study. Structure follows `docs/PHASE1_PROJECT_DEFINITION.md` §10.

| Path | Content | Status |
|---|---|---|
| `raw/openalex/` | OpenAlex API export as retrieved (`works_YYYYMMDD.jsonl` + `.csv`). Track A primary source. | `works_20260830.*` — 5,936 works |
| `raw/arxiv/` | arXiv API export (version-control / GitHub strand). | not yet run |
| `raw/manual/` | Google Scholar spot-check additions (`*.csv`, `source=GS`). | none yet |
| `raw/exclude_sources.txt` | Source-name substrings dropped as data/software-repository deposits. | active |
| `processed/corpus.csv` | De-duplicated, cleaned Track A corpus (one row per work). | 4,713 works |
| `processed/dedup_report.md` | Counts at each de-duplication / exclusion step. | generated |

Regenerate with `analysis/scripts/{fetch_openalex,build_corpus,bibliometrics_track_a}.py` (see `analysis/README.md`).

## Track B (completed)

The Track B evidence base is versioned under `literature/`, not here:

- `literature/included_studies.csv` — 52 studies (S01-S52)
- `literature/requirements_extraction.csv` — 17 requirement rows (RE01-RE17)
- `literature/lifecycle_coverage.csv` — 15 lifecycle stages
- `literature/references.bib` — BibTeX for S01-S52

## Provenance

Track B is normalised from `SOTA/SOTA.md` (Consensus Deep Search synthesis). Track A will produce an independent corpus from Scopus + Web of Science; see `literature/search_strategy.md` Part B.

## Deposit

`processed/` datasets, `literature/*.csv` and `literature/references.bib` are prepared for deposit on Zenodo/OSF with the manuscript's data-availability statement (connects to the prior GitHub-Zenodo-ORCID workflow).
