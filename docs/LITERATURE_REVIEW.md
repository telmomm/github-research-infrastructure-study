# Literature Analysis Protocol

# From Code Repository to Research Infrastructure: Evaluating GitHub for Managing the Scientific Research Lifecycle

**Aligned with:** `PHASE1_PROJECT_DEFINITION.md` (authoritative) · `RESEARCH_DESIGN.md` · `DECISION_LOG.md` D2–D4
**Target journal:** *Scientometrics* (Springer Nature)

---

# 1. Purpose

This document defines the Phase 2 literature analysis. Under the hybrid framing it has **two coupled tracks** over a single retrieval:

- **Track A — Bibliometric analysis** of the full retrieval corpus, answering RQ1 (structure of the field, trends, disciplines, venues, thematic map, under-represented lifecycle stages).
- **Track B — Structured review** of a PRISMA-screened subset, producing the evidence base for RQ2 (research management requirements).

The two tracks are **nested**: Track B's included studies are a screened subset of Track A's corpus. A PRISMA 2020 flow diagram documents the reduction.

This is not a comprehensive systematic review of all research-management literature. Track A is a bibliometric field study; Track B is a structured, reliability-checked evidence extraction.

---

# 2. Review objectives

| Track | Objective |
|---|---|
| A | Characterise the scholarly literature on digital / platform-based infrastructure for managing the research process, and identify which research-lifecycle stages are under-addressed. |
| B | Determine what requirements a system or framework should support to manage scientific research projects across the research lifecycle. |

---

# 3. Review questions

## Track A (bibliometric)

- **LRQ-A1** How has the annual volume of publications on research-process infrastructure evolved (2008–2025)?
- **LRQ-A2** Which disciplines, source titles and document types dominate the corpus?
- **LRQ-A3** What is the thematic structure of the field (author keywords, Keywords Plus, keyword co-occurrence / co-word clusters, thematic evolution)?
- **LRQ-A4** Which research-lifecycle stages (idea → publication) are well represented and which are under-represented in the corpus?
- **LRQ-A5** What are the most cited / most central works and concepts?

## Track B (requirements)

- **LRQ-B1** What challenges are reported in managing scientific research projects?
- **LRQ-B2** What activities must be managed across the research lifecycle?
- **LRQ-B3** What requirements are associated with effective research project management?
- **LRQ-B4** What mechanisms support research traceability, transparency and provenance?
- **LRQ-B5** What digital tools or infrastructures have been proposed to support scientific research workflows, and with what reported limitations?

---

# 4. Scope

Focus: scientific and scholarly research-process management. Relevant areas: scientific research / workflow / lifecycle management; scientific workflow systems; research information management; research provenance; research documentation; collaborative research; reproducible research; Open Science workflows; research data management; digital research infrastructures; use of code-hosting / version-control platforms in research.

General software-engineering or commercial project-management studies are included **only** when they contribute transferable concepts for scientific research management.

Constructs and boundaries as defined in `PHASE1_PROJECT_DEFINITION.md` §6.

---

# 5. Search strategy

## 5.1 Databases

| Role | Database |
|---|---|
| Primary (corpus + screening) | Scopus; Web of Science Core Collection |
| Coverage cross-check | OpenAlex; Dimensions |
| Grey-literature spot checks only | Google Scholar (first ~100 hits per query, not merged into the corpus counts) |

The final database list, access route and index versions are logged in `DATA_MANAGEMENT.md` before the definitive search.

## 5.2 Retrieval parameters (fixed at Phase 2 start)

- Time window: 2008–2025 inclusive (GitHub launched 2008).
- Document types for the corpus: articles, reviews, conference papers.
- Language: all languages retained in the corpus (Track A); English-language full texts required for extraction (Track B). Non-English records are counted and reported.
- Fields searched: title, abstract, author keywords (Scopus `TITLE-ABS-KEY`; WoS `TS=`).
- Each query string, database, date of retrieval, number of hits and export file name is recorded in `literature/search/search-log.md`.

## 5.3 Search concepts

```
( SCIENTIFIC / ACADEMIC RESEARCH )
        AND
( PROJECT MANAGEMENT  OR  WORKFLOW  OR  LIFECYCLE  OR  COORDINATION )
        AND / OR
( TRACEABILITY  OR  DOCUMENTATION  OR  PROVENANCE  OR  TRANSPARENCY )
        AND / OR
( DIGITAL PLATFORM  OR  INFRASTRUCTURE  OR  VERSION CONTROL  OR  GIT / GITHUB )
```

## 5.4 Example query blocks (to be finalised and registered)

```
"research project management" AND (scientific OR academic OR research)
"research workflow management"
"scientific workflow" AND (management OR collaboration OR documentation OR provenance)
"research lifecycle" AND (management OR infrastructure OR platform)
"research provenance" AND (traceability OR workflow OR management)
"open science" AND (workflow OR infrastructure OR "project management")
"research data management" AND (workflow OR lifecycle OR platform)
("version control" OR git OR github OR gitlab) AND (research OR science) AND (workflow OR "project management" OR reproducib*)
"reproducible research" AND (workflow OR infrastructure OR "project management")
```

The final Boolean strings (one per database, with field tags) are registered in `literature/search/search-strings.md` and treated as frozen once retrieval begins; any later change is a new `DECISION_LOG.md` entry.

---

# 6. Process overview

```
REGISTERED SEARCH (per database)
        │
        ▼
RECORD IDENTIFICATION  ──────────────►  export files (RIS/BibTeX/CSV) in literature/search/
        │
        ▼
DE-DUPLICATION  ─────────────────────►  CORPUS  ──►  TRACK A: bibliometric analysis (RQ1)
        │
        ▼
TITLE / ABSTRACT SCREENING
        │
        ▼
FULL-TEXT ASSESSMENT
        │
        ▼
INCLUDED STUDIES  ──────────────────►  TRACK B: data extraction + requirement extraction (RQ2)
        │
        ▼
SECOND-CODER RELIABILITY (~20%)  ───►  agreement statistic + reconciliation log
```

A PRISMA 2020 flow diagram records counts at identification, de-duplication, screening, full-text eligibility and inclusion.

---

# 7. Track A — Bibliometric analysis

## 7.1 Dataset preparation

- Merge database exports; de-duplicate on DOI, then normalised title + year.
- Field cleaning: author name disambiguation (best effort), source-title normalisation, keyword lemmatisation, country/affiliation parsing.
- Record retained/removed counts; store `data/raw/` (as retrieved) and `data/processed/` (cleaned corpus).

## 7.2 Indicators and analyses

| Analysis | Indicator / method |
|---|---|
| Production over time | Publications per year; compound annual growth rate |
| Document / source profile | Counts by document type; top source titles; Bradford zones |
| Disciplinary profile | Scopus subject areas / WoS categories distribution |
| Geography | Publications by country / affiliation; collaboration (co-authorship) overview |
| Citation structure | Most cited documents; most cited sources; reference spectroscopy optional |
| Thematic structure | Author-keyword and Keywords Plus frequency; keyword co-occurrence network; co-word clustering; thematic map (centrality vs. density); thematic evolution across time slices |
| Lifecycle gap analysis | Map corpus clusters / keywords onto lifecycle stages (idea, question, planning, literature, methods, data, analysis, results, manuscript, publication, outputs); report publications per stage; flag under-represented stages |

## 7.3 Tooling

`bibliometrix` (R) and/or VOSviewer. Scripts and configuration in `literature/bibliometrics/` and `analysis/scripts/`; software versions recorded. All figures reproducible from the deposited corpus.

## 7.4 Track A outputs

Cleaned corpus dataset · indicator tables · production timeline · thematic map and co-word network · thematic-evolution diagram · lifecycle gap table · list of central works/concepts.

---

# 8. Track B — Structured review

## 8.1 Screening

Two stages, screening decisions and reasons recorded per record.

### Stage 1 — Title and abstract

Assess relevance to: scientific research; research-process management; research workflows; lifecycle management; traceability; documentation; provenance; digital research infrastructure.

### Stage 2 — Full text

Assess against §8.2 / §8.3 and extract: management challenges, required activities, proposed mechanisms, reported limitations, infrastructure requirements.

## 8.2 Inclusion criteria

A study may be included if it:

1. addresses scientific or academic research workflows;
2. investigates research project management;
3. discusses research-lifecycle activities;
4. identifies research-management challenges;
5. describes requirements for research infrastructures;
6. addresses research provenance;
7. investigates research traceability;
8. discusses research documentation;
9. addresses collaboration in scientific research;
10. provides transferable findings relevant to research management.

## 8.3 Exclusion criteria

A study is excluded if it:

1. focuses exclusively on commercial project management with no transferable content;
2. has no relationship with scientific research;
3. addresses only technical infrastructure with no management implications;
4. provides insufficient methodological information;
5. is a duplicate;
6. is not accessible for full-text assessment;
7. is an editorial, note, abstract-only or non-English full text.

## 8.4 Data extraction

Extracted into `literature/extraction/extraction-table.csv`:

| Variable | Description |
|---|---|
| Study ID | Unique identifier |
| Authors / Year | Bibliographic |
| Research domain | Scientific discipline |
| Study type | Review, framework, empirical study, tool paper, etc. |
| Research problem | Identified problem |
| Management challenge | Reported challenge |
| Research activity | Lifecycle activity addressed |
| Proposed mechanism | Proposed solution / tool |
| Requirement | Identified requirement (explicit or implicit) |
| Lifecycle stage | Stage(s) the requirement applies to |
| Evidence | Supporting finding / quotation locator |
| Reported limitation | Stated limitation of the proposed mechanism |
| Relevance | Relevance to this study (high / medium / low) |

## 8.5 Requirement extraction logic

```
STUDY FINDING → IDENTIFIED PROBLEM → RESEARCH MANAGEMENT NEED → REQUIREMENT → REQUIREMENT CATEGORY
```

Examples:

```
Researchers use multiple disconnected systems      → fragmentation      → centralised coordination
Research decisions are hard to reconstruct          → weak traceability  → decision documentation and traceability
Analysis steps are not recorded                     → weak provenance    → activity-to-artifact linkage
```

Requirements are recorded with standardised descriptions and linked to their evidence. Provisional categories (revised against the data): planning, task management, documentation, collaboration, communication, version control, decision traceability, research provenance, artifact management, output management, transparency, reproducibility support, automation.

## 8.6 Reliability

A second coder independently codes a random ~20% sample of included studies for the *Requirement*, *Lifecycle stage* and *Requirement category* fields. Agreement is reported (Cohen's κ or percentage agreement per field). Disagreements are reconciled by discussion; unresolved cases go to a third reader. The reconciliation is logged in `literature/extraction/reliability.md`.

## 8.7 Track B outputs

PRISMA 2020 flow diagram + checklist · included-study dataset · data-extraction table · requirement-extraction dataset with evidence · reliability report · provisional requirement categories → handed to Phase 3.

---

# 9. Synthesis

## Descriptive synthesis (Track A)

Publication years, domains, document types, source titles, thematic clusters, lifecycle-stage coverage.

## Thematic synthesis (Track B)

Recurring challenges, management needs, proposed mechanisms, common requirements, reported limitations.

## Requirement synthesis (Track B → Phase 3)

Transformation of extracted evidence into the structured Research Management Requirements Framework (`REQUIREMENTS_FRAMEWORKS.md`).

## Cross-track integration

The Track A lifecycle gap analysis and the Track B requirement set are compared: stages that are under-represented in the literature but carry strong requirements are highlighted in the Discussion, and later cross-referenced with the GitHub lifecycle-coverage profile (Phase 5).

---

# 10. Outputs of Phase 2

1. Registered search strategy (strings, databases, dates, logs).
2. De-duplicated bibliographic corpus.
3. Bibliometric indicator tables, maps and lifecycle gap analysis.
4. PRISMA 2020 flow diagram and checklist.
5. Included-study dataset.
6. Data-extraction table.
7. Requirement-extraction dataset with supporting evidence.
8. Provisional requirement categories.
9. Inter-coder reliability report.

Datasets 2, 5, 6 and 7 are prepared for deposit (Zenodo/OSF) with the data-availability statement.

---

# 11. Reporting in the manuscript

The Materials and Methods and Results sections report: databases and index versions; retrieval dates; full search strings (supplement); inclusion/exclusion criteria; record counts at each stage; the PRISMA 2020 diagram; bibliometric data-cleaning steps; indicators and software versions; the requirement-extraction procedure and reliability statistics.

---

# 12. Relationship to the framework

```
SCIENTIFIC LITERATURE
      │
      ├─► BIBLIOMETRIC MAP (RQ1)  ─────────────┐
      │                                         │
      └─► SCREENED SUBSET                        │
             │                                  ▼
             ▼                        DISCUSSION: gaps vs. requirements
   RESEARCH MANAGEMENT CHALLENGES               │
             │                                  ▼
             ▼                        GITHUB LIFECYCLE-COVERAGE PROFILE (Phase 5)
   RESEARCH MANAGEMENT REQUIREMENTS
             │
             ▼
   REQUIREMENTS FRAMEWORK  ─►  GITHUB CAPABILITY MAPPING
```

---

# 13. Limitations

- Heterogeneous terminology across disciplines; terminology overlap between research management and commercial project management.
- Database coverage and indexing bias; different subject classifications across Scopus and WoS (mitigated by OpenAlex/Dimensions cross-check).
- English-language bias in requirement extraction.
- Publication bias; limited literature explicitly on GitHub-based research management.
- Requirement extraction involves interpretation (mitigated by evidence linkage and second-coder reliability).
- Author-name and keyword disambiguation in bibliometrics is best-effort.

These are documented here and discussed in the manuscript.
