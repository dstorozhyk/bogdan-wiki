---
title: Agent Knowledge Review Queue
created: 2026-06-20
updated: 2026-06-21
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

_No pending candidates yet._

## Pending Skill Candidates

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

- [ ] **2026-06-21 — Verify Rocket bot update announcement delivery**
  - Context: one-shot job `b12d4eb20acb` should send the approved update text on 2026-06-22 12:30 Europe/Kyiv about Bucha, Boryspil, and `/suggestcity`; confirm delivery summary afterward.

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

_No reviewed items yet._
