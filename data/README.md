# Data

Datasets for the study. Structure follows `docs/PHASE1_PROJECT_DEFINITION.md` §10.

| Path | Content | Status |
|---|---|---|
| `raw/openalex/` | OpenAlex API export as retrieved (`works_YYYYMMDD.{jsonl,csv}`). Track A primary source. | `works_20260830.*` — 5,936 works · `.gitignore`d |
| `raw/arxiv/` | arXiv API export (version-control / research-software strand). | `works_20260830.csv` — 462 preprints · `.gitignore`d |
| `raw/wos/` | Web of Science record exports, Q1–Q4, ≤1,000-row tab-delimited batches. **Coverage cross-check only** (not merged into the corpus). | `Q*_20260930/` — 9,441 records · `.gitignore`d |
| `raw/scopus/` | Scopus CSV exports, Q1–Q4. Coverage cross-check only. | `Q*_20260930.csv` — 8,809 records · `.gitignore`d |
| `raw/manual/` | Google Scholar spot-check additions (`*.csv`, `source=GS`). | none |
| `raw/exclude_sources.txt` | Source-name substrings dropped as data/software-repository deposits. | active |
| `processed/corpus.csv` | De-duplicated, cleaned Track A corpus (one row per work). | **5,139 works** (OpenAlex + arXiv) |
| `processed/dedup_report.md` | Counts at each de-duplication / exclusion step. | generated |
| `processed/corpus_enrichment.csv` | Crossref DOI/citation matches for no-DOI corpus records (side table). | generated |

Regenerate with `analysis/scripts/{fetch_openalex,fetch_arxiv,build_corpus,bibliometrics_track_a}.py` (see `analysis/README.md`).

## Track B

The Track B evidence base is versioned under `literature/`, not here (`included_studies.csv` S01–S52, `included_studies_primary.csv` S53–S67, `requirements_extraction.csv` RE01–RE17, `lifecycle_coverage.csv`, `references.bib`). Normalised from `SOTA/SOTA.md` (Consensus Deep Search).

## Raw retrieval exports → Zenodo

The `raw/{openalex,arxiv,wos,scopus}/` dumps are **not in git** — they are large and fully
regenerable from the frozen queries in `literature/search_strings.md` plus the retrieval
dates in `literature/search_log.md`. They are archived in a **companion Zenodo dataset
record**, separate from the auto-generated GitHub–Zenodo *software* record so it is not
overwritten by later releases:

- **Dataset record:** <https://doi.org/10.5281/zenodo.22173525> — Track A datasets and raw
  retrieval exports (OpenAlex, arXiv, WoS, Scopus). `isSupplementTo` the software record.
- **Software record:** <https://doi.org/10.5281/zenodo.22167500> — the repository at release.

Rebuild the bundle before re-depositing:

```
mkdir -p dist && cd data/raw && \
zip -rq -X ../../dist/track_a_raw_exports_$(date +%Y%m%d).zip \
    openalex arxiv wos scopus exclude_sources.txt && cd -
```

## Deposit (what goes to the dataset record)

- `processed/corpus.csv`, `processed/dedup_report.md`, `processed/corpus_enrichment.csv`
- `literature/*.csv`, `literature/references.bib`
- `dist/track_a_raw_exports_<date>.zip` (raw OpenAlex / arXiv / WoS / Scopus exports)

Both DOIs go in the manuscript's data-availability statement (code = software DOI,
data = dataset DOI). This connects to the prior GitHub–Zenodo–ORCID workflow.
