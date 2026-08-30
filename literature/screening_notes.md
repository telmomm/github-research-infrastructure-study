# Screening Notes

## Evidence base

Track B is built on the Consensus Deep Search synthesis in `SOTA/SOTA.md`. The Deep Search applied machine-learned relevance filtering (230 papers screened, 155 above threshold after de-duplication, top 100 review/survey/synthesis papers retained for qualitative analysis). The 52 studies cited in the `SOTA.md` reference list are normalised in `included_studies.csv` as S01-S52.

## Inclusion logic

A study is retained when it addresses at least one of:

- scientific / scholarly research-process management, workflows or lifecycle models;
- research data management as an infrastructure or service problem;
- provenance, traceability or research-object assembly;
- research information systems, repositories or preprint platforms;
- open-science workflows and practice;
- version control / Git / GitHub use in research, or mining of software repositories;
- virtual research environments / science gateways;
- multisite coordination or post-award research management;
- emergent infrastructure (AI-assisted planning, digital twins, ethics-review platforms).

Priority window 2008-2025; earlier works (Davidson & Freire 2008; Curcin & Ghanem 2008; Lu & Zhang 2009; Ludäscher et al. 2009) retained as field-formation anchors.

## Exclusion logic

Excluded when a record:

- concerns only commercial / industrial project management with no transferable content;
- has no relationship to scientific research;
- addresses only technical infrastructure (e.g. scheduling internals) with no research-management implication — a small number of scheduling-only surveys are kept (S44, S49) solely as evidence of the maturity of the computational-workflow tradition;
- is an editorial, note, or abstract without a retrievable full text.

## Requirement extraction

From the included studies, literature challenges were traced to management needs and then to derived requirements (`requirements_extraction.csv`), following the chain in `docs/LITERATURE_REVIEW.md` §8.5:

```
study finding -> identified problem -> research management need -> requirement -> requirement category
```

Each requirement row is mapped to the provisional `RM1-RM14` domains in `docs/REQUIREMENTS_FRAMEWORKS.md` and carries its evidence studies and an SOTA section pointer. Requirement-attention levels (strong / moderate / weak-gap / emerging) record how well the literature covers each requirement, not how important it is.

## Cross-track note

The lifecycle-attention judgements in `lifecycle_coverage.csv` are qualitative, taken from `SOTA.md` §3.4, the Discussion and the Research Gaps section. Track A (Scopus / WoS bibliometrics) will produce an independent, quantitative lifecycle-coverage profile; the two are compared in the manuscript Discussion.

## Primary-study supplement (S53–S67) — added 2026-08-30, OPEN_ITEMS 2.6

The Consensus Deep Search prioritised review / survey / synthesis papers, so primary
empirical studies of Git/GitHub in research were under-sampled. `included_studies_primary.csv`
adds **15 targeted primary studies** (S53–S67): operational-rules papers (Sandve, Wilson,
Perez-Riverol, Ram, Bryan), discipline-specific empirical studies of GitHub-in-research
(Braga et al. ecology, Chen et al. wet-lab), the ReScience platform, and mining / bibliometric
studies of GitHub in the scholarly record (Escamilla, Kalliamvakou, Trisovic, Pimentel,
Milewicz). Selection was purposive (well-cited, on-topic), not a systematic search —
flagged as such. Strand = VC for all. DOIs are in the CSV; BibTeX for the subset actually
cited is generated and factchecked at manuscript stage (Phase 11).

This supplement does not change the RQ2 requirement extraction (RE01–RE17), which stays
on the review-based Track B corpus; it strengthens the RQ4/RQ5 discussion of GitHub-in-research
evidence and the RQ1 note that GitHub adoption in publications is itself measurable (S66).

## Known limitations of the Track B base

- Single-provider synthesis (Consensus / Semantic Scholar backbone); database coverage and the ML relevance filter are not fully transparent — hence the complementary Scopus / WoS retrieval in Track A.
- Review / survey papers were prioritised, so primary empirical studies of GitHub-in-research are under-sampled (partly offset by S05, S09-S11 from the related reproducibility-workflow corpus).
- Biomedical and computer-science venues dominate the base; LIS is well represented for RDM. Other disciplines are thin.
- English-language and 2008-2025 priority window.

## Excluded records

The Deep Search did not expose the individual excluded records. Explicit exclusions made during normalisation into this repository are logged here as they occur.

| ID | Item | Reason |
|---|---|---|
| — | (none yet) | — |
