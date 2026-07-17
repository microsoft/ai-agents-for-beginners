# Dnevnik sprememb

Vse pomembne spremembe v tečaju **AI agenti za začetnike** so dokumentirane v tej datoteki.

## [Izdano] — 2026-07-13

Ta izdaja dodaja dve novi lekciji, ki zaključujeta razdelek o uvajanju — skaliranje agentov do Microsoft Foundry in nazaj do ene delovne postaje — poleg tega pa tudi pipeline za hitri test, osveženo navigacijo po tečaju, nove veščine za udeležence in posodobljeno blagovno znamko.

### Dodano

- **Lekcija 16 — Uvajanje skalabilnih agentov z Microsoft Foundry.** Nova lekcija [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) in izvajalni zvezek [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb), ki gradi proizvodnega agenta za podporo uporabnikom (orodja, RAG, pomnilnik, usmerjanje modela, predpomnjenje odzivov, človeško odobritev, ocenjevalna zapora in OpenTelemetry sledenje), z diagrami razvoja/uvajanja/izvajanja v Mermaidu, preverjanjem znanja, nalogo in izzivom.
- **Lekcija 17 — Ustvarjanje lokalnih AI agentov z Foundry Local in Qwen.** Nova lekcija [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) in zvezek [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb), ki gradi popolnoma lokalnega inženirskega asistenta (klic funkcij Qwen preko Foundry Local, zaprta orodja za datoteke, lokalni RAG s Chromo, opcijski lokalni MCP), z diagrami samo lokalno / lokalni RAG / klici orodij, preverjanjem znanja, nalogo in izzivom.
- **Pipeline za hitri test.** Nov [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) workflow [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) ter katalozi po lekcijah v [tests/](./tests/README.md) za uvajalne agente v Lekcijah 01, 04, 05 in 16, z indeksom README, ki zemljevidi vsak katalog na njegovo lekcijo in ime hostanega agenta. Lekcija 16 dobi oddelek "Preverjanje uvajanega agenta s testi dima"; Lekcije 01/04/05 dobijo opcijsko povezavo do testa dima.
- **Veščine udeležencev.** Nove agentne veščine pod `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (paketiranje napotkov iz Lekcij 16 in 17), in [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (kako validirati vzorce zvezkov proti živi postavitvi Microsoft Foundry / Azure OpenAI).
- **Zagon validacije zvezkov.** Nov [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), ki izvrši vsak Python zvezek brez glave z `nbconvert` in izpiše tabelo USPEŠNO/NEUSPEŠNO (plus `results.json`). Samodejno zazna koren repozitorija in Python, izključi ne-tečajne zvezke (`.venv`, `site-packages`, `translations`, predloge za veščine) in `.NET` zvezke privzeto, ter podpira `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` in `-Python`.
- **Navigacija po tečaju.** Dodane povezave do prejšnje/naslednje lekcije za lekcije 11–15 (pred tem manjkale), tako da je celoten tečaj zaporedje 00 → 18 v obeh smereh.
- **Nove sličice.** Sličice lekcij za Lekciji 16 in 17, plus osvežena socialna slika repozitorija [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (sedaj oglašuje dve novi lekciji in URL `aka.ms/ai-agents-beginners`).
- **Odvisnosti** ([requirements.txt](../../requirements.txt)): dodan `foundry-local-sdk` in `chromadb` za Lekcijo 17.

### Spremenjeno

- **Glavna tabela lekcij v [README.md](./README.md)**: Lekciji 16 in 17 zdaj povezujeta na vsebino (pred tem "Prihaja kmalu"); slika repozitorija nadgrajena na `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: dodani Lekciji 16 in 17 v vodič lekcija-po-lekciji in učne poti, ter odsek "Preverjanje uvajanih agentov s testi dima".
- **[AGENTS.md](./AGENTS.md)**: posodobljeno število/opis lekcij (00–18), dodan odsek za validacijo s testi dima in dodani primeri poimenovanja vzorcev za Lekciji 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Prejšnja lekcija" zdaj kaže na Lekcijo 17 (pred tem Lekcija 15), s čimer se veriga zaključi.
- **Standardizirani sklici na modele, ki niso zastareli.** Vsi `gpt-4o` / `gpt-4o-mini` sklici po tečaju (dokumentacija, `.env.example`, Python/.NET zvezki in vzorci) so bili nadomeščeni z `gpt-4.1-mini` — `gpt-4o` (vse različice) se umika leta 2026. Primer usmerjanja modela v Lekciji 16 ohranja kontrast majhnega/velikega z `gpt-4.1-mini` (majhen) in `gpt-4.1` (velik). Python zvezki zdaj izberejo model iz okoljskih spremenljivk (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) namesto, da je ime modela zakodirano.

### Opombe in znane omejitve

- **Ni izvajano na živi Azure.** Novi lekcijski zvezki so izobraževalni primeri; zaženite in validirajte jih preko svoje lastne Microsoft Foundry / Foundry Local postavitve. Workflow za test dima zahteva, da uvajate agenta lekcije in nastavite skrivnosti Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) z vlogo **Azure AI User** v obsegu Foundry projekta.
- **Lekcija 17 je samo lokalna.** Nima končne točke Foundry Responses, zato se akcija za test dima ne uporablja; validirajte jo z zagonom zvezka na vaši delovni postaji.

## [Izdano] — 2026-07-06

Ta izdaja migrira tečaj na **Azure OpenAI Responses API**, standardizira poimenovanje izdelkov na **Microsoft Foundry** in **Microsoft Agent Framework (MAF)**, umika GitHub Models, posodablja različice SDK in dodaja nove vsebine o lokalnih modelih ter gostovanju drugih okvirjev na Foundry.

### Dodano

- **Veščina migracije** — Nameščena Agent Skill [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (iz [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) pod `.agents/skills/`, vključno s sklici in skripto za pregledovanje.
- **Foundry Local (zaganjajte modele na napravi)** — Nov odsek "Alternativni ponudnik: Foundry Local" v [00-course-setup/README.md](./00-course-setup/README.md), ki pokriva namestitev (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` in povezovanje `FoundryLocalManager` z Microsoft Agent Framework preko `OpenAIChatClient`.
- **Gostovanje agentov LangChain / LangGraph na Microsoft Foundry** — Nov odsek v [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) ter izvajalni vzorec [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), ki uporablja `langchain-azure-ai[hosting]` in `ResponsesHostServer` (protokol `/responses`), na podlagi [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nov odsek "Primer iz resničnega sveta: Microsoft Project Opal" v [15-browser-use/README.md](./15-browser-use/README.md), ki uokvirja Opal kot agenta za podjetniško uporabo računalnika in ga poveže s koncepti tečaja (človek-v-zanki, zaupanje/varnost, načrtovanje, veščine).
- **Drugi vzorec Python iz Lekcije 02** — Dodan [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (glej "Spremenjeno" — migrirano iz prejšnjega Semantic Kernel zvezka) in povezan v README lekcije.
- Dodan odsek **Modeli in ponudniki** v [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Spremenjeno

- **Chat Completions → Responses API (Python).** Primeri, ki so neposredno klicali model, so bili migrirani iz Chat Completions na Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), z uporabo `OpenAI` klienta proti stabilni Azure OpenAI `/openai/v1/` končni točki (brez `api_version`). Vplivani vzorci vključujejo:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — celoten prikaz klica funkcij (shema orodja spremenjena v format Responses, rezultati orodij vrnjeni kot `function_call_output`, `max_output_tokens` itd.).
- **GitHub Models → Azure OpenAI.** GitHub Models so zastareli (ne bodo več podprti **julija 2026**) in ne podpirajo Responses API. Vsi GitHub Models kosi kode so bili pretvorjeni v Azure OpenAI / Microsoft Foundry za Python in .NET vzorce:
  - Python: delovni zvezki Lekcije 08 (`01`–`03`), Lekcija 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + spremljevalni `.md` dokumenti, ter delovni zvezki / `.md` iz Lekcije 08 za dotNET (`01`–`03`) zdaj uporabljajo `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` z `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Prejšnji `02-semantic-kernel.ipynb` je bil prepisan za uporabo Microsoft Agent Framework z Azure OpenAI (Responses API) in preimenovan v `02-python-agent-framework-azure-openai.ipynb`.
- **Standardizirano na `FoundryChatClient` + `as_agent`.** README in koda zvezkov, ki so sklicevali `AzureAIProjectAgentProvider`, so bili standardizirani na kanonični vzorec, ki se uporablja v Lekciji 01 in lastnih vzorcih frameworka: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` z `provider.as_agent(...)`. Posodobljeno v Lekcijah 02–14 v README in zvezkih (npr. pomnilnik Lekcije 13, vsi zvezki Lekcije 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Poimenovanje izdelkov.** Preimenovano po celotni angleški vsebini:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Nespremenjeno: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" in imena okoljskih spremenljivk.)
- **Odvisnosti** ([requirements.txt](../../requirements.txt)):
  - Fiksirane različice `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Fiksirana različica `openai>=1.108.1` (minimalna za Responses API).
  - Odstranjen `azure-ai-inference` (uporabljen samo v migriranih GitHub Models vzorcih).
- **Konfiguracija okolja** ([.env.example](../../.env.example)): odstranjene spremenljivke za GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); dodane `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` in opcijski `AZURE_OPENAI_API_KEY`; poimenovanje posodobljeno na Microsoft Foundry.
- **Dokumentacija** — Posodobljeni [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) in [STUDY_GUIDE.md](./STUDY_GUIDE.md) za zgoraj navedeno (nastavitve okolja, predogled preverjanja, navodila za ponudnika, poimenovanje).

### Odstranjeno

- Koraki za začetek uporabe GitHub Models in okoljske spremenljivke iz dokumentacije nastavitve (nadomeščeno z Azure OpenAI / Microsoft Foundry).

### Varnost / zasebnost (čiščenje deljenja v javnosti)

- Izbrisani rezultati izvršbe Jupyter zvezkov, ki so razkrivali resničen **ID naročnine Azure**, imena skupin virov / virov, povezavo Bing ter razvijalske **lokalne poti do datotek in uporabniška imena** v:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Preverjeno, da v spremljani angleški vsebini ni ostalo nobenih API ključev, žetonov, ID-jev naročnin ali osebnih poti (referenca `GITHUB_TOKEN`, ki ostaja, predstavlja GitHub Actions token v workflowih in GitHub MCP server PAT v nastavitvi Lekcije 11 — obe legitimni in nepovezani z GitHub Models).

### Opombe in znane omejitve

- **Ni izvedeno/prevajano.** To so izobraževalni primeri, posodobljeni za pravilnost API/imenovanja; niso bili zagnani na živih Azure virih, prav tako vzorci .NET niso bili prevedeni v tem okolju. Preverite s svojo lastno Microsoft Foundry / Azure OpenAI namestitvijo.
- **Nameščanje modela mora podpirati Responses API.** Uporabite nameščanje, kot je `gpt-4.1-mini`, `gpt-4.1` ali model `gpt-5.x`. Starejši modeli podpirajo osnovno funkcionalnost Responses, vendar ne vseh funkcij.
- **Verzija agent-frameworka.** Primeri ciljajo najnovejši MAF (`>=1.10.0`). Kanonični klic za ustvarjanje agenta je `client.as_agent(...)`; API-je smo preverili glede na objavljeno dokumentacijo frameworka in nameščeno verzijo. Če uporabite drugačno verzijo, potrdite razpoložljivost metode (`as_agent` vs `create_agent`).
- **Delovni zvezek Lekcije 08, 04** namerno ohranja `AzureAIAgentClient` (iz `agent-framework-azure-ai`), ker uporablja Microsoft Foundry Agent Service gostujoča orodja (Bing osnovo, interpretacijo kode); že temelji na Responses.
- **Privzeta .NET namestitev.** Dva vzorca workflowov Lekcije 08 dotNET sta prej vsebovala trdo kodiran specifičen model; zdaj privzeto uporabita `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Če vzorec zahteva multimodalni/vidni vhod, nastavite `AZURE_OPENAI_DEPLOYMENT` na ustrezen model.
- **Foundry Local** izpostavlja OpenAI združljiv konektor za **Chat Completions** in je namenjen lokalnemu razvoju; za polno funkcionalnost Responses API uporabite Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->