# Változásnapló

Minden jelentős változás az **AI Agents for Beginners** tanfolyamhoz ebben a fájlban van dokumentálva.

## [Kiadatlan] — 2026-07-06

Ez a kiadás áthelyezi a tanfolyamot az **Azure OpenAI Responses API** használatára, egységesíti a termékneveket a **Microsoft Foundry** és a **Microsoft Agent Framework (MAF)** körében, kivonja a GitHub Modelleket, frissíti az SDK verziókat, valamint új tartalmat ad hozzá a helyi modellekről és más keretrendszerek Foundry-n történő hosztolásáról.

### Hozzáadva

- **Migrációs képesség** — Telepítve az [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (az [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses) projektből) a `.agents/skills/` mappába, beleértve a hivatkozásait és a szkenner scriptet.
- **Foundry Local (modellek futtatása készüléken)** — Új "Alternatív Szolgáltató: Foundry Local" szakasz a [00-course-setup/README.md](./00-course-setup/README.md) fájlban, amely lefedi a telepítést (`winget` / `brew`), a `foundry model run` parancsot, a `foundry-local-sdk`-t és a `FoundryLocalManager` Microsoft Agent Frameworkhöz való csatlakoztatását az `OpenAIChatClient`-en keresztül.
- **LangChain / LangGraph ügynökök hosztolása Microsoft Foundry-n** — Új szakasz a [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) fájlban, továbbá futtatható példa [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) `langchain-azure-ai[hosting]` és `ResponsesHostServer` (a `/responses` protokoll) használatával, a [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) alapján.
- **Microsoft Project Opal** — Új "Valós Példa: Microsoft Project Opal" szakasz a [15-browser-use/README.md](./15-browser-use/README.md) fájlban, amely az Opalt vállalati számítógép-használati ügynökként mutatja be és kapcsolatba hozza a tanfolyam fogalmaival (human-in-the-loop, bizalom/biztonság, tervezés, képességek).
- **Második Lecke 02 Python példa** — Hozzáadva a [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (lásd a "Changed" pontot — átvitel a korábbi Semantic Kernel jegyzetfüzetből), és belinkelve a lecke README-jében.
- **Modellek és Szolgáltatók** szakasz hozzáadva a [STUDY_GUIDE.md](./STUDY_GUIDE.md) fájlhoz.

### Módosítva

- **Chat Completions → Responses API (Python).** Azokat a példákat, amelyek közvetlenül hívták a modellt, áthelyeztük a Chat Completions-ról a Responses API-ra (`client.responses.create(input=..., store=False)`, `resp.output_text`), az `OpenAI` klienssel az Azure OpenAI stabil `/openai/v1/` végpontja ellen (api_version nélkül). Az érintett példák:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — a teljes függvényhívó bemutató (eszközséma átformálva a Responses formátumra, eszköz eredmények visszaadva `function_call_output`, `max_output_tokens` stb. formában).
- **GitHub Modellek → Azure OpenAI.** A GitHub Modellek elavultak (2026 júliusától eltávolítva), és nem támogatják a Responses API-t. Minden GitHub Modellek kód útvonal át lett konvertálva Azure OpenAI / Microsoft Foundry-ra Python és .NET példákban:
  - Python: Lecke 08 workflow jegyzetfüzetek (`01`–`03`), Lecke 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + társ `.md` dokumentumok, valamint a Lecke 08 dotNET workflow jegyzetfüzetek/`.md` (`01`–`03`) mostantól a `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` metódust használják `AzureCliCredential`-lel.
- **Semantic Kernel → Microsoft Agent Framework.** A korábbi `02-semantic-kernel.ipynb` újraírásra került a Microsoft Agent Framework használatával Azure OpenAI (Responses API) alapon, és át lett nevezve `02-python-agent-framework-azure-openai.ipynb`-re.
- **Standardizálva a `FoundryChatClient` + `as_agent` használata.** A README és jegyzetfüzet kódok, amelyek az `AzureAIProjectAgentProvider`-t használták, egységesítve lettek a kanonikus mintára, amelyet a Lecke 01 és a keretrendszer saját példái használnak: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` és `provider.as_agent(...)`. Frissítve a Lecke 02–14 README-ken és jegyzetfüzeteken (pl. Lecke 13 memória, minden Lecke 14 jegyzetfüzet, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Terméknevek.** Átnevezve az angol tartalomban:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Nem változott: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", és környezeti változó nevek.)
- **Függőségek** ([requirements.txt](../../requirements.txt)):
  - Fixált `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Fixált `openai>=1.108.1` (a Responses API minimális követelménye).
  - Eltávolítva az `azure-ai-inference` (csak a migrált GitHub Modellek példák használták).
- **Környezeti beállítás** ([.env.example](../../.env.example)): eltávolítva a GitHub Modellek változók (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); hozzáadva `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, és opcionálisan `AZURE_OPENAI_API_KEY`; frissítve a névhasználat Microsoft Foundry-ra.
- **Dokumentációk** — Frissítve a [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), és [STUDY_GUIDE.md](./STUDY_GUIDE.md) a fentiekhez (környezeti változók beállítása, ellenőrző kód, szolgáltató irányelvek, elnevezés).

### Eltávolítva

- GitHub Modellek onboardolási lépései és környezeti változói a telepítési dokumentációkból (azok helyébe Azure OpenAI / Microsoft Foundry lép).

### Biztonság / Adatvédelem (nyilvános megosztás tisztítás)

- Kitisztítva a Jupyter jegyzetfüzetek végrehajtási kimenetei, amelyek valódi **Azure előfizetési azonosítót**, erőforrás-csoport / erőforrás nevét és Bing kapcsolatazonosítót, valamint fejlesztői **helyi fájl elérési útvonalakat és felhasználóneveket** szivárogtattak:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Ellenőrizve, hogy nem maradt API kulcs, token, előfizetési azonosító vagy személyes elérési út a követett angol tartalomban (a `GITHUB_TOKEN` hivatkozások, amelyek megmaradtak, a GitHub Actions token a workflow-kban és a GitHub MCP szerver PAT a Lecke 11 beállításában — mindkettő legális és nem kapcsolódik a GitHub Modellekhez).

### Megjegyzések és ismert korlátok

- **Nem futtatott/fordított minták.** Ezek oktató példák API/név helyesség szempontjából frissítve; nem futtatták élő Azure erőforrásokon, és a .NET példák nem lettek lefordítva ebben a környezetben. Ellenőrizze a saját Microsoft Foundry / Azure OpenAI telepítésén.
- **A modell telepítésének támogatnia kell a Responses API-t.** Használjon olyan telepítést, mint a `gpt-4o-mini`, `gpt-4.1` vagy `gpt-5.x` modell. A régebbi modellek támogatják a Responses API alapvető funkcióit, de nem minden szolgáltatást.
- **Agent-framework verzió.** A példák a legfrissebb MAF verziót célozzák (`>=1.10.0`). A kanonikus ügynök létrehozási hívás a `client.as_agent(...)`; az API-kat validálták a keretrendszer publikált dokumentációja és egy telepített build alapján. Ha más verziót használ, ellenőrizze a metódus elérhetőségét (`as_agent` vagy `create_agent`).
- **Lecke 08 workflow jegyzetfüzet 04** szándékosan megtartja az `AzureAIAgentClient`-et (az `agent-framework-azure-ai`-ből), mert Microsoft Foundry Agent Service által hosztolt eszközöket használ (Bing származtatás, kódértelmező); már Responses alapú.
- **.NET alapértelmezett telepítés.** Két Lecke 08 .NET workflow példa korábban keménykódolt `gpt-4o` modellt; most az `AZURE_OPENAI_DEPLOYMENT` változóra állítódik alapértelmezettként (`gpt-4o-mini`). Ha egy minta multimodális/vizuális bemenetet igényel, állítsa be az `AZURE_OPENAI_DEPLOYMENT` megfelelő modellre.
- **Foundry Local** egy OpenAI-kompatibilis **Chat Completions** végpontot szolgáltat, és helyi fejlesztésre készült; használja az Azure OpenAI / Microsoft Foundry-t a teljes Responses API funkcionalitáshoz.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->