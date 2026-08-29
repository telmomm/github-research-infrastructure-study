# Phase 4 — GitHub Capability Analysis

**Roadmap step:** 4 of 12 · **Feeds:** RQ3 · **Method doc:** `GITHUB_FEATURE_MAPPING.md`
**Started / completed:** 2026-08-30 · **Status: COMPLETE (v1)**

Catalogues GitHub's native functionalities in terms matchable against the `expected_capabilities` of RM1–RM15. Phase 5 grades the coverage; Phase 4 establishes what the platform offers and with what constraints.

---

## Outputs (`framework/mapping/`)

| File | Content |
|---|---|
| `github_capability_catalogue.csv` | **Canonical.** 68 capabilities (GC01–GC68) across 12 feature groups; per row: what_it_does, research_use, traceability, plan_availability, practical_complexity, limitations, candidate_requirements |
| `GITHUB_CAPABILITY_CATALOGUE.md` | Narrative: scope, plan model, the 12 groups, cross-cutting observations, candidate coverage, handoff |
| `results/framework/gc_*.csv` + `capability_summary.md` | Cross-tabs from `analysis/scripts/summarise_capabilities.py` |

## Catalogue at a glance

- **68 capabilities**, 12 groups: Issues 10 · Repository & Git 9 · Markdown & docs 8 · Projects 7 · Actions 7 · Access & meta 7 · Pull Requests 6 · Discussions 4 · Branches 3 · Releases & tags 3 · Milestones 2 · Labels 2.
- **Plan availability:** 53 / 68 on all plans incl. Free. Paid/org gates: branch-protection enforcement & required reviews on private repos (Team+), Issue Types & org audit log (org plans), private wikis/Pages, custom roles & `internal` visibility (Enterprise), Actions minutes.
- **Practical complexity:** 46 low · 19 medium · 3 high (Actions dominate the high end).
- **Scope:** native only. Excluded: Marketplace/GitHub Apps, Copilot, API-only, Enterprise-server admin. One kept exception: the GitHub–Zenodo release webhook (GC61) as the canonical archiving bridge.

## Cross-cutting observations

1. One manual linkage mechanism (cross-references GC23 + closing keywords GC24 + timeline GC25) underpins all traceability.
2. Records are UI-native but need the API to extract as structured data.
3. Automation (Actions) is capable but gated by engineering expertise and skewed to computational research.
4. Planning (Projects, fields) is separated from artifacts (repo); milestones/labels do not span repositories.

## Candidate coverage (hint for Phase 5, not a score)

Every RM has ≥5 candidate capabilities (RM6 15, RM11 15, RM3 14, RM5 14 … RM2 5, RM12 5). That GitHub has *some* mechanism for every requirement is a Phase-4 result in itself; Phase 5 will show the graded coverage is lower and uneven, especially for the differentiators RM1/RM2/RM5 whose candidates are mostly convention on a generic feature.

## Decisions logged

- `DECISION_LOG.md` D10 — native-only scope, 12-group structure, GC61 exception, candidate-requirement hint vs Phase-5 score.

## Handoff to Phase 5

For each RM × candidate capability: assign Direct 3 / Partial 2 / Limited 1 / Not supported 0 with an evidence note and an implementation pattern → `framework/mapping/requirement_feature_matrix.csv`; roll up to per-requirement / per-category coverage; combine with `lifecycle_requirements_matrix.csv` for the lifecycle-coverage profile.

## Open / optional (do not block Phase 5)

- [ ] Verify plan-availability details against current GitHub docs at write-up time (features move between tiers).
- [ ] Confirm the GC61 Zenodo-bridge framing with a reviewer-facing justification in the manuscript.
