# data/

| Path | Contents |
|---|---|
| `raw/` | Data exactly as acquired — never edited. Not committed if large; link the source. |
| `processed/` | Cleaned / derived data produced by `analysis/scripts/`. Regenerable. |
| `external/` | **Pointers** (`.md` / `.txt` with URL + DOI + checksum) to large data held in a data repository. |

Large data does **not** go in Git. Put a pointer in `external/` and link it from the relevant issue and from `docs/methodology.md`.
