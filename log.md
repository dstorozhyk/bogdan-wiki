# Wiki Log

Chronological record of all wiki actions. Append-only.
Format: `## [YYYY-MM-DD] action | subject`
Actions: ingest, update, query, lint, create, archive, delete

## [2026-05-29] create | Wiki initialized
- Domain: General knowledge base (AI/ML, .NET, infrastructure, tools, people, learning)
- Structure: SCHEMA.md, index.md, log.md, raw/, entities/, concepts/, comparisons/, queries/
- Ready for first ingest

## [2026-06-01] create | concepts/hermes-codex-oauth-quota-exhaustion
- Чому openai-codex (ChatGPT OAuth) застрягає в `exhausted` після транзитного 429 на свіжій підписці
- OpenAI нав'язує місячний reset_at, Hermes його поважає → circuit-breaker до кінця місяця
- Лікування: `hermes auth reset openai-codex`; запобігання: справні fallback-провайдери
- Спостережено на акаунті Denys (ChatGPT Plus), reset був до 2026-06-30

## [2026-06-10] create | SaaS payments/invoice validation research
- Створено decomposed wiki set замість одного монолітного note:
  - research/saas-payments-ukraine-validation-2026-06.md
  - research/payoneer-invoice-payment-request-ukraine-saas.md
  - research/saas-invoice-service-shortlist-ukraine.md
  - research/manual-paid-pilot-workflow.md
  - concepts/wiki-decomposition-workflow.md
- Оновлено index.md і SCHEMA.md tag taxonomy для `saas`, `payments`, `invoicing`, `validation`, `workflow`, `wiki`.

## [2026-06-14] update | Freedom24 funding and WhiteBIT/Binance USDT routes
- Створено research/whitebit-binance-usdt-staking-route-2026-06.md з правилом: WhiteBIT direct якщо effective < ~44.78 UAH/USDT, інакше Binance P2P → WhiteBIT.
- Оновлено research/freedom24-ukraine-funding-2026-06.md: Wise не підходить як on-ramp, ZEN заблокував Denys через Україну, Genome/SEPA лишається основним fallback; crypto тільки якщо Freedom24 має офіційний USDT deposit.
- Оновлено index.md.

## [2026-06-14] update | Genome status correction
- Уточнено research/freedom24-ukraine-funding-2026-06.md: Genome не блокував Denys; проблема — близько 20 EUR/USD місячної підписки для України/non-EEA.
- Оновлено index.md summary.

## [2026-06-20] create | Agent knowledge sleep policy and review queue
- Створено agents/knowledge-policy.md з правилами маршрутизації durable knowledge між memory, skills, wiki і session DB.
- Створено agents/review-queue.md як safe-mode staging queue для nightly consolidation.
- Створено logs/daily/ для щоденних digest-файлів.
- Оновлено index.md.

## [2026-06-20] create | daily-knowledge-consolidation-safe cron
- Створено Hermes cron job `1773cf46a5ec` з розкладом `30 3 * * *` UTC.
- Режим: SAFE MODE — пише daily digest і review queue у wiki, не змінює memory/skills автоматично.
- Delivery: origin Telegram chat.

## [2026-06-20] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-06-20.md.
- Added 0 memory candidates, 2 skill candidates, 2 wiki candidates, 5 open loops to agents/review-queue.md.

## [2026-06-21] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-06-21.md.
- Added 0 memory candidates, 1 skill candidates, 1 wiki candidates, 3 open loops to agents/review-queue.md.

## [2026-06-22] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-06-22.md.
- Added 0 memory candidates, 1 skill candidates, 2 wiki candidates, 4 open loops to agents/review-queue.md.
- Updated index.md with three newly discovered research notes from Jun 21 work.

## [2026-06-23] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-06-23.md.
- Added 1 memory candidates, 2 skill candidates, 4 wiki candidates, 4 open loops to agents/review-queue.md.
- `index.md` already mentioned `logs/daily/`; no index change needed.

## [2026-06-24] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-06-24.md.
- Added 1 memory candidates, 2 skill candidates, 3 wiki candidates, 3 open loops to agents/review-queue.md.
- `index.md` already mentioned `logs/daily/`; no index change needed.

## [2026-06-25] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-06-25.md.
- Added 1 memory candidates, 2 skill candidates, 3 wiki candidates, 3 open loops to agents/review-queue.md.
- `index.md` already mentioned `logs/daily/`; no index change needed.

## [2026-06-26] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-06-26.md.
- Added 0 memory candidates, 1 skill candidates, 1 wiki candidates, 3 open loops to agents/review-queue.md.
- `index.md` already mentioned `logs/daily/`; no index change needed.

## [2026-06-27] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-06-27.md.
- Added 0 memory candidates, 0 skill candidates, 1 wiki candidates, 2 open loops to agents/review-queue.md.
- Marked Rocket update announcement delivery open loop as resolved after 21/21 successful sends.
- `index.md` already mentioned `logs/daily/`; no index change needed.

## [2026-06-28] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-06-28.md.
- Added 0 memory candidates, 0 skill candidates, 0 wiki candidates, 1 open loops to agents/review-queue.md.
- `index.md` already mentioned `logs/daily/`; no index change needed.

## [2026-06-29] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-06-29.md.
- Added 0 memory candidates, 1 skill candidates, 0 wiki candidates, 1 open loops to agents/review-queue.md.
- `index.md` already mentioned `logs/daily/`; no index change needed.

## [2026-06-29] create | beauty masters SaaS requirements
- Створено research/beauty-masters-saas-ukraine-requirements-2026-06-29.md.
- Зафіксовано вимоги, MVP scope, competitor/source signals, trust-first automation model і objection handling для українських beauty-майстрів.
- Оновлено index.md.

## [2026-06-29] update | beauty masters SaaS upsell assistant
- Додано до research/beauty-masters-saas-ukraine-requirements-2026-06-29.md killer feature candidate: contextual upsell assistant.
- Зафіксовано add-on catalog, rules/templates MVP, client-side add-on choice, master approval, trust controls, ROI dashboard і validation experiment.

## [2026-06-29] update | beauty masters SaaS low-tech QR + analytics wedge
- Додано field signal: майстер готова платити навіть за QR-код на Instagram і Google Maps, що вказує на низьку технічну обізнаність і високу цінність простих digitization кроків.
- Додано концепцію low-tech revenue OS: QR mini-site → booking request → reminders/no-show → upsell assistant → money-hints analytics → CRM.
- Зафіксовано, що analytics має подаватись як прості money hints, а не BI dashboards.

## [2026-06-29] update | beauty masters SaaS QR as module, not separate product
- Уточнено product decision: QR/mini-site не варто виносити в окремий продукт; це має бути легка вбудована acquisition/onboarding фіча загальної системи.
- Core product лишається beauty revenue assistant: booking, reminders, upsells, repeat visits, money-hints analytics.

## [2026-06-29] update | beauty SaaS pricing and configuration model
- Уточнено: не продавати як “CRM”; продавати outcome — менше головного болю + більше грошей через записи, нагадування, допродажі, повторні візити і money hints.
- Зафіксовано, що QR/mini-site не тягне 1500–2000+ грн/міс сам по собі; premium plan має включати done-for-you/guided setup і ongoing growth assistant loop.
- Додано pricing hypothesis: Starter/QR 0–499 грн, Solo Growth 1500–2000 грн/міс, Studio Growth 2500–5000+ грн/міс.

## [2026-06-30] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-06-30.md.
- Added 3 memory candidates, 0 skill candidates, 3 wiki candidates, 5 open loops to agents/review-queue.md.
- `index.md` already mentioned `logs/daily/`; no index change needed.

## [2026-06-30] update | beauty public profile standalone-first
- Оновлено research/beauty-masters-saas-ukraine-requirements-2026-06-29.md.
- Зафіксовано правило: public-візитівка має працювати без CRM; CRM/calendar/free-slots/reminders/client-history — optional modules.
- Додано baseline без CRM, optional module table, design direction і theme rule: замість темної black/gold теми використовувати світлі premium напрями, зокрема Champagne Ivory.
- Оновлено index.md.

## [2026-07-01] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-07-01.md.
- Added 3 memory candidates, 3 skill candidates, 3 wiki candidates, 4 open loops to agents/review-queue.md.
- `index.md` already mentioned `logs/daily/`; no index change needed.


## [2026-07-01] ingest | Emergency Fund strategy documents
- Імпортовано 4 надані Denys Obsidian-документи у wiki:
  - research/emergency-fund-dashboard.md
  - research/emergency-fund-strategy.md
  - research/emergency-fund-ovdp-research.md
  - research/emergency-fund-usdt-usdc-research.md
- Зафіксовано source of truth для подушки: цілі $6k/$12k/$18k, повна ціль $18k, структура Р1/Р2/Р3, OВДП/UCITS/stablecoin розподіл і квартальний ребаланс.
- Оновлено index.md.

## [2026-07-02] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-07-02.md.
- Added 1 memory candidates, 1 skill candidates, 2 wiki candidates, 3 open loops to agents/review-queue.md.
- `index.md` already mentioned `logs/daily/`; no index change needed.

## [2026-07-03] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-07-03.md.
- Added 2 memory candidates, 2 skill candidates, 3 wiki candidates, 3 open loops to agents/review-queue.md.
- Updated index.md with the AI-assisted SDLC/vibe-coding lifecycle research note and refreshed counts.
## [2026-07-03] update | Sleep job memory compaction and skill usage tracking
- Updated `agents/knowledge-policy.md` with the >80% memory compaction exception and skill usage review rules.
- Created `agents/skill-usage.md` to track `/root/.hermes/skills/.usage.json` plus `hermes curator status`.
- Updated `index.md` to include the skill usage note.
- Updated cron job `1773cf46a5ec` to enable memory-aware compaction and skill-usage reporting.

## [2026-07-04] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-07-04.md.
- Memory pressure: MEMORY 2129→2129, USER 1294→1294; compaction proposed only because the memory tool was unavailable in this cron run.
- Skill usage: updated agents/skill-usage.md; added 3 skill-review candidates.
- Added 3 memory candidates, 3 skill candidates, 3 wiki candidates, 5 open loops to agents/review-queue.md.

## [2026-07-05] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-07-05.md.
- Memory pressure: MEMORY 2129→2129, USER 1294→1294; compaction proposed only because the memory tool was unavailable in this cron run.
- Skill usage: updated agents/skill-usage.md; added 1 skill-review candidate.
- Added 2 memory candidates, 1 skill candidate, 1 wiki candidate, 2 open loops to agents/review-queue.md.

## [2026-07-06] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-07-06.md.
- Memory pressure: MEMORY 2194→2194, USER 1294→1294; compaction proposed only because the memory tool was unavailable in this cron run.
- Skill usage: updated agents/skill-usage.md; added 2 skill-review candidates.
- Added 3 memory candidates, 2 skill candidates, 3 wiki candidates, 4 open loops to agents/review-queue.md.

## [2026-07-07] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-07-07.md.
- Memory pressure: MEMORY 2024→2024, USER 1294→1294; compaction proposed only because the memory tool was unavailable in this cron run.
- Skill usage: updated agents/skill-usage.md; added 2 skill-review candidates.
- Added 2 memory candidates, 2 skill candidates, 1 wiki candidates, 3 open loops to agents/review-queue.md.

## [2026-07-08] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-07-08.md.
- Memory pressure: MEMORY 2024→2024, USER 1368→1368; compaction proposed only because the memory tool was unavailable in this cron run.
- Skill usage: updated agents/skill-usage.md; added 2 skill-review candidates.
- Added 2 memory candidates, 2 skill candidates, 1 wiki candidates, 4 open loops to agents/review-queue.md.

## [2026-07-09] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-07-09.md.
- Memory pressure: MEMORY 2024→2024, USER 1368→1368; compaction proposed only because the memory tool was unavailable in this cron run.
- Skill usage: updated agents/skill-usage.md; added 2 skill-review candidates.
- Added 3 memory candidates, 2 skill candidates, 1 wiki candidates, 3 open loops to agents/review-queue.md.

## [2026-07-10] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-07-10.md.
- Memory pressure: MEMORY 2024→2024, USER 1358→1358; compaction proposed only because the memory tool was unavailable in this cron run.
- Skill usage: updated agents/skill-usage.md; added 2 skill-review candidates.
- Added 2 memory candidates, 2 skill candidates, 1 wiki candidates, 2 open loops to agents/review-queue.md.

## [2026-07-11] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-07-11.md.
- Memory pressure: MEMORY 2024→2024, USER 1358→1358; compaction proposed only because the memory tool was unavailable in this cron run.
- Skill usage: updated agents/skill-usage.md; added 4 skill-review candidates.
- Added 3 memory candidates, 4 skill candidates, 2 wiki candidates, 4 open loops to agents/review-queue.md.

## [2026-07-12] update | Daily knowledge consolidation
- Created/updated logs/daily/2026-07-12.md.
- Memory pressure: MEMORY 2024→2024, USER 1358→1358; compaction proposed only because the memory tool was unavailable in this cron run.
- Skill usage: updated agents/skill-usage.md; added 1 skill-review candidate.
- Skill automation: created 0 draft skills, patched 0 skills, queued 1 candidate, rejected 1 candidate.
- Added 2 memory candidates, 1 skill candidate, 1 wiki candidate, 2 open loops to agents/review-queue.md.

## [2026-07-12] create | Enterprise AI team vision / Tech Lead meeting preparation
- Created `research/enterprise-ai-team-vision-tech-lead-meeting-prep-2026-07-12.md`.
- Captured a practical enterprise AI thesis, controlled pilot model, AI-assisted SDLC guardrails, 90-day plan, targeted questions, and Tech Lead positioning for Denys’s internal meeting.
- Updated `index.md`.

## [2026-07-13] update | Daily knowledge consolidation
- Created `logs/daily/2026-07-13.md`.
- Memory pressure: MEMORY `2024→2024 / 2200`; USER `1358→1358 / 1375`; compaction proposed only because the memory tool is unavailable.
- Skill usage: updated `agents/skill-usage.md`; 113 tracked, 59 zero-use, 57 never-active; no skill-review candidate added.
- Skill automation: created 0 draft skills, patched 0 skills, queued 0 candidates, rejected 2 one-off/non-procedural candidates.
- Added 1 memory-compaction candidate and 2 open loops to `agents/review-queue.md`.
- Created `research/small-creator-brand-deals-{playbook,pricing}-2026-07-12.md`; updated `index.md`.

## [2026-07-14] update | Daily knowledge consolidation
- Created/updated `logs/daily/2026-07-14.md`.
- Memory pressure: MEMORY `2024→2024 / 2200`, USER `1358→1358 / 1375`; compaction proposed only because the `memory` tool is unavailable.
- Skill usage: updated `agents/skill-usage.md`; 113 tracked, 59 zero-use, 57 never-active; added 1 skill-review candidate.
- Skill automation: created 0 draft skills, patched 0 skills, queued 1 candidate, rejected 1 candidate.
- Added 1 memory candidate, 1 skill candidate, 0 wiki candidates, and 2 open loops to `agents/review-queue.md`.
