# Endringslogg

Alle merkbare endringer i kurset **AI Agents for Beginners** er dokumentert i denne filen.

## [Utgitt] — 2026-07-14

Denne utgivelsen flytter kurset bort fra to nylig avviklede modeller, migrerer gjenværende Leksjons-notatbøker til den stabile Microsoft Agent Framework API, og validerer Python-notatbøkene mot en aktiv Microsoft Foundry-distribusjon.

### Endret

- **Flyttet bort fra avviklede modeller (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Både `gpt-4.1` og `gpt-4.1-mini` er nå avviklet (publisert pensjonsdato **14. oktober 2026**). Erstattet hver kursreferanse (dokumentasjon, `.env.example`, Python/.NET-notatbøker og eksempler) med den ikke-avviklede `gpt-5-mini`. Lekjon 16s modell-rutings-eksempel beholder en liten/stor kontrast med `gpt-5-nano` (liten) og `gpt-5-mini` (stor). Inkluderte tredjepartsfiler ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), historisk GitHub Models-tekst, og `azure-openai-to-responses` ferdighets notater ble med vilje ikke endret.
- **Leksjon 14 overlevering-notatbok migrert til stabil API.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) bruker nå `agent_framework.orchestrations.HandoffBuilder` med `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type` basert streaming, og `FoundryChatClient` (erstatter de fjernede pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` symbolene).
- **Leksjon 14 mennesket-i-sløyfen-notatbok migrert til stabil API.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) pauser nå via `ctx.request_info(...)` + `@response_handler` (erstatter de fjernede `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), bygger med `WorkflowBuilder(start_executor=..., output_executors=[...])`, styrer strukturert utdata gjennom `default_options={"response_format": ...}`, og bruker et manusforfattet svar slik at notatboken kjører uten tilsyn (ingen blokkering med `input()`).
- **Miljøkonfigurasjon** ([.env.example](../../.env.example)): byttet modell-distribusjonsnavn til `gpt-5-mini`; lagt til `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (Lekjon 16 ruting) og det tidligere manglende `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (Lekjon 15 nettleserbruk).
- **Avhengigheter** ([requirements.txt](../../requirements.txt)): festet `agent-framework`, `agent-framework-foundry`, og `agent-framework-openai` til `~=1.10.0` for en selv-konsistent, validert sett (1.11.0 inneholder eksperimentelle brytende endringer for de overflatene disse leksjonene bruker).

### Notater og kjente begrensninger

- **Validert mot live Microsoft Foundry.** Python-notatbøker ble kjørt hodløst med `nbconvert` mot et Microsoft Foundry-prosjekt som bruker `gpt-5-mini` (og `gpt-5-nano` for Lekjon 16 ruting). Distribuer tilsvarende ikke-avviklede modeller i ditt eget prosjekt; notatbøkene leser distribusjonsnavnet fra `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Krever fortsatt ekstra ressurser for noen leksjoner.** Lekjon 05 trenger Azure AI Search; Lekjon 08 Bing-tilknytningsarbeidsflyt (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) trenger en Bing-tilkobling og Microsoft Foundry Agent Service hostede verktøy; Lekjon 13 (Cognee) og Lekjon 17 (Foundry Local) trenger egne kjøringsmiljøer.

## [Utgitt] — 2026-07-13

Denne utgivelsen legger til to nye leksjoner som fullfører distribusjonsbuen – skalering av agenter opp til Microsoft Foundry og ned til en enkelt arbeidsstasjon – pluss en røyktest-pipeline, oppdatert kurssnavigasjon, nye ferdigheter for lærende, og oppdatert merkevarebygging.

### Lagt til

- **Leksjon 16 — Distribuering av skalerbare agenter med Microsoft Foundry.** Ny leksjon [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) og kjørbar notatbok [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) som bygger en produksjons kunde-support agent (verktøy, RAG, minne, modell-ruting, respons-caching, menneskelig godkjenning, en evalueringsport og OpenTelemetry-sporing), med utviklings-/distribusjons-/kjørings Mermaids-diagrammer, en kunnskapssjekk, en oppgave, og en utfordring.
- **Leksjon 17 — Lage lokale AI-agenter med Foundry Local og Qwen.** Ny leksjon [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) og notatbok [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) som bygger en fullstendig lokalt enhets-basert ingeniørassistent (Qwen funksjonskall via Foundry Local, sandkasse-filverktøy, lokal RAG med Chroma, valgfrie lokale MCP), med diagrammer for kun lokalt / lokal RAG / verktøykall, en kunnskapssjekk, en oppgave, og en utfordring.
- **Røyktest-pipeline.** Ny [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) arbeidsflyt [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) pluss kataloger per leksjon under [tests/](./tests/README.md) for distribuerbare agenter i Leksjon 01, 04, 05, og 16, med en indeks README som kobler hver katalog til sin leksjon og hostet agent-navn. Lekjon 16 får en seksjon "Validering av distribuert agent med røyktester"; Lekser 01/04/05 får en valgfri røyktest-peker.
- **Ferdigheter for lærende.** Nye Agent Ferdigheter under `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (pakker veiledningene for Lekjon 16 og 17), og [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (hvordan validere notatbok-eksemplene mot et aktivt Microsoft Foundry / Azure OpenAI-oppsett).
- **Notatbok-valideringskjører.** Ny [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) som kjører hver Python-notatbok hodløst med `nbconvert` og skriver ut en PASS/FAIL matrise (pluss `results.json`). Den oppdager automatisk repo-rot og Python, utelukker standard ikke-kurs notatbøker (`.venv`, `site-packages`, `translations`, ferdighetsmal-ressurser) og `.NET` notatbøker, og støtter `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, og `-Python`.
- **Kurssnavigasjon.** La til Forrige/Neste leksjon-lenker til Lekser 11–15 (tidligere manglet) slik at hele kurset kjedes 00 → 18 i begge retninger.
- **Nye miniatyrbilder.** Leksyminiatyrbilder for Lekser 16 og 17, pluss et oppdatert depot sosiale bilde [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (nå annonserer de to nye leksjonene og `aka.ms/ai-agents-beginners` URL).
- **Avhengigheter** ([requirements.txt](../../requirements.txt)): la til `foundry-local-sdk` og `chromadb` for Lekjon 17.

### Endret

- **Hoved [README.md](./README.md)** leksjonstabell: Lekser 16 og 17 lenker nå til sitt innhold (tidligere "Kommer snart"); depotbilde oppdatert til `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: lagt til Lekser 16 og 17 i leksjon-for-leksjon guide og læringsstier, og en seksjon "Validering av distribuerte agenter med røyktester".
- **[AGENTS.md](./AGENTS.md)**: oppdatert antall beskrivelse (00–18), lagt til seksjon for røyktest-validering, og lagt til eksempler på filnavn for Lekser 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Forrige leksjon" peker nå til Lekjon 17 (var Lekjon 15), lukker kjeden.
- **Standardiserte modellreferanser til ikke-avviklede modeller.** Erstattet alle `gpt-4o` / `gpt-4o-mini` referanser over hele kurset (dokumentasjon, `.env.example`, Python/.NET-notatbøker og eksempler) med `gpt-4.1-mini` —`gpt-4o` (alle versjoner) pensjoneres i 2026. Lekjon 16s modell-rutings-eksempel beholder en liten/stor kontrast med `gpt-4.1-mini` (liten) og `gpt-4.1` (stor). Python-notatbøker velger nå modell fra miljøvariabler (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) i stedet for å hardkode et modellnavn.

### Notater og kjente begrensninger

- **Ikke kjørt mot live Azure.** De nye leksjonenes notatbøker er pedagogiske eksempler; kjør og valider dem mot ditt eget Microsoft Foundry / Foundry Local-oppsett. Røyktest-arbeidsflyten krever at du distribuerer leksjonens agent og konfigurerer Azure OIDC-hemmeligheter (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) med **Azure AI User** rolle på Foundry prosjektomfang.
- **Leksjon 17 er kun lokal.** Den har ikke Foundry Svar-endepunkt, så røyktest-aksjonen gjelder ikke; valider den ved å kjøre notatboken på din arbeidsstasjon.

## [Utgitt] — 2026-07-06

Denne utgivelsen migrerer kurset til **Azure OpenAI Responses API**, standardiserer produktnavn på **Microsoft Foundry** og **Microsoft Agent Framework (MAF)**, pensjonerer GitHub Models, oppdaterer SDK-versjoner, og legger til nytt innhold om lokale modeller og hosting av andre rammeverk på Foundry.

### Lagt til

- **Migrasjonsferdighet** — Installert [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Ferdighet (fra [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) under `.agents/skills/`, inkludert henvisninger og skanneskript.
- **Foundry Local (kjør modeller på enhet)** — Ny seksjon "Alternativ Leverandør: Foundry Local" i [00-course-setup/README.md](./00-course-setup/README.md) som dekker installasjon (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, og kobling av `FoundryLocalManager` til Microsoft Agent Framework via `OpenAIChatClient`.
- **Hosting LangChain / LangGraph agenter på Microsoft Foundry** — Ny seksjon i [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) pluss et kjørbart eksempel [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) som bruker `langchain-azure-ai[hosting]` og `ResponsesHostServer` (protokoll `/responses`), basert på [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Ny seksjon "Virkelighetseksempel: Microsoft Project Opal" i [15-browser-use/README.md](./15-browser-use/README.md) som rammer Opal som en bedriftsbrukeragent og kartlegger den til kurskonsepter (mennesket-i-sløyfen, tillit/sikkerhet, planlegging, Ferdigheter).
- **Andre Lekjon 02 Python-eksempel** — La til [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (se "Endret" — migrert fra den tidligere Semantic Kernel-notatboken) og lenket den i leksjons-README.
- **Seksjonen Modeller og Leverandører lagt til i [STUDY_GUIDE.md](./STUDY_GUIDE.md).**

### Endret

- **Chat Completions → Responses API (Python).** Eksempler som kalte modellen direkte ble migrert fra Chat Completions til Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), ved bruk av `OpenAI` klient mot den stabile Azure OpenAI `/openai/v1/` endepunktet (uten `api_version`). Berørte eksempler inkluderer:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — full gjennomgang av funksjonskalling (verktøyskjema omgjort til Responses-format, verktøyresultater returnert som `function_call_output`, `max_output_tokens`, osv.).

- **GitHub-modeller → Azure OpenAI.** GitHub Models er avviklet (opphører **juli 2026**) og støtter ikke Responses API. Alle GitHub Models-kodebaner ble konvertert til Azure OpenAI / Microsoft Foundry på tvers av Python- og .NET-eksempler:
  - Python: Lesson 08 workflow-notatbøker (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + tilhørende `.md`-dokumentasjon, og Lesson 08 dotNET workflow-notatbøker/`.md` (`01`–`03`) bruker nå `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` med `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Den tidligere `02-semantic-kernel.ipynb` ble omskrevet til å bruke Microsoft Agent Framework med Azure OpenAI (Responses API) og gitt nytt navn til `02-python-agent-framework-azure-openai.ipynb`.
- **Standardisert på `FoundryChatClient` + `as_agent`.** README og notatbok-kode som refererte til `AzureAIProjectAgentProvider` ble standardisert på det kanoniske mønsteret brukt av Lesson 01 og rammeverkets egne eksempler: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` med `provider.as_agent(...)`. Oppdatert på tvers av Lesson 02–14 README-filer og notatbøker (f.eks. Lesson 13 memory, alle Lesson 14-notatbøker, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Produktnavngivning.** Omdøpt gjennom hele det engelske innholdet:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Uendret: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", og miljøvariabelnavn.)
- **Avhengigheter** ([requirements.txt](../../requirements.txt)):
  - Festet `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Festet `openai>=1.108.1` (minimum for Responses API).
  - Fjernet `azure-ai-inference` (ble kun brukt av migrerte GitHub Models-eksempler).
- **Miljøkonfigurasjon** ([.env.example](../../.env.example)): fjernet GitHub Models-variablene (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); lagt til `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, og valgfri `AZURE_OPENAI_API_KEY`; oppdatert navngivning til Microsoft Foundry.
- **Dokumentasjon** — Oppdatert [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) og [STUDY_GUIDE.md](./STUDY_GUIDE.md) for ovennevnte (sette opp miljøvariabler, verifiseringssnutt, leverandørveiledning, navngivning).

### Fjernet

- GitHub Models onboarding-trinn og miljøvariabler fra oppsettdokumentene (erstattet av Azure OpenAI / Microsoft Foundry).

### Sikkerhet / Personvern (offentlig deling opprydning)

- Ryddet Jupyter notatbokkjøringsutdata som lekket et ekte **Azure-abonnements-ID**, ressursgruppe/ressursnavn og Bing-tilkoblings-ID, pluss utviklerens **lokale filstier og brukernavn**, i:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Verifisert at ingen API-nøkler, tokens, abonnement-IDer eller personlige stier er igjen i det versjonerte engelske innholdet (referanser til `GITHUB_TOKEN` som gjenstår er GitHub Actions-token i workflows og GitHub MCP server PAT i Lesson 11-oppsettet — begge legitime og ikke relatert til GitHub Models).

### Notater og kjente begrensninger

- **Ikke kjørt/kompilert.** Disse er utdanningsprøver oppdatert for API-/navnekorrekthet; de ble ikke kjørt mot levende Azure-ressurser, og .NET-eksemplene ble ikke kompilert i dette miljøet. Valider mot din egen Microsoft Foundry / Azure OpenAI-distribusjon.
- **Modell-distribusjon må støtte Responses API.** Bruk en distribusjon som `gpt-4.1-mini`, `gpt-4.1`, eller en `gpt-5.x` modell. Eldre modeller støtter grunnleggende Responses-funksjonalitet, men ikke alle funksjoner.
- **Agent-framework versjon.** Eksemplene sikter mot siste MAF (`>=1.10.0`). Det kanoniske agent-opprettelses-kallet er `client.as_agent(...)`; API-er ble validert mot rammeverkets publiserte dokumentasjon og et installert bygg. Hvis du fester en annen versjon, bekreft metode-tilgjengelighet (`as_agent` vs `create_agent`).
- **Lesson 08 workflow-notatbok 04** beholder med vilje `AzureAIAgentClient` (fra `agent-framework-azure-ai`) fordi den bruker Microsoft Foundry Agent Service hostede verktøy (Bing forankring, kode-tolker); den er allerede Response-basert.
- **.NET standarddistribusjon.** To Lesson 08 .NET workflow-eksempler kodet tidligere inn en spesifikk modell; de bruker nå som standard `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Hvis et eksempel er avhengig av multimodal/vision input, sett `AZURE_OPENAI_DEPLOYMENT` til en passende modell.
- **Foundry Local** eksponerer en OpenAI-kompatibel **Chat Completions** endepunkt og er ment for lokal utvikling; bruk Azure OpenAI / Microsoft Foundry for full Responses API-funksjonalitet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->