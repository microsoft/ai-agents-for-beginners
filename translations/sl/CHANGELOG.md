# Dnevnik sprememb

Vse pomembne spremembe pri **AI agentih za začetnike** so dokumentirane v tej datoteki.

## [Izdan] — 2026-07-14

Ta izdaja seli tečaj s dveh novo ukinjenih modelov, migrira preostale zvezke lekcij na stabilni Microsoft Agent Framework API in preveri Python zvezke v živi implementaciji Microsoft Foundry.

### Spremenjeno

- **Prešlo z ukinjenih modelov (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Tako `gpt-4.1` kot `gpt-4.1-mini` sta sedaj ukinjena (datum uradnega prenehanja **14. oktober 2026**). Vsaka referenca v tečaju (dokumentacija, `.env.example`, Python/.NET zvezki in primeri) je bila zamenjana z neukinjeno `gpt-5-mini`. Primer usmerjanja modela pri Lekciji 16 ohranja kontrast majhnega/velikega z `gpt-5-nano` (majhen) in `gpt-5-mini` (velik). Tretjeosebne datoteke ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), zgodovinski GitHub Models tekst in opombe o zmožnostih spretnosti `azure-openai-to-responses` so bile namenoma nespremenjene.
- **Zvezek za predajo Lekcije 14 migriran na stabilen API.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) sedaj uporablja `agent_framework.orchestrations.HandoffBuilder` s `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, pretočno vrsto na podlagi `event.type` ter `FoundryChatClient` (namesto odstranjene pred-1.0 različice simbolov `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Zvezek z ljudmi v zanki Lekcije 14 migriran na stabilen API.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) sedaj počaka preko `ctx.request_info(...)` + `@response_handler` (namesto odstranjene `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), gradi z `WorkflowBuilder(start_executor=..., output_executors=[...])`, poganja strukturiran izhod preko `default_options={"response_format": ...}`, in uporablja skriptiran odgovor, da zvezek deluje samodejno (brez blokirajočega `input()`).
- **Konfiguracija okolja** ([.env.example](../../.env.example)): zamenjana imena modelov za implementacijo na `gpt-5-mini`; dodano `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (usmerjanje Lekcije 16) in prej manjkajoče `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (uporaba brskalnika Lekcija 15).
- **Odvisnosti** ([requirements.txt](../../requirements.txt)): priklenjeni `agent-framework`, `agent-framework-foundry` in `agent-framework-openai` na `~=1.10.0` za samosestavljiv, preverjen komplet (1.11.0 prinaša eksperimentalne prelomne spremembe na površinah, ki jih uporabljajo te lekcije).

### Opombe in znane omejitve

- **Preverjeno na živi Microsoft Foundry.** Python zvezki so bili izvedeni brez glavnega vmesnika z `nbconvert` proti Microsoft Foundry projektu z `gpt-5-mini` (in `gpt-5-nano` za usmerjanje Lekcije 16). Implementirajte ustrezne neukinjene modele v svojem projektu; zvezki berejo ime implementacije iz `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Nekatere lekcije še zahtevajo dodatne vire.** Lekcija 05 potrebuje Azure AI Search; delovni tok Bing-pritrditve Lekcije 08 (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) potrebuje povezavo z Bingom in Microsoft Foundry Agent Service gostovane pripomočke; Lekcija 13 (Cognee) in Lekcija 17 (Foundry Local) potrebujeta lastna runtime okolja.

## [Izdan] — 2026-07-13

Ta izdaja doda dve novi lekciji, ki dokončata implementacijsko stopnjo — skaliranje agentov do Microsoft Foundry in nazaj na eno delovno postajo — plus preveritveni piping, osveženo navigacijo po tečaju, nove veščine učenca in posodobljeno znamčenje.

### Dodano

- **Lekcija 16 — Implementacija skalabilnih agentov z Microsoft Foundry.** Nova lekcija [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) in izvajalni zvezek [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb), ki gradi produkcijskega agenta za podporo strankam (orodja, RAG, pomnilnik, usmerjanje modelov, predpomnjenje odzivov, človeško odobravanje, ocenjevalni prehod in OpenTelemetry sledenje), z diagrami razvoja/implementacije/izvajanja Mermaid, preverjanjem znanja, nalogo in izzivom.
- **Lekcija 17 — Lokalni AI agenti z Foundry Local in Qwen.** Nova lekcija [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) in zvezek [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) za gradnjo popolnoma na napravi delujočega inženirskega asistenta (klic funkcij Qwen preko Foundry Local, peskovnik datotečnih orodij, lokalni RAG s Chroma, opcijski lokalni MCP), z diagrami samo lokalno / lokalni RAG / klic orodij, preverjanjem znanja, nalogo in izzivom.
- **Preveritveni piping.** Nov [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) delovni tok [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) plus kataloški seznami po lekcijah pod [tests/](./tests/README.md) za učljive agente v Lekcijah 01, 04, 05 in 16, s predgledom README, ki vsak katalog poveže z lekcijo in imenom gostujočega agenta. Lekcija 16 dobi poglavje "Preverjanje nameščenega agenta s preveritvenimi testi"; lekcije 01/04/05 dodajo možnost za preverjanje.
- **Veščine učenca.** Nove Agent Skills pod `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (paket navodil Lekcij 16 in 17), in [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (kako potrditi vzorce zvezkov na živi postavitvi Microsoft Foundry / Azure OpenAI).
- **Zagon potrditvenega postopka zvezkov.** Novi [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), ki izvaja vsak Python zvezek brez glave z `nbconvert` in izpiše matriko USPEH/NEUSPEH (ter `results.json`). Samodejno zazna koren repozitorija in Python, izključi nepripadajoče zvezke (`.venv`, `site-packages`, `translations`, predloge spretnosti) in `.NET` zvezke po privzetku, podpira `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` in `-Python`.
- **Navigacija tečaja.** Dodane so povezave na prejšnjo/naslednjo lekcijo za lekcije 11–15 (prej manjkale), tako da tečaj celostno povezuje 00 → 18 v obe smeri.
- **Nove sličice.** Sličice lekcij za Lekciji 16 in 17 ter osvežena družabna slika repozitorija [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (sedaj oglašuje dve novi lekciji in URL `aka.ms/ai-agents-beginners`).
- **Odvisnosti** ([requirements.txt](../../requirements.txt)): dodano `foundry-local-sdk` in `chromadb` za Lekcijo 17.

### Spremenjeno

- **Glavna [README.md](./README.md)** tabela lekcij: Lekciji 16 in 17 sedaj povezujeta na svojo vsebino (prej je pisalo "Kmalu na voljo"); slika repozitorija posodobljena na `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: Lekciji 16 in 17 dodani v vodič po lekcijah in učne poti, ter poglavje "Preverjanje nameščenih agentov s preveritvenimi testi".
- **[AGENTS.md](./AGENTS.md)**: posodobljeno število/opis lekcij (00–18), dodano poglavje za preverjanje dima in dodani primeri imen vzorcev za Lekciji 16 in 17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Prejšnja lekcija" sedaj kaže na Lekcijo 17 (bila je Lekcija 15), s čimer je veriga zaključena.
- **Standardizirane reference modelov na neukinjenih modelih.** Zamenjane vse reference `gpt-4o` / `gpt-4o-mini` v celotnem tečaju (dokumentacija, `.env.example`, Python/.NET zvezki in primeri) z `gpt-4.1-mini` — `gpt-4o` (vse verzije) preneha delovati v 2026. Primer usmerjanja modela pri Lekciji 16 ohranja kontrast majhnega/velikega z `gpt-4.1-mini` (majhen) in `gpt-4.1` (velik). Python zvezki sedaj izbirajo model iz spremenljivk okolja (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) namesto trde kode.

### Opombe in znane omejitve

- **Ni izvedeno na živi platformi Azure.** Novi zvezki lekcij so vzorčni izobraževalni primeri; zaženite in jih preverite na svoji implementaciji Microsoft Foundry / Foundry Local. Preveritveni delovni tok zahteva, da implementirate agenta lekcije in nastavite Azure OIDC skrivnosti (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) s **vlogo uporabnika Azure AI** na obsegu projekta Foundry.
- **Lekcija 17 je samo lokalna.** Nima končne točke Foundry Responses, zato preveritvena akcija ne velja; preverite jo z zagonom zvezka na svoji delovni postaji.

## [Izdan] — 2026-07-06

Ta izdaja migrira tečaj na **Azure OpenAI Responses API**, standardizira poimenovanje izdelkov na **Microsoft Foundry** in **Microsoft Agent Framework (MAF)**, ukinja GitHub Models, posodobi različice SDK in doda novo vsebino o lokalnih modelih ter gostovanju drugih okvirov na Foundry.

### Dodano

- **Migracijska spretnost** — Namestitev [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent spretnosti (iz [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) v `.agents/skills/`, vključno z njenimi referencami in skripto za skeniranje.
- **Foundry Local (zagon modelov na napravi)** — Novo poglavje "Alternativni ponudnik: Foundry Local" v [00-course-setup/README.md](./00-course-setup/README.md), ki pokriva namestitev (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` in povezavo `FoundryLocalManager` s Microsoft Agent Framework preko `OpenAIChatClient`.
- **Gostovanje LangChain / LangGraph agentov na Microsoft Foundry** — Novo poglavje v [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) in izvajalni primer [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), ki uporablja `langchain-azure-ai[hosting]` in `ResponsesHostServer` (protokol `/responses`), na osnovi [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Novo poglavje "Primer iz resničnega sveta: Microsoft Project Opal" v [15-browser-use/README.md](./15-browser-use/README.md), ki predstavlja Opal kot podjetniškega agenta za uporabo računalnika in ga preslika v pojme tečaja (človek v zanki, zaupanje/varnost, načrtovanje, spretnosti).
- **Drugi vzorec Python Lekcije 02** — Dodan [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (glej "Spremenjeno" — migrirano iz nekdanjega zvezka Semantic Kernel) in povezan v vodiču lekcije.
- **Dodano poglavje Modeli in Ponudniki** v [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Spremenjeno

- **Chat Completions → Responses API (Python).** Primeri, ki so neposredno klicali model, so bili migrirani iz Chat Completions na Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), pri tem uporabljajo `OpenAI` odjemalca preko stabilne točke Azure OpenAI `/openai/v1/` (brez `api_version`). Vpliva na naslednje primere:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — celoten potek klica funkcije (orodna shema je preoblikovana v obliko Responses, rezultati orodij vrnjeni kot `function_call_output`, `max_output_tokens`, itd.).

- **GitHub modeli → Azure OpenAI.** GitHub modeli so zastareli (prenavljajo se **julij 2026**) in ne podpirajo Responses API. Vse poti kode GitHub modelov so bile pretvorjene v Azure OpenAI / Microsoft Foundry v Python in .NET primerih:
  - Python: zvezki potekov lekcije 08 (`01`–`03`), lekcija 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + spremljevalni `.md` dokumenti, in zvezki/dotNET tok dela lekcije 08/`.md` (`01`–`03`) zdaj uporabljajo `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` z `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Prej `02-semantic-kernel.ipynb` je bil prepisan za uporabo Microsoft Agent Framework z Azure OpenAI (Responses API) in preimenovan v `02-python-agent-framework-azure-openai.ipynb`.
- **Standardizirano na `FoundryChatClient` + `as_agent`.** Koda README in zvezkov, ki je klicala `AzureAIProjectAgentProvider`, je bila standardizirana na kanonični vzorec, ki se uporablja v lekciji 01 in v okviru lastnih primerov: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` z `provider.as_agent(...)`. Posodobljeno v lekcijah 02–14 README in zvezkih (npr. lekcija 13 pomnilnik, vsi zvezki lekcije 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Poimenovanje izdelkov.** Preimenovano po celotnem angleškem vsebini:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Nespremenjeno: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" in imena okolijskih spremenljivk.)
- **Odvisnosti** ([requirements.txt](../../requirements.txt)):
  - Zaklenjeno `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Zaklenjeno `openai>=1.108.1` (minimalno za Responses API).
  - Odstranjen `azure-ai-inference` (je bil uporabljen samo v prevedenih primerih GitHub modelov).
- **Konfiguracija okolja** ([.env.example](../../.env.example)): odstranjene spremenljivke GitHub modelov (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); dodane `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` in opcijsko `AZURE_OPENAI_API_KEY`; posodobljeno poimenovanje v Microsoft Foundry.
- **Dokumentacija** — posodobljeno [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) in [STUDY_GUIDE.md](./STUDY_GUIDE.md) za zgoraj (nastavitev env spremenljivk, potrditvena koda, navodila za ponudnika, poimenovanje).

### Odstranjeno

- Koraki uvedbe GitHub modelov in okoljske spremenljivke iz dokumentacije nastavitve (zamenjano z Azure OpenAI / Microsoft Foundry).

### Varnost / zasebnost (čiščenje javnega deljenja)

- Očiščeni izhodi izvajanja Jupyter zvezkov, ki so razkrili resnični **ID naročnine Azure**, imena skupin virov / virov, ID povezave Bing ter razvijalske **lokalne poti do datotek in uporabniška imena**, v:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Preverjeno, da v sledeni angleški vsebini ni ostankov API ključev, žetonov, ID naročnin ali osebnih poti (ostanki `GITHUB_TOKEN` so žeton GitHub Actions v potekih in GitHub MCP strežniški PAT v nastavitvi lekcije 11 — oba zakonita in nista povezana z GitHub modeli).

### Opombe in znane omejitve

- **Ni izvršeno/prevajano.** To so izobraževalni primeri posodobljeni za pravilnost API/poimenovanja; niso bili zagnani na živih virih Azure, in .NET primeri niso bili prevedeni v tem okolju. Preverite na svoji Microsoft Foundry / Azure OpenAI namestitvi.
- **Namestitev modela mora podpirati Responses API.** Uporabite namestitev, kot je `gpt-4.1-mini`, `gpt-4.1` ali model `gpt-5.x`. Starejši modeli podpirajo osnovno funkcionalnost Responses, vendar ne vseh funkcij.
- **Različica agent-framework.** Primeri ciljajo najnovejši MAF (`>=1.10.0`). Kanonični klic za ustvarjanje agenta je `client.as_agent(...)`; API je preverjen glede na objavljeno dokumentacijo ogrodja in nameščeno različico. Če uporabljate drugo različico, potrdite razpoložljivost metode (`as_agent` vs `create_agent`).
- **Workflow zvezek lekcije 08 št. 04** namensko ohranja `AzureAIAgentClient` (iz `agent-framework-azure-ai`), ker uporablja orodja Microsoft Foundry Agent Service (Bing osnovo, interpretator kode); že temelji na Responses.
- **Privzeta namestitev .NET.** Dva primera dotNET toka dela lekcije 08 sta prej trdo določala določen model; zdaj privzeto uporabljata `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Če vzorec zahteva večmodalni/vizualni vhod, nastavite `AZURE_OPENAI_DEPLOYMENT` na ustrezen model.
- **Foundry Local** ponuja OpenAI združljivo izhodišče za **Chat Completions** in je namenjen lokalnemu razvoju; za celoten nabor funkcij Responses API uporabite Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->