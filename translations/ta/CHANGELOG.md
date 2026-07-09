# மாற்றங்கள் பட்டியல்

**ஆரம்பக்காரர்கள் க்கான AI முகவர்கள்** பாடத்திட்டத்தின் அனைத்து முக்கிய மாற்றங்களும் இந்த கோப்பில் பதிவாகியுள்ளன.

## [வெளியீடு செய்யப்படவில்லை] — 2026-07-06

இந்த வெளியீடு பாடத்திட்டத்தை **Azure OpenAI Responses API** க்கு இடமாற்றம் செய்கிறது, **Microsoft Foundry** மற்றும் **Microsoft Agent Framework (MAF)** இல் தயாரிப்பின் பெயரிடலை ஒரே மாதிரியாக்குகிறது, GitHub மாதிரிகளை முடக்குகிறது, SDK பதிப்புகளை மேம்படுத்துகிறது, மற்றும் உள்ளூர் மாதிரிகள் மற்றும் Foundry மீது பிற கட்டமைப்புகளை வரவழைக்கும் புதிய உள்ளடக்கத்தை சேர்க்கிறது.

### சேர்த்தவை

- **இடமாற்றக்கூறான திறன்** — `.agents/skills/` அடைவில் [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) முகவர் திறன் (Azure-Samples/azure-openai-to-responses யிலிருந்து) நிறுவியுள்ளோம், அதில் அதன் குறிப்பு மற்றும் ஸ்கானர் ஸ்கிரிப்டும் உள்ளடக்கப்பட்டுள்ளது.
- **Foundry உள்ளூர் (மாதிரிகளை சாதனத்தில் இயக்கு)** — [00-course-setup/README.md](./00-course-setup/README.md) இல் புதிய "விருப்ப வழங்குநர்: Foundry Local" பகுதி சேர்க்கப்பட்டுள்ளது, இதில் நிறுவுவது (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, மற்றும் Microsoft Agent Framework இல் `OpenAIChatClient` மூலம் `FoundryLocalManager` வை இணைத்தல் பற்றி சேர்க்கப்பட்டுள்ளது.
- **Microsoft Foundry இல் LangChain / LangGraph முகவர்களை ஹோஸ்ட் செய்தல்** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) இல் புதிய பகுதி மற்றும் `langchain-azure-ai[hosting]` மற்றும் `ResponsesHostServer`-ஐ ( `/responses` நெறிமுறை) பயன்படுத்தி இயங்கக்கூடிய மாதிரி [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) சேர்க்கப்பட்டுள்ளது, இது [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) இன் அடிப்படையில் உள்ளது.
- **Microsoft Project Opal** — Opal ஐ நிறுவன கணினி பயன்படுத்தும் முகவராக வடிவமைத்தும், பாடத்திட்டக் கருத்துகளுடன் (மனிதர் கட்டமைப்பில், நம்பிக்கை/பாதுகாப்பு, திட்டமிடல், திறன்கள்) பொருந்துமாறு அமைத்தும் [15-browser-use/README.md](./15-browser-use/README.md) இல் புதிய "உண்மையான உலக எடுத்துக்காட்டு: Microsoft Project Opal" பகுதி சேர்க்கப்பட்டுள்ளது.
- **இரண்டாவது பாடம் 02 Python மாதிரி** — [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) சேர்க்கப்பட்டுள்ளது (இது "மாற்றப்பட்டவை" பகுதியில் உள்ளது — முந்தைய Semantic Kernel நோட்புக் இடமாற்றப்பட்டு) மற்றும் பாட வகுப்பின் README லிண்க் செய்யப்பட்டுள்ளதில் உள்ளது.
- [STUDY_GUIDE.md](./STUDY_GUIDE.md) இல் **மாதிரிகள் மற்றும் வழங்குநர்கள்** பகுதி சேர்க்கப்பட்டுள்ளது.

### மாற்றப்பட்டவை

- **சட்டையாட்ட கம்ளிஷன்ஸ் → Responses API (Python).** நேரடியாக மாதிரியை அழைத்த மாதிரிகள் Response API க்கு (`client.responses.create(input=..., store=False)`, `resp.output_text`) மாற்றப்பட்டுள்ளன, இவை `OpenAI` கிளையன்ட் பயன்படுத்தி Azure OpenAI `/openai/v1/` நிலையான எண்ட்பாயிண்ட் க்கு அழைக்கப்படுகின்றன (api_version இல்லை). பாதிக்கப்பட்ட மாதிரிகள்:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — முழு ஒழுங்குமுறை அழைக்கும் நடைமுறை (கருவி ஸ்கீமா Responses வடிவத்திற்கு நேர்த்தியாக்கப்பட்டது, கருவி முடிவுகள் `function_call_output`, `max_output_tokens` போன்றவையாக மீண்டும் வழங்கப்பட்டது).
- **GitHub மாதிரிகள் → Azure OpenAI.** GitHub மாதிரிகள் நிறுத்தப்பட உள்ளது (2026 ஜூலைக்கு) மற்றும் Responses API ஐ ஆதரிக்காது. Python மற்றும் .NET மாதிரிகளில் அனைத்து GitHub மாதிரிகளின் குறியீடு பாதைகள் Azure OpenAI / Microsoft Foundry க்கு மாற்றப்பட்டுள்ளன:
  - Python: பாடம் 08 வேலைநடத்திய நோட்பூக்கள் (`01`–`03`), பாடம் 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + சார்ந்த `.md` ஆவணங்கள், மற்றும் பாடம் 08 dotNET வேலைநடத்திய நோட்பூக்கள்/`.md` (`01`–`03`) இப்போது `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` `AzureCliCredential` உடன் பயன்படுத்தப்படுகிறது.
- **Semantic Kernel → Microsoft Agent Framework.** முந்தைய `02-semantic-kernel.ipynb` Microsoft Agent Framework உடன் Azure OpenAI (Responses API) பயன்படுத்தி மறுகட்டமைக்கப்பட்டு `02-python-agent-framework-azure-openai.ipynb` என்ற பெயர்பெற்றுள்ளது.
- **`FoundryChatClient` + `as_agent`-ல் ஒருமுகப்படுத்தப்பட்டது.** README மற்றும் நோட்புக் குறியீட்டில் `AzureAIProjectAgentProvider` குறிப்பிடப்பட்ட இடங்கள் பாடம் 01 மற்றும் கட்டமைப்பின் சொந்த மாதிரிகள் பயன்படுத்தும் பொதுவான முறையில் `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` மற்றும் `provider.as_agent(...)` ஆக ஒருமுகப்படுத்தப்பட்டுள்ளன. பாடம் 02-14 README மற்றும் நோட்பூக்களில் புதுப்பிக்கப்பட்டுள்ளது (உதாரணம், பாடம் 13 நினைவகம், அனைத்து பாடம் 14 நோட்பூக்களும், `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **தயாரிப்பின் பெயரீடு.** ஆங்கில உள்ளடக்கத்தில் முழுக்கவும் பெயர் மாற்றங்கள் செய்யப்பட்டுள்ளன:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (மாற்றமின்றி: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", மற்றும் சுற்றுப்புற மாறி பெயர்கள்.)
- **தேவைகள்** ([requirements.txt](../../requirements.txt)):
  - `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0` பதிப்புகள் பிணைக்கப்பட்டுள்ளன.
  - Responses API க்குப் குறைந்தபட்சமாக `openai>=1.108.1` பிணைக்கப்பட்டுள்ளது.
  - GitHub மாதிரிகள் இடமாற்றிய மாதிரிகள் மட்டுமே பயன்படுத்திய `azure-ai-inference` நீக்கப்பட்டது.
- **சுற்றுப்புற கட்டமைப்பு** ([.env.example](../../.env.example)): GitHub Models மாறியில்கள் (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) நீக்கப்பட்டது; `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, மற்றும் விருப்ப `AZURE_OPENAI_API_KEY` சேர்க்கப்பட்டுள்ளன; பெயரீடு Microsoft Foundry இற்காக புதுப்பிக்கப்பட்டது.
- **ஆவணங்கள்** — மேம்படுத்தப்பட்டுள்ளன [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), மற்றும் [STUDY_GUIDE.md](./STUDY_GUIDE.md) மேலே குறிப்பிடப்பட்டபடி (சுற்றுப்புற மாறிகள், சோதனை குறியீடு உருட்டல், வழங்குநர் வழிகாட்டி, பெயரீடு).

### நீக்கப்பட்டவை

- GitHub Models தொடக்கம் படி மற்றும் சுற்றுப்புற மாறில்கள் அமைப்பு ஆவணங்கள் (Azure OpenAI / Microsoft Foundry மூலம் முற்றிலும் மாற்றப்பட்டது).

### பாதுகாப்பு / தனியுரிமை (பொது பகிர்வு சுத்தம்)

- உண்மையான **Azure பதிவு ஐடி**, வளக் குழு / வள பெயர்கள், மற்றும் பிங்க் இணைப்பு ஐடி, கூடவே மேம்படுத்தும் **உள்ளூர் கோப்பு பாதைகள் மற்றும் பயனர் பெயர்கள்** வெளிப்படுத்திய Jupyter நோட்புக் இயக்கு வெளியீடுகளை முழுமையாக அழிக்கப்பட்டுள்ளன:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- API விசைகள், டோக்கன்கள், பதிவு ஐடிகள் அல்லது தனிப்பட்ட பாதைகள் எதுவும் ஆங்கில உள்ளடக்கத்தில் இல்லை என்பதை ஆய்வு செய்துள்ளோம் (`GITHUB_TOKEN` குறிப்புக்கள் GitHub மாதிரிகள் உடன் தொடர்பில்லாத, workflow டோக்கன்கள் மற்றும் GitHub MCP சர்வர் PAT ல் பாடக் கட்டத்தில் உள்ளன — அனைத்தும் சட்டபூர்வம்).

### குறிப்புகள் மற்றும் அறிந்த வரம்புகள்

- **நடைமுறையாக்கப்படவில்லை/வடிகட்டப்படவில்லை.** இவை API/பெயரீடு துல்லியத்திற்கான கல்வி மாதிரிகள்; நேரடி Azure வளங்களில் இயக்கப்படவில்லை, .NET மாதிரிகள் இந்த சூழலில் வடிகட்டப்படவில்லை. உங்கள் சொந்த Microsoft Foundry / Azure OpenAI இடமாற்றத்தை எதிரொலிக்கவும்.
- **மாதிரி deployment Responses API ஐ ஆதரிக்க வேண்டும்.** `gpt-4o-mini`, `gpt-4.1`, அல்லது `gpt-5.x` மாதிரிகளைப் பயன்படுத்தவும். பழைய மாதிரிகள் Responses அடிப்படைக் செயல்பாட்டை ஆதரிக்கின்றன ஆனால் எல்லா அம்சங்களையும் இல்லை.
- **Agent-framework பதிப்பு.** மாதிரிகள் சமீபத்திய MAF (`>=1.10.0`) இலக்காகும். முகவர் உருவாக்கும் கால் `client.as_agent(...)`; API கள் கட்டமைப்பின் வெளியிடப்பட்ட ஆவணங்கள் மற்றும் நிறுவிய கட்டுமானத்துடன் ஒப்பீடு செய்யப்பட்டுள்ளன. வேறு பதிப்பு பிணைத்தால், `as_agent` மற்றும் `create_agent` இடையேயான பகுபடுத்தலை உறுதிப்படுத்தவும்.
- **பாடம் 08 வேலைநடத்திய நோட்புக் 04** காரணமாக `AzureAIAgentClient` (agent-framework-azure-ai இல் இருந்து) வைத்திருக்கப்படுகிறது ஏனென்றால் அது Microsoft Foundry Agent Service ஹோஸ்ட் செய்த கருவிகளை (பிங்க் நிலைமை, குறியீட்டு விளக்கி) பயன்படுத்துகிறது; இது Responses அடிப்படையிலானது.
- **.NET இயல்புநிலை deployment.** பாடம் 08 dotNET வேலைநடத்திய மாதிரிகள் முன்னர் கடுமையாக `gpt-4o` என குறியாக்கப்பட்டிருந்தன; இப்போது அவை `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`) ஐ இயல்புநிலையில் பயன்படுத்துகின்றன. மாதிரி பன்முக/காட்சி உள்ளீட்டிற்கு அவற்றுக்கேற்ப `AZURE_OPENAI_DEPLOYMENT` அமைக்கவும்.
- **Foundry உள்ளூர்** OpenAI-க்கு விருப்பமான **Chat Completions** எண்ட்பாயிண்ட் வழங்குகிறது மற்றும் உள்ளூர் மேம்பாட்டிற்காக உள்ளது; Responses API முழுமையான அம்சங்களுக்காக Azure OpenAI / Microsoft Foundry ஐ பயன்படுத்தவும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->