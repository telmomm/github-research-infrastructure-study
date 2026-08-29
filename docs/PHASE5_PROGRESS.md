# Phase 5 — Requirement–Feature Mapping

**Roadmap step:** 5 of 12 · **Answers:** RQ3 · **Method doc:** `GITHUB_FEATURE_MAPPING.md`
**Started / completed:** 2026-08-30 · **Status: COMPLETE (v1)**

Grades how well GitHub's native functionalities (Phase 4) support the requirements framework (Phase 3), and computes coverage indicators.

---

## Outputs (`framework/mapping/`)

| File | Content |
|---|---|
| `requirement_feature_matrix.csv` | **Canonical.** Per RM1–RM15: support_level (0–3), support_label, primary_capabilities (GC ids), contributing_groups (GF:weight), implementation_pattern, evidence_note, external_tools_needed, residual_gap |
| `coverage_analysis.md` | Narrative: method, headline result, strengths, weaknesses, the differentiator gap, lifecycle profile, external tools, feature-group contribution, RQ3 answer |
| `results/framework/coverage_*.csv` + `coverage_summary.md` | Indicators from `analysis/scripts/coverage_indicators.py` |
| `framework/requirements/requirements_framework.csv` | `github_support` column back-filled with the Phase 5 label per RM |

## Headline result (RQ3)

| Indicator | Value |
|---|---|
| Overall mean support (0–3) | **2.33** (≈ 78%) |
| Direct (3) | 7 — RM3, RM4, RM6, RM7, RM8, RM11, RM13 |
| Partial (2) | 6 — RM1, RM5, RM9, RM10, RM12, RM14 |
| Limited (1) | 2 — RM2, RM15 |
| Not supported (0) | 0 |
| Requirements needing an external tool | 5 — RM8, RM9, RM12, RM14, RM15 |

**By category:** Execution / Collaboration / Automation 3.00 · Documentation 2.67 · Planning / Traceability / Artifact mgmt / Output mgmt 2.00 · Governance 1.00.

**Differentiators RM1/RM2/RM5:** mean **1.67** vs **2.50** for the rest — the upstream planning / question / decision layer is under-supported by the platform, matching the RQ1 literature gap.

**Lifecycle profile:** flat-ish 2.1–2.4; lowest at idea (2.12) and question (2.25), highest at literature / analysis / manuscript (2.43).

**Feature-group contribution:** Issues (19) + Repository/Git (18) carry most of the framework; Projects (9), Access & meta (8), Pull Requests (7) next; Actions / Discussions / Branches / Releases (5 each) contribute narrowly.

## Interpretation

GitHub supports research management **substantially but unevenly**: Direct where research work resembles software engineering (tasks, review, communication, version control, documentation, transparency, automation), Partial or Limited for research-specific traceability of questions, decisions and provenance, and for planning and governance. No requirement is entirely unsupported, but a third of the framework rests on convention rather than purpose-built features.

## Decisions logged

- `DECISION_LOG.md` D11 — four-level rubric applied per requirement (best achievable level); scores, differentiator-gap finding, the 5 external-tool dependencies, and the "no 0s" note (nothing is wholly unsupported; two Limited).

## Handoff to Phase 6

The reference architecture organises the Direct and Partial capabilities into components, workflows and a lifecycle model, and specifies the conventions that lift RM1, RM2, RM5 and RM10 from raw features to research-usable support. Output to `framework/architecture/`.

## Open / optional (do not block Phase 6)

- [ ] Sensitivity check: re-score with a stricter rubric (convention-heavy = Limited) to show the result is not fragile.
- [ ] Second rater on the 15 scores (~all) — deferred, single-coder project, declared as a limitation.
- [ ] Confirm plan-availability caveats (Phase 4 open item) before the scores go in the manuscript.
