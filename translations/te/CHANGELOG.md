# మార్పుల చార్ట్

**AI Agents for Beginners** కోర్సుకు జరిగిన అన్ని ప్రధాన మార్పులు ఈ ఫైల్లో నమోదు చేయబడ్డాయి.

## [ఫրահాలిక] — 2026-07-13

ఈ విడుదల రెండు కొత్త పాఠాలు జోడిస్తుంది, అవి డిప్లాయ్‌మెంట్ చక్రాన్ని పూర్తి చేస్తాయి — Microsoft Foundryకి ఏజెంట్ల స్కేలింగ్ మరియు ఒక్క వర్క్‌స్టేషన్‌కు డౌన్ చేయడం — ముంబై పరీక్ష పైప్‌లైన్, పునరుద్ధరించబడిన కోర్సు నావిగేషన్, కొత్త అభ్యాసుల నైపుణ్యాలు, మరియు నవీకరింపబడిన బ్రాండ్.

### జోడించబడింది

- **పాఠం 16 — Microsoft Foundryతో స్కేలబుల్ ఏజెంట్లను డిప్లాయ్ చేయడం.** కొత్త పాఠం [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) మరియు అమలుచేయగల నోట్‌బుక్ [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) ఉత్పాదకత కస్టమర్-సపోర్ట్ ఏజెంట్ నిర్మాణం (పరికరాలు, RAG, మేమొరీ, మోడల్ రూటింగ్, స్పందన క్యాచింగ్, మానవ ఆమోదం, మూల్యాంకన గేట్, మరియు OpenTelemetry ట్రేసింగ్), అభివృద్ధి/డిప్లాయ్‌మెంట్/రంటైమ్ Mermaid చిత్రాలు, జ్ఞాన పరీక్ష, అసైన్‌మెంట్, మరియు సవాలు.
- **పాఠం 17 — Foundry Local మరియు Qwenతో స్థానిక AI ఏజెంట్లను సృష్టించడం.** కొత్త పాఠం [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) మరియు నోట్‌బుక్ [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) పూర్తిగా ఆన్-డివైస్ ఇంజనీరింగ్ అసిస్టెంట్ నిర్మించడం (Qwen ఫంక్షన్ కాలింగ్ ద్వారా Foundry Local, సాండ్‌బాక్స్ ఫైల్ పరికరాలు, స్థానిక RAG తో Chroma, ఐచ్ఛిక స్థానిక MCP), స్థానిక-మాత్రం/స్థానిక-RAG/పరికరం కాలింగ్ చిత్రాలతో, జ్ఞాన పరీక్ష, అసైన్‌మెంట్, మరియు సవాలు.
- **స్మోక్-టెస్ట్ పైప్‌లైన్.** కొత్త [AI స్మోక్ టెస్ట్](https://github.com/marketplace/actions/ai-smoke-test) వర్క్‌ఫ్లో [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) మరియు పాఠాలు 01, 04, 05, మరియు 16 లో డిప్లాయే‌బుల్ ఏజెంట్ల కోసం [tests/](./tests/README.md) కేటలాగ్‌లు, ప్రతి కేటలాగ్ తన పాఠం మరియు హోస్టెడ్ ఏజెంట్ పేరుతో సూచించబడింది. పాఠం 16కి "డిప్లాయ్ చేసిన ఏజెంట్‌ను స్మోక్ టెస్టులతో ధృవీకరించడం" శీర్షిక జోడించబడింది; పాఠాలు 01/04/05కి ఐచ్ఛిక స్మోక్-టెస్ట్ సూచిస్తుంది.
- **అభ్యాసుల నైపుణ్యాలు.** కొత్త ఏజెంట్ స్కిల్స్ `.agents/skills/` క్రింద: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (పాఠం 16 మరియు 17 మార్గనిర్దేశకాలను ప్యాకేజింగ్ చేస్తాయి), మరియు [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (Microsoft Foundry / Azure OpenAI సెటప్ తో నేరుగా చెలామణి అయిన నోట్‌బుక్ నమూనాలను ఎలా ధృవీకరించాలి).
- **నోట్‌బుక్ ధృవీకరణ రన్నర్.** కొత్త [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) ఇది ప్రతి Python నోట్‌బుక్‌ను `nbconvert` తో హెడ్లెస్‌గా అమలు చేసి PASS/FAIL మ్యాట్రిక్స్ (మరియు `results.json`) ప్రింట్ చేస్తుంది. ఇది ఆటోమేటిక్‌గా రిపోజిటరీ రూట్ మరియు Python గుర్తిస్తుంది, కోర్సు కాని నోట్‌బుక్‌లు (`.venv`, `site-packages`, `translations`, స్కిల్ టెంప్లేట్ ఆస్తులు) మరియు `.NET` నోట్‌బుక్‌లు డిఫాల్ట్ రీతిలో బయట పెడుతుంది, మరియు `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, మరియు `-Python` ఆప్షన్లను మద్దతు ఇస్తుంది.
- **కోర్సు నావిగేషన్.** పాఠాలు 11–15 లో ముందు/తరువాత పాఠం లింకులు జోడించబడినవి (ముందుగా లేవు) కాబట్టి మొత్తం కోర్స్ 00 → 18 రెండూ దిశల్లోను వరసగా ఉంటుంది.
- **కొత్త థంబ్‌నెయిల్స్.** పాఠాలు 16 మరియు 17 కి థంబ్‌నెయిల్‌లు, మరియు పునరుద్ధరించబడిన రిపోజిటరీ సామాజిక చిత్రం [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (ఇప్పటి రెండు కొత్త పాఠాలు మరియు `aka.ms/ai-agents-beginners` URLను ప్రకటన చేస్తోంది).
- **డిపెండెన్సీలు** ([requirements.txt](../../requirements.txt)): పాఠం 17 కోసం `foundry-local-sdk` మరియు `chromadb` జోడించబడ్డాయి.

### మార్పు

- **ప్రధాన [README.md](./README.md)** పాఠ పట్టిక: పాఠాలు 16 మరియు 17 ఇప్పుడు వాటి కంటెంట్‌కు లింక్ అవుతున్నారు (ముందు "Coming Soon"గా ఉండేవి); రిపోజిటరీ చిత్రం `repo-thumbnailv3.png` కి అప్డేట్ చేయబడింది.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: పాఠం 16 మరియు 17ని పాఠాల వారీ గైడ్ మరియు అభ్యాస మార్గాల్లో జోడించబడింది, మరియు "డిప్లాయ్ చేసిన ఏజెంట్లను స్మోక్ టెస్టులతో ధృవీకరించడం" శీర్షిక.
- **[AGENTS.md](./AGENTS.md)**: పాఠం లెక్క/వివరణను (00–18), స్మోక్-టెస్టింగ్ ధృవీకరణ భాగాన్ని, మరియు పాఠం 16/17 నమూనా పేరు ఉదాహరణలను అప్డేట్ చేయబడింది.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "ముందటి పాఠం" ఇప్పుడు పాఠం 17కి సూచిస్తుంది (ముందు పాఠం 15కి), తుర్మి ముగుస్తోంది.
- **పాత మోడల్లు కాకుండా మోడల్ సూచనలు ఒకే ధోరణిలో చేయబడ్డాయి.** కోర్సులో అన్ని `gpt-4o` / `gpt-4o-mini` సూచనలు `gpt-4.1-mini`తో (docs, `.env.example`, Python/.NET నోట్‌బుక్స్, సింపుల్) మారాయి — `gpt-4o`(అన్ని వెర్షన్లు) 2026లో రిటైర్ అవుతోంది. పాఠం 16కి మోడల్ రూటింగ్ ఉదాహరణ చిన్న/పెద్ద తేడాను `gpt-4.1-mini` (చిన్న) మరియు `gpt-4.1` (పెద్ద)తో చూపుతుంది. Python నోట్‌బుక్స్ ఇప్పుడు హార్డ్-కోడ్ చేసిన మోడల్ పేరు వాడకుండా వాతావరణ వేరియబుల్స్ (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) నుండి మోడల్ ఎంపిక చేస్తాయి.

### సూచనలు మరియు తెలిసిన పరిమితులు

- **లైవ్ Azure పై అమలు చేయబడలేదు.** కొత్త పాఠాల నోట్‌బుక్స్ విద్యార్థుల నమూనాలు; వాటిని మీ స్వంత Microsoft Foundry / Foundry Local సెటప్‌తో అమలు చేసి ధృవీకరించండి. స్మోక్-టెస్ట్ వర్క్‌ఫ్లోలో మీరు పాఠం ఏజెంట్‌ను డిప్లాయ్ చేసి Azure OIDC రహస్యాలు (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) ని Foundry ప్రాజెక్ట్ స్కోప్‌లో **Azure AI User** పాత్రతో కాపాడాలి.
- **పాఠం 17 స్థానికమే.** దీనికి Foundry Responses ఎండ్‌పాయింట్ లేదు కాబట్టి స్మోక్-టెస్ట్ యాక్షన్ వర్తించదు; మీ వర్క్‌స్టేషన్‌పై నోట్‌బుక్ అమలుచేసి ధృవీకరించండి.

## [ఫ្រះాలిక] — 2026-07-06

ఈ విడుదల కోర్సుని **Azure OpenAI Responses API**కి మైగ్రేట్ చేస్తుంది, ఉత్పత్తి పేర్లను **Microsoft Foundry** మరియు **Microsoft Agent Framework (MAF)**పై ప్రమాణీకరించి, GitHub Models‌ను రిటైర్ చేస్తుంది, SDK వెర్షన్లను నవీకరిస్తుంది, మరియు స్థానిక మోడల్స్ మరియు Foundryపై ఇతర ఫ్రేమ్‌వర్క్‌ల హోస్టింగ్ గురించి కొత్త విషయాలు కలుపుతుంది.

### జోడించబడింది

- **మైగ్రేషన్ స్కిల్** — `.agents/skills/` కింద `azure-openai-to-responses` ఏజెంట్ స్కిల్ ఇన్‌స్టాల్ అయింది ([Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses) నుండి), దాని సూచనలు మరియు స్కానర్ స్క్రిప్ట్ తో పాటు.
- **Foundry Local (మోడల్స్‌ను డివైస్‌లో అమలు చేయడం)** — కొత్త "వికల్ప ప్రొవైడర్: Foundry Local" భాగం [00-course-setup/README.md](./00-course-setup/README.md)లో అందించి, ఇన్‌స్టాల్ (winget/brew), `foundry model run`, `foundry-local-sdk`, మరియు Microsoft Agent Framework కు `OpenAIChatClient` ద్వారా FoundryLocalManager ను వైర్ చేయడం.
- **Microsoft Foundry పై LangChain / LangGraph ఏజెంట్లను హోస్టింగ్ చేయడం** — కొత్త భాగం [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md)లో, మరియు అమలుచేయగల నమూనా [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) `langchain-azure-ai[hosting]` మరియు `ResponsesHostServer` ("/responses" ప్రోటోకాల్) ఉపయోగించి, [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) ఆధారంగా.
- **Microsoft Project Opal** — కొత్త "వాస్తవ ప్రపంచ ఉదాహరణ: Microsoft Project Opal" భాగం [15-browser-use/README.md](./15-browser-use/README.md)లో, Opalని ఒక ఎంటర్ప్రైజ్ కంప్యూటర్-ఉపయోగ ఏజెంట్ గా చూపిస్తూ, కోర్సు కాన్సెప్ట్స్ (మానవ-లోప్, భరోసా/భద్రత, ప్రణాళిక, స్కిల్స్)తో సంబంధం చూపిస్తుంది.
- **రెండవ పాఠం 02 Python నమూనా** — [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) జోడించబడింది (మార్పులు చూడండి — మునుపటి Semantic Kernel నోట్‌బుక్ నుండి మైగ్రేట్ అయింది) మరియు పాఠం READMEలో లింక్ చేయబడింది.
- **మోడల్స్ మరియు ప్రొవైడర్లు** భాగం [STUDY_GUIDE.md](./STUDY_GUIDE.md)లో జోడించబడింది.

### మార్పు

- **Chat Completions → Responses API (Python).** మోడల్ నేరుగా పిలిచిన నమూనాలు Chat Completions నుండి Responses APIకి మారిపోయాయి (`client.responses.create(input=..., store=False)`, `resp.output_text`), `OpenAI` క్లయింట్ ఉపయోగించి Azure OpenAI `/openai/v1/` స్థిర ఎండ్‌పాయింట్ (api_version ఎర్రర్ లేకుండా). ప్రభావిత నమూనాలు:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — పూర్తి ఫంక్షన్-కాలింగ్ వాక్‌థ్రూ (tool schemaను Responses ఫార్మాట్‌కు ఫ్లాటెన్ చేసి, tool ఫలితాలను `function_call_output`, `max_output_tokens`, మొదలైనవి ద్వారా తిరిగి ఇచ్చటం).
- **GitHub Models → Azure OpenAI.** GitHub Models రిటైర్ అవుతోంది (2026 జూలైలో), మరియు Responses APIకు మద్దతు ఇవ్వదు. GitHub Models కోడ్ మార్గాలు అన్ని Azure OpenAI / Microsoft Foundryకి మార్చబడ్డాయి Python మరియు .NET నమూనాల్లో:
  - Python: పాఠం 08 వర్క్‌ఫ్లో నోట్‌బుక్స్ (`01`–`03`), పాఠం 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + అనుబంధ `.md` డాక్స్, మరియు పాఠం 08 dotNET వర్క్‌ఫ్లో నోట్‌బుక్స్/`.md` (`01`–`03`) ఇప్పుడు `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` మరియు `AzureCliCredential`తో ఉపయోగిస్తాయి.
- **Semantic Kernel → Microsoft Agent Framework.** పూర్వపు `02-semantic-kernel.ipynb` మళ్ళీ Microsoft Agent Framework తో Azure OpenAI (Responses API) ఉపయోగించి మళ్లీ రాయబడింది మరియు `02-python-agent-framework-azure-openai.ipynb`గా పునःపేర్కొనబడింది.
- **`FoundryChatClient` + `as_agent` పై ప్రమాణీకరణ.** README మరియు నోట్‌బుక్ కోడ్ అందరూ పాఠం 01 మరియు ఫ్రేమ్‌వర్క్ అందర్ నమూనాలకు అనుగుణంగా `AzureAIProjectAgentProvider` జాగా `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` తో `provider.as_agent(...)` ఉపయోగించేందుకు మార్పు చేయబడింది. పాఠాలు 02–14 READMEలు మరియు నోట్‌లో ఈ మార్పు చేయబడినవి (ఉదాహరణకు: పాఠం 13 మేమొరీ, అన్ని పాఠం 14 నోట్‌బుక్స్, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **ఉత్పత్తి పేర్ల మార్పులు.** అన్ని ఇంగ్లీషు కంటెంట్‌లో పేరు మార్చబడింది:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (మార్పు లేదు: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", మరియు వాతావరణ వేరియబుల్స్ పేర్లు.)
- **డిపెండెన్సీలు** ([requirements.txt](../../requirements.txt)):
  - `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`ని బిగ్చేశారు.
  - Responses APIకి కనీసం అవసరమైన `openai>=1.108.1`.
  - GitHub Models నమూనాలు మాత్రమే వాడుకున్న `azure-ai-inference` తొలగించబడింది.
- **పరిసర అమరిక** ([.env.example](../../.env.example)): GitHub Models వేరియబుల్స్ (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) తీసివేయబడ్డాయి; `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, మరియు ఐచ్ఛికంగా `AZURE_OPENAI_API_KEY` జోడించబడ్డాయి; Microsoft Foundry పేర్లతో అప్డేట్ చేయబడింది.
- **డాక్స్** — ఇంతకు ముందు భాగాలు అప్‌డేట్ చేయబడ్డాయి [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), మరియు [STUDY_GUIDE.md](./STUDY_GUIDE.md) (సెట్టప్ env వేరియబుళ్లు, ధృవీకరణ స్నిపెట్, ప్రొవైడర్ మార్గదర్శకం, పేర్లు).

### తొలగించబడింది

- GitHub Models ఆన్‌బోర్డింగ్ దశలు మరియు వాతావరణ వేరియబుల్స్ సెట్-అప్ డాక్స్ నుండి (Azure OpenAI / Microsoft Foundry చేత మార్చబడ్డాయి).

### భద్రత / గోప్యత (పబ్లిక్-షేరింగ్ శుభ్రపరచడం)

- నిజమైన **Azure Subscription ID**, రిసోర్స్ గ్రూప్ / రిసోర్స్ పేర్లు, Bing కనెక్షన్ ID, మరియు అభివృద్ధి చేసేవారి **స్థానిక ఫైల్ మార్గాలు మరియు యూజర్ పేర్లు** లీకైన Jupyter నోట్‌బుక్ ఎగ్జిక్యూషన్ అవుట్పుట్‌లను తీసివేశారు, ఆ ఫైళ్ళలో:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- ట్రాక్ చేయబడిన ఆంగ్ల విషయం లో ఏ API కీలు, టోకెన్లు, సబ్స్క్రిప్షన్ IDలు, లేదా వ్యక్తిగత మార్గాలు ఉండకూడదని ధృవీకరించారు (`GITHUB_TOKEN` సూచనలు గిట్హబ్ పంథాల్లో గిట్హబ్ ఆక్షన్స్ టోకెన్ మరియు లెషన్ 11 సెటప్ లో గిట్హబ్ MCP సర్వర్ PAT మాత్రమే ఉన్నాయి — ఇది సరైనవి మరియు గిట్హబ్ మోడల్స్కు సంబంధించని వాటి).

### గమనికలు మరియు తెలిసిన పరిమితులు

- **ప్రయోగం చేయలేదు/కంపైల్ చేయలేదు.** ఇవి API/పేరుమార్పు సరిచెక్కింపులకు సరిగ్గా నవీకరించిన విద్యా నమూనాలు; ఇవి ప్రత్యక్ష Azure వనరుల మీద నడపలేదు, మరియు .NET నమూనాలు ఈ వాతావరణంలో కంపైల్ చేయబడలేదు. మీ స్వంత Microsoft Foundry / Azure OpenAI నియామకం మీద ధృవీకరించండి.
- **మోడల్ నియామకం Responses APIకి మద్దతు ఇవ్వాలి.** `gpt-4.1-mini`, `gpt-4.1`, లేదా `gpt-5.x` మోడల్ లాంటి నియామకాన్ని ఉపయోగించండి. పాత మోడల్స్ Responses ప్రాథమిక కార్యాచరణను మద్దతు ఇస్తాయి కానీ అన్ని ఫీచర్లను కాదు.
- **ఏజెంట్-ఫ్రేమ్‌వర్క్ వెర్షన్.** నమూనాలు తాజా MAF (`>=1.10.0`)కు లక్ష్యంగా ఉన్నాయి. అధికారిక ఏజెంట్-సృష్టి కాల్ `client.as_agent(...)`; APIs ఫ్రేమ్‌వర్క్ ప్రచురించబడిన డాక్యూమెంటేషన్లు మరియు సంస్థాపిత బిల్డ్ తో ధృవీకరించబడ్డాయి. మీరు వేరే వెర్షన్ ను ఉపయోగిస్తే, పద్ధతి అందుబాటును నిర్ధారించండి (`as_agent` వర్సెస్ `create_agent`).
- **లెషన్ 08 వర్క్‌ఫ్లో నోట్‌బుక్ 04** ఉద్దేశపూర్వకంగా `AzureAIAgentClient` ( `agent-framework-azure-ai` నుండి) ను ఉంచుతుంది ఎందుకంటే ఇది Microsoft Foundry Agent Service ఆధారిత సాధనాలు (Bing గ్రౌండింగ్, కోడ్ ఇంటర్‌ప్రెటర్) ఉపయోగిస్తుంది; ఇది ఇప్పటికే Responses ఆధారితది.
- **.NET డిఫాల్ట్ నియామకం.** రెండు లెషన్ 08 dotNET వర్క్‌ఫ్లో నమూనాలు ముందు నిర్దిష్ట మోడల్‌ను హార్డ్‌కోడ్ చేసినవి; ఇప్పుడు అవి `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) కు డిఫాల్ట్. ఒక నమూనా మల్టీమోడల్/వి​ంక్షణ ఆ_INPUT_పై ఆధారపడి ఉంటే, `AZURE_OPENAI_DEPLOYMENT` ను అనుకూలమైన మోడల్‌కు సജ్జం చేయండి.
- **Foundry Local** ఓ OpenAI-అనుకూల **చాట్ కంప్లీషన్స్** ఎండ్‌పాయింట్‌ను అభివృద్ధి కోసం ప్రాథమిక వాతావరణం గా అందిస్తుంది; పూర్తి Responses API ఫీచర్ల కోసం Azure OpenAI / Microsoft Foundryను ఉపయోగించండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->