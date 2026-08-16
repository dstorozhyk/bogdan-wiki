---
title: Wiki migration review
created: 2026-08-16
updated: 2026-08-17
type: query
status: active
tags: [wiki]
sources: []
---

# Wiki migration review

Pages intentionally left in place because their primary semantic role remains debatable. The finance and project groups below were resolved during the user-directed first knowledge ingest later on 2026-08-16.

## Needs classification review

- `research/small-creator-brand-deals-playbook-2026-07-12.md` and `research/ukraine-specialists-strategy.md` — workflow-like pages that still contain research/context; review before moving to `workflows/`.
- `research/hermes-memory-roadmap.md` — mixed concept/roadmap content.
- Legacy pages without frontmatter — fix incrementally when substantively edited; do not bulk-invent creation dates or statuses.

## Resolved in first structured ingest

- Created `projects/` and moved Rocket marketing, Beauty requirements and Life RPG strategy/roadmap into project areas with explicit statuses.
- Created `finance/`; moved the approved emergency-fund strategy, stale-but-useful dashboard and historical portfolio snapshot. OVDP and stablecoin investigations remain in `research/` because their facts age quickly.
- Created `infrastructure/` and a credential-free main-VPS page from a timestamped live check.

## Resolved in second structured ingest

- Decomposed the mixed AI-assisted SDLC research into `concepts/ai-assisted-sdlc.md` and `workflows/ai-assisted-product-lifecycle.md`; retained the original research note as sourced provenance.
- Added a user-requested technical communication guide and a value-free secret-management policy.

## Resolved in third structured ingest

- Extracted stable emergency-fund tier logic and an approval-gated quarterly review workflow; kept dated platform/rate/tax facts in research and historical balances in the dashboard.
- Extracted a public-profile onboarding workflow from Beauty requirements while excluding later QR/dashboard/analytics candidates that conflict with the confirmed public scope.
- Created the canonical Hermes memory lifecycle from current policy/docs; retained the old enhancement roadmap as explicitly unapproved dated research.

## Known pre-existing link review

The earlier integrity audit found unresolved/template/external-style wikilinks in `SCHEMA.md`, `agents/review-queue.md`, `concepts/hermes-codex-oauth-quota-exhaustion.md`, and `logs/daily/2026-07-23.md`. Resolve only with domain context.

## Related

- [[wiki-decomposition-workflow]]
- [[knowledge-policy]]
