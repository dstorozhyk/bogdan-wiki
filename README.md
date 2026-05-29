# Bogdan's Wikis

Distributed knowledge bases for Hermes Agent profiles.

## Structure

- **main** — Default profile wiki (AI/ML, .NET, general knowledge)
- **freylina** — Freylina profile wiki (Royal families, blogger knowledge)
- **shared** — Cross-profile facts available to all agents

Each branch maintains its own `SCHEMA.md`, `index.md`, and wiki content.

## Syncing

Each Hermes profile runs a daily cron job that pushes updates to its branch.
