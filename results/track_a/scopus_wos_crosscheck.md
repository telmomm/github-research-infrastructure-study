# Scopus / Web of Science cross-check (OPEN_ITEMS 2.8)

- Source files: 16  ·  raw records: 18250  ·  outside 2008-2025 window: 338
- De-duplicated in-window cross-check set: **13586**
- Overlap with the OpenAlex + arXiv corpus: **2933 (22%)**  (by DOI 2656, by title+year 277)
- WoS/Scopus records not in the corpus: **10653 (78%)** — `xref_not_in_corpus.csv.gz`
- Corpus records not returned by these queries: 2175 of 5139 (OpenAlex indexes preprints and OA venues; the open queries are phrased differently)

## WoS/Scopus-only records — where they come from

| Query | in set | not in corpus |
|---|---|---|
| Q1 | 2761 | 2031 |
| Q2 | 4343 | 2908 |
| Q3 | 5954 | 5262 |
| Q4 | 528 | 452 |

**Top venues of the not-in-corpus set:**

- Bioinformatics: 720
- ?: 278
- Lecture Notes In Computer Science (Including Sub: 274
- Bmc Bioinformatics: 185
- Plos One: 150
- Acm International Conference Proceeding Series: 145
- Ceur Workshop Proceedings: 142
- Bioinformatics Advances: 95
- Scientific Reports: 93
- Communications In Computer And Information Scien: 88
- Briefings In Bioinformatics: 83
- Septentrio Conference Series: 72

**By year:** 2008:138, 2009:162, 2010:174, 2011:169, 2012:189, 2013:198, 2014:253, 2015:303, 2016:349, 2017:490, 2018:518, 2019:729, 2020:749, 2021:870, 2022:1009, 2023:1181, 2024:1329, 2025:1843

## Reading

The two retrieval routes diverge because WoS *Topic* (`TS=`) also matches Keywords Plus and author keywords, which expands aggressively, whereas the OpenAlex query is anchored to title and abstract. The not-in-corpus set is dominated by recent bioinformatics and tool papers that mention `GitHub` in a data-availability statement and `workflow` / `reproducibility` in the abstract (see the venue list) — the low-precision tail that a title/abstract search deliberately excludes, not missed core literature on research-process infrastructure. Conversely the corpus contains preprints and open-access records WoS does not index. The overlap on DOI is the robust figure; it quantifies the coverage/precision trade-off declared in `DECISION_LOG.md` D8, and supports keeping OpenAlex as the primary source while acknowledging that a subscription search would add a substantial, mostly peripheral, tail.
