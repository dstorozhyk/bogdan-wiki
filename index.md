# Wiki Index

Content catalog. Every wiki page listed under its type with a one-line summary.
Read this first to find relevant pages for any query.

> Last updated: 2026-08-17 | Third structured ingest: canonical finance/Beauty/memory lifecycle extraction.

## Core / Meta

- [README](README.md) — wiki repository overview.
- [SCHEMA](SCHEMA.md) — wiki schema, tag taxonomy, update policy.
- [SOUL](SOUL.md) — high-level operating note/persona artifact.
- [log](log.md) — append-only wiki action log.

## Agent Knowledge Ops

- [agents/knowledge-policy](agents/knowledge-policy.md) — routing policy for memory vs skills vs wiki plus nightly sleep job behavior.
- [agents/review-queue](agents/review-queue.md) — safe-mode staging queue for memory, skill, wiki, and open-loop candidates.
- [agents/skill-usage](agents/skill-usage.md) — skill usage telemetry and review rules for pruning/pinning/consolidation candidates.
- [agents/migration-review](agents/migration-review.md) — ambiguous legacy classifications and pre-existing link/frontmatter debt intentionally left for review.
- `logs/daily/` — generated daily knowledge digests from the safe nightly consolidation job.

## Career Context

- [career/profile/denys-career-direction](career/profile/denys-career-direction.md) — confirmed corporate-career direction: system-level influence, architecture judgment and Staff/Principal/Architect scope rather than startup/title signaling.
- [career/skills/professional-communication](career/skills/professional-communication.md) — practical structures for concise technical positions, calibrated confidence, trade-offs and decision-oriented Staff/architect communication.
- [career/profile/denys-6k-senior-to-tech-lead-gap-analysis-2026-08](career/profile/denys-6k-senior-to-tech-lead-gap-analysis-2026-08.md) — draft evidence-based profile/gap analysis; explicitly not an approved plan.
- [career/job-search/job-search-sources-denys](career/job-search/job-search-sources-denys.md) — Denys-provided active vacancy-monitoring criteria; not a career plan.
- [career/learning/corporate-influence-reading-path-2026-08](career/learning/corporate-influence-reading-path-2026-08.md) — active reading path for strategy, judgment, organizational influence, and cross-team coordination.
- [career/work-context/enterprise-ai-team-vision-tech-lead-meeting-prep-2026-07-12](career/work-context/enterprise-ai-team-vision-tech-lead-meeting-prep-2026-07-12.md) — durable reference from internal enterprise-AI meeting preparation.
- [career/ideas/denys-tech-lead-90-day-plan-2026-08](career/ideas/denys-tech-lead-90-day-plan-2026-08.md) — unapproved assistant draft; not Denys's plan.
- [career/ideas/work-situation-documentation-idea](career/ideas/work-situation-documentation-idea.md) — unapproved idea for anonymized work-situation notes; no routine is active.

## Projects

- [projects/rocket-attack-alarm/overview](projects/rocket-attack-alarm/overview.md) — active Telegram threat-alert bot: product scope, source-of-truth boundaries, documentation map and verified deployment snapshot.
- [projects/rocket-attack-alarm/operations-reference](projects/rocket-attack-alarm/operations-reference.md) — source-checked operational behavior, dedup distinctions, API/city workflow, disk-full SQLite lesson and deploy verification checklist.
- [projects/rocket-attack-alarm/marketing-ideas](projects/rocket-attack-alarm/marketing-ideas.md) — unapproved growth/content backlog; not an active publishing plan.
- [projects/beauty-growth-assistant/overview](projects/beauty-growth-assistant/overview.md) — active product context for the mobile-first beauty-master public profile and optional trust-first automation.
- [projects/beauty-growth-assistant/product-requirements](projects/beauty-growth-assistant/product-requirements.md) — user-directed product requirements, MVP/anti-automation response and confirmed public-profile direction.
- [projects/life-rpg/overview](projects/life-rpg/overview.md) — archived startup direction retained as a validation/product-asset case; no completed launch evidence found.
- [projects/life-rpg/startup-strategy](projects/life-rpg/startup-strategy.md) — archived assistant strategy draft.
- [projects/life-rpg/product-roadmap](projects/life-rpg/product-roadmap.md) — archived assistant roadmap draft.

## Personal Finance

- [finance/overview](finance/overview.md) — map of active strategy, historical state and time-sensitive research plus the observed EUR broker-funding route.
- [finance/emergency-fund/strategy](finance/emergency-fund/strategy.md) — user-directed $6k/$12k/$18k emergency-fund strategy and usage/rebalance rules; live facts must be rechecked before action.
- [finance/emergency-fund/dashboard](finance/emergency-fund/dashboard.md) — Dataview dashboard with numeric state last updated 2026-06-25; not a live balance.
- [finance/portfolio/snapshots/2026-06-22](finance/portfolio/snapshots/2026-06-22.md) — historical portfolio snapshot, not current holdings.

## Infrastructure

- [infrastructure/vps-main](infrastructure/vps-main.md) — credential-free host/service context and timestamped resource/deployment snapshot for the main VPS.
- [infrastructure/secret-management-policy](infrastructure/secret-management-policy.md) — Bitwarden EU/project-scoped least-privilege policy; deliberately contains no secret values or account-specific credentials.

## Entities

- [payoneer-invoice-payment-request-ukraine-saas](entities/payoneer-invoice-payment-request-ukraine-saas.md) — Payoneer invoice/payment request як швидкий спосіб приймати B2B/prosumer SaaS paid pilot платежі з України.

## Concepts

- [ai-assisted-sdlc](concepts/ai-assisted-sdlc.md) — canonical boundary: AI accelerates implementation but increases the need for scope, architecture guardrails and executable verification.
- [emergency-fund-liquidity-tiers](concepts/emergency-fund-liquidity-tiers.md) — approved three-tier model organized by time-to-access, failure domains and resilience rather than yield alone.
- [hermes-memory-lifecycle](concepts/hermes-memory-lifecycle.md) — canonical routing and lifecycle across working context, sessions, compact memory/profile, skills, wiki and runtime state.
- [hermes-codex-oauth-quota-exhaustion](concepts/hermes-codex-oauth-quota-exhaustion.md) — чому Codex (ChatGPT OAuth) застрягає в `exhausted` після 429 і як лікувати (`hermes auth reset openai-codex`).
- [wiki-decomposition-workflow](concepts/wiki-decomposition-workflow.md) — правило розкладати wiki-дослідження на overview/entity/comparison/workflow/checklist файли.

## Comparisons

- [saas-invoice-service-shortlist-ukraine](comparisons/saas-invoice-service-shortlist-ukraine.md) — shortlist Payoneer, crypto invoices, PayPal fallback, PayRequest, Zoho/Invoicely/Bonsai/Invoice2go для українського SaaS validation.

## Workflows

- [ai-assisted-product-lifecycle](workflows/ai-assisted-product-lifecycle.md) — RAT/prototype → walking skeleton → vertical slice → MLP → controlled pilot, with verification gates for agent-generated changes.
- [automation-idea-validation-funnel](workflows/automation-idea-validation-funnel.md) — approved multi-cycle filter: evidence/dedup → user fit → feasibility → ROI → adversarial pre-mortem → scored judge → gap recovery.
- [beauty-public-profile-onboarding](workflows/beauty-public-profile-onboarding.md) — owner-approved identity/services/trust/location/contact intake, mobile page hierarchy and pre-release verification without forcing CRM.
- [emergency-fund-quarterly-review](workflows/emergency-fund-quarterly-review.md) — refresh balances, recalculate resilience, verify live platform/instrument facts and prepare approval-gated rebalancing decisions.
- [manual-paid-pilot-workflow](workflows/manual-paid-pilot-workflow.md) — manual landing → invoice → activation workflow for SaaS validation.

## Queries

(No dedicated query pages yet.)

## Summaries / Research


- [ukraine-it-market-baseline-2026-08](research/ukraine-it-market-baseline-2026-08.md) — первинний, джерельно-обмежений зріз Djinni/офіційної статистики ІТ-ринку України: попит, конкуренція, Data/AI та макроконтекст.
- [dou-raw-salaries-dotnet-analysis-2026-08](research/dou-raw-salaries-dotnet-analysis-2026-08.md) — **застарілий mirror-аналітичний зріз 2015–2020**; збережено тільки для історії, поточне джерело нижче.
- [dou-current-raw-salaries-dotnet-analysis-2026-08](research/dou-current-raw-salaries-dotnet-analysis-2026-08.md) — Python-аналіз актуального `devua/csv` DOU raw dataset за 2026-06: .NET P25/median/P75/P90, $6k+ upper tail і тайтли.

- [part-time-opportunities-shortlist-2026-08-15](research/part-time-opportunities-shortlist-2026-08-15.md) — time-sensitive shortlist part-time Djinni ролей, оцінений під .NET/fintech/microservices профіль Дениса; відокремлено direct fit від stretch і mismatch.
- [part-time-dotnet-availability-snapshot-2026-08-15](research/part-time-dotnet-availability-snapshot-2026-08-15.md) — статистичний зріз доступності public .NET part-time: DOU 1 картка, Djinni 4, із **0** Senior backend/payments fit; короткострокова оцінка, не стратегія.

- [dotnet-ukrainian-language-vacancies-2026-08-15](research/dotnet-ukrainian-language-vacancies-2026-08-15.md) — dated full-time reference scan of nearby .NET backend roles; current monitoring criteria are maintained separately in `career/job-search/`.
- [ukraine-it-career-advantage-hypotheses-2026-08](research/ukraine-it-career-advantage-hypotheses-2026-08.md) — ранжовані гіпотези переваги Дениса: enterprise AI/platform architecture, regulated B2B/fintech, governance і технічний вплив; 90-денний експеримент.

- [small-creator-brand-deals-playbook-2026-07-12](research/small-creator-brand-deals-playbook-2026-07-12.md) — процес пошуку, пітчингу, узгодження та вимірювання перших brand deals для малого автора.
- [small-creator-brand-deals-pricing-2026-07-12](research/small-creator-brand-deals-pricing-2026-07-12.md) — робоча логіка rate card для «Все про Royal» на основі релевантності й перевіреної конверсії, а не лише CPM.
- [ai-assisted-sdlc-vibe-coding-project-lifecycle-2026-07-02](research/ai-assisted-sdlc-vibe-coding-project-lifecycle-2026-07-02.md) — original sourced synthesis retained for provenance; canonical concept and executable workflow now live under `concepts/` and `workflows/`.
- [emergency-fund-ovdp-research](research/emergency-fund-ovdp-research.md) — дослідження USD ОВДП для подушки; фінальне рішення: mono валютна банка $5k, звільнені $600 → SGOV/UCITS-equivalent routing.
- [emergency-fund-usdt-usdc-research](research/emergency-fund-usdt-usdc-research.md) — дослідження USDT/USDC частини подушки; фінальне рішення: $3.8k stablecoin sleeve через WhiteBIT/Binance, транші instant/30д/90д, ризики CEX/емітентів.
- [mobile-app-stores-as-saas-payment-route-ukraine-2026-06-21](research/mobile-app-stores-as-saas-payment-route-ukraine-2026-06-21.md) — using iOS/Android app stores and in-app purchases as a B2C/prosumer SaaS payment workaround for Ukraine.
- [saas-payments-ukraine-validation-2026-06](research/saas-payments-ukraine-validation-2026-06.md) — як тестити SaaS payments з України без негайного відкриття іноземної компанії.

- [whitebit-binance-usdt-staking-route-2026-06](research/whitebit-binance-usdt-staking-route-2026-06.md) — when WhiteBIT direct UAH→USDT beats Binance P2P, and Binance→WhiteBIT network workflow for USDT staking/lending.
- [freedom24-ukraine-funding-2026-06](research/freedom24-ukraine-funding-2026-06.md) — account-specific route confirmed 2026-06-23: Raiffeisen EUR → Wise EUR balance → Freedom EUR; 8.72 EUR credited as 8.72 EUR, with receipt-level fee verification still required.
- [hermes-memory-roadmap](research/hermes-memory-roadmap.md) — roadmap/research notes for Hermes memory improvements.
- [ai-agent-memory-landscape-2026](research/ai-agent-memory-landscape-2026.md) — landscape of AI agent memory approaches.
- [ai-agent-memory-papers-deep-dive](research/ai-agent-memory-papers-deep-dive.md) — deeper notes on AI agent memory papers.
- [lviv-ac-drain-shortlist-2026-06-01](research/lviv-ac-drain-shortlist-2026-06-01.md) — Lviv AC drain specialist shortlist.
- [ukraine-specialists](research/ukraine-specialists.md) — Ukraine specialists finder notes and contacts.
- [ukraine-specialists-strategy](research/ukraine-specialists-strategy.md) — strategy for finding local Ukrainian specialists.

## Memory Mirrors

- [memories/USER](memories/USER.md) — mirrored user-profile facts.
- [memories/MEMORY](memories/MEMORY.md) — mirrored agent memory facts.
