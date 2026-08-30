# Phase 9 — Evaluation

**Roadmap step:** 9 of 12 · **Answers:** RQ5 · **Protocol:** `EVALUATION_PROTOCOL.md`
**Started / completed:** 2026-08-30 · **Status: COMPLETE (v1)**

Scores the six evaluation dimensions against the self-referential case study and builds the fragmented-workflow comparison.

---

## Outputs (`case-study/`)

| File | Content |
|---|---|
| `evaluation_scores.csv` | **Canonical.** 21 sub-dimensions across E1–E6: score (0–2), max, basis (observed / retrospective / design-support / planned), evidence, note |
| `workflow_comparison.csv` | **Table 6.** Fragmented workflow vs GitHub-based framework across 6 dimensions, with advantage and caveat |
| `evaluation.md` | Narrative: method, results, dimension by dimension, comparison, observations, limitations, handoff |
| `results/framework/eval_*.csv` + `evaluation_summary.md` | Tallies (`analysis/scripts/evaluation_summary.py`) |

## Results

| Dim | Dimension | /2 | % |
|---|---|---|---|
| E1 | Requirement coverage | 2.00 | 100% |
| E2 | Traceability | 1.50 | 75% |
| E3 | Documentation | 2.00 | 100% |
| E4 | Organization | 1.75 | 88% |
| E5 | Transparency | 1.50 | 75% |
| E6 | Usability | 1.25 | 62% |
| | **Overall** | **1.62** | **81%** |

Observed-only mean (17 of 21 sub-scores): 1.76 / 2 (88%). E1 coverage from Phase 5: **13/15** requirements supported (7 Direct, 6 Partial), 0 unsupported.

Lowest sub-scores: E5 external visibility 0 (repo not yet public — Phase 12), E2 task traceability 1 (retrospective), E2 provenance linkage 1, E4 task categorization 1, E6 configuration complexity 1.

## Findings

- **Realised strengths:** requirement coverage (E1) and documentation (E3) at 2.0; decision and version traceability at 2.0.
- **Weakest dimension:** usability (E6, 1.25) — configuration complexity, technical-literacy barrier, and coordination-layer overhead that was not adopted under solo-sprint conditions.
- The framework's benefit is **linking artifacts a fragmented workflow leaves disconnected**; its cost is the **coordination layer**; its weak points **coincide with the thinnest areas of the literature** (upstream traceability).

## Decisions logged

- `DECISION_LOG.md` D15 — 0/1/2 per sub-dimension with explicit basis tags; un-exercised dimensions scored on design support and flagged; overall 1.62/2 reported alongside the observed-only 1.76/2.

## Handoff to Phase 10

Phase 10 synthesises RQ1–RQ5 (coverage, implementation results, strengths, limitations) for the manuscript. Inputs: `results/track_a/` (RQ1), `framework/` (RQ2–RQ4), `case-study/evaluation.md` + `evaluation_scores.csv` + `workflow_comparison.csv` (RQ5). These become Results §10.6 and Tables 5–6.

## Open / optional (see `docs/OPEN_ITEMS.md`)

- Independent second rater on the 21 sub-scores — **limitation** (single-coder project; declared).
- Re-score E5/E6 after the repo is public + a real cycle — **user-task** (depends on the Phase 7/8 user-tasks; re-run `evaluation_summary.py` afterwards).
