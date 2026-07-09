---
title: Hermes Skill Usage Review
created: 2026-07-03
updated: 2026-07-09
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

## Current Snapshot — 2026-07-09

From `/root/.hermes/skills/.usage.json`:

| Metric | Value |
|---|---:|
| Skills tracked | 112 |
| Zero-use skills | 57 |
| Never-active skills | 57 |

Most active examples by total activity (`use + view + patch`):

| Skill | Total | Use | View | Patch | Last activity |
|---|---:|---:|---:|---:|---|
| `nodejs-vps-operations` | 156 | 41 | 41 | 74 | 2026-07-03 |
| `crypto-fiat-onramps` | 69 | 19 | 19 | 31 | 2026-07-01 |
| `gemini-web-controller` | 67 | 16 | 16 | 35 | 2026-07-06 |
| `ukraine-specialists-finder` | 58 | 13 | 13 | 32 | 2026-06-17 |
| `mobile-app-idea-factory` | 50 | 17 | 16 | 17 | 2026-06-30 |
| `beauty-saas-product-design` | 49 | 20 | 20 | 9 | 2026-07-03 |
| `vps-monitor-telegram` | 46 | 8 | 8 | 30 | 2026-05-29 |
| `obsidian` | 43 | 30 | 10 | 3 | 2026-07-09 |
| `claude-code` | 42 | 20 | 18 | 4 | 2026-07-03 |
| `systematic-debugging` | 41 | 13 | 13 | 15 | 2026-07-01 |
| `youtube-content` | 36 | 18 | 18 | 0 | 2026-07-05 |
| `wiki-knowledge-pipelines` | 36 | 13 | 13 | 10 | 2026-07-06 |

Recently used / newly relevant:

- `obsidian` was used by the nightly consolidation job on 2026-07-09.
- `game-walkthrough-visual-guidance` remains recently relevant for CK3 strategy/UI coaching.
- `steam-game-purchase-advice` appeared in usage telemetry as agent-created on 2026-07-08 with 1 patch and 0 use/view; review after first real Steam purchase-advice task rather than archiving immediately.
- `codex`, `comfyui`, and `gemini-web-controller` remain recently relevant from media/wallpaper workflows.
- `maps`, `ocr-and-documents`, and `wiki-knowledge-pipelines` remain low-to-moderate-use but recently useful.

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
- `computer-use`
- `design-md`
- `evaluating-llms-harness`
- `excalidraw`
- `findmy`
- `gif-search`
- `github-auth`
- `github-code-review`
- `github-issues`
- `google-workspace`

Agent-created low/zero-use examples to review carefully:

- `payment-link-safety` — zero use/view/patch in usage sidecar; created by agent.
- `vps-monitor-dashboard-setup` — zero use/view but 8 patches; likely historical/operational, do not archive without checking VPS Monitor references.
- `steam-game-purchase-advice` — new agent-created skill with 1 patch and 0 use/view; keep until a real Steam purchase/advice task validates or disproves usefulness.
- `game-walkthrough-visual-guidance` — low count but recently used for CK3; currently more map/navigation oriented than strategy/Linux setup coaching.

Curator status (`hermes curator status`):

- Curator enabled; 6 runs; last run ~1 day before this nightly job.
- Last summary: `auto: no changes; llm: skipped (consolidation off)`.
- Last report: `/root/.hermes/logs/curator/20260707-235839`.
- Interval: every 7 days; stale after 30d unused; archive after 90d unused.
- Consolidation: off (prune-only; LLM merge pass opt-in).
- Agent-created skills: 80 active, 0 stale, 0 archived.
- Least recently active examples: `google-ai-tools`, `online-shopping-research`, `xurl`, `airtable`, `apple-notes`.
- Most active curator examples: `crypto-fiat-onramps`, `obsidian`, `claude-code`, `systematic-debugging`, `youtube-content`.

## Review Recommendations — 2026-07-09

- **Pin/review for criticality:** `obsidian`, `hermes-agent`, `wiki-knowledge-pipelines`, `claude-code`, `gemini-web-controller`, `hermes-deferred-task-queue`, `hermes-update-operations`, `youtube-content`, plus production/project runbooks once promoted.
- **Keep but monitor rare utility skills:** `codex`, `comfyui`, `ocr-and-documents`, `maps`, `game-walkthrough-visual-guidance`, and `steam-game-purchase-advice` are low-use/new but plausibly useful; low count alone is not archive evidence.
- **CK3/Linux setup gap:** Denys now asks both CK3 strategy/UI questions and Linux/Proton/NVIDIA performance questions; consider a narrow gaming runbook/wiki note if this continues.
- **Archive review only after human approval:** zero-use official/optional tools should stay unless agent-created, redundant, old enough, and no cron/project reference exists.
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
