# మార్పుల చర్చిలు

**AI Agents for Beginners** కోర్సుకు సంబంధించిన అన్ని ముఖ్యమైన మార్పులు ఈ ఫైల్‌లో నమోదయినవి.

## [విడుదల] — 2026-07-14

ఈ విడుదల కోర్సును రెండు కొత్తగా డిప్రికేటైన మోడల్స్ నుండి తరలిస్తుంది, మిగిలిన పాఠం నోట్బుక్స్‌ను স্থిర Microsoft Agent Framework APIకి మార్చింది, మరియు Python నోట్బుక్స్‌ను ప్రత్యక్ష Microsoft Foundry నియామకంపై ధ్రువీకరించింది.

### మారినవి

- **డిప్రికేటైన మోడల్స్ నుండి తరలింపు (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** `gpt-4.1` మరియు `gpt-4.1-mini` ఇప్పుడు డిప్రికేటెడ్ అయితే (ప్రచురణ విరమింపు తేదీ **14 అక్టోబర్ 2026**). ప్రతీ కోర్సు సూచన (డాక్యూమెంట్స్, `.env.example`, Python/.NET నోట్బుక్స్ మరియు నమూనాలు) ని డిప్రికేటెడ్ కాని `gpt-5-mini` తో మార్చారు. పాఠం 16 యొక్క మోడల్-రూటింగ్ ఉదాహరణ చిన్న/పెద్ద వ్యత్యాసాన్ని `gpt-5-nano` (చిన్న) మరియు `gpt-5-mini` (పెద్ద) ని ఉపయోగించి ఉంచింది. వేండర్డ్ తృతీయ పక్ష ఫైళ్ళు ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), చరిత్రాత్మక GitHub మోడల్స్ టెక్స్ట్, మరియు `azure-openai-to-responses` స్కిల్ యొక్క సామర్ధ్య సూచనలను ఉద్దేశపూర్వకంగా మార్చలేదు.
- **పాఠం 14 హాండాఫ్ నోట్బుక్ స్థిర APIకి మార్చబడింది.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) ఇప్పుడు `agent_framework.orchestrations.HandoffBuilder` తో `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type` ఆధారిత స్ట్రీమింగ్, మరియు `FoundryChatClient` (తొలగించిన pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` చిహ్నాలు మార్చి) ఉపయోగిస్తుంది.
- **పాఠం 14 హ్యూమన్-ఇన్-ది-లూఫ్ నోట్బుక్ స్థిర APIకి మార్చబడింది.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) ఇప్పుడు `ctx.request_info(...)` + `@response_handler` ద్వారా విరామం ఇస్తుంది (తొలగించిన `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` స్థానంలో), `WorkflowBuilder(start_executor=..., output_executors=[...])` తో రూపొందిస్తుంది, `default_options={"response_format": ...}` ద్వారా నిర్మిత ఉత్పత్తిని నడిపిస్తుంది, మరియు స్ర్కిప్టెడ్ సమాధానంతో నోట్బుక్ నిర్బంధం లేకుండా (క్లుప్త `input()` లేకుండా) నడుస్తుంది.
- **పర్యావరణ అమరిక** ([.env.example](../../.env.example)): మోడల్ నియామక పేర్లను `gpt-5-mini` కు మార్చింది; `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (పాఠం 16 రూటింగ్ కోసం) మరియు మొన్నటివరకు లేని `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (పాఠం 15 బ్రౌజర్-వినియోగం).
- **ఆధారాలు** ([requirements.txt](../../requirements.txt)): `agent-framework`, `agent-framework-foundry`, మరియు `agent-framework-openai` ని `~=1.10.0` కు పిన్ను చేసింది, స్వయం-సరిపోల్చుకొనే, ధృవీకృత సెట్ కోసం (1.11.0 లో ఈ పాఠాలు ఉపయోగించే ఉపరితలాలకు ప్రయోగాత్మక బ్రేకింగ్ మార్పులు ఉన్నాయి).

### గమనికలు మరియు తెలిసిన పరిమితులు

- **ప్రత్యక్ష Microsoft Foundry పై ధృవీకరణ.** Python నోట్బుక్స్ తలుపులు లేకుండా `nbconvert` తో Microsoft Foundry ప్రాజెక్ట్ పై `gpt-5-mini` (మరియు పాఠం 16 రూటింగ్ కోసం `gpt-5-nano`) ఉపయోగించి అమలు చేశారు. మీ ప్రాజెక్టులో సమానమైన నాన్-డిప్రికేటెడ్ మోడల్స్ ని నియమించండి; నోట్బుక్స్ నియామక పేరును `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` నుండి చదువుతాయి.
- **కొన్ని పాఠాలకి ఇంకా అదనపు వనరులు అవసరం.** పాఠం 05 కి Azure AI Search అవసరం; పాఠం 08 Bing-గ్రౌండింగ్ వర్క్‌ఫ్లో (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) కోసం Bing కనెక్షన్ మరియు Microsoft Foundry Agent Service ఆతిథ్యం వనరులు కలవలసినవి; పాఠం 13 (Cognee) మరియు పాఠం 17 (Foundry Local) కి వారి స్వంత రన్టైమ్స్ అవసరం.

## [విడుదల] — 2026-07-13

ఈ విడుదల రెండు కొత్త పాఠాలను చేరుస్తుంది, మైక్రోసాఫ్ట్ ఫౌండ్రీకి ఏజెంట్లను స్కేల్ చేయడం మరియు ఒకే వర్క్‌స్టేషన్‌కు తగ్గించడం పూర్తిగా సాకారం చేస్తుంది — మరియు ఒక స్మోక్-టెస్ట్ పైప్‌లైన్, తాజా కోర్సు నావిగేషన్, కొత్త నేర్చుకునే నైపుణ్యాలు మరియు కొత్త బ్రాండింగ్.

### జోడించబడినవి

- **పాఠం 16 — Microsoft Foundryతో స్కేలబుల్ ఏజెంట్లను నియామకం.** కొత్త పాఠం [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) మరియు నడుపగలిగే నోట్బుక్ [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb), ఉత్పత్తి కస్టమర్-సపోర్ట్ ఏజెంట్ (టూల్స్, RAG, మెమోరీ, మోడల్ రూటింగ్, స్పందన క్యాచింగ్, మానవ ఆమోదం, మూల్యాంకన గేట్, మరియు OpenTelemetry ట్రేసింగ్) నిర్మిస్తుంది, అభివృద్ధి/నియామకం/రన్‌టైమ్ Mermaid చిత్రాలు, జ్ఞాన పరీక్ష, అసైన్‌మెంట్, మరియు సవాలు ఉంటాయి.
- **పాఠం 17 — Foundry Local మరియు Qwen తో స్థానిక AI ఏజెంట్ల ఉత్పత్తి.** కొత్త పాఠం [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) మరియు నోట్బుక్ [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) పూర్తిగా పరికరం మీద నడిచే ఇంజినీరింగ్ అసిస్టెంట్ (Foundry Local ద్వారా Qwen ఫంక్షన్ కాలింగ్, సాండ్బాక్స్ ఫైల్ టూల్స్, స్థానిక RAG చొరకు Chroma, ఐచ్ఛిక స్థానిక MCP), స్థానిక-మాత్ర మాత్రమే / స్థానిక-RAG / టూల్-కాలింగ్ డయాగ్రామ్స్, జ్ఞాన పరీక్ష, అసైన్‌మెంట్, మరియు సవాలు కల్గి ఉంటుంది.
- **స్మోక్-టెస్ట్ పైప్‌లైన్.** కొత్త [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) వర్క్‌ఫ్లో [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) మరియు ప్రతి పాఠానికి క్యాటలాగ్లు [tests/](./tests/README.md) లో ఉన్నాయి, Lessons 01, 04, 05, మరియు 16 లోని నియమించదగిన ఏజెంట్ల కోసం, ప్రతి క్యాటలాగ్ తన పాఠం మరియు హోస్టెడ్ ఏజెంట్ పేరుకు READMEకి సంకetikిస్తుంది. పాఠం 16 లకు "స్మోక్ టెస్టులతో నియమించిన ఏజెంట్ ధృవీకరణ" సెక్షన్ పొందింది; పాఠాలు 01/04/05కి ఐచ్ఛిక స్మోక్-టెస్ట్ సూచిక.
- **నియమించే నైపుణ్యాలు.** కొత్త ఏజెంట్ నైపుణ్యాలు `.agents/skills/` క్రింద: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (పాఠం 16 మరియు 17 మార్గదర్శకత్వం), మరియు [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (నోట్బుక్ నమూనాలను ప్రత్యక్ష Microsoft Foundry / Azure OpenAI సెట్ అప్ తో ధ్రువీకరించడం).
- **నోట్బుక్ ధ్రువీకరణ రన్నర్.** కొత్త [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) ప్రతీ Python నోట్బుక్‌ను తలుపులు లేకుండా `nbconvert` తో అమలు చేసి PASS/FAIL మ్యాట్రక్స్ ప్రింట్ చేస్తుంది (`results.json` తోపాటు). ఇది ఆటోగా రెపో మూలాన్ని మరియు Python గుర్తిస్తుంది, కోర్సు కాని నోట్బుక్స్ (`.venv`, `site-packages`, `translations`, స్కిల్ టెంప్లేట్ ఆస్తులు) మరియు `.NET` నోట్బుక్స్ మినహాయిస్తుంది, మరియు `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, మరియు `-Python` సపోర్ట్ చాలు.
- **కోర్సు నావిగేషన్.** Lessons 11–15 కి ముందునిచ్చిన/తర్వాతినిచ్చే పాఠపు లింకులు జోడించబడ్డాయి (ముందు లేని), కాబట్టి మొత్తం కోర్సు 00 → 18 లో రెండింటి దిశలోనూ జతచేయబడింది.
- **కొత్త థంబ్నెయిల్లు.** పాఠం 16 మరియు 17కి థంబ్నెయిల్లు, మరియు తాజా రెపో సోషియల్ ఇమేజ్ [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (ఇప్పుడు రెండు కొత్త పాఠాలు మరియు `aka.ms/ai-agents-beginners` URL ని ప్రచారం చేస్తోంది).
- **ఆధారాలు** ([requirements.txt](../../requirements.txt)): పాఠం 17కి `foundry-local-sdk` మరియు `chromadb` జోడించబడినవి.

### మారినవి

- **ప్రధాన [README.md](./README.md)** పాఠ పట్టిక: పాఠాలు 16 మరియు 17 ఇప్పుడు వారి విషయాలకు లింకు పెట్టబడినవి (ముందు "త్వరలో రాబొతోంది"); రెపొ ఇమేజ్ `repo-thumbnailv3.png` కు పెరిగింది.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: పాఠం వారీగా గైడ్ మరియు నేర్చుకునే మార్గాల్లో పాఠాలు 16 మరియు 17 జోడించబడ్డాయి, మరియు "స్మోక్ టెస్టులతో నియమించిన ఏజెంట్ ధృవీకరణ" సెక్షన్.
- **[AGENTS.md](./AGENTS.md)**: పాఠాల సంఖ్య/వివరణ (00–18) నవీకరించబడింది, స్మోక్-టెస్ట్ ధృవీకరణ సెక్షన్ జోడించబడింది, మరియు పాఠం 16/17 నమూనా నామాల ఉదాహరణలు జోడించబడ్డాయి.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "మునుపటి పాఠం" ఇప్పుడు పాఠం 17 (ముందు పాఠం 15) కి సూచిస్తోంది, చైన్ ముగించింది.
- **బ్రేక్ కాని మోడల్స్ పై ఇష్టమైన మోడల్ సూచనలు.** కోర్స్ లోని అన్ని `gpt-4o` / `gpt-4o-mini` సూచనలను (డాక్స్, `.env.example`, Python/.NET నోట్బుక్స్ మరియు నమూనాలు) `gpt-4.1-mini` తో మార్చారు — `gpt-4o` అన్ని వర్షన్లు 2026లో విరమిస్తున్నారు. పాఠం 16 మోడల్-రూటింగ్ ఉదాహరణ చిన్న/పెద్ద వ్యత్యాసం `gpt-4.1-mini` (చిన్న) మరియు `gpt-4.1` (పెద్ద) తో ఉంచింది. Python నోట్బుక్స్ ఇప్పుడు పర్యావరణ చలామణీలు (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) నుండి మోడల్ ఎంచుకుంటాయి, హార్డ్‌కోడ్ చేసిన మోడల్ పేర్లు ఉపయోగించడం లేదు.

### గమనికలు మరియు తెలిసిన పరిమితులు

- **ప్రత్యక్ష Azure పై అమలు చేయలేదు.** కొత్త పాఠాల నోట్బుక్స్ విద్యాత్మక నమూనాలు; వాటిని మీ స్వంత Microsoft Foundry / Foundry Local సెటప్‌పై నడుపుతూ ధృవీకరించండి. స్మోక్-టెస్ట్ వర్క్‌ఫ్లోకి మీరు పాఠం ఏజెంట్‌ను నియమించి Azure OIDC రహస్యాలు (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`)ను **Azure AI User** పాత్రతో Foundry ప్రాజెక్ట్ రంగంలో కాన్ఫిగర్ చేయాలి.
- **పాఠం 17 స్థానిక-మాత్రమే.** దీని వద్ద Foundry Responses ఎండ్పాయింట్ లేదు, కనుక స్మోక్-టెస్ట్ చర్య వర్తించదు; మీ వర్క్‌స్టేషన్‌పై నోట్బుక్ నడుపుతూ ధృవీకరించండి.

## [విడుదల] — 2026-07-06

ఈ విడుదల కోర్సును **Azure OpenAI Responses API**కి మార్చదు, **Microsoft Foundry** మరియు **Microsoft Agent Framework (MAF)** పై ఉత్పత్తి పేర్లను సుస్థిరం చేస్తుంది, GitHub Modelsని విరమిస్తుంది, SDK వెర్షన్లను నవీకరించి, స్థానిక మోడల్స్ మరియు ఫౌండ్రీపై ఇతర ఫ్రేమ్‌వర్క్‌ల హోస్టింగ్‌పై కొత్త విషయాలను జోడిస్తుంది.

### జోడించబడ్డవి

- **మైగ్రేషన్ స్కిల్** — [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) ఏజెంట్ స్కిల్‌ను (`Azure-Samples/azure-openai-to-responses` నుండి) `.agents/skills/` క్రింద ఉంచారు, దాని సూచనలు మరియు స్కేనర్ స్క్రిప్ట్ సహా.
- **Foundry Local (పరికరంలోనే మోడల్స్ నడవటం)** — కొత్త "ఆల్టర్నేటివ్ ప్రొవైడర్: Foundry Local" సెక్షన్ [00-course-setup/README.md](./00-course-setup/README.md) లో ఇన్‌స్టాల్ (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, మరియు Microsoft Agent Framework ద్వారా `FoundryLocalManager` ను `OpenAIChatClient`తో కట్టడం గురించి ఉంది.
- **Microsoft Foundryపై LangChain / LangGraph ఏజెంట్ల హోస్టింగ్** — కొత్త సెక్షన్ [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) లో తో పాటు నడుపగలిగే నమూనా [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) లో `langchain-azure-ai[hosting]` మరియు `ResponsesHostServer` ( `/responses` ಪ್ರోటోకాల్) ఉపయోగించడం, [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) ఆధారంగా.
- **Microsoft Project Opal** — కొత్త "వాస్తవ ప్రపంచ ఉదాహరణ: Microsoft Project Opal" సెక్షన్ [15-browser-use/README.md](./15-browser-use/README.md) లో ఉంది, Opal‌ను ఒక సంస్థ కంప్యూటర్-ఉపయోగ ఏజెంట్ గా చూపిస్తూ కోర్సు భావనలతో (హ్యూమన్-ఇన్-ది-లూప్, నమ్మకం/భద్రత, ప్రణాళిక, నైపుణ్యాలు) మ్యాపింగ్ చేస్తుంది.
- **రెండవ పాఠం 02 Python నమూనా** — [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) జోడించబడింది (మారిన వాటిలో చూడండి — మొన్నటి సొంత Semantic Kernel నోట్బుక్ నుండి మార్చబడింది) మరియు పాఠం READMEలో లింకు.
- **మోడల్స్ మరియు ప్రొవైడర్స్** సెక్షన్ [STUDY_GUIDE.md](./STUDY_GUIDE.md) లో జోడించబడింది.

### మారినవి

- **చాట్ కంప్లిషన్ల నుంచి Responses APIకి (Python).** మోడల్‌ను నేరుగా పిలిచే నమూనాలు Chat Completions నుంచి Responses APIకి మార్చబడ్డాయి (`client.responses.create(input=..., store=False)`, `resp.output_text`), స్థిర Azure OpenAI `/openai/v1/` ఎండ్‌పాయింట్ ఉపయోగిస్తూ `OpenAI` క్లయింట్ సహా (మాత్రమే `api_version` లేదు). ప్రభావిత నమూనాల్లో ఉన్నాయి:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — పూర్తి ఫంక్షన్-కలింగ్ వాక్‌త్రూ (టూల్ స్కీమ్ Responses ఫార్మాట్‌కు మార్చబడింది, టూల్ ఫలితాలు `function_call_output`, `max_output_tokens`, మొదలైనవచ్చు).

- **GitHub మోడల్లు → Azure OpenAI.** GitHub మోడల్లు నిలిపివేయబడ్డాయి (జూలై 2026 లో రిటైర్ అవుతుంది) మరియు Responses API ని మద్దతు సరఫరా చేయవు. అన్ని GitHub మోడల్లు కోడ్ మార్గాలను Python మరియు .NET నమూనాలలో Azure OpenAI / Microsoft Foundry కి మార్చారు:
  - Python: Lesson 08 వర్క్‌ఫ్లో నోట్‌బుక్‌లు (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + అనుబంధ `.md` డాక్యుమెంట్లు, మరియు Lesson 08 dotNET workflow నోట్‌బుక్‌లు/`.md` (`01`–`03`) ఇప్పుడు `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` ద్వారా `AzureCliCredential` తో వాడుతున్నాయి.
- **Semantic Kernel → Microsoft Agent Framework.** పూర్వ `02-semantic-kernel.ipynb` ను Microsoft Agent Framework తో Azure OpenAI (Responses API) ఇంప్లిమెంట్ చేసి `02-python-agent-framework-azure-openai.ipynb` గా పునఃరాయిలు చేశారు.
- **`FoundryChatClient` + `as_agent` పై ప్రమాణీకరణ.** README మరియు నోట్‌బుక్ కోడ్ లో `AzureAIProjectAgentProvider` సూచించినవి Lesson 01 మరియు ఫ్రేం‌వర్క్ సాంపిల్స్ ఉపయోగించిన సంప్రదాయ నమూనాను అనుసరించేందుకు ప్రమాణీకరించారు: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` తో `provider.as_agent(...)`. Lesson 02–14 READMEలు, నోట్‌బుక్‌లలో నవీకరించారు (ఉదాహరణకు, Lesson 13 memory, అన్ని Lesson 14 నోట్‌బుక్‌లు, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **ఉత్పత్తి పేరు.** ఆంగ్ల కంటెంట్ అంతటా పేర్లు మార్చబడినవి:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (మార్పు లేదు: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", మరియు పర్యావరణ వేరియబుల్ పేర్లు.)
- **డిపెండెన్సీలు** ([requirements.txt](../../requirements.txt)):
  - `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0` పిన్ చేశారు.
  - Responses API కోసం కనిష్ఠం `openai>=1.108.1` పిన్ చేశారు.
  - గిట్హబ్ మోడల్లు నమూనాలు మాత్రమే వాడిన `azure-ai-inference` తీసివేశారు.
- **పర్యావరణ కాన్ఫిగరేషన్** ([.env.example](../../.env.example)): గిట్హబ్ మోడల్లు వేరియబుల్స్ (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`)ను తీసివేయగా; `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, మరియు ఐచ్ఛికం `AZURE_OPENAI_API_KEY` ని జోడించారు; పేర్లను Microsoft Foundry గా నవీకరించారు.
- **డాక్యుమెంటేషన్** — పై మార్పులకు అనుగుణంగా [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), మరియు [STUDY_GUIDE.md](./STUDY_GUIDE.md) నవీకరించారు (పరిసర వేరియబుల్స్ సెట్ చేయడం, ధ్రువీకరణ స్నిపెట్, ప్రొవైడర్ మార్గదర్శకం, పేర్ల అంశము).

### తీసివేయబడింది

- గిట్హబ్ మోడల్లు ఆన్‌బోర్డింగ్ దశలు మరియు పర్యావరణ వేరియబుల్స్ సెటప్ డాక్స్ నుండి తీసివేయబడ్డాయి (Azure OpenAI / Microsoft Foundry తో భర్తీపడ్డాయి).

### భద్రత / గోప్యత (జనరల్-షేరింగ్ శుభ్రపరచడం)

- నిజమైన **Azure subscription ID**, రిసోర్స్-గ్రూప్ / రిసోర్స్ పేర్లు, మరియు Bing కనెక్షన్ ID తో పాటు డెవలపర్ **స్థానిక ఫైల్ మార్గాలు మరియు ఉపయోక్తృ పేర్లు** ఉన్న Jupyter నోట్‌బుక్ ఎగ్జిక్యూషన్ అవుట్‌పుట్‌లు తొలగించారు:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- API కీలు, టోకెన్లు, సబ్‌స్క్రిప్షన్ IDలు లేదా వ్యక్తిగత మార్గాలు గమనించిన ఎంగ్లిష్ కంటెంట్ లో ఉండవని ధృవీకరించారు (`GITHUB_TOKEN` సూచనలు గిట్హబ్ Actions టోకెన్ వర్క్‌ఫ్లోలలో మరియు గిట్హబ్ MCP సర్వర్ PAT Lesson 11 సెటప్ లో ఉన్నవి — రెండూ చట్టపరమైనవి మరియు గిట్హబ్ మోడల్లు కి సంబంధించినవి కాదు).

### గమనికలు మరియు తెలిసిన పరిమితులు

- **అన్ని సాంపిల్స్ అమలు లేదా కంపైల్ చేయబడలేదు.** ఇవి విద్యా సాంపిల్స్, API / పేరుల సరిచేయడానికి నవీకరించబడ్డాయి; వీటిని ప్రత్యక్ష Azure వనరులపై నడిపించలేదు, .NET సాంపిల్స్ ఈ పరిసరంలో కంపైల్ చేయబడలేదు. మీ Microsoft Foundry / Azure OpenAI డిప్లాయ్‌మెంట్ పై ధృవీకరించండి.
- **మోడల్ డిప్లాయ్‌మెంట్ Responses API మద్దతు ఇవ్వాలి.** `gpt-4.1-mini`, `gpt-4.1`, లేదా `gpt-5.x` మోడల్ లాంటి డిప్లాయ్‌మెంట్ వాడండి. పాత మోడల్లు Responses యొక్క ప్రాథమిక పనితీరును మద్దతు ఇస్తాయి కాని అన్ని ఫీచర్లు కాదు.
- **Agent-framework సంస్కరణ.** నమూనాలు తాజా MAF (`>=1.10.0`) ని లక్ష్యం చేశాయి. ప్రామాణిక agent-సృష్టి పిలుపు `client.as_agent(...)`; APIs ఫ్రేం‌వర్క్ ప్రచురిత డాక్యుమెంట్స్ మరియు ఇన్‌స్టాల్ చేసిన బిల్డ్ తో ధృవీకరించినవి. మీరు వేరే సంస్కరణను పిన్ చేస్తే, పద్ధతుల అందుబాటును నిర్ధారించుకోండి (`as_agent` లేదా `create_agent`).
- **Lesson 08 వర్క్‌ఫ్లో నోట్‌బుక్ 04** ఉద్దేశపూర్వకంగా `AzureAIAgentClient` (agent-framework-azure-ai నుండి) నిలుపుదల చేస్తుంది ఎందుకంటే ఇది Microsoft Foundry Agent Service అతిథి సాంకేతిక పరికరాలు (Bing grounding, కోడ్ ఇంటర్‌ప్రెటర్) ఉపయోగిస్తుంది; ఇది ఇప్పటికే Responses ఆధారంగా.
- **.NET డిఫాల్ట్ డిప్లాయ్‌మెంట్.** రెండు Lesson 08 dotNET వర్క్‌ఫ్లో నమూనాలు ముందు নির్దిష్ట మోడల్ ను హార్డ్‌కోడ్ చేసుకున్నవి; ఇప్పుడు అవి డిఫాల్ట్ గా `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) ను ఉపయోగిస్తాయి. ఒక నమూనా మల్టీమొడల్/విజన్ ఇన్పుట్ మీద ఆధారపడి ఉంటే, సరిపోయే మోడల్ కి `AZURE_OPENAI_DEPLOYMENT` ని సెట్ చేయండి.
- **Foundry Local** ఓ OpenAI-సరఫరాదారుల **Chat Completions** ఎండ్‌పాయింట్ ను ఎక్స్‌పోజ్ చేస్తుంది మరియు స్థానిక అభివృద్ధి కోసం ఉద్దేశించబడింది; పూర్తి Responses API ఫీచర్ సెట్ కోసం Azure OpenAI / Microsoft Foundry వాడండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->