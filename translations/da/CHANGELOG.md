# Ændringslog

Alle væsentlige ændringer til **AI-agenter for begyndere**-kurset er dokumenteret i denne fil.

## [Udgivet] — 2026-07-14

Denne udgivelse flytter kurset væk fra to nyligt udfasede modeller, migrerer de resterende lektion-notebooks til den stabile Microsoft Agent Framework API og validerer Python-notebooks mod en live Microsoft Foundry-implementering.

### Ændret

- **Flyttet væk fra udfasede modeller (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Både `gpt-4.1` og `gpt-4.1-mini` er nu udfasede (officiel udfasningsdato **14. oktober 2026**). Alle kursusreferencer (dokumentation, `.env.example`, Python/.NET-notebooks og eksempler) er erstattet med den ikke-udfasede `gpt-5-mini`. Lektion 16's model-rutnings-eksempel bevarer en lille/stor kontrast med `gpt-5-nano` (lille) og `gpt-5-mini` (stor). Indlejrede tredjepartsfiler ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), historiske GitHub Models-tekster og `azure-openai-to-responses` færdighedens kapabilitetsnotater er bevidst uændrede.
- **Lektion 14 overdragelses-notebook migreret til den stabile API.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) bruger nu `agent_framework.orchestrations.HandoffBuilder` med `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, streaming baseret på `event.type` og `FoundryChatClient` (erstatter de fjernede pre-1.0 symboler `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Lektion 14 human-in-the-loop-notebook migreret til den stabile API.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) pauser nu via `ctx.request_info(...)` + `@response_handler` (erstatter de fjernede `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), bygges med `WorkflowBuilder(start_executor=..., output_executors=[...])`, leverer struktureret output gennem `default_options={"response_format": ...}`, og bruger et scriptet svar, så notebooken kan køre ubemandet (ingen blokerende `input()`).
- **Miljøkonfiguration** ([.env.example](../../.env.example)): skiftede model-deploymentsnavne til `gpt-5-mini`; tilføjede `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (Lektion 16 rutning) og den tidligere manglende `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (Lektion 15 browserbrug).
- **Afhængigheder** ([requirements.txt](../../requirements.txt)): fastlåste `agent-framework`, `agent-framework-foundry` og `agent-framework-openai` til `~=1.10.0` for et selvkonsistent, valideret sæt (1.11.0 bringer eksperimentelle brydende ændringer på de overflader, disse lektioner bruger).

### Noter og kendte begrænsninger

- **Valideret mod live Microsoft Foundry.** Python-notebookene blev udført headless med `nbconvert` mod et Microsoft Foundry-projekt ved brug af `gpt-5-mini` (og `gpt-5-nano` til Lektion 16 rutning). Udrul tilsvarende ikke-udfasede modeller i dit eget projekt; notebooks læser deploymentsnavnet fra `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Kræver stadig ekstra ressourcer for nogle lektioner.** Lektion 05 har brug for Azure AI Search; Lektion 08 Bing-grounding workflow (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) kræver en Bing-forbindelse og Microsoft Foundry Agent Service hostede værktøjer; Lektion 13 (Cognee) og Lektion 17 (Foundry Local) kræver deres egne runtime-miljøer.

## [Udgivet] — 2026-07-13

Denne udgivelse tilføjer to nye lektioner, der fuldender implementeringsforløbet — opskalering af agenter til Microsoft Foundry og nedskalering til en enkelt arbejdsstation — plus en smoke-test pipeline, opdateret kursusnavigation, nye elevfærdigheder og frisk branding.

### Tilføjet

- **Lektion 16 — Implementering af skalerbare agenter med Microsoft Foundry.** Ny lektion [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) og eksekverbar notebook [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb), der bygger en produktionskundesupport-agent (værktøjer, RAG, hukommelse, model-rutning, respons-caching, menneskelig godkendelse, evalueringsport og OpenTelemetry-tracing), med udviklings-/implementerings-/runtime Mermaid-diagrammer, en videnscheck, en opgave og en udfordring.
- **Lektion 17 — Oprettelse af lokale AI-agenter med Foundry Local og Qwen.** Ny lektion [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) og notebook [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb), der bygger en fuldt on-device engineering assistent (Qwen funktionsopkald via Foundry Local, sandboxede filværktøjer, lokal RAG med Chroma, valgfri lokal MCP), med diagrammer for lokale-only / lokal-RAG / værktøjsopkald, en videnscheck, en opgave og en udfordring.
- **Smoke-test pipeline.** Ny [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) workflow [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) plus per-lektion kataloger under [tests/](./tests/README.md) for deployable agenter i Lektion 01, 04, 05 og 16, med et indeks-README, der kortlægger hvert katalog til dets lektion og hostede agent-navn. Lektion 16 får en sektion "Validering af udrullet agent med smoke tests"; Lektionerne 01/04/05 får en valgbar smoke-test henvisning.
- **Elevfærdigheder.** Nye Agent Skills under `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (pakker lektion 16 og 17 vejledning), og [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (hvordan man validerer notebook-eksempler mod en live Microsoft Foundry / Azure OpenAI opsætning).
- **Notebook valideringskører.** Ny [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), der eksekverer alle Python-notebooks headless med `nbconvert` og printer en PASS/FAIL-matrix (plus `results.json`). Den opdager automatisk repo-roden og Python, udelukker ikke-kursus notebooks (`.venv`, `site-packages`, `translations`, skill template assets) og `.NET` notebooks som standard, og understøtter `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` og `-Python`.
- **Kursusnavigation.** Tilføjet Forrige/Næste lektion links til Lektionerne 11–15 (tidligere manglende), så hele kurset kæder 00 → 18 i begge retninger.
- **Nye thumbnails.** Lektionsthumbnails for Lektion 16 og 17, plus et opdateret repository socialt billede [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (nu med de to nye lektioner og `aka.ms/ai-agents-beginners` URL).
- **Afhængigheder** ([requirements.txt](../../requirements.txt)): tilføjet `foundry-local-sdk` og `chromadb` til Lektion 17.

### Ændret

- **Hoved [README.md](./README.md)** lektionstabel: Lektion 16 og 17 linker nu til deres indhold (tidligere "Kommer snart"); repository billedet opdateret til `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: tilføjet Lektion 16 og 17 til lektion-for-lektion guiden og læringsstier, samt en sektion "Validering af udrullede agenter med smoke tests".
- **[AGENTS.md](./AGENTS.md)**: opdateret lektionstælling/beskrivelse (00–18), tilføjet en smoke-test valideringssektion, og tilføjet navngivningseksempler for Lektion 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Forrige Lektion" peger nu til Lektion 17 (var Lektion 15), og lukker kæden.
- **Standardiserede modelreferencer på ikke-udfasede modeller.** Alle `gpt-4o` / `gpt-4o-mini` referencer på tværs af kurset (dokumenter, `.env.example`, Python/.NET notebooks og eksempler) er udskiftet med `gpt-4.1-mini` — `gpt-4o` (alle versioner) udfases i 2026. Lektion 16's model-rutnings-eksempel bevarer en lille/stor kontrast med `gpt-4.1-mini` (lille) og `gpt-4.1` (stor). Python-notebooks vælger nu model fra miljøvariabler (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) i stedet for at hardkode modellens navn.

### Noter og kendte begrænsninger

- **Ikke udført mod live Azure.** De nye lektioners notebooks er uddannelsesmæssige eksempler; kør og valider dem mod dit eget Microsoft Foundry / Foundry Local setup. Smoke-test workflowen kræver, at du deployer lektionens agent og konfigurerer Azure OIDC secrets (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) med **Azure AI User** rollen på Foundry projekt-scopeniveau.
- **Lektion 17 er kun lokal.** Den har ingen Foundry Responses-endpoint, så smoke-test action gælder ikke; valider den ved at køre notebooken på din arbejdsstation.

## [Udgivet] — 2026-07-06

Denne udgivelse migrerer kurset til **Azure OpenAI Responses API**, standardiserer produktnavne på **Microsoft Foundry** og **Microsoft Agent Framework (MAF)**, udfaser GitHub Models, opdaterer SDK-versioner og tilføjer nyt indhold om lokale modeller og hosting af andre frameworks på Foundry.

### Tilføjet

- **Migreringsfærdighed** — Installerede [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent-færdighed (fra [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) under `.agents/skills/`, inklusive dets referencer og scanningsscript.
- **Foundry Local (kør modeller on-device)** — Ny "Alternativ udbyder: Foundry Local" sektion i [00-course-setup/README.md](./00-course-setup/README.md) der dækker installation (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` og forbindelsen `FoundryLocalManager` til Microsoft Agent Framework via `OpenAIChatClient`.
- **Hosting af LangChain / LangGraph agenter på Microsoft Foundry** — Ny sektion i [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus eksekverbart eksempel [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) der bruger `langchain-azure-ai[hosting]` og `ResponsesHostServer` (protokol `/responses`), baseret på [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Ny sektion "Virkelighedsnær eksempel: Microsoft Project Opal" i [15-browser-use/README.md](./15-browser-use/README.md), der rammesætter Opal som en enterprise computer-bruger agent og kobler den til kursusbegreber (human-in-the-loop, tillid/sikkerhed, planlægning, Skills).
- **Andet Python-eksempel til Lektion 02** — Tilføjet [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (se "Ændret" — migreret fra den tidligere Semantic Kernel notebook) og linket den i lektionens README.
- **Modeller og udbydere** sektion tilføjet til [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Ændret

- **Chat Completions → Responses API (Python).** Eksempler, der kaldte modellen direkte, er migreret fra Chat Completions til Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), ved brug af `OpenAI` klienten mod den stabile Azure OpenAI `/openai/v1/` endpoint (ingen `api_version`). Berørte eksempler inkluderer:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — den komplette gennemgang af funktionsopkald (værktøjsskema fladet ud til Responses-formatet, værktøjsresultater returneret som `function_call_output`, `max_output_tokens`, osv.).

- **GitHub Models → Azure OpenAI.** GitHub Models er udfaset (udgår **juli 2026**) og understøtter ikke Responses API. Alle GitHub Models kodeveje blev konverteret til Azure OpenAI / Microsoft Foundry på tværs af Python og .NET eksempler:
  - Python: Lesson 08 workflow notebooks (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + ledsagende `.md` dokumenter, og Lesson 08 dotNET workflow notebooks/`.md` (`01`–`03`) bruger nu `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` med `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Den tidligere `02-semantic-kernel.ipynb` blev omskrevet til at bruge Microsoft Agent Framework med Azure OpenAI (Responses API) og omdøbt til `02-python-agent-framework-azure-openai.ipynb`.
- **Standardiseret på `FoundryChatClient` + `as_agent`.** README og notebook kode, der refererede til `AzureAIProjectAgentProvider` blev standardiseret efter det kanoniske mønster brugt i Lesson 01 og frameworkets egne eksempler: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` med `provider.as_agent(...)`. Opdateret i Lesson 02–14 README'er og notebooks (fx Lesson 13 memory, alle Lesson 14 notebooks, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Produktnavngivning.** Omdøbt gennem hele det engelske indhold:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Uændret: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", og miljøvariabelnavne.)
- **Afhængigheder** ([requirements.txt](../../requirements.txt)):
  - Fastlåst `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Fastlåst `openai>=1.108.1` (minimum for Responses API).
  - Fjernet `azure-ai-inference` (blev kun brugt af de migrerede GitHub Models eksempler).
- **Miljøkonfiguration** ([.env.example](../../.env.example)): fjernet GitHub Models variabler (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); tilføjet `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` og valgfri `AZURE_OPENAI_API_KEY`; opdateret navngivning til Microsoft Foundry.
- **Dokumentation** — Opdateret [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) og [STUDY_GUIDE.md](./STUDY_GUIDE.md) for ovenstående (opsætning af miljøvariabler, verifikationskode, vejledning til provider, navngivning).

### Fjernet

- GitHub Models onboarding trin og miljøvariabler fra opsætningsdokumenterne (erstattet af Azure OpenAI / Microsoft Foundry).

### Sikkerhed / Privatliv (offentlig delings oprydning)

- Rydede Jupyter notebook output, som lækkede et ægte **Azure abonnement ID**, resource gruppe / ressource navne og Bing forbindelses ID, plus udvikleres **lokale filstier og brugernavne**, i:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Bekræftet, at der ikke er API nøgler, tokens, abonnement ID'er eller personlige stier tilbage i det sporbare engelske indhold (de `GITHUB_TOKEN` referencer, der er tilbage, er GitHub Actions token i workflows og GitHub MCP server PAT i Lesson 11 opsætningen — begge legitime og uafhængige af GitHub Models).

### Noter og kendte begrænsninger

- **Ikke eksekveret/kompileret.** Disse er uddannelsesmæssige eksempler opdateret til API- og navngivningskorrekthed; de blev ikke kørt mod live Azure ressourcer, og .NET eksemplerne blev ikke kompileret i dette miljø. Validér mod din egen Microsoft Foundry / Azure OpenAI udgivelse.
- **Modeludrulning skal understøtte Responses API.** Brug en udrulning som `gpt-4.1-mini`, `gpt-4.1`, eller en `gpt-5.x` model. Ældre modeller understøtter kernefunktionalitet i Responses, men ikke alle funktioner.
- **Agent-framework version.** Eksemplerne sigter mod den seneste MAF (`>=1.10.0`). Det kanoniske agent-oprettelses kald er `client.as_agent(...)`; API'er blev valideret mod frameworkets publicerede dokumentation og en installeret build. Hvis du fastlåser en anden version, bekræft metode tilgængelighed (`as_agent` vs `create_agent`).
- **Lesson 08 workflow notebook 04** beholder bevidst `AzureAIAgentClient` (fra `agent-framework-azure-ai`), fordi den bruger Microsoft Foundry Agent Service hostede værktøjer (Bing grounding, code interpreter); den er allerede baseret på Responses.
- **.NET standardudrulning.** To Lesson 08 dotNET workflow eksempler brugte tidligere hårdkodet en specifik model; de bruger nu standardværdien `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Hvis et eksempel kræver multimodal/vision input, sæt `AZURE_OPENAI_DEPLOYMENT` til en egnet model.
- **Foundry Local** eksponerer en OpenAI-kompatibel **Chat Completions** endpoint og er beregnet til lokal udvikling; brug Azure OpenAI / Microsoft Foundry for det komplette Responses API funktionssæt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->