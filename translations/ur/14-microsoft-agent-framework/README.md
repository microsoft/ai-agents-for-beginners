# مائیکروسافٹ ایجنٹ فریم ورک کا جائزہ

![ایجنٹ فریم ورک](../../../translated_images/ur/lesson-14-thumbnail.90df0065b9d234ee.webp)

### تعارف

یہ سبق درج ذیل موضوعات کا احاطہ کرے گا:

- مائیکروسافٹ ایجنٹ فریم ورک کو سمجھنا: اہم خصوصیات اور فوائد  
- مائیکروسافٹ ایجنٹ فریم ورک کے کلیدی تصورات کا جائزہ
- ایڈوانسڈ MAF پیٹرنز: ورک فلو، مڈل ویئر، اور میموری

## تعلیمی مقاصد

اس سبق کو مکمل کرنے کے بعد، آپ جان سکیں گے کہ:

- مائیکروسافٹ ایجنٹ فریم ورک استعمال کرتے ہوئے پروڈکشن کے قابل AI ایجنٹس تیار کریں
- مائیکروسافٹ ایجنٹ فریم ورک کی بنیادی خصوصیات کو اپنے Agentic استعمال کے معاملات پر نافذ کریں
- پیجیدہ پیٹرنز جیسے ورک فلو، مڈل ویئر، اور آبزروبیلیٹی کو استعمال کریں

## کوڈ کے نمونے 

اس ریپوزیٹری میں [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) کے کوڈ کے نمونے `xx-python-agent-framework` اور `xx-dotnet-agent-framework` فائلوں کے تحت مل سکتے ہیں۔

## مائیکروسافٹ ایجنٹ فریم ورک کو سمجھنا

![فریم ورک کا تعارف](../../../translated_images/ur/framework-intro.077af16617cf130c.webp)

[مائیکروسافٹ ایجنٹ فریم ورک (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) AI ایجنٹس بنانے کے لیے مائیکروسافٹ کا متحد فریم ورک ہے۔ یہ پیداوار اور تحقیق کے دونوں ماحول میں دیکھی جانے والی ایجنٹک استعمال کے معاملات کی وسیع اقسام کو حل کرنے کی لچک فراہم کرتا ہے جن میں شامل ہیں:

- **تسلسلی ایجنٹ آرکسٹریشن** ایسی صورتحال میں جہاں قدم بہ قدم ورک فلو درکار ہوں۔
- **ہم وقت آرکسٹریشن** ایسی صورتحال میں جہاں ایجنٹس کو بیک وقت کام مکمل کرنے ہوں۔
- **گروپ چیٹ آرکسٹریشن** ایسی صورتحال میں جہاں ایجنٹس ایک کام پر مشترکہ طور پر تعاون کر سکتے ہوں۔
- **ہینڈ آف آرکسٹریشن** ایسی صورتحال میں جہاں ذیلی کام مکمل ہونے پر ایجنٹس ایک دوسرے کو کام سونپتے ہیں۔
- **میگنیٹک آرکسٹریشن** ایسی صورتحال جس میں ایک منیجر ایجنٹ ٹاسک لسٹ بناتا اور ترمیم کرتا ہے اور ذیلی ایجنٹس کے ہم آہنگی کا بندوبست کرتا ہے تاکہ کام مکمل ہو سکے۔

پیداوار میں AI ایجنٹس فراہم کرنے کے لیے، MAF میں درج ذیل خصوصیات بھی شامل ہیں:

- **Observability** — OpenTelemetry کے استعمال کے ذریعے جہاں AI ایجنٹ کی ہر کارروائی، بشمول ٹول انوکیشن، آرکسٹریشن کے مراحل، استدلال کے بہاؤ اور Microsoft Foundry ڈیش بورڈز کے ذریعے کارکردگی کی نگرانی شامل ہے۔
- **Security** — ایجنٹس کو Microsoft Foundry پر مقامی طور پر ہوسٹ کر کے جس میں رول-بیسڈ رسائی، نجی ڈیٹا ہینڈلنگ اور بلٹ اِن مواد کی حفاظت جیسے سیکیورٹی کنٹرولز شامل ہیں۔
- **Durability** — ایجنٹ تھریڈز اور ورک فلو کو وقفہ دینے، دوبارہ شروع کرنے اور غلطیوں سے بحال ہونے کی صلاحیت کے طور پر جس سے طویل چلنے والے عمل ممکن ہوتے ہیں۔
- **Control** — انسانی مداخلت والے ورک فلو کی حمایت جہاں ٹاسک کو انسانی منظوری کی ضرورت کے طور پر نشان زد کیا جاتا ہے۔

مائیکروسافٹ ایجنٹ فریم ورک بین الاعملیت (interoperability) پر بھی مرکوز ہے، بشمول:

- **Cloud-agnostic ہونا** - ایجنٹس کنٹینرز میں، آن-پریم اور مختلف کلاؤڈز میں چل سکتے ہیں۔
- **Provider-agnostic ہونا** - ایجنٹس آپ کے پسندیدہ SDK کے ذریعے بنائے جا سکتے ہیں بشمول Azure OpenAI اور OpenAI
- **اوپن اسٹینڈرڈز کا انضمام** - ایجنٹس Agent-to-Agent (A2A) اور Model Context Protocol (MCP) جیسے پروٹوکولز کو استعمال کر کے دوسرے ایجنٹس اور ٹولز کو دریافت اور استعمال کر سکتے ہیں۔
- **پلگ انز اور کنیکٹرز** - کنکشنز ڈیٹا اور میموری سروسز جیسے Microsoft Fabric, SharePoint, Pinecone اور Qdrant سے بنائے جا سکتے ہیں۔

آئیے دیکھتے ہیں کہ یہ خصوصیات مائیکروسافٹ ایجنٹ فریم ورک کے کچھ بنیادی تصورات پر کیسے لاگو ہوتی ہیں۔

## مائیکروسافٹ ایجنٹ فریم ورک کے کلیدی تصورات

### ایجنٹس

![ایجنٹ فریم ورک](../../../translated_images/ur/agent-components.410a06daf87b4fef.webp)

**ایجنٹس بنانا**

ایجنٹ کی تخلیق اس طرح کی جاتی ہے کہ استنتاجی سروس (LLM Provider)، AI ایجنٹ کے اتباع کے لیے ہدایات کا مجموعہ، اور تفویض کردہ `name` کی تعریف کی جائے:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

مذکورہ بالا `Azure OpenAI` استعمال کر رہا ہے لیکن ایجنٹس مختلف سروسز استعمال کرتے ہوئے بنائے جا سکتے ہیں بشمول `Microsoft Foundry Agent Service`:

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

یا A2A پروٹوکول استعمال کرتے ہوئے ریموٹ ایجنٹس:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ایجنٹس چلانا**

ایجنٹس کو غیر-اسٹریمنگ یا اسٹریمنگ جوابات کے لیے `.run` یا `.run_stream` میتھڈز کے ذریعے چلایا جاتا ہے۔

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ہر ایجنٹ رن میں اختیارات بھی ہوسکتے ہیں تاکہ ایسے پیرامیٹرز کو حسبِ ضرورت بنایا جا سکے جیسے ایجنٹ کے ذریعہ استعمال ہونے والا `max_tokens`, وہ `tools` جو ایجنٹ کال کر سکتا ہے، اور یہاں تک کہ خود `model` جو ایجنٹ کے لیے استعمال ہوتا ہے۔

یہ اُن صورتوں میں مفید ہے جہاں مخصوص ماڈلز یا ٹولز ضروری ہوں کسی صارف کے ٹاسک کو مکمل کرنے کے لیے۔

**ٹولز**

ٹولز ایجنٹ کی تعریف کرتے وقت بھی متعین کیے جا سکتے ہیں:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# جب براہِ راست ChatAgent بنایا جائے

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

اور ایجنٹ چلانے کے وقت بھی:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # صرف اس رن کے لیے فراہم کردہ ٹول )
```

**ایجنٹ تھریڈز**

ایجنٹ تھریڈز کو ملٹی ٹرن گفتگوؤں کو سنبھالنے کے لیے استعمال کیا جاتا ہے۔ تھریڈز درج ذیل طریقوں سے بنائے جا سکتے ہیں:

- `get_new_thread()` کا استعمال جو تھریڈ کو وقت کے ساتھ محفوظ کرنے کے قابل بناتا ہے
- ایجنٹ چلانے پر خودکار طریقے سے تھریڈ بنانا اور تھریڈ کو صرف موجودہ رن کے دوران برقرار رکھنا

تھریڈ بنانے کے لیے کوڈ کچھ یوں دکھائی دیتا ہے:

```python
# ایک نیا تھریڈ بنائیں۔
thread = agent.get_new_thread() # ایجنٹ کو تھریڈ کے ساتھ چلائیں۔
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

آپ پھر تھریڈ کو بعد میں استعمال کے لیے محفوظ کرنے کے لیے سیریئلائز کر سکتے ہیں:

```python
# ایک نیا تھریڈ بنائیں۔
thread = agent.get_new_thread() 

# ایجنٹ کو اس تھریڈ کے ساتھ چلائیں۔

response = await agent.run("Hello, how are you?", thread=thread) 

# تھریڈ کو ذخیرہ کرنے کے لیے سیریلائز کریں۔

serialized_thread = await thread.serialize() 

# ذخیرہ سے لوڈ کرنے کے بعد تھریڈ کی حالت کو ڈیسریلائز کریں۔

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ایجنٹ مڈل ویئر**

ایجنٹس صارف کے کام مکمل کرنے کے لیے ٹولز اور LLMs کے ساتھ تعامل کرتے ہیں۔ بعض حالات میں، ہم ان تعاملات کے درمیان کچھ کارروائی انجام دینا یا ان کا سراغ لگانا چاہتے ہیں۔ ایجنٹ مڈل ویئر ہمیں یہ کرنے کے قابل بناتا ہے:

*فنکشن مڈل ویئر*

یہ مڈل ویئر ایجنٹ اور کسی فنکشن/ٹول کے درمیان ایکشن انجام دینے کی اجازت دیتا ہے جو وہ کال کریگا۔ جب آپ فنکشن کال پر لاگنگ کرنا چاہیں تو اس کا استعمال مفید ہوتا ہے۔

ذیل کے کوڈ میں `next` بتاتا ہے کہ اگلا مڈل ویئر کال ہونا چاہیے یا حقیقی فنکشن کو کال کیا جانا چاہیے۔

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # پری پروسیسنگ: فنکشن کے اجرا سے پہلے لاگ کریں
    print(f"[Function] Calling {context.function.name}")

    # اگلے مڈل ویئر یا فنکشن کے اجرا کی طرف جاری رکھیں
    await next(context)

    # پوسٹ پروسیسنگ: فنکشن کے اجرا کے بعد لاگ کریں
    print(f"[Function] {context.function.name} completed")
```

*چیٹ مڈل ویئر*

یہ مڈل ویئر ہمیں ایجنٹ اور LLM کے درمیان درخواستوں کے درمیان کوئی کارروائی انجام دینے یا لاگ کرنے کے قابل بناتا ہے۔

اس میں اہم معلومات شامل ہوتی ہیں جیسے وہ `messages` جو AI سروس کو بھیجے جا رہے ہیں۔

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

جیسا کہ `Agentic Memory` سبق میں بیان کیا گیا، میموری ایجنٹ کو مختلف سیاق و سباق میں کام کرنے کے قابل بنانے کا ایک اہم عنصر ہے۔ MAF مختلف اقسام کی میموری فراہم کرتا ہے:

*ان-میموری اسٹوریج*

یہ وہ میموری ہے جو ایپلیکیشن رن ٹائم کے دوران تھریڈز میں محفوظ ہوتی ہے۔

```python
# ایک نیا تھریڈ بنائیں۔
thread = agent.get_new_thread() # ایجنٹ کو تھریڈ کے ساتھ چلائیں۔
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*مستقل پیغامات*

یہ میموری مختلف سیشنز کے درمیان گفتگو کی تاریخ محفوظ کرنے کے لیے استعمال ہوتی ہے۔ اسے `chat_message_store_factory` کا استعمال کرکے تعریف کیا جاتا ہے:

```python
from agent_framework import ChatMessageStore

# ایک حسبِ ضرورت پیغام اسٹور بنائیں
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*ڈائنامک میموری*

یہ میموری ایجنٹس چلانے سے پہلے سیاق و سباق میں شامل کی جاتی ہے۔ یہ میموری بیرونی سروسز جیسے mem0 میں محفوظ کی جا سکتی ہے:

```python
from agent_framework.mem0 import Mem0Provider

# جدید میموری صلاحیتوں کے لیے Mem0 کا استعمال
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

**ایجنٹ آبزروبیلیٹی**

قابلِ اعتماد اور قابلِ دیکھ بھال ایجنٹک سسٹمز بنانے کے لیے آبزروبیلیٹی ضروری ہے۔ MAF بہتر آبزروبیلیٹی کے لیے ٹریسنگ اور میٹرز فراہم کرنے کے لیے OpenTelemetry کے ساتھ مربوط ہوتا ہے۔

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

MAF ایسے ورک فلو فراہم کرتا ہے جو کسی ٹاسک کو مکمل کرنے کے لیے پہلے سے متعین مراحل ہوتے ہیں اور ان مراحل میں AI ایجنٹس کو اجزاء کے طور پر شامل کیا جاتا ہے۔

ورک فلو مختلف اجزاء پر مشتمل ہوتے ہیں جو بہتر کنٹرول فلو کی اجازت دیتے ہیں۔ ورک فلو **کثیر ایجنٹ آرکسٹریشن** اور **چیک پوائنٹنگ** کو بھی ممکن بناتے ہیں تاکہ ورک فلو اسٹیٹس محفوظ کیے جا سکیں۔

ورک فلو کے بنیادی اجزاء ہیں:

**ایگزیکیوٹرز**

ایگزیکیوٹرز ان پٹ پیغامات وصول کرتے ہیں، اپنے تفویض کردہ کام انجام دیتے ہیں، اور پھر ایک آؤٹ پٹ پیغام پیدا کرتے ہیں۔ یہ ورک فلو کو بڑے ٹاسک کی تکمیل کی سمت آگے بڑھاتا ہے۔ ایگزیکیوٹرز AI ایجنٹ یا کسٹم لاجک ہو سکتے ہیں۔

**ایجز**

ایجز ورک فلو میں پیغامات کے بہاؤ کی تعریف کرنے کے لیے استعمال ہوتے ہیں۔ یہ ہو سکتے ہیں:

*ڈائریکٹ ایجز* - ایگزیکیوٹرز کے درمیان سادہ ایک سے ایک کنیکشنز:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*کنڈیشنل ایجز* - مخصوص شرط پوری ہونے کے بعد فعال ہوتے ہیں۔ مثال کے طور پر، جب ہوٹل کے کمرے دستیاب نہ ہوں، ایک ایگزیکیوٹر دوسرے اختیارات تجویز کر سکتا ہے۔

*سوئچ-کیس ایجز* - متعین شرائط کی بنیاد پر پیغامات کو مختلف ایگزیکیوٹرز کی طرف بھیجتے ہیں۔ مثال کے طور پر، اگر سفر کا صارف ترجیحی رسائی رکھتا ہے تو ان کے ٹاسکس کسی دوسرے ورک فلو کے ذریعے سنبھالے جائیں گے۔

*فین-آؤٹ ایجز* - ایک پیغام کو متعدد ہدفوں کو بھیجیں۔

*فین-ان ایجز* - مختلف ایگزیکیوٹرز سے متعدد پیغامات جمع کریں اور ایک ہدف کو بھیجیں۔

**ایونٹس**

ورک فلو میں بہتر آبزروبیلیٹی فراہم کرنے کے لیے، MAF عملدرآمد کے لیے بلٹ اِن ایونٹس پیش کرتا ہے جن میں شامل ہیں:

- `WorkflowStartedEvent`  - ورک فلو کی عملدرآمد کا آغاز
- `WorkflowOutputEvent` - ورک فلو آؤٹ پٹ پیدا کرتا ہے
- `WorkflowErrorEvent` - ورک فلو کو خرابی پیش آتی ہے
- `ExecutorInvokeEvent`  - ایگزیکیوٹر پراسیسنگ شروع کرتا ہے
- `ExecutorCompleteEvent`  - ایگزیکیوٹر پراسیسنگ ختم کرتا ہے
- `RequestInfoEvent` - ایک درخواست جاری کی جاتی ہے

## ایڈوانسڈ MAF پیٹرنز

اوپر کے حصے مائیکروسافٹ ایجنٹ فریم ورک کے کلیدی تصورات کا احاطہ کرتے ہیں۔ جیسے جیسے آپ مزید پیچیدہ ایجنٹس بنائیں گے، ذیل میں کچھ ایڈوانسڈ پیٹرنز ہیں جن پر غور کیا جا سکتا ہے:

- **مڈل ویئر کمپوزیشن**: متعدد مڈل ویئر ہینڈلرز (لاگنگ، auth، rate-limiting) کو فنکشن اور چیٹ مڈل ویئر استعمال کر کے چین کریں تاکہ ایجنٹ کے رویے پر باریک بین کنٹرول حاصل کیا جا سکے۔
- **ورک فلو چیک پوائنٹنگ**: طویل چلنے والے ایجنٹ پراسیسز کو محفوظ کرنے اور دوبارہ شروع کرنے کے لیے ورک فلو ایونٹس اور سیریئلائزیشن کا استعمال کریں۔
- **ڈائنامک ٹول سلیکشن**: ٹول کی تفصیلات پر RAG کو MAF کے ٹول رجسٹریشن کے ساتھ جوڑیں تاکہ ہر سوال کے لیے صرف متعلقہ ٹولز دکھائے جائیں۔
- **کثیر ایجنٹ ہینڈآف**: مخصوص ایجنٹس کے درمیان ہینڈآف کو منظم کرنے کے لیے ورک فلو ایجز اور کنڈیشنل روٹنگ کا استعمال کریں۔

## کوڈ کے نمونے 

اس ریپوزیٹری میں مائیکروسافٹ ایجنٹ فریم ورک کے کوڈ کے نمونے `xx-python-agent-framework` اور `xx-dotnet-agent-framework` فائلوں کے تحت مل سکتے ہیں۔

## کیا آپ کو مائیکروسافٹ ایجنٹ فریم ورک کے بارے میں مزید سوالات ہیں؟

دیگر سیکھنے والوں سے ملنے، آفس آور میں شرکت کرنے اور اپنے AI ایجنٹس کے سوالات کے جواب حاصل کرنے کے لیے [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) میں شامل ہوں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
دستبرداری:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہِ کرم نوٹ کریں کہ خودکار تراجم میں غلطیاں یا عدمِ درستی ہو سکتی ہے۔ اصل دستاویز کو اس کی مادری زبان میں مستند ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تعبیر کے لیے ہم ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->