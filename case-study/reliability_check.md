# Second-Coding Reliability Check

**Addresses `docs/OPEN_ITEMS.md` 2.7 / 3.1 / 5.2 / 9.1 · GitHub issue #10.**

These four items were declared a single-coder limitation: no independent rater checked
the RE→RM assignment, the 15 requirement support levels, or the 21 evaluation
sub-scores. No second human coder was available for this project. This check substitutes
an **independent LLM re-code** — a partial mitigation, not an equivalent to a human
second coder (see *Limitations of this check* below).

## 1. Method

A large language model (Claude, Anthropic) was given, for each coding unit, the same
inputs the author worked from and the same rubric, and asked to assign a code
independently. Its codes were then compared with the author's.

| Unit | Items | Source material given | Rubric | Scale |
|---|---|---|---|---|
| A — RE→RM assignment | 17 (RE01–RE17) | `literature/requirements_extraction.csv` derived-requirement text + `framework/requirements/requirements_framework.csv` RM definitions | "which RM bucket does this derived requirement belong to?" | nominal (RM1–RM15 / governance) |
| B — Requirement support level | 15 (RM1–RM15) | `framework/mapping/requirement_feature_matrix.csv` implementation pattern, capabilities, evidence note, residual gap | Direct 3 / Partial 2 / Limited 1 / Not supported 0 (`GITHUB_CAPABILITY_CATALOGUE.md` rubric) | ordinal 0–3 |
| C — Evaluation sub-score | 21 | `case-study/evaluation_scores.csv` evidence column + `case-study/evaluation.md` + `docs/EVALUATION_PROTOCOL.md` | 0 not supported / 1 partially / 2 fully | ordinal 0–2 |

Every decision was coded (100%), not a 20% sample — the framework is small enough that a
full re-code is cheaper and more informative than sampling. Codes, agreement flags and
per-item notes are in `reliability_check.csv`; agreement statistics are computed by
`analysis/scripts/reliability_summary.py` → `results/framework/reliability_summary.md`.

## 2. Results

| Unit | n | Exact agreement | Cohen's κ | Linearly-weighted κ |
|---|---|---|---|---|
| A — RE→RM | 17 | **94.1%** (16/17) | 0.94 | — (nominal) |
| B — support level | 15 | **100%** (15/15) | 1.00 | 1.00 |
| C — evaluation sub-score | 21 | **95.2%** (20/21) | 0.83 | 0.83 |
| **pooled** | 53 | **96.2%** (51/53) | — | — |

Two disagreements, both one category wide:

1. **RE11** (artifact linkage / research-object assembly) — author RM10, second coder RM9.
   The derived requirement ("explicit links *assembling* related artifacts into one
   navigable object") reads toward RM9 (artifact management / research-object assembly);
   the author coded the *linkage relations* as RM10 (provenance). Adjudicated: **kept
   RM10** — its definition explicitly includes "artifact linkage" — with the RM9 overlap
   now recorded. No coverage count changes; RE11's evidence studies (S34, S48, S25) simply
   also bear on RM9.
2. **E6 workflow overhead** — author 2, second coder 1. The coordination layer (Issues /
   PRs / Project) was run end to end only once, and the score note itself calls per-item
   overhead "modest", which the second coder read as *partial* (1). Adjudicated: **kept
   2** — the documentation / decision / version-control spine, which is the bulk of the
   work, ran at near-zero overhead across all twelve phases and that is observed — but
   this is flagged as the softest 2 in the sheet.

Five further codes agreed but were flagged as **boundary calls** (`boundary` column):
RE06 and RE07 (RM6/RM7 overlap), RM1 and RM5 support levels (considered Limited before
settling on Partial), and E5 external visibility (considered 1 pending the GitHub Pages
summary page).

## 3. Sensitivity of the headline number

Adopting the second coder's stricter read on E6 workflow overhead:

- E6 (Usability) dimension mean **1.50 → 1.25**;
- Overall **1.86 → 1.81** (mean of 21 sub-scores); dimension-mean overall 1.86 → 1.83;
- dimension ranking unchanged (strongest E3/E4/E5 documentation-organization-transparency,
  weakest E6 usability); overall still in the "high" band.

The RE11 change propagates to no headline figure (coverage means, the 13/15 count, and the
Phase-5 rubric all operate on RM-level rows, not RE-level rows).

## 4. Limitations of this check

- **LLM, not a human second coder.** An independent human rater from a different research
  tradition could diverge more, especially on the ordinal boundary calls. This check
  raises confidence that the codes are *internally defensible and rubric-consistent*; it
  does not establish human inter-rater reliability.
- **Not fully blind.** The model had prior exposure to this repository within the working
  session, so this is closer to a structured audit against the rubric than a cold
  double-coding. The disagreements and boundary flags are the useful signal; the high
  agreement rate should be read with this caveat.
- **Unit B (support levels) is the least independent.** The matrix documents its own
  Direct/Partial/Limited rationale in the `evidence_note` and `residual_gap` columns, so a
  coder reading those columns is partly re-reading the author's reasoning — 100% agreement
  there reflects a well-anchored, self-documenting column more than a hard independent test.
- **κ paradox on Unit C.** Codes are almost all "2", so the marginals are skewed and
  Cohen's κ (0.83) is deflated relative to the 95.2% agreement (Cicchetti–Feinstein
  paradox); percent agreement is the more informative statistic for that unit.

## 5. Conclusion

Across 53 coded decisions the independent re-code agreed at **96.2%** (κ 0.83–1.00 per
unit), with two adjacent-category disagreements, neither of which changes a reported
conclusion. The single-coder limitation stands as declared, but the codes are now shown to
be rubric-consistent and robust to a stricter independent read. `OPEN_ITEMS.md`
2.7 / 3.1 / 5.2 / 9.1 move from *limitation* to *limitation (mitigated)*; `DECISION_LOG.md`
D26.
