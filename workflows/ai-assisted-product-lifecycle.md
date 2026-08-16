---
title: AI-assisted product lifecycle workflow
created: 2026-08-16
updated: 2026-08-16
type: workflow
status: reference
tags: [workflow, architecture, prompt-engineering, validation]
sources:
  - "research/ai-assisted-sdlc-vibe-coding-project-lifecycle-2026-07-02.md"
---

# AI-assisted product lifecycle workflow

Use this workflow when AI agents generate a significant part of a product implementation.

## Phase 0 — Product brief

Define:

- target user and painful problem;
- core promise and one primary scenario;
- riskiest assumption;
- measurable success signal;
- explicit non-goals;
- data, security and operational constraints.

**Gate:** another person can explain what is being tested and what is intentionally excluded.

## Phase 1 — RAT or prototype

Choose the cheapest artifact that tests the largest uncertainty:

- clickable prototype;
- landing/fake door;
- manual concierge flow;
- technical PoC;
- structured user conversations.

**Gate:** record evidence and choose `continue`, `pivot`, or `stop`. Interest without behavior is not validation.

## Phase 2 — Walking skeleton

Create the smallest real end-to-end system:

- repository and repeatable build;
- deploy target;
- CI or deterministic validation command;
- thin UI/API/data path where relevant;
- basic logging and error visibility;
- first automated tests.

**Gate:** the path runs in the target environment, not only in an agent's explanation.

## Phase 3 — Vertical slice

Implement one complete user action through every required layer:

> user intent → interface → domain/application logic → persistence/integration → observable result

Define acceptance criteria before implementation.

**Gate after every AI change:** build, tests, lint/typecheck, focused security sanity check, diff review and manual critical-path smoke test.

## Phase 4 — Minimum lovable product

Add only what is needed for trust:

- coherent mobile/desktop UX for the target audience;
- empty/loading/error states;
- onboarding or contact path;
- baseline accessibility and performance;
- safe credential handling;
- feedback capture.

**Gate:** a target user can complete the core scenario without developer assistance.

## Phase 5 — Controlled pilot

Launch to a bounded real audience with:

- offer/pricing hypothesis where relevant;
- analytics and operational telemetry;
- support and incident channel;
- bug/feedback triage;
- explicit rollback/stop criteria;
- roadmap driven by observed behavior.

## Agent execution rules

For every task, record:

1. allowed scope;
2. forbidden/unrelated changes;
3. files or systems that are source of truth;
4. commands required before done;
5. user-visible scenario to verify;
6. operations requiring separate approval.

An agent summary is not proof. The deliverable must be exercised and verified in the real target environment.

## Related

- [[ai-assisted-sdlc]]
- [[wiki-decomposition-workflow]]
- [[manual-paid-pilot-workflow]]
