# Microsoft Agent Framework ကို ရှာဖွေခြင်း

![Agent Framework](../../../translated_images/my/lesson-14-thumbnail.90df0065b9d234ee.webp)

### နိဒါန်း

ဤစာသင်ခန်းအတွက် အကြောင်းအရာများမှာ -

- Microsoft Agent Framework ကို နားလည်ခြင်း: အဓိက လက္ခဏာများနှင့် တန်ဖိုးများ
- Microsoft Agent Framework ၏ အဓိက အကြောင်းအရာများကို ရှာဖွေခြင်း
- MAF ၏ အဆင့်မြင့် ပုံစံများ: အလုပ်စဉ်များ၊ Middleware နှင့် မှတ်ဉာဏ်

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းပြီးပါက သင်သည်

- Microsoft Agent Framework ကို အသုံးပြု၍ ထုတ်လုပ်မှုအဆင့် AI Agents များ တည်ဆောက်နိင်ခြင်း
- Microsoft Agent Framework ၏ အဓိက လက္ခဏာများကို သင်၏ Agentic အသုံးအေဆာငး်များတွင် သုံးစွဲနိင်ခြင်း
- အဆင့်မြင့် ပုံစံများ (အလုပ်စဉ်များ၊ middleware နှင့် သိမြင်နိင်မှု) ကို အသုံးပြုနိင်ခြင်း

## ကုဒ်နမူနာများ

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) အတွက် ကုဒ်နမူနာများကို ဒီ repository မှာ `xx-python-agent-framework` နှင့် `xx-dotnet-agent-framework` ဖိုင်များအောက်တွင်တွေ့နိုင်သည်။

## Microsoft Agent Framework ကို နားလည်ခြင်း

![Framework Intro](../../../translated_images/my/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) သည် Microsoft ၏ AI agents များ တည်ဆောက်ရန် အစည်းအဝေးတစ်ခုဖြစ်သည်။ ၎င်းသည် ထုတ်လုပ်မှုနှင့် သုတေသနပတ်ဝန်းကျင်များတွင် တွေ့ရသော ချိတ်ဆက်အသုံးအေဆောင်မှုများစွာကို ဖြေရှင်းနိုင်ရန် လွယ်ကူသော ရရှိနိုင်မှုကို ပေးပါသည်။ ၎င်းတို့မှာ -

- **စဉ်ဆက်မပြတ် Agent ဝန်ဆောင်မှု စီမံခန့်ခွဲခြင်း** - အဆင့်လိုက် အလုပ်စဉ်များ လိုအပ်သော ရှုခင်းများတွင်။
- **အချိန်တစ်ပြိုင်နက်တည်း Agent စီမံခန့်ခွဲခြင်း** - Agent များအချင်းချင်း တာဝန်များ ပြီးမြောက်ရန် လိုအပ်သော ရှုခင်းများတွင်။
- **အဖွဲ့ဖော် စကားဝိုင်း စီမံခန့်ခွဲခြင်း**  - Agent များ တစ်ခုတည်းသော တာဝန်သို့ ပူးပေါင်းဆောင်ရွက်နိုင်သော ရှုခင်းများတွင်။
- **အလှမ်းဆက် ဖြတ်ပြောင်းခြင်း**  - Agent များ တာဝန်များ ဆက်လက်အလှမ်းပေးသွားခြင်း၊ ၁ ခုစီ ပြီးသော အပိုတာဝန်များအတွက်။
- **Magnetic Orchestration**  - မန်နေဂျာ Agent ၏ တာဝန်စာရင်း ဖန်တီးခြင်းနှင့် ပြင်ဆင်ခြင်း၊ သာမန် Agent များကို ညှိနှိုင်းမှုများ ပြုလုပ်ခြင်း။

ထုတ်လုပ်မှု AI Agents များကို ပေးပို့ရန် MAF တွင် အောက်ပါ လက္ခဏာများပါဝင်သည် -

- **OpenTelemetry ဖြင့် သတိပေးသံခြေခံမှု** - AI Agent ၏ လုပ်ဆောင်ချက်တိုင်းကို ထောက်လှမ်းနိုင်ရန်၊ ကိရိယာ အသုံးချမှု၊ စီမံခန့်ခွဲမှု အဆင့်များ နှင့် Microsoft Foundry dashboard များမှ အကျိုးသက်ရောက်မှုအခြေအနေများ စီးရီးတက်စီစစ်မှု။
- **လုံခြုံရေး** - Microsoft Foundry ပေါ်တွင် Agent များကို တည်ဆောက်ခြင်း၊ role-based access၊ ကိုယ်ပိုင်အချက်အလက် ကိုင်တွယ်မှုနှင့် ဝေဖန်မှုမရှိသော အကြောင်းအရာ လုံခြုံရေး စနစ်များ ပါရှိသည်။
- **မြင့်မားသော သက်တမ်း** - Agent အသင်းများနှင့် အလုပ်စဉ်များကို ရပ်တန့်၊ ပြန်လည်ဖွင့်တည်ဆောက်မှုများ ပြုလုပ်နိုင်ပြီး အချိန်ရှည် အလုပ္ဆက်လက် ဆောင်ရွက်ခြင်း အတွက် အထောက်အကူ ဖြစ်စေသည်။
- **ထိန်းချုပ်မှု** - လူတစ်ဦးအား အတည်ပြုမှု လိုအပ်သော တာဝန်များ သတ်မှတ်၍ လူ့အခန်းကဏ္ဍ ပါဝင်သော workflow များ ထောက်ပံ့သည်။

Microsoft Agent Framework သည် အခြားများနှင့် ကျဆုံးစေမှု ရှိစေရန် အခြားနည်းလမ်းများလည်း ပါဝင်သည်။

- **Cloud များအလိုက်မ အကိတ်သတ်မှု** - Agent များကို container များ၊ on-premises နှင့် မတူညီသော cloud များပေါ်တွင် အသုံးပြုနိုင်သည်။
- **Provider များအလိုက် မ အကိတ်သတ်မှု** - Agent များကို သင်နှစ်သက်သည့် SDK များဖြင့် ဖန်တီးနိုင်သည်။ ဥပမာ Azure OpenAI နှင့် OpenAI စသည်။
- **ပုံမှန်စံနှုန်းများ ထည့်သွင်းခြင်း** - Agent များသည် Agent-to-Agent(A2A) နှင့် Model Context Protocol (MCP) ကဲ့သို့သော စံနှုန်းများကို လိုက်နာကာ အခြား Agent များနှင့် ကိရိယာများကို ရှာဖွေဖွင့်နိုင်သည်။
- **Plugins နှင့် Connectors** - Microsoft Fabric, SharePoint, Pinecone, နှင့် Qdrant ကဲ့သို့သော ဒေတာနှင့် မှတ်ဉာဏ်ဝန်ဆောင်မှုများသို့ ချိတ်ဆက်နိုင်သည်။

ယခုလက္ခဏာများထဲမှ ဘယ်လို Microsoft Agent Framework ၏ အဓိက အကြောင်းအရာများတွင် အသုံးပြုလို့ရသည်ဆိုတာကို ကြည့်ကြရအောင်။

## Microsoft Agent Framework ၏ အဓိက အကြောင်းအရာများ

### Agents

![Agent Framework](../../../translated_images/my/agent-components.410a06daf87b4fef.webp)

**Agent များ ဖန်တီးခြင်း**

Agent ဖန်တီးခြင်းသည် ကျော်ဆဲအကြံပြုမှု ဝန်ဆောင်မှု (LLM Provider), AI Agent လိုက်နာရမည့် အညွှန်ကြားချက် အစုအဝေး နှင့် `name` တစ်ခု မှတ်သားရန်ဖြစ်သည်။


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

အထက်မှာ `Azure OpenAI` ကိုအသုံးပြုထားပေမယ့် Agents များကို `Microsoft Foundry Agent Service` ကိုပါ အသုံးပြုနိုင်သည်။

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI ၏ `Responses`, `ChatCompletion` API များ

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ဒါ့အပြင် [MiniMax](https://platform.minimaxi.com/) ကိုပါ အသုံးပြုနိုင်သည်၊ ၎င်းမှာ OpenAI ကိုလိုက်ဖက်သော API ကို 204K tokens အထိ context windows နှင့် ညီညွတ်စွာ ပံ့ပိုးပေးသည်။

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

သို့မဟုတ် A2A protocol ကို အသုံးပြုပြီး အဝေးတွင်ရှိသော agent များ ကို လုပ်ဆောင်နိုင်သည်။

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agent များကို လုပ်ဆောင်ခြင်း**

Agent များကို `.run` သို့မဟုတ် `.run_stream` method များဖြင့် non-streaming သို့ streaming အဖြေအသုံး ပြု၍ လုပ်ဆောင်နိုင်သည်။

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Agent တစ်ခုစီ run တဲ့အခါ `max_tokens`, `tools`, နှင့် အသုံးပြုမည့် `model` သတ်မှတ်နိုင်သည်။

၎င်းသည် အသုံးပြုသူ တာဝန်များ ပြီးမြောက်ရန် မည်သည့် model သို့ tool များလိုအပ်ပါက အထောက်အကူဖြစ်စေသည်။

**Tools**

Tools များကို Agent တည်ဆောက်အချိန်တွင် သတ်မှတ်နိုင်ပြီး

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ChatAgent ကိုတိုက်ရိုက်ဖန်တီးသောအခါ

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

Agent run ကာလတွင်လည်း သတ်မှတ်နိုင်သည်။

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ဤပြေးဆွဲမှုအတွက်သာပေးသောကိရိယာ)
```

**Agent Threads**

Agent Threads သည် multi-turn ဆွေးနွေးမှုများ ကို စီမံရန်အသုံးပြုသည်။ Threads များကို

- `get_new_thread()` ဖြင့် ဖန်တီးနိုင်ပြီး အချိန်ကြာရှည် စုဆောင်းထားနိုင်သည်။
- Agent run တစ်ခုအတွင်း သာ thread ကို auto-create လုပ်၍ အဲ့ run အတွင်းသာ အသုံးပြုနိုင်သည်။

Thread ဖန်တီးရန် ကုဒ် အဖြစ် -

```python
# သစ်တွဲအသစ်တစ်ခုဖန်တီးပါ။
thread = agent.get_new_thread() # ထိုတွဲနှင့်အေးဂျင့်ကို အလုပ်လုပ်ပါ။
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Thread ကို နောက်တစ်ချိန်တွင် အသုံးပြုရန် serialize လုပ်ထားနိုင်သည်။

```python
# နယူးသော thread တစ်ခု ဖန်တီးပါ။
thread = agent.get_new_thread() 

# Agent ကို thread နှင့်အတူ ပြေးပါ။

response = await agent.run("Hello, how are you?", thread=thread) 

# သိမ်းဆည်းမှုအတွက် thread ကို စီးရီးလိုက်ပြုလုပ်ပါ။

serialized_thread = await thread.serialize() 

# သိမ်းဆည်းမှုမှ ဖတ်လင့်ပြီးနောက် thread အခြေအနေကို ပြန်လည်ဖော်ဆောင်ပါ။

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agents သည် tools နှင့် LLM များနှင့် ဆက်သွယ်ကာ အသုံးပြုသူ တာဝန်များ ပြီးမြောက်စေသည်။ အချို့ ရှုခင်းများတွင် ၎င်း ချိတ်ဆက်မှုများအကြား လုပ်ဆောင်ချက်များ ပြုလုပ်ခြင်း သို့မဟုတ် စောင့်ကြည့်ခြင်း လိုအပ်သည်။ Agent middleware မှ တဆင့် ၎င်းလုပ်ဆောင်လိုက်နိုင်သည်။

*Function Middleware*

ဤ middleware သည် Agent နှင့် function/tool တစ်ခုအကြား လုပ်ဆောင်ချက် အသုံးပြုခွင့် ပေးသည်။ ဥပမာ function call အတွက် logging လုပ်လိုသော အခါတွင် အသုံးပြုသည်။

အောက်ပါ ကုဒ်တွင် `next` သည် နောက် middleware သို့မဟုတ် function ကို ခေါ်ရန် သတ်မှတ်သည်။

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ကြိုတင်ဖြတ်တောက်ခြင်း: ဖန်တီးမှုလုပ်ဆောင်မှုမစမီ မှတ်တမ်းတင်ခြင်း
    print(f"[Function] Calling {context.function.name}")

    # နောက်ထပ် middleware သို့မဟုတ် ဖန်တီးမှုလုပ်ဆောင်မှုဆက်လက်ခြင်း
    await next(context)

    # နောက်ဆုံးဖြတ်ခြင်း: ဖန်တီးမှုလုပ်ဆောင်ပြီးနောက် မှတ်တမ်းတင်ခြင်း
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

ဤ middleware သည် Agent နှင့် LLM အကြား သတင်းအချက်အလက် ပို့သွားမှုများအတွက် လုပ်ဆောင်ချက်များ သို့မဟုတ် logging ပြုလုပ်ရာတွင် အသုံးပြုသည်။

၎င်းတွင် AI ဝန်ဆောင်မှုသို့ ပို့ပေးသည့် `messages` အချက်အလက် အရေးကြီးသည်။

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ကြိုတင်လုပ်ငန်းဆောင်တာ: AI ခေါ်ဆိုမီ မှတ်တမ်းတင်ခြင်း
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # နောက်တစ်ခုသော middleware သို့မဟုတ် AI ဝန်ဆောင်မှုဆီ ဆက်လုပ်ခြင်း
    await next(context)

    # အပြီးလုပ်ငန်းဆောင်တာ: AI ပြန်တုံ့ပြန်မှုနောက်မှ မှတ်တမ်းတင်ခြင်း
    print("[Chat] AI response received")

```

**Agent Memory**

`Agentic Memory` သင်ခန်းစာတွင် ဖေါ်ပြသည့်အတိုင်း မှတ်ဉာဏ်သည် Agent ၏ မတူညီသော context များအတွင်း လုပ်ဆောင်နိုင်ရေးအတွက် အရေးကြီးမှုရှိသည်။ MAF တွင် မှတ်ဉာဏ်အမျိုးအစား များစွာ ရှိသည်။

*In-Memory Storage*

ထို memory သည် application runtime အတွင်း Thread များတွင် သိမ်းဆည်းထားသည်။

```python
# နယူးသရက်တစ်ခုဖန်တီးပါ။
thread = agent.get_new_thread() # သရက်နှင့်အတူအေးဂျင့်ကိုပြေးပါ။
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

session များ လျှောက်ပြန်ရန် သံသယ မရှိသော အချက်အလက်များ (conversation history) ကို ထိန်းသိမ်းဖို့ အသုံးပြုသည်။ `chat_message_store_factory` ဖြင့် သတ်မှတ်ထားသည်။

```python
from agent_framework import ChatMessageStore

# စိတ်ကြိုက်မက်ဆေ့ခ််ဆိုင်အတည်ပြုပါ
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamic Memory*

Agent run မတိုင်မီ context ထဲသို့ ထည့်သွင်းသည့် memory ဖြစ်သည်။ mem0 ကဲ့သို့သော အပြင်ဝန်ဆောင်မှုများတွင် သိမ်းဆည်းနိုင်သည်။

```python
from agent_framework.mem0 import Mem0Provider

# အဆင့်မြင့်မှတ်ဉာဏ်စွမ်းရည်များအတွက် Mem0 ကို အသုံးပြုခြင်း
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**Agent Observability**

Observability သည် ယုံကြည်ချက်ရှိသော၊ ပြုပြင်ထိန်းသိမ်းအရ အောင်မြင်သော agentic စနစ်များ တည်ဆောက်ရာတွင် အရေးကြီးသည်။ MAF သည် OpenTelemetry နှင့် ပေါင်းစည်းကာ ထောက်လှမ်းမှုနှင့် အတိုင်းအတာများ ပေးသည်။

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # တစ်ခုခု လုပ်ပါ
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### အလုပ်စဉ်များ (Workflows)

MAF သည် တာဝန်တစ်ခု သို့ ကုန်ဆုံးစေရန် ကြိုတင်သတ်မှတ်ထားသော အဆင့်များဖြင့် workflows များ ပံ့ပိုးပေးသည်။ ၎င်းတွင် AI Agents များ ပါဝင်သည်။

Workflows တွင် control flow ကို တိုးတက်စေသော ဝန်ဆောင်မှု အစိတ်အပိုင်းများ ပါဝင်ပြီး **multi-agent orchestration** နှင့် **checkpointing** တို့ကို ထောက်ပံ့သည့် အင်္ဂါရပ်များ ရှိသည်။

Workflow ၏ အဓိက အစိတ်အပိုင်းများမှာ -

**Executors**

Executors သည် input message များကို လက်ခံကာ၊ ခန့်အပ်ထားသော တာဝန် ကို ဆောင်ရွက်ပြီး ထွက်ရှိမည့် message များကို ထုတ်ပေးသည်။ ၎င်းသည် workflow ကို ကြီးမားသော တာဝန် ပြီးမြောက်မှုအထိ ရွေ့လျားစေနိုင်သည်။ Executors များသည် AI agent သို့မဟုတ် အထူး logic ဖြစ်နိုင်သည်။

**Edges**

Edges များက workflow တွင် message များရောက်ရှိသွားစေသည်။ ၎င်းတို့မှာ -

*Direct Edges* - Executor များအကြား တစ်ခုချင်းဆက်သွယ်မှုများ။

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Conditional Edges* - အခြေအနေတစ်ခုဖြစ်ပါက ဖွင့်လှစ်သည်။ ဥပမာ အိတ်ထဲတွင်နေရာများ မရနိုင်ပါက နောက်ထပ် ရွေးချယ်မှုများ ပြသသည်။

*Switch-case Edges* - ချမှတ်ထားသော အခြေအနေအရ message များကို executor များသို့ ပေးပို့သည်။ ဥပမာ ခရီးသွား ဖောက်သည်မှာ priority access ရှိပါက အခြား workflow မှတဆင့် တာဝန်များ ကိုင်တွယ်မည်။

*Fan-out Edges* - Message တစ်ခုကို အများအပြားသော နောက်ဆုံးခေါက်များသို့ ပေးပို့ခြင်း။

*Fan-in Edges* - Executor များအတွင်း အများအပြားသော message များကို စုဆောင်း၍ တစ်ခုတည်းသော နောက်ဆုံးခေါက်သို့ ပေးပို့ခြင်း။

**Events**

Workflows ထဲတွင် observability ကိုတိုးတက်စေရန် MAF သည် အောက်ပါ event များ built-in ပံ့ပိုး ပေးသည် -

- `WorkflowStartedEvent`  - Workflow လည်ပတ်မှု စတင်ခြင်း
- `WorkflowOutputEvent` - Workflow အဖြေ ထုတ်ပြန်ခြင်း
- `WorkflowErrorEvent` - Workflow တွင် မှားယွင်းမှု ဖြစ်ပေါ်ခြင်း
- `ExecutorInvokeEvent`  - Executor လုပ်ငန်း စတင်ခြင်း
- `ExecutorCompleteEvent`  - Executor လုပ်ငန်း ပြီးဆုံးခြင်း
- `RequestInfoEvent` - တောင်းဆိုချက် ထုတ်ပြန်ခြင်း

## MAF ၏ အဆင့်မြင့် ပုံစံများ

အထက်ဖော်ပြထားသော အပိုင်းများသည် Microsoft Agent Framework ၏ အဓိက အကြောင်းအရာများဖြစ်သည်။ ပို၍ ရိုးရှင်းသော Agent များ တည်ဆောက်သည့်အခါ အောက်ပါ အဆင့်မြင့် ပုံစံများကို ဦးစားပေးစဥ်းစားပါ။

- **Middleware ပေါင်းစပ်ခြင်း**: function နှင့် chat middleware များအဖြင့် logging, authentication, rate-limiting ကဲ့သို့သော middleware handler များကို လွယ်ကူစွာချိတ်ဆက်၍ Agent ၏ ချုပ်ကိုင်မှုအားအသေးစိတ်ထိန်းချုပ်ခြင်း။
- **Workflow Checkpointing**: ပါဝင်သော workflow event များနှင့် serialization ကို အသုံးပြု၍ ကြာရှည် agent process များကို သိမ်းဆည်းပြီး ပြန်လည်ဆက်လက်လုပ်ကိုင်နိုင်ခြင်း။
- **Dynamic Tool ရွေးချယ်မှု**: RAG ကို tool ဖော်ပြချက်များပေါ်တွင် တွဲဖက်ပြီး MAF ၏ tool မှတ်ပုံတင်မှု ဖြင့် မေးခွန်းတစ်ခုစီအတွက် သက်ဆိုင်ရာ tool များသာ ပြသခြင်း။
- **Multi-Agent Handoff**: workflow edges နှင့် conditional routing အသုံးပြု၍ အထူးပြု Agent များအကြား လက်မှတ်ပိုင်းဆက်သွယ်ခြင်း စီမံခန့်ခွဲမှု။

## LangChain / LangGraph Agents များကို Microsoft Foundry တွင် တင်ထားခြင်း

Microsoft Agent Framework သည် **framework-interoperable** ဖြစ်ပြီး MAF ဖြင့်သာ ရေးသားထားသော agent များထဲ အကန့်အသတ်မရှိပါ။ သင်တွင် **LangChain** သို့မဟုတ် **LangGraph** ဖြင့် ဖန်တီးထားသော agent ရှိပါက Foundry ကျင်းပရာ Microsoft Foundry hosted agent အဖြစ် လည်ပတ်စေခြင်းဖြင့် Foundry သည် runtime, sessions, scaling, identity နှင့် protocol endpoints များကို စီမံခန့်ခွဲပေးမည်ဖြစ်ပြီး သင်၏ Agent logic သည် LangGraph တွင် ဆက်လက်ရှိနေပါမည်။

၎င်းကို `langchain_azure_ai.agents.hosting` package ဖြင့် ပြုလုပ်နိုင်ပြီး Foundry hosted agents များသုံးသော protocol များကိုလည်း ထုတ်ပြန်ထားသည်။

**1. hosting extra ကို အပ်ဒိတ်ထည့်ခြင်း**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` extra သည် Foundry protocol libraries အဖြစ် `azure-ai-agentserver-responses` (OpenAI-compatible `/responses` endpoint) နှင့် `azure-ai-agentserver-invocations` (generic `/invocations` endpoint) ကို ထည့်သွင်းပေးပါသည်။

**2. hosting protocol ရွေးချယ်ခြင်း**

| Protocol | Host class | Endpoint | အသုံးပြုရမည့် အခါ |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | OpenAI-compatible chat, streaming, response history နှင့် conversation threading လိုအပ်ပါက အသုံးပြုရန်။ conversation agents များအတွက် ယခင်ဆုံးစံနှုန်းဖြစ်သည်။ |
| **Invocations** | `InvocationsHostServer` | `/invocations` | အသုံးပြုသူ သီးခြား JSON စံနှုန်း၊ webhook-style endpoint သို့မဟုတ် non-conversational processing လိုအပ်ပါက အသုံးပြုရန်။ |

**Responses API သည် Foundry တွင် agent-style ဖွံ့ဖြိုးမှုအတွက် မူလ API ဖြစ်သောကြောင့်** စကတ်အနေနှင့် များသော Agent များအတွက် `ResponsesHostServer` ကို စတင်အသုံးပြုပါ။

**3. ပတ်ဝန်းကျင် မတပ်ဆင်မှုများ သတ်မှတ်ခြင်း** (မည်သည့်အခါ `az login` ဖြင့် `DefaultAzureCredential` အတည်ပြုကာ authenticate ရမည်)

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Agent သည် နောက်ပိုင်း Foundry တွင် hosted agent အဖြစ် run မည့်အခါ platform မှ `FOUNDRY_PROJECT_ENDPOINT` သို့ အလိုအလျောက် ထည့်သွင်းပေးမည်။

**4. LangGraph Agent ကို Responses protocol ဖြင့် ဖော်ပြခြင်း**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI ဤနေရာတွင် Foundry စီမံကိန်း၏ OpenAI-ကိုက်ညီသော (ပြန်လည်တုံ့ပြန်မှုများ) endpoint ကို ရည်ညွှန်းသည်။
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

`python main.py` ဖြင့် ဒေသတွင် run ပြီး `http://localhost:8088/responses` သို့ Responses တောင်းဆိုချက် ပို့ရန်။

**အဓိက အပြုအမူများ**

- **စကားပြောဆိုမှုများ**: Client များသည် `previous_response_id` သို့မဟုတ် `conversation` ID ဖြင့် ဆက်လက်သော ဆွေးနွေးမှုကို ဆက်လက် ဖွင့်နိုင်သည်။ သင်၏ graph သည် LangGraph checkpointer ဖြင့် compiled ဖြစ်ပါက Foundry သည် conversation အခြေအနေကို checkpoint တွင် လုပ်ဆောင်သည် (ထုတ်လုပ်မှုတွင် durable checkpointer အသုံးပြုရန် မျှော်လင့်သည်။ `MemorySaver` သည် ဒေသတွင် စမ်းသပ်ရန် ပြည့်ပေါင်းကောင်းသည်။)
- **လူ့အစိတ်အပိုင်း ပါဝင်မှု**: သင်၏ graph သည် LangGraph `interrupt()` ကို အသုံးပြုပါက `ResponsesHostServer` သည် pending interrupt ကို Responses `function_call` / `mcp_approval_request` အဖြစ် ဖော်ပြပြီး client များသည် `function_call_output` / `mcp_approval_response` ဖြင့် စတင် ဆက်လက် လုပ်ဆောင်သည်။
- **Foundry သို့ တင်ပို့ခြင်း**: Azure Developer CLI ကို အသုံးပြု၍ - `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (ဒေသတွင် run အတွက် Docker လိုအပ်သည်), ထို့နောက် `azd provision` နှင့် `azd deploy` ပြုလုပ်ပါ။ Hosted-agent deployment အတွက် **Foundry Project Manager** အခန်းကဏ္ဍလိုအပ်သည်။

ဤနမူနာ၏ ဒေသတွင် run ပြုလုပ်နိုင်သည့် ဗားရှင်းကို [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) မှာ တွေ့ရပါသည်။ များသောအားဖြင့် walkthrough အတွက် (Invocations protocol, သီးခြားတောင်းဆိုချက် schemas နှင့် ပြဿနာဖြေရှင်းခြင်း) ကို [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) တွင် ဖတ်ရှုနိုင်ပါသည်။

## ကုဒ်နမူနာများ

Microsoft Agent Framework အတွက် ကုဒ်နမူနာများသည် ဒီ repository တွင် `xx-python-agent-framework` နှင့် `xx-dotnet-agent-framework` ဖိုင်များအောက်တွင်ရှိသည်။

## Microsoft Agent Framework နှင့် ပတ်သက်ပြီး ထပ်မံမေးမြန်းလိုပါသလား?

အခြား သင်ယူသူများနှင့် တွေ့ဆုံရန်၊ office hours အတက်ရန်နှင့် သင်၏ AI Agents မေးခွန်းများ ရယူရန် [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) တွင် ပါဝင်ဆွေးနွေးပါ။
## ယခင်သင်ခန်းစာ

[Memory for AI Agents](../13-agent-memory/README.md)

## နောက်သင်ခန်းစာ

[Computer Use Agents (CUA) တည်ဆောက်ခြင်း](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->