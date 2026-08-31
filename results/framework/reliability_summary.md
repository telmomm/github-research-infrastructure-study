# Inter-coder agreement — second-coding pass

Independent re-code of every coded decision in the framework (RE->RM assignment, requirement support levels, evaluation sub-scores) against the author's codes. Method and caveats: `case-study/reliability_check.md`. Issue #10; `DECISION_LOG.md` D26.

| Unit | n | Exact agree | % agree | Cohen's kappa | Weighted kappa |
|---|---|---|---|---|---|
| RE->RM assignment (literature/requirements_extraction.csv) | 17 | 16 | 94.1% | 0.937 | - |
| Requirement support level (framework/mapping/requirement_feature_matrix.csv) | 15 | 15 | 100.0% | 1.000 | 1.000 |
| Evaluation sub-score (case-study/evaluation_scores.csv) | 21 | 20 | 95.2% | 0.829 | 0.829 |
| **pooled** | 53 | 51 | 96.2% | - | - |

## Disagreements

- **RE11** (RE->RM assignment): author `RM10` vs second `RM9`. DISAGREE: 'assembling artifacts into one navigable object' leans RM9 (research-object assembly); author read the linkage relations as RM10. Adjudicated -> keep RM10 (its definition explicitly covers artifact linkage); RM9 overlap recorded
- **E6-overhead** (Evaluation sub-score): author `2` vs second `1`. DISAGREE: coordination layer run once end-to-end, note itself says 'per-item overhead is modest' -> second coder reads partial (1). Adjudicated -> keep 2: the doc/decision/version-control spine ran at near-zero overhead across all 12 phases (observed); softest 2 in the sheet

5 further codes agreed but were flagged as boundary calls (recorded in `reliability_check.csv`, column `boundary`).

## Sensitivity of the headline evaluation score

The one evaluation-score disagreement is **E6 workflow overhead** (author 2, second coder 1, adjacent). Adopting the stricter code:

- E6 (Usability) dimension mean 1.50 -> 1.25
- Overall (mean of 21 sub-scores) 1.86 -> 1.81; dimension-mean overall 1.86 -> 1.83
- Ranking unchanged: strongest E3/E4/E5, weakest E6; overall still 'high'.
