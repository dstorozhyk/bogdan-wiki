---
title: Hermes Skill Usage Review
created: 2026-07-03
updated: 2026-07-28
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

## Current Snapshot — 2026-07-29

| Metric | Value |
|---|---:|
| Skills tracked | 125 |
| Zero-use skills | 59 |
| Never-active skills (`use + view + patch = 0`) | 56 |
| Curator agent-created skills | 37 active; 47 stale; 0 archived (84 total) |

Most active by total sidecar activity:

| Skill | Total activity |
|---|---:|
| `nodejs-vps-operations` | 201 |
| `crypto-fiat-onramps` | 69 |
| `obsidian` | 68 |
| `gemini-web-controller` | 67 |
| `ukraine-specialists-finder` | 58 |

Zero-activity examples for human review only: `docx`, `pdf`, `xlsx`, `airtable`, `apple-notes`, `apple-reminders`, `architecture-diagram`, `arxiv`, `ascii-art`, `ascii-video`.

Curator is enabled: 9 runs; latest run was about 1 hour ago; 7-day interval; stale threshold 30 days; archive threshold 90 days; LLM consolidation is off. Its summary reports 47 stale agent-created skills. The sidecar's direct provenance field names only one stale agent-created skill, `google-ai-tools`; this discrepancy must not drive automatic lifecycle action.

## Review Recommendations — 2026-07-29

- Human-review `google-ai-tools` and the curator-reported stale cohort; retain, repair, pin, consolidate later, or archive only through an explicit decision.
- Keep high-impact operational skills—including `obsidian`, `claude-code`, `youtube-content`, `gemini-and-notebooklm`, and relevant Hermes operations runbooks—under explicit human pin/review consideration; do not pin automatically.
- Keep new or rare skills when they have plausible task value; zero use alone is not deletion or consolidation evidence.
- Retain the CK3 coaching broadening candidate only until disputed mechanics are independently verified.
- Do not archive, delete, install, consolidate, or pin skills in the nightly job without explicit approval.

## Nightly Job Rules

1. Read the usage sidecar and curator status.
2. Update totals, activity examples, and candidates concisely.
3. Queue human review instead of destructive skill actions.
4. Treat marketplace/official skills conservatively: unused does not mean obsolete.
