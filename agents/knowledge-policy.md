---
title: Agent Knowledge Policy
created: 2026-06-20
updated: 2026-07-03
type: concept
tags: [wiki, guide]
---

# Agent Knowledge Policy

Policy for deciding what Bogdan should preserve after daily work. Related: [[log]], [[index]], [[wiki-decomposition-workflow]].

## Purpose

Keep long-term knowledge useful without turning memory, skills, or wiki into a noisy transcript archive.

The rule of thumb:

- **Memory** stores compact, stable facts that reduce repeated steering.
- **Skills** store reusable procedures and workflows.
- **Wiki** stores durable, human-readable knowledge, research, decisions, and daily summaries.
- **Session DB** stores raw conversation history and should be searched instead of duplicated.

## Routing Rules

| Destination | Save when | Do not save |
|---|---|---|
| Memory | Stable fact likely useful in 30+ days; user preference; environment/config pointer; recurring correction | PR numbers, issue numbers, daily progress, temporary TODOs, raw transcripts, facts likely stale in a week |
| Skill | Reusable workflow; 5+ tool calls; tricky error/pitfall; exact commands; repeatable verification | One-off task status, broad research notes, artifact-specific logs |
| Wiki | Research, decisions, comparisons, architecture, runbooks, daily digests, review queues | Secrets, noisy raw output, unverified speculative claims without labels |
| Discard | Trivial, duplicate, already captured, or transient | Anything with future operational value |

## Daily Sleep Job Behavior

The nightly consolidation job runs in **safe mode** first:

1. Search/review recent Hermes sessions from the last 24 hours.
2. Extract durable knowledge candidates.
3. Write a daily digest under `logs/daily/YYYY-MM-DD.md`.
4. Append a short entry to `log.md`.
5. Update `agents/review-queue.md` with candidates.
6. Track skill usage in `agents/skill-usage.md` from `/root/.hermes/skills/.usage.json` and `hermes curator status`.
7. Do **not** automatically create/edit/delete skills unless Denys explicitly changes the mode.
8. **Memory compaction exception:** if `~/.hermes/memories/MEMORY.md` or `USER.md` exceeds 80% of its configured limit, the job may compact/remove stale or non-operational entries after first mirroring displaced detail to wiki. It must not invent new facts, store secrets, or remove core user preferences/config pointers.

## Memory Compaction Rules

Default limits: `MEMORY.md` 2,200 chars, `USER.md` 1,375 chars. The sleep job should calculate live usage from `/root/.hermes/memories/MEMORY.md` and `/root/.hermes/memories/USER.md`.

When either store is above 80%:

1. Archive displaced detail to a wiki note if it is still useful but too operational/verbose for always-on memory.
2. Prefer shortening/merging overlapping entries over deleting important facts.
3. Keep user identity, stable preferences, critical infra pointers, credentials/config pointers, and active project roots.
4. Move long project direction, research summaries, completed-task logs, and stale implementation detail to wiki.
5. Use the `memory` tool batch operations when available; otherwise write proposed compactions to review queue only.
6. Record before/after char counts in the daily digest.

## Skill Usage Rules

Skill lifecycle is handled by Hermes Curator plus human review, not daily-job deletion.

- Usage source: `/root/.hermes/skills/.usage.json`.
- Summary source: `hermes curator status`.
- Daily output: update `agents/skill-usage.md` with totals, most active, least active, zero-use/stale candidates.
- Review queue: add candidates for pin/archive/consolidation, but do not delete skills automatically.
- Marketplace fallback: when a needed skill is missing, first search/inspect hub sources before installing; install only with a clear task need and safe scan verdict.

## Daily Digest Template

```md
---
title: Daily Knowledge Digest YYYY-MM-DD
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: summary
tags: [wiki]
---

# Daily Knowledge Digest — YYYY-MM-DD

## Sessions Reviewed

- Session title/id/source/time — short purpose

## Durable Decisions / Facts

- Decision/fact
  - Evidence/session reference
  - Suggested destination: wiki | memory | skill | discard

## Wiki Updates Made

- File updated/created — why

## Memory Candidates

- Proposed text:
  - Why durable:
  - Risk/staleness:

## Skill Candidates

- Proposed skill name:
  - Trigger:
  - Reusable workflow:
  - Commands/pitfalls/verification to include:

## Open Loops

- [ ] Item — owner/context

## Discarded Noise

- Category — why discarded
```

## Review Queue Rules

`agents/review-queue.md` is the staging area for anything unsafe to auto-apply.

- Keep newest items at the top.
- Use checkboxes so Denys can approve/reject.
- Include enough context to act without re-reading the whole transcript.
- Remove or archive stale candidates after 30 days.

## Promotion Rules

A candidate can be promoted when:

- **Memory:** it is compact, declarative, stable, and not task progress.
- **Skill:** it has a clear trigger, exact steps, pitfalls, and verification.
- **Wiki:** it improves future retrieval or decision-making.

## Safety Defaults

- Never store secrets in wiki or memory.
- Never fabricate evidence if session search is incomplete.
- If uncertain, label as `needs review` instead of applying.
- Prefer multiple focused wiki pages over one monolith for substantial research.
