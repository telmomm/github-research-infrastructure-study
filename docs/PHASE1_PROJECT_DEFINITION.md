# Phase 1 — Project Definition

# From Code Repository to Research Infrastructure: Evaluating GitHub for Managing the Scientific Research Lifecycle

**Status:** Phase 1 deliverable (roadmap step 1 of 12)
**Target journal:** *Scientometrics* (Springer Nature)
**Manuscript language:** English
**Framing decision:** Hybrid — bibliometric mapping of the field + requirement–feature coverage analysis + reusable reference architecture/template (see §7 and `DECISION_LOG.md`, decisions D1–D4)

---

# 1. Purpose of this document

This document consolidates and closes Phase 1 of the roadmap. It fixes, as the authoritative reference for all subsequent phases:

1. the research problem;
2. the study aim and objectives;
3. the research questions (revised for the hybrid framing);
4. the conceptual scope and boundaries;
5. the target-journal positioning and fit argument;
6. the intended contributions;
7. the manuscript structure;
8. the repository architecture.

Where this document and earlier docs (`PAPER_PLAN.md`, `RESEARCH_QUESTION.md`, `RESEARCH_DESIGN.md`) disagree, **this document takes precedence**; the earlier docs are retained as design history and are being aligned incrementally.

---

# 2. Research problem

Scientific research projects produce a chain of interdependent artifacts — research question, protocol, literature corpus, data, analysis code, computational environment, intermediate results, figures, tables, manuscript, publication, software, supplementary material — that evolve continuously over a project's lifetime.

In common practice these artifacts and the activities that generate them are distributed across disconnected systems: email, cloud storage, local folders, spreadsheets, reference managers, statistical software, task managers, code repositories and manuscript editors. Each tool may serve its local function well, but the **coordination layer between them is largely absent**.

The consequences reported in the literature include weak decision traceability, incomplete process documentation, inconsistent versioning, limited research provenance, and low project visibility for collaborators and third parties. These are precisely the properties that open-science and reproducibility agendas require, yet the *management* of the research process — as opposed to the archiving of its outputs — has received comparatively little systematic, quantitative attention.

Code-hosting platforms, and GitHub in particular, already provide primitives for coordination, versioning, issue tracking, structured discussion, review and automation. Whether — and to what extent — these primitives can be organised into an infrastructure for managing the *research process itself*, and which stages of the research lifecycle such an infrastructure can actually cover, has not been established on an evidentiary basis.

---

# 3. Study aim

> **To characterise the scholarly literature on digital infrastructure for research-process management, derive a lifecycle-structured set of research management requirements from it, and determine quantitatively to what extent GitHub's native functionalities cover those requirements — consolidating the covered functionalities into a reusable reference architecture and project template, and probing its feasibility through a self-referential implementation.**

The study does **not** aim to show that GitHub is superior to, or a replacement for, specialised research infrastructure. It aims to establish *where, how and to what extent* GitHub can serve as a coordination, documentation and traceability layer for the research lifecycle.

---

# 4. Study objectives

| # | Objective | RQ | Phase |
|---|---|---|---|
| O1 | Build and describe a bibliographic corpus on digital / platform-based research-process management; analyse its temporal, disciplinary, venue and thematic structure; identify under-addressed lifecycle stages. | RQ1 | 2 |
| O2 | From a screened subset of the corpus, extract and thematically organise research project management requirements across the research lifecycle. | RQ2 | 2–3 |
| O3 | Catalogue GitHub's native functionalities relevant to research management and map each requirement to functionalities with an explicit support-level rubric. | RQ3 | 4–5 |
| O4 | Compute coverage indicators (per requirement, per requirement category, per lifecycle stage; support-level distribution). | RQ3 | 5 |
| O5 | Consolidate covered functionalities into a reference architecture and an operational, reusable GitHub research-project template. | RQ4 | 6–7 |
| O6 | Implement the framework self-referentially on this project and package the template as a transferable artifact; assess feasibility, traceability and limitations against a fragmented-workflow baseline. | RQ5 | 8–9 |

---

# 5. Research questions

## Main research question

> **To what extent can GitHub function as an integrated infrastructure for managing scientific research projects across the research lifecycle?**

## RQ1 — Bibliometric structure of the field *(science-of-science component)*

> How has the scholarly literature on digital infrastructure for managing the research process evolved in volume, disciplinary spread, publication venues and thematic structure, and which research-lifecycle stages are under-represented?

- **Method:** descriptive bibliometrics + co-word / keyword co-occurrence mapping (e.g., `bibliometrix`, VOSviewer) over the full corpus.
- **Output:** field map, trend analysis, lifecycle-coverage gap analysis.

## RQ2 — Research management requirements

> What research project management requirements across the research lifecycle can be derived from the screened literature?

- **Method:** thematic extraction and classification on the screened subset (PRISMA 2020 flow).
- **Output:** Research Management Requirements Framework (requirement ID, definition, evidence, lifecycle stage, category).

## RQ3 — GitHub coverage of requirements

> To what extent, with what support level, and with what limitations do GitHub's native functionalities cover the identified requirements, and how is that coverage distributed across research-lifecycle stages?

- **Method:** GitHub capability catalogue + requirement×functionality mapping with a 4-level rubric (Direct / Partial / Limited / Not supported), scored 3/2/1/0.
- **Output:** requirement–feature matrix; coverage indicators; lifecycle-coverage profile.

## RQ4 — Reference architecture and template

> How can the covered functionalities be organised into a coherent reusable reference architecture and project template for research-lifecycle management?

- **Method:** synthesis of the mapping into components, relationships, workflows and lifecycle integration; operationalisation as a GitHub template repository.
- **Output:** reference architecture; reusable template.

## RQ5 — Feasibility and limitations

> What does a self-referential implementation, together with the reusable template, reveal about the feasibility, traceability gains and limitations of GitHub-based research management relative to a fragmented workflow?

- **Method:** self-referential case study (this repository) + template packaging; structured evaluation on six dimensions (requirement coverage, traceability, documentation, organization, transparency, usability) with an explicit fragmented-workflow comparison.
- **Output:** evaluation results; limitations; boundary conditions.

## RQ → Results mapping

```
RQ1 ─────────────► Results §1  Bibliometric map of the field
RQ2 + RQ3 ───────► Results §2  Requirements and GitHub coverage
RQ4 + RQ5 ───────► Results §3  Reference architecture, template, feasibility
```

## Propositions (retained from `RESEARCH_QUESTION.md`, unchanged)

P1 research projects need structured lifecycle-spanning management mechanisms; P2 a substantial share of those requirements is supportable by native GitHub functionality or structured patterns; P3 those functionalities can be organised into a reusable lifecycle architecture; P4 the framework improves organization and traceability versus a fragmented approach; P5 GitHub-based management has real limits and cannot replace all specialised infrastructure.

---

# 6. Conceptual scope and boundaries

## 6.1 Key constructs

| Construct | Working definition for this study |
|---|---|
| **Research project management** | Coordination, documentation, traceability and preservation of the activities and artifacts of a scientific research project — distinct from the *scientific* content of the work and from commercial/industrial project management. |
| **Research lifecycle** | Idea → question → planning → literature → methods → data → analysis → results → manuscript → publication → outputs. Used as the common spine for requirements, mapping and coverage. |
| **Research infrastructure (in this study)** | A coordination/documentation/traceability layer connecting research activities and artifacts — not physical facilities, HPC, LIMS or clinical data systems. |
| **GitHub native functionality** | Features available in GitHub's standard product without third-party Marketplace apps: repositories, Issues, Projects, Milestones, Discussions, branches, Pull Requests, Markdown/README/wiki, Actions, Releases, Labels, and the Git version-control substrate. Marketplace/third-party integrations are out of scope; GitHub-plan differences are noted where they affect availability. |
| **Support level** | Direct (3) native feature meets the requirement; Partial (2) supported with additional process/convention; Limited (1) marginal support; Not supported (0). |

## 6.2 In scope

- Scholarly / scientific research-process management across all disciplines.
- GitHub as the platform under evaluation.
- A bibliometric corpus plus a screened requirement-extraction subset (nested design, §6.4).
- A single self-referential implementation plus a discipline-independent reusable template.

## 6.3 Out of scope

- Judging the scientific validity or quality of any research.
- Institutional research assessment / evaluation metrics of researchers.
- Full laboratory information management, clinical data management, or data-repository functions.
- Claiming GitHub replaces specialised research infrastructure.
- Multi-site, multi-team or longitudinal usability trials (named as future work).
- Comparison against other code-hosting platforms (GitLab, Codeberg, etc.) beyond brief discussion.

## 6.4 Nested literature design

Two nested sets are used and must be kept distinct in reporting:

- **Corpus (broad):** all records retrieved by the search strategy after de-duplication — analysed bibliometrically for RQ1.
- **Screened subset (deep):** records passing title/abstract and full-text screening against the inclusion criteria in `LITERATURE_REVIEW.md` — used for requirement extraction (RQ2). A PRISMA 2020 flow diagram documents the reduction from corpus to subset.

## 6.5 Parameters to fix at the start of Phase 2

- Databases: Scopus + Web of Science Core Collection as primary; OpenAlex/Dimensions as complementary coverage check; Google Scholar for grey-literature spot checks only.
- Time window: 2008 (GitHub launch) – 2025 inclusive.
- Language: English-language records for extraction; non-English retained in corpus counts.
- Document types: articles, reviews, conference papers; editorials/notes excluded from the screened subset.
- Bibliometric tooling: `bibliometrix` (R) and/or VOSviewer; export formats and field tags to be logged in `DATA_MANAGEMENT.md`.
- Inter-coder reliability: a second coder double-codes a random ~20% of the screened subset for requirement extraction; agreement reported (e.g., Cohen's κ or percentage agreement).

---

# 7. Target-journal positioning (*Scientometrics*, Springer Nature)

## 7.1 Fit argument

*Scientometrics* publishes quantitative studies of the science of science, scholarly communication, open science and research infrastructure. The hybrid framing gives the paper a bibliometric backbone (RQ1: corpus construction, trend and co-word analysis, gap identification) of the kind the journal routinely publishes, and adds a structured, reproducible coverage analysis (RQ2–RQ3) with explicit indicators. The reference architecture and template (RQ4–RQ5) are presented as a **synthesised, secondary contribution**, not as the paper's centre of gravity — this keeps the manuscript within the journal's scope.

## 7.2 What reviewers will scrutinise (and the mitigation)

| Scrutiny | Mitigation baked into the design |
|---|---|
| Reproducibility of the bibliometric dataset | Full query strings, dates, database versions, export files deposited; scripts released. |
| Subjectivity of requirement extraction and mapping | Explicit rubric; second-coder reliability on 20%; every mapping cell carries an evidence note. |
| "Framework" contributions being borderline for the journal | Framework/template kept to one Results section and one figure/table set; quantitative coverage results lead. |
| Single-case, self-referential evaluation / developer bias | Declared as a limitation; evaluation criteria pre-specified in `EVALUATION_PROTOCOL.md`; repository history is the evidence. |

## 7.3 Reporting standards to follow

- PRISMA 2020 for the screened subset (flow diagram + checklist as supplement).
- Bibliometric methods reported per common *Scientometrics* practice (data source, retrieval date, cleaning, indicators, software + versions).
- Data-availability statement; corpus, coding sheet and mapping matrix on Zenodo/OSF with DOI (connects to the prior GitHub–Zenodo–ORCID workflow).

## 7.4 Backup venues (if rejected on scope grounds)

*Quantitative Science Studies* (QSS), *Research Evaluation*, *PeerJ Computer Science*, *Journal of Open Research Software*.

---

# 8. Intended contributions

1. A bibliometric map of the literature on digital infrastructure for research-process management, with an explicit research-lifecycle gap analysis (RQ1).
2. A literature-derived, lifecycle-structured Research Management Requirements Framework (RQ2).
3. A reproducible requirement×functionality coverage analysis of GitHub, with per-stage coverage indicators (RQ3).
4. A GitHub-based research-management reference architecture (RQ4).
5. A reusable, discipline-independent GitHub research-project template, plus a self-referential feasibility assessment against a fragmented-workflow baseline (RQ4–RQ5).

---

# 9. Manuscript structure (hybrid)

```
1  Introduction
   1.1 Complexity and artifact proliferation in modern research
   1.2 Fragmentation of research-process management
   1.3 Research-lifecycle management vs. output archiving
   1.4 Code-hosting platforms beyond software; GitHub primitives
   1.5 Gap, aim, research questions (RQ1–RQ5)

2  Materials and Methods
   2.1 Overall design (nested bibliometric + coverage + synthesis)
   2.2 Corpus construction and bibliometric analysis (RQ1)
   2.3 Screening and requirement extraction (RQ2); reliability
   2.4 GitHub capability catalogue and mapping rubric (RQ3)
   2.5 Coverage indicators (RQ3)
   2.6 Reference architecture and template synthesis (RQ4)
   2.7 Self-referential implementation and evaluation protocol (RQ5)

3  Results
   3.1 Bibliometric map of the field (RQ1)
   3.2 Requirements and GitHub coverage (RQ2, RQ3)
   3.3 Reference architecture, template and feasibility (RQ4, RQ5)

4  Discussion
   4.1 Principal findings
   4.2 GitHub as a research-process coordination layer
   4.3 Which lifecycle stages benefit most / least
   4.4 Practical implications (researchers, groups, institutions)
   4.5 Relation to the GitHub–Zenodo–ORCID reproducibility workflow
   4.6 Limitations
   4.7 Future research

5  Conclusions
```

Figures/tables: as in `FIGURES_AND_TABLES.md`, plus (new) a bibliometric field map, a corpus timeline, and a PRISMA flow diagram.

---

# 10. Repository architecture (Phase 1 output)

Confirmed from `REPOSITORY_ARCHITECTURE.md`, with additions for the hybrid framing (marked **+**):

```
github-research-infrastructure-study/
│
├── README.md
├── LICENSE
├── CITATION.cff
│
├── docs/                         # design, protocols, decisions (this phase)
│
├── literature/
│   ├── search/                   # + query strings, exports, retrieval logs (corpus)
│   ├── screening/                # + PRISMA records, inclusion decisions (subset)
│   ├── bibliometrics/            # + bibliometrix/VOSviewer inputs, scripts, maps
│   ├── extraction/               # requirement coding sheets, reliability
│   └── references/               # .bib
│
├── data/
│   ├── raw/                      # corpus dataset as retrieved
│   ├── processed/                # de-duplicated / cleaned corpus, coding tables
│   └── README.md
│
├── analysis/
│   ├── scripts/                  # + bibliometric + coverage-indicator scripts
│   ├── notebooks/
│   └── results/                  # figures, coverage matrices, indicator tables
│
├── framework/
│   ├── requirements/             # Research Management Requirements Framework
│   ├── mapping/                  # requirement × functionality matrix
│   └── architecture/             # reference architecture
│
├── template/
│   └── github-research-project-template/   # reusable artifact (separate repo on release)
│
├── case-study/                   # self-referential implementation evidence
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

Two-repository strategy retained: this repository is the study; `github-research-project-template` is extracted as an independent reusable repository at release.

---

# 11. Phase 1 exit checklist

- [x] Research problem stated (§2)
- [x] Study aim and objectives fixed (§3–§4)
- [x] Research questions revised for hybrid framing (§5)
- [x] Conceptual scope and boundaries defined (§6)
- [x] Target-journal positioning and fit argument documented (§7)
- [x] Contributions listed (§8)
- [x] Manuscript structure drafted (§9)
- [x] Repository architecture confirmed and extended (§10)
- [x] Phase 1 decisions logged (`DECISION_LOG.md`, D1–D5)
- [x] `RESEARCH_DESIGN.md` and `LITERATURE_REVIEW.md` rewritten for the hybrid framing
- [ ] `PAPER_PLAN.md` and `RESEARCH_QUESTION.md` carry alignment notes; full rewrite deferred to manuscript drafting (Phase 11)

---

# 12. Handoff to Phase 2

Phase 2 (Literature analysis) begins from:

1. the fixed search parameters in §6.5;
2. the nested corpus / screened-subset design in §6.4;
3. the review protocol in `LITERATURE_REVIEW.md` (to be updated with the bibliometric branch);
4. `literature/` and `data/` directory scaffolding from §10.

First Phase 2 tasks: finalise database list and access; freeze and register the search strings; execute retrieval; log the corpus; run de-duplication.
