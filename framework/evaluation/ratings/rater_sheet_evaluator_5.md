**Limitation Note**: The search results do not cover all 62 specific capability tests required by the rating sheet. Several results provide only overviews of free plans (user limits, storage quotas, CI minutes) without confirmation of individual feature behaviors. Some scores are marked "?" accordingly. Where scores rely on official documentation or changelogs, citations are provided.

---

# Platform Rating Sheet — Independent Evaluation

**Name:** [To be completed]  
**Date of rating:** 2026-10-09  
**Role and field:** [To be completed]  
**Platforms you use regularly:** [To be completed]  
**Platforms you scored mainly from documentation:** A (GitHub), B (GitLab), C (Bitbucket), D (Bitbucket + Jira + Confluence)  
**Approximate time spent:** [To be completed]

**Context:** Free plan, public project, research group of up to five people, no budget for tools.

---

## RM1: Research planning and roadmap

| Test | A | B | C | D | Notes |
|---|---|---|---|---|---|
| RM1.1 | 3 | 3 | 2 | 3 | **A:** GitHub Milestones natively support named phases with dates; issues/PRs can be attached. **B:** GitLab Milestones native. **C:** Bitbucket Issues has a "milestone" field but it is free text, not structured date association. **D:** Jira Free provides Roadmap functionality . |
| RM1.2 | 2 | 3 | ? | 3 | **A:** Can approximate via Milestone issue completion rate, but no native "objective" record. **B:** GitLab has Epics and Roadmap for tracking objectives. **C:** No native objective object confirmed. **D:** Jira has Epics and Roadmap . |
| RM1.3 | 3 | 3 | 0 | 3 | **A:** Projects Roadmap layout natively displays items on a timeline with start/target dates . **B:** GitLab Roadmap natively displays Epic timeline (available on Free for single-group use ). **C:** No timeline view. **D:** Jira Timeline/Roadmap native . |
| RM1.4 | 3 | 3 | 3 | 3 | Git itself provides complete version history; Jira/Confluence also have version history. |

## RM2: Research question management

| Test | A | B | C | D | Notes |
|---|---|---|---|---|---|
| RM2.1 | 2 | 2 | 2 | 2 | No native "research question" object. Can use Issue (A/B/C) or Jira Issue (D) via label or title convention. |
| RM2.2 | 3 | 3 | 3 | 3 | Issue/Jira issue description edit history is retrievable and comparable. |
| RM2.3 | 3 | 3 | 0 | 3 | **A/B/D:** Issues/PRs and Jira issues support bidirectional linking and references. **C:** Bitbucket Issues lacks native bidirectional linking mechanism (manual URL writing required). |

## RM3: Task management

| Test | A | B | C | D | Notes |
|---|---|---|---|---|---|
| RM3.1 | 3 | 3 | 3 | 3 | Issues/Jira Issues native. |
| RM3.2 | 3 | 3 | 3 | 3 | **A/B/D:** Native open/closed and board column states. **C:** Bitbucket Issues has status fields (new/open/resolved/closed etc.). |
| RM3.3 | 3 | 3 | 3 | 3 | Native assignee field. |
| RM3.4 | 3 | 3 | 2 | 3 | **A:** Native Priority field (in Projects). **B:** Native Priority labels/weight. **C:** No native priority field; must use labels or title convention. **D:** Jira native Priority field. |
| RM3.5 | 3 | 2 | 0 | 3 | **A:** Issue dependencies now generally available on Free plan . Can mark as "blocked by" or "blocking." **B:** No native blocking relationship; requires label or description convention. **C:** Absent. **D:** Jira native "blocks" link type. |
| RM3.6 | 3 | 3 | 0 | 3 | **A:** Projects board layout. **B:** Issue Boards. **C:** No board view. **D:** Jira Board native. |

## RM4: Documentation

| Test | A | B | C | D | Notes |
|---|---|---|---|---|---|
| RM4.1 | 3 | 3 | 3 | 3 | Markdown rendering native. |
| RM4.2 | 2 | 2 | 0 | 3 | **A/B:** No native template object; can use `.github/ISSUE_TEMPLATE` or issue template convention. **C:** Absent. **D:** Confluence native templates . |
| RM4.3 | 3 | 3 | 3 | 3 | Wiki/Confluence page version history native . |
| RM4.4 | 2 | 2 | 0 | 1 | **A/B:** Can use YAML file convention for metadata, but platform does not natively parse. **C:** Absent. **D:** Confluence page properties limited; Jira issue fields structured but not general-purpose metadata. |

## RM5: Decision traceability

| Test | A | B | C | D | Notes |
|---|---|---|---|---|---|
| RM5.1 | 2 | 2 | 0 | 2 | **A/B:** No native decision type; requires issue label convention. **D:** Jira can use issue type convention. |
| RM5.2 | 0 | 0 | 0 | 0 | No native structured rationale/alternatives fields. |
| RM5.3 | 3 | 3 | 3 | 3 | Issue creation/update date native. |
| RM5.4 | 3 | 3 | 3 | 3 | Assignee/participants traceable. |
| RM5.5 | 3 | 3 | 0 | 3 | **A/B/D:** Issue linking native. **C:** No native linking. |

## RM6: Collaboration and contribution tracking

| Test | A | B | C | D | Notes |
|---|---|---|---|---|---|
| RM6.1 | 3 | 2 | 0 | 0 | **A:** Pull Request review native; can require approvals (branch protection on public repos with Free). **B:** GitLab Free allows approvals but they are **optional and do not prevent merging** without approval . **C/D:** Bitbucket Free lacks merge checks (paid feature) . |
| RM6.2 | 3 | 3 | 3 | 3 | Inline comments and suggested changes native. |
| RM6.3 | 3 | 3 | 3 | 3 | Git blame/commit history native. |
| RM6.4 | 3 | 3 | 3 | 3 | Git branching and merging native. |

## RM7: Communication

| Test | A | B | C | D | Notes |
|---|---|---|---|---|---|
| RM7.1 | 3 | 3 | 3 | 3 | Discussions/Issues comments/Jira comments native threading. |
| RM7.2 | 3 | 3 | 2 | 3 | **A/B/D:** Comments can link to issue/PR/Jira issue. **C:** Manual URL writing. |
| RM7.3 | 3 | 3 | 3 | 3 | Comments searchable. |

## RM8: Version control

| Test | A | B | C | D | Notes |
|---|---|---|---|---|---|
| RM8.1 | 3 | 3 | 3 | 3 | Git native. |
| RM8.2 | 3 | 3 | 3 | 3 | Git diff native. |
| RM8.3 | 3 | 3 | 3 | 3 | Git revert/checkout native. |
| RM8.4 | 3 | 3 | 3 | 3 | Git tags native. |
| RM8.5 | 2 | 2 | 2 | 2 | **A:** GitHub Free does not include Git LFS (paid add-on). **B:** GitLab Free includes 10 GiB LFS. **C:** Bitbucket Free includes 1 GB LFS . **D:** Same as C. |

## RM9: Research artifact management and integration

| Test | A | B | C | D | Notes |
|---|---|---|---|---|---|
| RM9.1 | 3 | 3 | 3 | 3 | Repository/project structure reusable. |
| RM9.2 | 2 | 2 | 2 | 2 | No native artifact type; can use label/issue type convention. |
| RM9.3 | 2 | 2 | 2 | 3 | **A/B/C:** Manual URL referencing. **D:** Jira's "remote issue link" or Confluence embedding natively supported. |
| RM9.4 | 2 | 2 | 2 | 3 | **D:** Jira + Confluence + Bitbucket integration provides unified entry point; others rely on README or Wiki index. |

## RM10: Research provenance and artifact linkage

| Test | A | B | C | D | Notes |
|---|---|---|---|---|---|
| RM10.1 | 3 | 3 | 3 | 3 | "Closes #issue" / smart commits native. |
| RM10.2 | 2 | 2 | 2 | 3 | **A/B/C:** Manual tracing required; no native bidirectional query chain. **D:** Jira ↔ Bitbucket ↔ Confluence integration provides cross-tool tracing . |
| RM10.3 | 2 | 2 | 0 | 3 | **A/B:** Can use issue linking convention. **D:** Native cross-stage linking. |
| RM10.4 | 3 | 3 | 3 | 3 | Git blame native. |

## RM11: Transparency

| Test | A | B | C | D | Notes |
|---|---|---|---|---|---|
| RM11.1 | 3 | 3 | 3 | 3 | Public repository/project visible without account. |
| RM11.2 | 3 | 3 | 3 | 3 | Public repository commit history visible. |
| RM11.3 | 3 | 3 | 3 | 3 | Public Wiki/README readable. |
| RM11.4 | 3 | 3 | 3 | 3 | Activity feed / commit log native. |

## RM12: Reproducibility support

| Test | A | B | C | D | Notes |
|---|---|---|---|---|---|
| RM12.1 | 3 | 3 | 2 | 2 | **A/B:** Actions/CI configuration files versionable. **C/D:** Pipelines config storable, but Free minutes severely limited (50 min/month for Bitbucket ). |
| RM12.2 | 3 | 3 | 3 | 3 | Git tags/commits SHA native. |
| RM12.3 | 3 | 3 | 2 | 2 | **A/B:** Actions/CI executable from platform. **C/D:** Pipelines executable but minutes extremely scarce. |
| RM12.4 | 3 | 2 | 0 | 0 | **A:** CI checks can be set as required (branch protection). **B:** GitLab Free approvals are optional, do not block merging . **C/D:** Bitbucket Free lacks merge checks . |

## RM13: Automation

| Test | A | B | C | D | Notes |
|---|---|---|---|---|---|
| RM13.1 | 3 | 3 | 3 | 3 | Actions/CI/Pipelines native; Jira has automation rules (100 runs/month on Free ). |
| RM13.2 | 3 | 3 | 3 | 3 | CI native. |
| RM13.3 | 3 | 3 | 2 | 2 | **A/B:** Scheduled workflows/CI native. **C/D:** Pipelines have schedule, but minute limits prohibitive. |
| RM13.4 | 3 | 3 | 2 | 2 | **A/B:** Actions/CI can build and publish. **C/D:** Pipelines can build, but Free quota extremely low. |

## RM14: Research output management and identification

| Test | A | B | C | D | Notes |
|---|---|---|---|---|---|
| RM14.1 | 3 | 3 | 3 | 3 | Releases native. |
| RM14.2 | 3 | 3 | 3 | 3 | **A:** Can trigger Zenodo integration. **B:** Can trigger Zenodo integration. **C/D:** Manual operation or via Pipelines. |
| RM14.3 | 2 | 2 | 2 | 2 | **A/B:** CITATION.cff can be parsed but not native. **D:** None. |
| RM14.4 | 3 | 3 | 3 | 3 | Release notes can link issues/PRs. |

## RM15: Governance and sustainability

| Test | A | B | C | D | Notes |
|---|---|---|---|---|---|
| RM15.1 | 3 | 3 | 3 | 3 | Role permissions native. |
| RM15.2 | 3 | 3 | 3 | 3 | Ownership transfer native. |
| RM15.3 | 2 | 2 | 2 | 2 | CONTRIBUTING.md convention; platform does not enforce. |
| RM15.4 | 3 | 3 | 3 | 3 | Project archivable/exportable. |

---

## General comments

- **RM8.5 (large files)**: GitHub Free **does not include Git LFS**—a common misconception. GitLab Free includes 10 GiB LFS; Bitbucket Free includes 1 GB .
- **RM6.1/RM12.4 (required approvals/checks)**: Bitbucket Free lacks merge checks, a critical shortfall for C and D in collaboration quality . GitLab Free approvals are optional and do not block merging .
- **RM10.2 (provenance chain query)**: Only configuration D (Bitbucket + Jira + Confluence) provides a native cross-tool provenance chain. This is the only configuration among the four approaching "end-to-end traceability" .
- **GitHub issue dependencies**: Now generally available on Free plan, including API and webhooks support .
- **Bitbucket Free storage**: Repository storage limit of **1 GB total** within the workspace; exceeding the 4 GB repository limit disables pushing .
- **Scoring uncertainty**: RM1.2, RM9.2, RM9.4 scores based on feature inference rather than direct testing. Recommend consulting latest documentation.
- **D configuration caveat**: Bitbucket + Jira + Confluence in Free plan is feasible for 5-person teams (Jira/Confluence Free support up to 10 users ; Bitbucket Free supports up to 5 users ). Integration depth (e.g., automation links) may be limited by Free plan.

---

**Consent to be named in acknowledgments:** No