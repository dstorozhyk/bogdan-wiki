# Денис: skill-gap analysis для $6k+ Senior → Tech Lead

> Статус: **чернетка на основі CV до поточного місця**. Не інтерпретувати «не вказано» як «не вміє».  
> База: CV Дениса, 2026-08-15; [[dou-current-raw-salaries-dotnet-analysis-2026-08]].

## Цільовий профіль і ринковий поріг

У актуальному DOU raw зрізі C#/.NET за червень 2026 Senior має медіану $4.5k, P75 $5.5k і P90 $7.0k; $6k+ мають 20.6% Senior. Для Tech Lead медіана $5.3k, P75 $6.55k, а $6k+ мають 41.2% вибірки.[13]

**Висновок:** $6k+ Senior — це не новий tech stack, а доведений рівень senior ownership. Tech Lead — наступний scope: не тільки робити систему, а систематично підвищувати capability команди й якість технічних рішень.

## Що вже є: сильний evidence

| Area | Доказ із CV | Оцінка для $6k Senior | Оцінка для Tech Lead |
|---|---|---|---|
| Backend / integrations | .NET, ASP.NET, SQL, Redis, RabbitMQ/Kafka, REST; банки, каси, чатботи | Сильна | Сильна база |
| Reliability / observability | ELK, Serilog, Prometheus, Grafana; міграція SSIS → ASP.NET для observability | Сильна | Сильна база |
| Delivery under ambiguity | 2 типи кас у 100+ локаціях за 6 тижнів; 30+ ETL міграцій; A/B infra 600k замовлень за 5 днів | Дуже сильна | Сильна |
| Business impact | 10–15 хв → 1 хв для звітів; 20+ год/міс ручної роботи прибрано; 85% tests на критичних процесах | Дуже сильна | Сильна |
| Data / AI leverage | Airflow, Python, ML experimentation, PhD, AI-agent enablement | Диференціатор | Диференціатор |
| Technical leadership | Повний цикл Tech Lead на Resource Management System; roadmap; навчання команди AI-практикам | Частково вже є | Є seed, треба формалізувати |
| Cross-boundary communication | Пряма комунікація з банками й зовнішніми vendors | Сильна | Сильна база |

## Найсильніша кар'єрна теза

Твій профіль уже не виглядає як «звичайний Senior .NET». Найрідкісніша комбінація: **enterprise/fintech integrations + observability + ETL/data + delivery з невизначених вимог + AI enablement**.

Це дає дві реалістичні позиції:

1. **$6k+ Senior Backend / Integration Engineer** — у product/fintech/enterprise середовищі, якщо CV й інтерв'ю чітко продають business-critical ownership.
2. **Tech Lead / Integration Platform Lead** — якщо ти регулярно ведеш technical decisions, планування, якість delivery та людей, а не лише маєш title в одному проєкті.

## Gaps: не «вмію / не вмію», а що поки не доведено

### G1 — Architecture evidence, що можна перевірити

**Що є:** архітектурні патерни, міграції, DevOps environment, масштабні системи.  
**Чого немає у CV:** 2–3 короткі decision cases формату *context → options → trade-offs → decision → metric/result*.

Для $6k Senior це важливіше за додатковий framework. Для Tech Lead це must-have: роботодавець купує не список технологій, а якість судження в умовах компромісів.

**Артефакти на 60 днів:**
- ADR про reliability/consistency в Kafka/RabbitMQ або data contract для банківської інтеграції;
- architecture one-pager про Resource Management System;
- один postmortem або risk register із запобіжними діями;
- прибрати confidential data, але залишити scale, альтернативи і виміряний результат.

### G2 — Cloud / platform depth

**Що є:** AWS і Azure services, Docker, CI/CD.  
**Не доведено:** IaC, cloud networking/IAM, Kubernetes або managed-platform operation, security boundaries, cost/availability trade-offs.

Це не означає, що потрібен Kubernetes certification. Gap треба закрити лише до рівня: **можеш спроєктувати, пояснити й безпечно експлуатувати production platform**, а не тільки деплоїти сервіс.

**Пріоритет:** високий для $7k+ Architect/Tech Lead; середній для першого $6k Senior offer.

### G3 — Explicit system-design interview fluency

**Що є:** реальні розподілені системи й high-load кейси.  
**Не доведено:** вміння за 45–60 хв структуровано провести interviewer-а через SLO, capacity, data model, failure modes, consistency, security, observability і rollout.

**Практика:** 6 design cases на базі власних проєктів: bank file exchange, ETL/Airflow, chatbot event flow, self-service checkout config, resource-management platform, AI-assisted internal workflow.

### G4 — People leadership operating system

**Що є:** Tech Lead delivery, roadmap, навчання команди, unblock зовнішніх integrations.  
**Не доведено:** регулярний цикл delegation → technical feedback → growth plan → expectation setting → conflict/risk management.

Для Tech Lead title потрібно не «керувати людьми», а зробити команду прогнозованішою та сильнішою.

**Артефакти/поведінки:**
- weekly technical planning і risk review;
- ownership map і явне делегування;
- якісні PR review standards;
- 1–2 people growth cases з конкретним підсумком;
- delivery metrics: lead time, escaped defects, predictability, incident rate.

### G5 — English + external executive communication

**Що є:** прямі комунікації з vendors.  
**Не вказано:** рівень англійської, англомовні architecture/discovery calls, письмові decision memos для non-technical stakeholders.

Для $6k+ це може бути реальним gate. Треба перевірити, не припускати.

**Ціль:** Upper-Intermediate+ у реальних робочих ситуаціях: 15-хв design walkthrough, status/risk update, technical negotiation.

### G6 — Комерційне позиціонування CV

**Що є:** зміст сильний.  
**Gap:** поточний headline «.NET Backend Developer» і список технологій продають тебе нижче фактичного scope.

Позиціонування для $6k Senior: **Senior Backend / Integration Engineer | .NET | Financial & enterprise systems | Event-driven reliability & observability**.

Позиціонування для Tech Lead: **Technical Lead | .NET & Integration Platforms | Delivery, reliability, data workflows and AI-enabled engineering**.

Не заявляти Architect/Staff до наявності повторюваного scope, але вже зараз продавати **результати, systems ownership і технічне лідерство**.

## Ранжування наступних кроків

| Пріоритет | Дія | Навіщо |
|---:|---|---|
| 1 | Зафіксувати 3 architecture cases та 5 quantified impact bullets | Відкриває Senior $6k interviews уже зараз |
| 2 | Перевірити English / interview delivery на реальних mock sessions | Може бути прихованим gate |
| 3 | Взяти на поточному місці ownership за один cross-team technical outcome | Створює доказ для Tech Lead, не лише title |
| 4 | Побудувати Team Lead operating system: planning, risk, reviews, delegation, mentoring | Перехід від сильного індивідуального виконання до leverage через команду |
| 5 | Поглибити cloud/platform architecture на конкретному production case | Піднімає стелю до Architect/Staff, не просто додає ключове слово |

## Дані, без яких фінальна персональна оцінка нечесна

CV не включає поточне місце/роль, англійську, фактичний розмір команди, частку часу на code vs leadership, наявність people management, compensation type та конкретні поточні outcomes.

Після додавання цього блоку треба:

1. оцінити кожен gap як **already strong / prove it / learn it / irrelevant**;
2. сформувати Senior-$6k CV/LinkedIn narrative;
3. сформувати Tech Lead promotion case і 90-day scoreboard.

## Sources

[13] https://github.com/devua/csv/tree/master/salaries
