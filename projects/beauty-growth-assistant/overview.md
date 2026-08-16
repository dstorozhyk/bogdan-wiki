---
title: Beauty Growth Assistant — project overview
created: 2026-08-16
updated: 2026-08-16
type: project
status: active
approval: user-directed
tags: [project, saas, beauty, typescript, validation]
sources:
  - "/opt/apps/beauty-growth-assistant/docs/beauty-crm-rebuild/00-master-workflow.md"
  - "/opt/apps/beauty-growth-assistant/docs/beauty-crm-rebuild/01-business-requirements.md"
  - "session:default/20260629_183841_50ab40de"
---

# Beauty Growth Assistant

Продуктовий напрям для українських solo beauty-майстрів: почати з mobile-first публічної візитівки та поступово додавати booking/CRM-модулі без втрати контролю майстром.

## Confirmed product direction

Поточний public-profile пріоритет:

1. identity майстра;
2. послуги й ціни;
3. слоти, лише якщо модуль підключений;
4. портфоліо;
5. відгуки / trust block;
6. локація і маршрут;
7. Instagram та прямий чат.

Базовий сценарій має працювати **без CRM**: клієнт переглядає роботи, ціни й адресу та пише майстру. QR, dashboard, analytics і внутрішня CRM не повинні перетворювати public page на mini-dashboard.

## Product principles confirmed by Denys

- Frontend Денис пише самостійно; не делегувати його Claude/Codex без окремого запиту.
- UI kit не перетворювати на landing page.
- Public profile — mobile-first персональна картка, а не generic SaaS landing.
- Автоматизацію вводити trust-first: заявка → ручне підтвердження, з опційними рівнями автоматизації.
- Для low-tech майстрів продавати outcome і контроль, а не слово “CRM”.

## Current artifact state

- Source root: `/opt/apps/beauty-growth-assistant`.
- Frontend base: React + TypeScript + Vite.
- Product-rebuild docs: `/opt/apps/beauty-growth-assistant/docs/beauty-crm-rebuild/`.
- Master workflow визначає послідовність: requirements → product design → architecture → backend → frontend → integration → QA → deploy.
- Business requirements документ існує, але source repository має незатрекані work-in-progress docs. Тому вони є сильним робочим джерелом, а не immutable approved specification.

## Source-of-truth boundaries

- Durable product intent and Denys corrections: [[product-requirements]].
- Current implementation/design details: source repository.
- Assistant-generated implementation plans залишаються drafts, доки Денис прямо не схвалить їх як plan.

## Related

- [[product-requirements]]
- [[manual-paid-pilot-workflow]]
- [[saas-payments-ukraine-validation-2026-06]]
