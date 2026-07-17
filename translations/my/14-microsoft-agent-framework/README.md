# Microsoft Agent Framework ကို စူးစမ်းလေ့လာခြင်း

![Agent Framework](../../../translated_images/my/lesson-14-thumbnail.90df0065b9d234ee.webp)

### နိဒါန်း

ဒီသင်ခန်းစာမှာ ပါဝင်မည့် အကြောင်းအရာများမှာ -

- Microsoft Agent Framework ကို နားလည်ခြင်း: အဓိက လက္ခဏာများနှင့် တန်ဖိုးများ  
- Microsoft Agent Framework ၏ အဓိက အယူအဆများကို စူးစမ်းလေ့လာခြင်း
- MAF ၏ အဆင့်မြင့် ပုံစံများ: အလုပ်စဉ်များ၊ Middleware နှင့် မှတ်ဉာဏ်

## သင်ယူရန် ရည်ရွယ်ချက်များ

ဒီသင်ခန်းစာပြီးဆုံးသည့်အခါ သင်သည် -

- Microsoft Agent Framework အသုံးပြု၍ ထုတ်လုပ်မှုအဆင်သင့် AI ကိုယ်စားလှယ်များ ဖန်တီးနည်းကို သိရှိရမည်
- Microsoft Agent Framework ၏ အဓိက လက္ခဏာများကို ကိုယ်စားလှယ်အသုံးပြုမှု လိုအပ်ချက်များတွင် လျှောက်လွှက်နည်းကို သင်ယူနိင်မည်
- အလုပ်စဉ်များ၊ middleware နှင့် နိဒါန်းဆိုင်ရာ များအပါအဝင် အဆင့်မြင့်ပုံစံများကို အသုံးပြုနိင်မည်

## ကုဒ်နမူနာများ

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) အတွက် ကုဒ်နမူနာများကို ဒီ repository ထဲရှိ `xx-python-agent-framework` နှင့် `xx-dotnet-agent-framework` ဖိုင်များတွင် ရှာဖွေနိင်ပါသည်။

## Microsoft Agent Framework ကို နားလည်ခြင်း

![Framework Intro](../../../translated_images/my/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) သည် AI ကိုယ်စားလှယ်များ ဖန်တီးရန် Microsoft ၏ ပေါင်းစပ်ထားသော framework ဖြစ်သည်။ ၎င်းသည် ထုတ်လုပ်မှုနှင့် သုတေသန ပတ်ဝန်းကျင်များတွင် တွေ့ရှိရသော တစ်မျိုးမျိုး agentic အသုံးပြုမှုများကို ဖြေရှင်းနိုင်ရန် လွယ်ကူမှုကို ပေးသည်၊ ၎င်းတို့တွင် -

- **လုပ်ငန်းစဉ် အဆင့်လိုက် စီမံခန့်ခွဲခြင်း** သင့်လျော်သော အခြေအနေများတွင် အဆင့်လိုက် အလုပ်စဉ်များ လိုအပ်သောအခါ။
- **အချိန်တပြိုင်နက် စီမံခန့်ခွဲခြင်း** ပိုင်းမှာ ကိုယ်စားလှယ်များ တစ်ပြိုင်နက်တည်း တာဝန်များ ပြီးဆုံးနိုင်ရန် လိုအပ်သော အခြေအနေများ။
- **အုပ်စုစကားပြော စီမံခန့်ခွဲခြင်း** ကိုယ်စားလှယ်များ တူတူ ပူးပေါင်းလုပ်နိုင်သော တာဝန်များတွင်။
- **တာဝန်လွှဲပြောင်း စီမံခန့်ခွဲခြင်း** ကိုယ်စားလှယ်များ သေးငယ်သော တာဝန်များ ပြီးစီးသည့်အခါ တစ်ယောက်နေနောက် တစ်ယောက် ဟန်လျှော့ခံရသည့် အခြေအနေများ။
- **မျက်နှာဆွဲ စီမံခန့်ခွဲခြင်း** တာဝန် စာရင်းတစ်ခုကို မန်နေဂျာ ကိုယ်စားလှယ် တည်ဆောက်ပြီး ပြင်ဆင်ခြင်းနှင့် သေးငယ်သော ကိုယ်စားလှယ်များ စီမံခန့်ခွဲခြင်း။

ထုတ်လုပ်မှုအတွက် AI ကိုယ်စားလှယ်များ ပို့ဆောင်ရာတွင် MAF သည် အောက်ပါ လက္ခဏာများကိုလည်း ပါဝင်ပေးထားသည် -

- **ကြည့်ရှုနိုင်မှု** - OpenTelemetry ကို အသုံးပြု၍ AI ကိုယ်စားလှယ်၏ မှုခင်းတိုင်းတွင် ပါဝင်သော ကိရိယာခေါ်ဆိုမှု၊ စီမံခန့်ခွဲမှု အဆင့်များ၊ ဆင်တူရည်မှန်းချက်များနှင့် Microsoft Foundry dashboard များမှ စွမ်းဆောင်ရည် စစ်ဆေးမှု။
- **လုံခြုံရေး** - Microsoft Foundry ပလက်ဖောင်းပေါ်တွင် ကိုယ်စားလှယ်များ ကို အလိုအလျောက် စောင့်ရှောက်ခြင်း၊ အခန်းကဏ္ဍအခြေခံ အချက်အလက် ဝင်ရောက်ခွင့်၊ ပုဂ္ဂလိကဒေတာ ထိန်းသိမ်းမှု နှင့် built-in အကြောင်းအရာ လုံခြုံမှုပိုင်းများ ပါဝင်ပါသည်။
- **တည်ရှိမှုခံနိုင်မှု** - ကိုယ်စားလှယ် တစ်ခု၏ စွဲစွဲမြဲမြဲ အလုပ်ခွင်များနှင့် အလုပ်စဉ်များကို ရပ်တန့်ရန်၊ ထပ်မံ စတင်ရန်နှင့် အမှားမှ ပြန်လည်လွှတ်ရန် အလုပ်အချိန်ရှည် ပိုင်းဆိုင်ရာဖြစ်စဉ်များအတွက်။
- **ထိန်းချုပ်မှု** - လူ့အထောက်အကူအဖြစ် ဦးဆောင်အလုပ်စဉ်များကို ထောက်ပံ့ပေးပြီး တာဝန်များကို လူတစ်ယောက်၏ အတည်ပြုချက်လိုအပ်သည်ဟု သတ်မှတ်နိုင်ပါသည်။

Microsoft Agent Framework သည် ဆက္သွယ္ ပေါင်းစပ် အသုံးပြုနိုင်မှုကိုလည်း အရေးပါသဖြင့် -

- **Cloud ဂိုဏ်း မရွေးခြင်း** - ကိုယ်စားလှယ်များကို ကြိုးသီး၊ On-premises နှင့် မတူညီသော cloud များတွင် စီမံဆောင်ရွက်နိုင်သည်။
- **ပံ့ပိုးသူ မရွေးခြင်း** - ကိုယ်စားလှယ်များကို သင်နှစ်သက်သည့် SDK များဖြင့် ဖန်တီးနိုင်ပြီး Azure OpenAI နှင့် OpenAI များပါဝင်သည်။
- **ဖွဲ့စည်းထားသော ဖွဲ့စည်းမှုများ ပေါင်းစည်းခြင်း** - ကယ့်ကူးအတိုင်း Agent-to-Agent (A2A) နှင့် Model Context Protocol (MCP) တို့ ကဲ့သို့ ပြောဆိုင်မှုများဖြင့် အခြားကိုယ်စားလှယ်များနှင့် ကိရိယာများကို ရှာဖွေ အသုံးပြုနိုင်သည်။
- **Plugins နှင့် Connectors** - Microsoft Fabric, SharePoint, Pinecone နှင့် Qdrant စသော ဒေတာနှင့် မှတ်ဥာဏ်ဝန်ဆောင်မှုများနှင့် ချိတ်ဆက်နိုင်သည်။

ယခု ကိုယ်စားလှယ် Framework ၏ အဓိက အယူအဆတချို့တွင် ဒီ လက္ခဏာများ ဘယ်လို အကောင်အထည်ဖော်သလဲ ဆိုတာကို ကြည့်ကြမယ်။

## Microsoft Agent Framework ၏ အဓိက အယူအဆများ

### ကိုယ်စားလှယ်များ

![Agent Framework](../../../translated_images/my/agent-components.410a06daf87b4fef.webp)

**ကိုယ်စားလှယ် ဖန်တီးခြင်း**

ကိုယ်စားလှယ် ဖန်တီးခြင်းမှာ inference service (LLM Provider) ကို သတ်မှတ်ခြင်း၊ ကိုယ်စားလှယ်လိုက်နာရမည့် စည်းကမ်းချက်များပါသော စာရင်းနှင့် `name` တပ်ထားခြင်းဖြင့် ပြုလုပ်သည်။


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```






```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ဒါမှမဟုတ် [MiniMax](https://platform.minimaxi.com/) ကို အသုံးပြုနိုင်ပြီး OpenAI သဘောတူညီချက်တူ API နှင့် ကြီးမားသော context ပိုင်း (204K tokens ထိ) ပါဝင်သည်။

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ဒါမှမဟုတ် A2A protocol များသုံး၍ ရေမဲ့ ကိုယ်စားလှယ်များဖြင့် ပြုလုပ်နိုင်သည်။

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ကိုယ်စားလှယ်များ ကို ခေတ္တစောင့်ကြည့် သုံးစွဲခြင်း**

ကိုယ်စားလှယ်များကို `.run` သို့မဟုတ် `.run_stream` နည်းလမ်းများသုံး၍ မရှိမဖြစ်ထုတ်လွှင့်ခြင်း သို့မဟုတ် ထွက်လွှင့်ခြင်း အတွက် စနစ်တကျပေးသည်။

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ကိုယ်စားလှယ် တစ်ယောက်စီ၏  parameter များကို စိတ်ကြိုက်ပြင်ဆင်နိုင်ရန် အထူးရွေးချယ်စရာများ ရှိသည်၊ ဥပမာ- `max_tokens` (ကိုယ်စားလှယ်သုံးသည့် စကားဝိုင်းအရေအတွက်၊ `tools` ကိုယ်စားလှယ်သည် ခေါ်ဆိုနိုင်သည့် ကိရိယာများ ‌နှင့် `model` ကိုယ်စားလှယ်သုံးသော မော်ဒယ်ကိုလည်း ဖော်ပြနိုင်သည်။

သုံးစွဲသူ၏ တာဝန် ပြီးမြောက်ရေးအတွက် သီးခြား မော်ဒယ်များ သို့မဟုတ် ကိရိယာများလိုအပ်သော အခြေအနေများတွင် အထူးအသုံးဝင်သည်။

**ကိရိယာများ (Tools)**

ကိရိယာများကို ကိုယ်စားလှယ် ဖော်ပြသည့်အခါ နှင့် ကိုယ်စားလှယ် ပြေးဆွဲသည့်အခါ နှစ်မျိုးစလုံးတွင် သတ်မှတ်နိုင်သည်။

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ChatAgent ကို တိုက်ရိုက် ဖန်တီးတဲ့အခါ

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```




**ကိုယ်စားလှယ် အတိုက်အခံများ (Agent Threads)**

ကိုယ်စားလှယ် အတိုက်အခံများသည်  multi-turn စကားပြောဆိုမှုများကို စီမံရန် အသုံးပြုသည်။ အတိုက်အခံများကို ဖန်တီးနိုင်သည့် နည်းလမ်းများမှာ -

- `get_new_thread()` ကို အသုံးပြုပြီး အချိန်အကြာကြီး မဖြုတ်ဘဲ သိမ်းဆည်းထားနိုင်သည်။
- ကိုယ်စားလှယ် တစ်ယောက်ကို သိမ်းဆည်းမှု မရှိဘဲ တစ်ခါအသုံးပြုချိန်တွင် အတိုက်အခံကို အလိုအလျောက် ဖန်တီးပေးသည်။

အတိုက်အခံ ဖန်တီးရန် အောက်ပါကုဒ်ကို အသုံးပြုသည်။

```python
# စသားသစ်တစ်ခု ဖန်တီးပါ။
thread = agent.get_new_thread() # စသားနှင့်အတူ အေးဂျင့်ကို အလုပ်လုပ်ပါ။
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

လိုအပ်ပါက အတိုက်အခံကို အလားတူ အသုံးပြုနိုင်ရန် သိမ်းဆည်းပါ။

```python
# နယူး thread တစ်ခု ဖန်တီးပါ။
thread = agent.get_new_thread() 

# thread နဲ့ agent ကို ပြေးပါ။

response = await agent.run("Hello, how are you?", thread=thread) 

# သိုလှောင်ရန် thread ကို စီးရီးလိုက်လုပ်ပါ။

serialized_thread = await thread.serialize() 

# သိုလှောင်မှုမှ လုပ်ဖော်ကိုင်ဖက်ကို ပြန်ဖတ်ပြီး thread အခြေအနေကို ပြန်လည်ဖော်ပြပါ။

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ကိုယ်စားလှယ် Middleware**

ကိုယ်စားလှယ်များသည် ကိရိယာများနှင့် LLM များနှင့် ပူးပေါင်းပြီး သုံးစွဲသူ၏ တာဝန်များ ပြီးမြောက်စေရန် ဖြေရှင်းသည့် အခါ Middleware သည် ၎င်းတို့အကြား ဖြစ်သည့် လုပ်ဆောင်မှုများကို ဆောင်ရွက်ရန် သို့မဟုတ် တင်ပြရန် အထောက်အကူဖြစ်သည်။

*Function Middleware*

ဒီ Middleware သည် ကိုယ်စားလှယ်နှင့် function/tool တစ်ခုအကြား လုပ်ဆောင်မှုများတစ်ခုကို အကောင်အထည်ဖော်ရန် ခွင့်ပြုသည်။ ဥပမာအနေဖြင့် function ခေါ်ဆိုမှုတွင် logging တစ်ခုလုပ်လိုသည်ဆိုပါက။

အောက်ပါကုဒ်တွင် `next` ဆိုသည်မှာ နောက်ထပ် middleware သို့မဟုတ် အမှန်တကယ် function ကို ခေါ်ဆိုမှု စနစ်ဖြစ်သည်။

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ကြိုတင်-လုပ်ငန်းစဉ်: ဖင့်ရှင်းလုပ်ဆောင်မှုမတိုင်မီ မှတ်တမ်းပေါင်းထည့်ခြင်း
    print(f"[Function] Calling {context.function.name}")

    # နောက်ထပ် middleware သို့မဟုတ် ဖင့်ရှင်းလုပ်ဆောင်ခြင်း ဆက်လုပ်ရန်
    await next(context)

    # နောက်-လုပ်ငန်းစဉ်: ဖင့်ရှင်းလုပ်ဆောင်ပြီးနောက် မှတ်တမ်းပေါင်းထည့်ခြင်း
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

ဒီ Middleware သည် ကိုယ်စားလှယ်နှင့် LLM အကြား တင်ပို့မှုများအကြား လုပ်ဆောင်မှုများ သို့မဟုတ် logging လုပ်ခြင်း စသည်များလုပ်ရန် အဆင်ပြေစေသည်။

AI ဝန်ဆောင်မှုသို့ ပို့သော `messages` ကဲ့သို့ အရေးပါတဲ့ အချက်အလက်များ ပါဝင်သည်။

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ကြိုတင်ပြင်ဆင်ခြင်း - AI ခေါ်ဆိုမှုမတိုင်မီ မှတ်တမ်းတင်ခြင်း
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # နောက်ထပ် middleware သို့မဟုတ် AI ဝန်ဆောင်မှုဆီ ဆက်လက်သွားရန်
    await next(context)

    # ပြီးစီးပြီးနောက် - AI တုံ့ပြန်ချက်မှတ်တမ်းတင်ခြင်း
    print("[Chat] AI response received")

```

**ကိုယ်စားလှယ် မှတ်ဉာဏ်**

`Agentic Memory` သင်ခန်းစာတွင် ဖော်ပြထားသကဲ့သို့ မှတ်ဉာဏ်သည် ကိုယ်စားလှယ်ကို မတူညီသော  context များမှာ လည်ပတ်နိုင်ရန် အရေးပါသော အစိတ်အပိုင်းဖြစ်သည်။ MAF တွင် မှတ်ဉာဏ်အမျိုးအစား အမျိုးမျိုး ပါဝင်သည်။

*In-Memory Storage*

ဒီ memory သည် application ရွှေ့ပြောင်းချိန်အတွင်း အတိုက်အခံ thread များထဲ ထိန်းသိမ်းထားသည်။

```python
# ဂျင်းထားသော သရက်အသစ်တစ်ခု ဖန်တီးပါ။
thread = agent.get_new_thread() # အဲဂျင့်ကို သရက်နှင့်အတူ လည်ပတ်ပါ။
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

ဒီ memory သည် အစည်းအဝေး အတင်းအကျပ်များအပြီး မျိုးစုံသော အစည်းအဝေး တိုင်ကြားမှုမှတ်တမ်း ထိန်းသိမ်းရန် အသုံးပြုသည်။ `chat_message_store_factory` ဖြင့် သတ်မှတ်သည်။

```python
from agent_framework import ChatMessageStore

# စိတ်ကြိုက်စာတိုများသိုလှောင်ရန်ဆိုင်သစ်တစ်ခုဖန်တီးပါ
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamic Memory*

ကိုယ်စားလှယ်များ ကို ပြေးဆွဲခေါ်ဆိုပြီး ကောင်တောက်ပေးမည့် context မတိုင်မီ ထည့်သွင်းရမည့် မှတ်ဉာဏ်ဖြစ်သည်။ mem0 ကဲ့သို့ ပြင်ပ အရင်းအမြစ်များတွင် သိမ်းဆည်းနိုင်သည်။

```python
from agent_framework.mem0 import Mem0Provider

# တိုးတက်သောမှတ်ဥာဏ်စွမ်းရည်များအတွက် Mem0 ကို အသုံးပြုခြင်း
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

**ကိုယ်စားလှယ် ကြည့်ရှုနိုင်မှု (Observability)**

ကြည့်ရှုနိုင်မှုသည် ယုံကြည်စိတ်ချရသော သမားရိုးကျ နိယာမဆိုင်ရာ ကိုယ်စားလှယ်စနစ်များ တည်ဆောက်ရန် အရေးပါသည်။ MAF သည် tracing နှင့် meters များ ပံ့ပိုးရန် OpenTelemetry နှင့် ပေါင်းစပ်ထားသည်။

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # အလုပ်တစ်ခုခုလုပ်ပါ
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### အလုပ်စဉ်များ (Workflows)

MAF သည် တာဝန်ပြီးဆုံးရန် ကြိုတင် သတ်မှတ်ထားသော အဆင့်များဖြင့် အလုပ်စဉ်များ ပေးသည်၊ ထိုအဆင့်များတွင် AI ကိုယ်စားလှယ်များ ပါဝင်သည်။

အလုပ်စဉ်များမှာ ပိုမိုထိန်းချုပ်နိုင်မှု ရရှိစေသော နေရာများအား အသွင်အပြင်အားဖြင့်ဖွဲ့စည်းထားပြီး မျိုးစုံ ကိုယ်စားလှယ် ဗို့လ်နှင့် checkpointing ကို အထောက်အကူပြုသည်။

အလုပ်စဉ်၏ အဓိက အစိတ်အပိုင်းများမှာ -

**အကောင်အထည်ဖော်သူများ (Executors)**

အကောင်အထည်ဖော်သူများသည် input messages ခံယူပြီး သတ်မှတ်ထားသော တာဝန်များ ဆောင်ရွက်ပြီး output message ထုတ်ပေးသည်။ ၎င်းက အလုပ်စဉ်ကို ကြီးမားသော တာဝန် ပြီးဆုံးမှုဆီသို့ ရွေ့လျားစေသည်။ အကောင်အထည်ဖော်သူများသည် AI ကိုယ်စားလှယ် သို့မဟုတ် custom logic ဖြစ်သနိုင်သည်။

**အနားများ (Edges)**

အနားများကို အလုပ်စဉ်၌ မက်ဆေ့ခ်ျများ ၏ လှိုင်းသွားလှိုင်းလာ ပုံကို သတ်မှတ်ရာ၌ သုံးသည်။ ၎င်းများမှာ -

*တိုက်ရိုက် အနား (Direct Edges)* - အကောင်အထည်ဖော်သူ တစ်ဦးမှ တစ်ဦး သို့ ရိုးရှင်းသော ချိတ်ဆက်မှုများ။

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*အခြေအနေ အနား (Conditional Edges)* - အစည်းအဝေးတစ်ခု ပြည့်ရန် တင်ပြမှု များသောအခါ အသက်သာသည့် အခြေအနေများ။ ဥပမာ တည်းခိုစခန်းများ မရရှိနိုင်ပါက အကောင်အထည်ဖော်သူသည် အခြားရွေးချယ်စရာများကို အဆိုပြုနိုင်သည်။

*Switch-case Edges* - သတ်မှတ်ထားသော အခြေအနေများပေါ် မူတည်၍ မက်ဆေ့ခ်ျများကို အကောင်အထည်ဖော်သူ များစွာသို့ လမ်းညွှန်ပေးသည်။ ဥပမာ ခရီးသွား ဖောက်သည်မှာ ဦးစားပေး ဝင်ခွင့်ရှိပါက ၎င်းအတွက် အခြား အလုပ်စဉ်ဖြင့် ကြပ်မတ်သည်။

*Fan-out Edges* - မက်ဆေ့ခ်ျ တစ်ခုကို သီးသန့်ရည်ရွယ်ထားသော အရေအတွက် များသို့ ပို့သည်။

*Fan-in Edges* - မက်ဆေ့ခ်ျ များစွာကို အကောင်အထည်ဖော်သူ အမျိုးမျိုးမှ စုဆောင်းပြီး တစ်ခုသို့ ပို့ဆောင်သည်။

**ဖြစ်ရပ်များ (Events)**

အလုပ်စဉ်များကို ပိုမို ကြည့်ရှုနိုင်စေရန် MAF သည် အလုပ်စဉ် ရေးဆွဲခြင်းနှင့် တွဲဖက် တည်ဆောက်ထားသော ဖြစ်ရပ်များ ကို ပံ့ပိုးပေးသည် ကျွန်တော်တို့၏ -

- `WorkflowStartedEvent`  - အလုပ်စဉ် တည်ဆောက်ခြင်း စတင်ခြင်း
- `WorkflowOutputEvent` - အလုပ်စဉ်တွင် ထုတ်လွှတ်မှု ဖြစ်ပေါ်ခြင်း
- `WorkflowErrorEvent` - အလုပ်စဉ်တွင် အမှား ဖြစ်ပေါ်ခြင်း
- `ExecutorInvokeEvent`  - အကောင်အထည်ဖော်သူ စတင် လုပ်ဆောင်မှု
- `ExecutorCompleteEvent`  - အကောင်အထည်ဖော်သူ လုပ်ငန်းပြီးဆုံးမှု
- `RequestInfoEvent` - တောင်းဆိုမှု ထုတ်ပြန်ခြင်း

## အဆင့်မြင့် MAF ပုံစံများ

အထက်တွင် ဖော်ပြထားသောအစိတ်အပိုင်းများသည် Microsoft Agent Framework ၏ အဓိက အယူအဆများ ဖြစ်သည်။ ကိုယ်စားလှယ်များ များပြားပြီး ဆင်တူစီမံခန့်ခွဲသည့်အခါ အောက်ဖော်ပြပါ အဆင့်မြင့် ပုံစံများကို ထည့်သွင်းစဉ်းစားကြည့်ပါ -

- **Middleware တည်ဆောက်မွေ့ခြင်း**: function နှင့် chat middleware ကို အသုံးပြု၍ လမ်းကြောင်းချ (logging, auth, rate-limiting) လုပ်ခြင်းဖြင့် ကိုယ်စားလှယ်၏ အပြုအမှုများကို ပိုမို ထိန်းချုပ်နိုင်သည်။
- **အလုပ်စဉ် Checkpointing**: အလုပ်စဉ်ဖြစ်ရပ်များနှင့် serialization တွင် တည်ဆောက်ပြီး ရှည်လျားစွာ အလုပ်လုပ်နေသည့် ကိုယ်စားလှယ်များကို စောင့်ဆောင်နိုင်သည်။
- **Dynamic Tool ရွေးချယ်မှု**: MAF ၏ tool registration နှင့် RAG ကို ပေါင်းစပ်၍ မေးခွန်းတစ်ခုချင်းစီအတွက် သက်ဆိုင်သော ကိရိယာများကိုသာ ထုတ်ပြရန်။
- **Multi-Agent Handoff**: အလုပ်စဉ် edges နှင့် conditional routing များကို အသုံးပြု၍ မှီခိုကူညီရေး အထူးပြုပြင်ထားသော ကိုယ်စားလှယ်များ အကြား တာဝန်လွှဲပေးခြင်း။

## Microsoft Foundry တွင် LangChain / LangGraph ကိုယ်စားလှယ်များ ကို ဧည့်ခံခြင်း

Microsoft Agent Framework သည် **framework မဟာမိတ် ယှဉ်ပါမည့်** ဖြစ်ပြီး သင်သည် MAF ဖြင့် ရေးသားထားသည့် ကိုယ်စားလှယ်များ ပမာဏသာ သတ်မှတ်ရန် မဟုတ်ပါ။ သင်တွင် **LangChain** သို့မဟုတ် **LangGraph** ဖြင့် ဆောက်ထားပြီးသား ကိုယ်စားလှယ်ရှိပါက၊ ၎င်းကို **Microsoft Foundry hosted agent** အဖြစ် ပြေးဆွဲနိုင်ပြီး Foundry သည် runtime, session, scaling, identity နှင့် protocol endpoints များကို စီမံခန့်ခွဲပေး မည်ဖြစ်ပြီး သင်၏ ကိုယ်စားလှယ် ဉာဏ်ရည်များ LangGraph မှာသာ နေမည် ဖြစ်သည်။

၎င်းကို `langchain_azure_ai.agents.hosting` package ဖြင့် ပြုလုပ်နိုင်ပြီး မတူညီသော protocols ကို ဖော်ထုတ်ထားသည်။

**1. Hosting extra ကို ထည့်သွင်းပါ:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` extra သည် Foundry protocol libraries များ ဖြစ်သည့် `azure-ai-agentserver-responses` (OpenAI-compatible `/responses` endpoint) နှင့် `azure-ai-agentserver-invocations` (generic `/invocations` endpoint) ကို ထည့်သွင်းပေးသည်။

**2. Hosting protocol ကို ရွေးပါ:**

| Protocol | Host class | Endpoint | အသုံးပြုရန်အချိန် |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | OpenAI-compatible chat, streaming, response history, နှင့် conversation threading လိုအပ်သောအခါ - စကားပြောဆိုမှုကို  အဓိကအောက်မေ့ထားသည်။|
| **Invocations** | `InvocationsHostServer` | `/invocations` | custom JSON ပုံစံ၊ webhook-style endpoint သို့မဟုတ် conversation မဖြစ်သော အလုပ်များအတွက်။|

**Responses API သည် Foundry တွင် ကိုယ်စားလှယ်စနစ် တည်ဆောက်ရာမှာ အဓိက API ဖြစ်သည်။** ထိုကြောင့် များသော ကိုယ်စားလှယ်များအတွက် `ResponsesHostServer` ဖြင့် စတင်ပါ။

**3. ပတ်ဝန်းကျင် environment variables ကို ပြင်ဆင်ပါ** (`az login` ပြုပြီး `DefaultAzureCredential` အသုံးပြုနိုင်ရန်):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

ကိုယ်စားလှယ်သည် နောက်ပိုင်း Foundry တွင် hosted agent အဖြစ် ပြေးသောအခါ platform သည် `FOUNDRY_PROJECT_ENDPOINT` ကို အလိုအလျောက် ထည့်သွင်းပေးသည်။

**4. LangGraph ကို Responses protocol ဖြင့် သတင်းစကားထုတ်ပါ:**

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-4.1")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI မှာ Foundry စီမံကိန်း၏ OpenAI နဲ့ကိုက်ညီတဲ့ (Responses) endpoint ကို ရည်ရွယ်ပါတယ်။
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

အိမ်ရှေ့မှာ `python main.py` ဖြင့် run ပြီးနောက် `http://localhost:8088/responses` သို့ Responses တောင်းဆိုမှု ပို့ပါ။

**အဓိကအပြုအမူများ:**

- **စကားပြောဆိုမှုများ**: Clients များသည် `previous_response_id` သို့မဟုတ် `conversation` ID ပို့သောအားဖြင့် ဆက်လက်ဆက်သွယ်နိုင်သည်။ သင်၏ graph ကို LangGraph checkpointer ရှိပါက Foundry သည် conversation state ကို checkpoint လုပ်သည် (ထုတ်လုပ်မှုတွင် durable checkpointer အသုံးပြုပါ; စမ်းသပ်မှုအတွက် `MemorySaver` ကောင်းသည်)။
- **လူ့အင်္ဂါရပ် (human-in-the-loop)**: သင်၏ graph မှ LangGraph `interrupt()` ကို အသုံးပြုပါက၊ `ResponsesHostServer` သည် pending interrupt ကို Responses `function_call` / `mcp_approval_request` အနေနှင့် မြင်သာစေပြီး clients များသည် `function_call_output` / `mcp_approval_response` အား ဖြင့် ဆက်လက်လုပ်ဆောင်နိုင်သည်။
- **Foundry သို့ တင်သွင်းမှု**: Azure Developer CLI ကို အသုံးပြုပြီး — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (local, Docker လိုအပ်သည်)၊ `azd provision` နှင့် `azd deploy` ကိုအသုံးပြုပါ။ Hosted-agent တင်သွင်းမှုအတွက် **Foundry Project Manager** အခွင့်အရေးလိုအပ်သည်။

ဒီနမူနာ၏ runnable ဗားရှင်းကို [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) တွင် တွေ့နိုင်သည်။ အပြည့်အစုံ လမ်းညွှန်ချက်များ (Invocations protocol, custom request schemas နှင့် troubleshooting) ကို [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) တွင် ကြည့်ပါ။

## ကုဒ်နမူနာများ 

Microsoft Agent Framework အတွက် ကုဒ်နမူနာများကို ဒီ repository တွင် `xx-python-agent-framework` နှင့် `xx-dotnet-agent-framework` ဖိုင်များဖြင့် ရှာဖွေနိုင်ပါသည်။

## Microsoft Agent Framework အကြောင်း ပိုမိုမေးမြန်းလိုပါသလား?

အခြားသင်ယူသူများနှင့် တွေ့ဆုံရန်၊ office hours တက်ရောက်ရန်နှင့် AI ကိုယ်စားလှယ်ဆိုင်ရာ မေးခွန်းများဖြေ မည့် [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) မှာ ပူးပေါင်းပါ။
## ယခင်သင်ခန်းစာ

[AI ကိုယ်စားလှယ်များအတွက် မှတ်ဉာဏ်](../13-agent-memory/README.md)

## နောက်ထပ်သင်ခန်းစာ

[ကွန်ပျူတာအသုံးပြု လူပြု ကိုယ်စားလှယ်များ ဖန်တီးခြင်း (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->