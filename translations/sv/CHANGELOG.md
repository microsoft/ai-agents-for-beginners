# Changelog

Alla viktiga ändringar i kursen **AI Agents for Beginners** dokumenteras i denna fil.

## [Ej släppt] — 2026-07-06

Denna version migrerar kursen till **Azure OpenAI Responses API**, standardiserar produktnamn på **Microsoft Foundry** och **Microsoft Agent Framework (MAF)**, pensionerar GitHub Models, uppdaterar SDK-versioner och lägger till nytt innehåll om lokala modeller och hosting av andra ramverk på Foundry.

### Tillagt

- **Migration skill** — Installerade [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (från [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) under `.agents/skills/`, inklusive dess referenser och scanner-script.
- **Foundry Local (kör modeller på enheten)** — Ny sektion "Alternative Provider: Foundry Local" i [00-course-setup/README.md](./00-course-setup/README.md) som täcker installation (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` och koppling av `FoundryLocalManager` till Microsoft Agent Framework via `OpenAIChatClient`.
- **Hosta LangChain / LangGraph-agenter på Microsoft Foundry** — Ny sektion i [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus ett körbart exempel [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) som använder `langchain-azure-ai[hosting]` och `ResponsesHostServer` (protokollet `/responses`), baserat på [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Ny sektion "Real-World Example: Microsoft Project Opal" i [15-browser-use/README.md](./15-browser-use/README.md) som ramverkar Opal som en agent för företagsdatoranvändning och kopplar den till kursens koncept (human-in-the-loop, förtroende/säkerhet, planering, Skills).
- **Andra lektionen 02 Python-exempel** — Lade till [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (se "Changed" — migrerad från det tidigare Semantic Kernel-notebooken) och länkade den i lektionens README.
- **Modeller och leverantörer** sektion tillagd i [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Ändrat

- **Chat Completions → Responses API (Python).** Exempel som kallade modellen direkt migrerades från Chat Completions till Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), med `OpenAI`-klienten mot den stabila Azure OpenAI `/openai/v1/`-endpointen (ingen `api_version`). Påverkade exempel inkluderar:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — hela genomgången för funktionsanrop (verktygsschema omvandlat till Responses-format, verktygsresultat returnerade som `function_call_output`, `max_output_tokens`, osv.).
- **GitHub Models → Azure OpenAI.** GitHub Models är föråldrat (pensioneras **juli 2026**) och stödjer inte Responses API. Alla GitHub Models-kodvägar konverterades till Azure OpenAI / Microsoft Foundry i Python- och .NET-exempel:
  - Python: Lektion 08 arbetsflödesnotebookar (`01`–`03`), Lektion 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + tillhörande `.md`-dokument och Lektion 08 dotNET arbetsflödesnotebookar/`.md` (`01`–`03`) använder nu `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` med `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Den tidigare `02-semantic-kernel.ipynb` omskrevs för att använda Microsoft Agent Framework med Azure OpenAI (Responses API) och bytte namn till `02-python-agent-framework-azure-openai.ipynb`.
- **Standardiserat på `FoundryChatClient` + `as_agent`.** README och notebook-kod som refererade till `AzureAIProjectAgentProvider` standardiserades till det kanoniska mönstret som används i Lektion 01 och ramverkets egna exempel: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` med `provider.as_agent(...)`. Uppdaterat i Lektion 02–14:s README och notebookar (t.ex. Lektion 13-minne, alla Lektion 14-notebookar, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Produktnamn.** Omdöpt genomgående i engelskt innehåll:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Oförändrat: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" och miljövariabelnamn.)
- **Beroenden** ([requirements.txt](../../requirements.txt)):
  - Pekade på `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Pekade på `openai>=1.108.1` (minimalt för Responses API).
  - Tog bort `azure-ai-inference` (var bara använt i de migrerade GitHub Models-exemplen).
- **Miljökonfiguration** ([.env.example](../../.env.example)): tog bort GitHub Models-variabler (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); lade till `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` och valfri `AZURE_OPENAI_API_KEY`; uppdaterade namngivning till Microsoft Foundry.
- **Dokumentation** — Uppdaterade [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) och [STUDY_GUIDE.md](./STUDY_GUIDE.md) för ovanstående (konfigurera env-variabler, verifieringskod, leverantörsrekommendationer, namngivning).

### Borttaget

- GitHub Models introduktionssteg och miljövariabler från installationsdokumentationen (ersatt av Azure OpenAI / Microsoft Foundry).

### Säkerhet / Integritet (städning av offentlig delning)

- Rensade Jupyter notebook-körningsutdata som läckte riktig **Azure-prenumerations-ID**, resursgrupps-/resursnamn och Bing-anslutnings-ID, plus utvecklarens **lokala filvägar och användarnamn**, i:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Verifierade att inga API-nycklar, tokens, prenumerations-ID eller personliga vägar finns kvar i det spårade engelska innehållet (de `GITHUB_TOKEN`-referenser som finns kvar är GitHub Actions-token i arbetsflöden och GitHub MCP server PAT i Lektion 11-installationen — båda legitima och orelaterade till GitHub Models).

### Noteringar och kända begränsningar

- **Ej exekverat/kompilerat.** Detta är utbildningsexempel uppdaterade för API-/namnkorrekthet; de kördes inte mot levande Azure-resurser och .NET-exemplen kompilerades inte i denna miljö. Validera mot din egen Microsoft Foundry / Azure OpenAI-distribution.
- **Modelldistribution måste stödja Responses API.** Använd en distribution som `gpt-4o-mini`, `gpt-4.1` eller en `gpt-5.x`-modell. Äldre modeller stödjer kärnfunktionalitet för Responses men inte alla funktioner.
- **Agent-framework-version.** Exemplen riktar sig till senaste MAF (`>=1.10.0`). Kanoniskt agent-skapande anrop är `client.as_agent(...)`; API:er validerades mot ramverkets publicerade dokumentation och en installerad byggnad. Om du pekar på en annan version, bekräfta metodtillgänglighet (`as_agent` vs `create_agent`).
- **Lektion 08 arbetsflödesnotebook 04** behåller medvetet `AzureAIAgentClient` (från `agent-framework-azure-ai`) eftersom den använder Microsoft Foundry Agent Service-hostade verktyg (Bing grounding, kodtolk); den är redan Responses-baserad.
- **.NET standarddistribution.** Två Lektion 08 dotNET arbetsflödesexempel hade tidigare hårdkodad `gpt-4o`; de använder nu standardvärdet `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Om ett exempel förlitar sig på multimodalt/syninmatning, ställ `AZURE_OPENAI_DEPLOYMENT` till en lämplig modell.
- **Foundry Local** exponerar en OpenAI-kompatibel **Chat Completions**-endpoint och är avsedd för lokal utveckling; använd Azure OpenAI / Microsoft Foundry för hela Responses API-funktionaliteten.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->