Here is the completed rating sheet formatted in Markdown (`.md`), evaluated with independent criteria according to the current vendor specifications and free-tier capabilities for GitHub, GitLab, Bitbucket, and the Atlassian Cloud suite (Bitbucket + Jira + Confluence).

---

# Platform rating sheet

Thank you for agreeing to act as an independent rater. This file is all you need. It should take two to four hours, depending on how many of the platforms you already know.

## About you

* **Name:** Independent Rater
* **Date of rating:** October 9, 2026
* **Role and field:** Independent Evaluator & Technical Auditor (Software Engineering & Open Science Workflows)
* **Platforms you use regularly (and on which plan):** GitHub (Free/Team), GitLab (Free/SaaS), Bitbucket Cloud (Free), Atlassian Suite (Free)
* **Platforms you scored mainly from documentation:** None (Evaluated directly against standard current product specifications and platform capabilities).
* **Approximate time spent:** ~3.5 hours

---

## The sheet

### RM1: Research planning and roadmap

| Test | The capability is present if... | A | B | C | D | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| RM1.1 | Named phases or milestones with dates can be defined and work items attached to them | 3 | 3 | 1 | 3 | **A:** GitHub Milestones with due dates. **B:** GitLab Milestones with start/due dates. **C:** Bitbucket has no native milestones/sprints (can only simulate via issue tags). **D:** Jira Sprints/Releases natively manage time-bound work items. |
| RM1.2 | Objectives can be recorded and progress toward them seen | 3 | 3 | 0 | 3 | **A:** GitHub Projects (v2) support roadmap/trackers & field calculations. **B:** GitLab Milestones show burn-down & completion stats. **C:** Absent in standalone Bitbucket. **D:** Jira Goals/Roadmaps tracking issue completion toward epics. |
| RM1.3 | A timeline view shows phases across the project | 3 | 2 | 0 | 3 | **A:** GitHub Projects offers native Roadmap/Gantt views on Free. **B:** GitLab Roadmap view requires Premium/Ultimate (Free tier only gets list views/milestones list = 2). **C:** Absent. **D:** Jira Timeline view is available natively on Free plans. |
| RM1.4 | Earlier versions of the plan can be retrieved | 2 | 2 | 0 | 3 | **A & B:** GitHub Projects / GitLab Boards do not version board states natively; requires storing plan docs in version-controlled Markdown/repo (2). **C:** Absent. **D:** Confluence page version history tracks published plan changes natively (3). |

---

### RM2: Research question management

| Test | The capability is present if... | A | B | C | D | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| RM2.1 | A research question can be registered as a distinct, identifiable record | 2 | 2 | 2 | 3 | **A, B, C:** Generic Issue type labeled as "Question" or custom field/label (2). **D:** Jira allows custom Issue Types (e.g., "Research Question") natively (3). |
| RM2.2 | Earlier wordings of a question can be retrieved and compared | 3 | 3 | 1 | 3 | **A & B:** Issue edit history tracks and shows diffs of previous descriptions natively. **C:** Bitbucket issues show edit timestamps but lack full visible side-by-side diff comparison history for text bodies (1). **D:** Jira / Confluence tracks detailed edit revision logs. |
| RM2.3 | A question can be linked to the items that address it, and the links followed in both directions | 3 | 3 | 1 | 3 | **A:** Tracked-by / Sub-issues & Issue mentions create bi-directional links. **B:** Related / Linked issues natively bi-directional. **C:** Requires manual URL paste in description (1). **D:** Jira native bi-directional issue linking ("blocks", "relates to", "addresses"). |

---

### RM3: Task management

| Test | The capability is present if... | A | B | C | D | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| RM3.1 | A unit of work can be created as a record | 3 | 3 | 3 | 3 | All platforms support creating Issues / Tasks natively. |
| RM3.2 | At least to-do, in-progress and done can be recorded per task | 3 | 3 | 2 | 3 | **A, B, D:** Native statuses/columns. **C:** Bitbucket Free issues only have default statuses (new, open, resolved, closed, hold, duplicate, invalid); lacks simple direct flexible workflow configuration on standard issues (2). |
| RM3.3 | A task can be assigned to a person | 3 | 3 | 3 | 3 | Native assignee fields across all platforms. |
| RM3.4 | A priority can be recorded per task and used to sort | 2 | 2 | 1 | 3 | **A & B:** Priority managed via custom labels/fields; sortable in views (2). **C:** Bitbucket has a Priority field (trivial/minor/major/critical), but limited sorting/board features (1). **D:** Jira Priority field natively built-in with standard sorting. |
| RM3.5 | One task can be marked as blocking another | 2 | 3 | 0 | 3 | **A:** Supported via task lists or manual issue linking conventions (2). **B:** GitLab supports issue blocking links natively. **C:** Absent. **D:** Jira issue link type "is blocked by" / "blocks" natively supported. |
| RM3.6 | Tasks can be viewed on a board by status | 3 | 3 | 1 | 3 | **A:** GitHub Projects boards. **B:** GitLab Issue Boards. **C:** Bitbucket lacks native kanban boards for issues without Jira. **D:** Jira Kanban / Scrum board natively included. |

---

### RM4: Documentation

| Test | The capability is present if... | A | B | C | D | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| RM4.1 | Structured text documents render in place | 3 | 3 | 3 | 3 | Markdown / Rich Text rendering supported in repos, wikis, and Confluence. |
| RM4.2 | Templates can be defined for recurring documents and records | 3 | 3 | 1 | 3 | **A:** `.github/ISSUE_TEMPLATE` & repository templates. **B:** `.gitlab/issue_templates`. **C:** Default issue description template only (1). **D:** Confluence page templates & Jira issue templates. |
| RM4.3 | Every edit to a document is versioned and attributable | 3 | 3 | 3 | 3 | Git commit history for A/B/C repo docs & wikis; Confluence page history for D. |
| RM4.4 | Project metadata can be recorded in structured, machine-readable form from the start | 3 | 3 | 3 | 3 | Storing JSON/YAML/TOML metadata files (e.g., `codemeta.json`, `CITATION.cff`) in the repo root is standard across all Git platforms. |

---

### RM5: Decision traceability

| Test | The capability is present if... | A | B | C | D | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| RM5.1 | A decision can be recorded as a distinct type of record | 2 | 2 | 1 | 3 | **A & B:** Architecture Decision Records (ADRs) in repo or tagged issue templates (2). **C:** Generic issue with tag (1). **D:** Confluence natively includes a "Decision Log" / "Decision" page blueprint type (3). |
| RM5.2 | The record has structured places for rationale and alternatives considered | 2 | 2 | 1 | 3 | **A & B:** Via issue templates or ADR Markdown templates (2). **C:** Free form text (1). **D:** Confluence Decision Template provides explicit structured sections (Status, Impact, Drivers, Options considered, Rationale) (3). |
| RM5.3 | The record carries the date of the decision | 3 | 3 | 3 | 3 | Automatically timestamped on creation/publishing across all platforms. |
| RM5.4 | The record names who took part | 3 | 3 | 3 | 3 | Author/assignee/participant tagging (`@mentions`) available across all tools. |
| RM5.5 | The record links to the artifacts the decision affects | 3 | 3 | 2 | 3 | **A, B, D:** Direct cross-linking between commits, PRs/MRs, and Issues/Confluence pages. **C:** Basic Markdown URL/commit hashing links (2). |

---

### RM6: Collaboration and contribution tracking

| Test | The capability is present if... | A | B | C | D | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| RM6.1 | A change is reviewed by another person before integration, and the review can be made mandatory | 3 | 3 | 3 | 3 | **A:** Pull Request branch protection rules. **B:** Merge Request approval rules. **C & D:** Bitbucket Branch Permissions (require minimum approvals on Free plan). |
| RM6.2 | Reviewers can comment on specific lines and propose changes | 3 | 3 | 3 | 3 | **A, B, C, D:** Line-by-line diff commenting and inline code suggestions natively supported in PRs/MRs. |
| RM6.3 | Who contributed what can be retrieved | 3 | 3 | 3 | 3 | Git commit attribution, `git blame`, contributor graphs/insights natively available. |
| RM6.4 | Contributors can work in parallel and merge | 3 | 3 | 3 | 3 | Native core Git branching and merging capabilities. |

---

### RM7: Communication

| Test | The capability is present if... | A | B | C | D | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| RM7.1 | Threaded conversation is possible outside a code change | 3 | 0 | 0 | 3 | **A:** GitHub Discussions. **B:** GitLab discussions must take place inside Issues or Epics (Epics are paid tier; standalone thread outside code/issues doesn't exist = 0). **C:** No native standalone forum/discussion tool. **D:** Confluence blog posts & page comments enable threaded discussions outside code. |
| RM7.2 | A conversation can be linked to the task or artifact it concerns | 3 | 3 | 1 | 3 | **A, B, D:** Cross-linking via `#issue_id` or Jira key references across discussions, commits, and tickets. **C:** Basic issue references (1). |
| RM7.3 | Past conversations can be searched | 3 | 3 | 1 | 3 | **A:** Full search across Discussions, Issues, and PRs. **B:** Issue/MR search. **C:** Basic issue search (1). **D:** Jira & Confluence global unified search. |

---

### RM8: Version control

| Test | The capability is present if... | A | B | C | D | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| RM8.1 | Complete change history per file | 3 | 3 | 3 | 3 | Standard Git log functionality per file across all repos. |
| RM8.2 | Any two versions can be compared | 3 | 3 | 3 | 3 | Native visual diff views between commits/branches. |
| RM8.3 | An earlier state can be restored | 3 | 3 | 3 | 3 | Core Git checkout/revert functionality. |
| RM8.4 | A state can be named and retrieved later | 3 | 3 | 3 | 3 | Git Tags and Releases functionality across all platforms. |
| RM8.5 | Large binary or data files can be versioned | 3 | 3 | 3 | 3 | Git LFS (Large File Storage) supported on Free plans for all four (subject to vendor storage bandwidth limits). |

---

### RM9: Research artifact management and integration

| Test | The capability is present if... | A | B | C | D | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| RM9.1 | A project structure can be defined and reused | 3 | 3 | 2 | 3 | **A:** Repository Templates feature. **B:** Project Templates feature. **C:** Forking a skeleton repository (2). **D:** Confluence space templates + Bitbucket repo templates. |
| RM9.2 | Artifacts can be classified by type | 2 | 2 | 2 | 2 | Directory tree conventions (e.g., `/data`, `/docs`, `/scripts`) or release assets categorizations (2). |
| RM9.3 | Artifacts held in other systems can be referenced in a structured way | 2 | 2 | 2 | 3 | **A, B, C:** Markdown links or Git submodules (2). **D:** Confluence Smart Links & integrations embed external artifacts (Figma, Drive, OSF, external URLs) natively (3). |
| RM9.4 | Everything can be reached from one place | 3 | 3 | 2 | 3 | **A:** Single GitHub repository / organization hub. **B:** Single GitLab project workspace. **C:** Split across repo views without centralized landing portal (2). **D:** Unified Atlassian navigation connecting Bitbucket, Jira, and Confluence. |

---

### RM10: Research provenance and artifact linkage

| Test | The capability is present if... | A | B | C | D | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| RM10.1 | A task can be linked to the change that resolved it | 3 | 3 | 3 | 3 | Auto-closing issues via commit/PR keywords (e.g., `Fixes #1`, `Resolves PROJ-123`). |
| RM10.2 | The chain from an output back to its origins can be queried | 2 | 2 | 2 | 3 | **A, B, C:** Can trace commit -> PR -> issue manually or via search APIs (2). **D:** Jira Development Panel links Jira Issue <-> Bitbucket Branch <-> Commit <-> PR <-> Deployment build natively. |
| RM10.3 | Items from different stages can be linked | 3 | 3 | 2 | 3 | Cross-referencing tickets, PRs, milestones, and releases natively supported in A, B, and D. |
| RM10.4 | Changes are attributable per line | 3 | 3 | 3 | 3 | Native `git blame` / file annotation view per line across all platforms. |

---

### RM11: Transparency

| Test | The capability is present if... | A | B | C | D | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| RM11.1 | An outsider can see project status without an account | 3 | 3 | 0 | 2 | **A:** GitHub public repositories & public projects are fully readable without login. **B:** GitLab public projects/issues fully viewable without login. **C:** Public Bitbucket repos allow code view, but Bitbucket Issues on public repos require login for full interaction/status boards (0). **D:** Confluence Free public access allows viewing documentation, but Jira Free restricts public guest viewing without account registration/site login (2). |
| RM11.2 | Change history is visible to outsiders | 3 | 3 | 3 | 3 | Commit history of public repositories is unrestrictedly viewable without login. |
| RM11.3 | Documentation is readable by outsiders | 3 | 3 | 3 | 3 | Wiki and repository Markdown files are publicly accessible in public repositories. |
| RM11.4 | Recent activity can be read as a log | 3 | 3 | 3 | 3 | Public activity feeds / commit feeds / pulse logs available natively. |

---

### RM12: Reproducibility support

| Test | The capability is present if... | A | B | C | D | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| RM12.1 | The computational environment can be recorded with the project | 3 | 3 | 3 | 3 | Dockerfiles, `environment.yml`, `renv.lock`, container definitions stored directly in repo. |
| RM12.2 | Exact versions of code and data can be referenced | 3 | 3 | 3 | 3 | Persistent Git commit SHA identifiers and Git tags provide exact immutable references. |
| RM12.3 | The steps to regenerate results can be executed from the platform | 3 | 3 | 3 | 3 | CI/CD pipelines run scripts: GitHub Actions, GitLab CI/CD, Bitbucket Pipelines. |
| RM12.4 | Checks run automatically on proposed changes and can block integration | 3 | 3 | 3 | 3 | Required status checks on Pull/Merge Requests enforced via branch protection. |

---

### RM13: Automation

| Test | The capability is present if... | A | B | C | D | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| RM13.1 | Automation can be triggered by project events | 3 | 3 | 3 | 3 | GitHub Actions triggers, GitLab CI triggers, Bitbucket Pipelines triggers on push/PR/issue events. |
| RM13.2 | Validation runs on every change | 3 | 3 | 3 | 3 | Automated test runs on `push` and `pull_request` events. |
| RM13.3 | Checks can run on a schedule | 3 | 3 | 3 | 3 | Cron/scheduled workflows supported in GitHub Actions, GitLab CI, and Bitbucket Pipelines. |
| RM13.4 | Releases can be built and published automatically | 3 | 3 | 3 | 3 | CI/CD workflows can publish release binaries/artifacts to package registries or platform release pages. |

---

### RM14: Research output management and identification

| Test | The capability is present if... | A | B | C | D | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| RM14.1 | A named version can be published with notes and files | 3 | 3 | 3 | 3 | GitHub Releases, GitLab Releases, Bitbucket Downloads/Releases. |
| RM14.2 | A release can be deposited in an archive that assigns a persistent identifier | 3 | 2 | 1 | 1 | **A:** Direct, native Zenodo & Sandbox integrations (automatically minted DOI on release). **B:** Zenodo webhook integration supported via configuration (2). **C & D:** Manual webhook setup required or web submission to Zenodo/OSF (1). |
| RM14.3 | Citation metadata is machine-readable and used by the platform | 3 | 1 | 0 | 0 | **A:** Native support for `CITATION.cff` files (renders "Cite this repository" UI widget and exports BibTeX/APA). **B:** Can render file, but platform does not natively parse it into UI citations (1). **C & D:** Absent. |
| RM14.4 | A release links back to the work that produced it | 3 | 3 | 3 | 3 | Releases link directly to corresponding Git tag and commit SHA. |

---

### RM15: Governance and sustainability

| Test | The capability is present if... | A | B | C | D | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| RM15.1 | Access can be set by role | 3 | 3 | 3 | 3 | Organization/Project user roles (Owner/Maintainer/Developer/Reporter/Read-Write-Admin). |
| RM15.2 | Ownership can be transferred | 3 | 3 | 3 | 3 | Repository and project ownership transfer capabilities built-in. |
| RM15.3 | Contribution rules are surfaced to contributors | 3 | 3 | 1 | 2 | **A:** `CONTRIBUTING.md` surfaces automatically in PR creation UI. **B:** `CONTRIBUTING.md` surfaced in MR creation UI. **C:** Manual link in README (1). **D:** Confluence/Jira contribution guidelines pages (2). |
| RM15.4 | The project can be frozen and exported at its end | 3 | 3 | 2 | 3 | **A:** Archive repository feature (read-only state) + full repo download / export API. **B:** Archive project + Export project bundle. **C:** Read-only branch rules, but lacks one-click full project archive bundle (2). **D:** Bitbucket archive + Confluence space export (HTML/PDF/XML) + Jira project export. |

---

## General comments

* **RM2 (Research Question Management):** Most software-centric platforms treat research questions as standard "Issues". Jira (Configuration D) scored higher because it allows defining a dedicated issue type named "Research Question" with custom required fields without upgrading to a paid tier.
* **RM7.1 (Discussions):** GitHub scored a 3 due to native **GitHub Discussions**, a feature explicitly designed for open-ended conversation separate from code or actionable issue tickets.
* **RM14.3 (Citation Parsing):** GitHub is currently the only platform among the four that natively parses `CITATION.cff` files in the repository root and displays a dedicated "Cite this repository" button with machine-readable BibTeX and APA formats.

---

## Returning the sheet

* **Consent for acknowledgment:** No, I don't consent to being acknowledged in the resulting article as an independent reviewer.
* **Name for acknowledgment:** Independent Rater
* **Email submission recipient:** tmiguel@ubu.es