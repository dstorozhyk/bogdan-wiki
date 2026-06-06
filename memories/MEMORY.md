Denys prefers Ukrainian/direct communication, full infra access, action over handoff questions, Claude/claude-code for coding tasks, and `gemini-web-controller`/`gweb image` for Gemini web media generation. VPS deployments: Docker/container-only runtime isolation, harden services, and do not claim “done” until prod is deployed/health-verified. “Повітряні Загрози” = `/opt/apps/rocket-attack-alarm`; Telegram UX: city click stays on region list with visible `☑️`; whole-region selection is exclusive.
§
GitHub authenticated as dstorozhyk via gh CLI with a Fine-grained PAT. Token stored in ~/.config/gh/hosts.yml. Access can be expanded dynamically by Denys in GitHub UI without replacing the token.
§
/balance uses direct_script patches in Hermes source code: agent/skill_commands.py (~L316) and gateway/run.py (~L7725) in /usr/local/lib/hermes-agent/. Patches get OVERWRITTEN on Hermes update. After updating Hermes, re-apply patches or /balance will return JSON / fail.
§
**Hermes провайдери — пріоритет (налаштовано в config.yaml):**
1. **OpenAI** (основний, openai-codex / gpt-5.5, автоматичне перемикання моделей)
2. **GitHub Copilot** (fallback 1 — haiku)
3. **GitHub Copilot** (fallback 2 — gpt-4.1)
4. **Google Gemini** (fallback 3 — gemini-2.5-flash, по API ключу)
5. **OpenRouter** (fallback 4 — deepseek/deepseek-v4-flash, платний)
§
**Wiki System** — Two separate repos with daily auto-sync:
  • bogdan-wiki: Default profile general KB, syncs 04:00 UTC (cron f7d4225863b6)
  • freylina-wiki: Freylina royal families KB, syncs 05:00 UTC (cron 78b491e5d6e3)
  • Each includes SOUL.md + memories/, copied from profile root before push via wiki-sync.sh
§
**Wiki-first:** Research docs → bogdan-wiki/research/. MEMORY = configs/credentials only.
§
Hermes CLI: The command for a single query in non-interactive mode is `hermes chat -q`, not `hermes ask`.
§
**ukraine-specialists-finder** skill + wiki guide: `/root/bogdan-wiki/research/ukraine-specialists.md`. Skill: python3 ~/.hermes/skills/ukraine-specialists-finder/scripts/find_specialist.py. Base: `/root/.hermes/skills/ukraine-specialists-finder/references/lviv_specialists.json`. Lviv contacts in wiki.