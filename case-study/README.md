# Case Study — Self-Referential Implementation

**Phase 8 deliverable** (roadmap step 8 of 12) · Feeds **RQ5**
**Approach:** self-referential + reusable template (`DECISION_LOG.md` D5)
**Protocol:** `docs/CASE_STUDY.md` · **Decisions:** `DECISION_LOG.md` D14

---

## 1. What the case study is

The framework is applied to the development of **this study itself**. The repository is both the research workspace and the empirical evidence for RQ5. There is no second project; the reusable template (`template/`) is the transferable artifact evaluated alongside.

## 2. Honest scope

Phases 1–7 were executed as a **single-author working sprint**. As a result:

- **Strongly realised natively:** the Record layer (B1 Documentation Set, B2 Decision Log), the Artifact Workspace (C1), the plan of record (A1), and Change History (B4) — see `implementation_record.csv`.
- **Specified and configured, not exercised:** the Issue/Project coordination (A2, A3 as GitHub objects), the Review Workflow (C2), GitHub Actions runs (C3), Releases (D1), the Zenodo bridge (D2), the public Transparency Surface (X1).
- **Reconstructed as a register:** `activity_register.csv` stands in for the Issues/Project the project would have had — 5 RQs, 8 milestones, 16 tasks, 14 decisions, with their links.

This substitution — file paths, decision ids and per-phase commits instead of Issue numbers, PRs and tags — is the case study's central limitation and exactly what Phase 9 evaluates.

## 3. Contents

| File | Content |
|---|---|
| `implementation_record.csv` | Per architecture component (A1–X1): status (native / config / retrospective / partial / planned), evidence, notes |
| `activity_register.csv` | Reconstructed RQ / milestone / task / decision register with links and evidence |
| `traceability_examples.md` | Four end-to-end chains through real artifacts |

## 4. Repository configuration added this phase (T16)

Applying `docs/CASE_STUDY.md` steps 1–4 to this repository:

- `.github/ISSUE_TEMPLATE/` (research-question, research-task, decision-record) + `config.yml`
- `.github/pull_request_template.md`
- `.github/labels.yml`, `.github/project-fields.md`
- `.github/workflows/validate-structure.yml` (adapted to this repo's layout)
- `docs/conventions.md` — the four conventions, as followed here
- `CONTRIBUTING.md`, `LICENSE` (placeholder)

## 5. What the case study shows so far

- The framework's **document / decision / version-control spine works and is low-friction**: 23 `docs/` files, 14 logged decisions, 10 regenerating scripts, a full plan of record — all produced without any coordination overhead.
- Document-level **linkage discipline is sustainable** and machine-checkable (the `summarise_*` scripts verify RE→RM→GC→component references).
- The **Issue/Project/PR overhead was not adopted under solo-sprint conditions** — an informative negative result about where the framework's cost falls.

Full evaluation against requirement coverage, traceability, documentation, organization, transparency and usability is Phase 9.

## 6. Handoff to Phase 9

Score the six evaluation dimensions (`docs/EVALUATION_PROTOCOL.md`) using `implementation_record.csv` and `activity_register.csv` as evidence, and build the fragmented-workflow comparison (Table 6).
