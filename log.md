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

