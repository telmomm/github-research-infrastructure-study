# Track A query precision check (OPEN_ITEMS 2.2)

- Heuristic: a research-context term AND a process/infrastructure term in title+abstract.
- Sample: 120 per query tag, seed 20260830.

| Query | pool | sample | on-topic | est. precision |
|---|---|---|---|---|
| Q2b | 1510 | 120 | 116 | 0.97 |
| Q3a | 964 | 120 | 111 | 0.93 |
| Q1g | 614 | 120 | 105 | 0.88 |
| Q2a | 641 | 120 | 118 | 0.98 |

- Weighted overall estimated precision: **0.94**

## Decision

The broad queries retain acceptable precision for a **bibliometric field map** (the corpus, not the screened subset). Low-relevance records add noise to concept-frequency tallies but do not distort the lifecycle-stage profile, which is the RQ1 result. The queries are **kept as frozen** (`search_strings.md`); the estimate and its heuristic are reported for transparency. Tightening would trade recall for precision with no benefit to the stage-coverage conclusion.
