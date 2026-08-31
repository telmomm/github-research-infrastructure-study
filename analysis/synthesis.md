# Phase 10 — Analysis and Synthesis

**Roadmap step:** 10 of 12 · Synthesises RQ1–RQ5 for the manuscript (Results §10, Discussion §11)
**Canonical:** `analysis/findings.csv` (32 findings) · **Decisions:** `docs/DECISION_LOG.md` D19
**Regenerate tallies:** `python3 analysis/scripts/synthesis_check.py`

This document does not add data. It integrates Phases 2–9.

---

## 1. The through-line

> The literature under-serves the upstream, research-specific layer of the research process (**RQ1**); those needs are real and rated important (**RQ2** — the *differentiators*); GitHub also under-serves exactly that layer (**RQ3**); the reference architecture names the conventions that partially close the gap (**RQ4**); and a real implementation shows the record / version-control spine works cheaply while the coordination layer's collaborative benefit is unproven for a solo author (**RQ5**).

The gap identified bibliometrically (RQ1) and the gap measured in GitHub's coverage (RQ3) are **the same gap**, reached by independent routes. That convergence is the study's central result.

## 2. Findings by research question

### RQ1 — Structure of the field (bibliometric)

- **F01** The literature is an assembly of partially connected strands (scientific workflows, RDM, provenance, research information systems, open science, version control), not one field.
- **F02** It is output-biased: data management 50.8% of the corpus and analysis/workflow 41.9%, against idea/question 3.7% and provenance 7.0%.
- **F03** 7 of 15 lifecycle stages are thinly covered — idea, question, planning, ethics, post-publication traceability, cross-stage coordination, governance.
- **F04** Output rises ~10× 2008→2024; 2025 partially indexed (trimmed series used for the trend).
- **F05** Track B (52 review papers) and Track A (5,139-work corpus) independently show the same bias — convergent evidence.

### RQ2 — Research management requirements

- **F06** 15 requirements (RM1–RM15), concentrated in Traceability (4), Documentation (3), Collaboration (2).
- **F07** Three *differentiators* — RM1 planning, RM2 research-question management, RM5 decision traceability — are High-importance but weak in literature attention.
- **F08** The requirements are interdependent (RM10 provenance consumes RM2/RM4/RM5/RM8/RM9; RM11 transparency is emergent).

### RQ3 — GitHub coverage

- **F09** 13/15 requirements Partial-or-better, 7 Direct, 0 unsupported; mean 2.43/3 core-14 (2.33 full-15).
- **F10** Direct where research work resembles software engineering (task, review, communication, version control, documentation, transparency, automation — category means 3.0).
- **F11** Partial/Limited for research-specific traceability (RM2 Limited; RM5, RM10 Partial), planning (RM1) and governance (RM15 Limited).
- **F12** Differentiators mean 1.67 vs 2.50 for the rest — the RQ1 gap, on the tool side.
- **F13** 5 requirements (RM8, RM9, RM12, RM14, RM15) need external infrastructure.
- **F14** Lifecycle-coverage profile lowest at idea (2.12) / question (2.25), highest at literature / analysis / manuscript — same shape as RQ1.
- **F15** Issues + the Git repository carry most of the framework.
- **F16** Robust to rubric: stricter scoring gives 2.13, conclusion unchanged.

### RQ4 — Reference architecture and template

- **F17** A 15-component, 5-layer architecture; GitHub as a coordination/traceability layer, not a container.
- **F18** B3 Linkage Discipline + four named conventions are the contribution over a plain repo; they lift RM1/RM2/RM5/RM10.
- **F19** Operationalised as a 33-file, discipline-independent template; every RM served.

### RQ5 — Feasibility and evaluation

- **F20** Self-referential: 13/15 components exercised (8 in the single-author phase, +5 after one live cycle and making the repo public); documentation/decision/version-control spine works at near-zero overhead.
- **F21** Evaluation 1.86/2 overall (1.85/2 observed-only, n=20) after the D23 re-score; coverage, documentation, organization and transparency at 2.0, usability lowest at 1.50.
- **F22** vs fragmented workflow: benefit = linking otherwise-disconnected artifacts; cost = the coordination layer.

## 3. Framework coverage analysis

| Lens | Result |
|---|---|
| Requirement breadth | 13/15 at Partial+; only RM2 and RM15 at Limited; none unsupported |
| Depth | 7 Direct, 6 Partial; mean 2.43/3 (core-14) |
| By category | Execution / Collaboration / Automation 3.0; Documentation 2.67; Planning / Traceability / Artifact mgmt / Output mgmt 2.0; Governance 1.0 |
| By lifecycle stage | flat 2.1–2.4; trough at idea/question; peak at literature/analysis/manuscript |
| External dependence | 5 requirements need Zenodo / containers / data repositories / institutional governance |
| Robustness | strict rubric 2.13; plan-availability verified; conclusion stable |

**Reading:** GitHub covers the *execution-to-output* span of the lifecycle well and the *research-question → decision → provenance* layer poorly. It is a partial infrastructure, and the partiality is systematic, not random.

## 4. Implementation results (RQ5)

- The **record layer** (documentation, decision log), the **artifact workspace** and **version control** were realised natively and at full evaluation strength (E3 = 2.0, decision/version traceability = 2).
- The **coordination layer** (Issues, Project, Pull Requests, Releases) was configured during the single-author phase and then **run once end-to-end** (one Issue→branch→PR→merge→`v1.1.0` Release cycle over the study's own backlog); the repository was made public. This lifted E2/E4/E5/E6 sub-scores to observed and the overall evaluation to **1.86/2** (D23). The per-item overhead is modest solo.
- **Cost/benefit shape:** the low-cost half of the framework delivered fully; the coordination layer is feasible and low-overhead for a solo author, but its **collaborative** value — multi-author review and communication — is still unproven.

## 5. Strengths

1. **Breadth of coverage** — 13/15 requirements supported (F09).
2. **Realised traceability of decisions and versions** — full strength in the case study (F20, F21).
3. **Reproducible, transparent method** — every table from a versioned script; open corpus; decisions logged (D1–D19).
4. **Reusable artifact** — a discipline-independent template with complete requirement coverage (F19).
5. **Explicit boundaries** — the 5 external-tool dependencies are named, not hidden (F13, F28).
6. **Convergent gap identification** — RQ1 and RQ3 reach the same conclusion independently (F12, F14).

## 6. Limitations

1. **The upstream gap is mapped, not closed** — RM1/RM2/RM5 stay Partial/Limited even with conventions (F23).
2. **Collaborative benefit unproven** — the coordination layer was run once solo, so its multi-author review / communication value is untested; E6 configuration and technical-literacy costs remain (F24).
3. **Single-case, self-referential, single-coder** evaluation (F25); an independent LLM re-code of all 53 coded decisions agreed at 96.2% (κ 0.83–1.00), changing no reported conclusion, but no human second coder was available.
4. **OpenAlex+arXiv corpus** — coverage/precision trade-off vs Scopus/WoS (F26; precision ≈ 0.94).
5. **Convention-dependence** — ~1/3 of coverage rests on discipline, not features (F27; strict rubric 2.13).
6. **Not a complete infrastructure** — preservation, environments, large data, governance are external (F28).

## 7. Implications

- **Practice (F29):** adopt the record/version-control spine first; add the coordination layer with collaborators.
- **The field (F30):** the upstream traceability gap is a target for tool development and for reporting standards (decision records, research-question provenance).
- **Open science (F31):** GitHub-based process management is the upstream half of a GitHub–Zenodo–ORCID lifecycle.

## 8. Answer to the main research question

> *To what extent can GitHub function as an integrated infrastructure for managing scientific research projects across the research lifecycle?*

**GitHub can serve as an integrated coordination and traceability *layer* for a substantial part of the research lifecycle — strong from execution to output and for software-like research work, weak for upstream planning, research-question and decision traceability, and dependent on complementary infrastructure for preservation and large data. It maps the research-process-management gap rather than closing it.** (F32)

## 9. Handoff to Phase 11

`findings.csv` rows map to manuscript sections: F01–F05 → Results §10.1 (bibliometric map); F06–F08 → §10.2 (requirements); F09–F16 → §10.3 (coverage) + Table 2; F17–F19 → §10.4 (architecture) + Figs 3–4 + Table 3; F20–F22 → §10.5–10.6 (case study, evaluation) + Tables 5–6; F23–F28 → §11.6 (Limitations); F29–F32 → §11.1–11.7 (Discussion, Conclusions). The three user-tasks in `OPEN_ITEMS.md` are completed before submission and, where relevant, E5/E6 re-scored.
