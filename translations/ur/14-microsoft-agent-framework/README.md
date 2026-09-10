# مائیکروسافٹ ایجنٹ فریم ورک کا جائزہ

![Agent Framework](../../../translated_images/ur/lesson-14-thumbnail.90df0065b9d234ee.webp)

### تعارف

اس سبق میں درج ذیل موضوعات شامل ہوں گے:

- مائیکروسافٹ ایجنٹ فریم ورک کو سمجھنا: اہم خصوصیات اور قیمت  
- مائیکروسافٹ ایجنٹ فریم ورک کے کلیدی تصورات کی تلاش
- اعلی درجے کے MAF نمونے: ورک فلو، مڈل ویئر، اور میموری

## تعلیمی اہداف

اس سبق کو مکمل کرنے کے بعد، آپ جان جائیں گے کہ کیسے:

- مائیکروسافٹ ایجنٹ فریم ورک کے استعمال سے پروڈکشن کے لئے تیار AI ایجنٹس بنائیں
- مائیکروسافٹ ایجنٹ فریم ورک کی بنیادی خصوصیات کو اپنے ایجنٹک استعمال کے کیسز پر لاگو کریں
- ورک فلو، مڈل ویئر، اور مشاہدہ کاری جیسے اعلی درجے کے نمونوں کا استعمال کریں

## کوڈ کے نمونے

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) کے کوڈ نمونے اس مخزن میں `xx-python-agent-framework` اور `xx-dotnet-agent-framework` فائلوں کے تحت مل سکتے ہیں۔

## مائیکروسافٹ ایجنٹ فریم ورک کو سمجھنا

![Framework Intro](../../../translated_images/ur/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) مائیکروسافٹ کا متحدہ فریم ورک ہے جو AI ایجنٹس بنانے کے لیے استعمال ہوتا ہے۔ یہ لچکدار ہے تاکہ مختلف قسم کے ایجنٹک استعمال کے کیسز کو حل کیا جا سکے جو پروڈکشن اور تحقیقاتی ماحول دونوں میں دیکھے جاتے ہیں، جن میں شامل ہیں:

- **تسلسل میں ایجنٹ کی ترتیب** ایسی صورتوں میں جہاں قدم بہ قدم ورک فلو کی ضرورت ہو۔
- **متوازی ترتیب** ایسی صورتوں میں جہاں ایجنٹس کو بیک وقت کام مکمل کرنا ہو۔
- **گروپ چیٹ کی ترتیب** ایسی صورتوں میں جہاں ایجنٹس ایک ساتھ مل کر ایک کام پر تعاون کرتے ہیں۔
- **ہینڈ آف کی ترتیب** ایسی صورتوں میں جہاں ایجنٹس ذیلی کام مکمل ہونے پر کام ایک دوسرے کو منتقل کرتے ہیں۔
- **مقناطیسی ترتیب** ایسی صورتوں میں جہاں ایک مینیجر ایجنٹ کام کی فہرست بناتا اور تبدیل کرتا ہے اور ذیلی ایجنٹس کی ہم آہنگی کو سنبھالتا ہے تاکہ کام مکمل ہو۔

پروڈکشن میں AI ایجنٹس کی فراہمی کے لیے، MAF میں مزید خصوصیات شامل کی گئی ہیں:

- **مشاہدہ کاری** اوپن ٹیلی میٹری کے استعمال سے جہاں AI ایجنٹ کے ہر عمل بشمول ٹول بلانے، ترتیب کے مراحل، منطق کے بہاؤ اور مائیکروسافٹ فاؤنڈری ڈیش بورڈز کے ذریعے کارکردگی کی نگرانی شامل ہے۔
- **سیکیورٹی** مائیکروسافٹ فاؤنڈری پر ایجنٹس کی مقامی میزبانی کے ذریعے جو رول بیسڈ ایکسیس، نجی ڈیٹا ہینڈلنگ اور بلٹ ان مواد کی حفاظت جیسے سیکیورٹی کنٹرولز شامل ہے۔
- **دوامی** کیونکہ ایجنٹ کے دھاگے اور ورک فلو روک، دوبارہ شروع اور غلطیوں سے بحال ہو سکتے ہیں جو طویل مدتی عمل کی اجازت دیتا ہے۔
- **کنٹرول** کیونکہ انسان کی شمولیت کے ساتھ ورک فلو کی حمایت کی جاتی ہے جہاں کاموں کو انسانی منظوری کی ضرورت کے طور پر نشان زد کیا جاتا ہے۔

مائیکروسافٹ ایجنٹ فریم ورک کی توجہ بین الاطلاقیت پر بھی ہے:

- **کلاؤڈ سے آزاد** - ایجنٹس کنٹینرز، آن پرائمز اور مختلف کلاؤڈز میں چل سکتے ہیں۔
- **پرووائیڈر سے آزاد** - ایجنٹس آپکے پسندیدہ SDK جیسے Azure OpenAI اور OpenAI کے ذریعے بنائے جا سکتے ہیں۔
- **اوپن اسٹینڈرڈز کا انضمام** - ایجنٹس دیگر ایجنٹس اور ٹولز کو دریافت کرنے اور استعمال کرنے کے لیے ایجنٹ ٹو ایجنٹ (A2A) اور ماڈل کانٹیکسٹ پروٹوکول (MCP) جیسے پروٹوکول استعمال کر سکتے ہیں۔
- **پلگ انز اور کنیکٹرز** - کنکشنز ڈیٹا اور میموری سروسز جیسے Microsoft Fabric, SharePoint, Pinecone, اور Qdrant سے کیے جا سکتے ہیں۔

آئیے دیکھتے ہیں کہ یہ خصوصیات مائیکروسافٹ ایجنٹ فریم ورک کے کچھ بنیادی تصورات پر کیسے لاگو ہوتی ہیں۔

## مائیکروسافٹ ایجنٹ فریم ورک کے کلیدی تصورات

### ایجنٹس

![Agent Framework](../../../translated_images/ur/agent-components.410a06daf87b4fef.webp)

**ایجنٹس بنانا**

ایجنٹ کی تخلیق انفرنس سروس (LLM پرووائیڈر) کی تعریف کرکے کی جاتی ہے، AI ایجنٹ کو پیروی کرنے کے لیے ہدایات کا مجموعہ، اور ایک مختص `name`:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

اوپر `Azure OpenAI` استعمال ہو رہا ہے لیکن ایجنٹس مختلف سروسز کے استعمال سے بنائے جا سکتے ہیں جن میں `Microsoft Foundry Agent Service` شامل ہے:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI کی `Responses`، `ChatCompletion` API

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

یا [MiniMax](https://platform.minimaxi.com/), جو بڑا کانٹیکسٹ ونڈوز (204K ٹوکن تک) کے ساتھ OpenAI-مطابق API فراہم کرتا ہے:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

یا ریموٹ ایجنٹس جو A2A پروٹوکول استعمال کرتے ہیں:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ایجنٹس چلانا**

ایجنٹس کو `.run` یا `.run_stream` طریقوں سے چلایا جاتا ہے، غیر-اسٹریمنگ یا اسٹریمنگ جوابات کے لیے۔

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ہر ایجنٹ رن کے ساتھ اختیارات بھی شامل ہو سکتے ہیں جیسے ایجنٹ کے استعمال کردہ `max_tokens`، ایجنٹ کی کال کر سکنے والی `tools`، اور خود ایجنٹ کے لیے استعمال ہونے والا `model`۔

یہ مخصوص ماڈلز یا ٹولز کی ضرورت والے کاموں کے لیے مفید ہے۔

**ٹولز**

ٹولز کو ایجنٹ کی تعریف کرتے وقت بھی مقرر کیا جا سکتا ہے:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# جب براہِ راست ایک ChatAgent بنایا جا رہا ہو

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

اور ایجنٹ کو چلانے کے وقت بھی:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # صرف اس دوڑ کے لیے فراہم کردہ آلہ )
```

**ایجنٹ دھاگے**

ایجنٹ دھاگے کثیر دور بات چیت سنبھالنے کے لیے استعمال ہوتے ہیں۔ دھاگے بنانے کے دو طریقے ہیں:

- `get_new_thread()` کا استعمال جو وقت کے ساتھ دھاگے کو محفوظ کرنے کی اجازت دیتا ہے
- کوئی دھاگہ خود بخود ایجنٹ کے چلانے پر پیدا ہو جائے، اور صرف موجودہ رن کے دوران موجود رہے۔

دھاگہ بنانے کا کوڈ اس طرح دکھتا ہے:

```python
# ایک نئی تھریڈ بنائیں۔
thread = agent.get_new_thread() # تھریڈ کے ساتھ ایجنٹ چلائیں۔
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

آپ بعد میں استعمال کے لیے دھاگے کو سیریلائز کر سکتے ہیں:

```python
# نیا تھریڈ بنائیں۔
thread = agent.get_new_thread() 

# ایجنٹ کو تھریڈ کے ساتھ چلائیں۔

response = await agent.run("Hello, how are you?", thread=thread) 

# اسٹوریج کے لیے تھریڈ کو سیریلائز کریں۔

serialized_thread = await thread.serialize() 

# اسٹوریج سے لوڈ کرنے کے بعد تھریڈ کی حالت کو ڈیسریلائز کریں۔

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ایجنٹ مڈل ویئر**

ایجنٹس اوزار اور LLMs کے ساتھ صارف کے کام پورے کرنے کے لیے بات چیت کرتے ہیں۔ کچھ صورتوں میں، ہم ان تعاملات کے درمیان ایکشن چلانے یا ٹریک کرنے کا ارادہ رکھتے ہیں۔ ایجنٹ مڈل ویئر ہمیں یہ کرنے کی اجازت دیتا ہے:

*فنکشن مڈل ویئر*

یہ مڈل ویئر ہمیں ایجنٹ اور اس فنکشن/ٹول کے درمیان ایکشن چلانے کی سہولت دیتا ہے جسے وہ کال کرے گا۔ مثال کے طور پر، آپ فنکشن کال پر لاگنگ کرنا چاہیں۔

نیچے کوڈ میں `next` بتاتا ہے کہ اگلا مڈل ویئر یا اصل فنکشن کال ہونا چاہیے۔

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # پری پروسیسنگ: فنکشن کی عمل آوری سے پہلے لاگ کریں
    print(f"[Function] Calling {context.function.name}")

    # اگلے مڈل ویئر یا فنکشن کی عمل آوری جاری رکھیں
    await next(context)

    # پوسٹ پروسیسنگ: فنکشن کی عمل آوری کے بعد لاگ کریں
    print(f"[Function] {context.function.name} completed")
```

*چیٹ مڈل ویئر*

یہ مڈل ویئر ایجنٹ اور LLM کے درمیان درخواستوں کے دوران کوئی ایکشن چلانے یا لاگ کرنے کی اجازت دیتا ہے۔

اس میں اہم معلومات شامل ہیں جیسے AI سروس کو بھیجے جانے والے `messages`۔

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # پری پروسیسنگ: اے آئی کال سے پہلے لاگ کریں
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # اگلے مڈل ویئر یا اے آئی سروس پر جاری رکھیں
    await next(context)

    # پوسٹ پروسیسنگ: اے آئی کے جواب کے بعد لاگ کریں
    print("[Chat] AI response received")

```

**ایجنٹ میموری**

جیسا کہ `Agentic Memory` سبق میں بتایا گیا، میموری ایجنٹ کو مختلف سیاق و سباق میں کام کرنے کے قابل بنانے کے لیے اہم عنصر ہے۔ MAF مختلف اقسام کی میموریز پیش کرتا ہے:

*ان-میموری اسٹوریج*

یہ میموری دھاگوں میں ایپلیکیشن رن ٹائم کے دوران محفوظ ہوتی ہے۔

```python
# ایک نیا تھریڈ بنائیں۔
thread = agent.get_new_thread() # تھریڈ کے ساتھ ایجنٹ چلائیں۔
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*مستقل پیغامات*

یہ میموری مختلف سیشنز میں گفتگو کی تاریخ محفوظ کرنے کے لیے استعمال ہوتی ہے۔ اسے `chat_message_store_factory` کے ذریعے متعین کیا جاتا ہے:

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

*متحرک میموری*

یہ میموری ایجنٹس کو چلانے سے قبل سیاق و سباق میں شامل کی جاتی ہے۔ یہ بیرونی خدمات میں محفوظ کی جا سکتی ہے جیسے mem0:

```python
from agent_framework.mem0 import Mem0Provider

# میم۰ کو جدید میموری صلاحیتوں کے لیے استعمال کرنا
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

مشاہدہ کاری قابل اعتماد اور قابلِ برقرار رکھنے والے ایجنٹک سسٹمز بنانے کے لیے اہم ہے۔ MAF اوپن ٹیلی میٹری کے ساتھ انضمام کرتا ہے تاکہ بہتر مشاہدہ کاری کے لیے ٹریسنگ اور میٹرز فراہم کی جا سکیں۔

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # کچھ کرو
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### ورک فلو

MAF ورک فلو پیش کرتا ہے جو کام مکمل کرنے کے پہلے سے مقرر شدہ مراحل ہوتے ہیں جن میں AI ایجنٹس کو اجزاء کے طور پر شامل کیا جاتا ہے۔

ورک فلو مختلف اجزاء پر مشتمل ہوتے ہیں جو بہتر کنٹرول فلو کی اجازت دیتے ہیں۔ ورک فلو **کثیر ایجنٹ ترتیب** اور **چیک پوائنٹنگ** کی بھی اجازت دیتے ہیں تاکہ ورک فلو کی حالتیں محفوظ کی جا سکیں۔

ورک فلو کے بنیادی اجزاء ہیں:

**ایگزیکیوٹرز**

ایگزیکیوٹرز ان پٹ پیغامات وصول کرتے ہیں، اپنے مختص شدہ کام انجام دیتے ہیں، اور پھر آؤٹ پٹ پیغام بناتے ہیں۔ یہ ورک فلو کو بڑے کام کی تکمیل کی جانب آگے بڑھاتا ہے۔ ایگزیکیوٹرز AI ایجنٹ یا کسٹم لاجک ہو سکتے ہیں۔

**ایجز**

ایجز ورک فلو میں پیغامات کے بہاؤ کی تعریف کے لیے استعمال ہوتے ہیں۔ یہ ہو سکتے ہیں:

*براہ راست ایجز* - ایگزیکیوٹرز کے درمیان سادہ ایک سے ایک کنکشنز:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*شرائطی ایجز* - مخصوص شرط پورا ہونے کے بعد فعال ہوتے ہیں۔ مثال کے طور پر، جب ہوٹلز کے کمرے دستیاب نہ ہوں، ایک ایگزیکیوٹر دیگر اختیارات تجویز کر سکتا ہے۔

*سوئچ-کیس ایجز* - پیغامات کو مختلف ایگزیکیوٹرز کی طرف بھیجنا، شرائط کی بنیاد پر۔ مثلاً اگر سفر کا صارف ترجیحی رسائی رکھتا ہے تو اس کے کام دوسرے ورک فلو کے ذریعے انجام دیے جائیں گے۔

*فین آؤٹ ایجز* - ایک پیغام کو متعدد ہدفوں تک بھیجنا۔

*فین ان ایجز* - متعدد پیغامات کو مختلف ایگزیکیوٹرز سے جمع کر کے ایک ہدف کو بھیجنا۔

**ایونٹس**

ورک فلو کی بہتر مشاہدہ کاری کے لیے، MAF تعمیل ایونٹس فراہم کرتا ہے جن میں شامل ہیں:

- `WorkflowStartedEvent`  - ورک فلو کی شروعات
- `WorkflowOutputEvent` - ورک فلو ایک آؤٹ پٹ پیدا کرتا ہے
- `WorkflowErrorEvent` - ورک فلو میں خرابی ہوتی ہے
- `ExecutorInvokeEvent`  - ایگزیکیوٹر کام شروع کرتا ہے
- `ExecutorCompleteEvent`  - ایگزیکیوٹر کام ختم کرتا ہے
- `RequestInfoEvent` - ایک درخواست جاری کی جاتی ہے

## اعلی درجے کے MAF نمونے

اوپر کے سیکشنز مائیکروسافٹ ایجنٹ فریم ورک کے کلیدی تصورات کا احاطہ کرتے ہیں۔ جب آپ مزید پیچیدہ ایجنٹس بناتے ہیں تو یہاں کچھ اعلی درجے کے نمونے ہیں جن پر غور کریں:

- **مڈل ویئر کمپوزیشن**: کئی مڈل ویئر ہینڈلرز (لاگنگ، اجازت، ریٹ-لیمٹینگ) کو فنکشن اور چیٹ مڈل ویئر کے ذریعہ سلسلہ وار جوڑیں تاکہ ایجنٹ کے رویے پر باریک کنٹرول حاصل ہو۔
- **ورک فلو چیک پوائنٹنگ**: ورک فلو ایونٹس اور سیریلائزیشن کے ذریعے طویل عمل کرنے والے ایجنٹ کے عمل کو محفوظ اور بحال کریں۔
- **متحرک ٹول منتخب کرنا**: MAF کے ٹول رجسٹریشن کے ساتھ RAG کو ٹول وضاحتوں پر ملا کر صرف متعلقہ ٹولز کو ہر سوال کے لیے پیش کریں۔
- **کثیر ایجنٹ ہینڈ آف**: ورک فلو ایجز اور شرائطی روٹنگ کا استعمال کریں تاکہ خصوصی نوعیت کے ایجنٹس کے درمیان ہینڈ آف کو ترتیب دیا جا سکے۔

## مائیکروسافٹ فاؤنڈری پر LangChain / LangGraph ایجنٹس کی میزبانی

مائیکروسافٹ ایجنٹ فریم ورک **فریم ورک بین الاطلاقی** ہے — آپ MAF کے ساتھ لکھے گئے ایجنٹس تک محدود نہیں ہیں۔ اگر آپ کے پاس پہلے سے **LangChain** یا **LangGraph** میں بنا ہوا ایجنٹ ہے، تو آپ اسے **مائیکروسافٹ فاؤنڈری ہوسٹڈ ایجنٹ** کے طور پر چلا سکتے ہیں تاکہ فاؤنڈری رن ٹائم، سیشنز، اسکیلنگ، شناخت، اور پروٹوکول اینڈ پوائنٹس کو سنبھالے، جبکہ آپ کی ایجنٹ لاجک LangGraph میں رہے۔

یہ `langchain_azure_ai.agents.hosting` پیکج کے ذریعے کیا جاتا ہے، جو کمپائل شدہ LangGraph گراف کو ان ہی پروٹوکولز پر ظاہر کرتا ہے جو فاؤنڈری ہوسٹڈ ایجنٹس استعمال کرتے ہیں۔

**1. ہوسٹنگ ایکسٹرا انسٹال کریں:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` ایکسٹرا Foundry پروٹوکول لائبریریز انسٹال کرتا ہے: `azure-ai-agentserver-responses` (OpenAI-مطابق `/responses` اینڈپوائنٹ) اور `azure-ai-agentserver-invocations` (جنرل `/invocations` اینڈپوائنٹ)۔

**2. ہوسٹنگ پروٹوکول منتخب کریں:**

| پروٹوکول | میزبان کلا‌س | اینڈپوائنٹ | کب استعمال کریں |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | جب آپ OpenAI-مطابق چیٹ، اسٹریمنگ، جواب کی تاریخ، اور گفتگو کے دھاگے چاہتے ہیں — جو مشورہ شدہ ڈیفالٹ ہے بات چیت کے ایجنٹس کے لیے۔ |
| **Invocations** | `InvocationsHostServer` | `/invocations` | جب آپ کو کسٹم JSON شکل، ویب ہک طرز کا اینڈپوائنٹ، یا غیر بات چیت پر مبنی پروسیسنگ کی ضرورت ہو۔ |

چونکہ **Responses API Foundry میں ایجنٹ اسٹائل ڈیولپمنٹ کے لیے بنیادی API ہے**، زیادہ تر ایجنٹس کے لیے `ResponsesHostServer` کے ساتھ شروع کریں۔

**3. ماحول کی متغیرات ترتیب دیں** (`az login` پہلے کریں تاکہ `DefaultAzureCredential` تصدیق کر سکے):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

جب ایجنٹ بعد میں فاؤنڈری میں ہوسٹڈ ایجنٹ کے طور پر چلایا جائے گا، پلیٹ فارم خودبخود `FOUNDRY_PROJECT_ENDPOINT` ڈالے گا۔

**4. Responses پروٹوکول پر LangGraph ایجنٹ ظاہر کریں:**

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

    # ChatOpenAI یہاں Foundry پروجیکٹ کے OpenAI کے موافق (Responses) اینڈپوائنٹ کو ہدف بناتا ہے۔
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

**کلیدی رویے:**

- **گفتگو**: کلائنٹ گفتگو کو `previous_response_id` یا `conversation` ID بھیج کر جاری رکھتے ہیں۔ اگر آپ کا گراف LangGraph چیک پوائنٹر کے ساتھ کمپائل کیا گیا ہے، تو فاؤنڈری گفتگو کی حالت کو چیک پوائنٹ سے جوڑتا ہے (پروڈکشن میں دیرپا چیک پوائنٹر استعمال کریں؛ لوکل ٹیسٹنگ کے لیے `MemorySaver` ٹھیک ہے)۔
- **انسانی مداخلت**: اگر آپ کا گراف LangGraph `interrupt()` استعمال کرتا ہے، تو `ResponsesHostServer` منتظر مداخلت کو Responses `function_call` / `mcp_approval_request` آئٹم کے طور پر ظاہر کرتا ہے، اور کلائنٹس مطابقت رکھنے والے `function_call_output` / `mcp_approval_response` کے ساتھ دوبارہ شروع ہوتے ہیں۔
- **Foundry پر تعینات کریں**: Azure Developer CLI استعمال کریں — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (لوکل، ڈوکر کی ضرورت)، پھر `azd provision` اور `azd deploy`۔ ہوسٹڈ ایجنٹ کی تعیناتی کے لیے **Foundry Project Manager** کا کردار ضروری ہے۔

اس مثال کا چلنے والا ورژن [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) میں موجود ہے۔ مکمل وضاحت (Invocations پروٹوکول، کسٹم درخواست اسکیمے، اور خرابی کی تشخیص) کے لیے دیکھیں [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)۔

## کوڈ کے نمونے

مائیکروسافٹ ایجنٹ فریم ورک کے کوڈ نمونے اس مخزن میں `xx-python-agent-framework` اور `xx-dotnet-agent-framework` فائلوں کے تحت مل سکتے ہیں۔

## مائیکروسافٹ ایجنٹ فریم ورک کے متعلق مزید سوالات ہیں؟

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) میں شامل ہوں تاکہ دوسرے سیکھنے والوں سے ملیں، آفس آورز میں شرکت کریں اور اپنے AI ایجنٹس کے سوالات کے جواب پائیں۔
## پچھلا سبق

[AI ایجنٹس کے لیے میموری](../13-agent-memory/README.md)

## اگلا سبق

[کمپیوٹر استعمال کرنے والے ایجنٹس (CUA) بنانا](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->