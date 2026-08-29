# Track A — Frozen Search Strings

**Status:** frozen 2026-08-30. Any change after this point requires a new `docs/DECISION_LOG.md` entry.
**Window:** 2008–2025 inclusive. **Document types:** article, review, conference paper. **Language:** no restriction at retrieval; English full text required for any extraction.
**Primary source:** OpenAlex (open, reproducible — see §"Open sources" below and `DECISION_LOG.md` D8). Scopus/WoS strings below are kept as optional cross-checks if access appears. Record every run in `search_log.md`.

> **Executed 2026-08-30:** OpenAlex 15 queries (5,936 works) + arXiv 5 queries (462 preprints) → **5,139-work corpus** after removing repository deposits and duplicates. Scopus/WoS: not run.

---

## Concept blocks

- **C1 process/management:** research project management, research workflow management, research lifecycle, research process management, scientific workflow
- **C2 function:** management, coordination, documentation, provenance, traceability, transparency, monitoring
- **C3 platform/infra:** digital platform, infrastructure, version control, git, github, gitlab, virtual research environment, science gateway, research information system, CRIS
- **C4 adjacent:** research data management, open science, reproducible research

---

## Scopus (TITLE-ABS-KEY)

### Q1 — core process management
```
TITLE-ABS-KEY (
  ( "research project management" OR "research workflow management" OR "research workflow"
    OR "research lifecycle" OR "research life cycle" OR "research process management"
    OR "scientific workflow" OR "scholarly workflow" )
  AND ( management OR coordination OR documentation OR provenance OR traceability
        OR transparency OR monitoring OR "decision*" )
)
AND PUBYEAR > 2007 AND PUBYEAR < 2026
AND ( LIMIT-TO ( DOCTYPE , "ar" ) OR LIMIT-TO ( DOCTYPE , "re" ) OR LIMIT-TO ( DOCTYPE , "cp" ) )
```

### Q2 — data management / open science + workflow
```
TITLE-ABS-KEY (
  ( "research data management" OR "open science" OR "reproducible research" )
  AND ( workflow OR lifecycle OR "life cycle" OR infrastructure OR platform OR "project management" )
)
AND PUBYEAR > 2007 AND PUBYEAR < 2026
AND ( LIMIT-TO ( DOCTYPE , "ar" ) OR LIMIT-TO ( DOCTYPE , "re" ) OR LIMIT-TO ( DOCTYPE , "cp" ) )
```

### Q3 — version control in research
```
TITLE-ABS-KEY (
  ( "version control" OR git OR github OR gitlab )
  AND ( research OR science OR scientific OR scholarly )
  AND ( workflow OR "project management" OR reproducib* OR collaboration OR provenance OR documentation )
)
AND PUBYEAR > 2007 AND PUBYEAR < 2026
AND ( LIMIT-TO ( DOCTYPE , "ar" ) OR LIMIT-TO ( DOCTYPE , "re" ) OR LIMIT-TO ( DOCTYPE , "cp" ) )
```

### Q4 — research environments / information systems
```
TITLE-ABS-KEY (
  ( "virtual research environment" OR "science gateway" OR "virtual laboratory"
    OR "research information system" OR "current research information system" OR CRIS )
  AND ( workflow OR lifecycle OR "life cycle" OR "project management" OR coordination OR provenance )
)
AND PUBYEAR > 2007 AND PUBYEAR < 2026
AND ( LIMIT-TO ( DOCTYPE , "ar" ) OR LIMIT-TO ( DOCTYPE , "re" ) OR LIMIT-TO ( DOCTYPE , "cp" ) )
```

---

## Web of Science Core Collection (TS = Topic)

### Q1
```
TS = (
  ( "research project management" OR "research workflow management" OR "research workflow"
    OR "research lifecycle" OR "research life cycle" OR "research process management"
    OR "scientific workflow" OR "scholarly workflow" )
  AND ( management OR coordination OR documentation OR provenance OR traceability
        OR transparency OR monitoring OR decision* )
)
```
Refine: Publication Years 2008–2025; Document Types Article OR Review OR Proceedings Paper.

### Q2
```
TS = (
  ( "research data management" OR "open science" OR "reproducible research" )
  AND ( workflow OR lifecycle OR "life cycle" OR infrastructure OR platform OR "project management" )
)
```
Refine as Q1.

### Q3
```
TS = (
  ( "version control" OR git OR github OR gitlab )
  AND ( research OR science OR scientific OR scholarly )
  AND ( workflow OR "project management" OR reproducib* OR collaboration OR provenance OR documentation )
)
```
Refine as Q1.

### Q4
```
TS = (
  ( "virtual research environment" OR "science gateway" OR "virtual laboratory"
    OR "research information system" OR "current research information system" OR CRIS )
  AND ( workflow OR lifecycle OR "life cycle" OR "project management" OR coordination OR provenance )
)
```
Refine as Q1.

---

## Open sources (primary — executed)

### OpenAlex — primary corpus

Endpoint: `https://api.openalex.org/works`. Common filters on every query:
`from_publication_date:2008-01-01`, `to_publication_date:2025-12-31`, `type:article|review|proceedings-article`.
Run via `analysis/scripts/fetch_openalex.py --mailto <email>` (polite pool). Query tags and `title_and_abstract.search` strings (frozen):

| Tag | search string |
|---|---|
| Q1a | `"research project management" (scientific OR academic OR research)` |
| Q1b | `"research workflow management"` |
| Q1c | `"research workflow" (management OR coordination OR documentation OR provenance)` |
| Q1d | `"research lifecycle" (management OR infrastructure OR platform OR coordination)` |
| Q1e | `"research life cycle" (management OR infrastructure OR platform)` |
| Q1f | `"research process management"` |
| Q1g | `"scientific workflow" (management OR collaboration OR documentation OR provenance)` |
| Q2a | `"research data management" (workflow OR lifecycle OR infrastructure OR platform OR "project management")` |
| Q2b | `"open science" (workflow OR infrastructure OR "project management" OR lifecycle)` |
| Q2c | `"reproducible research" (workflow OR infrastructure OR "project management")` |
| Q3a | `github (research OR science OR scholarly) (workflow OR "project management" OR reproducibility OR provenance OR collaboration)` |
| Q3b | `"version control" (research OR science OR scholarly) (workflow OR "project management" OR reproducibility OR documentation)` |
| Q4a | `"virtual research environment" (workflow OR lifecycle OR "project management" OR coordination)` |
| Q4b | `"science gateway" (workflow OR lifecycle OR "project management" OR coordination)` |
| Q4c | `"research information system" (workflow OR lifecycle OR coordination OR interoperability)` |

Cleaning: `data/raw/exclude_sources.txt` drops data/software-repository deposits (Zenodo, Figshare, Dryad, Dataverse, OSF, …) — these are not scholarly documents.

### arXiv — supplement (version-control / GitHub strand)

Endpoint: `http://export.arxiv.org/api/query`. Run via `analysis/scripts/fetch_arxiv.py`. `search_query` blocks (frozen 2026-08-30), abstract/title-scoped so this stays a supplement, 2008–2025:

| Tag | search_query |
|---|---|
| A1 | `abs:"version control" AND (abs:research OR abs:reproducibility OR abs:"scientific workflow" OR abs:"research software")` |
| A2 | `(ti:github OR abs:github) AND (abs:reproducibility OR abs:reproducible OR abs:"research software" OR abs:"scientific workflow" OR abs:"open science" OR abs:"version control") AND (cat:cs.DL OR cat:cs.SE OR cat:cs.CY OR cat:cs.DC)` |
| A3 | `abs:"scientific workflow" AND (abs:provenance OR abs:reproducibility OR abs:"workflow management")` |
| A4 | `abs:"research software" AND (abs:sustainability OR abs:reproducibility OR abs:citation OR abs:workflow)` |
| A5 | `abs:"reproducible research" AND (abs:workflow OR abs:infrastructure OR abs:"version control" OR abs:"project management")` |

### Dimensions (optional cross-check, not merged into primary counts)

- OpenAlex: `title_and_abstract.search` with the C1 phrase list; filter `from_publication_date=2008-01-01`, `to_publication_date=2025-12-31`, `type:article|review|proceedings-article`.
- Dimensions: "full data" search on the same C1 phrase list, 2008–2025, publication types Article / Proceeding.

Purpose: estimate how many relevant records Scopus + WoS miss; report the delta in the manuscript.

---

## Google Scholar (grey-literature spot check only)

Run Q1 and Q3 phrasings; inspect first 100 results each; add only items that clearly fit the inclusion criteria and are missing from the corpus, flagged `source=GS` in the corpus file. Not counted in database-recall figures.

---

## Export

Per database and per query: BibTeX + CSV/RIS with abstract, author keywords, Keywords Plus (WoS), affiliations, cited-by count, references where available. Save under `data/raw/<database>/<query>_<YYYYMMDD>.<ext>` and log in `search_log.md`.
