# Changelog

All notable changes to this research project are recorded here.
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions
follow the roadmap release points (`docs/CASE_STUDY.md` §5): v0.1 concept, v0.2
literature, v0.3 requirements framework, v0.4 reference architecture, v1.0 paper.
Methodological decisions are logged separately in [`docs/DECISION_LOG.md`](docs/DECISION_LOG.md).

## [Unreleased]

### Working towards
- Phase 12 — Publication: final review; complete the three `docs/OPEN_ITEMS.md` user-tasks (make the repo public, run one live Issue→PR→Release cycle, screenshot the Project); archive on Zenodo and add the DOI to `paper.tex` and `CITATION.cff`; submit to *Scientometrics*.

### Carried to the manuscript (not blockers)
- Limitations: single-coder project (no second rater on RE→RM, the 15 support scores, or the 21 evaluation sub-scores); no Scopus/WoS access (OpenAlex trade-off).
- Future work: instantiate the template for an unrelated second project.

---

## [1.0.0] — 2026-08-30

Roadmap Phases 3–11: the requirements framework, GitHub capability analysis and coverage
mapping, the reference architecture and reusable template, the self-referential case study,
the six-dimension evaluation, the RQ1–RQ5 synthesis, and a complete v1 manuscript for
*Scientometrics*. Answers RQ1–RQ5. `DECISION_LOG.md` D6–D20.

### Added — Phase 3: Research Management Requirements Framework (RQ2)
- `framework/requirements/requirements_framework.csv` — canonical set RM1–RM15 (id, name, category, definition, expected_capabilities, lifecycle stages, evidence, literature attention, importance, differentiator flag, relationships, limitations).
- `framework/requirements/lifecycle_requirements_matrix.csv` — RM × 11 lifecycle stages, applicability 0–3.
- `framework/requirements/REQUIREMENTS_FRAMEWORK.md` — narrative: method, the 15 requirements, classification, relationship model, changes from the provisional set, RQ1 corroboration.
- `framework/README.md`; `framework/mapping/`, `framework/architecture/` (placeholders for Phases 5–6).
- `analysis/scripts/summarise_requirements.py` → `results/framework/*.csv`, `requirements_summary.md`.
- `docs/PHASE3_PROGRESS.md`; `DECISION_LOG.md` D9.

### Changed
- `docs/REQUIREMENTS_FRAMEWORKS.md` — reframed as the method doc; the built framework in `framework/requirements/` is authoritative.
- `docs/ROADMAP.md` — Phase 3 marked complete; `docs/README.md`, `analysis/README.md` indexes updated.

### Added — Phase 4: GitHub capability analysis (RQ3)
- `framework/mapping/github_capability_catalogue.csv` — 68 native capabilities (GC01–GC68) across 12 feature groups (GF1–GF12), with what_it_does, research_use, traceability, plan_availability, practical_complexity, limitations, candidate_requirements.
- `framework/mapping/GITHUB_CAPABILITY_CATALOGUE.md` — narrative: scope (native only; GC61 Zenodo-bridge exception), plan model, the 12 groups, cross-cutting observations, candidate coverage.
- `analysis/scripts/summarise_capabilities.py` → `results/framework/gc_*.csv`, `capability_summary.md`.
- `docs/PHASE4_PROGRESS.md`; `DECISION_LOG.md` D10.

### Changed
- `docs/GITHUB_FEATURE_MAPPING.md` — reframed as the method doc for Phases 4–5; the built catalogue is authoritative.
- `docs/ROADMAP.md` — Phase 4 marked complete; `docs/README.md`, `analysis/README.md`, `framework/README.md` indexes updated.

### Added — Phase 5: Requirement–feature mapping (RQ3)
- `framework/mapping/requirement_feature_matrix.csv` — RM1–RM15 support scores (Direct 3 / Partial 2 / Limited 1 / Not supported 0) with primary capabilities, contributing feature groups, implementation pattern, evidence note, external-tool dependencies, residual gap.
- `framework/mapping/coverage_analysis.md` — narrative: method, headline (mean 2.33/3; 7 Direct, 6 Partial, 2 Limited, 0 Not supported), strengths/weaknesses, differentiator gap (RM1/RM2/RM5 mean 1.67 vs 2.50), lifecycle-coverage profile, 5 external-tool dependencies, feature-group contribution, RQ3 answer.
- `analysis/scripts/coverage_indicators.py` → `results/framework/coverage_*.csv`, `coverage_summary.md`.
- `docs/PHASE5_PROGRESS.md`; `DECISION_LOG.md` D11.

### Changed
- `framework/requirements/requirements_framework.csv` — `github_support` column back-filled with Phase 5 labels.
- `docs/GITHUB_FEATURE_MAPPING.md` — Phase 5 status/headline added.
- `docs/ROADMAP.md` — Phase 5 marked complete; `docs/README.md`, `analysis/README.md`, `framework/README.md` indexes updated.

### Added — Phase 6: Reference architecture (RQ3, constructive)
- `framework/architecture/reference_architecture.md` — narrative: concept, 5-layer conceptual architecture, 15 components, the four lifting conventions, lifecycle model, 7 workflows, external-tool boundaries, implementation principles.
- `framework/architecture/architecture_components.csv` — 15 components (A1–A4, B1–B4, C1–C3, D1–D3, X1) with github_basis, convention, requirements_served, traceability_role.
- `framework/architecture/workflows.csv` — 7 workflows (WF1–WF7) with steps, components, requirements, traceability link.
- `framework/architecture/lifecycle_model.csv` — 12 stages → active components, artifacts, entry/exit links.
- `analysis/scripts/summarise_architecture.py` → `results/framework/arch_*.csv`, `architecture_summary.md` (consistency checks all pass).
- `docs/PHASE6_PROGRESS.md`; `DECISION_LOG.md` D12.

### Changed
- `docs/REFERENCE_ARCHITECTURE.md` — marked as an early sketch; the built architecture in `framework/architecture/` is authoritative.
- `docs/ROADMAP.md` — Phase 6 marked complete; `docs/README.md`, `analysis/README.md`, `framework/README.md`, `FIGURES_AND_TABLES.md` updated.

### Added — Phase 7: Reusable GitHub Research Project Template
- `template/github-research-project-template/` — 33-file template: repo skeleton; `docs/` set with `conventions.md` (the four architecture conventions), charter, protocol, methodology, roadmap (plan of record), decision log, glossary; three issue forms (research-question, research-task, decision-record); PR template with reproducibility checklist; `labels.yml`, `project-fields.md`, `release-checklist.md`; starter Actions `validate-structure`, `markdown-link-check`, `reproduce`.
- `template/template_manifest.csv` — every file → architecture component(s) → requirement(s) → purpose.
- `template/README.md`; `analysis/scripts/check_template.py` → `results/framework/template_coverage.csv`, `template_summary.md`.
- `docs/PHASE7_PROGRESS.md`; `DECISION_LOG.md` D13.

### Changed
- `docs/TEMPLATE_PROJECT.md` — marked as draft; the built template in `template/` is authoritative.
- `docs/ROADMAP.md` — Phase 7 marked complete; `docs/README.md`, `analysis/README.md` updated.

### Added — Phase 8: Case study (self-referential, RQ5)
- `case-study/implementation_record.csv` — architecture components A1–X1 with implementation status and evidence.
- `case-study/activity_register.csv` — reconstructed register: 5 RQs, 8 milestones, 16 tasks, 14 decisions, with links.
- `case-study/traceability_examples.md` — four end-to-end chains through real artifacts; `case-study/README.md`.
- Framework configuration applied to this repository: `CITATION.cff`, `CONTRIBUTING.md`, `LICENSE`; `.github/ISSUE_TEMPLATE/`, `.github/pull_request_template.md`, `.github/labels.yml`, `.github/project-fields.md`, `.github/mlc-config.json`, `.github/release-checklist.md`, `.github/workflows/validate-structure.yml`, `.github/workflows/markdown-link-check.yml`; `docs/conventions.md`, `docs/glossary.md`. Root/`.github` inventory now mirrors the template.
- `analysis/scripts/summarise_case_study.py` → `results/framework/cs_*.csv`, `case_study_summary.md`.
- `docs/PHASE8_PROGRESS.md`; `DECISION_LOG.md` D14.

### Changed
- `docs/CASE_STUDY.md` — marked as protocol; the `case-study/` record is authoritative.
- `docs/ROADMAP.md` — Phase 8 marked complete; `docs/README.md`, `analysis/README.md` updated.

### Added — Phase 9: Evaluation (RQ5)
- `case-study/evaluation_scores.csv` — 21 sub-dimensions across E1–E6, scored 0/1/2 with a basis tag (observed / retrospective / design-support / planned).
- `case-study/workflow_comparison.csv` — Table 6: fragmented workflow vs the framework across 6 dimensions.
- `case-study/evaluation.md` — narrative: method, results (overall 1.62/2; observed-only 1.76/2), dimension by dimension, comparison, observations, limitations.
- `analysis/scripts/evaluation_summary.py` → `results/framework/eval_*.csv`, `evaluation_summary.md`.
- `docs/PHASE9_PROGRESS.md`; `DECISION_LOG.md` D15.

### Changed
- `docs/EVALUATION_PROTOCOL.md` — marked as protocol; `case-study/evaluation.md` is the record.
- `docs/ROADMAP.md` — Phase 9 marked complete; `docs/README.md`, `analysis/README.md` updated.

### Added — Open-items close-out (Phases 2–9)
- `docs/OPEN_ITEMS.md` — consolidated ledger; 15 closed, 5 limitations, 3 user-tasks, 1 future-work.
- Track A: `analysis/scripts/enrich_crossref.py` (+ `data/processed/corpus_enrichment.csv`), `query_precision_check.py` (+ `results/track_a/query_precision.md`), `coword_map.py` (+ `results/track_a/coword_map.gexf`, `manuscript/figures/coword_map.svg`); `annual_production_trimmed.csv` (2008–2024).
- `literature/references_factcheck.md`; `literature/included_studies_primary.csv` (S53–S67).
- `framework/mapping/requirement_feature_matrix_strict.csv` + `coverage_indicators.py --strict`; core-14 vs full-15 headline coverage.
- `framework/mapping/plan_availability_check.md`; GC15 plan note refined; `GITHUB_CAPABILITY_CATALOGUE.md` §2 GC61 justification expanded.
- `manuscript/figures/fig3_architecture.svg`, `fig4_traceability.svg`.
- `LICENSES/{MIT,CC-BY-4.0}.txt` + `REUSE.toml` (study repo); `LICENSES/` + `CC0-1.0.txt` and `.github/workflows/label-sync.yml` in both repo and template.
- `DECISION_LOG.md` D16 (2025 tail), D17 (RM15 headline scope), D18 (coverage sensitivity check).

### Changed
- Every `PHASEn_PROGRESS.md` "Open / optional" section replaced with a resolution table pointing to `docs/OPEN_ITEMS.md`.

### Added — Phase 10: Analysis
- `analysis/synthesis.md` — integrates RQ1–RQ5: the through-line, findings by RQ, framework-coverage analysis, implementation results, strengths, limitations, implications, answer to the main RQ, Phase 11 section map.
- `analysis/findings.csv` — 32 findings (F01–F32), typed (result / limitation / implication), strength-rated, with verifiable evidence paths.
- `analysis/scripts/synthesis_check.py` → `results/framework/synthesis_*.csv`, `synthesis_summary.md`.
- `docs/PHASE10_PROGRESS.md`; `DECISION_LOG.md` D19.

### Changed
- `docs/ROADMAP.md` — Phase 10 marked complete; `docs/README.md`, `analysis/README.md` updated.

### Added — Phase 11: Manuscript development
- `manuscript/paper.tex` — complete v1 draft for *Scientometrics* (`sn-jnl`): Abstract, Introduction, Materials and Methods, Results (bibliometric map / requirements + coverage / architecture + template + feasibility), Discussion, Conclusions, Declarations. 16 pp., 4 tables, 3 figures; compiles clean (0 undefined citations/references).
- `manuscript/references.bib` — 62 entries (52 from `literature/references.bib` + 10 primary GitHub-in-research studies cited).
- `manuscript/figures/*.pdf` — architecture, traceability path and co-word map rendered from SVG; `manuscript/build.sh`.
- `docs/PHASE11_PROGRESS.md`; `DECISION_LOG.md` D20.

### Changed
- `docs/ROADMAP.md` — Phase 11 marked complete (v1 draft); `docs/README.md` updated.

### Added — Phase 12 preparation
- `manuscript/build.sh`; `docs/OPEN_ITEMS.md` summary of the 3 pre-submission user-tasks.
- `CITATION.cff` version → 1.0.0; `CHANGELOG.md` [Unreleased] promoted to [1.0.0]; `DECISION_LOG.md` D21.

---

## [0.2.0] — 2026-08-30 — Phase 2: Literature analysis

Two-track literature analysis (`DECISION_LOG.md` D2 hybrid framing).

### Added — Track B (structured evidence review)
- `SOTA/SOTA.md` adopted as the Track B evidence base (Consensus Deep Search synthesis) — `DECISION_LOG.md` D6.
- `literature/included_studies.csv` — 52 studies (S01–S52), coded by strand and lifecycle focus.
- `literature/requirements_extraction.csv` — 17 requirement rows (RE01–RE17), challenge → need → requirement, mapped to RM1–RM14.
- `literature/lifecycle_coverage.csv` — 15 lifecycle stages with literature-attention level.
- `literature/references.bib` — BibTeX for S01–S52.
- `literature/screening_notes.md`, `literature/background_synthesis.md` (working synthesis for the Introduction / Results §10.1).
- `analysis/scripts/summarise_track_b.py` and generated `results/tb_*.csv`, `results/track_b_summary.md`.

### Added — Track A (bibliometric corpus, open sources — `DECISION_LOG.md` D8)
- `literature/search_strings.md` — frozen OpenAlex (15 queries) and arXiv (5 queries) search strings; Scopus/WoS strings kept as optional cross-checks.
- `literature/search_log.md` — retrieval and de-duplication log.
- `analysis/scripts/fetch_openalex.py` — OpenAlex API retrieval (cursor pagination, abstract reconstruction).
- `analysis/scripts/fetch_arxiv.py` — arXiv supplement for the version-control / research-software strand.
- `analysis/scripts/build_corpus.py` — merge, repository-deposit exclusion (`data/raw/exclude_sources.txt`), de-duplication (DOI → title+year).
- `analysis/scripts/bibliometrics_track_a.py` — zero-dependency descriptives + co-word edge list; `bibliometrics_track_a.R` — bibliometrix thematic-map skeleton.
- First run: OpenAlex 5,936 + arXiv 462 → **5,139-work corpus** (`data/processed/corpus.csv`); descriptives in `results/track_a/`. Lifecycle stage-hit profile independently reproduces the Track B output bias (data management 50.8 %, analysis/workflow 41.9 % vs idea/question 3.7 %).

### Added — infrastructure
- Repository scaffolding `literature/`, `data/`, `analysis/`, `results/`, `manuscript/` mirroring the prior GitHub–Zenodo–ORCID workflow repository.
- Root `README.md`; `.gitignore` (LaTeX aux, Python cache, raw API dumps).
- `manuscript/` LaTeX skeleton: `paper.tex` (Springer `sn-jnl` class), `.latexmkrc`, `references.bib`, `figures/`, `tables/`.
- `docs/PHASE2_PROGRESS.md`.

### Changed
- `docs/RESEARCH_DESIGN.md` and `docs/LITERATURE_REVIEW.md` rewritten for the hybrid framing (nested corpus + screened subset, bibliometric branch).
- Working synthesis moved `manuscript/literature-review.md` → `literature/background_synthesis.md` (manuscript prose deferred to Phase 11).
- `docs/DECISION_LOG.md` — D6, D7, D8.
- `docs/ROADMAP.md` — added a current-status block; Phase 2 marked closed.

---

## [0.1.0] — 2026-08-29 — Phase 1: Project definition

### Added
- `docs/PHASE1_PROJECT_DEFINITION.md` — authoritative Phase 1 output: research problem, aim, objectives, revised research questions (RQ1–RQ5), conceptual scope, target-journal positioning (*Scientometrics*, Springer Nature), manuscript structure, repository architecture.
- `docs/DECISION_LOG.md` — D1 (target journal), D2 (hybrid framing: bibliometric map + coverage analysis + synthesised architecture/template), D3 (revised RQ set), D4 (nested literature design), D5 (case study: self-referential + reusable template).

### Changed
- `docs/RESEARCH_QUESTION.md`, `docs/PAPER_PLAN.md` — alignment notes pointing to the Phase 1 definition as authoritative; superseded sections flagged.
- `docs/README.md` — index updated.

---

## [0.0.1] — 2026-08-29 — Initial documentation

### Added
- `docs/` — initial research design, protocols and planning documents: `PAPER_PLAN.md`, `ROADMAP.md`, `RESEARCH_DESIGN.md`, `RESEARCH_QUESTION.md`, `LITERATURE_REVIEW.md`, `REQUIREMENTS_FRAMEWORKS.md`, `GITHUB_FEATURE_MAPPING.md`, `REFERENCE_ARCHITECTURE.md`, `REPOSITORY_ARCHITECTURE.md`, `TEMPLATE_PROJECT.md`, `CASE_STUDY.md`, `EVALUATION_PROTOCOL.md`, `FIGURES_AND_TABLES.md`.
