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
