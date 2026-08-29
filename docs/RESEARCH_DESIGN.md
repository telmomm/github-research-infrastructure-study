# Research Design

# From Code Repository to Research Infrastructure: Evaluating GitHub for Managing the Scientific Research Lifecycle

---

# 1. Purpose

This document defines the overall research design for the study:

> **From Code Repository to Research Infrastructure: Evaluating GitHub for Managing the Scientific Research Lifecycle**

The study investigates whether GitHub can be systematically used beyond software development as a structured infrastructure for managing scientific research activities across the research lifecycle.

The research design integrates:

* structured literature analysis;
* requirements identification;
* GitHub capability analysis;
* requirement-feature mapping;
* reference architecture development;
* reusable template development;
* real-world implementation;
* framework evaluation.

The study follows a **design-and-evaluation research approach**, in which a practical artifact is developed from identified research needs and subsequently evaluated through systematic analysis and real-world implementation.

---

# 2. Research problem

Scientific research projects generate multiple interconnected activities and artifacts.

These may include:

* research ideas;
* research questions;
* project plans;
* protocols;
* literature searches;
* methodological decisions;
* datasets;
* analysis scripts;
* computational environments;
* intermediate results;
* figures;
* tables;
* manuscripts;
* publications;
* software;
* supplementary materials.

These artifacts frequently evolve throughout a research project and may be distributed across multiple disconnected systems.

A typical fragmented research environment may include:

```text
Email
   +
Cloud storage
   +
Local folders
   +
Spreadsheets
   +
Reference managers
   +
Statistical software
   +
Code repositories
   +
Task management tools
   +
Manuscript editors
```

Although specialized tools may effectively support individual activities, fragmentation can create challenges related to:

* project coordination;
* traceability;
* documentation;
* version consistency;
* research provenance;
* decision reconstruction;
* project visibility;
* artifact relationships.

The study investigates whether GitHub can provide a structured coordination and traceability layer connecting significant components of the scientific research lifecycle.

---

# 3. Central research concept

The central concept of the study is:

```text
SCIENTIFIC RESEARCH
        │
        ▼
RESEARCH MANAGEMENT REQUIREMENTS
        │
        ▼
DIGITAL CAPABILITIES
        │
        ▼
GITHUB-BASED IMPLEMENTATION
        │
        ▼
RESEARCH MANAGEMENT INFRASTRUCTURE
```

The study does not assume that GitHub should replace all existing research tools.

Instead, it evaluates whether GitHub can function as a central infrastructure for:

* coordination;
* documentation;
* traceability;
* collaboration;
* version control;
* workflow management;
* research artifact organization.

---

# 4. Study aim

The overall aim of the study is:

> **To develop and evaluate a GitHub-based framework for managing scientific research projects across the research lifecycle.**

---

# 5. Study objectives

The study will pursue the following objectives.

## Objective 1

Identify research project management requirements reported in scientific literature.

## Objective 2

Analyse GitHub functionalities relevant to scientific research management.

## Objective 3

Develop a systematic mapping between research management requirements and GitHub capabilities.

## Objective 4

Develop a GitHub-based Research Management Reference Architecture.

## Objective 5

Develop a reusable GitHub Research Project Template.

## Objective 6

Implement the proposed framework in a real research context.

## Objective 7

Evaluate the framework regarding:

* requirement coverage;
* traceability;
* documentation;
* organization;
* transparency;
* usability.

---

# 6. Research approach

The study combines conceptual and practical research components.

```text
CONCEPTUAL RESEARCH
        │
        ├── Literature analysis
        │
        ├── Requirement identification
        │
        └── Framework development
        │
        ▼
PRACTICAL DEVELOPMENT
        │
        ├── GitHub implementation
        │
        ├── Template development
        │
        └── Case study
        │
        ▼
EVALUATION
        │
        ├── Requirement coverage
        ├── Traceability
        ├── Documentation
        ├── Organization
        ├── Transparency
        └── Usability
```

The overall approach can therefore be described as a **design-and-evaluation study**.

---

# 7. Research process

The research process consists of eight principal stages.

```text
PHASE 1
Research problem definition
        │
        ▼
PHASE 2
Literature analysis
        │
        ▼
PHASE 3
Research management requirements
        │
        ▼
PHASE 4
GitHub capability analysis
        │
        ▼
PHASE 5
Requirement-feature mapping
        │
        ▼
PHASE 6
Reference architecture development
        │
        ▼
PHASE 7
Template and case study implementation
        │
        ▼
PHASE 8
Evaluation
```

---

# 8. Phase 1 — Research problem definition

The first phase defines:

* the research problem;
* study scope;
* study objectives;
* research questions;
* conceptual boundaries.

## Output

A clearly defined research problem and study scope.

---

# 9. Phase 2 — Literature analysis

The literature analysis will identify previous evidence related to:

* scientific research management;
* research workflows;
* research lifecycle management;
* scientific collaboration;
* research provenance;
* research documentation;
* digital research infrastructures;
* reproducibility-related workflows.

The purpose is not simply to summarize previous research.

The evidence will be analysed to identify research management challenges and derive structured requirements.

## Output

A dataset of literature-derived research management needs and requirements.

---

# 10. Phase 3 — Research Management Requirements Framework

Literature evidence will be transformed into structured requirements.

The transformation process will follow:

```text
LITERATURE EVIDENCE
        │
        ▼
RESEARCH MANAGEMENT CHALLENGE
        │
        ▼
MANAGEMENT NEED
        │
        ▼
REQUIREMENT
        │
        ▼
REQUIREMENT CATEGORY
```

The resulting requirements may include:

* planning;
* task management;
* documentation;
* collaboration;
* communication;
* decision traceability;
* version control;
* artifact management;
* research provenance;
* transparency;
* reproducibility support;
* automation;
* output management.

## Output

Research Management Requirements Framework.

---

# 11. Phase 4 — GitHub capability analysis

GitHub functionalities will be analysed according to their potential research management applications.

The analysis will include:

```text
Repositories
Issues
Projects
Milestones
Discussions
Branches
Pull Requests
Markdown
Actions
Releases
Labels
```

Each functionality will be assessed regarding:

* technical capability;
* research applicability;
* traceability;
* integration;
* practical complexity;
* limitations.

## Output

GitHub capability catalogue.

---

# 12. Phase 5 — Requirement-feature mapping

Research management requirements will be mapped to GitHub capabilities.

```text
REQUIREMENT
     │
     ▼
REQUIRED CAPABILITY
     │
     ▼
GITHUB FEATURE
     │
     ▼
IMPLEMENTATION PATTERN
     │
     ▼
SUPPORT LEVEL
```

Each mapping will be classified as:

```text
DIRECT SUPPORT
PARTIAL SUPPORT
LIMITED SUPPORT
NOT SUPPORTED
```

## Output

Requirement-feature mapping matrix.

---

# 13. Phase 6 — Reference architecture development

The mapping analysis will be used to develop a structured reference architecture.

The architecture will define how GitHub components can support research management.

```text
RESEARCH MANAGEMENT
        │
        ▼
GITHUB SERVICES
        │
        ▼
RESEARCH ARTIFACTS
        │
        ▼
RESEARCH OUTPUTS
```

The architecture should define:

* components;
* relationships;
* workflows;
* lifecycle integration;
* implementation principles.

## Output

GitHub-Based Research Management Reference Architecture.

---

# 14. Phase 7 — Template development

The proposed framework will be operationalized as a reusable project template.

The template may include:

```text
Repository structure
Documentation templates
Issue templates
Pull request templates
Labels
Project configuration
Milestones
Automation workflows
Release procedures
```

The template should be:

* reusable;
* discipline-independent where possible;
* understandable;
* adaptable;
* minimally complex.

## Output

GitHub Research Project Template.

---

# 15. Phase 8 — Case study implementation

The framework will be implemented in a real research context.

The case study will demonstrate:

* repository organization;
* research planning;
* Issue management;
* documentation;
* research artifact organization;
* decision traceability;
* version history;
* output management.

The implementation will generate empirical evidence regarding the practical application of the framework.

## Output

Implemented GitHub-based research project.

---

# 16. Evaluation design

The framework will be evaluated across several dimensions.

## 16.1. Requirement coverage

Assessment of whether identified requirements are supported.

## 16.2. Traceability

Assessment of whether research activities and relationships can be reconstructed.

Example:

```text
RESEARCH QUESTION
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

## 16.3. Documentation

Assessment of whether research activities are systematically documented.

---

## 16.4. Organization

Assessment of whether research artifacts and tasks are structured and manageable.

---

## 16.5. Transparency

Assessment of whether project progress and development can be understood.

---

## 16.6. Usability

Assessment of practical implementation complexity.

---

# 17. Units of analysis

The study will analyse several units.

## Unit 1 — Literature evidence

Scientific publications describing research management needs and challenges.

## Unit 2 — Research management requirements

Requirements derived from literature evidence.

## Unit 3 — GitHub functionalities

Platform capabilities relevant to research management.

## Unit 4 — Requirement-feature relationships

Relationships between identified requirements and GitHub capabilities.

## Unit 5 — Framework components

Components of the proposed reference architecture.

## Unit 6 — Case study artifacts

Artifacts generated during implementation.

---

# 18. Data sources

Potential study data sources include:

* scientific literature;
* GitHub documentation;
* GitHub repository artifacts;
* Issues;
* Projects;
* Discussions;
* commits;
* Pull Requests;
* workflow executions;
* releases;
* structured evaluation records.

---

# 19. Evidence integration

The study integrates multiple evidence sources.

```text
LITERATURE
    │
    ▼
REQUIREMENTS
    │
    ▼
GITHUB ANALYSIS
    │
    ▼
MAPPING
    │
    ▼
FRAMEWORK
    │
    ▼
IMPLEMENTATION
    │
    ▼
EVALUATION
```

The evidence produced in one phase informs the subsequent phase.

---

# 20. Study validity considerations

The study should consider several potential validity issues.

## Construct validity

Are the identified requirements an appropriate representation of research management needs?

## Internal validity

Are framework conclusions adequately supported by the mapping and case study evidence?

## External validity

Can the framework be transferred across research disciplines and project types?

## Practical validity

Can researchers realistically implement and maintain the framework?

---

# 21. Potential sources of bias

Potential sources of bias include:

* researcher involvement in framework development;
* subjective requirement interpretation;
* single-case evaluation;
* prior familiarity with GitHub;
* selective implementation of platform features.

Mitigation strategies should include:

* transparent methodology;
* documented decisions;
* explicit evaluation criteria;
* evidence-based requirement identification;
* publication of research artifacts where possible.

---

# 22. Expected scientific outputs

The study is expected to produce:

1. Literature-derived Research Management Requirements Framework.
2. GitHub Capability Catalogue.
3. Requirement-Feature Mapping Matrix.
4. GitHub-Based Research Management Reference Architecture.
5. Reusable GitHub Research Project Template.
6. Case Study Implementation.
7. Framework Evaluation Results.
8. Scientific Manuscript.

---

# 23. Relationship with the previous reproducibility workflow

The proposed study extends the conceptual scope of the previous GitHub–Zenodo–ORCID reproducibility workflow.

The previous workflow focuses primarily on:

```text
RESEARCH OUTPUT
        │
        ▼
GITHUB
        │
        ▼
ZENODO
        │
        ▼
DOI
        │
        ▼
ORCID
```

The present study focuses on the broader research process:

```text
IDEA
 │
 ▼
PLANNING
 │
 ▼
RESEARCH ACTIVITIES
 │
 ▼
DOCUMENTATION
 │
 ▼
ANALYSIS
 │
 ▼
MANUSCRIPT
 │
 ▼
OUTPUT
```

The two studies are therefore complementary.

The first study investigates the reproducibility and traceability of research outputs.

The present study investigates the management and traceability of the research process leading to those outputs.

---

# 24. Final conceptual workflow

```text
RESEARCH PROBLEM
        │
        ▼
LITERATURE ANALYSIS
        │
        ▼
REQUIREMENT IDENTIFICATION
        │
        ▼
REQUIREMENTS FRAMEWORK
        │
        ▼
GITHUB CAPABILITY ANALYSIS
        │
        ▼
REQUIREMENT-FEATURE MAPPING
        │
        ▼
REFERENCE ARCHITECTURE
        │
        ▼
REUSABLE TEMPLATE
        │
        ▼
CASE STUDY
        │
        ▼
EVALUATION
        │
        ▼
SCIENTIFIC PAPER
```
