# மாற்றுச்சீட்டு

**ஆதாரம் கற்றவர்களுக்கு AI முகவர்கள்** பாடத்திட்டத்திற்கு அனைத்து குறிப்பிடத்தகுந்த மாற்றங்களும் இந்த கோப்பில் பதிவாக்கப்பட்டுள்ளது.

## [வெளியிடப்பட்டது] — 2026-07-13

இந்த வெளியீடு, விநியோக அடுக்கை நிறைவு செய்ய இரண்டு புதிய பாடங்களையும் சேர்க்கிறது — முகவர்களை Microsoft Foundry வரை பெரிதாக்கலும் ஒரே பணியாளர் இயந்திரத்திற்குக் குறைத்தலும் — கூடவே ஒரு புகை-சோதனை குழாய், புதுப்பிக்கப்பட்ட பாடக் கோப்பு வழிசெலுத்தல், புதிய கற்றல் திறன்கள் மற்றும் புதுப்பிக்கப்பட்ட பிராண்டிங்.

### சேர்க்கப்பட்டது

- **பாடம் 16 — Microsoft Foundry உடன் விரிவாக்கக்கூடிய முகவர்களை வெளியிடுதல்.** புதிய பாடம் [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) மற்றும் இயக்கக்கூடிய நோட்புக் [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) ஒரு உற்பத்தி வாடிக்கையாளர் சேவை முகவரியை உருவாக்குகிறது (கருவிகள், RAG, நினைவு, மாதிரி வழியமைப்பு, பதில் சேமிப்பு, மனித அங்கீகாரம், மதிப்பீட்டு வாசல் மற்றும் OpenTelemetry கண்காணிப்பு), வளர்ச்சி/வெளியீடு/இயக்க Mermaid வரைபடங்கள், அறிவு சோதனை, போர்ட்டாளம் மற்றும் சவால் உடன்.
- **பாடம் 17 — Foundry Local மற்றும் Qwen உடன் உள்ளூர் AI முகவர்களை உருவாக்குதல்.** புதிய பாடம் [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) மற்றும் நோட்புக் [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) ஒரு முழுமையாக சாதனத்தில் இயங்கும் பொறியியல் உதவியாளர் (Qwen செயல்பாடு அழைப்பு Foundry Local வழியாக, முடுக்கப்பட்ட கோப்பு கருவிகள், உள்ளூர் RAG Chroma உடன், விருப்பம் உள்ள உள்ளூர் MCP), உள்ளூர் மட்டுமே / உள்ளூர்-RAG / கருவி அழைப்பு வரைபடங்கள், அறிவு சோதனை, போர்ட்டாளம் மற்றும் சவால் உடன்.
- **புகை-சோதனை குழாய்.** புதிய [AI புகை சோதனை](https://github.com/marketplace/actions/ai-smoke-test) workflow [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) மற்றும் பாட 01, 04, 05 மற்றும் 16ல் உள்ள வெளியிடக்கூடிய முகவர்களுக்கான பாடம் அடிப்படையான பட்டியல்கள் [tests/](./tests/README.md), ஒவ்வொரு பட்டியலும் அதை சார்ந்த பாடம் மற்றும் ஹோஸ்ட் முகவர் பெயருடன் குறிக்கப்பட்டுள்ளது. பாடம் 16க்கு "புகை சோதனைகளுடன் வெளியிடப்பட்ட முகவரியை சரிபார்த்தல்" பகுதி சேர்க்கப்பட்டது; பாடங்கள் 01/04/05க்கு விருப்பமான புகை-சோதனை குறிப்பு.
- **கற்றல் திறன்கள்.** புதிய முகவர் திறன்கள் `.agents/skills/` அடைவில்: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (பாடங்கள் 16 மற்றும் 17 வழிகாட்டுதலை தொகுத்தல்), மற்றும் [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (நோட்புக் எடுத்துக்காட்டுகளை நேரடி Microsoft Foundry / Azure OpenAI அமைப்புக்கு எதிராக எப்படிப் பரிசோதிப்பது).
- **நோட்புக் சரிபார்ப்பு இயக்கி.** புதிய [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) இது ஒவ்வொரு Python நோட்புக்கையும் `nbconvert` மூலம்த் தலையில்லாமல் இயக்கி PASS/FAIL அட்டவணையை அச்சிடுகிறது (மேலும் `results.json`). இது தானாகக் கிடைக்கும் ரெப்போ ரூட் மற்றும் Python ஐ கண்டறிந்து, பாடமின்மேல் நோட்புக்(கள்) (`.venv`, `site-packages`, `translations`, திறன் மாதிரி சொத்துக்கள்) மற்றும் `.NET` நோட்புக்(களை) தவிர்க்கிறது, மற்றும் `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, மற்றும் `-Python` விருப்ப உரைகளை ஆதரிக்கிறது.
- **பாடக் கோப்புப் வழிசெலுத்தல்.** பாடங்கள் 11–15க்கு முன்/அடுத்த பாட இணைப்புகளைச் சேர்த்தது (முன்னர் காணவில்லை) என்பதால் முழு பாடம் 00 → 18 இரு திசைகளிலும் தொடுகிறது.
- **புதிய சின்னப்படங்கள்.** பாடங்கள் 16 மற்றும் 17க்கான சின்னப்படங்கள், மற்றும் புதுப்பிக்கப்பட்ட ரெப்போ சமூக படம் [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (இப்போது இரண்டு புதிய பாடங்களையும் `aka.ms/ai-agents-beginners` URL ஐ விளம்பரம் செய்கிறது).
- **பிரதி சார்புகள்** ([requirements.txt](../../requirements.txt)): பாடம் 17க்காக `foundry-local-sdk` மற்றும் `chromadb` உட்பட.

### மாற்றங்கள்

- **முக்கிய [README.md](./README.md)** பாட அட்டவணை: பாடங்கள் 16 மற்றும் 17 இப்போது அவர்களின் உள்ளடக்கத்துடன் இணைக்கப்பட்டுள்ளன (முன்னர் "விரைவில் வருகிறது"); ரெப்போ படம் `repo-thumbnailv3.png` ஆக மேம்படுத்தப்பட்டது.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: பாடம்-தொடர்பான வழிகாட்டல் மற்றும் கற்றல் பாதைகளுக்கு பாடங்கள் 16 மற்றும் 17 சேர்த்து, மற்றும் "புகை சோதனைகளுடன் வெளியிடப்பட்ட முகவரிகளை சரிபார்த்தல்" பகுதியுடன்.
- **[AGENTS.md](./AGENTS.md)**: பாடக்கணக்கு/விவரணையை (00–18) புதுப்பித்தது, புகை-சோதனை சரிபார்ப்பு பகுதியையும் சேர்த்தது, மற்றும் பாடங்கள் 16/17 எடுத்துக்காட்டு பெயர்நிலை குறிப்புக்கள் சேர்த்தது.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "முன்னர் பாடம்" இப்போது பாடம் 17க்கு எதிர்பார்க்கிறது (முந்தையது பாடம் 15), சங்கிலியை முடிக்கிறது.
- **பழையத்தடையாளமற்ற மாதிரிகளில் ஒரே மாதிரிகருவை பயன்படுத்துதல்.** பாடம் முழுவதும் உள்ள `gpt-4o` / `gpt-4o-mini` குறிப்பிடுக்களை `gpt-4.1-mini` ஆக மாற்றியது — `gpt-4o` (எல்லா பதிப்புகளும்) 2026-ல் ஓய்வு பெறுகிறது. பாடம் 16 இல் மாதிரி வழி அமைப்பில் `gpt-4.1-mini` (சிறியது) மற்றும் `gpt-4.1` (பெரியது) என ஒரு சிறிய/பெரிய மாறுபாடு உள்ளது. Python நோட்புக்குகள் தற்போது மாதிரியை இன்று தேர்வு செய்யும் (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) சுற்றுப்புற மாறிகள் மூலம், கையெழுத்து உள்ளிடுகையை தவிர்த்து.

### குறிப்புகள் மற்றும் தெரிந்த வரம்புகள்

- **நேரடி Azure மீது இயக்கப்படவில்லை.** புதிய பாட நோட்புக்கள் கல்வி எடுத்துக்காட்டுகள்; உங்கள் சொந்த Microsoft Foundry / Foundry Local அமைப்பிற்கு எதிராக இயக்கி சரிபார்க்கவும். புகை-சோதனை வேலைநிரல் பாட முகவரியை வெளியிட்டு Azure OIDC ரகசியங்கள் (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`)ஐ **Azure AI பயனர்** அதிகாரத்துடன் Foundry திட்டப் பகுதிக்கு அமைக்க வேண்டும்.
- **பாடம் 17 உள்ளூர் மட்டுமே.** இது Foundry Responses வழிமுறை இல்லாததால் புகை-சோதனை செயல்பாடு பொருந்தாது; இதில் வரும் நோட்புக் உங்கள் பணியாளர் இயந்திரத்தில் இயக்கி சரிபார்க்கவும்.

## [வெளியிடப்பட்டது] — 2026-07-06

இந்த வெளியீடு பாடத்திட்டத்தை **Azure OpenAI Responses API**க்கு மாற்றுகிறது, **Microsoft Foundry** மற்றும் **Microsoft Agent Framework (MAF)** மீது தயாரிப்பு பெயரிடலை ஒருங்குத்துகிறது, GitHub Modelsஐ ஓய்வு பெறுகிறது, SDK பதிப்புகளை புதுப்பிக்கிறது மற்றும் உள்ளூர் மாதிரிகளுக்கும் Foundry-ல் பிற கட்டமைப்புகளை தங்க செய்யும் புதிய உள்ளடக்கங்களை சேர்க்கிறது.

### சேர்க்கப்பட்டது

- **மாற்று திறன்** — `.agents/skills/` இல் [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) முகவர் திறன் நிறுவப்பட்டது ([Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses) இருந்து), இது குறிப்பு மற்றும் ஸ்கேனர் ஸ்கிரிப்டையும் கொண்டுள்ளது.
- **Foundry Local (மாதிரிகளை சாதனத்தில் இயக்கு)** — [00-course-setup/README.md](./00-course-setup/README.md) இல் புதிய "மாற்று வழங்குநர்: Foundry Local" பகுதி நிறுவல் (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, மற்றும் Microsoft Agent Frameworkக்கு `OpenAIChatClient` மூலம் FoundryLocalManager இணைப்பிற்கு பேசுகிறது.
- **Microsoft Foundry-ல் LangChain / LangGraph முகவர்களைத் தங்கித்தல்** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) இல் புதிய பகுதி மற்றும் இயக்கக்கூடிய எடுத்துக்காட்டு [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) `langchain-azure-ai[hosting]` மற்றும் `ResponsesHostServer` (இயக்கு `/responses` நெறிமுறை) பயன்படுத்தி, [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) அடிப்படையில்.
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md) இல் புதிய "உண்மை உலக எடுத்துக்காட்டு: Microsoft Project Opal" பகுதி, Opal ஐ ஒரு நிறுவன கணினி பயன்பாட்டு முகவரியாக விளக்கும், மற்றும் பாடக் கொள்கைகளுடன் சேர்க்கிறது (மனிதன் கட்டுப்பாட்டில், நம்பிக்கை/பாதுகாப்பு, திட்டமிடல், திறன்கள்).
- **இரண்டாவதாக பாடம் 02 Python எடுத்துக்காட்டு** — [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) சேர்க்கப்பட்டது ("மாற்றப்பட்டது" பார்க்க — பழைய Semantic Kernel நோட்புக்கிலிருந்து இடமாற்றியது) மற்றும் README இல் இணைத்தது.
- **மாதிரிகள் மற்றும் வழங்குநர்கள்** பகுதி [STUDY_GUIDE.md](./STUDY_GUIDE.md) இல் சேர்க்கப்பட்டது.

### மாற்றங்கள்

- **Chat Completions → Responses API (Python).** நேரடியாக மாதிரி அழைத்த எடுத்துக்காட்டு களுக்கு Chat Completions-இலிருந்து Responses APIக்கு மாற்றம் செய்யப்பட்டு (`client.responses.create(input=..., store=False)`, `resp.output_text`) Azure OpenAI நிலையான `/openai/v1/` முனையத்துடன் `OpenAI` கிளையின்ட் பயன்படுத்தப்பட்டது (`api_version` இல்லை). பாதிக்கப்பட்ட எடுத்துக்காட்டுகள்:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — முழு செயல்பாட்டுக் அழைப்பு நடைமுறை (கருவி திட்டவட்டம் Responses வடிவத்திற்கு மாற்றப்பட்டது, கருவி முடிவுகள் `function_call_output`, `max_output_tokens` ஆகியவையாக வந்தன).
- **GitHub Models → Azure OpenAI.** GitHub Models ஓய்வு பெறுகிறது (**ஜூலை 2026**), Responses API-ஐ ஆதரிப்பதில்லை. அனைத்து GitHub Models நிரல் பாதைகள் Azure OpenAI / Microsoft Foundryக்கு மாற்றப்பட்டுள்ளன Python மற்றும் .NET எடுத்துக்காட்டுகளில்:
  - Python: பாடம் 08 வேலைநடை நோட்புக் கள (`01`–`03`), பாடம் 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + இணைப்பான `.md` ஆவணங்கள், மற்றும் பாடம் 08 dotNET வேலைநடை நோட்புக் கள்/`.md` (`01`–`03`) இப்போது `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` `AzureCliCredential` உடன் பயன்படுத்துகின்றன.
- **Semantic Kernel → Microsoft Agent Framework.** பழைய `02-semantic-kernel.ipynb` Microsoft Agent Framework மூலம் Azure OpenAI (Responses API) பயன்படுத்துவதற்காக மறுசீரமைக்கப்பட்டு, `02-python-agent-framework-azure-openai.ipynb` என பெயரிடப்பட்டது.
- **`FoundryChatClient` + `as_agent` அனைத்தும் இணக்கப்படுத்தப்பட்டது.** README மற்றும் நோட்புக் குறியீடு, `AzureAIProjectAgentProvider` குறிப்புகள் பாடம் 01 மற்றும் அமைப்பின் சொந்த எடுத்துக்காட்டுகள் போல ஒன்றிணைக்கப்பட்டன: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` மற்றும் `provider.as_agent(...)`. பாடம் 02–14 READMEs மற்றும் நோட்புக் களில் (உதாரணம்: பாடம் 13 நினைவு, பாடம் 14 எல்லாவற்றும், `11-agentic-protocols/code_samples/github-mcp/app.py`) புதுப்பிக்கப்பட்டது.
- **தயாரிப்பு பெயரிடல்.** ஆங்கில உள்ளடக்கத்தில் முழுமையாக மறுபெயரிடல்:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (மாற்றமில்லாமல்: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", மற்றும் சுற்றுப்புற மாறிகள் பெயர்கள்.)
- **பிரதி சார்புகள்** ([requirements.txt](../../requirements.txt)):
  - `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0` நிரந்தரப்படுத்தப்பட்டன.
  - Responses APIக்கு குறைந்தபட்சமாக `openai>=1.108.1` நிரந்தரப்படுத்தப்பட்டது.
  - `azure-ai-inference` அகற்றப்பட்டது (மாறிய GitHub Models எடுத்துக்காட்டில் மட்டுமே பயன்படுத்தப்பட்டது).
- **சுற்றுச்சூழல் கட்டமைப்பு** ([.env.example](../../.env.example)): GitHub Models மாறிகள் (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) அகற்றப்பட்டன; `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, மற்றும் விருப்ப `AZURE_OPENAI_API_KEY` சேர்க்கப்பட்டன; Microsoft Foundry பெயர்களுக்கு புதுப்பிக்கப்பட்டன.
- **ஆவணங்கள்** — மேலே குறிப்பிட்டவற்றுக்கான புதுப்பிக்கைகள் செய்யப்பட்டன: [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), மற்றும் [STUDY_GUIDE.md](./STUDY_GUIDE.md) (அமைப்பு மாறிகள், சரிபார்க்கும் குறிப்பு, வழங்குநர் வழிகாட்டல், பெயரிடல்).

### நீக்கப்பட்டவை

- GitHub Models ஆரம்ப கட்ட படிகள் மற்றும் சுற்றுச்சூழல் மாறிகள் அமைப்பு ஆவணங்களில் இருந்து நீக்கப்பட்டது (Azure OpenAI / Microsoft Foundry மூலம் மாற்றப்பட்டது).

### பாதுகாப்பு / தனியுரிமை (பொதுவான பகிர்வு சுத்திகரம்)

- ஒரு உண்மையான **Azure சந்தாதாரர் ஐடி**, வள குழு / வள பெயர்கள், மற்றும் Bing இணைப்பு ஐடிகளை வெளியே விட்ட Jupyter நோட்புக் செயற்பாட்டு வெளியீடுகள், கூடவே டெவல் பணியாளர் **உள்ளூர் கோப்பு பாதைகள் மற்றும் பயனர் பெயர்கள்** கீழ்காணும் இடங்களில் எமது அறியப்பட்ட ஒழிக்கப்பட்டது:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- பின்தொடரப்பட்ட ஆங்கில உள்ளடக்கத்தில் எந்த API விசைகள், டோகன்கள், சந்தா ஐடிகள் அல்லது தனிப்பட்ட பாதைகளும் உள்ளதாக இல்லை என்று உறுதி செய்யப்பட்டது (`GITHUB_TOKEN` குறிக்கோள்கள் வேலைப்பிரवाहங்களில் உள்ள GitHub Actions டோக்கன் மற்றும் பாடம் 11 அமைப்பில் GitHub MCP சேவையகம் PAT ஆகும் — இரண்டும் சட்டபூர்வமானவை மற்றும் GitHub மாதிரிகளுடன் தொடர்புடையவை அல்ல).

### குறிப்புகள் மற்றும் அறியப்பட்ட வரம்புகள்

- **செயல்படுத்தப்படவில்லை/முழுமையா இயக்கப்படவில்லை.** இவை API/பெயரிடல் துல்லியத்திற்காக புதுப்பிக்கப்பட்ட கல்வி மாதிரிகள்; அவை நேரடி Azure வளங்களுக்கு எதிராக இயக்கப்படவில்லை, மற்றும் .NET மாதிரிகள் இந்த சூழலில் தொகுக்கப்படவில்லை. உங்கள் சொந்த Microsoft Foundry / Azure OpenAI நிறுவலுடன் சரிபார்க்கவும்.
- **மாதிரி பரவல் Responses API-ஐ ஆதரிக்க வேண்டும்.** `gpt-4.1-mini`, `gpt-4.1`, அல்லது `gpt-5.x` மாதிரி போன்ற பரவலைப் பயன்படுத்தவும். பழைய மாதிரிகள் Responses அடிப்படையான செயல்பாட்டை ஆதரிக்கின்றன, ஆனால் அனைத்து அம்சங்களையும் அல்ல.
- **Agent-framework பதிப்பு.** மாதிரிகள் சமீபத்திய MAF (`>=1.10.0`) இலக்கை குறிக்கின்றன. canonical agent-creation அழைப்பு `client.as_agent(...)`; APIகள் framework வெளியிடப்பட்ட ஆவணங்கள் மற்றும் நிறுவப்பட்ட கட்டமைப்புடன் சரிபார்க்கப்பட்டது. நீங்கள் வேறுபட்ட பதிப்பை பिन்செய்வீர்கள் என்றால், முறை கிடைக்கும் என்பதை உறுதிசெய்யவும் (`as_agent` அல்லது `create_agent`).
- **பாடம் 08 வேலைப்பிரவா் நோட்புக் 04** குற்றதாளாக `AzureAIAgentClient` ( `agent-framework-azure-ai` இலிருந்து) வைத்திருக்கிறது காரணம் அது Microsoft Foundry Agent Service ஆக கைதாகும் கருவிகள் (Bing அடிப்படை, குறியீடு விளக்கி) ஐ பயன்படுத்துகிறது; இது ஏற்கனவே Responses அடிப்படையிலானது.
- **.NET இயல்புநிலை பரவல்.** இரு பாடம் 08 dotNET வேலைப்பிரவு மாதிரிகள் முன்பே குறிப்பிட்ட மாதிரியை கடைசியாக நிரல் செய்தன; இப்போது இயல்பாக `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) ஆகும். ஒரு மாதிரி மில்டிமோடல்/காட்சி உள்ளீட்டில் நம்பிக்கை வைக்கின், `AZURE_OPENAI_DEPLOYMENT` ஐ பொருத்த மாதிரிக்கு அமைக்கவும்.
- **Foundry Local** OpenAI-ஐ பொருந்தும் **உரையாடல் முடிப்புகள்** எண்ட்பாயின்டை வெளிப்படுத்துகிறது மற்றும் உள்ளூர் வளர்ச்சிக்காக திட்டமிடப்பட்டுள்ளது; முழு Responses API அம்சங்களைப் பெற Azure OpenAI / Microsoft Foundry ஐப் பயன்படுத்தவும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->