# Wiki Schema — Bogdan's General Knowledge Base

## Domain

A compounding knowledge base covering AI/ML research, software engineering (.NET/C#, Python, TypeScript),
infrastructure, devops, programming techniques, tools, people, organizations, and any interesting discoveries
relevant to daily work and learning.

**Division of labor:** Denys (human) curates sources and directs analysis. Bogdan (agent) ingests, summarizes,
cross-references, and maintains consistency.

## Conventions

- **File names:** lowercase, hyphens, no spaces (e.g., `transformer-architecture.md`)
- **Wikilinks:** Use `[[page-name]]` to link between pages. Minimum 2 outbound links per page.
- **Frontmatter:** Every wiki page starts with YAML (see below). Every new page gets added to `index.md`.
- **Updates:** Bump `updated` date on every edit. Append action to `log.md`.
- **Provenance:** On pages synthesizing 3+ sources, append `^[raw/articles/source-name.md]` markers
  to paragraphs so claims can be traced back without re-reading the source.
- **Raw sources:** Immutable. Never edit files in `raw/`. Corrections go in wiki pages.

## Directory Routing

Route by the page's semantic role, not merely by whether sources were consulted:

- `raw/` — immutable source captures.
- `research/` — provisional/source-backed investigations, datasets, and dated market scans or snapshots.
- `entities/`, `concepts/`, `comparisons/`, `queries/` — stable reusable knowledge by type.
- `workflows/` — executable playbooks and repeatable procedures.
- `career/` — Denys's durable career context, clearly separated into profile, job-search, learning, work-context, and unapproved ideas/drafts.
- `logs/` — chronology and generated daily digests; `agents/` — agent policy and review queues.
- `state/` — persisted machine/runtime state such as crawler seen-URL files. It is not human-readable knowledge and is not indexed page-by-page.
- `_archive/` — superseded material retained for history.

User-approved decisions/plans must say `status: approved`. Assistant-generated proposals must use `status: idea` or `status: draft` plus `approval: unapproved`; never call them Denys's plan before approval. Ambiguous legacy pages stay in place and are listed in `agents/migration-review.md` rather than moved speculatively.

## Frontmatter (Wiki Pages)

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary | research | workflow | profile | context | guide | idea | draft | decision | plan
tags: [tag1, tag2]  # Only from taxonomy below
sources: [raw/articles/source-name.md, ...]
status: active | reference | idea | draft | approved | superseded | archived  # Optional, required for ideas/drafts/plans/decisions
approval: unapproved | user-directed  # Optional; required when approval could be confused
confidence: high | medium | low    # Optional; omit if high is implied
contested: false                   # Set true if unresolved contradictions exist
contradictions: [other-page-slug]  # Optional; pages this one conflicts with
---
```

## Frontmatter (Raw Sources)

```yaml
---
source_url: https://example.com/article
ingested: YYYY-MM-DD
sha256: <hex digest of body only>
---
```

The `sha256` prevents duplicate ingests and detects source drift on re-ingest.

## Tag Taxonomy

**Core domains (add new tags here BEFORE using them):**

### AI/ML Models & Architecture
- model, transformer, llm, diffusion, vision, multimodal, moe, quantization, benchmark, training

### .NET Ecosystem
- csharp, dotnet, aspnet, ef, linq, testing, nuget, roslyn, performance

### Programming Techniques
- algorithm, optimization, concurrency, async, design-pattern, refactoring, testing, debugging

### Infrastructure & DevOps
- kubernetes, docker, systemd, networking, monitoring, ci-cd, postgres, redis, vps

### Data & ML Ops
- dataset, evaluation, fine-tuning, rag, inference, prompt-engineering, alignment

### Languages & Tools
- python, typescript, nodejs, bash, git, cli, ide

### People & Organizations
- person, company, lab, open-source, researcher, startup

### Product & Business
- saas, payments, invoicing, validation, workflow, wiki

### Career & Personal Context
- career, tech-lead, job-search, learning, enterprise, architecture, delivery, finance

### Meta
- comparison, timeline, controversy, prediction, guide, tutorial

**Rule:** Every tag must appear in this list. New tags require a schema update first.

## Page Thresholds

- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **Don't create a page** for passing mentions, minor details, or out-of-scope items
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links
- **Archive a page** (move to `_archive/`) when fully superseded

## Entity Pages

One page per notable entity (person, org, model, tool). Include:
- Overview / what it is
- Key facts and dates
- Relationships to other entities ([[wikilinks]])
- Source references

## Concept Pages

One page per concept or technique. Include:
- Definition / explanation
- Current state of knowledge
- Open questions or debates
- Related concepts ([[wikilinks]])

## Comparison Pages

Side-by-side analyses. Include:
- What is being compared and why
- Dimensions of comparison
- Verdict or synthesis
- Sources

## Update Policy

When new information conflicts with existing content:
1. Check dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction: set `contradictions: [page-name]` in frontmatter
4. Flag for user review in lint report

---

*Last updated: 2026-08-16*
