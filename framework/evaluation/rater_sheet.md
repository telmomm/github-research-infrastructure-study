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

| Code | Configuration |
|---|---|
| A | GitHub: GitHub Free, organization account, public repository |
| B | GitLab: GitLab.com Free, public project |
| C | Bitbucket: Bitbucket Cloud Free, public repository, used on its own |
| D | Bitbucket Cloud Free used together with Jira Free and Confluence Free |

Count only features supplied by the vendor on that plan. Do not count third-party or marketplace applications. The one exception is test RM14.2, which is about depositing in an external archive and says so.

If you know only some of the configurations well, score those and leave the other columns empty. A partial sheet is useful.

## The scale

| Score | Meaning |
|---|---|
| 3 | **Native.** The platform ships a feature that does what the test describes. The team does not have to invent a convention. |
| 2 | **By convention.** It can be done with the platform's features, but only by configuring a generic object for the purpose or by following a rule that the platform neither represents nor enforces. |
| 1 | **Marginal.** Only a fragment of the capability, or free text with no structure. |
| 0 | **Absent.** Another product would be needed. |

Two examples of the difference between 3 and 2, using a capability that is not in the sheet. "A meeting can be scheduled": a calendar feature is a 3; an issue with the date typed in its title is a 2. "Tasks can be assigned to a person": an assignee field is a 3; writing a name in the task's description is a 2.

When you hesitate between two scores, give the lower one and say so in the notes.

## What to write

- **A, B, C, D:** the score on the free plan, in the context above.
- **Notes:** the feature you relied on, and anything that affected your score: a capability available only on a paid plan, a recent change, a doubt. A link to the documentation page is welcome where you looked one up. Notes matter most for scores of 2 and below.

## About you

Please fill this in. It is used only to describe the raters as a group.

- Name:
- Date of rating:
- Role and field:
- Platforms you use regularly (and on which plan):
- Platforms you scored mainly from documentation:
- Approximate time spent:

## The sheet


### RM1: Research planning and roadmap

| Test | The capability is present if... | A | B | C | D | Notes |
|---|---|---|---|---|---|---|
| RM1.1 | Named phases or milestones with dates can be defined and work items attached to them |  |  |  |  |  |
| RM1.2 | Objectives can be recorded and progress toward them seen |  |  |  |  |  |
| RM1.3 | A timeline view shows phases across the project |  |  |  |  |  |
| RM1.4 | Earlier versions of the plan can be retrieved |  |  |  |  |  |

### RM2: Research question management

| Test | The capability is present if... | A | B | C | D | Notes |
|---|---|---|---|---|---|---|
| RM2.1 | A research question can be registered as a distinct, identifiable record |  |  |  |  |  |
| RM2.2 | Earlier wordings of a question can be retrieved and compared |  |  |  |  |  |
| RM2.3 | A question can be linked to the items that address it, and the links followed in both directions |  |  |  |  |  |

### RM3: Task management

| Test | The capability is present if... | A | B | C | D | Notes |
|---|---|---|---|---|---|---|
| RM3.1 | A unit of work can be created as a record |  |  |  |  |  |
| RM3.2 | At least to-do, in-progress and done can be recorded per task |  |  |  |  |  |
| RM3.3 | A task can be assigned to a person |  |  |  |  |  |
| RM3.4 | A priority can be recorded per task and used to sort |  |  |  |  |  |
| RM3.5 | One task can be marked as blocking another |  |  |  |  |  |
| RM3.6 | Tasks can be viewed on a board by status |  |  |  |  |  |

### RM4: Documentation

| Test | The capability is present if... | A | B | C | D | Notes |
|---|---|---|---|---|---|---|
| RM4.1 | Structured text documents render in place |  |  |  |  |  |
| RM4.2 | Templates can be defined for recurring documents and records |  |  |  |  |  |
| RM4.3 | Every edit to a document is versioned and attributable |  |  |  |  |  |
| RM4.4 | Project metadata can be recorded in structured, machine-readable form from the start |  |  |  |  |  |

### RM5: Decision traceability

| Test | The capability is present if... | A | B | C | D | Notes |
|---|---|---|---|---|---|---|
| RM5.1 | A decision can be recorded as a distinct type of record |  |  |  |  |  |
| RM5.2 | The record has structured places for rationale and alternatives considered |  |  |  |  |  |
| RM5.3 | The record carries the date of the decision |  |  |  |  |  |
| RM5.4 | The record names who took part |  |  |  |  |  |
| RM5.5 | The record links to the artifacts the decision affects |  |  |  |  |  |

### RM6: Collaboration and contribution tracking

| Test | The capability is present if... | A | B | C | D | Notes |
|---|---|---|---|---|---|---|
| RM6.1 | A change is reviewed by another person before integration, and the review can be made mandatory |  |  |  |  |  |
| RM6.2 | Reviewers can comment on specific lines and propose changes |  |  |  |  |  |
| RM6.3 | Who contributed what can be retrieved |  |  |  |  |  |
| RM6.4 | Contributors can work in parallel and merge |  |  |  |  |  |

### RM7: Communication

| Test | The capability is present if... | A | B | C | D | Notes |
|---|---|---|---|---|---|---|
| RM7.1 | Threaded conversation is possible outside a code change |  |  |  |  |  |
| RM7.2 | A conversation can be linked to the task or artifact it concerns |  |  |  |  |  |
| RM7.3 | Past conversations can be searched |  |  |  |  |  |

### RM8: Version control

| Test | The capability is present if... | A | B | C | D | Notes |
|---|---|---|---|---|---|---|
| RM8.1 | Complete change history per file |  |  |  |  |  |
| RM8.2 | Any two versions can be compared |  |  |  |  |  |
| RM8.3 | An earlier state can be restored |  |  |  |  |  |
| RM8.4 | A state can be named and retrieved later |  |  |  |  |  |
| RM8.5 | Large binary or data files can be versioned |  |  |  |  |  |

### RM9: Research artifact management and integration

| Test | The capability is present if... | A | B | C | D | Notes |
|---|---|---|---|---|---|---|
| RM9.1 | A project structure can be defined and reused |  |  |  |  |  |
| RM9.2 | Artifacts can be classified by type |  |  |  |  |  |
| RM9.3 | Artifacts held in other systems can be referenced in a structured way |  |  |  |  |  |
| RM9.4 | Everything can be reached from one place |  |  |  |  |  |

### RM10: Research provenance and artifact linkage

| Test | The capability is present if... | A | B | C | D | Notes |
|---|---|---|---|---|---|---|
| RM10.1 | A task can be linked to the change that resolved it |  |  |  |  |  |
| RM10.2 | The chain from an output back to its origins can be queried |  |  |  |  |  |
| RM10.3 | Items from different stages can be linked |  |  |  |  |  |
| RM10.4 | Changes are attributable per line |  |  |  |  |  |

### RM11: Transparency

| Test | The capability is present if... | A | B | C | D | Notes |
|---|---|---|---|---|---|---|
| RM11.1 | An outsider can see project status without an account |  |  |  |  |  |
| RM11.2 | Change history is visible to outsiders |  |  |  |  |  |
| RM11.3 | Documentation is readable by outsiders |  |  |  |  |  |
| RM11.4 | Recent activity can be read as a log |  |  |  |  |  |

### RM12: Reproducibility support

| Test | The capability is present if... | A | B | C | D | Notes |
|---|---|---|---|---|---|---|
| RM12.1 | The computational environment can be recorded with the project |  |  |  |  |  |
| RM12.2 | Exact versions of code and data can be referenced |  |  |  |  |  |
| RM12.3 | The steps to regenerate results can be executed from the platform |  |  |  |  |  |
| RM12.4 | Checks run automatically on proposed changes and can block integration |  |  |  |  |  |

### RM13: Automation

| Test | The capability is present if... | A | B | C | D | Notes |
|---|---|---|---|---|---|---|
| RM13.1 | Automation can be triggered by project events |  |  |  |  |  |
| RM13.2 | Validation runs on every change |  |  |  |  |  |
| RM13.3 | Checks can run on a schedule |  |  |  |  |  |
| RM13.4 | Releases can be built and published automatically |  |  |  |  |  |

### RM14: Research output management and identification

| Test | The capability is present if... | A | B | C | D | Notes |
|---|---|---|---|---|---|---|
| RM14.1 | A named version can be published with notes and files |  |  |  |  |  |
| RM14.2 | A release can be deposited in an archive that assigns a persistent identifier |  |  |  |  |  |
| RM14.3 | Citation metadata is machine-readable and used by the platform |  |  |  |  |  |
| RM14.4 | A release links back to the work that produced it |  |  |  |  |  |

### RM15: Governance and sustainability

| Test | The capability is present if... | A | B | C | D | Notes |
|---|---|---|---|---|---|---|
| RM15.1 | Access can be set by role |  |  |  |  |  |
| RM15.2 | Ownership can be transferred |  |  |  |  |  |
| RM15.3 | Contribution rules are surfaced to contributors |  |  |  |  |  |
| RM15.4 | The project can be frozen and exported at its end |  |  |  |  |  |

## General comments

Anything about the tests themselves is useful: a test that was unclear, two tests that seemed to ask the same thing, a capability you think is missing, a configuration you found hard to score.

-

## Returning the sheet

Send the completed file to tmiguel@ubu.es. If you agree, you will be named in the acknowledgments of the resulting article; please say whether you consent to that and how your name should appear.
