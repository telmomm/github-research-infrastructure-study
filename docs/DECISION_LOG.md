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
