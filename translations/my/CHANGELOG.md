# ပြောင်းလဲချက်များ မှတ်တမ်း

**AI Agents for Beginners** သင်တန်း၏ အရေးပါသော ပြောင်းလဲချက်များအားလုံးကို ဒီဖိုင်တွင် မှတ်တမ်းတင်ထားပါသည်။

## [မထွက်သေးသော] — 2026-07-06

ဤထုတ်လုပ်မှုသည် သင်တန်းကို **Azure OpenAI Responses API** သို့ အပြောင်းအလဲပြုလုပ်ပြီး၊ **Microsoft Foundry** နှင့် **Microsoft Agent Framework (MAF)** တွင် ထုတ်ကုန်အမည်များကို တပြားပြားဆင်ခြင်ပြီး၊ GitHub Models ကို သက်တမ်းကုန်စေပြီး၊ SDK ဗားရှင်းများအား သတင်းအချက်အလက်ပြောင်းလဲထားပြီး၊ Foundry ပေါ်တွင် ဒေသခံမော်ဒယ်များနှင့် အခြား Framework များကို ဟိုစတင်လုပ်ခြင်းဆိုင်ရာ အသစ်သော အကြောင်းအရာများ ထည့်သွင်းထားပါသည်။

### ထည့်သွင်းထားသော

- **ပြောင်းရွှေ့မှု ကျွမ်းကျင်မှု** — [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill ကို `.agents/skills/` အောက်တွင် ထည့်သွင်းပြီး၊ ၎င်း၏ ကိုးကားချက်များနှင့် စကင်နာ စာရင်းကိုပါ အပြည့်အစုံ ထည့်သွင်းထားသည်။
- **Foundry Local (ပစ္စည်းပေါ်တွင် မော်ဒယ်များ စိစစ်ခြင်း)** — [00-course-setup/README.md](./00-course-setup/README.md) တွင် အသစ်ထည့်သွင်းထားသော "Alternative Provider: Foundry Local" အပိုင်းမှာ `winget`/`brew` ဖြင့် ထည့်သွင်းခြင်း၊ `foundry model run`၊ `foundry-local-sdk` နှင့် Microsoft Agent Framework တွင် `OpenAIChatClient` ချိတ်ဆက်ထားသည့် `FoundryLocalManager` ကို ဖော်ပြထားသည်။
- **Microsoft Foundry ပေါ်တွင် LangChain / LangGraph အေဂျင့်များ ဟိုစတင်ခြင်း** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) တွင် အသစ်သော အပိုင်းနှင့် langchain-azure-ai[hosting] နှင့် ResponsesHostServer ("/responses" ပရိုတိုကော) ကိုအသုံးပြုသော ပြေးစေသောနမူနာ [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) ပါဝင်သည်၊ [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) ကို အခြေခံထားသည်။
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md) တွင် "အမှန်တကယ်ကြုံတွေ့နိုင်သော ตัวอย่าง: Microsoft Project Opal" အပိုင်း အသစ် ထည့်သွင်းထားပြီး Opal ကို စီးပွားရေး ကွန်ပျူတာအသုံးပြုခြင်း အေဂျင့်အဖြစ် နှင့် သင်တန်း အယူအဆများ (လူအချင်းချင်း လည်ပတ်မှု၊ ယုံကြည်မှု/လုံခြုံမှု၊ စီမံချက်များ၊ ကျွမ်းကျင်မှုများနှင့် ချိတ်ဆက်ထားသည်။
- **အတန်း ၂ Python နမူနာ ဒုတိယ** — ယခင် Semantic Kernel notebook မှ ရွှေ့ပြောင်းထားသော [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) ကို ထည့်သွင်းပြီး အတန်း README တွင် လင့်ခ်ထားသည်။
- **မော်ဒယ်များနှင့် ပေးသွင်းသူများ** အပိုင်းအား [STUDY_GUIDE.md](./STUDY_GUIDE.md) တွင် ထည့်သွင်းထားသည်။

### ပြောင်းလဲထားသောများ

- **Chat Completions → Responses API (Python)** ။ မော်ဒယ်ကို တိုက်ရိုက် ခေါ်သုံးသည့် နမူနာများကို Chat Completions မှ Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`) သို့ ပြောင်းရွှေ့ပြီး၊ `OpenAI` client ကို Azure OpenAI `/openai/v1/` stable endpoint နှင့် (api_version မပါ) အသုံးပြုသည်။ ထိခိုက်သည့် နမူနာများမှာ -
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — function-calling ကိုအပြည့်အစုံ လမ်းညွှန်ကြားခြင်း (tool schema ကို Responses format သို့ပြောင်း၍၊ tool ရလဒ်များကို `function_call_output`, `max_output_tokens` စသည်ဖြင့် ပြန်ပေးသည်)။
- **GitHub Models → Azure OpenAI** ။ GitHub Models သည် ပျက်သီးသွားပြီး (2026 ခုနှစ် ဇူလိုင်) Responses API ကို မပံ့ပိုးတော့ပါ။ Python နှင့် .NET နမူနာများအားလုံးကို Azure OpenAI / Microsoft Foundry သို့ ပြောင်းလဲထားသည် -
  - Python: အတန်း 08 workflow notebooks (`01`–`03`), အတန်း 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`)။
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` နဲ့ ပူးတွဲ `.md` လက်စွဲစာအုပ်များ၊ အတန်း 08 dotNET workflow notebooks/`.md` (`01`–`03`) က AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...) အသုံးပြုပြီး `AzureCliCredential` ဖြင့် လုပ်ဆောင်သည်။
- **Semantic Kernel → Microsoft Agent Framework** ။ ယခင် `02-semantic-kernel.ipynb` ကို Microsoft Agent Framework နှင့် Azure OpenAI (Responses API) အသုံးပြုပြီး ပြန်ရေးသားကာ `02-python-agent-framework-azure-openai.ipynb` ဟု နာမည်ပြောင်းထားသည်။
- **`FoundryChatClient` + `as_agent` အပေါ် စံပြထားသည်** ။ README နှင့် notebook စာမျက်နှာများတွင် `AzureAIProjectAgentProvider` ကိုကိုးကားထားသောနေရာများကို အတန်း 01 နှင့် Framework ၏ ကိုယ်ပိုင် နမူနာများနှင့် လိုက်ဖက်စေရန် `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` နှင့် `provider.as_agent(...)` ကို စံပြအနေဖြင့် သုံးသည်။ Lesson 02–14 README နှင့် notebook များ (ဥပမာ၊ Lesson 13 memory, Lesson 14 ဗားရှင်းအားလုံး, `11-agentic-protocols/code_samples/github-mcp/app.py`) တွင် ပြောင်းလဲထားသည်။
- **ထုတ်ကုန်အမည်များ။** အင်္ဂလိပ်စာဝတ္ထုအတွင်း ပြောင်းလဲထားသည်။
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (မပြောင်းလဲသောအကြောင်းအရာများ - "Azure OpenAI", "Azure AI Search", "Azure AI Inference" နှင့် ပတ်ဝန်းကျင်အတည်ပြု အမည်များ မပြောင်းလဲ)
- **လိုအပ်ချက်များ** ([requirements.txt](../../requirements.txt)) -
  - `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0` ကို ပင်းထားသည်။
  - Responses API အတွက် အနည်းဆုံး ဖြစ်သော `openai>=1.108.1` ကို ပင်းထားသည်။
  - GitHub Models မှ ေရွှ့ေျပာင္းခဲ့သောနမူနာများတွင်သာ အသုံးပြုခဲ့သော `azure-ai-inference` ကို ဖယ်ရှားထားသည်။
- **ပတ်ဝန်းကျင် ဖွဲ့စည်းခြင်း** ([.env.example](../../.env.example)) မှ GitHub Models များ၏ စကားဝှက်များ (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) ကို ဖယ်ရှားပြီး `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, နှင့် ရွေးချယ်စရာ `AZURE_OPENAI_API_KEY` ကို ထည့်သွင်းသည်။ Microsoft Foundry အမည် ၊ အသုံးပြုမှုများ ပြောင်းလဲထားသည်။
- **စာရွက်စာတမ်းများ** — [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), နှင့် [STUDY_GUIDE.md](./STUDY_GUIDE.md) ကို ထည့်သွင်း ပြောင်းလဲထားသည် (ပတ်ဝန်းကျင်အတည်ပြု မော်ကွန်းများ၊ စစ်ဆေးခြင်း၊ ပေးသွင်းသူ လမ်းညွှန်ချက်များ၊ အမည်များ)။

### ဖယ်ရှားထားသော

- GitHub Models onboarding အဆင့်များနှင့် ပတ်ဝန်းကျင် သတ်မှတ်ချက်များကို setup စာရွက်စာတမ်းများမှ ဖယ်ရှားထားသည် (Azure OpenAI / Microsoft Foundry ဖြင့် ပြောင်းပြန်သည်)။

### လုံခြုံရေး / ကိုယ်ရေးကာကွယ်မှု (အများပြည်သူမျှဝေမှု ဖယ်ရှားခြင်း)

- အမှန်တကယ်ရှိသော **Azure subscription ID**, resource-group / resource အမည်များနှင့် Bing ချိတ်ဆက်မှု ID များ၊ ဖက်ရပ်ဖိုင်လမ်းကြောင်းများနှင့် အသုံးပြုသူနာမည်များကို Jupyter notebook အထွက်တွေမှ ဖယ်ရှားပြီးသန့်ရှင်းထားသည်။
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- အဓိက ပြင်ဆင်ချက်မှာ API keys၊ token များ၊ subscription ID များ သို့မဟုတ် ကိုယ်ရေးကာကွယ်မှု လမ်းကြောင်းများ မကျန်မှီသည်ဟု အတည်ပြုထားသည် (GITHUB_TOKEN ကို GitHub Actions token နှင့် Lesson 11 setup တွင် GitHub MCP server PAT အဖြစ် သုံးထားပြီး GitHub Models နှင့် မဆိုင်ပါ)။

### မှတ်ချက်များနှင့် သိရှိထားသော ကန့်သတ်ချက်များ

- **မပြေးဆောင်သုံး/ မဖြည့်သားထားသောနမူနာများ** ။ ဤနမူနာများမှာ API / အမည်ဆိုင်ရာ မှန်ကန်မှုများအတွက် တည်းဖြတ်ထားသော်လည်း၊ လူတိုက်ရိုက် Azure အရင်းအမြစ်များနှင့် မရောက်ရှိသေးဘူး၊ .NET နမူနာများကိုလည်း ဤပတ်ဝန်းကျင်တွင် စမ်းသပ်မလုပ်ထားကြောင်း သိရှိထားပါ။
- **မော်ဒယ် တပ်ဆင်မှုတွင် Responses API ပံ့ပိုးရန် လိုအပ်ပါသည်။** `gpt-4o-mini`, `gpt-4.1`, သို့မဟုတ် `gpt-5.x` မော်ဒယ် မည်သို့မဆို ရွေးချယ်အသုံးပြုပါ။ ဟောင်းသော မော်ဒယ်များသည် Responses အခြေခံ လုပ်ဆောင်ချက်များကိုသာ ပံ့ပိုးပြီး အားလုံးသော လက္ခဏာများကို မပံ့ပိုးပါ။
- **Agent-framework ဗားရှင်း** ။ နမူနာများသည် အများဆုံး အသုံးပြု MAF (`>=1.10.0`) ကို ရည်ညွှန်းပါသည်။ canonical agent-creation ဖုန်းခေါ်ဆိုမှုမှာ `client.as_agent(...)` ဖြစ်ပြီး API များကို Framework ထုတ်ပြန်စာရွက်များနှင့် ထည့်သွင်းထားသော build ဖြင့် အတည်ပြုထားသည်။ အခြားဗားရှင်းကို အသုံးပြုမည်ဆိုပါက `as_agent` နှင့် `create_agent` ဂဏန်းဗေဒကို အတည်ပြုပါ။
- **Lesson 08 workflow notebook 04** သည် Microsoft Foundry Agent Service ဧရိယာ တည်ရှိမှု (Bing grounding, code interpreter) များ အတွက် `AzureAIAgentClient` (agent-framework-azure-ai မှ) ကိုထားရှိထားပြီး Responses အခြေခံဖြစ်သည်။
- **.NET ပုံမှန် တပ်ဆင်မှု** ။ ယခင် Lesson 08 dotNET workflow နမူနာ ၂ ခုသည် `gpt-4o` ကို အတိအကျ ထည့်ထားခဲ့ပြီး၊ ယခုမှာ `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`) ကို ပုံမှန်အသုံးပြုပါသည်။ multimodal/vision input လိုအပ်သောနမူနာများတွင် `AZURE_OPENAI_DEPLOYMENT` သတ်မှတ်ပေးရန် လိုအပ်သည်။
- **Foundry Local** သည် OpenAI-ကိုက်ညီပြီး **Chat Completions** endpoint ကို ဖော်ဆောင်ပေးပြီး ဒေသခံဖန်တီးရေးအတွက် ရည်ရွယ်သည်။ Responses API ၏ အပြည့်အစုံ လက္ခဏာများအတွက် Azure OpenAI / Microsoft Foundry ကို အသုံးပြုပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->