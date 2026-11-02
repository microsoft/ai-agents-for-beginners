# Dnevnik promjena

Sve značajne promjene u tečaju **AI agenti za početnike** dokumentirane su u ovoj datoteci.

## [Izdano] — 2026-07-14

Ovo izdanje premješta tečaj s dva novo zastarjela modela, migrira preostale bilježnice Lekcija na stabilni API Microsoft Agent Frameworka i potvrđuje Python bilježnice protiv aktivnog Microsoft Foundry postava.

### Promijenjeno

- **Premješteno s zastarjelih modela (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Oba modela `gpt-4.1` i `gpt-4.1-mini` su sada zastarjela (datum povlačenja **14. listopada 2026**). Zamijenjeni su svi refensi na tečaj (dokumentacija, `.env.example`, Python/.NET bilježnice i primjeri) ne-zastarjelim `gpt-5-mini`. Primjer usmjeravanja modela u Lekciji 16 zadržava kontrast mali/veliki koristeći `gpt-5-nano` (mali) i `gpt-5-mini` (veliki). Vanjski datoteke treće strane ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), povijesni GitHub Models tekst i bilješke o sposobnostima vještine `azure-openai-to-responses` namjerno su ostavljeni nepromijenjeni.
- **Bilježnica predaje Lekcije 14 migrirana na stabilni API.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) sada koristi `agent_framework.orchestrations.HandoffBuilder` s `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, streaming temeljen na `event.type` i `FoundryChatClient` (zamjenjujući uklonjene simbole pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Bilježnica za human-in-the-loop u Lekciji 14 migrirana na stabilni API.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) sada pauzira preko `ctx.request_info(...)` + `@response_handler` (zamjenjujući uklonjene `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), gradi se sa `WorkflowBuilder(start_executor=..., output_executors=[...])`, upravlja strukturiranim izlazom kroz `default_options={"response_format": ...}`, i koristi skriptirani odgovor tako da bilježnica radi bez nadzora (bez blokirajućeg `input()`).
- **Konfiguracija okoline** ([.env.example](../../.env.example)): promijenjena imena implementacije modela u `gpt-5-mini`; dodani `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (usmjeravanje Lekcije 16) i prethodno nedostajući `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (Lekcija 15 korištenje preglednika).
- **Ovisnosti** ([requirements.txt](../../requirements.txt)): fiksirane verzije `agent-framework`, `agent-framework-foundry` i `agent-framework-openai` na `~=1.10.0` za samosustavan, potvrđeni skup (verzija 1.11.0 donosi eksperimentalne prekidne promjene na površinama koje ove lekcije koriste).

### Bilješke i poznata ograničenja

- **Potvrđeno protiv aktivnog Microsoft Foundry.** Python bilježnice su izvršene bezglavno s `nbconvert` u Microsoft Foundry projektu koristeći `gpt-5-mini` (i `gpt-5-nano` za usmjeravanje u Lekciji 16). Implementirajte ekvivalentne ne-zastarjele modele u svom projektu; bilježnice čitaju ime implementacije iz `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Neki dodatni resursi još su potrebni za određene lekcije.** Lekcija 05 treba Azure AI Search; proces rada Lekcije 08 Bing-grounding (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) treba Bing vezu i Microsoft Foundry Agent Service alate; Lekcija 13 (Cognee) i Lekcija 17 (Foundry Local) trebaju vlastita runtime okruženja.

## [Izdano] — 2026-07-13

Ovo izdanje dodaje dvije nove lekcije koje zaokružuju luk implementacije — skaliranje agenata na Microsoft Foundry i spuštanje na jedno radno mjesto — plus pipeline za test dima, obnovljenu navigaciju tečajem, nove vještine učenika i ažurirani branding.

### Dodano

- **Lekcija 16 — Implementacija skalabilnih agenata s Microsoft Foundry.** Nova lekcija [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) i izvršna bilježnica [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) koja gradi produkcijskog agenta za korisničku podršku (alati, RAG, memorija, usmjeravanje modela, spremanje odgovora, ljudsko odobrenje, evaluacijska kapija i OpenTelemetry praćenje), s razvojnim/implementacijskim/runtime Mermaid dijagramima, provjerom znanja, zadatkom i izazovom.
- **Lekcija 17 — Kreiranje lokalnih AI agenata s Foundry Local i Qwenom.** Nova lekcija [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) i bilježnica [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) koja gradi potpuno asistenta za inženjering na uređaju (Qwen funkcijsko pozivanje preko Foundry Local, sandboxirani alati za datoteke, lokalni RAG s Chromom, opcionalni lokalni MCP), s dijagramima samo za lokalno / lokalni-RAG / pozivanje alata, provjerom znanja, zadatkom i izazovom.
- **Pipeline za test dima.** Novi [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) workflow [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) plus katalozi po lekcijama pod [tests/](./tests/README.md) za implementirane agente u Lekcijama 01, 04, 05 i 16, s index README-om koji povezuje svaki katalog s lekcijom i imenom hostiranog agenta. Lekcija 16 ima odjeljak "Validacija implementiranog agenta pomoću testova dima"; Lekcije 01/04/05 dobivaju opcionalni pokazivač za test dima.
- **Vještine učenika.** Nove Agentičke vještine pod `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (povezuju smjernice Lekcija 16 i 17) i [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (kako potvrditi uzorke bilježnica protiv aktivnog Microsoft Foundry / Azure OpenAI postava).
- **Pokretač za validaciju bilježnica.** Novi [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) koji izvršava svaku Python bilježnicu bezglavno s `nbconvert` i ispisuje PASS/FAIL matricu (plus `results.json`). Automatski otkriva root repozitorij i Python, po defaultu isključuje nelečajne bilježnice (`.venv`, `site-packages`, `translations`, predloške vještina) i `.NET` bilježnice, te podržava `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` i `-Python`.
- **Navigacija tečajem.** Dodane veze Prethodna/Sljedeća lekcija za Lekcije 11–15 (prijašnje su nedostajale) tako da cijeli tečaj može linearno povezati 00 → 18 u oba smjera.
- **Nove sličice.** Sličice za Lekcije 16 i 17, plus osvježena društvena slika repozitorija [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (sada promovira dvije nove lekcije i URL `aka.ms/ai-agents-beginners`).
- **Ovisnosti** ([requirements.txt](../../requirements.txt)): dodani `foundry-local-sdk` i `chromadb` za Lekciju 17.

### Promijenjeno

- **Glavna [README.md](./README.md)** tablica lekcija: Lekcije 16 i 17 sada vode na svoje sadržaje (prije "Uskoro"); slika repozitorija ažurirana na `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: dodane Lekcije 16 i 17 u vodič po lekcijama i putovima učenja, te odjeljak "Validacija implementiranih agenata putem testova dima".
- **[AGENTS.md](./AGENTS.md)**: ažuriran broj/opis lekcija (00–18), dodan odjeljak za potvrdu testova dima, te primjeri imenovanja uzoraka Lekcija 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Prethodna lekcija" sada vodi na Lekciju 17 (prije Lekcija 15), zatvarajući lanac.
- **Standardizirani refensi modela na ne-zastarjele modele.** Zamijenjeni svi refensi `gpt-4o` / `gpt-4o-mini` širom tečaja (dokumentacija, `.env.example`, Python/.NET bilježnice i primjeri) s `gpt-4.1-mini` — `gpt-4o` (sve verzije) se povlači 2026. Primjer usmjeravanja modela u Lekciji 16 zadržava kontrast mali/veliki koristeći `gpt-4.1-mini` (mali) i `gpt-4.1` (veliki). Python bilježnice sada biraju model iz varijabli okoline (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) umjesto tvrdog koda naziva modela.

### Bilješke i poznata ograničenja

- **Nisu izvršene protiv aktivnog Azurea.** Nove bilježnice lekcija su edukativni primjeri; pokrenite ih i validirajte na vlastitom Microsoft Foundry / Foundry Local postavu. Workflow za test dima zahtijeva da implementirate agenta lekcije i konfigurirate Azure OIDC tajne (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) s ulogom **Azure AI User** na razini Foundry projekta.
- **Lekcija 17 je samo lokalna.** Nema Foundry Responses endpoint, tako da se akcija test dima ne primjenjuje; validirajte je pokretanjem bilježnice na svom računalu.

## [Izdano] — 2026-07-06

Ovo izdanje migrira tečaj na **Azure OpenAI Responses API**, standardizira nazive proizvoda na **Microsoft Foundry** i **Microsoft Agent Framework (MAF)**, povlači GitHub Models, ažurira verzije SDK-a i dodaje novi sadržaj o lokalnim modelima i hostiranju drugih frameworka na Foundry.

### Dodano

- **Migracijska vještina** — Instalirana [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent vještina (iz [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) pod `.agents/skills/`, uključujući reference i skriptu za skeniranje.
- **Foundry Local (pokretanje modela na uređaju)** — Novi odjeljak "Alternativni pružatelj: Foundry Local" u [00-course-setup/README.md](./00-course-setup/README.md) koji pokriva instalaciju (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` i povezivanje `FoundryLocalManager` s Microsoft Agent Frameworkom preko `OpenAIChatClient`.
- **Hostiranje LangChain / LangGraph agenata na Microsoft Foundry** — Novi odjeljak u [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus izvršni primjer [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) koristeći `langchain-azure-ai[hosting]` i `ResponsesHostServer` (protokol `/responses`), temeljen na [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Novi odjeljak "Stvarni primjer: Microsoft Project Opal" u [15-browser-use/README.md](./15-browser-use/README.md) koji opisuje Opal kao agenta za korištenje računala u poduzeću i mapira ga na koncepte tečaja (human-in-the-loop, povjerenje/sigurnost, planiranje, vještine).
- **Drugi Python primjer za Lekciju 02** — Dodan [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (pogledajte "Promijenjeno" — migrirano iz bivše Semantic Kernel bilježnice) i povezan u README lekcije.
- Dodan odjeljak "Models and Providers" u [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Promijenjeno

- **Chat Completions → Responses API (Python).** Primjeri koji su izravno pozivali model migrirani su s Chat Completions na Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), koristeći `OpenAI` klijenta prema stabilnom Azure OpenAI `/openai/v1/` endpointu (bez `api_version`). Uključeni primjeri su:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — potpuni vodič kroz pozivanje funkcija (šema alata pretvorena u Responses format, rezultati alata vraćeni kao `function_call_output`, `max_output_tokens`, itd.).

- **GitHub modeli → Azure OpenAI.** GitHub modeli su zastarjeli (povlače se **srpanj 2026**) i ne podržavaju Responses API. Svi kodni putovi GitHub modela prebačeni su na Azure OpenAI / Microsoft Foundry u Python i .NET primjerima:
  - Python: radni bilježnici lekcije 08 (`01`–`03`), lekcija 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + prateće `.md` dokumentacije, i radni bilježnici/leksikoni lekcije 08 dotNET/`.md` (`01`–`03`) sada koriste `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` s `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Prijašnji `02-semantic-kernel.ipynb` preprisan je da koristi Microsoft Agent Framework s Azure OpenAI (Responses API) i preimenovan u `02-python-agent-framework-azure-openai.ipynb`.
- **Standardizirano na `FoundryChatClient` + `as_agent`.** README i kod u bilježnicama koji su referencirali `AzureAIProjectAgentProvider` standardizirani su na kanonski uzorak korišten u lekciji 01 i vlastitim uzorcima okvira: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` s `provider.as_agent(...)`. Ažurirano u lekcijama 02–14 README i bilježnicama (npr. lekcija 13 memory, sve bilježnice lekcije 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Nazivi proizvoda.** Preimenovano u cijelom engleskom sadržaju:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Nepromijenjeno: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" i nazivi varijabli okoline.)
- **Ovisnosti** ([requirements.txt](../../requirements.txt)):
  - Fiksirano `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Fiksirano `openai>=1.108.1` (minimalno za Responses API).
  - Uklonjeno `azure-ai-inference` (koristilo se samo u migriranim GitHub Models primjerima).
- **Konfiguracija okoline** ([.env.example](../../.env.example)): uklonjene varijable GitHub modela (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); dodano `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` i opcionalno `AZURE_OPENAI_API_KEY`; ažurirani nazivi za Microsoft Foundry.
- **Dokumentacija** — ažurirani [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) i [STUDY_GUIDE.md](./STUDY_GUIDE.md) za navedeno (postavljanje varijabli okoline, provjerna skripta, smjernice za pružatelja, nazivi).

### Uklonjeno

- Koraci za uključivanje (onboarding) GitHub modela i varijable okoline iz dokumentacije za postavljanje (zastarjeli zbog Azure OpenAI / Microsoft Foundry).

### Sigurnost / Privatnost (čišćenje javnih podataka)

- Očišćeni rezultati izvršavanja Jupyter bilježnica u kojima su procurili stvarni **Azure ID pretplate**, imena resource-group / resursa i Bing connection ID, plus developerski **lokalni putovi do datoteka i korisnička imena**, u:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Provjereno da nema API ključeva, tokena, ID pretplate ili osobnih putanja u praćenom engleskom sadržaju (preostale reference na `GITHUB_TOKEN` su GitHub Actions token u workflows i GitHub MCP server PAT u postavljanju lekcije 11 — oboje legitimno i nevezano uz GitHub modele).

### Napomene i poznata ograničenja

- **Nisu izvršavani/kompilirani.** Ovo su obrazovni primjeri ažurirani radi ispravnosti API/naziva; nisu pokretani na živim Azure resursima i .NET primjeri nisu kompilirani u ovom okruženju. Provjerite vlastitu instalaciju Microsoft Foundry / Azure OpenAI.
- **Implementacija modela mora podržavati Responses API.** Koristite implementaciju poput `gpt-4.1-mini`, `gpt-4.1` ili `gpt-5.x` modela. Stariji modeli podržavaju osnovne funkcije Responses API ali ne sve značajke.
- **Verzija agent-frameworka.** Primjeri ciljaju najnoviju verziju MAF (`>=1.10.0`). Kanonski poziv za kreiranje agenta je `client.as_agent(...)`; API su potvrđeni prema objavljenim dokumentima okvira i instaliranoj izvedbi. Ako koristite drugu verziju, potvrdite dostupnost metoda (`as_agent` vs `create_agent`).
- **Radni bilježnik lekcije 08 workflow 04** namjerno koristi `AzureAIAgentClient` (iz `agent-framework-azure-ai`) jer koristi alate Microsoft Foundry Agent Service (Bing podrška, interpreter koda); već je baziran na Responses.
- **.NET zadana implementacija.** Dva .NET primjera za lekciju 08 workflow prethodno su hardkodirala određeni model; sad su prema zadanim postavkama na `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Ako primjer zahtijeva multimodalni/vision input, postavite `AZURE_OPENAI_DEPLOYMENT` na odgovarajući model.
- **Foundry Local** izlaže OpenAI-kompatibilni **Chat Completions** endpoint i namijenjen je za lokalni razvoj; koristite Azure OpenAI / Microsoft Foundry za potpuni skup značajki Responses API.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->