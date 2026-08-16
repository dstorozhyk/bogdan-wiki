---
title: AI-assisted SDLC
created: 2026-08-16
updated: 2026-08-16
type: concept
status: reference
tags: [workflow, architecture, prompt-engineering]
sources:
  - "research/ai-assisted-sdlc-vibe-coding-project-lifecycle-2026-07-02.md"
---

# AI-assisted SDLC

## Definition

**AI-assisted SDLC** is a normal software-development lifecycle in which AI participates in discovery, planning, implementation, review, testing, documentation and maintenance.

It is not a replacement for engineering responsibility. Human ownership shifts toward:

- defining intent and non-goals;
- architecture and constraints;
- acceptance criteria;
- review of generated changes;
- verification and operational accountability;
- control of security, data and technical debt.

## Vibe coding as a development mode

Vibe coding is the use of natural-language intent to generate a substantial part of an implementation. It can increase iteration speed, but without explicit guardrails it amplifies:

- plausible-looking hidden defects;
- unrelated rewrites;
- architecture drift;
- inconsistent UX;
- unverified security assumptions;
- unclear definition of done.

Therefore AI-heavy development needs **stronger acceptance and verification gates**, not a weaker SDLC.

## Choosing the first artifact

Do not use “MVP” as a generic synonym for every early product. Choose the artifact by the risk being tested:

| Artifact | Question it answers |
|---|---|
| PoC | Is this technically possible? |
| Prototype | How should the experience look and feel? |
| RAT | Does the riskiest assumption hold? |
| Walking skeleton | Can a thin real path run end-to-end? |
| Vertical slice | Does one complete user scenario work across all layers? |
| MLP | Is the smallest usable product trustworthy and pleasant? |
| MMP/Pilot | Can it be offered to a controlled real audience? |

For AI-built products, a useful default is:

> **RAT/prototype → walking skeleton → vertical slice → MLP → controlled pilot**

## Minimum architecture guardrails

Before agents implement broad scope, define at least:

- stack and deployment target;
- module boundaries;
- data model and migration policy;
- API/contracts;
- authentication and secret boundaries;
- testing strategy;
- coding conventions;
- allowed and forbidden changes;
- human-review checkpoints.

The artifact can be short. Its value is that it constrains autonomous changes.

## Core principle

> Faster code generation increases the value of precise scope, small vertical slices and executable verification.

## Related

- [[ai-assisted-product-lifecycle]]
- [[wiki-decomposition-workflow]]
- [[projects/beauty-growth-assistant/overview|Beauty Growth Assistant]]
