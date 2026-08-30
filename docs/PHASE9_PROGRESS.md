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

## Results (after the D23 re-score)

| Dim | Dimension | /2 | % |
|---|---|---|---|
| E1 | Requirement coverage | 2.00 | 100% |
| E2 | Traceability | 1.75 | 88% |
| E3 | Documentation | 2.00 | 100% |
| E4 | Organization | 2.00 | 100% |
| E5 | Transparency | 2.00 | 100% |
| E6 | Usability | 1.50 | 75% |
| | **Overall** | **1.86** | **93%** |

Observed-only mean (20 of 21 sub-scores): 1.85 / 2 (92%). E1 coverage from Phase 5: **13/15** requirements supported (7 Direct, 6 Partial), 0 unsupported.

Initial Phase 9 scoring was **1.62 / 2** (E2 1.50, E4 1.75, E5 1.50, E6 1.25); after the repository was made public (D22) and one live Issue→PR→Release cycle was run (issue #2), four sub-scores moved from planned/retrospective/design-support to observed — E5 external visibility 0→2, E2 task traceability 1→2, E4 task categorization 1→2, E6 workflow overhead 1→2 (`DECISION_LOG.md` D23).

Remaining lowest sub-scores: E2 provenance/artifact linkage 1 (no automated lineage query), E6 configuration complexity 1, E6 technical-knowledge 1.

## Findings

- **Realised strengths:** requirement coverage (E1), documentation (E3), organization (E4) and transparency (E5) at 2.0; decision, version and task traceability at 2.0.
- **Weakest dimension:** usability (E6, 1.50) — configuration complexity and the technical-literacy barrier; the coordination layer's *collaborative* value is still untested (single author).
- The framework's benefit is **linking artifacts a fragmented workflow leaves disconnected**; its weak points **coincide with the thinnest areas of the literature** (upstream traceability).

## Decisions logged

- `DECISION_LOG.md` D15 — 0/1/2 per sub-dimension with explicit basis tags; un-exercised dimensions scored on design support and flagged; initial overall 1.62/2 alongside observed-only 1.76/2.
- `DECISION_LOG.md` D23 — re-score after D22 (public) and issue #2 (live cycle): overall **1.62 → 1.86 / 2**.

## Handoff to Phase 10

Phase 10 synthesises RQ1–RQ5 (coverage, implementation results, strengths, limitations) for the manuscript. Inputs: `results/track_a/` (RQ1), `framework/` (RQ2–RQ4), `case-study/evaluation.md` + `evaluation_scores.csv` + `workflow_comparison.csv` (RQ5). These become Results §10.6 and Tables 5–6.

## Open / optional (see `docs/OPEN_ITEMS.md`)

- Independent second rater on the 21 sub-scores — **limitation** (single-coder project; declared).
- Re-score E5/E6 after the repo is public + a real cycle — **user-task** (depends on the Phase 7/8 user-tasks; re-run `evaluation_summary.py` afterwards).
