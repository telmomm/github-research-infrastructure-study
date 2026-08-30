# Scopus / Web of Science cross-check (OPEN_ITEMS 2.8)

- Source files: 12  ·  raw records: 9441  ·  outside 2008-2025 window: 338
- De-duplicated in-window cross-check set: **8819**
- Overlap with the OpenAlex + arXiv corpus: **2373 (27%)**  (by DOI 2186, by title+year 187)
- WoS/Scopus records not in the corpus: **6446 (73%)** — `xref_not_in_corpus.csv`
- Corpus records not returned by these queries: 2717 of 5139 (OpenAlex indexes preprints and OA venues; the open queries are phrased differently)

## WoS/Scopus-only records — where they come from

| Query | in set | not in corpus |
|---|---|---|
| Q1 | 1035 | 561 |
| Q2 | 3064 | 1826 |
| Q3 | 4484 | 3875 |
| Q4 | 236 | 184 |

**Top venues of the not-in-corpus set:**

- Bioinformatics: 718
- ?: 278
- Bmc Bioinformatics: 180
- Plos One: 144
- Bioinformatics Advances: 95
- Scientific Reports: 89
- Briefings In Bioinformatics: 82
- Septentrio Conference Series: 72
- Siam Journal On Scientific Computing: 67
- Ieee Transactions On Geoscience And Remote Sensi: 64
- Plos Computational Biology: 62
- Computers In Biology And Medicine: 56

**By year:** 2008:15, 2009:25, 2010:34, 2011:37, 2012:51, 2013:62, 2014:102, 2015:160, 2016:196, 2017:303, 2018:328, 2019:471, 2020:502, 2021:635, 2022:698, 2023:822, 2024:895, 2025:1110

## Reading

The two retrieval routes diverge because WoS *Topic* (`TS=`) also matches Keywords Plus and author keywords, which expands aggressively, whereas the OpenAlex query is anchored to title and abstract. The not-in-corpus set is dominated by recent bioinformatics and tool papers that mention `GitHub` in a data-availability statement and `workflow` / `reproducibility` in the abstract (see the venue list) — the low-precision tail that a title/abstract search deliberately excludes, not missed core literature on research-process infrastructure. Conversely the corpus contains preprints and open-access records WoS does not index. The overlap on DOI is the robust figure; it quantifies the coverage/precision trade-off declared in `DECISION_LOG.md` D8, and supports keeping OpenAlex as the primary source while acknowledging that a subscription search would add a substantial, mostly peripheral, tail.
