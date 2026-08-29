# Contributing

This repository is a managed research project and also the case study for the framework it
develops. Follow the four conventions in [`docs/conventions.md`](docs/conventions.md).

## Roles

Currently single-author (PI = admin). When collaborators join: `write` for contributors,
`triage` for reviewers, `read` public at publication (Phase 12).

## Workflow

1. Work is tracked in [`case-study/activity_register.csv`](case-study/activity_register.csv)
   (RQ / milestone / task / decision). Add a row before starting substantial work.
2. Significant choices go in [`docs/DECISION_LOG.md`](docs/DECISION_LOG.md) as `Dn` with an **Affects** line.
3. Each phase closes with a `docs/PHASEn_PROGRESS.md` and a `CHANGELOG.md` entry.
4. Commit per phase (`Phase n`) or per coherent change; keep `analysis/scripts/` the single
   source of every table in `results/`.
5. Regenerate cross-tabs before committing framework changes:
   `for s in analysis/scripts/summarise_*.py analysis/scripts/coverage_indicators.py analysis/scripts/check_template.py; do python3 "$s"; done`

## Large files

No large datasets in Git. Raw API dumps are `.gitignore`d; keep the reproducible
`data/processed/corpus.csv` and pointers only.
