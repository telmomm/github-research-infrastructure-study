# Phase 3 — Research Management Requirements Framework

**Roadmap step:** 3 of 12 · **Answers:** RQ2 · **Method doc:** `REQUIREMENTS_FRAMEWORKS.md`
**Started / completed:** 2026-08-30 · **Status: COMPLETE (v1)**

Develops the platform-independent set of requirements a system must support to manage a scientific research project across its lifecycle. Derived from the Phase 2 literature; the reference for Phases 4–6.

---

## Inputs

- `literature/requirements_extraction.csv` — 17 rows RE01–RE17 (challenge → need → requirement, provisional RM mapping).
- `literature/lifecycle_coverage.csv` — stage-level literature attention.
- `docs/REQUIREMENTS_FRAMEWORKS.md` — provisional domains RM1–RM14, attribute template.
- `literature/background_synthesis.md`, `results/track_a/` — corroboration only.

## Outputs (all under `framework/requirements/`)

| File | Content |
|---|---|
| `requirements_framework.csv` | **Canonical.** RM1–RM15: id, name, category, definition, expected_capabilities, lifecycle_stages, evidence_re, evidence_studies, literature_attention, importance, differentiator, relationships, known_limitations, github_support (empty until Phase 5) |
| `lifecycle_requirements_matrix.csv` | RM × 11 lifecycle stages, applicability 0–3 |
| `REQUIREMENTS_FRAMEWORK.md` | Narrative: method, the 15 requirements, classification, lifecycle mapping, relationship model, changes from the provisional set, RQ1 corroboration, handoff |
| `results/framework/*.csv` + `requirements_summary.md` | Cross-tabs from `analysis/scripts/summarise_requirements.py` |

## The framework at a glance

- **15 requirements** RM1–RM15.
- **Categories:** Traceability 4 (RM2, RM5, RM8, RM10) · Documentation 3 (RM4, RM11, RM12) · Collaboration 2 (RM6, RM7) · Planning / Execution / Artifact management / Automation / Output management 1 each · Cross-cutting 1 (RM15).
- **Importance:** High 8 · Medium-High 4 · Medium 2 · Low-Medium 1.
- **Differentiators** (High importance, weak literature attention): **RM1, RM2, RM5** — the upstream planning / question / decision gap the study targets.
- **Lifecycle load** peaks at analysis, data, manuscript, outputs; lowest at idea and question — but the framework retains strong upstream requirements there by design.

## Changes from provisional RM1–RM14

RM9 broadened to absorb tool integration (RE09); RM10 to absorb artifact linkage (RE11); RM14 to absorb PIDs / interoperable metadata (RE15). **RM15 (governance and sustainability)** added from RE17, flagged as only partly in scope. All definitions rewritten to be testable, each with an `expected_capabilities` field for Phase 5. Full list in `REQUIREMENTS_FRAMEWORK.md` §8.

## Decisions logged

- `DECISION_LOG.md` D9 — final requirement set RM1–RM15, additions and definition changes, differentiator flag.

## Handoff to Phase 4

Catalogue GitHub native functionalities against the `expected_capabilities` of RM1–RM15 → `framework/mapping/`. Then Phase 5 fills `github_support` (Direct 3 / Partial 2 / Limited 1 / Not supported 0) and combines it with `lifecycle_requirements_matrix.csv` for the coverage profile.

## Open / optional (do not block Phase 4)

- [ ] Second-coder check on the RE→RM assignment (~20%) — deferred, single-coder project, declared as a limitation.
- [ ] Revisit RM15 scope after the Phase 5 mapping (may be dropped from headline coverage figures).
