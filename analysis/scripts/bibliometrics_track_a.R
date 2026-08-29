#!/usr/bin/env Rscript
# Track A bibliometric analysis (RQ1).
#
# Input : data/processed/corpus.csv  (from build_corpus.py)
# Output: results/track_a/*.csv  + manuscript/figures/track_a/*.png
#
# Install once:
#   install.packages(c("bibliometrix", "readr", "dplyr", "stringr", "tidyr", "ggplot2"))
# Optional (pull straight from the API instead of the CSV): install.packages("openalexR")
#
# Run: Rscript analysis/scripts/bibliometrics_track_a.R

suppressPackageStartupMessages({
  library(readr); library(dplyr); library(stringr); library(tidyr); library(ggplot2)
})
have_biblio <- requireNamespace("bibliometrix", quietly = TRUE)

# Resolve repo root: walk up from the working directory until data/ is found.
root <- getwd()
for (i in 1:5) {
  if (dir.exists(file.path(root, "data")) && dir.exists(file.path(root, "literature"))) break
  root <- normalizePath(file.path(root, ".."))
}
corpus_fp <- file.path(root, "data", "processed", "corpus.csv")
res_dir   <- file.path(root, "results", "track_a")
fig_dir   <- file.path(root, "manuscript", "figures", "track_a")
dir.create(res_dir, showWarnings = FALSE, recursive = TRUE)
dir.create(fig_dir, showWarnings = FALSE, recursive = TRUE)

corpus <- read_csv(corpus_fp, show_col_types = FALSE)
message(sprintf("corpus: %d works, %d with DOI", nrow(corpus), sum(nchar(corpus$doi) > 0)))

## 1. Annual production -------------------------------------------------------
prod <- corpus %>% filter(!is.na(publication_year)) %>% count(publication_year, name = "n")
write_csv(prod, file.path(res_dir, "annual_production.csv"))
ggplot(prod, aes(publication_year, n)) +
  geom_col() +
  labs(x = NULL, y = "publications", title = "Track A corpus — annual production") +
  theme_minimal()
ggsave(file.path(fig_dir, "annual_production.png"), width = 7, height = 4, dpi = 200)

## 2. Sources / venues ------------------------------------------------------
src <- corpus %>% filter(nchar(source) > 0) %>% count(source, sort = TRUE, name = "n")
write_csv(src, file.path(res_dir, "top_sources.csv"))

## 3. Countries -----------------------------------------------------------
countries <- corpus %>%
  filter(nchar(countries) > 0) %>%
  separate_rows(countries, sep = ";\\s*") %>%
  filter(nchar(countries) > 0) %>%
  count(countries, sort = TRUE, name = "n")
write_csv(countries, file.path(res_dir, "countries.csv"))

## 4. Concepts -> research-lifecycle stage mapping -----------------------
# Edit this lookup after eyeballing results/track_a/top_concepts.csv.
concepts <- corpus %>%
  filter(nchar(concepts) > 0) %>%
  separate_rows(concepts, sep = ";\\s*") %>%
  mutate(concept = str_trim(str_remove(concepts, ":[0-9.]+$"))) %>%
  filter(nchar(concept) > 0) %>%
  count(concept, sort = TRUE, name = "n")
write_csv(concepts, file.path(res_dir, "top_concepts.csv"))

stage_lex <- list(
  idea_question   = c("research question", "hypothesis", "ideation"),
  planning        = c("project management", "research planning", "grant", "proposal"),
  literature      = c("systematic review", "literature review", "bibliometrics"),
  methods         = c("protocol", "study design", "preregistration", "methodology"),
  data            = c("research data management", "data curation", "data management", "fair"),
  analysis        = c("workflow", "scientific workflow", "pipeline", "reproducibility", "computation"),
  provenance      = c("provenance", "lineage", "traceability"),
  dissemination   = c("preprint", "repository", "open access", "scholarly communication"),
  outputs_id      = c("persistent identifier", "doi", "orcid", "research information system"),
  coordination    = c("collaboration", "coordination", "virtual research environment", "science gateway"),
  governance      = c("research policy", "governance", "sustainability", "funding")
)
stage_hits <- lapply(names(stage_lex), function(st) {
  pat <- paste0(stage_lex[[st]], collapse = "|")
  tibble(stage = st, n = sum(str_detect(tolower(corpus$concepts), pat) |
                              str_detect(tolower(corpus$abstract), pat), na.rm = TRUE))
}) %>% bind_rows()
write_csv(stage_hits, file.path(res_dir, "lifecycle_stage_hits.csv"))
message("lifecycle stage hits (quantitative Track A view) -> compare with literature/lifecycle_coverage.csv")

## 5. Keyword co-occurrence + thematic map (bibliometrix) --------------
if (have_biblio) {
  library(bibliometrix)
  # bibliometrix wants Web-of-Science-style columns; map the essentials.
  M <- corpus %>%
    transmute(
      AU = str_replace_all(authors, ";\\s*", ";"),
      TI = title,
      AB = abstract,
      PY = suppressWarnings(as.integer(publication_year)),
      SO = source,
      DI = doi,
      DE = str_replace_all(keywords, ";\\s*", ";"),
      ID = str_replace_all(concepts, ":[0-9.]+", ""),
      TC = suppressWarnings(as.integer(cited_by_count)),
      DB = "OPENALEX",
      AU_CO = countries
    ) %>% as.data.frame()
  M$SR <- paste0("DOC", seq_len(nrow(M)))
  try({
    res <- biblioAnalysis(M)
    capture.output(summary(res, k = 20, pause = FALSE), file = file.path(res_dir, "biblioAnalysis_summary.txt"))
  }, silent = TRUE)
  try({
    png(file.path(fig_dir, "coword_network.png"), width = 1400, height = 1000, res = 150)
    NetMatrix <- biblioNetwork(M, analysis = "co-occurrences", network = "keywords", sep = ";")
    networkPlot(NetMatrix, n = 40, Title = "Keyword co-occurrence", type = "fruchterman",
                labelsize = 0.7, cluster = "louvain")
    dev.off()
  }, silent = TRUE)
  try({
    tm <- thematicMap(M, field = "ID", n = 250, minfreq = 5)
    ggsave(file.path(fig_dir, "thematic_map.png"), tm$map, width = 8, height = 7, dpi = 200)
    write_csv(tm$words, file.path(res_dir, "thematic_map_words.csv"))
  }, silent = TRUE)
} else {
  message("bibliometrix not installed — skipped co-word network and thematic map")
}

message("done. tables in ", res_dir, " ; figures in ", fig_dir)
