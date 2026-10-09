# Platform evaluation protocol (manuscript 2)

Instrument: the fifteen research-management requirements of manuscript 1 and their 62 expected
capabilities (`framework/requirements/requirements_framework.csv`), used unchanged. Each expected
capability is one criterion with a written test (`criteria.csv`).

## What is evaluated

| Code | Configuration | Fixed context |
|---|---|---|
| GH | GitHub | GitHub Free, organization account, public repository |
| GL | GitLab | GitLab.com Free, public project |
| BB | Bitbucket | Bitbucket Cloud Free (up to 5 users), public repository |
| AT | Bitbucket + Jira + Confluence | Free plans of the three Atlassian products used together |

The context is an open research project run by a small group with no budget for tooling. AT is
included because Bitbucket Cloud removed its native issue tracker and wiki in August 2026 and
Atlassian directs users to Jira and Confluence; BB alone shows what the code host provides.
Only vendor features count. Third-party and marketplace applications are excluded, with one
exception carried over from manuscript 1: an external archive that assigns persistent identifiers,
which criterion RM14.2 names explicitly.

## Criterion score

| Score | Meaning |
|---|---|
| 3 | Native: the platform ships a feature that performs the capability as tested, with no convention imposed by the team |
| 2 | By convention: achievable with platform features, but through a generic object the team configures or a convention the platform neither models nor enforces |
| 1 | Marginal: only a fragment of the capability, or free text with no structure |
| 0 | Absent: needs another product |

Each cell has two scores: `score_free` in the fixed context and `score_best` on the vendor's
highest paid tier. The difference shows which capabilities are gated by price.

## Aggregation

Requirement score = mean of its criterion scores. Label: Direct >= 2.5, Partial >= 1.5,
Limited >= 0.5, Not supported otherwise. Reported alongside it:

- the weakest-link reading (minimum criterion score per requirement), because a mean can hide one missing capability;
- best of breed (maximum free score per criterion across configurations) and the residual gaps no configuration meets natively.

RM15 (governance) is scored on its four listed capabilities only; its institutional side
(funding, workforce) is outside any platform. Means are given for all fifteen and for the core fourteen.

## Evidence and verification

Every cell records the feature that justifies the score. Cells marked `verified: Vn` were checked
against vendor documentation on 2026-10-08 (`verification_log.md`). The rest are scored from
documentation knowledge and have not been re-verified. No score comes from hands-on use: none of
the configurations was exercised in a sandbox project for this evaluation.

## Status and known weaknesses

- The protocol and the scores were drafted in the same session, by a language model, and have not
  been checked by a human rater. The protocol was not registered before scoring.
- Second reading (2026-10-09): the blank sheet (`rater_sheet.md`) was completed by five AI assistants
  (`ratings/`, described in `ratings/README.md`). Agreement with the reference scores is moderate
  (Krippendorff's alpha, ordinal, 0.54; exact agreement 63-69%). The reference scores were not changed.
  `analysis/scripts/rater_agreement.py` writes the comparison to `results/evaluation/panel_*`;
  the cells all five sheets dispute are listed in `panel_summary.md` for adjudication.
  This is a robustness check, not human inter-rater reliability.
- Vendor plans change. Three of the facts verified here changed within the last fourteen months.
- Three probes requested by the journal editor (`probes.csv`) are descriptive and not part of the scores:
  mandatory review before integration, runners, and the path to a citable publication.
