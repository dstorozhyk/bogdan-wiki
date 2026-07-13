# Wiki Index

Content catalog. Every wiki page listed under its type with a one-line summary.
Read this first to find relevant pages for any query.

> Last updated: 2026-07-03 | Content pages listed: 28 | Markdown files total: 48 including schema/log/memory

## Core / Meta

- [README](README.md) — wiki repository overview.
- [SCHEMA](SCHEMA.md) — wiki schema, tag taxonomy, update policy.
- [SOUL](SOUL.md) — high-level operating note/persona artifact.
- [log](log.md) — append-only wiki action log.

## Agent Knowledge Ops

- [agents/knowledge-policy](agents/knowledge-policy.md) — routing policy for memory vs skills vs wiki plus nightly sleep job behavior.
- [agents/review-queue](agents/review-queue.md) — safe-mode staging queue for memory, skill, wiki, and open-loop candidates.
- [agents/skill-usage](agents/skill-usage.md) — skill usage telemetry and review rules for pruning/pinning/consolidation candidates.
- `logs/daily/` — generated daily knowledge digests from the safe nightly consolidation job.

## Entities

- [payoneer-invoice-payment-request-ukraine-saas](research/payoneer-invoice-payment-request-ukraine-saas.md) — Payoneer invoice/payment request як швидкий спосіб приймати B2B/prosumer SaaS paid pilot платежі з України.

## Concepts

- [hermes-codex-oauth-quota-exhaustion](concepts/hermes-codex-oauth-quota-exhaustion.md) — чому Codex (ChatGPT OAuth) застрягає в `exhausted` після 429 і як лікувати (`hermes auth reset openai-codex`).
- [wiki-decomposition-workflow](concepts/wiki-decomposition-workflow.md) — правило розкладати wiki-дослідження на overview/entity/comparison/workflow/checklist файли.

## Comparisons

- [saas-invoice-service-shortlist-ukraine](research/saas-invoice-service-shortlist-ukraine.md) — shortlist Payoneer, crypto invoices, PayPal fallback, PayRequest, Zoho/Invoicely/Bonsai/Invoice2go для українського SaaS validation.

## Queries

(No dedicated query pages yet.)

## Summaries / Research

- [enterprise-ai-team-vision-tech-lead-meeting-prep-2026-07-12](research/enterprise-ai-team-vision-tech-lead-meeting-prep-2026-07-12.md) — підготовка Дениса до внутрішньої зустрічі «Обговорення бачення AI-команди»: enterprise AI vision, controlled pilots, AI-assisted SDLC guardrails, 90-денний plan і позиціонування на Tech Lead.
- [small-creator-brand-deals-playbook-2026-07-12](research/small-creator-brand-deals-playbook-2026-07-12.md) — процес пошуку, пітчингу, узгодження та вимірювання перших brand deals для малого автора.
- [small-creator-brand-deals-pricing-2026-07-12](research/small-creator-brand-deals-pricing-2026-07-12.md) — робоча логіка rate card для «Все про Royal» на основі релевантності й перевіреної конверсії, а не лише CPM.
- [ai-assisted-sdlc-vibe-coding-project-lifecycle-2026-07-02](research/ai-assisted-sdlc-vibe-coding-project-lifecycle-2026-07-02.md) — AI-assisted SDLC для vibe-coded продуктів: PoC/Prototype/RAT/Walking Skeleton/Vertical Slice/MLP/Pilot замість автоматичного “MVP”.
- [emergency-fund-dashboard](research/emergency-fund-dashboard.md) — Obsidian Dataview dashboard для трекінгу Emergency Fund: фази $6k/$12k/$18k, рівні доступу, географія, категорії та current/target по інструментах.
- [emergency-fund-strategy](research/emergency-fund-strategy.md) — стратегія побудови подушки Denys: $2k/міс витрат, ціль $18k, структура Р1/Р2/Р3, правила використання і квартальний ребаланс.
- [emergency-fund-ovdp-research](research/emergency-fund-ovdp-research.md) — дослідження USD ОВДП для подушки; фінальне рішення: mono валютна банка $5k, звільнені $600 → SGOV/UCITS-equivalent routing.
- [emergency-fund-usdt-usdc-research](research/emergency-fund-usdt-usdc-research.md) — дослідження USDT/USDC частини подушки; фінальне рішення: $3.8k stablecoin sleeve через WhiteBIT/Binance, транші instant/30д/90д, ризики CEX/емітентів.
- [beauty-masters-saas-ukraine-requirements-2026-06-29](research/beauty-masters-saas-ukraine-requirements-2026-06-29.md) — вимоги, MVP, позиціонування, standalone-first public-візитівка і objection handling для SaaS/CRM українських beauty-майстрів із optional automation modules.
- [life-rpg-startup-strategy-2026-06-21](research/life-rpg-startup-strategy-2026-06-21.md) — startup strategy for a mobile-first AI-powered Life RPG habit/self-improvement app.
- [life-rpg-habit-app-roadmap-2026-06-21](research/life-rpg-habit-app-roadmap-2026-06-21.md) — roadmap, MVP scope, validation metrics, and launch plan for the Life RPG habit app concept.
- [mobile-app-stores-as-saas-payment-route-ukraine-2026-06-21](research/mobile-app-stores-as-saas-payment-route-ukraine-2026-06-21.md) — using iOS/Android app stores and in-app purchases as a B2C/prosumer SaaS payment workaround for Ukraine.
- [saas-payments-ukraine-validation-2026-06](research/saas-payments-ukraine-validation-2026-06.md) — як тестити SaaS payments з України без негайного відкриття іноземної компанії.
- [manual-paid-pilot-workflow](research/manual-paid-pilot-workflow.md) — покроковий ручний paid pilot workflow: landing → form → invoice → manual activation.
- [whitebit-binance-usdt-staking-route-2026-06](research/whitebit-binance-usdt-staking-route-2026-06.md) — when WhiteBIT direct UAH→USDT beats Binance P2P, and Binance→WhiteBIT network workflow for USDT staking/lending.
- [freedom24-ukraine-funding-2026-06](research/freedom24-ukraine-funding-2026-06.md) — практичний маршрут поповнення Freedom24/Freedom Finance з України; Wise/ZEN викреслені, Genome/SEPA лишається fallback через ~20 EUR/USD monthly fee.
- [rocket-attack-alarm-marketing](research/rocket-attack-alarm-marketing.md) — marketing/research notes for the Повітряні Загрози / rocket attack alarm project.
- [hermes-memory-roadmap](research/hermes-memory-roadmap.md) — roadmap/research notes for Hermes memory improvements.
- [ai-agent-memory-landscape-2026](research/ai-agent-memory-landscape-2026.md) — landscape of AI agent memory approaches.
- [ai-agent-memory-papers-deep-dive](research/ai-agent-memory-papers-deep-dive.md) — deeper notes on AI agent memory papers.
- [lviv-ac-drain-shortlist-2026-06-01](research/lviv-ac-drain-shortlist-2026-06-01.md) — Lviv AC drain specialist shortlist.
- [ukraine-specialists](research/ukraine-specialists.md) — Ukraine specialists finder notes and contacts.
- [ukraine-specialists-strategy](research/ukraine-specialists-strategy.md) — strategy for finding local Ukrainian specialists.

## Memory Mirrors

- [memories/USER](memories/USER.md) — mirrored user-profile facts.
- [memories/MEMORY](memories/MEMORY.md) — mirrored agent memory facts.
