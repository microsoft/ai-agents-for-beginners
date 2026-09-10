# کاوش در چارچوب مامور مایکروسافت

![Agent Framework](../../../translated_images/fa/lesson-14-thumbnail.90df0065b9d234ee.webp)

### مقدمه

این درس موارد زیر را پوشش خواهد داد:

- درک چارچوب مامور مایکروسافت: ویژگی‌های کلیدی و ارزش  
- کاوش در مفاهیم کلیدی چارچوب مامور مایکروسافت
- الگوهای پیشرفته MAF: جریان‌های کاری، میان‌افزار و حافظه

## اهداف یادگیری

پس از پایان این درس، شما خواهید دانست چگونه:

- ساخت ماموران هوش مصنوعی آماده تولید با استفاده از چارچوب مامور مایکروسافت
- اعمال ویژگی‌های اصلی چارچوب مامور مایکروسافت در موارد استفاده ماموری شما
- استفاده از الگوهای پیشرفته شامل جریان‌های کاری، میان‌افزار و قابلیت مشاهده

## نمونه‌های کد

نمونه‌های کد برای [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) در این مخزن، زیر فایل‌های `xx-python-agent-framework` و `xx-dotnet-agent-framework` یافت می‌شوند.

## درک چارچوب مامور مایکروسافت

![Framework Intro](../../../translated_images/fa/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) چارچوب متحد مایکروسافت برای ساخت ماموران هوش مصنوعی است. این چارچوب انعطاف‌پذیری لازم برای پاسخ به انواع مختلف موارد استفاده ماموری را که در هر دو محیط تولید و تحقیق دیده می‌شوند ارائه می‌دهد از جمله:

- **ارکستراسیون توالی مامور** در سناریوهایی که به جریان‌های کاری گام به گام نیاز است.
- **ارکستراسیون همزمان** در سناریوهایی که مامورها باید وظایف را به‌طور همزمان انجام دهند.
- **ارکستراسیون گفتگوی گروهی** در سناریوهایی که مامورها می‌توانند روی یک وظیفه با هم همکاری کنند.
- **ارکستراسیون تحویل** در سناریوهایی که مامورها وظایف را به یکدیگر تحویل می‌دهند با اتمام زیروظایف.
- **ارکستراسیون مغناطیسی** در سناریوهایی که یک مامور مدیر فهرست وظایف را ایجاد و اصلاح می‌کند و هماهنگی زیرماموران برای اتمام وظیفه را بر عهده دارد.

برای ارائه ماموران هوش مصنوعی در تولید، MAF همچنین ویژگی‌هایی برای:

- **قابلیت مشاهده** از طریق استفاده از OpenTelemetry که هر اقدام مامور هوش مصنوعی را شامل فراخوانی ابزار، مراحل ارکستراسیون، جریان‌های استدلال و نظارت بر عملکرد از طریق داشبوردهای Microsoft Foundry ثبت می‌کند.
- **امنیت** با میزبانی بومی مامورها در Microsoft Foundry که شامل کنترل‌های امنیتی مانند دسترسی بر اساس نقش، مدیریت داده‌های خصوصی و امنیت محتوای ساخته شده است.
- **دوام** به این صورت که رشته‌ها و جریان‌های کاری مامور می‌توانند متوقف، از سر گرفته و از خطاها بازیابی شوند که امکان اجرای فرآیندهای طولانی‌تر را فراهم می‌کند.
- **کنترل** به عنوان جریان‌های کاری انسان در حلقه پشتیبانی می‌شوند که در آن وظایف به عنوان نیازمند تأیید انسانی علامت‌گذاری می‌شوند.

چارچوب مامور مایکروسافت همچنین بر قابلیت همکاری متمرکز است از طریق:

- **بی‌طرفی در برابر ابر** - مامورها می‌توانند در کانتینرها، در محل و در چندین ابر مختلف اجرا شوند.
- **بی‌طرفی در برابر ارائه‌دهنده** - مامورها می‌توانند از طریق SDK مورد علاقه شما از جمله Azure OpenAI و OpenAI ایجاد شوند.
- **ادغام استانداردهای باز** - مامورها می‌توانند از پروتکل‌هایی مانند Agent-to-Agent (A2A) و Model Context Protocol (MCP) برای کشف و استفاده از سایر مامورها و ابزارها بهره ببرند.
- **افزونه‌ها و کانکتورها** - اتصال به خدمات داده و حافظه مانند Microsoft Fabric، SharePoint، Pinecone و Qdrant امکان‌پذیر است.

بیایید ببینیم چگونه این ویژگی‌ها در برخی از مفاهیم کلیدی چارچوب مامور مایکروسافت به کار گرفته شده‌اند.

## مفاهیم کلیدی چارچوب مامور مایکروسافت

### مامورها

![Agent Framework](../../../translated_images/fa/agent-components.410a06daf87b4fef.webp)


**ایجاد نمایندگان**

ایجاد نماینده با تعریف سرویس استنتاج (ارائه‌دهنده LLM)، مجموعه‌ای از دستورالعمل‌ها برای دنبال کردن توسط نماینده هوش مصنوعی و انتساب یک `نام` انجام می‌شود:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

مثال بالا از `Azure OpenAI` استفاده می‌کند اما نمایندگان را می‌توان با استفاده از انواع سرویس‌ها از جمله `Microsoft Foundry Agent Service` ایجاد کرد:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

APIهای OpenAI `Responses`، `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

یا [MiniMax](https://platform.minimaxi.com/) که API سازگار با OpenAI با پنجره‌های متن بزرگ (تا ۲۰۴ هزار توکن) فراهم می‌کند:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

یا نمایندگان راه دور با استفاده از پروتکل A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**اجرای نمایندگان**

نمایندگان با استفاده از متدهای `.run` یا `.run_stream` برای پاسخ‌های غیرجریان یا جریان اجرا می‌شوند.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

هر اجرای نماینده همچنین می‌تواند گزینه‌هایی برای سفارشی کردن پارامترهایی مانند `max_tokens` استفاده شده توسط نماینده، `tools`هایی که نماینده قادر به فراخوانی آن‌ها است، و حتی خود `model` مورد استفاده برای نماینده داشته باشد.

این در مواردی مفید است که مدل‌ها یا ابزارهای خاصی برای تکمیل وظیفه کاربران لازم باشد.

**ابزارها**

ابزارها می‌توانند هم هنگام تعریف نماینده تعیین شوند:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# هنگام ایجاد مستقیم یک ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

و همچنین هنگام اجرای نماینده:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ابزاری که فقط برای این اجرا ارائه شده است )
```

**رشته‌های نماینده**

رشته‌های نماینده برای مدیریت گفتگوهای چند مرحله‌ای استفاده می‌شوند. رشته‌ها می‌توانند به یکی از دو روش ایجاد شوند:

- استفاده از `get_new_thread()` که امکان ذخیره رشته در طول زمان را فراهم می‌کند
- ایجاد خودکار یک رشته هنگام اجرای نماینده که تنها در طول اجرای جاری زنده می‌ماند.

برای ایجاد یک رشته، کد به این شکل است:

```python
# ایجاد یک رشته جدید.
thread = agent.get_new_thread() # اجرای عامل با رشته.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

سپس می‌توانید رشته را سریال کنید تا بعداً ذخیره شود:

```python
# ایجاد یک نخ جدید.
thread = agent.get_new_thread() 

# اجرای نماینده با نخ.

response = await agent.run("Hello, how are you?", thread=thread) 

# سریال‌سازی نخ برای ذخیره‌سازی.

serialized_thread = await thread.serialize() 

# دی‌سریال‌سازی وضعیت نخ پس از بارگذاری از ذخیره‌سازی.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**واسط نماینده**

نمایندگان برای تکمیل وظایف کاربر با ابزارها و LLMها تعامل دارند. در برخی سناریوها، می‌خواهیم بین این تعاملات اجرا یا پیگیری انجام دهیم. واسط نماینده این امکان را فراهم می‌کند از طریق:

*واسط توابع*

این واسط اجازه می‌دهد عملی بین نماینده و تابع/ابزاری که فراخوانی می‌کند، اجرا شود. مثالی که کاربرد دارد، ثبت وقایع (Logging) بر روی فراخوانی تابع است.

در کد زیر `next` تعیین می‌کند که آیا باید واسط بعدی اجرا شود یا خود تابع اصلی فراخوانی شود.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # پیش‌پردازش: ثبت لاگ قبل از اجرای تابع
    print(f"[Function] Calling {context.function.name}")

    # ادامه به میان‌افزار بعدی یا اجرای تابع
    await next(context)

    # پس‌پردازش: ثبت لاگ پس از اجرای تابع
    print(f"[Function] {context.function.name} completed")
```

*واسط چت*

این واسط اجازه می‌دهد عملی بین نماینده و درخواست‌های بین LLM اجرا یا ثبت شود.

این شامل اطلاعات مهمی مانند `messages` است که به سرویس هوش مصنوعی ارسال می‌شوند.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # پیش‌پردازش: ثبت لاگ قبل از فراخوانی هوش مصنوعی
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # ادامه به میان‌افزار یا سرویس هوش مصنوعی بعدی
    await next(context)

    # پس‌پردازش: ثبت لاگ پس از پاسخ هوش مصنوعی
    print("[Chat] AI response received")

```

**حافظه نماینده**

همان‌طور که در درس `Agentic Memory` گفته شد، حافظه عنصر مهمی برای امکان کارکرد نماینده در زمینه‌های مختلف است. MAF چندین نوع حافظه متفاوت ارائه می‌دهد:

*ذخیره‌سازی در حافظه*

این حافظه در رشته‌ها در طول زمان اجرای برنامه ذخیره می‌شود.

```python
# ایجاد یک رشته جدید.
thread = agent.get_new_thread() # اجرای عامل با استفاده از رشته.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*پیام‌های پایدار*

این حافظه برای ذخیره تاریخچه مکالمه در جلسات مختلف استفاده می‌شود. با استفاده از `chat_message_store_factory` تعریف می‌شود:

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


این حافظه قبل از اجرای عامل‌ها به متن اضافه می‌شود. این حافظه‌ها می‌توانند در سرویس‌های خارجی مانند mem0 ذخیره شوند:

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

قابلیت مشاهده برای ساخت سیستم‌های عامل قابل اعتماد و قابل نگهداری اهمیت دارد. MAF با OpenTelemetry ادغام می‌شود تا ردیابی و معیارهایی برای مشاهده بهتر فراهم کند.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # کاری انجام بده
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### جریان‌های کاری

MAF جریان‌های کاری را ارائه می‌دهد که گام‌های از پیش تعریف‌شده‌ای برای تکمیل یک وظیفه هستند و عامل‌های هوش مصنوعی را به عنوان اجزا در آن گام‌ها شامل می‌شوند.

جریان‌های کاری از اجزای متفاوتی تشکیل شده‌اند که امکان کنترل بهتر جریان را می‌دهند. جریان‌های کاری همچنین **هماهنگی چندعامله** و **checkpointing** برای ذخیره وضعیت جریان کاری را فعال می‌کنند.

اجزای اصلی یک جریان کاری عبارت‌اند از:

**اجراکننده‌ها**

اجراکننده‌ها پیام‌های ورودی را دریافت می‌کنند، وظایف محوله‌شده خود را انجام می‌دهند، و سپس پیام خروجی تولید می‌کنند. این باعث پیشرفت جریان کاری به سمت تکمیل وظیفه بزرگ‌تر می‌شود. اجراکننده‌ها می‌توانند عامل هوش مصنوعی یا منطق سفارشی باشند.

**لبه‌ها**

از لبه‌ها برای تعریف جریان پیام‌ها در یک جریان کاری استفاده می‌شود. این‌ها می‌توانند:

*لبه‌های مستقیم* - اتصالات ساده یک‌به‌یک بین اجراکننده‌ها:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*لبه‌های شرطی* - بعد از برآورده شدن شرط خاصی فعال می‌شوند. به عنوان مثال، وقتی که اتاق‌های هتل در دسترس نیستند، یک اجراکننده می‌تواند گزینه‌های دیگر را پیشنهاد دهد.

*لبه‌های سوئیچ-کیس* - پیام‌ها را بر اساس شرایط تعریف‌شده به اجراکننده‌های مختلف مسیریابی می‌کنند. برای مثال، اگر مشتری سفر دسترسی اولویت داشته باشد، وظایفش از طریق جریان کاری دیگری مدیریت می‌شوند.

*لبه‌های انشعاب* - ارسال یک پیام به چندین مقصد.

*لبه‌های جمع‌آوری* - جمع‌آوری چندین پیام از اجراکننده‌های مختلف و ارسال به یک مقصد.

**رویدادها**

برای ارائه قابلیت مشاهده بهتر در جریان‌های کاری، MAF رویدادهای ساخته‌شده برای اجرا را ارائه می‌دهد که شامل:

- `WorkflowStartedEvent` - اجرای جریان کاری آغاز می‌شود
- `WorkflowOutputEvent` - جریان کاری خروجی تولید می‌کند
- `WorkflowErrorEvent` - خطایی در جریان کاری رخ می‌دهد
- `ExecutorInvokeEvent` - اجراکننده شروع به پردازش می‌کند
- `ExecutorCompleteEvent` - اجراکننده پردازش را پایان می‌دهد
- `RequestInfoEvent` - یک درخواست صادر می‌شود

## الگوهای پیشرفته MAF

بخش‌های بالا مفاهیم کلیدی چارچوب عامل مایکروسافت را پوشش می‌دهند. هنگام ساخت عامل‌های پیچیده‌تر، اینجا برخی الگوهای پیشرفته برای در نظر گرفتن وجود دارد:

- **ترکیب میان‌افزار**: زنجیره‌ای از چندین دستگیره میان‌افزار (ثبت، احراز هویت، محدودیت نرخ) را با استفاده از میان‌افزار تابعی و چت برای کنترل دقیق رفتار عامل پیاده‌سازی کنید.
- **checkpointing جریان کاری**: از رویدادهای جریان کاری و سریال‌سازی برای ذخیره و ادامه فرآیندهای عامل طولانی‌مدت استفاده کنید.
- **انتخاب ابزار پویا**: ترکیب RAG بر روی توصیف ابزارها با ثبت ابزار MAF برای ارائه فقط ابزارهای مرتبط در هر پرسش.
- **تحویل چندعامله**: از لبه‌های جریان کاری و مسیریابی شرطی برای هماهنگ‌کردن تحویل بین عامل‌های تخصصی استفاده کنید.

## میزبانی عامل‌های LangChain / LangGraph روی Microsoft Foundry

چارچوب عامل مایکروسافت **قابلیت همکاری با چارچوب‌های دیگر** را دارد — محدود به عامل‌های نوشته‌شده با MAF نیستید. اگر قبلاً عاملی با **LangChain** یا **LangGraph** ساخته‌اید، می‌توانید آن را به عنوان **عامل میزبانی شده مایکروسافت Foundry** اجرا کنید تا Foundry مدیریت زمان اجرا، جلسات، مقیاس‌بندی، هویت و نقاط پایانی پروتکل را بر عهده بگیرد، در حالی که منطق عامل شما در LangGraph باقی می‌ماند.

این کار با بسته `langchain_azure_ai.agents.hosting` انجام می‌شود که یک گراف کامپایل‌شده LangGraph را از طریق همان پروتکل‌هایی که عوامل میزبانی شده Foundry استفاده می‌کنند، در دسترس قرار می‌دهد.

**1. افزودن ماژول میزبانی:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

ماژول `hosting` کتابخانه‌های پروتکل Foundry را نصب می‌کند: `azure-ai-agentserver-responses` (نقطه پایانی `/responses` سازگار با OpenAI) و `azure-ai-agentserver-invocations` (نقطه پایانی عمومی `/invocations`).

**2. انتخاب پروتکل میزبانی:**

| پروتکل | کلاس میزبان | نقطه پایانی | استفاده زمانی که |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | می‌خواهید چت، پخش، تاریخچه پاسخ، و رشته مکالمات سازگار با OpenAI داشته باشید — پیش‌فرض توصیه‌شده برای عامل‌های مکالمه‌ای. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | به شکل JSON سفارشی، نقطه پایانی به سبک وب‌هوک، یا پردازش غیرمکالمه‌ای نیاز دارید. |

چون **API Responses، API اصلی برای توسعه عوامل سبک-Agent در Foundry است**، برای اکثر عامل‌ها با `ResponsesHostServer` شروع کنید.

**3. پیکربندی متغیرهای محیطی** (`az login` ابتدا برای احراز هویت `DefaultAzureCredential`):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

وقتی عامل بعداً به عنوان عامل میزبانی شده در Foundry اجرا می‌شود، پلتفرم به‌طور خودکار `FOUNDRY_PROJECT_ENDPOINT` را تزریق می‌کند.

**4. عرضه عامل LangGraph از طریق پروتکل Responses:**

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

    # اینجا ChatOpenAI به نقطه پایانی سازگار با OpenAI پروژه Foundry (Responses) هدف‌گذاری می‌کند.
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

آن را به صورت محلی با `python main.py` اجرا کنید، سپس یک درخواست Responses به `http://localhost:8088/responses` ارسال کنید.

**رفتارهای کلیدی:**

- **مکالمات**: کلاینت‌ها با ارسال `previous_response_id` یا شناسه `conversation` مکالمه را ادامه می‌دهند. اگر گراف شما با checkpointer LangGraph کامپایل شده باشد، Foundry وضعیت مکالمه را به checkpoint کلید می‌کند (از checkpointer پایدار در محیط تولید استفاده کنید؛ `MemorySaver` برای تست محلی مناسب است).
- **انسان در حلقه**: اگر گراف شما از `interrupt()` LangGraph استفاده کند، `ResponsesHostServer` وقفه در انتظار را به صورت یک آیتم `function_call` یا `mcp_approval_request` در Responses نشان می‌دهد و کلاینت‌ها با `function_call_output` یا `mcp_approval_response` مطابقت‌دار ادامه می‌دهند.
- **استقرار در Foundry**: از Azure Developer CLI استفاده کنید — `azd ext install azure.ai.agents`، `azd ai agent init -m <manifest>`، `azd ai agent run` (به صورت محلی، نیازمند Docker)، سپس `azd provision` و `azd deploy`. مستقرسازی عوامل میزبانی شده نیازمند نقش **Foundry Project Manager** است.

نسخه قابل اجرا از این مثال در [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) موجود است. برای راهنمای کامل (پروتکل Invocations، قالب‌های سفارشی درخواست، و رفع اشکال)، به [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) مراجعه کنید.

## نمونه‌های کد

نمونه‌های کد برای چارچوب عامل مایکروسافت را می‌توان در این مخزن زیر فایل‌های `xx-python-agent-framework` و `xx-dotnet-agent-framework` یافت.

## سوالات بیشتری درباره چارچوب عامل مایکروسافت دارید؟

به [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) بپیوندید تا با سایر یادگیرندگان ملاقات کنید، در ساعت‌های مشاوره شرکت کنید و سوالات خود درباره عامل‌های هوش مصنوعی را مطرح کنید.
## درس قبلی

[حافظه برای عامل‌های هوش مصنوعی](../13-agent-memory/README.md)

## درس بعدی


[ساخت مأموران استفاده از رایانه (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->