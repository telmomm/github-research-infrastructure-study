# Figures and Tables

# Proposed Figures

> **Status (2026-08-30, Phase 10).** Figure sources: Fig 1 study design (ASCII below → to render); Fig 2 requirements framework (`results/framework/rm_by_category.csv`); **Fig 3 architecture** = `manuscript/figures/fig3_architecture.svg` (done); **Fig 4 traceability path** = `manuscript/figures/fig4_traceability.svg` (done); **Fig 5** conventional vs proposed = `case-study/workflow_comparison.csv`; **new: bibliometric co-word map** = `manuscript/figures/coword_map.svg` + `results/track_a/coword_map.gexf`; **new: RQ1 production timeline** = `results/track_a/annual_production{,_trimmed}.csv`; **new: lifecycle-coverage profile** = `results/framework/coverage_lifecycle_profile.csv`. Findings→section map in `analysis/synthesis.md` §9.

## Figure 1

### Study design

```text
Literature
    ↓
Requirements
    ↓
GitHub analysis
    ↓
Mapping
    ↓
Framework
    ↓
Template
    ↓
Implementation
    ↓
Evaluation
```

---

## Figure 2

### Research management requirements framework

```text
                RESEARCH PROJECT
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
     PLANNING      DOCUMENTATION    TRACEABILITY
        │               │               │
        └───────────────┼───────────────┘
                        ▼
              RESEARCH MANAGEMENT
```

---

## Figure 3

### GitHub-based reference architecture

```text
Research management
        ↓
GitHub services
        ↓
Research artifacts
        ↓
Research outputs
```

---

## Figure 4

### Research lifecycle and GitHub integration

```text
Idea → Planning → Research → Analysis → Manuscript → Publication
          │          │          │          │
       GitHub     GitHub     GitHub     GitHub
```

---

## Figure 5

### Conventional versus proposed workflow

```text
FRAGMENTED WORKFLOW

Email + Documents + Local files + Tools


                VS


INTEGRATED GITHUB WORKFLOW

Projects + Issues + Documentation + Version Control
```

---

## Figure 6 (supplementary)

### The study's GitHub Project in use

*Source: `manuscript/figures/project-board.png` (board view grouped by Status) and
`manuscript/figures/project-roadmap.png` (roadmap view grouped by Research phase),
captured from the configured Project with issues #1–#12. Evidence for RQ5 (component
A1/A2 exercised) and for the case-study record. Closes `OPEN_ITEMS.md` 7.3.*

> **Note:** `project-roadmap.png` currently duplicates `project-board.png`; recapture the
> roadmap view before using it as a second panel, or ship the board panel alone.

---

# Proposed Tables

## Table 1

Research management requirements identified in the literature.
*Source: `framework/requirements/requirements_framework.csv` (RM1–RM15). — Phase 3, done.*

## Table 2

Mapping between research management requirements and GitHub functionalities.
*Source: `framework/mapping/requirement_feature_matrix.csv` + `results/framework/coverage_by_requirement.csv`. — Phase 5, done. Companion: RM × feature-group heatmap from `coverage_group_matrix.csv`; lifecycle-coverage profile from `coverage_lifecycle_profile.csv`.*

## Table 3

Reference architecture components.
*Source: `framework/architecture/architecture_components.csv` (15 components, 5 layers). — Phase 6, done. Companions: `workflows.csv` (Table for workflow definitions), `lifecycle_model.csv` (Figure 4 traceability path).*

## Table 4

Reusable template components.
*Source: `template/template_manifest.csv` (33 files → architecture components → requirements). — Phase 7, done.*

## Table 5

Evaluation results.
*Source: `case-study/evaluation_scores.csv` + `results/framework/eval_by_dimension.csv` (E1–E6, 0–2). — Phase 9, done. Overall 1.62/2; observed-only 1.76/2.*

## Table 6

Comparison between conventional and GitHub-based research workflows.
*Source: `case-study/workflow_comparison.csv` (6 dimensions × fragmented / framework / advantage / caveat). — Phase 9, done.*
