---
title: Rocket Attack Alarm — operations reference
created: 2026-08-16
updated: 2026-08-16
type: guide
status: reference
tags: [project, telegram, nodejs, docker, monitoring]
sources:
  - "/opt/apps/rocket-attack-alarm/src/core/config/constants.ts"
  - "/opt/apps/rocket-attack-alarm/src/delivery/air-alert-api-monitor.service.ts"
  - "/opt/apps/rocket-attack-alarm/src/core/utils/formatter.ts"
  - "/opt/apps/rocket-attack-alarm/src/database/repositories/city-suggestion.repository.ts"
  - "logs/daily/2026-06-21.md"
  - "logs/daily/2026-06-23.md"
  - "logs/daily/2026-06-24.md"
---

# Rocket Attack Alarm — operations reference

This is a cross-session operational reference, not a substitute for the current source repository. Before changing or deploying behavior, inspect the live code and project `AGENTS.md`/deployment docs.

## Current source-confirmed behavior

### Threat categories and ended events

Current model categories include:

- `drone`;
- `cruise_missile`;
- `ballistic`;
- `mig`;
- `air_alert`.

MiG-31K warnings have a distinct `mig` category. Clear/negation content is classified as `threat_ended` before normal threat delivery and must not become a new active-warning alert.

### Air-alert API source

`AirAlertApiMonitorService` currently:

- uses source identity `air_alert_api`;
- defaults to `https://ubilling.net.ua/aerialalerts/`;
- polls every 30 seconds;
- establishes a baseline on startup;
- emits transitions only after state changes, avoiding a startup burst from already-active regions.

### Duplicate suppression

Two different mechanisms must not be confused:

1. exact/canonical cross-channel dedup TTL: **5 minutes**;
2. same active threat status re-alert cooldown: **30 minutes**.

Dashboard analytics additionally group events by category + normalized locations + a 30-minute received-time bucket. That statistical grouping is not itself the user-delivery cooldown.

### Non-alert and promotional content

- Retrospective `#зведення` and visualization content is excluded from live alert delivery.
- Footer-style social/promotional posts such as `Підписатись | Підтримати канал` are treated as non-alert unless real-time guards prove an actual current threat.
- Promotional lines such as “Підписатися на …” are stripped from otherwise valid alerts before delivery.

### City suggestion workflow

The bot supports `/suggestcity <місто>`:

- submissions are stored in `city_suggestions`;
- new items can be grouped/reviewed;
- status transitions are `reviewed`, `added`, or `rejected`;
- the workflow is intended to add real demand-driven city filters without silently duplicating existing seed/live DB entries.

## Historical production recovery lesson

A June 2026 incident showed that **disk exhaustion can present as an application/database failure**:

- root disk reached 100%;
- SQLite could not create/use WAL/SHM files;
- the container entered a restart loop;
- cleanup of Docker build cache/old images freed substantial space;
- broken WAL/SHM sidecars were removed only after the container was stopped;
- restart and `/health`/`/ready` verification restored service.

Do not generalize this into “delete WAL when the bot fails.” First verify disk pressure and stop writers; SQLite sidecar removal is a recovery action with data-safety implications.

## Deployment verification checklist

Before deployment:

1. inspect `git status` and existing uncommitted work;
2. read current project `AGENTS.md` and deployment docs;
3. run focused regression tests for the changed behavior;
4. run TypeScript/build checks;
5. validate Docker Compose configuration.

After deployment:

1. verify container state and restart count;
2. verify `/health` and `/ready` where available;
3. inspect startup logs for DB migrations, API baseline and source initialization;
4. run a behavior-specific probe/dry run;
5. verify disk space and memory ceiling;
6. avoid exposing credentials or raw user/chat data in logs/wiki.

## Known documentation boundary

The source repository contains active uncommitted WIP. Therefore this page records stable operational behavior confirmed in both source and prior executions, but it must not be used to assume a clean release/commit boundary.

## Related

- [[overview]]
- [[marketing-ideas]]
- [[vps-main]]
