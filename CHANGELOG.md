# Changelog

All notable changes to this research project are recorded here.
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions
follow the roadmap release points (`docs/CASE_STUDY.md` §5): v0.1 concept, v0.2
literature, v0.3 requirements framework, v0.4 reference architecture, v1.0 paper.
Methodological decisions are logged separately in [`docs/DECISION_LOG.md`](docs/DECISION_LOG.md).

## [Unreleased]

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

### Working towards
- Phase 7 — Reusable GitHub Research Project Template (operationalise the architecture in `template/`).

### Pending / optional (do not block Phase 7)
- Track A: Crossref / Semantic Scholar citation enrichment; precision check on the broad OpenAlex queries; 2025 tail treatment; co-word map rendering.
- Factcheck `literature/references.bib` (venues, volumes, pages, DOIs).
- Second-coder reliability on the requirement extraction and the RE→RM assignment (~20%) — deferred, single-coder project.
- Scopus / WoS cross-check if access appears.
- Revisit RM15 (governance) scope after the Phase 5 mapping.

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
