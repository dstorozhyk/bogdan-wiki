---
title: Hermes — заморозка OpenAI Codex (ChatGPT OAuth) після 429
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [debugging, guide, cli]
confidence: high
---

# Hermes — заморозка OpenAI Codex (ChatGPT OAuth) після 429

Як працює circuit-breaker облікових даних у Hermes для провайдера `openai-codex`
(вхід через підписку ChatGPT, `auth_mode = chatgpt`), чому свіжа підписка може
одразу «не працювати» і як це лікувати. Спостережено 2026-06-01 на акаунті Denys
(план ChatGPT **Plus**).

## Симптом

- Куплено/оновлено підписку ChatGPT, ліміти «фулові», але Hermes не використовує Codex.
- В `~/.hermes/auth.json` по `credential_pool.openai-codex[0]`:
  - `last_status = exhausted`
  - `last_error_code = 429`, `last_error_message = "quota exceeded"`
  - `last_error_reset_at` — аж до **кінця місяця** (місячне вікно квоти Plus).
- Авторизація при цьому **валідна**: JWT access_token містить `chatgpt_plan_type: "plus"`
  і правильний `chatgpt_account_id`. Проблема не в токені.

## Корінь проблеми

1. У JWT `iat` (видача токена) і `last_error_at` відрізнялись лише на **~9 хвилин** —
   удар по Codex стався одразу після логіну, поки **свіжа підписка ще провізіонилась**
   на боці OpenAI. Бекенд повернув 429 з місячним `reset_at`.
2. Hermes ([[credential-pool]]) поважає **provider-supplied `reset_at`**: за замовчуванням
   429 = заморозка на 1 годину (`EXHAUSTED_TTL_429_SECONDS = 3600`), але якщо OpenAI
   передав власний `reset_at`, він **перекриває дефолт**. Тому креденшел застряг до кінця місяця.
3. Circuit-breaker після цього **навіть не пробує** провайдер до `reset_at` — навіть якщо
   квота вже стала доступною. Звідси «не працює взагалі», хоча реальної вичерпаної квоти вже немає.

> Це **не баг Hermes** і **не помилка авторизації** — місячне вікно нав'язав OpenAI,
> а Hermes його чесно дотримався. Спусковий гачок (удар по неактивованій підписці) — разовий.

## Лікування

Скинути статус exhaustion штатною командою (очищає `last_status` / `last_error_*` /
`last_error_reset_at` для всіх креденшелів провайдера):

```bash
hermes auth reset openai-codex
```

Те саме робить повторний логін — re-auth теж обнуляє `last_error_reset_at`:

```bash
hermes auth logout openai-codex   # потім device-code логін заново
```

Перевірити стан: `hermes auth status openai-codex`.

## Як не допустити повторення

- **Тривалість заморозки диктує OpenAI** — конфіга/env, щоб урізати нав'язане `reset_at`,
  у коді немає. Тому стратегія — не боротись із заморозкою, а мати робочий обхід.
- **Тримати справні fallback-провайдери** ([[hermes-fallback-providers]]). У Denys налаштовано
  й усі `last_status = ok`: `copilot → copilot/gpt-4.1 → gemini-2.5-flash → openrouter/deepseek`.
  Заморожений Codex тоді не валить агента — той перемикається на резерв.
- **Не автоматизувати періодичний `auth reset` по крону** — для *справжнього* ліміту заморозка
  корисна; автоскид просто молотитиме 429 і знищить сенс circuit-breaker'а. Скидати лише вручну,
  коли точно відомо, що квота вже є.
- Окремо: ChatGPT-Codex квота (`auth_mode = chatgpt`) — це **окремий бакет від OpenAI API-кредитів**.
  «Фулові ліміти» на API не зараховуються в Codex-через-підписку.

## Ключові файли / точки в коді

- `~/.hermes/auth.json` — `credential_pool.openai-codex[*]` (`last_status`, `last_error_reset_at`).
- `agent/credential_pool.py` — `EXHAUSTED_TTL_429_SECONDS`, `_normalize_error_context()` (парсинг
  `reset_at`/`retry_after`), `_exhausted_until()`, `mark_exhausted_and_rotate()`.
- `hermes_cli/auth_commands.py` — `auth_reset_command()` (`hermes auth reset <provider>`).

## Пов'язане

- [[credential-pool]]
- [[hermes-fallback-providers]]
