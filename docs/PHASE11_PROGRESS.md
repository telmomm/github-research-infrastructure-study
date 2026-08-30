# Phase 11 — Manuscript Development

**Roadmap step:** 11 of 12 · **Target:** *Scientometrics* (Springer Nature) · **Class:** `sn-jnl` (sn-mathphys-num)
**Started / completed:** 2026-08-30 · **Status: COMPLETE (v1 draft)**

Full manuscript assembled from `analysis/findings.csv` and the framework artifacts.

---

## Output (`manuscript/`)

| File | State |
|---|---|
| `paper.tex` | **Complete v1 draft** — Abstract, Introduction (1.1–1.5), Materials and Methods (2.1–2.7), Results (3.1–3.3), Discussion (4.1–4.7), Conclusions, Declarations. 16 pp., compiles clean (0 undefined citations/refs). |
| `references.bib` | 62 entries — the 52 from `literature/references.bib` plus 10 primary GitHub-in-research studies actually cited. |
| `figures/fig3_architecture.pdf`, `fig4_traceability.pdf`, `coword_map.pdf` | Rendered from the SVGs via `rsvg-convert`. |
| `build.sh` | Regenerates figure PDFs then runs `latexmk`. |
| `paper.pdf` | Compiled draft. |

## Structure and finding map

| Section | Content | Findings / sources |
|---|---|---|
| Abstract | Aims / Methods / Results / Conclusion | F32 + headline numbers |
| 1 Introduction | complexity, fragmentation, process vs output, code-hosting platforms, RQ1–RQ5 | F01, F02, framing |
| 2 Materials and Methods | design; bibliometric corpus; review + extraction; capability catalogue + rubric; coverage indicators; architecture + template; self-referential evaluation | Phases 2–9 methods |
| 3.1 Bibliometric map | field structure, production, venues, co-word map (Fig 1), lifecycle stage-hit profile (Table 1) | F01–F05 |
| 3.2 Requirements + coverage | RM1–RM15 (Table 2), support levels, category means + differentiators (Table 3), external tools, lifecycle profile, robustness | F06–F16 |
| 3.3 Architecture, template, feasibility | 15-component architecture (Fig 3), traceability path (Fig 4), 33-file template, evaluation (Table 4), comparison (Table 5) | F17–F22 |
| 4 Discussion | convergence; coordination layer; lifecycle stages; practical implications; relation to output-preservation workflows; limitations; future research | F23–F31 |
| 5 Conclusions | answer to the main RQ | F32 |

4 tables + 3 figures. ~6,000 words of body text — on the short side for *Scientometrics*; expansion candidates noted below.

## Decisions logged

- `DECISION_LOG.md` D20 — manuscript assembled from `findings.csv`; hybrid structure per `PHASE1_PROJECT_DEFINITION.md` §9; figures rendered SVG→PDF via `rsvg-convert`; `references.bib` = 52 + 10 primary.

## Handoff to Phase 12

Final review, then: complete the three `OPEN_ITEMS.md` user-tasks (make repo public, run one live Issue→PR→Release cycle, Project screenshot), archive on Zenodo for a DOI, add the DOI to `paper.tex` and `CITATION.cff`, and submit.

## Open / optional (do not block Phase 12)

- [ ] Expand the body toward ~8,000 words: more depth in Methods 2.2–2.3 (query strings, PRISMA-style counts), a related-work paragraph per literature strand in the Introduction, and per-requirement narrative in Results 3.2.
- [ ] Full `references.bib` check for the cited subset (page ranges for article-numbered journals; `escamilla2022` volume) — `literature/references_factcheck.md`.
- [ ] Switch author-facing figures to vector PDF from a drawing tool if the SVG→PDF raster/label quality is insufficient at print size.
- [ ] Cover letter and *Scientometrics* submission checklist.
