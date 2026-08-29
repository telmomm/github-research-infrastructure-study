# Track A — Search Log

Strings frozen in `search_strings.md`. Primary source: OpenAlex (open, reproducible). See `DECISION_LOG.md` D8.

## OpenAlex — run 2026-08-30

Fetched with `analysis/scripts/fetch_openalex.py --mailto tmiguel@ubu.es`. Per-query result counts (OpenAlex `meta.count`, with overlap between queries):

| Query | Count | Query | Count |
|---|---|---|---|
| Q1a `"research project management" …` | 266 | Q2b `"open science" …` | 2131 |
| Q1b `"research workflow management"` | 4 | Q2c `"reproducible research" …` | 287 |
| Q1c `"research workflow" …` | 215 | Q3a `github …` | 1148 |
| Q1d `"research lifecycle" …` | 185 | Q3b `"version control" …` | 366 |
| Q1e `"research life cycle" …` | 87 | Q4a `"virtual research environment" …` | 74 |
| Q1f `"research process management"` | 19 | Q4b `"science gateway" …` | 87 |
| Q1g `"scientific workflow" …` | 651 | Q4c `"research information system" …` | 66 |
| Q2a `"research data management" …` | 926 | **sum (with overlap)** | **6512** |

Export: `data/raw/openalex/works_20260830.jsonl` + `works_20260830.csv` — **5,936 unique works**.

## arXiv — run 2026-08-30

`analysis/scripts/fetch_arxiv.py` (A1–A5), abstract/title-scoped, category-filtered for A2. Supplement for the version-control / research-software strand.

| Query | In-window results |
|---|---|
| A1 `abs:"version control" …` | 124 |
| A2 `(ti:github OR abs:github) … AND cat:(cs.DL/SE/CY/DC)` | 133 |
| A3 `abs:"scientific workflow" …` | 108 |
| A4 `abs:"research software" …` | 87 |
| A5 `abs:"reproducible research" …` | 52 |
| **unique preprints** | **462** |

Export: `data/raw/arxiv/works_20260830.csv`. (First attempt used broad `all:` fields — A2 hit the 2000 cap with mostly repo-link noise — and was discarded; queries tightened, see `search_strings.md`.)

## Scopus / Web of Science — not run

Optional cross-check only (no subscription used). Strings in `search_strings.md`.

## Google Scholar — spot checks

Manual, first ~100 results per phrasing; add only clearly-relevant items missing from the corpus, into `data/raw/manual/gs_<date>.csv` with `source=GS`. Not counted in database-recall figures.

| Date | Query | Items added | File |
|---|---|---|---|
| — | — | — | — |

---

## De-duplication (`analysis/scripts/build_corpus.py`, 2026-08-30, OpenAlex + arXiv)

| Step | Records |
|---|---|
| Input rows (OpenAlex 5,936 + arXiv 462) | 6,398 |
| Removed as data/software-repository deposits (`exclude_sources.txt`: Zenodo, Figshare, …) | 1,167 |
| Removed as duplicate DOI | 29 |
| Removed as duplicate title+year (no DOI) | 9 |
| Removed as no-DOI row matching a DOI row on title+year | 31 |
| **Corpus** (`data/processed/corpus.csv`) | **5,139** |

By source: OpenAlex 4,689 · arXiv 426 · both 24. See `data/processed/dedup_report.md` for the by-year breakdown.

## PRISMA 2020 counts (corpus → screened subset)

Only needed if the requirement extraction is expanded beyond the current Track B set (RE01–RE17). To be filled if/when the deep screen is run.

| Stage | n |
|---|---|
| Records identified (corpus) | 5,139 |
| Records screened (title/abstract) | — |
| Records excluded | — |
| Full-text assessed | — |
| Full-text excluded (with reasons) | — |
| Studies included (screened subset) | — |
