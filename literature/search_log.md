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

## Scopus / Web of Science — cross-check, run 2026-09-30

Retrieved via FECYT institutional access as an independent coverage cross-check of the
OpenAlex + arXiv corpus (not merged into it). Strings frozen in `search_strings.md`
(WoS `TS=`; Scopus `TITLE-ABS-KEY` with `DOCTYPE(ar|re|cp)`), window 2008–2025.

| Query | Web of Science | Scopus |
|---|---|---|
| Q1 core process management        | 1,060 | 2,273 |
| Q2 data mgmt / open science       | 3,301 | 3,063 |
| Q3 version control in research    | 4,812 | 2,986 |
| Q4 research environments / RIS    |   268 |   487 |
| **raw total** | **9,441** | **8,809** |

Combined raw 18,250 → **13,586** de-duplicated in-window records (338 outside 2008–2025 dropped).
WoS exported record-level tab-delimited "Full Record" in ≤1,000-row batches under
`data/raw/wos/Q*/`; Scopus CSV (Citation + Bibliographical) under `data/raw/scopus/Q*.csv`.
Raw exports are `.gitignore`d. Analysis: `analysis/scripts/scopus_wos_crosscheck.py`;
result: `results/track_a/scopus_wos_crosscheck.md` (**22% DOI overlap** with the corpus;
`DECISION_LOG.md` D24).

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
