# Muudatuste logi

Kõik olulised muudatused kursuses **AI Agents for Beginners** on dokumenteeritud selles failis.

## [Välja antud] — 2026-07-13

See väljaanne lisab kaks uut õppetundi, mis lõpetavad juurutamise arengu – agente skaleerimine Microsoft Foundry’sse ja ühe töölaua tasemele – ning suitsutesti torujuhtme, värskendatud kursuse navigeerimise, uued õppija oskused ja uuendatud brändingu.

### Lisatud

- **Õppetund 16 — Skaleeritavate agentide juurutamine Microsoft Foundry abil.** Uus õppetund [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) ja käivitatav märkmik [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb), mis ehitab tootmisvalmis klienditoe agendi (tööriistad, RAG, mälu, mudeli marsruutimine, vastuste vahemällu salvestamine, inimkinnitus, hindamislukk ja OpenTelemetry jälgimine), koos arendus-/juurutus-/käivitamise Mermaid diagrammidega, teadmiste kontrolli, ülesande ja väljakutsega.
- **Õppetund 17 — Kohalike AI agentide loomine Foundry Local ja Qwen abil.** Uus õppetund [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) ja märkmik [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb), mis ehitab täielikult seadmes töötava inseneriassistendi (Qwen funktsioonikõned Foundry Local kaudu, turvalised failitööriistad, kohalik RAG koos Chromaga, valikuline kohalik MCP), koos kohalikult piiratud / kohaliku RAG / tööriista kutsumise diagrammidega, teadmiste kontrolli, ülesande ja väljakutsega.
- **Suitsutesti torujuhtme töövoog.** Uus [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) töövoog [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) ning iga õppetunni kataloogid [tests/](./tests/README.md) juurutatavate agentide jaoks õppetundides 01, 04, 05 ja 16, koos indeksi README-ga, mis seob iga kataloogi vastava õppetunni ja hostitud agendi nimega. Õppetund 16 lisab sektsiooni "Juurutatud agendi valideerimine suitsutestidega"; õppetunnid 01/04/05 lisavad valikulise suitsutesti viite.
- **Õppija oskused.** Uued Agent Skills kaustas `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (mis pakendab õppetundide 16 ja 17 juhised) ning [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (kuidas valideerida märkmiku näidiseid reaalse Microsoft Foundry / Azure OpenAI seadistusega).
- **Märkmike valideerimise jooksutaja.** Uus [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1), mis täidab kõik Python märkmikud pealetükkimatult `nbconvert`-i abil ja kuvab Õnnestus/Ebaõnnestus maatriksi (pluss `results.json`). Tuvastab automaatselt repos juurkausta ja Pythoni, jätab vaikimisi välja mitte-kursuse märkmikud (`.venv`, `site-packages`, `translations`, oskuste mallivarad) ja `.NET` märkmikud ning toetab parameetreid `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` ja `-Python`.
- **Kursuse navigeerimine.** Lisatud eelmise / järgmise õppetunni lingid õppetundidele 11–15 (varem puudusid), nii et kogu kursus on ühendatud jadana 00 → 18 mõlemas suunas.
- **Uued pisipildid.** Pisipildid õppetundidele 16 ja 17, samuti uuendatud repositooriumi sotsiaalne pilt [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (reklaamides nüüd kahte uut õppetundi ja aadressi `aka.ms/ai-agents-beginners`).
- **Sõltuvused** ([requirements.txt](../../requirements.txt)): lisatud `foundry-local-sdk` ja `chromadb` õppetunni 17 jaoks.

### Muudetud

- **Põhifaili [README.md](./README.md)** õppetabel: õppetunnid 16 ja 17 lingivad nüüd oma sisule (varem "Peagi saadaval"); repositooriumi pilt uuendatud `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: lisatud õppetunnid 16 ja 17 õppetunni-põhisesse juhendisse ja õppimisteedesse ning sektsioon "Juurutatud agentide valideerimine suitsutestidega".
- **[AGENTS.md](./AGENTS.md)**: uuendatud õppetundide arv/selgitus (00–18), lisatud suitsutesti valideerimise sektsioon ning õppetundide 16/17 näidismallide nimed.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Eelmine õppetund" suunab nüüd õppetundi 17 (varem oli 15), sulgedes järjendi.
- **Mudelite viidete standardimine mitteoskustamata mudelitele.** Asendatud kõik `gpt-4o` / `gpt-4o-mini` viited üle kursuse (dokumentatsioon, `.env.example`, Python/.NET märkmikud ja näited) `gpt-4.1-mini`-ga — `gpt-4o` (kõik versioonid) läheb pensionile 2026. Õppetunni 16 mudelimarsruudi näites hoitakse väikest/suurt vastandust, kasutades `gpt-4.1-mini` (väike) ja `gpt-4.1` (suur). Python märkmikud valivad nüüd mudeli keskkonnamuutujate (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) põhjal, mitte ei kasuta kõvakodetud mudelinime.

### Märkused ja teadaolevad piirangud

- **Ei täideta otse elava Azure’i vastu.** Uute õppetundide märkmikud on hariduslikud näited; käivitage ja valideerige neid oma Microsoft Foundry / Foundry Local seadistuse vastu. Suitsutesti töövoog nõuab, et juurutaksite õppetunni agendi ja seadistaksite Azure OIDC saladused (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) Microsoft Foundry projekti ulatuses koos rolliga **Azure AI User**.
- **Õppetund 17 on ainult kohalik.** Sellel puudub Foundry Responses lõpp-punkt, seega suitsutesti tegevus ei kehti; valideerige see, käivitades märkmiku oma töölaual.

## [Välja antud] — 2026-07-06

See väljaanne viib kursuse üle **Azure OpenAI Responses API** kasutusele, standardiseerib toodete nimetused **Microsoft Foundry** ja **Microsoft Agent Framework (MAF)** all, lõpetab GitHub Modelsi toetuse, uuendab SDK versioone ning lisab uut sisu kohalike mudelite ja teiste raamistikude majutamise kohta Foundry’s.

### Lisatud

- **Migreerimisoskused** — Paigaldatud [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (Azure-Samples/azure-openai-to-responses repost), koos viidete ja skanneri skriptiga kaustas `.agents/skills/`.
- **Foundry Local (mudelite seadmes töötamine)** — Uus jaotis "Alternatiivne pakkuja: Foundry Local" failis [00-course-setup/README.md](./00-course-setup/README.md), mis käsitleb installimist (`winget` / `brew`), `foundry model run` käsku, `foundry-local-sdk`-d ning `FoundryLocalManager` ühendamist Microsoft Agent Framework’iga `OpenAIChatClient` kaudu.
- **LangChain / LangGraph agentide majutamine Microsoft Foundry’s** — Uus sektsioon failis [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) ja käivitatav näidis [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), mis kasutab `langchain-azure-ai[hosting]` ja `ResponsesHostServer`it (`/responses` protokoll), põhineb [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Uus sektsioon "Reaalmaailma näide: Microsoft Project Opal" failis [15-browser-use/README.md](./15-browser-use/README.md), mis käsitleb Opalit ettevõtte arvutikasutuse agendina ja seob kursuse mõistetega (inimene silmus, usaldus/turvalisus, planeerimine, oskused).
- **Teine õppetunni 02 Python näidis** — Lisatud [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (võrdle "Muudetud" – migreeritud varasemast Semantic Kernel märkmikust) ja lingitud õppetunni README-s.
- Lisatud jaotis "Mudelite ja pakkujate" kohta failis [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Muudetud

- **Vestlusvalmidused → Responses API (Python).** Näited, mis kutsusid mudelit otse, viidi Chat Completions’ist üle Responses API kasutusse (`client.responses.create(input=..., store=False)`, `resp.output_text`), kasutades `OpenAI` klienti stabiilses Azure OpenAI `/openai/v1/` lõpp-punktis (ilma `api_version`ita). Mõjutatud näited on:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — täielik funktsioonikõne käik (tööriista skeem teisendatud Responses formaati, tööriista tulemused tagastatud kui `function_call_output`, `max_output_tokens`, jmt).
- **GitHub Models → Azure OpenAI.** GitHub Models on aegunud (lõpetamine **juulis 2026**) ega toeta Responses API-d. Kõik GitHub Modelsi koodirajad konverteeriti Azure OpenAI / Microsoft Foundry’le nii Python kui .NET näidetes:
  - Python: Õppetunni 08 töövoo märkmikud (`01`–`03`), õppetund 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + kaasnevad `.md` dokumendid, ning õppetunni 08 dotNET töövoo märkmikud/`.md` (`01`–`03`) kasutavad nüüd `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` koos `AzureCliCredential`-ga.
- **Semantic Kernel → Microsoft Agent Framework.** Varasem `02-semantic-kernel.ipynb` kirjutati ümber kasutamaks Microsoft Agent Frameworki Azure OpenAI (Responses API) toel ning nimetati ümber `02-python-agent-framework-azure-openai.ipynb`-ks.
- **Standardiseeritud kasutamine `FoundryChatClient` + `as_agent`.** README ja märkmikukoodid, mis viitasid `AzureAIProjectAgentProvider`ile, standardiseeriti kanonilisele mustrile, mida kasutas õppetund 01 ja raamistik ise: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` koos `provider.as_agent(...)`. Uuendatud õppetundide 02–14 README-d ja märkmikud (nt õppetund 13 mälu, kõik õppetund 14 märkmikud, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Toote nimetamine.** Ümber nimetatud kogu ingliskeelses sisus:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Muutmata: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" ja keskkonnamuutujate nimed.)
- **Sõltuvused** ([requirements.txt](../../requirements.txt)):
  - Kindlaksmääratud `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Kindlaksmääratud `openai>=1.108.1` (minimaalne Responses API jaoks).
  - Eemaldatud `azure-ai-inference` (kasutati vaid migreeritud GitHub Modelsi näidetes).
- **Keskkonna konfiguratsioon** ([.env.example](../../.env.example)): eemaldatud GitHub Modelsi muutujad (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); lisatud `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` ja valikuline `AZURE_OPENAI_API_KEY`; uuendatud nimetamist Microsoft Foundry järgi.
- **Dokumentatsioon** — Uuendatud [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) ja [STUDY_GUIDE.md](./STUDY_GUIDE.md) vastavalt ülaltoodule (keskkonnamuutujate seadistamine, valideerimise näide, pakkuja juhised, nimetused).

### Eemaldatud

- GitHub Modelsi kasutamise sammud ja keskkonnamuutujad seadistusdokumentidest (asendatud Azure OpenAI / Microsoft Foundry poolt).

### Turvalisus / Privaatsus (avaliku jagamise korrastamine)

- Kustutatud Jupyter märkmike täitmismärgid, mis lekkisid reaalse **Azure tellimuse ID**, ressursigrupi / ressursi nimed ja Bing ühenduse ID, samuti arendaja **kohalikud failiteed ja kasutajanimed**, failides:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Kontrollitud, et jälgitavas ingliskeelses sisus puuduvad API-võtmed, tokenid, tellimuse ID-d või isiklikud failiteed (jäävad olevad `GITHUB_TOKEN` viited on GitHub Actions token töövoogudes ja GitHub MCP serveri PAT 11. õppetunni seadistuses — mõlemad on seaduslikud ja GitHubi mudelitest eraldiseisvad).

### Märkused ja teadaolevad piirangud

- **Ei ole käivitatud/kompileeritud.** Need on hariduslikud näited, mis on uuendatud API/ nimetamise korrektsuse tarbeks; neid ei käideldud otse Azure'i ressurssidega ning .NET näiteid ei kompileeritud selles keskkonnas. Kontrolli oma Microsoft Foundry / Azure OpenAI keskkonnas.
- **Mudeli juurutus peab toetama Responses API-t.** Kasuta juurutust nagu `gpt-4.1-mini`, `gpt-4.1` või mõnda `gpt-5.x` mudelit. Vanemad mudelid toetavad põhifunktsionaalsust, kuid mitte kõiki võimalusi.
- **Agent-raamistiku versioon.** Näited on suunatud uusimale MAF-ile (`>=1.10.0`). Kanoniline agendi loomise kutsung on `client.as_agent(...)`; API-d kontrolliti raamatu avaldatud dokumentatsiooni ja paigaldatud versiooni põhjal. Kui lukustad teise versiooni, veendu meetodi olemasolus (`as_agent` vs `create_agent`).
- **8. õppetunni töövoo märkmik 04** hoiab teadlikult `AzureAIAgentClient` (moodulist `agent-framework-azure-ai`), kuna see kasutab Microsoft Foundry Agent Service'i hostitud tööriistu (Bing võttealus, koodi interpreteerija); see on juba Responses-põhine.
- **.NET vaikimisi juurutus.** Kaks 8. õppetunni dotNET töövoo näidet kasutasid varem otse määratud konkreetset mudelit; nüüd on vaikimisi `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Kui näide sõltub multimodaalsest/visuaalsest sisendist, seadista `AZURE_OPENAI_DEPLOYMENT` sobivale mudelile.
- **Foundry Local** pakub OpenAI ühilduvat **Chat Completions** lõpp-punkti ja on mõeldud kohalikuks arenduseks; kogu Responses API funktsionaalsuse jaoks kasuta Azure OpenAI-d / Microsoft Foundryt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->