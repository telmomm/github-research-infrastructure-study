# Crossref enrichment (OPEN_ITEMS 2.1)

- No-DOI corpus records processed: 250
- Confident Crossref matches (title Jaccard >= 0.6, year +/-1): **20** (8%)
- Output: `data/processed/corpus_enrichment.csv` (side table; corpus.csv unchanged)

Most no-DOI records are preprints, reports, or venue types Crossref does not index; the matched DOIs and citation counts are available for the manuscript's descriptive statistics but are not merged into the frozen corpus. OpenAlex `cited_by_count` remains the primary citation field for RQ1.
