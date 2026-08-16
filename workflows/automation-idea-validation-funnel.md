---
title: Automation idea validation funnel
created: 2026-08-17
updated: 2026-08-17
type: workflow
status: approved
approval: user-directed
tags: [workflow, validation, automation]
sources:
  - "session:current/2026-08-17"
---

# Automation idea validation funnel

## Purpose

Prevent attractive but generic automation ideas from reaching Denys as recommendations.

The funnel separates **generation** from **selection**. Research agents may produce a broad pool, but an idea becomes recommendable only after surviving independent evidence, fit, feasibility, value and adversarial checks.

## When to use

Use this workflow before proposing:

- new recurring automation;
- an agent-owned career or life-support system;
- a high-maintenance monitoring/research cadence;
- a “top ideas” shortlist presented as personalized;
- work that would consume material token, infrastructure or Denys attention.

A trivial one-off action does not need the full funnel.

## Stage 0 — Independent candidate generation

Use several independent lanes so the initial pool is not anchored to one framing:

1. **Needs mining** — wiki, sessions, repeated corrections, unfinished loops and actual friction.
2. **External leverage research** — current opportunities, practices and source-backed asymmetries.
3. **Operator capability mapping** — what the agent can really execute with available access and tools.

Output is raw candidate material, not recommendations.

## Stage 1 — Evidence and deduplication

For each candidate require:

- Denys-specific pain or opportunity evidence;
- source path/session or directly observed system state;
- distinction between confirmed need and assistant inference;
- comparison with existing jobs, projects and ad-hoc use;
- an exact outcome rather than a theme.

Merge true duplicates.

### Automatic kill criteria

Kill an idea if any is true:

- no identifiable Denys-specific evidence;
- it is another digest, report, reminder or dashboard without a closed-loop action;
- it duplicates an existing job/project;
- it needs continuous manual context feeding;
- the agent cannot perform at least roughly 70% of the recurring work;
- no verifiable outcome is possible within 30 days;
- it depends on inaccessible workplace systems or oral context;
- it conflicts with NDA, privacy, corporate or бронювання constraints;
- token/maintenance cost is likely greater than the benefit.

## Stage 2 — User-fit / anti-generic challenge

Ask:

- Would Denys still use this after week two?
- Which recurring pain disappears?
- Why is this better than asking the agent ad hoc?
- What is the embarrassing generic interpretation?
- Does it create a new asset/action or merely more information?
- Which past correction or stated priority supports it?

Ideas based mainly on “personal brand”, “networking”, “AI assistant”, “more visibility” or “more information” fail unless converted into an autonomous, verifiable outcome.

## Stage 3 — Operational feasibility

Describe the exact operating model:

- inputs and source of truth;
- tools/access already available;
- agent steps and durable state;
- Denys-only touchpoints;
- approval boundaries;
- verification and failure recovery;
- token/runtime cadence;
- privacy and secret boundaries.

Kill if agent autonomy is below 70%, recurring Denys burden exceeds about 30 minutes/week without proportional upside, or the external result cannot be verified.

## Stage 4 — ROI and opportunity cost

Compare against:

- do nothing;
- use the agent ad hoc;
- improve an existing automation;
- spend the same effort on direct career evidence or another proven goal.

Estimate ranges for:

- hours saved;
- time to first proof;
- probability of a usable result;
- career/income/risk leverage;
- recurring token/tool cost.

Reject vanity metrics and dominated ideas.

## Stage 5 — Adversarial pre-mortem

Assume the idea failed after 30 days and after six months. Attack:

- false assumptions and missing access;
- hidden manual work;
- noisy or stale output;
- maintenance creep;
- provider/token limits;
- NDA/privacy/security exposure;
- platform policy and external dependencies;
- artificial-looking AI-generated career signal;
- weak user adoption.

The result is `kill` or a materially strengthened operating model. Adding caveats alone is not strengthening.

## Stage 6 — Scored final judge

Score each survivor from 0 to 100:

| Criterion | Weight |
|---|---:|
| Real pain fit | 20 |
| Agent autonomy | 15 |
| Tangible/verifiable output | 15 |
| Expected leverage | 15 |
| 30-day feasibility | 10 |
| Low Denys burden | 10 |
| Privacy/NDA safety | 5 |
| Maintenance/token efficiency | 5 |
| Uniqueness/non-duplication | 5 |

Default pass threshold: **75/100**.

The judge must verify that support comes from evidence, not previous agents repeating one another. Fewer strong survivors are better than filling a requested count with weak ideas.

## Stage 7 — Gap recovery

If fewer ideas pass than requested:

- search narrowly for the missing leverage mechanism;
- do not resurrect killed candidates;
- run replacements through the same rubric and pre-mortem;
- leave the slot empty if no replacement passes.

## Required final idea format

Every recommended idea must include:

1. pain/opportunity evidence;
2. why it fits Denys specifically;
3. exact agent-owned work;
4. required Denys touchpoints;
5. tangible artifact or closed-loop result;
6. reversible 7–14 day experiment;
7. objective success and kill metrics;
8. risks and what remains unproven;
9. score and strongest rejected alternative.

## Principle

> The purpose of the funnel is not to make ideas sound safer. It is to eliminate weak ideas before Denys sees them.

## Related

- [[ai-assisted-product-lifecycle]]
- [[wiki-decomposition-workflow]]
- [[denys-career-direction]]
