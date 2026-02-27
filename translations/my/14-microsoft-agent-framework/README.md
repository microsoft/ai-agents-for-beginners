# Microsoft Agent Framework ကို လေ့လာခြင်း

![Agent Framework](../../../translated_images/my/lesson-14-thumbnail.90df0065b9d234ee.webp)

### မိတ်ဆက်

ဒီသင်ခန်းစာမှာ အောက်ပါအကြောင်းအရာများကို ဖော်ပြသွားမှာ ဖြစ်ပါတယ်-

- Microsoft Agent Framework ကိုနားလည်ခြင်း။ အဓိက လက္ခဏာများနှင့် တန်ဖိုးများ  
- Microsoft Agent Framework ၏ အဓိက အယူအဆများကို ရှာဖွေခြင်း
- ကြီးမားသော MAF ပုံစံများ- Workflow များ၊ Middleware နှင့် မှတ်ဉာဏ်

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဒီသင်ခန်းစာပြီးဆုံးမည့်အခါ သင်သည်-

- Microsoft Agent Framework ကို အသုံးပြု၍ ထုတ်လုပ်မှုအဆင့် အဆင့်အသစ် AI Agent များကို တည်ဆောက်နိုင်မည်
- Microsoft Agent Framework ၏ အဓိက လက္ခဏာများကို သင့် Agent ဆိုင်ရာ အသုံးပြုမှုများတွင် လျှောက်ထားနိုင်မည်
- Workflow များ၊ middleware နှင့် ကြည့်ရှုနိုင်ရေးများ အပါအဝင် ကြီးမားသော ပုံစံများကို အသုံးပြုနိုင်မည်

## ကွပ်ကိုဒ် နမူနာများ

Microsoft Agent Framework (MAF) အတွက် ကွပ်ကိုဒ် နမူနာများကို ဒီ repository ထဲမှ `xx-python-agent-framework` နှင့် `xx-dotnet-agent-framework` ဖိုင်များတွင် ရှာဖွေတွေ့နိုင်ပါသည်။

## Microsoft Agent Framework ကို နားလည်ခြင်း

![Framework Intro](../../../translated_images/my/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) သည် Microsoft ၏ AI agent များ တည်ဆောက်ရန် ယူနိုက်ဖက် Framework ဖြစ်သည်။ ထုတ်လုပ်မှုနှင့် သုတေသန ပတ်ဝန်းကျင်များတွင် တွေ့ရှိရသော agentic အသုံးပြုမှုမျိုးစုံကို ဖြေရှင်းနိုင်စေရန် ပေါင်းစပ်ထားသည်။ ၎င်းတွင်-

- **စဉ်ဆက်မပြတ် Agent အဆင့်ဆင့် စီမံခန့်ခွဲမှု** - အဆင့်ခြင်း Workflow များ လိုအပ်သောအခြေအနေများတွင်
- **အချိန်တပြေးညီ စီမံခန့်ခွဲမှု** - Agent များ တပြိုင်နက် တာဝန်များ ပြီးမြောက်စေရန်လိုအပ်သောအခြေအနေများတွင်
- **အုပ်စု စကားပြောစီမံခန့်ခွဲမှု** - Agent များ တစ်ခုတည်းသော တာဝန်တစ်ခု အပေါ် ပူးပေါင်းဆောင်ရွက်နိုင်သောအခြေအနေများတွင်
- **အလုပ်ပေးအပ်မှု စီမံခန့်ခွဲမှု** - Agent များ တာဝန်များကို တစ်ဦးမှတစ်ဦးသို့ အလုပ်ပေးအပ်သွားခြင်း  (subtasks ပြီးမြောက်သည့်အခါ)
- **Magnetic စီမံခန့်ခွဲမှု** - မန်နေဂျာ Agent သည် တာဝန်စာရင်းကို ဖန်တီးပြင်ဆင်ပြီး subagent များကို ညှိနှိုင်းကူညီစေခြင်း

ထုတ်လုပ်မှု AI Agents ချမှတ်ရာတွင် MAF သည် အောက်ပါ လက္ခဏာများပါဝင်သည်-

- **ကြည့်ရှုနိုင်မှု**- OpenTelemetry အသုံးပြု၍ AI Agent ၏ လှုပ်ရှားမှုတိုင်း၊ ကိရိယာ သုံးစွဲခြင်း၊ စီမံခန့်ခွဲမှု အဆင့်များ၊ မှတ်ချက်တည်ဆောက်မှု၊ Microsoft Foundry dashboard များမှ စွမ်းဆောင်ရည် စောင့်ကြည့်မှုများ။
- **လုံခြုံမှု**- Microsoft Foundry တွင် Agent များကို တိုက်ရိုက် ဟိုစ့်လုပ်ခြင်းဖြင့် Role-based access, ပုဂ္ဂိုလ်ရေး အချက်အလက် ကိုင်တွယ်မှု နှင့် built-in မူဝါဒ လုံခြုံရေးကိုပါ ထည့်သွင်းထားခြင်း။
- **ခံနိုင်ရည်**- Agent threads နှင့် workflows များသည် ရပ်ဆိုင်း၊ ပြန်စတင်နှင့် အမှားမှ ပြန်လည်ကောင်းမွန်နိုင်ခြင်းဖြင့် ကြာရှည်ပြေးနေမှု ဖြစ်စေခြင်း။
- **ထိန်းချုပ်မှု**- လူဖက် ကုန်လမ်းများ ပါဝင်ပြီး တာဝန်များသည် လူသည် အတည်ပြုရန် လိုအပ်သည် ဟူ၍ သတ်မှတ်နိုင်ခြင်း။

Microsoft Agent Framework သည် interoperability ကိုလည်း ဦးတည်ထားပြီး-

- **Cloud-ပလက်ဖောင်းမပါးပါး** - Agent များကို containers, on-premises နှင့် Cloud များအနှံ့ အသုံးပြုနိုင်ခြင်း။
- **Provider မပါးပါး** - Azure OpenAI နှင့် OpenAI အပါအဝင် သင့်နှစ်သက်ရာ SDK များဖြင့် Agent များ ဖန်တီးနိုင်ခြင်း။
- **Open စံချိန်စံညွှန်းများ ပေါင်းစပ်မှု** - Agent-to-Agent (A2A) နှင့် Model Context Protocol (MCP) ကြိုဆိုမှုများဖြင့် တခြား Agent များ နဲ့ ကိရိယာများ ကိုရှာဖွေနိုင်ခြင်း။
- **Plugins နှင့် Connectors** - Microsoft Fabric, SharePoint, Pinecone နှင့် Qdrant ကဲ့သို့ ဒေတာနှင့် မှတ်ဉာဏ် ဝန်ဆောင်မှုများ ချိတ်ဆက်နိုင်ခြင်း။

ယခု Microsoft Agent Framework ၏ အဓိက အယူအဆများ ချိတ်ဆက်တည်ဆောက်မှုကို လေ့လာကြပါစို့။

## Microsoft Agent Framework ၏ အဓိက အယူအဆများ

### Agents

![Agent Framework](../../../translated_images/my/agent-components.410a06daf87b4fef.webp)

**Agent ဖန်တီးခြင်း**

Agent ဖန်တီးခြင်းမှာ inference service (LLM Provider) ကို သတ်မှတ်ခြင်း၊ AI Agent လိုက်နာရမည့် လမ်းညွှန်ချက်များကို သတ်မှတ်ခြင်းနှင့် `name` တစ်ခုချထားခြင်းဖြင့် ပြုလုပ်သည်-

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```
  
အထက်မှာ `Azure OpenAI` ကို အသုံးပြုထားသော်လည်း `Microsoft Foundry Agent Service` ကဲ့သို့ အမျိုးမျိုးသော ဝန်ဆောင်မှုများဖြင့်လည်း Agent များ ဖန်တီးနိုင်သည်-

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```
  
OpenAI ၏ `Responses`, `ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```
  
```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```
  
သို့မဟုတ် A2A protocol ကို အသုံးပြု၍ remote agent များဖြင့်လည်း-

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```
  
**Agent မောင်းနှင်ခြင်း**

Agent များကို `.run` သို့မဟုတ် `.run_stream` များဖြင့် မောင်းနှင်နိုင်ပြီး non-streaming သို့ streaming ထုတ်ပြန်မှု အတွက် အသုံးပြုသည်။

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```
  
```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```
  
Agent မောင်းနှင်ရာတွင် `max_tokens`၊ အေးဂျင့်ခေါ်နိုင်သော `tools` များ နှင့် သုံးရန် `model` များ စသည်တို့ကို စိတ်ကြိုက်ပြင်ဆင်နိုင်သည်။

အသုံးပြုသူ၏ တာဝန် ပြီးမြောက်ရန် အထူးသီးသန့် မော်ဒယ်များ သို့မဟုတ် ကိရိယာများ လိုအပ်သောအခါ အသုံးဝင်သည်။

**ကိရိယာများ (Tools)**

Agent ကို သတ်မှတ်တဲ့အခါ ဆောက်နိုင်သလို-

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ChatAgent ကိုတိုက်ရိုက်ဖန်တီးသောအခါ

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```
  
Agent မောင်းစဉ်တွင်လည်း သတ်မှတ်နိုင်သည်-

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ဒီသုံးမှသာ အသုံးပြုရန် ကိရိယာ provided ဖြစ်သည် )
```
  
**Agent Threads**

Agent Thread များကို multi-turn စကားပြောပလုတ်များကို ဦးစီးရန်အသုံးပြုသည်။ Threads များကို-

- `get_new_thread()` ဖြင့် Thread ကို အချိန်ကြာမြင့်စွာ သိမ်းဆည်းနိုင်
- Agent မောင်းစဉ် အလိုအလျောက် Thread ဖန်တီးနိုင်၊ အဲဒီအချိန်အထိသာ မည်သို့တည်ရှိစေမည်။

Thread ဖန်တီးရန် ကုဒ်သည်-

```python
# သွားရောက်မှုအသစ်တစ်ခု ဖန်တီးပါ။
thread = agent.get_new_thread() # သွားရောက်မှုနှင့်အတူ ကိုယ်စားလှယ်ကို ပြေးဆွဲပါ။
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```
  
နောက်ပြီး Thread ကို သိမ်းဆည်းရန် serialize လုပ်နိုင်သည်-

```python
# သစ်သော thread အသစ်ကို ဖန်တီးပါ။
thread = agent.get_new_thread() 

# အဲဂျင့်ကို thread ဖြင့် ပြေးပါ။

response = await agent.run("Hello, how are you?", thread=thread) 

# သိမ်းဆည်းမှုအတွက် thread ကို စီးရီးလိုက်ပြုလုပ်ပါ။

serialized_thread = await thread.serialize() 

# သိမ်းဆည်းမှုပြီးနောက် thread အခြေအနေကို ပြန်ထုတ်ပါ။

resumed_thread = await agent.deserialize_thread(serialized_thread)
```
  
**Agent Middleware**

Agents များသည် Tools နှင့် LLM များနှင့် ဆက်သွယ်ကိရိယာ အသုံးပြုပြီး တာဝန် ပြီးမြောက်စေသည်။ တချို့အခြေအနေများတွင် အဲဒီဆက်သွယ်မှု ကြားတွင် လုပ်ဆောင်မှု သို့ဆိုလည်း မှတ်တမ်းတင်လိုခြင်း ဖြစ်နိုင်သည်။ ထိုသို့လုပ်နိုင်ခြင်းအတွက် Agent middleware အသုံးပြုသည်-

*Function Middleware*  
ဒီ middleware သည် Agent နှင့် function/tool ခေါ်ဆိုမှုကြား လုပ်ဆောင်ချက် တစ်ခု ပါဝင်ခွင့် ပေးသည်။ ဥပမာ၊ function ခေါ်ဆိုမှုကို အကြောင်းပြု အချက်အလက် မှတ်တမ်းတင်ချင်သောအခါ အသုံးပြုသည်။

Code အောက်တွင် `next` သည် နောက်တစ်ခု middleware သို့မဟုတ် function ကို ခေါ်ဆိုရန် သတ်မှတ်သည်။

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ကြိုတင်အဆင့်လုပ်ဆောင်ခြင်း: ဖန်ရှင်အလုပ်ဆောင်မှုမတိုင်မီ မှတ်တမ်းတင်ခြင်း
    print(f"[Function] Calling {context.function.name}")

    # နောက်တစ်ခု middleware သို့ function အလုပ်ဆောင်မှုဆက်လက်လုပ်ဆောင်ခြင်း
    await next(context)

    # အလုပ်ပြီးသည့်အခါ အဆင့်ဆက်လုပ်ဆောင်ခြင်း: ဖန်ရှင်အလုပ်ပြီးနောက် မှတ်တမ်းတင်ခြင်း
    print(f"[Function] {context.function.name} completed")
```
  
*Chat Middleware*  
Agent နှင့် LLM အကြား တောင်းဆိုမှုများအကြား လုပ်ဆောင်ချက် တစ်ခု ထည့်သွင်းခြင်း သို့မဟုတ် မှတ်တမ်းတင်ခြင်း ပေးနိုင်သည်။

၎င်းတွင် AI ဝန်ဆောင်မှုသို့ ပို့သော `messages` အချက်အလက် ပါဝင်သည်။

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ကြိုတင်ပြင်ဆင်ခြင်း: AI ခေါ်ဆိုမှုပြီးမှတ်တမ်းတင်ခြင်း
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # နောက်ဆက်တွဲ middleware သို့မဟုတ် AI service သို့ ဆက်လက်သွားရန်
    await next(context)

    # နောက်ပြုလုပ်ခြင်း: AI တုံ့ပြန်ချက်ရရှိပြီးမှတ်တမ်းတင်ခြင်း
    print("[Chat] AI response received")

```
  
**Agent မှတ်ဉာဏ်**

`Agentic Memory` သင်ခန်းစာတွင် ဖော်ပြခဲ့သည့်အတိုင်း အေးဂျင့်သည် ကွဲပြားသော context များတွင် ဆောင်ရွက်နိုင်ရန် မှတ်ဉာဏ်မှာ အရေးကြီးသည်။ MAF တွင် memory အမျိုးအစား များစွာပါဝင်သည်-

*In-Memory Storage*  
Application runtime အတွင်း Thread များတွင် သိမ်းဆည်းထားသော မှတ်ဉာဏ်။

```python
# သဲရဲကြိုးအသစ်တစ်ခု ဖန်တီးပါ။
thread = agent.get_new_thread() # ထိုသဲရဲကြိုးနှင့်အတူ အေးဂျင့်ကို ယူဆောင်ပြေးပါ။
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```
  
*Persistent Messages*  
အခြား Session များအတွင်း စကားပြောမှတ်တမ်း သိမ်းဆည်းရာသုံးသည်။ `chat_message_store_factory` ဖြင့် သတ်မှတ်သည်-

```python
from agent_framework import ChatMessageStore

# ပုဂ္ဂိုလ်ရေး စာတည်းသိုလှောင်မှုဆိုင်ရာ ဆိုင်ကို ဖန်တီးပါ။
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```
  
*Dynamic Memory*  
Agent များအတွက် စခရင် အသစ်များ ထည့်သွင်းမည့် Context မတိုင်ခင် ထည့်သွင်းပေးသည်။ အစီအစဉ်ကို mem0 ကဲ့သို့သော နိုင်ငံခြား ဝန်ဆောင်မှုများထဲ ထည့်သိမ်းနိုင်သည်-

```python
from agent_framework.mem0 import Mem0Provider

# အဆင့်မြင့်မှတ်ဥာဏ်စွမ်းရည်များအတွက် Mem0 ကိုအသုံးပြုခြင်း
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
  
**Agent ၏ ကြည့်ရှုနိုင်ရေး (Observability)**

Agentic စနစ် တည်ဆောက်ရာတွင် ကြည့်ရှုနိုင်ရေး အရေးကြီးသည်။ MAF သည် OpenTelemetry နှင့် ပေါင်းစပ်၍ ပိုမိုကောင်းမွန်သော tracing နှင့် meter များ ရရှိစေသည်။

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # ဘာလို မလုပ်ကြပါ။
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```
  
### Workflow များ

MAF သည် တာဝန်တစ်ခု ပြီးမြောက်စေရန် ပြီးပြည့်စုံသည့် အဆင့်ဆင့် အဆင့်များ ပါသော Workflow များ ပါဝင်သည်။ AI Agent များကို လုပ်ဆောင်ချက် တစ်ခုတည်းအတွင်း တွဲတွယ်သွားသည်။

Workflow များတွင် ကြိုတင်သတ်မှတ်ထားသော component များ ပါဝင်ပြီး ထိန်းချုပ်မှု ပိုမိုကောင်းစေသည်။ Workflow များသည် **multi-agent orchestration** နှင့် **checkpointing** (Workflow အခြေအနေ သိမ်းဆည်းခြင်း) ကိုလည်း ပံ့ပိုးသည်။

Workflow ၏ အဓိက component များမှာ-

**Executors**

Executor များသည် input message များကို လက်ခံပြီး, တာဝန် ဖြည့်ဆောင်ပြီး, ထွက်သည့် output message များ ဖန်တီးပေးသည်။ ၎င်းက workflow ကို ပြီးမြောက်မှုဘက်သို့ ရွေ့ပြောင်းစေသည်။ Executor များသည် AI agent သို့ ထုံးစံ logic ဖြစ်နိုင်သည်။

**Edges**

Edges များမှာ workflow ထဲ message များ လည်ပတ်မှုဖြင့် ဖော်ပြသည်။ ၎င်းတို့အမျိုးအစားများမှာ-

*Direct Edges* - Executor တစ်ခုမှ တစ်ခုသို့ လွယ်ကူပြတ်သားစွာ ချိတ်ဆက်ခြင်း-

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```
  
*Conditional Edges* - သတ်မှတ်ထားသော ကိုယ်ထင်သွားသော အခြေအနေ ပြည့်မှ လုပ်ဆောင်ခြင်း။ ဥပမာ- ဟိုတယ် အခန်း မရရှိနိုင်ပါက Executor တစ်ခုက တခြားရွေးချယ်စရာများကို အကြံပြုသည်။

*Switch-case Edges* - သတ်မှတ်ထားသော အခြေအနေများအပေါ် မက်ဆေ့ခ်ျများ ကို Executor မတူညီသို့ ခွဲခြားပေးသည်။ ဥပမာ- ခရီးသွားဝယ်သူ တစ်ယောက်တွင် ဦးစားပေး ဝင်ခွင့် ရှိပါက သူ၏ တာဝန်များကို တခြား workflow မှတဆင့် ဖြေရှင်းသည်။

*Fan-out Edges* - မက်ဆေ့ခ်ျတစ်ခုကို ရည်မှန်းထားသည့် ပစ်မှတ်အများသို့ ပေးပို့ခြင်း။

*Fan-in Edges* - Executor များ အများပေါင်းစုပြီး မက်ဆေ့ခ်ျတစ်ခုသို့ ပေးပို့ခြင်း။

**Events**

Workflow များ၏ အသေးစိတ် ကြည့်ရှုနိုင်ရေးအတွက် MAF သည် အောက်ပါ event များ ပါဝင်သည်-

- `WorkflowStartedEvent` - Workflow စတင်ခြင်း
- `WorkflowOutputEvent` - Workflow မှ ထွက်ရှိသော output
- `WorkflowErrorEvent` - Workflow မှာ အမှားဖြစ်ခြင်း
- `ExecutorInvokeEvent` - Executor ကို အလုပ် စတင်လိုက်ခြင်း
- `ExecutorCompleteEvent` - Executor အလုပ် ပြီးဆုံးခြင်း
- `RequestInfoEvent` - တောင်းဆိုမှု တစ်ခု ပြုလုပ်ခြင်း

## ကြီးမားသော MAF ပုံစံများ

အထက်ပါအကြောင်းအရာများသည် Microsoft Agent Framework ၏ အဓိက အယူအဆများဖြစ်ပြီး၊ ပိုမိုရှုပ်ထွေးသော Agent များ တည်ဆောက်ရာတွင် အောက်ပါ ကြီးမားသော ပုံစံများကို စဉ်းစားပါ-

- **Middleware ပေါင်းစပ်ခြင်း**: များစွာသော middleware handler များ (logging, authentication, rate-limiting) ကို function နှင့် chat middleware များဖြင့် ဆက်သွယ်ပြီး Agent ၏ လုပ်ဆောင်မှု ပေါ် စုံလင်စွာ ထိန်းချုပ်နိုင်ခြင်း။
- **Workflow Checkpointing**: Workflow events နှင့် serialization ကို အသုံးပြုပြီး ကြာရှည်များသော Agent လုပ်ငန်းစဉ်များ သိမ်းဆည်းနှင့် ပြန်လည် စတင်နိုင်ခြင်း။
- **Dynamic Tool ရွေးချယ်ခြင်း**: RAG ကိရိယာဖေါ်ပြချက်များအပေါ် စုစည်းခြင်းနှင့် MAF ၏ tool မှတ်ပုံတင်မှုကို ပေါင်းစပ်ပြီး မေးခွန်းတစ်ခုတွင် သက်ဆိုင်ရာ Tools များသာ ပြသခြင်း။
- **Multi-Agent Handoff**: Workflow edges နှင့် condition-based routing ကို အသုံးပြု၍ အထူးပြု Agent များအကြား handoff စီမံခန့်ခွဲမှု။

## ကွပ်ကိုဒ် နမူနာများ

Microsoft Agent Framework အတွက် ကွပ်ကိုဒ်နမူနာများကို `xx-python-agent-framework` နှင့် `xx-dotnet-agent-framework` ဖိုင်များတွင် ဒီ repository ထဲတွင် ရှာဖွေတွေ့နိုင်သည်။

## Microsoft Agent Framework အကြောင်း ပိုမိုမေးမြန်းလိုပါသလား?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) တွင် အခြားသင်ယူသူများနှင့် တွေ့ဆုံ၊ office hours တက်ရောက်၊ သင့် AI Agent မေးခွန်းများ ဖြေဆိုရန် အဖွဲ့ဝင်ဖြစ်ပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အတည်မပြုချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြုပြီး ဘာသာပြန်ထားခြင်း ဖြစ်ပါသည်။ တိကျမှန်ကန်မှုအတွက် ကြိုးစားဖြစ်သော်လည်း၊ စက်ရုပ်ဘာသာပြန်ခြင်းက အမှား သို့မဟုတ် တိကျမှုမရှိမှုများ ဖြစ်နိုင်သည်ကို သတိပြုပါရန် အကြံပြုပါသည်။ မူရင်းစာရွက်စာတမ်းကို မူလဘာသာဖြင့် ထောက်ခံအတည်ပြုရမည်ဖြစ်ပြီး အရေးကြီးသော သတင်းအချက်အလက်များအတွက် လူ့ဘာသာပြန်အမှုထမ်း၏ ကျွမ်းကျင်သော ဘာသာပြန်ချက်ကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်လာနိုင်သည့် မတိကျမှုများ သို့မဟုတ် အနားလွှတ်မှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->