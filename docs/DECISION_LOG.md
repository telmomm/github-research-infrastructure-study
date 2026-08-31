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

---

## D16 — 2025 tail kept in the production trend, with a caveat and a trimmed series

- **Date:** 2026-08-30 · **Closes:** OPEN_ITEMS 2.3
- **Context:** The Track A corpus shows 1,030 works dated 2025 vs 585 in 2024 — a spike driven by OpenAlex indexing recency, not a real doubling of output.
- **Decision:** Keep 2025 in the corpus and in the production figure, annotated as **partially indexed**. Report a **2008–2024 trimmed series** alongside for any growth-rate statement (`results/track_a/annual_production_trimmed.csv`). Do not compute a CAGR that ends in 2025.
- **Rationale:** dropping 2025 loses genuine recent work; keeping it unannotated invites a misreading. The trimmed series carries the trend claim.
- **Affects:** `PHASE2_PROGRESS.md`; `results/track_a/`; the manuscript RQ1 figure caption.

---

## D17 — RM15 kept in the framework, excluded from headline coverage

- **Date:** 2026-08-30 · **Closes:** OPEN_ITEMS 3.2
- **Context:** RM15 (governance and sustainability) is flagged since D9 as only partly in scope; Phase 5 scored it Limited (1), and most of the requirement (funding, workforce, institutional continuity) is not a platform matter.
- **Decision:** **Keep RM15** in `requirements_framework.csv` and the architecture (component D3) for completeness, but report **headline coverage for the core 14** (mean 2.43/3) as well as the full 15 (mean 2.33/3). `coverage_indicators.py` now emits both. The manuscript leads with the core-14 figure and notes RM15 separately.
- **Rationale:** removing RM15 would hide a real, literature-attested need; letting it drag the headline number understates GitHub's support for the requirements that are actually in scope.
- **Affects:** `analysis/scripts/coverage_indicators.py`; `framework/mapping/coverage_analysis.md`; `PHASE3_PROGRESS.md`, `PHASE5_PROGRESS.md`; the manuscript RQ3 results.

---

## D18 — Coverage-score sensitivity check (strict rubric)

- **Date:** 2026-08-30 · **Closes:** OPEN_ITEMS 5.1
- **Context:** Phase 5 scored several requirements Partial where the support is a mandatory convention on a generic feature; a reviewer could argue those should be Limited.
- **Decision:** Add `framework/mapping/requirement_feature_matrix_strict.csv` — a stricter variant capping convention-heavy support (RM1, RM5, RM10) at Limited — and `coverage_indicators.py --strict`. Result: overall mean **2.33 → 2.13** (core-14 2.43 → 2.21); distribution 7 Direct / 3 Partial / 5 Limited / 0 Not supported. The qualitative conclusion (Direct where research resembles software work; Limited for upstream research-specific traceability) is unchanged under both rubrics.
- **Rationale:** shows the headline finding is not an artefact of a generous rubric.
- **Affects:** `analysis/scripts/coverage_indicators.py`; `framework/mapping/`; `results/framework/coverage_*_strict.*`; the manuscript methods/robustness note.

---

## D19 — Phase 10 synthesis: 32 typed findings with verifiable evidence

- **Date:** 2026-08-30
- **Context:** Phase 10 integrates RQ1–RQ5 for the manuscript.
- **Decision:** Record the synthesis as **`analysis/findings.csv`** — 32 findings (F01–F32), each tagged with its RQ, a **type** (result / limitation / implication), a **strength** (strong / moderate), a one-sentence statement, and **evidence paths** that `analysis/scripts/synthesis_check.py` verifies exist. `analysis/synthesis.md` is the narrative. `findings.csv` rows are pre-mapped to manuscript sections.
- **Central analytical claim:** the RQ1 literature gap and the RQ3 coverage gap are the same gap reached independently; GitHub is a coordination/traceability *layer*, systematically strong execution-to-output and weak upstream.
- **Rationale:** a typed, evidence-linked finding list keeps the Discussion honest (limitations and implications are first-class, not an afterthought) and makes Phase 11 a mechanical assembly rather than a fresh argument.
- **Affects:** `analysis/synthesis.md`, `analysis/findings.csv`; `PHASE10_PROGRESS.md`; `analysis/scripts/synthesis_check.py`; `results/framework/synthesis_*`; the manuscript Results and Discussion.

---

## D20 — Manuscript: hybrid structure, assembled from `findings.csv`

- **Date:** 2026-08-30
- **Context:** Phase 11 writes the *Scientometrics* manuscript (`sn-jnl`, sn-mathphys-num).
- **Decision:** Write `manuscript/paper.tex` as a complete v1 draft on the hybrid structure fixed in `PHASE1_PROJECT_DEFINITION.md` §9 (Introduction; Materials and Methods; Results 3.1 bibliometric map / 3.2 requirements + coverage / 3.3 architecture + template + feasibility; Discussion; Conclusions), with each Results/Discussion paragraph traceable to rows of `analysis/findings.csv`. Four tables (lifecycle stage-hits, RM1–RM15 + support, coverage by category + differentiators, evaluation) and three figures (co-word map, architecture, traceability path). `manuscript/references.bib` = the 52 `literature/references.bib` entries plus 10 primary GitHub-in-research studies actually cited. Figures rendered SVG→PDF with `rsvg-convert` via `manuscript/build.sh`.
- **Rationale:** driving the prose from a typed, evidence-linked finding list keeps the claims aligned with the artifacts and makes the draft auditable against `xray`/`factcheck`.
- **Status:** compiles clean (0 undefined citations/references, 16 pp.); ~6,000 words of body — expansion candidates listed in `PHASE11_PROGRESS.md`.
- **Affects:** `manuscript/`; `PHASE11_PROGRESS.md`; `PAPER_PLAN.md` (design input; `paper.tex` is now the artifact); `FIGURES_AND_TABLES.md`.

---

## D21 — Release v1.0.0

- **Date:** 2026-08-30
- **Context:** Roadmap Phases 1–11 are complete: the requirements framework, capability catalogue and coverage mapping, reference architecture, reusable template, self-referential case study, six-dimension evaluation, RQ1–RQ5 synthesis, and a complete v1 *Scientometrics* manuscript that compiles clean. All closeable open items (`OPEN_ITEMS.md`) are closed.
- **Decision:** Cut **v1.0.0**. `CHANGELOG.md` `[Unreleased]` promoted to `[1.0.0] — 2026-08-30`; `CITATION.cff` `version: 1.0.0`. This is the pre-submission research snapshot: it answers RQ1–RQ5 and packages every artifact needed to reproduce the study.
- **Not in v1.0.0 (Phase 12):** the three pre-submission user-tasks (make the repository public, run one live Issue→PR→Release cycle, screenshot the Project), the Zenodo archive and DOI, the manuscript body expansion toward ~8,000 words, and the full `references.bib` check for the cited subset. These land in a later 1.x release.
- **Rationale:** the scientific contribution is done and self-contained; tagging it fixes a citable state before the outward-facing publication steps, which depend on actions outside this working session.
- **Affects:** `CHANGELOG.md`; `CITATION.cff`; `ROADMAP.md`; git tag `v1.0.0`.

---

## D22 — Repository made public

- **Date:** 2026-08-30 · **Closes:** GitHub issue #4
- **Context:** The self-referential design (`D5`, `D14`) scored the Transparency dimension (E5) on *internal* visibility because the repository was private during the work; `X1 Transparency Surface` was `planned`. Making the repository public is the governance decision that enacts the "private during the work, public at publication" policy.
- **Pre-public checklist (verified):** no secrets or tokens in history (`git log -p` scan; `.claude/` untracked since D-note in `.gitignore`); no embargoed or third-party-restricted material (the corpus is bibliographic metadata; `SOTA/SOTA.md` is a Consensus export used under its personal-use terms and cited, not redistributed as a product); licensing in place (`LICENSES/`, `REUSE.toml`, D7.1); raw API dumps `.gitignore`d, only the reproducible `data/processed/corpus.csv` tracked.
- **Decision:** Set repository visibility to **public**. This enacts E5 external visibility, enables third-party inspection of the full history for RQ5, and is a precondition for issue #3 (re-score E5/E6) and issue #5 (Zenodo DOI wiring).
- **Not done here:** GitHub Pages summary page and Insights write-up (`X1` stays `partial`); the E5/E6 re-score (issue #3).
- **Affects:** repository settings; `case-study/implementation_record.csv` (X1 `planned` → `partial`, D3 `config` → `partial`); `results/framework/cs_*`; `docs/OPEN_ITEMS.md`.

---

## D23 — Evaluation re-score after the repository was made public and one live cycle was run

- **Date:** 2026-08-30 · **Closes:** GitHub issue #3
- **Context:** In `D15` four evaluation sub-scores were tagged *planned* / *retrospective* / *design-support* because Phases 1–11 were a single-author sprint with the coordination layer only configured. `D22` (repo public) and issue #2 (one full Issue→branch→PR→merge→Release cycle over the study's backlog) removed those preconditions.
- **Decision:** Re-score four sub-scores in `case-study/evaluation_scores.csv` on observed evidence:
  - **E5 external project visibility** `0` (planned) → `2` (observed) — repository public, full history / docs / Insights / Project #2 third-party inspectable.
  - **E2 task traceability** `1` (retrospective) → `2` (observed) — real GitHub Issues #1–#12 cross-referenced; one full coordination cycle demonstrated.
  - **E4 task categorization** `1` (design-support) → `2` (observed) — the activity label set applied to Issues #1–#12.
  - **E6 workflow overhead** `1` → `2` (observed) — the Issue/PR/Release layer run once end-to-end; per-item overhead modest solo.
- **Result:** dimension means E1 2.00, E2 1.75, E3 2.00, E4 2.00, E5 2.00, E6 1.50. **Overall 1.62 → 1.86 / 2** (observed-only 1.76 → 1.85, n 17 → 20).
- **Unchanged / still limiting:** E6 configuration complexity and technical-literacy (1 each); E2 provenance/artifact linkage (1 — one chain demonstrated, no automated lineage); the coordination layer's **collaborative** value (multi-author review, communication) remains untested.
- **Affects:** `case-study/evaluation_scores.csv`, `case-study/evaluation.md`; `results/framework/eval_*`; `analysis/findings.csv` (F21), `analysis/synthesis.md`; `docs/PHASE9_PROGRESS.md`, `docs/OPEN_ITEMS.md`. **`manuscript/paper.tex` still carries the pre-re-score figures (Abstract, Results §3.3, Table 4, Methods §2.7, Limitations §4.6) and is updated in the manuscript pass (issue #6).**

---

## D24 — Scopus / Web of Science coverage cross-check executed

- **Date:** 2026-09-30 · **Closes:** GitHub issue #11 · OPEN_ITEMS 2.8
- **Context:** `D8` executed Track A on OpenAlex + arXiv and declared the coverage/precision trade-off versus Scopus/WoS as a limitation. Institutional access (FECYT) later became available, so the trade-off was measured rather than only asserted.
- **Method:** the frozen `search_strings.md` queries Q1–Q4 were run in Web of Science (`TS=`, Full Record tab-delimited, ≤1,000-row batches) and Scopus (`TITLE-ABS-KEY` + `DOCTYPE(ar|re|cp)`, CSV), window 2008–2025. Raw exports (`data/raw/{wos,scopus}/`, `.gitignore`d) → `analysis/scripts/scopus_wos_crosscheck.py`.
- **Result:** 18,250 raw → **13,586 de-duplicated in-window** records. Overlap with the OpenAlex + arXiv corpus: **22 % (2,933; 2,656 by DOI)**. Not in the corpus: 10,653; 2,175 corpus records not returned by these queries (OpenAlex indexes preprints and OA venues).
- **Interpretation:** the divergence is dominated by Q3 (`"version control" OR git OR github OR gitlab`), 88 % of whose records are not in the corpus, and by WoS *Topic* also matching Keywords Plus / author keywords. The not-in-corpus set is concentrated in recent bioinformatics and CS tool papers that cite a GitHub repository and mention "workflow"/"reproducibility" (top venues: *Bioinformatics*, *BMC Bioinformatics*, LNCS, *PLoS ONE*) — the low-precision tail a title/abstract-anchored search deliberately excludes, not missed core literature on research-process infrastructure.
- **Decision:** OpenAlex + arXiv stays the primary Track A corpus; the cross-check is reported as evidence for that choice, not a reason to re-run. `OPEN_ITEMS.md` 2.8 moves from *limitation* to *closed*; the `manuscript/paper.tex` wording in Methods §2.2 and Limitations §4.6 is updated in the manuscript pass (issue #6) from "not used, a limitation" to "cross-checked; 22 % DOI overlap; the delta is a characterised precision tail".
- **Affects:** `literature/search_log.md`; `results/track_a/scopus_wos_crosscheck.md`, `xref_not_in_corpus.csv.gz`; `analysis/scripts/scopus_wos_crosscheck.py`; `.gitignore`; `docs/OPEN_ITEMS.md`; the companion Zenodo dataset record <https://doi.org/10.5281/zenodo.22173525> (raw WoS/Scopus/OpenAlex/arXiv exports + processed datasets, `isSupplementTo` the software DOI); (deferred) `manuscript/paper.tex`, `analysis/findings.csv` F26.

---

## D25 — Template external validity tested by retrospective instantiation on a second project

- **Date:** 2026-08-30 · **Closes:** GitHub issue #12 · OPEN_ITEMS 8.2
- **Context:** The reusable template (`D19`, Phase 7) and the case study (`D5`, `D14`, Phase 8) were both exercised only on this study's own meta-research repository. OPEN_ITEMS 8.2 held a second-project instantiation as *future work*. RQ4/RQ5 need some evidence that the framework's structure is not specific to scientometrics.
- **Target:** *PreMoCir* — a completed, published clinical-machine-learning project by the same lead author (mortality prediction in cardiac surgery with SHAP explainability and a decision-support web app), *Sensors* **26**(5):1656, 2026; 3 Jupyter notebooks archived at Zenodo `10.5281/zenodo.18249069` (CC-BY-4.0); underlying data a retrospective clinical cohort held under a data-use agreement. Discipline unrelated to this study.
- **Method:** a structural / coverage test, not a usability test. For each requirement RM1–RM15 and each template component, ask whether a repository created from the template would have served it, and by what mechanism — scored **covered** (native feature/file), **convention** (served only if the linkage/decision conventions are followed; not exercised here), or **external** (needs an out-of-repo system). Recorded in `case-study/external_validity_mapping.csv`; tallied by `analysis/scripts/summarise_external_validity.py`.
- **Result:** **8 covered** (RM1–RM5, RM8, RM10, RM14), **3 convention** (RM6, RM7, RM13), **4 external** (RM9, RM11, RM12, RM15) — the same coverage profile as the self-referential case. RM14 (output identification / release-then-archive) maps 1:1 to what PreMoCir already did. The external set is external for the same reasons as in the main study, plus that the clinical data blocker is *access restriction* (DUA), not size, which stresses the `data/external/` pointer and the RM11 embargo caveat harder; RM15's institutional part (IRB, hospital data governance) is heavier.
- **Decision:** the template transfers to an unrelated discipline with an unchanged coverage/boundary profile — reported as support for the discipline-independence claim in `case-study/external_validity.md`. OPEN_ITEMS 8.2 moves *future-work* → *closed*.
- **Limitations:** retrospective, single additional case, same lead author, no live use with the clinical co-authors — tests structural/coverage transfer only. A *prospective* instantiation on an in-progress project stays as future work (`case-study/external_validity.md` §5).
- **Affects:** `case-study/external_validity.md`, `case-study/external_validity_mapping.csv`; `analysis/scripts/summarise_external_validity.py`, `results/framework/external_validity_summary.md`; `analysis/README.md`; `docs/OPEN_ITEMS.md`. Manuscript RQ4/RQ5 and Future Research wording (deferred to issue #6).

---

## D26 — Second-coding reliability check (LLM re-code) for the coded framework decisions

- **Date:** 2026-08-31 · **Closes (mitigates):** GitHub issue #10 · OPEN_ITEMS 2.7, 3.1, 5.2, 9.1
- **Context:** Four open items were declared a single-coder limitation: no independent rater checked the RE→RM assignment (17), the requirement support levels (15) or the evaluation sub-scores (21). No second human coder was available. `D15`/`D23` set the scores; nothing tested their stability under an independent read.
- **Decision:** run an **independent LLM re-code** (Claude) of *all* 53 coded decisions — full re-code, not a 20% sample, the framework being small enough — from the same source materials and rubric, then compare. Report percent agreement and Cohen's κ (nominal for RE→RM, linearly-weighted for the ordinal units). Keep the author's codes; adjudicate disagreements in the open.
- **Result:** pooled exact agreement **96.2%** (51/53). By unit: RE→RM 94.1%, κ 0.94; support levels 100%, κ 1.00; evaluation sub-scores 95.2%, κ 0.83 (deflated by skewed all-"2" marginals — the Cicchetti–Feinstein paradox; percent agreement is the more informative statistic there). Two adjacent-category disagreements: **RE11** RM10 vs RM9 (kept RM10; no coverage count changes) and **E6 workflow overhead** 2 vs 1 (kept 2; adopting the stricter code moves Overall only 1.86 → 1.81, dimension ranking unchanged). Five further agreed codes flagged as boundary calls.
- **Framing:** this is a **partial mitigation, not human inter-rater reliability** — the LLM had prior repository exposure (not fully blind), and the support-level unit is the least independent because the matrix documents its own Direct/Partial/Limited rationale. The single-coder limitation therefore *stands as declared* in the manuscript, now qualified by a measured robustness check. OPEN_ITEMS 2.7/3.1/5.2/9.1 move *limitation* → *limitation (mitigated)*.
- **Alternatives:** intra-rater test–retest (same coder, same biases; needs a washout the compressed build cannot provide); publish the rubric only and leave the items as pure limitations (rejected as weaker — a re-code, even LLM, is concrete evidence of rubric-consistency).
- **Affects:** `case-study/reliability_check.md`, `case-study/reliability_check.csv`; `analysis/scripts/reliability_summary.py`, `results/framework/reliability_summary.md`; `analysis/README.md`; `case-study/evaluation.md` §1/§6; `docs/OPEN_ITEMS.md`. Manuscript Limitations wording (deferred to issue #6): "single coder; an independent LLM re-code of all 53 coded decisions agreed at 96.2%, κ 0.83–1.00, changing no reported conclusion".

---

## D27 — Manuscript reconciled and expanded for submission

- **Date:** 2026-08-31 · **Closes:** GitHub issues #5, #6, #7 (with #8, #9) · OPEN_ITEMS 12.2–12.4
- **Context:** `manuscript/paper.tex` still carried pre-re-score figures and the "Scopus/WoS not used" framing; `D23`, `D24`, `D25`, `D26` each deferred their manuscript wording to this pass. The body was also short (~3.7k words) and thin on related work and per-requirement detail (issue #6).
- **Decision:** execute the deferred edits and a bounded expansion in one manuscript pass:
  - **Figures reconciled** — evaluation overall 1.62 → **1.86** (observed-only, n=20, **1.85**); components exercised 8/15 → **13/15**; usability 1.25 → **1.50**; E2 1.50→1.75, E4 1.75→2.00, E5 1.50→2.00; Table 4 and its caption; Abstract, Results §3.3, Methods §2.7, Discussion §4.2 ("nineteen"→"twenty-six" logged decisions), Limitations.
  - **Scopus/WoS** (`D24`) — Methods §2.2 and Limitations changed from "not used, a limitation" to "cross-checked; 18,250 raw records; 22% DOI overlap; characterised precision tail".
  - **External validity** (`D25`) — new Results §3.3 paragraph and a Future-research sentence (retrospective single-case done; prospective multi-author instantiation is the next step).
  - **Reliability re-code** (`D26`) — Methods §2.3 and Limitations note the 96% / κ 0.83–1.00 re-code and that it leaves every figure unchanged.
  - **DOIs** (issue #5) — data-availability statement cites the software DOI `10.5281/zenodo.22167500` and dataset DOI `10.5281/zenodo.22173525`; matches `CITATION.cff` and the README badge.
  - **References** (issue #7) — all 24 cited entries verified against Crossref; `chen2025` issue 3→2; 15 entries gained missing `number`/`pages`; 4 entries added for the new related-work text, also Crossref-checked.
  - **Expansion** (issue #6) — new §1.4 "Prior reviews, by strand"; expanded Methods §2.2/§2.3; a per-requirement narrative in Results §3.2. Body 3.7k → **4.9k words**, 19 pp., `latexmk` clean (bibtex 0 warnings, no undefined citations). Not padded to a literal 8k — *Scientometrics* sets no minimum and further depth would be unsupported prose; revisited against the author guidelines in issue #9.
- **Affects:** `manuscript/paper.tex`, `manuscript/references.bib`; `analysis/findings.csv` (F26); `literature/references_factcheck.md`; `docs/OPEN_ITEMS.md`. Figures 3 & 4 redrawn to a common palette (issue #8): `fig3_architecture.svg` restyled by the author, `fig4_traceability.svg` rebuilt to match; both render as clean vector PDF via `rsvg-convert` in `build.sh`.
