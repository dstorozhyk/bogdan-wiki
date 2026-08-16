---
title: Rocket Attack Alarm — project overview
created: 2026-08-16
updated: 2026-08-16
type: project
status: active
approval: user-directed
tags: [project, telegram, nodejs, typescript, monitoring]
sources:
  - "/opt/apps/rocket-attack-alarm/README.md"
  - "/opt/apps/rocket-attack-alarm/docs/INDEX.md"
  - "live-vps-check:2026-08-16T22:20:35Z"
---

# Rocket Attack Alarm

Telegram-бот для моніторингу каналів повітряних загроз через MTProto та доставки персоналізованих сповіщень через Bot API.

## Confirmed product scope

- Ієрархічні локації: область → місто → район.
- Категорії загроз: БпЛА, крилаті ракети, балістика.
- До 30 персональних фільтрів на користувача.
- Інтерактивний onboarding із вибором міста.
- Quiet hours і тимчасова пауза з bypass для балістики.
- Feedback про false positive / false negative.

`city` у правилах бота є регіональним фільтром; retrospective `#зведення` та `візуалізація` не мають породжувати оперативні алерти.

## Current deployment snapshot

Перевірено на VPS `2026-08-16T22:20:35Z`:

- application root: `/opt/apps/rocket-attack-alarm`;
- Docker container: `rocket-attack-alarm`;
- image: `rocket-attack-alarm:latest`;
- status: `healthy`, uptime понад 3 доби;
- local binding: `127.0.0.1:9090 → 9090/tcp`;
- production memory guard: V8 heap configured separately from the container ceiling after a previous OOM incident.

Це snapshot, а не гарантія майбутнього стану.

## Source of truth

- Onboarding і quickstart: `/opt/apps/rocket-attack-alarm/README.md`.
- Documentation map: `/opt/apps/rocket-attack-alarm/docs/INDEX.md`.
- Deployment details: `/opt/apps/rocket-attack-alarm/DEPLOYMENT.md`.
- AI-agent rules: `/opt/apps/rocket-attack-alarm/AGENTS.md`.
- Production operations and backups: project `docs/operations/`.

Wiki не дублює implementation docs. Вона зберігає durable project context, cross-project decisions і зв’язки.

## Documentation landscape

У source repository уже є окремі матеріали про:

- filter scaling та inverted-index phase;
- Redis phase 2, consistency, deployment і operations;
- Postgres + Redis architecture recommendation;
- validation/annotation pipeline;
- encrypted offsite backups.

Перед використанням конкретного design document треба перевіряти його `Last reviewed` і звіряти з кодом: repository містить активний незакомічений WIP, тому старі docs можуть відставати від implementation.

## Related wiki pages

- [[operations-reference]] — source-checked operations and recovery reference.
- [[marketing-ideas]] — непогоджений growth/content backlog.
- [[vps-main]] — host-level deployment context.
