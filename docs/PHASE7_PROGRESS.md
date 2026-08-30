# Phase 7 — Reusable Template

**Roadmap step:** 7 of 12 · **Method doc:** `TEMPLATE_PROJECT.md` (draft, now superseded)
**Started / completed:** 2026-08-30 · **Status: COMPLETE (v1)**

Operationalises the Phase 6 reference architecture as a ready-to-use GitHub template.

---

## Outputs (`template/`)

| Path | Content |
|---|---|
| `github-research-project-template/` | **The template** — 33 files: repo skeleton, `docs/` set (charter, protocol, methodology, roadmap = plan of record, decision log, **conventions.md**, glossary), issue forms (research-question, research-task, decision-record), PR template with reproducibility checklist, `labels.yml`, `project-fields.md`, `release-checklist.md`, 3 starter Actions (`validate-structure`, `markdown-link-check`, `reproduce`) |
| `template_manifest.csv` | **Canonical.** 33 files → architecture component(s) → requirement(s) → purpose |
| `template/README.md` | What the template is; the two-repository strategy; coverage |
| `results/framework/template_coverage.csv` + `template_summary.md` | Consistency check (`analysis/scripts/check_template.py`) |

## Consistency (all pass)

- 33 manifest files all present on disk; no unlisted files.
- Every architecture component covered by ≥1 template file, except A1, A2, D2, X1 which are GitHub **configuration** (Project fields/board → `project-fields.md`; Zenodo webhook → `release-checklist.md`; public visibility → governance decision).
- Every requirement RM1–RM15 touched by ≥1 template file.

## What the template contributes over a bare repo

The four conventions from the architecture, made concrete and enforceable:

| Convention | Template mechanism |
|---|---|
| Phased plan (A1) | `docs/roadmap.md` as plan of record + fixed phase vocabulary in `project-fields.md` + `validate-structure` |
| Question register (A3) | `research-question.yml` issue form (`RQ-n:` title, `research-question` label) + pinned index convention |
| Decision record (B2) | `decision-record.yml` form + `docs/decision-log.md` `Dn` format + PR checklist item |
| Linkage discipline (B3) | `CONTRIBUTING.md` rules + `pull_request_template.md` (`Closes #`) + commit-message format |

## Design principles honoured

Discipline-independent core (layout, workflows, linkage rules fixed; labels / Project fields / Issue Types are the adaptation points); minimal viable configuration; native-first; large data excluded by `.gitignore` and `data/external/` pointers; everything regenerable.

## Decisions logged

- `DECISION_LOG.md` D13 — 33-file template; config-only components (A1, A2, D2, X1); two-repository strategy (extract at Phase 12); starter Actions kept generic with adaptation notes.

## Handoff to Phase 8

Case study: apply the framework to a real project. Recommended (D5): self-referential + the template as a transferable artifact. Check the lifecycle model and conventions against this repository's own history; then instantiate the template for a second, independent project if feasible.

## Open / optional — closed 2026-08-30 (see `docs/OPEN_ITEMS.md`)

- `LICENSES/` REUSE directory — **done**: `LICENSES/{MIT,CC-BY-4.0,CC0-1.0}.txt` + `REUSE.toml` in the template and this repo; root `LICENSE` explains the split.
- `label-sync` workflow — **done**: `.github/workflows/label-sync.yml` (template + this repo).
- Project screenshot — **user-task** (needs a live GitHub Project; before submission).
