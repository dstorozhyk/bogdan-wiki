---
title: Manual paid pilot workflow for SaaS validation
created: 2026-06-10
updated: 2026-06-10
type: summary
tags: [guide, saas, payments, validation, invoicing]
sources:
  - https://www.payoneer.com/invoice-payments/
  - https://www.payoneer.com/get-paid-by-clients/payment-request/
confidence: medium
---

# Manual paid pilot workflow for SaaS validation

## Goal

Перевірити, чи люди реально платять за SaaS-ідею, без відкриття іноземної компанії, Stripe Billing або повної автоматизації.

## Landing structure

Pricing block:

```text
Founding paid pilot — $99 / 30 days
Manual onboarding during private beta.
You will receive a secure invoice/payment link.
```

CTA:

```text
Start paid pilot
```

Form fields:

- email;
- company/site;
- use case;
- desired plan;
- preferred payment: card/bank invoice, crypto, PayPal fallback;
- optional: Telegram/Discord/contact.

## Payment flow

Primary:

```text
Lead submits form
→ create Payoneer payment request/invoice
→ send payment link
→ client pays
→ manually activate account / whitelist / license key
→ send onboarding message
```

Backup:

```text
If Payoneer card method unavailable
→ offer crypto invoice or PayPal manual fallback
```

## Product access flow

Use simple manual gates before building billing automation:

- whitelist email/domain;
- feature flag paid account;
- license key stored in DB;
- private beta invite link;
- manual account creation.

## Validation thresholds

Move to foreign entity + Stripe/MoR when at least one is true:

- 5–10 users paid manually;
- 2–3 B2B buyers are willing to pay materially more;
- repeated manual checkout causes measurable lost deals;
- customer base needs self-serve recurring card billing;
- tax/compliance burden becomes real.

## Metrics to track

- landing visitors;
- CTA clicks;
- form submissions;
- invoices sent;
- invoices paid;
- payment method used;
- time from form to payment;
- objections;
- refund/dispute events;
- activation-to-usage conversion.

## Anti-patterns

- Spending weeks on company/Stripe before proving demand.
- Building subscription billing before anyone paid manually.
- Using another person's Stripe/company informally.
- Pretending Ukrainian PayPal personal flow is a proper SaaS merchant account.
- Ignoring VAT/sales tax if sales start scaling.

## Related

- [[saas-payments-ukraine-validation-2026-06]]
- [[payoneer-invoice-payment-request-ukraine-saas]]
- [[saas-invoice-service-shortlist-ukraine]]
