# Research Questions

# From Code Repository to Research Infrastructure: Evaluating GitHub for Managing the Scientific Research Lifecycle

---

# 1. Purpose

This document defines the research questions, study objectives, expected propositions and evaluation criteria for the study.

The research questions are designed to guide the complete research process:

```text
Research questions
        │
        ▼
Literature analysis
        │
        ▼
Requirements
        │
        ▼
GitHub analysis
        │
        ▼
Framework development
        │
        ▼
Implementation
        │
        ▼
Evaluation
```

---

# 2. Main research question

The primary research question is:

> **To what extent can GitHub function as an integrated infrastructure for managing scientific research projects across the research lifecycle?**

This question represents the central problem investigated by the study.

---

# 3. Research Question 1

## RQ1 — Research management requirements

> **What requirements are necessary for effectively managing scientific research projects across the research lifecycle?**

### Purpose

Identify the requirements that a research management infrastructure should support.

### Method

Structured literature analysis.

### Evidence

* scientific literature;
* research workflow studies;
* research infrastructure studies;
* research management studies.

### Expected output

A **Research Management Requirements Framework**.

---

# 4. Research Question 2

## RQ2 — GitHub capability coverage

> **To what extent can GitHub functionalities support identified scientific research management requirements?**

### Purpose

Evaluate the relationship between research requirements and GitHub capabilities.

### Method

Requirement-feature mapping.

### Evidence

* GitHub functionality analysis;
* official documentation;
* implementation testing;
* practical observations.

### Expected output

A **Requirement-Feature Mapping Matrix**.

---

# 5. Research Question 3

## RQ3 — Reference architecture

> **How can GitHub functionalities be systematically organized into a reusable framework for managing scientific research projects?**

### Purpose

Develop a structured implementation model.

### Method

Reference architecture development.

### Expected output

A **GitHub-Based Research Management Reference Architecture**.

---

# 6. Research Question 4

## RQ4 — Practical implementation

> **Can the proposed GitHub-based framework be practically implemented to support the management of a real scientific research project?**

### Purpose

Evaluate implementation feasibility.

### Method

Case study.

### Expected output

A documented implementation of the framework.

---

# 7. Research Question 5

## RQ5 — Framework evaluation

> **What benefits and limitations result from using the proposed GitHub-based framework for scientific research management?**

### Purpose

Evaluate the practical implications of the framework.

### Evaluation dimensions

* requirement coverage;
* traceability;
* documentation;
* organization;
* transparency;
* usability;
* implementation complexity.

### Expected output

Framework evaluation results.

---

# 8. Research question relationships

The research questions follow a sequential structure.

```text
RQ1
Research requirements
        │
        ▼
RQ2
GitHub capability coverage
        │
        ▼
RQ3
Reference architecture
        │
        ▼
RQ4
Practical implementation
        │
        ▼
RQ5
Benefits and limitations
```

This sequence represents the logical structure of the study.

---

# 9. Study propositions

Because the study focuses primarily on framework development and evaluation, the research may use propositions rather than traditional statistical hypotheses.

---

## Proposition P1

> Scientific research projects require structured mechanisms for planning, documentation, task management, collaboration and traceability across multiple stages of the research lifecycle.

### Evidence source

Literature analysis.

---

## Proposition P2

> A substantial proportion of identified research management requirements can be supported by native GitHub functionalities or structured GitHub-based implementation patterns.

### Evidence source

Requirement-feature mapping.

---

## Proposition P3

> GitHub functionalities can be organized into a reusable architecture supporting multiple stages of the scientific research lifecycle.

### Evidence source

Reference architecture development.

---

## Proposition P4

> A GitHub-based research management framework can improve the organization and traceability of research activities compared with a fragmented approach to research project management.

### Evidence source

Case study and comparative evaluation.

---

## Proposition P5

> GitHub-based research management presents practical limitations and cannot independently replace all specialized research infrastructure systems.

### Evidence source

Mapping analysis and case study evaluation.

---

# 10. Objectives and research questions

| Objective                                 | Research question |
| ----------------------------------------- | ----------------- |
| Identify research management requirements | RQ1               |
| Analyse GitHub capability coverage        | RQ2               |
| Develop reference architecture            | RQ3               |
| Test practical implementation             | RQ4               |
| Evaluate benefits and limitations         | RQ5               |

---

# 11. Research question operationalization

## RQ1

### Input

Scientific literature.

### Process

Requirement extraction and thematic analysis.

### Output

Research Management Requirements Framework.

---

## RQ2

### Input

Research requirements and GitHub features.

### Process

Requirement-feature mapping.

### Output

Coverage matrix.

---

## RQ3

### Input

Requirements and capability mapping.

### Process

Architecture design.

### Output

Reference architecture.

---

## RQ4

### Input

Reference architecture.

### Process

Real-world implementation.

### Output

Case study repository and implementation evidence.

---

## RQ5

### Input

Case study evidence and evaluation results.

### Process

Structured framework evaluation.

### Output

Benefits and limitations analysis.

---

# 12. Evaluation dimensions

The research questions will be evaluated through the following dimensions.

---

## E1 — Requirement coverage

### Question

How many identified research management requirements can be supported?

### Measurement

```text
Number of supported requirements
────────────────────────────────
Total identified requirements
```

Support may be classified as:

* direct;
* partial;
* limited;
* unsupported.

---

## E2 — Traceability

### Question

Can relevant research relationships be reconstructed?

Example:

```text
QUESTION
    │
    ▼
METHOD
    │
    ▼
DATA
    │
    ▼
ANALYSIS
    │
    ▼
RESULT
    │
    ▼
MANUSCRIPT
```

---

## E3 — Documentation

### Question

Are relevant research processes systematically documented?

Potential indicators:

* documented protocol;
* documented methodology;
* documented decisions;
* documented project roadmap.

---

## E4 — Organization

### Question

Are research artifacts and activities systematically organized?

Potential indicators:

* defined repository structure;
* task categorization;
* research phase identification;
* artifact classification.

---

## E5 — Transparency

### Question

Can project progress and research development be understood?

Potential indicators:

* visible project status;
* accessible documentation;
* historical changes;
* traceable decisions.

---

## E6 — Usability

### Question

Can researchers practically implement and maintain the framework?

Potential indicators:

* configuration complexity;
* maintenance requirements;
* technical knowledge;
* workflow overhead.

---

# 13. Criteria for framework success

The framework should be considered successful if it demonstrates:

## Criterion 1

Coverage of a substantial proportion of identified research management requirements.

## Criterion 2

A clear and reproducible mapping between requirements and implementation mechanisms.

## Criterion 3

A coherent reference architecture.

## Criterion 4

Successful implementation in a real research context.

## Criterion 5

Demonstrable traceability between relevant research activities and artifacts.

## Criterion 6

Identification of clear limitations and unsupported requirements.

The objective is not to demonstrate that GitHub is universally superior to all other systems.

The objective is to determine:

> **Where, how and to what extent GitHub can provide useful infrastructure for scientific research management.**

---

# 14. Scope boundaries

The study focuses on scientific research management.

The study does not attempt to evaluate:

* scientific validity of research results;
* research quality;
* institutional research assessment;
* complete laboratory information management;
* complete clinical data management;
* replacement of all specialized research infrastructure.

The framework may interact with external systems.

Example:

```text
GITHUB
   │
   ├── Data repository
   │
   ├── Reference manager
   │
   ├── Zenodo
   │
   ├── Institutional repository
   │
   └── Publication platform
```

---

# 15. Relationship between framework and previous workflow

The previous GitHub–Zenodo–ORCID workflow investigates:

```text
RESEARCH OUTPUT
        │
        ▼
VERSION CONTROL
        │
        ▼
ARCHIVING
        │
        ▼
PERSISTENT IDENTIFICATION
        │
        ▼
RESEARCHER ATTRIBUTION
```

The current study investigates:

```text
RESEARCH IDEA
        │
        ▼
PROJECT MANAGEMENT
        │
        ▼
RESEARCH ACTIVITIES
        │
        ▼
DOCUMENTATION
        │
        ▼
TRACEABILITY
        │
        ▼
RESEARCH OUTPUT
```

The two research projects therefore address different but complementary stages.

Together:

```text
RESEARCH MANAGEMENT
        │
        ▼
GITHUB-BASED
RESEARCH LIFECYCLE
        │
        ▼
RESEARCH OUTPUT
        │
        ▼
ZENODO ARCHIVING
        │
        ▼
DOI
        │
        ▼
ORCID CONNECTION
```

---

# 16. Final research logic

```text
RQ1
What does scientific research management require?
        │
        ▼
RQ2
What can GitHub support?
        │
        ▼
RQ3
How should GitHub be structured?
        │
        ▼
RQ4
Can it be implemented in practice?
        │
        ▼
RQ5
What benefits and limitations result?
```

---

# 17. Core study statement

The central proposition of the study is:

> **GitHub may function beyond a conventional code repository as a structured coordination, documentation and traceability layer for significant components of the scientific research lifecycle, although its effectiveness depends on systematic implementation and integration with complementary research infrastructures.**
