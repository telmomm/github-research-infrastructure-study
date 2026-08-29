# GitHub Feature Mapping — Method

> **Status (2026-08-30).** Method for Phases 4–5.
> **Phase 4 done:** the built catalogue is authoritative at
> [`framework/mapping/github_capability_catalogue.csv`](../framework/mapping/) (68 capabilities,
> 12 groups) + `GITHUB_CAPABILITY_CATALOGUE.md`. See `DECISION_LOG.md` D10.
> **Phase 5 (pending):** the requirement–feature matrix and coverage indicators
> will be written to `framework/mapping/requirement_feature_matrix.csv`.
> The GF1–GF11 groups below were the starting point; the catalogue uses GF1–GF12 at finer grain.

# Purpose

This document defines the methodology for analysing GitHub functionalities and mapping them to research management requirements.

The objective is not simply to list GitHub features.

The objective is to determine:

> **Which scientific research management requirements can be supported by GitHub, to what extent, and with what limitations?**

---

# 1. Mapping process

```text
RESEARCH MANAGEMENT
REQUIREMENT
        │
        ▼
REQUIRED CAPABILITY
        │
        ▼
GITHUB FEATURE
        │
        ▼
IMPLEMENTATION MODEL
        │
        ▼
SUPPORT ASSESSMENT
```

---

# 2. GitHub capability domains

The analysis will consider the following GitHub capability domains.

---

## GF1 — Repository

### Potential research role

Central organization of research artifacts.

### Relevant requirements

* documentation;
* artifact management;
* transparency;
* reproducibility support.

---

## GF2 — Issues

### Potential research role

Management and tracking of research activities.

### Potential applications

* research tasks;
* methodological questions;
* research questions;
* decisions;
* literature review tasks;
* data tasks;
* analysis tasks.

---

## GF3 — Projects

### Potential research role

Research planning and project coordination.

### Potential applications

* research roadmap;
* task status;
* lifecycle tracking;
* priorities.

---

## GF4 — Milestones

### Potential research role

Management of major research phases.

### Potential applications

* literature review completion;
* methodology completion;
* data collection;
* analysis;
* manuscript preparation.

---

## GF5 — Discussions

### Potential research role

Structured research communication.

### Potential applications

* scientific discussion;
* methodological decisions;
* project planning;
* collaborative feedback.

---

## GF6 — Branches

### Potential research role

Parallel development of research artifacts.

### Potential applications

* alternative analyses;
* manuscript development;
* experimental approaches;
* methodological changes.

---

## GF7 — Pull Requests

### Potential research role

Structured review and integration.

### Potential applications

* code review;
* manuscript review;
* methodological review;
* documentation review.

---

## GF8 — Markdown documentation

### Potential research role

Version-controlled research documentation.

### Potential applications

* protocols;
* methodology;
* decision logs;
* project documentation;
* research notes.

---

## GF9 — GitHub Actions

### Potential research role

Automation.

### Potential applications

* validation;
* testing;
* documentation generation;
* artifact generation;
* reproducibility checks;
* release workflows.

---

## GF10 — Releases

### Potential research role

Identification of stable research versions.

### Potential applications

* research snapshots;
* software versions;
* dataset versions;
* manuscript versions;
* reproducible releases.

---

## GF11 — Labels

### Potential research role

Research activity classification.

### Potential applications

```text
literature
methodology
data
analysis
validation
documentation
manuscript
decision
```

---

# 3. Requirement-feature mapping matrix

The primary analytical output will be a matrix.

| Requirement           | GitHub Feature | Support | Implementation       | Limitation                            |
| --------------------- | -------------- | ------- | -------------------- | ------------------------------------- |
| Planning              | Projects       | Direct  | Research roadmap     | Requires configuration                |
| Task management       | Issues         | Direct  | Research tasks       | Manual maintenance                    |
| Documentation         | Markdown       | Direct  | Research documents   | Technical familiarity                 |
| Collaboration         | Pull Requests  | Direct  | Review               | Not ideal for all disciplines         |
| Decision traceability | Discussions    | Partial | Decision discussion  | Requires structured use               |
| Automation            | Actions        | Direct  | Validation workflows | Technical complexity                  |
| Version control       | Git            | Direct  | Artifact history     | Large files limitations               |
| Output management     | Releases       | Direct  | Research versions    | External preservation may be required |

---

# 4. Support classification

GitHub support should be classified as:

```text
DIRECT

GitHub provides native functionality
for the requirement.
```

```text
PARTIAL

GitHub can support the requirement,
but additional processes or tools are required.
```

```text
LIMITED

GitHub provides limited support.
```

```text
NOT SUPPORTED

The requirement cannot reasonably
be supported by GitHub alone.
```

---

# 5. Mapping criteria

Each mapping should consider:

## Functional support

Can GitHub technically support the required activity?

## Research suitability

Is the feature appropriate for scientific research?

## Traceability

Does the implementation preserve research history?

## Documentation

Can the activity be documented?

## Integration

Can the feature connect with other research activities?

## Practical complexity

Can researchers reasonably implement the feature?

---

# 6. Example mapping

## Requirement

Decision traceability.

## Required capability

The ability to document:

* decision;
* rationale;
* participants;
* date;
* related research activity.

## GitHub implementation

Possible mechanisms:

* Discussions;
* Issues;
* Markdown decision log.

## Support assessment

Partial to Direct depending on implementation.

## Limitation

GitHub does not automatically distinguish research decisions from ordinary platform discussions.

A structured implementation model is required.

---

# 7. Lifecycle mapping

GitHub features should also be mapped to lifecycle stages.

| Lifecycle stage   | Potential GitHub features     |
| ----------------- | ----------------------------- |
| Idea              | Discussions                   |
| Research question | Issues                        |
| Planning          | Projects                      |
| Research phases   | Milestones                    |
| Literature        | Issues + documentation        |
| Methods           | Markdown + branches           |
| Data              | Repository + external storage |
| Analysis          | Code + branches               |
| Review            | Pull Requests                 |
| Documentation     | Markdown                      |
| Automation        | Actions                       |
| Manuscript        | Version-controlled files      |
| Output            | Releases                      |

---

# 8. Coverage analysis

A coverage score may be calculated for each requirement.

```text
0 = Not supported
1 = Limited support
2 = Partial support
3 = Direct support
```

A coverage matrix can then be used to calculate:

* number of supported requirements;
* number of partially supported requirements;
* unsupported requirements;
* lifecycle coverage.

---

# 9. Framework development

The mapping analysis will provide the foundation for the proposed reference architecture.

```text
REQUIREMENTS
     │
     ▼
GITHUB FEATURES
     │
     ▼
IMPLEMENTATION PATTERNS
     │
     ▼
REFERENCE ARCHITECTURE
```

---

# 10. Important principle

The study should avoid claiming:

> GitHub replaces all research management tools.

The framework should instead identify:

* what GitHub supports well;
* what GitHub partially supports;
* what requires complementary tools;
* what remains outside GitHub.

---

# 11. Expected output

The final mapping should produce:

1. GitHub capability catalogue.
2. Requirement-feature matrix.
3. Support classification.
4. Lifecycle coverage analysis.
5. Identified limitations.
6. Recommended implementation patterns.
