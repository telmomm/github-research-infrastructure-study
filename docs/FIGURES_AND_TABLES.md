# Figures and Tables

# Proposed Figures

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

## Table 6

Comparison between conventional and GitHub-based research workflows.
