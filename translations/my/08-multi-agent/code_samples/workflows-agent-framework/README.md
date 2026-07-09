# Microsoft Agent Framework Workflow နှင့် Multi-Agent အပလီကေးရှင်းများ တည်ဆောက်ခြင်း

ဤသင်ခန်းစာသည် Microsoft Agent Framework ကို အသုံးပြုခြင်းဖြင့် multi-agent အပလီကေးရှင်းများကို နားလည်ပြီး တည်ဆောက်နိုင်ရန် လမ်းညွှန်ပေးပါလိမ့်မည်။ Multi-agent စနစ်များ၏ အခြေခံအယူများကို စူးစမ်းကြည့်ရှုကာ Framework ၏ Workflow အစိတ်အပိုင်း၏ စနစ်တက်ပုံကို ဖော်ထုတ်သည်။ အမျိုးမျိုးသော workflow နမူနာများအတွက် Python နှင့် .NET နှစ်ခုလုံးတွင် လက်တွေ့ ဥပမာများကို လေ့လာကြမည်။

## 1\. Multi-Agent စနစ်များ နားလည်ခြင်း

AI Agent ဆိုသည်မှာ ပုံမှန် Large Language Model (LLM) ၏ လုပ်ဆောင်နိုင်မှုများအပေါ် ဝင်ရောက် လုပ်ဆောင်နိုင်သည့် စနစ်တစ်ခုဖြစ်ကာ၊ ၎င်းသည် ပတ်ဝန်းကျင်ကို သိရှိနိုင်ခြင်း၊ ဆုံးဖြတ်ချက်ချနိုင်ခြင်းနှင့် သတ်မှတ်ထားသောရည်မှန်းချက်များကို ပြည့်မှီရန် လုပ်ဆောင်ချက်များ ရယူနိုင်ပါသည်။ Multi-agent စနစ်မှာ ဤ agent များစွာပေါင်းစည်းပြီး တစ်ဦးတည်း agent တစ်ခုဖြင့် ကျေရာမဖြေရှင်းနိုင်သော ပြဿနာများကို ပူးပေါင်းဖြေရှင်းသည့် စနစ်ဖြစ်သည်။

### ပုံမှန် အသုံးချမှုပုံစံများ

  * **ရှုပ်ထွေးသော ပြဿနာ ဖြေရှင်းခြင်း**: ကြီးမားသော တာဝန်တစ်ခု (ဥပမာ၊ ကုမ္ပဏီတစ်ခုလုံး ပွဲစီစဉ်ခြင်း) ကို အထူးပြု agent များ (ဥပမာ၊ ဘတ်ဂျက် agent၊ ဂုဏ်သတ္တိ agent၊ စျေးကွက် agent) သည် ဂဏန်းပိုင်းခွဲ၍ လုပ်ဆောင်သည်။
  * **အိမ်သာနာခံသူများ (Virtual Assistants)**: အဓိက အကူအညီ agent သည် အချိန်ဇယားသတ်မှတ်ခြင်း၊ သုတေသနလုပ်ခြင်းနှင့် စိတ်ကြိုက် မှားနားစာရင်းဖော်ခြင်း တို့ကို အထူးပြု agent များထံအပ်နှံပေးသည်။
  * **အလိုအလျောက် အကြောင်းအရာ ဖန်တီးခြင်း**: agent တစ်ယောက်သည် အကြောင်းအရာစာမူရေးသည်၊ နောက်တစ်ယောက်သည် တိကျမှုနှင့် ဆန္ဒ ပြန်လည်သုံးသပ်သည်၊ တတိယ agent သည် ထုတ်ဝေသည်။

### Multi-Agent ပုံစံများ

Multi-agent စနစ်များသည် အပြန်အလှန်ဆက်သွယ်မှု နည်းလမ်းများအား ဆုံးဖြတ်သော ပုံစံနည်းမျိုးစုံဖြင့် စီမံနိုင်သည်။

  * **စဉ်ဆက်ဖြစ်**: Agent များသည် ကြိုတင်သတ်မှတ်ထားသည့် အဆင့်လိုက်အတန်းအမှတ်စဥ်ဖြင့် လုပ်ဆောင်ကြသည်။ Agent တစ်ယောက်၏ ထုတ်အပေါက်သည် နောက်တစ်ယောက်အတွက် Input ဖြစ်သည်။
  * **အချိန်တပြိုင်နက်**: Agent များသည် တာဝန်တစ်ခု၏ မတူညီသော အပိုင်းများကို တပြိုင်နက်တည်း လုပ်ဆောင်ပြီး ၎င်း၏ ရလဒ်များကို အဆုံးတွင်စုစည်းသည်။
  * **ကွဲပြားမှုရှိသောအခြေအနေ**: Workflow သည် agent ထုတ်အပေါက်အပေါ် အခြေခံ၍ မတူညီသော လမ်းကြောင်းများကို လိုက်နာသည်၊ if-then-else ကြောင့်ပါပဲ။

## 2\. Microsoft Agent Framework Workflow စနစ်တည်ဆောက်ပုံ

Agent Framework ၏ workflow စနစ်သည် multi-agent များအကြား ရှုပ်ထွေးသော အပြန်အလှန် ဆက်သွယ်မှုများကို စီမံရန် ဖန်တီးထားသည့် ကီယန်းတင်စွမ်းဆောင်သော ဂရပ်စီစဉ်စက်တစ်ခုဖြစ်သည်။ ၎င်းသည် [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf) ကို အသုံးပြုသည့် ဂရပ်ပေါ်တွင် ဆောက်လုပ်ထားပြီး "supersteps" ဟုခေါ်သော ထပ်တူညီသော အဆင့်များဖြင့် ချိတ်ဆက်လုပ်ဆောင်သည်။

### အဓိကအစိတ်အပိုင်းများ

ထိပ်တန်းအစိတ်အပိုင်း သုံးခု ပါဝင်သည်။

1.  **Executors**: ၎င်းတို့သည် အခြေခံ စီမံခန့်ခွဲမှုယူနစ်ဖြစ်သည်။ ဥပမာများ၌ `Agent` တစ်မျိုးသော executor ဖြစ်သည်။ executor တစ်ခုစီတွင် မက်ဆေ့ခ်ျအမျိုးအစားအပေါ်အခြေခံပြီး အလိုအလျောက်ခေါ်ဆိုသော မက်ဆေ့ခ်ျလိုင်ဒါများရှိနိုင်သည်။
2.  **Edges**: executors များအကြား မက်ဆေ့ခ်ျများ လမ်းကြောင်းကို သတ်မှတ်သည်။ စည်းမျဉ်းများပါရှိနိုင်ပြီး အချက်အလက်များကို လွတ်လပ်စွာ တစ်နေရာမှတစ်နေရာသို့ ပို့ဆောင်လှည့်ပတ်နိုင်သည်။
3.  **Workflow**: ၎င်းသည် လုပ်ငန်းစဉ်တစ်ခုလုံးကို စီမံခန့်ခွဲသည့်အစိတ်အပိုင်းဖြစ်ပြီး executors, edges များနှင့် လုပ်ငန်းစဉ်အပြေး ကို ထိန်းသိမ်းစောင့်ရှောက်သည်။ မက်ဆေ့ခ်ျများ ရှေ့နောက်လိုက်မှုမှန်ကန်စွာ ရှောင်ရှားပေးပြီး ကြည့်ရှုနိုင်ရေး အတွက် အဖြစ်များကို လွှင့်ပေးသည်။

*Workflow စနစ်၏ အဓိကအစိတ်အပိုင်းများကို ဖော်ပြထားသော ခြပုံရိတ် ကြည့်ရန်။*

ဤဖွဲ့စည်းပုံသည် စဉ်ဆက်လိုက် ဆက်စပ်ခြင်းများ၊ ဘေးဘက်ပိုင်း လုပ်ဆောင်ခြင်းအတွက် fan-out/fan-in နှင့် conditional လမ်းကြောင်းအတွက် switch-case logic နည်းပညာများကို အသုံးပြု၍ အင်အားပြင်းသော နှင့် တိုးတက်နိုင်သော အပလီကေးရှင်းများ ဖန်တီးရ မည်ဖြစ်သည်။

## 3\. လက်တွေ့ ဥပမာများနှင့် ကုဒ် ဖတ်ရှုခြင်း

လက်ရှိတွင် Framework ကို အသုံးပြု၍ အမျိုးမျိုးသော workflow ပုံစံများကို ဘယ်လို အကောင်အထည်ဖော်မည်ကို စတင်ကြည့်ရန်။ Python နှင့် .NET ကုဒ်ကို ဥပမာတစ်ခုချင်း စီတွင် ကြည့်မည်။

### မူလကိစ္စ ၁: အခြေခံ စဉ်ဆက်ဖြစ် Workflow

၎င်းသည် အလွန်ရိုးရှင်းသော ပုံစံဖြစ်ပြီး Agent တစ်ဦး၏ ထုတ်အပေါက်ကို တိုက်ရိုက် နောက်တစ်ဦးထံ ပို့ဆောင်သည်။ ကျွန်ုပ်တို့၏ နမူနာမှာ ဟိုတယ် `FrontDesk` agent တစ်ယောက်သည် ခရီးစဉ် အကြံပြုချက်အနေဖြင့် ထုတ်ဖော်ပြီး `Concierge` agent မှ ပြန်လည်သုံးသပ်သည်။

*အခြေခံ FrontDesk -> Concierge workflow ၏ ခြပုံရိတ်။*

#### နမူနာ နောက်ခံ

ခရီးသွားတစ်ဦးသည် ပဲရစ်မြို့၌ အကြံပြုချက် တောင်းဆိုသည်။

1.  `FrontDesk` agent သည် လိပ်စာတိုပြီး Louvre ပြတိုက်ကို သွားရောက်အကြံပြုသည်။
2.  `Concierge` agent သည် အမှန်တကယ်ရောက်ရှိမှုကို အရေးထားသောအတွက် အကြံပြုချက်ကို လက်ခံပြီး ပြန်လည်သုံးသပ်ကာ ခရီးသွားများ မရောက်သော ဒေသတွင် လမ်းညွှန်ချက်များ ပေးသည်။

#### Python အကောင်အထည်ဖော်မှု သုံးသပ်ချက်

Python ဥပမာတွင် Agent နှစ်ခုကို အဲ့ဒီလို သတ်မှတ်ပြီး ဖန်တီးသည်။

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# အေးဂျင့်တာဝန်များနှင့် ညွှန်ကြားချက်များ သတ်မှတ်ပါ
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# အေးဂျင့်အခြေအနေများ ဖန်တီးပါ
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

WorkflowBuilder ကို အသုံးပြုပြီး ဂရပ်ကို တည်ဆောက်သည်။ `front_desk_agent` ကို စတင်နေရာအဖြစ် သတ်မှတ်ပြီး ဂရပ်တွင် ၎င်း၏ ထုတ်အပေါက်ကို `reviewer_agent` သို့ ချိတ်ဆက်သည်။

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

နောက်ဆုံးတွင် workflow ကို စတင်၍ အသုံးပြုသူ၏ စကား၀ိုင်း ဖြင့် ဆောင်ရွက်သည်။

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run သည် workflow ကို အကောင်အထည်ဖော်သည်။ get_outputs() သည် output executor ၏ရလဒ်ကို ပြန်လည်ပေးပါသည်။
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) အကောင်အထည်ဖော်မှု သုံးသပ်ချက်

.NET အသုံးပြုပုံတွင်လည်း တူညီသော နည်းလမ်းဖြင့် လုပ်ဆောင်တယ်။ Agent များအမည်နှင့် ညွှန်ကြားချက်များကို ကွန်စတန့် အဖြစ် သတ်မှတ်သည်။

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

`AzureOpenAIClient` (Responses API) ကို အသုံးပြုပြီး agent များ ဖန်တီးပြီး `WorkflowBuilder` သည် `frontDeskAgent` မှ `reviewerAgent` သို့ စဉ်ဆက်လိုက်အတိုင်း လမ်းကြောင်း ထည့်သွင်းသည်။

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

workflow ကို အသုံးပြုသူ၏ စကား၀ိုင်းဖြင့် လည်ပတ်၍ ရလဒ်များကို ပြန်လည်ပို့ပေးသည်။

### မူလကိစ္စ ၂: အဆင့်မတူညီသော စဉ်ဆက်ဖြစ် Workflow

ဤပုံစံသည် အခြေခံစဉ်ဆက်ဖြစ် Workflow ကို တိုးချဲ့ကာ Agent များ ပိုများစေသည်။ အဆင့်အတန်း မတူညီသော ပြုပြင်ပြောင်းလဲမှုများ သို့မဟုတ် ပြောင်းလဲမှုများလိုအပ်သော လုပ်ငန်းစဉ်များအတွက် အကောင်းဆုံးဖြစ်သည်။

#### နမူနာ နောက်ခံ

အသုံးပြုသူသည် အိမ်အခန်းဓာတ်ပုံတစ်ပုံ ပေးပြီး ပရိဘောဂအစားထိုးနှုန်းကို တောင်းဆိုသည်။

1.  **Sales-Agent**: ဓာတ်ပုံအတွင်း ပရိဘောဂပစ္စည်းများကို သတ်မှတ်ပြီး စာရင်း ရေးဆွဲသည်။
2.  **Price-Agent**: ပစ္စည်းစာရင်းကို လက်ရှိဈေးနှုန်းအကြောင်းကို ဖော်ပြပြီး ဘတ်ဂျက်၊ အလယ်အလတ်နှင့် အဆင့်မြင့်ရွေးချယ်စရာများ ထည့်သွင်းထားသည်။
3.  **Quote-Agent**: စျေးနှုန်းဖော်ပြချက်ပါ စာရင်းကို Markdown ဖိုင်အဖြစ် ကောင်းမွန်စွာ ပုံဖော်သည်။

*Sales -> Price -> Quote workflow ၏ ခြပုံရိတ်။*

#### Python အကောင်အထည်ဖော်မှု သုံးသပ်ချက်

ဝါရင့် ထူးခြားသော အခန်းကဏ္ဍ ဖြင့် Agent သုံးယောက် ထားရှိသည်။ Workflow ကို `add_edge` ဖြင့် Agent အသစ်တစ်ဆင့်စီ ဆက်သွယ်သည်။ `sales_agent` -> `price_agent` -> `quote_agent` ဖြစ်သည်။

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# သီးသန့်အေးဂျင့်သုံးယောက် ဖန်တီးပါ
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# စဉ်လိုက်လုပ်ငန်းစဉ်ကို တည်ဆောက်ပါ
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Input သည် စာသားနှင့် ဓာတ်ပုံ URI ပါဝင်သော `ChatMessage` ဖြစ်သည်။ Framework သည် agent တစ်ယောက်၏ ထုတ်အပေါက်ကို နောက်တစ်ခုထံ စဉ်ဆက်လိုက် ပို့ဆောင်သည်။ နောက်ဆုံးတွင် မူပိုင်စာချုပ် ထုတ်ပေးသည်။

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# အသုံးပြုသူ၏စာတိုတွင် စာပိုဒ်နှင့် ပုံတစ်ပုံ ပါဝင်သည်
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# လုပ်ငန်းစဉ်ကို အမည်ပြုပါဦး
events = await workflow.run(message)
```

#### .NET (C\#) အကောင်အထည်ဖော်မှု သုံးသပ်ချက်

.NET ဥပမာသည် Python ဗားရှင်းနှင့် ဆင်တူသည်။ Agent သုံးယောက် (`salesagent`, `priceagent`, `quoteagent`) ဖန်တီးသည်။ `WorkflowBuilder` သည် ထိုများကို စဉ်ဆက်လိုက် ချိတ်ဆက်သည်။

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent priceagent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent quoteagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

အသုံးပြုသူ၏ စာသား နှင့် ဓာတ်ပုံဒေတာ (bytes အဖြစ်) ကို ထည့်သွင်းပြီး `InProcessExecution.StreamAsync` နည်းလမ်းဖြင့် workflow စတင်ကာ နောက်ဆုံးထွက်သည် stream မှ ဖမ်းဆီးသည်။

### မူလကိစ္စ ၃: အချိန်တပြိုင်နက် Workflow

ဤပုံစံသည် အလုပ်အချိန်ကို လျှော့ချရန် တချိန်တည်းလုပ်နိုင်သော တာဝန်များအတွက် အသုံးပြုသည်။ အများအပြား agent များသို့ "fan-out" လုပ်ပြီး ရလဒ်များကို "fan-in" ဖြင့် စုစည်းသည်။

#### နမူနာ နောက်ခံ

သုံးစွဲသူသည် Seattle ခရီးစီစဉ်ပေးရန် တောင်းဆိုသည်။

1.  **Dispatcher (Fan-Out)**: အသုံးပြုသူ၏ တောင်းဆိုမှုကို Agent နှစ်ယောက်ထံ တချိန်တည်း ပို့သည်။
2.  **Researcher-Agent**: Seattle မြို့၏ ဆွဲဆောင်မှုများ၊ ရာသီဥတုနှင့် အခြေခံ စဉ်းစားချက်များကို သုတေသန လုပ်သည်။
3.  **Plan-Agent**: တစ်နေ့ရက်စဉ် ခရီးစဉ် ဝင်မည့် အပြည့်အစုံ စီမံတည်ဆောက်သည်။
4.  **Aggregator (Fan-In)**: သုတေသနလုပ်သူနှင့် စီမံသူ ထုတ်အပေါက်များကို စုစည်းပြီး နောက်ဆုံး တင်ပြသည်။

*Concurrent Researcher နှင့် Planner workflow ၏ ခြပုံရိတ်။*

#### Python အကောင်အထည်ဖော်မှု သုံးသပ်ချက်

`ConcurrentBuilder` သည် ဤပုံစံ ဖန်တီးရာကို လွယ်ကူစေသည်။ ပါဝင်သော agent များကို စာရင်းပေးရုံဖြင့် fan-out နှင့် fan-in လုပ်ဆောင်ချက်များကို အလိုအလျောက် ဖန်တီးပေးသည်။

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder က fan-out/fan-in သဘောတရားကို ကိုင်တွယ်သည်
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Workflow ကို chạy ပြုလုပ်ပါ။
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework သည် `research_agent` နှင့် `plan_agent` ကို တပြိုင်နက် လုပ်ဆောင်ကြပြီး ၎င်းတို့ရလဒ်များကို စာရင်းအဖြစ် စုဆောင်းထားသည်။

#### .NET (C\#) အကောင်အထည်ဖော်မှု သုံးသပ်ချက်

.NET တွင် ဤပုံစံသည် ပိုမို ပြတ်သားသော သတ်မှတ်ချက်လိုအပ်ပါသည်။ အထူးပြု Custom Executors (`ConcurrentStartExecutor` နှင့် `ConcurrentAggregationExecutor`) များ Fan-out နှင့် Fan-in ကို တာဝန်ယူပါသည်။

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

ထို့နောက် `WorkflowBuilder` သည် `AddFanOutEdge` နှင့် `AddFanInEdge` ကို အသုံးပြုပြီး ဤ executors နှင့် agents များကို ဂရပ်ဖွဲ့စည်းသည်။

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### မူလကိစ္စ ၄: အခြေအနေပါ Workflow

အခြေအနေပါ Workflow များတွင် လမ်းခွဲခြင်း သဘောတရားများ ပါရှိကာ များသောအားဖြင့် အလယ်အလတ် ရလဒ်အပေါ် မှီခို၍ သွေးကြောပုံသဏ္ဍာန် ထွက်ပေါ်စေသည်။

#### နမူနာ နောက်ခံ

လုပ်ငန်းစဉ်သည် နည်းပညာ သင်ခန်းစာ တစ်ခု ရေးသားပြီး ထုတ်ဝေလုပ်ခြင်းကို အလိုအလျောက် ကျစ်လစ်စွာ လုပ်ဆောင်တယ်။

1.  **Evangelist-Agent**: သတ်မှတ်ထားသော အကြောင်းအရာ နှင့် URL များအပေါ် အခြေခံ၍ သင်ခန်းစာ မူကြမ်းရေးဆွဲသည်။
2.  **ContentReviewer-Agent**: မူကြမ်းကို စိစစ်သည်။ စာ စာရေအကျယ်က 200 စကားထက် အများကြီးမဟုတ်ကြောင်း စစ်ဆေးသည်။
3.  **အခြေအနေ လမ်းခွဲ**:
      * **လက်ခံသည် (ဟုတ်တယ်)**: Workflow သည် `Publisher-Agent` ဆီသို့ ဆက်လက်သွားသည်။
      * **ငြင်းဆိုသည် (မဟုတ်)**: Workflow ရပ်နားပြီး ငြင်းဆိုသည့်အကြောင်းရင်းကို ထုတ်ပေးသည်။
4.  **Publisher-Agent**: မူကြမ်းလက်ခံပါက Markdown ဖိုင်အဖြစ် အကြောင်းအရာကို သိမ်းဆည်းသည်။

#### Python အကောင်အထည်ဖော်မှု သုံးသပ်ချက်

ဤဥပမာသည် အခြေအနေ logic ကို အကောင်အထည်ဖော်ရန် `select_targets` ဆိုသော custom function ကို အသုံးပြုသည်။ ၎င်းမှာ `add_multi_selection_edge_group` သို့ ပေးပို့ပြီး reviewer's output ထဲမှ `review_result` များ ကို ကြည့်၍ workflow ကို ဦးတည်စေသည်။

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# ဒီ function က သုံးသပ်မှုရလဒ်အပေါ်မူတည်ပြီး နောက်တစ်ဆင့်ကိုဆုံးဖြတ်တယ်
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # အတည်ပြုရင် 'save_draft' executor ကိုဆက်လုပ်တယ်
        return [save_draft_id]
    else:
        # ငြင်းဆန်ရင် 'handle_review' executor ကိုသွားပြီး မအောင်မြင်မှုကိုအသိပေးတယ်
        return [handle_review_id]

# workflow builder က routing အတွက် selection function ကိုသုံးတယ်
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # multi-selection edge က စည်းမျဉ်းအခြေအနေ logic ကို လုပ်ဆောင်တယ်
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

`to_reviewer_result` ကဲ့သို့သော custom executors များသည် agent များမှ JSON ထွက်ကုန်ကို ရင်းနှီးသော အသွင်ပြောင်းလဲမှုအားဖြင့်၊ selection function ပိုင်းရှင်းစေသည်။

#### .NET (C\#) အကောင်အထည်ဖော်မှု သုံးသပ်ချက်

.NET ဗားရှင်းတွင်လည်း အခြားအဆင့်တူနည်းလမ်းတစ်ခုဖြင့် `Func<object?, bool>` တစ်ခုကို သတ်မှတ်ကာ `ReviewResult` object ၏ `Result` ကို စစ်ဆေးသည်။

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

`AddEdge` method ၏ `condition` ပါရာမီတာက `WorkflowBuilder` ကို လမ်းခွဲများ ဖန်တီးခွင့်ပြုသည်။ `GetCondition(expectedResult: "Yes")` မှားမှန်စစ်ဆေးကာ `"Yes"` ဖြစ်လျှင် `publishExecutor` သို့ ချိတ်ဆက်သည်။ မဟုတ်လျှင် `sendReviewerExecutor` သို့ လမ်းလိုက်သည်။

## နိဂုံးချုပ်

Microsoft Agent Framework Workflow သည် ရှုပ်ထွေးသော multi-agent စနစ်များအား စီမံခန့်ခွဲခြင်းအတွက် ခိုင်မာတည်ငြိမ်ပြီး သက်တောင့်သက်သာ ရလဒ် ရရှိစေရန် များစွာ ထောက်ပံ့ပေးသော အခြေခံ အဆောက်အအုံ ဖြစ်သည်။ ၎င်း၏ ဂရပ်ပေါ် အခြေခံ သဘောတရားနှင့် အဓိက အစိတ်အပိုင်းများကို အသုံးပြုကာ၊ တီထွင်သူများသည် Python နှင့် .NET တွင် ပရော်ဖက်ရှင်နယ် workflow များဖန်တီးနိုင်သည်။ သင်၏ အပလီကေးရှင်းသည် ရိုးရိုးစဉ်ဆက်သို့မဟုတ် တင်ပြနိုင်သော အချိန်တပြိုင်နက် လုပ်ငန်းစဉ်များ သို့မဟုတ် အခြေအနေ လမ်းကြောင်းများ လိုအပ်ပါက Framework သည် ပင်ပန်းလျှော့ချပြီး ခိုင်မာသော AI စွမ်းအားဖြင့် လက်တွေ့ အသုံးချနိုင်သော ဆော့ဖ်ဝဲများ တည်ဆောက်ရန် ကိရိယာများကို ပံ့ပိုးပေးသည်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->