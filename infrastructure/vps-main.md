---
title: Main VPS — host and service context
created: 2026-08-16
updated: 2026-08-16
type: entity
status: active
tags: [infrastructure, vps, docker, systemd, monitoring]
sources:
  - "live-vps-check:2026-08-16T22:20:35Z"
---

# Main VPS

## Host

Live snapshot verified at `2026-08-16T22:20:35Z`:

- hostname: `main-ubuntu-4gb-fsn1-1`;
- kernel: Linux `7.0.0-15-generic`, x86_64;
- RAM: 3.7 GiB total, 1.5 GiB available at snapshot time;
- swap: 2.0 GiB `/swapfile`, 309 MiB used;
- root filesystem: 38 GiB, 32 GiB used, 3.7 GiB available (**90%**).

Resource numbers are timestamped operational state, not durable capacity guarantees.

## Active service context

At the snapshot:

- `nginx`: active;
- `docker`: active;
- `cron`: active;
- `tor`: active;
- Docker workload: `rocket-attack-alarm`, healthy, bound only to `127.0.0.1:9090`;
- the unit named `hermes-gateway` was inactive; this does not by itself prove that Hermes messaging is unavailable because runtime/supervision may use a different process path.

## Resource decisions already applied

- A persistent 2 GiB swapfile was added to absorb memory spikes.
- `vm.swappiness=10` was selected so swap acts primarily as an emergency buffer.
- Unneeded CUPS, libvirt helper sockets and `multipathd` were disabled.
- Tor and relevant application workloads were intentionally preserved.
- Rocket’s V8 heap ceiling was raised within its container memory limit after a JavaScript heap OOM.

## Known current concern

Root disk usage was **90%** at this snapshot. Treat it as a capacity warning to investigate, not as proof of an incident. Any cleanup requires a separate inventory and approval; do not delete caches, images, backups or project artifacts blindly.

## Project roots inventoried

- `/opt/apps/rocket-attack-alarm` — ~175 MiB;
- `/opt/apps/beauty-growth-assistant` — ~430 MiB;
- `/root/life-rpg-validation` — ~502 MiB.

These sizes include working files/build dependencies and are only an inventory snapshot.

## Security boundary

Wiki pages must not contain:

- `.env` values;
- tokens, API keys, passwords, session cookies;
- Bitwarden secret values;
- private Telegram credentials;
- copied production databases or user data.

## Related

- [[projects/rocket-attack-alarm/overview|Rocket Attack Alarm]]
