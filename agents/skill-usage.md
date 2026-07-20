---
title: Hermes Skill Usage Review
created: 2026-07-03
updated: 2026-07-20
type: query
tags: [wiki, skills]
---

# Hermes Skill Usage Review

Operational note for the nightly sleep job. Related: [[agents/knowledge-policy]], [[agents/review-queue]], [[log]], [[index]].

## Purpose

Track actual Hermes skill use to preserve high-signal workflows, identify candidates for human review, and avoid automatic deletion of rare but legitimate tools.

## Data Sources

- Runtime usage: `/root/.hermes/skills/.usage.json`
- Curator: `hermes curator status`

## Current Snapshot — 2026-07-20

| Metric | Value |
|---|---:|
| Skills tracked | 113 |
| Zero-use skills | 59 |
| Never-active skills (`use + view + patch = 0`) | 57 |
| Agent-created skills | 80 active; 0 stale; 0 archived |

Most active by total activity:

| Skill | Total activity |
|---|---:|
| `nodejs-vps-operations` | 156 |
| `crypto-fiat-onramps` | 69 |
| `gemini-web-controller` | 67 |
| `ukraine-specialists-finder` | 58 |
| `obsidian` | 56 |
| `mobile-app-idea-factory` | 50 |
| `beauty-saas-product-design` | 49 |
| `claude-code` | 46 |

Zero-activity examples for human review only: `airtable`, `apple-notes`, `apple-reminders`, `architecture-diagram`, `arxiv`, `ascii-art`, `ascii-video`, `audiocraft-audio-generation`, `baoyu-infographic`, `codebase-inspection`.

Curator is enabled: 7 runs; last run 5 days before this snapshot; 7-day interval; stale threshold 30 days; archive threshold 90 days; LLM consolidation is off. Least-recently-active nonzero examples: `google-ai-tools` (33 days), `online-shopping-research` (30 days), and `xurl` (28 days); never-active skills follow.

## Review Recommendations — 2026-07-20

- Keep high-impact operational skills—including `obsidian`, `claude-code`, `youtube-content`, `gemini-and-notebooklm`, and relevant Hermes operations runbooks—under explicit human pin/review consideration; do not pin automatically.
- Keep new or rare skills when they have plausible task value; zero use alone is not deletion or consolidation evidence.
- Retain the existing CK3 coaching broadening candidate only until mechanics are independently verified.
- Do not archive, delete, install, consolidate, or pin skills in the nightly job without explicit approval.

## Nightly Job Rules

1. Read the usage sidecar and curator status.
2. Update totals, activity examples, and candidates concisely.
3. Queue human review instead of destructive skill actions.
4. Treat marketplace/official skills conservatively: unused does not mean obsolete.
