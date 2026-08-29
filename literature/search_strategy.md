# Literature Search Strategy

Phase 2 of the roadmap. Protocol: `docs/LITERATURE_REVIEW.md`. Framing: hybrid (see `docs/DECISION_LOG.md` D2).

The literature analysis has two coupled tracks over the same topic:

- **Track B — structured evidence review** (this file, Part A): the base of the manuscript's background / related-work section and the source of the requirement extraction. Evidence base: a Consensus Deep Search synthesis, captured in `SOTA/SOTA.md` and normalised into `included_studies.csv`, `requirements_extraction.csv` and `lifecycle_coverage.csv`.
- **Track A — bibliometric field analysis** (this file, Part B): a complementary Scopus + Web of Science retrieval, still to be executed, that produces the corpus for RQ1 (trends, disciplines, venues, co-word map, lifecycle gap analysis).

---

# Part A — Track B evidence base (completed)

## A.1 Source

`SOTA/SOTA.md` — "Research Process Management Infrastructure", a synthesis produced with Consensus Deep Search over >220M records indexed from Semantic Scholar, PubMed and other sources.

## A.2 Search concepts (six groups, as reported by the Deep Search)

1. Foundational workflow and infrastructure models.
2. Terminology variants for lifecycle, coordination, provenance and platforms.
3. Lifecycle-stage-specific searches (idea, planning, methods, data, analysis, dissemination).
4. Challenges and requirements.
5. Git / version-control terms.
6. Adjacent literatures: open science, digital humanities, data curation.

## A.3 Screening and inclusion flow (as reported)

| Step | Count |
|---|---|
| Broad seed search (records identified) | 1,290,829 |
| Additional targeted searches | large overlapping sets |
| Citation-crawl related papers | 3,231 |
| Machine-learned relevance screening | 230 |
| Passed relevance threshold after de-duplication | 155 |
| Included for qualitative analysis (top review / survey / synthesis papers) | 100 |
| Cited in `SOTA.md` reference list and normalised here | 52 |

Priority window: 2008-2025, with earlier conceptual anchors allowed for field formation.

## A.4 Normalisation into this repository

| Artifact | Content |
|---|---|
| `included_studies.csv` | 52 studies (S01-S52): id, authors, year, title, venue, DOI, document type, literature strand, lifecycle focus, relevance, notes |
| `requirements_extraction.csv` | 17 requirement rows (RE01-RE17): literature challenge -> management need -> derived requirement, mapped to `RM1-RM14` from `docs/REQUIREMENTS_FRAMEWORKS.md`, with lifecycle stage, literature-attention level and evidence studies |
| `lifecycle_coverage.csv` | 15 lifecycle stages with literature-attention level, dominant infrastructure traditions and evidence |
| `screening_notes.md` | inclusion / exclusion logic and known limitations of the Deep Search base |
| `references.bib` | BibTeX for S01-S52 |

## A.5 Strand coding used in `included_studies.csv`

| Code | Strand |
|---|---|
| SWf | scientific workflow systems |
| RDM | research data management / library services |
| PROV | provenance systems |
| RIS | research information systems, repositories, preprint platforms |
| OS | open science workflows and practice |
| VC | version control / Git / GitHub / mining software repositories |
| VRE | virtual research environments / science gateways |
| COORD | multisite coordination / post-award management |
| EMERG | emergent (AI-assisted planning, digital twins, ethics platforms) |

---

# Part B — Track A bibliometric search (planned, not yet executed)

## B.1 Objective

Build a de-duplicated bibliographic corpus for RQ1: production over time, document and source profile, disciplinary profile, geography, citation structure, keyword co-occurrence / thematic map, and a mapping of themes onto research-lifecycle stages.

## B.2 Databases

| Role | Database |
|---|---|
| Primary | Scopus; Web of Science Core Collection |
| Coverage cross-check | OpenAlex; Dimensions |
| Grey-literature spot check only | Google Scholar (first ~100 hits per query, not merged into counts) |

## B.3 Parameters

- Window: 2008-2025 inclusive.
- Document types: articles, reviews, conference papers.
- Language: all retained in the corpus; English full text required for any extraction.
- Fields: Scopus `TITLE-ABS-KEY`; WoS `TS=`.
- Retrieval date, hit counts and export filenames logged in `search_log.md` (to be created at execution).

## B.4 Draft query blocks (to be finalised and frozen before retrieval)

```
("research project management" OR "research workflow management" OR "research lifecycle"
  OR "research process management" OR "scientific workflow")
AND
(management OR coordination OR documentation OR provenance OR traceability OR transparency)

("research data management" OR "open science") AND (workflow OR lifecycle OR infrastructure OR platform OR "project management")

("version control" OR git OR github OR gitlab) AND (research OR science OR scholarly)
  AND (workflow OR "project management" OR reproducib* OR collaboration OR provenance)

"research provenance" AND (traceability OR workflow OR management OR lifecycle)

("virtual research environment" OR "science gateway" OR "research information system" OR CRIS)
  AND (workflow OR lifecycle OR "project management" OR coordination)
```

Each database gets one final Boolean string with field tags, registered in `search_strings.md` and frozen once retrieval begins; any later change is a new `DECISION_LOG.md` entry.

## B.5 Tooling

`bibliometrix` (R) and/or VOSviewer. Inputs and scripts under `literature/bibliometrics/` and `analysis/scripts/`; software versions recorded.

## B.6 Outputs

Cleaned corpus (`data/processed/`), indicator tables, production timeline, thematic map / co-word network, thematic-evolution diagram, lifecycle gap table, PRISMA 2020 flow diagram (corpus -> screened subset).
