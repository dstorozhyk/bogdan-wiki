“Повітряні Загрози” = `/opt/apps/rocket-attack-alarm`; Telegram UX: city click stays on region list with visible `☑️`; whole-region selection is exclusive. User-facing alerts must exclude retrospective reports/digests like `#зведення` and `візуалізація`.
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
**Wiki System** — bogdan-wiki `/root/bogdan-wiki`: nightly safe knowledge consolidation cron `1773cf46a5ec` 03:30 UTC writes digest/review queue; GitHub sync cron `f7d4225863b6` 04:00 UTC via `wiki-sync-bogdan.sh`. freylina-wiki `/root/.hermes/profiles/freylina/wiki`: sync cron `78b491e5d6e3` 05:00 UTC. Cron scripts need wrapper/no args; exclude `*.lock`.
§
**Wiki-first:** Research docs → bogdan-wiki/research/. MEMORY = configs/credentials only.
§
Hermes CLI: The command for a single query in non-interactive mode is `hermes chat -q`, not `hermes ask`.
§
**ukraine-specialists-finder** skill + wiki guide: `/root/bogdan-wiki/research/ukraine-specialists.md`. Skill: python3 ~/.hermes/skills/ukraine-specialists-finder/scripts/find_specialist.py. Base: `/root/.hermes/skills/ukraine-specialists-finder/references/lviv_specialists.json`. Lviv contacts in wiki.