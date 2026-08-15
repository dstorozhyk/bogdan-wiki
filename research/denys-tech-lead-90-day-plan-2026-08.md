# Непогоджена чернетка: можливі кроки $6k+ Senior → Tech Lead

> Це **не план Дениса** і не домовленість про дії. Це лише research outline, сформований з ринкових даних і CV; використовувати його можна тільки після того, як Денис сам створить або підтвердить власний план.

> Пов'язано з: [[denys-6k-senior-to-tech-lead-gap-analysis-2026-08]].

## Рамка

Денис уже має неформальний end-to-end ownership фінансового B2B SaaS: .NET microservices, PostgreSQL, Wolverine, DDD, high-load, payment processing і AI-enabled development process. Ціль наступних 90 днів — **перетворити персональний ownership на повторюваний organizational leverage**.

## Дні 1–30: зробити ownership видимим і безпечним

### 1. Payment-processing technical brief

Створити 2–4 сторінки, які відповідають:

- які bounded contexts і data ownership;
- які гроші/статуси/side effects не можна задублювати;
- idempotency key, retry policy, outbox/inbox, poison messages;
- reconciliation і audit trail;
- SLO, dashboard, alerts, rollback/recovery.

**Outcome:** system design case для $6k Senior interview та спільна база для команди.

### 2. Service maturity baseline

Для кожного мікросервісу: owner, dependencies, API/events, database ownership, tests, dashboard, runbook, known risks, deployment/rollback.

**Outcome:** не «я знаю весь проєкт», а команда може бачити та обговорювати систему.

### 3. AI development process як engineering system

Зафіксувати правила: де AI можна застосовувати, як перевіряти output, що не можна відправляти в model context, required tests/review, які артефакти автоматично генеруються.

**Outcome:** безпечний process, який хтось інший зможе повторити.

## Дні 31–60: створити leverage через команду

### 4. Щотижневий technical planning / risk review

30 хвилин, структура:

- delivery objective;
- ризики/залежності;
- architecture decision потрібні цього тижня;
- хто owner;
- метрика success/rollback.

Не потрібно командувати людьми: це сервіс ясності, який підвищує predictability.

### 5. Delegation-by-design

Вибрати один bounded, але нетривіальний шматок: новий event consumer, reporting flow, observability improvement або payment-adjacent service. Підготувати design constraints, acceptance criteria та review plan; не писати все самому.

**Outcome:** доказ, що ти підвищуєш output команди, а не лише власну швидкість.

### 6. Engineering standards

Запропонувати короткі стандарти для:

- event contracts/versioning;
- idempotency/retry/error handling;
- logs/metrics/traces;
- PR checklist для критичних payment changes;
- ADR format.

**Outcome:** 1–2 стандарти реально використовуються, а не лежать у Confluence.

## Дні 61–90: конвертація в formal Tech Lead case

### 7. Quarterly technical roadmap

На 1 сторінку: quality/reliability debt, delivery enablers, risk reduction, platform opportunities, estimates and trade-offs. Прив'язати кожен пункт до грошей, ризику, часу delivery або customer impact.

### 8. Manager conversation

Не просити title абстрактно. Питання:

> «Я вже відповідаю за весь technical outcome проєкту. Хочу формалізувати Tech Lead scope. Які 3–5 observable behaviors і результати потрібні тут, щоб через 6–8 тижнів оцінити готовність?»

Домовитися про письмовий scorecard і дату review.

### 9. External-market readiness

Підготувати:

- 3 architecture stories;
- 5 quantified impact bullets;
- 1 leadership story про AI process;
- 1 incident/failure/recovery story;
- CV headline та LinkedIn positioning під Senior Backend/Integration або Technical Lead.

## Reading cadence: підсилити практику, а не відкласти її

Цю непогоджену чернетку можна, за бажання Дениса, розглянути паралельно з короткою послідовністю читання — одна книга на 3–4 тижні, але кожна має породити конкретний робочий експеримент:

1. **High Output Management** (дні 1–21): застосувати до service maturity baseline, weekly risk review і делегування. Питання: *де я є bottleneck і який процес збільшить output команди?*
2. **The Staff Engineer’s Path** (дні 22–42): застосувати до architecture brief, standards і cross-team trust. Питання: *який вплив я можу створити без формальної влади?*
3. **Good Strategy/Bad Strategy** (дні 43–63): застосувати до quarterly technical roadmap. Питання: *який реальний діагноз payment/platform проблеми, а не перелік бажань?*
4. **Thinking in Bets** (дні 64–90): застосувати до risk register, rollout/rollback і decision reviews. Питання: *чи було рішення хорошим до того, як став відомий результат?*

Не робити «книжковий план» окремим хобі: після кожної книги — один короткий memo, одна перевірена гіпотеза та одна зміна робочого процесу. Це прямо накопичує evidence для Tech Lead case.

## Success scoreboard

| Напрям | Minimum evidence |
|---|---|
| Technical ownership | Payment/system design + current risk register + service map |
| Reliability | 1 production SLO/dashboard/runbook, baseline і результат |
| Team leverage | 1 delegated delivery або mentoring case, який закінчився результатом |
| Standards | 1–2 прийняті engineering practices |
| Stakeholder influence | Регулярний risk/status update + roadmap decision |
| Career | Written Tech Lead criteria або 3+ сильні зовнішні interview conversations |
