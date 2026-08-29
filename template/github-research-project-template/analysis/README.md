# analysis/

| Path | Contents |
|---|---|
| `scripts/` | Analysis code. Each script regenerates a specific output. |
| `notebooks/` | Exploratory notebooks (keep outputs cleared in Git). |
| `results/` | Generated tables/figures. Regenerable — do not hand-edit. |

State the entry point and environment in `docs/methodology.md`. The reproducibility
workflow (`.github/workflows/reproduce.yml`) re-runs the analysis on every PR.
