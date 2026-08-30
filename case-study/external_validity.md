# External Validity — Template Instantiation on a Second Project

**Closes `docs/OPEN_ITEMS.md` 8.2 · GitHub issue #12 · relates to RQ4/RQ5.**

A retrospective instantiation of the reusable template
(`template/github-research-project-template/`) on a **completed, published research project
in a different discipline**, to test whether the framework's structure and requirement
coverage transfer beyond this study's own meta-research context.

## 1. Target project

| | |
|---|---|
| Paper | *PreMoCir* — machine-learning mortality prediction in cardiac surgery (with SHAP explainability and a decision-support web app) |
| Venue | *Sensors* (MDPI) **26**(5): 1656, 2026 |
| Code | 3 Jupyter notebooks — data analysis, model development, interpretability — Zenodo **10.5281/zenodo.18249069** (CC-BY-4.0) |
| Data | retrospective clinical cohort (cardiac-surgery patients); **access-restricted** (patient privacy, ethics approval, data-use agreement) |
| Discipline | clinical machine learning / medical informatics — unrelated to this study's scientometrics / meta-research |

## 2. Method

For each of the 15 requirements (RM1–RM15) and each template component, the study asked:
*if PreMoCir had been run in a repository created from this template, would the requirement
have been served, and by what mechanism?* Scored in `external_validity_mapping.csv` as
**covered** (a native template feature or file serves it), **convention** (served, but only
if the linkage/decision conventions are followed — not exercised here), or **external**
(needs a system outside the repository). This is a structural / coverage test, not a live
usability test.

## 3. Result

| Status | RMs | Count |
|---|---|---|
| covered | RM1, RM2, RM3, RM4, RM5, RM8, RM10, RM14 | **8** |
| convention (designed, not exercised) | RM6, RM7, RM13 | 3 |
| external dependency | RM9, RM11, RM12, RM15 | 4 |

Artifact placement in the instantiated template:

| PreMoCir artifact | Template location |
|---|---|
| cohort protocol, feature list, preprocessing, evaluation plan | `docs/research-protocol.md`, `docs/methodology.md` |
| model choice, imbalance strategy, threshold, ethics approvals | `docs/decision-log.md` (Dn) + `decision` issues |
| 3 notebooks, model configs, app code | `analysis/notebooks/`, `analysis/scripts/` (outputs stripped) |
| SHAP / evaluation figures | `analysis/results/` → `manuscript/figures/` |
| restricted patient dataset | `data/external/` pointer (DUA-gated), **not** in the repo |
| Zenodo notebook deposit + DOI | `outputs/` + `CITATION.cff` + release checklist (D1/D2) |
| MDPI paper | `manuscript/` |

## 4. Observations

1. **The framework's realised strengths transfer.** Documentation (RM4), decision
   traceability (RM5), version control (RM8), provenance linkage (RM10) and output
   management (RM14) map onto PreMoCir at least as well as onto this study — and RM5 is
   *more* valuable here, because a clinical-ML paper must justify model, imbalance and
   threshold choices to reviewers, and the decision-log convention captures exactly those.
2. **RM14 maps 1:1.** PreMoCir already followed the release-then-archive shape (notebooks →
   Zenodo DOI → published paper); the template's D1/D2 components describe what it did.
3. **The same requirements need external infrastructure**, for the same reasons plus one:
   RM9/RM11/RM12 need an out-of-repo store — and here the blocker is not size but
   **access restriction** (patient data under a data-use agreement), which stresses the
   `data/external/` pointer convention and the RM11 embargo caveat harder than a
   large-open-dataset would. RM15 (IRB, DUA, hospital data governance) is heavier than in
   this study; the platform part is covered, the institutional part is out of scope — the
   same boundary the main study reports.
4. **Setup cost (retrospective estimate).** `Use this template` + fill placeholders
   (~30 min); Project fields + labels (~20 min); write charter / protocol / methodology
   from the existing paper (~2–3 h); relocate notebooks and add `data/external/` pointers
   (~1 h) → roughly half a day to instantiate retrospectively. For a project run from the
   start, the documents accrue incrementally and the marginal cost is the ~1 h of
   configuration.

## 5. Limitations

Retrospective, single additional case, same lead author, no live use with the clinical
co-authors — so this tests **structural and coverage transfer**, not usability or the
collaborative value of the coordination layer. A prospective instantiation on a project
still in progress (e.g. a manuscript under revision) would test those and is the natural
next step for the future-work line in `case-study/evaluation.md` §5.

## 6. Bottom line

The template transfers to an unrelated clinical-ML project with the same coverage profile
as the self-referential case: the documentation / decision / version-control / output
spine is served directly, the coordination layer is available but unexercised, and a small
set of requirements (restricted data, environments, institutional governance) depend on
external systems — supporting the discipline-independence claim while confirming the
framework's boundaries.
