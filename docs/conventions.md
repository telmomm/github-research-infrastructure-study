# Working Conventions (this repository)

The four conventions from the reference architecture (`framework/architecture/reference_architecture.md` §4), as applied to this study. See `case-study/implementation_record.csv` for how fully each is realised.

---

## 1. Phased-plan convention (A1)

- `docs/ROADMAP.md` is the **plan of record**; its "Current status" table tracks the 12 phases. Each phase has a `docs/PHASEn_PROGRESS.md`.
- Phase vocabulary: the roadmap phases map to the lifecycle stages in `framework/architecture/lifecycle_model.csv`.
- If a GitHub Project is added, use the fields in `.github/project-fields.md`.

## 2. Question-register convention (A3)

- The study's questions are **RQ1–RQ5**, fixed in `docs/PHASE1_PROJECT_DEFINITION.md` §5.
- Every `docs/PHASEn_PROGRESS.md` names the RQ(s) it advances.
- `case-study/activity_register.csv` holds the RQ ↔ phase ↔ task ↔ decision links (standing in for GitHub Issues; see D14).

## 3. Decision-record convention (B2)

- **`docs/DECISION_LOG.md`** — every significant decision is a numbered entry `Dn` with date, context, decision, rationale, alternatives, **Affects**.
- Superseding decisions link back (`D7` → superseded by `D8`).
- Deliberation for this solo project happened in the working session; with collaborators it moves to GitHub Discussions.

## 4. Linkage-discipline convention (B3)

- Every `Dn` entry has an **Affects** line naming the files/artifacts it changes.
- Every `docs/PHASEn_PROGRESS.md` has a **Handoff** section linking to the next phase's inputs.
- Framework artifacts cross-reference by id: `RE`→`RM`→`GC`→component; the `analysis/scripts/summarise_*` scripts verify these resolve.
- Commits are phase-scoped (`Phase n`); when the Issue layer is used, commits and PRs will also carry `refs #` / `Closes #`.
