---
title: Freedom24/Freedom Finance поповнення з України — червень 2026
created: 2026-06-09
updated: 2026-08-16
type: research
status: reference
tags: [finance, payments]
sources:
  - "session:default/20260623_120149_3bb6c070"
  - "session:default/20260622_163026_d7eee1f1"
---

# Freedom24/Freedom Finance поповнення з України — червень 2026

Останній account-specific verification: **2026-06-23**.

## Короткий висновок

**Confirmed best observed route for Denys:**

> **Raiffeisen EUR → Wise EUR balance/main account → Freedom24/Freedom Finance Europe EUR**

Тестовий переказ **8.72 EUR** був зарахований брокером як **8.72 EUR**. Це підтверджує нульову втрату на credited amount у конкретному тесті; окрему комісію Raiffeisen/Wise, якщо вона списувалась поза сумою переказу, завжди треба перевіряти у квитанціях.

Практичні правила:

- використовувати EUR end-to-end без USD→EUR conversion;
- відправляти саме з Wise EUR balance/main account, а не через Wise card payment;
- вказувати Freedom reference/client ID;
- власники рахунків Raiffeisen, Wise і Freedom мають збігатися;
- перевіряти live quote і broker credit перед масштабуванням.

Не рекомендуються для цього account-specific flow: direct Ukrainian card top-up to broker, direct SWIFT, Paysera, USD conversion, third-party accounts. Genome/SEPA нижче збережено як **superseded discovery context**, а не поточна основна рекомендація.

## Superseded discovery context (2026-06-09 — 2026-06-14)

До успішного Wise test основним fallback-кандидатом розглядався Genome EUR IBAN → SEPA. Genome не блокував Denys, але тариф для Ukraine/non-EEA (~20 EUR/USD monthly) і card top-up до 3% робили його економічно слабшим.

## Дані зі скріну Дениса, 2026.02

Колонки: банк → TransferGo → Genome; банк → Genome.

- mono: 0%; bank→Genome 1%
- Globus: 0%; bank→Genome 1%
- Raiffeisen: 0% акція; bank→Genome 0% акція
- Agricole: 0%; bank→Genome не вказано
- Kredo: 0%; bank→Genome немає
- Alliance: 0%; bank→Genome 0.8% від суми
- PUMB: 0.5%; bank→Genome 0.9%
- Ukrgas: 0.6%; bank→Genome немає
- A-Bank: 0.9%; bank→Genome не вказано
- Privat: 1%; bank→Genome 1% (з $ на €)
- O.Bank: 1%; bank→Genome немає
- own account: TransferGo немає; bank→Genome 1%
- TAS: 1.8% від суми; bank→Genome немає
- Sense: 1.5% від суми; bank→Genome 1.5% від суми
- OTP / ProCredit / UkrSib: немає / немає
- Unex, Lviv: не вдалося зареєструвати
- Komin: не працює
- Crystal: реєстрація у відділенні

## Офіційні/перевірені джерела

- Freedom24 FAQ: `https://freedom24.com/faq/13006-how-to-deposit-funds?__lang__=uk`
  - картка: кошти миттєво, комісія 2%;
  - банківський переказ: 1–3 робочі дні, без комісії Freedom24, можлива комісія банку;
  - обов’язково вказувати номер брокерського рахунку у призначенні платежу.
- Genome pricing non-EEA / individuals:
  - incoming SEPA: free;
  - outgoing SEPA: 1 EUR;
  - top-up by non-Genome card: 3%;
  - card-to-card incoming in supported currency may be free (за Genome support snippet), але треба перевіряти в додатку перед платежем;
  - 2026-06-14 promo-code check: публічних активних promo/coupon кодів для зниження monthly fee не знайдено. Офіційна non-EEA сторінка має лише старі Ukrainian promotion cohorts: 5 EUR/month для реєстрацій до 13.06.2025 або 01.09.2025–15.12.2025 (для другої когорти fee мав піднятись з 14.02.2026), і 0 EUR до 13.06.2026 для перших українських клієнтів 13.06.2025–31.08.2025. Referral program дає commission/referral benefit рефереру, не явно discount новому клієнту; referral terms забороняють affiliates давати самовільні discounts/rebates.
- НБУ/ринкові зведення по Постанові №18:
  - SWIFT для фізосіб під час воєнного стану суттєво обмежений і не покриває звичайне поповнення брокера для інвестицій;
  - P2P/карткові перекази за кордон мають ліміти й банки можуть відхиляти операції за MCC/призначенням.

## Confirmed practical route

1. Поповнити власний **Wise EUR balance** із власного Raiffeisen EUR account перевіреним account flow.
2. У Freedom24 відкрити `Поповнити → Банківський переказ → EUR` і взяти актуальні EUR реквізити та payment reference.
3. У Wise відправити з **EUR balance/main account** на Freedom EUR details.
4. Внести Freedom reference/client ID навіть якщо Wise позначає поле необов'язковим.
5. Після зарахування звірити `Raiffeisen spent`, `Wise received/sent`, `Freedom credited`, fees і час проходження.

Observed test: **8.72 EUR sent/credited as 8.72 EUR on 2026-06-23**.

### Superseded fallback: Genome → SEPA

Genome може бути технічним fallback, але не є рекомендованим основним маршрутом через monthly fee і top-up friction. Якщо Wise route перестане працювати, Genome слід перевіряти заново live, починаючи з малої тестової суми.

### Crypto fallback

Використовувати тільки якщо у Freedom24 в кабінеті доступний офіційний crypto/USDT deposit:

```text
UAH → Binance/WhiteBIT USDT → Freedom24 USDT deposit
```

Якщо crypto deposit у Freedom24 недоступний, не використовувати Wise або ZEN як міст для crypto/P2P. Підтверджений Wise route — це EUR bank/balance flow, а не crypto on-ramp.

## Ризики/пастки

- Не відправляти з рахунку третьої особи: Freedom24 може повернути або запросити документи.
- Не робити прямий TransferGo → Freedom24, якщо платник у SEPA буде TransferGo, а не Denys; краще через власний Genome, щоб SEPA-відправник збігався з власником брокерського рахунку.
- Не орієнтуватися на заявлені 0% без фінального quote: TransferGo/банк можуть ховати витрату в курсі.
- Зробити тест 50–100 EUR перед великою сумою.
- Зберігати квитанції та підтвердження походження коштів для AML/податків.
