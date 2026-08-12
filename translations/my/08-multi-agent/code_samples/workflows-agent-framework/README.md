# Microsoft Agent Framework Workflow ဖြင့် Multi-Agent အက်ပ်လီကေးရှင်းများ တူးဆောက်ခြင်း

ဒီသင်ခန်းစာက Microsoft Agent Framework ကို အသုံးပြု၍ multi-agent အက်ပ်လီကေးရှင်းများကို နားလည်ဆွေးနွေးခြင်းနှင့် တည်ဆောက်ခြင်းကို တည်ထောင်နည်းကြောင်း လမ်းညွှန်ပေးမည်။ Multi-agent system ရဲ့ အခြေခံသဘောတရားများကို စတင်လေ့လာပြီး၊ framework ရဲ့ Workflow ကွန်ပွန်နန်း၏ စွမ်းဆောင်ပုံ ရုပ်ပုံအကြောင်း၊ Python နှင့် .NET တွင် workflow ပုံစံအမျိုးမျိုးအတွက် လက်တွေ့ ဥပမာများကို လိုက်လံရှင်းလင်းမည်ဖြစ်သည်။

## 1\. Multi-Agent Systems ကို နားလည်ခြင်း

AI Agent ဆိုတာ standard Large Language Model (LLM) ရဲ့ စွမ်းဆောင်ရည်ကို ကျော်လွန်သည့် စနစ်ဖြစ်သည်။ ၎င်းသည် ပတ်ဝန်းကျင်ကို မြင်တွေ့နိုင်၊ ဆုံးဖြတ်ချက်ချနိုင်ပြီး သတ်မှတ်ထားသော ရည်မှန်းချက်များကို အောင်မြင်ရန် လုပ်ဆောင်ချက်များယူနိုင်သည်။ Multi-agent system ဆိုသည်မှာ ဤ agent များစွာပေါင်းစည်းပြီး တစ်ဦးတည်း agent ၏ လုပ်နိုင်ချက်ထက် မဖြေရှင်းနိုင်သော ပြဿနာကို ပူးပေါင်းဖြေရှင်းသည်။

### ပုံမှန် အသုံးပြုမှု အကြောင်းအရာများ

  * **ရှုပ်ထွေးသော ပြဿနာ ဖြေရှင်းခြင်း**: ကြီးမားသော အလုပ်တစ်ခု (ဥပမာ၊ ကုမ္ပဏီတစ်ခုလုံး အခမ်းအနား စီစဉ်ခြင်း) ကို သီးသန့် အဖွဲအစည်း agent များက တာဝန် အပိုင်းအစ သို့ ခွဲဝေ အောင်လုပ်ခြင်း (ဥပမာ၊ ဘတ်ဂျက် agent, သယ်ယူပို့ဆောင်ရေး agent, မားကက်တင်း agent)။
  * **ဗာချွယ်အကူအညီပေးသူများ**: မူလ ကူညီစွမ်းအား agent သည် အချိန်ဇယားချိန်ညှိခြင်း၊ သုတေသနလုပ်ခြင်း၊ နှင့် ရက်စွဲစာရင်း တင်ခြင်းကဲ့သို့သော တာဝန်များကို အခြားအထူးပြု agent များသို့ ချိတ်ဆက်ပေးခြင်း။
  * **အလိုအလျောက် ရေးသားထုတ်လုပ်မှု**: agent တစ်ဦးသည် မူကြမ်းရေးသားခြင်းလုပ်ဆောင်ပြီး၊ အခြား agent မှ မှန်ကန်မှုနှင့် အသံထွက်ကို ကြည့်ရှုနှင့် ပြန်လည်စစ်ဆေးပြီး၊ တတိယ agent မှ ထုတ်ဝေခြင်းလုပ်ငန်းစဉ်။

### Multi-Agent ပုံစံများ

Multi-agent system များသည် စနစ်ကျပြီး သွင်ပြင်ပုံစံအလိုက် စီစဉ်ဖွဲ့စည်းနိုင်ပြီး၊ ၎င်းတို့၏ ပူးပေါင်းဆောင်ရွက်ပုံကို သတ်မှတ်ပေးနိုင်သည်။

  * **အဆက်လိုက် (Sequential)**: Agent များသည် ကြိုတင်သတ်မှတ်ထားသည့် စဉ်လိုက် အဆင့်ရိုးအတိုင်း လုပ်ဆောင်သည်။ တစ်ဦး၏ ထွက်ရှိမှုသည် ဆက်လက်လုပ်ဆောင်သူ agent ၏ ဝင်ပေးမှုဖြစ်လာသည်။
  * **အချိန်တူ (Concurrent)**: Agent များသည် တာဝန်အပိုင်းအစ တစ်ခုချင်းစီတွင် 병렬 (parallel) ဆောင်ရွက်ပြီး၊ ၎င်းတို့၏ ရလဒ်များကို အဆုံးပေါ်တွင် စုပေါင်းသည်။
  * **အခြေအနေ အကျင့် (Conditional)**: Workflow သည် agent ၏ ထွက်ရှိမှုအရ အကွဲအလဲအတိုင်း လမ်းကြောင်း များကို လိုက်နာသည်၊ if-then-else စကား၍ တူသည်။

## 2\. Microsoft Agent Framework Workflow ၏ ဆောက်လုပ်ပုံ

Agent Framework ၏ workflow စနစ်သည် အဆင့်မြင့် စီမံခန့်ခွဲမှုအင်ဂျင်တစ်ခုဖြစ်ပြီး၊ ဂရပ်ဖ်ပေါ်တွင် ဆောက်လုပ်ထားသော [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf) ကို အသုံးပြုသည်။ လုပ်ထုံးလုပ်နည်းများကို "supersteps" ဟု ခေါ်သော အဆင့်လိုက် အချိန်ညှိများဖြင့် ဆောင်ရွက်သည်။

### အခြေခံ ကွန်ပွန်နန်များ

ဆောက်လုပ်ပုံတွင် အဓိက အပိုင်း သုံးခု ပါဝင်သည်-

1.  **Executors** - ဤသည်မှာ အခြေခံ ပြုလုပ်ရေးယူနစ်များဖြစ်သည်။ ဥပမာများတွင်၊ `Agent` သည် executor တစ်မျိုးဖြစ်သည်။ executor တစ်ခုစီတွင် မက်ဆေ့ချ်ရင်းအမျိုးအစားများအတိုင်း အလိုအလျောက် ခေါ်ဆိုခံရရှိသည့် မက်ဆေ့ချ် handlers များစွာ ပါဝင်နိုင်သည်။
2.  **Edges** - Executors များအကြား မက်ဆေ့ချ်များ စွာလမ်းသွားရာ လမ်းကြောင်းများ သတ်မှတ်သည်။ မည်သည့် သဘောထားများနှင့်အညီ မေးတာများ၏ လမ်းကြောင်းများကို ဂရပ်ဖ်တွင် သွားလာအောင် လုပ်နိုင်ကြောင်း အခြေအနေများပါရှိနိုင်သည်။
3.  **Workflow** - ၎င်းသည် လုပ်ငန်းစဉ်အပြည့်အစုံကို စီမံခန့်ခွဲသော ကွန်ပွန်နန်ဖြစ်ပြီး၊ executor များ၊ edges များနှင့် လုပ်ဆောင်မှုလှုပ်ရှားမှုကို ညွှန်ကြားသည်။ မက်ဆေ့ချ်များသည် တိကျသော အစီအစဉ်ဖြင့် လုပ်ဆောင်ခြင်းကို သေချာစေပြီး ပြသနိုင်မှုအတွက် ဖြစ်စဉ်များကို စီမံ၍ ပြသသည်။

*Workflow စနစ်၏ အခြေခံ အစိတ်အပိုင်းများ၏ ကွက်ပုံ။*

ဤဖွဲ့စည်းတည်ဆောက်ပုံသည် စနစ်အဆင့်မြင့် ဖြစ်ပြီး အသံလိုက်လိုက် ပြုလုပ်ခြင်းများ (sequential chains), 병렬 ပြုလုပ်ခြင်းများအတွက် fan-out/fan-in, နှင့် အခြေအနေအပေါ် အခြေခံသဘောဆောင် switch-case logic အသုံးပြုမှုများ ဖြင့် သင့်တော်သော application များ ဆောက်နိုင်သည်။

## 3\. လက်တွေ့ ဥပမာများနှင့် ကုဒ်များ ဝေဖန်ခြင်း

ယခု ကျွန်တော်တို့ framework ကို အသုံးပြု၍ workflow ပုံစံအမျိုးမျိုးကို မည်သို့ သက်ဆိုင်စွာ တည်ဆောက်မည်ကို သိရှိကြည့်ရှုမည်။ Python နှင့် .NET နှစ်မျိုးစလုံးအတွက် ဥပမာများကို တစ်ခုပြီး တစ်ခုပြပါမည်။

### အမှု ၁: အခြေခံ အဆက်လိုက် Workflow

၎င်းသည် အရေးပေါ် အဆွဲဖြစ်သော ပုံစံဖြစ်၍ agent တစ်ဦးမှ ထွက်ရှိသော အချက်အလက်ကို တိုက်ရိုက်ခြင်းဖြင့် နောက်တစ်ဦးဆီပို့ပေးသည်။ ဥပမာတွင် ဟိုတယ်ရဲ့ `FrontDesk` agent သည် ခရီးသွားအကြံပြုချက် တစ်ခုပေးထားပြီး၊ `Concierge` agent မှ ထိုအကြံပြုချက်ကို ပြန်လည် စစ်ဆေးသည်။

*အခြေခံ FrontDesk -> Concierge workflow ၏ ကွက်ပုံ။*

#### အမှုနောက်ခံ

ခရီးသည်တစ်ဦးသည် ပါရီတွင် အကြံပြုချက်တောင်းခံသည်။

1.  မိမိတိုင်းပြည်ကို သိမ်းထားသော `FrontDesk` agent မှ Louvre ပြတိုက်သွားရန် အကြံပေးသည်။
2.  `Concierge` agent က ထိုအကြံပြုချက်ကို လက်ခံပြီး၊ ပိုပြီး ပြည်သတ် အတွေ့အကြုံရရှိနိုင်သော နေရာတစ်ခုကို အစားထိုး အကြံပြုသည်။

#### Python အကောင်အထည်ဖော်ချက် ပိုင်းစိတ်

Python ဥပမာတွင် ကျွန်တော်တို့ agent နှစ်ဦး၊ တစ်ဦးစီအတွက် အသေးစိတ်ညွှန်ကြားချက်များ ဖြင့် သတ်မှတ် ဖန်တီးပါမည်။

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# ကိုယ်စားလှယ် အခန်းကဏ္ဍများနှင့်ညွှန်ကြားချက်များ သတ်မှတ်ပါ
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# ကိုယ်စားလှယ်အကြောင်းအရာများ ဖန်တီးပါ
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

နောက်တစ်ဆင့်တွင် `WorkflowBuilder` ကို အသုံးပြု၍ ဂရပ်ဖ်ကို တည်ဆောက်မည်။ `front_desk_agent` ကို စတင်နေရာအဖြစ် သတ်မှတ်ပြီး၊ ၎င်း၏ ထွက်ရှိမှုကို `reviewer_agent` သို့ ချိတ်ဆက်သည်။

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

နောက်ဆုံးတွင် workflow ကို သုံးစွဲသူ ရဲ့ စတင်သော မက်ဆေ့ချ်ဖြင့် အကောင်အထည်ဖော်သည်။

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run သည် workflow ကို အကောင်အထည်ဖော်သည်; get_outputs() သည် output executor ၏ရလဒ်ကို 반환သည်။
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) အကောင်အထည်ဖော်ချက် ပိုင်းစိတ်

.NET ၌လည်း ထို logic နှင့် ဆင်တူသည်။ ပထမဦးဆုံး agent များ၏ နာမည်နှင့် ညွှန်ကြားချက်များ သတ်မှတ်ထားသည်။

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

`AzureOpenAIClient` (Responses API) အသုံးပြု၍ agent များ ဖန်တီးပြီး၊ `WorkflowBuilder` သည် `frontDeskAgent` မှ `reviewerAgent` သို့ အဆက်လိုက် အစဉ် သတ်မှတ်ခြင်း ပြုလုပ်သည်။

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetChatClient(deployment).AsAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

သုံးစွဲသူ၏ မက်ဆေ့ချ်ဖြင့် workflow ကို ပြေးဆောင်ရွက်ကာ ရလဒ်များကို ပြန်လည်လွှတ်ပေးသည်။

### အမှု ၂: အဆင့်စဉ်လိုက် Workflow အများကြီး

ဤပုံစံသည် အခြေခံ အဆက်လိုက် အစီအစဉ်ကို တိုးချဲ့သည့် ပုံစံဖြစ်ပြီး အခြား agent များ ပိုမိုပါဝင်သော အဆင့်များဆက်တိုက် လုပ်ဆောင်ရန် သင့်တော်သည်။

#### အမှုနောက်ခံ

သုံးစွဲသူသည် အခန်းတစ်ခန်းရဲ့ ဓာတ်ပုံ တင်ပို့ပြီး ပရိဘောဂ သတ်မှတ်ရန် တောင်းဆိုသည်။

1.  **Sales-Agent**: ဓာတ်ပုံတွင်ပါဝင်သည့် ပရိဘောဂ ပစ္စည်းများကို ဖော်ထုတ်ပြီး စာရင်းပြုစုသည်။
2.  **Price-Agent**: ပစ္စည်းစာရင်းကို သုံးစွဲ၍ ဘတ်ဂျက်၊ အလယ်အလတ်နှင့် အမြင့်ဆုံး ဈေးနှုန်းများဖြင့် အသေးစိတ် ကောက်ချက်များ ပေးသည်။
3.  **Quote-Agent**: ဈေးနှုန်း ပြုစုထားသော စာရင်းကို Markdown စာရွက်စာတမ်း အဖြစ် ပုံစံပြောင်းပြီး ကောက်ချက် ထုတ်ပေးသည်။

*Sales -> Price -> Quote workflow ၏ ကွက်ပုံ။*

#### Python အကောင်အထည်ဖော်ချက် ပိုင်းစိတ်

agent သုံးဦးကို အထူးပြု အခန်းကဏ္ဍများနှင့် သတ်မှတ်ပြီး workflow ကို `add_edge` ဖြင့် `sales_agent` -> `price_agent` -> `quote_agent` အဆက်လိုက် အဖြစ် တည်ဆောက်သည်။

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# အထူးပြုထားသောဆယ့်သုံးဦးသောအေးဂျင့်များကိုဖန်တီးပါ
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# အဆက်မပြတ်သောအလုပ်စဉ်ကိုတည်ဆောက်ပါ
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

input ၌ စာသားနှင့် ဓာတ်ပုံ URI ပါဝင်သည်။ framework မှ agent တစ်ဦး၏ ထွက်ရှိမှုကို နောက်တစ်ဦးသို့ လိုက်လျောညီထွေမှုရှိအောင် ဖြတ်သန်းပေးသည်။

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# အသုံးပြုသူမှစာကို စာသားနဲ့ပုံနှစ်မျိုးပါဝင်ပါတယ်
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# workflow ကို chạy ပါ
events = await workflow.run(message)
```

#### .NET (C\#) အကောင်အထည်ဖော်ချက် ပိုင်းစိတ်

.NET ဥပမာသည် Python နှင့် တူညီသည်။ agent သုံးဦး (salesagent, priceagent, quoteagent) ဖန်တီးပြီး `WorkflowBuilder` မှ အဆက်လိုက် ချိတ်ဆက်ထားသည်။

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent priceagent  = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent quoteagent = azureClient.GetChatClient(deployment).AsAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

သုံးစွဲသူ မက်ဆေ့ချ်သည် ဓာတ်ပုံ ဒေတာ (bytes) နှင့် စာသား prompt ပါသော ပုံစံဖြစ်ပြီး `InProcessExecution.RunStreamingAsync` ဖြင့် workflow ကို စတင်ကာ နောက်ဆုံးထွက်ရှိမှုကို stream မှ သိမ်းဆည်းသည်။

### အမှု ၃: အချိန်တူ Workflow

ဒီပုံစံကို အလုပ်များကို တပြိုင်နက်တည်း ဆောင်ရွက်နိုင်ရန် အသုံးပြုသည်။ fan-out ၏ agent များ စုပေါင်း fan-in အစီအစဉ်ဖြင့် ရလဒ်များ စုဆောင်းသည်။

#### အမှုနောက်ခံ

သုံးစွဲသူသည် Seattle ခရီးစဉ် ကို စီစဉ်ရန် တောင်းဆိုသည်။

1.  **Dispatcher (Fan-Out)**: သုံးစွဲသူ တောင်းဆိုချက်ကို Agent နှစ်ဦးထံ တပြိုင်နက်ပေးပို့သည်။
2.  **Researcher-Agent**: Seattle ၏ ခရီးသွားဖွင့်ဆိုချက်များ၊ ရာသီဥတုနှင့် အရေးပါတ်အချက်များကို သုတေသနလုပ်သည်။
3.  **Plan-Agent**: အသီးသီးနေ့စဉ်ခရီးစဉ်ကို မူတည်၍ အသေးစိတ်အစီအစဉ် ပြုစုသည်။
4.  **Aggregator (Fan-In)**: researcher နှင့် planner ၏ အချက်အလက်များကို စုပေါင်းကာ နောက်ဆုံးအဖြေတစ်ခုအဖြစ် တင်ဆက်သည်။

*Concurrent Researcher နှင့် Planner workflow ၏ ကွက်ပုံ။*

#### Python အကောင်အထည်ဖော်ချက် ပိုင်းစိတ်

`ConcurrentBuilder` သည် ဒီပုံစံဖန်တီးရန် အဆင်ပြေစေနိုင်သည်။ သင့်ရဲ့ agent များကို စာရင်းပေးရုံဖြင့် builder သည် ဖန်တီးပေးသည်။

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder သည် fan-out/fan-in အလုပ်လုပ်နည်းကို ကူညီဖြေရှင်းသည်
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# workflow ကို အကောင်အထည်ဖော်ပါ
events = await workflow.run("Plan a trip to Seattle in December")
```

framework မှ `research_agent` နှင့် `plan_agent` တို့ကို 병렬 ဆောင်ရွက်စေပြီး နောက်ဆုံး ထွက်ရှိမှုများကို စုစည်းသည်။

#### .NET (C\#) အကောင်အထည်ဖော်ချက် ပိုင်းစိတ်

.NET တွင် ထိုပုံစံသည် ပိုပြီး ကြည်ညိုရှင်းလင်းသော ကြေညာချက်များ လိုအပ်သည်။ Custom executors (`ConcurrentStartExecutor` နှင့် `ConcurrentAggregationExecutor`) ကို fan-out, fan-in logic ကို ကိုင်တွယ်ရန် ဖန်တီးသည်။

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

`WorkflowBuilder` မှ `AddFanOutEdge` နှင့် `AddFanInEdge` ကို အသုံးပြုပြီး ဂရပ်ဖ်ကို ဒီ custom executors နှင့် agent များဖြင့် တည်ဆောက်သည်။

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### အမှု ၄: အခြေအနေအပေါ် အခြေခံ Workflow

အခြေအနေအပေါ် အခြေခံ workflow များသည် ရလဒ်အလယ်ပိုင်း အရ အခြေခံကာ လမ်းကြောင်း ဝေခြားမှုများ ထည့်သွင်းအသုံးပြုသည်။

#### အမှုနောက်ခံ

ဒီ workflow သည် နည်းပညာဆိုင်ရာ သင်ခန်းစာတစ်ခုကို အလိုအလျောက် ဖန်တီး၊ ထုတ်ဝေရန် အသုံးပြုသည်။

1.  **Evangelist-Agent**: ပုံစံနှင့် URL များအရ သင်ခန်းစာ မူကြမ်းရေးသားသည်။
2.  **ContentReviewer-Agent**: မူကြမ်းကို စစ်ဆေးသည်၊ စာလုံးရေ ၂၀၀ ကျော်ရှိမရှိ စစ်ဆေးသည်။
3.  **အခြေအနေ ညွှန်ကြားချက်**:
      * **ခွင့်ပြုထားပါက (`Yes`)**: workflow သည် `Publisher-Agent` သို့ ဆက်လုပ်ဆောင်သည်။
      * **ငြင်းဆိုပါက (`No`)**: workflow သည် ရပ်စဲပြီး ငြင်းဆိုမှုအကြောင်းအရာထုတ်ပြန်သည်။
4.  **Publisher-Agent**: မူကြမ်း ခွင့်ပြုပါက content ကို Markdown ဖိုင်အဖြစ် သိမ်းဆည်းသည်။

#### Python အကောင်အထည်ဖော်ချက် ပိုင်းစိတ်

ဤဥပမာတွင် `select_targets` ဟူသော အထူးသီးသန့် function ကို သုံးပြီး conditional logic ကို အကောင်အထည်ဖော်သည်။ ၎င်းကို `add_multi_selection_edge_group` သို့ ပေးပို့ကာ `review_result` ၏ အခြေအနေနှင့် ကိုက်ညီစေရန် အသုံးပြုသည်။

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# ဒီ function က ပြန်လည်သုံးသပ်မှုရလဒ်ပေါ်မူတည်ပြီး နောက်တစ်ဆင့်ကိုဆုံးဖြတ်ပါတယ်
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # အတည်ပြုရင် 'save_draft' executor ကို ဆက်လက်လုပ်ဆောင်ပါ
        return [save_draft_id]
    else:
        # ပယ်ဖျက်ထားရင် 'handle_review' executor ကို သွားပြီး အလုပ်မတက်မှုကို အစီရင်ခံပါ
        return [handle_review_id]

# workflow builder သည် ရွေးချယ်မှု function ကို လမ်းကြောင်းသတ်မှတ်ရန်အသုံးပြုသည်
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # multi-selection edge သည် ဆိုင်းငံ့ ကိုယ်စား အခြေအနေသတ်မှတ်ချက်ကို အကောင်အထည်ဖော်သည်
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Custom executors များဖြစ်သည့် `to_reviewer_result` မှ agent များမှ ရရှိသော JSON output ကို ကြောင်းတစ်ခုပြီးတစ်ခု တိကျသော object များအဖြစ် ပြောင်းစေသည့် function ဖြစ်သည်။

#### .NET (C\#) အကောင်အထည်ဖော်ချက် ပိုင်းစိတ်

.NET ဗားရှင်းတွင်လည်း အခြား function တစ်ခုအား သတ်မှတ်ပြီး `ReviewResult` object ၏ `Result` property ကို စစ်ဆေးသည်။

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

`AddEdge` method ၏ `condition` ပါရာမီတာဖြင့် `WorkflowBuilder` သည် လမ်းကြောင်း နှစ်ခုခွဲခြားဖန်တီးနိုင်သည်။  `publishExecutor` သို့ သွားရန် အခြေအနေ  `GetCondition(expectedResult: "Yes")` မှန်ရပါကသာ လမ်းကြောင်း ချိတ်ဆက်သည်၊ မဟုတ်ပါက `sendReviewerExecutor` သို့ ဆက်သွားပါသည်။

## နိဂုံးချုပ်

Microsoft Agent Framework Workflow သည် စပ်လျဉ်းသော multi-agent system များကို စိတ်ကြိုက် ဖန်တီးနိင်မည့် တည်မြဲခိုင်ခံ့၍ တိုးချဲ့နိုင်သော အခြေခံ ပလက်ဖောင်းဖြစ်သည်။ ၎င်း၏ graph-based architecture နှင့် အခြေခံ ကွန်ပွန်နန်များကို အသုံးပြုကာ Python နှင့် .NET နှစ်မျိုးလုံးတွင် အဆင်ပြေစွာ workflow များအသုံးပြုနိုင်သည်။ သင့် application တွင် အဆက်လိုက်လုပ်ငန်းစဉ်များ၊ 병렬 ဆောင်ရွက်မှုများသို့မဟုတ် မတူညီသော dynamic conditional လုပ်ဆောင်မှုများရှိပါက ၎င်းတို့အား အကောင်းဆုံးထောက်ပံ့ပေးမည့် အခွင့်အလမ်းများ ပေးထားပါသည်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->