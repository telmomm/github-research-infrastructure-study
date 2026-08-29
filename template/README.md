# template/

The reusable **GitHub Research Project Template** — Phase 7 output, operationalising the
Phase 6 reference architecture (`framework/architecture/`).

| Path | Contents |
|---|---|
| `github-research-project-template/` | The template repository content (33 files): repo skeleton, `docs/` set with the four conventions, issue forms, PR template, label set, Project field definitions, starter Actions, release checklist |
| `template_manifest.csv` | Every template file → architecture component(s) → requirement(s) served → purpose |

## Two-repository strategy

This directory holds the template *inside the study repo* for development and evaluation.
At release (roadmap Phase 12) `github-research-project-template/` is extracted as an
**independent repository** and marked as a GitHub template, so users get a clean project
without the study's data and analysis. See `docs/REPOSITORY_ARCHITECTURE.md`.

## Coverage

`template_manifest.csv` maps files to the 15 architecture components. Verify with:

```
python3 analysis/scripts/check_template.py
```

Every architecture component with a file-expressible basis (A1–A4 docs/config, B1–B2,
B3 via CONTRIBUTING + PR template, C1, C2, C3, D1, D3) has at least one template file.
D2 (Zenodo) and the Project itself (A1/A2) are configuration steps, documented in
`.github/release-checklist.md` and `.github/project-fields.md`.
