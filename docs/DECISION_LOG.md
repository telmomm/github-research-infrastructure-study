# Decision Log

Chronological record of major methodological decisions. Each entry: ID, date, context, decision, rationale, alternatives considered, affected documents.

---

## D1 — Target journal: *Scientometrics* (Springer Nature)

- **Date:** 2026-08-29
- **Context:** A target venue was needed to fix framing, scope and reporting standards for Phase 1.
- **Decision:** Target *Scientometrics*. Backups: *Quantitative Science Studies*, *Research Evaluation*, *PeerJ Computer Science*, *Journal of Open Research Software*.
- **Rationale:** The study concerns digital infrastructure for the research process and open science, and can be given a quantitative (bibliometric + coverage-analysis) core that matches the journal's scope.
- **Alternatives:** Software-engineering or e-research venues (weaker open-science audience); design-science IS venues (would foreground the artifact, not the measurement).
- **Affects:** `PHASE1_PROJECT_DEFINITION.md` §7, all downstream docs.

---

## D2 — Framing: hybrid (bibliometric map + coverage analysis + synthesised architecture/template)

- **Date:** 2026-08-29
- **Context:** The original docs framed the study as design-and-evaluation / design science, which is a borderline scope fit for *Scientometrics*. Three options were weighed: (a) empirical requirement–feature mapping with coverage metrics; (b) keep design-science framing; (c) reframe as a bibliometric "science of research infrastructure" study.
- **Decision:** Hybrid of (a) and (c): a bibliometric analysis of the literature (RQ1) as the quantitative backbone, a reproducible requirement×functionality coverage analysis (RQ2–RQ3), and the reference architecture + reusable template (RQ4–RQ5) as a secondary synthesised contribution.
- **Rationale:** Gives the journal the quantitative core it expects while preserving the framework/template as a transferable artifact; strongest acceptance profile without abandoning the project's practical goal.
- **Alternatives:** Pure (a) — keeps artifact central but higher scope risk; pure (c) — safest fit but dilutes the artifact.
- **Affects:** `PHASE1_PROJECT_DEFINITION.md` §5, §7–§9; `PAPER_PLAN.md`; `RESEARCH_QUESTION.md`; `RESEARCH_DESIGN.md`; `LITERATURE_REVIEW.md` (adds bibliometric branch); `FIGURES_AND_TABLES.md` (adds field map, timeline, PRISMA diagram).

---

## D3 — Revised research-question set (RQ1–RQ5)

- **Date:** 2026-08-29
- **Context:** The hybrid framing needs an explicit bibliometric question and a clean RQ→Results mapping.
- **Decision:** Adopt RQ1 (bibliometric structure + lifecycle gaps), RQ2 (requirements), RQ3 (GitHub coverage + indicators), RQ4 (reference architecture + template), RQ5 (feasibility + limitations vs. fragmented workflow). Main RQ unchanged. Propositions P1–P5 unchanged.
- **Rationale:** RQ1 supplies the science-of-science component; RQ2–RQ3 carry the quantitative coverage core; RQ4–RQ5 deliver the artifact concisely.
- **Supersedes:** the RQ1–RQ5 set in `RESEARCH_QUESTION.md` (design-science phrasing).
- **Affects:** `PHASE1_PROJECT_DEFINITION.md` §5; `RESEARCH_QUESTION.md`; `PAPER_PLAN.md` §5–§6.

---

## D4 — Nested literature design (corpus vs. screened subset)

- **Date:** 2026-08-29
- **Context:** Bibliometrics needs a broad corpus; requirement extraction needs a screened, quality-controlled subset.
- **Decision:** Maintain two nested sets — a de-duplicated retrieval **corpus** (bibliometric analysis, RQ1) and a PRISMA-screened **subset** (requirement extraction, RQ2). Report both; document the reduction with a PRISMA 2020 flow diagram. Double-code ~20% of the subset for inter-coder reliability.
- **Rationale:** Keeps the quantitative field analysis broad while keeping requirement claims defensible; standard practice reviewers will expect.
- **Affects:** `PHASE1_PROJECT_DEFINITION.md` §6.4–§6.5; `LITERATURE_REVIEW.md`; `data/`, `literature/` scaffolding.

---

## D5 — Case study: self-referential (Option A) + reusable template

- **Date:** 2026-08-29
- **Context:** Case-study options were A (self-referential), B (existing project), C (dedicated project), or a combination.
- **Decision:** Combination A + reusable template — the framework manages this study's own development (this repository as evidence), and the template is packaged as an independent transferable artifact evaluated at a second level.
- **Rationale:** Full documentation and direct access to all project activity; the template addresses transferability. Circularity and developer-evaluation bias are declared limitations.
- **Alternatives:** B — real-world context but incomplete prior documentation and migration cost; C — controlled but low ecological validity.
- **Affects:** `CASE_STUDY.md`; `PHASE1_PROJECT_DEFINITION.md` §5 (RQ5), §6.2; `EVALUATION_PROTOCOL.md`.

---

## D6 — SOTA / Consensus Deep Search adopted as the Track B evidence base

- **Date:** 2026-08-29
- **Context:** Phase 2 needs an evidence base for the manuscript background and for requirement extraction. A synthesis of the literature (`SOTA/SOTA.md`) was produced with Consensus Deep Search (>220M records; 1.29M seed hits → ML relevance screening → 155 after de-duplication → top 100 reviews/surveys → 52 cited).
- **Decision:** Use `SOTA/SOTA.md` as the Track B evidence base. Normalise it into versioned artifacts under `literature/` (`included_studies.csv` S01–S52, `requirements_extraction.csv` RE01–RE17 mapped to RM1–RM14, `lifecycle_coverage.csv`, `references.bib`, `search_strategy.md`, `screening_notes.md`). Build the study folder structure (`data/`, `analysis/`, `results/`, `manuscript/`) mirroring the prior GitHub–Zenodo–ORCID workflow repository.
- **Rationale:** Fast, transparent, reproducible starting point that already maps challenges → requirements and lifecycle coverage, and already argues the *Scientometrics* positioning. Its limitations (single-provider synthesis, review-paper bias, opaque ML filter, biomedical/CS skew) are the explicit reason Track A (independent Scopus + WoS bibliometric retrieval) is retained and still required for RQ1.
- **Alternatives:** Start Phase 2 only from a manual Scopus/WoS search (slower, delays the background draft); treat `SOTA.md` as the whole literature review (insufficient rigor and coverage for *Scientometrics*).
- **Affects:** `LITERATURE_REVIEW.md`; `PHASE2_PROGRESS.md`; `literature/`, `data/`, `analysis/`, `results/`, `manuscript/`.

---

## D7 — Phase 2 closed with Track A (bibliometric retrieval) deferred

- **Date:** 2026-08-30
- **Context:** Track B (structured evidence review from `SOTA/SOTA.md`) is complete. Track A (Scopus + Web of Science bibliometric corpus for RQ1) is fully specified but cannot run without database access.
- **Decision:** Close Phase 2 with Track B as the deliverable. Freeze the Track A search strings (`literature/search_strings.md`) and prepare the retrieval/PRISMA log templates (`literature/search_log.md`) so Track A can be executed later without re-design. Proceed to Phase 3 on the Track B requirement set (RE01–RE17); Track A results, when available, refine RQ1 and the Discussion but do not gate Phase 3.
- **Rationale:** The requirements framework depends on the requirement extraction, which is done. Blocking the whole project on institutional database access is avoidable; the bibliometric map can be slotted in during Phases 10–11.
- **Also decided:** the working synthesis was moved from `manuscript/literature-review.md` to `literature/background_synthesis.md` — `manuscript/` holds only the paper; `literature/` holds Phase 2 inputs. Manuscript prose is not written into `paper.tex` until Phase 11 (earliest sensible start: end of Phase 3).
- **Open (non-blocking):** execute Track A; factcheck `references.bib`; optional Track B expansion with primary GitHub-in-research studies; second-coder reliability (deferred, single-coder project, declared as a limitation).
- **Affects:** `PHASE2_PROGRESS.md`; `ROADMAP.md`; `literature/`; `manuscript/`.

---

## D8 — Track A executed on open sources (OpenAlex primary), not Scopus/WoS

- **Date:** 2026-08-30
- **Context:** D7 deferred Track A pending Scopus/WoS access. Decision taken to run it now on open, subscription-free sources instead.
- **Decision:** Build the Track A bibliometric corpus from **OpenAlex** (primary, full API query frozen in `literature/search_strings.md`), with **arXiv** as a supplement for the version-control / GitHub strand, **Crossref / Semantic Scholar** for citation enrichment if needed, and **Google Scholar** for manual spot-checks only (flagged `source=GS`, never part of the counted corpus). Scopus/WoS remain optional cross-checks if access appears later.
- **Rationale:** OpenAlex is fully reproducible (open data, exact query + snapshot date publishable), covers journals + conferences + preprints, and carries abstracts, concepts, citations and affiliations. More reproducible than Scopus/WoS; the coverage/precision trade-off versus Scopus is declared as a limitation and cross-checked against Crossref counts.
- **Pipeline:** `analysis/scripts/fetch_openalex.py` → `fetch_arxiv.py` → `build_corpus.py` (dedup + optional `data/raw/exclude_sources.txt` to drop data/software-repository deposits) → `bibliometrics_track_a.py` (zero-dependency descriptives + co-word edge list) and/or `bibliometrics_track_a.R` (bibliometrix thematic maps).
- **First run (2026-08-30):** OpenAlex 15 queries (5,936 works) + arXiv 5 queries (462 preprints) → 6,398 in → −1,167 repository deposits → −69 duplicates → **corpus 5,139**. Lifecycle stage-hit profile independently reproduces the Track B output bias: data management 50.8% and analysis/workflow 41.9% dominate; idea/question 3.7% and provenance 7.0% are lowest.
- **Open refinements:** decide whether to trim the 2025 tail (indexing recency: 901 vs 529 in 2024) for trend claims; tighten the broad `"open science"` and `github` queries if precision is low on manual inspection; run the PRISMA screen from this corpus to the deep subset if expanding requirement extraction.
- **Affects:** `search_strings.md`; `search_log.md`; `PHASE2_PROGRESS.md`; `RESEARCH_DESIGN.md` §9; `LITERATURE_REVIEW.md` §5.1; `analysis/`, `data/`, `results/track_a/`.

---

## D9 — Research Management Requirements Framework: final set RM1–RM15

- **Date:** 2026-08-30
- **Context:** Phase 3 turns the 17 literature-extraction rows (RE01–RE17) into a defined, classified requirement set. The provisional list in `REQUIREMENTS_FRAMEWORKS.md` had 14 domains (RM1–RM14).
- **Decision:** Adopt **RM1–RM15** as the framework (`framework/requirements/requirements_framework.csv`). Changes from the provisional set:
  - RM9 "Research artifact management" → "…and integration" (absorbs RE09, integration across heterogeneous tools — the most-cited literature challenge).
  - RM10 "Research provenance" → "…and artifact linkage" (absorbs RE11).
  - RM14 "Research output management" → "…and identification" (absorbs RE15: PIDs, interoperable metadata).
  - **RM15 Governance and sustainability** added (RE17); flagged as only partly in scope per `PHASE1_PROJECT_DEFINITION.md` §6.3.
  - All 14 provisional definitions rewritten to be testable, each with an `expected_capabilities` field (the hook for the Phase 5 mapping).
  - `differentiator = yes` flag introduced for **RM1, RM2, RM5** — High importance despite weak literature attention (the upstream planning / research-question / decision-traceability gap the study targets).
- **Rationale:** the extraction evidence did not fit 14 clean domains — integration, artifact linkage and interoperability were distinct enough to name explicitly, and governance recurred often enough to record even though it is largely institutional. The differentiator flag makes the paper's central argument checkable against the framework itself.
- **Importance scale:** High / Medium-High / Medium / Low-Medium, assigned from evidence weight, centrality in the relationship model, and (for the differentiators) the size of the literature gap.
- **Not done:** second-coder check on the RE→RM assignment — deferred (single-coder project), declared as a limitation.
- **Affects:** `framework/requirements/`; `REQUIREMENTS_FRAMEWORKS.md` (now a method doc; the artifact is authoritative); `PHASE3_PROGRESS.md`; `analysis/scripts/summarise_requirements.py`; `results/framework/`.

---

## D10 — GitHub capability catalogue: native-only scope, 12 groups

- **Date:** 2026-08-30
- **Context:** Phase 4 catalogues GitHub functionality for the Phase 5 requirement mapping.
- **Decision:** Adopt `framework/mapping/github_capability_catalogue.csv` — **68 capabilities (GC01–GC68)** in **12 feature groups** GF1–GF12. Rules:
  - **Native only.** Excluded: GitHub Marketplace apps and third-party GitHub Apps, Copilot, API-only capabilities without a UI surface, Enterprise-server-only administration.
  - **One kept exception:** the GitHub–Zenodo release webhook (GC61) — a third-party service, but the canonical bridge for persistent identification and preservation, and the link to the prior GitHub–Zenodo–ORCID workflow.
  - Capabilities are catalogued at finer grain than the GF1–GF11 groups in `GITHUB_FEATURE_MAPPING.md` (e.g. Issues → issue, forms, types, sub-issues, assignees, cross-references, closing keywords, timeline, reactions, pinned). A 12th group (GF12 Access, identity & meta) was added for permissions, visibility, forks, insights, audit log and Dependabot.
  - Each row records `plan_availability` and `practical_complexity`; `candidate_requirements` is a **Phase-4 hint** at which RM(s) a capability might serve, explicitly not the Phase-5 support score.
- **Rationale:** native-only keeps the framework reproducible by any researcher on a standard account; finer grain makes the Phase 5 mapping a near-mechanical join on `expected_capabilities`.
- **Affects:** `framework/mapping/`; `GITHUB_FEATURE_MAPPING.md` (now method for Phases 4–5); `PHASE4_PROGRESS.md`; `analysis/scripts/summarise_capabilities.py`; `results/framework/`.

---

## D11 — Requirement–feature mapping: per-requirement support scores

- **Date:** 2026-08-30
- **Context:** Phase 5 grades GitHub's support for RM1–RM15 for RQ3.
- **Decision:** Score **one support level per requirement** — the best level GitHub's native functionality can reach with a reasonable implementation pattern — using the four-level rubric (Direct 3 / Partial 2 / Limited 1 / Not supported 0). Recorded in `framework/mapping/requirement_feature_matrix.csv` with primary capabilities, contributing feature groups (weighted), a concrete implementation pattern, an evidence note, external-tool dependencies and the residual gap. Per-cell RM×capability scoring was rejected as 15×68 with little added insight; the RM×feature-group contribution matrix (`coverage_group_matrix.csv`) is derived from the `contributing_groups` field instead.
- **Scores:** Direct RM3, RM4, RM6, RM7, RM8, RM11, RM13 (7); Partial RM1, RM5, RM9, RM10, RM12, RM14 (6); Limited RM2, RM15 (2); none Not supported. Overall mean **2.33/3**.
- **Key findings:** (a) Direct where research work resembles software engineering; Partial/Limited for research-specific traceability of questions/decisions/provenance and for planning/governance. (b) Differentiators RM1/RM2/RM5 mean **1.67** vs **2.50** for the rest — the upstream gap is real on the tool side, matching RQ1. (c) **5 requirements need external tools** (RM8, RM9, RM12, RM14, RM15). (d) Issues + Git repository carry most of the framework.
- **Note on "no 0s":** nothing is scored Not supported because every requirement has *some* workable pattern; the honesty is carried by the two Limited scores, the convention caveats in the evidence notes, and the external-tool column. A stricter-rubric sensitivity check is listed as optional.
- **Also:** `requirements_framework.csv` `github_support` column back-filled with the Phase 5 label.
- **Affects:** `framework/mapping/`; `framework/requirements/requirements_framework.csv`; `PHASE5_PROGRESS.md`; `analysis/scripts/coverage_indicators.py`; `results/framework/`; `FIGURES_AND_TABLES.md` (Table 2 produced).

---

## D12 — Reference architecture: 15 components, 5 layers, conventions as first-class

- **Date:** 2026-08-30
- **Context:** Phase 6 turns the Phase 5 coverage assessment into a buildable framework.
- **Decision:** Adopt a **15-component, 5-layer** architecture (`framework/architecture/architecture_components.csv`): Coordination (A1–A4), Record (B1–B4), Production (C1–C3), Release (D1–D3), Cross-cutting (X1). Each component is one GitHub configuration serving a named set of RMs. Plus `workflows.csv` (7 workflows) and `lifecycle_model.csv` (12 stages). Key choices:
  - **B3 Linkage Discipline** (cross-references + closing keywords + timeline) is a named component and the keystone — a mandatory practice, not a feature.
  - The **four conventions** that lift RM1 (phased-plan), RM2 (question register), RM5 (decision-record) and RM10 (linkage discipline) from Partial/Limited toward research-usable are **part of the architecture**, specified in `reference_architecture.md` §4, not left implicit.
  - **Boundary rule:** at every external-tool boundary (large data, containers, DOI/preservation, institutional governance) the repository holds a durable versioned **reference** (URL/DOI/id), never the artifact.
  - Design stance retained from `RESEARCH_DESIGN.md`: GitHub is a coordination and traceability layer, not a container.
- **Rationale:** a small named component set makes the framework teachable, checkable (every RM served, no idle component — verified by `summarise_architecture.py`) and directly operationalisable as the Phase 7 template.
- **Affects:** `framework/architecture/`; `REFERENCE_ARCHITECTURE.md` (draft; the built artifact is authoritative); `PHASE6_PROGRESS.md`; `analysis/scripts/summarise_architecture.py`; `results/framework/`; `FIGURES_AND_TABLES.md` (Table 3, Figures 3–4).

---

## D13 — Reusable template: 33 files, config-only components, two-repo strategy

- **Date:** 2026-08-30
- **Context:** Phase 7 operationalises the reference architecture (D12) as a GitHub template.
- **Decision:** Build `template/github-research-project-template/` — **33 files** mapped in `template/template_manifest.csv` to the 15 architecture components and RM1–RM15. Choices:
  - **Config-only components:** A1, A2 (GitHub Project + fields, not file-expressible → documented in `.github/project-fields.md`), D2 (Zenodo webhook → `release-checklist.md`), X1 (public visibility → a governance decision). Every other component has ≥1 template file; verified by `analysis/scripts/check_template.py`.
  - The **four architecture conventions** are made enforceable through `docs/conventions.md`, the three issue forms, the PR template, `CONTRIBUTING.md` and the `validate-structure` Action.
  - **Starter Actions kept generic** (`validate-structure` fully working; `markdown-link-check` via a public action; `reproduce` a matrix stub with adaptation notes) — the template must run for any discipline out of the box.
  - **Large data excluded** by `.gitignore` and the `data/external/` pointer convention.
  - **Two-repository strategy** (from `REPOSITORY_ARCHITECTURE.md`): the template lives inside the study repo for development/evaluation; it is extracted as an independent GitHub template repository at Phase 12.
- **Affects:** `template/`; `TEMPLATE_PROJECT.md` (draft; the built template is authoritative); `PHASE7_PROGRESS.md`; `analysis/scripts/check_template.py`; `results/framework/`; `FIGURES_AND_TABLES.md` (Table 4).

---

## D14 — Case study executed self-referentially; coordination layer specified but not exercised

- **Date:** 2026-08-30
- **Context:** Phase 8 applies the framework (D5: self-referential + template). Phases 1–7 were done as a single-author working sprint, so the GitHub-native Issue / Project / Pull Request / Release layer was never used during the study.
- **Decision:** Record the case study honestly as a **document-and-git implementation** of the framework:
  - `case-study/implementation_record.csv` classifies each architecture component as native / partial / config / retrospective / planned.
  - `case-study/activity_register.csv` **reconstructs** the RQ / milestone / task / decision register that would have been GitHub Issues (5 RQs, 8 milestones, 16 tasks, 14 decisions) — labelled as a reconstruction, not lived history.
  - Framework configuration (`.github/` issue forms, PR template, labels, project-fields, `validate-structure` workflow, `docs/conventions.md`, `CONTRIBUTING.md`, `LICENSE`) is **added to this repository** now (task T16) so it is available going forward.
  - The un-exercised components (A4, D1, D2, X1) and the requirements they serve (RM6, RM7, RM14, RM15) are scored in Phase 9 on **design support**, not observed use, and flagged.
- **Rationale:** fabricating an Issue/PR history would be dishonest and circular. The genuine result — the record/decision/version-control spine works with near-zero overhead while the coordination layer was not adopted solo — is itself informative and becomes the study's main practical limitation and a clear future-work direction (multi-author, multi-project evaluation).
- **Affects:** `case-study/`; `.github/`; `docs/conventions.md`; `CONTRIBUTING.md`; `LICENSE`; `CASE_STUDY.md` (draft; `case-study/` is the record); `PHASE8_PROGRESS.md`; `analysis/scripts/summarise_case_study.py`; `EVALUATION_PROTOCOL.md` (Phase 9 scores design support where use is absent).

---

## D15 — Evaluation: 0/1/2 per sub-dimension with an explicit basis tag

- **Date:** 2026-08-30
- **Context:** Phase 9 scores the six evaluation dimensions (`EVALUATION_PROTOCOL.md`). The single-author self-referential case (D14) means several dimensions cannot be scored on observed use.
- **Decision:** Score **21 sub-dimensions** across E1–E6 on the protocol's 0/1/2 scale (`case-study/evaluation_scores.csv`), each tagged with its **basis**: `observed` (17), `retrospective` (1), `design-support` (2), `planned` (1). E1 additionally uses the quantitative Phase 5 coverage (13/15 supported). Report both the **overall mean 1.62/2** and the **observed-only mean 1.76/2**. Un-exercised dimensions (notably E5 external visibility = 0, pending public release) are scored on design support and flagged, not omitted or inflated.
- **Rationale:** transparent basis tags let a reviewer see exactly which scores rest on the actual repository and which on the framework's design; reporting the observed-only figure alongside the overall prevents the planned/design items from either deflating or hiding the realised result.
- **Results:** E1 2.00, E3 2.00, E4 1.75, E2 1.50, E5 1.50, E6 1.25. Table 6 (`workflow_comparison.csv`) contrasts the fragmented workflow with the framework across 6 dimensions.
- **Affects:** `case-study/evaluation_scores.csv`, `workflow_comparison.csv`, `evaluation.md`; `EVALUATION_PROTOCOL.md` (draft; `case-study/evaluation.md` is the record); `PHASE9_PROGRESS.md`; `analysis/scripts/evaluation_summary.py`; `results/framework/`; `FIGURES_AND_TABLES.md` (Tables 5–6).
