# Microsoft Agent Framework ကို ရှာဖွေတွေ့ရှိခြင်း

![Agent Framework](../../../translated_images/my/lesson-14-thumbnail.90df0065b9d234ee.webp)

### နိဒါန်း

ဒီသင်ခန်းစာမှာကတော့:

- Microsoft Agent Framework ကို နားလည်ခြင်း - အဓိကအင်္ဂါရပ်များနှင့် တန်ဖိုး
- Microsoft Agent Framework ၏ အဓိက အယူအဆများ ရှာဖွေခြင်း
- မြှင့်တင်ထားသော MAF ပုံစံများ - အလုပ်လုပ်စဉ်များ၊ Middleware နှင့် မှတ်ဉာဏ်

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဒီသင်ခန်းစာကိုပြီးစီးပြီးနောက် သင်သည် အောက်ပါအရာများကို သိရှိနိုင်မည်ဖြစ်သည်-

- Microsoft Agent Framework ကို အသုံးပြုကာ ထုတ်လုပ်မှုအဆင်သင့် AI Agent များ တည်ဆောက်ခြင်း
- Microsoft Agent Framework ၏ အဓိက အင်္ဂါရပ်များကို သင့် Agentic အသုံးပြုမှုများတွင် လုပ်ဆောင်ခြင်း
- အလုပ်လုပ်စဉ်များ၊ middleware နှင့် ကြည့်ရှုနိုင်မှု အပါအဝင် မြှင့်တင်ထားသော ပုံစံများကို အသုံးပြုခြင်း

## ကုဒ်နမူနာများ

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) အတွက် ကုဒ်နမူနာများကို `xx-python-agent-framework` နှင့် `xx-dotnet-agent-framework` ဖိုင်များအောက်ရှိ ဒီ repository မှာတွေ့နိုင်ပါသည်။

## Microsoft Agent Framework ကို နားလည်ခြင်း

![Framework Intro](../../../translated_images/my/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) သည် AI agent များ တည်ဆောက်ရန် Microsoft ၏ ထဲဝင်ပေါင်းစည်းထားသော framework ဖြစ်သည်။ ၎င်းသည် ထုတ်လုပ်မှုနှင့် သုတေသနပတ်ဝန်းကျင်များရှိ agentic အသုံးပြုမှု များစွာကို ကောင်းစွာ ကိုင်တွယ်နိုင်ရန် ဖလှယ်နိုင်မှု ရှိသည်၊ ဤတွင်ပါဝင်သည်-

- **အဆင့်စဉ်တစ်ဆင့် Agent စီမံခန့်ခွဲမှု** - အဆင့်လိုက် အလုပ်လုပ်စဉ်များ လိုအပ်သော အခြေအနေများတွင်။
- **တပြိုင်နက် မှ လုပ်ဆောင်ခြင်း** - Agent များ တချိန်တည်း အလုပ်ပြီးစီးရန် လိုအပ်သော အခြေအနေများတွင်။
- **အုပ်စု စကားများ စီမံခန့်ခွဲမှု** - Agent များ တစ်လုပ်ဆောင်ချက်ပြန်ရန် တွဲဖက်ဆောင်ရွက်နိုင်သည့် အခြေအနေများတွင်။
- **လွှဲပြောင်း စီမံခန့်ခွဲမှု** - Agent များ တစ်ဦးကနေ တစ်ဦးဆီ သေးငယ်သော အလုပ်များ ပြီးစီးသလို လွှဲပြောင်းပေးသည့် အခြေအနေများတွင်။
- **ကွမ်းဆစ် စီမံခန့်ခွဲမှု** - အုပ်ချုပ်သူ agent တစ်ဦးသည် အလုပ်စာရင်းတစ်ရပ်ကို ဖန်တီးပြီး ပြုပြင်ပြောင်းလဲကာ သေးငယ်သော agent များနှင့် ပူးပေါင်း၍ အလုပ်ကိုပြီးစီးစေသည့် အခြေအနေများတွင်။

ထုတ်လုပ်မှုအတွက် AI Agent များ ပေးပို့ရာတွင် MAF တွင် အောက်ပါ အင်္ဂါရပ်များလည်း ပါဝင်သည်-

- **ကြည့်ရှုနိုင်မှု** - OpenTelemetry ကို အသုံးပြုကာ AI Agent ၏ လုပ်ဆောင်ချက်တိုင်း၊ tools ဖိတ်ခေါ်ခြင်း၊ စီမံခန့်ခွဲမှုအဆင့်များ၊ ရှာဖွေရေးစဉ်များနှင့် Microsoft Foundry dashboard များမှ တာဝန်ထမ်းဆောင်မှု စောင့်ကြည့်နိုင်ခြင်း။
- **လုံခြုံရေး** - agents များကို Microsoft Foundry ပေါ်တွင် native အနေနဲ့ တည်ဆောက်ထားခြင်းဖြင့် role-based access, ကိုယ်ပိုင်ဒေတာ ကာကွယ်မှုနှင့် အကြောင်းအရာ လုံခြုံရေး အစသော လုံခြုံရေးထိန်းချုပ်မှုများ ပါဝင်သည်။
- **ခံနိုင်ရည်** - Agent thread များနှင့် အလုပ်လုပ်စဉ်များသည် ရပ်နား၊ ပြန်တက်ခြင်းနှင့် အမှားများမှ ပြန်လည်ထူထောင်နိုင်မှုရှိသောကြောင့် ပိုမိုရှည်လျားသောလုပ်ငန်းစဉ်များ လုပ်နိုင်ခြင်း။
- **ထိန်းချုပ်မှု** - လူ့အတွင်း ပါဝင်မှုရှိသော workflow များကို မေးမြန်းနိုင်ပြီး အလုပ်များကို လူ့အတည်ပြုချက် လိုအပ်သည်ဖြင့် မှတ်သားပေးနိုင်ခြင်း။

Microsoft Agent Framework သည် အောက်ပါအတိုင်းလည်း အပြန်အလှန် လုပ်ဆောင်နိုင်စေရန် အာရုံစိုက်ထားသည်-

- **Cloud မျိုးစုံကို အတူတူ အသုံးပြုနိုင်ခြင်း** - Agent များကို container များ၊ on-premises နှင့် cloud မျိုးစုံတွင် ပြေးဆွဲနိုင်ခြင်း။
- **Provider မျိုးစုံကို လက်ခံနိုင်ခြင်း** - သင်နှစ်သက်ရာ SDK များဖြင့် Agent များ ဖန်တီးနိုင်ခြင်း၊ အတွင် Azure OpenAI နှင့် OpenAI ပါဝင်သည်။
- **Open Standards များ ပေါင်းစည်းခြင်း** - Agent-to-Agent (A2A) နှင့် Model Context Protocol (MCP) စသည့် ပရိုတိုကောများကို အသုံးပြုပြီး အခြား agent များနှင့် သုံးစွဲမှုတို့ကို ရှာတွေ့နိုင်ခြင်း။
- **Plugins နှင့် Connectors** - Microsoft Fabric, SharePoint, Pinecone နှင့် Qdrant တို့ကဲ့သို့ ဒေတာနှင့် မှတ်ဉာဏ် ဝန်ဆောင်မှုများနှင့် ချိတ်ဆက်နိုင်ခြင်း။

Microsoft Agent Framework ၏ အင်္ဂါရပ်များအား Microsoft Agent Framework ၏ အဓိက အယူအဆတချို့တွင် ဘယ်လို အသုံးပြုကြသည်ဆိုတာ ကြည့်လိုက်ရအောင်။

## Microsoft Agent Framework ၏ အဓိက အယူအဆများ

### Agents များ

![Agent Framework](../../../translated_images/my/agent-components.410a06daf87b4fef.webp)

**Agent များ ဖန်တီးခြင်း**

Agent ဖန်တီးခြင်းကို inference ဝန်ဆောင်မှု (LLM Provider) ကို သတ်မှတ်ခြင်း၊ AI Agent လိုက်နာရမည့် အညွှန်းများကို သတ်မှတ်ခြင်း၊ နှင့် `name` တပ်ဆင်ခြင်းဖြင့် ပြုလုပ်သည်-


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

အထက်မှာ `Azure OpenAI` ကို အသုံးပြုထားသော်လည်း `Microsoft Foundry Agent Service` အပါအဝင် ဝန်ဆောင်မှုမျိုးစုံဖြင့် agent များ ဖန်တီးနိုင်ပါသည်။

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API များ

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ဒါမှမဟုတ် [MiniMax](https://platform.minimaxi.com/) မှ ရရှိနိုင်ပြီး OpenAI ကို တူညီသော API ကို context window ကြီးများ (204K tokens အထိ) ဖြင့် ပံ့ပိုးပါသည်။

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ဒါမှမဟုတ် A2A ပရိုတိုကောကို အသုံးပြု၍ remote agent များကို အသုံးပြုနိုင်ပါသည်။

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agent များ စတင် လည်ပတ်ခြင်း**

Agents များကို `.run` သို့မဟုတ် `.run_stream` method များဖြင့် မရိုးရာ ပျံ့နှံ့မှု မရှိသော response များ သို့မဟုတ် streaming response များအတွက် အသုံးပြုနိုင်သည်။

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Agent တစ်ယောက်စီ run လုပ်ရာတွင် agent ကိုအသုံးပြုသော `max_tokens`, သုံးနိုင်သော `tools`, နှင့် agent အတွက် အသုံးပြုမည့် `model` အပါအဝင် ကန့်သတ်ချက်များကို user ပြင်၍ အသုံးပြုနိုင်ပါသည်။

၎င်းသည် အသုံးပြုသူ၏ အလုပ်ကို ဖြည့်ဆည်းရန် အထူးသတ်မှတ်ထားသော model များ သို့မဟုတ် tools များ လိုအပ်သောအခြေအနေများတွင် အထောက်အကူ ဖြစ်သည်။

**Tools များ**

Tools များကို agent ကို သတ်မှတ်စဉ်တွင်သတ်မှတ်နိုင်သည်-

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ChatAgent ကိုတိုက်ရိုက်ဖန်တီးသောအခါ

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

သို့မဟုတ် agent run လုပ်သည့်အခါတွင်လည်း သတ်မှတ်နိုင်သည်-

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ဒီလုလုပ်ချက်အတွက်သာ ပစ္စည်း (ကိရိယာ) ပေးထားခြင်း)
```

**Agent Threads**

Multi-turn စကားပြောဆိုမှုများကို ကိုင်တွယ်ရန် Agent Threads ကို သုံးသည်။ Thread များကို အောက်ပါနည်းလမ်းများဖြင့် ဖန်တီးနိုင်သည်-

- `get_new_thread()` ကို သုံးပြီး thread ကို အချိန်အလိုက် သိမ်းဆည်းထားနိုင်သည်
- Agent run လုပ်တဲ့အခါ စက်ဖြင့် thread ကို ဖန်တီးပြီး လက်ရှိ run အတွင်းစတင်အဆုံးသာရှိသည့် thread ဖြစ်သည်။

Thread ဖန်တီးရန် ကုဒ်က ဒီလိုပုံစံပါ-

```python
# သွားကြောင်းအသစ် တစ်ခု ဖန်တီးပါ။
thread = agent.get_new_thread() # အဲဂျင့်ကို သွားကြောင်းနှင့် တစ်ပြိုင်နက် ပြေးပါ။
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

နောက်တစ်ချိန်တွင် အသုံးပြုရန် thread ကို serialize လုပ်၍ သိမ်းဆည်းနိုင်သည်-

```python
# အသစ်သော တေ့ဒ်ကို ဖန်တီးပါ။
thread = agent.get_new_thread() 

# အဲဂျင့်ကို တေ့ဒ်နှင့် အတူ ပြေးပါ။

response = await agent.run("Hello, how are you?", thread=thread) 

# သိမ်းဆည်းရန် တေ့ဒ်ကို စီးရီးလိုက်ချပါ။

serialized_thread = await thread.serialize() 

# သိမ်းဆည်းထားသောနေရာမှ ဖတ်ပြီးနောက် တေ့ဒ်အခြေအနေကို ပြန်လည်ဖော်ထုတ်ပါ။

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agent များသည် အသုံးပြုသူအလုပ်များ ပြီးစီးရန် tools နှင့် LLM များနှင့် ဆက်သွယ်သည်။ အချို့ အခြေအနေများတွင် ၎င်းဆက်သွယ်မှုများတွင် အကြား ဆောင်ရွက်စေရန် သို့မဟုတ် လိုက်လံစောင့်ကြည့်ရန် လိုအပ်သည်။ Agent middleware သည် အောက်ပါအတိုင်း ပြုလုပ်နိုင်စေသည်-

*Function Middleware*

ဤ middleware သည် agent နှင့် function/tool တို့အကြား လုပ်ဆောင်မှု တစ်ခုကို အကောင်အထည်ဖော်ရန် ခွင့်ပြုသည်။ ဥပမာအားဖြင့် function call တစ်ခုကို logging ပြုလုပ်လိုသောအခါ အသုံးပြုနိုင်သည်။

နမူနာကုဒ်တွင် `next` သည် နောက်တစ်ခု middleware သို့မဟုတ် မူရင်း function ကို ခေါ်ဆိုရမည်ကို သတ်မှတ်သည်။

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # မူလလုပ်ဆောင်မှုမပြုမီ မှတ်တမ်းတင်ခြင်း
    print(f"[Function] Calling {context.function.name}")

    # နောက်တစ်ခု middleware သို့မဟုတ် function ကို ဆက်လက်ဆောင်ရွက်ရန်
    await next(context)

    # လုပ်ဆောင်မှုပြီးချိန့် မှတ်တမ်းတင်ခြင်း
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

ဤ middleware သည် agent နှင့် LLM တို့အကြား ပြန်လည်တောင်းဆိုမှုများကို လုပ်ဆောင်ရန် သို့မဟုတ် logging ပြုလုပ်ရန် ခွင့်ပြုသည်။

ဤတွင် AI ဝန်ဆောင်မှုသို့ ပို့ဆောင်သည့် `messages` များ စသည့် အရေးကြီးသော အချက်အလက်များ ပါဝင်သည်။

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ကြိုတင်ကုသမှု: AI ခေါ်ဆိုမှုမပြုမီ မှတ်တမ်းတင်ခြင်း
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # နောက်ထပ် middleware သို့မဟုတ် AI ဝန်ဆောင်မှုသို့ ဆက်လုပ်ဆောင်ရန်
    await next(context)

    # နောက်ကုသမှု: AI တုံ့ပြန်ချက်လက်ခံပြီးနောက် မှတ်တမ်းတင်ခြင်း
    print("[Chat] AI response received")

```

**Agent Memory**

`Agentic Memory` သင်ခန်းစာတွင် ဖေါ်ပြခဲ့သည့်အတိုင်း မှတ်ဉာဏ်သည် agent အနေဖြင့် မတူညီသော context များပေါ်တွင် လည်ပတ်နိုင်ရန် အရေးကြီးသော အရာဖြစ်သည်။ MAF တွင် မှတ်ဉာဏ် အမျိုးအစားများစွာ ပါဝင်သည်-

*In-Memory Storage*

၎င်းသည် application runtime အတွင်း thread များတွင် သိမ်းဆည်းထားသော မှတ်ဉာဏ်ဖြစ်သည်။

```python
# ချိတ်ဆက်မှုအသစ် တစ်ခု ဖန်တီးပါ။
thread = agent.get_new_thread() # ချိတ်ဆက်မှုဖြင့် ပြုလုပ်မြှပ်ထားသော ကိုယ်စားလှယ်ကို လည်ပတ်ပါ။
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

မတူညီသော session များအတွင်း စကားပြောဆိုမှုမှတ်တမ်းများ သိမ်းဆည်းရန် အသုံးပြုသည်။ ၎င်းကို `chat_message_store_factory` ဖြင့် သတ်မှတ်သည်။

```python
from agent_framework import ChatMessageStore

# စိတ်ကြိုက်စာတိုက် သိမ်းဆည်းရန် ဖန်တီးပါ
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamic Memory*

Agent များ run မပြုမီ context တွင် ထည့်သွင်းသည့် မှတ်ဉာဏ်ဖြစ်သည်။ ၎င်းများကို mem0 ကဲ့သို့သော ပြင်ပဝန်ဆောင်မှုများတွင် သိမ်းဆည်းနိုင်သည်။

```python
from agent_framework.mem0 import Mem0Provider

# အဆင့်မြင့်မှတ်ဉာဏ်စွမ်းဆောင်ရည်များအတွက် Mem0 ကိုအသုံးပြုခြင်း
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

**Agent ကြည့်ရှုနိုင်မှု**


agentic စနစ်များကို ယုံကြည်စိတ်ချရပြီး ပြုပြင်ထိန်းသိမ်းနိုင်ရန် Observability သည် အရေးကြီးသည်။ MAF သည် OpenTelemetry နှင့် ပေါင်းစပ်ကာ လုပ်ဆောင်မှုစောင့်ကြပ်မှုနှင့် မီတာများကို ပေးပြီး Observability ကို ပိုမိုကောင်းမွန်စေသည်။

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # မည်သည့်အရာမဆိုလုပ်ဆောင်ပါ
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### လုပ်ငန်းစဥ်များ

MAF သည် တစ်ခုသော အလုပ်တစ်ခုကို ပြီးစီးရန် ကြိုတင်သတ်မှတ်ထားသော အဆင့်များရှိသည့် လုပ်ငန်းစဥ်များကို ပေးသည်။ ၎င်းအဆင့်များတွင် AI agent များကို ပါဝင်ပစ္စည်းများအဖြစ် စုစည်းထားသည်။

လုပ်ငန်းစဥ်များသည် ပိုမိုကောင်းမွန်သည့် ထိန်းချုပ်မှုစီးဆင်းမှုကို ခွင့်ပြုသော မတူညီသော ပစ္စည်းများဖြင့် ဖွဲ့စည်းထားသည်။ လုပ်ငန်းစဥ်များသည် **အတင်းအကျပ် စီမံခန့်ခွဲမှု (multi-agent orchestration)** နှင့် **checkpointing** ကိုလည်း အထောက်အပံ့ပြု၍ လုပ်ငန်းစဉ်အခြေအနေများကို သိမ်းဆည်းနိုင်သည်။

လုပ်ငန်းစဉ်၏ အချက်အလက်အဓိက လုပ်ဆောင်ပစ္စည်းများမှာ -

**အကောင်အထည်ဖော်သူများ (Executors)**

အကောင်အထည်ဖော်သူများတွင် အဝင်စာတိုက်များကို ရရှိပြီး, တာဝန်ပေးထားသော လုပ်ငန်းများကို လုပ်ဆောင်ကာ ထွက်ရှိစာတိုက်တစ်ခု ထုတ်ပေးသည်။ ၎င်းသည် လုပ်ငန်းစဉ်ကို ပိုမိုကြီးမားသော တာဝန်ကို အပြီးသတ်ရန် ရွှေ့ပြောင်းစေသည်။ အကောင်အထည်ဖော်သူများသည် AI agent သို့မဟုတ် စိတ်ကြိုက်လောဂျစ်တစ်ခု ဖြစ်နိုင်သည်။

**အကျဉ်း (Edges)**

အကျဉ်းများကို လုပ်ငန်းစဉ်တွင် စာတိုက်စီးဆင်းမှုကို သတ်မှတ်ရန် သုံးသည်။ ၎င်းတို့သည် -

*တိုက်ရိုက် အကျဉ်းများ* - အကောင်အထည်ဖော်သူများအကြား တစ်ခုနှင့်တစ်ခု သာ ချိတ်ဆက်မှုများ။

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*အခြေအနေအလျောက် အကျဉ်းများ* - အခြေအနေတစ်ခု ပြည့်မှောက်ပြီးနောက် ဖွင့္လှစ်သည်။ ဥပမာ ဂိုဒေါင်အခန်းများ မရနိုင်သောအခါမှာ အကောင်အထည်ဖော်သူတစ်ဦးက အခြားရွေးချယ်စရာများကို အကြံပြုနိုင်သည်။

*Switch-case အကျဉ်းများ* - သတ်မှတ်ထားသော အခြေအနေများအပေါ် အခြေခံ၍ စာတိုက်များကို အကောင်အထည်ဖော်သူအမျိုးမျိုးသို့ လမ်းညွှန်ပေးသည်။ ဥပမာ - ခရီးသွားဖောက်သည်တွင် ဦးစားပေးဝင်ခွင့် ရှိပါက ၎င်းတို့ရဲ့ လုပ်ငန်းများကို ထောင့်တစ်ခုရှိ မတူညီသော လုပ်ငန်းစဉ်မှတစ်ဆင့် ကိုင်တွယ်မည်ဖြစ်သည်။

*Fan-out အကျဉ်းများ* - တစ်ခုသော စာတိုက်ကို အတန်းတစ်ခုထဲ ရောက်ရှိသည့် တစ်ချို့သောလမ်းများသို့ ပေးပို့သည်။

*Fan-in အကျဉ်းများ* - မတူညီသော အကောင်အထည်ဖော်သူများမှ စာတိုက်များစုပြီး တစ်ခုသော လမ်းသို့ ပေးပို့သည်။

**ပွဲများ (Events)**

လုပ်ငန်းစဉ်များကို ပိုမိုကောင်းမွန်စွာ စောင့်ကြည့်ရန် MAF သည် အလုပ်ဆောင်မှု ပွဲများကို အောက်ပါအတိုင်း ထောက်ပံ့သည်။

- `WorkflowStartedEvent`  - လုပ်ငန်းစဉ် စတင်မှု
- `WorkflowOutputEvent` - လုပ်ငန်းစဉ် ထွက်ရှိမှု
- `WorkflowErrorEvent` - လုပ်ငန်းစဉ်တွင် အမှားဖြစ်ပေါ်ခြင်း
- `ExecutorInvokeEvent`  - အကောင်အထည်ဖော်သူ စတင်လုပ်ဆောင်ခြင်း
- `ExecutorCompleteEvent`  - အကောင်အထည်ဖော်သူ လုပ်ဆောင်မှုပြီးဆုံးခြင်း
- `RequestInfoEvent` - တောင်းဆိုမှုတစ်ခု ထုတ်ပြန်ခြင်း

## မြင့်မားသော MAF ပုံစံများ

အထက်ပါ အပိုင်းများတွင် Microsoft Agent Framework ၏ အဓိက အယူအဆများကို ဖော်ပြထားသည်။ သင်က ပိုမိုရှုပ်ထွေးသော agent များတည်ဆောက်သည့်အခါ အောက်ပါ မြင့်မားသော ပုံစံများကို စဉ်းစားနိုင်သည်။

- **Middleware Composition**: လုပ်ဆောင်မှုတိုင်းအတွက် log ဖတ်ခြင်း၊ အသုံးပြုခွင့်နှင့် အမြန်နှုန်းကန့်သတ်မှု middleware ကို function နှင့် chat middleware ဖြင့် ချိတ်ဆက်၍ agent အပြုအမှုအပေါ် အသေးစိတ်ထိန်းချုပ်မှု။
- **Workflow Checkpointing**: workflow ပွဲများနှင့် serialization ကို အသုံးပြုပြီး ကြာရှည် သက်တမ်း agent လုပ်ငန်းစဉ်များကို သိမ်းဆည်းရန်နှင့် ပြန်လည်စတင်ရန်။
- **Dynamic Tool Selection**: RAG ကို tool ဖော်ပြချက်များအပေါ် ပေါင်းစပ်ပြီး MAF ၏ tool မှတ်ပုံတင်မှုနှင့် တွဲ၍ လွှာမေးခွန်းတိုင်းအတွက် သက်ဆိုင်ရာ ဉာဏ်စမ်းပစ္စည်းများသာ ပြသခြင်း။
- **Multi-Agent Handoff**: workflow အကျဉ်းများနှင့် အခြေအနေအလျောက် လမ်းညွှန်မှုကို အသုံးပြု၍ အထူးပြု agent များအကြား လက်ခံပေးခြင်းကို စီမံခန့်ခွဲခြင်း။

## Microsoft Foundry ပေါ်တွင် LangChain / LangGraph Agents များ တည်ဆောက်ခြင်း

Microsoft Agent Framework သည် **framework-interoperable** ဖြစ်သည် — သင်သည် MAF ဖြင့်ရေးသားထားသည့် agent များသာမက၊ **LangChain** သို့မဟုတ် **LangGraph** ဖြင့် ရေးသားထားသော agent များကိုပါ Official Microsoft Foundry ရှိ hosted agent အဖြစ် ပြေးနိုင်သည်။ ဒီအခါ သင်၏ agent logic သည် LangGraph မှာတည်ရှိသော်လည်း Foundry သည် runtime, sessions, scaling, identity, နှင့် protocol endpoints များကို စီမံခန့်ခွဲပေးသည်။

၎င်းကို `langchain_azure_ai.agents.hosting` အထုပ်ဖြင့် ပြုလုပ်နိုင်ပြီး LangGraph graph တစ်ခုကို Foundry hosted agent များအသုံးပြုသည့် protocols များနှင့် တူညီသော protocols တွင် ဖော်ပြသည်။

**1. hosting extra ကို တပ်ဆင်ပါ:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` extra သည် Foundry protocol စာကြည့်တိုက်များဖြစ်သည့် `azure-ai-agentserver-responses` (OpenAI-compatible `/responses` endpoint) နှင့် `azure-ai-agentserver-invocations` (generic `/invocations` endpoint) ကို တပ်ဆင်ပေးသည်။

**2. hosting protocol ကို ရွေးချယ်ပါ:**

| Protocol | Host class | Endpoint | အသုံးပြုသည့်အချိန် |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | OpenAI-compatible chat, streaming, response history နှင့် စကားပြော Threading လုပ်နိုင်သော agent များအတွက် အကြံပြုသည့် Default ဖြစ်သော conversational agents များအတွက်။ |
| **Invocations** | `InvocationsHostServer` | `/invocations` | custom JSON shape, webhook-style endpoint သို့မဟုတ် စကားပြောမဟုတ်သော လုပ်ဆောင်မှုများလိုအပ်သောအခါ။ |

**Responses API သည် Foundry တွင် agent များ ဖွံ့ဖြိုးတိုးတက်မှုအတွက် အဓိက API ဖြစ်သည့်ကြောင့်** အများဆုံး agent များအတွက် `ResponsesHostServer` ဖြင့် စတင်ရန် အကြံပြုသည်။

**3. ပတ်ဝန်းကျင်သတ်မှတ်ချက်များ (environment variables) ကို ပြင်ဆင်ပါ** (`az login` လုပ်ပြီး `DefaultAzureCredential` အသုံးပြုနိုင်ရန်):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

agent ကို နောက်ပိုင်း Foundry တွင် hosted agent အဖြစ် ပြေးသောအခါ 플랫폼သည် `FOUNDRY_PROJECT_ENDPOINT` ကို မူလပြင်သတ်မှတ်ချက်အလိုက် ကိုယ်တိုင် ထည့်သွင်းပေးသည်။

**4. LangGraph agent ကို Responses protocol ဆက်သွယ်မှုဖြင့် ဖော်ပြပါ:**

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

    # ChatOpenAI သည် Foundry project ၏ OpenAI- ကိုက်ညီသော (Responses) endpoint ကို ပစ်မှတ်ထားသည်။
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

ဒါကို စက်ပေါ်တွင် `python main.py` ဖြင့် ပြေးပြီးနောက် `http://localhost:8088/responses` သို့ Responses တောင်းဆိုမှု ပို့ပါ။

**အဓိကအပြုအမှုများ:**

- **စကားဝိုင်းများ**: Clients များသည် `previous_response_id` သို့မဟုတ် `conversation` ID တစ်ခု ဖြင့် စကားဝိုင်းကို ဆက်လက်ဆောင်ရွက်သည်။ သင်၏ စာမျက်နှာသည် LangGraph checkpoint နဲ့ ပြုလုပ်ထားပါက Foundry သည် စကားဝိုင်းအခြေအနေကို checkpoint နှင့် ကိုက်ညီစေလိမ့်မည် (ထုတ်လုပ်မှုတွင် durable checkpointer အသုံးပြုပါ၊ ဒါ့အပြင် `MemorySaver` သည် ဒေသဆိုင်ရာ စမ်းသပ်မှုများအတွက် ပြည့်စုံသည်)။
- **လူအပြန်အလှန်**: သင်၏ စာမျက်နှာသည် LangGraph `interrupt()` ကို အသုံးပြုပါက `ResponsesHostServer` သည် မပြုလုပ်သေးသည့် interrupt ကို Responses `function_call` / `mcp_approval_request` အဖြစ် ပြသပြီး clients များသည် `function_call_output` / `mcp_approval_response` နှင့်လိုက်ဖက်သော ဖြေဆိုမှုဖြင့် ဆက်လက်လုပ်ဆောင်သည်။
- **Foundry သို့ တင်ပို့ခြင်း**: Azure Developer CLI ကို အသုံးပြု၍ — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (ဒို့ကာလိုက်ရှိရန်)၊ ထို့နောက် `azd provision` နှင့် `azd deploy` လုပ်ပါ။ Hosted-agent deployment သည် **Foundry Project Manager** အခန်းကဏ္ဍလိုအပ်သည်။

ဤနမူနာ၏ ပြေးနိုင်သောဗားရှင်းကို [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) တွင် ဖတ်ရှုနိုင်သည်။ အပြည့်အစုံ walkthrough (Invocations protocol, custom request schemas, နှင့် troubleshooting) များအတွက် [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) ကို ကြည့်ပါ။

## ကုတ်နမူနာများ 

Microsoft Agent Framework အတွက် ကုတ်နမူနာများကို ဤ repository တွင် `xx-python-agent-framework` နှင့် `xx-dotnet-agent-framework` ဖိုင်များအောက်တွင် တွေ့နိုင်ပါသည်။

## Microsoft Agent Framework အကြောင်း နောက်ထပ်မေးခွန်းများရှိပါသလား?

အခြားလေ့လာသူများနှင့် တွေ့ဆုံစကားပြောရန်, office hours များတွင် ပါဝင်ရန် နှင့် သင့် AI Agents မေးခွန်းများကို ဖြေဆိုရန် [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) သို့ ပါ၀င်ဆက်သွယ်ပါ။
## အရင်သင်ခန်းစာ

[Memory for AI Agents](../13-agent-memory/README.md)

## နောက်တစ်ခုပညာသင်ခန်းစာ

[Building Computer Use Agents (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->