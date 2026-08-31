# Open Items Ledger

Consolidates every "open / optional" item raised in `PHASE2–9_PROGRESS.md`. Each phase doc now links here instead of keeping its own list.

**Status vocabulary**
- **closed** — done; see the linked artifact
- **limitation** — cannot be closed within this study's constraints; recorded in the manuscript limitations (single-coder, no Scopus/WoS access)
- **limitation (mitigated)** — the constraint stands but a partial robustness check was run and is reported
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
| 2.7 | Second-coder reliability on requirement extraction (~20%) | **limitation (mitigated)** | No human second coder. Independent LLM re-code of all 17 RE→RM assignments: 94.1% agreement, κ 0.94; one adjacent disagreement (RE11 RM10/RM9), no coverage count affected. `case-study/reliability_check.md`, `reliability_check.csv`; `DECISION_LOG.md` D26. Issue #10. |
| 2.8 | Scopus / WoS cross-check | **closed** | Run 2026-09-30 via FECYT: WoS + Scopus Q1–Q4, 13,586 de-dup in-window records, **22% DOI overlap** with the corpus; the delta is a characterised precision tail (bioinformatics/CS tool papers via `git`/`github` + Keywords Plus). `DECISION_LOG.md` D24; `results/track_a/scopus_wos_crosscheck.md`. Issue #11. |

## Phase 3 — Requirements framework

| # | Item | Status | Resolution |
|---|---|---|---|
| 3.1 | Second-coder check on the RE→RM assignment | **limitation (mitigated)** | Covered by the 2.7 re-code (RE→RM unit: 94.1%, κ 0.94). `case-study/reliability_check.md`; D26. Issue #10. |
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
| 5.2 | Second rater on the 15 support scores | **limitation (mitigated)** | Independent LLM re-code of all 15 support levels: 100% agreement (κ 1.00) — but the least independent unit, since the matrix documents its own Direct/Partial/Limited rationale (caveat in `reliability_check.md` §4). D26. Issue #10. |
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
| 8.2 | Instantiate the template for a second project | **closed** | Retrospective instantiation on *PreMoCir* (clinical-ML mortality prediction, *Sensors* **26**(5):1656 2026; notebooks Zenodo 10.5281/zenodo.18249069). Structural / coverage test over RM1–RM15: **8 covered / 3 convention / 4 external**, same profile as the self-referential case → supports discipline-independence. `case-study/external_validity.md`, `case-study/external_validity_mapping.csv`, `results/framework/external_validity_summary.md`; `DECISION_LOG.md` D25. Retrospective single-case (same lead author) — a prospective instantiation stays as future work. Issue #12. |

## Phase 9 — Evaluation

| # | Item | Status | Resolution |
|---|---|---|---|
| 9.1 | Independent second rater on the 21 sub-scores | **limitation (mitigated)** | Independent LLM re-code of all 21 sub-scores: 95.2% agreement, κ 0.83 (deflated by skewed marginals; see §4). One adjacent disagreement (E6 workflow overhead 2/1); stricter read moves Overall 1.86 → 1.81, ranking unchanged. `case-study/reliability_check.md`; D26. Issue #10. |
| 9.2 | Re-score E5/E6 after the repo is public + a real cycle | **closed** | `DECISION_LOG.md` D23; E2/E4/E5/E6 sub-scores re-scored on observed evidence; overall **1.62 → 1.86 / 2**. `evaluation.md`, `results/framework/eval_*`, `findings.csv`, `synthesis.md` updated. `manuscript/paper.tex` figures updated in the manuscript pass (issue #6). Issue #3. |

## Phase 12 — Publication

| # | Item | Status | Resolution |
|---|---|---|---|
| 12.1 | Make the repository public | **closed** | `DECISION_LOG.md` D22; `implementation_record.csv` X1/D3 → partial; 13/15 components exercised. Issue #4. |
| 12.2 | Wire the Zenodo DOI into the manuscript | **closed** | `paper.tex` data-availability statement now cites the software DOI 10.5281/zenodo.22167500 and the companion dataset DOI 10.5281/zenodo.22173525; matches `CITATION.cff` `identifiers:` and the README badge. Fresh release for the submitted version stays a user step (`.github/release-checklist.md`). Issue #5. |
| 12.3 | Expand manuscript body toward ~8,000 words | **closed** | Body 3.7k → 4.9k words: added a per-strand related-work subsection (§1.4), expanded Methods 2.2 (query strands, PRISMA-style de-dup chain, Scopus/WoS cross-check) and 2.3 (evidence base, re-code), a per-requirement narrative in Results 3.2, and an external-validity paragraph in 3.3. Also reconciled all stale figures: evaluation 1.62→**1.86**, 8/15→**13/15** components, usability 1.25→**1.50**, Table 4, `tab:eval` caption; Scopus/WoS "not used"→cross-checked (22% DOI overlap, D24); single-coder→re-code mitigation (D26); external validity (D25). `analysis/findings.csv` F26 reworded. `latexmk` clean, 19 pp. Issue #6. |
| 12.4 | Full `references.bib` check for the cited subset | **closed** | All 24 cited entries in `manuscript/references.bib` verified against Crossref; `chen2025` issue 3→2, 15 entries gained missing `number`/`pages`, `escamilla2022` LNCS 13541 confirmed. `latexmk` clean (bibtex 0 warnings, no undefined citations). `literature/references_factcheck.md` "Phase 12" section. Issue #7. |
| 12.5 | Publication-quality vector figures 3 & 4 | **closed** | `fig3_architecture.svg` restyled by the author (refined palette, B3 keystone highlighted); `fig4_traceability.svg` rebuilt to the same palette with fixed geometry (connector lands on the target node, no label overflow) and a portable font stack. Both render as clean vector PDF via `rsvg-convert` in `build.sh`; `latexmk` clean, 19 pp. Issue #8. |
| 12.6 | Cover letter + Scientometrics submission checklist | **closed** | `manuscript/cover_letter.md` (draft, bracketed fields + reviewer slots) and `manuscript/submission_checklist.md` (per-item status against Springer Nature guidelines). Abstract trimmed 377→290 words, keywords 8→6, Declarations gained Ethics approval + Author contributions. Flagged for the author: reference style `sn-mathphys-num`→`sn-basic` (author–year), ORCID on the title page, fresh Zenodo release. Issue #9. |

---

## Summary

| Status | Count | Items |
|---|---|---|
| **closed** | 26 | 2.1–2.6, 2.8, 3.2, 4.1, 4.2, 5.1, 5.3, 6.1, 6.2, 7.1, 7.2, 7.3, 8.1, 8.2, 9.2, 12.1–12.6 |
| **limitation (mitigated)** | 4 | 2.7, 3.1, 5.2, 9.1 — "single-coder project" (no *human* second rater); an independent LLM re-code of all 53 coded decisions agreed at 96.2% (κ 0.83–1.00), `case-study/reliability_check.md`, D26. Still declared in the manuscript. |
| **user-task** (before submission) | 0 | — (all Phase 12 issues #1–#12 resolved; the pre-upload steps in `manuscript/submission_checklist.md` remain: reference style `sn-basic`, ORCID, fresh Zenodo release) |
| **future-work** | 0 | — (8.2 closed retrospectively; a *prospective* second-project instantiation is noted as future work in `case-study/external_validity.md` §5) |

Tracked as GitHub issues #1–#12 (milestone *Phase 12 – Publication*). The 4 limitations
are recorded in `case-study/evaluation.md` §6 and appear in the manuscript's Limitations;
the prospective-instantiation future-work line is in `case-study/external_validity.md` §5.
