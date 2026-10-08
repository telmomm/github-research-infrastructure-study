# Verification log

Checked against vendor documentation on 2026-10-08.

| Ref | Fact | Source |
|---|---|---|
| V1 | Bitbucket Cloud native Issues and Wikis were removed in August 2026 (no new activation from April 2026; removed from UI and API by 20 August 2026). Atlassian recommends Jira and Confluence | https://community.atlassian.com/forums/discussion/3193882/announcing-sunset-of-bitbucket-issues-and-wikis |
| V2 | GitLab epics: Premium, Ultimate | https://docs.gitlab.com/user/group/epics/ |
| V3 | GitLab roadmaps: Premium, Ultimate | https://docs.gitlab.com/user/group/roadmap/ |
| V4 | GitLab linked items: 'relates to' on Free; 'blocks' and 'is blocked by' on Premium, Ultimate | https://docs.gitlab.com/user/project/issues/related_issues/ |
| V5 | GitLab merge request approvals: optional on Free ("don't prevent merging without approval"); required approvals on Premium, Ultimate | https://docs.gitlab.com/user/project/merge_requests/approvals/ |
| V6 | GitLab requirements management: Ultimate | https://docs.gitlab.com/user/project/requirements/ |
| V7 | GitLab issue boards: multiple project boards on Free; scoped boards, assignee, milestone and iteration lists on Premium | https://docs.gitlab.com/user/project/issue_board/ |
| V8 | GitLab code owners: Premium, Ultimate | https://docs.gitlab.com/user/project/codeowners/ |
| V9 | GitLab iterations: Premium, Ultimate | https://docs.gitlab.com/user/group/iterations/ |
| V10 | GitLab health status: Ultimate | https://docs.gitlab.com/user/project/issues/managing_issues/ |
| V11 | GitLab description change history with "Compare with previous version": Premium, Ultimate | https://docs.gitlab.com/user/discussions/ |
| V12 | GitLab configurable work item status: Premium, Ultimate (generally available in 18.4); Free keeps open/closed | https://docs.gitlab.com/user/work_items/status/ |
| V13 | GitLab.com Free: 400 compute minutes per month, 10 GiB storage including LFS, Pages | https://about.gitlab.com/pricing/feature-comparison/ |
| V14 | GitHub issue dependencies (blocked by, blocking): generally available 21 August 2025, on Free | https://github.blog/changelog/2025-08-21-dependencies-on-issues/ |
| V15 | GitHub sub-issues: up to 100 per parent, eight levels | https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues |
| V16 | GitHub Free: full feature set for public repositories; Actions free on standard runners in public repositories; Pages in public repositories. Protected branches, required reviewers and code owners need Team only for private repositories | https://docs.github.com/en/get-started/learning-about-github/githubs-plans |
| V17 | GitHub Free: Git LFS 10 GiB storage and 10 GiB bandwidth | https://docs.github.com/billing/managing-billing-for-git-large-file-storage/about-billing-for-git-large-file-storage |
| V18 | GitHub issue types (up to 25 per organization) and issue fields (generally available 2 July 2026 for all organizations including Free) | https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/managing-issue-types-in-an-organization ; https://github.blog/changelog/2026-07-02-issue-fields-are-now-generally-available/ |
| V19 | GitHub reads CITATION.cff on the default branch and shows "Cite this repository" | https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files |
| V20 | Bitbucket merge checks: recommended checks on all plans; preventing a merge needs Premium | https://support.atlassian.com/bitbucket-cloud/docs/suggest-or-require-checks-before-a-merge/ |
| V21 | Bitbucket Free: up to 5 users, 50 build minutes per month, 1 GB LFS, unlimited public and private repositories | https://www.atlassian.com/software/bitbucket/pricing |
| V22 | Bitbucket self-hosted runners do not consume build minutes; runner pricing changed in 2026 (v5), with sources disagreeing on the free allowance | https://support.atlassian.com/bitbucket-cloud/docs/runners/ ; https://www.atlassian.com/blog/bitbucket/announcing-v5-self-hosted-runners |
| V23 | Bitbucket Cloud has no archive (read-only) state for repositories; the feature exists only in Data Center | https://jira.atlassian.com/browse/SRCTREEWIN-14608 |
| V24 | Jira Free: permissions and roles are not configurable and projects cannot be made public | https://support.atlassian.com/jira-cloud-administration/docs/what-is-the-free-jira-cloud-plan/ |
| V25 | Confluence Decisions blueprint creates a decision log for the space; DACI template has status, driver, approver, contributors, informed, due date, outcome | https://confluence.atlassian.com/doc/decisions-blueprint-339739406.html ; https://www.atlassian.com/software/confluence/templates/decision |
| V26 | Zenodo integrates natively with GitHub only. GitLab has open feature requests; workarounds are manual deposit, a CI job or the third-party gitlab2zenodo | https://gitlab.com/gitlab-org/gitlab/-/issues/25587 ; https://pypi.org/project/gitlab2zenodo/ |
| V27 | No GitLab documentation of CITATION.cff support was found (negative result of two searches, not proof of absence) | https://gitlab.com/gitlab-org/gitlab/-/issues/18763 |
| V28 | JOSS: repository may be on any host where anyone can browse the code and open issues without approval or payment; OSI licence; review runs in GitHub issues (openjournals/joss-reviews); archive with a DOI (Zenodo, figshare) after acceptance | https://joss.readthedocs.io/en/latest/submitting.html |

## Not verified, to check before submission

- Whether Jira Free includes the timeline view and custom issue link types (scored 3 for RM1.3 and RM2.3 from knowledge).
- GitHub issue fields: which field types exist and whether a default priority field ships (RM3.4).
- GitLab: "Pipelines must succeed" on Free (RM12.4); CONTRIBUTING surfaced in the project page (RM15.3).
- Bitbucket: free allowance for self-hosted runners after the v5 pricing change (V22).
- All cells marked "documented knowledge" in `scores.csv`.
