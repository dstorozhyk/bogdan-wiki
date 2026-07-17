---
title: Agent Knowledge Review Queue
created: 2026-06-20
updated: 2026-07-16
type: query
tags: [wiki]
---

# Agent Knowledge Review Queue

Staging area for nightly consolidation candidates. Related: [[agent-knowledge-policy]], [[log]], [[index]].

## How to Use

- `[ ]` pending review
- `[x]` accepted/applied
- `[-]` rejected/no longer relevant

The nightly sleep job should prepend new candidates below.

---

## Pending Memory Candidates

- [ ] **2026-07-17 — Restore memory tool, then apply staged non-secret compaction**
  - Proposed change: compact `MEMORY.md` to high-signal project/config/routing pointers and replace the credential-bearing VPS Monitor user-memory entry with a non-secret endpoint plus secure-config pointer.
  - Why durable: live pressure remains `2024 / 2200` (92.0%) for MEMORY and `1358 / 1375` (98.8%) for USER.
  - Risk/staleness: retain identity, stable preferences, active roots, and essential non-secret configuration pointers; do not mirror credentials or keys in the wiki.
  - Evidence: 2026-07-17 nightly consolidation; one batched operation per target was attempted and returned unavailable.

- [ ] **2026-07-15 — Apply staged safe non-secret memory compaction after memory-tool repair**
  - Proposed change: compact `MEMORY.md` to concise project/config/routing pointers; replace the credential-bearing VPS Monitor user-memory content with a non-secret endpoint plus secure-config pointer.
  - Why durable: live pressure is `2024 / 2200` (92.0%) for MEMORY and `1358 / 1375` (98.8%) for USER.
  - Risk/staleness: retain identity, stable preferences, active roots, and essential non-secret configuration pointers; do not mirror credentials or keys in the wiki.
  - Evidence: 2026-07-15 nightly consolidation; one batched `memory` operation per target returned unavailable.

- [ ] **2026-07-14 — Apply staged non-secret memory compaction after memory-tool repair**
  - Proposed change: compact `MEMORY.md` into shorter project/config/routing pointers and replace the credential-bearing VPS Monitor user-memory line with a non-secret endpoint plus secure-config pointer.
  - Why durable: current live pressure is `2024 / 2200` (92.0%) for MEMORY and `1358 / 1375` (98.8%) for USER.
  - Risk/staleness: retain identity, stable preferences, active roots and essential config pointers; do not mirror credentials/keys in wiki.
  - Evidence: 2026-07-14 nightly consolidation; one batched `memory` operation failed because memory is unavailable in the cron environment.

- [ ] **2026-07-13 — Apply safe memory compaction when the memory tool is available**
  - Proposed change: compact `MEMORY.md` to preserve project roots, source pointers and routing rules; remove volatile cron IDs and verbose duplicate phrasing. Replace the VPS Monitor credential-bearing `USER.md` entry with a non-secret host/port and operational config pointer.
  - Why durable: live pressure remains `2024 / 2200` (`92.0%`) for MEMORY and `1358 / 1375` (`98.8%`) for USER.
  - Risk/staleness: retain identity, stable preferences and infrastructure pointers; never mirror credentials or keys into wiki.
  - Evidence: 2026-07-13 nightly consolidation; one batched operation per target was attempted but the memory tool is disabled/unavailable.

- [ ] **2026-07-12 — Proposed compaction for MEMORY.md; tool unavailable**
  - Proposed change: shorten verbose Rocket/wiki/specialist/media/Beauty entries and remove volatile cron IDs while retaining project roots, routing rules, and non-secret configuration pointers.
  - Why durable: `MEMORY.md` is `2024 / 2200` chars (`92.0%`), above threshold.
  - Risk/staleness: preserve source pointers; inspect live cron rather than retaining IDs.
  - Evidence: 2026-07-12 nightly consolidation; batched `memory` operation returned unavailable.

- [ ] **2026-07-12 — Proposed compaction for USER.md / secret minimization; tool unavailable**
  - Proposed change: replace raw VPS Monitor credential material with a non-secret host/port plus operational env/config pointer; keep identity, preferences, and reference location.
  - Why durable: `USER.md` is `1358 / 1375` chars (`98.8%`), above threshold.
  - Risk/staleness: do not lose the actual credential source or copy any secret into wiki.
  - Evidence: 2026-07-12 nightly consolidation; batched `memory` operation returned unavailable.

- [ ] **2026-07-11 — Proposed compaction for MEMORY.md still blocked by unavailable memory tool**
  - Proposed change: shorten Rocket, wiki-system, wiki-first, Ukraine-specialists, image/media, and Beauty public-profile entries; remove volatile cron IDs from always-on memory while preserving active project roots/source pointers and stable routing rules.
  - Why durable: `MEMORY.md` is `2024 / 2200` chars (`92.0%`), above the 80% compaction threshold; proposed replacements preserve high-signal operational pointers while reducing prompt pressure.
  - Risk/staleness: low if source-of-truth paths remain; verify live cron IDs before relying on schedule details.
  - Evidence: 2026-07-11 nightly consolidation; `memory` tool returned unavailable, so no mutation was applied.

- [ ] **2026-07-11 — Proposed compaction for USER.md / secret minimization still blocked**
  - Proposed change: replace raw VPS Monitor credential material with a non-secret pointer such as `VPS Monitor: 178.105.214.165:3000; credentials/keys live in operational env/config, not wiki/memory`; preserve identity, seniority, backend/Claude preference, Markdown preference, Lviv reference location, and CK3 Ukrainian-UI preference.
  - Why durable: `USER.md` is `1358 / 1375` chars (`98.8%`) and should not embed secrets in always-on prompt context.
  - Risk/staleness: must not lose the actual credential source; do not copy secrets into wiki.
  - Evidence: 2026-07-11 nightly consolidation; `memory` tool returned unavailable.

- [ ] **2026-07-11 — Game-purchase edition preference if Steam advice recurs**
  - Proposed text: `For Denys’s game-purchase advice, if he says he will “play once and forget,” favor Standard/discount over Deluxe/Ultimate unless extras add substantial story/gameplay.`
  - Why durable: captures a clear purchase-style preference from the Assassin’s Creed edition task.
  - Risk/staleness: validate across more game-purchase sessions before using scarce memory.
  - Evidence: `20260710_134926_0ceafcf6`.

- [ ] **2026-07-10 — Proposed compaction for MEMORY.md still blocked by unavailable memory tool**
  - Proposed change: shorten Rocket, wiki-system, wiki-first, Ukraine-specialists, image/media, broker-funding, and Beauty public-profile entries; remove volatile cron IDs from always-on memory while preserving active project roots/source pointers and stable routing rules.
  - Why durable: `MEMORY.md` is `2024 / 2200` chars (`92.0%`), above the 80% compaction threshold; proposed replacements preserve high-signal operational pointers while reducing prompt pressure.
  - Risk/staleness: low if paths/source-of-truth pointers remain; verify live cron IDs before relying on schedule details.
  - Evidence: 2026-07-10 nightly consolidation; `memory` tool returned unavailable, so no mutation was applied.

- [ ] **2026-07-10 — Proposed compaction for USER.md / secret minimization still blocked**
  - Proposed change: replace raw VPS Monitor credential material with a non-secret pointer such as `VPS Monitor: 178.105.214.165:3000; credentials/keys live in operational env/config, not wiki/memory`; preserve identity, backend/Claude preference, Markdown preference, Lviv reference location, and CK3 Ukrainian-UI preference.
  - Why durable: `USER.md` is `1358 / 1375` chars (`98.8%`) and should not embed secrets in always-on prompt context.
  - Risk/staleness: must not lose the actual credential source; do not copy secrets into wiki.
  - Evidence: 2026-07-10 nightly consolidation; `memory` tool returned unavailable.

- [ ] **2026-07-09 — Proposed compaction for MEMORY.md still blocked by unavailable memory tool**
  - Proposed change: shorten Rocket, wiki-system, wiki-first, image/media, broker-funding, and Beauty public-profile entries; remove volatile cron IDs from always-on memory; keep project roots/source pointers and stable routing rules.
  - Why durable: `MEMORY.md` is `2024 / 2200` chars (`92.0%`), above the 80% compaction threshold; proposed replacements preserve operational pointers while reducing prompt pressure.
  - Risk/staleness: low if active project roots and source-of-truth paths remain; verify live cron IDs before relying on schedules.
  - Evidence: 2026-07-09 nightly consolidation; memory tool returned unavailable, so no mutation was applied.

- [ ] **2026-07-09 — Proposed compaction for USER.md / secret minimization still blocked**
  - Proposed change: replace raw VPS Monitor credential material with a non-secret pointer such as `VPS Monitor: 178.105.214.165:3000; credentials/keys live in operational env/config, not wiki/memory`; keep identity, Claude Code preference, formatting preference, Lviv reference location, and CK3 UI-language preference.
  - Why durable: `USER.md` is `1368 / 1375` chars (`99.5%`) and should not embed secrets in always-on prompt context.
  - Risk/staleness: must not lose the actual credential source; do not copy secrets into wiki.
  - Evidence: 2026-07-09 nightly consolidation; memory tool returned unavailable.

- [ ] **2026-07-09 — CK3/Linux setup memory candidate if gaming support recurs**
  - Proposed text: `Denys’s CK3/Linux setup: HP Pavilion Power 15-cb0xx on Pop!_OS; CK3 works best via Proton on NVIDIA GTX 1050 (not Intel HD 630), medium settings ok; use English language when enabling Ukrainian Workshop localizer that replaces English.`
  - Why durable: could prevent repeated hardware/launch troubleshooting if CK3 support continues.
  - Risk/staleness: device setup, driver, Proton version, and Workshop mod IDs can change; prefer wiki note unless repeated often.
  - Evidence: `20260708_084508_c98db802`.

- [ ] **2026-07-08 — Proposed compaction for MEMORY.md still blocked by unavailable memory tool**
  - Proposed change: shorten Rocket, wiki-system, Ukraine-specialists, and Beauty entries; remove volatile cron IDs from always-on memory; keep project roots/source pointers and stable routing rules.
  - Why durable: `MEMORY.md` is `2024 / 2200` chars (`92.0%`), above the 80% compaction threshold; proposed replacements preserve operational pointers while reducing prompt pressure.
  - Risk/staleness: low if active project roots and source-of-truth paths remain; verify live cron IDs before relying on schedules.
  - Evidence: 2026-07-08 nightly consolidation; memory tool returned unavailable, so no mutation was applied.

- [ ] **2026-07-08 — Proposed compaction for USER.md / secret minimization still blocked**
  - Proposed change: replace raw VPS Monitor credential material with `VPS Monitor: 178.105.214.165:3000; credentials/keys live in operational env/config, not wiki/memory`; shorten infrastructure-access and preference lines while keeping identity, Claude Code preference, formatting preference, Lviv reference location, and CK3 Russian-UI preference.
  - Why durable: `USER.md` is `1368 / 1375` chars (`99.5%`) and should not embed secrets in always-on prompt context.
  - Risk/staleness: must not lose the actual credential source; do not copy secrets into wiki.
  - Evidence: 2026-07-08 nightly consolidation; memory tool returned unavailable.

- [ ] **2026-07-07 — Proposed compaction for MEMORY.md still blocked by unavailable memory tool**
  - Proposed change: shorten the Rocket, wiki-system, Ukraine-specialists, media-generation, broker-funding, and Beauty public-profile entries while keeping project roots, stable routing rules, and source pointers.
  - Why durable: `MEMORY.md` is `2024 / 2200` chars (`92.0%`), above the 80% compaction threshold; proposed replacements would reduce always-on prompt pressure without losing operational pointers.
  - Risk/staleness: low if volatile cron IDs and verbose wording are removed but active roots and core preferences remain; verify live cron IDs before relying on schedules.
  - Evidence: 2026-07-07 nightly consolidation; memory tool returned unavailable, so no mutation was applied.

- [ ] **2026-07-07 — Proposed compaction for USER.md / secret minimization still blocked**
  - Proposed change: replace raw VPS Monitor credential material in always-on user memory with a non-secret pointer to the secure operational config/credential location; keep identity, seniority, infrastructure access preference, Claude Code preference, formatting preference, and Lviv reference location.
  - Why durable: `USER.md` is `1294 / 1375` chars (`94.1%`) and should not embed secrets in prompt context.
  - Risk/staleness: must not lose the actual credential source; do not copy secrets into wiki.
  - Evidence: 2026-07-07 nightly consolidation; memory tool returned unavailable.

- [ ] **2026-07-06 — MAMENORI correction for Lviv sushi/NOA context**
  - Proposed text: `For Denys's Lviv sushi/place lookups, “sushi near NOA” referred to MAMENORI; do not default to Red Pepper / Yoki / ЯпонаХата for that context.`
  - Why durable: direct correction likely prevents repeat wrong recommendations in local restaurant lookups.
  - Risk/staleness: restaurants, hours, and quality can change; verify current location/hours before recommending.
  - Evidence: `20260705_175420_3a0830d4`.

- [ ] **2026-07-06 — Proposed memory compaction for MEMORY.md**
  - Proposed change: shorten the Rocket alert bot entry, remove volatile cron IDs from the wiki-system entry, and merge duplicate Beauty public-profile direction entries.
  - Why durable: `MEMORY.md` is at `2194 / 2200` chars (`99.7%`), above the 80% compaction threshold; compaction preserves high-signal routing/project pointers while reducing prompt pressure.
  - Risk/staleness: low if active project roots, stable preferences, wiki/source pointers, and config pointers are kept; verify live cron before relying on job IDs/schedules.
  - Evidence: 2026-07-06 nightly consolidation; memory tool returned unavailable, so no mutation was applied.

- [ ] **2026-07-06 — Proposed memory compaction for USER.md / secret minimization**
  - Proposed change: replace raw VPS Monitor credential material with a non-secret pointer to operational env/config/credential location; keep identity, seniority, infrastructure access preference, formatting preferences, and workflow preferences.
  - Why durable: `USER.md` is at `1294 / 1375` chars (`94.1%`) and should not embed secrets in always-on prompt context.
  - Risk/staleness: must not lose the actual credential source; do not copy secrets into wiki.
  - Evidence: 2026-07-06 nightly consolidation; memory tool returned unavailable, so no mutation was applied.

- [ ] **2026-07-05 — Proposed memory compaction for MEMORY.md**
  - Proposed change: shorten the Rocket alert bot memory, remove volatile cron IDs from the wiki-system memory, and merge duplicate Beauty public-profile direction entries.
  - Why durable: `MEMORY.md` is still at `2129 / 2200` chars (`96.8%`), above the 80% compaction threshold; compaction preserves high-signal routing/project pointers while reducing prompt pressure.
  - Risk/staleness: low if active project roots and stable preferences are kept; verify current cron before relying on schedule details.
  - Evidence: 2026-07-05 nightly consolidation; memory tool returned unavailable, so no mutation was applied.

- [ ] **2026-07-05 — Proposed memory compaction for USER.md / secret minimization**
  - Proposed change: replace raw VPS Monitor credential material with a non-secret pointer to operational env/config/credential location; keep Denys identity, seniority, access preference, formatting preferences, and key workflow preferences.
  - Why durable: `USER.md` is still at `1294 / 1375` chars (`94.1%`) and should not embed secrets in always-on prompt context.
  - Risk/staleness: must not lose the actual credential source; do not copy secrets into wiki.
  - Evidence: 2026-07-05 nightly consolidation; memory tool returned unavailable, so no mutation was applied.

- [ ] **2026-07-04 — Beauty Growth Assistant gated rebuild workflow**
  - Proposed text: `Beauty Growth Assistant rebuild should follow a gated workflow: approved business requirements → design → architecture → backend → frontend from approved design → QA → UX validation loop; core product is solo-master mobile-first CRM/booking with manual confirmation by default.`
  - Why durable: stable project direction and workflow guardrail for the active Beauty project.
  - Risk/staleness: may change after Denys reviews BRD/open questions.
  - Evidence: `20260703_145854_9a7ecf72`.

- [ ] **2026-07-04 — Proposed memory compaction for MEMORY.md**
  - Proposed change: shorten the Rocket alert memory, remove volatile cron IDs from the wiki-system memory, and merge duplicate Beauty public-profile direction entries.
  - Why durable: memory is at `2129 / 2200` chars (`96.8%`), above the 80% compaction threshold; compaction preserves routing/project pointers while reducing prompt pressure.
  - Risk/staleness: low if core pointers are kept; do not remove active project roots or stable preferences.
  - Evidence: 2026-07-04 nightly consolidation; memory tool unavailable, so no mutation was applied.

- [ ] **2026-07-04 — Proposed memory compaction for USER.md / secret minimization**
  - Proposed change: shorten the status/preferences line and remove raw VPS credential material from always-on memory, replacing it with a non-secret pointer to operational config/credential location.
  - Why durable: `USER.md` is at `1294 / 1375` chars (`94.1%`) and should avoid embedding secrets in the always-on prompt.
  - Risk/staleness: must not lose the actual credential source; do not copy secrets into wiki.
  - Evidence: 2026-07-04 nightly consolidation; memory tool unavailable, so no mutation was applied.

- [ ] **2026-07-03 — AI-assisted SDLC terminology for vibe-coded products**
  - Proposed text: `For Denys's vibe-coded product planning, use the wiki note /root/bogdan-wiki/research/ai-assisted-sdlc-vibe-coding-project-lifecycle-2026-07-02.md and frame early stages as AI-assisted SDLC with PoC/Prototype/RAT/Walking Skeleton/Vertical Slice/MLP/Pilot rather than defaulting to “MVP”.`
  - Why durable: stable terminology/preference pointer for future project planning.
  - Risk/staleness: terminology can evolve; use the note as a starting point, not a rigid taxonomy.
  - Evidence: `20260702_192700_19352d8d`.

- [ ] **2026-07-03 — Wise KYC should wait for pending broker transfer settlement**
  - Proposed text: `For Denys's Wise→broker route, if Wise asks to confirm Ukraine residence while broker transfers are still pending, prefer waiting until broker credit is confirmed and Wise balance is zero/minimal if there is no hard Wise deadline; do not advise fake residence data.`
  - Why durable: account/route-specific operational rule that reduces future transfer/KYC risk.
  - Risk/staleness: Wise country/product rules can change; verify current Wise prompts/help pages before high-stakes advice.
  - Evidence: `20260702_155655_553cd9a5`.

- [ ] **2026-07-02 — Emergency fund source-of-truth wiki files**
  - Proposed text: `Denys's emergency fund source of truth lives in /root/bogdan-wiki/research/emergency-fund-{dashboard,strategy,ovdp-research,usdt-usdc-research}.md; use those files before advising on podushka/stablecoin allocation.`
  - Why durable: stable wiki/source pointer that prevents repeated rediscovery of the emergency-fund strategy.
  - Risk/staleness: allocation and filenames can change; verify current wiki files before detailed advice.
  - Evidence: `20260701_110157_85b8c913`.

- [ ] **2026-07-01 — Front/UI work should be manual and not confuse UI kits with landing pages**
  - Proposed text: `For Denys's frontend/UI kit work, write frontend manually without “колода”/external UI generator unless explicitly asked, and do not replace a requested UI kit/design-system task with a landing page.`
  - Why durable: direct recurring workflow preference and correction.
  - Risk/staleness: term “колода” may refer to a specific tool; keep broad until clarified.
  - Evidence: `20260630_182440_b9e4ac` compacted context.

- [ ] **2026-07-01 — Beauty Growth Assistant preview routes**
  - Proposed text: `Beauty Growth Assistant project preview routes: /beauty/ is the UI kit/design page; /beauty/olena-nails is the standalone mobile-first client public profile. Latest public-profile commit observed: 0351b0e.`
  - Why durable: project route/config pointer useful for future continuation.
  - Risk/staleness: deployment URL, routes, and commit can change.
  - Evidence: `20260630_205901_297be096`.

- [ ] **2026-07-01 — Hermes deferred task queue operational paths**
  - Proposed text: `Hermes deferred task queue is installed under ~/.hermes/deferred-tasks with scripts ~/.hermes/scripts/deferred_tasks.py and ~/.hermes/scripts/deferred_task_watchdog.py; cron job ed23278d9458 runs the no-agent watchdog every 20m.`
  - Why durable: operational config pointer likely useful for future large tasks.
  - Risk/staleness: cron/job IDs and script paths may change after refactors.
  - Evidence: `20260630_191516_dda9ca32`, `20260630_192732_bb7b42`.

- [ ] **2026-06-30 — Mobile app ideas should use portfolio/business validation discipline**
  - Proposed text: `When Denys asks for smartphone app ideas, treat it as business-side portfolio research: use current market/app-store data, monetization evidence, distribution strategy, validation gates, and explicit kill/bankruptcy criteria before recommending development.`
  - Why durable: stable preference for future app-idea work and avoids generic ideation.
  - Risk/staleness: benchmarks and source availability change; keep the principle but refresh data.
  - Evidence: `20260629_175146_d78a7cb1`, `cron_54b894b9fd7d_20260630_000558`.

- [ ] **2026-06-30 — Micro-SaaS feature discovery should be evidence-first**
  - Proposed text: `When Denys asks for micro-SaaS feature discovery or business analysis, derive features from the business flow plus internet evidence: competitors, reviews/pain, pricing, monetization, onboarding, validation, and prioritization; avoid vibe-based feature lists.`
  - Why durable: recurring workflow preference and quality bar for future business-analysis tasks.
  - Risk/staleness: exact frameworks/tools may evolve, but the evidence-first preference is stable.
  - Evidence: `20260629_183354_7d362b1f`.

- [ ] **2026-06-30 — Beauty Growth Assistant project location**
  - Proposed text: `Beauty Growth Assistant prototype lives at /opt/apps/beauty-growth-assistant and GitHub repo https://github.com/dstorozhyk/beauty-growth-assistant; initial scaffold commit is d6fc4a3.`
  - Why durable: project location/config pointer useful for future continuation.
  - Risk/staleness: repo path, branch, deploy status, and commit pointer can change.
  - Evidence: `20260629_183841_50ab40de`.

- [ ] **2026-06-25 — Freedom cash-like UCITS ETF ticker mapping**
  - Proposed text: `Freedom/Freedom24 showed the accumulating SGOV-like UCITS ETF as IB01.EU; verify ISIN IE00BGSF1X88 before buying. Related cash-like UCITS candidates discussed: IB01/IE00BGSF1X88 for 0–1yr US Treasuries, IBTA/IE00BYXPSP02 for 1–3yr, IBTE/IE00BDFK1573 for EUR-hedged 1–3yr.`
  - Why durable: account/platform-specific lookup that can prevent repeated ETF-symbol discovery.
  - Risk/staleness: broker ticker suffixes, availability, yields, and tax treatment can change; treat as symbol lookup, not investment advice.
  - Evidence: `20260624_151903_aef3232f`.

- [ ] **2026-06-24 — Broker funding route confirmed with 0 EUR observed fee**
  - Proposed text: `Broker funding confirmed: Raiffeisen EUR → Wise EUR balance/main account → Freedom/Freedom24 EUR credited successfully; observed test transfer 8.72 EUR arrived as 8.72 EUR, implying 0 EUR route fee if no separate Wise/bank fee exists.`
  - Why durable: account-specific route confirmation that should prevent repeated exploration of Paysera/SWIFT/card alternatives for the same workflow.
  - Risk/staleness: financial rails and account rules can change; mark as confirmed as of 2026-06-23.
  - Evidence: `20260623_120149_3bb6c070`.

- [ ] **2026-06-23 — Broker funding confirmed candidate route**
  - Proposed text: `Broker funding: current best candidate route is Raiffeisen EUR → Wise EUR balance/main account → Freedom24/Freedom Finance Europe EUR. Avoid Paysera, direct SWIFT, direct broker card top-up, Wise card payment, and USD→EUR conversion for this flow; verify final route after Freedom credits funds.`
  - Why durable: account-specific correction that prevents repeated bad recommendations for Denys's broker-funding workflow.
  - Risk/staleness: route is not fully final until Freedom credits funds; financial rails/compliance can change.
  - Evidence: `20260622_163026_d7eee1f1`.

## Pending Skill Candidates

- [ ] **2026-07-17 — Human review of critical-skill pinning from repeated telemetry**
  - Proposed action: explicitly decide whether high-impact skills such as `obsidian`, `claude-code`, `youtube-content`, `gemini-and-notebooklm`, and Hermes operational runbooks should be pinned.
  - Evidence: nightly telemetry from 2026-07-07 through 2026-07-17; current usage: 113 tracked, `obsidian` activity 53, and curator reports 80 agent-created skills active with none stale/archived.
  - Boundary: pinning is a human lifecycle decision; nightly consolidation must not pin, archive, delete, install, or consolidate automatically.

- [ ] **2026-07-15 — Human review of critical-skill pinning from repeated telemetry**
  - Proposed action: explicitly decide whether high-impact skills such as `obsidian`, `claude-code`, `youtube-content`, `gemini-and-notebooklm`, and Hermes operational runbooks should be pinned.
  - Evidence: nightly telemetry from 2026-07-07 through 2026-07-15; current usage: 113 tracked, `obsidian` activity 51, and curator reports 80 agent-created skills active with none stale/archived.
  - Boundary: pinning is a human lifecycle decision; nightly consolidation must not pin, archive, delete, install, or consolidate automatically.

- [ ] **2026-07-14 — Human review of critical-skill pinning from repeated telemetry**
  - Proposed action: explicitly decide whether high-impact skills such as `obsidian`, `claude-code`, `youtube-content`, `gemini-and-notebooklm`, and Hermes operations runbooks should be pinned.
  - Evidence: repeated nightly telemetry reviews (2026-07-07–14); current usage shows `obsidian` activity 50 and curator reports 80 agent-created skills active, none stale/archived.
  - Boundary: this is a human lifecycle decision; nightly consolidation must not pin, archive, delete, install or consolidate automatically.

- [ ] **2026-07-12 — Fact-check before broadening `ck3-economic-vassal-play`**
  - Proposed action: verify and then narrowly patch `gaming/ck3-economic-vassal-play/SKILL.md` for council eligibility, faith-defined criminal status, inherited claims, and papal/event claims.
  - Trigger: Denys’s recurring Ukrainian-UI CK3 coaching now includes council and dynasty questions, not only economy.
  - Evidence: 3 sessions across 2026-07-09–11: `20260709_144322_da2aa910`, `20260710_211638_149336a6`, `20260711_121523_815dd800`.
  - Blocker: the latest answer made conflicting unverified claims about secular council eligibility. Do not encode it until an in-game tooltip/current source confirms the rule.

- [ ] **2026-07-11 — Broaden/review CK3 coaching skill beyond economy**
  - Proposed skill name: update `ck3-economic-vassal-play` or create broader `ck3-strategy-coach`.
  - Trigger: Denys asks CK3 beginner questions beyond economy: marriage acceptance, dynastic succession, claims, council roles, court recruitment, female council eligibility, intrigue.
  - Reusable workflow: answer in Ukrainian with Ukrainian UI labels; inspect screenshots when present; distinguish marriage/claim/succession mechanics; provide ordered click/check steps; preserve low-expansion roleplay constraints unless Denys pivots.
  - Include pitfalls/verification: do not overclaim exact CK3 localization names; verify war goal/succession before advising inheritance schemes; do not treat traits like `Блудниця` as hard council blockers without checking eligibility rules.
  - Evidence: `20260710_211638_149336a6`, `20260709_144322_da2aa910`.

- [ ] **2026-07-11 — Review `steam-game-purchase-advice` after first real use**
  - Proposed action: keep for now; review after a few more edition/DLC/bundle tasks to decide whether it stays standalone or merges into a broader gaming purchase/research workflow.
  - Trigger: Denys asks whether to buy a specific game edition/DLC/bundle.
  - Reusable workflow: compare live store prices, edition contents, DLC substance vs cosmetics, likely discount cadence, and Denys’s intended play style (`one-and-done` vs completionist/live-service).
  - Include pitfalls/verification: source-first price/content lookup; use arithmetic tools for price deltas; avoid hallucinating edition contents; distinguish remake/new release from old editions when store/search results are confusing.
  - Evidence: `20260710_134926_0ceafcf6`; usage sidecar now shows `steam-game-purchase-advice` active.

- [ ] **2026-07-11 — Update `hermes-update-operations` for interrupted update resume**
  - Proposed skill name: update `hermes-update-operations`.
  - Trigger: Hermes update/gateway restart interrupts an active session after local patches were backed up/stashed.
  - Reusable workflow: find backup path, inspect git status/stash, verify `hermes --version`, resume/complete update, reapply local patches as needed, run `hermes doctor`, verify gateway services and cron `[SILENT]` behavior.
  - Include pitfalls/verification: `git stash list`, `/tmp/hermes_update_backup_path`, backup dir under `~/hermes-update-backups/`, `systemctl status hermes-gateway*`; pitfall: do not blindly continue if production/gateway state is unclear after restart.
  - Evidence: `20260710_075319_5503656c`.

- [ ] **2026-07-11 — Refresh skill pin/review candidates from usage telemetry**
  - Proposed action: review whether to pin critical operational skills: `obsidian`, `hermes-agent`, `wiki-knowledge-pipelines`, `claude-code`, `gemini-web-controller`, `hermes-deferred-task-queue`, `hermes-update-operations`, `youtube-content`, and promoted production/project runbooks.
  - Rationale: these are high-activity or high-impact skills where accidental archive/removal would be costly; pinning should remain explicit, not automatic from SAFE MODE.
  - Evidence: `/root/.hermes/skills/.usage.json` and `hermes curator status` in 2026-07-11 nightly consolidation; 113 tracked skills, 57 zero-use, curator enabled with no changes.

- [ ] **2026-07-10 — Review new `ck3-economic-vassal-play` skill after more real CK3 coaching**
  - Proposed action: keep for now; after 2–3 more CK3 sessions, decide whether it should stay standalone, merge into a broader CK3 skill, or be mirrored mainly as a wiki playbook.
  - Trigger: Denys asks CK3 economy/roleplay/count-under-liege questions with Ukrainian UI terms.
  - Reusable workflow: use Ukrainian UI labels; preserve Denys's peaceful/economic roleplay constraint; prioritize control, economic buildings, development, reserve, hooks, liege politics, council roles, activities, and practical “what to click/check” guidance.
  - Include pitfalls/verification: avoid Russian UI terms unless Denys switches back; avoid default conquest-first advice; verify answers include a practical ordered checklist and reserve/risk caveats.
  - Evidence: `20260709_144322_da2aa910`; skill was created and used once during the session.

- [ ] **2026-07-10 — Refresh skill pin/review candidates from usage telemetry**
  - Proposed action: review whether to pin critical operational skills: `obsidian`, `hermes-agent`, `wiki-knowledge-pipelines`, `claude-code`, `gemini-web-controller`, `hermes-deferred-task-queue`, `hermes-update-operations`, `youtube-content`, and promoted production/project runbooks.
  - Rationale: these are high-activity or high-impact skills where accidental archive/removal would be costly; pinning should remain explicit, not automatic from SAFE MODE.
  - Evidence: `/root/.hermes/skills/.usage.json` and `hermes curator status` in 2026-07-10 nightly consolidation; 113 tracked skills, 60 zero-use, curator enabled with no changes.

- [ ] **2026-07-09 — Create/update CK3 Linux/Proton setup runbook if support recurs**
  - Proposed skill name: `ck3-linux-proton-setup` or update `game-walkthrough-visual-guidance` / `steam-game-purchase-advice`.
  - Trigger: Denys asks about CK3 on Linux/Pop!_OS, Proton/native choice, NVIDIA hybrid graphics, performance settings, or Workshop localization.
  - Reusable workflow: inspect hardware/driver output; force NVIDIA/Hybrid launch options; choose Proton if native lags; set low/medium graphics with FPS cap; enable shader pre-caching; preserve Proton prefix/shader cache; explain Russian/UI labels in Ukrainian.
  - Include pitfalls/verification: `system76-power graphics`, Steam launch options `__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia gamemoderun %command%`, `sudo apt install gamemode`; pitfall: Steam may launch on Intel HD 630 unless NVIDIA offload is explicit; Ukrainian localizer may require Steam game language `English`.
  - Evidence: `20260708_084508_c98db802`.

- [ ] **2026-07-09 — Review new `steam-game-purchase-advice` skill after first real use**
  - Proposed action: keep for now, then review whether it overlaps with existing gaming/product-research skills after the first Steam edition/DLC/bundle task.
  - Rationale: usage sidecar shows it was agent-created on 2026-07-08, patched once, and has 0 use/view so far; new zero-use is not enough archive evidence.
  - Evidence: `/root/.hermes/skills/.usage.json` and 2026-07-09 nightly consolidation.

- [ ] **2026-07-08 — Create/update CK3 Ukrainian/Russian-interface coaching skill if game help recurs**
  - Proposed skill name: `ck3-ukrainian-russian-ui-coach` or update `game-walkthrough-visual-guidance` with CK3 strategy-coaching guidance.
  - Trigger: Denys asks about Crusader Kings 3 mechanics, strategy, screenshots, or “how do I play” questions while using Russian UI.
  - Reusable workflow: answer in Ukrainian, include Russian in-game labels, map abstract strategy/Machiavelli concepts to actual CK3 buttons/mechanics, distinguish direct actions from passive modifiers/events, and give immediate next actions plus risk checks.
  - Include pitfalls/verification: use vision on screenshots; do not hallucinate unavailable CK3 buttons; avoid long lore unless asked; ask for exact screenshot/state only when it changes the tactical recommendation.
  - Evidence: `20260706_193417_6f92bafb`, `20260707_182842_7d5b042a`.

- [ ] **2026-07-08 — Refresh skill pin/review candidates from usage telemetry**
  - Proposed action: review whether to pin critical operational skills: `obsidian`, `hermes-agent`, `wiki-knowledge-pipelines`, `claude-code`, `gemini-web-controller`, `hermes-deferred-task-queue`, `hermes-update-operations`, `youtube-content`, and promoted production/project runbooks.
  - Rationale: these are high-activity or high-impact skills where accidental archive/removal would be costly; pinning should remain explicit, not automatic from SAFE MODE.
  - Evidence: `/root/.hermes/skills/.usage.json` and `hermes curator status` in 2026-07-08 nightly consolidation; 111 tracked skills, 57 zero-use, curator enabled with no changes.

- [ ] **2026-07-07 — Create/update media wallpaper outpaint QA workflow**
  - Proposed skill name: `media-wallpaper-outpaint-qa` or update `gemini-web-controller` / creative media workflow.
  - Trigger: Denys asks to turn a found/screenshot image into desktop wallpaper, upscale, outpaint, or “догенеруй правильно через gweb”.
  - Reusable workflow: identify original/source image; download/verify dimensions; create candidate canvases; run outpaint/upscale; verify file exists and visually QA before promising or sending; compare candidates; only deliver final `MEDIA:` after successful file size/dimension check and visual pass.
  - Include pitfalls/verification: `file`, PIL dimension checks, `test -s`, visual QA; avoid claiming a generated variant exists before checking; don’t send weak intermediates unless user asks; if Gemini/browser generation fails, explicitly report the blocker and best verified candidate.
  - Evidence: `20260706_074551_d8ebfdbc` ended with “Не бачу” and no verified ready 78% wallpaper file.

- [ ] **2026-07-07 — Skill pin/review candidates from usage telemetry**
  - Proposed action: review whether to pin critical operational skills: `obsidian`, `hermes-agent`, `wiki-knowledge-pipelines`, `claude-code`, `gemini-web-controller`, `hermes-deferred-task-queue`, `hermes-update-operations`, and recurring production/project runbooks once promoted.
  - Rationale: these are high-activity or high-impact skills where accidental archive/removal would be costly; pinning should still be explicit, not automatic from SAFE MODE.
  - Evidence: `/root/.hermes/skills/.usage.json` and `hermes curator status` in 2026-07-07 nightly consolidation.

- [ ] **2026-07-06 — Update/create Freylina YouTube pipeline operations runbook**
  - Proposed skill name: update/create Freylina `youtube-to-wiki-pipeline` / operations runbook.
  - Trigger: Freylina YouTube cron reports missing `devops/youtube-to-wiki-pipeline`, duplicate queues, or already-processed pending videos.
  - Reusable workflow: distinguish stale default-profile cron jobs from canonical `freylina` profile script-only jobs; inspect canonical and nested `.pending-videos.json`; check `video-log.json`; verify page files exist; clear stale nested duplicates only after confirming already processed; smoke-test wrappers; verify `hermes -p freylina cron list --all`.
  - Include pitfalls/verification: `hermes cron list --all`, `hermes -p freylina cron list --all`, `python3 /root/.hermes/profiles/freylina/scripts/video-analyzer-cron.py`, inspect `/root/.hermes/profiles/freylina/wiki/.pending-videos.json` and `/root/.hermes/profiles/freylina/home/.hermes/profiles/freylina/wiki/.pending-videos.json`; pitfall: default profile can contain stale duplicate jobs with missing skills even when the freylina profile is healthy.
  - Evidence: `20260705_113458_df8d2751`.

- [ ] **2026-07-06 — Document PDF-to-wiki extraction pattern if repeated**
  - Proposed skill name: update `ocr-and-documents` or create a narrow `document-to-wiki-ingest` workflow if Denys repeats “process, understand, remember this document”.
  - Trigger: Denys sends PDFs/documents and asks to process them for future use.
  - Reusable workflow: extract with PyMuPDF, write a focused wiki note, add only a compact source pointer/correction to memory when pressure allows, and verify the created note by reading it back.
  - Include pitfalls/verification: install `pymupdf` in the active env if missing; verify page count/chars; do not add long summaries to memory; avoid raw transcript dumps; if memory is above pressure, stage pointer/compaction instead of adding.
  - Evidence: `20260705_205457_e86ffdf2`.

- [ ] **2026-07-05 — Repair/consolidate Freylina YouTube pipeline skill reference**
  - Proposed skill name: repair/consolidate Freylina `youtube-to-wiki-pipeline` profile reference.
  - Trigger: Freylina cron starts with “Skill(s) not found and skipped: devops/youtube-to-wiki-pipeline”.
  - Reusable workflow: check Freylina profile skill inventory/reference, canonical queue, stale nested queue, `video-log.json`, existing pages, and git HEAD; if queue is empty or videos are already processed, report no-op instead of duplicating pages.
  - Include pitfalls/verification: inspect `/root/.hermes/profiles/freylina/wiki/.pending-videos.json`, `/root/.hermes/profiles/freylina/home/.hermes/profiles/freylina/wiki/.pending-videos.json`, `video-log.json`, `git status --short`, `git log -1 --oneline`; pitfall: dotfile queue discovery may require explicit path/Python traversal rather than filename search.
  - Evidence: `cron_ef9b3fb5feed_20260705_030040`.

- [ ] **2026-07-04 — Update/create Beauty CRM rebuild workflow skill**
  - Proposed skill name: update `beauty-saas-product-design` or create `beauty-crm-rebuild-workflow`.
  - Trigger: Denys asks to rebuild/design/implement the Beauty Growth Assistant CRM/booking product.
  - Reusable workflow: enforce BRD/PRD approval, design gate, architecture gate, backend implementation, frontend from approved design only, automated/manual QA, and repeated UX validation loop before shipping.
  - Include pitfalls/verification: keep docs under `/opt/apps/beauty-growth-assistant/docs/beauty-crm-rebuild/`; do not return only local paths when Denys needs content in Telegram; verify mobile 390px UX; avoid generic dashboard/fake metrics; public page must not use CRM/SaaS/admin language.
  - Evidence: `20260703_145854_9a7ecf72`.

- [ ] **2026-07-04 — Update Claude/Hermes ops skill for Claude Code update verification**
  - Proposed skill name: update `claude-code` or `hermes-update-operations`.
  - Trigger: updating Claude Code on this VPS.
  - Reusable workflow: check `claude --version`, npm global package, package metadata, and executable path; tolerate `claude doctor` hanging if bounded by timeout and other checks pass.
  - Include pitfalls/verification: `npm install -g @anthropic-ai/claude-code@latest`, `npm list -g @anthropic-ai/claude-code --depth=0`, `claude --version`, `node -p "require('/root/.hermes/node/lib/node_modules/@anthropic-ai/claude-code/package.json').version"`; pitfall: full `claude doctor` can hang.
  - Evidence: `20260703_065217_4498a970`.

- [ ] **2026-07-04 — Repair/consolidate Freylina YouTube pipeline skill reference**
  - Proposed skill name: repair/consolidate Freylina `youtube-to-wiki-pipeline` profile reference.
  - Trigger: Freylina cron starts with “Skill(s) not found and skipped: devops/youtube-to-wiki-pipeline”.
  - Reusable workflow: check Freylina profile skill path/reference, canonical queue, nested stale queue, processed `video-log.json`, and git HEAD; do not mutate another profile except in explicitly scoped repair mode.
  - Include pitfalls/verification: read `/root/.hermes/profiles/freylina/wiki/.pending-videos.json`, `video-log.json`, git status/HEAD; avoid treating an empty queue as failure.
  - Evidence: `cron_ef9b3fb5feed_20260704_030027`.

- [ ] **2026-07-03 — Update `rocket-attack-alarm-ops` for migration permissions + aftermath false positives**
  - Proposed skill name: update `rocket-attack-alarm-ops`.
  - Trigger: Rocket bot is in restart-loop after migration/deploy, or false positives are sent for attack aftermath reports.
  - Reusable workflow: inspect Docker `RestartCount`, logs, `/health`/`/ready`; run a foreground/debug container if needed; check copied migration file permissions in both `src/database/migrations` and `dist/database/migrations`; normalize unreadable migration files to `644`; run focused tests/build; redeploy; verify container health and readiness; for aftermath false positives, query recent `alert_outbox`, add strong report patterns and regression tests before deploy.
  - Include pitfalls/verification: `docker inspect rocket-attack-alarm`, `docker compose -f docker-compose.prod.yml up -d --build bot`, `stat -c '%a %U:%G %n' src/database/migrations/*.sql dist/database/migrations/*.sql`, `chmod 644 ...`, `npm run test:report-filter`, `npm run build`, `curl http://127.0.0.1:9090/ready`; pitfall: words like `зараз`/`зафіксовано` can appear in retrospective casualty/cleanup reports and should not automatically make them live alerts.
  - Evidence: `20260702_060227_507ddd8d`.

- [ ] **2026-07-03 — Create/update `ai-assisted-sdlc-product-planning`**
  - Proposed skill name: create/update `ai-assisted-sdlc-product-planning`.
  - Trigger: Denys asks how to structure a vibe-coded/AI-built product, or asks “PoC vs MVP vs something else”.
  - Reusable workflow: choose the first artifact type by the risk being tested: PoC for feasibility, Prototype for UX, RAT for riskiest assumption, Spike for implementation uncertainty, Walking Skeleton for end-to-end technical foundation, Vertical Slice for one complete scenario, MLP for polished first user value, MMP/Pilot for marketable controlled launch.
  - Include pitfalls/verification: use wiki note `research/ai-assisted-sdlc-vibe-coding-project-lifecycle-2026-07-02.md`; produce an AI-assisted SDLC brief with product intent, artifact type, core scenario, acceptance criteria, architecture guardrails, AI-agent rules, and definition of done; pitfall: do not call every early artifact “MVP”.
  - Evidence: `20260702_192700_19352d8d`.

- [ ] **2026-07-02 — Update `rocket-attack-alarm-ops` for restart-loop/OOM production debugging**
  - Proposed skill name: update `rocket-attack-alarm-ops`.
  - Trigger: Rocket bot misses alerts, health endpoint is down, Docker container is restarting, or logs show Node.js heap out-of-memory.
  - Reusable workflow: inspect `docker inspect` RestartCount/OOMKilled/ExitCode and recent events/logs; if production stop/restart/debug is destructive, require explicit approval; run a debug container on a separate health port if possible; capture exact startup error; apply fix; run focused tests/build; redeploy and verify `/health`/`/ready` plus live channel monitoring.
  - Include pitfalls/verification: `docker inspect rocket-attack-alarm`, `docker events --since=... --filter container=rocket-attack-alarm`, foreground debug run with env/data mounts and alternate `HEALTH_PORT`; pitfall: a restart-loop means no Telegram monitoring even if source channels have messages; Hermes may block `docker stop`/production restart without explicit user confirmation.
  - Evidence: `20260701_215059_abd2456d`.

- [ ] **2026-07-01 — Review/update `beauty-saas-product-design` for standalone public profile route and no-photo rules**
  - Proposed skill name: review/update `beauty-saas-product-design`.
  - Trigger: designing Beauty Growth Assistant public profiles, no-photo variants, UI kit vs client-facing visit-card pages.
  - Reusable workflow: keep `/beauty/` as UI kit/design surface and `/beauty/<slug>` as client-facing standalone profile; strip CRM/dashboard/SaaS copy from public pages; use service-first no-photo headers; verify via build/lint/deploy/browser screenshot; commit/push.
  - Include pitfalls/verification: run `npm run build`, `npm run lint`, deploy `dist/` to `/var/www/beauty-growth-assistant`, `nginx -t`, `systemctl reload nginx`, browser verify `/beauty/` and `/beauty/olena-nails`; pitfall: fake monogram no-photo headers look artificial; avoid storing preview credentials.
  - Evidence: `20260630_182440_b9e4ac`, `20260630_205901_297be096`.

- [ ] **2026-07-01 — Review/update `hermes-deferred-task-queue` runbook**
  - Proposed skill name: review/update `hermes-deferred-task-queue`.
  - Trigger: large Hermes tasks risk provider limits or context exhaustion and need automatic continuation.
  - Reusable workflow: create task/progress/artifact files, capture session id, watchdog picks `pending/`, runs `hermes --resume <session_id> chat -Q -q ...`, moves tasks to `done/failed`, stays silent when idle or rate-limited.
  - Include pitfalls/verification: run `python3 -m py_compile ~/.hermes/scripts/deferred_tasks.py ~/.hermes/scripts/deferred_task_watchdog.py`, `python3 ~/.hermes/scripts/deferred_tasks.py create/list/show`, `HERMES_DEFERRED_DRY_RUN=1 python3 ~/.hermes/scripts/deferred_task_watchdog.py`, `hermes cron list`; verify no pending produces empty stdout and self-test reaches `done/`.
  - Evidence: `20260630_191516_dda9ca32`, `20260630_192732_bb7b42`.

- [ ] **2026-07-01 — Update `hermes-update-operations` for Jun 30 Hermes/Claude update and gateway restart handling**
  - Proposed skill name: update `hermes-update-operations`.
  - Trigger: Hermes/Claude updates on a gateway-hosting VPS, especially when reports fail or local patches must survive update.
  - Reusable workflow: inspect cron output and gateway logs; backup local patches; run `hermes update`, `hermes doctor --fix`, `hermes doctor`, `claude update`, Claude smoke test; confirm direct-script custom commands and cron `[SILENT]` behavior; restart gateways via delayed `systemd-run` rather than direct restart inside gateway.
  - Include pitfalls/verification: backup path `/root/hermes-update-backups/YYYYMMDD_HHMMSS/local-patches.patch`; run `hermes --version`, `claude --version`, `claude -p 'Reply with exactly: OK' --max-turns 1 --model haiku`; pitfall: default gateway restart may hang until current response delivery completes.
  - Evidence: `20260630_194546_704e6fbb`.

- [ ] **2026-06-29 — Update `game-walkthrough-visual-guidance` with annotated map-tile workflow**
  - Proposed skill name: update `game-walkthrough-visual-guidance`.
  - Trigger: user is stuck locating an in-game objective and asks for a drawn/visual map rather than more text directions.
  - Reusable workflow: identify exact quest/location; search for a reliable interactive/static map; if browser rendering fails, fetch map page assets/tiles directly; crop the relevant area; draw labels, route, and target marker; verify the output image visually before sending.
  - Include pitfalls/verification: use `requests`/PIL for tile downloads and annotation when browser navigation times out; inspect JS/assets for tile URL patterns and coordinate conventions; verify labels are not cropped; avoid overclaiming exact routes when coordinates are approximate.
  - Evidence: `20260628_202416_b4f12782`.

- [ ] **2026-06-26 — Update `rocket-attack-alarm-ops` for source-channel repeat alerts + `/updates` toggle**
  - Proposed skill name: update `rocket-attack-alarm-ops`.
  - Trigger: changing active-threat deduplication, repeat notifications, update-news broadcasts, command menu, dashboard tracking, or production deploys for `/opt/apps/rocket-attack-alarm`.
  - Reusable workflow: model 30-minute locks with `sourceChannel`; allow repeat notification only when the same active threat comes from the channel that created the lock; keep cross-channel suppression; add/update regression tests; implement `/updates` as a single toggle rather than separate on/off commands; update `/help`, Telegram command menu, scheduled update text, dashboard metrics, and container dry-run.
  - Include pitfalls/verification: run `npm run test:deduplication`, `npx tsc --noEmit`, `npm run test:dashboard`, `npm run updates:send -- --dry-run`, `npm run build`, `docker compose -f docker-compose.prod.yml up -d --build bot`, health checks, and `docker exec rocket-attack-alarm node dist/scripts/send-update-notification.js --dry-run`; pitfall: wording “уточнює” is too weak/incorrect for new launches or new waves.
  - Evidence: `20260625_180939_5df7944e`.

- [ ] **2026-06-25 — Update `rocket-attack-alarm-ops` for city-suggestion live DB + real bot broadcast**
  - Proposed skill name: update `rocket-attack-alarm-ops`.
  - Trigger: adding city suggestions/filters, updating live DB, or sending Rocket bot user broadcasts.
  - Reusable workflow: separate city vs district filters when needed; update seed keywords and regression tests; backup live DB before insertion; insert missing `locations_hierarchy` rows; verify FTS lookup; mark `city_suggestions` as `added`; send subscriber announcements from inside the bot container, not by scheduling an origin-chat cron response.
  - Include pitfalls/verification: run `npm run test:location-seeds`, `npm run build`; create DB backup under `/opt/apps/rocket-attack-alarm/data/backups/manual/`; verify inserted rows and FTS; use `docker exec rocket-attack-alarm` so `TELEGRAM_BOT_TOKEN` stays in container env; pitfall: one-shot Hermes cron delivery to origin chat is not a Telegram bot broadcast.
  - Evidence: `20260624_072541_0e1e451a`, `cron_e717319bd742_20260624_093041`.

- [ ] **2026-06-25 — Update/create Freylina YouTube-to-wiki pipeline runbook for cron-safe paths**
  - Proposed skill name: update/create Freylina `youtube-to-wiki-pipeline` runbook.
  - Trigger: Freylina YouTube fetcher/analyzer cron failure, missing `devops/youtube-to-wiki-pipeline`, or queued @vse_pro_royal videos.
  - Reusable workflow: use absolute Freylina profile paths; fetch @vse_pro_royal videos; generate wiki pages with deterministic title heuristics when LLM/OAuth is unavailable; update `video-log.json`, clear `.pending-videos.json`, commit/push, verify cron jobs.
  - Include pitfalls/verification: avoid `Path.home()` because Freylina cron HOME may become `/root/.hermes/profiles/freylina/home`; verify with `py_compile`, JSON validation, `hermes -p freylina skills list`, scheduler tick/cron list, `git status --short`, and latest commit hash; investigate why Jun 25 cron still reports missing skill despite the Jun 24 repair.
  - Evidence: `20260624_055648_7bbd60f9`, `cron_ef9b3fb5feed_20260625_030044`.

- [ ] **2026-06-24 — Update `rocket-attack-alarm-ops` for state-based dedup + disk-full recovery**
  - Proposed skill name: update `rocket-attack-alarm-ops`.
  - Trigger: changing Rocket bot deduplication, production deploy/restart, or recovering bot container failures.
  - Reusable workflow: add regression tests for semantic duplicates; implement threat-status keying by user/filter/category; keep content-hash dedup; run focused tests/build; deploy Docker; verify `/health`, `/ready`, runtime dedup probe; if SQLite fails due to disk full, clean Docker cache/images, remove broken WAL/SHM only after stopping the container, then restart.
  - Include pitfalls/verification: run `npm run test:deduplication`, `npm run test:mig-nationwide`, `npm run build`, `docker compose -f docker-compose.prod.yml up -d --build bot`, `curl http://127.0.0.1:9090/health`, `curl http://127.0.0.1:9090/ready`, `df -h /`; clarify that “same threat later” is inferred only from another same-status message, not a separate authoritative continuous state.
  - Evidence: `20260623_192047_4f643f`.

- [ ] **2026-06-24 — Update `crypto-fiat-onramps` for Binance P2P → WhiteBIT workflow**
  - Proposed skill name: update `crypto-fiat-onramps`.
  - Trigger: Denys asks for cheapest UAH→USDT or Binance/WhiteBIT route.
  - Reusable workflow: compare WhiteBIT spot + actual UAH deposit fee against Binance/Bybit P2P; treat Binance P2P→WhiteBIT as main practical path when WhiteBIT direct is expensive; inspect screenshots for auto-selected bad offers; advise manual Binance P2P filter/sorting and network compatibility before withdrawal.
  - Include pitfalls/verification: timestamp quotes; calculate effective UAH/USDT with a tool; avoid ERC20 unless explicitly acceptable; verify WhiteBIT supports the selected withdrawal network; warn that Binance “Buy Crypto” auto flow may show worse rates than manual P2P.
  - Evidence: `20260623_193417_3dd79fc7`.

- [ ] **2026-06-23 — Update `rocket-attack-alarm-ops` for air-alert API + city suggestions**
  - Proposed skill name: update `rocket-attack-alarm-ops`.
  - Trigger: adding/changing Rocket bot alert data sources, city suggestions, user broadcasts, or production deploys.
  - Reusable workflow: inspect suggestions DB; avoid duplicating cities already in seeds/live DB; mark suggestions `added/reviewed/rejected`; add source-specific tests; route synthetic API messages through `MonitorService.processSyntheticMessage`; run focused tests + TypeScript/build; deploy via `docker compose -f docker-compose.prod.yml up -d --build bot`; verify `/health`, logs, runtime channel list, API baseline, and broadcast dry-runs.
  - Include pitfalls/verification: public endpoint `https://ubilling.net.ua/aerialalerts/`; baseline on startup to avoid mass notifications; clear messages should remain non-alert; foreground debug container timeouts/SIGTERM can look like restart loops; verify `npm run test:city-suggestions`, `npm run test:location-seeds`, `npm run test:air-alert-api`, `npx tsc --noEmit`, `npm run build`, Docker health, and `Air alert API baseline loaded`.
  - Evidence: `20260622_190640_2a951e4e`.

- [ ] **2026-06-23 — Update `cross-border-broker-funding` for Raiffeisen → Wise → Freedom EUR route**
  - Proposed skill name: update `cross-border-broker-funding`.
  - Trigger: Denys asks how to fund Freedom24/Freedom Finance Europe or calculate real funding friction.
  - Reusable workflow: prefer account-proven flows over generic fee-page research; inspect screenshots; test EUR end-to-end; record Raif spent, Wise received, Wise sent, Freedom credited, fees, conversion rates, dates; compute all-in friction.
  - Include pitfalls/verification: use actual arithmetic with a tool; distinguish Wise EUR balance transfer from Wise card payment; Paysera card/transfer route is not viable here; final confirmation requires broker credit, not just Wise send screen.
  - Evidence: `20260622_163026_d7eee1f1`.

- [ ] **2026-06-22 — Create `startup-validation-asset-pack` skill**
  - Proposed skill name: `startup-validation-asset-pack`
  - Trigger: validating a startup/product idea quickly when Denys asks to “do what you can yourself,” especially before committing to a full build.
  - Reusable workflow: synthesize positioning and validation plan; create wiki/research notes; build a local artifact folder with README, brand positioning, validation plan, landing page, mockup board, content pack, and generated MP4 prototypes; verify HTML via local HTTP checks and videos via `ffprobe`; package artifacts as a tarball for delivery.
  - Include pitfalls/verification: Python/PIL/ffmpeg is enough for fast local video prototypes; `ffmpeg` filter args like `d=.4` can fail and should be `d=0.4`; generated app-screen art often has tiny/incorrect text, so prefer controlled UI overlays for later iterations; verify `test -s`, `ffprobe`, HTTP 200, and final artifact paths.
  - Evidence: `20260621_130017_acde58` — Life RPG validation pack plus promo v1/v2 generation.

- [ ] **2026-06-21 — Create `rocket-attack-alarm-ops` skill**
  - Proposed skill name: `rocket-attack-alarm-ops`
  - Trigger: modifying/deploying `/opt/apps/rocket-attack-alarm` bot behavior, especially threat categories, nationwide alert logic, city filters, Telegram commands, cron scripts, or production deploys.
  - Reusable workflow: inspect recent source messages/logs/DB evidence; update detection/filter/formatter/config/migrations; add regression tests; run focused tests plus TypeScript/build; rebuild/restart Docker production; verify `/health`, container health, runtime artifacts, and Telegram command menu/cron outputs.
  - Include pitfalls/verification: host `sqlite3` may be unavailable while container `sqlite3` works; avoid leaking bot tokens by running send scripts inside the container; distinguish active MiG warnings from `threat_ended`; sanitize source promotional lines before broadcast; verify `npm run test:*`, `npx tsc --noEmit`, `npm run build`, `docker compose -f docker-compose.prod.yml up -d --build`, `/health`.
  - Evidence: `20260620_211226_b41178` — MiG-31K nationwide alerts, source-text sanitization, Boryspil filter, `/suggestcity`, daily city-suggestion digest, production deploy.

- [ ] **2026-06-20 — Update `hermes-update-operations` / add `hermes-gateway-safe-restart` workflow**
  - Proposed skill name: `hermes-update-operations` update or `hermes-gateway-safe-restart`
  - Trigger: updating Hermes Agent on a gateway-hosting VPS, especially with local gateway patches or Telegram custom commands.
  - Reusable workflow: check versions/git diff; backup local patches; update Hermes; reapply `/balance` direct-script patches; run `py_compile` and `hermes doctor --fix`; verify `/balance`; restart gateway safely after the active gateway process.
  - Include pitfalls/verification: `hermes gateway restart` is blocked from inside the gateway process; delayed restart script may fail without execute bit; use `bash /tmp/hermes-delayed-gw.sh` via `terminal(background=true)`; verify `hermes-gateway.service` and `hermes-gateway-freylina.service`.
  - Evidence: `20260619_201814_ecad0c9f` — Hermes `v0.14.0 → v0.17.0`, Claude Code `2.1.159 → 2.1.183`, `/balance` patches restored.

- [ ] **2026-06-20 — Create/repair Freylina YouTube-to-wiki pipeline skill**
  - Proposed skill name: `freylina-youtube-to-wiki-pipeline`
  - Trigger: Freylina cron job receives queued @vse_pro_royal YouTube videos or reports missing `devops/youtube-to-wiki-pipeline`.
  - Reusable workflow: read `/root/.hermes/profiles/freylina/wiki/.pending-videos.json`; generate heuristic markdown under `content/youtube`; update `video-log.json`; clear queue after success; commit only if changed; report short summary or `[SILENT]` when appropriate.
  - Include pitfalls/verification: avoid mutating the wrong profile unless explicitly scoped; handle empty queue cleanly; verify `git status --short` and `git rev-parse --short HEAD`; do not dump raw JSON.
  - Evidence: `cron_ef9b3fb5feed_20260620_030049`; skill was missing and queue was empty at HEAD `654a3f9`.

## Pending Wiki Candidates

- [ ] **2026-07-12 — Validate/update Codex model usage-limit guidance**
  - Suggested destination: update `concepts/hermes-codex-oauth-quota-exhaustion.md` or create a focused current-plan note only after official-source confirmation.
  - Candidate content: session reported that Codex/ChatGPT Work share usage and that `gpt-5.6-luna` targets higher-volume/lighter work. Preserve the distinction between plan quota, shared usage, and model-specific limits.
  - Evidence: `20260711_120917_3c02d715`.
  - Caveat: direct session output was oversized; the nightly job did not independently revalidate current OpenAI pricing/docs.

- [ ] **2026-07-11 — Add CK3 dynastic/council playbook note if coaching continues**
  - Suggested destination: `games/ck3-learning-notes.md` or `games/ck3-dynasty-and-court-playbook.md`.
  - Candidate content: marriage acceptance via `Велике весілля`; avoid matrilineal marriage for male-heir dynasty continuity; verify whether target has inheritance, claim, or only succession position; check war goal before letting another ruler weaken/replace the current holder; high-stat women may be blocked from council by status/gender/religion/council-right rules, not by `Блудниця` itself.
  - Evidence: `20260710_211638_149336a6`.

- [ ] **2026-07-11 — Add Hermes interrupted-update note to ops docs**
  - Suggested destination: `agents/hermes-update-operations.md` or a future Hermes ops weekly-update note.
  - Candidate content: Jul 10 `hermes update` attempt backed up/stashed local patches (`agent/skill_commands.py`, `gateway/run.py`, `cron/scheduler.py`) and wrote a backup path under `~/hermes-update-backups/`, but the session was interrupted by gateway restart before completion; resume requires checking git status/stash, versions, gateway services, and local patch reapplication.
  - Evidence: `20260710_075319_5503656c`.

- [ ] **2026-07-10 — Add CK3 economic-vassal playbook note if game coaching continues**
  - Suggested destination: `games/ck3-economic-vassal-playbook.md` or extend a future `games/ck3-learning-notes.md`.
  - Candidate content: Denys is learning CK3 with Ukrainian UI and likes a count-under-liege, low-expansion economic roleplay. Capture durable guidance: control before development; economic buildings first; `+2 gold/month` is normal for counts; keep reserves; use hooks/secrets, ransoms, activities, council positions, and liege politics; recommended start is Werner von Habsburg in Aargau, 1066.
  - Evidence: `20260709_144322_da2aa910`.

- [ ] **2026-07-09 — Add CK3 Linux/Proton setup note if game support continues**
  - Suggested destination: `games/ck3-linux-popos-setup.md` or extend a future `games/ck3-learning-notes.md`.
  - Candidate content: Denys’s HP Pavilion Power / Pop!_OS setup runs CK3 acceptably via Proton on NVIDIA GTX 1050; native/Intel path can lag; useful settings include NVIDIA offload, GameMode, shader pre-caching, medium/low graphics, FPS cap, and avoiding deletion of `compatdata/1158310` / `shadercache/1158310`; Ukrainian localizer candidate was Workshop `3197478188` with English game language caveat.
  - Evidence: `20260708_084508_c98db802`.

- [ ] **2026-07-08 — Add CK3 learning/playbook note if game coaching continues**
  - Suggested destination: `games/ck3-learning-notes.md` or a lightweight gaming note linked from the index if Denys keeps asking CK3 questions.
  - Candidate content: Denys is learning CK3 through Ireland/tutorial-like play, prefers Ukrainian explanations with Russian UI labels, and is interested in practical power-politics/Machiavelli framing; capture recurring concepts such as direct actions vs passive modifiers, raids/prestige, schemes/secrets, rival assessment, and succession/army basics.
  - Evidence: `20260706_193417_6f92bafb`, `20260707_182842_7d5b042a`.

- [ ] **2026-07-07 — Add media-generation QA note/playbook if wallpaper work recurs**
  - Suggested destination: `agents/media-generation-qa.md`, a creative workflow note, or a section in an existing Gemini/media ops note.
  - Candidate content: for wallpaper/outpaint tasks, keep a verified artifact ledger with source URL/file, candidate dimensions, generation prompt, visual QA result, final file path, and whether `MEDIA:` was actually sent. Never promise a “ready in minutes” result until a non-empty output file and visual pass exist.
  - Evidence: `20260706_074551_d8ebfdbc`.

- [ ] **2026-07-06 — Update Freylina/Hermes ops note with resolved stale default cron jobs**
  - Suggested destination: Freylina operations/runbook wiki or a Hermes ops note linked from Agent Knowledge Ops.
  - Candidate content: Jul 5 repair found two parallel Freylina YouTube cron schemes. Stale duplicate default-profile jobs `b12b466f905d` (fetcher) and `ef9b3fb5feed` (analyzer with missing `devops/youtube-to-wiki-pipeline`) were removed. Canonical `freylina` profile script-only jobs remain `84a87c09869f` (`youtube-fetcher-cron.py`) and `ab1160450211` (`video-analyzer-cron.py`). Nested stale queue was cleared after all four videos were verified in `video-log.json` and page files.
  - Evidence: `20260705_113458_df8d2751`.

- [ ] **2026-07-06 — Add local places/preference note for MAMENORI if local-food lookups recur**
  - Suggested destination: `research/lviv-local-places.md` or a lightweight local preferences note.
  - Candidate content: Denys corrected that in the “sushi near NOA” context he meant MAMENORI, not Red Pepper / Yoki / ЯпонаХата; verify current location/hours before making future recommendations.
  - Evidence: `20260705_175420_3a0830d4`.

- [ ] **2026-07-06 — Index or cross-link options investor guide**
  - Suggested destination: `index.md` finance/research section or a future finance hub.
  - Candidate content: `research/options-investor-guide.md` is the source-of-truth summary for the Jul 5 options PDF; includes IV = Implied Volatility, Greeks, CALL/PUT, covered calls, CSP, PMCC/LEAPS, debit spreads, liquidity and assignment/exercise risk checklist.
  - Evidence: `20260705_205457_e86ffdf2`.

- [ ] **2026-07-05 — Update Freylina/Hermes ops note with stale duplicate queue behavior**
  - Suggested destination: Freylina operations/runbook wiki or a Hermes ops note linked from Agent Knowledge Ops.
  - Candidate content: Jul 5 analyzer found canonical queue empty (`/root/.hermes/profiles/freylina/wiki/.pending-videos.json`) and repo clean at `06acf06`; stale nested duplicate queue under `/root/.hermes/profiles/freylina/home/.hermes/profiles/freylina/wiki/.pending-videos.json` listed four videos already in `video-log.json` and with existing pages, so they should not be reprocessed.
  - Evidence: `cron_ef9b3fb5feed_20260705_030040`.

- [ ] **2026-07-04 — Create/update Beauty Growth Assistant rebuild/project note**
  - Suggested destination: `projects/beauty-growth-assistant.md` or `projects/beauty-growth-assistant/overview.md`, linked from the existing beauty SaaS research note.
  - Candidate content: Jul 3 Claude Sonnet UI/UX audit scored the current UI about 6/10; top issues were missing real photos/portfolio/trust on public profile, duplicated services, unclear CTA, and placeholder-like copy. Rebuild direction: solo-master mobile-first CRM/booking assistant, calendar/control-first, manual confirmation by default, public profile standalone, no generic dashboards/fake metrics. Process gate: BRD/PRD → design → architecture → backend → frontend from approved design → QA → UX validation loop.
  - Evidence: `20260703_145854_9a7ecf72`.

- [ ] **2026-07-04 — Update emergency fund / ETF note with IBTA screenshot confirmation**
  - Suggested destination: `research/emergency-fund-strategy.md`, `research/emergency-fund-dashboard.md`, or a future cash-like UCITS ETF note.
  - Candidate content: Denys screenshot of `IBTA.EU / IBTA` was confirmed as the 1–3yr US Treasury UCITS Acc candidate for the podushka strategy; it maps to VGSH-like exposure and should be verified by ISIN `IE00BYXPSP02` before trading. `IB01` remains the more cash-like 0–1yr option.
  - Evidence: `20260703_144155_2968a206`.

- [ ] **2026-07-04 — Update Hermes ops note with Claude Code 2.1.199 and weekly report**
  - Suggested destination: `agents/hermes-ops-weekly-updates.md` or `agents/hermes-update-operations.md`.
  - Candidate content: Claude Code updated from `2.1.197` to `2.1.199`; executable path `/root/.hermes/node/bin/claude`, npm package and package metadata verified; full `claude doctor` timed out after 180s. Weekly report also noted Hermes v0.18.0 / v2026.7.1 release items and follow-up commits, but those external facts were not re-verified in consolidation.
  - Evidence: `20260703_065217_4498a970`, `cron_d809074fdb23_20260703_060059`.

- [ ] **2026-07-03 — Index and cross-link AI-assisted SDLC/vibe-coding lifecycle note**
  - Suggested destination: `index.md`, and possibly a future `concepts/product-development-lifecycle.md` or project-planning hub.
  - Candidate content: new research note `research/ai-assisted-sdlc-vibe-coding-project-lifecycle-2026-07-02.md` defines AI-assisted SDLC and the ladder PoC → Prototype/RAT/Spike → Walking Skeleton → Vertical Slice → MLP → Pilot/MMP/v1. Use it when Denys asks how to structure AI/vibe-coded product work instead of defaulting to MVP.
  - Evidence: `20260702_192700_19352d8d`.

- [ ] **2026-07-03 — Update broker-funding/Wise route note with KYC timing rule**
  - Suggested destination: `research/freedom24-ukraine-funding-2026-06.md` or a focused Wise/Freedom route section.
  - Candidate content: if Wise requests confirmation of Ukraine residence while broker transfers are pending, wait until broker deposit is credited and Wise balance is zero/minimal when no hard deadline exists; confirming real data is safer than fake EU residence, but unsupported Ukrainian-resident product access can still cause onboarding/balance restrictions.
  - Evidence: `20260702_155655_553cd9a5`.

- [ ] **2026-07-03 — Update Rocket project/runbook with Jul 2 restart-loop and false-positive fixes**
  - Suggested destination: `projects/rocket-attack-alarm.md` or decomposed `projects/rocket-attack-alarm/{runbook,incidents,decisions}.md`.
  - Candidate content: Jul 2 repair found `rocket-attack-alarm` restart-looping (`RestartCount=815`, unhealthy) because new migration files `019_city_suggestions.sql` and `020_update_notification_preferences.sql` were mode `600`; normalizing `src`/`dist` copies to `644`, rebuild, and redeploy restored healthy readiness. Same session fixed a false-positive Kyiv alert from `@vanek_nikolaev` message `41404` sent to 10 users by adding strong aftermath report patterns for cleanup/casualty/overnight totals and regression test coverage (`npm run test:report-filter` 23/23, `npm run build`, healthy `/ready`).
  - Evidence: `20260702_060227_507ddd8d`.

- [ ] **2026-07-02 — Update emergency fund stablecoin note with custody split discussion**
  - Suggested destination: `research/emergency-fund-usdt-usdc-research.md` and possibly `research/emergency-fund-strategy.md`.
  - Candidate content: clarify that CEX balance is an operational hot exchange path, not the safest store; self-custody can usually be converted via wallet → WhiteBIT/Binance deposit → sell → card in ~10–30 minutes on normal days but adds network/deposit/error friction; Earn locks reduce emergency liquidity. Candidate alternative crypto sleeve: `$200–300 WhiteBIT hot balance`, `$700–1000 self-custody USDT/USDC`, `$1,200 30d Earn`, and `$1,300–1,700 60–90d Earn`, instead of keeping the full instant/long sleeve on CEX.
  - Evidence: `20260701_110157_85b8c913`.

- [ ] **2026-07-02 — Update Rocket project/runbook with restart-loop/OOM incident**
  - Suggested destination: `projects/rocket-attack-alarm.md` or decomposed `projects/rocket-attack-alarm/{runbook,incidents,open-loops}.md`.
  - Candidate content: July 1 incident where Kyiv/alert messages were missed because production container `rocket-attack-alarm` was in a restart loop (`RestartCount=336`, `ExitCode=1`) after Node.js heap out-of-memory around `2026-07-01T16:20:05Z`; repair required explicit approval for production stop/restart/debug, so no fix was applied in that session.
  - Evidence: `20260701_215059_abd2456d`.

- [ ] **2026-07-01 — Update/create Beauty Growth Assistant project note with public profile route**
  - Suggested destination: `projects/beauty-growth-assistant.md` or `projects/beauty-growth-assistant/overview.md`, linked from the existing beauty SaaS research note.
  - Candidate content: `/beauty/` remains the UI kit/design page; `/beauty/olena-nails` is the clean standalone mobile-first client public profile without CRM/dashboard/SaaS copy; no-photo design should be service-first/editorial rather than fake monogram; commits observed: `80e46e3 ui: replace no-photo monogram with service-first header` and `0351b0e feat: add standalone beauty public profile route`; verification included build/lint/nginx/browser checks and screenshots under deferred-task artifacts.
  - Evidence: `20260630_182440_b9e4ac`, `20260630_205901_297be096`.

- [ ] **2026-07-01 — Create Hermes deferred task queue operations note**
  - Suggested destination: `agents/hermes-deferred-task-queue.md` or `agents/hermes-ops-deferred-tasks.md` linked from Agent Knowledge Ops.
  - Candidate content: document queue folders `pending/running/done/failed/progress/artifacts/logs`, scripts `~/.hermes/scripts/deferred_tasks.py` and `~/.hermes/scripts/deferred_task_watchdog.py`, cron `ed23278d9458` every 20m no-agent, resume prompt rules, silent no-op/rate-limit behavior, self-test evidence, and manual create/list/show commands.
  - Evidence: `20260630_191516_dda9ca32`, `20260630_192732_bb7b42`.

- [ ] **2026-07-01 — Update Hermes ops note with weekly report delivery bug and Jun 30 update**
  - Suggested destination: `agents/hermes-ops-weekly-updates.md` or `agents/hermes-update-operations.md`.
  - Candidate content: weekly Hermes report generated but did not deliver to Telegram; Hermes updated to upstream `571092ee`, Claude Code to `2.1.197`, config migrated v30→v32, direct-script commands and cron `[SILENT]` behavior checked, gateway restart had to be scheduled via delayed `systemd-run` from inside gateway.
  - Evidence: `20260630_194546_704e6fbb`.

- [ ] **2026-06-30 — Create mobile app portfolio research hub**
  - Suggested destination: `research/mobile-app-portfolio-strategy-2026-06.md` or decomposed `projects/mobile-app-portfolio/{overview,research-log,idea-scorecards}.md`.
  - Candidate content: Denys wants app ideation as a business portfolio discipline; first CLI scan tested `ai calorie counter`, `macro tracker`, `pet symptom checker`, `baby sleep tracker`, `plant disease identifier`, `receipt scanner expense tracker`, `medication reminder`, `outfit planner wardrobe`, `home workout planner`, `travel packing list`, `skin care routine tracker`, and `room design ai`. Top smoke-test candidates were privacy-first family travel packing, receipt scanner for freelancers outside the US, and outfit purchase checker; avoid generic AI calorie/home workout/room design unless narrowed to a strong wedge. Jun 30 research update added theses: mobile spend grows while downloads are flat, AI monetizes but needs vertical/outcome-specific apps, visual AI has stronger viral/purchase signals, and top-paid iOS can still reward narrow pro utilities.
  - Evidence: `20260629_175146_d78a7cb1`, `cron_54b894b9fd7d_20260630_000558`.

- [ ] **2026-06-30 — Create Beauty Growth Assistant project/prototype note**
  - Suggested destination: `projects/beauty-growth-assistant.md` or `projects/beauty-growth-assistant/overview.md`, linked from the existing beauty SaaS research note.
  - Candidate content: repo `https://github.com/dstorozhyk/beauty-growth-assistant`, local path `/opt/apps/beauty-growth-assistant`, initial commit `d6fc4a3 feat: scaffold beauty growth assistant UI`; React/Vite/MUI prototype includes dashboard, money hints, QR/mini-page module, booking/manual approval, upsell/add-on performance, public mini-page preview, and Ukrainian outcome-based copy. Verification passed `npm run build` and `npm run lint`; deployment of protected preview remains blocked pending explicit approval for Nginx/basic-auth changes.
  - Evidence: `20260629_183841_50ab40de`.

- [ ] **2026-06-30 — Capture business-analysis feature discovery methodology in wiki**
  - Suggested destination: `concepts/micro-saas-feature-discovery-workflow.md` or a section in an existing product strategy note.
  - Candidate content: derive feature lists from business flow, process mapping, JTBD, competitor/pricing/review/search evidence, sellable MVP scope, manual/fake-now scope, validation plan, and MoSCoW/RICE-style prioritization; avoid generic feature lists not tied to revenue outcomes or internet evidence.
  - Evidence: `20260629_183354_7d362b1f`.

- [ ] **2026-06-27 — Capture weekly Hermes/Claude update report in ops notes**
  - Suggested destination: `agents/hermes-ops-weekly-updates.md` or a focused Hermes/Claude operations note linked from Agent Knowledge Ops.
  - Candidate content: weekly report said local Hermes Agent is v0.17.0 / 2026.6.19 but 807 commits behind; local Claude Code is 2.1.183 while latest reported is 2.1.193; prioritize Hermes update for gateway/Telegram/email/cron/browser reliability/security; after update run `hermes doctor`, gateway restart/status, `hermes cron list`, Telegram `[SILENT]` smoke test, and email/browser checks if used; for Claude update verify OTEL assistant-response privacy, MCP auth, `sandbox.credentials`, and changed `!` bash behavior.
  - Evidence: `cron_d809074fdb23_20260626_060049`.

- [ ] **2026-06-26 — Update Rocket project/runbook with source-channel repeat alerts, `/updates`, and dashboard tracking**
  - Suggested destination: `projects/rocket-attack-alarm.md` or decomposed `projects/rocket-attack-alarm/{overview,runbook,decisions,open-loops}.md`.
  - Candidate content: 30-minute active-threat lock now stores `sourceChannel`; repeat notifications are allowed from the channel that created the lock, while other-channel duplicates remain suppressed; update-news preferences use a single `/updates` toggle; `/updates_on` and `/updates_off` were removed; `/help`, Telegram command menu, scheduled update text, dashboard metric, dry-run and production deploy were verified; user-approved wording should describe new launches/new waves/continued activity, not merely “clarification.”
  - Evidence: `20260625_180939_5df7944e`.

- [ ] **2026-06-25 — Update Rocket project/runbook with Шептицький filters + broadcast correction**
  - Suggested destination: `projects/rocket-attack-alarm.md` or decomposed `projects/rocket-attack-alarm/{overview,runbook,decisions,open-loops}.md`.
  - Candidate content: add separate filters for city `Шептицький` and administrative `Шептицький район`; include legacy names `Червоноград`/`Червоноградський район`; live DB insert used backup `/opt/apps/rocket-attack-alarm/data/backups/manual/bot-before-sheptytskyi-live-2026-06-24T094035831Z.db`; suggestion was marked `added`; corrected broadcast went through the bot to `21/21` active subscribers.
  - Evidence: `20260624_072541_0e1e451a`.

- [ ] **2026-06-25 — Add Freylina YouTube-to-wiki pipeline operational note**
  - Suggested destination: Freylina operations/runbook wiki or a Hermes ops note linked from agent knowledge docs.
  - Candidate content: repaired pipeline uses absolute Freylina profile paths, deterministic title heuristics, fetcher/analyzer cron wrappers, and jobs `84a87c09869f` / `ab1160450211`; Jun 24 verification created pages and commit `4cbeb58`; Jun 25 analyzer still reported missing skill and found empty queue, so profile skill preload/reference should be checked.
  - Evidence: `20260624_055648_7bbd60f9`, `cron_ef9b3fb5feed_20260625_030044`.

- [ ] **2026-06-25 — Create finance note for accumulating cash-like UCITS ETF alternatives**
  - Suggested destination: `finance/cash-like-ucits-etfs-freedom.md` or `research/freedom24-cash-parking-ucits-2026-06.md`.
  - Candidate content: `IB01` / `IE00BGSF1X88` as SGOV-like accumulating 0–1yr US Treasury UCITS; `IBTA` / `IE00BYXPSP02` as VGSH-like 1–3yr; `IBTE` / `IE00BDFK1573` as EUR-hedged 1–3yr; Freedom may show `IB01.EU`; explain inverted yield curve and why 1–3yr yield can be below 0–1yr; include tax/staleness caveats.
  - Evidence: `20260624_151903_aef3232f`.

- [ ] **2026-06-24 — Update Freedom24/broker-funding wiki with confirmed route**
  - Suggested destination: `research/freedom24-ukraine-funding-2026-06.md` and/or a focused route note.
  - Candidate content: `Raiffeisen EUR → Wise EUR balance/main account → Freedom/Freedom24 EUR` was confirmed by a test transfer: 8.72 EUR arrived as 8.72 EUR; apparent route fee is 0 EUR if Wise/bank show no separate fee; keep date and caveat that rails can change.
  - Evidence: `20260623_120149_3bb6c070`.

- [ ] **2026-06-24 — Update Rocket Attack Alarm project/runbook with dedup + recovery notes**
  - Suggested destination: `projects/rocket-attack-alarm.md` or decomposed `projects/rocket-attack-alarm/{overview,runbook,decisions,open-loops}.md`.
  - Candidate content: state-based dedup by user/filter/threat category; MiG duplicate suppression across channels; 30-minute re-alert cooldown; content-hash dedup retained; user-facing wording caveat; verification commands; SQLite WAL/SHM + disk-full recovery steps; DB size after incident (~1.9 MB plus WAL/SHM).
  - Evidence: `20260623_192047_4f643f`.

- [ ] **2026-06-24 — Update UAH→USDT route note with Binance P2P → WhiteBIT workflow**
  - Suggested destination: `research/whitebit-binance-usdt-staking-route-2026-06.md` or a focused crypto on-ramp note.
  - Candidate content: if WhiteBIT UAH deposit/quick exchange is expensive, use Binance P2P UAH→USDT then withdraw to WhiteBIT over a supported low-fee network; avoid auto-selected Binance Buy Crypto offers when they are materially worse than manual P2P; compare final effective UAH/USDT with a timestamp.
  - Evidence: `20260623_193417_3dd79fc7`.

- [ ] **2026-06-23 — Create/update Rocket Attack Alarm project/runbook page**
  - Suggested destination: `projects/rocket-attack-alarm.md` or decomposed `projects/rocket-attack-alarm/{overview,runbook,roadmap,open-loops}.md`, linked from `index.md`.
  - Candidate content: air-alert API source `https://ubilling.net.ua/aerialalerts/`; `air_alert_api` synthetic source; 30s polling; startup baseline/no burst; active/clear synthetic messages; removal of `sirena_kyiv`; city suggestion `Кривий Ріг` marked `added` without duplicate; `markSuggestionStatus`; tests/deploy/health verification; broadcast script with marker protection.
  - Evidence: `20260622_190640_2a951e4e`.

- [ ] **2026-06-23 — Add Rocket bot stateful live-card UX roadmap note**
  - Suggested destination: Rocket bot roadmap/project page or `projects/rocket-attack-alarm/roadmap.md`.
  - Candidate content: replace raw event stream/concatenation with one live card per active incident; edit card for minor updates; push only on significant risk changes; group by incident type; expose optional history/details buttons.
  - Evidence: `20260622_211516_f2939aa1`.

- [ ] **2026-06-23 — Update Freedom24/broker-funding wiki after final credit confirmation**
  - Suggested destination: `research/freedom24-ukraine-funding-2026-06.md` and/or focused route note.
  - Candidate content: Paysera rejected for this route; current best candidate is `Raiffeisen EUR → Wise EUR balance/main account → Freedom EUR`; avoid USD conversion, Wise card payment, direct SWIFT, direct broker card top-up; compute all-in friction after Freedom credits funds.
  - Evidence: `20260622_163026_d7eee1f1`.

- [ ] **2026-06-23 — Create portfolio tracking note if Denys wants recurring checks**
  - Suggested destination: `finance/portfolio-tracker.md` or `research/investment-portfolio-2026.md` with clear staleness/date labels.
  - Candidate content: consultant-report holdings/targets, satellite thesis monitors, DCA plan, podushka distinction, and a checklist for future “глянь портфель” requests; do not treat prices as durable.
  - Evidence: `20260622_061004_e3501b49`.

- [ ] **2026-06-22 — Create Life RPG project overview / validation hub**
  - Suggested destination: `projects/life-rpg/overview.md` or `research/life-rpg-validation-hub-2026-06.md`, linked from `index.md`.
  - Candidate content: central links to `research/life-rpg-startup-strategy-2026-06-21.md`, `research/life-rpg-habit-app-roadmap-2026-06-21.md`, `/root/life-rpg-validation` artifact pack, landing/mockup/video files, current positioning, validation metrics, and next actions.
  - Evidence: `20260621_130017_acde58`.

- [ ] **2026-06-22 — Integrate mobile app-store payment route into SaaS payments wiki set**
  - Suggested destination: update `research/saas-payments-ukraine-validation-2026-06.md` and `research/saas-invoice-service-shortlist-ukraine.md` to link `research/mobile-app-stores-as-saas-payment-route-ukraine-2026-06-21.md` as a B2C/prosumer route.
  - Candidate content: app stores can reduce Ukrainian PSP friction for B2C/prosumer SaaS by using Apple/Google IAP/subscriptions, but require store fees, app review, platform policy compliance, entitlement sync, and payout/KYC verification; verify Apple App Store Connect for Denys’s real account/entity.
  - Evidence: `20260621_130017_acde58`.

- [ ] **2026-06-21 — Create Rocket Attack Alarm project/runbook wiki page**
  - Suggested destination: new `projects/rocket-attack-alarm.md` or decomposed `projects/rocket-attack-alarm/{overview,runbook,decisions,open-loops}.md`, linked from `index.md`.
  - Candidate content: current operational facts for `/opt/apps/rocket-attack-alarm`, MiG-31K as `mig` nationwide alert category, `threat_ended` suppression for MiG all-clear posts, source-text sanitization of promotional lines, Boryspil/Bucha city-filter changes, `/suggestcity` workflow, daily city-suggestion digest, and production deploy verification checklist.
  - Evidence: `20260620_211226_b41178`.

- [ ] **2026-06-20 — Add Paysera route to broker-funding wiki if confirmed**
  - Suggested destination: `research/freedom24-ukraine-funding-2026-06.md` or a focused Paysera route note linked from it.
  - Candidate content: Paysera app showed basic EUR accounts for Denys, but practical IBAN/top-up/SEPA operations likely require `https://bank.paysera.com` web banking; confirm KYC status, EUR IBAN, top-up fees, outbound SEPA fee/limits before treating it as a recommended route.
  - Evidence: `20260619_181923_8e5326e1`.

- [ ] **2026-06-20 — Consider project note for rocket-alert non-alert filtering rules**
  - Suggested destination: existing `research/rocket-attack-alarm-marketing.md` only if it is also used as project notes, or a new project/runbook page if rocket bot ops become recurring wiki content.
  - Candidate content: user-facing alerts must filter retrospective reports/digests and promotional/social posts such as `#зведення`, `візуалізація`, and footer combo `Підписатись | Підтримати канал`, while preserving live alert markers.
  - Evidence: `20260618_050621_9d7fda8b` and `20260615_200525_df2af912`.

## Open Loops

- [ ] **2026-07-15 — Enable or repair memory-tool availability for nightly compaction**
  - Context: `MEMORY.md` remains `2024 / 2200` (92.0%) and `USER.md` `1358 / 1375` (98.8%). Both batched safe-compaction attempts again returned `Memory is not available`; secret minimization remains blocked.

- [ ] **2026-07-15 — Human-review critical-skill pinning**
  - Context: repeated telemetry supports review of high-impact operational skills, but no lifecycle action was taken automatically.

- [ ] **2026-07-13 — Validate the «Все про Royal» tour-conversion case before using it in a rate card**
  - Context: the session reported 10 confirmed participants for an author-led European tour. Confirm attribution, period, booking evidence and partner permission; then use it as a case study with UTM/promo-code tracking.

- [ ] **2026-07-13 — Enable or repair memory-tool availability for nightly compaction**
  - Context: both memory files remain above the 80% pressure threshold. The cron environment again returned `Memory is not available`; no compaction could be applied.

- [ ] **2026-07-11 — Resume or explicitly close interrupted Hermes update**
  - Context: Jul 10 update attempt backed up/stashed local patches and started `hermes update`, but the active session was interrupted by gateway restart; verify git status/stash, Hermes version, local patches, gateway services, and cron `[SILENT]` behavior before considering update complete.

- [ ] **2026-07-11 — Enable or repair memory-tool availability for nightly compaction**
  - Context: `MEMORY.md` is `2024 / 2200` chars (`92.0%`) and `USER.md` is `1358 / 1375` chars (`98.8%`), but the memory tool is unavailable in the cron environment again; compaction remains proposed only, and secret minimization in `USER.md` is still blocked.

- [ ] **2026-07-11 — Decide whether active CK3 coaching belongs in a wiki playbook, broader skill, or both**
  - Context: CK3 sessions now cover economy, development/control, raids/prestige, intrigue, marriage acceptance, inheritance, council eligibility, and court recruitment; current `ck3-economic-vassal-play` may be too narrow if this continues.

- [ ] **2026-07-11 — Review `steam-game-purchase-advice` after more purchase tasks**
  - Context: the skill now has real usage after Assassin’s Creed edition advice; keep it for now and decide later whether it overlaps with broader gaming/product-research skills.

- [ ] **2026-07-10 — Enable or repair memory-tool availability for nightly compaction**
  - Context: `MEMORY.md` is `2024 / 2200` chars (`92.0%`) and `USER.md` is `1358 / 1375` chars (`98.8%`), but the memory tool is unavailable in the cron environment again; compaction remains proposed only.

- [ ] **2026-07-10 — Review whether CK3 economic-vassal guidance belongs in skill, wiki, or both**
  - Context: Jul 9 session created and used `ck3-economic-vassal-play`; it captures a recurring-looking game coaching pattern, but should be validated with more use before pinning/consolidation.

- [ ] **2026-07-09 — Enable or repair memory-tool availability for nightly compaction**
  - Context: `MEMORY.md` is `2024 / 2200` chars (`92.0%`) and `USER.md` is `1368 / 1375` chars (`99.5%`), but the memory tool is unavailable in the cron environment again; compaction remains proposed only.

- [ ] **2026-07-09 — Decide whether CK3/Linux setup deserves a wiki note or skill**
  - Context: Jul 8 session covered CK3 system requirements, Pop!_OS/NVIDIA/Proton tuning, slow loading causes, and Ukrainian Workshop localization setup; keep as review candidate unless CK3 support continues.

- [ ] **2026-07-09 — Review `steam-game-purchase-advice` after first real invocation**
  - Context: usage sidecar shows a new agent-created, patched-once skill with 0 use/view; do not archive automatically, but check whether it overlaps with existing gaming/product-research workflows.

- [ ] **2026-07-08 — Enable or repair memory-tool availability for nightly compaction**
  - Context: `MEMORY.md` is `2024 / 2200` chars (`92.0%`) and `USER.md` is `1368 / 1375` chars (`99.5%`), but the memory tool is unavailable in the cron environment again; compaction remains proposed only.

- [ ] **2026-07-08 — Finish or explicitly close Haaland/Fabinho wallpaper task**
  - Context: Jul 6–7 resume still did not deliver a verified final wallpaper; the 78% composite depended on missing `/root/haaland_wallpaper/refocus_strict_expand_78_gweb.png`, and later validation stopped before a successful `MEDIA:` final.

- [ ] **2026-07-08 — Decide whether recurring CK3 coaching should become a skill/wiki note**
  - Context: Denys had two CK3 sessions in the last 24h covering strategy, UI labels, raids, prestige, army growth, laws, inheritance, secrets, and murder schemes; current `game-walkthrough-visual-guidance` is only partially suited.

- [ ] **2026-07-08 — Improve local business-hours lookup fallback for blocked sources**
  - Context: Kebabця hours lookup failed due DNS/login/anti-bot blocks across Google/Facebook/Instagram/TripAdvisor/RestaurantGuru; future local lookup should try direct map/search APIs or ask for exact branch only after source-first attempts are exhausted.

- [ ] **2026-07-07 — Enable or repair memory-tool availability for nightly compaction**
  - Context: `MEMORY.md` is `2024 / 2200` chars (`92.0%`) and `USER.md` is `1294 / 1375` chars (`94.1%`), but the memory tool is unavailable in the cron environment again; compaction remains proposed only.

- [ ] **2026-07-07 — Finish or explicitly close Haaland/Fabinho wallpaper task**
  - Context: Jul 6 wallpaper session ended with Denys saying “Не бачу”; latest visible assistant state said no verified high-quality 78% generated file was available. If Denys still wants it, resume from verified files under `/root/haaland_wallpaper/` and do not promise delivery before file/visual QA.

- [ ] **2026-07-07 — Decide whether media wallpaper/outpaint QA becomes a skill**
  - Context: The Jul 6 task exposed a reusable pitfall: generated image variants and final delivery must be verified before reporting completion.

- [ ] **2026-07-06 — Enable or repair memory-tool availability for nightly compaction**
  - Context: `MEMORY.md` is `2194 / 2200` chars (`99.7%`) and `USER.md` is `1294 / 1375` chars (`94.1%`), but the memory tool returned unavailable during the July 6 cron run, so only proposed compaction was staged again.

- [ ] **2026-07-06 — Promote Freylina canonical script-only cron workflow into runbook/skill**
  - Context: Jul 5 user-triggered repair removed stale default duplicate cron jobs and cleared the nested duplicate queue; reusable documentation still needs to capture the canonical `freylina` profile workflow and verification commands.

- [ ] **2026-07-06 — Finish high-quality football photo search if Denys still needs it**
  - Context: Jul 5 photo session found a likely AP/Alamy candidate (`2MA74T0`, Fabinho vs Erling Haaland at Anfield, 2022-10-16), but the session ended after browser/reverse-search issues without a final confirmed high-res source delivered.

- [ ] **2026-07-06 — Decide whether MAMENORI local-place correction belongs in memory or wiki**
  - Context: direct correction may be useful for future Lviv food lookups, but memory is over pressure; keep in review queue until compaction works.

- [ ] **2026-07-05 — Enable or repair memory-tool availability for nightly compaction**
  - Context: both `MEMORY.md` and `USER.md` remain above 80% pressure, but the memory tool returned unavailable during the July 5 cron run, so only proposed compaction was staged again.

- [ ] **2026-07-05 — Reconcile Freylina analyzer missing skill warning and stale nested queue**
  - Context: Jul 5 Freylina analyzer still began with missing `devops/youtube-to-wiki-pipeline`; canonical queue was empty and repo stayed clean at `06acf06`, while the stale nested queue contains videos already processed in `video-log.json`.

- [ ] **2026-07-04 — Review Beauty Growth Assistant BRD v0.1 and answer open questions**
  - Context: BRD asks whether MVP is strictly solo-master or also small studio; whether confirming a request creates `pending` or `confirmed`; first channels; public booking vs public profile + chat CTA; and auth/preview approach.

- [ ] **2026-07-04 — Promote Beauty rebuild process and UI audit into project/wiki docs**
  - Context: current durable decisions live in session/digest only; project note should capture Claude audit, gated workflow, and mobile-first solo-master product direction.

- [ ] **2026-07-04 — Enable or repair memory-tool availability for nightly compaction**
  - Context: both `MEMORY.md` and `USER.md` exceed 80% pressure, but `memory` tool returned unavailable during the July 4 cron run, so only proposed compaction was staged.

- [ ] **2026-07-04 — Reconcile Freylina analyzer missing skill warning**
  - Context: Jul 4 Freylina analyzer still began with missing `devops/youtube-to-wiki-pipeline`; canonical queue was empty and repo HEAD stayed `06acf06`, so this is workflow/profile-skill repair rather than content recovery.

- [ ] **2026-07-04 — Decide whether to document Claude Code 2.1.199 update in Hermes ops**
  - Context: update succeeded, but `claude doctor` hung; a concise ops note would prevent future confusion about acceptable verification.

- [ ] **2026-07-03 — Decide whether to create/update AI-assisted SDLC product-planning skill**
  - Context: Jul 2 research produced `research/ai-assisted-sdlc-vibe-coding-project-lifecycle-2026-07-02.md` and a practical taxonomy for PoC/Prototype/RAT/Walking Skeleton/Vertical Slice/MLP/Pilot.

- [ ] **2026-07-03 — Promote Rocket Jul 2 migration-permission and aftermath false-positive fix into runbook/skill**
  - Context: bot restart-loop was repaired by normalizing migration SQL file modes to `644`; later a false-positive Kyiv aftermath report was fixed with strong report patterns and regression tests.

- [ ] **2026-07-03 — Update broker-funding note with Wise KYC pending-transfer timing rule**
  - Context: Wise Ukraine residence confirmation is safer with real data, but if broker transfers are still pending and no deadline exists, wait until broker credit and Wise balance is zero/minimal.

- [ ] **2026-07-02 — Repair Rocket Attack Alarm restart loop after explicit production approval**
  - Context: Jul 1 session found `rocket-attack-alarm` in restart loop (`RestartCount=336`, `ExitCode=1`) after a Node.js heap out-of-memory around `2026-07-01T16:20:05Z`; bot was not monitoring/sending Kyiv alerts. Debug/repair was blocked because stopping production container required explicit confirmation.

- [ ] **2026-07-02 — Update emergency fund stablecoin note with custody/hot-balance trade-off**
  - Context: Jul 1 discussion clarified that `$600` on WhiteBIT only makes sense as a hot operational exchange balance, while a self-custody wallet can still be used relatively quickly but adds network/deposit/error steps; consider documenting the `$200–300 hot + $700–1000 wallet` alternative.

- [ ] **2026-07-02 — Reconcile Freylina analyzer missing skill warning plus stale nested queue**
  - Context: Jul 2 Freylina analyzer still begins with missing `devops/youtube-to-wiki-pipeline`; canonical queue is empty and repo HEAD stayed `06acf06`, but stale nested queue remains at `~/.hermes/profiles/freylina/home/.hermes/profiles/freylina/wiki/.pending-videos.json` with videos already processed in `video-log.json`.

- [ ] **2026-07-01 — Verify default Hermes gateway restart completed after delayed update restart**
  - Context: Jun 30 Hermes/Claude update scheduled gateway restart via `systemd-run`; final report said Freylina had a new PID, but default gateway restart was still in `systemctl restart` while the response was being delivered.

- [ ] **2026-07-01 — Decide whether to create/update Beauty Growth Assistant project note**
  - Context: `/beauty/olena-nails` is now a deployed standalone client public profile route, `/beauty/` remains UI kit/design page, and commits `80e46e3`/`0351b0e` plus screenshot artifacts should be captured if the project note is promoted.

- [ ] **2026-07-01 — Decide whether to create Hermes deferred task queue wiki runbook**
  - Context: deferred task queue/watchdog is installed and tested; a wiki runbook would make future recovery, debugging, and manual task creation easier.

- [ ] **2026-07-01 — Reconcile Freylina analyzer missing skill warning plus stale nested queue**
  - Context: Jul 1 Freylina analyzer still begins with missing `devops/youtube-to-wiki-pipeline`; default queue is empty and repo clean at `06acf06`, but stale nested queue remains at `~/.hermes/profiles/freylina/home/.hermes/profiles/freylina/wiki/.pending-videos.json`.

- [ ] **2026-06-30 — Decide whether to create mobile app portfolio research hub**
  - Context: Jun 29–30 work produced a repeatable app-idea factory skill, a first 12-keyword App Store/Google Play scan, and updated 2026 mobile monetization theses. This could become a wiki hub for scorecards, killed ideas, and validated app bets.

- [ ] **2026-06-30 — Decide whether to create Beauty Growth Assistant project note**
  - Context: `/opt/apps/beauty-growth-assistant` and GitHub repo `dstorozhyk/beauty-growth-assistant` now contain the first React/Vite/MUI prototype at commit `d6fc4a3`; build/lint passed, but protected preview is not deployed.

- [ ] **2026-06-30 — Deploy Beauty Growth Assistant protected preview if approved**
  - Context: source session planned `https://bodya-monitor.duckdns.org/beauty/`, but Nginx/basic-auth and `/var/www` changes required explicit approval. Do not store the basic-auth password in wiki.

- [ ] **2026-06-30 — Fix Claude Code auth before using it for review**
  - Context: beauty project review was cancelled because Claude Code returned `401 Invalid authentication credentials` even though `claude auth status` reportedly showed a Claude Pro login.

- [ ] **2026-06-30 — Reconcile Freylina analyzer missing-skill warning persists**
  - Context: Jun 30 Freylina analyzer still began with “Skill(s) not found and skipped: devops/youtube-to-wiki-pipeline”; default queue was empty, no files changed, repo was clean at `06acf06`, and no content loss was observed.

- [ ] **2026-06-29 — Reconcile Freylina analyzer missing-skill warning persists**
  - Context: Jun 29 Freylina analyzer still began with “Skill(s) not found and skipped: devops/youtube-to-wiki-pipeline”; default queue `/root/.hermes/profiles/freylina/wiki/.pending-videos.json` was empty, no files were changed, and no commit was created. This remains an operational profile/skill-reference repair; no content loss was observed in this run.

- [ ] **2026-06-28 — Reconcile Freylina analyzer missing-skill warning persists**
  - Context: Jun 28 Freylina analyzer still began with “Skill(s) not found and skipped: devops/youtube-to-wiki-pipeline”; default queue `/root/.hermes/profiles/freylina/wiki/.pending-videos.json` was empty, no files were changed, and repo HEAD remained `4cbeb58`. This is an operational profile/skill-reference repair rather than content recovery.

- [ ] **2026-06-27 — Update Hermes Agent on VPS and smoke-test gateway/cron flows**
  - Context: weekly report found local Hermes Agent v0.17.0 / 2026.6.19 but 807 commits behind; recommended checks after update include `hermes doctor`, gateway restart/status, `hermes cron list`, Telegram `[SILENT]`, and email/browser flows if active.

- [ ] **2026-06-27 — Update Claude Code and check privacy/security settings**
  - Context: weekly report found local Claude Code 2.1.183 while latest reported was 2.1.193; check OTEL assistant-response logging, MCP headless auth, `sandbox.credentials`, and changed `!` bash response behavior after update.

- [-] **2026-06-26 — Verify Rocket update announcement delivery**
  - Result: resolved in `cron_56aaf01b43a2_20260626_070049`; production command sent to 21/21 recipients with 0 failures, and `/updates` remains the user toggle for update-news messages.

- [ ] **2026-06-26 — Promote Rocket repeat-alert logic and `/updates` toggle into runbook**
  - Context: source-channel repeat notifications, dashboard tracking, one-command `/updates` toggle, and user-approved wording for new launches/new waves should be added to the project/runbook docs.

- [ ] **2026-06-26 — Reconcile Freylina analyzer missing-skill warning persists**
  - Context: Jun 26 Freylina cron still reported missing `devops/youtube-to-wiki-pipeline`; default queue was empty and no files were changed, but the profile/skill preload/reference mismatch remains unresolved.

- [ ] **2026-06-25 — Reconcile Freylina analyzer missing-skill warning**
  - Context: Jun 24 repaired/replaced Freylina `youtube-to-wiki-pipeline` and verified jobs, but Jun 25 analyzer cron still began with “Skill(s) not found and skipped: devops/youtube-to-wiki-pipeline”; likely profile/skill preload/reference mismatch.

- [ ] **2026-06-25 — Promote Rocket Шептицький filters and bot-broadcast method into runbook**
  - Context: live DB insert and broadcast were verified, but project/runbook docs still need city-vs-district split, backup/FTS/mark-added steps, and warning that origin-chat cron is not a subscriber broadcast.

- [ ] **2026-06-25 — Decide whether to create Freedom cash-like UCITS ETF note**
  - Context: SGOV/VGSH accumulating alternatives were identified for Freedom (`IB01`, `IBTA`, `IBTE`), but yields/prices are time-sensitive and tax treatment needs explicit caveats.

- [ ] **2026-06-24 — Verify Rocket bot update announcement delivery**
  - Context: one-shot cron job `e717319bd742` is scheduled for 2026-06-24 09:30 UTC / 12:30 Kyiv; text was corrected to avoid implying an authoritative continuous threat state.

- [ ] **2026-06-24 — Promote Rocket bot state-based dedup into project/runbook docs**
  - Context: production deploy was verified with tests/build/health/ready/runtime probe, but wiki runbook still needs the new 30-minute cooldown, semantic dedup, and disk-full SQLite recovery notes.

- [ ] **2026-06-24 — Repair Freylina missing YouTube-to-wiki pipeline skill reference**
  - Context: Jun 24 analyzer again reported missing `devops/youtube-to-wiki-pipeline`; no `.pending-videos.json` queue was found and no content was processed.

- [ ] **2026-06-23 — Verify Rocket bot 12:30 broadcast delivery**
  - Context: one-shot cron job `5ab7ee5a7792` should run at 2026-06-23 09:30 UTC / 12:30 Kyiv; dry-run showed 21 active subscribers and marker-file duplicate protection.

- [ ] **2026-06-23 — Confirm broker-funding route after Freedom credits funds**
  - Context: need Raif spent, Wise received, Wise sent, Freedom credited, fees/conversions, and timing; then compute all-in friction as `1 - Freedom credited / Raif spent` normalized to one currency.

- [ ] **2026-06-23 — Decide whether to create a persistent portfolio tracker**
  - Context: no saved portfolio/targets were found before Denys pasted the consultant report; a structured wiki/file would let future “глянь портфель” checks run without re-supplying data.

- [ ] **2026-06-23 — Convert Rocket live-card/significant-change UX into roadmap/issue**
  - Context: Denys liked anti-spam improvements but rejected simple concatenation; the stronger direction is a stateful incident manager with live cards and pushes only when risk changes.

- [ ] **2026-06-22 — Repair Rocket bot `Дніпровський район (Київ)` live filters**
  - Context: `20260621_094520_60c52a99` found 2 live filters where `Дніпровський район (Київ)` was incorrectly linked to `Київська область` instead of district hierarchy id `83`; needs explicit approval because it requires live DB update/restart.

- [ ] **2026-06-22 — Decide next Life RPG validation step**
  - Context: Life RPG validation pack and promo v2 exist; next likely steps are deploy landing + waitlist, clean generated UI text/artifacts, and/or create promo v3 with controlled UI overlays and better motion/audio.

- [ ] **2026-06-22 — Cross-link App Store payment route in SaaS payments wiki**
  - Context: `mobile-app-stores-as-saas-payment-route-ukraine-2026-06-21.md` exists and is now indexed, but still needs integration into the earlier decomposed SaaS payments overview/comparison.

- [ ] **2026-06-22 — Repair Freylina missing YouTube-to-wiki pipeline skill reference**
  - Context: Jun 22 cron again reported missing `devops/youtube-to-wiki-pipeline`; no pending queue was found and the wiki repo was clean, so this is a workflow repair, not urgent content recovery.

- [ ] **2026-06-21 — Review first `/suggestcity` daily digest**
  - Context: daily job `7c6dab4509cc` reports new `city_suggestions` if users submit missing cities; review whether suggestions should be added and whether the workflow needs a runbook.

- [ ] **2026-06-21 — Clarify Freylina nested pending queue behavior**
  - Context: default Freylina queue was empty, but `/root/.hermes/profiles/freylina/home/.hermes/profiles/freylina/wiki/.pending-videos.json` contained duplicate items already processed in `video-log.json`; decide whether to clean up or document this path issue while repairing the missing YouTube-to-wiki pipeline skill.

- [ ] **2026-06-20 — Evaluate safe nightly consolidation after ~7 days**
  - Context: `20260620_143820_d1e8512f` proposed starting in safe mode, then deciding whether limited autopilot memory/skill promotion is warranted.

- [ ] **2026-06-20 — Confirm/repair Freylina missing pipeline skill reference**
  - Context: June 20 Freylina cron skipped `devops/youtube-to-wiki-pipeline`; queue was empty, so no immediate content loss.

- [ ] **2026-06-20 — Decide whether to update Hermes update runbook/skill**
  - Context: `20260619_201814_ecad0c9f` uncovered reusable Hermes update steps and gateway restart pitfalls.

- [ ] **2026-06-20 — Confirm Paysera funding workflow before wiki promotion**
  - Context: Denys registered Paysera, but KYC, EUR IBAN, card/top-up fees, and outbound SEPA behavior still need confirmation.

- [ ] **2026-06-20 — Confirm RSP Lviv padel price/slots if booking**
  - Context: from `Кульпарківська 64а`, RSP was closest, but public court price was not found.

## Archive / Decisions

- [x] **2026-06-22 — Rocket bot update announcement delivery verified early**
  - Result: the scheduled 2026-06-22 12:30 announcement was deleted and sent immediately in `20260621_094520_60c52a99`; delivery was `17/18`, with 1 Telegram `Forbidden: bot was blocked by the user` failure.
