# مائیکروسافٹ ایجنٹ فریم ورک کی تلاش

![Agent Framework](../../../translated_images/ur/lesson-14-thumbnail.90df0065b9d234ee.webp)

### تعارف

اس سبق میں کور کیا جائے گا:

- مائیکروسافٹ ایجنٹ فریم ورک کو سمجھنا: کلیدی خصوصیات اور قیمت  
- مائیکروسافٹ ایجنٹ فریم ورک کے کلیدی تصورات کی تلاش
- جدید MAF پیٹرنز: ورک فلو، مڈل ویئر، اور میموری

## سیکھنے کے مقاصد

اس سبق کو مکمل کرنے کے بعد، آپ جان سکیں گے کہ:

- مائیکروسافٹ ایجنٹ فریم ورک کا استعمال کرتے ہوئے پروڈکشن کے قابل AI ایجنٹس بنائیں
- مائیکروسافٹ ایجنٹ فریم ورک کی بنیادی خصوصیات کو اپنے ایجنٹک استعمال کے کیسز میں لاگو کریں
- ورک فلو، مڈل ویئر، اور مشاہدے سمیت جدید پیٹرنز کا استعمال کریں

## کوڈ کے نمونے 

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) کے لئے کوڈ کے نمونے اس رپوزیٹری میں `xx-python-agent-framework` اور `xx-dotnet-agent-framework` فائلوں کے تحت مل سکتے ہیں۔

## مائیکروسافٹ ایجنٹ فریم ورک کو سمجھنا

![Framework Intro](../../../translated_images/ur/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) مائیکروسافٹ کا متحدہ فریم ورک ہے AI ایجنٹس بنانے کے لیے۔ یہ پروڈکشن اور تحقیقاتی ماحول میں مختلف قسم کے ایجنٹک استعمال کے کیسز کو حل کرنے کی لچک فراہم کرتا ہے جن میں شامل ہیں:

- **تسلسل وار ایجنٹ آرکیسٹریشن** ان escenarios میں جہاں قدم بہ قدم ورک فلو کی ضرورت ہوتی ہے۔
- **ہم وقت ساز آرکیسٹریشن** ان escenarios میں جہاں ایجنٹس کو ایک ساتھ کام مکمل کرنا ہوتا ہے۔
- **گروپ چیٹ آرکیسٹریشن** ان escenarios میں جہاں ایجنٹس ایک ساتھ مل کر ایک کام پر کام کر سکتے ہیں۔
- **ہینڈ آف آرکیسٹریشن** ان escenarios میں جہاں ایجنٹس کام کے ذیلی کام مکمل ہونے پر کام ایک دوسرے کو سونپ دیتے ہیں۔
- **مقناطیسی آرکیسٹریشن** ان escenarios میں جہاں ایک مینیجر ایجنٹ کام کی فہرست بناتا اور ترمیم کرتا ہے اور ذیلی ایجنٹس کے ہم آہنگی کو سنبھالتا ہے تاکہ کام مکمل ہو۔

پروڈکشن میں AI ایجنٹس کو فراہم کرنے کے لیے، MAF میں شامل خصوصیات بھی ہیں:

- **مشاہدہ کاری** OpenTelemetry کے ذریعے جہاں AI ایجنٹ کی ہر کارروائی بشمول ٹول کال، آرکیسٹریشن کے مراحل، سوچنے کے بہاؤ، اور کارکردگی کی نگرانی Microsoft Foundry ڈیش بورڈز کے ذریعے ہوتی ہے۔
- **سلامتی** مائیکروسافٹ فاؤنڈری پر ایجنٹس کو میزبان کر کے جہاں رول بیسڈ رسائی، نجی ڈیٹا کی ہینڈلنگ، اور بلٹ ان مواد کی حفاظت شامل ہے۔
- **دوامی صلاحیت** کیونکہ ایجنٹ تھریڈز اور ورک فلو وقفہ، دوبارہ شروع، اور خرابیوں سے بحال ہو سکتے ہیں جو طویل عرصے تک چلنے والے عمل کو ممکن بناتا ہے۔
- **قابو** جہاں انسان کے ذریعہ منظوری کی ضرورت والے کاموں کو سپورٹ کرنے والے انسانی در لُوپ ورک فلو۔

مائیکروسافٹ ایجنٹ فریم ورک کا دھیان ایک دوسرے کے ساتھ انٹرآپریبل ہونے پر بھی ہے:

- **کلاؤڈ سے آزاد** - ایجنٹس کنٹینرز میں، آن-پریمیسس اور مختلف کلاؤڈز میں چل سکتے ہیں۔
- **پرووائیڈر سے آزاد** - ایجنٹس آپ کے پسندیدہ SDK جیسے Azure OpenAI اور OpenAI کے ذریعے بنائے جا سکتے ہیں۔
- **کھلے معیارات کا انضمام** - ایجنٹس Agent-to-Agent (A2A) اور Model Context Protocol (MCP) جیسے پروٹوکول استعمال کر کے دوسرے ایجنٹس اور ٹولز کو دریافت اور استعمال کر سکتے ہیں۔
- **پلگ ان اور کنیکٹرز** - Microsoft Fabric، SharePoint، Pinecone، اور Qdrant جیسے ڈیٹا اور میموری سروسز سے کنکشن بنائے جا سکتے ہیں۔

آئیے دیکھتے ہیں کہ یہ خصوصیات مائیکروسافٹ ایجنٹ فریم ورک کے کچھ بنیادی تصورات پر کیسے لاگو ہوتی ہیں۔

## مائیکروسافٹ ایجنٹ فریم ورک کے کلیدی تصورات

### ایجنٹس

![Agent Framework](../../../translated_images/ur/agent-components.410a06daf87b4fef.webp)

**ایجنٹس بنانا**

ایجنٹ کی تخلیق انفرنس سروس (LLM فراہم کنندہ)، AI ایجنٹ کے پیروی کرنے کے لیے ہدایات کے ایک سیٹ، اور ایک مختص شدہ `name` کی تعریف کر کے کی جاتی ہے:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

اوپر `Azure OpenAI` استعمال کیا جا رہا ہے لیکن ایجنٹس مختلف خدمات کے ذریعے بنائے جا سکتے ہیں جن میں `Microsoft Foundry Agent Service` شامل ہے:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

یا [MiniMax](https://platform.minimaxi.com/)، جو کہ بڑی کانٹیکسٹ ونڈو (204K ٹوکن تک) کے ساتھ OpenAI-مطابق API فراہم کرتا ہے:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

یا A2A پروٹوکول کا استعمال کرتے ہوئے ریموٹ ایجنٹس:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ایجنٹس چلانا**

ایجنٹس کو `.run` یا `.run_stream` طریقوں سے چلایا جاتا ہے جو نان-اسٹریمنگ یا اسٹریمنگ جوابات کے لیے ہوتے ہیں۔

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ہر ایجنٹ رن میں اختیارات بھی ہو سکتے ہیں تاکہ ایجنٹ کے استعمال کردہ `max_tokens`, ایجنٹ کے کال کرنے والے `tools`، اور یہاں تک کہ ایجنٹ کے لیے استعمال ہونے والے `model` جیسے پیرامیٹرز کو حسب ضرورت بنایا جا سکے۔

یہ ایسے حالات میں مددگار ہوتا ہے جہاں مخصوص ماڈلز یا ٹولز صارف کے کام کو مکمل کرنے کے لیے ضروری ہوں۔

**ٹولز**

ٹولز کو ایجنٹ کی تعریف کے دوران بھی متعین کیا جا سکتا ہے:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# جب ایک ChatAgent براہ راست بنایا جائے

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

اور ایجنٹ کو چلانے کے وقت بھی:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # صرف اس رن کے لئے فراہم کردہ آلہ )
```

**ایجنٹ تھریڈز**

ایجنٹ تھریڈز ملٹی ٹرن بات چیت کو سنبھالنے کے لیے استعمال ہوتے ہیں۔ تھریڈز کو یا تو اس طرح بنایا جا سکتا ہے:

- `get_new_thread()` استعمال کر کے جو تھریڈ کو وقت کے ساتھ محفوظ کرنے کے قابل بناتا ہے
- ایجنٹ چلانے کے دوران خود بخود تھریڈ بنانے اور صرف موجودہ رن کے دوران تھریڈ کو برقرار رکھنے کے ذریعے۔

تھریڈ بنانے کے لیے کوڈ ایسا ہوگا:

```python
# ایک نیا تھریڈ بنائیں۔
thread = agent.get_new_thread() # ایجنٹ کو تھریڈ کے ساتھ چلائیں۔
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

آپ پھر تھریڈ کو بعد میں استعمال کے لیے سیریلائز بھی کر سکتے ہیں:

```python
# ایک نیا تھریڈ بنائیں۔
thread = agent.get_new_thread() 

# ایجنٹ کو تھریڈ کے ساتھ چلائیں۔

response = await agent.run("Hello, how are you?", thread=thread) 

# اسٹوریج کے لیے تھریڈ کو سیریلائز کریں۔

serialized_thread = await thread.serialize() 

# اسٹوریج سے لوڈ کرنے کے بعد تھریڈ کی حالت کو ڈیسریلائز کریں۔

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ایجنٹ مڈل ویئر**

ایجنٹس ٹولز اور LLMs کے ساتھ تعامل کرتے ہیں تاکہ صارف کے کام مکمل کریں۔ بعض حالات میں، ہم ان تعاملات کے درمیان عمل درآمد یا ٹریک کرنا چاہتے ہیں۔ ایجنٹ مڈل ویئر ہمیں یہ کرنے کی اجازت دیتا ہے:

*فنکشن مڈل ویئر*

یہ مڈل ویئر ایجنٹ اور فنکشن/ٹول کے درمیان عمل درآمد کی اجازت دیتا ہے جسے ایجنٹ کال کرے گا۔ ایک مثال جب یہ استعمال ہوگا وہ ہے فنکشن کال پر لاگنگ کرنا۔

نیچے کوڈ میں `next` متعین کرتا ہے کہ آیا اگلا مڈل ویئر یا اصل فنکشن کو کال کیا جانا چاہیے۔

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # پروسیسنگ سے پہلے: فنکشن کے عمل درآمد سے پہلے لاگ کریں
    print(f"[Function] Calling {context.function.name}")

    # اگلے مڈل ویئر یا فنکشن کے عمل درآمد کو جاری رکھیں
    await next(context)

    # پروسیسنگ کے بعد: فنکشن کے عمل درآمد کے بعد لاگ کریں
    print(f"[Function] {context.function.name} completed")
```

*چیٹ مڈل ویئر*

یہ مڈل ویئر ایجنٹ اور LLM کے درمیان درخواستوں کے درمیان ایکشن لاگ یا عمل درآمد کرنے کی اجازت دیتا ہے۔

اس میں اہم معلومات شامل ہیں جیسے کہ AI سروس کو بھیجے جانے والے `messages`۔

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # پری پروسیسنگ: اے آئی کال سے پہلے لاگ
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # اگلے مڈل ویئر یا اے آئی سروس پر جاری رکھیں
    await next(context)

    # پوسٹ پروسیسنگ: اے آئی کے جواب کے بعد لاگ
    print("[Chat] AI response received")

```

**ایجنٹ میموری**

`Agentic Memory` سبق میں پہلے بتایا گیا ہے کہ میموری ایجنٹ کو مختلف سیاق و سباق پر کام کرنے کے قابل بنانے کا ایک اہم عنصر ہے۔ MAF کئی مختلف قسم کی میموریز پیش کرتا ہے:

*ان-میموری اسٹوریج*

یہ وہ میموری ہے جو تھریڈز میں درخواست کے رن ٹائم کے دوران محفوظ ہوتی ہے۔

```python
# ایک نیا تھریڈ بنائیں۔
thread = agent.get_new_thread() # ایجنٹ کو تھریڈ کے ساتھ چلائیں۔
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*مستقل پیغامات*

یہ میموری بات چیت کی تاریخ کو مختلف سیشنز کے دوران محفوظ کرنے کے لیے استعمال ہوتی ہے۔ اسے `chat_message_store_factory` کا استعمال کرتے ہوئے متعین کیا جاتا ہے:

```python
from agent_framework import ChatMessageStore

# ایک حسب ضرورت پیغام اسٹور بنائیں
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*ڈائنامک میموری*

یہ میموری سیاق و سباق میں ایجنٹس کے چلانے سے پہلے شامل کی جاتی ہے۔ یہ میموریز بیرونی سروسز مثلاً mem0 میں محفوظ کی جا سکتی ہیں:

```python
from agent_framework.mem0 import Mem0Provider

# میموری کی اعلی صلاحیتوں کے لیے Mem0 کا استعمال
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

**ایجنٹ مشاہدہ کاری**

مشاہدہ کاری قابل اعتماد اور قابل نگہداشت ایجنٹک نظام بنانے کے لیے اہم ہے۔ MAF OpenTelemetry کے ساتھ انضمام کرتا ہے تاکہ بہتر مشاہدہ کاری کے لیے ٹریسنگ اور میٹر فراہم کرے۔

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # کچھ کریں
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### ورک فلو

MAF ایسے ورک فلو پیش کرتا ہے جو کام مکمل کرنے کے پیشگی متعین مراحل ہیں اور ان مراحل میں AI ایجنٹس کو اجزاء کے طور پر شامل کیا جاتا ہے۔

ورک فلو مختلف اجزاء پر مشتمل ہوتے ہیں جو بہتر کنٹرول فلو کی اجازت دیتے ہیں۔ ورک فلو **کثیر ایجنٹ آرکیسٹریشن** اور ورک فلو ریاستوں کو محفوظ کرنے کے لیے **چیک پوائنٹنگ** کو بھی ممکن بناتے ہیں۔

ورک فلو کے بنیادی اجزاء یہ ہیں:

**ایگزیکیوٹرز**

ایگزیکیوٹرز ان پٹ پیغامات وصول کرتے ہیں، تفویض کردہ کام انجام دیتے ہیں، اور پھر ایک پیداوار پیغام دیتے ہیں۔ یہ ورک فلو کو بڑے کام کی تکمیل کی طرف بڑھاتا ہے۔ ایگزیکیوٹرز یا تو AI ایجنٹ ہو سکتے ہیں یا حسب ضرورت منطق۔

**ایجز**

ایجز ورک فلو میں پیغامات کے بہاؤ کو تعریف کرنے کے لیے استعمال ہوتے ہیں۔ یہ ہو سکتے ہیں:

*براہ راست ایجز* - ایگزیکیوٹرز کے درمیان سادہ ایک سے ایک رابطے:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*مشروط ایجز* - جب کوئی خاص شرط پوری ہو تو فعال ہوتے ہیں۔ مثال کے طور پر، جب ہوٹل کے کمرے دستیاب نہ ہوں، ایک ایگزیکیوٹر دوسرے اختیارات تجویز کر سکتا ہے۔

*سوئچ-کیس ایجز* - پیغامات کو مختلف ایگزیکیوٹرز کی طرف مختلف شرائط کی بنیاد پر بھیجتے ہیں۔ مثال کے طور پر، اگر سفر کے صارف کو ترجیحی رسائی حاصل ہو اور ان کے کام دوسرے ورک فلو کے ذریعے سنبھالے جائیں۔

*فین آؤٹ ایجز* - ایک پیغام کو متعدد مقامات پر بھیجنا۔

*فین اِن ایجز* - مختلف ایگزیکیوٹرز سے متعدد پیغامات جمع کر کے ایک ہدف کو بھیجنا۔

**ایونٹس**

ورک فلو کی بہتر مشاہدہ کاری کے لیے، MAF ایگزیکیوٹر کے ایگزیکیوشن کے لیے بلٹ ان ایونٹس فراہم کرتا ہے جن میں شامل ہیں:

- `WorkflowStartedEvent`  - ورک فلو کا آغاز ہوتا ہے
- `WorkflowOutputEvent` - ورک فلو ایک آؤٹ پٹ پیدا کرتا ہے
- `WorkflowErrorEvent` - ورک فلو کو کوئی خرابی پیش آتی ہے
- `ExecutorInvokeEvent`  - ایگزیکیوٹر پروسیسنگ شروع کرتا ہے
- `ExecutorCompleteEvent`  - ایگزیکیوٹر پروسیسنگ مکمل کرتا ہے
- `RequestInfoEvent` - درخواست جاری کی جاتی ہے

## جدید MAF پیٹرنز

اوپر کے حصے مائیکروسافٹ ایجنٹ فریم ورک کے کلیدی تصورات کو کور کرتے ہیں۔ جیسے جیسے آپ مزید پیچیدہ ایجنٹس بنائیں، یہاں کچھ جدید پیٹرنز غور کرنے کے لیے ہیں:

- **مڈل ویئر کمپوزیشن**: فنکشن اور چیٹ مڈل ویئر استعمال کر کے متعدد مڈل ویئر ہینڈلرز (لاگنگ، تصدیق، ریٹ-لمٹنگ) کو چین کریں تاکہ ایجنٹ کے رویے پر باریک کنٹرول حاصل کیا جا سکے۔
- **ورک فلو چیک پوائنٹنگ**: ورک فلو ایونٹس اور سیریلائزیشن کا استعمال کر کے طویل چلنے والے ایجنٹ پروسیسز کو محفوظ اور دوبارہ شروع کریں۔
- **ڈائنامک ٹول انتخاب**: MAF کے ٹول رجسٹریشن کے ساتھ ٹول کے وضاحتی RAG کو ملا کر صرف متعلقہ ٹولز کو ہر سوال پر پیش کریں۔
- **کثیر ایجنٹ ہینڈ آف**: ورک فلو ایجز اور مشروط راستہ بندی کا استعمال کرتے ہوئے مہارت یافتہ ایجنٹس کے درمیان ہینڈ آف کو منظم کریں۔

## Microsoft Foundry پر LangChain / LangGraph ایجنٹس کی میزبانی

مائیکروسافٹ ایجنٹ فریم ورک **فریم ورک-انٹرآپریبل** ہے— آپ MAF کے ساتھ لکھے گئے ایجنٹس تک محدود نہیں ہیں۔ اگر آپ کے پاس پہلے سے ہی **LangChain** یا **LangGraph** میں بنایا ہوا ایجنٹ ہے، تو آپ اسے **Microsoft Foundry میزبان ایجنٹ** کے طور پر چلا سکتے ہیں تاکہ Foundry رن ٹائم، سیشنز، اسکیلنگ، شناخت، اور پروٹوکول اینڈ پوائنٹس کو سنبھالے جبکہ آپ کی ایجنٹ منطق LangGraph میں رہے۔

یہ `langchain_azure_ai.agents.hosting` پیکج کے ذریعے کیا جاتا ہے، جو وہی پروٹوکولز استعمال کرتا ہے جو Foundry میزبان ایجنٹس استعمال کرتے ہیں اور LangGraph گراف کو مرتب کر کے ایکسپورٹ کرتا ہے۔

**1. ہوسٹنگ ایکسٹرا انسٹال کریں:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` ایکسٹرا Foundry پروٹوکول لائبریریاں انسٹال کرتا ہے: `azure-ai-agentserver-responses` (OpenAI-مطابق `/responses` اینڈ پوائنٹ) اور `azure-ai-agentserver-invocations` (عام `/invocations` اینڈ پوائنٹ)۔

**2. ہوسٹنگ پروٹوکول منتخب کریں:**

| پروٹوکول | میزبان کلاس | اینڈ پوائنٹ | کب استعمال کریں |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | آپ OpenAI-مطابق چیٹ، اسٹریمنگ، جواب کی تاریخ، اور گفتگو کے تھریڈنگ چاہتے ہیں — مکالماتی ایجنٹس کے لیے سفارش کردہ ڈیفالٹ۔ |
| **Invocations** | `InvocationsHostServer` | `/invocations` | آپ کو حسب ضرورت JSON شکل، ویب ہک طرز اینڈ پوائنٹ، یا غیر مکالماتی پروسیسنگ کی ضرورت ہے۔ |

کیونکہ **Responses API Foundry میں ایجنٹ-اسٹائل ترقی کے لیے بنیادی API ہے**، زیادہ تر ایجنٹس کے لیے `ResponsesHostServer` سے شروع کریں۔

**3. ماحول کے متغیرات مرتب کریں** (`az login` پہلے کریں تاکہ `DefaultAzureCredential` تصدیق کر سکے):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

جب ایجنٹ بعد میں Foundry میں میزبان ایجنٹ کے طور پر چلتا ہے، تو پلیٹ فارم خود بخود `FOUNDRY_PROJECT_ENDPOINT` داخل کرتا ہے۔

**4. Responses پروٹوکول پر LangGraph ایجنٹ کا انکشاف کریں:**

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

    # ChatOpenAI یہاں Foundry پروجیکٹ کے OpenAI مطابقت پذیر (Responses) اینڈ پوائنٹ کو ہدف بناتا ہے۔
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

اسے مقامی طور پر `python main.py` سے چلائیں، پھر `http://localhost:8088/responses` پر Responses کی درخواست بھیجیں۔

**کلیدی خصوصیات:**

- **گفتگو**: کلائنٹس گفتگو جاری رکھتے ہیں `previous_response_id` یا `conversation` ID کے ذریعے۔ اگر آپ کا گراف LangGraph چیک پوائنٹر کے ساتھ مرتب کیا گیا ہے، تو Foundry کنورسیشن اسٹیٹ کو چیک پوائنٹ سے مربوط کرتا ہے (پروڈکشن میں پائیدار چیک پوائنٹر استعمال کریں؛ مقامی جانچ کے لیے `MemorySaver` ٹھیک ہے)۔
- **انسان-در-لُوپ**: اگر آپ کا گراف LangGraph `interrupt()` استعمال کرتا ہے، تو `ResponsesHostServer` زیر التواء انٹرپٹ کو Responses `function_call` / `mcp_approval_request` آئٹم کے طور پر ظاہر کرتا ہے، اور کلائنٹس میچنگ `function_call_output` / `mcp_approval_response` کے ساتھ دوبارہ شروع ہوتے ہیں۔
- **Foundry پر تعینات کریں**: Azure Developer CLI استعمال کریں — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (مقامی، ڈوکر کی ضرورت ہے)، پھر `azd provision` اور `azd deploy`۔ میزبان ایجنٹ کی تعیناتی کے لیے **Foundry Project Manager** کردار ضروری ہے۔

اس مثال کا چلنے والا ورژن [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) میں موجود ہے۔ مکمل رہنمائی (Invocations پروٹوکول، حسب ضرورت درخواست کے اسکیمے، اور مسئلہ حل) کے لیے دیکھیں [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)۔

## کوڈ کے نمونے 

مائیکروسافٹ ایجنٹ فریم ورک کے کوڈ کے نمونے اس رپوزیٹری میں `xx-python-agent-framework` اور `xx-dotnet-agent-framework` فائلوں کے تحت مل سکتے ہیں۔

## مائیکروسافٹ ایجنٹ فریم ورک کے بارے میں مزید سوالات ہیں؟

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) میں شامل ہوں تاکہ دوسرے سیکھنے والوں سے ملیں، آفس آور میں شرکت کریں اور اپنے AI ایجنٹس کے سوالات کے جواب حاصل کریں۔
## پچھلا سبق

[AI ایجنٹس کے لیے میموری](../13-agent-memory/README.md)

## اگلا سبق

[کمپیوٹر یوز ایجنٹس (CUA) بنانا](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->