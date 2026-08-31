# Scientometrics submission checklist

Target journal: *Scientometrics* (Springer Nature). GitHub issue #9 / OPEN_ITEMS 12.6.
Verify each item against the live author guidelines
(<https://link.springer.com/journal/11192/submission-guidelines>) before upload — the
notes below are from the Springer Nature general instructions and the `sn-jnl` template.

## Manuscript file

| Item | Status | Note |
|---|---|---|
| Springer Nature LaTeX template (`sn-jnl.cls`) | ✅ | `manuscript/paper.tex`, builds clean with `latexmk` (bibtex 0 warnings, no undefined refs), 19 pp. |
| **Reference style** | ⚠️ **decision needed** | Currently `sn-mathphys-num` → numbered `[1]` citations. *Scientometrics* uses **author–year (APA-like)**. Switch the class option to `sn-basic` and rebuild; check `\citep`/`\citet` render as "(Author, year)". This re-flows the bibliography — do it as its own step. |
| Title page: title, author, affiliation, e-mail | ✅ | `\author*`, `\affil`, `\email` set. |
| **ORCID** | ❌ | Add the author ORCID iD (`\orcidlink{...}` or the template's ORCID field). Not yet in `paper.tex`. |
| Structured abstract | ✅ | Aims / Methods / Results / Conclusion, **290 words**. Springer's soft limit is ~250; 290 is acceptable for a structured abstract but trim if the editor flags it. |
| Keywords | ✅ | 6 (`research infrastructure, research process management, GitHub, research lifecycle, reproducibility, open science`). Guideline range 4–6. |
| Section numbering (Introduction … Conclusions) | ✅ | Intro, Materials and Methods, Results, Discussion, Conclusions, Declarations. |
| Figures: vector, embedded, captioned, referenced | ⚠️ | 3 figures. `coword_map` is fine; `fig3_architecture` and `fig4_traceability` are SVG→PDF via `rsvg-convert` and are being redrawn to print quality (**issue #8**). All are `\ref`-cited and captioned. |
| Tables: editable text, captioned, referenced | ✅ | 6 tables, `booktabs`, all `\ref`-cited. |
| Line numbers for review | ⬜ | Add `\usepackage{lineno}\linenumbers` for the review copy if the editor asks (not in the template by default). |
| Word count | ℹ️ | Body ≈ 4.9k words (excl. abstract, references, tables). *Scientometrics* has no hard limit; typical research articles run 6–10k. Consider further depth in Methods/Results if reviewers ask for it. |

## Declarations (present in `paper.tex` §Declarations)

| Declaration | Status |
|---|---|
| Data and code availability (with the two Zenodo DOIs) | ✅ issue #5 |
| Competing interests | ✅ "no competing interests" |
| Funding | ✅ "no specific grant …" |
| Ethics approval | ✅ "Not applicable" (publication metadata only) |
| Author contributions | ✅ single author, CRediT-style sentence |
| Consent to participate / for publication | ⬜ Not applicable (no human participants) — add an explicit "Not applicable" line if the submission system requires all five. |
| Acknowledgements | ⬜ optional — add if anyone is to be thanked. |

## References

| Item | Status | Note |
|---|---|---|
| Every citation resolves; no orphan bib entries | ✅ | 28 cited, bibtex "used 28 entries", 0 undefined. |
| Cited-subset metadata verified | ✅ issue #7 | All 24 (now 28) cited entries checked against Crossref; `literature/references_factcheck.md` "Phase 12" section. |
| DOIs present on all entries | ✅ | Every entry has a `doi`. |
| `references.bib` in the submission bundle | ✅ | `manuscript/references.bib`. |
| Uncited entries in `references.bib` | ℹ️ | 34 uncited entries retain SOTA-derived values; harmless (not printed) but delete before upload if the journal wants a lean bib. |

## Cover letter

| Item | Status |
|---|---|
| Draft cover letter | ✅ `manuscript/cover_letter.md` |
| States novelty / fit for *Scientometrics* | ✅ |
| Confirms originality, not under review elsewhere | ✅ |
| Suggested reviewers (3–4, no conflicts) | ⬜ add before submission |
| Opposed reviewers, if any | ⬜ optional |

## Pre-upload steps for the author

1. Decide and apply the **reference style** (`sn-basic`), rebuild, re-check citations.
2. Add the **ORCID iD** to the title page.
3. Cut a **fresh Zenodo release** for the submitted version so the software DOI resolves to the exact commit (`.github/release-checklist.md`); confirm the DOI in `paper.tex`, `CITATION.cff` and the README badge still match.
4. Finish the **figure redraw** (issue #8) and rebuild.
5. Add **suggested reviewers** to the cover letter.
6. Generate the final **PDF** from `build.sh`; upload `paper.tex`, `references.bib`, `sn-jnl.cls`, `sn-mathphys-num.bst` (or the `sn-basic` bst), the figure files, and the PDF.
7. Optionally add **line numbers** for the review copy.
