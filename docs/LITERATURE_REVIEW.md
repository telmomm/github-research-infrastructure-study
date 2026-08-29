# Literature Review Protocol

# From Code Repository to Research Infrastructure: Evaluating GitHub for Managing the Scientific Research Lifecycle

---

# 1. Purpose

This document defines the literature review strategy used to identify research project management requirements relevant to the scientific research lifecycle.

The literature review is not intended to produce a comprehensive systematic review of all research project management literature. Instead, it is designed as a structured evidence analysis supporting the development of the proposed GitHub-based research management framework.

The primary purpose is to identify:

* research project management challenges;
* research workflow challenges;
* requirements for managing scientific research projects;
* traceability requirements;
* documentation requirements;
* collaboration requirements;
* research provenance requirements;
* transparency requirements;
* reproducibility-related management requirements.

The resulting evidence will be used to define the **Research Management Requirements Framework**.

---

# 2. Review objective

The objective of the literature analysis is to answer:

> **What requirements should a system or framework support to effectively manage scientific research projects across the research lifecycle?**

---

# 3. Review questions

## LRQ1

What challenges are reported in the management of scientific research projects?

## LRQ2

What activities must be managed throughout the scientific research lifecycle?

## LRQ3

What requirements are associated with effective research project management?

## LRQ4

What mechanisms support research traceability, transparency and provenance?

## LRQ5

What digital tools or infrastructures have been proposed to support scientific research workflows?

---

# 4. Review scope

The review will focus on scientific and scholarly research rather than general commercial project management.

Relevant areas may include:

* scientific research management;
* research workflow management;
* research lifecycle management;
* scientific workflow systems;
* research information management;
* research provenance;
* research documentation;
* collaborative research;
* reproducible research;
* Open Science workflows;
* research data management;
* digital research infrastructures.

General software engineering or commercial project management studies may be included only when they provide transferable concepts relevant to scientific research management.

---

# 5. Search strategy

## 5.1. Proposed databases

The primary databases should include:

* Scopus;
* Web of Science;
* Google Scholar for complementary searches.

Additional sources may include:

* PubMed;
* IEEE Xplore;
* ACM Digital Library.

Database selection should be documented before the final search.

---

# 6. Search concepts

The search strategy will combine concepts related to:

```text
SCIENTIFIC RESEARCH
        +
PROJECT MANAGEMENT
        +
WORKFLOW
        +
TRACEABILITY
        +
DOCUMENTATION
        +
PROVENANCE
```

---

# 7. Example search queries

## Research project management

```text
"research project management"
AND
(scientific OR academic OR research)
```

## Research workflow management

```text
"research workflow management"
```

## Scientific workflow

```text
"scientific workflow"
AND
(management OR collaboration OR documentation)
```

## Research lifecycle

```text
"research lifecycle management"
```

## Research provenance

```text
"research provenance"
AND
(traceability OR workflow OR management)
```

## Open Science workflows

```text
"open science workflow"
```

## Research collaboration

```text
"research collaboration"
AND
(digital OR platform OR infrastructure)
```

---

# 8. Search process

The literature analysis will follow the process:

```text
SEARCH
   │
   ▼
RECORD IDENTIFICATION
   │
   ▼
DUPLICATE REMOVAL
   │
   ▼
TITLE AND ABSTRACT SCREENING
   │
   ▼
FULL-TEXT ASSESSMENT
   │
   ▼
INCLUDED STUDIES
   │
   ▼
DATA EXTRACTION
   │
   ▼
REQUIREMENT IDENTIFICATION
```

---

# 9. Inclusion criteria

Studies may be included when they:

1. address scientific or academic research workflows;
2. investigate research project management;
3. discuss research lifecycle activities;
4. identify research management challenges;
5. describe requirements for research infrastructures;
6. address research provenance;
7. investigate research traceability;
8. discuss research documentation;
9. address collaboration in scientific research;
10. provide transferable findings relevant to research management.

---

# 10. Exclusion criteria

Studies may be excluded when they:

1. focus exclusively on commercial project management;
2. contain no relationship with scientific research;
3. focus exclusively on technical infrastructure without management implications;
4. provide insufficient methodological information;
5. are duplicates;
6. are not accessible for full-text assessment where full-text analysis is required.

---

# 11. Screening process

Screening should occur in two stages.

## Stage 1 — Title and abstract screening

Records will be assessed according to relevance to:

* scientific research;
* research management;
* research workflows;
* lifecycle management;
* research traceability;
* research documentation.

---

## Stage 2 — Full-text assessment

Potentially relevant studies will be reviewed to identify:

* management challenges;
* required activities;
* proposed solutions;
* reported limitations;
* research infrastructure requirements.

---

# 12. Data extraction

The following information should be extracted from included studies.

| Variable             | Description                              |
| -------------------- | ---------------------------------------- |
| Study ID             | Unique identifier                        |
| Authors              | Study authors                            |
| Year                 | Publication year                         |
| Research domain      | Scientific discipline                    |
| Study type           | Review, framework, empirical study, etc. |
| Research problem     | Identified problem                       |
| Management challenge | Reported challenge                       |
| Research activity    | Lifecycle activity                       |
| Proposed mechanism   | Proposed solution                        |
| Requirement          | Identified requirement                   |
| Evidence             | Supporting findings                      |
| Relevance            | Relevance to this study                  |

---

# 13. Requirement extraction

The main output of the literature analysis will not simply be a summary of previous studies.

The literature will be analysed to identify explicit or implicit requirements for managing scientific research.

Example:

```text
Study finding:
Researchers use multiple disconnected systems.

                ↓

Identified problem:
Research fragmentation.

                ↓

Potential requirement:
Centralized coordination.
```

Another example:

```text
Study finding:
Research decisions are difficult to reconstruct.

                ↓

Identified problem:
Limited decision traceability.

                ↓

Potential requirement:
Decision documentation and traceability.
```

---

# 14. Requirement identification process

The process will follow:

```text
LITERATURE EVIDENCE
        │
        ▼
IDENTIFIED CHALLENGE
        │
        ▼
RESEARCH MANAGEMENT NEED
        │
        ▼
REQUIREMENT
        │
        ▼
REQUIREMENT CATEGORY
```

Requirements should be recorded using standardized descriptions.

---

# 15. Proposed requirement categories

Initial categories may include:

* planning;
* task management;
* documentation;
* collaboration;
* communication;
* version control;
* decision traceability;
* research provenance;
* artifact management;
* research output management;
* transparency;
* reproducibility;
* automation.

These categories are provisional and should be revised based on the literature analysis.

---

# 16. Literature synthesis

The evidence synthesis will combine:

## Descriptive analysis

Including:

* publication years;
* research domains;
* study types;
* investigated research activities.

## Thematic analysis

Identifying:

* recurring challenges;
* management needs;
* proposed solutions;
* common requirements.

## Requirement synthesis

Transforming literature evidence into structured research management requirements.

---

# 17. Output

The literature analysis will produce:

1. Search strategy documentation.
2. Study selection record.
3. Included study dataset.
4. Data extraction table.
5. Research management requirement dataset.
6. Requirement categories.
7. Evidence supporting each requirement.

---

# 18. Relationship with the proposed framework

```text
SCIENTIFIC LITERATURE
        │
        ▼
RESEARCH MANAGEMENT
CHALLENGES
        │
        ▼
RESEARCH MANAGEMENT
REQUIREMENTS
        │
        ▼
REQUIREMENTS FRAMEWORK
        │
        ▼
GITHUB CAPABILITY
MAPPING
```

The literature review therefore provides the evidence base for the proposed framework.

---

# 19. Reporting

The final paper should report:

* databases searched;
* search dates;
* search strategies;
* inclusion criteria;
* exclusion criteria;
* number of records;
* screening process;
* included studies;
* requirement identification methodology.

A flow diagram should be included where appropriate.

---

# 20. Limitations

Potential limitations include:

* heterogeneous terminology;
* disciplinary differences;
* incomplete indexing;
* terminology overlap between research management and project management;
* publication bias;
* limited availability of studies specifically addressing GitHub-based research management.

These limitations should be documented and discussed in the final manuscript.
