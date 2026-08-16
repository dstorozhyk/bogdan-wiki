---
title: Wiki migration review
created: 2026-08-16
updated: 2026-08-16
type: query
status: active
tags: [wiki]
sources: []
---

# Wiki migration review

Pages intentionally left in place during the 2026-08-16 conservative migration because their primary semantic role is debatable or a broader domain migration would be disproportionate.

## Needs classification review

- `research/emergency-fund-{dashboard,strategy,ovdp-research,usdt-usdc-research}.md` and `research/portfolio-denys-snapshot-2026-06-22.md` — likely a future `finance/` domain, but the set mixes stable strategy, imported dashboard syntax, research, and a dated snapshot.
- `research/life-rpg-{startup-strategy,habit-app-roadmap}-2026-06-21.md` and `research/beauty-masters-saas-ukraine-requirements-2026-06-29.md` — product strategies/roadmaps; move only when a project/product area is adopted consistently.
- `research/small-creator-brand-deals-playbook-2026-07-12.md` and `research/ukraine-specialists-strategy.md` — workflow-like pages that still contain research/context; review before moving to `workflows/`.
- `research/ai-assisted-sdlc-vibe-coding-project-lifecycle-2026-07-02.md`, `research/hermes-memory-roadmap.md`, and `research/rocket-attack-alarm-marketing.md` — mixed concept/project/roadmap content.
- Legacy pages without frontmatter — fix incrementally when substantively edited; do not bulk-invent creation dates or statuses.

## Known pre-existing link review

The integrity audit also found unresolved/template/external-style wikilinks in `SCHEMA.md`, `agents/review-queue.md`, `concepts/hermes-codex-oauth-quota-exhaustion.md`, `logs/daily/2026-07-23.md`, and imported `research/emergency-fund-dashboard.md`. These were not caused by this migration and should be resolved only with domain context.

## Related

- [[wiki-decomposition-workflow]]
- [[knowledge-policy]]
