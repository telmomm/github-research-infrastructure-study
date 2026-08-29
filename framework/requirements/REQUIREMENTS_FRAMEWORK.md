# Research Management Requirements Framework

**Phase 3 deliverable** (roadmap step 3 of 12) · Answers **RQ2**
**Authoritative artifact:** `requirements_framework.csv` (this directory) + `lifecycle_requirements_matrix.csv`
**Method doc:** `docs/REQUIREMENTS_FRAMEWORKS.md` · **Decisions:** `docs/DECISION_LOG.md` D9

---

## 1. Purpose

A structured, evidence-grounded set of requirements that a system or framework must support to manage a scientific research project across its lifecycle. It is the reference against which GitHub's native functionalities are assessed in Phases 4–5.

The framework is **derived from the literature** (Phase 2), not from GitHub. It is deliberately platform-independent.

## 2. Method

Thematic analysis of the Phase 2 evidence:

```
SOTA/SOTA.md  ──►  literature/requirements_extraction.csv (RE01–RE17)
                          │  challenge → management need → derived requirement
                          ▼
                   thematic grouping + reconciliation with the
                   provisional domains RM1–RM14 (docs/REQUIREMENTS_FRAMEWORKS.md)
                          ▼
              Research Management Requirements Framework (RM1–RM15)
```

Each of the 17 extraction rows was assigned to a requirement domain; domains were then defined, classified and related. Two additions and several definition changes resulted (§8). Track A (RQ1, `results/track_a/`) is used only to corroborate the framing, not to derive requirements.

## 3. Requirement attributes

Per requirement (`requirements_framework.csv`): `rm_id`, `name`, `category`, `definition`, `expected_capabilities` (what a supporting system must do — the hook for Phase 5), `lifecycle_stages`, `evidence_re`, `evidence_studies`, `literature_attention`, `importance`, `differentiator`, `relationships`, `known_limitations`, `github_support` (empty until Phase 5).

**Literature attention** records how well the literature *covers* the requirement (strong / moderate / weak-gap / emerging), not how important it is. **Differentiator = yes** marks requirements rated High importance *despite* weak literature attention — the study's core argument that process management is under-served upstream.

## 4. The requirements

### Planning

**RM1 — Research planning and roadmap.** Define, structure and maintain the research plan (phases, objectives, milestones, timeline) as a living, inspectable record. *Capabilities:* phase/milestone definition, objective tracking, roadmap overview, plan revision history. *Lifecycle:* planning (primary). *Evidence:* RE01 — S41, S13, S08. *Attention:* weak-gap. *Importance:* **High — differentiator.** *Limits:* research plans are emergent; over-formalisation can misrepresent non-linear work (S08).

### Execution

**RM3 — Task management.** Identification, assignment, prioritisation and status tracking of discrete research activities and their dependencies. *Capabilities:* task creation, status, assignment, priority, dependency links, board overview. *Lifecycle:* all execution stages. *Evidence:* RE04 — S09, S52. *Attention:* weak. *Importance:* High. *Limits:* manual upkeep; not all research work decomposes into tasks.

### Documentation

**RM4 — Documentation.** Systematic, version-controlled recording of methodology, protocols, project structure and technical context, created from project start rather than at dissemination. *Capabilities:* structured documents, templates, versioned edits, early-stage metadata. *Lifecycle:* all. *Evidence:* RE05 — S15, S21, S17. *Attention:* strong importance / weak practice. *Importance:* High. *Limits:* documentation debt; needs familiarity with Markdown / version control.

**RM11 — Transparency.** Project progress, artifacts and change history are inspectable and understandable by third parties without privileged access. *Capabilities:* visible status, shared/public history, accessible documentation, readable activity log. *Lifecycle:* all. *Evidence:* RE12 — S41, S08, S47. *Attention:* weak-moderate. *Importance:* Medium-High. *Note:* emergent property of RM4, RM5, RM8, RM10. *Limits:* some material must stay embargoed.

**RM12 — Reproducibility support.** Documentation and preservation of the information needed to re-execute or re-derive the work — supporting, not guaranteeing, reproducibility. *Capabilities:* environment capture, pinned data/code versions, runnable steps, hooks for automated checks. *Lifecycle:* methods, analysis, outputs. *Evidence:* RE13 — S21, S17, S16. *Attention:* strong-normative. *Importance:* Medium-High. *Limits:* full reproducibility needs external tooling; not in scope to guarantee.

### Collaboration

**RM6 — Collaboration and contribution tracking.** Support for multiple contributors — review, feedback, contribution attribution, parallel work — with a durable record of who did what. *Capabilities:* review workflow, comment/feedback, contribution history, parallel branches. *Lifecycle:* all. *Evidence:* RE06 — S30, S22, S03. *Attention:* moderate. *Importance:* Medium-High. *Limits:* review norms vary by discipline.

**RM7 — Communication.** Structured, traceable project communication (discussions, threaded decisions, agreements) linked to the research activities it concerns. *Capabilities:* threaded discussion, linking of topics to tasks/artifacts, searchable archive. *Lifecycle:* all. *Evidence:* RE07 — S30, S52, S03. *Attention:* moderate. *Importance:* Medium. *Limits:* informal channels leak outside the system.

### Traceability

**RM2 — Research question management.** Explicit documentation and versioning of research questions and their evolution, with links to the methods, analyses and outputs that address them. *Capabilities:* question registration, revision history, question-to-method/analysis/output links. *Lifecycle:* idea/question (primary). *Evidence:* RE02 — S41, S13. *Attention:* weak-gap. *Importance:* **High — differentiator.** *Limits:* questions are often implicit or reformulated post hoc.

**RM5 — Decision traceability.** Recording of significant research decisions with rationale, alternatives, date, participants and links to affected artifacts. *Capabilities:* decision records, rationale + alternatives, timestamp, participants, artifact links. *Lifecycle:* all. *Evidence:* RE03 — S23, S41, S36. *Attention:* weak-gap. *Importance:* **High — differentiator** (provenance tools miss upstream decisions, S23). *Limits:* judging what counts as a decision; tacit decisions unrecorded.

**RM8 — Version control.** Identifiable versions, change history, diffing and restoration for all artifact types — data, code, documentation, text — not only source code. *Capabilities:* history, diff, restore, tags/snapshots, large-file handling. *Lifecycle:* all execution + manuscript. *Evidence:* RE08 — S10, S48, S04. *Attention:* moderate (partial for non-code). *Importance:* High. *Limits:* large binary/data files; learning curve for non-programmers.

**RM10 — Research provenance and artifact linkage.** Capture and retrieval of the relationships linking questions, methods, data, analyses, results and outputs, so the origin and evolution of any output can be traced end to end. *Capabilities:* activity-to-artifact links, lineage retrieval, cross-stage linking, granular history. *Lifecycle:* all. *Evidence:* RE10, RE11 — S12, S40, S16, S23, S37, S34. *Attention:* strong (mature but incomplete; upstream under-covered). *Importance:* High (core). *Limits:* coverage typically stops at data/computation.

### Artifact management

**RM9 — Research artifact management and integration.** Systematic organisation of research artifacts (datasets, code, protocols, results, figures, manuscripts) in one structured space, with continuity across the heterogeneous tools that produce them. *Capabilities:* defined repository structure, artifact classification, cross-tool references, single navigable workspace. *Lifecycle:* all. *Evidence:* RE09, RE11 — S48, S09, S39, S34. *Attention:* strong (fragmentation is the most-cited challenge). *Importance:* High. *Limits:* some artifacts must live in external systems; integration is by reference, not containment.

### Automation

**RM13 — Automation.** Automatable execution of repetitive project activities — validation, testing, documentation/artifact generation, release steps. *Capabilities:* event-triggered workflows, validation/CI, scheduled checks, build/release automation. *Lifecycle:* execution, outputs. *Evidence:* RE14 — S20, S16, S29. *Attention:* emerging. *Importance:* Medium. *Limits:* technical complexity; benefit concentrated in computational research.

### Output management

**RM14 — Research output management and identification.** Identifiable, citable research versions (releases) connected back to the tasks and decisions that produced them, with persistent identifiers and interoperable metadata for exchange with external systems. *Capabilities:* versioned releases, PIDs via external archive, machine-readable metadata, output-to-process links. *Lifecycle:* results, manuscript, publication, outputs. *Evidence:* RE15, RE16 — S33, S25, S05, S38, S45, S19. *Attention:* strong. *Importance:* Medium-High. *Note:* bridges to the prior GitHub–Zenodo–ORCID workflow. *Limits:* long-term preservation and DOIs require external infrastructure.

### Cross-cutting (partly out of core scope)

**RM15 — Governance and sustainability.** Organisational arrangements for the continuity of the research management setup beyond the project — ownership, maintenance, access policy, skills, archival exit. *Capabilities:* access/permission policy, ownership/handover, contribution guidelines, archival exit plan. *Lifecycle:* whole project + post-project. *Evidence:* RE17 — S14, S36, S42. *Attention:* weak. *Importance:* Low-Medium. *Note:* retained for completeness; only partly in scope per `docs/PHASE1_PROJECT_DEFINITION.md` §6.3 — largely institutional, not platform-solvable.

## 5. Classification

| Category | Requirements |
|---|---|
| Planning | RM1 |
| Execution | RM3 |
| Documentation | RM4, RM11, RM12 |
| Collaboration | RM6, RM7 |
| Traceability | RM2, RM5, RM8, RM10 |
| Artifact management | RM9 |
| Automation | RM13 |
| Output management | RM14 |
| Cross-cutting / partly out of scope | RM15 |

Importance: **High** RM1, RM2, RM3, RM4, RM5, RM8, RM9, RM10 · **Medium-High** RM6, RM11, RM12, RM14 · **Medium** RM7, RM13 · **Low-Medium** RM15.
Differentiators (High importance, weak literature attention): **RM1, RM2, RM5**.

## 6. Lifecycle mapping

`lifecycle_requirements_matrix.csv` scores each requirement against 11 stages (3 = primary, 2 = applies, 1 = marginal, 0 = n/a). Stage load (sum of weights, `results/framework/requirements_summary.md`) is highest at analysis, data, manuscript and outputs, and lowest at idea and question — yet the framework keeps strong upstream requirements (RM1, RM2, RM5) precisely where the literature and existing infrastructure are thinnest. Phase 5 combines this matrix with the GitHub support levels to produce the lifecycle-coverage profile.

## 7. Relationship model

```
RM15 governance  ── context for all ──►

RM1 planning ──► RM3 tasks ──► RM9 artifacts ──► RM14 outputs
     │              │              │                ▲
     ▼              ▼              ▼                │
RM2 questions ─► RM5 decisions ─► RM10 provenance ──┘
     │              ▲   ▲            ▲
     │        RM7 comms │            │
     ▼              │   │            │
RM4 documentation ──┴───┴──► RM11 transparency
     │
     ▼
RM8 version control ──► RM12 reproducibility ◄── RM13 automation
RM6 collaboration ──► (uses RM8, informs RM10)
```

Requirements are interdependent: RM10 (provenance) consumes RM2, RM4, RM5, RM8, RM9; RM11 (transparency) is an emergent property of RM4, RM5, RM8, RM10; RM12 builds on RM4, RM8, RM10 and is partly realised through RM13.

## 8. Changes from the provisional RM1–RM14

| Change | Detail |
|---|---|
| **RM9 broadened** | "Research artifact management" → "…and integration": absorbs RE09 (integration across heterogeneous tools), the most-cited literature challenge. |
| **RM10 broadened** | "Research provenance" → "…and artifact linkage": absorbs RE11 (linking disconnected papers/tools/data/code). |
| **RM14 broadened** | "Research output management" → "…and identification": absorbs RE15 (PIDs, interoperable metadata) alongside RE16. |
| **RM15 added** | Governance and sustainability (RE17) — retained for completeness, flagged as only partly in scope. |
| **Differentiator flag added** | RM1, RM2, RM5 marked as High importance despite weak literature attention. |
| **Definitions tightened** | All 14 provisional definitions rewritten to be evidence-grounded and testable, with an explicit `expected_capabilities` field for Phase 5. |
| RM12 unchanged in scope | Still "support", not "guarantee", reproducibility. |

## 9. Corroboration from RQ1 (Track A)

The Track A bibliometric corpus (5,139 works, `results/track_a/`) independently reproduces the pattern this framework responds to: literature attention concentrates on data management (50.8 %) and analysis/workflow (41.9 %) and falls to 3.7 % for idea/question and 7.0 % for provenance. The three differentiator requirements sit in exactly that gap.

## 10. Handoff

- **Phase 4 (GitHub capability analysis):** catalogue native functionalities against the `expected_capabilities` of RM1–RM15.
- **Phase 5 (requirement–feature mapping):** fill `github_support` per requirement (Direct 3 / Partial 2 / Limited 1 / Not supported 0), combine with `lifecycle_requirements_matrix.csv` for the coverage profile, write into `framework/mapping/`.
- **Phase 6 (reference architecture):** organise the Direct/Partial functionalities into components and workflows.
