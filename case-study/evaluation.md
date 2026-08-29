# Framework Evaluation

**Phase 9 deliverable** (roadmap step 9 of 12) · Answers **RQ5**
**Protocol:** `docs/EVALUATION_PROTOCOL.md` · **Evidence:** `case-study/implementation_record.csv`, `activity_register.csv`, `traceability_examples.md`
**Artifacts:** `evaluation_scores.csv` (21 sub-dimensions), `workflow_comparison.csv` (Table 6) · **Decisions:** `docs/DECISION_LOG.md` D15

---

## 1. Method

The six dimensions of `EVALUATION_PROTOCOL.md` are each scored **0 (not supported) / 1 (partially) / 2 (fully)**, broken into sub-dimensions. Every sub-score records its **basis**:

- **observed** — evidenced by the actual state of this repository (17 of 21 sub-scores);
- **retrospective** — evidenced by the reconstructed register, not lived (1);
- **design-support** — the framework provides the mechanism but it was not exercised (2);
- **planned** — deferred to Phase 12 (1).

E1 also uses the quantitative coverage from the Phase 5 mapping.

## 2. Results

| Dim | Dimension | Score /2 | % | Basis |
|---|---|---|---|---|
| E1 | Requirement coverage | **2.00** | 100% | design-support (Phase 5) |
| E2 | Traceability | **1.50** | 75% | mostly observed |
| E3 | Documentation | **2.00** | 100% | observed |
| E4 | Organization | **1.75** | 88% | observed |
| E5 | Transparency | **1.50** | 75% | observed; external visibility planned |
| E6 | Usability | **1.25** | 62% | observed |
| | **Overall** | **1.62** | **81%** | (observed-only: 1.76 / 88%) |

## 3. Dimension by dimension

### E1 — Requirement coverage (2.00)

From `framework/mapping/requirement_feature_matrix.csv`: **13 of 15** requirements are supported at Partial or better (7 Direct, 6 Partial); mean 2.33/3. The two Limited are **RM2** (research-question management — a differentiator) and **RM15** (governance — declared partly out of scope). No requirement is unsupported.

### E2 — Traceability (1.50)

| Sub-dimension | Score | Basis |
|---|---|---|
| Decision traceability | 2 | observed — `DECISION_LOG.md` D1–D15, each with rationale, alternatives and an *Affects* line |
| Version traceability | 2 | observed — Git history, phase-scoped commits; `corpus.csv` reproducible. Release-level (tags) not yet exercised |
| Task traceability | 1 | retrospective — reconstructed in `activity_register.csv`; links are document references, not lived Issue cross-references |
| Provenance / artifact linkage | 1 | observed — document-level linkage works and is machine-checked (`summarise_*` verify RE→RM→GC→component), but manual, no lineage query, no Issue/PR chain |

Decision and version traceability are the framework's realised strengths; task-level and provenance linkage need the Issue/PR layer that the solo sprint did not use.

### E3 — Documentation (2.00)

Protocol (`RESEARCH_DESIGN.md`, `LITERATURE_REVIEW.md`), per-phase methodology (`PHASE1–9_PROGRESS.md`, framework narratives), decisions (`DECISION_LOG.md`) and roadmap (`ROADMAP.md`, `CHANGELOG.md`) are all systematically documented from project start — 23 `docs/` files plus folder READMEs. The framework's clearest success.

### E4 — Organization (1.75)

Repository structure (enforced by `validate-structure.yml`), research-phase identification (12-stage lifecycle, milestones M1–M8) and folder-level artifact classification are fully realised (2). **Task categorization** scores 1: the 12-label activity taxonomy (`.github/labels.yml`) is defined but was not applied as GitHub Issue labels.

### E5 — Transparency (1.50)

Accessible documentation, visible history and traceable decisions all score 2. **External project visibility scores 0**: the repository is not yet public and no Project board / Insights are in use. Everything needed for a third-party view is in place; the dimension reaches 2 on public release (Phase 12).

### E6 — Usability (1.25)

| Sub-dimension | Score | Note |
|---|---|---|
| Maintenance effort | 2 | scripts regenerate every `results/` table; layout guarded by CI |
| Configuration complexity | 1 | `Use this template` + placeholders is quick, but Project/labels/Actions setup is manual |
| Technical knowledge | 1 | Git + Markdown + YAML literacy assumed — a real barrier outside computational fields |
| Workflow overhead | 1 | the documentation/decision/version-control spine was near-zero-overhead solo; the Issue/PR coordination layer was not adopted under solo-sprint conditions |

The lowest-scoring dimension, and the honest one: the framework is practical for a technically literate researcher, its light layer is sustainable, and its coordination overhead is real and unadopted solo.

## 4. Conventional-workflow comparison (Table 6)

`workflow_comparison.csv`. Summary: the framework's benefit is concentrated in **linking artifacts that a fragmented workflow (email + documents + local files + separate tools) leaves disconnected** — decision rationale, version history, and the question→data→analysis→result chain become reconstructable. Its cost is concentrated in the **coordination layer** (Issues, PRs, Project), and its weak points (upstream planning, research-question tracking, decision traceability) coincide with the thinnest areas of the literature (RQ1).

## 5. Observations

1. The framework realises a **document / decision / version-control spine** that a fragmented workflow lacks, at near-zero overhead — this is its robust contribution.
2. The **coordination layer pays off with collaborators and is optional for a solo author**; the self-referential case could not test the collaborative benefit.
3. GitHub is a **coordination and traceability layer, not a complete research infrastructure**: five requirements (RM8, RM9, RM12, RM14, RM15) need complementary external systems.
4. The framework is **weakest exactly where the field is least developed** — upstream, research-specific traceability — so it does not close that gap, it maps it.

## 6. Limitations

- **Single-case, self-referential** implementation → circularity and developer-as-evaluator bias.
- **Single author** → collaboration, communication and coordination dimensions scored on design support, not observed use.
- **Repository not yet public** → transparency scored internally.
- **Single coder** on the scores; no independent rater.
- **Bibliometric corpus from OpenAlex + arXiv** → coverage/precision trade-off versus Scopus/WoS.
- **Compressed build** → does not test sustained multi-month or multi-project use.

## 7. Handoff to Phase 10

Phase 10 analyses framework coverage, implementation results, strengths and limitations across RQ1–RQ5 for the manuscript; Phase 11 writes it up. The evaluation numbers here (overall 1.62/2; E1 and E3 at 2.0; E6 at 1.25) and Table 6 are the Results §10.6 and Table 5/6 inputs.
