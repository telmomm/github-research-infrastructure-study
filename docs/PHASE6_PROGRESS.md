# Phase 6 — Reference Architecture

**Roadmap step:** 6 of 12 · **Answers:** RQ3 (constructive part) · **Method doc:** `REFERENCE_ARCHITECTURE.md` (draft, now superseded by the built artifact)
**Started / completed:** 2026-08-30 · **Status: COMPLETE (v1)**

Organises the Phase 5 Direct- and Partial-support capabilities into a named component set, a lifecycle model and concrete workflows, and fixes the conventions that lift RM1/RM2/RM5/RM10.

---

## Outputs (`framework/architecture/`)

| File | Content |
|---|---|
| `reference_architecture.md` | **Narrative deliverable.** Concept, layered conceptual architecture, components, lifting conventions, lifecycle model, 7 workflows, what stays outside GitHub, implementation principles, how it realises the Phase 5 scores |
| `architecture_components.csv` | **Canonical.** 15 components (A1–A4, B1–B4, C1–C3, D1–D3, X1): layer, github_basis, convention, requirements_served, lifecycle_stages, traceability_role |
| `workflows.csv` | 7 workflows (WF1–WF7): trigger, steps, components, requirements, traceability_link |
| `lifecycle_model.csv` | 12 stages → active components, primary artifacts, entry/exit links |
| `results/framework/arch_*.csv` + `architecture_summary.md` | Consistency checks + cross-tabs (`analysis/scripts/summarise_architecture.py`) |

## Architecture at a glance

- **15 components in 5 layers:** Coordination 4 (A1–A4) · Record 4 (B1–B4) · Production 3 (C1–C3) · Release 3 (D1–D3) · Cross-cutting 1 (X1).
- **B3 Linkage Discipline is the keystone** — a mandatory practice (cross-references + closing keywords + timeline), not a feature; without it RM10 collapses to Limited.
- **7 workflows** WF1–WF7: register a research question, execute a task, record a decision, peer-review an artifact, release & archive, reproducibility check, onboard/hand over.
- **Lifecycle model** shifts active components A4→A3→A1 (coordination) → B*/C* (record + production) → D* (release), with B3 and B4 active throughout; the end-to-end traceability path RQ → task → commits → PR → result → manuscript → release → DOI is realised.

## Consistency (all pass)

- Every RM1–RM15 served by ≥1 component; no idle component.
- All workflow and lifecycle component references resolve.

## The four lifting conventions (Phase 5 handoff)

| RM | Convention (component) |
|---|---|
| RM1 (Partial) | Phased-plan convention (A1) |
| RM2 (Limited) | Question Register convention (A3) + Linkage discipline (B3) |
| RM5 (Partial) | Decision-record convention (B2) + deliberation in A4 |
| RM10 (Partial) | Linkage-discipline convention (B3) |

## Decisions logged

- `DECISION_LOG.md` D12 — 15-component / 5-layer structure, B3 as keystone, the four named conventions as part of the architecture, boundary rule (hold a reference, not the artifact, at external-tool boundaries).

## Handoff to Phase 7

Operationalise as the reusable GitHub Research Project Template (`template/`): repo skeleton (C1), issue/PR templates (A2, B2, C2), label set + Project field definitions (A1, A2), starter Actions (C3), CITATION.cff + release checklist (D1), CONTRIBUTING + roles (D3), a `docs/` set pre-seeded with the §4 conventions.

## Open / optional — closed 2026-08-30 (see `docs/OPEN_ITEMS.md`)

- Figures 3 & 4 — **done**: `manuscript/figures/fig3_architecture.svg` (5-layer architecture), `fig4_traceability.svg` (end-to-end path).
- Lifecycle-model sanity check — **done** in Phase 8 (`case-study/traceability_examples.md`, `implementation_record.csv`).
