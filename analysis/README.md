# Analysis

Scripts that regenerate the study's tables and figures from the versioned datasets.

## Track B (evidence review)

| Script | Input | Output |
|---|---|---|
| `scripts/summarise_track_b.py` | `literature/*.csv` | `results/tb_*.csv`, `results/track_b_summary.md` |

## Track A (bibliometric corpus, open sources — `DECISION_LOG.md` D8)

Run in order:

| # | Script | Does |
|---|---|---|
| 1 | `scripts/fetch_openalex.py --mailto <email>` | Fetch the primary corpus from the OpenAlex API (15 frozen queries) → `data/raw/openalex/works_<date>.{jsonl,csv}`. `--dry-run` prints counts only. |
| 2 | `scripts/fetch_arxiv.py` | Supplement: arXiv preprints for the version-control / GitHub strand → `data/raw/arxiv/works_<date>.csv`. |
| 3 | `scripts/build_corpus.py` | Merge all `data/raw/` sources, drop repository deposits (`data/raw/exclude_sources.txt`), de-duplicate (DOI → title+year) → `data/processed/corpus.csv`, `data/processed/dedup_report.md`. |
| 4 | `scripts/bibliometrics_track_a.py` | Zero-dependency descriptives → `results/track_a/*.csv`, `results/track_a/track_a_summary.md`, plus `coword_nodes.csv` / `coword_edges.csv` for VOSviewer / Gephi. |
| 4′ | `scripts/bibliometrics_track_a.R` | Optional: `bibliometrix` thematic maps and co-word networks. Needs `install.packages(c("bibliometrix","readr","dplyr","stringr","tidyr","ggplot2"))`. |

Steps 1–4 are standard-library Python 3 only. Manual Google Scholar spot-check additions go in `data/raw/manual/*.csv` (columns: `title,doi,publication_year,source`; `source=GS`) and are picked up by step 3.

## Running

```
python3 analysis/scripts/summarise_track_b.py
python3 analysis/scripts/fetch_openalex.py --mailto you@example.org
python3 analysis/scripts/build_corpus.py
python3 analysis/scripts/bibliometrics_track_a.py
```
