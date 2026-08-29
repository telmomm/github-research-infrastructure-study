# Traceability Demonstrations

Concrete chains reconstructed from artifacts actually present in this repository. Each realises the end-to-end path defined in the reference architecture (`framework/architecture/reference_architecture.md` §5).

---

## T-1 — Research question to output (RQ3)

```
RQ3  (PHASE1_PROJECT_DEFINITION.md §5)
 └─ requirements framework RM1–RM15  (framework/requirements/requirements_framework.csv)  ← RQ2/T09/D9
     └─ GitHub capability catalogue GC01–GC68  (framework/mapping/github_capability_catalogue.csv)  ← T10/D10
         └─ requirement_feature_matrix.csv  (support score + implementation pattern per RM)  ← T11/D11
             └─ coverage_indicators.py → results/framework/coverage_*.csv  ← T12
                 └─ coverage_analysis.md §9  (answer to RQ3)
                     └─ reference_architecture.md §9  (architecture realises the scores)  ← T13/D12
```
Every hop is a file reference or a decision id; the scripts (`summarise_*`, `coverage_indicators`) verify the RE→RM→GC→component references resolve.

## T-2 — Literature evidence to a framework requirement (RM5)

```
SOTA/SOTA.md §3.4  "upstream intellectual decisions not captured by provenance tools"
 └─ literature/requirements_extraction.csv  RE03  (evidence: S23, S41, S36)
     └─ requirements_framework.csv  RM5 "Decision traceability"  (differentiator = yes)
         └─ requirement_feature_matrix.csv  RM5 = Partial (2), pattern = decision-record convention
             └─ architecture_components.csv  B2 Decision Log + B3 Linkage Discipline
                 └─ template: .github/ISSUE_TEMPLATE/decision-record.yml + docs/decision-log.md
                     └─ this repo: docs/DECISION_LOG.md  D1–D14  (the convention, exercised)
```

## T-3 — Decision to affected artifacts (D8)

```
DECISION_LOG.md  D8  "Track A executed on open sources"
 ├─ "Affects" → literature/search_strings.md, search_log.md
 ├─ analysis/scripts/fetch_openalex.py, fetch_arxiv.py, build_corpus.py
 ├─ data/raw/openalex/, data/raw/arxiv/, data/processed/corpus.csv
 └─ results/track_a/*  →  PHASE2_PROGRESS.md "Track A first-run result"
```
The `Affects` line is the linkage-discipline convention (B3) applied at document level.

## T-4 — Task to change history (T14)

```
activity_register.csv  T14 "Build the reusable template"  (serves RQ4, milestone M7, decision D13)
 └─ template/github-research-project-template/ (33 files) + template/template_manifest.csv
     └─ check_template.py → results/framework/template_coverage.csv  (all components covered)
         └─ git commit "Phase 7"  (origin/main)
             └─ CHANGELOG.md  [Unreleased] → Phase 7 entry
```

---

## What is *not* demonstrated here

No chain runs through a GitHub **Issue number, Pull Request, or Release tag**, because the study was executed as a single-author sprint (decision D14). The chains above use file paths, decision ids and commit subjects instead. Phase 9 evaluates what this substitution costs against the six evaluation dimensions.
