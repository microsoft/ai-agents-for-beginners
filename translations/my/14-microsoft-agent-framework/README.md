# Microsoft Agent Framework ကို ရှာဖွေခြင်း

![Agent Framework](../../../translated_images/my/lesson-14-thumbnail.90df0065b9d234ee.webp)

### နိဒါန်း

ဒီသင်ခန်းစာမှာ ဖော်ပြမှာတွေကတော့ -

- Microsoft Agent Framework ကို နားလည်ခြင်း: အဓိက လက္ခဏာများနှင့် တန်ဖိုးများ  
- Microsoft Agent Framework ၏ အဓိက အကြောင်းအရာများကို ရှာဖွေခြင်း
- တိုးတက်သော MAF ပုံစံများ: Workflows, Middleware, နှင့် Memory

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဒီသင်ခန်းစာပြီးဆုံးပြီးနောက်မှာ သင်သည် -

- Microsoft Agent Framework အသုံးပြုပြီး ထုတ်လုပ်မှုမှ အဆင်သင့် AI Agents တည်ဆောက်နည်းကို သိရှိနိုင်မည်
- Microsoft Agent Framework ၏ အဓိက လက္ခဏာများကို သင့် Agentic အသုံးတော်များတွင် အသုံးပြုနည်း
- worklow, middleware, နှင့် obserability တွေအပါအဝင် တိုးတက်သော ပုံစံများကို အသုံးပြုနည်း

## ကုဒ် နမူနာများ

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) အတွက် ကုဒ် နမူနာများကို ဒီ repository ၏ `xx-python-agent-framework` နှင့် `xx-dotnet-agent-framework` ဖိုင်များအောက်တွင် တွေ့နိုင်ပါသည်။

## Microsoft Agent Framework ကို နားလည်ခြင်း

![Framework Intro](../../../translated_images/my/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) သည် AI agents များ တည်ဆောက်ရန် Microsoft ၏ စုပေါင်း framework ဖြစ်သည်။ ထုတ်လုပ်မှုနှင့် သုတေသနပတ်ဝန်းကျင်များတွင် တွေ့ရသော agentic အသုံးတော် မျိုးစုံကို ဖြေရှင်းနိုင်ရန် အလွယ်တကူညှိနှိုင်းနိုင်မှုကို ပံ့ပိုးပေးသည်၊ အထူးသဖြင့် -

- **လိုက်စီးပြီး အချက်တစ်ချက်ချင်း လုပ်ဆောင်လိုသော စနစ်များတွင် Sequential Agent orchestration**
- **အချိန်တစ်ပြိုင်နက်မှာ တာဝန်များ ပြီးမြောက်ရန် concurrent orchestration**
- **တစ်ခုသော တာဝန်တွင် အီးဂျင်များ ပူးပေါင်းဆောင်ရွက်နိုင်ရန် group chat orchestration**
- **သေးငယ်သေးဆုံး အဆင့်များ ပြီးမြောက်သည့်အခါ တာဝန်များကို အီးဂျင်များ ဆက်လက်လွှဲပြောင်းရန် handoff orchestration**
- **မန်နေဂျာအီးဂျင်တစ်ခုဖြင့် တာဝန်စာရင်း ဖန်တီး၊ ပြုပြင်ပြီး သေးငယ်သူ အီးဂျင်များ စနစ်တက်ညှိနှိုင်းဖြင့် အလုပ်လုပ်စေနိုင်သော magnetic orchestration**

ထုတ်လုပ်မှု AI Agents ပေးဆောင်ရာတွင် MAF သည် -

- **OpenTelemetry အသုံးပြု၍ AI Agent ၏ Tool ခေါ်ဆိုမှု၊ orchestration အဆင့်များ၊ ကြားခံစဉ်းစားမှုများနှင့် Microsoft Foundry dashboard တွင် စွမ်းဆောင်ရည် စောင့်ကြည့်မှုစသည့် Observability ကို ပံ့ပိုးသည်။**
- **Microsoft Foundry တွင် native ဖြင့် hosting လုပ်သောကြောင့် role-based access control, အထူးသီးသန့်ဒေတာ ကိုင်တွယ်မှု နှင့် built-in content safety စသည့် security နှင့် ကာကွယ်မှုကို ထောက်ပံ့သည်။**
- **Agent စီးရီးများနှင့် workflows များ မိမိလိုအပ်သလို ရပ်တန့်၊ ပြန်လည်အလှမ်းလိုက်၊ အမှားမှ ပြန်လည်ကောင်းမွန်နိုင်စေသည့် durability ကို ပံ့ပိုးပေးသည်။**
- **လူ့အင်အားပါဝင်သော workflows များကိုသာလျှင် ပံ့ပိုးကာ မည်သည့်တာဝန်ကိုမဆို လူအတည်ပြုချက်လိုအပ်မှုအဖြစ် ဖော်ပြနိုင်သည်။**

Microsoft Agent Framework သည် interoperability အတွက်လည်း အာရုံစိုက်မှုရှိကာ -

- **Cloud မျိုးစုံမရွေး အသုံးပြုနိုင်ခြင်း - containers, on-premise နှင့် cloud များစွာတွင် ဆောင်ရွက်နိုင်သော agents များ**
- **Provider မျိုးစုံမရွေး အသုံးပြုနိုင်ခြင်း - Azure OpenAI နှင့် OpenAI အပါအဝင် သင်နှစ်သက်ရာ SDK များဖြင့် agent များ ဖန်တီးနိုင်ခြင်း**
- **Open စံချိန်စံညွှန်းများပါ ပေါင်းစပ်ထားခြင်း - Agent-to-Agent (A2A) နှင့် Model Context Protocol (MCP) စသည်ဖြင့် အခြား agent များနှင့် Tools များ ရှာဖွေရန်နှင့် အသုံးပြုရန် ပံ့ပိုးမှု**
- **Plugins နှင့် Connectors - Microsoft Fabric, SharePoint, Pinecone, Qdrant ကဲ့သို့ ဒေတာနှင့် မှတ်ဉာဏ် ဝန်ဆောင်မှုများနှင့် ဆက်သွယ်နိုင်ရန်**

ဒီတော့ Microsoft Agent Framework ၏ အဓိက အကြောင်းအရာများတွင် ဒီ လက္ခဏာများဘယ်လိုပါဝင်သလို် တင်ပြအကြောင်းကြည့်လိုက်မယ်။

## Microsoft Agent Framework ၏ အဓိက ဆိုဒီ

### Agents

![Agent Framework](../../../translated_images/my/agent-components.410a06daf87b4fef.webp)

**အီးဂျင်များ ဖန်တီးခြင်း**

Agent ဖန်တီးခြင်းမှာ inference service (LLM Provider), AI Agent အတွက် လိုက်နာရမည့် ညွှန်ကြားချက်များနှင့် ခန့်အပ်ထားသော `name` တန်ဖိုး တိုက်ရိုက် သတ်မှတ်ခြင်းဖြစ်သည်-

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

အထက်ပါ ကုဒ်မှာ `Azure OpenAI` ဖြင့် အသုံးပြုထားသော်လည်း `Microsoft Foundry Agent Service` အပါအဝင် နောက်ထပ် ဝန်ဆောင်မှု မျိုးစုံမှ Devices များ ဖန်တီးနိုင်သည်-

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

သို့မဟုတ် A2A protocol အသုံးပြု၍ အဝေးမှ ထိန်းချုပ် agent များ -

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agent များ လည်ပတ်ခြင်း**

Agents များကို non-streaming သို့မဟုတ် streaming ဖြင့် `.run` သို့မဟုတ် `.run_stream` ပုံစံဖြင့် လည်ပတ်နိုင်သည်။

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Agent တစ်ခုလည်ပတ်တိုင်းမှာ agent အသုံးပြုမည့် `max_tokens`, agent ခေါ်ဆိုမှု လုပ်နိုင်သော `tools`, ဖြင့် ဖန်တီးသုံးမည့် `model` တို့ စိတ်ကြိုက် ပြင်ဆင်နိုင်သည်။

အသုံးပြုသူ၏ တာဝန်နှင့် ကိုက်ညီသည့် အထူးပုံစံ မော်ဒယ်များ သို့ tools များ သတ်မှတ်လိုသည့် ရည်ရွယ်ချက်များတွင် အထူးအသုံးဝင်သည်။

**Tools**

Tools များကို agent ဖန်တီးစဉ်တွင် သတ်မှတ်နိုင်သည်-

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ChatAgent ကိုတိုက်ရိုက်ဖန်တီးထားတဲ့အခါ

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

နှင့် agent လည်ပတ်စဉ်တွင်လည်း သတ်မှတ်အသုံးပြုနိုင်သည်-

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ဤအလုပ်အတွက်သာ ပံ့ပိုးပေးထားသောကိရိယာ)
```

**Agent Threads**

Agent Threads သည် multi-turn စကားပြောဆိုမှုများကို ကိုင်တွယ်ရန် အသုံးပြုသည်။ Threads များကို အောက်ပါ နည်းလမ်းနှစ်မျိုးဖြင့် ဖန်တီးနိုင်သည်-

- `get_new_thread()` ဖြင့် thread ကို အချိန်ကြာရှည်သိမ်းဆည်းထားရန်
- Agent run စဉ်အတွင်း မိမိကိုယ်တိုင် auto ဖန်တီးပြီး ယင်း run အတွင်းသာ thread ကို ထိန်းသိမ်းခြင်း။

Thread ဖန်တီးရန် နမူနာ ကုဒ် -

```python
# သစ် thread အသစ်တစ်ခုကို ဖန်တီးပါ။
thread = agent.get_new_thread() # thread နှင့်အတူ agent ကို ပြေးပါ။
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Thread ကို သိမ်းဆည်းရန် serialization လုပ်နိုင်ပါသည်-

```python
# သစ်တစ်ခုသော စကြည်ကို ဖန်တီးပါ။
thread = agent.get_new_thread() 

# စကြည်နဲ့ အေးဂျင့်ကို အတူ လည်ပတ်ပါ။

response = await agent.run("Hello, how are you?", thread=thread) 

# သိမ်းဆည်းရန် စကြည်ကို စီရင်လိုးတိုင်လုပ်ပါ။

serialized_thread = await thread.serialize() 

# သိမ်းဆည်းထားမှုမှ ဒေတာ tải ချင်းပြီးနောက် စကြည်အခြေအနေကို အစီအစဉ်ချပါ။

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agents များသည် tools နှင့် LLM များအား အသုံးပြု၍ အသုံးပြုသူ၏ တာဝန်များကို ပြီးမြောက်စေသည်။ အချို့ ဇာတ်ကြောင်းများတွင် နှစ်ဖက်စွပ်စွဲမှုများကို ကြားနားတွင် လုပ်ဆောင်ခြင်း သို့မဟုတ် မှတ်တမ်းတင်ခြင်း လိုအပ်သည်။ Agent middleware သည် အောက်ပါအတိုင်း ထောက်ပံ့ပေးသည်-

*Function Middleware*

Middleware သည် agent နှင့် ဖုန်းခေါ်ဆိုမည့် function/tool အကြား action ဆောင်ရွက်ရန် အသုံးပြုသည်။ ဥပမာ logging လုပ်ချင်သော function call များအတွက် အသုံးချနိုင်သည်။

ကုဒ်တွင် `next` သည် နောက်တစ်ခုသော middleware သို့မဟုတ် function ကိုခေါ်ရန် သတ်မှတ်သည်။

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ရှေ့ဆောင်လုပ်ငန်းစဉ်: လုပ်ဆောင်ချက်စတင်မတိုင်မှီ မှတ်တမ်းတင်ခြင်း
    print(f"[Function] Calling {context.function.name}")

    # နောက်ထပ် middleware သို့မဟုတ် လုပ်ဆောင်ချက်စဉ်ဆက်လုပ်ရန်
    await next(context)

    # နောက်ဆက်တွဲလုပ်ငန်းစဉ်: လုပ်ဆောင်ချက်ပြီးနောက်မှတ်တမ်းတင်ခြင်း
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Middleware သည် agent နှင့် LLM  ကြား ပေးပို့သော စာတိုများအား လုပ်ဆောင်ခြင်း သို့မှတ်တမ်းတင်ခြင်းများ ဆောင်ရွက်သည်။

AI ဝန်ဆောင်မှုသို့ ပေးပို့သော `messages` အချက်အလက်များ ပါဝင်သည်။

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ပြင်ဆင်ခြင်းမပြုမီ: AI ခေါ်ဆိုမှုမပြုမီ မှတ်တမ်းတင်ခြင်း
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # နောက်ထပ် middleware သို့မဟုတ် AI ဝန်ဆောင်မှုဆီသို့ ဆက်လက်သွားရန်
    await next(context)

    # ပြင်ဆင်ပြီးချိန်: AI ရဲ့တုံ့ပြန်ချက်အပြီး မှတ်တမ်းတင်ခြင်း
    print("[Chat] AI response received")

```

**Agent Memory**

`Agentic Memory` သင်ခန်းစာတွင် ဖော်ပြသလို မှတ်ဉာဏ်သည် အီးဂျင်အား စကားဝိုင်း အမျိုးမျိုးအပေါ် အလုပ်လုပ်ဆောင်နိုင်ရန် အရေးကြီးသော အစိတ်အပိုင်းဖြစ်သည်။ MAF သည် မှတ်ဉာဏ်အမျိုးမျိုးကို ပံ့ပိုးပေးသည်။

*In-Memory Storage*

ဒီ memory သည် application runtime ခန္ဓာကိုယ်တွင် threads ထဲတွင် သိမ်းဆည်းထားသည်။

```python
# Thread အသစ်တစ်ခု ဖန်တီးပါ။
thread = agent.get_new_thread() # Thread နဲ့အတူ agent ကို chạy ပါ။
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

ဒီ memory သည် ဆွေးနွေးမှုမှတ်တမ်းများကို မတူညီသော session များအတွင်း သိမ်းဆည်းရန် အသုံးပြုသည်။ `chat_message_store_factory` ဖြင့် သတ်မှတ်သည် -

```python
from agent_framework import ChatMessageStore

# စိတ်ကြိုက်သတင်းစကားဒေတာစတိုးတည်ဆောက်ပါ
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamic Memory*

ဒီ memory သည် agents လည်ပတ်မည့် context မတိုင်မီ ထည့်သွင်းထားသော memory များဖြစ်သည်။ mem0 ကဲ့သို့သော ပြင်ပ ဝန်ဆောင်မှုများတွင် သိမ်းဆည်းနိုင်သည်။

```python
from agent_framework.mem0 import Mem0Provider

# အဆင့်မြင့်မွန်းမာရေးစွမ်းရည်များအတွက် Mem0 ကိုသုံးခြင်း
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

Observability သည် ယုံကြည် စိတ်ချရပြီး ထိန်းသိမ်းနိုင်သော agentic စနစ်များ အတွက် အရေးကြီးသည်။ MAF သည် OpenTelemetry နှင့် ပေါင်းစပ်၍ သတိထားကြည့်ရှုမှုနှင့် အတိုင်းအတာများ ပံ့ပိုးပေးသည်။

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # တစ်ခုခုလုပ်ပါ
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Workflows

MAF သည် မှီဝဲတောင့်တင်းလိုအပ်သည့် အဆင့်များကို တွေ့ရှိပြီး တာဝန်ပြည့်စုံအောင် AI agents များ ပါဝင်သည့် workflows များကို ပံ့ပိုးပေးသည်။

Workflows သည် ဖွဲ့စည်းမှုအပိုင်းများ များစွာ ပါဝင်ပြီး ထိန်းချုပ်မှု ပိုမိုကောင်းမွန်စေသည်။ Workflows သည် **multi-agent orchestration** နှင့် **checkpointing** များဖြင့် workflow အခြေအနေများ သိမ်းဆည်းနိုင်သည်။

Workflow ၏ အဓိက အစိတ်အပိုင်းများမှာ -

**Executors**

Executors သည် input messages လက်ခံကာ ဖော်ပြထားသောလုပ်ဆောင်ချက်များ ပြီးမှ output message ထုတ်ပေးသည်။ ၎င်းသည် workflow ကို ပြီးမြောက်စေရန် ဆက်လက်ရွှေ့ဆိုင်းသည်။ Executors သည် AI agent သို့မဟုတ် စိတ်ကြိုက် logic ဖြစ်နိုင်သည်။

**Edges**

Edges များသည် workflow ၌ messages များ စီးဆင်းပုံကို သတ်မှတ်ရန် အသုံးပြုသည်။ ၎င်းများမှာ -

*Direct Edges* - Executor တစ်ခုမှ တစ်ခုသို့ တိုက်ရိုက်ချိတ်ဆက်ခြင်း -

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Conditional Edges* - သတ်မှတ်ထားသောအခြေအနေဖြစ်ပေါ်ပြီးမှ ဖွင့်လှစ်သည်။ ဥပမာ- စတိတ်ခန်းလွတ်ရှိမှုမရှိပါက အခြားရွေးချယ်စရာအကြံပြုခြင်း။

*Switch-case Edges* - သတ်မှတ်ထားသော အခြေအနေများအလိုက် messages များကို တိုင်းတာ၍ အခြား executors များသို့ ပေးပို့ခြင်း။ ဥပမာ- ခရီးသွားဖောက်သည်တွင် မြန်ဆန်ရုံးဝင်ခွင့်ရှိပြီး workflow အခြားဖြင့် စီမံမည်။

*Fan-out Edges* - တစ်စိတ်တစ်ပိုင်း message を 多数のターゲットに送信。

*Fan-in Edges* - 多数のexecutorsからのメッセージを集めて、一つのターゲットに送信。

**Events**

Workflows တွင် observation ပိုမိုတိကျစေရန် MAF သည် အောက်ပါ အမျိုးအစား built-in events များကို ပံ့ပိုးပေးသည် -

- `WorkflowStartedEvent` - Workflow လည်ပတ်မှု စတင်သည်
- `WorkflowOutputEvent` - Workflow နှင့် တွက်ချက် ပြန်လည်ထုတ်ပေးသည့် output
- `WorkflowErrorEvent` - Workflow သည် အမှားတက်သည်
- `ExecutorInvokeEvent` - Executor သည် ဖြေရှင်းရေး စတင်သည်
- `ExecutorCompleteEvent` - Executor ဖြေရှင်းရေး ပြီးမြောက်သည်
- `RequestInfoEvent` - တောင်းဆိုမှု တစ်ခု ထုတ်ပေးသည်

## Advanced MAF Patterns

အထက်ပါ အကြောင်းအရာများသည် Microsoft Agent Framework ၏ အဓိက မှတ်ချက်များ ဖြစ်သည်။ agents များ ပို၍ရှုပ်ထွေးလာသောအခါ - အောက်ပါ တိုးတက်သော ပုံစံများကို စဉ်းစားပါ-

- **Middleware Composition**: logging, authentication, rate-limiting ကဲ့သို့ မျိုးစုံသော middleware handler များ function နှင့် chat middleware ဖြင့် ဆက်သွယ်စဉ်ကို စီမံခြင်း၊ agent ဖော်ပြချက် ပိုမိုလေ့လာခြင်း။
- **Workflow Checkpointing**: workflow events နှင့် serialization ဖြင့် agent စဥ်တစ်ခဲ့ များ ကို သိမ်းဆည်းပီး ဆက်လက်ပြုလုပ်ခြင်း။
- **Dynamic Tool Selection**: RAG ဝန်ဆောင်မှု အပေါ် မူတည်၍ MAF tool စာရင်းနှင့် ပေါင်းစပ်၍ အကြောင်းအရစပ်ဘို့ version ကိရိယာများ တင်ပြခြင်း။
- **Multi-Agent Handoff**: workflow edges နှင့် conditional routing  အသုံးပြု အထူးပြု agents များ အကြား သတိထားမှု လွှဲပြောင်းခြင်း။

## ကုဒ် နမူနာများ

Microsoft Agent Framework သော ကုဒ် နမူနာများကို ဒီ repository ၏ `xx-python-agent-framework` နှင့် `xx-dotnet-agent-framework` ဖိုင်များ အောက်တွင် တွေ့နိုင်ပါသည်။

## Microsoft Agent Framework ပိုမိုမေးမြန်းလိုပါသလား?

အခြား တက်ကြွသူများနှင့် တွေ့ဆုံ၊ office hours တက်ရောက်ပြီး AI Agents သာမန်မေးခွန်း များကို ဖြေကြားပေးရန် [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) တွင် ပါဝင်ဆွေးနွေးလိုက်ပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အကြောင်းပြချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားဆောင်ရွက်သော်လည်း အလိုအလျောက်ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မှားယွင်းသည့်အချက်များ ပါရှိနိုင်ကြောင်း သတိပြု Awareness၊ မူလစာတမ်း၏ မူလဘာသာဖြင့် ရေးသားထားသည့် မူရင်းကို ကိုးကားသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုအား အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသည့် တိတိကျကျမရှိမှုများ သို့မဟုတ် မှားယွင်းဖော်ပြချက်များအတွက် ကျွန်ုပ်တို့တာဝန်မရှိပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->