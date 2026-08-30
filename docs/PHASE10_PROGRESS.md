# Phase 10 — Analysis

**Roadmap step:** 10 of 12 · **Synthesises:** RQ1–RQ5 · **Feeds:** manuscript Results §10 + Discussion §11
**Started / completed:** 2026-08-30 · **Status: COMPLETE (v1)**

Integrates Phases 2–9 into a single analytical narrative. No new data.

---

## Outputs (`analysis/`)

| File | Content |
|---|---|
| `synthesis.md` | **Narrative.** The through-line, findings by RQ, framework-coverage analysis, implementation results, strengths, limitations, implications, answer to the main RQ, section map for Phase 11 |
| `findings.csv` | **Canonical.** 32 findings (F01–F32): RQ, type (result / limitation / implication), strength, statement, evidence paths |
| `results/framework/synthesis_*.csv` + `synthesis_summary.md` | Tallies + evidence-path check (`analysis/scripts/synthesis_check.py`) |

## The central result

The gap identified bibliometrically (RQ1 — the literature under-serves idea / question / planning / decision traceability) and the gap measured in GitHub's coverage (RQ3 — RM1/RM2/RM5 differentiators score 1.67 vs 2.50) are **the same gap, reached by two independent routes**. GitHub covers the execution-to-output span of the lifecycle well and the upstream research-specific layer poorly; the partiality is systematic.

## Findings profile (`synthesis_summary.md`)

- 32 findings: 22 results, 6 limitations, 4 implications; 17 strong / 15 moderate.
- By RQ: RQ1 6, RQ2 3, RQ3 9, RQ4 3, RQ5 5, main 6.
- Every finding's evidence paths verified to exist.

## Answer to the main research question

GitHub can serve as an integrated **coordination and traceability layer** for a substantial part of the research lifecycle — strong from execution to output and for software-like research work, weak for upstream planning / research-question / decision traceability, and dependent on complementary infrastructure (Zenodo, containers, data repositories, institutional governance). It **maps the research-process-management gap rather than closing it**.

## Strengths / limitations (summary)

**Strengths:** breadth of coverage (13/15); realised decision- and version-traceability; reproducible transparent method; reusable discipline-independent template; explicit boundaries; convergent gap identification.
**Limitations:** the upstream gap is mapped not closed; the coordination layer's collaborative benefit is unproven (solo sprint); single-case / self-referential / single-coder / not-yet-public; OpenAlex+arXiv corpus trade-off; ~1/3 of coverage rests on convention; GitHub is not a complete infrastructure.

## Decisions logged

- `DECISION_LOG.md` D19 — 32-finding synthesis; results / limitations / implications typed and strength-rated; each finding carries verifiable evidence paths; `findings.csv` is the bridge to the manuscript sections.

## Handoff to Phase 11

`findings.csv` → manuscript sections: F01–F05 → §10.1; F06–F08 → §10.2; F09–F16 → §10.3 + Table 2; F17–F19 → §10.4 + Figs 3–4 + Table 3; F20–F22 → §10.5–10.6 + Tables 5–6; F23–F28 → §11.6; F29–F32 → §11.1–11.7. Complete the three `OPEN_ITEMS.md` user-tasks before submission and re-score E5/E6 if the repo is made public.
