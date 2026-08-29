# Repository Architecture

# Proposed research repository structure

```text
github-research-infrastructure/
│
├── README.md
├── LICENSE
├── CITATION.cff
│
├── docs/
│
├── literature/
│   ├── search/
│   ├── screening/
│   ├── extraction/
│   └── references/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
│
├── analysis/
│   ├── scripts/
│   ├── notebooks/
│   └── results/
│
├── framework/
│   ├── requirements/
│   ├── mapping/
│   └── architecture/
│
├── template/
│   └── github-research-project-template/
│
├── case-study/
│
├── manuscript/
│   ├── figures/
│   ├── tables/
│   └── manuscript.md
│
└── .github/
    ├── ISSUE_TEMPLATE/
    ├── workflows/
    └── pull_request_template.md
```

---

# Repository purpose

The repository should serve simultaneously as:

1. Research workspace.
2. Evidence of the proposed framework.
3. Reproducible research record.
4. Source for manuscript generation.
5. Foundation for the reusable template.

---

# Proposed repository relationships

```text
RESEARCH REPOSITORY
        │
        ├── Documentation
        │
        ├── Literature analysis
        │
        ├── Data
        │
        ├── Analysis
        │
        ├── Framework
        │
        ├── Template
        │
        ├── Case study
        │
        └── Manuscript
```

---

# Template repository strategy

The study may produce two repositories.

```text
RESEARCH PAPER REPOSITORY
        │
        │ develops and evaluates
        ▼
GITHUB RESEARCH PROJECT TEMPLATE
        │
        │ reusable by
        ▼
OTHER RESEARCH PROJECTS
```

The research repository contains the study.

The template repository contains the reusable implementation.

This separation is recommended because:

* the scientific study should remain focused;
* the template should be reusable;
* users should not need to navigate research data;
* template development can continue independently.
