# Mabadiliko ya Taarifa

Mabadiliko yote muhimu kwa kozi ya **Wakala wa AI kwa Waanzilishi** yameandikwa katika faili hii.

## [Imetolewa] — 2026-07-14

Toleo hili linaondoa kozi kwenye mifano miwili iliyopigwa marufuku hivi karibuni, linahamisha daftari za Masomo zilizobaki kwa API thabiti ya Microsoft Agent Framework, na linathibitisha daftari za Python dhidi ya utekelezaji wa moja kwa moja wa Microsoft Foundry.

### Imebadilishwa

- **Imehamishwa kutoka kwa mifano iliyopigwa marufuku (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** `gpt-4.1` na `gpt-4.1-mini` zote sasa ni zilizopigwa marufuku (tarehe rasmi ya kuachishwa ni **14 Oktoba 2026**). Kila rejeleo la kozi (nyaraka, `.env.example`, daftari za Python/.NET na mifano) zilibadilishwa na `gpt-5-mini` isiyo na marufuku. Mfano wa kugawanya modeli wa Somo la 16 unatumia utofauti wa ukubwa mdogo/kubwa kwa kutumia `gpt-5-nano` (mdogo) na `gpt-5-mini` (kubwa). Faili za watu wa tatu zilizohifadhiwa ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), maandishi ya kihistoria ya GitHub Models, na maelezo ya uwezo wa ujuzi `azure-openai-to-responses` zilibaki vile vile kwa makusudi.
- **Daftari la kuhamisha la Somo la 14 limehamishwa kwa API thabiti.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) sasa linatumia `agent_framework.orchestrations.HandoffBuilder` na `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, uelekezaji wa kutiririsha wa `event.type`, na `FoundryChatClient` (kubadilisha alama za awali kabla ya 1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` zilizotolewa).
- **Daftari la mwanadamu-mkondo wa Somo la 14 limehamishwa kwa API thabiti.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) sasa linasitisha kwa kutumia `ctx.request_info(...)` + `@response_handler` (kubadilisha `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` zilizotolewa), linasanifu kwa `WorkflowBuilder(start_executor=..., output_executors=[...])`, linaendesha matokeo yaliyoandaliwa kupitia `default_options={"response_format": ...}`, na linatumia jibu lililoandikwa ili daftari lihaririki bila kuingiliwa (hakuna `input()` inayozuia).
- **Usanifu wa mazingira** ([.env.example](../../.env.example)): majina ya utekelezaji wa modeli yamebadilishwa kuwa `gpt-5-mini`; imeongeza `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (marudio ya Somo la 16) na `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` iliyokosekana awali (matumizi ya kivinjari ya Somo la 15).
- **Mategemeo** ([requirements.txt](../../requirements.txt)): `agent-framework`, `agent-framework-foundry`, na `agent-framework-openai` zimesimamiwa kwa toleo `~=1.10.0` kwa seti inayojitegemea yenye uthibitisho (1.11.0 inaleta mabadiliko ya majaribio yanayovunja sehemu zinazotumika kwenye masomo haya).

### Vidokezo na vikwazo vinavyojulikana

- **Imethibitishwa dhidi ya Microsoft Foundry ya moja kwa moja.** Daftari za Python zilitendaji bila kichwa kwa kutumia `nbconvert` dhidi ya mradi wa Microsoft Foundry wakitumia `gpt-5-mini` (na `gpt-5-nano` kwa marudio ya Somo la 16). Tekeleza mifano sawa isiyo na marufuku kwenye mradi wako mwenyewe; daftari husoma jina la utekelezaji kutoka `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Bado inahitaji rasilimali za ziada kwa baadhi ya masomo.** Somo la 05 linahitaji Azure AI Search; mtiririko wa Somo la 08 Bing-grounding (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) unahitaji muunganisho wa Bing na zana zilizo hifadhiwa na Huduma ya Wakala wa Microsoft Foundry; Somo la 13 (Cognee) na Somo la 17 (Foundry Local) zinahitaji runtime zao wenyewe.

## [Imetolewa] — 2026-07-13

Toleo hili linaongeza masomo mawili mapya yanayokamilisha mzunguko wa utekelezaji — kupanua mawakala hadi Microsoft Foundry na kushusha hadi kwenye stesheni moja ya kazi — pamoja na bomba la kipimo cha moshi, urambazaji wa kozi uliosasishwa, ujuzi mpya za mwanafunzi, na chapa iliyosasishwa.

### Imeongezwa

- **Somo la 16 — Kuweka Wakili Walio Panuka kwa Microsoft Foundry.** Somo jipya [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) na daftari inayoweza kuendeshwa [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) inayojenga wakili wa huduma kwa wateja wa viwandani (zana, RAG, kumbukumbu, uelekezaji wa modeli, kuhifadhi majibu, idhini ya binadamu, mlango wa tathmini, na ufuatiliaji wa OpenTelemetry), na michoro ya maendeleo/utekelezaji/runtime ya Mermaid, mtihani wa maarifa, kazi, na changamoto.
- **Somo la 17 — Kuunda Wakala wa AI wa Kijiji kwa kutumia Foundry Local na Qwen.** Somo jipya [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) na daftari [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) inayojenga msaidizi wa uhandisi anayefanya kazi kabisa kifaa (kuitisha kazi ya Qwen kupitia Foundry Local, zana za faili zilizo chini ya kifaa, RAG ya eneo na Chroma, MCP ya eneo hiari), yenye michoro ya eneo tu / RAG ya eneo / kuitisha zana, mtihani wa maarifa, kazi, na changamoto.
- **Bomba la kipimo cha moshi.** Mtiririko mpya wa [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) pamoja na katalogi kwa kila somo chini ya [tests/](./tests/README.md) kwa mawakala wanaoweza kupelekwa katika Masomo 01, 04, 05, na 16, ikiwa na README ya kiashiria ambayo inaunganisha kila katalogi kwa somo lake na jina la wakili aliyehifadhiwa. Somo la 16 linapata sehemu ya "Kuthibitisha Wakili Uliowekwa kwa Vipimo vya Moshi"; Masomo 01/04/05 yanapata kidokezo cha kipimo cha moshi kinachoweza kuchaguliwa.
- **Ujuzi wa mwanafunzi.** Ujuzi mpya wa Wakala chini ya `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (kufunga mwongozo wa Masomo 16 na 17), na [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (jinsi ya kuthibitisha mifano ya daftari dhidi ya Microsoft Foundry/Mshtuko wa Azure OpenAI wa moja kwa moja).
- **Mtendaji wa uthibitishaji wa daftari.** Mpya [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) inayotekeleza kila daftari la Python bila kichwa kwa kutumia `nbconvert` na kuchapisha matokeo ya PASS/FAIL (pamoja na `results.json`). Hutatua chombo cha mizizi cha repo na Python, hutenganisha daftari zisizo za kozi (`.venv`, `site-packages`, `translations`, mali za template za ujuzi) na daftari za `.NET` kwa chaguo-msingi, na ina msaada wa `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, na `-Python`.
- **Urambazaji wa kozi.** Imeongeza viungo vya Somo lililopita/lijalo kwa Masomo 11–15 (ambayo awali hazikutumika) ili kozi nzima iwe mlolongo kutoka 00 → 18 kwa mwelekeo yote miwili.
- **Vichapishaji vipya.** Vichapishaji vya masomo 16 na 17, pamoja na picha mpya ya kijamii ya hazina [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (sasa ikitangaza masomo mawili mapya na URL ya `aka.ms/ai-agents-beginners`).
- **Mategemeo** ([requirements.txt](../../requirements.txt)): imeongeza `foundry-local-sdk` na `chromadb` kwa Somo la 17.

### Imebadilishwa

- Meza kuu ya somo [README.md](./README.md): Masomo 16 na 17 sasa yanahusiana na maudhui yao (awali "Inakuja Hivi Karibuni"); picha ya hazina imesasishwa kuwa `repo-thumbnailv3.png`.
- [STUDY_GUIDE.md](./STUDY_GUIDE.md): iliongeza Masomo 16 na 17 kwenye mwongozo wa somo kwa somo na njia za kujifunza, na sehemu ya "Kuthibitisha mawakala waliowekwa kwa Vipimo vya Moshi".
- [AGENTS.md](./AGENTS.md): imesasisha hesabu/maelezo ya somo (00–18), iliongeza sehemu ya uthibitisho wa kipimo cha moshi, na kuongeza mifano ya majina ya Somo la 16/17.
- [18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md): "Somo lililopita" sasa linaelekeza kwenye Somo la 17 (awali lilikuwa Somo la 15), likifunga mlolongo.
- Marejeleo ya modeli yamefaulu kwenye mifano isiyo na marufuku. Badilisha yote `gpt-4o` / `gpt-4o-mini` katika kozi (nyaraka, `.env.example`, daftari za Python/.NET na mifano) na `gpt-4.1-mini` — `gpt-4o` (tofauti zote) inakumbuka kutolewa mnamo 2026. Mfano wa uelekezaji wa modeli wa Somo la 16 unahifadhi tofauti ya mdogo/kubwa kwa kutumia `gpt-4.1-mini` (mdogo) na `gpt-4.1` (kubwa). Daftari za Python sasa huchagua modeli kutoka kwa vigezo vya mazingira (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) badala ya kuweka jina la modeli moja kwa moja.

### Vidokezo na vikwazo vinavyojulikana

- **Haijatendeka dhidi ya Azure ya moja kwa moja.** Daftari za masomo mapya ni sampuli za kielimu; endesha na thibitisha dhidi ya mipangilio yako ya Microsoft Foundry / Foundry Local. Mtiririko wa kipimo cha moshi unahitaji wewe kueneza wakili wa somo na kusanidi siri za Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) ukiwa na nafasi ya **Azure AI User** katika mipaka ya mradi wa Foundry.
- **Somo la 17 ni la eneo tu.** Halina sehemu ya Majibu ya Foundry, kwa hiyo kitendo cha kipimo cha moshi hakihusiki; thibitisha kwa kuendesha daftari katika stesheni yako ya kazi.

## [Imetolewa] — 2026-07-06

Toleo hili linahamisha kozi hadi **Azure OpenAI Responses API**, linaweka jina la bidhaa rasmi kwa **Microsoft Foundry** na **Microsoft Agent Framework (MAF)**, linaachisha GitHub Models, linasasisha matoleo ya SDK, na linaongeza maudhui mapya juu ya mifano ya eneo na kuendesha mifumo mingine kwenye Foundry.

### Imeongezwa

- **Ujuzi wa uhamishaji** — Imajiwa Ujuzi wa Wakala [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (kutoka [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) chini ya `.agents/skills/`, pamoja na rejeleo na skripti ya skana.
- **Foundry Local (kimbia mifano kifaa kwa kifaa)** — Sehemu mpya "Mtoa Mbadala: Foundry Local" katika [00-course-setup/README.md](./00-course-setup/README.md) inajumuisha usakinishaji (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, na kuunganisha `FoundryLocalManager` na Microsoft Agent Framework kupitia `OpenAIChatClient`.
- **Hudumia mawakala wa LangChain / LangGraph kwenye Microsoft Foundry** — Sehemu mpya katika [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) pamoja na sampuli inayoweza kutekelezwa [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) inayotumia `langchain-azure-ai[hosting]` na `ResponsesHostServer` (itifaki ya `/responses`), kulingana na [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Sehemu mpya "Mfano Halisi: Microsoft Project Opal" katika [15-browser-use/README.md](./15-browser-use/README.md) ikifafanua Opal kama wakili wa matumizi ya kompyuta kielimu na kuhusisha na dhana za kozi (binadamu-mkondo, uaminifu/usalama, upangaji, Ujuzi).
- **Sampuli ya pili ya Python ya Somo la 02** — Imeongeza [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (angalia "Imebadilishwa" — ilihamishwa kutoka daftari la Semantic Kernel la zamani) na kuunganishwa katika README ya somo.
- Sehemu ya Mifano na Watoa Huduma imeongezwa katika [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Imebadilishwa

- **Chat Completions → Responses API (Python).** Sampuli zilizoita moja kwa moja modeli zimehamishwa kutoka Chat Completions kwenda Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), zikitumia mteja wa `OpenAI` dhidi ya kiunganishi thabiti cha Azure OpenAI `/openai/v1/` (bila `api_version`). Sampuli zilizoathirika ni:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — mwongozo mzima wa kuitisha kazi (schema ya zana iliyopondwa hadi muundo wa Responses, matokeo ya zana yakirudishwa kama `function_call_output`, `max_output_tokens`, n.k.).

- **Mifano ya GitHub → Azure OpenAI.** Mifano ya GitHub imeachwa rasmi (itaondolewa **Julai 2026**) na haitegemezi API ya Majibu. Njia zote za msimbo wa Mifano ya GitHub zilibadilishwa kuwa Azure OpenAI / Microsoft Foundry katika mifano ya Python na .NET:
  - Python: Daftari za mtiririko wa kazi wa Somo la 08 (`01`–`03`), Somo la 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + nyaraka za companion `.md`, na daftari za mtiririko wa kazi wa Somo la 08 dotNET/`.md` (`01`–`03`) sasa zinatumia `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` na `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Daftari la zamani `02-semantic-kernel.ipynb` lilibadilishwa ili kutumia Microsoft Agent Framework pamoja na Azure OpenAI (API ya Majibu) na kubadilishwa jina kuwa `02-python-agent-framework-azure-openai.ipynb`.
- **Imefikia viwango vilivyo juu kwa kutumia `FoundryChatClient` + `as_agent`.** README na msimbo wa daftari uliotaja `AzureAIProjectAgentProvider` ulipangwa kuwa mtindo wa kawaida uliotumiwa na Somo la 01 na mifano ya mfumo wenyewe: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` na `provider.as_agent(...)`. Imesasishwa katika README na daftari za Somo la 02–14 (mfano, kumbukumbu ya Somo la 13, daftari zote za Somo la 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Majina ya Bidhaa.** Yamebadilishwa katika maudhui yote ya Kiingereza:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Bado ziko sawa: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", na majina ya vitu vya mazingira.)
- **Mtegemezo** ([requirements.txt](../../requirements.txt)):
  - Imefungwa `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Imefungwa `openai>=1.108.1` (chini kabisa kwa API ya Majibu).
  - Kuondolewa `azure-ai-inference` (ilikuwa ikitumika tu na mifano iliyohamishwa ya Mifano ya GitHub).
- **Mpangilio wa Mazingira** ([.env.example](../../.env.example)): kuondoa vigezo vya Mifano ya GitHub (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); kuongezwa `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, na hiari `AZURE_OPENAI_API_KEY`; kusasisha majina kuwa Microsoft Foundry.
- **Nyaraka** — Imesasishwa [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), na [STUDY_GUIDE.md](./STUDY_GUIDE.md) kwa yale yaliyotajwa hapo juu (kuanzisha vigezo vya mazingira, kipande cha uthibitisho, mwongozo wa mtoa huduma, majina).

### Imeondolewa

- Hatua za kuanzisha Mifano ya GitHub na vigezo vya mazingira kutoka kwa nyaraka za usanidi (zilibadilishwa na Azure OpenAI / Microsoft Foundry).

### Usalama / Faragha (usafi wa kushiriki kwa umma)

- Kuondolewa kwa matokeo ya utekelezaji wa daftari la Jupyter yaliyoonyesha **Kitambulisho halisi cha usajili cha Azure**, majina ya kundi la rasilimali / rasilimali, na kitambulisho cha muunganisho wa Bing, pamoja na **njia za faili za mtaalamu na majina ya watumiaji**, katika:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Thibitisha hakuna funguo za API, tokeni, vitambulisho vya usajili, au njia za kibinafsi zilizobaki katika maudhui ya Kiingereza yaliyojumuishwa (marejeleo ya `GITHUB_TOKEN` yaliyobaki ni tokeni ya GitHub Actions katika mtiririko na PAT ya seva ya GitHub MCP katika usanidi wa Somo la 11 — zote ni halali na zisizo na uhusiano na Mifano ya GitHub).

### Vidokezo na vizuizi vinavyojulikana

- **Haijatekelezwa/kukusanywa.** Hizi ni mifano ya kielimu iliyosasishwa kwa usahihi wa API/majina; hazikutumika kwa rasilimali halisi za Azure, na mifano ya .NET haikukusanywa katika mazingira haya. Hakikisha dhidi ya usambazaji wako wa Microsoft Foundry / Azure OpenAI.
- **Usambazaji wa mfano lazima uunge mkono API ya Majibu.** Tumia usambazaji kama `gpt-4.1-mini`, `gpt-4.1`, au mfano wa `gpt-5.x`. Mifano ya zamani inasaidia vipengele vya msingi vya Majibu lakini si kila kipengele.
- **Toleo la agent-framework.** Mifano inalenga MAF ya hivi karibuni (`>=1.10.0`). Mwito wa ubunifu wa wakala wa kawaida ni `client.as_agent(...)`; API zilithibitishwa dhidi ya nyaraka zilizochapishwa za mfumo na ujenzi uliowekwa. Ikiwa utaweka toleo tofauti, thibitisha upatikanaji wa njia (`as_agent` dhidi ya `create_agent`).
- **Daftari la mtiririko wa Somo la 08 04** linaendelea kutumia `AzureAIAgentClient` (kutoka `agent-framework-azure-ai`) kwa kukusudia kwa sababu linatumia zana za Microsoft Foundry Agent Service zilizo hifadhiwa ( msingi wa Bing, fasiri ya msimbo); tayari linategemea API ya Majibu.
- **Usambazaji wa chaguo-msingi wa .NET.** Sampuli mbili za mtiririko wa kazi za Somo la 08 dotNET awali zilikuwa na mfano maalum umewekwa kwa usahihi; sasa zinatumia chaguo-msingi `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Ikiwa sampuli inategemea pembejeo ya multimodal/maono, weka `AZURE_OPENAI_DEPLOYMENT` kwa mfano unaofaa.
- **Foundry Local** hutoa sehemu ya OpenAI inayolingana na **Chat Completions** na inalenga maendeleo ya ndani; tumia Azure OpenAI / Microsoft Foundry kwa seti kamili ya vipengele vya API ya Majibu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->