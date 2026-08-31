# Framework Evaluation

**Phase 9 deliverable** (roadmap step 9 of 12) · Answers **RQ5**
**Protocol:** `docs/EVALUATION_PROTOCOL.md` · **Evidence:** `case-study/implementation_record.csv`, `activity_register.csv`, `traceability_examples.md`
**Artifacts:** `evaluation_scores.csv` (21 sub-dimensions), `workflow_comparison.csv` (Table 6), `reliability_check.csv` (second-coding pass) · **Decisions:** `docs/DECISION_LOG.md` D15, D23, D26

> **Re-score (2026-08-30, `DECISION_LOG.md` D23, GitHub issue #3).** After the repository was made public (D22) and one full Issue→PR→Release cycle was run (`live_cycle_demo.md`), four sub-scores that had been *planned* / *retrospective* / *design-support* were re-scored on observed evidence: E5 external visibility 0→2, E2 task traceability 1→2, E4 task categorization 1→2, E6 workflow overhead 1→2. **Overall 1.62 → 1.86 / 2** (observed-only 1.76 → 1.85). The numbers below are the re-scored values.

---

## 1. Method

The six dimensions of `EVALUATION_PROTOCOL.md` are each scored **0 (not supported) / 1 (partially) / 2 (fully)**, broken into sub-dimensions. Every sub-score records its **basis**:

- **observed** — evidenced by the actual state of this repository (20 of 21 sub-scores after the D23 re-score);
- **design-support** — the framework provides the mechanism, assessed from the Phase 5 mapping (1, E1).

E1 also uses the quantitative coverage from the Phase 5 mapping.

## 2. Results

| Dim | Dimension | Score /2 | % | Basis |
|---|---|---|---|---|
| E1 | Requirement coverage | **2.00** | 100% | design-support (Phase 5) |
| E2 | Traceability | **1.75** | 88% | observed |
| E3 | Documentation | **2.00** | 100% | observed |
| E4 | Organization | **2.00** | 100% | observed |
| E5 | Transparency | **2.00** | 100% | observed |
| E6 | Usability | **1.50** | 75% | observed |
| | **Overall** | **1.86** | **93%** | (observed-only: 1.85 / 92%, n=20) |

## 3. Dimension by dimension

### E1 — Requirement coverage (2.00)

From `framework/mapping/requirement_feature_matrix.csv`: **13 of 15** requirements are supported at Partial or better (7 Direct, 6 Partial); mean 2.33/3. The two Limited are **RM2** (research-question management — a differentiator) and **RM15** (governance — declared partly out of scope). No requirement is unsupported.

### E2 — Traceability (1.75)

| Sub-dimension | Score | Basis |
|---|---|---|
| Decision traceability | 2 | observed — `DECISION_LOG.md`, each entry with rationale, alternatives and an *Affects* line |
| Version traceability | 2 | observed — Git history; `corpus.csv` reproducible; `v1.0.0` / `v1.1.0` tags |
| Task traceability | 2 | observed (D23 re-score) — GitHub Issues #1–#12 on Project #2, cross-referenced; one full Issue→branch→PR→merge→Release cycle (`live_cycle_demo.md`) |
| Provenance / artifact linkage | 1 | observed — document-level linkage machine-checked; one Issue→PR→Release chain demonstrated. Still manual, no lineage query |

Only provenance/artifact linkage stays at 1: the manual chain is now demonstrated once but there is no automated lineage retrieval.

### E3 — Documentation (2.00)

Protocol (`RESEARCH_DESIGN.md`, `LITERATURE_REVIEW.md`), per-phase methodology (`PHASE1–9_PROGRESS.md`, framework narratives), decisions (`DECISION_LOG.md`) and roadmap (`ROADMAP.md`, `CHANGELOG.md`) are all systematically documented from project start — 23 `docs/` files plus folder READMEs. The framework's clearest success.

### E4 — Organization (2.00)

Repository structure (enforced by `validate-structure.yml`), research-phase identification (12-stage lifecycle, milestones M1–M8) and folder-level artifact classification are fully realised. **Task categorization** now also scores 2 (D23 re-score): the activity label set is applied to GitHub Issues #1–#12.

### E5 — Transparency (2.00)

Accessible documentation, visible history, traceable decisions and — after D22 — **external project visibility** all score 2: the repository is public, and its full history, documentation, Insights and Project #2 are third-party inspectable. A Pages summary page (component X1) is still to build but is not required for the dimension.

### E6 — Usability (1.50)

| Sub-dimension | Score | Note |
|---|---|---|
| Maintenance effort | 2 | scripts regenerate every `results/` table; layout guarded by CI |
| Workflow overhead | 2 | (D23 re-score) doc/decision/version-control spine near-zero overhead solo; the Issue/PR/Release layer was run once end-to-end — per-item overhead is modest solo |
| Configuration complexity | 1 | `Use this template` + placeholders is quick, but Project / labels / Actions setup is manual |
| Technical knowledge | 1 | Git + Markdown + YAML literacy assumed — a real barrier outside computational fields |

Still the lowest dimension: configuration cost and the technical-literacy barrier are unchanged, and the *collaborative* benefit of the coordination layer remains untested (single author).

## 4. Conventional-workflow comparison (Table 6)

`workflow_comparison.csv`. Summary: the framework's benefit is concentrated in **linking artifacts that a fragmented workflow (email + documents + local files + separate tools) leaves disconnected** — decision rationale, version history, and the question→data→analysis→result chain become reconstructable. Its cost is concentrated in the **coordination layer** (Issues, PRs, Project), and its weak points (upstream planning, research-question tracking, decision traceability) coincide with the thinnest areas of the literature (RQ1).

## 5. Observations

1. The framework realises a **document / decision / version-control spine** that a fragmented workflow lacks, at near-zero overhead — this is its robust contribution.
2. The **coordination layer pays off with collaborators and is optional for a solo author**; the self-referential case could not test the collaborative benefit.
3. GitHub is a **coordination and traceability layer, not a complete research infrastructure**: five requirements (RM8, RM9, RM12, RM14, RM15) need complementary external systems.
4. The framework is **weakest exactly where the field is least developed** — upstream, research-specific traceability — so it does not close that gap, it maps it.

## 6. Limitations

- **Single-case, self-referential** implementation → circularity and developer-as-evaluator bias.
- **Single author** → the coordination layer was run once end-to-end but its *collaborative* value (multi-author review, communication) is untested; E6 configuration and technical-literacy costs remain.
- **Single coder** on the scores; no human second rater. *Mitigated:* an independent LLM re-code of all 53 coded decisions (RE→RM, 15 support levels, 21 sub-scores) agreed at 96.2% (κ 0.83–1.00 per unit); the two adjacent-category disagreements change no reported conclusion, and adopting the stricter read moves Overall only 1.86 → 1.81. `reliability_check.md`; `DECISION_LOG.md` D26.
- **Bibliometric corpus from OpenAlex + arXiv** → coverage/precision trade-off versus Scopus/WoS.
- **Compressed build** → does not test sustained multi-month or multi-project use.

## 7. Handoff to Phase 10

Phase 10 analyses framework coverage, implementation results, strengths and limitations across RQ1–RQ5 for the manuscript; Phase 11 writes it up. The evaluation numbers here (overall 1.86/2 after the D23 re-score; E1, E3, E4, E5 at 2.0; E6 lowest at 1.5) and Table 6 are the Results §10.6 and Table 5/6 inputs.
