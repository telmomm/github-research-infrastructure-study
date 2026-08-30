# GitHub Capability Catalogue

**Phase 4 deliverable** (roadmap step 4 of 12) · Feeds **RQ3**
**Authoritative artifact:** `github_capability_catalogue.csv` (this directory)
**Method doc:** `docs/GITHUB_FEATURE_MAPPING.md` · **Decisions:** `docs/DECISION_LOG.md` D10

---

## 1. Purpose

A catalogue of GitHub's **native** functionalities, described in terms that can be matched against the `expected_capabilities` of the requirements framework (RM1–RM15). Phase 5 grades how well each requirement is actually covered; Phase 4 only establishes what the platform offers and with what constraints.

## 2. Scope

**In scope — native platform functionality**, organised into 12 feature groups:

| Group | Feature group | Capabilities |
|---|---|---|
| GF1 | Repository & Git | 9 |
| GF2 | Markdown & documentation | 8 |
| GF3 | Issues | 10 |
| GF4 | Projects | 7 |
| GF5 | Milestones | 2 |
| GF6 | Labels | 2 |
| GF7 | Discussions | 4 |
| GF8 | Branches | 3 |
| GF9 | Pull Requests | 6 |
| GF10 | Actions | 7 |
| GF11 | Releases & tags | 3 |
| GF12 | Access, identity & meta | 7 |
| | **Total** | **68** |

**Out of scope:** GitHub Marketplace apps and third-party GitHub Apps; GitHub Copilot; API-only capabilities without a UI surface; Enterprise-server-only administration.

**One deliberate exception — GC61, the GitHub–Zenodo release webhook.** It is a third-party service, not a native GitHub feature, yet it is catalogued. The justification, for a reviewer: (i) it is the *de facto standard* mechanism for archiving a GitHub release and minting a DOI — documented by GitHub, Zenodo and the Software Heritage / FORCE11 software-citation guidance, and used across the research-software community; (ii) it requires **no code and no third-party app installation** — the researcher flips one switch in Zenodo's GitHub settings; (iii) persistent identification and long-term preservation (RM14) are the one requirement GitHub cannot meet even in principle, so omitting the standard bridge would misrepresent what a GitHub-based setup achieves in practice; (iv) it is the explicit connection point to the prior GitHub–Zenodo–ORCID reproducibility workflow this study extends. Every other non-native integration (CI providers, project-management apps, review tools) *is* excluded, because native equivalents exist. GC61 is flagged in the catalogue with `plan_availability = "all plans (external service)"` so it is never counted as native support.

**Plan model.** Each capability records `plan_availability`. 53 of 68 are available on all plans including Free. The notable paid/organisation gates: branch-protection enforcement and required reviews on **private** repos (Team+), Issue Types and the organisation audit log (organisation plans), private wikis and private Pages, custom repository roles and `internal` visibility (Enterprise), Actions minutes beyond the free quota.

## 3. Assessment dimensions

Every catalogue row carries: `what_it_does` (technical function), `research_use` (how it serves research management), `traceability` (what durable record it leaves), `plan_availability`, `practical_complexity` (low / medium / high — 46 low, 19 medium, 3 high), `limitations`, and `candidate_requirements` (a Phase-4 hint at the RM(s) it might support, **not** the Phase-5 score).

## 4. Feature groups

**GF1 Repository & Git.** The substrate. A repository is a single navigable, fully version-controlled workspace (GC01); the commit history gives every artifact an attributable, timestamped change record (GC02), with line-level diff and blame (GC03). Signed commits (GC04) and the co-authored-by trailer (GC05) address authorship; Git LFS (GC06) extends versioning to mid-size data with quota limits; tags (GC07) mark named states. Repository templates (GC08) and org-level health files (GC09) let a group standardise structure across projects — directly relevant to the study's own template output.

**GF2 Markdown & documentation.** READMEs (GC10) put versioned documentation beside the artifacts it describes; GitHub-Flavored Markdown (GC11) turns protocols, methodology and decision logs into diffable prose; inline Mermaid and math (GC12) render workflow and lifecycle diagrams without external tools. Task lists (GC13), the wiki (GC14), GitHub Pages (GC15), `CITATION.cff` (GC16) and commit-pinned permalinks (GC17) round out the documentation surface.

**GF3 Issues.** The workhorse for research activities. An issue (GC18) is a stateful, fully-timelined unit usable as a task, a methodological question, a decision thread or a research-question record. Forms and templates (GC19) and organisation Issue Types (GC20) add structure; sub-issues (GC21) give hierarchy; assignees (GC22) give ownership. The linkage machinery — bidirectional cross-references (GC23), closing keywords (GC24) and the immutable timeline (GC25) — is what lets question → task → commit → PR → release be reconstructed later.

**GF4 Projects.** Projects v2 (GC28) is a table/board/roadmap layer over issues and PRs. Custom fields (GC29) implement exactly the `TEMPLATE_PROJECT.md` scheme (Research phase, Related RQ, Artifact, Priority); saved views (GC30) and the roadmap view (GC31) present the same items to different audiences; built-in workflows (GC32) keep the board current; insights (GC33) expose progress. Draft issues (GC34) capture ideas before they are formalised.

**GF5 Milestones / GF6 Labels.** Milestones (GC35–GC36) group work under named research phases with automatic progress. Labels (GC37–GC38) classify issues and PRs by activity type (literature, methodology, data, analysis, decision, manuscript).

**GF7 Discussions.** A categorised forum (GC39–GC40) for methodological debate and open questions not tied to a task; mark-as-answer (GC41) and polls (GC42) turn a thread into a lightweight, recorded group decision.

**GF8 Branches.** Independent lines of work (GC43) for alternative analyses and parallel manuscript drafts; branch protection / rulesets (GC44) enforce that changes to protected refs go through reviewed PRs (enforcement is paid on private repos); the compare view (GC45) makes divergence explicit.

**GF9 Pull Requests.** A PR (GC46) bundles rationale, diff, approvals and linked issues into one reviewable record. Formal reviews (GC47), required reviews / CODEOWNERS (GC48), suggested changes (GC49), linked issues (GC50) and PR templates (GC51) support internal peer review of analysis code, methodology changes and manuscript sections.

**GF10 Actions.** Event-, schedule- and dispatch-triggered YAML automation (GC52–GC54) for validation, tests, figure regeneration, reproducibility checks and release packaging; artifacts and job summaries (GC55) attach outputs and results to a run; matrix builds (GC56) test across environments; secrets/OIDC (GC57) enable credentialed deposit to external archives; reusable workflows (GC58) standardise automation across a group. This is the highest-complexity group (2 of 3 "high" ratings).

**GF11 Releases & tags.** A release (GC59) is a citable, notes-bearing snapshot tied to a tag and to the work merged since the last release; autogenerated notes (GC60) produce a version-to-version changelog; the Zenodo webhook (GC61) mints a DOI and preserves each release.

**GF12 Access, identity & meta.** Repository roles (GC62), visibility (GC63), forks (GC64), insights (GC65), notifications (GC66), the organisation audit log (GC67) and Dependabot (GC68) cover governance, disclosure control and contribution transparency.

## 5. Cross-cutting observations

1. **One linkage mechanism underpins traceability.** Cross-referencing (GC23) plus closing keywords (GC24) plus the issue/PR timeline (GC25) is the connective tissue for RM10; it is entirely manual and only as complete as contributors' referencing discipline.
2. **Records are UI-native but not export-native.** Timelines, reviews and project fields are durable in the interface but require the API to extract as structured data — relevant to the "auditable record" claim.
3. **Automation is powerful but gated by expertise.** Actions can support reproducibility (RM12) and output management (RM14), but the complexity rating (high) and the computational-research skew are real limits.
4. **The platform separates planning from artifacts.** Projects and their fields live outside the repository; milestones and labels are repo-scoped and do not span repositories. Multi-repository research programmes hit this boundary.

## 6. Candidate coverage (Phase-4 hint only)

Every requirement has at least five candidate capabilities (`results/framework/capability_summary.md`):

| RM | candidates | | RM | candidates |
|---|---|---|---|---|
| RM1 planning | 11 | | RM9 artifact mgmt | 6 |
| RM2 question mgmt | 5 | | RM10 provenance | 11 |
| RM3 task mgmt | 14 | | RM11 transparency | 15 |
| RM4 documentation | 10 | | RM12 reproducibility | 5 |
| RM5 decision traceability | 14 | | RM13 automation | 8 |
| RM6 collaboration | 15 | | RM14 output mgmt | 7 |
| RM7 communication | 7 | | RM15 governance | 13 |
| RM8 version control | 8 | | | |

That GitHub has *some* candidate mechanism for every RM is itself a Phase-4 result. Phase 5 grades each candidate as Direct (3) / Partial (2) / Limited (1) / Not supported (0) with an evidence note, so the coverage figures will be lower and uneven — in particular the differentiator requirements RM1, RM2, RM5, whose candidates (Projects fields, issues-as-questions, decision-log conventions) are mostly *convention on top of a generic feature* rather than purpose-built support.

## 7. Handoff to Phase 5

For each RM × candidate capability, assign a support level and an implementation pattern; roll up to per-requirement and per-category coverage; combine with `framework/requirements/lifecycle_requirements_matrix.csv` for the lifecycle-coverage profile. Output to `framework/mapping/` (`requirement_feature_matrix.csv`, coverage indicators).
