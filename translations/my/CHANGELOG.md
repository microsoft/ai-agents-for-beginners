# ပြောင်းလဲမှုများမှတ်တမ်း

**AI Agents for Beginners** သင်တန်းတွင် ထင်ရှားစွာပြောင်းလဲမှုများအားလုံးကိုဤဖိုင်တွင်မှတ်တမ်းတင်ထားသည်။

## [ထုတ်ပြန်ပြီး] — ၂၀၂၆-ခုနှစ် ၇-လ ၁၃-ရက်

ဤထုတ်ပိုးမှုတွင် Microsoft Foundry မှအေဂျင့်များကို အဆင့်မြှင့်တင်ခြင်းနှင့် တစ်လုံးတည်းရှိ workstation သို့ အဆင့်ချန့်တင်ခြင်းကို စုစည်းပြီးမောင်းနှင်ခြင်း (deployment arc) ကိုပြီးစီးစေသည့်သင်ခန်းစာနှစ်ခုအသစ်၊ smoke-test pipeline အသစ်၊ သင်တန်းလမ်းညွှန်ကို ပြန်လည်အသစ်ပြုပြင်ခြင်း၊ သင်ကြားသူကျွမ်းကျင်မှုအသစ်များနှင့် အမှတ်တံဆိပ်ပုံစံကို အပ်ဒိတ်လုပ်ထားသည်။

### ထည့်သွင်းခဲ့သည်

- **သင်ခန်းစာ ၁၆ — Microsoft Foundry ဖြင့် အစွမ်းထက်သောအေဂျင့်များတပ်ဆင်ခြင်း။** အသစ်ထည့်သွင်းသောသင်ခန်းစာ [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) နှင့် production customer-support agent တည်ဆောက်ခြင်း (ကိရိယာများ၊ RAG, memory, ပုံစံချိတ်ဆက်မှု, တုံ့ပြန်မှု cache ထည့်ခြင်း၊ လူ့အတည်ပြုခြင်း၊ အကဲဖြတ်ရန်တံခါး၊ OpenTelemetry ခြေရာခံမှုများ) ပါဝင်သည့် ဖြည့်စွက် Notebook [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb), တီထွင်အားဖြင့်/တပ်ဆင်ခြင်း/အချိန်ပြေး Mermaid ပုံနှိပ်များ၊ အတတ်ပညာစစ်ဆေးမှု၊ အိမ်စာ၊ နှင့် စိန်ခေါ်မှုပါရှိသည်။
- **သင်ခန်းစာ ၁၇ — Foundry Local နှင့် Qwen ဖြင့် ဒေသိယ AI အေဂျင့်များ ဖန်တီးခြင်း။** အသစ်ထည့်သွင်းသည့်သင်ခန်းစာ [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) နှင့် ဖန်တီးရေးသားထားသော Notebook [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) (Qwen function calling ဖြင့် Foundry Local, sandboxed ဖိုင်ကိရိယာများ၊ Chroma ဖြင့် ဒေသိယ RAG၊ ရွေးချယ်နိုင်သော ဒေသိယ MCP) ပါဝင်ပြီး ဒေသိယသာ/ဒေသိယ RAG/ကိရိယာခေါ်မှုအစီအစဉ်များ၊ အတတ်ပညာစစ်ဆေးမှု၊ အိမ်စာနှင့် စိန်ခေါ်မှုပါဝင်သည်။
- **Smoke-test pipeline အသစ်။** အသစ် [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) workflow [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) နှင့် Lessons 01, 04, 05, 16 တွင် တပ်ဆင်နိုင်သောအေဂျင့်များအတွက် [tests/](./tests/README.md) အောက်ရှိ per-lesson အညွှန်းများ၊ စာရင်းများ၊ နှင့် စာမျက်နှာ README တစ်ခု၍ သင်ခန်းစာနှင့် hosted-agent အမည်တိုက်ဆိုင်မှုပါရှိသည်။ သင်ခန်းစာ ১৬ တွင် "Smoke Tests ဖြင့် တပ်ဆင်ပြီးအေဂျင့်ကို စစ်ဆေးခြင်း" အပိုင်းအသစ် ထည့်သွင်းပြီး Lessons 01/04/05 တွင် ရွေးချယ်စရာ smoke-test လင့်ခ်ပါဝင်သည်။
- **သင်ကြားသူ ကျွမ်းကျင်မှုများ။** အသစ် `.agents/skills/` အောက်ရှိ Agent Skills: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (သင်ခန်းစာ ၁၆ နှင့် ၁၇ အကြောင်းအရာများနှင့်အတူ) နှင့် [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (live Microsoft Foundry / Azure OpenAI ပတ်ဝန်းကျင်အတိုင်း notebook စမ်းသပ်ချက်များစစ်ဆေးနည်း)။
- **Notebook စစ်ဆေးမှု runner.** အသစ် [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) သည် Python notebook များအားလုံးကို `nbconvert` ဖြင့် ခေါ်ယူလုပ်ဆောင်ပြီး PASS/FAIL matrix (နှင့် `results.json`) ပုံသဏ္ဍာန်ဖြင့် ဖော်ပြသည်။ repo အမြစ်အတိုင်းမှ သိမ်းဆည်းပြီး Python ကို ရှာတွေ့သည်၊ သင်တန်းပြင်ပ notebook များ (`.venv`, `site-packages`, `translations`, skill template assets) နှင့် `.NET` notebook များကို မပါဝင်စေဘဲ၊ `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, `-Python` option များကို ထောက်ပံ့သည်။
- **သင်တန်းလမ်းညွှန်။** သင်ခန်းစာ ၁၁ မှ ၁၅ အထိ မရှိသည့် Previous/Next lesson link များကို ထည့်သွင်းပြီး သင်တန်းတစ်ခုလုံးကို ၀၀ → ၁၈ တိုင် အဆက်မပြတ် ချိတ်ဆက်ထားသည်။
- **သင်ခန်းစာ thumbnail အသစ်များ။** သင်ခန်းစာ ၁၆ နှင့် ၁၇ အတွက် thumbnail များနှင့် repository ရဲ့ လူမှုရေးပုံစံတစ်ခုအသစ် [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (သင်ခန်းစာနှစ်ခုနှင့် `aka.ms/ai-agents-beginners` URL ကို ကြော်ငြာနေသည်)။
- **လိုအပ်ချက်များ** ([requirements.txt](../../requirements.txt)): သင်ခန်းစာ ၁၇ အတွက် `foundry-local-sdk` နှင့် `chromadb` ထည့်သွင်းခြင်း။

### ပြောင်းလဲမှုများ

- **Main [README.md](./README.md)** သင်ခန်းစာဇယား: သင်ခန်းစာ ၁၆ နှင့် ၁၇ အကြောင်းအရာကို "Coming Soon" မှအကြောင်းအရာတွေသို့ ပြောင်းလဲပြီး repository ၏ပုံစံသည် `repo-thumbnailv3.png` ဖြစ်သွားသည်။
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: သင်ခန်းစာ ၁၆ နှင့် ၁၇ ကို သင်ခန်းစာအလိုက်လမ်းညွှန်နှင့် သင်ယူမှုလမ်းကြောင်းများသို့ ထည့်သွင်းပြီး "Smoke Tests ဖြင့် တပ်ဆင်ပြီးအေဂျင့်ကို စစ်ဆေးခြင်း" အပိုင်းအသစ်ပါဝင်သည်။
- **[AGENTS.md](./AGENTS.md)**: သင်ခန်းစာအရေအတွက်/ဖော်ပြချက် (၀၀–၁၈), smoke-testing validation အပိုင်းနှင့် သင်ခန်းစာ ၁၆/၁၇ နမူနာအမည်များကို ပြင်ဆင်ထားသည်။
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Previous Lesson" သည် ယခင် Lesson ၁၅ မှ Lesson ၁၇သို့ ပြောင်းလဲပြီး ချိတ်ဆက်မှုကို ပိတ်သည်။
- **ဟောင်းကွယ်နေသော မော်ဒယ်များမပါဘဲ စံပြ မော်ဒယ်ကို သတ်မှတ်ခြင်း။** တစ်ခုတည်းသော `gpt-4o`/`gpt-4o-mini` ကို `gpt-4.1-mini` ဖြင့် အစားထိုးပြီး ၂၀၂၆ တွင် `gpt-4o` (ဗားရှင်းအားလုံး) ပယ်ဖျက်မည်။ သင်ခန်းစာ ၁၆ ၏ မော်ဒယ်ချိတ်ဆက်မှု ဥပမာသည် သေးငယ်/ကြီးမား ခြားနားချက်ကို `gpt-4.1-mini` (သေးငယ်) နှင့် `gpt-4.1` (ကြီးမား) အသုံးပြုထားသည်။ Python notebook များသည် မော်ဒယ်အမည်တစ်ခုကို ခိုင်လုံစွာမသုံးဘဲ environment variable များမှ ရွေးချယ်သည် (`AZURE_AI_MODEL_DEPLOYMENT_NAME`/`AZURE_OPENAI_DEPLOYMENT`)။

### မှတ်ချက်များနှင့် သိရှိထားသောကန့်သတ်ချက်များ

- **အသက်ဝင်သော Azure မ်ားအပေါ် အလုပ်မလုပ်ပါ။** သင်ခန်းစာအသစ်များ၏ Notebook များသည် ပညာပေး နမူနာအနေနှင့် Microsoft Foundry / Foundry Local ကိုယ်ပိုင်စနစ်တွင် စမ်းသပ်ပြင်ဆင်ရန် ဖြစ်သည်။ smoke-test workflow သည် သင်ခန်းစာအေဂျင့်ကို တပ်ဆင်ပြီး Azure OIDC လျှို့ဝှက်ချက်များ (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) ကို Foundry project scope တွင် **Azure AI User** အခန်းကဏ္ဍဖြင့် ချိန်ညှိရမည်။
- **သင်ခန်းစာ ၁၇ သည် ဒေသိယသာဖြစ်သည်။** Foundry Responses endpoint မရှိသောကြောင့် smoke-test လုပ်ဆောင်မှု မသင့်တော်ပါ; သင်၏ workstation ပေါ်တွင် Notebook များကို ပတ်သက်၍ စစ်ဆေးရန်လိုသည်။

## [ထုတ်ပြန်ပြီး] — ၂၀၂၆-ခုနှစ် ၇-လ ၆-ရက်

ဤထုတ်ပိုးမှုသည် သင်တန်းကို **Azure OpenAI Responses API** သို့ ပြောင်းရွှေ့ခြင်း၊ **Microsoft Foundry** နှင့် **Microsoft Agent Framework (MAF)** ထွက်ကုန်အမည်ကို စံချိန်တင်ခြင်း၊ GitHub Models ပယ်ဖျက်ခြင်း၊ SDK ဗားရှင်းများကို အပ်ဒိတ်လုပ်ခြင်းနှင့် ဒေသိယ မော်ဒယ်များနှင့် Foundry တွင် အခြား Framework များကို ဟိုစတင်း စနစ်အကြောင်းအသစ်များ ထည့်သွင်းထားသည်။

### ထည့်သွင်းခဲ့သည်

- **ပြောင်းရွှေ့မှု ကျွမ်းကျင်မှု** — `.agents/skills/` အောက်ရှိ [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill ကို ထည့်သွင်းပြီး (အရင်းအမြစ် [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses) မှ) ၊ အညွှန်းနှင့် စကင်နာ script ပါဝင်သည်။
- **Foundry Local (မော်ဒယ်များကို device တွင် တိုက်ရိုက်ပြောင်းလဲသုံးခြင်း)** — [00-course-setup/README.md](./00-course-setup/README.md) တွင် အသစ် “Alternative Provider: Foundry Local” အပိုင်းဖြင့် ထည့်သွင်းခြင်း။ winget / brew ဖြင့် ထည့်သွင်းခြင်း၊ `foundry model run` သုံးခြင်း၊ `foundry-local-sdk` သုံးခြင်း နှင့် Microsoft Agent Framework တွင် `OpenAIChatClient` ဖြင့် FoundryLocalManager ဆက်သွယ်ခြင်း။
- **Microsoft Foundry တွင် LangChain / LangGraph အေဂျင့်များ ဟိုစတင်းခြင်း** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) တွင် အသစ် အပိုင်းပေါင်းထည့်ပြီး `langchain-azure-ai[hosting]` နှင့် `ResponsesHostServer` ( `/responses` ပရိုတိုကော) အသုံးပြုထားသော ဥပမာများ [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) ပါဝင်သည်၊ [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) ကို အခြေခံသည်။
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md) တွင် "လက်တွေ့ဥပမာ: Microsoft Project Opal" အပိုင်းအသစ် ထည့်သွင်းပြီး Opal ကို ဆန်းပြားစွာအသုံးပြုသော ကွန်ပြူတာသုံး အေဂျင့်အဖြစ် ဖော်ပြသည် (လူအဖွဲ့ ထဲတွင်ပါဝင်ခြင်း၊ ယုံကြည်မှု/လုံခြုံရေး, စီမံခန့်ခွဲမှု, ကျွမ်းကျင်မှုများ)။
- **ဒုတိယ သင်ခန်းစာ ၀၂ Python နမူနာ** — [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) အသစ်ထည့်သွင်း၊ ပြောင်းရွှေ့ထားသော Semantic Kernel notebook မှ ရွှေ့ပြောင်းပြီး README တွင် ဖော်ပြသည်။
- **မော်ဒယ်များနှင့် ပံ့ပိုးသူများ** အပိုင်းကို [STUDY_GUIDE.md](./STUDY_GUIDE.md) တွင် ထည့်သွင်းသည်။

### ပြောင်းလဲမှုများ

- **Chat Completions → Responses API (Python).** မော်ဒယ်ကို တိုက်ရိုက် အခေါ်ပြုခဲ့သည့် နမူနာများကို Chat Completions မှ Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`) သို့ ပြောင်းရွှေ့ပြီး Azure OpenAI `/openai/v1/` stabilized endpoint သုံးသည် (version မပါရှိ)။ သက်ရောက်မှုရှိသော နမူနာများမှာ -
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — function-calling လမ်းညွှန်သူမလေးတစ်ခု (tool schema ကို Responses format တွင် သတ်မှတ်၊ tool results ကို `function_call_output`, `max_output_tokens` နှင့် ပြန်လည်ထုတ်ပြန်ခြင်း)။
- **GitHub Models → Azure OpenAI.** GitHub Models သည် ပယ်ဖျက်တောင့်တင်းနေပြီး (၂၀၂၆ ဇူလိုင်တွင် ပယ်ဖျက်မည်) Responses API မထောက်ပံ့တော့ပါ။ GitHub Models ကို Python နှင့် .NET နမူနာများတွင် Azure OpenAI / Microsoft Foundry သို့ ပြောင်းလဲထားသည်။
  - Python: Lesson 08 workflow notebooks (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`)။
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` နှင့် `.md` စာရွက်စာတမ်းများ၊ Lesson 08 dotNET workflow notebooks/`.md` (`01`–`03`) ကို `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` နှင့် `AzureCliCredential` အသုံးပြုသည်။
- **Semantic Kernel → Microsoft Agent Framework.** ယခင် `02-semantic-kernel.ipynb` ကို Microsoft Agent Framework နှင့် Azure OpenAI (Responses API) ဖြင့်ပြန်ရေးပြီး `02-python-agent-framework-azure-openai.ipynb` ဟု အမည်ပြောင်းထားသည်။
- **`FoundryChatClient` + `as_agent` ကို စံပြအသုံးပြုခြင်း။** README နှင့် notebook တွင် `AzureAIProjectAgentProvider` ကိုသုံးမှုသည် သင်ခန်းစာ ၀၁ နှင့် framework ၏ မူလနမူနာများတွင် သုံးသော canonical ပုံစံဖြင့် `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` နှင့် `provider.as_agent(...)` ဖြင့် ပြောင်းလဲထားသည်။ သင်ခန်းစာ ၀၂ မှ ၁၄ ထိ README များနှင့် notebook များကို ပြုပြင်ထားသည် (ဥပမာ- သင်ခန်းစာ ၁၃ မှ Memory, သင်ခန်းစာ ၁၄ များအားလုံး, `11-agentic-protocols/code_samples/github-mcp/app.py`)။
- **ထုတ်ကုန်အမည်များ**။ အင်္ဂလိပ်ဘာသာအချက်အလက်အပြင် အတိအကျ ပြောင်းလဲထားသည်။
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (မပြောင်းလဲသည့်အကြောင်းအရာများ: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", နှင့် environment-variable အမည်များ)
- **လိုအပ်ချက်များ** ([requirements.txt](../../requirements.txt)):
  - `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0` ကို အတက်ခံထားသည်။
  - Responses API အတွက် `openai>=1.108.1` ကို ထည့်သွင်းထားသည်။
  - GitHub Models နမူနာများမှ အသုံးပြုပုံရှိသော `azure-ai-inference` ကို ဖယ်ရှားထားသည်။
- **ပတ်ဝန်းကျင်ချိန်ညှိမှု** ([.env.example](../../.env.example)): GitHub Models ပြင်ပပတ်ဝန်းကျင်များ (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) ကို ဖယ်ရှားပြီး `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, နှင့် ရွေးချယ်စရာ `AZURE_OPENAI_API_KEY` ကို ထည့်သွင်းထားသည်။ Microsoft Foundry အမည်များကို ပြင်ဆင်ထားသည်။
- **စာရွက်စာတမ်းများ** — [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), နှင့် [STUDY_GUIDE.md](./STUDY_GUIDE.md) ကို အထက်ဖေါ်ပြပါ အချက်အလက်များအတိုင်း ပြင်ဆင်ထားသည် (env ရွေ့ပြောင်းချက်များ၊ သက်ဆိုင်မှု စစ်ဆေးမှု နမူနာ၊ ပံ့ပိုးသူလမ်းညွှန်ချက်များ, အမည်ပေါ်မူတည်မှု)။

### ဖျက်သိမ်းခဲ့သည်

- GitHub Models စတင်အသုံးပြုခြင်းအဆင့်နှင့် ပတ်ဝန်းကျင်အပြောင်းအလဲများကို ဖယ်ရှားထားသည် (Azure OpenAI / Microsoft Foundry ဖြင့် အစားထိုးသည်)။

### လုံခြုံရေး / ကိုယ်ရေးအချက်အလက်(အများပြည်သူဝေမျှမှု ဖြုတ်ချခြင်း)

- လက်တွေ့ **Azure subscription ID**, resource-group/ resource အမည်များ၊ Bing ချိတ်ဆက်မှတ်ပါ၊ developer ဒေသိယ ဖိုင်လမ်းကြောင်းများနှင့် အသုံးပြုသူအမည်များ ပါဝင်သော Jupyter notebook အထွက်များကို ဖယ်ရှားထားသည်။
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- တွေ့ရှိချက်အရ API keys, tokens, subscription IDs, သို့မဟုတ် ကိုယ်ပိုင်လမ်းကြောင်းများသည် စောင့်ကြည့်နေသော အင်္ဂလိပ်စာအတွက် မကျန်ရှိကြောင်း အတည်ပြုခဲ့သည် (GITHUB_TOKEN မှ ရည်ညွှန်းချက်များမှာ workflow များအတွက် GitHub Actions token နှင့် Lesson 11 setup မှ GitHub MCP server PAT ဖြစ်ပြီး လက်ခံရရှိနိုင်ပြီး GitHub Models နှင့်ဆက်စပ်မှုမရှိပါ)။

### မှတ်ချက်များနှင့် သိရှိထားသော ကန့်သတ်ချက်များ

- **မပြေးသော/မစုစည်းသော။** ဤနမူနာများသည် API/နာမတ် မှန်ကန်မှု အတွက် ပြင်ဆင်ထားသော ပညာရေးဆိုင်ရာ နမူနာများဖြစ်သည်၊ Azure အသုံးပြုမှုတွင် အသုံးမပြုခဲ့ကြ၊ .NET နမူနာများကိုလည်း ဤပတ်ဝန်းကျင်တွင် စုစည်းခြင်းမပြုခဲ့ပါ။ မိမိ၏ Microsoft Foundry / Azure OpenAI သွင်းထားမှုနှင့် စစ်ဆေးပါ။
- **မော်ဒယ် ဖြန့်ချိမှုသည် Responses API ကို ထောက်ပံ့ရမည်။** `gpt-4.1-mini`, `gpt-4.1`, သို့မဟုတ် `gpt-5.x` မော်ဒယ်တစ်ခုအသုံးပြုပါ။ မဟောင်းမော်ဒယ်များသည် Responses ကို အခြေခံ အလုပ်လုပ်နိုင်သော်လည်း စိတ်ကြိုက် လုပ်ဆောင်ချက်အားလုံး မပါဝင်ပါ။
- **Agent-framework ဗားရှင်း။** နမူနာများသည် နောက်ဆုံး MAF (`>=1.10.0`) ကို ရည်ညွှန်းသည်။ ပုံမှန် agent ဖန်တီးမှုခေါ်ဆိုချက်မှာ `client.as_agent(...)` ဖြစ်ပြီး API များကို framework ထုတ်ပြန်ထားသော စာတမ်းများနှင့် တပ်ဆင်ထားသော ကိုယ်ပိုင် build ဖြင့် စစ်ဆေးထားသည်။ မတူညီသော ဗားရှင်း pin လုပ်လိုပါက အကြံပြုချက်များကို သေချာစွာ စစ်ဆေးပါ (`as_agent` နှင့် `create_agent`)။
- **Lesson 08 workflow notebook 04** သည် `AzureAIAgentClient` (agent-framework-azure-ai မှ) ကို ရည်ရွယ်ပြီး ထိုးထွင်းထားသည်၊ မိုက်ခရိုဆိုဖ် Foundry Agent Service အစီအစဉ်များ (Bing grounding, code interpreter) အသုံးပြုသည်၊ သက်ဆိုင်ရာ Responses အခြေပြုဖြစ်သည်။
- **.NET ပုံသေ ဖြန့်ချိမှု။** Lesson 08 dotNET workflow နမူနာ နှစ်ခုသည် အရင်က အထူးမော်ဒယ်တစ်ခုကို ချိတ်ဆက်ထားခဲ့သည်။ ယခုတွင် `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) ကို ပုံသေထားသည်။ မူလ multimodal/vision input အသုံးပြုမှုရှိပါက `AZURE_OPENAI_DEPLOYMENT` ကို သင့်တော်သော မော်ဒယ်သို့ သတ်မှတ်ပါ။
- **Foundry Local** သည် OpenAI နှင့် ကိုက်ညီသော **Chat Completions** endpoint ကို ဖော်ပြသည်၊ ဒေသတွင်း ဖွံ့ဖြိုးရေးအတွက် ရည်ရွယ်သည်။ Responses API အပြည့်အစုံ လုပ်ဆောင်ချက်အတွက် Azure OpenAI / Microsoft Foundry ကို အသုံးပြုပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->