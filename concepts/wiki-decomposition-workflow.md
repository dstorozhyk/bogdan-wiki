---
title: Wiki decomposition workflow
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [guide, workflow, wiki]
sources: []
confidence: high
---

# Wiki decomposition workflow

## Principle

Research should compound through **small focused pages**, not one large mixed note. Each page should answer one role: overview, entity, comparison, workflow, decision, source notes, or open questions.

This was requested by Denys on 2026-06-10 after the SaaS payment/invoice research: split information across files so decomposition happens naturally and future answers can reuse precise pages.

## Recommended split

For a practical research task, create/update separate files:

1. **Overview / synthesis** — final answer, decision, current recommendation.
2. **Entity/service pages** — one page per important tool/company/API.
3. **Comparison page** — ranked shortlist and trade-offs.
4. **Workflow/playbook** — exact steps to execute.
5. **Open questions / verification checklist** — what must be tested next.
6. **Raw/source notes** — immutable source captures when doing larger research.

## Linking rules

- The overview links to all child pages.
- Child pages link back to the overview and to siblings.
- The comparison links to entity pages.
- The workflow links to the selected service page.
- Index gets updated after every new page.
- Log gets append-only entries.

## Example from SaaS payments

- [[saas-payments-ukraine-validation-2026-06]] — overview.
- [[payoneer-invoice-payment-request-ukraine-saas]] — service/entity page.
- [[saas-invoice-service-shortlist-ukraine]] — comparison.
- [[manual-paid-pilot-workflow]] — executable workflow.

## Related

- [[saas-payments-ukraine-validation-2026-06]]
- [[manual-paid-pilot-workflow]]
