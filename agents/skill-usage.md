---
title: Hermes Skill Usage Review
created: 2026-07-03
updated: 2026-07-06
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

## Current Snapshot — 2026-07-06

From `/root/.hermes/skills/.usage.json`:

| Metric | Value |
|---|---:|
| Skills tracked | 111 |
| Zero-use skills | 59 |
| Never-active skills | 59 |

Most active examples:

| Skill | Use | View | Patch | Last activity |
|---|---:|---:|---:|---|
| `nodejs-vps-operations` | 41 | 41 | 74 | 2026-07-03 |
| `obsidian` | 26 | 9 | 3 | 2026-07-06 |
| `beauty-saas-product-design` | 20 | 20 | 9 | 2026-07-03 |
| `claude-code` | 20 | 18 | 4 | 2026-07-03 |
| `crypto-fiat-onramps` | 19 | 19 | 31 | 2026-07-01 |
| `youtube-content` | 18 | 18 | 0 | 2026-07-05 |
| `mobile-app-idea-factory` | 17 | 16 | 17 | 2026-06-30 |
| `gemini-web-controller` | 15 | 15 | 25 | 2026-06-22 |
| `hermes-agent` | 14 | 12 | 0 | 2026-07-05 |
| `ukraine-specialists-finder` | 13 | 13 | 32 | 2026-06-17 |
| `systematic-debugging` | 13 | 13 | 15 | 2026-07-01 |
| `popular-web-designs` | 13 | 13 | 7 | 2026-07-03 |

Recently used / newly relevant:

- `ocr-and-documents` was used 2026-07-05 to extract and summarize an options PDF into wiki.
- `maps` was used 2026-07-05 for Lviv restaurant/place lookup.
- `hermes-agent` was used 2026-07-05 for Freylina cron/profile cleanup.

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
- `codex`
- `comfyui`
- `computer-use`
- `design-md`
- `evaluating-llms-harness`
- `excalidraw`
- `github-auth`
- `github-code-review`
- `google-workspace`
- `jupyter-live-kernel`

Agent-created low/zero-use examples to review carefully:

- `payment-link-safety` — zero use/view/patch in usage sidecar; created by agent.
- `vps-monitor-dashboard-setup` — zero use/view but 8 patches; likely historical/operational, do not archive without checking VPS Monitor references.
- `game-walkthrough-visual-guidance` — 1 use/1 view/1 patch; rare but useful workflow, not an archive candidate yet.

Curator status (`hermes curator status`):

- Curator enabled; 5 runs; last run 5 days ago.
- Last summary: `auto: no changes; llm: skipped (consolidation off)`.
- Interval: every 7 days; stale after 30d unused; archive after 90d unused.
- Consolidation: off (prune-only; LLM merge pass opt-in).
- Agent-created skills: 79 active, 0 stale, 0 archived.
- Least recently active examples: `google-ai-tools`, `online-shopping-research`, `xurl`, `airtable`, `apple-notes`.
- Most active curator examples: `crypto-fiat-onramps`, `claude-code`, `systematic-debugging`, `obsidian`, `youtube-content`.

## Review Recommendations — 2026-07-06

- **Pin/review for criticality:** `obsidian`, `claude-code`, `hermes-agent`, `hermes-deferred-task-queue`, `hermes-update-operations`, `youtube-content`, and recurring production/project skills such as Rocket/Beauty workflows once promoted.
- **Keep but monitor rare utility skills:** `ocr-and-documents` and `maps` were useful in the last 24h despite low total usage; do not treat low usage alone as archive evidence.
- **Consolidation / repair candidate now mostly resolved:** Freylina’s duplicate default-profile cron jobs that referenced missing `devops/youtube-to-wiki-pipeline` were removed in a user-triggered repair session; keep a review item to capture the canonical script-only Freylina profile workflow in a runbook/skill, but no destructive skill action is needed from nightly SAFE MODE.
- **Archive review only after human approval:** zero-use official/optional tools should stay unless they are agent-created, redundant, old enough, and have no cron/project reference.
- **Marketplace replacement:** safe to propose missing skills via review queue, but do not auto-install from the nightly job.

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
