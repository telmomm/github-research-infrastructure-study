# Second-reading check (AI raters): summary

5 completed rating sheets (P1-P5), compared with the reference scores. The sheets were
completed by AI assistants; this is a robustness check, not human inter-rater reliability.

- Krippendorff's alpha (ordinal), reference + panel: **0.54**; panel only: 0.54

| Pair | n | Exact | Within one | Weighted kappa | Mean difference |
|---|---|---|---|---|---|
| reference vs P1 | 248 | 69% | 96% | 0.54 | +0.02 |
| reference vs P2 | 248 | 66% | 95% | 0.46 | +0.17 |
| reference vs P3 | 248 | 66% | 94% | 0.45 | +0.27 |
| reference vs P4 | 248 | 67% | 96% | 0.48 | +0.17 |
| reference vs P5 | 247 | 63% | 88% | 0.34 | +0.18 |
| P1 vs P2 | 248 | 74% | 99% | 0.60 |  |
| P1 vs P3 | 248 | 62% | 97% | 0.43 |  |
| P1 vs P4 | 248 | 76% | 99% | 0.63 |  |
| P1 vs P5 | 247 | 64% | 94% | 0.42 |  |
| P2 vs P3 | 248 | 70% | 96% | 0.42 |  |
| P2 vs P4 | 248 | 71% | 98% | 0.51 |  |
| P2 vs P5 | 247 | 67% | 94% | 0.37 |  |
| P3 vs P4 | 248 | 76% | 98% | 0.57 |  |
| P3 vs P5 | 247 | 71% | 91% | 0.34 |  |
| P4 vs P5 | 247 | 71% | 94% | 0.45 |  |
| reference vs panel median | 248 | 71% | 96% |  | +0.19 |

## Overall mean (15 requirements) by configuration

| Source | GitHub | GitLab | Bitbucket | Bitbucket + Jira + Confluence | Ranking |
|---|---|---|---|---|---|
| reference | 2.75 | 2.55 | 1.76 | 2.48 | GH > GL > AT > BB |
| P1 | 2.55 | 2.65 | 1.87 | 2.47 | GL > GH > AT > BB |
| P2 | 2.61 | 2.65 | 2.11 | 2.85 | AT > GL > GH > BB |
| P3 | 2.86 | 2.74 | 2.08 | 2.87 | AT > GH > GL > BB |
| P4 | 2.83 | 2.71 | 1.99 | 2.67 | GH > GL > AT > BB |
| P5 | 2.74 | 2.72 | 2.17 | 2.66 | GH > GL > AT > BB |
| median | 2.78 | 2.73 | 2.01 | 2.76 | GH > AT > GL > BB |

## Differentiators (RM1, RM2, RM5) vs the other twelve

| Source | GitHub | GitLab | Bitbucket | Bitbucket + Jira + Confluence |
|---|---|---|---|---|
| reference | 2.41 vs 2.84 | 2.02 vs 2.68 | 1.01 vs 1.94 | 2.66 vs 2.44 |
| P1 | 2.07 vs 2.67 | 2.32 vs 2.73 | 1.07 vs 2.07 | 2.61 vs 2.44 |
| P2 | 2.11 vs 2.74 | 2.28 vs 2.74 | 1.31 vs 2.31 | 3.00 vs 2.82 |
| P3 | 2.67 vs 2.91 | 2.59 vs 2.78 | 1.19 vs 2.30 | 3.00 vs 2.83 |
| P4 | 2.59 vs 2.90 | 2.34 vs 2.80 | 1.42 vs 2.13 | 2.85 vs 2.63 |
| P5 | 2.54 vs 2.80 | 2.62 vs 2.74 | 1.51 vs 2.34 | 2.62 vs 2.67 |
| median | 2.59 vs 2.82 | 2.59 vs 2.76 | 1.24 vs 2.21 | 2.93 vs 2.71 |

- Requirement labels unchanged between reference and panel median: 40 of 60
- Cells where the panel median differs from the reference by 1.5 or more: 11
  - RM1.1 BB: reference 0, panel [2, 1, 1, 2, 2]
  - RM2.2 GL: reference 1, panel [2, 3, 3, 3, 3]
  - RM3.1 BB: reference 0, panel [2, 2, 3, 2, 3]
  - RM3.2 BB: reference 0, panel [2, 2, 2, 2, 3]
  - RM3.3 BB: reference 0, panel [3, 3, 3, 3, 3]
  - RM3.4 BB: reference 0, panel [1, 2, 1, 2, 2]
  - RM10.1 BB: reference 1, panel [2, 3, 3, 3, 3]
  - RM10.2 AT: reference 1, panel [2, 3, 3, 2, 3]
  - RM11.1 BB: reference 1, panel [3, 3, 0, 3, 3]
  - RM14.1 BB: reference 1, panel [2, 3, 3, 3, 3]
  - RM14.4 BB: reference 1, panel [2, 3, 3, 3, 3]

- Verified cells where the panel median differs from the reference by 1 or more: 32 of 72
  - RM1.1 BB: reference 0, panel median 2
  - RM1.2 GL: reference 2, panel median 3
  - RM1.2 BB: reference 0, panel median 1.0
  - RM1.3 GL: reference 1, panel median 2
  - RM2.2 GL: reference 1, panel median 3
  - RM2.3 GH: reference 2, panel median 3
  - RM2.3 GL: reference 2, panel median 3
  - RM3.1 BB: reference 0, panel median 2
  - RM3.2 GL: reference 2, panel median 3
  - RM3.2 BB: reference 0, panel median 2
  - RM3.3 BB: reference 0, panel median 3
  - RM3.4 BB: reference 0, panel median 2
  - RM3.5 GH: reference 3, panel median 2
  - RM3.5 GL: reference 1, panel median 2
  - RM3.5 BB: reference 0, panel median 1
  - RM3.6 BB: reference 0, panel median 1
  - RM4.1 BB: reference 3, panel median 2
  - RM5.2 AT: reference 3, panel median 2
  - RM6.1 GL: reference 2, panel median 3
  - RM6.1 BB: reference 2, panel median 3
  - RM6.1 AT: reference 2, panel median 3
  - RM9.4 BB: reference 3, panel median 2
  - RM10.1 BB: reference 1, panel median 3
  - RM11.1 BB: reference 1, panel median 3
  - RM11.1 AT: reference 1, panel median 2
  - RM11.3 BB: reference 2, panel median 3
  - RM11.3 AT: reference 2, panel median 3
  - RM12.3 BB: reference 3, panel median 2
  - RM12.3 AT: reference 3, panel median 2
  - RM14.2 GL: reference 1, panel median 2
  - RM15.1 AT: reference 2, panel median 3
  - RM15.4 BB: reference 1, panel median 2

## Agreement with the reference by stratum (range over the sheets)

| Stratum | Cells | Exact | Within one | Mean difference | Exact vs panel median |
|---|---|---|---|---|---|
| verified cells | 72 | 46%-54% | 70%-92% | +0.19 to +0.49 | 56% |
| unverified cells | 176 | 70%-76% | 95%-99% | -0.06 to +0.18 | 78% |
| GitHub | 62 | 77%-89% | 98%-100% | -0.19 to +0.10 | 89% |
| GitLab | 62 | 71%-79% | 94%-98% | +0.10 to +0.21 | 77% |
| Bitbucket | 62 | 41%-53% | 70%-90% | +0.16 to +0.41 | 56% |
| Bitbucket + Jira + Confluence | 62 | 60%-68% | 90%-100% | -0.02 to +0.37 | 63% |

## Sensitivity: reference on verified cells, panel median on the rest

| GitHub | GitLab | Bitbucket | Bitbucket + Jira + Confluence | Ranking |
|---|---|---|---|---|
| 2.77 | 2.57 | 1.77 | 2.72 | GH > AT > GL > BB |

## What holds across the 6 readings (reference and 5 sheets)

- Highest overall mean: GitHub 3, Bitbucket + Jira + Confluence 2, GitLab 1
- Lowest overall mean: Bitbucket 6
- RM1, RM2 and RM5 score below the other twelve: GitHub 6 of 6, GitLab 6 of 6, Bitbucket 6 of 6, Bitbucket + Jira + Confluence 1 of 6
- Native criteria (score 3) per reading: reference 48/39/18/34; P1 35/41/17/35; P2 39/40/27/54; P3 53/50/33/57; P4 52/47/19/45; P5 48/46/34/48; median 48/45/22/49
- RM5.1 (decision as a distinct record), sheets scoring 3: GitHub 0, GitLab 0, Bitbucket 0, Bitbucket + Jira + Confluence 3; reference 2/2/1/3
- RM6.1 (mandatory review), sheets scoring 3: GitHub 5, GitLab 4, Bitbucket 3, Bitbucket + Jira + Confluence 3; reference 3/2/2/2
- RM14.2 (archive with identifier), sheets scoring 3: GitHub 4, GitLab 1, Bitbucket 1, Bitbucket + Jira + Confluence 1; reference 3/1/1/1
- RM14.3 (citation metadata used), sheets scoring 3: GitHub 4, GitLab 0, Bitbucket 0, Bitbucket + Jira + Confluence 0; reference 3/2/2/2

## Residual gaps (no configuration native): 11 in the reference

- Criteria with no native support, per reading: reference 11, P1 10, P2 5, P3 1, P4 4, P5 8, median 3
- Reference gaps and the number of sheets that also find no configuration native: RM1.2 0/5, RM1.4 2/5, RM2.1 1/5, RM5.5 0/5, RM8.5 3/5, RM9.1 0/5, RM9.2 2/5, RM9.3 0/5, RM10.2 2/5, RM10.3 0/5, RM12.1 3/5
- Confirmed by a majority of the sheets: 2 of 11

## Cells every sheet scores on the same side of the reference: 27

Verified 13, unverified 14. The unverified ones are the candidates for adjudication.

- RM1.1 BB: reference 0, sheets [2, 1, 1, 2, 2] (verified)
- RM1.2 AT: reference 2, sheets [3, 3, 3, 3, 3]
- RM2.2 GL: reference 1, sheets [2, 3, 3, 3, 3] (verified)
- RM3.1 BB: reference 0, sheets [2, 2, 3, 2, 3] (verified)
- RM3.2 GL: reference 2, sheets [3, 3, 3, 3, 3] (verified)
- RM3.2 BB: reference 0, sheets [2, 2, 2, 2, 3] (verified)
- RM3.3 BB: reference 0, sheets [3, 3, 3, 3, 3] (verified)
- RM3.4 BB: reference 0, sheets [1, 2, 1, 2, 2] (verified)
- RM3.5 GL: reference 1, sheets [3, 2, 3, 2, 2] (verified)
- RM4.2 BB: reference 2, sheets [1, 1, 1, 1, 0]
- RM5.5 AT: reference 2, sheets [3, 3, 3, 3, 3]
- RM6.3 BB: reference 2, sheets [3, 3, 3, 3, 3]
- RM6.3 AT: reference 2, sheets [3, 3, 3, 3, 3]
- RM9.1 AT: reference 2, sheets [3, 3, 3, 3, 3]
- RM9.3 AT: reference 2, sheets [3, 3, 3, 3, 3]
- RM9.4 BB: reference 3, sheets [1, 1, 2, 2, 2] (verified)
- RM9.4 AT: reference 2, sheets [3, 3, 3, 3, 3]
- RM10.1 BB: reference 1, sheets [2, 3, 3, 3, 3] (verified)
- RM10.2 GH: reference 1, sheets [2, 2, 2, 2, 2]
- RM10.2 GL: reference 1, sheets [2, 2, 2, 2, 2]
- RM10.2 AT: reference 1, sheets [2, 3, 3, 2, 3]
- RM10.3 AT: reference 2, sheets [3, 3, 3, 3, 3]
- RM11.3 BB: reference 2, sheets [3, 3, 3, 3, 3] (verified)
- RM14.1 BB: reference 1, sheets [2, 3, 3, 3, 3]
- RM14.2 GL: reference 1, sheets [2, 2, 2, 2, 3] (verified)
- RM14.4 BB: reference 1, sheets [2, 3, 3, 3, 3]
- RM15.4 BB: reference 1, sheets [2, 2, 2, 2, 3] (verified)
