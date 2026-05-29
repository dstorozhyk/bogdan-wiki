User is Denys (Senior .NET/C# developer, PhD, also Python/TypeScript). He likes a direct, informal tone. Communication is in Ukrainian (with some Russian mix). He has other Hermes profiles (including "girlfriend profiles") that he'll discuss later. Full access to infrastructure is expected. The agent is called Bohdan/Богдан/Бодя.
§
GitHub authenticated as dstorozhyk via gh CLI with a Fine-grained PAT. Token stored in ~/.config/gh/hosts.yml. Access can be expanded dynamically by Denys in GitHub UI without replacing the token.
§
Profile "freylina" created — Telegram assistant/bot for Karina Polischuk's "Все про Royal" project about royal families. Bot token configured, gateway running as systemd service hermes-gateway-freylina. Allowed user: 441672981 (Denys). SOUL.md set to Freylina persona — virtual lady-in-waiting and assistant for the blogger. Inherits main profile's model/provider (deepseek/deepseek-v4-flash via OpenRouter).
§
/balance uses direct_script patches in Hermes source code: agent/skill_commands.py (~L316) and gateway/run.py (~L7725) in /usr/local/lib/hermes-agent/. Patches get OVERWRITTEN on Hermes update. After updating Hermes, re-apply patches or /balance will return JSON / fail.
§
**Hermes провайдери — Денис хоче приоритет:**
1. Claude Haiku (основний, швидко + дешево)
2. Google Gemini 2.5 Flash (резерв, коли Haiku)
3. GPT-4.1 (резерв)
4. DeepSeek v4 Flash (остаточний резерв, платний але надійний)

Це налаштування застосовується на **обидва** профілі: основний і `freylina`. Gemini на безкоштовному плані, має ліміти (250k токенів), тому fallback механізм критичний.
§
**Wiki System** — LLM wikis synced daily to dstorozhyk/bogdan-wikis: Default profile (main branch) for general KB; Freylina (freylina branch) for royal families. Auto-sync 04:00/05:00 UTC. WIKI_PATH envvars set per profile.
§
**VPS Monitor Dashboard** — ~/.hermes/data/vps-monitor/. Start: ~/.hermes/bin/vps-monitor.sh {start|stop|status}. http://localhost:3000, pw: Клубняк2007.