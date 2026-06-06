# Hermes Memory Enhancement Roadmap (Based on Research)

> Як покращити Hermes Agent на основі наукових досліджень про AI agent memory  
> Практичні кроки для offline consolidation, selective forgetting, cross-session awareness

---

## Current State (May 2026)

### What Hermes Has
✅ **Core memory:** MEMORY.md (semantic facts) + USER.md (user profile)
✅ **Episodic:** session_search (full access to past 100+ sessions)
✅ **Procedural:** skills library (executable plans)
✅ **Working:** Context window (LLM's internal WM)

### What Hermes Lacks
❌ **Offline consolidation** — episodic logs not automatically → semantic
❌ **Selective forgetting** — no staleness detection / soft deletion
❌ **Knowledge graph** — no entity-relationship indexing (only flat search)
❌ **Cross-session identity** — recognizes Denys, but not robust across devices
❌ **Self-aware memory management** — no RL-based or principled update strategy

---

## Phase 1: Offline Consolidation (Sleep Cycle)

### Rationale
From **SCM paper (2604.20943):**
- Episodic noise accumulates over 50+ turns
- 90.9% noise reduction possible via consolidation
- Should happen during idle time (cron job, not during live chat)

### Implementation: 5-Phase Consolidation

**Every night at 2 AM UTC (via cron):**

#### Phase 1: Collect Episodic Log
```bash
hermes session_search --query="*" --limit=50 --since="24h"
```
Export last 24 hours of sessions into temp file.

#### Phase 2: Extract & Tag Facts
```python
# Pseudo-code
facts = llm.extract(episodic_log, task="extract_memorable_facts")
# Output: [
#   {"fact": "User's email is alice@example.com", "importance": 0.9, "temporal": "recent", "category": "contact"},
#   {"fact": "Project X deadline is June 30", "importance": 0.7, "temporal": "future", "category": "project"},
#   ...
# ]
```

Use Claude Haiku (fast + cheap) for extraction.

#### Phase 3: Consolidation
Three sub-tasks:

**3a. Merge into MEMORY.md**
- Check: does this fact already exist?
- If yes: update timestamp, increase importance weight
- If no: add to appropriate section
- Format: bullet point with [date_added, importance_score]

**3b. Build temporal index**
- Some facts become stale (user's job changed, project ended)
- Tag old facts as `[STALE: review manually]`
- Don't auto-delete (conservative)

**3c. Weak consolidation (if knowledge graph added later)**
- Extract entities: Person → Project, Person → Contact, Project → Deadline
- Build relationship edges
- Feed to graph storage

#### Phase 4: Value-Based Pruning
```python
# Clean up duplicates in episodic log
# Remove facts with importance < 0.3
# Compress "User told me X on date Y" → "User's preference: X"
```

#### Phase 5: Validation
```bash
# Check MEMORY.md didn't grow > 10KB (hard limit)
# If it did, manually review & prune
# Alert Denys to review changes
```

### Cron Job Setup
```bash
hermes cronjob create \
  --name "memory-consolidation" \
  --schedule "0 2 * * *" \
  --prompt "Run 5-phase sleep consolidation: extract facts from last 24h sessions, merge into MEMORY.md, tag staleness, prune noise, validate"
```

---

## Phase 2: Staleness Detection (Light Version)

### Rationale
From **MemoryAgentBench (2507.05257):**
- "Memory staleness" is open problem
- Facts become false when conditions change (person's job, project status)
- No one solves this automatically

### Simple Implementation

**Monthly review (Denys manually triggered):**
```bash
hermes /stale-check
```

Script:
1. Load MEMORY.md
2. For each fact, ask LLM: "Is this still true as of May 2026?"
3. Tag questionable facts: `[REVIEW: might be stale]`
4. Email Denys digest
5. Denys reviews & updates

**Example:**
```markdown
- **[REVIEW]** User works at Company X (added 2025-03, not confirmed since)
- **[STALE]** Phone number 555-1234 (user changed phones; added 2025-01, now May 2026)
```

### Why Manual?
Because **selective forgetting is unsolved in ML**. No algorithm reliably detects "this is now false" without external signal. Better to be conservative and let Denys decide.

---

## Phase 3: Cross-Session Identity (Robust)

### Rationale
Denys might:
- Use Telegram from phone + desktop
- Switch accounts/auth flows
- Reference old sessions

Current implementation: `USER.md` identifies Denys.
Improvement: **ensure all sessions tagged with user_id regardless of channel.**

### Implementation

In `gateway/run.py` or agent startup:
```python
# Associate all sessions with user UUID
user_id = hash(user.telegram_id) or hash(user.email) or hash(user.github_username)
session_metadata = {
  "user_id": user_id,
  "platform": "telegram",
  "device": fingerprint(),
  "timestamp": now(),
}
session_search --user_id=$user_id  # Search across all their sessions
```

**Benefit:** session_search becomes more powerful
```bash
session_search --user="denys" --across_devices=true --query="memory research"
# Returns results from all Denys' sessions on all devices/platforms
```

---

## Phase 4: Knowledge Graph (Medium-term)

### Rationale
From **MemoryAgentBench & MAGMA papers:**
- Vector search fails at multi-hop reasoning
- Graph excels: "Who did [person] work with on [project] in [date]?"
- Not critical but powerful for Hermes at scale

### Minimal Implementation

**Option A: Skip (use Mem0 integration instead)**
- Mem0 already has graph in Pro tier
- Could integrate Mem0 as external provider

**Option B: DIY with SQLite + FTS5 (like Holographic)**
```python
# entities table
CREATE TABLE entities (
  id TEXT,
  type TEXT,  -- "person", "project", "tool", "date"
  name TEXT,
  properties JSON
);

# relations table
CREATE TABLE relations (
  source_id TEXT,
  rel_type TEXT,  -- "works_on", "related_to", "created_at"
  target_id TEXT,
  weight FLOAT,  -- importance
  created_at TIMESTAMP
);

# Search: find path A → B → C
SELECT * FROM relations WHERE source_id="Alice" AND rel_type="works_on"
  JOIN relations on relations.source_id=target_id where rel_type="created_by" AND target_id="ProjectX"
```

**Cost:** 1-2 days of work
**Benefit:** Multi-hop reasoning, relationship visualization

**Recommendation:** Skip for now. Revisit after Phase 1 & 2 stable.

---

## Phase 5: RL-Based Memory Management (Research-Phase)

### Rationale
From **AgeMem paper (2506.01551):**
- Train agent's memory policy via RL
- "What to store, recall, update, delete" becomes learned skill
- Generalizes to new task types

### Not Recommended for Hermes (Yet)
**Why:**
- Complex (needs RL training loop)
- Only valuable at scale (100+ agents sharing memory)
- Hermes is single-user focused (Denys)

**Defer to:** When Denys runs multi-agent system or scales to team

---

## Phase 6: GEPA Integration (Already Planned)

### From Your Notes
**GEPA:** Genetic-Pareto Prompt Evolution
- Offline skill evolution pipeline
- Solves "skills created inline are self-congratulatory"
- Runs as separate background process

### How It Fits
```
Episodic log → Consolidation (Phase 1)
            → Skill evaluation (GEPA)
            → Update skills library
```

**Timeline:** After Phase 1 stable (July 2026)

---

## Priority Roadmap

### Tier 1: Do First (May-June 2026)
1. **Phase 1 (Sleep Consolidation)** — 3-4 days implementation
   - Massive value (90% noise reduction from research)
   - Directly improves MEMORY.md quality
   - Can use existing tools (session_search, LLM)

2. **Phase 3 (Cross-session identity)** — 1 day
   - Easy win (better session_search)
   - No breaking changes

### Tier 2: Do After (July-August 2026)
3. **Phase 2 (Staleness detection)** — 2-3 days (mostly UX)
   - Manual review is OK (conservative)
   - Set up cron job + email digest

4. **GEPA integration** — depends on Nous Release schedule

### Tier 3: Maybe Later
5. **Phase 4 (Knowledge graph)** — Only if needed for scale
6. **Phase 5 (RL memory)** — Only if multi-agent

---

## Quick Wins (This Week)

If you want to start TODAY:

### 1. Add Staleness Tags (Manual, 30 min)
Edit MEMORY.md sections. Add dates:
```markdown
GitHub authenticated as dstorozhyk via gh CLI with a Fine-grained PAT. 
**Last confirmed:** 2026-05-29 ✅
```

### 2. Set Up Manual Consolidation Script (1 hour)
```bash
#!/bin/bash
# Run this monthly: consolidate yesterday's sessions into MEMORY.md

hermes session_search --since="7d" --output=json > /tmp/weekly_sessions.json

# Use Claude Haiku to extract facts
cat /tmp/weekly_sessions.json | llm prompt \
  "Extract memorable facts (3-5 max) that should go into MEMORY.md. Format as bullets with [importance_score]."

# Manual review, copy-paste into MEMORY.md
```

### 3. Add wiki-consolidation.md (Right Now)
Write a checklist in your personal wiki:
```
- [ ] Monthly staleness review
- [ ] Check if Hermes wiki auto-sync working
- [ ] Verify MEMORY.md under 10KB
```

---

## Research References

All papers that informed this roadmap:

**Sleep Consolidation:**
- SCM (2604.20943) — 5-phase model
- SleepGate (2603.14517) — interference handling
- "Language Models Need Sleep" (OpenReview 2025)

**Benchmarks showing value:**
- MemoryArena (2602.16313) — 80% vs 45% with/without memory
- MemoryAgentBench (2507.05257) — 4 competencies
- LongMemEval (2410.10813) — temporal eval

**Memory management:**
- AgeMem (2506.01551) — RL approach
- CoALA (2309.02427) — taxonomy

**Existing inspiration:**
- Karpathy's LLM Wiki — "compilation not interpretation"
- Hermes MEMORY.md — already half the battle
- Cognee's self-improvement cycle — automated consolidation example

---

## Final Notes

**You have a head start.**
Hermes already has:
- episodic search (session_search)
- semantic core (MEMORY.md)
- procedural library (skills)

**Most agents lack episodic + semantic + procedural together.** You're already at 3/4.

**Sleep consolidation is the missing piece** — automate merging episodic into semantic nightly.

**By July 2026, you could have:**
- Better MEMORY.md (90% less noise via consolidation)
- Staleness awareness (manual but systematic)
- Cross-session search (all devices unified)
- GEPA-evolved skills (next-gen auto-skill-creation)

= Better Bohdan that learns + remembers + forgets intelligently.

---

**Last Updated:** May 29, 2026  
**Author:** Bohdan (based on research dive)  
**Next Action:** Implement Phase 1 (Sleep Consolidation cron job)
