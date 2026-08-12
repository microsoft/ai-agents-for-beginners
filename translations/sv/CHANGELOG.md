# Ändringslogg

Alla betydande ändringar i kursen **AI Agents for Beginners** dokumenteras i denna fil.

## [Släppt] — 2026-07-14

Denna version flyttar kursen bort från två nyligen föråldrade modeller, migrerar de återstående Lektionerna till stabila Microsoft Agent Framework API och validerar Python-notebooks mot en live Microsoft Foundry-distribution.

### Ändrat

- **Flyttat bort från föråldrade modeller (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Både `gpt-4.1` och `gpt-4.1-mini` är nu föråldrade (officiellt pensionsdatum **14 oktober 2026**). Ersatte alla referenser i kursen (dokumentation, `.env.example`, Python/.NET notebooks och exempel) med den icke-föråldrade `gpt-5-mini`. Lektion 16:s modellruttnings-exempel behåller en liten/stor kontrast med `gpt-5-nano` (liten) och `gpt-5-mini` (stor). Levererade tredjepartsfiler ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), historisk GitHub Models-text och `azure-openai-to-responses`-färdighetens förmåger anteckningar lämnades medvetet oförändrade.
- **Lektion 14 handoff-notebook migrerad till stabila API.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) använder nu `agent_framework.orchestrations.HandoffBuilder` med `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, streaming baserat på `event.type`, och `FoundryChatClient` (ersätter de borttagna pre-1.0-symbolerna `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Lektion 14 human-in-the-loop notebook migrerad till stabila API.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) pausar nu via `ctx.request_info(...)` + `@response_handler` (ersätter de borttagna `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), bygger med `WorkflowBuilder(start_executor=..., output_executors=[...])`, styr strukturerad output via `default_options={"response_format": ...}`, och använder ett skriptat svar så notebooken körs utan övervakning (ingen blockerande `input()`).
- **Miljökonfiguration** ([.env.example](../../.env.example)): bytte modell-distributionsnamn till `gpt-5-mini`; lade till `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (Lektion 16 routing) och den tidigare saknade `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (Lektion 15 browser-use).
- **Beroenden** ([requirements.txt](../../requirements.txt)): fäste `agent-framework`, `agent-framework-foundry` och `agent-framework-openai` till version `~=1.10.0` för en självkonsekvent, validerad uppsättning (1.11.0 levererar experimentella brytande ändringar för de ytor som dessa lektioner använder).

### Noteringar och kända begränsningar

- **Validerade mot live Microsoft Foundry.** Python-notebooks kördes headless med `nbconvert` mot ett Microsoft Foundry-projekt som använde `gpt-5-mini` (och `gpt-5-nano` för Lektion 16 routing). Distribuera motsvarande icke-föråldrade modeller i ditt eget projekt; notebooks läser distributionsnamnet från `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Kräver fortfarande extra resurser för vissa lektioner.** Lektion 05 behöver Azure AI Search; Lektion 08 Bing-grounding-workflow (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) behöver en Bing-anslutning och Microsoft Foundry Agent Service värdverktyg; Lektion 13 (Cognee) och Lektion 17 (Foundry Local) behöver egen runtime.

## [Släppt] — 2026-07-13

Denna version lägger till två nya lektioner som fullbordar distributionsbågen — att skala agenter upp till Microsoft Foundry och ner till en enda arbetsstation — samt ett rök-test pipeline, uppdaterad kursnavigering, nya lärandefärdigheter och uppdaterad varumärkesprofil.

### Tillagt

- **Lektion 16 — Distribuera skalbara agenter med Microsoft Foundry.** Ny lektion [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) och körbar notebook [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) som bygger en produktionsagent för kundsupport (verktyg, RAG, minne, modellrutning, cache för svar, godkännande av människa, en evalueringsgrind och OpenTelemetry-tracing), med utvecklings-/distributions-/kördiagram i Mermaid, kunskapskontroll, uppgift och utmaning.
- **Lektion 17 — Skapa lokala AI-agenter med Foundry Local och Qwen.** Ny lektion [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) och notebook [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) som bygger en helt enhetsbaserad teknisk assistent (Qwen funktionsanrop via Foundry Local, sandboxade filverktyg, lokal RAG med Chroma, valfri lokal MCP), med diagram för endast lokal / lokal RAG / verktygsanrop, kunskapskontroll, uppgift och utmaning.
- **Rök-test pipeline.** Ny [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) workflow [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) plus per-lektion kataloger under [tests/](./tests/README.md) för distribuerbara agenter i Lektion 01, 04, 05 och 16, med en index-README som kopplar varje katalog till dess lektion och värd-agentnamn. Lektion 16 får en avsnitt "Validera en distribuerad agent med rök-test"; Lektioner 01/04/05 får en valfri pekare till rök-test.
- **Lärandefärdigheter.** Nya Agent Skills under `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (paketerar vägledningen från Lektion 16 och 17), och [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (hur man validerar notebook-exemplen mot en live Microsoft Foundry / Azure OpenAI installation).
- **Notebook-valideringsverktyg.** Nya [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) som kör varje Python-notebook headless med `nbconvert` och skriver ut en PASS/FAIL-matris (plus `results.json`). Den upptäcker automatiskt repo-roten och Python, exkluderar icke-kurs notebooks (`.venv`, `site-packages`, `translations`, färdighetsmallstillgångar) och `.NET` notebooks som standard, och stöder `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` och `-Python`.
- **Kursnavigering.** Lade till tidigare/nästa lektion länkar till Lektion 11–15 (saknades tidigare) så hela kursen kedjas 00 → 18 i båda riktningarna.
- **Nya miniatyrbilder.** Lektionminiatyrbilder för Lektion 16 och 17, plus en uppdaterad social bild för repo [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (annonserar nu de två nya lektionerna och `aka.ms/ai-agents-beginners` URL).
- **Beroenden** ([requirements.txt](../../requirements.txt)): lade till `foundry-local-sdk` och `chromadb` för Lektion 17.

### Ändrat

- **Huvud [README.md](./README.md)** lektionstabell: Lektion 16 och 17 länkas nu till sitt innehåll (tidigare "Kommer snart"); repon bild uppdaterad till `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: lade till Lektion 16 och 17 till lektion-för-lektion-guiden och lärandestigar, samt ett avsnitt "Validera distribuerade agenter med rök-test".
- **[AGENTS.md](./AGENTS.md)**: uppdaterade antalet lektioner/beskrivning (00–18), lade till rök-test valideringsavsnitt, och lade till namngivningsexempel för Lektion 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Föregående lektion" pekar nu på Lektion 17 (var Lektion 15), vilket stänger kedjan.
- **Standardiserade modellreferenser till icke-föråldrade modeller.** Ersatte alla `gpt-4o` / `gpt-4o-mini` referenser i hela kursen (dokumentation, `.env.example`, Python/.NET notebooks och exempel) med `gpt-4.1-mini` — `gpt-4o` (alla versioner) pensioneras år 2026. Lektion 16:s modell-ruttningsexempel behåller en liten/stor kontrast med `gpt-4.1-mini` (liten) och `gpt-4.1` (stor). Python-notebooks väljer nu modell från miljövariabler (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) istället för att hårdkoda modellnamn.

### Noteringar och kända begränsningar

- **Körs inte mot live Azure.** De nya lektionernas notebooks är utbildningsexempel; kör och validera dem mot din egen Microsoft Foundry / Foundry Local-installation. Rök-test-workflow kräver att du distribuerar lektionens agent och konfigurerar Azure OIDC-hemligheter (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) med rollen **Azure AI User** på Foundry projektomfång.
- **Lektion 17 är endast lokal.** Den har ingen Foundry Responses-endpoint, så rök-test-åtgärden gäller inte; validera den genom att köra notebooken på din arbetsstation.

## [Släppt] — 2026-07-06

Denna version migrerar kursen till **Azure OpenAI Responses API**, standardiserar produktnamn på **Microsoft Foundry** och **Microsoft Agent Framework (MAF)**, pensionerar GitHub Models, uppdaterar SDK-versioner och lägger till nytt innehåll om lokala modeller och att hosta andra ramverk på Foundry.

### Tillagt

- **Migrerings-färdighet** — Installerade [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (från [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) under `.agents/skills/`, inklusive dess referenser och skanningsscript.
- **Foundry Local (kör modeller på enheten)** — Nytt avsnitt "Alternativ leverantör: Foundry Local" i [00-course-setup/README.md](./00-course-setup/README.md) som täcker installation (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` och kopplar `FoundryLocalManager` till Microsoft Agent Framework via `OpenAIChatClient`.
- **Hosta LangChain / LangGraph agenter på Microsoft Foundry** — Nytt avsnitt i [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus körbart exempel [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) som använder `langchain-azure-ai[hosting]` och `ResponsesHostServer` (protokoll `/responses`), baserat på [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nytt "Verklig värld-exempel: Microsoft Project Opal" avsnitt i [15-browser-use/README.md](./15-browser-use/README.md) som ramar in Opal som en agent för företagsanvändning av datorer och kartlägger den till kurskoncept (human-in-the-loop, tillit/säkerhet, planering, färdigheter).
- **Andra Lektion 02 Python-exemplet** — Lagt till [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (se "Ändrat" — migrerad från tidigare Semantic Kernel notebook) och länkat det i lektionens README.
- Avsnittet **Modeller och leverantörer** tillagd i [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Ändrat

- **Chat Completions → Responses API (Python).** Exempel som kallade modellen direkt migrerades från Chat Completions till Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`) med `OpenAI`-klienten mot den stabila Azure OpenAI `/openai/v1/`-endpointen (ingen `api_version`). Påverkade exempel inkluderar:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — komplett genomgång av funktionsanrop (verktygsschema omvandlat till Responses-format, verktygsresultat returnerade som `function_call_output`, `max_output_tokens`, etc.).

- **GitHub Models → Azure OpenAI.** GitHub Models är föråldrat (avvecklas **juli 2026**) och stöder inte Responses API. Alla GitHub Models kodvägar konverterades till Azure OpenAI / Microsoft Foundry i både Python- och .NET-exempel:
  - Python: Lesson 08 arbetsflödesanteckningsböcker (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + tillhörande `.md`-dokumentation, och Lesson 08 dotNET arbetsflödesanteckningsböcker/`.md` (`01`–`03`) använder nu `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` med `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Den tidigare `02-semantic-kernel.ipynb` skrevs om för att använda Microsoft Agent Framework med Azure OpenAI (Responses API) och bytte namn till `02-python-agent-framework-azure-openai.ipynb`.
- **Standardiserat på `FoundryChatClient` + `as_agent`.** README och notebook-kod som refererade till `AzureAIProjectAgentProvider` standardiserades till det kanoniska mönstret som används i Lesson 01 och ramverkets egna exempel: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` med `provider.as_agent(...)`. Uppdaterat i Lesson 02–14 README-filer och notebooks (t.ex. Lesson 13 minne, alla Lesson 14 notebooks, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Produktnamn.** Omdöpt i hela den engelska innehållet:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Oförändrat: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" och miljövariabelnamn.)
- **Beroenden** ([requirements.txt](../../requirements.txt)):
  - Fäst `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Fäst `openai>=1.108.1` (minimum för Responses API).
  - Tog bort `azure-ai-inference` (användes bara av migrerade GitHub Models-exempel).
- **Miljökonfiguration** ([.env.example](../../.env.example)): tog bort GitHub Models variabler (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); lade till `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` och valfri `AZURE_OPENAI_API_KEY`; uppdaterade namngivning till Microsoft Foundry.
- **Dokumentation** — Uppdaterade [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) och [STUDY_GUIDE.md](./STUDY_GUIDE.md) för ovanstående (inställning av miljövariabler, verifieringskod, leverantörsvägledning, namn).

### Borttaget

- GitHub Models introduktionssteg och miljövariabler från installationsdokumentationen (ersatt av Azure OpenAI / Microsoft Foundry).

### Säkerhet / Integritet (rensa offentlig delning)

- Rensade Jupyter-notebook körningsutdata som läckte en verklig **Azure-prenumerations-ID**, resursgrupps-/resursnamn, samt Bing-anslutnings-ID, plus utvecklarens **lokala filvägar och användarnamn**, i:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Verifierat att inga API-nycklar, tokens, prenumerations-ID:n eller personliga sökvägar finns kvar i den spårade engelska innehållet (de `GITHUB_TOKEN`-referenser som finns är GitHub Actions-token i arbetsflöden och GitHub MCP server PAT i Lesson 11 setup — båda legitima och orelaterade till GitHub Models).

### Noteringar och kända begränsningar

- **Ej körda/kompilerade.** Dessa är utbildningsexempel uppdaterade för API-/namnkorrigering; de kördes inte mot levande Azure-resurser, och .NET-exemplen kompilerades inte i denna miljö. Validera mot din egen Microsoft Foundry / Azure OpenAI-distribution.
- **Modelldistribution måste stödja Responses API.** Använd en distribution som `gpt-4.1-mini`, `gpt-4.1` eller en `gpt-5.x` modell. Äldre modeller stöder kärnfunktionaliteter i Responses men inte alla funktioner.
- **Agent-framework version.** Exemplen riktar sig mot senaste MAF (`>=1.10.0`). Den kanoniska agent-skapande anropet är `client.as_agent(...)`; API:er validerades mot ramverkets publicerade dokumentation och en installerad build. Om du fäster en annan version, bekräfta metodtillgänglighet (`as_agent` vs `create_agent`).
- **Lesson 08 arbetsflödesanteckningsbok 04** behåller avsiktligt `AzureAIAgentClient` (från `agent-framework-azure-ai`) eftersom den använder Microsoft Foundry Agent Service hostade verktyg (Bing grounding, kodtolk); den är redan baserad på Responses.
- **.NET standarddistribution.** Två Lesson 08 dotNET arbetsflödesexempel hårdkodade tidigare en specifik modell; de använder nu `AZURE_OPENAI_DEPLOYMENT` som standard (`gpt-4.1-mini`). Om ett exempel kräver multimodalt/visionsinmatning, sätt `AZURE_OPENAI_DEPLOYMENT` till en lämplig modell.
- **Foundry Local** exponerar en OpenAI-kompatibel **Chat Completions**-endpoint och är avsedd för lokal utveckling; använd Azure OpenAI / Microsoft Foundry för fullständiga Responses API-funktioner.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->