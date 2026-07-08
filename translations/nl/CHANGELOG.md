# Wijzigingslogboek

Alle opmerkelijke wijzigingen aan de cursus **AI Agents for Beginners** zijn in dit bestand gedocumenteerd.

## [Niet uitgebracht] — 2026-07-06

Deze release migreert de cursus naar de **Azure OpenAI Responses API**, standaardiseert productnamen op **Microsoft Foundry** en het **Microsoft Agent Framework (MAF)**, stopt met GitHub Models, werkt SDK-versies bij en voegt nieuwe inhoud toe over lokale modellen en het hosten van andere frameworks op Foundry.

### Toegevoegd

- **Migratievaardigheid** — Geïnstalleerde [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (van [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) onder `.agents/skills/`, inclusief referenties en scanner script.
- **Foundry Local (modellen lokaal draaien)** — Nieuwe sectie "Alternatieve Provider: Foundry Local" in [00-course-setup/README.md](./00-course-setup/README.md) met installatiestappen (`winget` / `brew`), `foundry model run`, de `foundry-local-sdk`, en het koppelen van `FoundryLocalManager` aan het Microsoft Agent Framework via `OpenAIChatClient`.
- **Hosten van LangChain / LangGraph agents op Microsoft Foundry** — Nieuwe sectie in [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus een uitvoerbaar voorbeeld [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) met `langchain-azure-ai[hosting]` en `ResponsesHostServer` (het `/responses` protocol), gebaseerd op [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nieuwe sectie "Real-World Example: Microsoft Project Opal" in [15-browser-use/README.md](./15-browser-use/README.md) die Opal positioneert als een enterprise computergebruik-agent en dit koppelt aan cursusconcepten (mens-in-de-lus, vertrouwen/veiligheid, planning, vaardigheden).
- **Tweede Les 02 Python voorbeeld** — Toegevoegd [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (zie "Gewijzigd" — gemigreerd vanuit het voormalige Semantic Kernel notebook) en gelinkt in de les README.
- **Sectie Modellen en Providers** toegevoegd aan [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Gewijzigd

- **Chat Completions → Responses API (Python).** Voorbeelden die het model direct aanriepen zijn gemigreerd van Chat Completions naar de Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), met gebruik van de `OpenAI` client tegen de stabiele Azure OpenAI `/openai/v1/` endpoint (zonder `api_version`). Betroffen voorbeelden zijn onder andere:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — de volledige walkthrough voor functie-aanroepen (tool schema afgevlakt naar het Responses-formaat, tool-resultaten teruggegeven als `function_call_output`, `max_output_tokens`, etc.).
- **GitHub Models → Azure OpenAI.** GitHub Models wordt uitgefaseerd (stopzetting **juli 2026**) en ondersteunt de Responses API niet. Alle GitHub Models codepaden zijn geconverteerd naar Azure OpenAI / Microsoft Foundry in Python en .NET voorbeelden:
  - Python: Les 08 workflow notebooks (`01`–`03`), Les 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + bijbehorende `.md` documentatie, en de Les 08 dotNET workflow notebooks/`.md` (`01`–`03`) gebruiken nu `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` met `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Het voormalige `02-semantic-kernel.ipynb` is herschreven om het Microsoft Agent Framework met Azure OpenAI (Responses API) te gebruiken en hernoemd tot `02-python-agent-framework-azure-openai.ipynb`.
- **Gestandaardiseerd op `FoundryChatClient` + `as_agent`.** README en notebook code die verwezen naar `AzureAIProjectAgentProvider` zijn gestandaardiseerd volgens het canonieke patroon dat gebruikt wordt in Les 01 en de framework-eigen voorbeelden: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` met `provider.as_agent(...)`. Dit is bijgewerkt in de Les 02–14 READMEs en notebooks (bijv. Les 13 geheugen, alle Les 14 notebooks, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Productnamen.** Hernoemd door de Engelse inhoud heen:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Ongewijzigd: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", en omgevingsvariabele namen.)
- **Afhankelijkheden** ([requirements.txt](../../requirements.txt)):
  - Vastgezet op `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Vastgezet op `openai>=1.108.1` (minimaal voor de Responses API).
  - Verwijderd `azure-ai-inference` (werd alleen gebruikt door de gemigreerde GitHub Models voorbeelden).
- **Omgevingsconfiguratie** ([.env.example](../../.env.example)): de GitHub Models variabelen (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) verwijderd; toegevoegd `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` en optioneel `AZURE_OPENAI_API_KEY`; naamswijziging naar Microsoft Foundry doorgevoerd.
- **Documentatie** — Bijgewerkt [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), en [STUDY_GUIDE.md](./STUDY_GUIDE.md) voor bovenstaande (omgeving variabelen setup, verificatie snippet, provider richtlijnen, namen).

### Verwijderd

- GitHub Models onboarding stappen en omgevingsvariabelen uit de opzetdocumenten (vervangen door Azure OpenAI / Microsoft Foundry).

### Beveiliging / Privacy (opruimen publieke gedeelde inhoud)

- Jupyter notebook uitvoeroutputs verwijderd die een echte **Azure abonnement-ID**, resourcegroep / resource namen, en Bing verbinding-ID leken te lekken, plus ontwikkelaars **lokale bestands-paden en gebruikersnamen**, in:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Gecontroleerd dat er geen API-sleutels, tokens, abonnement-IDs of persoonlijke paden meer aanwezig zijn in de bijgehouden Engelse inhoud (de resterende `GITHUB_TOKEN` verwijzingen zijn de GitHub Actions token in workflows en de GitHub MCP server PAT in Les 11 setup — beide legitiem en niet gerelateerd aan GitHub Models).

### Notities en bekende beperkingen

- **Niet uitgevoerd/gecompileerd.** Dit zijn educatieve voorbeelden die zijn bijgewerkt voor API-/naamscorrectheid; ze zijn niet uitgevoerd tegen live Azure resources, en de .NET voorbeelden zijn niet gecompileerd in deze omgeving. Valideer met je eigen Microsoft Foundry / Azure OpenAI implementatie.
- **Model deployment moet de Responses API ondersteunen.** Gebruik een deployment zoals `gpt-4o-mini`, `gpt-4.1` of een `gpt-5.x` model. Oudere modellen ondersteunen de kernfunctionaliteit van Responses, maar niet alle features.
- **Agent-framework versie.** De voorbeelden zijn gericht op de nieuwste MAF (`>=1.10.0`). De canonieke agent-creatie aanroep is `client.as_agent(...)`; API's zijn gevalideerd tegen de gepubliceerde documentatie en een geïnstalleerde build. Als je een andere versie vastzet, controleer dan de beschikbaarheid van methoden (`as_agent` vs `create_agent`).
- **Les 08 workflow notebook 04** behoudt opzettelijk `AzureAIAgentClient` (van `agent-framework-azure-ai`) omdat het Microsoft Foundry Agent Service gehoste tools gebruikt (Bing grounding, code interpreter); het is al gebaseerd op Responses.
- **.NET standaard deployment.** Twee Les 08 dotNET workflow voorbeelden hadden voorheen `gpt-4o` hard-coded; ze gebruiken nu standaard `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Als een voorbeeld gebruikmaakt van multimodaal/visuele input, stel dan `AZURE_OPENAI_DEPLOYMENT` in op een geschikt model.
- **Foundry Local** biedt een OpenAI-compatibele **Chat Completions** endpoint en is bedoeld voor lokale ontwikkeling; gebruik Azure OpenAI / Microsoft Foundry voor de volledige feature set van Responses API.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->