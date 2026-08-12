# Wijzigingslogboek

Alle belangrijke wijzigingen aan de **AI Agents for Beginners** cursus worden in dit bestand gedocumenteerd.

## [Uitgebracht] — 2026-07-14

Deze release verplaatst de cursus weg van twee recent uitgefaseerde modellen, migreert de resterende Les-notebooks naar de stabiele Microsoft Agent Framework API en valideert de Python-notebooks tegen een actieve Microsoft Foundry-implementatie.

### Gewijzigd

- **Overgestapt van uitgefaseerde modellen (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Zowel `gpt-4.1` als `gpt-4.1-mini` zijn nu uitgefaseerd (officiële retirement datum **14 oktober 2026**). Iedere verwijzing in de cursus (documentatie, `.env.example`, Python/.NET notebooks en voorbeelden) is vervangen door het niet-uitgefaseerde `gpt-5-mini`. Les 16’s model-routingvoorbeeld behoudt een klein/groot contrast met `gpt-5-nano` (klein) en `gpt-5-mini` (groot). Gelinkte bestanden van derden ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), historische GitHub Models-tekst en de capability-notities van de `azure-openai-to-responses` skill zijn opzettelijk ongewijzigd gebleven.
- **Les 14 handoff-notebook gemigreerd naar de stabiele API.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) gebruikt nu `agent_framework.orchestrations.HandoffBuilder` met `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, op `event.type` gebaseerde streaming en `FoundryChatClient` (vervanging voor de verwijderde pre-1.0 symbolen `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Les 14 human-in-the-loop-notebook gemigreerd naar de stabiele API.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) pauzeert nu via `ctx.request_info(...)` + `@response_handler` (vervangen de verwijderde `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), bouwt met `WorkflowBuilder(start_executor=..., output_executors=[...])`, stuurt gestructureerde output door `default_options={"response_format": ...}`, en gebruikt een gescripte antwoord zodat de notebook onbemand kan draaien (geen blokkering door `input()`).
- **Omgevingsconfiguratie** ([.env.example](../../.env.example)): gewijzigde model-implementatienamen naar `gpt-5-mini`; toegevoegd `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (Les 16 routing) en de eerder ontbrekende `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (Les 15 browser-gebruik).
- **Afhankelijkheden** ([requirements.txt](../../requirements.txt)): `agent-framework`, `agent-framework-foundry` en `agent-framework-openai` vastgezet op `~=1.10.0` voor een zelf-consistente, gevalideerde set (1.11.0 brengt experimentele breaking changes voor de interfaces die door deze lessen worden gebruikt).

### Notities en bekende beperkingen

- **Gevalideerd tegen live Microsoft Foundry.** De Python-notebooks werden headless uitgevoerd met `nbconvert` tegen een Microsoft Foundry-project dat `gpt-5-mini` (en `gpt-5-nano` voor Les 16 routing) gebruikt. Implementeer equivalente niet-uitgefaseerde modellen in je eigen project; de notebooks lezen de implementatienaam uit `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Bieden nog steeds aanvullende bronnen nodig voor sommige lessen.** Les 05 heeft Azure AI Search nodig; de Les 08 Bing-ondersteunde workflow (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) heeft een Bing-verbinding en Microsoft Foundry Agent Service gehoste tools nodig; Les 13 (Cognee) en Les 17 (Foundry Local) hebben hun eigen runtimes nodig.

## [Uitgebracht] — 2026-07-13

Deze release voegt twee nieuwe lessen toe die de implementatie-arc compleet maken — schalen van agents tot Microsoft Foundry en terug naar een enkele werkplek — plus een smoke-test pipeline, vernieuwde cursusnavigatie, nieuwe leerdervaardigheden en bijgewerkte branding.

### Toegevoegd

- **Les 16 — Schaalbare Agents implementeren met Microsoft Foundry.** Nieuwe les [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) en uitvoerbare notebook [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) die een productieklantenservice-agent bouwt (tools, RAG, geheugen, model-routing, respons-caching, menselijke goedkeuring, een evaluatiepoort en OpenTelemetry-tracing), met ontwikkeling/implementatie/runtime Mermaid-diagrammen, een kennischeck, een opdracht en een uitdaging.
- **Les 17 — Lokale AI Agents maken met Foundry Local en Qwen.** Nieuwe les [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) en notebook [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) die een volledig op het apparaat werkende engineering-assistent bouwt (Qwen function calling via Foundry Local, gesandboxte bestands-tools, lokale RAG met Chroma, optionele lokale MCP), met lokaal-only / lokaal-RAG / tool-calling diagrammen, een kennischeck, een opdracht en een uitdaging.
- **Smoke-test pipeline.** Nieuwe [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) workflow [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) plus per-les catalogi onder [tests/](./tests/README.md) voor de implementeerbare agents in Lessen 01, 04, 05 en 16, met een index README die elke catalogus aan de les en hosted-agent naam koppelt. Les 16 krijgt een sectie "Validating a Deployed Agent with Smoke Tests"; Lessen 01/04/05 krijgen een optionele smoke-test verwijzing.
- **Leerdervaardigheden.** Nieuwe Agent Skills onder `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (bevat de Richtlijnen van Les 16 en 17) en [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (hoe de notebookvoorbeelden te valideren tegen een live Microsoft Foundry / Azure OpenAI setup).
- **Notebook validatie runner.** Nieuwe [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) die elke Python-notebook headless uitvoert met `nbconvert` en een PASS/FAIL matrix afdrukt (plus `results.json`). Het detecteert automatisch de repo-root en Python, sluit standaard niet-cursusnotebooks uit (`.venv`, `site-packages`, `translations`, skill template assets) en `.NET` notebooks en ondersteunt `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` en `-Python`.
- **Cursusnavigatie.** Toegevoegd Vorige/Volgende lessen-links aan Lessen 11–15 (voorheen ontbrak) zodat de hele cursus 00 → 18 in beide richtingen ketent.
- **Nieuwe thumbnails.** Les-thumbnail afbeeldingen voor Lessen 16 en 17, plus een vernieuwde repository social image [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (nu met reclame voor de twee nieuwe lessen en de URL `aka.ms/ai-agents-beginners`).
- **Afhankelijkheden** ([requirements.txt](../../requirements.txt)): toegevoegd `foundry-local-sdk` en `chromadb` voor Les 17.

### Gewijzigd

- **Hoofd [README.md](./README.md)** lessen-tabel: Lessen 16 en 17 linken nu naar hun inhoud (voorheen "Coming Soon"); repository afbeelding geüpdatet naar `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: lessen 16 en 17 toegevoegd aan de les-voor-les-gids en leerpaden, en een sectie "Validating Deployed Agents with Smoke Tests".
- **[AGENTS.md](./AGENTS.md)**: bijgewerkt lesaantal/beschrijving (00–18), smoke-test validatie sectie toegevoegd, en voorbeeldnamen uit Les 16/17 toegevoegd.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Vorige Les" verwijst nu naar Les 17 (was Les 15), waarmee de keten is gesloten.
- **Gestandaardiseerde modelverwijzingen op niet-uitgefaseerde modellen.** Alle `gpt-4o` / `gpt-4o-mini` verwijzingen in de cursus (documentatie, `.env.example`, Python/.NET notebooks en voorbeelden) vervangen door `gpt-4.1-mini` — `gpt-4o` (alle versies) wordt in 2026 uitgefaseerd. Les 16’s model-routingvoorbeeld behoudt een klein/groot contrast met `gpt-4.1-mini` (klein) en `gpt-4.1` (groot). Python notebooks selecteren nu het model uit omgevingsvariabelen (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) in plaats van harde codering van een modelnaam.

### Notities en bekende beperkingen

- **Niet uitgevoerd tegen live Azure.** De notebooks van de nieuwe lessen zijn educatieve voorbeelden; voer ze uit en valideer ze tegen je eigen Microsoft Foundry / Foundry Local setup. De smoke-test workflow vereist dat je de agent van de les implementeert en Azure OIDC secrets (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) configureert met de **Azure AI User** rol op projectniveau in Foundry.
- **Les 17 is alleen lokaal.** Het heeft geen Foundry Responses endpoint, dus de smoke-test actie is hier niet van toepassing; valideer het door de notebook op je werkstation te draaien.

## [Uitgebracht] — 2026-07-06

Deze release migreert de cursus naar de **Azure OpenAI Responses API**, standaardiseert productnamen op **Microsoft Foundry** en het **Microsoft Agent Framework (MAF)**, faseert GitHub Models uit, werkt SDK-versies bij en voegt nieuwe inhoud toe over lokale modellen en het hosten van andere frameworks op Foundry.

### Toegevoegd

- **Migratie skill** — Geïnstalleerde [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (van [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) onder `.agents/skills/`, inclusief referenties en de scanner-script.
- **Foundry Local (modellen on-device draaien)** — Nieuwe sectie "Alternatieve Provider: Foundry Local" in [00-course-setup/README.md](./00-course-setup/README.md) met installatie (`winget` / `brew`), `foundry model run`, de `foundry-local-sdk` en het aansturen van `FoundryLocalManager` naar het Microsoft Agent Framework via `OpenAIChatClient`.
- **Hosten van LangChain / LangGraph agents op Microsoft Foundry** — Nieuwe sectie in [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus een uitvoerbaar voorbeeld [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) die `langchain-azure-ai[hosting]` en `ResponsesHostServer` (het `/responses`-protocol) gebruikt, gebaseerd op [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nieuwe sectie "Praktijkvoorbeeld: Microsoft Project Opal" in [15-browser-use/README.md](./15-browser-use/README.md) die Opal positioneert als een enterprise computer-gebruik agent en koppelt aan cursusconcepten (human-in-the-loop, vertrouwen/veiligheid, planning, Skills).
- **Tweede Les 02 Python voorbeeld** — Toegevoegd [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (zie "Gewijzigd" — gemigreerd van het oude Semantic Kernel notebook) en gelinkt in de les README.
- **Models en Providers** sectie toegevoegd aan [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Gewijzigd

- **Chat Completions → Responses API (Python).** Voorbeelden die het model direct aanriepen, zijn gemigreerd van Chat Completions naar de Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), met gebruik van de `OpenAI` client tegen de stabiele Azure OpenAI `/openai/v1/` endpoint (zonder `api_version`). Betroffen voorbeelden zijn:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — de volledige walkthrough voor function-calling (toolschema afgevlakt naar het Responses-format, toolresultaten geretourneerd als `function_call_output`, `max_output_tokens`, enzovoort).

- **GitHub-modellen → Azure OpenAI.** GitHub-modellen zijn verouderd (worden **juli 2026** uitgefaseerd) en ondersteunen de Responses API niet. Alle GitHub-modellen codepaden zijn geconverteerd naar Azure OpenAI / Microsoft Foundry in zowel Python- als .NET-voorbeelden:
  - Python: Les 08 workflow notebooks (`01`–`03`), Les 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + begeleidende `.md` documenten, en de Les 08 dotNET workflow notebooks/`.md` (`01`–`03`) gebruiken nu `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` met `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Het voormalige `02-semantic-kernel.ipynb` is herschreven om het Microsoft Agent Framework met Azure OpenAI (Responses API) te gebruiken en hernoemd naar `02-python-agent-framework-azure-openai.ipynb`.
- **Gestandaardiseerd op `FoundryChatClient` + `as_agent`.** README- en notebookcode die verwees naar `AzureAIProjectAgentProvider` zijn gestandaardiseerd naar het canonieke patroon gebruikt in Les 01 en de eigen voorbeelden van het framework: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` met `provider.as_agent(...)`. Bijgewerkt in de READMEs en notebooks van Les 02–14 (bijv. Les 13 geheugen, alle notebooks van Les 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Productnaamgeving.** Doorheen de Engelse inhoud hernoemd:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Ongewijzigd: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" en omgevingsvariabelen.)
- **Afhankelijkheden** ([requirements.txt](../../requirements.txt)):
  - Gegroepeerd `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Gegroepeerd `openai>=1.108.1` (minimum voor de Responses API).
  - Verwijderd `azure-ai-inference` (werd alleen gebruikt door de gemigreerde GitHub Models voorbeelden).
- **Omgevingsconfiguratie** ([.env.example](../../.env.example)): verwijderd de GitHub Models variabelen (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); toegevoegd `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` en optioneel `AZURE_OPENAI_API_KEY`; naamgeving aangepast naar Microsoft Foundry.
- **Documentatie** — Bijgewerkt [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) en [STUDY_GUIDE.md](./STUDY_GUIDE.md) voor het bovenstaande (env variabelen setup, verificatiesnippet, provider-advies, naamgeving).

### Verwijderd

- GitHub Models onboarding-stappen en omgevingsvariabelen uit de setup-docs (vervangen door Azure OpenAI / Microsoft Foundry).

### Beveiliging / Privacy (opschoning openbare delen)

- Jupyter notebook uitvoer verwijderd die een echte **Azure-abonnements-ID**, resourcegroep-/resource-namen, en Bing verbinding-ID lekte, plus ontwikkelaars **lokale bestandslocaties en gebruikersnamen**, in:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Gecontroleerd dat er geen API-sleutels, tokens, abonnements-IDs of persoonlijke paden meer aanwezig zijn in de getrackte Engelse inhoud (de `GITHUB_TOKEN` verwijzingen die blijven zijn de GitHub Actions-token in workflows en de GitHub MCP server PAT in Les 11 setup — beide legitiem en niet gerelateerd aan GitHub Models).

### Notities en bekende beperkingen

- **Niet uitgevoerd/gecompileerd.** Dit zijn educatieve voorbeelden bijgewerkt voor API/naamcorrectheid; ze zijn niet gedraaid op live Azure-resources, en de .NET-voorbeelden zijn niet gecompileerd in deze omgeving. Valideer tegen je eigen Microsoft Foundry / Azure OpenAI implementatie.
- **Model-implementatie moet de Responses API ondersteunen.** Gebruik een implementatie zoals `gpt-4.1-mini`, `gpt-4.1` of een `gpt-5.x` model. Oudere modellen ondersteunen kernfunctionaliteit van Responses, maar niet elke feature.
- **Agent-framework versie.** De voorbeelden mikken op de laatste MAF (`>=1.10.0`). De canonieke aanroep voor agent-creatie is `client.as_agent(...)`; API’s zijn gevalideerd tegen de documentatie van het framework en een geïnstalleerde build. Bij gebruik van een andere versie, controleer de beschikbaarheid van methoden (`as_agent` vs `create_agent`).
- **Les 08 workflow notebook 04** behoudt bewust `AzureAIAgentClient` (van `agent-framework-azure-ai`) omdat het Microsoft Foundry Agent Service gehoste tools gebruikt (Bing grounding, code-interpreter); het is al op Responses gebaseerd.
- **.NET standaardimplementatie.** Twee Les 08 dotNET workflow-voorbeelden hadden voorheen een hardcoded specifiek model; ze gebruiken nu standaard `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Als een voorbeeld multimodaal/visuele input vereist, stel `AZURE_OPENAI_DEPLOYMENT` in op een geschikt model.
- **Foundry Local** biedt een OpenAI-compatibele **Chat Completions**-endpoint en is bedoeld voor lokale ontwikkeling; gebruik Azure OpenAI / Microsoft Foundry voor het volledige Responses API feature-set.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->