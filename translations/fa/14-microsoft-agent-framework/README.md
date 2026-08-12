# بررسی چارچوب Microsoft Agent

![Agent Framework](../../../translated_images/fa/lesson-14-thumbnail.90df0065b9d234ee.webp)

### معرفی

این درس شامل موارد زیر است:

- درک چارچوب Microsoft Agent: ویژگی‌های کلیدی و ارزش  
- بررسی مفاهیم کلیدی چارچوب Microsoft Agent
- الگوهای پیشرفته MAF: جریان‌های کاری، میان‌افزار و حافظه

## اهداف یادگیری

پس از اتمام این درس، شما خواهید دانست چگونه:

- ساخت عوامل هوش مصنوعی آماده برای تولید با استفاده از چارچوب Microsoft Agent
- به‌کارگیری ویژگی‌های اصلی چارچوب Microsoft Agent برای موارد استفاده عاملی خود
- استفاده از الگوهای پیشرفته شامل جریان‌های کاری، میان‌افزار و قابلیت مشاهده

## نمونه‌های کد 

نمونه‌های کد برای [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) در این مخزن زیر فایل‌های `xx-python-agent-framework` و `xx-dotnet-agent-framework` قرار دارند.

## درک چارچوب Microsoft Agent

![Framework Intro](../../../translated_images/fa/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) چارچوب متحد مایکروسافت برای ساخت عوامل هوش مصنوعی است. این چارچوب انعطاف‌پذیری لازم برای رسیدگی به انواع گسترده موارد استفاده عاملی را در محیط‌های تولید و پژوهشی از جمله موارد زیر ارائه می‌دهد:

- **هماهنگی عوامل توالی‌وار** در سناریوهایی که جریان‌های کاری مرحله به مرحله لازم است.
- **هماهنگی همزمان** در سناریوهایی که عوامل باید وظایف را به صورت همزمان کامل کنند.
- **هماهنگی چت گروهی** در سناریوهایی که عوامل می‌توانند با هم برای یک وظیفه همکاری کنند.
- **هماهنگی انتقال کار** در سناریوهایی که عوامل وظیفه را به یکدیگر منتقل می‌کنند در حالی که زیرکارها کامل می‌شوند.
- **هماهنگی مغناطیسی** در سناریویی که یک عامل مدیر فهرست وظایف را ایجاد و اصلاح کرده و هماهنگی زیرعوامل برای تکمیل وظیفه را مدیریت می‌کند.

برای ارائه عوامل هوش مصنوعی در تولید، MAF همچنین ویژگی‌هایی برای موارد زیر ارائه می‌دهد:

- **قابلیت مشاهده‌پذیری** از طریق استفاده از OpenTelemetry که هر اقدام عامل هوش مصنوعی شامل فراخوانی ابزار، مراحل هماهنگی، جریان‌های استدلال و نظارت عملکرد از طریق داشبوردهای Microsoft Foundry را شامل می‌شود.
- **امنیت** با میزبانی عوامل به‌صورت بومی در Microsoft Foundry که شامل کنترل‌های امنیتی مانند دسترسی مبتنی بر نقش، مدیریت داده‌های خصوصی و ایمنی محتوا به‌صورت داخلی است.
- **دوام** به‌طوری که رشته‌ها و جریان‌های کاری عامل می‌توانند متوقف، ادامه داده شده و از خطاها بازیابی شوند که امکان اجرای فرآیندهای طولانی‌تر را فراهم می‌کند.
- **کنترل** به‌طوری که جریان‌های کاری انسان در حلقه پشتیبانی می‌شوند که در آن وظایف به عنوان نیازمند تأیید انسانی علامت‌گذاری می‌شوند.

چارچوب Microsoft Agent همچنین بر قابلیت همکاری متمرکز است از طریق:

- **غیر وابسته به ابر بودن** - عوامل می‌توانند در کانتینرها، در محل و در چندین ابر مختلف اجرا شوند.
- **غیر وابسته به ارائه‌دهنده بودن** - عوامل می‌توانند از طریق SDK ترجیحی شما از جمله Azure OpenAI و OpenAI ساخته شوند.
- **ادغام استانداردهای باز** - عوامل می‌توانند از پروتکل‌هایی مانند Agent-to-Agent(A2A) و Model Context Protocol (MCP) برای کشف و استفاده از سایر عوامل و ابزارها بهره ببرند.
- **افزونه‌ها و اتصال‌دهنده‌ها** - ارتباطاتی می‌توانند با خدمات داده و حافظه مانند Microsoft Fabric، SharePoint، Pinecone و Qdrant برقرار شوند.

بیایید ببینیم چگونه این ویژگی‌ها در برخی از مفاهیم اصلی چارچوب Microsoft Agent اعمال می‌شوند.

## مفاهیم کلیدی چارچوب Microsoft Agent

### عوامل

![Agent Framework](../../../translated_images/fa/agent-components.410a06daf87b4fef.webp)

**ایجاد عوامل**

ایجاد عامل با تعریف سرویس استنتاج (ارائه‌دهنده LLM)،
مجموعه‌ای از دستورالعمل‌ها برای پیروی عامل هوش مصنوعی، و یک `name` اختصاص یافته انجام می‌شود:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

کد بالا از `Azure OpenAI` استفاده می‌کند اما عوامل می‌توانند با استفاده از انواع خدمات از جمله `Microsoft Foundry Agent Service` ایجاد شوند:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`، APIهای `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

یا [MiniMax](https://platform.minimaxi.com/) که API سازگار با OpenAI با پنجره‌های زمینه بزرگ (تا 204 هزار توکن) ارائه می‌دهد:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

یا عوامل راه دور با استفاده از پروتکل A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**اجرای عوامل**

عوامل با استفاده از متدهای `.run` یا `.run_stream` برای پاسخ‌های بدون جریان یا جریانی اجرا می‌شوند.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

هر اجرای عامل همچنین می‌تواند گزینه‌هایی برای سفارشی‌سازی پارامترهایی مانند `max_tokens` مصرفی توسط عامل، `tools` که عامل می‌تواند فراخوانی کند، و حتی خود `model` مورد استفاده برای عامل داشته باشد.

این در مواردی مفید است که مدل‌ها یا ابزارهای خاص برای تکمیل وظیفه کاربر لازم می‌باشند.

**ابزارها**

ابزارها را می‌توان هم هنگام تعریف عامل مشخص کرد:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# هنگام ایجاد مستقیم یک ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

و هم هنگام اجرای عامل:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ابزار ارائه شده فقط برای این اجرا )
```

**رشته‌های عامل**

رشته‌های عامل برای مدیریت مکالمات چند مرحله‌ای استفاده می‌شوند. رشته‌ها می‌توانند به دو صورت ایجاد شوند:

- استفاده از `get_new_thread()` که به ذخیره شدن رشته در طول زمان امکان می‌دهد
- ایجاد یک رشته به‌صورت خودکار هنگام اجرای عامل که فقط در طول اجرای فعلی پایدار است.

برای ایجاد یک رشته، کد به این صورت است:

```python
# ایجاد یک نخ جدید.
thread = agent.get_new_thread() # اجرا کردن عامل با نخ.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

سپس می‌توانید رشته را به صورت سریالی ذخیره کنید تا برای استفاده بعدی نگهداری شود:

```python
# یک نخ جدید ایجاد کنید.
thread = agent.get_new_thread() 

# عامل را با نخ اجرا کنید.

response = await agent.run("Hello, how are you?", thread=thread) 

# نخ را برای ذخیره‌سازی سریال کنید.

serialized_thread = await thread.serialize() 

# پس از بارگذاری از ذخیره‌سازی، وضعیت نخ را سریال‌زدایی کنید.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**میان‌افزار عامل**

عوامل با ابزارها و مدل‌های زبان بزرگ تعامل دارند تا وظایف کاربران را کامل کنند. در برخی سناریوها می‌خواهیم بین این تعاملات اجرا یا رهگیری انجام دهیم. میان‌افزار عامل این امکان را می‌دهد از طریق:

*میان‌افزار تابع*

این میان‌افزار امکان اجرای عملی بین عامل و تابع/ابزاری که فراخوانی می‌کند فراهم می‌نماید. مثالی از کاربرد آن وقتی است که می‌خواهید روی فراخوانی تابع لاگ‌برداری انجام دهید.

در کد زیر `next` مشخص می‌کند که آیا میان‌افزار بعدی یا تابع اصلی باید فراخوانی شود.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # پیش‌پردازش: ثبت لاگ قبل از اجرای تابع
    print(f"[Function] Calling {context.function.name}")

    # ادامه به میدل‌ور بعدی یا اجرای تابع
    await next(context)

    # پس‌پردازش: ثبت لاگ بعد از اجرای تابع
    print(f"[Function] {context.function.name} completed")
```

*میان‌افزار چت*

این میان‌افزار امکان اجرا یا لاگ‌برداری عملی بین عامل و درخواست‌های بین مدل زبان بزرگ را فراهم می‌کند.

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

    # پس‌پردازش: ثبت لاگ پس از دریافت پاسخ هوش مصنوعی
    print("[Chat] AI response received")

```

**حافظه عامل**

همانطور که در درس `حافظه عاملی` پوشش داده شده است، حافظه نقش مهمی در توانمندسازی عامل برای کار در بافت‌های مختلف دارد. MAF انواع مختلفی از حافظه‌ها را ارائه می‌دهد:

*ذخیره‌سازی درون حافظه‌ای*

این حافظه در رشته‌ها در طول اجرای برنامه ذخیره می‌شود.

```python
# یک رشته جدید ایجاد کنید.
thread = agent.get_new_thread() # عامل را با رشته اجرا کنید.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*پیام‌های ماندگار*

این حافظه برای ذخیره تاریخچه مکالمات در جلسات مختلف استفاده می‌شود. با استفاده از `chat_message_store_factory` تعریف می‌شود:

```python
from agent_framework import ChatMessageStore

# ایجاد یک مخزن پیام سفارشی
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*حافظه پویا*

این حافظه قبل از اجرای عوامل به بافت اضافه می‌شود. این حافظه‌ها می‌توانند در سرویس‌های خارجی مانند mem0 ذخیره شوند:

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

**قابلیت مشاهده‌پذیری عامل**

قابلیت مشاهده‌پذیری برای ساخت سیستم‌های عاملی قابل اطمینان و قابل نگهداری اهمیت دارد. MAF با OpenTelemetry ادغام می‌شود تا ردیابی و اندازه‌گیری برای قابلیت مشاهده بهتر فراهم کند.

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

MAF جریان‌های کاری را ارائه می‌دهد که گام‌های از پیش تعریف‌شده برای کامل کردن یک وظیفه هستند و عوامل هوش مصنوعی را به عنوان اجزا در آن مراحل شامل می‌شوند.

جریان‌های کاری از اجزای مختلفی تشکیل شده‌اند که جریان کنترل بهتری را امکان‌پذیر می‌کنند. جریان‌های کاری همچنین امکان **هماهنگی چندعامل** و **نقطه ذخیره‌سازی** برای ذخیره وضعیت جریان کاری را فراهم می‌کنند.

اجزای اصلی یک جریان کاری عبارتند از:

**مجریان**

مجریان پیام‌های ورودی را دریافت می‌کنند، وظایف اختصاص‌یافته خود را انجام می‌دهند و سپس پیام خروجی تولید می‌کنند. این جریان کاری را به سمت تکمیل وظیفه بزرگ‌تر پیش می‌برد. مجریان می‌توانند عامل هوش مصنوعی یا منطق سفارشی باشند.

**لبه‌ها**

لبه‌ها برای تعریف جریان پیام‌ها در یک جریان کاری استفاده می‌شوند. این‌ها می‌توانند:

*لبه‌های مستقیم* - اتصال‌های ساده یک به یک بین مجریان:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*لبه‌های شرطی* - فعال شده پس از برآورده شدن شرایط خاص. به عنوان مثال، وقتی اتاق‌های هتل در دسترس نیستند، یک مجری می‌تواند گزینه‌های دیگر را پیشنهاد دهد.

*لبه‌های سوئیچ-کیس* - روت‌کردن پیام‌ها به مجریان مختلف بر اساس شرایط تعریف شده. مثلا اگر مشتری سفر دسترسی اولویت دارد و وظایفش از طریق جریان کاری دیگری پردازش می‌شوند.

*لبه‌های پخش‌کننده* - ارسال یک پیام به چندین مقصد.

*لبه‌های جمع‌کننده* - جمع‌آوری چندین پیام از مجریان مختلف و ارسال به یک مقصد.

**رویدادها**

برای ارائه قابلیت مشاهده بهتر در جریان‌های کاری، MAF رویدادهای داخلی برای اجرای جریان کاری ارائه می‌دهد از جمله:

- `WorkflowStartedEvent`  - اجرای جریان کاری آغاز می‌شود
- `WorkflowOutputEvent` - جریان کاری خروجی تولید می‌کند
- `WorkflowErrorEvent` - جریان کاری با خطا مواجه می‌شود
- `ExecutorInvokeEvent`  - مجری شروع به پردازش می‌کند
- `ExecutorCompleteEvent`  -  مجری پردازش را تمام می‌کند
- `RequestInfoEvent` - یک درخواست صادر شده است

## الگوهای پیشرفته MAF

بخش‌های بالا مفاهیم کلیدی چارچوب Microsoft Agent را پوشش دادند. هنگامی که عوامل پیچیده‌تر می‌سازید، الگوهای پیشرفته زیر را در نظر بگیرید:

- **ترکیب میان‌افزار**: زنجیره‌ای از چندین دستیگر میان‌افزار (لاگ‌برداری، احراز هویت، محدودیت نرخ) با استفاده از میان‌افزار تابع و چت برای کنترل دقیق‌تر رفتار عامل.
- **نقطه ذخیره‌سازی جریان کاری**: استفاده از رویدادهای جریان کاری و سریال‌سازی برای ذخیره و ادامه فرآیندهای طولانی عامل.
- **انتخاب پویا ابزار**: ترکیب RAG روی توضیحات ابزار با ثبت ابزارهای MAF برای ارائه تنها ابزارهای مرتبط در هر پرس‌وجو.
- **انتقال چندعاملی**: استفاده از لبه‌های جریان کاری و مسیریابی شرطی برای هماهنگی انتقال بین عوامل تخصصی.

## میزبانی عوامل LangChain / LangGraph روی Microsoft Foundry

چارچوب Microsoft Agent  **قابلیت همکاری چارچوبی** دارد — شما محدود به عوامل نوشته شده با MAF نیستید. اگر قبلاً عاملی با **LangChain** یا **LangGraph** ساخته‌اید، می‌توانید آن را به عنوان عامل میزبانی شده در **Microsoft Foundry** اجرا کنید تا Foundry زمان اجرا، جلسات، مقیاس‌دهی، هویت و نقاط پایانی پروتکل را مدیریت کند، در حالی که منطق عامل شما در LangGraph باقی می‌ماند.

این با بسته `langchain_azure_ai.agents.hosting` انجام می‌شود که یک گراف کامپایل شده LangGraph را روی همان پروتکل‌هایی که عوامل میزبانی شده Foundry استفاده می‌کنند، ارائه می‌دهد.

**1. نصب افزونه میزبانی:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

افزونه `hosting` کتابخانه‌های پروتکل Foundry را نصب می‌کند: `azure-ai-agentserver-responses` (نقطه پایانی سازگار با OpenAI `/responses`) و `azure-ai-agentserver-invocations` (نقطه پایانی عمومی `/invocations`).

**2. انتخاب پروتکل میزبانی:**

| پروتکل | کلاس میزبان | نقطه پایانی | مواقع استفاده |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | می‌خواهید چت سازگار با OpenAI، استریمینگ، تاریخچه پاسخ‌ها و موضوع‌بندی مکالمه — که پیش‌فرض توصیه شده برای عوامل مکالمه‌ای است. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | نیاز به شکل JSON سفارشی، نقطه پایانی نوع وب‌هوک، یا پردازش غیر مکالمه‌ای دارید. |

چون **API پاسخ‌ها (Responses) API اصلی برای توسعه به سبک عامل‌ها در Foundry است**، برای بیشتر عوامل با `ResponsesHostServer` شروع کنید.

**3. پیکربندی متغیرهای محیطی** (`az login` را ابتدا انجام دهید تا `DefaultAzureCredential` بتواند احراز هویت کند):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

وقتی عامل به عنوان عامل میزبانی شده در Foundry اجرا شود، پلتفرم به صورت خودکار `FOUNDRY_PROJECT_ENDPOINT` را تزریق می‌کند.

**4. ارائه یک عامل LangGraph روی پروتکل Responses:**

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

    # ChatOpenAI در اینجا به نقطه پایانی (Responses) سازگار با OpenAI پروژه Foundry اشاره دارد.
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

آن را به صورت محلی با `python main.py` اجرا کنید، سپس یک درخواست Responses به آدرس `http://localhost:8088/responses` ارسال کنید.

**رفتارهای کلیدی:**

- **مکالمات**: کلاینت‌ها مکالمه‌ای را با ارسال `previous_response_id` یا شناسه `conversation` ادامه می‌دهند. اگر گراف شما با کنترل‌کننده نقطه ذخیره‌سازی LangGraph کامپایل شده باشد، Foundry وضعیت مکالمه را به نقطه ذخیره نگاشت می‌کند (در تولید از کنترل‌کننده پایدار استفاده کنید؛ `MemorySaver` برای تست محلی مناسب است).
- **انسان در حلقه**: اگر گراف شما از `interrupt()` LangGraph استفاده کند، `ResponsesHostServer` قطعی در حال انتظار را به عنوان آیتم `function_call` / `mcp_approval_request` در Responses ظاهر می‌کند، و کلاینت‌ها با `function_call_output` / `mcp_approval_response` متناظر ادامه می‌دهند.
- **استقرار در Foundry**: از Azure Developer CLI استفاده کنید — `azd ext install azure.ai.agents`، `azd ai agent init -m <manifest>`، `azd ai agent run` (محلی، نیازمند داکر)، سپس `azd provision` و `azd deploy`. استقرار عامل میزبانی شده نیازمند نقش **Foundry Project Manager** است.

نسخه اجرایی این مثال در [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) موجود است. برای راهنمای کامل (پروتکل Invocations، اسکیمای درخواست سفارشی، و رفع خطا) به [میزبانی عوامل LangGraph به عنوان عوامل میزبانی شده Foundry](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) مراجعه کنید.

## نمونه‌های کد 

نمونه‌های کد برای چارچوب Microsoft Agent در این مخزن زیر فایل‌های `xx-python-agent-framework` و `xx-dotnet-agent-framework` قرار دارند.

## سوالات بیشتری درباره چارچوب Microsoft Agent دارید؟

به [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) بپیوندید تا با یادگیرندگان دیگر ملاقات کنید، در ساعات اداری شرکت کنید و سوالات خود درباره عوامل هوش مصنوعی را پاسخ دهید.
## درس قبلی

[حافظه برای عوامل هوش مصنوعی](../13-agent-memory/README.md)

## درس بعدی

[ساخت عوامل استفاده‌کننده از کامپیوتر (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->