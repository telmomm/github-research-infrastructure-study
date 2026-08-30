# Release checklist (component D1 / D2)

Cut a release at each roadmap point (`v0.1` … `v1.0`). Workflow WF5.

## One-time setup

- [ ] Log in to Zenodo with GitHub and **flip the switch** for this repository (Zenodo → GitHub).
- [ ] `CITATION.cff` has authors + ORCIDs and a `license`.

## Per release

- [ ] `docs/roadmap.md` phase table and RQ summary are current.
- [ ] `docs/decision-log.md` is up to date.
- [ ] `CHANGELOG.md` has an entry for this version (if you keep one).
- [ ] `CITATION.cff`: bump `version` and `date-released`.
- [ ] All CI green on the default branch.
- [ ] Tag `vX.Y` (annotated) and push.
- [ ] Publish a **GitHub Release** from the tag with **auto-generated notes**; attach any output assets.
- [ ] Zenodo mints a DOI — copy it into `CITATION.cff` (`doi:`) and `README.md`, commit.
- [ ] Attach the raw retrieval bundle: build `dist/track_a_raw_exports_<date>.zip` (see `data/README.md`) and add it to the Zenodo record as a supplementary file (Zenodo web UI → Edit → Upload).
- [ ] For `v1.0`: make the repository **public** (governance decision — log it), update visibility note in `docs/project-charter.md`.
- [ ] Link the release from the relevant `outputs/` entry and closing issues.
