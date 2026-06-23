---
title: Agent Knowledge Review Queue
created: 2026-06-20
updated: 2026-06-23
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

- [ ] **2026-06-23 — Broker funding confirmed candidate route**
  - Proposed text: `Broker funding: current best candidate route is Raiffeisen EUR → Wise EUR balance/main account → Freedom24/Freedom Finance Europe EUR. Avoid Paysera, direct SWIFT, direct broker card top-up, Wise card payment, and USD→EUR conversion for this flow; verify final route after Freedom credits funds.`
  - Why durable: account-specific correction that prevents repeated bad recommendations for Denys's broker-funding workflow.
  - Risk/staleness: route is not fully final until Freedom credits funds; financial rails/compliance can change.
  - Evidence: `20260622_163026_d7eee1f1`.

## Pending Skill Candidates

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
