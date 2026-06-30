---
title: Agent Knowledge Review Queue
created: 2026-06-20
updated: 2026-06-30
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
