# Open Items Ledger

Consolidates every "open / optional" item raised in `PHASE2–9_PROGRESS.md`. Each phase doc now links here instead of keeping its own list.

**Status vocabulary**
- **closed** — done; see the linked artifact
- **limitation** — cannot be closed within this study's constraints; recorded in the manuscript limitations (single-coder, no Scopus/WoS access)
- **user-task** — requires the author's manual action on GitHub (making the repo public, running a live Issue→PR→Release cycle, screenshots) — to do before submission
- **future-work** — out of scope for this study; goes in "Future research"

---

## Phase 2 — Literature analysis

| # | Item | Status | Resolution |
|---|---|---|---|
| 2.1 | Crossref DOI/citation enrichment for no-DOI records | **closed** | `analysis/scripts/enrich_crossref.py` — 250 no-DOI records processed, only 8% Crossref-matchable (they are grey literature); `data/processed/corpus_enrichment.csv`, `results/track_a/enrichment_summary.md`. OpenAlex `cited_by_count` stays primary. |
| 2.2 | Precision check + tighten broad OpenAlex queries (`"open science"`, `github`) | **closed** | `analysis/scripts/query_precision_check.py`; `results/track_a/query_precision.md` — precision acceptable, queries kept, documented |
| 2.3 | 2025 tail treatment for the production trend | **closed** | `DECISION_LOG.md` D16 — 2025 kept with a caveat; a 2008–2024 trimmed series is reported alongside (`results/track_a/annual_production_trimmed.csv`) |
| 2.4 | Render the co-word map | **closed** | `analysis/scripts/coword_map.py` → `results/track_a/coword_map.gexf` (Gephi-ready) + `manuscript/figures/coword_map.svg` |
| 2.5 | Factcheck `literature/references.bib` | **closed** | `phd-skills:factcheck` run; corrections applied; `literature/references_factcheck.md` |
| 2.6 | Expand Track B with primary GitHub-in-research studies | **closed** | `literature/included_studies_primary.csv` (S53–S67, purposive) + `screening_notes.md`; does not change RE01–RE17; BibTeX for the cited subset generated at Phase 11 |
| 2.7 | Second-coder reliability on requirement extraction (~20%) | **limitation** | Single-coder project; declared in `case-study/evaluation.md` §6 and the manuscript |
| 2.8 | Scopus / WoS cross-check | **limitation** | No subscription access; OpenAlex coverage/precision trade-off declared; `DECISION_LOG.md` D8 |

## Phase 3 — Requirements framework

| # | Item | Status | Resolution |
|---|---|---|---|
| 3.1 | Second-coder check on the RE→RM assignment | **limitation** | Same as 2.7 |
| 3.2 | Revisit RM15 (governance) scope after Phase 5 | **closed** | `DECISION_LOG.md` D17 — RM15 kept in the framework but excluded from headline coverage; `coverage_indicators.py` now reports core-14 and full-15 means |

## Phase 4 — GitHub capability analysis

| # | Item | Status | Resolution |
|---|---|---|---|
| 4.1 | Verify plan-availability against current GitHub docs | **closed** | `framework/mapping/plan_availability_check.md` — 8 plan-gated capabilities spot-checked against GitHub Docs (2026-08-30), catalogue notes reconciled |
| 4.2 | GC61 Zenodo-bridge reviewer-facing justification | **closed** | `GITHUB_CAPABILITY_CATALOGUE.md` §2.1 expanded |

## Phase 5 — Requirement–feature mapping

| # | Item | Status | Resolution |
|---|---|---|---|
| 5.1 | Sensitivity check with a stricter rubric | **closed** | `DECISION_LOG.md` D18; `framework/mapping/requirement_feature_matrix_strict.csv` + `coverage_indicators.py --strict` → `results/framework/coverage_summary_strict.md`; overall mean 2.33 → 2.13, conclusion unchanged |
| 5.2 | Second rater on the 15 support scores | **limitation** | Same as 2.7 |
| 5.3 | Confirm plan-availability caveats before scores go in the manuscript | **closed** | Folded into 4.1 |

## Phase 6 — Reference architecture

| # | Item | Status | Resolution |
|---|---|---|---|
| 6.1 | Conceptual-architecture and traceability-path figures | **closed** | `manuscript/figures/fig3_architecture.svg`, `fig4_traceability.svg` |
| 6.2 | Sanity-check the lifecycle model against this repo's history | **closed** | Done in Phase 8 (`case-study/traceability_examples.md`, `implementation_record.csv`) |

## Phase 7 — Reusable template

| # | Item | Status | Resolution |
|---|---|---|---|
| 7.1 | REUSE-style `LICENSES/` directory | **closed** | `LICENSES/MIT.txt`, `LICENSES/CC-BY-4.0.txt` + `REUSE.toml` in the study repo and the template; root `LICENSE` explains the split |
| 7.2 | Optional `label-sync` workflow | **closed** | `.github/workflows/label-sync.yml` added to the template and this repo |
| 7.3 | Screenshot the configured Project | **closed** | Project #2 configured (fields per `.github/project-fields.md`, issues #1–#12 added); `manuscript/figures/project-board.png` (+ roadmap panel to recapture). `FIGURES_AND_TABLES.md` Figure 6. Issue #1. |

## Phase 8 — Case study

| # | Item | Status | Resolution |
|---|---|---|---|
| 8.1 | Run one real Issue→PR→Release cycle | **closed** | One full cycle run (issue #2 → branch → PR → merge → `v1.1.0` Release). `case-study/live_cycle_demo.md`; `implementation_record.csv` A2 → native, C2/D1 → partial; 11/15 components now exercised. |
| 8.2 | Instantiate the template for a second project | **future-work** | External-validity study |

## Phase 9 — Evaluation

| # | Item | Status | Resolution |
|---|---|---|---|
| 9.1 | Independent second rater on the 21 sub-scores | **limitation** | Same as 2.7 |
| 9.2 | Re-score E5/E6 after the repo is public + a real cycle | **closed** | `DECISION_LOG.md` D23; E2/E4/E5/E6 sub-scores re-scored on observed evidence; overall **1.62 → 1.86 / 2**. `evaluation.md`, `results/framework/eval_*`, `findings.csv`, `synthesis.md` updated. `manuscript/paper.tex` figures updated in the manuscript pass (issue #6). Issue #3. |

## Phase 12 — Publication

| # | Item | Status | Resolution |
|---|---|---|---|
| 12.1 | Make the repository public | **closed** | `DECISION_LOG.md` D22; `implementation_record.csv` X1/D3 → partial; 13/15 components exercised. Issue #4. |
| 12.2 | Wire the Zenodo DOI into the manuscript | **user-task** | DOI in `CITATION.cff` / README; add to `paper.tex` data-availability — GitHub issue #5 |
| 12.3 | Expand manuscript body toward ~8,000 words | **user-task** | GitHub issue #6 |
| 12.4 | Full `references.bib` check for the cited subset | **user-task** | GitHub issue #7 |
| 12.5 | Publication-quality vector figures 3 & 4 | **user-task** | GitHub issue #8 |
| 12.6 | Cover letter + Scientometrics submission checklist | **user-task** | GitHub issue #9 |

---

## Summary

| Status | Count | Items |
|---|---|---|
| **closed** | 19 | 2.1–2.6, 3.2, 4.1, 4.2, 5.1, 5.3, 6.1, 6.2, 7.1, 7.2, 7.3, 8.1, 9.2, 12.1 |
| **limitation** (declared in the manuscript) | 5 | 2.7, 2.8, 3.1, 5.2, 9.1 — all reduce to "single-coder project" and "no Scopus/WoS access" |
| **user-task** (before submission) | 5 | 12.2–12.6 — GitHub issues #5–#9 |
| **future-work** | 1 | 8.2 second-project external validity — GitHub issue #12 |

Tracked as GitHub issues #1–#12 (milestone *Phase 12 – Publication*). The 5 limitations
and 1 future-work item are recorded in `case-study/evaluation.md` §6 and appear in the
manuscript's Limitations and Future Research.
