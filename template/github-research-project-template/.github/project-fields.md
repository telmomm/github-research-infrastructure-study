# Project (v2) field definitions

GitHub Projects cannot be seeded from files, so configure these by hand once, on a
user- or org-level Project linked to this repository (components A1, A2).

## Fields

| Field | Type | Options / notes |
|---|---|---|
| **Status** | single select | `Todo`, `In progress`, `In review`, `Blocked`, `Done` |
| **Research phase** | single select | `Idea`, `Question`, `Planning`, `Literature`, `Methods`, `Data`, `Analysis`, `Results`, `Manuscript`, `Publication`, `Outputs` — must match `docs/roadmap.md` and the milestone names |
| **Priority** | single select | `P0`, `P1`, `P2` |
| **Related RQ** | text | the `RQ-n` this item serves (also add `Refs #<rq>` in the issue body) |
| **Artifact** | text | main file / folder the item touches |
| **Target** | date | optional |

## Views

| View | Layout | Group by | Use |
|---|---|---|---|
| Board | board | Status | day-to-day |
| Roadmap | roadmap | Research phase (date/Target on the timeline) | planning |
| By phase | table | Research phase | phase progress |
| By artifact | table | Artifact | see what touches each part of the repo |

## Built-in workflows to enable

- Item added → Status `Todo`
- Pull request merged → Status `Done`
- Issue closed → Status `Done`
- Issue reopened → Status `In progress`
