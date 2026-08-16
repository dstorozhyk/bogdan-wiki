---
title: Hermes memory lifecycle
created: 2026-08-17
updated: 2026-08-17
type: concept
status: reference
tags: [wiki, workflow]
sources:
  - "agents/knowledge-policy.md"
  - "research/hermes-memory-roadmap.md"
  - "https://hermes-agent.nousresearch.com/docs/user-guide/features/memory"
  - "https://hermes-agent.nousresearch.com/docs/user-guide/features/skills"
---

# Hermes memory lifecycle

## Purpose

Hermes uses several persistence layers with different jobs. Reliable memory comes from routing information to the right layer, not copying every conversation into an always-on prompt. ^[agents/knowledge-policy.md]

## Layers

### Working context

The current conversation and tool results support the active task. Context compression may summarize older turns. This is temporary working memory, not the durable source of truth.

### Session history

The canonical session store preserves conversation history for later `session_search`. It is episodic evidence: useful for reconstructing what happened, but too noisy to inject wholesale into every future turn.

### User profile and compact memory

Persistent user/profile memory contains compact stable facts that reduce repeated steering:

- identity and durable preferences;
- stable environment/config pointers;
- recurring corrections and operating boundaries.

It should not contain task progress, raw transcripts, secrets or facts likely to expire quickly.

### Skills

Skills are procedural memory: reusable triggers, exact steps, pitfalls and verification. A workflow belongs in a skill when the agent should execute it repeatedly, not merely understand it.

### Wiki

The wiki is durable human-readable knowledge:

- concepts, entities and architecture;
- sourced research and dated scans;
- decisions and approved strategy context;
- workflows/runbooks;
- open questions and review queues.

It supports more detail and provenance than compact memory.

### Operational state

Cron state, crawler state, queues and progress files are runtime state. They belong in scheduler/state/task storage, not semantic memory.

## Lifecycle

### 1. Observe

Work occurs in a session. Preserve raw evidence in the session store rather than copying it immediately.

### 2. Classify

Ask what future use the information has:

- stable steering fact → memory/profile;
- repeatable procedure → skill;
- durable knowledge or decision context → wiki;
- runtime progress → state/task system;
- trivial, duplicate or transient → discard.

### 3. Verify and label

Before promotion:

- distinguish user-confirmed facts from assistant inference;
- attach source/session provenance;
- label drafts and ideas as unapproved;
- timestamp volatile claims;
- keep secret values out of every knowledge layer.

### 4. Promote minimally

Store the smallest representation appropriate to the target. Do not mirror the same long text across memory, skill and wiki.

A compact memory entry may point to a wiki page. A wiki page may point to a source session. A skill may link a runbook/reference without copying all research.

### 5. Consolidate

Periodic consolidation should:

- deduplicate candidates;
- merge overlapping compact memory;
- route detail out of always-on memory;
- update canonical pages rather than create parallel truths;
- stage uncertain changes for review;
- preserve chronology separately from current knowledge.

### 6. Refresh and forget conservatively

Facts can become stale. Prefer:

- live-source verification when a current system/source is available;
- explicit `updated`/verification dates;
- superseding old conclusions rather than silently rewriting history;
- archiving or marking stale before deletion;
- human review for ambiguous identity/preferences/decisions.

## Retrieval order

When answering or acting:

1. inspect a direct source supplied by the user or live system when accessible;
2. use canonical wiki/skill/memory for durable context;
3. use session search to reconstruct historical decisions/evidence;
4. verify current external facts live;
5. state uncertainty when evidence is incomplete.

Session history describes what was said; it does not prove the current state of an external account, website, file or service.

## Current system vs research roadmap

Current stable capabilities include persistent profile/memory, session search, skills and pluggable memory providers. ^[https://hermes-agent.nousresearch.com/docs/user-guide/features/memory]

Research ideas such as automatic staleness inference, knowledge graphs, RL-based memory policy or broad autonomous consolidation remain roadmap/research unless verified in the live installation. ^[research/hermes-memory-roadmap.md]

The old roadmap contains dated implementation sketches and pseudo-commands. It is retained as research provenance, not operational documentation. ^[research/hermes-memory-roadmap.md]

## Safety invariants

- no secret values in memory, wiki, skills or session summaries;
- no fabricated provenance;
- no promotion of assistant drafts into user decisions;
- no automatic destructive forgetting of ambiguous high-value facts;
- source-first verification for live systems;
- compact always-on memory, detailed wiki, procedural skills, raw session history.

## Related

- [[agents/knowledge-policy|Agent knowledge policy]]
- [[wiki-decomposition-workflow]]
- [[automation-idea-validation-funnel]]
- [[research/hermes-memory-roadmap|Hermes memory enhancement roadmap]]
