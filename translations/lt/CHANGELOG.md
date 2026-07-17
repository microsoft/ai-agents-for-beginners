# Pakeitimų žurnalas

Visos svarbios **AI agentų pradedantiesiems** kurso pakeitimų detalės dokumentuotos šiame faile.

## [Išleista] — 2026-07-13

Šis leidimas prideda dvi naujas pamokas, kurios užbaigia diegimo ciklą — agentų mastelio didinimą Microsoft Foundry ir mažinimą iki vieno darbo stoties — bei prideda dūmų testavimo seką, atnaujintą kurso navigaciją, naujus mokinių įgūdžius ir atnaujintą prekės ženklą.

### Pridėta

- **16 pamoka — Mastelio didinimo agentų diegimas su Microsoft Foundry.** Nauja pamoka [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) ir paleidžiamas bloknotas [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb), kuriame kuriamas gamybos klientų aptarnavimo agentas (įrankiai, RAG, atmintis, modelių maršrutizavimas, atsakymų kešavimas, žmogaus patvirtinimas, vertinimo vartai ir OpenTelemetry stebėjimas), su vystymo/diegimo/veikimo Mermaid diagramomis, žinių patikra, užduotimi ir iššūkiu.
- **17 pamoka — Vietinių AI agentų kūrimas su Foundry Local ir Qwen.** Nauja pamoka [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) ir bloknotas [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb), kuriame kuriamas visiškai įrenginyje veikiantis inžinerinis asistentas (Qwen funkcijų kvietimas per Foundry Local, saugūs failų įrankiai, vietinis RAG su Chroma, neprivalomas vietinis MCP), su tik vietinėms / vietiniu RAG / įrankių kvietimų diagramomis, žinių patikra, užduotimi ir iššūkiu.
- **Dūmų testavimo pipeline.** Naujas [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) darbas [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) bei pamokų katalogai po [tests/](./tests/README.md) skirti diegiamų agentų testavimui pamokose 01, 04, 05 ir 16, su README indeksu, kuriame kiekvienas katalogas susietas su pamoka ir talpinamo agento pavadinimu. Pamokoje 16 pridėtas skirsnis „Diegto agente dūmų testų patvirtinimas“; pamokose 01/04/05 pridėtas neprivalomas dūmų testo nukreipimas.
- **Mokinių įgūdžiai.** Nauji Agentų įgūdžiai `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (apimantys 16 ir 17 pamokų nurodymus) ir [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (kaip patikrinti bloknotų pavyzdžius suveikiančius gyvai Microsoft Foundry / Azure OpenAI aplinkoje).
- **Bloknotų patvirtinimo vykdytojas.** Naujas [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), kuris paleidžia kiekvieną Python bloknotą be vartotojo sąveikos su `nbconvert` ir pateikia PRAĖJO/NEPRAĖJO matricą (plus `results.json`). Automatiškai nustato repozitorijos šaknį ir Python, pagal nutylėjimą neįtraukia nekurso bloknotų (`.venv`, `site-packages`, `translations`, įgūdžių šablonų turtas) ir `.NET` bloknotų, palaiko filtrus `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` ir `-Python`.
- **Kurso navigacija.** Pridėti ankstesnės/kitos pamokos saitai pamokoms 11–15 (anksčiau jų nebuvo), tad visas kursas sujungtas grandine nuo 00 iki 18 abiem kryptimis.
- **Nauji miniatiūrų paveikslėliai.** Pamokų 16 ir 17 miniatiūros, taip pat atnaujintas socialinis vaizdas repozitorijai [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (dabar reklamuoja dvi naujas pamokas ir `aka.ms/ai-agents-beginners` adresą).
- **Priklausomybės** ([requirements.txt](../../requirements.txt)): pridėti `foundry-local-sdk` ir `chromadb` pamokai 17.

### Pakeista

- **Pagrindinis [README.md](./README.md)** pamokų lentelė: pamokos 16 ir 17 dabar turi nuorodas į turinį (anksčiau buvo „Greitai“); repo paveikslėlis atnaujintas į `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: pridėtos pamokos 16 ir 17 pamokų vadove ir mokymosi keliuose, taip pat pridėtas skyrius „Diegtų agentų patvirtinimas dūmų testais“.
- **[AGENTS.md](./AGENTS.md)**: atnaujintas pamokų skaičius/aprašymas (nuo 00 iki 18), pridėtas skyrius apie dūmų testavimą, taip pat pavyzdžių pavadinimai pamokoms 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: „Ankstesnė pamoka“ dabar nurodo pamoką 17 (anksčiau buvo 15), taip užbaigiant nuoseklumą.
- **Standartizuotos modelių nuorodos nepasenusiuose modeliuose.** Visos `gpt-4o` / `gpt-4o-mini` nuorodos dokumentacijoje, `.env.example`, Python/.NET bloknotuose ir pavyzdžiuose pakeistos į `gpt-4.1-mini` — `gpt-4o` (visos versijos) bus nutrauktos 2026 metais. Pamokos 16 modelių maršrutizavimo pavyzdyje išlaikomas mažo/didelio kontrastas naudojant `gpt-4.1-mini` (mažas) ir `gpt-4.1` (didelis). Python bloknotai dabar renkasi modelį iš aplinkos kintamųjų (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`), o ne kietai įrašyto modelio pavadinimo.

### Pastabos ir žinomi apribojimai

- **Nevykdomi tiesiogiai Azure aplinkoje.** Naujos pamokos bloknotai yra mokomieji pavyzdžiai; juos paleiskite ir patikrinkite savo Microsoft Foundry / Foundry Local aplinkoje. Dūmų testavimo veikla reikalauja diegti pamokos agentą ir sukonfigūruoti Azure OIDC slaptažodžius (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) su **Azure AI vartotojo** teise Foundry projekto lygiu.
- **Pamoka 17 yra tik vietinė.** Ji neturi Foundry Responses taško, todėl dūmų testo veiksmas netaikomas; ją patikrinkite paleisdami bloknotą savo darbo vietoje.

## [Išleista] — 2026-07-06

Šis leidimas perkelia kursą prie **Azure OpenAI Responses API**, standartizuoja produkto pavadinimus į **Microsoft Foundry** ir **Microsoft Agent Framework (MAF)**, nutraukia GitHub modelius, atnaujina SDK versijas ir prideda naują turinį apie vietinius modelius ir kitų sistemų talpinimą Foundry.

### Pridėta


- **Migracijos įgūdis** — Įdiegta [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agentų įgūdžių rinkinys (iš [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) po `.agents/skills/`, įskaitant jo nuorodas ir skenerio scenarijų.
- **Foundry Local (modelių vykdymas įrenginyje)** — Nauja skiltis "Alternatyvus tiekėjas: Foundry Local" dokumente [00-course-setup/README.md](./00-course-setup/README.md), apimanti įdiegimą (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` ir `FoundryLocalManager` sujungimą su Microsoft Agent Framework per `OpenAIChatClient`.
- **LangChain / LangGraph agentų talpinimas Microsoft Foundry aplinkoje** — Nauja skiltis dokumente [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) ir paleidžiamas pavyzdys [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), naudojantis `langchain-azure-ai[hosting]` ir `ResponsesHostServer` (pagal `/responses` protokolą), remiantis [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nauja "Tikrojo pasaulio pavyzdys: Microsoft Project Opal" skiltis dokumente [15-browser-use/README.md](./15-browser-use/README.md), apibūdinanti Opal kaip įmonės kompiuterio naudojimo agentą ir siejanti jį su kurso koncepcijomis (žmogus procese, pasitikėjimas/sauga, planavimas, Įgūdžiai).
- **Antroji pamoka 02 Python pavyzdys** — Pridėtas [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (žr. "Pakeista" — migracija iš ankstesnio Semantic Kernel užrašų knygelės) ir susietas su pamokos README.
- Pridėta skiltis **Modeliai ir tiekėjai** į [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Pakeista

- **Chat Completions → Responses API (Python).** Pavyzdžiai, kurie tiesiogiai kvietė modelį, buvo perkelti iš Chat Completions į Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`) naudojant `OpenAI` klientą prie stabilaus Azure OpenAI `/openai/v1/` galinio taško (be `api_version`). Paveikti pavyzdžiai:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — pilnas funkcijos kvietimo vedlys (įrankio schema supaprastinta į Responses formatą, įrankio rezultatai grąžinami kaip `function_call_output`, `max_output_tokens` ir kt.).
- **GitHub Modeliai → Azure OpenAI.** GitHub Modeliai yra pasenę (nutraukiami **2026 m. liepos mėn.**) ir nepalaiko Responses API. Visi GitHub Modelių kodo keliai buvo konvertuoti į Azure OpenAI / Microsoft Foundry Python ir .NET pavyzdžiuose:
  - Python: pamokos 08 darbo eigų užrašų knygelės (`01`–`03`), pamoka 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + papildomi `.md` dokumentai ir pamokos 08 dotNET darbo eigos užrašų knygelės / `.md` (`01`–`03`) dabar naudoja `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` su `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Ankstesnis `02-semantic-kernel.ipynb` buvo perrašytas naudojant Microsoft Agent Framework su Azure OpenAI (Responses API) ir pervadintas į `02-python-agent-framework-azure-openai.ipynb`.
- **Standartizuota naudojant `FoundryChatClient` + `as_agent`.** README ir užrašų knygelės kodas, kuris nurodė `AzureAIProjectAgentProvider`, buvo standartizuotas pagal kanoninį modelį, kaip naudotas Pamokoje 01 ir sistemos savose pavyzdžiuose: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` kartu su `provider.as_agent(...)`. Atnaujinta Pamokų 02–14 README ir užrašų knygelėse (pvz., Pamokos 13 atmintis, visos Pamokos 14 užrašų knygelės, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Produkto pavadinimai.** Pervadinta visame anglų kalbos turinyje:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Išliko nepakitę: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" ir aplinkos kintamųjų pavadinimai.)
- **Priklausomybės** ([requirements.txt](../../requirements.txt)):
  - Fiksuota `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Fiksuota `openai>=1.108.1` (minimumas Responses API).
  - Pašalinta `azure-ai-inference` (naudota tik migravimuose GitHub Modelių pavyzdžiuose).
- **Aplinkos konfigūracija** ([.env.example](../../.env.example)): pašalinti GitHub Modelių kintamieji (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); pridėti `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` ir neprivalomą `AZURE_OPENAI_API_KEY`; atnaujinti pavadinimus į Microsoft Foundry.
- **Dokumentacija** — Atvesta tvarka atnaujinta [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), ir [STUDY_GUIDE.md](./STUDY_GUIDE.md) atsižvelgiant į aukščiau nurodytus pakeitimus (apima aplinkos kintamųjų nustatymą, tikrinimo fragmentą, tiekėjų gaires, pavadinimus).

### Pašalinta

- GitHub Modelių įvedimo žingsniai ir aplinkos kintamieji pašalinti iš nustatymo dokumentacijos (pakeista Azure OpenAI / Microsoft Foundry).

### Saugumas / Privatumas (viešo dalinimosi valymas)

- Išvalyti Jupyter užrašų knygelės vykdymo rezultatai, kurie atskleidė tikrą **Azure prenumeratos ID**, išteklių grupės / išteklių pavadinimus ir Bing prisijungimo ID, taip pat kūrėjo **vietinius failų kelius ir vartotojų vardus**, dokumentuose:

  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Patikrinta, kad stebimoje anglų kalbos medžiagoje neliko API raktų, žetonų, prenumeratos ID ar asmeninių kelių (likę `GITHUB_TOKEN` nuorodos yra GitHub Actions žetonai srautuose ir GitHub MCP serverio PAT 11 pamokos konfigūracijoje — abu teisėti ir nesusiję su GitHub Models).

### Pastabos ir žinomi apribojimai

- **Nekompiliuota/nevykdyta.** Tai yra mokomieji pavyzdžiai, atnaujinti dėl API/vardų teisingumo; jie nebuvo vykdomi tiesiogiai prieš gyvus Azure išteklius, o .NET pavyzdžiai nebuvo kompiliuoti šioje aplinkoje. Patikrinkite pagal savo Microsoft Foundry / Azure OpenAI diegimą.
- **Modelio diegimas turi palaikyti Responses API.** Naudokite diegimą, pvz., `gpt-4.1-mini`, `gpt-4.1` arba `gpt-5.x` modelį. Senesni modeliai palaiko pagrindinį Responses funkcionalumą, bet ne kiekvieną funkciją.
- **Agent-framework versija.** Pavyzdžiai orientuoti į naujausią MAF (`>=1.10.0`). Kanoninis agento kūrimo kvietimas yra `client.as_agent(...)`; API buvo tikrinamos pagal oficialią dokumentaciją ir įdiegtą versiją. Jei naudojate kitą versiją, patikrinkite metodo prieinamumą (`as_agent` vs `create_agent`).
- **Pamokos 08 darbo eigos užrašų knyga 04** tyčia naudoja `AzureAIAgentClient` (iš `agent-framework-azure-ai`), nes ji naudoja Microsoft Foundry Agent Service įrankius (Bing pagrindimas, kodo interpretatorius); ji jau paremta Responses API.
- **.NET numatytasis diegimas.** Du pamokos 08 dotNET darbo eigos pavyzdžiai anksčiau turėjo konkretaus modelio užkoduotą reikšmę; dabar numatytasis modelis yra `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Jei pavyzdys remiasi multimodaliu / vizualiniu įvestimi, nustatykite `AZURE_OPENAI_DEPLOYMENT` į tinkamą modelį.
- **Foundry Local** teikia OpenAI suderinamą **Chat Completions** galinį tašką ir yra skirtas vietinei plėtrai; norint pilno Responses API funkcionalumo naudokite Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->