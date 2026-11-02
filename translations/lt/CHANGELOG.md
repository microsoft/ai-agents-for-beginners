# Pakeitimų žurnalas

Visos svarbios **AI Agentų pradedantiesiems** kurso naujienos dokumentuojamos šiame faile.

## [Išleista] — 2026-07-14

Šiame leidime kursas perkeliamas nuo dviejų naujai pasenusių modelių, likę pamokų užrašai migravami į stabilų Microsoft Agent Framework API, o Python užrašai tikrinami tiesioginėje Microsoft Foundry aplinkoje.

### Pakeista

- **Perkelta nuo pasenusių modelių (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Dabar `gpt-4.1` ir `gpt-4.1-mini` yra pasenę (paskelbtas išjungimo terminas **2026 m. spalio 14 d.**). Visos kurso nuorodos (dokumentuose, `.env.example`, Python/.NET užrašuose ir pavyzdžiuose) pakeistos į nepasenusį `gpt-5-mini`. 16 pamokos modelio maršruto pavyzdyje išlaikytas mažo/didelio kontrastas naudojant `gpt-5-nano` (mažas) ir `gpt-5-mini` (didelis). Trečiųjų šalių duomenys ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), istoriniai GitHub Models tekstai ir `azure-openai-to-responses` įgūdžių pastabos liko nepakeisti.
- **14 pamokos perdavimo užrašas migravo į stabilų API.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) dabar naudoja `agent_framework.orchestrations.HandoffBuilder` su `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type` pagrindu transliuojamą srautą ir `FoundryChatClient` (vietoje pašalintų iki 1.0 versijos `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` simbolių).
- **14 pamokos žmogaus į kilpą užrašas migravo į stabilų API.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) dabar pristabdomas per `ctx.request_info(...)` + `@response_handler` (vietoje pašalintų `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), kuriamas su `WorkflowBuilder(start_executor=..., output_executors=[...])`, struktūruotą išvestį valdo per `default_options={"response_format": ...}`, ir naudoja skriptinį atsakymą, todėl užrašas veikia be žmogaus įsikišimo (nereikia blokuojančios `input()` funkcijos).
- **Aplinkos konfigūracija** ([.env.example](../../.env.example)): pakeisti modelių diegimo pavadinimai į `gpt-5-mini`; pridėti `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (16 pamokos maršrutizavimui) ir anksčiau trūkstamas `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (15 pamokos naršyklės naudojimui).
- **Priklausomybės** ([requirements.txt](../../requirements.txt)): užfiksuotos `agent-framework`, `agent-framework-foundry` ir `agent-framework-openai` versijos `~=1.10.0`, kad būtų užtikrintas savitarpiškai suderinamas, patikrintas rinkinys (versija 1.11.0 įveda eksperimentinius negrįžtamus pokyčius šioms pamokoms reikalingose funkcijose).

### Pastabos ir žinomi apribojimai

- **Patikrinta tiesioginėje Microsoft Foundry aplinkoje.** Python užrašai vykdyti nesuvaidintai naudojant `nbconvert` prieš Microsoft Foundry projektą su `gpt-5-mini` (ir `gpt-5-nano` 16 pamokos maršrutizavimui). Diekite lygiavertį nepasektą modelį savo projekte; užrašai skaito diegimo pavadinimą iš `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Kai kurioms pamokoms vis dar reikia papildomų išteklių.** 5 pamokai reikalinga Azure AI Search; 8 pamokos Bing pagrįstam veiksmui (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) reikia Bing jungties ir Microsoft Foundry Agent Service patalpintų įrankių; 13 (Cognee) ir 17 (Foundry Local) pamokoms reikalingos atskiros vykdymo aplinkos.

## [Išleista] — 2026-07-13

Šiame leidime pridėtos dvi naujos pamokos, užbaigiančios diegimo lanką — agentų mastelio didinimą Microsoft Foundry ir mažinimą iki vieno darbo stoties — taip pat pateikiamas gedimų testavimo procesas, atnaujinta kurso navigacija, nauji mokymosi įgūdžiai ir atnaujintas ženklinimas.

### Pridėta

- **16 pamoka — Skalavimo agentų diegimas su Microsoft Foundry.** Nauja pamoka [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) ir vykdomasis užrašas [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb), kuriuose kuriamas gamybinis klientų aptarnavimo agentas (įrankiai, RAG, atmintis, modelių maršrutizavimas, atsakymų talpinimas, žmogaus patvirtinimas, vertinimo vartai ir OpenTelemetry sekimas), taip pat pateikiami kūrimo/diegimo/vykdymo Mermaid diagramos, žinių testas, užduotis ir iššūkis.
- **17 pamoka — Vietinių AI agentų kūrimas su Foundry Local ir Qwen.** Nauja pamoka [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) ir užrašas [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb), kuriuose kuriamas visiškai įrenginio viduje veikiantis inžinerinis asistentas (Qwen funkcijų kvietimas per Foundry Local, izoliaciniai failų įrankiai, vietinis RAG su Chroma, pasirinktinai vietinė MCP), su vietinėmis/ vietinio RAG / įrankių kvietimo diagramomis, žinių testu, užduotimi ir iššūkiu.
- **Gedimų testavimo procesas.** Naujas [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) darbų procesas [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) ir pamokų katalogai po [tests/](./tests/README.md) skirtas diegiamiesiems agentams pamokose 01, 04, 05 ir 16, su pagrindiniu README, kuriame kiekvienas katalogas priskirtas konkrečiai pamokai ir agentų vardui. 16 pamokoje pridėta skyrius „Diegto agento tikrinimas per gedimų testus“; pamokose 01/04/05 pridėtas pasirinktinai gedimų testų rodyklė.
- **Mokinio įgūdžiai.** Nauji agentų įgūdžiai `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (apimantys 16 ir 17 pamokų gaires) ir [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (kaip patikrinti užrašų pavyzdžius tiesioginėje Microsoft Foundry / Azure OpenAI aplinkoje).

- **Užrašų validavimo vykdytojas.** Nauji [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), kurie kiekvieną Python užrašą vykdo be galvos su `nbconvert` ir atspausdina PASS/FAIL matricą (taip pat `results.json`). Automatiškai aptinka repo šaknį ir Python, pagal numatytuosius nustatymus neįtraukia ne kursų užrašų (`.venv`, `site-packages`, `translations`, įgūdžių šablonų turtas) ir `.NET` užrašų, palaiko `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` ir `-Python`.
- **Kurso navigacija.** Pridėtos Ankstesnio/Kito pamokos nuorodos pamokoms 11–15 (anksčiau jų nebuvo), todėl visas kursas grandine jungiasi nuo 00 iki 18 abiem kryptimis.
- **Nauji miniatiūros atvaizdai.** Pamokų miniatiūros 16 ir 17 pamokoms, taip pat atnaujintas saugyklos socialinės žiniasklaidos paveikslėlis [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (dabar reklamuoja dvi naujas pamokas ir `aka.ms/ai-agents-beginners` URL).
- **Priklausomybės** ([requirements.txt](../../requirements.txt)): pridėti `foundry-local-sdk` ir `chromadb` 17 pamokai.

### Pakeista

- **Pagrindinė [README.md](./README.md)** pamokų lentelė: pamokos 16 ir 17 dabar nuorodo į savo turinį (anksčiau „Greitai bus“); saugyklos paveikslėlis pakeistas į `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md):** pridėtos pamokos 16 ir 17 prie pamokų gido ir mokymosi kelių, taip pat „Įdiegto agento patikrinimas dūminių testų pagalba“ skyrius.
- **[AGENTS.md](./AGENTS.md):** atnaujintas pamokų skaičius/ aprašymas (00–18), pridėtas dūminio testavimo patvirtinimo skyrius ir pamokų 16/17 pavyzdinių vardų pavyzdžiai.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md):** „Ankstesnė pamoka“ dabar rodo į pamoką 17 (anksčiau buvo pamoka 15), taip užbaigiant grandinę.
- **Standartizuoti modelių pavadinimai nepasenusiems modeliams.** Visos `gpt-4o` / `gpt-4o-mini` nuorodos per visą kursą (dokumentacijoje, `.env.example`, Python/.NET užrašuose ir pavyzdžiuose) pakeistos į `gpt-4.1-mini` — `gpt-4o` (visos versijos) bus nutrauktos 2026 metais. 16 pamokos modelio maršrutizavimo pavyzdyje išlaikytas mažo/didelio kontrastas naudojant `gpt-4.1-mini` (mažas) ir `gpt-4.1` (didelis). Python užrašai dabar pasirenka modelį iš aplinkos kintamųjų (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`), o ne kodo viduje užkoduoto pavadinimo.

### Pastabos ir žinomi apribojimai

- **Nedirba tiesiogiai su tiesioginiu Azure.** Naujos pamokos užrašai yra edukaciniai pavyzdžiai; paleiskite ir tikrinkite juos savo Microsoft Foundry / Foundry Local aplinkoje. Dūminio testavimo darbo eiga reikalauja įdiegti pamokos agentą ir sukonfigūruoti Azure OIDC paslaptis (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) su **Azure AI vartotojo** rolė Foundry projekto lygmenyje.
- **17 pamoka skirta tik lokaliai naudoti.** Ji neturi Foundry Atsakymų (Responses) pabaigos taško, todėl dūminio testavimo veiksmas netaikomas; patikrinkite ją paleisdami užrašą savo darbo stotyje.

## [Išleista] — 2026-07-06

Šis leidimas perkelia kursą prie **Azure OpenAI Responses API**, standartizuoja produkto pavadinimus **Microsoft Foundry** ir **Microsoft Agent Framework (MAF)**, nutraukia GitHub modelius, atnaujina SDK versijas ir prideda naują turinį apie vietinius modelius bei kitų sistemų talpinimą Foundry.

### Pridėta

- **Migracijos įgūdis** — Įdiegta [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) agente įgūdis (iš [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) kataloge `.agents/skills/`, įskaitant nuorodas ir skenerio skriptą.
- **Foundry Local (modelių paleidimas vietoje įrenginyje)** — Naujas skyrius „Alternatyvus tiekėjas: Foundry Local“ [00-course-setup/README.md](./00-course-setup/README.md), aprašantis diegimą (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` ir `FoundryLocalManager` sujungimą su Microsoft Agent Framework per `OpenAIChatClient`.
- **LangChain / LangGraph agentų talpinimas Microsoft Foundry** — Naujas skyrius [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md), kartu su paleidžiamu pavyzdžiu [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), naudojant `langchain-azure-ai[hosting]` ir `ResponsesHostServer` (protokolą `/responses`), pagal [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Naujas skyriaus „Realaus pasaulio pavyzdys: Microsoft Project Opal“ [15-browser-use/README.md](./15-browser-use/README.md), pristatantis Opal kaip įmonės kompiuterio naudotojo agentą ir susieto su kurso koncepcijomis (žmogiškas įsikišimas, pasitikėjimas/sauga, planavimas, įgūdžiai).
- **Antras Python pavyzdys pamokoje 02** — Pridėtas [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (žr. „Pakeista“ skyrių – perkelta iš ankstesnio Semantic Kernel užrašo) ir susietas su pamokos README.
- Pridėtas skyrius „Modeliai ir tiekėjai“ į [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Pakeista

- **Chat Completions → Responses API (Python).** Pavyzdžiai, kurie tiesiogiai kvietė modelį, perkelti iš Chat Completions į Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), naudojant `OpenAI` klientą stabiliajame Azure OpenAI `/openai/v1/` gale (be `api_version`). Paveikti pavyzdžiai:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)

  - [04-tool-use/README.md](./04-tool-use/README.md) — pilnas funkcijų kvietimo vadovas (įrankio schema sulydyta į Atsakymų formatą, įrankio rezultatai grąžinti kaip `function_call_output`, `max_output_tokens` ir kt.).

- **GitHub modeliai → Azure OpenAI.** GitHub modeliai yra nebenaudojami (bus nutraukti **2026 m. liepos mėn.**) ir nepalaiko Responses API. Visi GitHub modelių kodo keliai buvo konvertuoti į Azure OpenAI / Microsoft Foundry Python ir .NET pavyzdžiuose:
  - Python: pamokos 08 darbo eigos užrašų knygelės (`01`–`03`), pamoka 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + papildomi `.md` dokumentai, ir pamokos 08 dotNET darbo eigos užrašų knygelės/`.md` (`01`–`03`) dabar naudoja `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` su `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Buvęs `02-semantic-kernel.ipynb` buvo perrašytas naudoti Microsoft Agent Framework su Azure OpenAI (Responses API) ir pervadintas į `02-python-agent-framework-azure-openai.ipynb`.
- **Standartizuota naudojant `FoundryChatClient` + `as_agent`.** README ir užrašų knygelių kodas, kuris nurodė `AzureAIProjectAgentProvider`, buvo standartizuotas pagal kanoninį modelį, naudojamą pamokoje 01 ir framework'o pavyzdžiuose: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` su `provider.as_agent(...)`. Atnaujinta per pamokų 02–14 README ir užrašų knygeles (pvz., pamoka 13 atmintis, visos pamokos 14 užrašų knygelės, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Produkto pavadinimai.** Pervadinta visuose anglų kalbos turiniuose:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Ne pasikeitė: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" ir aplinkos kintamųjų pavadinimai.)
- **Priklausomybės** ([requirements.txt](../../requirements.txt)):
  - Užfiksuota `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Užfiksuota `openai>=1.108.1` (minimalus Responses API palaikymas).
  - Pašalinta `azure-ai-inference` (naudota tik su perkeltais GitHub modelių pavyzdžiais).
- **Aplinkos konfigūracija** ([.env.example](../../.env.example)): pašalinti GitHub modelių kintamieji (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); pridėti `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` ir neprivalomas `AZURE_OPENAI_API_KEY`; atnaujinta pavadinimų naudojimas Microsoft Foundry.
- **Dokumentacija** — atnaujinta [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) ir [STUDY_GUIDE.md](./STUDY_GUIDE.md) pagal aukščiau nurodytus pakeitimus (aplinkos kintamųjų nustatymas, patikros fragmentas, tiekėjo gairės, pavadinimų atnaujinimas).

### Pašalinta

- GitHub modelių įvedimo žingsniai ir aplinkos kintamieji iš nustatymo dokumentų (pakeisti Azure OpenAI / Microsoft Foundry).

### Saugumas / Privatumas (viešo dalijimosi išvalymas)

- Išvalyti Jupyter užrašų knygelių vykdymo rezultatai, kuriuose nutekėjo tikras **Azure prenumeratos ID**, išteklių grupių / išteklių pavadinimai ir Bing ryšio ID, plius kūrėjo **vietiniai failų keliai ir vartotojų vardai**, šiuose failuose:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Patikrinta, kad nesiliktų API raktų, žetonų, prenumeratos ID ar asmeninių kelių sekamuose anglų kalbos failuose (liekantys `GITHUB_TOKEN` nurodymai yra GitHub Actions žetonas darbo eigoje ir GitHub MCP serverio PAT pamokoje 11 — abu teisėti ir nesusiję su GitHub modeliais).

### Pastabos ir žinomi apribojimai

- **Nevykdyta / nerekompiliuota.** Tai yra mokomieji pavyzdžiai, atnaujinti dėl API / pavadinimų teisingumo; jie nebuvo paleisti tiesiogiai prieš tiesiogines Azure išteklius, o .NET pavyzdžiai nebuvo kompiliuoti šioje aplinkoje. Patikrinkite su savo Microsoft Foundry / Azure OpenAI diegimu.
- **Modelio diegimas turi palaikyti Responses API.** Naudokite diegimą, pvz., `gpt-4.1-mini`, `gpt-4.1` arba `gpt-5.x` modelį. Senesni modeliai palaiko pagrindinę Responses funkcionalumo dalį, bet ne visas ypatybes.
- **Agent-framework versija.** Pavyzdžiai skirti naujausiam MAF (`>=1.10.0`). Kanoninis agento kūrimo kvietimas yra `client.as_agent(...)`; API buvo patikrintos pagal framework dokumentaciją ir įdiegtą versiją. Jei fiksuojate kitą versiją, patikrinkite metodų prieinamumą (`as_agent` prieš `create_agent`).
- **Pamokos 08 darbo eigos užrašų knygelė 04** sąmoningai naudoja `AzureAIAgentClient` (iš `agent-framework-azure-ai`), nes naudojami Microsoft Foundry Agent Service įrankiai (Bing žemėlapiai, kodo interpretatorius); jau pagrįsta Responses.
- **.NET numatytasis diegimas.** Du pamokos 08 dotNET darbo eigos pavyzdžiai anksčiau turėjo konkretaus modelio kietąjį kodą; dabar naudojama numatytoji `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Jei pavyzdys naudoja multimodal / vaizdo įvestį, nustatykite `AZURE_OPENAI_DEPLOYMENT` į tinkamą modelį.
- **Foundry Local** teikia OpenAI suderinamą **Chat Completions** galinį tašką ir skirtas vietiniam vystymui; pilnoms Responses API funkcijoms naudokite Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->