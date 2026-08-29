# Research Design

# From Code Repository to Research Infrastructure: Evaluating GitHub for Managing the Scientific Research Lifecycle

**Aligned with:** `PHASE1_PROJECT_DEFINITION.md` (authoritative) · `DECISION_LOG.md` D1–D5
**Target journal:** *Scientometrics* (Springer Nature)
**Framing:** Hybrid — bibliometric field analysis + reproducible requirement–feature coverage analysis + synthesised reference architecture and reusable template

---

# 1. Purpose

This document defines the overall research design: the logic connecting the research questions to the data, methods and outputs. It operationalises the Phase 1 project definition and governs Phases 2–10 of the roadmap.

The study investigates whether, and to what extent, GitHub's native functionalities can serve as an integrated coordination, documentation and traceability layer for scientific research projects across the research lifecycle. It does **not** treat GitHub as a replacement for specialised research infrastructure.

---

# 2. Research problem

Scientific projects generate a chain of interdependent artifacts — research question, protocol, literature corpus, data, analysis code, computational environment, intermediate results, figures, tables, manuscript, publication, software, supplementary material — that evolve over the life of the project.

In common practice these artifacts and their generating activities are spread across disconnected systems (email, cloud storage, local folders, spreadsheets, reference managers, statistical software, code repositories, task managers, manuscript editors). Each tool serves its local function, but the coordination layer between them is largely absent. The literature associates this fragmentation with weak decision traceability, incomplete process documentation, inconsistent versioning, limited provenance and low project visibility.

Code-hosting platforms already provide primitives for coordination, versioning, issue tracking, structured discussion, review and automation. Whether these primitives can be organised into an infrastructure for managing the research *process* — and which lifecycle stages such an infrastructure can actually cover — has not been established on an evidentiary basis. The *management* of the research process, as distinct from the archiving of its outputs, has received little systematic quantitative attention.

---

# 3. Central research concept

```
SCIENTIFIC LITERATURE ON RESEARCH-PROCESS INFRASTRUCTURE
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
BIBLIOMETRIC MAP          SCREENED SUBSET
(field structure,          (requirement
 trends, gaps)              extraction)
        │                       │
        │                       ▼
        │          RESEARCH MANAGEMENT REQUIREMENTS
        │                       │
        │                       ▼
        │          GITHUB CAPABILITY CATALOGUE
        │                       │
        │                       ▼
        └────────►  REQUIREMENT × FUNCTIONALITY COVERAGE
                                │
                                ▼
                    REFERENCE ARCHITECTURE + TEMPLATE
                                │
                                ▼
                 SELF-REFERENTIAL IMPLEMENTATION + EVALUATION
```

---

# 4. Study aim

> **To characterise the scholarly literature on digital infrastructure for research-process management, derive a lifecycle-structured set of research management requirements from it, and determine quantitatively to what extent GitHub's native functionalities cover those requirements — consolidating the covered functionalities into a reusable reference architecture and project template, and probing its feasibility through a self-referential implementation.**

---

# 5. Objectives and research questions

| Objective | Research question | Method | Phase |
|---|---|---|---|
| O1 Characterise the field | **RQ1** How has the literature on digital infrastructure for managing the research process evolved in volume, disciplines, venues and thematic structure, and which lifecycle stages are under-represented? | Descriptive bibliometrics + co-word / keyword co-occurrence mapping over the full corpus | 2 |
| O2 Derive requirements | **RQ2** What research project management requirements across the research lifecycle can be derived from the screened literature? | Thematic extraction and classification on the PRISMA-screened subset | 2–3 |
| O3–O4 Map and quantify coverage | **RQ3** To what extent, with what support level and limitations do GitHub's native functionalities cover the requirements, and how is coverage distributed across lifecycle stages? | Capability catalogue + requirement×functionality mapping (4-level rubric) + coverage indicators | 4–5 |
| O5 Synthesise the artifact | **RQ4** How can the covered functionalities be organised into a coherent reusable reference architecture and project template? | Synthesis of components, relationships, workflows, lifecycle integration; template operationalisation | 6–7 |
| O6 Probe feasibility | **RQ5** What does a self-referential implementation plus the reusable template reveal about feasibility, traceability gains and limitations versus a fragmented workflow? | Self-referential case study + template packaging + structured six-dimension evaluation with fragmented-workflow comparison | 8–9 |

**Main research question.** *To what extent can GitHub function as an integrated infrastructure for managing scientific research projects across the research lifecycle?*

**RQ → Results mapping.** RQ1 → Results §1; RQ2 + RQ3 → Results §2; RQ4 + RQ5 → Results §3.

---

# 6. Research approach

The study is a **multi-method evidence synthesis** with three coupled components:

```
COMPONENT A — BIBLIOMETRIC ANALYSIS        (quantitative, descriptive)
   corpus construction · trends · disciplines · venues · co-word maps · lifecycle gap analysis
                    │
                    ▼
COMPONENT B — COVERAGE ANALYSIS            (structured, reproducible mapping)
   requirement extraction · GitHub capability catalogue · requirement×functionality matrix · coverage indicators
                    │
                    ▼
COMPONENT C — SYNTHESIS + FEASIBILITY      (design synthesis, secondary)
   reference architecture · reusable template · self-referential implementation · six-dimension evaluation
```

Component A supplies the science-of-science backbone expected by the target journal. Component B is the quantitative core of the contribution. Component C delivers the transferable artifact concisely and tests it once, self-referentially.

The design retains a design-and-evaluation element (Component C) but subordinates it to the empirical components; it is **not** presented as a design-science paper.

---

# 7. Research process

```
PHASE 1  Project definition                     → PHASE1_PROJECT_DEFINITION.md
   │
   ▼
PHASE 2  Literature analysis (two tracks)        → corpus + screened subset + extraction dataset
   │        A: bibliometric corpus  ·  B: PRISMA-screened subset
   ▼
PHASE 3  Requirements framework                  → Research Management Requirements Framework
   │
   ▼
PHASE 4  GitHub capability analysis              → GitHub capability catalogue
   │
   ▼
PHASE 5  Requirement–feature mapping             → coverage matrix + indicators
   │
   ▼
PHASE 6  Reference architecture                  → conceptual architecture + lifecycle model
   │
   ▼
PHASE 7  Reusable template                       → github-research-project-template
   │
   ▼
PHASE 8  Case study (self-referential + template)→ implementation evidence
   │
   ▼
PHASE 9  Evaluation                              → six-dimension scores + comparison
   │
   ▼
PHASE 10 Analysis                                → coverage, feasibility, strengths, limitations
```

Evidence produced in each phase feeds the next.

---

# 8. Phase 1 — Project definition

Fixes the research problem, aim, objectives, RQs, conceptual scope, journal positioning, manuscript structure and repository architecture. Output: `PHASE1_PROJECT_DEFINITION.md`. Closed 2026-08-29.

---

# 9. Phase 2 — Literature analysis (two-track, nested)

Detailed protocol in `LITERATURE_REVIEW.md`. Summary:

## Track A — Bibliometric corpus (RQ1)

- Databases: Scopus + Web of Science Core Collection (primary); OpenAlex / Dimensions (coverage check); Google Scholar (grey-literature spot checks only).
- Registered search strings; retrieval date logged; window 2008–2025.
- De-duplication → **corpus**.
- Analysis: publication-year trend, document types, source/venue distribution, disciplinary categories, country/affiliation, author keywords and Keywords Plus, keyword co-occurrence and co-word maps (`bibliometrix` / VOSviewer), thematic evolution, and a mapping of corpus themes onto research-lifecycle stages to expose under-represented stages.

## Track B — Screened subset (RQ2)

- Title/abstract screening then full-text assessment against the inclusion/exclusion criteria in `LITERATURE_REVIEW.md`.
- PRISMA 2020 flow diagram from corpus to included studies.
- Data extraction per the variable table in `LITERATURE_REVIEW.md`.
- Requirement extraction: literature evidence → identified challenge → management need → requirement → requirement category.
- Reliability: a second coder double-codes a random ~20% of included studies for requirement extraction; agreement reported (Cohen's κ or percentage agreement); disagreements reconciled and logged.

## Outputs

Corpus dataset · bibliometric indicator tables and maps · PRISMA record · included-study dataset · data-extraction table · requirement-extraction dataset with evidence.

---

# 10. Phase 3 — Research Management Requirements Framework (RQ2)

Literature evidence is transformed into structured requirements:

```
LITERATURE EVIDENCE → RESEARCH MANAGEMENT CHALLENGE → MANAGEMENT NEED → REQUIREMENT → REQUIREMENT CATEGORY
```

Each requirement records: ID, name, definition, supporting evidence, research-lifecycle stage(s), category (planning / execution / documentation / collaboration / traceability / artifact management / automation / output management), relative importance. The provisional domains RM1–RM14 in `REQUIREMENTS_FRAMEWORKS.md` are the starting point and are revised against the extracted evidence. Requirement relationships (e.g., planning → task management → documentation → traceability → provenance) are modelled explicitly.

Output: **Research Management Requirements Framework**.

---

# 11. Phase 4 — GitHub capability analysis (RQ3)

GitHub **native** functionalities are catalogued (repositories, Issues, Projects, Milestones, Discussions, branches, Pull Requests, Markdown/README/wiki, Actions, Releases, Labels, and the Git substrate). Marketplace / third-party apps are out of scope; plan-dependent availability is noted.

Each functionality is assessed for: technical capability, research applicability, traceability preservation, integration with other activities, practical implementation complexity, and limitations.

Output: **GitHub capability catalogue**.

---

# 12. Phase 5 — Requirement–feature mapping and coverage indicators (RQ3)

```
REQUIREMENT → REQUIRED CAPABILITY → GITHUB FUNCTIONALITY → IMPLEMENTATION PATTERN → SUPPORT LEVEL
```

Support-level rubric (every cell carries an evidence note):

| Level | Score | Meaning |
|---|---|---|
| Direct | 3 | Native functionality meets the requirement |
| Partial | 2 | Supported with an additional process or convention |
| Limited | 1 | Marginal support only |
| Not supported | 0 | Cannot reasonably be met by GitHub alone |

Coverage indicators computed from the matrix:

- per-requirement support level;
- share of requirements Direct / Partial / Limited / Not supported;
- mean coverage per requirement category;
- **lifecycle-coverage profile**: mean coverage per lifecycle stage (idea → publication), cross-referenced with the RQ1 gap analysis;
- count of requirements needing complementary external tools.

Output: **requirement–feature matrix**, coverage indicator tables, lifecycle-coverage profile.

---

# 13. Phase 6 — Reference architecture (RQ4)

The mapping is synthesised into an architecture defining components, relationships, workflows, lifecycle integration and implementation principles. GitHub operates as a **central traceability and coordination layer**, not as a container for every research activity. Detail in `REFERENCE_ARCHITECTURE.md`.

Output: **GitHub-Based Research Management Reference Architecture**.

---

# 14. Phase 7 — Reusable template (RQ4)

The architecture is operationalised as `github-research-project-template`: repository structure, documentation templates, Issue templates, Pull Request template, labels, Project configuration, milestones, automation workflows, release procedure. Design principles: reusable, discipline-independent, understandable, adaptable, minimally complex, platform-native. Detail in `TEMPLATE_PROJECT.md`.

Output: **GitHub Research Project Template** (extracted as an independent repository at release).

---

# 15. Phase 8 — Case study: self-referential + template (RQ5)

Decision D5: the framework manages this study's own development (Option A), and the template is packaged as a transferable artifact evaluated at a second level.

The implementation demonstrates repository organisation, research planning (Project + milestones), Issue structure, documentation, artifact organisation, decision traceability, version history and output management. The repository history itself is the empirical evidence. Protocol and traceability demonstrations in `CASE_STUDY.md`.

Circularity and developer-evaluation bias are declared limitations (§20–§21).

Output: implemented research repository + packaged template + implementation observations.

---

# 16. Evaluation design (RQ5)

Protocol in `EVALUATION_PROTOCOL.md`. Six dimensions, each scored 0 (not supported) / 1 (partially) / 2 (fully):

| Dimension | Question |
|---|---|
| Requirement coverage | Are the identified requirements supported by the implemented framework? |
| Traceability | Can research activities, decisions and artifact relationships be reconstructed (question → method → data → analysis → result → manuscript)? |
| Documentation | Are major research processes systematically documented? |
| Organization | Are artifacts and tasks systematically structured? |
| Transparency | Can project progress and development be understood by a third party? |
| Usability | Can researchers realistically implement and maintain the framework? |

A **fragmented-workflow comparison** contrasts the GitHub implementation with a conventional email + documents + local files + separate tools setup across task, decision and version traceability, documentation, provenance and project visibility. The comparison identifies specific advantages and limitations rather than assuming the conventional workflow is ineffective.

Output: coverage score, traceability/documentation/organization/transparency/usability assessment, comparison table, implementation observations, identified limitations.

---

# 17. Units of analysis

| Unit | Description | Used for |
|---|---|---|
| U1 Bibliographic record | Publication in the corpus | RQ1 |
| U2 Included study | Screened publication with extracted data | RQ2 |
| U3 Research management requirement | Requirement derived from U2 | RQ2, RQ3 |
| U4 GitHub functionality | Native platform capability | RQ3 |
| U5 Requirement–functionality relationship | Mapping cell with support level and evidence | RQ3 |
| U6 Architecture component | Element of the reference architecture | RQ4 |
| U7 Case-study artifact | Issue, Project item, commit, PR, release, doc from the implementation | RQ5 |

---

# 18. Data sources

Scientific literature (Scopus, WoS, OpenAlex/Dimensions); GitHub official documentation; GitHub repository artifacts of this project (Issues, Projects, Discussions, commits, Pull Requests, workflow runs, Releases); structured evaluation records.

---

# 19. Evidence integration

```
LITERATURE ─┬─► BIBLIOMETRIC MAP (RQ1)
            └─► REQUIREMENTS (RQ2) ─► GITHUB ANALYSIS ─► COVERAGE MATRIX (RQ3)
                                                             │
                                                             ▼
                                              REFERENCE ARCHITECTURE + TEMPLATE (RQ4)
                                                             │
                                                             ▼
                                              SELF-REFERENTIAL IMPLEMENTATION + EVALUATION (RQ5)
```

---

# 20. Validity considerations

| Type | Question | Handling |
|---|---|---|
| Construct | Do the extracted requirements faithfully represent research-management needs? | Evidence-linked extraction; second-coder reliability; provisional RM1–RM14 revised against data. |
| Internal | Are coverage conclusions supported by the mapping? | Explicit rubric; per-cell evidence notes; scores and scripts released. |
| External | Do the requirements and architecture transfer across disciplines and project types? | Discipline-independent template; scope limited to scholarly research; multi-site transfer named as future work. |
| Reproducibility | Can the bibliometric and coverage results be regenerated? | Registered queries, retrieval dates, database versions, export files and scripts deposited (Zenodo/OSF). |
| Practical | Can researchers realistically run the framework? | Usability dimension in the evaluation; minimal-complexity template principle. |

---

# 21. Sources of bias and mitigation

Bias: researcher involvement in framework development; subjective requirement interpretation; single-case, self-referential evaluation; prior GitHub familiarity; selective feature use; database coverage bias; English-language bias.

Mitigation: transparent, registered methodology; `DECISION_LOG.md`; pre-specified evaluation criteria; evidence-based requirement extraction with reliability check; multi-database retrieval with OpenAlex/Dimensions cross-check; explicit statement of language and coverage limits; public release of all artifacts.

---

# 22. Expected scientific outputs

1. Bibliometric map of the research-process-infrastructure literature, with lifecycle gap analysis.
2. Literature-derived Research Management Requirements Framework.
3. Reproducible requirement×functionality coverage analysis of GitHub, with lifecycle-coverage profile.
4. GitHub-Based Research Management Reference Architecture.
5. Reusable GitHub Research Project Template.
6. Self-referential case-study implementation and six-dimension evaluation.
7. Deposited datasets (corpus, coding sheet, mapping matrix) with DOI.
8. Scientific manuscript for *Scientometrics*.

---

# 23. Relationship with the previous reproducibility workflow

The prior GitHub–Zenodo–ORCID workflow addresses the archiving and persistent identification of research **outputs**:

```
RESEARCH OUTPUT → GITHUB → ZENODO → DOI → ORCID
```

The present study addresses the management and traceability of the research **process** that produces those outputs:

```
IDEA → PLANNING → RESEARCH ACTIVITIES → DOCUMENTATION → ANALYSIS → MANUSCRIPT → OUTPUT
```

The two are complementary: process management upstream, output preservation downstream. The data-availability deposit in this study (§22.7) is itself an instance of the earlier workflow.

---

# 24. Final conceptual workflow

```
RESEARCH PROBLEM
      ▼
LITERATURE ANALYSIS ──► BIBLIOMETRIC MAP (RQ1)
      ▼
REQUIREMENT IDENTIFICATION (RQ2)
      ▼
REQUIREMENTS FRAMEWORK
      ▼
GITHUB CAPABILITY ANALYSIS
      ▼
REQUIREMENT–FEATURE MAPPING + COVERAGE INDICATORS (RQ3)
      ▼
REFERENCE ARCHITECTURE (RQ4)
      ▼
REUSABLE TEMPLATE (RQ4)
      ▼
SELF-REFERENTIAL CASE STUDY (RQ5)
      ▼
EVALUATION + FRAGMENTED-WORKFLOW COMPARISON (RQ5)
      ▼
SCIENTIFIC MANUSCRIPT
```
