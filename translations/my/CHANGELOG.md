# အပြောင်းအလဲမှတ်တမ်း

**AI Agents for Beginners** သင်ရိုးကိုယ်ပိုင်သင်ခန်းစာများရှိ အရေးကြီးပြောင်းလဲမှုများအားလုံးကို ဤဖိုင်တွင်မှတ်တမ်းတင်ထားသည်။

## [ထုတ်လုပ်ပြီး] — 2026-07-14

ဤထုတ်လုပ်မှုသည် သင်ခန်းစာကို နောက်ဆုံးထုတ်ခဲ့ပြီး အသုံးမပြုတော့သော မော်ဒယ်၂ခုမှ ကူးပြောင်းသွားပြီး ကျန်ရှိသည့် သင်ခန်းစာမှတ်စုများကို Microsoft Agent Framework API တည်ငြိမ်သော ဗားရှင်းသို့ ပြောင်းရွှေ့ပြီး Python မှတ်စုများကို Microsoft Foundry တင်ထားသည့် live ပတ်ဝန်းကျင်တွင် စစ်ဆေးသေချာထားသည်။

### ပြောင်းလဲခဲ့သည်

- **အသုံးမပြုတော့သည့် မော်ဒယ်များမှ ကူးပြောင်းခြင်း (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`)။** `gpt-4.1` နှင့် `gpt-4.1-mini` တို့အား ၂၀၂၆ အောက်တိုဘာ ၁၄ ရက်မှစ၍ အသုံးမပြုတော့အောင် ထုတ်ပြန်ထားသည်။ သင်ခန်းစာတွင်ပါဝင်သည့် စာရွက်စာတမ်းများ၊ `.env.example`၊ Python/.NET မှတ်စုများနှင့် နမူနာများကို `gpt-5-mini` ဖြင့် အစားထိုးထားသည်။ သင်ခန်းစာ ၁၆ ရဲ့ မော်ဒယ်လမ်းညွှန် ဥပမာတွင် အသေးစား/ကြီးစား ကွာခြားမှုကို `gpt-5-nano` (အသေးစား) နှင့် `gpt-5-mini` (ကြီးစား) ကို အသုံးပြုထားသည်။ တတိယ पक्षဖိုင်များ ([15-browser-use/llms.txt](../../15-browser-use/llms.txt))၊ သမိုင်းဝင် GitHub မော်ဒယ်စာသားများနှင့် `azure-openai-to-responses` ကျွမ်းကျင်မှု မှတ်စုများကို မပြောင်းလဲထားပဲ ကျန်ရှိထားသည်။
- **သင်ခန်းစာ ၁၄ handoff မှတ်စုသည် တည်ငြိမ် API သို့ ကူးပြောင်းထားသည်။** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) သည် `agent_framework.orchestrations.HandoffBuilder` နှင့် `.with_start_agent(...)`၊ `HandoffAgentUserRequest.create_response(...)`၊ `event.type` အခြေခံ သတင်းစီးဆင်းမှုနှင့် `FoundryChatClient` ကို အသုံးပြုထားပြီး ယခင်က ဖယ်ရှားထားသော `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` သင်္ကေတများကို အစားထိုးထားသည်။
- **သင်ခန်းစာ ၁၄ human-in-the-loop မှတ်စုသည် တည်ငြိမ် API သို့ ကူးပြောင်းထားသည်။** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) သည် `ctx.request_info(...)` နှင့် `@response_handler` မှတဆင့် ရပ်နားပြီး (ဖယ်ရှားထားသော `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` ကို အစားထိုး), `WorkflowBuilder(start_executor=..., output_executors=[...])` ဖြင့် တည်ဆောက်၊ `default_options={"response_format": ...}` ဖြင့် စနစ်တကျ ထုတ်လွှင့်ပြီး script ဖြင့် ဖြေရှင်းမှုရှိသော ရေးသားချက်ကို အသုံးပြုပြီး လူထည့်စောင့်ကြည့်မလိုအပ်သော မှတ်စုဖြစ်သည် (input() အသုံးပြု၍ ပိတ်ရန် မလိုအပ်)။
- **ပတ်ဝန်းကျင်အဆင်ပြေမှု စီမံချက်** ([.env.example](../../.env.example)): မော်ဒယ်တင်သွင်းမှု အမည်များကို `gpt-5-mini` သို့ ပြောင်းပြီး `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (သင်ခန်းစာ ၁၆ လမ်းညွှန်မှု) နှင့် ယခင်တွင် မပါဝင်သော `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (သင်ခန်းစာ ၁၅ browser-use) ကို ထည့်သွင်းထားသည်။
- **လိုအပ်ချက်များ** ([requirements.txt](../../requirements.txt)): `agent-framework`, `agent-framework-foundry` နှင့် `agent-framework-openai` ကို `~=1.10.0` မှတ်ထားပြီး၊ နောက်ထပ် စမ်းသပ်ခွင့်ပြုချက် ယူထားသည် (1.11.0 သည် သင်ခန်းစာများအသုံးပြုရာ surface များတွင် စမ်းသပ်မှု ချိုးဖောက် အပြောင်းအလဲများပါရှိသည်)။

### မှတ်ချက်များနှင့် သိရှိရသော ကန့်သတ်ချက်များ

- **Microsoft Foundry သက်ထိမ်းစစ်ဆေးထားသည်။** Python မှတ်စုများကို Microsoft Foundry စီမံကိန်းတစ်ခုတွင် `gpt-5-mini` (နှင့် သင်ခန်းစာ ၁၆ လမ်းညွှန်မှုအတွက် `gpt-5-nano`) အသုံးပြု၍ `nbconvert` ဖြင့် မျက်မှောက်မမြင် စစ်ဆေးထားသည်။ ကျွန်ုပ်တို့၏စီမံကိန်းတွင် အသုံးမပြုတော့သော မော်ဒယ်များကို တင်သွင်းပြီး၊ မှတ်စုများသည် `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` မှ Deployment အမည်ကို ဖတ်ယူသည်။
- **အချို့သင်ခန်းစာများအတွက် ထပ်ဆောင်းအရင်းအမြစ်များ လိုအပ်ခြင်းစိတ်မပျက်။** သင်ခန်းစာ ၀၅ အတွက် Azure AI Search လိုအပ်သည်။ သင်ခန်းစာ ၀၈ အတွက် Bing ပြင်ဆင်မှု workflow (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) တွင် Bing ချိတ်ဆက်မှုနှင့် Microsoft Foundry Agent Service hosted tools လိုအပ်သည်။ သင်ခန်းစာ ၁၃ (Cognee) နှင့် ၁၇ (Foundry Local) သည် မိမိအလိုက် Runtime များ လိုအပ်သည်။

## [ထုတ်လုပ်ပြီး] — 2026-07-13

ဤထုတ်လုပ်မှုသည် တင်သွင်းမှု သင်ခန်းစာ၂ခု (Microsoft Foundry နှင့် workstation တစ်ခုတည်းသို့ အဆင့်ချထားခြင်း) ဖြင့် ပြီးစီးမှု ၊ Smoke-test pipeline အသစ်၊ သင်ခန်းစာ navigation ပြန်လည်သစ်ခြင်း၊ သင်ယူသူ ကျွမ်းကျင်မှုအသစ်များနှင့် အမှတ်တံဆိပ်ကို အပ်ဒိတ်လုပ်ပေးသည်။

### ထည့်စွက်ခဲ့သည်

- **သင်ခန်းစာ ၁၆ — Microsoft Foundry ဖြင့် Scalable Agents တင်သွင်းခြင်း။** သစ်ထည့်သွင်းသင်ခန်းစာ [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) နှင့် ထုတ်လုပ်မှုဖောက်သည်-ထောက်ပံ့မှု agent တစ်ခု တည်ဆောက်သော runnable notebook [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) (ကိရိယာများ၊ RAG, memory, မော်ဒယ်လမ်းညွှန်မှု, ပြန်ကြားမှု cache, လူ့အတည်ပြုခြင်း, သုံးသပ်မှု စနစ်နှင့် OpenTelemetry စိတ်ကြိုက်ပြည့်စုံခြင်း), ဖွံ့ဖြိုးမှု/တင်သွင်းမှု/အသုံးပြုမှု Mermaid diagrams၊ ဗဟုသုတ စစ်ဆေးမှု၊ တာဝန်ပေးမှု နှင့် စိန်ခေါ်မှုပါရှိသည်။
- **သင်ခန်းစာ ၁၇ — Foundry Local နှင့် Qwen ဖြင့် ဒေသန္တရ AI Agents ဖန်တီးခြင်း။** သစ်ထည့်သွင်းသင်ခန်းစာ [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) နှင့် fully on-device အင်ဂျင်နီယာ အကူအညီပေးသူ တည်ဆောက်သော notebook [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) (Foundry Local မှ Qwen function calling, sandboxed ဖိုင်ကိရိယာများ, local RAG with Chroma, ရွေးချယ်ရသော local MCP), local-only / local-RAG / tool-calling diagram များ၊ ဗဟုသုတစစ်ဆေးမှု၊ တာဝန်ပေးမှု နှင့် စိန်ခေါ်မှု ပါဝင်သည်။
- **Smoke-test pipeline**: အသစ်ထည့်သွင်းထားသော [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) workflow [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) နှင့် သင်ခန်းစာ ၀၁၊ ၀၄၊ ၀၅၊ ၁၆ မှ deploy လုပ်နိုင်သော agents များအတွက် catalog များကို [tests/](./tests/README.md) တွင် ထည့်သွင်းထားပြီး၊ စာရင်းတစ်ခုတွင် မှတ်စုတွင်သင့်တော်သည့် သင်ခန်းစာနှင့် hosted-agent အမည်ဖော်ပြထားသည်။ သင်ခန်းစာ ၁၆ တွင် "Smoke Tests ဖြင့် တင်သွင်းထားသော Agent အတည်ပြုခြင်း" အပိုင်း ပါဝင်ပြီး သင်ခန်းစာ ၀၁/၀၄/၀၅ တွင် အလိုအလျောက် smoke-test လမ်းညွှန်ထည့်သွင်းထားသည်။
- **သင်ယူသူ ကျွမ်းကျင်မှုများ။** `.agents/skills/` တွင် အသစ်ထည့်သွင်းပြီး [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (သင်ခန်းစာ ၁၆ နှင့် ၁၇ ညွှန်ကြားချက်များ ပက်ကေး) နှင့် [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (Microsoft Foundry / Azure OpenAI တင်ထားသည့် notebook နမူနာများစစ်ဆေးခြင်း) ပါဝင်သည်။
- **Notebook သေချာစစ်ဆေးမှု runner။** အသစ်ထည့်သွင်းထားသော [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) သည် Python မှတ်စုများအားလုံးကို `nbconvert` ဖြင့် မျက်မှောက်မမြင်စွာ ပြေးဆွဲပြီး PASS/FAIL matrix (နှင့် `results.json`) ကို ထုတ်ပြသည်။ repo root နှင့် Python ကို အလိုအလျောက် တွေ့ရှိပြီး သင်ခန်းစာ မဟုတ်သော မှတ်စုများ (`.venv`, `site-packages`, `translations`, skill template asset များ) နှင့် `.NET` မှတ်စုများကို ပယ်ဖျက်ထားသည်။ `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, နှင့် `-Python` ကို ထောက်ပံ့သည်။
- **သင်ခန်းစာ navigation.** သင်ခန်းစာ ၁၁ မှ ၁၅ အထိ အရင် မပါဝင်ခဲ့သော Previous/Next link များ ထည့်သွင်းကာ သင်ခန်းစာ ၀၀ မှ ၁၈ အထိ ရိုးဝိုင်းချိတ်ဆက်ထားသည်။
- **အသစ်ထည့်သွင်းသည့် Thumbnailsများ။** သင်ခန်းစာ ၁၆ နှင့် ၁၇ အတွက် သင်ခန်းစာ thumbnail များ၊ အတူတူ repository social image အသစ် [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (သစ်ထည့်သွင်းသင်ခန်းစာ နှစ်ခုနှင့် `aka.ms/ai-agents-beginners` URL ကို ကြော်ညာထားသည်) ပါဝင်သည်။
- **လိုအပ်ချက်များ** ([requirements.txt](../../requirements.txt)): သင်ခန်းစာ ၁၇ အတွက် `foundry-local-sdk` နှင့် `chromadb` ထည့်သွင်းထားသည်။

### ပြောင်းလဲခဲ့သည်

- **Main [README.md](./README.md)** သင်ခန်းစာ အချက်အလက်ဇယား: သင်ခန်းစာ ၁၆ နှင့် ၁၇ တွင် ယခုအခါ ကောင်းမွန်သော content link များ (အရင်အခါ "လျင်မြန်စွာ ရောက်ရှိမည်" ဟု မှတ်သား) ပါရှိသည်။ repository image ကို `repo-thumbnailv3.png` သို့ မြှင့်တင်ထားသည်။
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: သင်ခန်းစာ ၁၆ နှင့် ၁၇ ကို သင်ခန်းစာအလိုက် လမ်းညွှန်နှင့် သင်ယူမှု လမ်းကြောင်းများတွင် ထည့်သွင်းပြီး "Smoke Tests ဖြင့် တင်သွင်းထားသော Agents အတည်ပြုခြင်း" အပိုင်း ရှိသည်။
- **[AGENTS.md](./AGENTS.md)**: သင်ခန်းစာ အရေအတွက်/ဖေါ်ပြချက် (၀၀–၁၈) ကို အပ်ဒိတ်လုပ်ပြီး smoke-testing အတည်ပြုမှု အပိုင်း ထည့်သွင်းသည်။ သင်ခန်းစာ ၁၆/၁၇ ၏ နမူနာအမည်ဖေါ်ပြချက်များပါဝင်သည်။
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Previous Lesson" ကို ယခု သင်ခန်းစာ ၁၇ (အရင် ၁၅) သို့ ချိတ်ဆက်ပြီး စနစ်ကို ပိတ်ပင်သည်။
- **သုံးလုံး မော်ဒယ်များအတွက် စံချိန်သတ်မှတ်ထားသော ကိုးကားမှုများ။** သင်ခန်းစာတွင်ပါဝင်သည့် `gpt-4o` / `gpt-4o-mini` ကို `gpt-4.1-mini` ဖြင့် အစားထိုးထားသည် (docs, `.env.example`, Python/.NET မှတ်စုများနှင့် နမူနာများ). `gpt-4o` (အားလုံး ဗားရှင်းများ) သည် ၂၀၂၆ တွင် အသုံးမပြုတော့ပါ။ သင်ခန်းစာ ၁၆ ရဲ့ မော်ဒယ်လမ်းညွှန် ဥပမာတွင် အသေးစား/ကြီးစား အား `gpt-4.1-mini` (အသေးစား) နှင့် `gpt-4.1` (ကြီးစား) ဖြင့် ထားရှိသည်။ Python မှတ်စုများတွင် မော်ဒယ်အမည်ကို မိုက်ခရိုဆိုဖ် Azure openAI မော်ဒယ် အသုံးပြုရန် မှတ်ပုံတင်အမှတ်အသားများ (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) မှ ဖတ်ရွေးရသည်။

### မှတ်ချက်များနှင့် သိရှိရသော ကန့်သတ်ချက်များ

- **Live Azure တွင် စမ်းသပ်မထားပါ။** သစ်ထည့်သွင်းသင်ခန်းစာများမှာ ပညာရေးနမူနာများဖြစ်ပြီး မိမိ Microsoft Foundry / Foundry Local ပြင်ပတပ်ဆင်မှု၌ စမ်းသပ်ရမည်။ Smoke-test workflow သည် သင်ခန်းစာ တွင် အေးဂျင့်ကို တင်သွင်း၍ Azure OIDC လျှို့ဝှက်ချက်များ (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) ကို Microsoft Foundry စီမံကိန်း ကွက်လပ်တွင် Azure AI User အလုပ်အတွက် သတ်မှတ်ထားရန်လိုအပ်သည်။
- **သင်ခန်းစာ ၁၇ သည် ဒေသန္တရသာ ဖြစ်သည်။** ဤသင်ခန်းစာတွင် Foundry Responses endpoint မရှိသဖြင့် smoke-test လည်ပတ်မှု မဟုတ်ပါ။ သင်ခန်းစာကို မိမိ ဒက်စတော့ပ်ပေါ်တွင် မိမိဖြင့် စစ်ဆေးရန်ရှိသည်။

## [ထုတ်လုပ်ပြီး] — 2026-07-06

ဤထုတ်လုပ်မှုသည် သင်ခန်းစာကို **Azure OpenAI Responses API** သို့ ကူးပြောင်း၊ **Microsoft Foundry** နှင့် **Microsoft Agent Framework (MAF)** က ထုတ်ကုန်အမည်များ တူညီစေပြီး GitHub မော်ဒယ်များကို ရုပ်သိမ်း၊ SDK ဗားရှင်းများ ထပ်မံ အပ်ဒိတ်လုပ်ပြီး ဒေသန္တရ မော်ဒယ်များမှာမဟုတ်သော ဖောင်မြားများကို Foundry တွင် တင်သွင်းခြင်း အကြောင်း အမြင်သစ် များ ထည့်သွင်းသည်။

### ထည့်သွင်းခဲ့သည်

- **ကူးပြောင်းခြင်း ကျွမ်းကျင်မှု** — `.agents/skills/` အောက်မှ [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill ကို [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses) မှ ထည့်သွင်းပြီး အသုံးပြုမှုအညွှန်းနှင့် scanner script ပါဝင်သည်။
- **Foundry Local (မော်ဒယ်များကို on-device တွင် ပြေးဆွဲခြင်း)** — [00-course-setup/README.md](./00-course-setup/README.md) တွင် "Alternative Provider: Foundry Local" အပိုင်း အသစ် ထည့်သွင်းထားကာ install လုပ်ခြင်း (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, နှင့် Microsoft Agent Framework မှ `OpenAIChatClient` ကို FoundryLocalManager တွင် ဆက်သွယ်ခြင်း ဖေါ်ပြထားသည်။
- **Microsoft Foundry တွင် LangChain / LangGraph agents ကို တင်သွင်းခြင်း** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) တွင် အသစ်အပိုင်း ထည့်သွင်းပြီး runnable နမူနာတစ်ခု [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) သည် `langchain-azure-ai[hosting]` နှင့် `ResponsesHostServer` (/responses protocol) ကို အသုံးပြုသည်၊ [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) ကို အခြေခံထားသည်။
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md) တွင် "Real-World Example: Microsoft Project Opal" အပိုင်း အသစ်ထည့်ကာ Opal ကို ကုမ္ပဏီတွင် ကြားနာကူညီမှု agent အဖြစ် ဖော်ပြထားသည်။ သင်ခန်းစာ အကြောင်းအရာများ (လူအတည်ပြုမှု, ဘေးကင်းကြပ်ကြားမှု, စီမံချက်, ကျွမ်းကျင်မှုများ) နှင့် မြှင့်တင်တွဲဖက်ထားသည်။
- **သင်ခန်းစာ ၀၂ Python နမူနာ ၂ ခုမြောက်** — ယခင် Semantic Kernel မှတ်စုမှ ကူးပြောင်းထားသည့် [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) ထပ်ထည့်သွင်းပြီး သင်ခန်းစာ README တွင် ချိတ်ဆက်ထားသည်။
- **မော်ဒယ်များနှင့် ပံ့ပိုးသူများ** အပိုင်းကို [STUDY_GUIDE.md](./STUDY_GUIDE.md) တွင် ထည့်သွင်းထားသည်။

### ပြောင်းလဲခဲ့သည်

- **Chat Completions → Responses API (Python).** မော်ဒယ်ကို တိုက်ရိုက် ခေါ်ဆိုထားသည့် နမူနာများကို Chat Completions မှ Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`) သို့ ပြောင်းလဲပြီး၊ Azure OpenAI stable `/openai/v1/` endpoint တွင် `OpenAI` client ကို အသုံးပြုထားသည် (api_version မပါ။) ထိခိုက်မှုရှိသည့် နမူနာများတွင်:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — function-calling ပြည့်စုံမှု (tool schema ကို Responses ပုံစံသို့ ပြောင်းလဲသွားပြီး tool ရလဒ်များကို `function_call_output`, `max_output_tokens` အစရှိသဖြင့် ပြန်လည်ပေးပို့သည်)။

- **GitHub Models → Azure OpenAI.** GitHub Models သည် ပျက်သိမ်းသွားပြီး (အလုပ်မှ ထွက်ခွာမည့်အချိန် **ဇူလိုင် ၂၀၂၆**) Responses API ကို မပံ့ပိုးပါ။ GitHub Models ၏ ကုဒ်လမ်းကြောင်းများအားလုံးကို Python နှင့် .NET စမ်းသပ်မှုများတွင် Azure OpenAI / Microsoft Foundry သို့ ပြောင်းလဲထားသည်။
  - Python: Lesson 08 workflow notebooks (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`)။
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` နှင့် အထက်ပါ `.md` စာရွက်များ၊ Lesson 08 dotNET workflow notebooks/`.md` (`01`–`03`) သည် ယခု `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` နှင့် `AzureCliCredential` ကို အသုံးပြုသည်။
- **Semantic Kernel → Microsoft Agent Framework.** ယခင် `02-semantic-kernel.ipynb` ကို Microsoft Agent Framework နှင့် Azure OpenAI (Responses API) ဖြင့် ပြန်ရေးပြီး `02-python-agent-framework-azure-openai.ipynb` ဟု အမည်ပြောင်းခဲ့သည်။
- **`FoundryChatClient` + `as_agent` သို့ တည်ဆောက်ခြင်း။** README နှင့် notebook ကုဒ်များတွင် `AzureAIProjectAgentProvider` ကို ကိုးကားသော နေရာအားလုံးကို Lesson 01 နှင့် Framework ၏ မူရင်း စမ်းသပ်မှုများတွင် အသုံးပြုသည့် ပုံစံဖြင့်: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` နှင့် `provider.as_agent(...)` ဖြင့် စံပြုပြောင်းလဲထားသည်။ Lesson 02–14 README များနှင့် notebook များ (ဥပမာ၊ Lesson 13 memory, Lesson 14 အားလုံး၊ `11-agentic-protocols/code_samples/github-mcp/app.py`) တွင် ပြင်ဆင်ပြီးဖြစ်သည်။
- **ကုန်ပစ္စည်းအမည်များ။** အင်္ဂလိပ်ဘာသာ စာအချက်အလက်များတွင် အမည်များ ပြောင်းလဲထားသည်။
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (မပြောင်းလဲသေးသည် - "Azure OpenAI", "Azure AI Search", "Azure AI Inference", နှင့် ပတ်ဝန်းကျင် ဗေရီယာများအမည်များ)
- **လိုအပ်သော အပလီကေးရှင်းများ** ([requirements.txt](../../requirements.txt)):
  - `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0` တို့ကို သတ်မှတ်ထားသည်။
  - Responses API အတွက် အနည်းဆုံး သုံးစွဲရန် `openai>=1.108.1` ကို သတ်မှတ်ထားသည်။
  - GitHub Models မှ ရွှေ့ပြောင်းခဲ့သော စမ်းသပ်မှုများတွင်သာ အသုံးပြုသော `azure-ai-inference` ကို ဖယ်ရှားထားသည်။
- **ပတ်ဝန်းကျင် ဆက်တင်များ** ([.env.example](../../.env.example)) တွင် GitHub Models အသုံးပြုထားသော ဗေရီယာများ (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) ကို ဖယ်ရှားပြီး `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, နှင့် ရွေးချယ်စရာ `AZURE_OPENAI_API_KEY` ကို ထည့်သွင်းထားကာ Microsoft Foundry အမည်ပြောင်းခြင်း ပြုလုပ်ရသည်။
- **စာရွက်များ** — [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), နှင့် [STUDY_GUIDE.md](./STUDY_GUIDE.md) တွင် အထက်ဖော်ပြပါအတိုင်း (ပတ်ဝန်းကျင်ဗေရီယာ စနစ် ရေးထည့်ခြင်း၊ စစ်ဆေးရေး snippet, provider လမ်းညွှန်ချက်၊ အမည်ပြောင်းခြင်း) များ ပြင်ဆင်ထားသည်။

### ဖယ်ရှားပြီး

- GitHub Models ၏ onboarding အဆင့်များနှင့် ပတ်ဝန်းကျင်ဗေရီယာများကို setup စာရွက်များမှ ဖယ်ရှားထားပြီး Azure OpenAI / Microsoft Foundry ဖြင့် အစားထိုးထားသည်။

### လုံခြုံရေး / ကိုယ်ရေးအချက်အလက် လုံခြုံမှု (အများပြည်သူ ဝေမျှမှု စစ်ဆေးခြင်း)

- Jupyter notebook များတွင် ထွက်ရှိခဲ့သော အမှန်တကယ်ရှိသော **Azure subscription ID**, resource-group / resource အမည်များ၊ Bing ဆက်သွယ်မှု ID နှင့် developer **တည်နေရာ ဖိုင်လမ်းကြောင်းများ နှင့် အသုံးပြုသူအမည်များ**ကို စာရွက်များတွင် ဖယ်ရှားထားသည်။
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- API key များ၊ token များ၊ subscription ID များ သို့မဟုတ် ကိုယ်ရေးသတင်းအချက်အလက်များ မရှိကြောင်း စစ်ဆေးခဲ့ပြီး ရှိနေသေးသော `GITHUB_TOKEN` တွင် GitHub Actions token (workflows တွင်) နှင့် GitHub MCP server PAT (Lesson 11 setup တွင်) ဖြစ်ကာ GitHub Models နှင့် မဆက်နွယ်ပါ။

### မှတ်ချက်များ နှင့် သိရှိထားသည့် ကန့်သတ်ချက်များ

- **မဖြစ်ရပ်/မပြုလုပ်ထား။** ဤသည်များသည် အတတ်ပညာဆိုင်ရာ စမ်းသပ်မှုများဖြစ်ပြီး API နှင့် အမည်ပြောင်းခြင်းတို့အတွက် ပြင်ဆင်ထားသည်။ Azure ရှိတည်နေရာများတွင် run မလုပ်ခဲ့ခြင်းသဖြင့် .NET စမ်းသပ်မှုများကို ဒီပတ်ဝန်းကျင်တွင် ဂျုံမကုပ်ထားပါ။ သင့် Microsoft Foundry / Azure OpenAI deployment တွင် စစ်ဆေးရန် လိုအပ်သည်။
- **Model deployment သည် Responses API ကို ပံ့ပိုးရမည်။** `gpt-4.1-mini`, `gpt-4.1`, သို့မဟုတ် `gpt-5.x` မော်ဒယ်တစ်ခုကို အသုံးပြုပါ။ ဟောင်းသော မော်ဒယ်များသည် Responses ၏ အခြေခံလုပ်ဆောင်မှုကိုသာ ပံ့ပိုးပြီး feature အားလုံး မပါဝင်နိုင်ပါ။
- **Agent-framework ဗားရှင်း။** စမ်းသပ်မှုများသည် နောက်ဆုံး MAF (`>=1.10.0`) ကို ရည်ညွှန်းသည်။ canonical agent-ဖြစ်စေတာ ကို `client.as_agent(...)` ဟူ၍ ရည်ညွှန်းပြီး API များကို framework ၏ ထုတ်ဝေထားသော စာရွက်များနှင့် တပ်ဆင်ထားသော build နှင့် မျှတမှုရှိကြောင်း အတည်ပြုထားသည်။ သင့်အား အခြားဗားရှင်းတစ်ခုကို သတ်မှတ်ပါက method ရှိမရှိ စစ်ဆေးပါ (`as_agent` နှင့် `create_agent`)။
- **Lesson 08 workflow notebook 04** တွင်  `AzureAIAgentClient` (`agent-framework-azure-ai` မှ) ကို ရည်ရွယ်တည်ရှိစွာ သုံးစွဲထားပြီး Microsoft Foundry Agent Service ၏ hosted tools (Bing grounding, code interpreter) ကို အသုံးပြုသည်။ ယင်းအရာသည် Responses-based ဖြစ်ပြီး ဖြစ်သည်။
- **.NET default deployment.** Lesson 08 dotNET workflow စမ်းသပ်မှု ၂ ခုသည် မော်ဒယ် အသေးစိတ်ကို ကုတ်ထဲတွင် ဖြည့်ထားခဲ့ပြီး ယခုမှာ `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) ကို default သတ်မှတ်ထားသည်။ စမ်းသပ်မှုတစ်ခုတွင် multimodal/vision input ကို အားထားပါက `AZURE_OPENAI_DEPLOYMENT` ကို သင့်လျော်သည့် မော်ဒယ်ဖြင့် သတ်မှတ်ပါ။
- **Foundry Local** သည် OpenAI-compatible **Chat Completions** endpoint ကို ဖော်ပြထားပြီး local development အတွက် ရည်ရွယ်သည်။ Responses API ၏ လုံးဝ လုပ်ဆောင်ချက်များအတွက် Azure OpenAI / Microsoft Foundry ကို အသုံးပြုပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->