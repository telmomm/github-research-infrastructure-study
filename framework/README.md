# Framework

The study's constructed artifacts, built across Phases 3–6.

| Path | Phase | Contents | Status |
|---|---|---|---|
| `requirements/` | 3 | Research Management Requirements Framework — `REQUIREMENTS_FRAMEWORK.md` (narrative), `requirements_framework.csv` (canonical, RM1–RM15), `lifecycle_requirements_matrix.csv` | **done** |
| `mapping/` | 4–5 | Phase 4: `github_capability_catalogue.csv` + `GITHUB_CAPABILITY_CATALOGUE.md` (68 capabilities). Phase 5: `requirement_feature_matrix.csv` (RM1–RM15 scored) + `coverage_analysis.md` | **done** |
| `architecture/` | 6 | `reference_architecture.md` + `architecture_components.csv` (15 components, 5 layers) + `workflows.csv` (7) + `lifecycle_model.csv` (12 stages) | **done** |

## Requirements framework (Phase 3)

15 platform-independent requirements (RM1–RM15) derived from the Phase 2 literature (`literature/requirements_extraction.csv`, RE01–RE17), classified into 9 categories, scored for importance and literature attention, mapped across 11 lifecycle stages, and related in a dependency model.

Regenerate the cross-tabs: `python3 analysis/scripts/summarise_requirements.py` → `results/framework/`.

Three requirements (RM1 planning, RM2 research-question management, RM5 decision traceability) are flagged **differentiators**: High importance despite weak literature attention — the gap the study targets.
