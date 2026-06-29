# SaaS для beauty-майстрів України — вимоги, MVP і заперечення щодо автоматизації

> Date: 2026-06-29  
> Tags: `saas`, `ukraine`, `beauty`, `requirements`, `mvp`, `automation`, `objection-handling`, `crm`  
> Status: synthesis / product discovery note  
> Related: [[manual-paid-pilot-workflow]], [[saas-payments-ukraine-validation-2026-06]]

## TL;DR

Для українського beauty-сегменту краще продавати не “повну автоматизацію”, а **контрольований порядок у записах**:

> **Онлайн-запис без втрати контролю.**  
> Клієнти залишають заявки, система нагадує й веде історію, а майстер сам вирішує, що підтверджувати.

Головна продуктова відповідь на недовіру до автоматизації: **режим “заявка → ручне підтвердження”** + поступові рівні автоматизації:

1. **Асистент** — система збирає заявки, майстер усе підтверджує.
2. **Напівавтомат** — постійні клієнти можуть записуватись автоматично, нові — через підтвердження.
3. **Автопілот** — система сама підтверджує записи за правилами.

Перший MVP варто робити для **solo beauty-майстрів**: манікюр, брови/вії, косметологія, масаж, депіляція, PMU, перукарі/барбери.

---

## Source signals

| Джерело | Сигнал | Що це означає для продукту |
|---|---|---|
| [EasyWeek — програма для салону краси](https://easyweek.com.ua/business/solutions/beauty-salon) | Онлайн-запис 24/7, SMS-нагадування, історія клієнтів, фінансовий облік, розклад майстрів | Це базові очікування ринку: календар, запис, нагадування, CRM |
| [EasyWeek — рішення для індустрії краси](https://easyweek.com.ua/business/solutions/category/beauty) | No-show protection, форми, сайт/віджет, лояльність, сертифікати, абонементи | Попит не тільки на запис, а й на повторні продажі, захист від неявок, маркетинг |
| [Altegio Ukraine — beauty](https://alteg.io/uk/beauty/) | Онлайн-запис, CRM, сповіщення, фінанси, аналітика, зарплати, склад | Для салонів потрібні складні ERP/CRM функції, але для solo-майстра це може бути overkill |
| [Altegio — online booking](https://alteg.io/uk/online-booking/) | Запис через сайт, мобільний додаток, месенджери, соцмережі; планування/перенесення/скасування | Канали соцмереж і месенджерів критичні для України |
| [DIKIDI](https://dikidi.net/en) | Online booking platform, automation and promotion in service sector | Каталог/маркетплейс може бути каналом залучення, але не варто починати MVP з marketplace |
| [Booksy Biz](https://booksy.com/biz/en-us/) | Booking, reminders, marketing, payments, marketplace, no-show protection | Глобальний патерн: “stay booked without back-and-forth” + no-show protection |

---

## Target segments

### 1. Solo-майстер

Приклади: майстер манікюру, бровіст, lashmaker, косметолог, масажист, депіляція, PMU.

**Потреби:**

- не забувати записи;
- не відповідати багато разів на “коли є вільне?”;
- зменшити неявки;
- мати базу клієнтів;
- бачити, хто давно не приходив;
- не втрачати клієнтів з Instagram/Telegram/Viber;
- не користуватись складною CRM.

**Головний страх:**

> “Я не хочу, щоб клієнти самі лізли в мій графік і записувались як попало.”

### 2. Міні-студія 2–7 майстрів

**Потреби:**

- розклад по майстрах;
- власник/адміністратор бачить завантаження;
- різні послуги, ціни, тривалість;
- контроль скасувань;
- клієнтська база;
- фінансова статистика;
- зарплата/відсоток майстрів;
- стандартизовані повідомлення.

**Головний страх:**

> “Якщо автоматизація помилиться, буде хаос у розкладі й конфлікти з клієнтами.”

### 3. Салон / мережа

Не пріоритет для першого MVP: потрібні ролі, каса, склад, зарплати, складні права, інтеграції.

---

## As-is flow → pains → feature opportunities

| Етап | Як зараз часто відбувається | Біль / ризик | SaaS opportunity |
|---|---|---|---|
| Клієнт питає вільний час | Instagram / Telegram / Viber | Довгі переписки, майстер відволікається | Посилання на вільні слоти |
| Уточнення послуги | Вручну в чаті | Клієнт може вибрати не ту послугу | Форма запису з питаннями |
| Підтвердження запису | Вручну | Можна забути внести в календар | Режим “заявка → підтвердити” |
| Нагадування | Вручну або ніяк | Неявки / запізнення | Автоматичні або напівавтоматичні нагадування |
| Перенесення / скасування | Переписка | Хаос у графіку | Кнопки “перенести / скасувати” з правилами |
| Історія клієнта | У голові / нотатках | Забуваються матеріали, алергії, побажання | Картка клієнта |
| Повторний запис | Клієнт сам має згадати | Втрата повторних продажів | М’які follow-up повідомлення |
| Облік доходу | Нотатки / таблиця / нічого | Немає розуміння прибутку | Простий фінансовий звіт |

---

## Sellable MVP scope

### Paid promise

> За 10 хвилин майстер отримує сторінку запису, календар, клієнтську базу і нагадування — але жоден запис не підтверджується без дозволу майстра.

### Build now

- реєстрація майстра;
- профіль/сторінка майстра;
- список послуг;
- календар;
- ручне створення запису;
- онлайн-посилання для клієнта;
- заявка на запис;
- підтвердити / відхилити / запропонувати інший час;
- картка клієнта;
- базові нагадування;
- статуси записів;
- простий звіт за період;
- журнал змін;
- шаблони повідомлень.

### Fake/manual now

| Функція | MVP fallback |
|---|---|
| Viber / Instagram інтеграції | копіювання тексту + кнопка “відкрити чат” |
| Передоплата | ручна інструкція “скиньте на карту” |
| AI-відповіді клієнтам | шаблони відповідей |
| CRM-маркетинг | список “клієнти, які давно не були” |
| Аналітика прибутковості | базовий дохід і кількість записів |

### Later

- Telegram Bot / Viber інтеграції;
- онлайн-оплата;
- депозити;
- Instagram DM;
- маркетингові кампанії;
- абонементи;
- сертифікати;
- склад;
- зарплати;
- мультифіліальність;
- marketplace.

---

## Feature backlog

| Priority | Feature | Why needed | MVP |
|---|---|---|---|
| P0 | Календар записів | Основний робочий інструмент | Yes |
| P0 | Ручне створення запису | Швидко внести клієнта з чату | Yes |
| P0 | Послуги з тривалістю/ціною | Без цього неможливий запис | Yes |
| P0 | Онлайн-форма запису | Зменшує переписки | Yes |
| P0 | Режим “заявка на підтвердження” | Знімає страх перед автоматизацією | Yes |
| P0 | Картка клієнта | Цінність навіть без автозапису | Yes |
| P0 | Нагадування клієнту | Зменшує no-show | Yes |
| P1 | Telegram/Viber повідомлення | Канали релевантні Україні | Partial/Yes |
| P1 | Шаблони повідомлень | Майстер контролює tone of voice | Yes |
| P1 | Журнал змін | Підвищує довіру | Yes |
| P1 | Статуси запису | Контроль процесу | Yes |
| P1 | No-show tracking | Показує втрати | Yes |
| P1 | Повторний запис / follow-up | Ріст доходу | Later |
| P2 | Передоплата | Захист від неявок | Later |
| P2 | Програма лояльності | Retention | Later |
| P2 | Фінансовий звіт | ROI для майстра | Basic in MVP |
| P3 | Склад / матеріали | Для салонів, не solo MVP | No |
| P3 | Зарплати майстрів | Для салонів | No |
| P3 | Marketplace | Складно, інша бізнес-модель | No |

---

## Product requirements

### Calendar

**User story:**  
Як майстер, я хочу бачити всі записи на день, щоб не тримати графік у голові.

**Acceptance criteria:**

- майстер бачить записи на сьогодні;
- може додати запис за ≤30 секунд;
- система попереджає про конфлікт часу;
- можна змінити статус запису;
- можна перенести запис;
- можна додати нотатку.

### Online booking with confirmation

**User story:**  
Як майстер, я хочу отримувати заявки на запис, але підтверджувати їх вручну, щоб не втратити контроль.

**Acceptance criteria:**

- клієнт обирає послугу, дату, час;
- заявка не стає автоматично підтвердженим записом;
- майстер отримує notification;
- майстер може підтвердити, відхилити, запропонувати інший час або написати клієнту;
- клієнт отримує відповідь.

### Message control

**User story:**  
Як майстер, я хочу бачити, що система напише клієнту, щоб не виглядати бездушно або непрофесійно.

**Acceptance criteria:**

- всі шаблони можна редагувати;
- є preview повідомлення;
- можна вимкнути автоматичну відправку;
- можна включити “питати перед відправкою”;
- є історія відправлених повідомлень.

### New vs returning clients

**User story:**  
Як майстер, я хочу дозволити постійним клієнтам записуватись автоматично, а нових перевіряти вручну.

**Acceptance criteria:**

- клієнт має статус: новий / постійний / VIP / проблемний;
- для кожної групи можна налаштувати правила запису;
- нові клієнти можуть вимагати ручного підтвердження;
- проблемні клієнти можуть вимагати передоплату.

---

## Objection handling: “Я не довіряю автоматизації”

### Core answer

> Вам не треба довіряти автоматизації одразу. Спочатку вона працює як секретар: збирає заявки, нагадує, показує конфлікти, але нічого не підтверджує без вас.

### Longer answer

> Так і має бути. У beauty-сфері багато нюансів: складність процедури, стан клієнта, час на підготовку, попередній досвід. Тому в продукті є режим ручного підтвердження. Клієнт не просто займає ваш час — він залишає заявку, а ви вирішуєте: підтвердити, запропонувати інший час або уточнити деталі.

### Objection matrix

| Заперечення | Відповідь |
|---|---|
| “Я боюся, що система зробить помилку” | На старті система не приймає рішень. Вона тільки показує заявки й попереджає про конфлікти. |
| “Мені треба бачити кожного клієнта” | Нових клієнтів можна поставити тільки на ручне підтвердження. Автозапис — лише для постійних. |
| “Я краще сама напишу клієнту” | Можна. Система підготує текст, а ви натиснете “надіслати”, коли перевірите. |
| “Я не хочу втрачати особисте спілкування” | Ви не втрачаєте спілкування. Просто клієнт одразу бачить вільні години, а ви не відповідаєте на одне й те саме 10 разів. |
| “У мене все в Instagram, мені CRM не треба” | Це не заміна Instagram. Це порядок після того, як клієнт написав: запис, нагадування, історія, повторний візит. |
| “Я не хочу, щоб клієнти бачили весь мій графік” | Вони бачать тільки ті слоти, які ви дозволили показувати. |
| “А якщо мені треба більше часу на конкретного клієнта?” | Можна додати буфери, приховані слоти або підтверджувати складні послуги вручну. |
| “Я не хочу автоматичні повідомлення” | Можна включити режим: система готує повідомлення, але відправляєте тільки ви. |

---

## Positioning

Bad:

> Повністю автоматизуйте свій beauty-бізнес.

Better:

> **Порядок у записах без втрати контролю.**

Alternatives:

- **Ваш beauty-асистент: клієнти записуються легше, а ви підтверджуєте важливе.**
- **Менше переписок. Менше неявок. Усе під вашим контролем.**
- **Онлайн-запис без втрати контролю.**

---

## Killer feature candidate: low-tech revenue OS

New field signal from Denys: a beauty master was ready to pay even for a simple QR code that links to Instagram and Google Maps. This implies the average target user can have **very low technical maturity**, while even small digitization steps can create visible revenue lift. The product should not start as a complex CRM; it should feel like a low-tech revenue layer that begins with QR/links and gradually grows into booking, upsells, reminders, and analytics.

Core wedge:

> **Start with the general beauty system, but make QR/mini-page a lightweight built-in acquisition feature, not a separate product. Then use analytics to show where money is being lost and what simple action increases revenue.**

Important product decision: **do not spin QR into a separate product**. It is too simple and strategically better as an entry/onboarding module inside the overall system. It should be the first “aha” moment and acquisition surface, while the core product remains the broader beauty revenue assistant: booking, reminders, upsells, repeat visits, and money-hints analytics.

This reframes the SaaS from “software to manage a salon” into “a simple tool that makes the master easier to find, easier to book, and easier to buy more from.”

### Entry-level product: QR mini-site

The QR/mini-site should be a **module of the general system**, not a standalone product. It is the easiest entry point for low-tech masters and should be included in onboarding, plan packaging, and printed materials.

The first sellable unit can be extremely simple:

- QR code for studio/workplace;
- mobile mini-page with:
  - Instagram;
  - Google Maps;
  - phone / Telegram / Viber;
  - services and prices;
  - “book appointment” button;
  - reviews/photos;
  - add-ons or promos;
- printable QR assets for mirror/table/door/business card;
- basic click tracking.

Why this matters:

- requires almost no technical learning;
- is easy to explain in-person;
- creates immediate perceived value;
- can become the acquisition wedge for later CRM features.

### Analytics as killer feature

Analytics should not look like BI dashboards. For low-tech beauty masters, it should be phrased as **money hints**:

> “Ось де ви втрачаєте гроші. Ось що зробити цього тижня.”

Examples:

| Insight | Plain-language message | Suggested action |
|---|---|---|
| Many profile clicks, few bookings | “Люди дивляться, але не записуються” | add visible booking button / price / reviews |
| Clients choose service but abandon | “На цьому етапі клієнти губляться” | shorten form / add manual confirmation text |
| No repeat booking after manicure | “Після манікюру клієнти не повертаються вчасно” | send reminder after 3–4 weeks |
| No add-ons selected | “Клієнти не бачать додаткові послуги” | show 1 relevant add-on in booking flow |
| High no-show rate | “Ви втрачаєте X грн через неявки” | enable confirmation reminder / deposit for risky clients |
| Google Maps clicks are low | “Вас важко знайти на місці” | improve map link, address text, route button |

This can make analytics a killer feature because it connects data to direct money outcomes, not abstract charts.

### Product maturity ladder

| Level | User-facing product | Value |
|---|---|---|
| 0 | QR to Instagram + Google Maps | easy visibility, immediate low-tech value |
| 1 | QR mini-site with services/prices/contact buttons | more conversions from existing traffic |
| 2 | Booking request form with manual confirmation | fewer переписок, more structured demand |
| 3 | Reminders and no-show tracking | less lost revenue |
| 4 | Add-on suggestions / upsell assistant | higher average check |
| 5 | Money hints analytics | tells master what to improve next |
| 6 | Full CRM / automation | only after trust and digital habit exist |

### Revised positioning

For low-tech market entry:

> **QR-сторінка, яка приводить клієнтів у Instagram, Google Maps і запис — без складної CRM.**

For evolved product:

> **Простий beauty-асистент, який показує, де ви втрачаєте гроші, і допомагає збільшити запис та середній чек.**

### Product implication

The first onboarding should not ask the master to “configure CRM”. It should ask:

1. Як вас знайти в Instagram?
2. Де ви на Google Maps?
3. Які 3–5 послуг найпопулярніші?
4. Як клієнту записатись?
5. Хочете QR-код для столу/дзеркала/дверей?

Only after this should the product introduce booking, reminders, upsells, and analytics.

---

## Killer feature candidate: contextual upsell assistant

This can become the next differentiator after the low-tech QR wedge: not just “calendar/CRM”, but a system that **helps the master earn more from every booking without sounding pushy**.

### Core idea

> **Smart add-on offers at the right moment.**  
> The system suggests a relevant drink, product, or extra service based on the booked service, client history, timing, and context — but the master controls whether to offer it.

This fits the trust-first positioning: the product does not blindly sell. It prepares a suggestion, and the master approves or edits it.

### Why this can be a killer feature

Most beauty CRMs optimize operations: calendar, reminders, client base. Upsell assistant directly connects to revenue:

- increases average check;
- helps sell low-effort add-ons;
- gives measurable ROI for the SaaS;
- makes the tool feel like a revenue assistant, not an admin burden;
- works even for solo masters without complex salon infrastructure.

### Upsell types

| Type | Examples | When to suggest |
|---|---|---|
| Drink / comfort add-on | кава, чай, матча, просекко, вода, снек | before arrival, during confirmation, at check-in |
| Service add-on | зняття покриття, укріплення, дизайн, SPA-догляд, маска, тонування брів, ламінування, масаж рук | during booking after main service selection |
| Product retail | олійка для кутикули, шампунь, SPF, крем, сироватка, догляд після процедури | after service or in follow-up |
| Time-slot optimization | “Є +20 хв — можна додати догляд/дизайн” | when selected slot has buffer |
| Repeat booking | “Записати наступний візит через 3–4 тижні?” | after visit / payment |
| Bundle | “Манікюр + педикюр”, “брови + вії”, “чистка + SPF” | during booking or follow-up |

### MVP version

Do not start with AI. Start with **rules + templates**:

1. Master defines add-ons:
   - name;
   - price;
   - duration;
   - eligible services;
   - message template;
   - whether it requires extra time.
2. System suggests add-ons during booking:
   - “До цієї послуги часто додають…”;
   - only if enough time exists;
   - only if master enabled the add-on.
3. Client can select add-on, but if it changes timing/price, booking goes to manual confirmation.
4. Master sees: base service + selected add-ons + extra time + extra revenue.
5. Dashboard shows upsell revenue.

### Product UX patterns

#### Booking flow

After choosing the main service:

> **Хочете додати щось до візиту?**  
> - Дизайн нігтів +150 грн / +15 хв  
> - SPA-догляд рук +250 грн / +20 хв  
> - Кава/чай під час процедури +0–80 грн

Important: keep it tasteful, not marketplace-like. Beauty clients buy trust and comfort.

#### Master-side suggestion

For manual-confirmation workflow:

> Client booked: Манікюр гель-лак, 90 хв, 700 грн.  
> Suggested upsell: Зняття старого покриття, +150 грн / +20 хв.  
> Reason: client selected “є старе покриття” in form.  
> Buttons: `Запропонувати`, `Додати вручну`, `Не пропонувати`.

#### Follow-up retail

After visit:

> “Дякую за візит ❤️ Щоб покриття трималось довше, можна використовувати олійку для кутикули. Якщо хочете — відкладу для вас до наступного разу.”

### Trust controls

| Risk | Control |
|---|---|
| Master fears pushy sales | suggestions disabled by default; preview before sending |
| Client annoyed by irrelevant offers | only 1–2 contextual offers; no spam |
| Add-on breaks schedule | offer only if enough time or route to manual confirmation |
| Product sounds robotic | editable templates in master’s tone |
| Master wants full control | “suggest only to me” mode before client-facing automation |

### Revenue dashboard

This is essential for making it sellable:

- upsell conversion rate;
- extra revenue from add-ons;
- top add-ons;
- missed opportunities;
- repeat booking revenue;
- no-show savings.

Example ROI message inside product:

> “Цього місяця add-ons принесли +2 450 грн. Підписка окупилась у 6.1×.”

### Prioritization

| Feature | MVP? | Why |
|---|---|---|
| Add-on catalog | Yes | foundation for upsells |
| Add-on eligibility by service | Yes | keeps offers relevant |
| Add-on duration and price | Yes | prevents schedule conflict |
| Client-side add-on choice | Yes | direct average-check lift |
| Master approval for add-on bookings | Yes | trust-first control |
| Editable upsell templates | Yes | avoids robotic/pushy tone |
| Upsell revenue dashboard | Yes | proves SaaS ROI |
| AI recommendations | Later | useful only after data exists |
| Inventory-linked retail | Later | salon/studio feature, not solo MVP |
| A/B testing offers | Later | growth feature after traction |

### Positioning extension

Base positioning:

> Порядок у записах без втрати контролю.

Stronger revenue positioning:

> **Не просто записує клієнтів — допомагає збільшувати середній чек.**

Or:

> **Beauty-асистент, який нагадує, підтверджує і м’яко допомагає продавати додаткові послуги.**

### Validation experiment

Run a concierge test before building full automation:

1. Pick 5–10 masters.
2. For each, define 3 add-ons manually.
3. Add add-on checkboxes to the booking form or ask via message after booking.
4. Track:
   - % bookings with add-on;
   - average extra revenue;
   - client complaints/annoyance;
   - whether master keeps using it after 2 weeks.

Continue if:

- 15–25% of bookings accept at least one add-on; or
- add-ons generate enough monthly revenue to cover subscription 3×+; and
- masters do not feel it damages client relationship.

---

## Packaging hypothesis

### Solo

| Plan | Approx. price | Contents |
|---|---:|---|
| Free / Starter | 0 грн | календар, до 20 записів/міс, ручні заявки |
| Solo | 199–399 грн/міс | необмежені записи, клієнти, нагадування, онлайн-посилання |
| Solo Pro | 499–799 грн/міс | follow-up, no-show tracking, фінанси, шаблони, Telegram/Viber |

### Studio

| Plan | Approx. price | Contents |
|---|---:|---|
| Studio | 799–1499 грн/міс | 2–5 майстрів, спільний календар, ролі, базова аналітика |
| Studio Pro | 1499–2999 грн/міс | зарплати, передоплата, лояльність, розширені звіти |

---

## Validation plan

| Experiment | Metric | Continue if | Adjust if |
|---|---|---|---|
| Landing page для майстрів | % заявок | 5–10% залишають контакт | <2% conversion |
| Concierge MVP: календар + ручний Telegram/admin | Usage 2 weeks | майстер реально веде записи | повертається в блокнот |
| Test “ручне підтвердження заявок” | % confirmed requests | майстер не боїться давати посилання | майстри не шарять посилання |
| Test reminders | no-show rate | no-show падає | клієнти ігнорують/дратуються |
| Test price 299 грн/міс | willingness to pay | 20–30% тестових платять | “корисно, але не платитиму” |
| Interviews after 10 bookings | repeated pains | повторюються 3–5 болів | фічі не збігаються з реальністю |

---

## Interview questions

### Current process

1. Де ви зараз ведете записи?
2. Скільки часу на день витрачаєте на переписки?
3. Як клієнти зазвичай записуються?
4. Що найчастіше питають перед записом?
5. Як ви нагадуєте клієнтам?
6. Скільки неявок/скасувань буває на місяць?
7. Чи берете передоплату?
8. Що найбільше дратує в записах?

### Trust and automation

1. Чи дали б ви клієнтам посилання для самостійного запису?
2. Що має бути, щоб ви не боялись онлайн-запису?
3. Які послуги можна записувати автоматично?
4. Які послуги треба підтверджувати вручну?
5. Чи дозволили б постійним клієнтам записуватись без підтвердження?
6. Чи хочете бачити текст повідомлення перед відправкою?
7. Що система точно не має робити без вас?

### Payment

1. Скільки ви готові платити, якщо це зекономить 5 годин на місяць?
2. Скільки коштує одна неявка?
3. Якщо система поверне 2 клієнтів на місяць, чи вартує вона 300–500 грн?
4. Що має бути в продукті, щоб ви платили щомісяця?

---

## Decision

Start with a **trust-first SaaS for solo beauty masters**, not a full salon CRM.

The wedge is not “more features than Altegio/EasyWeek”. The wedge is:

1. faster setup for solo masters;
2. Ukrainian messenger-first workflow;
3. manual approval as default;
4. gradual automation only after trust is earned;
5. clear ROI: fewer переписок, fewer no-shows, more repeat bookings.
