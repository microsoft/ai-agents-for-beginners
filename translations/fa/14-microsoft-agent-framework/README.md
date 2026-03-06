# کاوش در Microsoft Agent Framework

![چارچوب عامل](../../../translated_images/fa/lesson-14-thumbnail.90df0065b9d234ee.webp)

### مقدمه

این درس شامل موارد زیر است:

- فهم Microsoft Agent Framework: ویژگی‌های کلیدی و ارزش  
- کاوش در مفاهیم کلیدی Microsoft Agent Framework  
- الگوهای پیشرفته MAF: جریان‌های کاری، میان‌افزار و حافظه

## اهداف یادگیری

پس از تکمیل این درس، شما خواهید دانست چگونه:

- ساخت عامل‌های هوش مصنوعی آماده تولید با استفاده از Microsoft Agent Framework  
- اعمال ویژگی‌های اصلی Microsoft Agent Framework در موارد استفاده عاملی خود  
- استفاده از الگوهای پیشرفته شامل جریان‌های کاری، میان‌افزار و قابلیت مشاهده

## نمونه کدها

نمونه کدهای مربوط به [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) را می‌توان در این مخزن در فایل‌های `xx-python-agent-framework` و `xx-dotnet-agent-framework` یافت.

## درک Microsoft Agent Framework

![معرفی چارچوب](../../../translated_images/fa/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) چارچوب یکپارچه مایکروسافت برای ساخت عامل‌های هوش مصنوعی است. این چارچوب انعطاف‌پذیری لازم را برای پاسخ به انواع مختلف موارد استفاده عاملی که در محیط‌های تولید و تحقیق مشاهده می‌شوند ارائه می‌دهد که شامل موارد زیر است:

- **سازماندهی ترتیبی عامل‌ها** در سناریوهایی که جریان‌های کاری گام به گام نیاز است.  
- **سازماندهی همزمان** در حالتی که عامل‌ها باید هم‌زمان کارها را انجام دهند.  
- **سازماندهی گروهی گفتگو** در سناریوهایی که عامل‌ها می‌توانند به صورت گروهی روی یک کار همکاری کنند.  
- **سازماندهی انتقال کار** در سناریوهایی که عامل‌ها هنگام تکمیل زیرکار‌ها کار را به یکدیگر منتقل می‌کنند.  
- **سازماندهی مغناطیسی** در سناریوهایی که یک عامل مدیر فهرست کاری ایجاد و ویرایش می‌کند و هماهنگی زیرعامل‌ها برای تکمیل کار را به عهده دارد.  

برای ارائه عامل‌های هوش مصنوعی در تولید، MAF همچنین ویژگی‌هایی برای موارد زیر دارد:

- **قابلیت مشاهده** از طریق استفاده از OpenTelemetry که هر عمل عامل هوش مصنوعی شامل فراخوانی ابزار، گام‌های سازماندهی، جریان‌های استدلال و نظارت بر عملکرد از طریق داشبوردهای Microsoft Foundry را شامل می‌شود.  
- **امنیت** با میزبانی بومی عامل‌ها روی Microsoft Foundry که شامل کنترل‌های امنیتی مانند دسترسی مبتنی بر نقش، مدیریت داده‌های خصوصی و ایمنی محتوای داخلی است.  
- **پایداری** زیرا رشته‌ها و جریان‌های کاری عامل می‌توانند متوقف، از سر گرفته و از خطاها بازیابی شوند که این امکان اجرای فرآیندهای طولانی‌تر را فراهم می‌کند.  
- **کنترل** زیرا جریان‌های کاری انسان در حلقه پشتیبانی می‌شوند که در آن کارها به عنوان نیازمند تایید انسانی علامت‌گذاری می‌شوند.  

Microsoft Agent Framework همچنین تمرکز زیادی بر وابستگی‌ناپذیری دارد از جمله:

- **وابستگی نداشتن به کلود خاص** - عامل‌ها می‌توانند در کانتینرها، محیط‌های محلی و در چندین کلود مختلف اجرا شوند.  
- **وابستگی نداشتن به ارائه‌دهنده خاص** - عامل‌ها می‌توانند از طریق SDK دلخواه شما از جمله Azure OpenAI و OpenAI ایجاد شوند.  
- **یکپارچگی با استانداردهای باز** - عامل‌ها می‌توانند از پروتکل‌هایی مانند Agent-to-Agent (A2A) و Model Context Protocol (MCP) برای کشف و استفاده از دیگر عامل‌ها و ابزارها بهره ببرند.  
- **افزونه‌ها و اتصال‌دهنده‌ها** - می‌توان به سرویس‌های داده و حافظه مانند Microsoft Fabric، SharePoint، Pinecone و Qdrant متصل شد.  

بیایید ببینیم چگونه این ویژگی‌ها در برخی مفاهیم اصلی Microsoft Agent Framework به کار گرفته شده‌اند.

## مفاهیم کلیدی Microsoft Agent Framework

### عامل‌ها

![چارچوب عامل](../../../translated_images/fa/agent-components.410a06daf87b4fef.webp)

**ایجاد عامل‌ها**

ایجاد عامل با تعریف سرویس استنتاج (تأمین‌کننده LLM)، مجموعه‌ای از دستورالعمل‌ها برای دنبال کردن توسط عامل هوش مصنوعی و تعیین `name` انجام می‌شود:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```
  
کد فوق از `Azure OpenAI` استفاده می‌کند اما عامل‌ها می‌توانند با استفاده از خدمات متنوعی از جمله `Microsoft Foundry Agent Service` ایجاد شوند:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```
  
OpenAI `Responses`، `ChatCompletion` APIها

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```
  
```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```
  
یا عامل‌های راه دور با استفاده از پروتکل A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```
  
**اجرای عامل‌ها**

عامل‌ها با استفاده از متدهای `.run` یا `.run_stream` برای پاسخ‌های غیرجریان یا جریان اجرا می‌شوند.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```
  
```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```
  
هر اجرای عامل همچنین می‌تواند گزینه‌هایی برای سفارشی‌سازی پارامترها مانند `max_tokens` مصرفی توسط عامل، `tools` که عامل قادر به فراخوانی آنها است، و حتی خود `model` استفاده شده توسط عامل داشته باشد.

این در مواردی مفید است که مدل‌ها یا ابزارهای خاصی برای انجام کار کاربر لازم است.

**ابزارها**

ابزارها می‌توانند هنگام تعریف عامل مشخص شوند:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# هنگام ایجاد مستقیم یک ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```
  
و همچنین هنگام اجرای عامل:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ابزار ارائه شده فقط برای این اجرا )
```
  
**رشته‌های عامل**

رشته‌های عامل برای مدیریت مکالمات چند مرحله‌ای استفاده می‌شوند. رشته‌ها می‌توانند به دو روش ایجاد شوند:

- استفاده از `get_new_thread()` که امکان ذخیره شدن رشته را در طول زمان فراهم می‌آورد  
- ایجاد خودکار یک رشته هنگام اجرای عامل که فقط در طول همان اجرای فعلی باقی می‌ماند  

برای ایجاد یک رشته، کد به این شکل است:

```python
# ایجاد یک رشته جدید.
thread = agent.get_new_thread() # اجرای عامل با استفاده از رشته.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```
  
شما می‌توانید سپس رشته را سریالیزه کنید تا برای استفاده بعدی ذخیره شود:

```python
# یک رشته جدید بسازید.
thread = agent.get_new_thread() 

# عامل را با رشته اجرا کنید.

response = await agent.run("Hello, how are you?", thread=thread) 

# رشته را برای ذخیره‌سازی سریالی کنید.

serialized_thread = await thread.serialize() 

# حالت رشته را پس از بارگذاری از ذخیره‌سازی سریالی کنید.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```
  
**میان‌افزار عامل**

عامل‌ها با ابزارها و LLM‌ها تعامل دارند تا کارهای کاربر را انجام دهند. در برخی سناریوها، می‌خواهیم بین این تعاملات اجرا یا ردیابی انجام دهیم. میان‌افزار عامل این امکان را فراهم می‌کند از طریق:

*میان‌افزار عملکرد*

این میان‌افزار به ما اجازه می‌دهد بین عامل و یک تابع/ابزار که عامل فراخوانی می‌کند عملی را اجرا کنیم. نمونه استفاده می‌تواند هنگام لاگ‌گیری فراخوانی تابع باشد.

در کد زیر، `next` تعیین می‌کند که میان‌افزار بعدی یا تابع واقعی باید فراخوانی شود.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # پیش‌پردازش: لاگ قبل از اجرای تابع
    print(f"[Function] Calling {context.function.name}")

    # ادامه به میدل‌ور بعدی یا اجرای تابع
    await next(context)

    # پس‌پردازش: لاگ بعد از اجرای تابع
    print(f"[Function] {context.function.name} completed")
```
  
*میان‌افزار گفتگو*

این میان‌افزار به ما امکان می‌دهد عملی را بین عامل و درخواست‌ها به LLM اجرا یا لاگ کنیم.

این شامل اطلاعات مهمی مانند `messages` است که به سرویس هوش مصنوعی ارسال می‌شوند.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # پیش‌پردازش: ثبت لاگ قبل از فراخوانی هوش مصنوعی
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # ادامه به میان‌افزار بعدی یا سرویس هوش مصنوعی
    await next(context)

    # پس‌پردازش: ثبت لاگ بعد از پاسخ هوش مصنوعی
    print("[Chat] AI response received")

```
  
**حافظه عامل**

همان‌طور که در درس `Agentic Memory` اشاره شد، حافظه عنصر مهمی در فعال کردن عامل برای عمل در زمینه‌های مختلف است. MAF چند نوع حافظه مختلف ارائه می‌دهد:

*حافظه درون برنامه‌ای*

این حافظه در طول اجرای برنامه در رشته‌ها ذخیره می‌شود.

```python
# ایجاد یک رشته جدید.
thread = agent.get_new_thread() # اجرای عامل با رشته.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```
  
*پیام‌های پایدار*

این حافظه هنگام ذخیره تاریخچه گفتگو در جلسات مختلف استفاده می‌شود. این حافظه با استفاده از `chat_message_store_factory` تعریف می‌شود:

```python
from agent_framework import ChatMessageStore

# ایجاد یک فروشگاه پیام سفارشی
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```
  
*حافظه پویا*

این حافظه قبل از اجرای عامل‌ها به زمینه اضافه می‌شود. این حافظه‌ها می‌توانند در سرویس‌های خارجی مانند mem0 ذخیره شوند:

```python
from agent_framework.mem0 import Mem0Provider

# استفاده از Mem0 برای قابلیت‌های پیشرفته حافظه
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
  
**قابلیت مشاهده عامل**

قابلیت مشاهده برای ساخت سیستم‌های عاملی قابل اعتماد و قابل نگهداری اهمیت دارد. MAF با OpenTelemetry ادغام شده است تا ردیابی و شمارنده‌هایی برای مشاهده بهتر فراهم کند.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # انجام کاری
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```
  
### جریان‌های کاری

MAF جریان‌های کاری ارائه می‌دهد که مراحل از پیش تعریف شده برای تکمیل یک کار هستند و عامل‌های هوش مصنوعی را به عنوان اجزایی در آن مراحل شامل می‌شوند.

جریان‌های کاری از اجزای مختلفی تشکیل شده‌اند که امکان کنترل بهتر جریان را فراهم می‌کنند. جریان‌های کاری همچنین امکان **سازماندهی چندعاملی** و **ایجاد نقطه بازگشت** برای ذخیره وضعیت جریان کاری را فراهم می‌آورند.

اجزای کلیدی جریان کاری عبارتند از:

**اجراآکنندگان**

اجراآکنندگان پیام‌های ورودی را دریافت می‌کنند، وظایف خود را انجام می‌دهند و سپس پیام خروجی تولید می‌کنند. این پیام جریان کاری را به سمت تکمیل وظیفه بزرگ‌تر پیش می‌برد. اجراآکنندگان می‌توانند عامل هوش مصنوعی یا منطق سفارشی باشند.

**لبه‌ها**

لبه‌ها برای تعریف جریان پیام‌ها در یک جریان کاری استفاده می‌شوند. این لبه‌ها می‌توانند شامل موارد زیر باشند:

*لبه‌های مستقیم* - اتصال ساده یک به یک بین اجراآکنندگان:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```
  
*لبه‌های شرطی* - زمانی فعال می‌شوند که شرط خاصی برآورده شود. به عنوان مثال، زمانی که اتاق‌های هتل در دسترس نیستند، یک اجراآکننده می‌تواند گزینه‌های دیگر را پیشنهاد دهد.

*لبه‌های حالت-سوئیچ* - پیام‌ها را بر اساس شرایط تعریف شده به اجراآکنندگان مختلف هدایت می‌کنند. به عنوان مثال، اگر مشتری سفر دارای دسترسی اولویت‌دار باشد و وظایف او از طریق جریان کاری دیگری مدیریت شود.

*لبه‌های پخش-خروجی* - یک پیام را به چندین مقصد ارسال می‌کنند.

*لبه‌های جمع-ورودی* - پیام‌های متعدد از اجراآکنندگان مختلف جمع‌آوری کرده و به یک مقصد ارسال می‌کنند.

**رویدادها**

برای فراهم آوردن قابلیت مشاهده بهتر در جریان‌های کاری، MAF رویدادهای توکار برای اجرای جریان کاری ارائه می‌دهد که شامل موارد زیر است:

- `WorkflowStartedEvent` - اجرای جریان کاری آغاز می‌شود  
- `WorkflowOutputEvent` - جریان کاری خروجی تولید می‌کند  
- `WorkflowErrorEvent` - جریان کاری با خطا مواجه می‌شود  
- `ExecutorInvokeEvent` - اجراآکننده شروع به پردازش می‌کند  
- `ExecutorCompleteEvent` - اجراآکننده پردازش را به پایان می‌رساند  
- `RequestInfoEvent` - یک درخواست صادر می‌شود  

## الگوهای پیشرفته MAF

بخش‌های بالا مفاهیم کلیدی Microsoft Agent Framework را پوشش می‌دهند. هنگامی که عامل‌های پیچیده‌تری می‌سازید، در نظر گرفتن الگوهای پیشرفته زیر کمک کننده است:

- **ترکیب میان‌افزار**: زنجیره کردن چندین میان‌افزار (لاگ‌گیری، احراز هویت، محدودیت نرخ) با استفاده از میان‌افزار عملکرد و گفتگو برای کنترل دقیق رفتار عامل.  
- **نقطه بازگشت جریان کاری**: استفاده از رویدادها و سریالی سازی جریان کاری برای ذخیره و از سرگیری فرآیندهای طولانی عامل.  
- **انتخاب پویا ابزار**: ترکیب RAG بر اساس توصیفات ابزار با ثبت ابزار MAF برای ارائه فقط ابزارهای مرتبط با هر پرس‌وجو.  
- **انتقال چندعاملی**: استفاده از لبه‌های جریان کاری و هدایت شرطی برای سازماندهی انتقال کار بین عامل‌های تخصصی.  

## نمونه کدها

نمونه کدهای Microsoft Agent Framework را می‌توان در این مخزن در فایل‌های `xx-python-agent-framework` و `xx-dotnet-agent-framework` یافت.

## سوالات بیشتری درباره Microsoft Agent Framework دارید؟

به [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) بپیوندید تا با دیگر یادگیرندگان ملاقات کنید، در ساعات اداری شرکت کنید و سوالات خود درباره عامل‌های هوش مصنوعی را مطرح کنید.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه خودکار [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نواقص باشند. سند اصلی به زبان بومی خود باید به‌عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هرگونه سوء تفاهم یا تفسیر نادرست ناشی از استفاده این ترجمه نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->