# Contributing

This repository is a managed research project. Please follow the four conventions in
[`docs/conventions.md`](docs/conventions.md) — they are what makes the project traceable.

## Roles

| Role | Who | Can |
|---|---|---|
| admin | PI | everything, incl. settings and releases |
| write | core collaborators | branches, PRs, issues |
| triage | reviewers | manage issues, review PRs |
| read | everyone (once public) | view |

## Workflow

1. Pick or open an **issue** (use a template). It must have a **Research phase**, a **milestone**, and a `Refs #<RQ>` line.
2. Branch from the default branch: `phase/<short-name>` or `rq-<n>/<short-name>`.
3. Commit in small steps; every message ends with `(refs #<issue>)`.
4. Open a **pull request**; the body has `Closes #<issue>`; fill the PR checklist.
5. At least one review approval; CI must be green.
6. Squash or merge; the issue closes and the Project status updates.

## Decisions

Significant choices go in [`docs/decision-log.md`](docs/decision-log.md) **and** a `decision` issue. See `conventions.md` §3.

## Large files

Do not commit large datasets. Put a pointer in `data/external/` and link the source (URL/DOI) from the relevant issue.

## Commit message format

```
<summary in imperative mood> (refs #<issue>)

<optional body: what and why>
```
