# GitHub-Based Research Management Reference Architecture — Sketch

> **Status (2026-08-30).** Early sketch. Phase 6 executed; the **built architecture**
> is authoritative at [`framework/architecture/`](../framework/architecture/) —
> `reference_architecture.md` (narrative), `architecture_components.csv` (15 components,
> 5 layers), `workflows.csv` (7), `lifecycle_model.csv` (12 stages). See `DECISION_LOG.md` D12.
> The layer stack and lifecycle table below are retained as the conceptual seed.

## Concept

The proposed framework treats GitHub as an integrated environment supporting multiple components of scientific research management.

---

# Architecture

```text
╔══════════════════════════════════════════════════════╗
║                    RESEARCH PROJECT                  ║
╚══════════════════════════╦═══════════════════════════╝
                           ║
                           ▼
╔══════════════════════════════════════════════════════╗
║                RESEARCH MANAGEMENT                   ║
║                                                      ║
║ Questions · Planning · Tasks · Decisions             ║
╚══════════════════════════╦═══════════════════════════╝
                           ║
                           ▼
╔══════════════════════════════════════════════════════╗
║                  GITHUB SERVICES                     ║
║                                                      ║
║ Projects · Issues · Discussions · Pull Requests      ║
║ Actions · Releases · Branches                        ║
╚══════════════════════════╦═══════════════════════════╝
                           ║
                           ▼
╔══════════════════════════════════════════════════════╗
║                 RESEARCH ARTIFACTS                   ║
║                                                      ║
║ Data · Code · Documentation · Analysis · Manuscript  ║
╚══════════════════════════╦═══════════════════════════╝
                           ║
                           ▼
╔══════════════════════════════════════════════════════╗
║                   RESEARCH OUTPUTS                   ║
║                                                      ║
║ Results · Publications · Releases · Research Objects ║
╚══════════════════════════════════════════════════════╝
```

---

# Lifecycle mapping

```text
IDEA
 │
 ▼
QUESTION
 │
 ▼
PLANNING
 │
 ▼
LITERATURE
 │
 ▼
METHODS
 │
 ▼
DATA
 │
 ▼
ANALYSIS
 │
 ▼
RESULTS
 │
 ▼
MANUSCRIPT
 │
 ▼
PUBLICATION
 │
 ▼
RESEARCH OUTPUTS
```

---

# GitHub implementation

| Lifecycle stage   | GitHub component          |
| ----------------- | ------------------------- |
| Idea              | Discussion                |
| Research question | Issue                     |
| Planning          | Project                   |
| Research phase    | Milestone                 |
| Task              | Issue                     |
| Decision          | Discussion / Decision Log |
| Documentation     | Markdown                  |
| Development       | Branch                    |
| Review            | Pull Request              |
| Automation        | Action                    |
| Version           | Release                   |
| Output            | Repository artifact       |

---

# Design principle

The framework should not attempt to force every research activity into GitHub.

Instead, GitHub should operate as a:

> **central traceability and coordination layer**

connecting research activities and artifacts.
