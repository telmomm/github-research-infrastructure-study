# Phase 8 — Case Study

**Roadmap step:** 8 of 12 · **Feeds:** RQ5 · **Protocol:** `CASE_STUDY.md`
**Started / completed:** 2026-08-30 · **Status: COMPLETE (v1)**

Self-referential implementation (`DECISION_LOG.md` D5): the framework is applied to the development of this study; the repository is the evidence.

---

## Outputs (`case-study/`)

| File | Content |
|---|---|
| `implementation_record.csv` | Per architecture component A1–X1: status (native / partial / config / retrospective / planned), evidence (paths, decisions, commits), notes |
| `activity_register.csv` | Reconstructed register — 5 RQs, 8 milestones, 16 tasks, 14 decisions — with links and evidence (stands in for GitHub Issues) |
| `traceability_examples.md` | Four end-to-end chains through real artifacts |
| `README.md` | Approach, honest scope, contents, what it shows |

## Repository configuration added this phase (task T16)

- `.github/ISSUE_TEMPLATE/` (research-question, research-task, decision-record) + `config.yml`
- `.github/pull_request_template.md`, `.github/labels.yml`, `.github/project-fields.md`, `.github/mlc-config.json`, `.github/release-checklist.md`
- `.github/workflows/validate-structure.yml` (adapted: checks this repo's layout + that all `analysis/scripts/summarise_*` regenerate), `.github/workflows/markdown-link-check.yml`
- `docs/conventions.md` — the four conventions as applied here; `docs/glossary.md`
- `README.md` companions at root: `CITATION.cff`, `CONTRIBUTING.md`, `LICENSE` (placeholder)

The repository's root and `.github/` inventory now mirrors the template (bar `reproduce.yml`, whose role — re-running the analysis — is filled by `validate-structure.yml` running the script battery).

## Implementation status (`analysis/scripts/summarise_case_study.py`)

| Status | Components |
|---|---|
| **native** (working via a native mechanism) | A1 plan of record, A3 RQ set, B1 documentation, B2 decision log, B4 git history, C1 artifact workspace |
| **partial** | B3 linkage discipline (document-level, machine-checked; no commit→issue links), C3 automation (10 regenerating scripts, no Actions runs) |
| **config** (added, not exercised) | C2 review workflow, D1 release process (CHANGELOG + CITATION.cff + checklist; no tags yet), D3 governance |
| **retrospective** | A2 activity tracker → `activity_register.csv` |
| **planned** (Phase 12) | A4 Discussions, D2 Zenodo bridge, X1 public transparency surface |

**8 of 15 components exercised.** Requirements with no exercised component: RM6, RM7, RM14, RM15 — consistent with a single-author sprint and no releases yet.

## Central finding (feeds RQ5)

- The framework's **document / decision / version-control spine works with essentially zero coordination overhead**: 23 `docs/` files, 14 logged decisions, 10 regenerating scripts, a full plan of record.
- **Document-level linkage discipline is sustainable and machine-checkable** — the `summarise_*` scripts verify RE→RM→GC→component references resolve.
- The **Issue / Project / Pull Request layer was not adopted under solo-sprint conditions** (`DECISION_LOG.md` D14) — an informative negative result: the framework's cost concentrates in the coordination layer, which pays off with collaborators and is optional for a solo author.

## Consistency checks (all pass)

15/15 components recorded; 43/43 register items with resolving links; every milestone has ≥1 task; every `serves_rq` resolves.

## Decisions logged

- `DECISION_LOG.md` D14 — case study executed self-referentially; Issue/Project/PR layer specified and configured but not exercised; consequences declared as the study's main practical limitation.

## Handoff to Phase 9

Evaluate the six dimensions (`EVALUATION_PROTOCOL.md`) using `implementation_record.csv` and `activity_register.csv` as evidence; build the conventional-vs-GitHub comparison (Table 6). The un-exercised components (RM6, RM7, RM14, RM15) are scored on *design support*, not observed use, and flagged.

## Open / optional

- [ ] If time allows before submission: run one real cycle (Issue → branch → PR → review → merge → Release) for a small task, to demonstrate the coordination layer in practice.
- [ ] Instantiate the template for an unrelated second project (external validity) — future work otherwise.
