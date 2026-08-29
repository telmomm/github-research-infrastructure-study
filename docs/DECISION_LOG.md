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
