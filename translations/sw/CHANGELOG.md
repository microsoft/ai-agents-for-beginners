# Mabadiliko ya Toleo

Mabadiliko yote muhimu katika kozi ya **Maajenti wa AI kwa Waanzilishi** yameandikwa katika faili hii.

## [Bado Hazijatolewa] — 2026-07-06

Toleo hili linahamisha kozi kwa **Azure OpenAI Responses API**, hurekebisha majina ya bidhaa kwenye **Microsoft Foundry** na **Microsoft Agent Framework (MAF)**, linaondoa GitHub Models, linasasisha matoleo ya SDK, na linaongeza maudhui mapya kuhusu mifano ya ndani na kuendesha mifumo mingine kwenye Foundry.

### Imeongezwa

- **Uwezo wa Kuhamisha** — Imesakinishwa Uwezo wa Mwakala [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (kutoka [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) chini ya `.agents/skills/`, pamoja na marejeleo na skripti ya kukagua.
- **Foundry Local (endesha mifano kwenye kifaa)** — Sehemu mpya "Mtoaji Mbadala: Foundry Local" katika [00-course-setup/README.md](./00-course-setup/README.md) ikijumuisha usakinishaji (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, na kuunganisha `FoundryLocalManager` na Microsoft Agent Framework kupitia `OpenAIChatClient`.
- **Kuendesha maajenti wa LangChain / LangGraph kwenye Microsoft Foundry** — Sehemu mpya katika [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) pamoja na mfano unaoweza kuchezwa [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) ukitumia `langchain-azure-ai[hosting]` na `ResponsesHostServer` (itifaki ya `/responses`), msingi wa [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Mradi wa Microsoft Opal** — Sehemu mpya "Mfano Halisi: Mradi wa Microsoft Opal" katika [15-browser-use/README.md](./15-browser-use/README.md) ikimuelezea Opal kama wakala wa matumizi ya kompyuta wa shirika na kuoanisha na dhana za kozi (mwanadamu katikati ya mchakato, uaminifu/usalama, upangaji, Uwezo).
- **Mfano wa Somo la Pili 02 Python** — Imeongezwa [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (tazama "Imebadilika" — kuhamishwa kutoka kwa daftari la Semantic Kernel la awali) na kuunganishwa katika README ya somo.
- Sehemu ya **Mifano na Watoa Huduma** imeongezwa kwenye [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Imebadilika

- **Chat Completions → Responses API (Python).** Mifano iliyoitisha moodeli moja kwa moja ilihamishwa kutoka Chat Completions kwenda Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), ikitumia mteja wa `OpenAI` dhidi ya huduma imara ya Azure OpenAI `/openai/v1/` (hakuna `api_version`). Mifano iliyohusika ni:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — maelekezo kamili ya utumaji wa kazi (muundo wa zana umebadilishwa kwa muundo wa Responses, matokeo ya zana yamerudi kuwa `function_call_output`, `max_output_tokens`, n.k.).
- **GitHub Models → Azure OpenAI.** GitHub Models zimepitwa na wakati (zitafutwa **Julai 2026**) na hazitungi Responses API. Mifumo yote ya msimbo ya GitHub Models ilibadilishwa kwenda Azure OpenAI / Microsoft Foundry kwa mifano ya Python na .NET:
  - Python: Daftari za mtiririko wa Somo la 08 (`01`–`03`), Somo la 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + nyaraka za mwenza `.md`, na daftari za mtiririko wa Somo la 08 dotNET/`.md` (`01`–`03`) sasa zinatumia `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` kwa kutumia `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Daftari la zamani `02-semantic-kernel.ipynb` lilirekebishwa kutumia Microsoft Agent Framework na Azure OpenAI (Responses API) na kubadilishwa jina kuwa `02-python-agent-framework-azure-openai.ipynb`.
- **Hurekebishwa kuwa `FoundryChatClient` + `as_agent`.** README na msimbo wa daftari uliorejelea `AzureAIProjectAgentProvider` umeunganishwa kwenye mfano rasmi ulio tumika na Somo la 01 na mifano ya mfumo: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` kwa kutumia `provider.as_agent(...)`. Imesasishwa katika README na daftari za Somo la 02–14 (k.m., kumbukumbu ya Somo la 13, daftari zote za Somo la 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Majina ya Bidhaa.** Yamebadilishwa katika maudhui yote ya Kiingereza:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Haijabadilika: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", na majina ya mabadiliko ya mazingira.)
- **Mategemeo** ([requirements.txt](../../requirements.txt)):
  - Imesimamiwa `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Imesimamiwa `openai>=1.108.1` (chini kabisa kwa Responses API).
  - Kuondolewa `azure-ai-inference` (ilikuwa ikitumika tu na mifano iliyohamishwa ya GitHub Models).
- **Mazingira ya huduma** ([.env.example](../../.env.example)): kuondolewa kwa mabadiliko ya GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); kuongezwa `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, na chaguo la `AZURE_OPENAI_API_KEY`; kuboreshwa kwa majina hadi Microsoft Foundry.
- **Nyaraka** — Imeboreshwa [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), na [STUDY_GUIDE.md](./STUDY_GUIDE.md) kwa mabadiliko hapo juu (kupanua mabadiliko ya mazingira, kipande cha uhakiki, mwongozo wa mtayarishaji, majina).

### Imeondolewa

- Hatua za kuanzisha GitHub Models na mabadiliko ya mazingira kutoka kwa nyaraka za usanidi (zimebadilishwa na Azure OpenAI / Microsoft Foundry).

### Usalama / Faragha (kusafisha ushirikiano wa umma)

- Imeksafishwa matokeo ya utekelezaji wa daftari za Jupyter yaliyoonyesha **Kitambulisho Halali cha Usajili wa Azure**, majina ya kundi la rasilimali / rasilimali, na kitambulisho cha muunganisho wa Bing, pamoja na njia za faili za eneo na majina ya watumiaji wa wasanidi, katika:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Imethibitishwa kuwa hakuna funguo za API, tokeni, kitambulisho cha usajili, au njia za kibinafsi zilizobaki katika maudhui ya Kiingereza yaliyotazamwa (marejeleo yaliyobaki ya `GITHUB_TOKEN` ni tokeni za GitHub Actions kwenye mtiririko na PAT ya seva ya GitHub MCP katika usanidi wa Somo la 11 — zote halali na hazihusiani na GitHub Models).

### Vidokezo na vizingiti vinavyojulikana

- **Haikutekelezwa/kuunganishwa.** Hivi ni mifano ya kielimu iliyosasishwa kwa usahihi wa API/majina; haikuendeshwa dhidi ya rasilimali za moja kwa moja za Azure, na mifano ya .NET haikuunganishwa katika mazingira haya. Hakikisha dhidi ya usanidi wako wa Microsoft Foundry / Azure OpenAI.
- **Usanidi wa mfano lazima uunge mkono Responses API.** Tumia usanidi kama `gpt-4o-mini`, `gpt-4.1`, au mfano wa `gpt-5.x`. Mifano ya zamani inaunga mkono vipengele vikuu vya Responses lakini si kila kipengele.
- **Toleo la agent-framework.** Mifano inalenga toleo jipya la MAF (`>=1.10.0`). Simu rasmi ya kuunda wakala ni `client.as_agent(...)`; API zilihakikiwa dhidi ya nyaraka zilizochapishwa na mfumo na kifurushi kilichosakinishwa. Ikiwa unaweka toleo tofauti, hakikisha upatikanaji wa njia (`as_agent` dhidi ya `create_agent`).
- **Daftari la mtiririko wa Somo la 08 notebook 04** linaweka makusudi `AzureAIAgentClient` (kutoka `agent-framework-azure-ai`) kwa sababu linatumia zana za huduma za Microsoft Foundry Agent (kuunganishwa kwa Bing, mwelekezi wa msimbo); tayari linatumia Responses.
- **Usanidi wa chaguo-msingi wa .NET.** Mifano miwili ya mtiririko wa Somo la 08 dotNET hapo awali ilikuwa na `gpt-4o` imeshabadilishwa kuwa chaguo-msingi la `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Ikiwa mfano unategemea ingizo la multimodal/maono, weka `AZURE_OPENAI_DEPLOYMENT` kwa mfano unaofaa.
- **Foundry Local** inaonyesha kiunganishi cha Chat Completions kinacholingana na OpenAI na imekusudiwa kwa maendeleo ya eneo; tumia Azure OpenAI / Microsoft Foundry kwa seti kamili ya vipengele vya Responses API.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->