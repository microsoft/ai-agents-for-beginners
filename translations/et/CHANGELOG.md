# Muutuste ajalugu

Kõik olulised muudatused **AI Agents for Beginners** kursusel on dokumenteeritud selles failis.

## [Avaldatud] — 2026-07-14

See versioon toob kursuse üle kahel uuel kasutusest kõrvaldatud mudelil, migreerib ülejäänud õppetükkide märkmikud stabiilsele Microsoft Agent Framework API-le ning valideerib Python-märkmikud reaalajas Microsoft Foundry juurutuse vastu.

### Muudetud

- **Liigutatud kõrvale kasutusest kõrvaldatud mudelid (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Nii `gpt-4.1` kui ka `gpt-4.1-mini` on nüüd kõrvaldatud (ametlik pensionile jäämise kuupäev **14. oktoober 2026**). Asendatud kõik kursuse viited (dokumendid, `.env.example`, Python/.NET märkmikud ja näited) mitte-kõrvaldatud mudeliga `gpt-5-mini`. Õppetüki 16 mudeli marsruutimise näide säilitab väikese/suuruse kontrasti kasutades `gpt-5-nano` (väike) ja `gpt-5-mini` (suur). Kolmanda osapoole failid ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), ajaloolised GitHubi mudelite tekstid ning `azure-openai-to-responses` oskuse võimekuse märkmed jäid tahtlikult muutmata.
- **Õppetüki 14 üleandmise märkmik viidi üle stabiilsele API-le.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) kasutab nüüd `agent_framework.orchestrations.HandoffBuilder` koos `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type` põhise voogedastuse ja `FoundryChatClient`-iga (asendades eemaldatud pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` sümbolid).
- **Õppetüki 14 manus inimtsüklis märkmik viidi üle stabiilsele API-le.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) peatub nüüd `ctx.request_info(...)` + `@response_handler` abil (asendades eemaldatud `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), ehitab `WorkflowBuilder(start_executor=..., output_executors=[...])` abil, juhib struktureeritud väljundit `default_options={"response_format": ...}` kaudu ning kasutab skriptitud vastust, nii et märkmik töötab iseseisvalt (ilma blokeeriva `input()`-ta).
- **Keskkonna konfiguratsioon** ([.env.example](../../.env.example)): mudelide juurutuste nimed on muudetud `gpt-5-mini`-ks; lisatud `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (õppetüki 16 marsruutimine) ja varasemalt puudunud `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (õppetükk 15 brauserikasutus).
- **Sõltuvused** ([requirements.txt](../../requirements.txt)): spetsiaalselt fikseeritud `agent-framework`, `agent-framework-foundry` ja `agent-framework-openai` versiooniks `~=1.10.0` iseennast kinnitava komplekti jaoks (1.11.0 sisaldab eksperimentaalseid katkestavaid muudatusi nende õppetükkide kasutatavates näidetes).

### Märkused ja teadaolevad piirangud

- **Valideeritud reaalajas Microsoft Foundry vastu.** Python-märkmikud käideldi peata (headlessly) läbi `nbconvert`-iga Microsoft Foundry projektis kasutades `gpt-5-mini` (ja `gpt-5-nano` õppetüki 16 marsruutimiseks). Kasutage oma projektis samaväärseid mitte-kõrvaldatud mudelite juurutusi; märkmikud loevad juurutuse nime keskkonnamuutujatest `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Mõne õppetüki jaoks on vaja endiselt lisavarustust.** Õppetükk 05 vajab Azure AI Search’i; õppetüki 08 Bing-põhist töövoogu (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) vajab Bing’i ühendust ja Microsoft Foundry Agent Service’i majutustööriistu; õppetükk 13 (Cognee) ja õppetükk 17 (Foundry Local) vajavad eraldi käituskeskkondi.

## [Avaldatud] — 2026-07-13

See versioon lisab kaks uut õppetükki, mis lõpetavad juurutuse arengukaare — agendid skaleeritakse Microsoft Foundrys ja vähendatakse ühe tööjaamani — lisaks suitsutesti torujuhi, värskendatud kursuse navigeerimise, uued õppija oskused ja uuendatud brändingu.

### Lisatud

- **Õppetükk 16 — skaleeritavate agentide juurutamine Microsoft Foundrys.** Uus õppetükk [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) ja käivitatav märkmik [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb), mis ehitab tootmisvalmis klienditoe agendi (tööriistad, RAG, mälu, mudeli marsruutimine, vastuse vahemällu salvestamine, inimkinnitus, hindamislukk ja OpenTelemetry jälgimine), koos arendus/juurutus/käitusaeg Mermaid diagrammidega, teadmiste kontrolli, ülesande ja väljakutsega.
- **Õppetükk 17 — lokaalsete AI agentide loomine Foundry Locali ja Qweniga.** Uus õppetükk [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) ja märkmik [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) ehitab täisfunktsionaalse seadmel baseeruva inseneri assistendi (Qweni funktsioonikõne Foundry Local kaudu, liivakastis failitööriistad, lokaalne RAG Chromaga, valikuline kohalik MCP), koos ainult lokaalse / lokaalse RAG / tööriistakõnede diagrammidega, teadmiste kontrolli, ülesande ja väljakutsega.
- **Suitsutesti torujuht.** Uus [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) töövoog [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) koos iga õppetüki jaoks kataloogidega [tests/](./tests/README.md), juurutatavate agentide jaoks õppetundides 01, 04, 05 ja 16, koos indeks-README-ga, mis kaardistab iga kataloogi õppetüki ja majutatud agendi nimega. Õppetükk 16 lisab jaotise "Juurutatud agendi valideerimine suitsutestidega"; õppetükid 01/04/05 saavad valikulise suitsutesti osutaja.
- **Õppija oskused.** Uued agentide oskused kaustas `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (pakendades õppetükkide 16 ja 17 juhendid) ja [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (kuidas valideerida märkmiku näidised reaalajas Microsoft Foundry / Azure OpenAI keskkonnas).
- **Märkmike valideerija jooksutaja.** Uus [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), mis täidab iga Python-märkmiku peata (headlessly) `nbconvert` abil ja kuvab PASS/FAIL maatriksi (pluss `results.json`). Leiab automaatselt hoidla juure ja Pythoni, välistab vaikimisi mitte-kursuse märkmikud (`.venv`, `site-packages`, `translations`, oskuse templiidivarad) ja `.NET` märkmikud, toetab `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` ja `-Python` valikuid.
- **Kursusnavigeerimine.** Lisatud eelmise / järgmise õppetüki lingid õppetundidele 11–15 (varem puudusid), nii et kogu kursus ühendub jadana 00 → 18 mõlemas suunas.
- **Uued pisipildid.** Pisipildid õppetundidele 16 ja 17, lisaks värskendatud hoidla sotsiaalne pilt [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (kuvab nüüd kahte uut õppetundi ja URL-i `aka.ms/ai-agents-beginners`).
- **Sõltuvused** ([requirements.txt](../../requirements.txt)): lisatud `foundry-local-sdk` ja `chromadb` õppetükile 17.

### Muudetud

- **Põhi- [README.md](./README.md)** õppetükkide tabel: Õppetükid 16 ja 17 lingivad nüüd oma sisule (varem "Varsti tulemas"); hoidla pilt uuendatud `repo-thumbnailv3.png`-ks.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: lisatud õppetükid 16 ja 17 üksikult juhendisse ja õpiteedele ning lisatud jaotis "Juurutatud agentide valideerimine suitsutestidega".
- **[AGENTS.md](./AGENTS.md)**: uuendatud õppetükkide arv/kirjeldus (00–18), lisatud suitsutesti valideerimise jaotis ja lisatud näited õppetükkide 16/17 proovinäidiste nimede kohta.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Eelmine õppetükk" osutab nüüd õppetükile 17 (varem õppetükk 15), lõpetades järjestuse.
- **Standardiseeritud mudeliviited mitte-kõrvaldatud mudelitele.** Asendatud kõik `gpt-4o` / `gpt-4o-mini` viited kogu kursusel (dokumendid, `.env.example`, Python/.NET märkmikud ja näited) mudeliga `gpt-4.1-mini` — `gpt-4o` (kõik versioonid) kaotab toe 2026. Õppetüki 16 mudeli marsruutimise näide säilitab väikese/suuruse kontrasti kasutades `gpt-4.1-mini` (väike) ja `gpt-4.1` (suur). Python-märkmikud valivad nüüd mudeli keskkonnamuutujate (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) põhjal, mitte ei kodeeri mudeli nime kõvasti.

### Märkused ja teadaolevad piirangud

- **Ei täidetud reaalajas Azure’i keskkonnas.** Uute õppetükkide märkmikud on harjutuslikud näited; jooksutage ja valideerige neid oma Microsoft Foundry / Foundry Local keskkonnas. Suitsutesti töövoog nõuab, et juurutaksite õppetüki agendi ja seadistaksite Azure OIDC saladused (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) koos **Azure AI User** rolliga Foundry projekti ulatuses.
- **Õppetükk 17 on ainult lokaalne.** Sellel pole Foundry Responses lõpp-punkti, seega suitsutesti tegevus sellele ei kehti; valideerige seda, käivitades märkmiku oma töölaual.

## [Avaldatud] — 2026-07-06

See versioon toob kursuse üle **Azure OpenAI Responses API** peale, standardiseerib tootenimed **Microsoft Foundry** ja **Microsoft Agent Framework (MAF)** all, loobub GitHubi mudelitest, uuendab SDK versioone ning lisab uut sisu kohalikest mudelitest ja teiste raamistikude majutamisest Foundrys.

### Lisatud

- **Migreerimise oskus** — Paigaldatud [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) agentide oskus (agent skill) kaustas `.agents/skills/`, kaasa arvatud selle viited ja skanneri skript.
- **Foundry Local (mudelite jooksutamine seadmel)** — uus jaotis "Alternatiivne teenusepakkuja: Foundry Local" failis [00-course-setup/README.md](./00-course-setup/README.md), mis käsitleb installi (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` ja `FoundryLocalManager` ühendamist Microsoft Agent Frameworkiga `OpenAIChatClient` kaudu.
- **LangChain / LangGraph agentide majutamine Microsoft Foundrys** — uus jaotis failis [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md), pluss käivitatav näide [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), kasutades `langchain-azure-ai[hosting]` ja `ResponsesHostServer` (protokoll `/responses`), põhineb [Microsoft Learn-il](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — uus jaotis "Reaalmaailma näide: Microsoft Project Opal" failis [15-browser-use/README.md](./15-browser-use/README.md), mis esitab Opali ettevõtte arvutikasutuse agendina ja seob selle kursuse mõistetega (inimene-tsüklis, usaldus/turvalisus, planeerimine, oskused).
- **Teine õppetüki 02 Python näide** — lisatud [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (vaata "Muudetud" — migreeritud endisest Semantic Kernel märkmikust) ja link majutatud õppetüki README-s.
- Lisatud uus jaotis "Models and Providers" failile [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Muudetud

- **Vestluse lõpetustest → Responses API (Python).** Näited, mis varem kutsusid mudelit otse, migrati üle Chat Completion-st Responses API-le (`client.responses.create(input=..., store=False)`, `resp.output_text`), kasutades `OpenAI` klienti stabiilse Azure OpenAI `/openai/v1/` lõpp-punkti vastu (ilma `api_version`-ita). Mõjutatud näited:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — täielik funktsiooni kutsumise juhend (tööriista skeem muudetud Responses formaati, tööriista tulemused tagastatud `function_call_output`, `max_output_tokens` jpt kujul).

- **GitHub mudelid → Azure OpenAI.** GitHub Models on aegunud (väljumas **juulis 2026**) ja ei toeta Responses API-d. Kõik GitHub Models koodirajad konverteeriti Azure OpenAI / Microsoft Foundry'ks Pythonis ja .NET näidetes:
  - Python: Lesson 08 töövoo märkmikud (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + kaaslaste `.md` dokumendid ning Lesson 08 dotNET töövoo märkmikud/`.md` (`01`–`03`) kasutavad nüüd `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` koos `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Endine `02-semantic-kernel.ipynb` kirjutati ümber kasutamaks Microsoft Agent Frameworki Azure OpenAI (Responses API) abil ning nimetati ümber `02-python-agent-framework-azure-openai.ipynb`.
- **Standardiseeritud `FoundryChatClient` + `as_agent`.** README ja märkmikukood, mis viitas `AzureAIProjectAgentProvider`-ile, standardiseeriti canoonilisele mustrile, mida kasutab Lesson 01 ja raamistu enda näited: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` koos `provider.as_agent(...)`. Uuendatud kõigis Lesson 02–14 README-des ja märkmikes (nt Lesson 13 mälu, kõik Lesson 14 märkmikud, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Toote nimetamine.** Nimetati ümber kogu ingliskeelses sisus:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Muutumata: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" ja keskkonnamuutuja nimed.)
- **Sõltuvused** ([requirements.txt](../../requirements.txt)):
  - Lukustatud `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Lukustatud `openai>=1.108.1` (miinimum Responses API jaoks).
  - Eemaldatud `azure-ai-inference` (kasutatud ainult migreeritud GitHub Models näidetes).
- **Keskkonna konfiguratsioon** ([.env.example](../../.env.example)): eemaldatud GitHub Models muutujad (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); lisatud `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` ja valikuline `AZURE_OPENAI_API_KEY`; uuendatud nimetused Microsoft Foundry-le.
- **Dokumendid** — Uuendatud [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) ja [STUDY_GUIDE.md](./STUDY_GUIDE.md) ülaltoodu jaoks (keskkonnamuutujate seadistus, kontrollkilluke, pakkuja juhis, nimetused).

### Eemaldatud

- GitHub Models kasutusele võtmise sammud ja keskkonnamuutujad seadistusdokumentidest (asendatud Azure OpenAI / Microsoft Foundryga).

### Turvalisus / Privaatsus (avaliku jagamise koristus)

- Puhastatud Jupyteri märkmiku käitusväljundid, mis lekkisid reaalse **Azure tellimuse ID**, ressursigrupi / ressursi nimed ja Bingi ühenduse ID, samuti arendaja **kohalikud failiteed ja kasutajanimed**, failides:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Kinnitatud, et jälgitud ingliskeelses sisus ei ole jäänud API võtmeid, token'eid, tellimuse IDsid ega isiklikke teid (jäägid `GITHUB_TOKEN` on ainult GitHub Actions token töövoogudes ja GitHub MCP server PAT Lesson 11 seadistuses — mõlemad on seaduslikud ja ei puutu GitHub Modelsid).

### Märkused ja teadaolevad piirangud

- **Ei käivitatud/kompileeritud.** Need on hariduslikud näited, mis on uuendatud API / nimetuste õigeks tööks; neid ei käidatud elavate Azure ressursside peal ning .NET näiteid ei kompileeritud selles keskkonnas. Kontrolli enda Microsoft Foundry / Azure OpenAI juurutuse vastu.
- **Mudeli juurutus peab toetama Responses API-d.** Kasuta sellist juurutust nagu `gpt-4.1-mini`, `gpt-4.1` või `gpt-5.x` mudel. Vanemad mudelid toetavad põhifunktsioone, aga mitte kõiki omadusi.
- **Agent-frameworki versioon.** Näited on mõeldud uusimale MAF-versioonile (`>=1.10.0`). Canoni agent-loomis kutsumine on `client.as_agent(...)`; API-sid kontrolliti raamistu avaldatud dokumentatsiooni ja paigaldatud build'i vastu. Kui kasutad teist versiooni, kinnita meetodi olemasolu (`as_agent` vs `create_agent`).
- **Lesson 08 töövoo märkmik 04** hoiab teadlikult `AzureAIAgentClient` (pärit `agent-framework-azure-ai`), sest see kasutab Microsoft Foundry Agent Service majutatud tööriistu (Bing grounding, koodi tõlgendaja); see baseerub juba Responses-l.
- **.NET vaikimisi juurutus.** Kaks Lesson 08 dotNET töövoo näidet varem koodis fikseerisid kindla mudeli; nüüd on vaikimisi `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Kui näide vajab multimodaalset / nägemisteavet, sea `AZURE_OPENAI_DEPLOYMENT` sobivaks mudeliks.
- **Foundry Local** pakub OpenAI-ga ühilduvat **Chat Completions** lõpp-punkti ja on mõeldud kohalikuks arenduseks; täiskomplekti Responses API funktsioone kasuta Azure OpenAI / Microsoft Foundryga.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->