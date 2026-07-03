---
title: Hermes Skill Usage Review
created: 2026-07-03
updated: 2026-07-03
type: query
tags: [wiki, skills]
---

# Hermes Skill Usage Review

Operational note for the nightly sleep job. Related: [[agents/knowledge-policy]], [[agents/review-queue]], [[log]], [[index]].

## Purpose

Track which Hermes skills are actually used so Bogdan can keep the skill library lean:

- preserve high-signal skills that are repeatedly loaded or patched;
- identify zero-use / stale skills for review;
- avoid deleting useful but rare skills automatically;
- use Hermes Curator for lifecycle state and backups.

## Data Sources

- Runtime usage sidecar: `/root/.hermes/skills/.usage.json`
- Curator CLI summary: `hermes curator status`
- Installed skill inventory: `hermes skills list`
- Hub/marketplace discovery when a missing skill is needed: `hermes skills search`, `hermes skills inspect`, `hermes skills install`

## Current Snapshot — 2026-07-03

From `/root/.hermes/skills/.usage.json`:

| Metric | Value |
|---|---:|
| Skills tracked | 111 |
| Zero-use skills | 60 |
| Old or never active skills | 65 |

Most active examples:

| Skill | Use | View | Patch | Last activity |
|---|---:|---:|---:|---|
| `nodejs-vps-operations` | 41 | 41 | 74 | today |
| `crypto-fiat-onramps` | 19 | 19 | 31 | 1d ago |
| `ukraine-specialists-finder` | 13 | 13 | 32 | 15d ago |
| `gemini-web-controller` | 15 | 15 | 25 | 10d ago |
| `mobile-app-idea-factory` | 17 | 16 | 17 | 3d ago |
| `obsidian` | 23 | 9 | 2 | today |
| `claude-code` | 17 | 15 | 4 | today |

Zero-use examples to keep under review, not auto-delete:

- `airtable`
- `apple-notes`
- `apple-reminders`
- `architecture-diagram`
- `arxiv`
- `ascii-art`
- `ascii-video`
- `audiocraft-audio-generation`
- `baoyu-infographic`
- `codebase-inspection`

## Nightly Job Rules

1. Read `/root/.hermes/skills/.usage.json` if it exists.
2. Run `hermes curator status` when available.
3. Update this note with a concise snapshot: totals, most active, least active, zero-use, stale candidates.
4. Add review candidates to `agents/review-queue.md` instead of deleting skills directly.
5. Never delete or archive skills from the daily job. Use curator or explicit Denys approval for destructive changes.
6. Treat hub-installed/official skills conservatively: unused does not mean worthless; many are intentionally rare tools.

## Review Thresholds

- **Candidate for review:** `use_count=0`, `view_count=0`, `patch_count=0` and older than 30 days / never active.
- **Candidate for consolidation:** overlaps heavily with a more active skill or has duplicated purpose.
- **Candidate for pinning:** rare but high-impact operational skill where losing it would be costly.
- **Candidate for archive:** agent-created, unused/stale, not pinned, no active cron/job reference, and no recent session mentions.
