# {{PROJECT_NAME}}

> One-sentence description of the research project.

A GitHub-based research project managed with the **GitHub Research Project Template** — an operationalisation of a literature-derived research-management reference architecture. GitHub is used here as a coordination, documentation and traceability layer for the research process, not as a store for large data or a replacement for specialised infrastructure.

## How this repository is organised

| Path | Contents |
|---|---|
| `docs/` | Project charter, protocol, methodology, **roadmap (plan of record)**, **decision log**, and **`conventions.md`** — read that first |
| `literature/` | Search strategy, screening, references |
| `data/` | `raw/`, `processed/`, and `external/` (pointers to large data held elsewhere) |
| `analysis/` | Scripts, notebooks, generated results |
| `manuscript/` | Manuscript sources, figures, tables |
| `outputs/` | Released datasets, software, reports |
| `.github/` | Issue forms, PR template, label set, Project field definitions, starter workflows, release checklist |

## Working conventions (mandatory)

This template only works if four conventions are followed — see [`docs/conventions.md`](docs/conventions.md):

1. **Phased plan** — every work item has a *Research phase* and a milestone; `docs/roadmap.md` is the plan of record.
2. **Question register** — one issue per research question (`RQ-n: …`), pinned index; downstream work references its RQ.
3. **Decision record** — every significant decision gets a `docs/decision-log.md` entry *and* a `decision` issue linked to the artifacts it affects.
4. **Linkage discipline** — every commit names its issue; every PR uses `Closes #`; every issue names its RQ and milestone.

## Getting started

1. Create a repository from this template (`Use this template`).
2. Replace every `{{PLACEHOLDER}}` in `README.md`, `CITATION.cff`, `docs/project-charter.md`.
3. Create a Project (v2) and add the fields in [`.github/project-fields.md`](.github/project-fields.md).
4. Apply the label set in [`.github/labels.yml`](.github/labels.yml).
5. Fill `docs/project-charter.md`, then open your first `RQ-1` issue.
6. Enable the GitHub–Zenodo integration before your first release (see [`.github/release-checklist.md`](.github/release-checklist.md)).

## Reuse

This template is discipline-independent. The adaptation points are the label set, the Project fields, and the Issue Types — the folder layout, workflows and linkage rules stay as they are.
