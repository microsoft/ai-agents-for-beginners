# Muudatuste logi

Kõik olulised muudatused kursuses **AI Agents for Beginners** on dokumenteeritud selles failis.

## [Väljaandmata] — 2026-07-06

See versioon viib kursuse üle **Azure OpenAI Responses API**-le, standardiseerib tootemärgistuse **Microsoft Foundry** ja **Microsoft Agent Frameworki (MAF)** puhul, loob GitHub Modelsi toe maha, uuendab SDK versioone ning lisab uut sisu kohalikest mudelitest ja teiste raamistikude majutamisest Foundry-l.

### Lisatud

- **Migreerumise oskus** — Paigaldati [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (allikast [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) kausta `.agents/skills/`, kaasa arvatud selle viited ja skanneri skript.
- **Foundry Local (mudelite käitamine seadmes)** — Uus "Alternatiivne pakkuja: Foundry Local" sektsioon failis [00-course-setup/README.md](./00-course-setup/README.md), mis hõlmab paigaldust (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` ja `FoundryLocalManager` ühendamist Microsoft Agent Frameworkiga läbi `OpenAIChatClient`.
- **LangChain / LangGraph agentide majutamine Microsoft Foundry’l** — Uus sektsioon failis [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) pluss käivitatav näide [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) kasutades `langchain-azure-ai[hosting]` ja `ResponsesHostServer` (protokoll `/responses`), põhineb [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) juhendil.
- **Microsoft Project Opal** — Uus "Reaalmaailma näide: Microsoft Project Opal" sektsioon failis [15-browser-use/README.md](./15-browser-use/README.md), mis esitleb Opalit ettevõtte arvutikasutaja agendina ja seob selle kursuse mõistetega (inimene silmuses, usaldus/turvalisus, planeerimine, oskused).
- **Teise õppetunni 02 Python näide** — Lisatud [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (vt "Muudetud" — migreeriti endisest Semantic Kernel märkmikust) ja link sellel õppetunni README-s.
- Sektsioon **Mudelite ja pakkujate kohta** lisatud faili [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Muudetud

- **Chat Completions → Responses API (Python).** Näited, mis kutsusid mudelit otse, viidi üle Chat Completions’ist Responses API-le (`client.responses.create(input=..., store=False)`, `resp.output_text`), kasutades `OpenAI` klienti stabiilse Azure OpenAI `/openai/v1/` lõpp-punkti vastu (ilma `api_version`’ita). Mõjutatud näidised:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — täielik funktsiooni kutsumise läbivaatus (tööriista skeem ümber tehtud Responses formaati, tööriista tulemused tagastatud kui `function_call_output`, `max_output_tokens` jms).
- **GitHub Models → Azure OpenAI.** GitHub Models on aegunud (eemaldatakse **juulis 2026**) ja ei toeta Responses API-d. Kõik GitHub Modelsi koodirajad muudeti Azure OpenAI / Microsoft Foundry kasutamiseks Python ja .NET näidetes:
  - Python: Õppetunni 08 töövoo märkmikud (`01`–`03`), õppetund 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + kaasnevad `.md` dokumendid, ning õppetunni 08 dotNET töövoo märkmikud/`.md` (`01`–`03`) kasutavad nüüd `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` koos `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Endine `02-semantic-kernel.ipynb` kirjutati ümber Microsoft Agent Frameworki kasutama Azure OpenAI (Responses API) ja nimetati ümber `02-python-agent-framework-azure-openai.ipynb`.
- **Standardiseeritud `FoundryChatClient` + `as_agent`.** README ja märkmiku kood, mis viitas `AzureAIProjectAgentProvider`-ile, standardiseeriti kanonilisele mustrile, mida kasutab õppetund 01 ja raamistik ise: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` koos `provider.as_agent(...)`. Uuendatud õppetundide 02–14 README-d ja märkmikud (nt õppetund 13 mälu, kõik õppetunni 14 märkmikud, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Tootemärgistus.** Inglise sisu ulatuses ümber nimetatud:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Muutmata: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" ja keskkonnamuutujate nimed.)
- **Sõltuvused** ([requirements.txt](../../requirements.txt)):
  - Lukustatud `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Lukustatud `openai>=1.108.1` (vähemalt Responses API jaoks).
  - Eemaldatud `azure-ai-inference` (kasutati ainult migreeritud GitHub Models näidetes).
- **Keskkonna konfiguratsioon** ([.env.example](../../.env.example)): eemaldatud GitHub Models muutujad (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); lisatud `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` ja valikuline `AZURE_OPENAI_API_KEY`; nimed uuendatud Microsoft Foundry jaoks.
- **Dokumentatsioon** — Uuendatud [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) ja [STUDY_GUIDE.md](./STUDY_GUIDE.md) vastavalt eeltoodule (paigalduskeskkonna muutujad, kinnituse näidiskood, pakkuja juhised, nimetus).

### Eemaldatud

- GitHub Modelsi alustamise sammud ja keskkonnamuutujad paigaldusjuhenditest (asendatud Azure OpenAI / Microsoft Foundry’ga).

### Turvalisus / Privaatsus (avaliku jagamise korrastus)

- Tühjendatud Jupyter märkmiku täitmise väljundid, mis lekkisid tõelise **Azure tellimuse ID**, ressursigrupi/ressursside nimed ning Bing ühenduse ID, samuti arendaja **kohalikud failiteed ja kasutajanimed** failides:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Kinnitatud, et jälgitud ingliskeelses sisus ei ole jäänud API võtmeid, tokeneid, tellimuse ID-sid ega isiklikke radu (jäänud `GITHUB_TOKEN` viited on GitHub Actionsi tokenid töövoogudes ning GitHub MCP serveri PAT õppetunni 11 seadistuses – mõlemad seaduslikud ja GitHub Modelsiga mitteseotud).

### Märkused ja teadaolevad piirangud

- **Ei ole käivitatud/kompileeritud.** Need on õppeotstarbelised näited, mis uuendati API/kasutusnõuetele vastavaks; neid ei käideldud otse reaalsete Azure ressursside peal ning .NET näidiseid selles keskkonnas ei kompileeritud. Testige oma Microsoft Foundry / Azure OpenAI juurutuse vastu.
- **Mudeli juurutus peab toetama Responses API-d.** Kasutage juurutust nagu `gpt-4o-mini`, `gpt-4.1` või `gpt-5.x` mudelit. Vanemad mudelid toetavad Responses funktsioone, kuid mitte kõiki.
- **Agent-framework versioon.** Näited kasutavad uusimat MAF versiooni (`>=1.10.0`). Kanoniline agendi loomise kutse on `client.as_agent(...)`; API-sid on kontrollitud raamatu avaldatud dokumentatsiooni ja installeeritud versiooni vastu. Kui kasutate teistsugust versiooni, kinnitage meetodi olemasolu (`as_agent` vs `create_agent`).
- **Õppetundi 08 töövoo märkmikus 04** hoitakse teadlikult `AzureAIAgentClient` (`agent-framework-azure-ai`-st), sest see kasutab Microsoft Foundry Agent Service majutatud tööriistu (Bing aluseks, koodi interpreteerija); see on juba Responses-põhine.
- **.NET vaikimisi deploy.** Kaks õppetunni 08 dotNET töövoo näidet varem kasutasid kõvaks kodeeritud `gpt-4o`; nüüd on vaikimisi `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Kui näide sõltub multimodaalsest/visioon sisendist, seadke `AZURE_OPENAI_DEPLOYMENT` sobivale mudelile.
- **Foundry Local** pakub OpenAI-sarnast **Chat Completions** lõpp-punkti ja on mõeldud kohalikuks arenduseks; kasutage täieliku Responses API funktsionaalsuse jaoks Azure OpenAI / Microsoft Foundryt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->