#చేంజ్లాగ్

**AI Agents for Beginners** కోర్సుకు సంబంధించిన అన్ని ముఖ్యమైన మార్పులు ఈ ఫైల్‌లో నమోదు చేయబడ్డాయి.

## [విడుదలను పొందలేదు] — 2026-07-06

ఈ రిలీజ్ కోర్సును **Azure OpenAI Responses API** కి మైగ్రేట్ చేస్తుంది, **Microsoft Foundry** మరియు **Microsoft Agent Framework (MAF)**పై ఉత్పత్తి పేరుమార్పులను సమీకరించి, GitHub మోడల్స్‌ను రిటైర్ చేసి, SDK సంస్కరణలను అప్డేట్ చేస్తుంది మరియు లోకల్ మోడల్స్ మరియు Foundryలో ఇతర ఫ్రేమ్‌వర్క్‌లను హోస్ట్ చేయడం గురించి కొత్త విషయాలను జోడిస్తుంది.

### జోడించబడింది

- **మైగ్రేషన్ స్కిల్స్** — `.agents/skills/` లో [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) ఏజెంట్ స్కిల్ ఇన్‌స్టాల్ చేయడం ([Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses) నుండి), దాని రిఫరెన్సులు మరియు స్కానర్ స్క్రిప్ట్‌తో సహా.
- **Foundry Local (పరికరంపై మోడల్స్‌ని నడపడం)** — [00-course-setup/README.md](./00-course-setup/README.md) లో కొత్త "Alternative Provider: Foundry Local" సెక్షన్, ఇన్‌స్టాల్ (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, మరియు Microsoft Agent Framework కి `OpenAIChatClient` ద్వారా `FoundryLocalManager` ను వేయడం.
- **Microsoft Foundryలో LangChain / LangGraph ఏజెంట్స్ హోస్టింగ్** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md)లో కొత్త సెక్షన్ మరియు `langchain-azure-ai[hosting]` మరియు `ResponsesHostServer` ("/responses" ప్రోటోకాల్) ఉపయోగించి ఒక రన్నబుల్ సాంపిల్ [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) ఆధారంగా.
- **Microsoft ప్రాజెక్ట్ Opal** — [15-browser-use/README.md](./15-browser-use/README.md)లో కొత్త "రియల్-వరల్డ్ ఉదాహరణ: Microsoft ప్రాజెక్ట్ Opal" సెక్షన్, Opal ను ఒక ఎంటర్‌ప్రైజ్ కంప్యూటర్-ఉపయోగ ఏజెంట్‌గా ఫ్రేమ్ చేసి, కోర్సు కాన్సెప్ట్స్‌తో (మానవ-లోప్, ట్రస్టు/సెక్యూరిటీ, ప్లానింగ్, స్కిల్స్) మ్యాప్ చేస్తుంది.
- **రెండవ పాఠం 02 Python సాంపిల్** — [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) జోడించింది (మార్పులైనవి క్రింద "Changed" లో చూడండి — మునుపటి Semantic Kernel నోటుబుక్ నుండి మైగ్రేట్ అయింది) మరియు పాఠం README లో లింక్ చేసింది.
- [STUDY_GUIDE.md](./STUDY_GUIDE.md) లో **మోడల్స్ మరియు ప్రొవైడర్స్** సెక్షన్ జోడించబడింది.

### మార్పులు

- **Chat Completions → Responses API (Python).** మోడల్‌ను సిడిచటగా పిలిచే నమూనాలను Chat Completions నుండి Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`) కి మార్పు చేయబడింది, స్థిరమైన Azure OpenAI `/openai/v1/` ఎండ్‌పాయింట్ (ఏ `api_version` లేకుండా) వ్యతిరేకంగా `OpenAI` క్లయింట్ ఉపయోగించి. ప్రభావిత నమూనాలు ఉన్నాయి:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — పూర్తి ఫంక్షన్-కాల్ వాక్‌త్రూ (టూల్ స్కీమాను Responses ఫార్మాట్‌గా ఫ్లాట్ చేయడం, టూల్ ఫలితాలను `function_call_output`, `max_output_tokens` మొదలైనవి రూపంలో రాబట్టడం).
- **GitHub Models → Azure OpenAI.** GitHub Models పాతది కావడంతో (జూలై 2026లో రిటైర్ అవుతోంది) మరియు Responses APIకు మద్దతు ఇవ్వదని అందువల్ల అన్ని GitHub Models కోడ్ మార్గాలను Python మరియు .NET నమూనాల్లో Azure OpenAI / Microsoft Foundryకి మార్చారు:
  - Python: పాఠం 08 వర్క్‌ఫ్లో నోటుబుక్స్ (`01`–`03`), పాఠం 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + సహచర `.md` డాక్స్, మరియు పాఠం 08 dotNET వర్క్‌ఫ్లో నోటుబుక్స్/`.md` (`01`–`03`) ఇప్పుడు `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` మరియు `AzureCliCredential` ఉపయోగిస్తుంది.
- **Semantic Kernel → Microsoft Agent Framework.** మునుపటి `02-semantic-kernel.ipynb`ను Microsoft Agent Frameworkతో Azure OpenAI (Responses API) ఉపయోగించి తిరిగి రాశారు మరియు పేరు మార్చి `02-python-agent-framework-azure-openai.ipynb` చేశారు.
- **`FoundryChatClient` + `as_agent` ను ప్రమాణీకరించారు.** README మరియు నోటుబుక్ కోడ్ లో `AzureAIProjectAgentProvider` కు సంబంధించినవి పోగొట్టకుండా Lesson 01 మరియు ఫ్రేమ్‌వర్క్ స్వంత నమూనాలు ఉపయోగించే కానానికల్ ప్యాటర్న్ `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` మరియు `provider.as_agent(...)`గా పూర్తి చేశారు. Lesson 02–14 READMEs మరియు నోటుబుక్స్ లో అప్డేట్ చేయబడింది (ఉదాహరణకు, పాఠం 13 మెమొరీ, అన్ని పాఠం 14 నోటుబుక్స్, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **ఉత్పత్తి పేరు పరివర్తన.** అన్ని ఆంగ్ల విషయాలలో పేరు మార్చారు:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (మార్పు లేదు: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", మరియు పరిసర-శ్రేణి పేర్లు.)
- **ఆధారాలు** ([requirements.txt](../../requirements.txt)):
  - `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0` ను పిన్ చేశారు.
  - Responses API కొరకు కనీసంగా `openai>=1.108.1` ను పిన్ చేశారు.
  - `azure-ai-inference` తొలగించారు (గతంలో GitHub Models నమూనాల్లో మాత్రమే ఉపయోగించబడింది).
- **పర్యావరణ కాన్ఫిగరేషన్** ([.env.example](../../.env.example)): GitHub Models వేరియబుల్స్ (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) తొలగించారు; `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, మరియు ఐచ్ఛిక `AZURE_OPENAI_API_KEY` జోడించారు; పేరుమార్పులు Microsoft Foundry ప్రక్కన ఉన్నవి.
- **డాక్యుమెంట్లు** — పై అంశాలకు అనుగుణంగా [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), మరియు [STUDY_GUIDE.md](./STUDY_GUIDE.md) నవీకరించారు (సెట్టప్ env vars, ధృవీకరణ కోడ్, ప్రొవైడర్ మార్గదర్శకం, పేరు పరివర్తన).

### తొలగింపబడింది

- GitHub Models ఆన్‌బోర్డింగ్ దశలు మరియు పర్యావరణ వేరియబుల్స్ సెట్టప్ డాక్స్ నుండి తొలగించబడ్డాయి (Azure OpenAI / Microsoft Foundryతో ఉపసంహరించబడ్డాయి).

### భద్రత / గోప్యత (పబ్లిక్-షేరింగ్ శుభ్రపరచడం)

- నిజమైన **Azure సబ్స్క్రిప్షన్ ID**, రీసోర్స్-గ్రూపు / రీసోర్స్ పేర్లు, Bing కనెక్షన్ ID, మరియు డెవలపర్ **లోకల్ ఫైల్ పాత్‌లు మరియు యూజర్‌నేమ్స్** ఉన్న Jupyter నోటుబుక్ ఎగ్జిక్యూషన్ అవుట్పుట్‌లను తొలగించారు:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- ట్రాక్ చేయబడిన ఆంగ్ల విషయాల్లో ఏ API కీలు, టోకెన్లు, సబ్స్క్రిప్షన్ IDలు లేదా వ్యక్తిగత పాత్‌లు లేవని నిర్ధారించారు (`GITHUB_TOKEN` రిఫరెన్సులు వర్క్‌ఫ్లోలో GitHub Actions టోకెన్ మరియు Lesson 11 సెట్టప్‌లో GitHub MCP సర్వర్ PAT మాత్రమే ఉన్నాయి — ఇవి చెల్లుబాటుగా మరియు GitHub Modelsకి సంబంధం లేనివి).

### నోట్స్ మరియు తెలిసిన పరిమితులు

- **పనిచేయలేదు / కాంపైల్ చేయలేదు.** ఇవి API / పేరుమార్పు సరిదిద్దిన విద్యా నమూనాలు; లైవ్ Azure వనరులపై నడపబడలేదు, .NET నమూనాలు ఈ వాతావరణంలో కాంపైల్ చేయబడలేదు. మీ స్వంత Microsoft Foundry / Azure OpenAI డిప్లాయ్‌మెంట్‌తో పరీక్షించండి.
- **మోడల్ డిప్లాయ్‌మెంట్ Responses APIకు మద్దతు ఇవ్వాలి.** `gpt-4o-mini`, `gpt-4.1`, లేదా `gpt-5.x` మోడల్ వంటివి ఉపయోగించండి. పాత మోడల్స్ Responses API యొక్క ముఖ్య ఫంక్షనల్‌ను మద్దతు ఇస్తాయి కానీ ప్రతి ఫీచర్‌కు కాదు.
- **ఏజెంట్-ఫ్రేమ్‌వర్క్ సంస్కరణ.** ఉదాహరణలు లేటెస్ట్ MAF (`>=1.10.0`) టార్గెట్ చేస్తాయి. ప్రామాణిక ఏజెంట్ సృష్టి కాల్ `client.as_agent(...)`; APIs ఫ్రేమ్‌వర్క్ ప్రచురించిన డాక్యుమెంట్ల మరియు ఇన్స్టాల్ చేసిన బిల్డ్‌తో తనిఖీ చేయబడ్డాయి. మీరు వేరే సంస్కరణ పిన్ చేస్తే, పద్ధతి అందుబాటులో ఉందా లేదా అని నిర్ధారించండి (`as_agent` vs `create_agent`).
- **పాఠం 08 వర్క్‌ఫ్లో నోటుబుక్ 04** ఉద్దేశపూర్వకంగా `AzureAIAgentClient` (agent-framework-azure-ai నుండి) ఉంచింది ఎందుకంటే అది Microsoft Foundry Agent Serviceలో హోస్టై చేసిన టూల్స్ (Bing గ్రౌండింగ్, కోడ్ ఇంటర్‌ప్రెటర్) ఉపయోగిస్తుంది; ఇది ఇప్పటికే Responses ఆధారితంగా ఉంది.
- **.NET డిఫాల్ట్ డిప్లాయ్‌మెంట్.** రెండు పాఠం 08 dotNET వర్క్‌ఫ్లో నమూనాలు మునుపెప్పుడు `gpt-4o`ను హార్డ్-కోడ్ చేశాయి; ఇప్పుడు అవి డిఫాల్ట్‌గా `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`) ఉపయోగిస్తాయి. ఒక నమూనా మల్టిమోడల్/విజన్ ఇన్‌పుట్‌పై ఆధారపడితే, `AZURE_OPENAI_DEPLOYMENT` ను తగిన మోడల్‌కు సెట్ చేయండి.
- **Foundry Local** ఓపెన్‌ఏఆర్-పరిచయమైన **Chat Completions** ఎండ్‌పాయింట్‌ను ఎక్స్‌పోజ్ చేస్తుంది మరియు లోకల్ అభివృద్ధికి ఉద్దేశించబడింది; పూర్తి Responses API ఫీచర్ సెట్ కొరకు Azure OpenAI / Microsoft Foundry వినియోగించండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->