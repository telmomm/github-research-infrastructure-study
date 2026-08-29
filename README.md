# From Code Repository to Research Infrastructure

**Evaluating GitHub for Managing the Scientific Research Lifecycle**

A hybrid bibliometric + coverage-analysis study, targeted at *Scientometrics* (Springer Nature). It maps the literature on digital infrastructure for research-process management, derives a lifecycle-structured set of research management requirements, measures how far GitHub's native functionalities cover them, and consolidates the covered functionalities into a reusable reference architecture and project template tested self-referentially on this repository.

## Repository structure

| Path | Contents |
|---|---|
| `docs/` | Research design, protocols, decisions. Start at [`docs/PHASE1_PROJECT_DEFINITION.md`](docs/PHASE1_PROJECT_DEFINITION.md) (authoritative) and [`docs/PHASE2_PROGRESS.md`](docs/PHASE2_PROGRESS.md). |
| `SOTA/` | `SOTA.md` — Consensus Deep Search synthesis; the Track B literature evidence base. |
| `literature/` | Search strategy, screening notes, included studies (S01–S52), requirement extraction (RE01–RE17), lifecycle coverage, `references.bib`. |
| `data/` | `raw/` and `processed/` bibliographic datasets (Track A, pending). |
| `analysis/` | Scripts regenerating tables and figures from the datasets. |
| `results/` | Generated summary tables. |
| `manuscript/` | Paper sections, `figures/`, `tables/`. |
| [`CHANGELOG.md`](CHANGELOG.md) | Chronological record of changes, by roadmap release point. |

## Research questions

- **RQ1** How has the literature on research-process infrastructure evolved, and which lifecycle stages are under-represented?
- **RQ2** What research management requirements can be derived from it?
- **RQ3** To what extent do GitHub's native functionalities cover those requirements, across the lifecycle?
- **RQ4** How can the covered functionalities be organised into a reusable architecture and template?
- **RQ5** What does a self-referential implementation reveal about feasibility and limitations versus a fragmented workflow?

## Status

Phase 1 (project definition) complete. Phase 2 (literature analysis): Track B (structured evidence review) complete; Track A (OpenAlex + arXiv bibliometric corpus, 5,139 works) first run done, analysis refinement open. Phase 3 (requirements framework) next. See [`docs/ROADMAP.md`](docs/ROADMAP.md) and [`docs/PHASE2_PROGRESS.md`](docs/PHASE2_PROGRESS.md).

## Related work

Complements the prior [GitHub–Zenodo–ORCID reproducibility workflow](https://github.com/telmomm/github-zenodo-orcid-reproducibility-workflow): that study covers preservation of research *outputs*; this one covers management of the research *process*.
