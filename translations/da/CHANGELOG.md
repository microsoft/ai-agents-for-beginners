# Ændringslog

Alle bemærkelsesværdige ændringer til **AI Agents for Beginners**-kurset er dokumenteret i denne fil.

## [Ikke udgivet] — 2026-07-06

Denne udgivelse migrerer kurset til **Azure OpenAI Responses API**, standardiserer produktnavne til **Microsoft Foundry** og **Microsoft Agent Framework (MAF)**, udfaser GitHub Models, opdaterer SDK-versioner og tilføjer nyt indhold om lokale modeller og hosting af andre framework på Foundry.

### Tilføjet

- **Migreringsfærdighed** — Installerede [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (fra [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) under `.agents/skills/`, inklusive dets referencer og scanner-script.
- **Foundry Local (kør modeller lokalt)** — Ny "Alternativ leverandør: Foundry Local" sektion i [00-course-setup/README.md](./00-course-setup/README.md), der dækker installation (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` samt kobling af `FoundryLocalManager` til Microsoft Agent Framework via `OpenAIChatClient`.
- **Hosting af LangChain / LangGraph agenter på Microsoft Foundry** — Ny sektion i [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) samt et kørbart eksempel [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) vha. `langchain-azure-ai[hosting]` og `ResponsesHostServer` (protokollen `/responses`), baseret på [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Ny "Virkelighedsnært eksempel: Microsoft Project Opal" sektion i [15-browser-use/README.md](./15-browser-use/README.md), der præsenterer Opal som en virksomhedskomputerbrugsagent og kobler den til kursuskoncepter (mennesket-i-loopet, tillid/sikkerhed, planlægning, færdigheder).
- **Andet Python-eksempel til Lektion 02** — Tilføjede [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (se "Ændret" — migreret fra det tidligere Semantic Kernel-notebook) og linkede det i lektions-README'en.
- Tilføjet afsnit **Modeller og leverandører** til [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Ændret

- **Chat Completions → Responses API (Python).** Eksempler, der kaldte modellen direkte, blev migreret fra Chat Completions til Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), ved brug af `OpenAI`-klienten imod den stabile Azure OpenAI `/openai/v1/` endpoint (uden `api_version`). Berørte eksempler inkluderer:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — den fulde funktion-kald walkthrough (tool schema fladet til Responses-format, tool resultater returneret som `function_call_output`, `max_output_tokens`, osv.).
- **GitHub Models → Azure OpenAI.** GitHub Models er udfaset (udgår i **juli 2026**) og understøtter ikke Responses API. Alle GitHub Models-kodeveje blev konverteret til Azure OpenAI / Microsoft Foundry på tværs af Python- og .NET-eksempler:
  - Python: Lektions 08 workflow-notebooks (`01`–`03`), lektion 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + ledsagende `.md` dokumenter, og Lektions 08 dotNET workflow notebooks/`.md` (`01`–`03`) bruger nu `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` med `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Den tidligere `02-semantic-kernel.ipynb` blev omskrevet til at bruge Microsoft Agent Framework med Azure OpenAI (Responses API) og omdøbt til `02-python-agent-framework-azure-openai.ipynb`.
- **Standardiseret på `FoundryChatClient` + `as_agent`.** README og notebook-kode, der refererede til `AzureAIProjectAgentProvider`, blev standardiseret på det kanoniske mønster brugt i Lektion 01 og frameworkets egne eksempler: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` med `provider.as_agent(...)`. Opdateret i Lektion 02–14 README'er og notebooks (fx Lektion 13 hukommelse, alle Lektion 14 notebooks, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Produktnavngivning.** Omdøbt i hele det engelske indhold:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Uændret: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" og miljøvariabelnavne.)
- **Afhængigheder** ([requirements.txt](../../requirements.txt)):
  - Fastlåst `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Fastlåst `openai>=1.108.1` (minimum for Responses API).
  - Fjernet `azure-ai-inference` (blev kun brugt af de migrerede GitHub Models-eksempler).
- **Miljøkonfiguration** ([.env.example](../../.env.example)): fjernet GitHub Models variabler (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); tilføjet `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` og valgfri `AZURE_OPENAI_API_KEY`; opdateret navngivning til Microsoft Foundry.
- **Dokumenter** — Opdaterede [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) og [STUDY_GUIDE.md](./STUDY_GUIDE.md) for ovenstående (opsætning af miljøvariabler, verifikationssnippets, leverandørvejledning, navngivning).

### Fjernet

- GitHub Models onboarding trin og miljøvariabler fra opsætningsdokumenterne (erstattet af Azure OpenAI / Microsoft Foundry).

### Sikkerhed / Privatliv (oprydning af offentligt delte data)

- Rydde Jupyter notebook-udførselsoutput, der lækkede et rigtigt **Azure abonnement-ID**, resourcegruppe / resourcenavne, og Bing-forbindelses ID, plus udviklerens **lokale filstier og brugernavne**, i:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Bekræftet at ingen API-nøgler, tokens, abonnement-ID'er eller personlige stier findes længere i det sporede engelske indhold (de `GITHUB_TOKEN` referencer, som stadig er, er GitHub Actions token i workflows og GitHub MCP server PAT i Lektion 11 opsætningen — begge legitime og uden relation til GitHub Models).

### Noter og kendte begrænsninger

- **Ikke udført/kompileret.** Disse er undervisningseksempler opdateret for korrekt API/ navngivning; de blev ikke kørt mod live Azure-ressourcer, og .NET-eksemplerne blev ikke kompillet i dette miljø. Valider mod dit eget Microsoft Foundry / Azure OpenAI deployment.
- **Modeldeployment skal understøtte Responses API.** Brug et deployment som `gpt-4o-mini`, `gpt-4.1` eller en `gpt-5.x` model. Ældre modeller understøtter kernefunktionalitet i Responses, men ikke alle funktioner.
- **Agent-framework version.** Eksemplerne sigter mod den nyeste MAF (`>=1.10.0`). Det kanoniske agent-creation kald er `client.as_agent(...)`; API'er er valideret mod frameworkets publicerede dokumentation og en installeret build. Hvis du fastlåser en anden version, bekræft metode-tilgængelighed (`as_agent` vs `create_agent`).
- **Lektion 08 workflow notebook 04** beholder bevidst `AzureAIAgentClient` (fra `agent-framework-azure-ai`), fordi den bruger værktøjer hostet af Microsoft Foundry Agent Service (Bing grounding, kodefortolker); den er allerede baseret på Responses.
- **.NET standard deployment.** To Lektion 08 dotNET workflow eksempler havde tidligere hardkodet `gpt-4o`; de bruger nu som standard `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Hvis et eksempel er afhængigt af multimodal/vision input, sæt `AZURE_OPENAI_DEPLOYMENT` til en passende model.
- **Foundry Local** eksponerer en OpenAI-kompatibel **Chat Completions** endpoint og er tænkt til lokal udvikling; brug Azure OpenAI / Microsoft Foundry for det fulde Responses API funktionssæt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->