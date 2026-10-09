# Platform rating sheet — completed independent assessment

**Assessment date:** 2026-10-09  
**Scope:** Free plans; public project/repository; research group of up to five people; no budget for tools.  
**Method note:** This is a documentation-led independent assessment, not a hands-on audit of four newly created accounts. Scores reflect native vendor functionality available in the stated plans. Where plan-specific behaviour or an exact test interpretation is uncertain, the notes say so and the score is conservative.


## Scale

- **3 — Native:** purpose-built feature does the test.
- **2 — By convention:** achievable with generic features or an unenforced team convention.
- **1 — Marginal:** partial capability or unstructured free text.
- **0 — Absent:** another product/service is needed.
- **? — Undetermined:** evidence insufficient.

## RM1: Research planning and roadmap

| Test | A: GitHub Free (org, public repo) | B: GitLab.com Free (public project) | C: Bitbucket Cloud Free (public repo, standalone) | D: Bitbucket + Jira Free + Confluence Free | Notes |
|---|---:|---:|---:|---:|---|
| RM1.1 Phases/milestones with dates and work items attached | 2 | 3 | 2 | 3 | GitHub Projects can represent milestones and dates, but project phases need configuration; GitLab milestones have dates and can group issues/MRs; Bitbucket alone has no integrated roadmap; Jira issues can be grouped under versions/epics and dated. |
| RM1.2 Objectives recorded and progress seen | 2 | 3 | 1 | 3 | GitHub Projects fields/views support a convention; GitLab milestones/issues expose progress; Bitbucket alone is mostly repository/PR-centric; Jira dashboards, boards and issue fields support progress tracking. |
| RM1.3 Timeline view of phases across project | 2 | 3 | 0 | 3 | GitHub Projects offers configurable roadmap/timeline-style views; GitLab milestone planning provides time-based planning (roadmap/epic capabilities can vary by tier, so score is based on milestones rather than assuming paid-tier epics); Bitbucket alone lacks this; Jira timeline/roadmap view supports dated work. |
| RM1.4 Earlier plan versions retrievable | 2 | 2 | 1 | 2 | Git-backed plans/docs can be versioned on GitHub/GitLab; Bitbucket has Git history but no integrated plan record; Jira issue history captures edits, but not a coherent snapshot/version of the whole plan. |

## RM2: Research question management

| Test | A | B | C | D | Notes |
|---|---:|---:|---:|---:|---|
| RM2.1 Research question as distinct identifiable record | 2 | 2 | 1 | 3 | GitHub/GitLab issues can be used as question records, but question is not a dedicated record type; Bitbucket standalone has limited issue tracking and is not a research-question manager; Jira issues can represent a question, although a dedicated custom issue type may not be available on Free, so this is a conservative 3 for a distinct issue record rather than a specialist research object. |
| RM2.2 Earlier wordings retrieved and compared | 2 | 2 | 1 | 2 | Git history/issue edits provide some history, but comparison is not always convenient or structured; Jira issue history shows changes, though side-by-side comparison of question wording may require manual inspection. |
| RM2.3 Question linked to items addressing it, navigable both ways | 2 | 2 | 1 | 3 | GitHub issue references/projects and GitLab issue links can connect work items; Bitbucket standalone linking is limited; Jira issue links and issue search support bidirectional navigation. |

## RM3: Task management

| Test | A | B | C | D | Notes |
|---|---:|---:|---:|---:|---|
| RM3.1 Work unit created as a record | 3 | 3 | 2 | 3 | GitHub issues, GitLab issues and Jira issues are native records; Bitbucket standalone provides repository issues but is less fully featured. |
| RM3.2 To-do, in-progress and done status per task | 3 | 3 | 2 | 3 | GitHub Projects status fields and GitLab issue boards support workflow status; Bitbucket issues have a simpler workflow; Jira workflow/status fields are native. |
| RM3.3 Task assigned to a person | 3 | 3 | 3 | 3 | All four configurations support assignment, though Bitbucket standalone issue tracking is comparatively basic. |
| RM3.4 Priority recorded per task and used to sort | 2 | 3 | 1 | 3 | GitHub can use project fields/labels but priority is not a universal issue field in the same way; GitLab issues have priority; Bitbucket standalone is limited; Jira has native priority and sorting/filtering. |
| RM3.5 One task marked as blocking another | 2 | 3 | 1 | 3 | GitHub can express dependencies via issue references/projects but semantics may be conventional; GitLab issue links include blocking relationships; Bitbucket standalone lacks a robust dependency model; Jira issue links include “blocks/is blocked by”. |
| RM3.6 Tasks viewed on board by status | 3 | 3 | 1 | 3 | GitHub Projects board, GitLab issue boards and Jira Kanban/Scrum boards are native; Bitbucket standalone does not provide an equivalent integrated task board. |

## RM4: Documentation

| Test | A | B | C | D | Notes |
|---|---:|---:|---:|---:|---|
| RM4.1 Structured text documents render in place | 3 | 3 | 2 | 3 | Markdown renders in GitHub/GitLab and repository README/wiki; Bitbucket supports README/Markdown but not a full documentation workspace; Confluence is a native rich-text documentation tool. |
| RM4.2 Templates for recurring documents and records | 2 | 2 | 1 | 3 | GitHub issue/PR templates are available, but general research document templates are conventions; GitLab description templates are available; Bitbucket has limited templates; Confluence page templates are native and Jira supports issue templates through configuration/features with some limits. |
| RM4.3 Every document edit versioned and attributable | 3 | 3 | 2 | 3 | Git commits provide attributable history for repo documents; Bitbucket likewise versions tracked files but not every external document; Confluence page history records edits and authors. |
| RM4.4 Project metadata recorded in structured, machine-readable form from the start | 2 | 2 | 1 | 2 | Repository metadata/topics and files such as YAML/JSON are possible but require conventions; Jira fields are structured but do not automatically form a research metadata schema; Confluence content is primarily page-oriented. |

## RM5: Decision traceability

| Test | A | B | C | D | Notes |
|---|---:|---:|---:|---:|---|
| RM5.1 Decision recorded as distinct record type | 2 | 2 | 1 | 2 | GitHub/GitLab issues can be labelled as decisions; Bitbucket issues can be repurposed; Jira can use an issue type or issue convention, but a dedicated custom type may depend on plan/configuration. |
| RM5.2 Structured rationale and alternatives fields | 2 | 2 | 1 | 2 | Templates can prompt for these fields but do not create validated structured fields; Jira descriptions/templates remain largely free text unless configured with supported fields. |
| RM5.3 Decision record carries date | 3 | 3 | 2 | 3 | Creation/edit timestamps are native; explicit decision date may still need a field or text in GitHub/GitLab/Bitbucket. |
| RM5.4 Record names participants | 2 | 2 | 1 | 2 | Authors, assignees and comments identify some participants; a complete participant list usually requires a convention or manual field. |
| RM5.5 Decision links to affected artifacts | 2 | 2 | 1 | 3 | References/links can be recorded in issues; Jira issue links and URLs make linked artifacts more navigable. |

## RM6: Collaboration and contribution tracking

| Test | A | B | C | D | Notes |
|---|---:|---:|---:|---:|---|
| RM6.1 Another person reviews before integration and review can be mandatory | 3 | 3 | 2 | 2 | GitHub Free supports branch protection and required pull-request reviews for public repositories in organizations; GitLab merge requests and approval rules have tier-specific restrictions, so conservative score reflects review workflow but not assuming all mandatory approval controls are Free; Bitbucket supports PR reviews, while mandatory merge checks are limited by plan; Jira/Confluence do not replace repository merge controls. |
| RM6.2 Reviewers comment on lines and propose changes | 3 | 3 | 3 | 3 | Pull/merge requests in all three repository platforms support inline review comments and suggested changes or equivalent review discussion. Jira/Confluence add context but do not change the repository review mechanism. |
| RM6.3 Contributions by person retrievable | 3 | 3 | 3 | 3 | Git commit history, PR/MR records and authorship provide contribution evidence. |
| RM6.4 Contributors work in parallel and merge | 3 | 3 | 3 | 3 | Git branches and pull/merge requests are native across all three. |

## RM7: Communication

| Test | A | B | C | D | Notes |
|---|---:|---:|---:|---:|---|
| RM7.1 Threaded conversation outside a code change | 2 | 3 | 2 | 3 | GitHub Discussions may depend on repository configuration and are not a universal general-purpose workspace; GitLab issues/threads provide conversation, though conversations often remain issue-centred; Bitbucket issues/comments are limited; Jira comments and Confluence pages/comments support discussions outside code changes. |
| RM7.2 Conversation linked to task or artifact | 3 | 3 | 2 | 3 | Issues/PRs and URL references link discussion to work; Jira issue links and Confluence links support this. |
| RM7.3 Past conversations searchable | 2 | 3 | 1 | 3 | GitHub search covers issues/discussions/comments to a degree; GitLab has integrated search; Bitbucket standalone search is limited; Jira search/JQL and Confluence search provide stronger retrieval. |

## RM8: Version control

| Test | A | B | C | D | Notes |
|---|---:|---:|---:|---:|---|
| RM8.1 Complete change history per file | 3 | 3 | 3 | 3 | Git history records tracked file changes across all repository configurations. |
| RM8.2 Any two versions compared | 3 | 3 | 3 | 3 | Git diff and web comparison tools are native. |
| RM8.3 Earlier state restored | 3 | 3 | 3 | 3 | Revert/reset/checkout operations are supported by Git; web UIs also support reverting changes in common workflows. |
| RM8.4 State named and retrieved later | 3 | 3 | 3 | 3 | Git tags and commits identify states; releases add named snapshots. |
| RM8.5 Large binary/data files versioned | 2 | 2 | 2 | 2 | Git LFS is available but free storage/usage limits apply; ordinary Git can track binaries but is poor for large evolving datasets. Score 2 means feasible with constraints, not unlimited scientific-data versioning. |

## RM9: Research artifact management and integration

| Test | A | B | C | D | Notes |
|---|---:|---:|---:|---:|---|
| RM9.1 Project structure defined and reused | 2 | 2 | 2 | 3 | Repository templates/forking provide conventions; Jira project templates and Confluence spaces can structure recurring work more directly. |
| RM9.2 Artifacts classified by type | 2 | 2 | 1 | 3 | Labels, folders, file extensions and project fields can classify artifacts; Jira issue types/fields and Confluence page organization provide more structure. |
| RM9.3 Artifacts in other systems referenced structurally | 2 | 2 | 1 | 3 | URLs and references are possible, but structured integration is limited without apps; Jira/Confluence links and issue links are native within the suite. |
| RM9.4 Everything reachable from one place | 2 | 2 | 1 | 3 | Repository pages/project boards can act as an index but do not aggregate all systems automatically; Bitbucket/Jira/Confluence links and project pages create a stronger integrated hub, though the free products still have access restrictions. |

## RM10: Research provenance and artifact linkage

| Test | A | B | C | D | Notes |
|---|---:|---:|---:|---:|---|
| RM10.1 Task linked to change that resolved it | 3 | 3 | 2 | 3 | GitHub closing keywords and issue/PR references; GitLab issue/MR links; Bitbucket commit/PR references; Jira can link issues to branches/commits/PRs through supported Bitbucket integration. |
| RM10.2 Chain from output back to origins can be queried | 2 | 2 | 1 | 2 | Commit history, issue links and manifests can reconstruct parts of a chain, but none is a full research-provenance graph natively; Jira integrations add links but do not guarantee data/output lineage. |
| RM10.3 Items from different stages can be linked | 2 | 2 | 1 | 3 | Cross-references are possible; Jira issue links and Confluence links provide more explicit navigation across planning and documentation. |
| RM10.4 Changes attributable per line | 3 | 3 | 3 | 3 | Git blame/annotate and commit history are native in each repository platform. |

## RM11: Transparency

| Test | A | B | C | D | Notes |
|---|---:|---:|---:|---:|---|
| RM11.1 Outsider sees project status without an account | 3 | 3 | 3 | 1 | Public GitHub/GitLab/Bitbucket repository content is visible without an account; Jira/Confluence Free does not provide anonymous access to project tracking/docs, although the Bitbucket repository itself remains public. |
| RM11.2 Change history visible to outsiders | 3 | 3 | 3 | 1 | Public Git history is visible; Jira/Confluence histories are not anonymously visible on Free. |
| RM11.3 Documentation readable by outsiders | 3 | 3 | 3 | 1 | README/wiki docs in public repositories are public; Confluence Free does not include anonymous access, so suite documentation is not public by default. |
| RM11.4 Recent activity readable as a log | 3 | 3 | 2 | 2 | Git commit/issue/MR activity is visible in public repositories; Bitbucket has commit/PR activity but less unified project activity; Jira has activity streams for signed-in users, not anonymous viewers on Free. |

## RM12: Reproducibility support

| Test | A | B | C | D | Notes |
|---|---:|---:|---:|---:|---|
| RM12.1 Computational environment recorded with project | 2 | 2 | 2 | 2 | Files such as `environment.yml`, `requirements.txt`, Dockerfiles or lockfiles can be committed, but the platforms do not infer/validate a complete environment automatically. |
| RM12.2 Exact versions of code and data referenced | 3 | 3 | 3 | 3 | Commits/tags/releases identify code versions; data versions require the data itself or a stable external identifier and manifest. |
| RM12.3 Steps to regenerate results executable from platform | 2 | 3 | 2 | 2 | GitHub Actions, GitLab CI/CD and Bitbucket Pipelines can run scripts, subject to quotas; GitLab CI/CD is particularly integrated with project pipelines. Jira/Confluence do not themselves execute research workflows. |
| RM12.4 Checks run automatically on proposed changes and can block integration | 3 | 3 | 2 | 2 | GitHub branch protection can require status checks in public org repos; GitLab CI and merge-request checks are available but some approval/merge controls are tier-sensitive; Bitbucket Pipelines runs checks but mandatory merge checks are limited on Free; Jira/Confluence do not add repository enforcement. |

## RM13: Automation

| Test | A | B | C | D | Notes |
|---|---:|---:|---:|---:|---|
| RM13.1 Automation triggered by project events | 3 | 3 | 3 | 3 | GitHub Actions, GitLab CI/CD and Bitbucket Pipelines support event-triggered workflows; Jira automation is included on Free with usage limits. |
| RM13.2 Validation runs on every change | 3 | 3 | 3 | 2 | CI workflows can be configured on pushes/PRs/MRs; execution is configurable and limited by free quotas. Jira automation can react to events but is not a substitute for code validation. |
| RM13.3 Checks run on a schedule | 3 | 3 | 2 | 2 | GitHub Actions and GitLab CI support scheduled workflows/pipelines; Bitbucket Pipelines supports scheduled pipelines with plan limits; Jira scheduled automation is possible but capped. |
| RM13.4 Releases built and published automatically | 3 | 3 | 2 | 2 | GitHub Actions and GitLab CI/CD can build/publish releases; Bitbucket Pipelines can build and deploy, but release management is less integrated; Jira/Confluence do not publish software releases by themselves. |

## RM14: Research output management and identification

| Test | A | B | C | D | Notes |
|---|---:|---:|---:|---:|---|
| RM14.1 Named version published with notes and files | 3 | 3 | 2 | 2 | GitHub Releases and GitLab Releases are native; Bitbucket has downloads/tags but not the same integrated release object; Jira/Confluence do not replace repository release features. |
| RM14.2 Release deposited in archive that assigns persistent identifier | 3 | 2 | 1 | 1 | Exception permits an external archive. GitHub has a documented Zenodo integration that archives releases and assigns a DOI; GitLab/Bitbucket can be deposited manually, but the platform does not provide the same native Zenodo release integration. |
| RM14.3 Machine-readable citation metadata used by platform | 3 | 2 | 1 | 1 | GitHub recognises `CITATION.cff` for a citation suggestion and Zenodo can use it for release metadata; GitLab/Bitbucket can store citation files, but their platforms do not provide the same integrated citation UI/metadata workflow. |
| RM14.4 Release links back to work that produced it | 3 | 3 | 2 | 2 | GitHub/GitLab release pages link to tags and repository history; Bitbucket tags/downloads can be linked manually; Jira/Confluence can link records but do not create software-release provenance automatically. |

## RM15: Governance and sustainability

| Test | A | B | C | D | Notes |
|---|---:|---:|---:|---:|---|
| RM15.1 Access set by role | 3 | 3 | 3 | 2 | GitHub organizations, GitLab projects and Bitbucket workspaces/repositories have roles/permissions; Jira/Confluence Free has simplified permission controls and no anonymous access, so the suite's role granularity is more limited. |
| RM15.2 Ownership transferred | 3 | 3 | 3 | 2 | Repository/workspace or project transfer is supported, subject to account/admin conditions; Jira/Confluence project and site ownership is less directly comparable and may require administrative changes. |
| RM15.3 Contribution rules surfaced to contributors | 3 | 3 | 2 | 2 | GitHub `CONTRIBUTING.md` and contribution guidance can be surfaced in contribution workflows; GitLab supports contribution templates/guidance; Bitbucket can store guidance but has less built-in surfacing; Confluence/Jira pages can document rules but rely on contributors finding them. |
| RM15.4 Project frozen and exported at end | 2 | 2 | 2 | 2 | Repositories can be made read-only/archived and cloned/exported; issues, wiki and platform metadata may not all export as one complete portable package. Jira/Confluence export exists but is not a seamless full-suite archival snapshot on Free. |

## General comments

1. **The test suite mixes repository hosting, project management and knowledge management.** GitHub and GitLab provide more of the workflow in one developer platform; Bitbucket on its own is much narrower. Configuration D is strongest for task planning and documentation, but it is not fully public to outsiders on Free because Jira/Confluence Free do not provide anonymous access.
2. **“Native” is interpreted narrowly.** A generic issue, label or Markdown file is generally scored 2 when it can represent a capability but the platform does not model or enforce the specific research concept. This particularly affects research questions, decisions, objectives, provenance and project metadata.
3. **Free-tier limits matter.** CI/CD minutes, Git LFS storage, automation quotas, anonymous access, merge checks and some advanced roadmap/approval controls are not unlimited and can vary by plan or product changes.
4. **RM14.2 is scored separately from ordinary platform-native features** because the sheet explicitly allows an external archive. GitHub's documented Zenodo integration is a materially more direct route than a manual deposit from the other platforms.
5. Some scores could reasonably differ by one point depending on whether the test accepts a generic issue or a Markdown convention as sufficient. The most interpretation-sensitive tests are RM1.3, RM2.1–RM2.3, RM5.1–RM5.5, RM9.4, RM10.2 and RM14.2–RM14.3.

## About the rater

- **Name:** Telmo Miguel-Medina
- **Date of rating:** 2026-10-09
- **Role and field:** Doctoral researcher and university lecturer; biomedical engineering/eHealth and applied machine learning.
- **Platforms used regularly (and plan):** GitHub — Free (regular use inferred from my research/software workflow; please correct if inaccurate). Regular use of GitLab/Bitbucket/Jira/Confluence was not established for this assessment.
- **Platforms scored mainly from documentation:** GitLab.com Free, Bitbucket Cloud Free, Jira Free and Confluence Free; plan-specific GitHub details were also checked against documentation.
- **Approximate time spent:** Documentation-led desk assessment; estimated 2–4 hours, not a timed hands-on test.
- **Acknowledgment consent:** Not specified — confirm before returning the sheet. Suggested name format if consent is given: Telmo Miguel-Medina.

## Documentation consulted

- GitHub Docs, *About protected branches*: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- GitHub Docs, *Repository roles for an organization*: https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization
- GitLab Docs, *Milestones*: https://docs.gitlab.com/user/project/milestones/
- GitLab Docs, *Compute minutes*: https://docs.gitlab.com/ci/pipelines/compute_minutes/
- Atlassian Support, *Manage your plan and billing (Bitbucket Cloud)*: https://support.atlassian.com/bitbucket-cloud/docs/manage-your-plan-and-billing/
- Atlassian Support, *Limitations of Bitbucket Pipelines*: https://support.atlassian.com/bitbucket-cloud/docs/limitations-of-bitbucket-pipelines/
- Atlassian, *Jira editions*: https://www.atlassian.com/es/software/jira/guides/more/jira-editions
- Atlassian, *Cloud licensing*: https://www.atlassian.com/licensing/cloud
- Atlassian Support, *Confluence permissions*: https://support.atlassian.com/confluence-cloud/docs/what-are-confluence-cloud-permissions-and-restrictions/
- Zenodo Help, *GitHub and Software*: https://help.zenodo.org/docs/github/
- Zenodo Help, *CITATION.cff file*: https://help.zenodo.org/docs/github/describe-software/citation-file/
