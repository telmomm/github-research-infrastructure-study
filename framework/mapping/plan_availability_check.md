# Plan-availability spot-check

**OPEN_ITEMS 4.1 / 5.3.** Verified against [GitHub Docs — GitHub's plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans) on **2026-08-30**. GitHub periodically moves features between tiers; re-check at manuscript submission.

| Capability | Catalogue value | Docs (2026-08-30) | Verdict |
|---|---|---|---|
| GC52 Actions minutes | "all plans (minutes quota; free for public)" | Free 2,000 min/mo, Team 3,000, Enterprise Cloud 50,000; unlimited for public repos | **confirmed** |
| GC44 Branch protection / rulesets | "public repos all plans; private needs Team+" | "Protected branches" listed as a Team advanced tool; rulesets on private repos require Team+ | **confirmed** |
| GC48 Required reviews / CODEOWNERS | "public all plans; private Team+" | "Required pull request reviewers" and "Code owners" listed under Team | **confirmed** |
| GC14 Private wiki | "all plans (private wiki paid)" | Wikis on private repos require Team+ | **confirmed** |
| GC15 Private Pages | "all plans (public; paid for private)" | Publishing a Pages site privately requires an **organization** account (Team+) | **refined** — note updated to "public any plan; private requires an organization (Team+)" |
| GC20 Issue Types | "org (Team/Enterprise)" | Issue Types are configured at organization level | **confirmed** |
| GC62 Custom repository roles | "all plans (custom roles Enterprise)" | Custom repository roles are an Enterprise feature; the five base roles are available to all | **confirmed** |
| GC63 `internal` visibility | "all plans (internal = Enterprise)" | Internal repositories require an enterprise account | **confirmed** |
| GC67 Organization audit log | "org (Team/Enterprise)" | Basic org audit log on Team; audit-log **streaming** is Enterprise Cloud | **confirmed** (streaming clarified as Enterprise) |
| GC68 Dependabot | "all plans (public); private Team+" | Dependabot alerts available on Free; Dependabot on private repos is broadly available now — **may have moved to Free** | **flag** — re-verify at submission; downgrade risk is nil for the coverage scores (RM12 is Partial regardless) |

## Effect on the coverage scores

None of the ten checks changes a Phase 5 support level. The plan gates affect *enforcement* features (branch protection, required reviews) whose absence on Free-private drops RM6/RM8 from "guaranteed" to "by policy", already reflected in their evidence notes. The one refinement (GC15 private Pages → organization) and the one flag (GC68) are documentation-note changes only.

## Catalogue reconciliation

`github_capability_catalogue.csv` GC15 `plan_availability` updated: `all plans (public; private requires an organization / Team+)`.
