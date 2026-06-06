# AI Agent Long-Term Memory — Research Landscape (May 2026)

> Дослідження та аналіз: травень 2026  
> Контекст: наукові досягнення і комерційні рішення в управлінні довготривалою пам'яттю AI-агентів

---

## 1. Таксономія пам'яті агентів (CoALA Framework)

Пам'ять агента ділиться на чотири типи за аналогією з когнітивною наукою людини:

| Тип | Назва англ. | Опис | Аналог | Посилання |
|-----|-------------|------|--------|----------|
| **Working** | Working memory | Активне контекстне вікно під час виконання | RAM | — |
| **Episodic** | Episodic memory | Записи конкретних подій, tool calls, поворотів розмов | Щоденник | [Generative Agents](https://arxiv.org/abs/2304.03442) |
| **Semantic** | Semantic memory | Абстраговані факти, відокремлені від контексту | Енциклопедія | — |
| **Procedural** | Procedural memory | Навички та виконувані плани (scripts, workflows) | М'язова пам'ять | [Voyager](https://arxiv.org/abs/2305.16291) |

### Ключовий висновок
**Різниця між "є пам'ять" і "немає пам'яті" часто більша, ніж різниця між різними LLM-моделями.**

Приклад з MemoryArena:
- Агент з memory: **80%+** точність на multi-session tasks
- Baseline без memory: **~45%**

📄 **CoALA Framework** — arXiv:2309.02427 — Tagging Agent Behavior in Long-Horizon Tasks  
📄 **Survey 2026** — arXiv:2603.07670 — State of the Field in AI Agent Memory

---

## 2. П'ять основних механізмів зберігання

### 2.1 RAG (Retrieval-Augmented Generation)
**Підхід:** Vector DB semantic search при кожному запиті  
**Особливість:** Не накопичує — кожного разу дістає заново  
**Характеристика:** "RAG retrieves and forgets"  

**Приклади:** Pinecone, Weaviate, Milvus  
📄 [Lewis et al. 2020](https://arxiv.org/abs/2005.11401) — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

---

### 2.2 Selective Memory Extraction
**Підхід:** LLM витягує дискретні факти з розмови, дедуплікує, зберігає структурованим чином  
**Лідер:** **Mem0** — hybrid triple-store (vector + key-value + knowledge graph)  
**Точність на LongMemEval-S:** 67.6%  

**Особливість:** На чотирьох компетентностях MemoryAgentBench показує середні результати, але найбільш mature ecosystem

**Ліцензія:** Apache 2.0, 51k+ stars на GitHub  

📄 [Mem0 / ECAI 2025](https://arxiv.org/abs/2504.19413)  
🔧 [mem0.ai](https://mem0.ai) — Продукт / API

---

### 2.3 Hierarchical Memory (MemGPT / Letta)
**Підхід:** STM (short-term) / LTM (long-term) / archival по аналогії з ОС  

**Модель:**
- Контекстне вікно = RAM (fast, limited)
- Vector DB = диск (slower, bigger)
- Cold storage = архів (slowest, unlimited)

**Переміщення:** Агент або мережа правил переміщує стару інформацію вниз по иерархії

📄 [MemGPT / Letta](https://arxiv.org/abs/2310.08560) — Towards LLMs as Operating Systems

---

### 2.4 Graph Memory (Knowledge Graphs)
**Підхід:** Зберігання як knowledge graph з entity-relationship моделью замість плоских векторів  

**Переваги:**
- Явні зв'язки (entity → relation → entity)
- Temporal validity windows
- Multi-hop reasoning (A→B→C)
- Pruning старих вузлів / переважування ребер

**Лідер:** **MAGMA** — Multi-graph Agentic Memory Architecture  
📄 [MAGMA](https://arxiv.org/abs/2501.13956)

**Комерційні:** Cognee (($7.5M seed, 12k stars), Zep/Graphiti

---

### 2.5 Policy-Learned Memory (RL-based)
**Підхід:** Агент через Reinforcement Learning навчається **самостійно** вирішувати що зберігати, читати, оновлювати, видаляти  

**Статус:** Нова хвиля 2025–2026  
**Лідер:** **AgeMem** (arXiv:2506.01551)

**Основна ідея:** Замість fixed rules, агент має reward signal за точність recall + ефективність

---

## 3. Offline Consolidation — "Sleep Cycle"

### Гарячий тренд 2026
Найактивніше дослідження останнім часом. **Ідея:** агент обробляє episodic log **у фоні** під час простою — по аналогії з гіпокампальним replay під час сну у людей.

### 3.1 SCM: Sleep-Consolidated Memory
**П'ять компонентів системи:**
1. Working memory з обмеженою ємністю
2. Multi-dimensional importance tagging (теги для кожного запису)
3. Offline sleep-stage consolidation (NREM + REM фази)
4. Value-based forgetting (видалення неважливого)
5. Computational self-model (агент розуміє власну архітектуру)

**Результат:** 
- Perfect recall при зниженні memory noise на **90.9%**
- Прямий аналог людського сну

📄 [SCM](https://arxiv.org/abs/2604.20943) — Sleep-Consolidated Memory for Long-context Reasoning

---

### 3.2 SleepGate
**Фокус:** Вирішення **proactive interference** (коли старі спогади заважають новим)

**Компоненти:**
- Conflict-aware temporal tagger
- Lightweight forgetting gate
- Consolidation module

📄 [SleepGate](https://arxiv.org/abs/2603.14517)

---

### 3.3 "Language Models Need Sleep"
**Two-process consolidation:**
1. **Memory Consolidation** — RL-based upward distillation (STM → LTM)
2. **Dreaming** — самомодифікація моделі, синтетичні тренування

📄 [OpenReview 2025](https://openreview.net/forum?id=iiZy6xyVVE)

---

## 4. Competitive Landscape — Лідери ринку

### 4.1 Karpathy's LLM Wiki Approach
**Ключова ідея:** Пам'ять як **"компіляція"**, а не **"інтерпретація"**

| Підхід | Опис |
|--------|------|
| **RAG** | Інтерпретатор — перечитує щоразу |
| **LLM Wiki** | Компілятор — накопичує, синтезує |

**Workflow:**
1. **Collect** — сирі джерела, інтернет, файли
2. **Compile** — LLM інтегрує інформацію у markdown wiki
3. **View** — Obsidian чи webview для пошуку та читання

**Ключова думка:** Markdown стає мовою програмування AI-ери

🔗 [Karpathy на X/Twitter](https://x.com/karpathy)

---

### 4.2 Hermes Agent (Nous Research)
**Двошарова архітектура:**

**Core memory:**
- `MEMORY.md` — факти про проект/контекст
- `USER.md` — профіль користувача
- **Завжди в контексті**, character limits як feature

**External providers:**
- Honcho, Mem0, Hindsight, Holographic, RetainDB, ByteRover, Supermemory, OpenViking

**Проблема:** Skills створюються inline кожні 15 tool calls → агент схильний до self-congratulation

**Рішення:** GEPA (Genetic-Pareto Prompt Evolution) як окремий offline pipeline

🔗 [Hermes docs](https://hermes-agent.nousresearch.com)  
🔗 [GEPA repo](https://github.com/NousResearch/hermes-agent-self-evolution)

---

### 4.3 Cognee
**Open-source graph memory engine** з cross-agent knowledge sharing

**Особливість:** self-improving memify cycle
- Pruning stale nodes
- Reweighting edges
- Automated consolidation

**Інвестиції:** $7.5M seed  
**Community:** 12k+ stars  
**Клієнти:** Bayer (case study)

🔗 [cognee.ai](https://cognee.ai)

---

### 4.4 Slipstream / Vektor
**REM Cycle Engine** — seven-phase background consolidation

**Особливість:** Consolidates, clusters, promotes memories **без блокування** активних операцій

**Статус:** Node.js first, Python на roadmap

---

## 5. Порівняння провайдерів (Benchmarks)

| Провайдер | Підхід | LongMemEval | Особливість | Посилання |
|-----------|--------|-----------|-------------|----------|
| **Hindsight** | TEMPR (4 паралельних retrieval) | 91.4–94.6% | Найвищі бенчмарки, MIT | [Hindsight](https://hindsight.vectorize.io) |
| **ByteRover** | Markdown context tree | 92.2% (LoCoMo) | Сильний на temporal reasoning | [ByteRover](https://byterover.dev) |
| **Supermemory** | Semantic search, multi-source | 81.6% | Generous free tier | — |
| **Mem0** | Hybrid triple-store | 67.6% | All-around, Apache 2.0, 51k stars | [mem0.ai](https://mem0.ai) |
| **Holographic** | SQLite FTS5 + HRR | — | Zero deps, privacy-first | — |
| **OpenViking** | Tiered context (L0/L1/L2) | — | 80–90% token savings | [OpenViking](https://github.com/volcengine/OpenViking) |
| **Honcho** | User dialectic modeling | — | Будує модель юзера, не просто факти | [honcho.dev](https://honcho.dev) |
| **RetainDB** | Database-style schema | — | Structured recall, cloud only | — |

📄 [Hermes memory providers comparison](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers)

---

## 6. Відкриті проблеми (Research Gaps)

З MemoryAgentBench — **жодна система не опановує всі чотири компетентності одночасно:**

1. ✅ **Точний retrieval** — вирішено у більшості
2. ⚠️ **Test-time learning** — частково
3. ⚠️ **Long-range understanding** — частково
4. ❌ **Selective forgetting** — **відкрита проблема**

### Додаткові проблеми
- **Cross-session identity** — впізнавати одного користувача через сесії, девайси, auth flows
- **Memory staleness** — факти що були правдою але застаріли (зміна роботи, проекту, контакту)
- **Memory security** / "mnemonic sovereignty" — хто може писати, читати, видаляти

📄 [MemoryAgentBench](https://arxiv.org/abs/2507.05257) — Unified Benchmark for Agent Memory Across Multiple Competencies  
📄 [Security & Privacy](https://arxiv.org/abs/2604.16548)  
📄 [State of AI Memory 2026](https://mem0.ai/blog/state-of-ai-agent-memory-2026)

---

## 7. Бенчмарки й оцінка

| Бенчмарк | Що вимірює | Посилання |
|----------|-----------|----------|
| **LongMemEval** | Довготривалий recall (single-agent) | [arXiv:2410.10813](https://arxiv.org/abs/2410.10813) |
| **LoCoMo** | Multi-hop і temporal reasoning | [arXiv:2402.17753](https://arxiv.org/abs/2402.17753) |
| **MemoryArena** | Multi-session agentic tasks | [arXiv:2602.16313](https://arxiv.org/abs/2602.16313) |
| **MemoryAgentBench** | 4 компетентності разом | [arXiv:2507.05257](https://arxiv.org/abs/2507.05257) |

---

## 8. Competitive Window — Що немає на ринку

### Що вже є
- ✅ **Граф + крос-агентність** → Cognee ($7.5M, 12k stars)
- ✅ **Sleep-like consolidation** → Slipstream REM Cycle (Node.js, молодий)
- ✅ **Memory as a service для розробників** → Mem0, Zep, LangMem

### Що реально не існує як **єдиний інтегрований продукт**
> **Граф + контрольований sleep cycle + cross-agent namespace isolation + non-technical UX**

**Критичні gap'и:**
- Cognee: sleep — евристика, governance — слабка
- Slipstream: sleep є, граф — немає, Python — roadmap
- Zep/Graphiti: temporal граф є, sleep — немає, cross-agent — базово
- Mem0: mature SDK, граф тільки в Pro tier, sleep — немає

---

## 9. Ключові посилання (Консолідований Index)

### Наукові Papers
- [CoALA Framework](https://arxiv.org/abs/2309.02427) — таксономія пам'яті агентів
- [Survey 2026](https://arxiv.org/pdf/2603.07670) — comprehensive стан поля
- [Generative Agents](https://arxiv.org/abs/2304.03442) — episodic memory + reflection (Stanford)
- [Voyager](https://arxiv.org/abs/2305.16291) — procedural memory / skill library
- [MemGPT](https://arxiv.org/abs/2310.08560) — hierarchical memory
- [Reflexion](https://arxiv.org/abs/2303.11366) — reflective memory
- [AgeMem](https://arxiv.org/abs/2506.01551) — RL-based memory management
- [MAGMA](https://arxiv.org/abs/2501.13956) — multi-graph agentic memory
- [Mem0](https://arxiv.org/abs/2504.19413) — selective memory extraction (ECAI 2025)
- [SCM](https://arxiv.org/abs/2604.20943) — sleep-consolidated memory
- [SleepGate](https://arxiv.org/abs/2603.14517) — forgetting gate & conflict resolution
- [Language Models Need Sleep](https://openreview.net/forum?id=iiZy6xyVVE) — OpenReview 2025
- [MemoryArena](https://arxiv.org/abs/2602.16313) — multi-session benchmark
- [MemoryAgentBench](https://arxiv.org/abs/2507.05257) — 4-competency evaluation
- [LongMemEval](https://arxiv.org/abs/2410.10813) — single-agent long-term recall
- [LoCoMo](https://arxiv.org/abs/2402.17753) — multi-hop temporal reasoning
- [Memory Security](https://arxiv.org/abs/2604.16548) — privacy & sovereignty
- [RAG Foundational Work](https://arxiv.org/abs/2005.11401) — Lewis et al. 2020

### Комерційні продукти & Інструменти
- [Mem0](https://mem0.ai) — Memory as a service (51k+ stars)
- [Cognee](https://cognee.ai) — Graph memory engine ($7.5M)
- [Zep / Graphiti](https://getzep.com) — Temporal knowledge graph
- [Honcho](https://honcho.dev) — User dialectic modeling
- [ByteRover](https://byterover.dev) — Markdown context tree
- [Hindsight](https://hindsight.vectorize.io) — TEMPR retrieval (MIT)
- [OpenViking](https://github.com/volcengine/OpenViking) — Tiered context
- [Hermes Agent](https://hermes-agent.nousresearch.com) — MEMORY.md + providers
- [GEPA](https://github.com/NousResearch/hermes-agent-self-evolution) — Offline skill evolution

---

## Вихідні матеріали

- **Оригінальне дослідження:** ai_agent_memory_research.md (травень 2026)
- **Джерело:** Комбінація arXiv papers, GitHub stars, case studies, product docs
- **Статус:** Living document — оновлюється при виході нових papers

---

**Tags:** `ai-agents`, `memory-systems`, `nlp`, `rl`, `knowledge-graphs`, `benchmarks`, `research`
