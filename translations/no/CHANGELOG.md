# Endringslogg

Alle bemerkelsesverdige endringer i **AI Agents for Beginners**-kurset dokumenteres i denne filen.

## [Utgitt ikke ennå] — 2026-07-06

Denne utgivelsen migrerer kurset til **Azure OpenAI Responses API**, standardiserer produktnavn på **Microsoft Foundry** og **Microsoft Agent Framework (MAF)**, pensjonerer GitHub Models, oppdaterer SDK-versjoner, og legger til nytt innhold om lokale modeller og hosting av andre rammeverk på Foundry.

### Lagt til

- **Migreringsferdighet** — Installert [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Ferdighet (fra [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) under `.agents/skills/`, inkludert dets referanser og skanner-skript.
- **Foundry Local (kjør modeller lokalt på enheten)** — Nytt avsnitt "Alternative Provider: Foundry Local" i [00-course-setup/README.md](./00-course-setup/README.md) som dekker installasjon (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, og kobling av `FoundryLocalManager` til Microsoft Agent Framework via `OpenAIChatClient`.
- **Hosting av LangChain / LangGraph-agenter på Microsoft Foundry** — Nytt avsnitt i [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) pluss et kjørbart eksempel [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) som bruker `langchain-azure-ai[hosting]` og `ResponsesHostServer` (protokoll `/responses`), basert på [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nytt avsnitt "Real-World Example: Microsoft Project Opal" i [15-browser-use/README.md](./15-browser-use/README.md) som framstiller Opal som en enterprise-databrukeragent og kartlegger den til kurskonsepter (menneske-i-løkken, tillit/sikkerhet, planlegging, ferdigheter).
- **Andre leksjon 02 Python-eksempel** — Lagt til [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (se "Endret" — migrert fra det tidligere Semantic Kernel-notatboken) og lenket til i leksjonens README.
- Seksjonen **Modeller og tilbydere** lagt til i [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Endret

- **Chat Completions → Responses API (Python).** Eksempler som kalte modellen direkte ble migrert fra Chat Completions til Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), ved bruk av `OpenAI`-klienten mot den stabile Azure OpenAI `/openai/v1/` endepunktet (uten `api_version`). Berørte eksempler inkluderer:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — hele funksjonskall-gjennomgangen (verktøyskjema flattened til Responses-format, verktøyresultater returnert som `function_call_output`, `max_output_tokens`, osv.).
- **GitHub Models → Azure OpenAI.** GitHub Models er avviklet (pensjoneres **juli 2026**) og støtter ikke Responses API. Alle GitHub Models-kodeveier ble konvertert til Azure OpenAI / Microsoft Foundry i Python- og .NET-eksempler:
  - Python: Leksjon 08 arbeidsflytnotatbøker (`01`–`03`), Leksjon 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + ledsagende `.md`-dokumenter, og Leksjon 08 dotNET arbeidsflytnotatbøker/`.md` (`01`–`03`) bruker nå `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` med `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Den tidligere `02-semantic-kernel.ipynb` ble omskrevet til å bruke Microsoft Agent Framework med Azure OpenAI (Responses API) og omdøpt til `02-python-agent-framework-azure-openai.ipynb`.
- **Standardisert på `FoundryChatClient` + `as_agent`.** README og notatbokkode som refererte til `AzureAIProjectAgentProvider` ble standardisert til det kanoniske mønsteret brukt av Leksjon 01 og rammeverkets egne eksempler: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` med `provider.as_agent(...)`. Oppdatert i Leksjon 02–14 sine README-filer og notatbøker (f.eks. Leksjon 13 memory, alle Leksjon 14 notatbøker, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Produktnavngivning.** Omdøpt gjennom hele det engelske innholdet:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Uendret: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", og miljøvariabelnavn.)
- **Avhengigheter** ([requirements.txt](../../requirements.txt)):
  - Festet `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Festet `openai>=1.108.1` (minimum for Responses API).
  - Fjernet `azure-ai-inference` (ble kun brukt av migrerte GitHub Models-eksempler).
- **Miljøkonfigurasjon** ([.env.example](../../.env.example)): fjernet GitHub Models-variabler (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); lagt til `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, og valgfri `AZURE_OPENAI_API_KEY`; oppdatert navngiving til Microsoft Foundry.
- **Dokumenter** — Oppdatert [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), og [STUDY_GUIDE.md](./STUDY_GUIDE.md) for det ovennevnte (konfigurasjon av miljøvariabler, verifiseringssnutt, tilbyderveiledning, navngiving).

### Fjernet

- GitHub Models onboarding-trinn og miljøvariabler fjernet fra oppsettdokumentasjonen (erstattet av Azure OpenAI / Microsoft Foundry).

### Sikkerhet / Personvern (opprydding ved offentlig deling)

- Tømte Jupyter-notatbok-utførselsutdata som lekket en ekte **Azure-abonnements-ID**, ressursgruppe / ressursnavn, og Bing-tilkoblings-ID, pluss utvikleres **lokale filstier og brukernavn**, i:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Verifiserte at ingen API-nøkler, tokens, abonnements-IDer, eller personlige stier forblir i det sporede engelske innholdet (de gjenværende `GITHUB_TOKEN`-referansene er GitHub Actions-token i arbeidsflyter og GitHub MCP server PAT i Leksjon 11-oppsett — begge legitime og ikke relatert til GitHub Models).

### Notater og kjente begrensninger

- **Ikke utført/kompilert.** Dette er utdannings-eksempler oppdatert for API-/navnekorrekthet; de ble ikke kjørt mot live Azure-ressurser, og .NET-eksemplene ble ikke kompilert i dette miljøet. Valider mot din egen Microsoft Foundry / Azure OpenAI-distribusjon.
- **Modell-distribusjon må støtte Responses API.** Bruk en distribusjon som `gpt-4o-mini`, `gpt-4.1`, eller en `gpt-5.x` modell. Eldre modeller støtter kjernefunksjonalitet i Responses men ikke alle funksjoner.
- **Agent-framework-versjon.** Eksemplene retter seg mot siste MAF (`>=1.10.0`). Den kanoniske agent-oppkallingen er `client.as_agent(...)`; API-ene er validert mot rammeverkets publiserte dokumentasjon og en installert bygg. Hvis du fester en annen versjon, bekreft metode-tilgjengelighet (`as_agent` vs `create_agent`).
- **Leksjon 08 arbeidsflytnotatbok 04** beholder med vilje `AzureAIAgentClient` (fra `agent-framework-azure-ai`) fordi den bruker Microsoft Foundry Agent Service hostede verktøy (Bing grounding, kodeinterpreter); den er allerede Response-basert.
- **.NET standard distribusjon.** To Leksjon 08 dotNET arbeidsflyt-eksempler hadde tidligere hardkodet `gpt-4o`; de bruker nå `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`) som standard. Hvis et eksempel er avhengig av multimodal/visions-input, sett `AZURE_OPENAI_DEPLOYMENT` til en passende modell.
- **Foundry Local** eksponerer en OpenAI-kompatibel **Chat Completions**-endepunkt og er ment for lokal utvikling; bruk Azure OpenAI / Microsoft Foundry for hele Responses API-funksjonaliteten.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->