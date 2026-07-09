# Změny

Všechny významné změny v kurzu **AI Agenti pro začátečníky** jsou zdokumentovány v tomto souboru.

## [Nevydané] — 2026-07-06

Toto vydání migruje kurz na **Azure OpenAI Responses API**, standardizuje pojmenování produktů na **Microsoft Foundry** a **Microsoft Agent Framework (MAF)**, ukončuje GitHub Models, aktualizuje verze SDK a přidává nový obsah o lokálních modelech a hostování dalších frameworků na Foundry.

### Přidáno

- **Dovednost migrace** — Instalace Agent Skill [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (z [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) pod `.agents/skills/`, včetně jejích odkazů a skriptu pro skenování.
- **Foundry Local (spouštění modelů lokálně na zařízení)** — Nová sekce "Alternativní poskytovatel: Foundry Local" v [00-course-setup/README.md](./00-course-setup/README.md) pokrývající instalaci (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` a propojení `FoundryLocalManager` s Microsoft Agent Framework pomocí `OpenAIChatClient`.
- **Hostování LangChain / LangGraph agentů na Microsoft Foundry** — Nová sekce v [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus spustitelný příklad [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) používající `langchain-azure-ai[hosting]` a `ResponsesHostServer` (protokol `/responses`), založený na [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nová sekce "Reálný příklad: Microsoft Project Opal" v [15-browser-use/README.md](./15-browser-use/README.md) představující Opal jako agenta pro firemní využití počítače a mapující jej na koncepty kurzu (člověk v cyklu, důvěra/bezpečnost, plánování, dovednosti).
- **Druhý ukázkový příklad Python pro lekci 02** — Přidána [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (viz "Změněno" — migrováno z bývalého notebooku Semantic Kernel) a propojen v README lekce.
- Přidána sekce **Modely a poskytovatelé** do [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Změněno

- **Chat Completions → Responses API (Python).** Vzorky, které volaly model přímo, byly migrovány z Chat Completions na Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), s použitím `OpenAI` klienta proti stabilnímu Azure OpenAI `/openai/v1/` endpointu (bez `api_version`). Dotčené příklady zahrnují:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — kompletní průchod voláním funkce (schéma nástroje převedeno do formátu Responses, výsledky nástrojů vráceny jako `function_call_output`, `max_output_tokens`, atd.).
- **GitHub Models → Azure OpenAI.** GitHub Models je zastaralý (ukončení **červenec 2026**) a nepodporuje Responses API. Všechny cesty kódu GitHub Models byly převedeny na Azure OpenAI / Microsoft Foundry v Python i .NET příkladech:
  - Python: notebooky workflow Lekce 08 (`01`–`03`), Lekce 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + doprovodné `.md` dokumenty, a workflow notebooky/`.md` Lekce 08 (`01`–`03`) nyní používají `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` s `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Bývalý `02-semantic-kernel.ipynb` byl přepsán tak, aby používal Microsoft Agent Framework s Azure OpenAI (Responses API) a přejmenován na `02-python-agent-framework-azure-openai.ipynb`.
- **Standardizace na `FoundryChatClient` + `as_agent`.** README a kód v noteboocích, které odkazovaly na `AzureAIProjectAgentProvider`, byly standardizovány dle kanonického vzoru použitého v Lekci 01 a vzorcích frameworku: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` s `provider.as_agent(...)`. Aktualizováno v README a noteboocích Lekcí 02–14 (např. paměť Lekce 13, všechny noteboocy Lekce 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Pojmenování produktů.** Přejmenováno napříč anglickým obsahem:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Beze změny: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" a názvy proměnných prostředí.)
- **Závislosti** ([requirements.txt](../../requirements.txt)):
  - Přesně stanovené `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Přesně stanovené `openai>=1.108.1` (minimální pro Responses API).
  - Odstraněno `azure-ai-inference` (používalo se pouze u migrovaných vzorků GitHub Models).
- **Konfigurace prostředí** ([.env.example](../../.env.example)): odstraněny proměnné GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); přidány `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` a volitelný `AZURE_OPENAI_API_KEY`; aktualizováno pojmenování na Microsoft Foundry.
- **Dokumentace** — Aktualizovány [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) a [STUDY_GUIDE.md](./STUDY_GUIDE.md) odpovídajícím způsobem (nastavení proměnných prostředí, ověřovací úryvek, návody k poskytovateli, pojmenování).

### Odstraněno

- Kroky onboardingu GitHub Models a proměnné prostředí z instalačních dokumentů (nahrazeno Azure OpenAI / Microsoft Foundry).

### Bezpečnost / Soukromí (vyčištění pro veřejné sdílení)

- Vyčištěny výstupy z Jupyter notebooků, které prozrazovaly skutečné **Azure subscription ID**, názvy resource group / resource a Bing connection ID, plus vývojářské **lokální cesty a uživatelská jména**, v:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Ověřeno, že v sledovaném anglickém obsahu nezůstal žádný klíč API, token, ID předplatného ani osobní cesty (reference na `GITHUB_TOKEN` zůstávají tokenem GitHub Actions ve workflows a GitHub MCP serverovým PAT v nastavení Lekce 11 – obojí legitimní a nesouvisející s GitHub Models).

### Poznámky a známá omezení

- **Nespouštěné/nesestavené.** Jedná se o vzdělávací příklady aktualizované pro správnost API/pojmenování; nebyly spuštěny vůči živým Azure zdrojům a .NET příklady nebyly v tomto prostředí sestaveny. Ověřte na vlastní implementaci Microsoft Foundry / Azure OpenAI.
- **Nasazení modelu musí podporovat Responses API.** Použijte nasazení jako `gpt-4o-mini`, `gpt-4.1` nebo model `gpt-5.x`. Starší modely podporují základní funkce Responses, ale ne všechny vlastnosti.
- **Verze agent-frameworku.** Příklady cílí na nejnovější MAF (`>=1.10.0`). Kanonický volací vzor vytvoření agenta je `client.as_agent(...)`; API bylo ověřeno podle publikovaných dokumentů frameworku a nainstalované verze. Pokud použijete jinou verzi, ověřte dostupnost metod (`as_agent` vs `create_agent`).
- **Workflow notebook Lekce 08, ukázka 04** záměrně zachovává `AzureAIAgentClient` (z `agent-framework-azure-ai`), protože používá nástroje hostované Microsoft Foundry Agent Service (Bing grounding, interpreter kódu); již je založen na Responses.
- **.NET výchozí nasazení.** Dvě workflow ukázky Lekce 08 pro dotNET dříve pevně kódovaly `gpt-4o`; nyní implicitně používají `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Pokud ukázka spoléhá na multimodální/vision vstup, nastavte `AZURE_OPENAI_DEPLOYMENT` na vhodný model.
- **Foundry Local** zpřístupňuje OpenAI-kompatibilní endpoint **Chat Completions** a je určen pro lokální vývoj; pro plný rozsah funkcí Responses API používejte Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->