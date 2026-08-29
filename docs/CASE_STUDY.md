# Case Study Protocol

# Purpose

This document defines the real-world implementation and evaluation of the proposed GitHub-based research management framework.

The case study is intended to demonstrate how the reference architecture can be implemented in practice.

---

# 1. Case study objective

The objective is to evaluate whether the proposed framework can be practically implemented to manage a scientific research project.

The case study should evaluate:

* implementation feasibility;
* requirement coverage;
* traceability;
* documentation;
* organization;
* practical limitations.

---

# 2. Case study design

```text
REFERENCE ARCHITECTURE
        │
        ▼
PROJECT CONFIGURATION
        │
        ▼
RESEARCH ACTIVITIES
        │
        ▼
GITHUB IMPLEMENTATION
        │
        ▼
RESEARCH ARTIFACTS
        │
        ▼
EVALUATION
```

---

# 3. Case study alternatives

The project may be implemented using one of the following approaches.

---

## Option A — Self-referential case study

The framework is used to manage the development of the current research study.

```text
FRAMEWORK
    │
    ▼
MANAGES
ITS OWN
DEVELOPMENT
```

### Advantages

* complete documentation;
* direct access to all project activities;
* natural implementation.

### Limitation

Potential circularity.

---

## Option B — Existing research project

The framework is implemented within an existing research project.

```text
EXISTING PROJECT
        │
        ▼
FRAMEWORK IMPLEMENTATION
        │
        ▼
BEFORE / AFTER ANALYSIS
```

### Advantages

* real-world context;
* possibility of comparative analysis.

### Limitations

* previous documentation may be incomplete;
* migration may require effort.

---

## Option C — Dedicated reference project

A research project is created specifically to test the framework.

### Advantages

* controlled implementation;
* complete documentation.

### Limitations

* may not represent the complexity of established research projects.

---

# 4. Recommended approach

The preferred strategy is a combination of:

```text
CURRENT STUDY
        +
REUSABLE TEMPLATE
        +
REAL RESEARCH IMPLEMENTATION
```

This allows evaluation at multiple levels.

---

# 5. Implementation protocol

## Step 1 — Repository initialization

Create the research repository.

Required components:

```text
README.md
docs/
literature/
data/
analysis/
framework/
manuscript/
```

---

## Step 2 — Research planning

Configure:

* GitHub Project;
* research phases;
* milestones;
* research tasks.

---

## Step 3 — Issue structure

Create Issues for:

* literature tasks;
* methodology;
* data;
* analysis;
* documentation;
* manuscript;
* decisions.

---

## Step 4 — Documentation

Create structured documentation in:

```text
/docs
```

Documentation should include:

* project plan;
* roadmap;
* methodology;
* decisions;
* evaluation protocol.

---

## Step 5 — Research artifact management

Organize:

* literature;
* datasets;
* analysis;
* framework;
* results;
* manuscript.

---

## Step 6 — Collaboration and review

Where applicable:

* use branches;
* create Pull Requests;
* document reviews;
* record changes.

---

## Step 7 — Automation

Implement selected automated workflows.

Possible examples:

* Markdown validation;
* repository structure validation;
* link checking;
* documentation checks.

---

## Step 8 — Research releases

Create identifiable research versions.

Potential release points:

```text
v0.1
Concept definition

v0.2
Literature analysis

v0.3
Requirements framework

v0.4
Reference architecture

v1.0
Paper release
```

---

# 6. Implementation record

The case study should document every relevant implementation decision.

Example:

| Component     | Implementation           | Requirement           |
| ------------- | ------------------------ | --------------------- |
| Project       | Research roadmap         | Planning              |
| Issues        | Research tasks           | Task management       |
| Markdown      | Protocol                 | Documentation         |
| Discussions   | Methodological decisions | Decision traceability |
| Pull Requests | Review                   | Collaboration         |
| Actions       | Validation               | Automation            |
| Releases      | Research versions        | Output management     |

---

# 7. Traceability demonstration

The case study should demonstrate traceability pathways.

Example:

```text
RESEARCH QUESTION
        │
        ▼
GITHUB ISSUE
        │
        ▼
METHOD
        │
        ▼
ANALYSIS
        │
        ▼
RESULT
        │
        ▼
MANUSCRIPT SECTION
```

Another example:

```text
PROJECT TASK
        │
        ▼
ISSUE
        │
        ▼
COMMIT
        │
        ▼
PULL REQUEST
        │
        ▼
RELEASE
```

---

# 8. Evaluation criteria

The implementation should be evaluated according to:

## Requirement coverage

How many identified requirements are supported?

## Traceability

Can research development be reconstructed?

## Documentation

Are major activities documented?

## Organization

Are research artifacts systematically organized?

## Transparency

Can project status and development be understood?

## Usability

Can researchers practically maintain the framework?

---

# 9. Conventional workflow comparison

Where possible, the implementation should be compared conceptually or empirically with a fragmented workflow.

```text
CONVENTIONAL RESEARCH

Email
   +
Documents
   +
Local folders
   +
Spreadsheets
   +
Separate tools

        VS

GITHUB RESEARCH FRAMEWORK

Repository
   +
Projects
   +
Issues
   +
Documentation
   +
Version control
```

The comparison should avoid assuming that every conventional workflow is ineffective.

Instead, it should identify specific advantages and limitations.

---

# 10. Case study evidence

Evidence may include:

* repository history;
* Issues;
* Projects;
* Pull Requests;
* documentation;
* commits;
* releases;
* workflow executions.

The repository itself may therefore constitute part of the empirical evidence.

---

# 11. Case study outputs

The case study should produce:

1. Implemented research repository.
2. Configured GitHub Project.
3. Research Issue structure.
4. Documentation structure.
5. Traceability examples.
6. Evaluation dataset.
7. Implementation observations.

---

# 12. Limitations

Potential limitations include:

* single-case evaluation;
* researcher familiarity with GitHub;
* technical learning curve;
* discipline-specific differences;
* limited collaborative testing;
* potential bias from framework developers evaluating their own system.

These limitations should be explicitly discussed in the manuscript.

---

# 13. Future evaluation

Future research may evaluate the framework through:

* multiple research groups;
* different scientific disciplines;
* usability studies;
* controlled comparisons;
* longitudinal studies;
* institutional implementations.

---

# 14. Final case study workflow

```text
RESEARCH REQUIREMENTS
        │
        ▼
REFERENCE ARCHITECTURE
        │
        ▼
REUSABLE TEMPLATE
        │
        ▼
CASE STUDY IMPLEMENTATION
        │
        ▼
TRACEABILITY ANALYSIS
        │
        ▼
FRAMEWORK EVALUATION
        │
        ▼
SCIENTIFIC RESULTS
```
