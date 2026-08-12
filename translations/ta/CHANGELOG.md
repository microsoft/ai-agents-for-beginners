# மாற்றங்களின் தொகுப்பு

**ஆரம்ப நிலை AI முகவர்கள்** படிப்புக்கான அனைத்து முக்கிய மாற்றங்களும் இந்தக் கோப்பில் பதிவுசெய்யப்பட்டுள்ளன.

## [வெளியீடு] — 2026-07-14

இந்த வெளியீடு படிப்பை இரண்டு புதிய பழமைவாய்ந்த மாதிரிகளிலிருந்து மாற்றுகிறது, மீதமுள்ள பாடங்களின் நோட்புக்க்களை நிலையான Microsoft Agent Framework API-க்கு இடமாற்றம் செய்கிறது, மற்றும் Python நோட்புக்க்களை நேரடி Microsoft Foundry நிலைக்கு எதிராக சரிபார்க்கிறது.

### மாற்றியமைக்கப்பட்டது

- **பழியடைந்த மாதிரிகளிலிருந்து மாற்றப்பட்டது (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** இரண்டும் `gpt-4.1` மற்றும் `gpt-4.1-mini` இப்போது பழையவை (பதிவீட்டு ஓய்வுத் தேதி **14 அக்டோபர் 2026**). அனைத்து பாடக் குறிப்புகளிலும் (`docs`, `.env.example`, Python/.NET நோட்புக்க்கள் மற்றும் மாதிரிகள்) பழையதல்லாத `gpt-5-mini` மாதிரியில் மாற்றப்பட்டுள்ளது. பாடம் 16-ன் மாதிரி வழிமாற்ற உதாரணம் சிறிய/பெரிய மாற்றுத்தன்மையை `gpt-5-nano` (சிறியது) மற்றும் `gpt-5-mini` (பெரியது) கொண்டு காப்பது தொடர்கிறது. மூன்றாம் தரப்பை நோட்புக்க்கள் ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), பழைய GitHub மாடல் உரைகள் மற்றும் `azure-openai-to-responses` திறனின் குறிப்புகள் உள்ளடக்கமாக மாற்றப்படாமல் வைக்கப்பட்டன.
- **பாடம் 14 ஹேன்ட்அப் நோட்புக் நிலையான API-க்கு இடமாற்றம் செய்யப்பட்டது.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) இப்போது `agent_framework.orchestrations.HandoffBuilder` உடன் `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type` அடிப்படையிலான ஷ்ட்ரீமிங் மற்றும் புதுப்பிக்கப்பட்ட `FoundryChatClient` (மறைந்துள்ள முன்-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` ஐ மாற்றுகிற) பயன்படுத்துகிறது.
- **பாடம் 14 மனித-இணைப்பு நோட்புக் நிலையான API-க்கு இடமாற்றம் செய்யப்பட்டது.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) இப்போது `ctx.request_info(...)` + `@response_handler` மூலம் நிறுத்துகிறது (மறைந்துள்ள `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` ஐ மாற்றுவது), `WorkflowBuilder(start_executor=..., output_executors=[...])` கொண்டு கட்டமைக்கிறது, `default_options={"response_format": ...}` மூலம் கட்டமைக்கப்பட்ட வெளியீட்டை இயக்குகிறது, மற்றும் நோட்புக் தன்னிச்சையாக இயக்கப்படும் (இன்க வேலைத்தொடர்பைத் தவிர்க்கிறது).
- **சூழல் அமைப்பு** ([.env.example](../../.env.example)): மாதிரி பயன்பாட்டு பெயர்கள் `gpt-5-mini` க்கு மாற்றப்பட்டு; `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (பாடம் 16 வழிமாற்றம்) மற்றும் முந்தையபடி இல்லை ஆன `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (பாடம் 15 உலாவி பயன்பாடு) சேர்க்கப்பட்டன.
- **பிணையங்கள்** ([requirements.txt](../../requirements.txt)): `agent-framework`, `agent-framework-foundry`, மற்றும் `agent-framework-openai` ஐ `~=1.10.0` க்கு அடையவைத்தது (1.11.0 போட்டுத் தேர்வில் உடன்பட்ட மாற்றங்கள் உள்ளன).

### குறிப்பு மற்றும் அறிவிக்கப்படாத வரம்புகள்

- **நேரடி Microsoft Foundryக்கு எதிராக பரிசோதிக்கப்பட்டது.** Python நோட்புக்க்கள் தலை இல்லாமல் `nbconvert` மூலம் Microsoft Foundry திட்டத்தில் `gpt-5-mini` (மற்றும் பாடம் 16 வழிமாற்றத்திற்கு `gpt-5-nano`) பயன்படுத்தி இயக்கின. உங்கள் திட்டத்தில் தவறில்லாத மாதிரிகளை நிறுவவும்; நோட்புக்க்கள் `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` உள்ளிட்ட சூழல் மாறிலிகளிலிருந்து பயன்பாட்டு பெயரை படிக்கின்றன.
- **சில பாடங்களுக்குச் கூடுதல் வளங்கள் இன்னும் தேவை.** பாடம் 05 இற்கு Azure AI Search தேவை; பாடம் 08 Bing-அடிப்படை வேலைப்பாட்டிற்கு (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) Bing இணைப்பு மற்றும் Microsoft Foundry Agent Service கருவிகள்; பாடம் 13 (Cognee) மற்றும் பாடம் 17 (Foundry Local) அவர்களது சொந்த ரன்டைம்களைக் கொண்டிருக்க வேண்டும்.

## [வெளியீடு] — 2026-07-13

இந்த வெளியீடு புதிய இரண்டு பாடங்களைச் சேர்க்கிறது, நிறுவலுக்கு முழுமையான வளைவு — முகவர்களை Microsoft Foundry வரை உயர்த்துதல் மற்றும் ஒரே ஒருங்கிணைப்புக் கணினிக்குத் தாழ்த்துதல் — அத்துடன் சோதனை-சோதனை வாயிலாக, புதுப்பிக்கப்பட்ட பயிற்சி வழிச் செருகல், புதிய கற்றல் திறன்கள் மற்றும் புதுப்பிக்கப்பட்ட பிராண்டிங்.

###ச் சேர்க்கப்பட்டது

- **பாடம் 16 — Microsoft Foundry உடன் அளவிடக்கூடிய முகவர்களை நிறுவுதல்.** புதிய பாடம் [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) மற்றும் இயங்கக்கூடிய நோட்புக் [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) வாடிக்கையாளர் ஆதரவு முகவரைக் கட்டமைப்பைக் கற்றுத்தருகிறது (கருவிகள், RAG, நினைவு, மாதிரி வழிமாற்றம், பதிலளிப்பு மேம்பாடு, மனித அனுமதி, மதிப்பீட்டுக் கதவு, மற்றும் OpenTelemetry தடம்), மேம்பாடு/நிறுவல்/ரன்டைம் Mermaid வரைபடங்கள், அறிவு சோதனை, பணிப்பதி, மற்றும் சவால்.
- **பாடம் 17 — Foundry Local மற்றும் Qwen உடன் உள்ளூர்மையான AI முகவர்களை உருவாக்குதல்.** புதிய பாடம் [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) மற்றும் நோட்புக் [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) முழுமையாக சாதனத்தில் இயங்கும் பொறியியல் உதவியாளரை கட்டமைக்கிறது (Foundry Local மூலம் Qwen செயல்பாடு அழைப்பு, பாதுகாக்கப்பட்ட கோப்பு கருவிகள், உள்ளூர் RAG Chroma உடன், விருப்பமான உள்ளூர் MCP), உள்ளூர் மட்டுமே/உள்ளூர் RAG/கருவி அழைப்பு வரைபடங்கள், அறிவு சோதனை, பணிப்பதி மற்றும் சவால்.
- **புகை-சோதனை வழித்தடம்.** புதிய [AI புகை சோதனை](https://github.com/marketplace/actions/ai-smoke-test) வேலைப்பாடல் [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) மற்றும் பாடங்கள் 01, 04, 05 மற்றும் 16 இல் நிறுவக்கூடிய முகவர்களின் பட்டியல்கள் [tests/](./tests/README.md) கீழ் சேர்க்கப்பட்டன, ஒவ்வொரு பட்டியலும் அதன் பாடம் மற்றும் ஹோஸ்ட் முகவரின் பெயரை மேப்பிங் செய்கிறது. பாடம் 16க்கு "நிறுவப்பட்ட முகவரின் புகை சோதனைகளுடன் சரிபார்ப்பு" பிரிவு சேர்க்கப்பட்டது; பாடங்கள் 01/04/05 இற்கு விருப்பமான புகை-சோதனை குறிப்பு.
- **கற்றல் திறன்கள்.** புதிய முகவர் திறன்கள் `.agents/skills/` கீழ்: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (பாடம் 16 மற்றும் 17 வழிகாட்டலை தொகுத்தவை), மற்றும் [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (நோட்புக் மாதிரிகளை நேரடி Microsoft Foundry / Azure OpenAI அமைப்புடன் சரிபார்ப்பது எப்படி).
- **நோட்புக் சரிபார்ப்பு இயக்கி.** புதிய [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) அனைத்து Python நோட்புக்க்களையும் தலை இல்லாமல் `nbconvert` மூலம் இயக்கி PASS/FAIL அட்டவணையை (மேலும் `results.json`) அச்சிடுகிறது. அது ரெப்போ ரூட் மற்றும் Python ஐ தானாக கண்டறிகிறது, பாடம் சாராத நோட்புக்க்கள் (`.venv`, `site-packages`, `translations`, திறன் டெம்ப்ளேட் ரிசோர்ஸ்) மற்றும் `.NET` நோட்புக்க்களை இயல்பாக தவிர்க்கிறது, மற்றும் `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, மற்றும் `-Python` ஆதரிக்கிறது.
- **பாட நெவிகேஷன்.** பாடங்கள் 11–15க்கு முன்/பின் பாடக் குறும்பட இணைப்புகள் சேர்க்கப்பட்டன (முந்தையபடி இல்லாது இருந்த), இதனால் 00 → 18 வரை படிப்பு முழுவதும் தொடர் அமைந்தது.
- **புதிய ஷாம்பில்கள்.** பாடங்கள் 16 மற்றும் 17க்கான சின்னப்படங்கள் மற்றும் புதுப்பிக்கப்பட்ட ரெப்போ சமூக படம் [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (இப்போது இரண்டு பாடங்களையும் மற்றும் `aka.ms/ai-agents-beginners` URL-ஐ விளம்பரப்படுத்துகிறது).
- **பிணையங்கள்** ([requirements.txt](../../requirements.txt)): பாடம் 17க்கு `foundry-local-sdk` மற்றும் `chromadb` சேர்க்கப்பட்டன.

### மாற்றியமைக்கப்பட்டது

- **முதன்மை [README.md](./README.md)** பாட அட்டவணை: பாடங்கள் 16 மற்றும் 17 இப்போது உள்ளடக்கத்துடன் இணைக்கப்பட்டன (முந்தைய "விரைவில் வரும்" என்பதை மாற்றியது); ரெப்போ படம் `repo-thumbnailv3.png` ஆக புதுப்பிக்கப்பட்டது.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: பாடம் முறையே இடங்கள் மற்றும் கற்றல் பாதைகளில் பாடங்கள் 16 மற்றும் 17 சேர்க்கப்பட்டன மற்றும் "நிறுவப்பட்ட முகவர்களை புகை சோதனையால் சரிபார்த்தல்" பகுதி சேர்க்கப்பட்டது.
- **[AGENTS.md](./AGENTS.md)**: பாட எண்ணிக்கை/விபரம் (00–18), சோதனை-சோதனை சரிபார்ப்பு பகுதி, மற்றும் பாடம் 16/17 மாதிரி-பெயரிடல் உதாரணங்கள் புதுப்பிக்கப்பட்டன.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "முந்தைய பாடம்" இப்போது பாடம் 17 (முந்தைய 15)வது நோக்குகிறது, தொடரை முடிக்கிறது.
- **பழைய மாதிரிகளை தவிர்த்து மாதிரி குறிப்பு வழக்கமைக்கப்பட்டது.** அனைத்து `gpt-4o` / `gpt-4o-mini` குறிப்பு (docs, `.env.example`, Python/.NET நோட்புக்க்கள் மற்றும் மாதிரிகள்) `gpt-4.1-mini` ஆக மாற்றப்பட்டது — `gpt-4o` (அனைத்து பதிப்பும்) 2026ல் ஓய்வு பெறுகிறது. பாடம் 16 மாதிரி வழிமாற்ற உதாரணம் சிறிய/பெரிய வேறுபாட்டை `gpt-4.1-mini` (சிறியது) மற்றும் `gpt-4.1` (பெரியது) கொண்டு தொடர்கிறது. Python நோட்புக்க்கள் இப்போது கடுமையாக மாதிரி பெயர் கொடுக்காமல் சூழல் மாறிலிகளிலிருந்து மாதிரி தேர்வு செய்கின்றன (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`).

### குறிப்பு மற்றும் அறிவிக்கப்படாத வரம்புகள்

- **நேரடி Azure-க்கு எதிராக இயக்கப்படவில்லை.** புதிய பாடங்களின் நோட்புக்க்கள் கல்விக்கான மாதிரிகள்; உங்கள் Microsoft Foundry / Foundry Local அமைப்பில் ஓடவைத்து சரிபார்க்கவும். புகை-சோதனை வேலைப்பாடு பாட முகவரைக் நிறுவி Azure OIDC ரகசியங்களை (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) **Azure AI User** பங்கு கொண்டு Foundry திட்ட அளவில் அமைக்க வேண்டும்.
- **பாடம் 17 உள்ளூர் மட்டுமே.** அதற்கு Foundry பதில்கள் முக்கோணமில்லை, எனவே புகை-சோதனை செயல்பாடு பொருந்தாது; உங்கள் ஒருங்கிணைப்புக் கணினியில் நோட்புக் இயக்கி சரிபார்க்கவும்.

## [வெளியீடு] — 2026-07-06

இந்த வெளியீடு படிப்பை **Azure OpenAI Responses API** க்கு இடமாற்றம் செய்கிறது, **Microsoft Foundry** மற்றும் **Microsoft Agent Framework (MAF)** என்ற தயாரிப்பு பெயரீடுகளுக்கு ஒருமைப்படுத்தலை செய்கிறது, GitHub மாடல்களை ஓய்வை அறிவிக்கிறது, SDK பதிப்புகளை புதுப்பிக்கிறது, மற்றும் உள்ளூர் மாதிரிகள் மற்றும் Foundry இல் பிற கட்டமைப்புகளை அலகுசெய்யும் புதிய உள்ளடக்கத்தை சேர்க்கிறது.

### சேர்க்கப்பட்டது

- **இடமாற்ற திறன்** — `.agents/skills/` இல் நிறுவப்பட்ட [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) முகவர் திறன் (Azure-Samples/azure-openai-to-responses) உடன், அதன் குறிப்புகள் மற்றும் ஸ்கானர் ஸ்கிரிப்ட் உட்பட.
- **Foundry Local (சாதனத்தில் மாதிரிகள் இயக்கம்)** — [00-course-setup/README.md](./00-course-setup/README.md) இல் புதிய "மாற்று வழங்குநர்: Foundry Local" பகுதி, நிறுவல் (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, மற்றும் `FoundryLocalManager` ஐ Microsoft Agent Framework உடன் `OpenAIChatClient` மூலம் இணைத்தல்.
- **Microsoft Foundry இல் LangChain / LangGraph முகவர்களை ஹோஸ்ட் செய்வது** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) இல் புதிய பகுதி மற்றும் இயங்கக்கூடிய மாதிரி [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) `langchain-azure-ai[hosting]` மற்றும் `ResponsesHostServer` (/responses செயல்பாடு) பயன்படுத்தி, [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) அடிப்படையில்.
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md) இல் புதிய "உண்மையான உலக உதாரணம்: Microsoft Project Opal" பகுதி, Opal ஐ ஒரு நிறுவன கணினி பயன்பாட்டு முகவராக விவரித்து, பாடக் கருத்துக்களுடன் (மனித இணைப்பு, நம்பிக்கை/பாதுகாப்பு, திட்டமிடல், திறன்கள்) மேப்பிங் செய்கிறது.
- **இரண்டாவது பாடம் 02 Python மாதிரி** — பின்னர் மாற்றப்பட்ட Semantic Kernel நோட்புக்கிலிருந்து இடமாற்றப்பட்ட [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) சேர்க்கப்பட்டது மற்றும் பாட README இல் இணைக்கப்பட்டது.
- **மாதிரிகள் மற்றும் வழங்குநர்கள்** பகுதி [STUDY_GUIDE.md](./STUDY_GUIDE.md) இல் சேர்க்கப்பட்டது.

### மாற்றியமைக்கப்பட்டது

- **ஆலாபம் நிறைவு → பதில்கள் API (Python).** மாதிரியை நேரடியாக அழைத்த மாதிரிகள் Chat Completions இருந்து Responses APIக்கு மாற்றப்பட்டன (`client.responses.create(input=..., store=False)`, `resp.output_text`) Azure OpenAI `/openai/v1/` நிலையான சுடுகாட்டை பயன்படுத்தி (எந்த `api_version` இல்லாமல்). பாதிக்கப்பட்ட மாதிரிகள்:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — முழு செயல்பாடு அழைப்பு நடைமுறை (கருவி வடிவமைப்பு Responses வடிவத்தில் குறைத்தல், கருவி முடிவுகள் `function_call_output`, `max_output_tokens` போன்றவையாக திரும்புதல்).

- **GitHub மாதிரிகள் → Azure OpenAI.** GitHub மாதிரிகள் பயன்படுத்தப்படாமல் விடப்பட்டுள்ளன (**ஜூலை 2026** அன்று நிறுத்தப்படுகின்றன) மற்றும் Responses API ஐ ஆதரவிடவில்லை. அனைத்து GitHub மாதிரி குறியீடு பாதைகளும் Python மற்றும் .NET உதாரணங்களில் Azure OpenAI / Microsoft Foundry ஆக மாற்றப்பட்டுள்ளன:
  - Python: பாடம் 08 வேலைபாடு நோட்புக்குகள் (`01`–`03`), பாடம் 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + இணை `.md` ஆவணங்கள் மற்றும் பாடம் 08 dotNET வேலைபாடு நோட்புக்குகள்/`.md` (`01`–`03`) இப்போது `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` மற்றும் `AzureCliCredential` ஐ பயன்படுத்துகின்றன.
- **Semantic Kernel → Microsoft Agent Framework.** முந்தைய `02-semantic-kernel.ipynb` Microsoft Agent Framework மற்றும் Azure OpenAI (Responses API) உடன் மறுமொழிக்க்கப்பட்டு `02-python-agent-framework-azure-openai.ipynb` என்ற பெயரில் மாற்றப்பட்டது.
- **`FoundryChatClient` + `as_agent` என்பது தகுதி அடையாளமாக்கப்பட்டது.** README மற்றும் நோட்புக் குறியீடு `AzureAIProjectAgentProvider` ஐ மேற்கோள் செய்தது பாடம் 01 மற்றும் ஃப்ரேம்வர்க் தன்னுடைய உதாரணங்களில் பயன்படுத்தப்பட்ட canonical மாதிரியை பின்பற்றியது: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` மற்றும் `provider.as_agent(...)` . பாடம் 02–14 README மற்றும் நோட்புக்குகளில் (உதா., பாடம் 13 நினைவகம், அனைத்து பாடம் 14 நோட்புக்குகள், `11-agentic-protocols/code_samples/github-mcp/app.py`) இதை புதுப்பித்துள்ளோம்.
- **தயாரிப்பு பெயரிடல்.** ஆங்கில உள்ளடக்கத்தில் முழுவதும் பெயர் மாற்றம்:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (மாற்றம் இல்லை: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", மற்றும் சுற்றுச்சூழல் மாறிலி பெயர்கள்.)
- **அடிப்படைகள்** ([requirements.txt](../../requirements.txt)):
  - `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0` ஐ உறுதி செய்துள்ளோம்.
  - Responses API க்கான குறைந்தபட்சம் `openai>=1.108.1` ஐ உறுதி செய்துள்ளோம்.
  - மாறிய GitHub மாதிரியான உதாரணங்களுக்கு மட்டுமே பயன்படுத்தப்பட்ட `azure-ai-inference` அகற்றப்பட்டுள்ளது.
- **சுற்றுச்சூழல் கட்டமைப்பு** ([.env.example](../../.env.example)): GitHub மாதிரிகள் மாறிகள் (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) நீக்கப்பட்டன; `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, மற்றும் விருப்பமான `AZURE_OPENAI_API_KEY` சேர்க்கப்பட்டன; மாறிய பெயர்களை Microsoft Foundry ஆக மாற்றியது.
- **ஆவணங்கள்** — மேம்படுத்தியுள்ளோம் [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), மற்றும் [STUDY_GUIDE.md](./STUDY_GUIDE.md) மேலே சொல்லப்பட்டவை (சுற்றுச்சூழல் மாறிகளைக் கட்டமைத்தல், சரிபார்ப்பு குறிச்சொல், வழங்குநர் வழிகாட்டி, பெயரிடல்).

### அகற்றப்பட்டது

- GitHub மாதிரிகள் பதிவு செய்யும் படிநிலைகள் மற்றும் சுற்றுச்சூழல் மாறிகள் முன்னிலை ஆவணங்களிலிருந்து (Azure OpenAI / Microsoft Foundry மூலம் மாற்றப்பட்டவை).

### பாதுகாப்பு / தனியுரிமை (பொது பகிர்வு சுத்திகரிப்பு)

- ஒரு உண்மையான **Azure சந்தா அடையாளம்**, resource-group / resource பெயர்கள் மற்றும் Bing இணைப்பு அடையாளம், மேலும் டெவலப்பர் உள்ளூர் கோப்பு பாதைகள் மற்றும் பயனர் பெயர்களைப் புகும் Jupyter நோட்புக் செயலாக்க வெளியீடுகள் நீக்கப்பட்டன:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- கண்காணிக்கப்பட்ட ஆங்கில உள்ளடக்கத்தில் எந்த API விசைகள், டோக்கன்கள், சந்தா அடையாளங்கள் அல்லது தனிப்பட்ட பாதைகள் மீதமிருக்கவில்லை என்பதை உறுதி செய்தோம் (இங்கு உள்ள GITHUB_TOKEN காணReferencesகள் GitHub Actions டோக்கன்கள் மற்றும் GitHub MCP சர்வர் PAT பற்றியது, இரண்டும் சட்டபூர்வமாகவும் GitHub Models உடனான தொடர்பற்றவை).

### குறிப்புகள் மற்றும் அறியப்பட்ட வரம்புகள்

- **செயல்படுத்தப்படவில்லை/செயலாக்கப்படவில்லை.** இவை API/பெயரிடல் சரியானதற்காக புதுப்பிக்கப்பட்ட கல்வி உதாரணங்கள்; நேரடி Azure வளங்களை எதிர்கொள்ளவில்லை, மற்றும் .NET உதாரணங்கள் இங்கு தொகுக்கப்படவில்லை. உங்கள் சொந்த Microsoft Foundry / Azure OpenAI நிறைவேற்றலை வைத்து பின்பற்றவும்.
- **மாதிரி ஆವிருத்தமானது Responses API ஐ ஆதரிக்க வேண்டும்.** `gpt-4.1-mini`, `gpt-4.1`, அல்லது `gpt-5.x` மாதிரிகளைப் பயன்படுத்தவும். பழைய மாதிரிகள் Responses API அம்சங்களை எல்லாவற்றையும் ஆதரிக்காது.
- **Agent-framework பதிப்பு.** உதாரணங்கள் சமீபத்திய MAF (`>=1.10.0`) க்கு இலக்காகும். canonical agent-உருவாக்க கூற்று `client.as_agent(...)`; API கள் ஃப்ரேம்வர்க் வெளியிட்ட ஆவணங்களுடன் சரிபார்க்கப்பட்டன. நீங்கள் வேறு பதிப்பை நிரூபித்தால், முறைவழிப்பாய்வை உறுதிசெய்யவும் (`as_agent` மற்றும் `create_agent`).
- **பாடம் 08 வேலைபாடு நோட்புக் 04** கருநி `AzureAIAgentClient` (agent-framework-azure-ai இலிருந்து) பயன்படுத்தப்படுவதால் அதேபோல் உள்ளது; இது Microsoft Foundry Agent Service இல் இணையத்தில் உள்ள கருவிகள்(Bing மடிவடுப்பு, குறியீடு பகுப்பாய்வாளர்) பயன்படுத்துகிறது; இது Responses அடிப்படையிலானது.
- **.NET இயல்புநிலை deployment.** பாடம் 08 dotNET வேலைபாடு உதாரணங்கள் முன்பு ஒரு குறிப்பிட்ட மாதிரியை கடுமையாக குறியிட்டு வைத்திருந்தன; இப்போது இயல்புநிலை `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) ஆகும். பல்மொழி/காட்சி உள்ளீடு தேவையாக இருந்தால் `AZURE_OPENAI_DEPLOYMENT` ஐ பொருத்தமான மாதிரியாக அமைக்கவும்.
- **Foundry Local** OpenAI பொருந்தும் **Chat Completions** முடிவுகோட்டை வெளிப்படுத்துகிறது மற்றும் உள்ளூர் மேம்பாட்டுக்கு உள்ளது; முழு Responses API அம்சங்களுக்காக Azure OpenAI / Microsoft Foundry ஐ பயன்படுத்தவும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->