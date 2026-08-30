# Requirement–Feature Coverage Analysis

**Phase 5 deliverable** (roadmap step 5 of 12) · Answers **RQ3**
**Artifacts:** `requirement_feature_matrix.csv` (per-requirement assessment), `coverage_group_matrix` (RM × feature group), `results/framework/coverage_*.csv`
**Decisions:** `docs/DECISION_LOG.md` D11

---

## 1. Method

Each requirement RM1–RM15 was assessed for the best support level GitHub's **native** functionality can reach, using the Phase 4 catalogue (`github_capability_catalogue.csv`) and the four-level rubric:

| Level | Score | Meaning |
|---|---|---|
| Direct | 3 | Native functionality meets the requirement |
| Partial | 2 | Met with an additional process or convention on native features |
| Limited | 1 | Marginal support only |
| Not supported | 0 | Cannot reasonably be met by GitHub alone |

Every row of `requirement_feature_matrix.csv` records the level, the primary capabilities (GC ids), the contributing feature groups with weights, a concrete implementation pattern, an evidence note justifying the level, any external tools required, and the residual gap.

## 2. Headline result

| Indicator | Value |
|---|---|
| Overall mean support (0–3), core 14 | **2.43** (≈ 81%) |
| Overall mean support (0–3), full 15 | **2.33** (≈ 78%) |
| Direct | 7 / 15 — RM3, RM4, RM6, RM7, RM8, RM11, RM13 |
| Partial | 6 / 15 — RM1, RM5, RM9, RM10, RM12, RM14 |
| Limited | 2 / 15 — RM2, RM15 |
| Not supported | 0 / 15 |
| Requirements needing a complementary external tool | 5 — RM8, RM9, RM12, RM14, RM15 |

GitHub provides at least Partial support for 13 of 15 requirements and Direct support for 7. No requirement is entirely unsupported, but the support is uneven and, for a third of the framework, rests on convention rather than purpose-built features.

## 3. Where GitHub is strong

Mean support by category:

| Category | Mean | |
|---|---|---|
| Execution (RM3) | 3.00 | Direct |
| Collaboration (RM6, RM7) | 3.00 | Direct |
| Automation (RM13) | 3.00 | Direct |
| Documentation (RM4, RM11, RM12) | 2.67 | |
| Planning (RM1) | 2.00 | Partial |
| Traceability (RM2, RM5, RM8, RM10) | 2.00 | |
| Artifact management (RM9) | 2.00 | Partial |
| Output management (RM14) | 2.00 | Partial |
| Governance (RM15) | 1.00 | Limited |

GitHub is strongest exactly where research work resembles software work: discrete tasks (RM3), branch-and-review collaboration (RM6), structured communication (RM7), version control (RM8), Markdown documentation (RM4), public transparency (RM11) and CI-style automation (RM13). These map onto mature, purpose-built features.

## 4. Where GitHub is weak

The weak points cluster in **research-specific traceability and upstream work**:

- **RM2 Research question management — Limited (1).** No research-question concept. The workable pattern (an issue per question + labels + manual cross-references) is pure convention with poor discoverability and no structured question-to-artifact model.
- **RM5 Decision traceability — Partial (2).** Achievable with a decision-record issue template or a versioned `DECISION_LOG.md` (as this repository does), but GitHub does not distinguish research decisions from ordinary discussion; the level depends entirely on discipline.
- **RM10 Provenance and artifact linkage — Partial (2).** The connective tissue (cross-references, closing keywords, timelines, release notes) exists but is manual, has no lineage query and no PROV/RO-Crate export, and — matching the literature — tends to stop at data and computation.
- **RM1 Planning — Partial (2).** Assembled from a generic Project tool; no research-plan object and weak plan-revision history.
- **RM15 Governance and sustainability — Limited (1).** Access control is handled well; ownership continuity, funding and workforce are not platform matters (and the requirement is already flagged as only partly in scope).

## 5. The differentiator gap is real on the tool side too

The three requirements flagged in Phase 3 as **differentiators** — RM1 planning, RM2 research-question management, RM5 decision traceability, High importance but weak literature attention — have a **mean GitHub support of 1.67**, against **2.50 for all other requirements**. The upstream planning / question / decision layer is under-served both by the literature (RQ1: 3.7% of the corpus touches idea/question) and by the platform.

## 6. Lifecycle-coverage profile

Weighted mean support per lifecycle stage (`coverage_lifecycle_profile.csv`, support × applicability from `lifecycle_requirements_matrix.csv`):

| Stage | Support | Stage | Support |
|---|---|---|---|
| idea | 2.12 | results | 2.35 |
| question | 2.25 | manuscript | 2.42 |
| planning | 2.36 | publication | 2.41 |
| literature | 2.43 | outputs | 2.39 |
| methods | 2.39 | | |
| data | 2.41 | | |
| analysis | 2.43 | | |

The profile is comparatively flat (2.1–2.4) but lowest at **idea (2.12)** and **question (2.25)** and highest at **literature, analysis and manuscript (2.4+)** — the same shape as the RQ1 bibliometric gap. GitHub covers the execution-to-output span well and the earliest, most intellectual phases least.

## 7. External tools required

Five requirements cannot be fully met by GitHub alone:

| RM | External tool | Why |
|---|---|---|
| RM8 | data repository | large datasets exceed LFS quotas and do not diff |
| RM9 | external stores / specialised tools | integration is by reference, not containment |
| RM12 | containerisation; archive | no native environment capture |
| RM14 | Zenodo / repository | GitHub mints no persistent identifier and gives no archival guarantee |
| RM15 | institutional governance | continuity, funding and workforce are outside any platform |

RM14's gap is closed in practice by the standard **GitHub–Zenodo** release integration (GC61), which also connects this framework to the prior GitHub–Zenodo–ORCID reproducibility workflow.

## 8. Feature-group contribution

Which native feature groups carry the framework (sum of RM contribution weights, `coverage_group_matrix.csv`):

| Group | Weight | Group | Weight |
|---|---|---|---|
| GF3 Issues | 19 | GF9 Pull Requests | 7 |
| GF1 Repository & Git | 18 | GF5 Milestones | 5 |
| GF2 Markdown & documentation | 10 | GF7 Discussions | 5 |
| GF4 Projects | 9 | GF8 Branches | 5 |
| GF12 Access & meta | 8 | GF10 Actions | 5 |
| | | GF11 Releases & tags | 5 |
| | | GF6 Labels | 4 |

**Issues and the Git repository together carry most of the framework.** Projects, Actions, Discussions, Branches and Releases each contribute narrowly to a few requirements. A GitHub-based research-management setup is, first and foremost, a disciplined use of issues and version-controlled files.

## 9. Answer to RQ3

GitHub's native functionalities support research project management requirements **substantially but unevenly** (mean 2.33/3; Direct for 7 of 15, at least Partial for 13). Support is **Direct where research work resembles software engineering** — tasks, review, communication, version control, documentation, transparency, automation — and **Partial or Limited for the research-specific traceability of questions, decisions and provenance, and for planning and governance**. Five requirements need complementary external infrastructure. The under-served upstream layer (RM1, RM2, RM5) is exactly the literature gap identified in RQ1.

## 9a. Robustness (added 2026-08-30)

- **RM15 scope (`DECISION_LOG.md` D17).** RM15 (governance and sustainability) is only partly in scope. Headline coverage is reported for the **core 14** (mean 2.43/3) and the full 15 (2.33/3); the qualitative picture is identical either way.
- **Stricter rubric (`DECISION_LOG.md` D18).** Re-scoring with convention-heavy support capped at Limited (RM1, RM5, RM10 → 1) gives `requirement_feature_matrix_strict.csv`: overall mean **2.13** (core-14 2.21), distribution 7 Direct / 3 Partial / 5 Limited / 0 Not supported. The conclusion — Direct where research resembles software work, Limited for upstream research-specific traceability — holds under both rubrics. Run: `coverage_indicators.py --strict`.
- **Plan availability.** Ten plan-gated capabilities were verified against GitHub Docs (2026-08-30, `plan_availability_check.md`); none changes a support level.

## 10. Handoff to Phase 6

The reference architecture organises the **Direct and Partial** capabilities into components, workflows and a lifecycle model, and specifies the **conventions** that lift RM2, RM5, RM10 and RM1 from raw features to research-usable support. Output to `framework/architecture/`.
