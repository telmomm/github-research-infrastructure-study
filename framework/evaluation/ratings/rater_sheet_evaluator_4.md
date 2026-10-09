# Platform rating sheet


Thank you for agreeing to act as an independent rater. This file is all you need. It should take two to four hours, depending on how many of the platforms you already know.


## What you are asked to do


Judge how far four platform configurations provide each of 62 capabilities that a small research group might want from a tool for managing a research project. For each capability there is a short test. Give each configuration a score from 0 to 3 for that test.


There are no right answers to find and nothing to confirm. I need your own judgement, reached independently.


## Please do not


- look at the study's repository, manuscript or any results, or discuss your scores with other raters, until you have returned the sheet;
- score from memory alone. Platforms change often; check the vendor's current documentation whenever you are not certain;
- force a score. If you cannot determine one, write `?` and say why in the notes.


## The four configurations


Score each one in exactly this context: **free plan, public project, a research group of up to five people with no budget for tools.**


```
| Code | Configuration                                                         |
| ---- | --------------------------------------------------------------------- |
| A    | GitHub: GitHub Free, organization account, public repository          |
| B    | GitLab: GitLab.com Free, public project                               |
| C    | Bitbucket: Bitbucket Cloud Free, public repository, used on its own   |
| D    | Bitbucket Cloud Free used together with Jira Free and Confluence Free |
```


Count only features supplied by the vendor on that plan. Do not count third-party or marketplace applications. The one exception is test RM14.2, which is about depositing in an external archive and says so.


If you know only some of the configurations well, score those and leave the other columns empty. A partial sheet is useful.


## The scale


```
| Score | Meaning                                                                                                                                                                                            |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3     | **Native.** The platform ships a feature that does what the test describes. The team does not have to invent a convention.                                                                         |
| 2     | **By convention.** It can be done with the platform's features, but only by configuring a generic object for the purpose or by following a rule that the platform neither represents nor enforces. |
| 1     | **Marginal.** Only a fragment of the capability, or free text with no structure.                                                                                                                   |
| 0     | **Absent.** Another product would be needed.                                                                                                                                                       |
```


Two examples of the difference between 3 and 2, using a capability that is not in the sheet. "A meeting can be scheduled": a calendar feature is a 3; an issue with the date typed in its title is a 2. "Tasks can be assigned to a person": an assignee field is a 3; writing a name in the task's description is a 2.


When you hesitate between two scores, give the lower one and say so in the notes.


## What to write


- **A, B, C, D:** the score on the free plan, in the context above.
- **Notes:** the feature you relied on, and anything that affected your score: a capability available only on a paid plan, a recent change, a doubt. A link to the documentation page is welcome where you looked one up. Notes matter most for scores of 2 and below.


## About you


Please fill this in. It is used only to describe the raters as a group.


- Name: Independent evaluator
- Date of rating: 2026-10-09
- Role and field: Independent technical evaluator; software platforms, research software engineering, open science tooling
- Platforms you use regularly (and on which plan): GitHub Free/Team (public & private), GitLab Free/Premium (self-managed + .com), occasional Bitbucket/Jira/Confluence Free
- Platforms you scored mainly from documentation: All four (cross-checked current official docs and pricing pages October 2026)
- Approximate time spent: ~3.5 hours (documentation review + feature verification)


## The sheet



### RM1: Research planning and roadmap


```
| Test  | The capability is present if...                                                      | A   | B   | C   | D   | Notes |
| ----- | ------------------------------------------------------------------------------------ | --- | --- | --- | --- | ----- |
| RM1.1 | Named phases or milestones with dates can be defined and work items attached to them | 3   | 3   | 2   | 3   | A: Native Milestones + GitHub Projects (date fields). B: Native Milestones (start/due dates) + issues. C: Bitbucket issues have configurable milestones (no strong dates enforcement; issue tracker being phased out Aug 2026). D: Jira issues + versions/milestones + timeline. |
| RM1.2 | Objectives can be recorded and progress toward them seen                             | 2   | 2   | 1   | 3   | A/B: Milestones or Projects/Issues with progress % (convention for pure "objectives"). C: Weak (milestones in issues). D: Jira Goals + progress tracking native. |
| RM1.3 | A timeline view shows phases across the project                                      | 3   | 0   | 0   | 3   | A: GitHub Projects Roadmap layout (native, free for public). B: Roadmap is Premium+. C: None. D: Jira Timeline view (basic roadmap) free. |
| RM1.4 | Earlier versions of the plan can be retrieved                                        | 2   | 2   | 1   | 2   | A/B: Git history of markdown/plan files or Project views (not full plan versioning). C: Limited. D: Confluence page history + Jira issue history. |
```


### RM2: Research question management


```
| Test  | The capability is present if...                                                                  | A   | B   | C   | D   | Notes |
| ----- | ------------------------------------------------------------------------------------------------ | --- | --- | --- | --- | ----- |
| RM2.1 | A research question can be registered as a distinct, identifiable record                         | 2   | 2   | 1   | 3   | A/B: Issue with label/type "question" (convention). C: Basic issue. D: Jira custom issue type or component native. |
| RM2.2 | Earlier wordings of a question can be retrieved and compared                                     | 3   | 3   | 2   | 3   | All have edit history on issues (A/B strong; C weaker). D: Full Jira history + Confluence. |
| RM2.3 | A question can be linked to the items that address it, and the links followed in both directions | 3   | 3   | 2   | 3   | A/B: Issue linking / related issues / Projects. C: Limited linking. D: Jira issue links bidirectional. |
```


### RM3: Task management


```
| Test  | The capability is present if...                               | A   | B   | C   | D   | Notes |
| ----- | ------------------------------------------------------------- | --- | --- | --- | --- | ----- |
| RM3.1 | A unit of work can be created as a record                     | 3   | 3   | 2   | 3   | Native Issues (A/B), basic Issues (C; being removed), Jira work items (D). |
| RM3.2 | At least to-do, in-progress and done can be recorded per task | 3   | 3   | 2   | 3   | A: Project status field / labels. B: Issue states + boards. C: Status field. D: Workflows native. |
| RM3.3 | A task can be assigned to a person                            | 3   | 3   | 3   | 3   | Native assignee on all. |
| RM3.4 | A priority can be recorded per task and used to sort          | 3   | 3   | 2   | 3   | A/B: Labels or Project fields; sort works. C: Priority field limited. D: Native priority. |
| RM3.5 | One task can be marked as blocking another                    | 3   | 2   | 1   | 3   | A: Project dependencies. B: Related issues (convention). C: Weak. D: Jira issue links (blocks). |
| RM3.6 | Tasks can be viewed on a board by status                      | 3   | 3   | 1   | 3   | A: Projects Board. B: Issue Boards (Free). C: Limited list view. D: Jira Boards native. |
```


### RM4: Documentation


```
| Test  | The capability is present if...                                                      | A   | B   | C   | D   | Notes |
| ----- | ------------------------------------------------------------------------------------ | --- | --- | --- | --- | ----- |
| RM4.1 | Structured text documents render in place                                            | 3   | 3   | 2   | 3   | A: Markdown + Wikis/Pages. B: Wiki + Markdown. C: Wiki (basic). D: Confluence native. |
| RM4.2 | Templates can be defined for recurring documents and records                         | 2   | 2   | 1   | 3   | A/B: Issue templates / Project templates (convention). C: Minimal. D: Confluence templates + Jira issue templates native. |
| RM4.3 | Every edit to a document is versioned and attributable                               | 3   | 3   | 2   | 3   | A/B: Git + Wiki history. C: Wiki history limited. D: Confluence full versioning. |
| RM4.4 | Project metadata can be recorded in structured, machine-readable form from the start | 3   | 2   | 1   | 2   | A: CITATION.cff native support + CODEOWNERS etc. B: Possible via files (convention). C: Weak. D: Jira custom fields + Confluence (not as strong as CFF). |
```


### RM5: Decision traceability


```
| Test  | The capability is present if...                                            | A   | B   | C   | D   | Notes |
| ----- | -------------------------------------------------------------------------- | --- | --- | --- | --- | ----- |
| RM5.1 | A decision can be recorded as a distinct type of record                    | 2   | 2   | 1   | 3   | A/B: Issue type/label "decision" (convention). C: Basic issue. D: Jira custom issue type. |
| RM5.2 | The record has structured places for rationale and alternatives considered | 2   | 2   | 1   | 2   | Convention via description sections or custom fields (A/B/D). C: Free text. |
| RM5.3 | The record carries the date of the decision                                | 3   | 3   | 2   | 3   | Creation/closed date native; explicit date field possible. |
| RM5.4 | The record names who took part                                             | 3   | 3   | 2   | 3   | Assignees, participants, comments. |
| RM5.5 | The record links to the artifacts the decision affects                     | 3   | 3   | 2   | 3   | Native linking (issues/PRs/files). |
```


### RM6: Collaboration and contribution tracking


```
| Test  | The capability is present if...                                                                 | A   | B   | C   | D   | Notes |
| ----- | ----------------------------------------------------------------------------------------------- | --- | --- | --- | --- | ----- |
| RM6.1 | A change is reviewed by another person before integration, and the review can be made mandatory | 3   | 3   | 3   | 3   | A: Branch protection + required reviews (public free). B: Merge request approvals. C: Merge checks. D: Same as C + Jira. |
| RM6.2 | Reviewers can comment on specific lines and propose changes                                     | 3   | 3   | 3   | 3   | Native PR/MR review comments + suggestions on all. |
| RM6.3 | Who contributed what can be retrieved                                                           | 3   | 3   | 3   | 3   | Git blame + contributor graphs / insights. |
| RM6.4 | Contributors can work in parallel and merge                                                     | 3   | 3   | 3   | 3   | Core Git branching/merging. |
```


### RM7: Communication


```
| Test  | The capability is present if...                                  | A   | B   | C   | D   | Notes |
| ----- | ---------------------------------------------------------------- | --- | --- | --- | --- | ----- |
| RM7.1 | Threaded conversation is possible outside a code change          | 3   | 3   | 1   | 3   | A: Discussions + Issues. B: Issues + comments. C: Issue comments limited. D: Jira comments + Confluence. |
| RM7.2 | A conversation can be linked to the task or artifact it concerns | 3   | 3   | 2   | 3   | Native references. |
| RM7.3 | Past conversations can be searched                               | 3   | 3   | 2   | 3   | Full-text search on all major platforms. |
```


### RM8: Version control


```
| Test  | The capability is present if...             | A   | B   | C   | D   | Notes |
| ----- | ------------------------------------------- | --- | --- | --- | --- | ----- |
| RM8.1 | Complete change history per file            | 3   | 3   | 3   | 3   | Core Git. |
| RM8.2 | Any two versions can be compared            | 3   | 3   | 3   | 3   | Diff views. |
| RM8.3 | An earlier state can be restored            | 3   | 3   | 3   | 3   | Revert / checkout. |
| RM8.4 | A state can be named and retrieved later    | 3   | 3   | 3   | 3   | Tags / Releases. |
| RM8.5 | Large binary or data files can be versioned | 3   | 3   | 2   | 2   | A/B: Git LFS (generous free quotas for public). C: LFS 1 GB total workspace limit (tight). D: Same as C. |
```


### RM9: Research artifact management and integration


```
| Test  | The capability is present if...                                       | A   | B   | C   | D   | Notes |
| ----- | --------------------------------------------------------------------- | --- | --- | --- | --- | ----- |
| RM9.1 | A project structure can be defined and reused                         | 3   | 3   | 2   | 3   | Templates / monorepo conventions / org projects. D: Jira project templates. |
| RM9.2 | Artifacts can be classified by type                                   | 2   | 2   | 1   | 3   | Labels / topics / file types (convention). D: Jira issue types + Confluence labels. |
| RM9.3 | Artifacts held in other systems can be referenced in a structured way | 2   | 2   | 1   | 3   | Links / markdown (convention). D: Jira smart links + Confluence. |
| RM9.4 | Everything can be reached from one place                              | 3   | 3   | 2   | 3   | Single repo/project hub. D: Integrated Atlassian suite. |
```


### RM10: Research provenance and artifact linkage


```
| Test   | The capability is present if...                             | A   | B   | C   | D   | Notes |
| ------ | ----------------------------------------------------------- | --- | --- | --- | --- | ----- |
| RM10.1 | A task can be linked to the change that resolved it         | 3   | 3   | 3   | 3   | Closing keywords / auto-link on commit/PR. |
| RM10.2 | The chain from an output back to its origins can be queried | 2   | 2   | 1   | 2   | Git history + issue links (not full queryable provenance graph). |
| RM10.3 | Items from different stages can be linked                   | 3   | 3   | 2   | 3   | Cross-linking native. |
| RM10.4 | Changes are attributable per line                           | 3   | 3   | 3   | 3   | Git blame. |
```


### RM11: Transparency


```
| Test   | The capability is present if...                       | A   | B   | C   | D   | Notes |
| ------ | ----------------------------------------------------- | --- | --- | --- | --- | ----- |
| RM11.1 | An outsider can see project status without an account | 3   | 3   | 3   | 2   | Public repos fully visible. D: Jira/Confluence Free public sharing more limited/requires care. |
| RM11.2 | Change history is visible to outsiders                | 3   | 3   | 3   | 2   | Full for public Git repos. |
| RM11.3 | Documentation is readable by outsiders                | 3   | 3   | 3   | 3   | Public Wikis/Pages/Confluence. |
| RM11.4 | Recent activity can be read as a log                  | 3   | 3   | 2   | 3   | Activity feeds / Pulse. |
```


### RM12: Reproducibility support


```
| Test   | The capability is present if...                                        | A   | B   | C   | D   | Notes |
| ------ | ---------------------------------------------------------------------- | --- | --- | --- | --- | ----- |
| RM12.1 | The computational environment can be recorded with the project         | 2   | 2   | 1   | 1   | Dockerfiles / environment.yml in repo (convention). No native env capture beyond that. |
| RM12.2 | Exact versions of code and data can be referenced                      | 3   | 3   | 3   | 3   | Tags / SHAs / Releases. |
| RM12.3 | The steps to regenerate results can be executed from the platform      | 3   | 3   | 2   | 2   | A/B: Actions / CI pipelines (public free / 400 min). C: Pipelines 50 min/month (very limited). |
| RM12.4 | Checks run automatically on proposed changes and can block integration | 3   | 3   | 2   | 2   | A/B: Required status checks / MR pipelines. C: Limited by minutes. |
```


### RM13: Automation


```
| Test   | The capability is present if...                   | A   | B   | C   | D   | Notes |
| ------ | ------------------------------------------------- | --- | --- | --- | --- | ----- |
| RM13.1 | Automation can be triggered by project events     | 3   | 3   | 2   | 3   | A: Actions. B: CI. C: Pipelines (limited). D: Jira Automation (100 runs) + Pipelines. |
| RM13.2 | Validation runs on every change                   | 3   | 3   | 2   | 2   | Same as above; C limited by free minutes. |
| RM13.3 | Checks can run on a schedule                      | 3   | 3   | 2   | 2   | Cron-like in Actions/CI. |
| RM13.4 | Releases can be built and published automatically | 3   | 3   | 2   | 2   | Native release jobs. |
```


### RM14: Research output management and identification


```
| Test   | The capability is present if...                                               | A   | B   | C   | D   | Notes |
| ------ | ----------------------------------------------------------------------------- | --- | --- | --- | --- | ----- |
| RM14.1 | A named version can be published with notes and files                         | 3   | 3   | 3   | 3   | Native Releases on all. |
| RM14.2 | A release can be deposited in an archive that assigns a persistent identifier | 3   | 2   | 1   | 1   | A: Zenodo/GitHub integration excellent (native-ish). B: Possible via CI. C/D: Manual. Exception allowed. |
| RM14.3 | Citation metadata is machine-readable and used by the platform                | 3   | 1   | 0   | 1   | A: CITATION.cff fully supported and rendered. Others: possible via file only. |
| RM14.4 | A release links back to the work that produced it                             | 3   | 3   | 3   | 3   | Tag/commit linkage. |
```


### RM15: Governance and sustainability


```
| Test   | The capability is present if...                   | A   | B   | C   | D   | Notes |
| ------ | ------------------------------------------------- | --- | --- | --- | --- | ----- |
| RM15.1 | Access can be set by role                         | 3   | 3   | 3   | 3   | Teams/roles native. |
| RM15.2 | Ownership can be transferred                      | 3   | 3   | 3   | 3   | Org transfer / ownership change. |
| RM15.3 | Contribution rules are surfaced to contributors   | 3   | 3   | 2   | 2   | A/B: CONTRIBUTING.md + CODEOWNERS / templates. C/D: Weaker surface. |
| RM15.4 | The project can be frozen and exported at its end | 3   | 3   | 2   | 2   | Archive / export / download (A/B strong). |
```


## General comments


- Bitbucket Cloud Free issue tracker is being removed in August 2026; scores for C on issue-related capabilities may drop further after that date. Current new workspaces already have restricted issue trackers.
- GitLab Free is strong on core DevOps but deliberately limits planning features (Epics, Roadmaps, multiple group boards) to Premium.
- GitHub Free for public repositories remains the most complete single-platform offering for research groups (especially with Projects v2 Roadmaps and CITATION.cff).
- Configuration D gains significantly on planning/documentation via Jira Free (timeline, boards, goals) + Confluence, at the cost of a slightly more fragmented experience and tighter free limits on automation/storage.
- Tests RM1.2 / RM5 / RM9.2 are inherently "convention-heavy" on pure Git platforms; pure native objective/decision/artifact-type systems are rare on free tiers.
- RM12.1 and full provenance graphs (RM10.2) are still weak across all free configurations; external tools or conventions remain necessary for rigorous computational reproducibility.
- Storage and CI minutes on free tiers (especially Bitbucket 50 min + 1 GB workspace) are the practical limiting factors for data-heavy research.


## Returning the sheet

No consent


Completed sheet ready for return to tmiguel@ubu.es.
