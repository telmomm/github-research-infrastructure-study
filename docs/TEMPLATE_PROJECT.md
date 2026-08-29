# GitHub Research Project Template

## Purpose

This document defines the reusable project structure resulting from the study.

The template should support scientific research projects while remaining adaptable across disciplines.

---

# Proposed structure

```text
github-research-project-template/
│
├── README.md
├── LICENSE
├── CITATION.cff
│
├── docs/
│   ├── project-charter.md
│   ├── research-protocol.md
│   ├── methodology.md
│   ├── decision-log.md
│   └── roadmap.md
│
├── literature/
│   ├── search-strategy.md
│   └── references/
│
├── data/
│   ├── README.md
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── analysis/
│   ├── scripts/
│   ├── notebooks/
│   └── results/
│
├── manuscript/
│   ├── figures/
│   ├── tables/
│   └── manuscript.md
│
├── outputs/
│
└── .github/
    ├── ISSUE_TEMPLATE/
    ├── workflows/
    └── pull_request_template.md
```

---

# Research management workflow

```text
Research question
        ↓
GitHub Issue
        ↓
Project planning
        ↓
Research tasks
        ↓
Implementation
        ↓
Review
        ↓
Documentation
        ↓
Research output
```

---

# Recommended issue categories

```text
research-question
literature
methodology
data
analysis
validation
documentation
manuscript
decision
general-task
```

---

# Recommended project fields

* Status.
* Research phase.
* Priority.
* Responsible researcher.
* Artifact.
* Related research question.

---

# Template design principles

1. Transparency.
2. Traceability.
3. Reusability.
4. Minimal complexity.
5. Platform-native implementation.
6. Discipline independence.
