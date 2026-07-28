[![چگونه نمایندگان هوش مصنوعی خوبی طراحی کنیم](../../../translated_images/fa/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(برای مشاهده ویدئوی این درس روی تصویر بالا کلیک کنید)_

# الگوی طراحی استفاده از ابزار

ابزارها جالب هستند زیرا به نمایندگان هوش مصنوعی اجازه می‌دهند دامنه وسیع‌تری از قابلیت‌ها را داشته باشند. به جای اینکه نماینده فقط یک مجموعه محدود از اقدامات را انجام دهد، با افزودن یک ابزار نماینده می‌تواند طیف گسترده‌ای از اقدامات را انجام دهد. در این فصل، به الگوی طراحی استفاده از ابزار می‌پردازیم که شرح می‌دهد چگونه نمایندگان هوش مصنوعی می‌توانند از ابزارهای خاص برای رسیدن به اهداف خود استفاده کنند.

## مقدمه

در این درس، ما به دنبال پاسخ به سوالات زیر هستیم:

- الگوی طراحی استفاده از ابزار چیست؟
- موارد کاربردی که می‌توان آن را به کار برد چه هستند؟
- عناصر/بخش‌های لازم برای پیاده‌سازی این الگو چه هستند؟
- ملاحظات ویژه در استفاده از الگوی طراحی استفاده از ابزار برای ساخت نمایندگان هوش مصنوعی قابل اعتماد چیست؟

## اهداف آموزشی

پس از اتمام این درس، قادر خواهید بود:

- الگوی طراحی استفاده از ابزار و هدف آن را تعریف کنید.
- موارد کاربردی که این الگو در آنها قابل استفاده است را شناسایی کنید.
- عناصر کلیدی لازم برای پیاده‌سازی این الگو را درک کنید.
- ملاحظات لازم برای اطمینان از قابل اعتماد بودن نمایندگان هوش مصنوعی با استفاده از این الگو را بشناسید.

## الگوی طراحی استفاده از ابزار چیست؟

**الگوی طراحی استفاده از ابزار** بر اعطای قابلیت تعامل با ابزارهای خارجی به مدل‌های زبان بزرگ (LLM) برای رسیدن به اهداف خاص تمرکز دارد. ابزارها کدهایی هستند که توسط نماینده اجرا می‌شوند تا اقدامات را انجام دهند. یک ابزار می‌تواند تابع ساده‌ای مانند ماشین حساب باشد، یا فراخوانی API به سرویس شخص ثالثی مانند جستجوی قیمت سهام یا پیش‌بینی هواشناسی. در زمینه نمایندگان هوش مصنوعی، ابزارها به گونه‌ای طراحی شده‌اند که در پاسخ به **فراخوانی‌های تابع ایجاد شده توسط مدل** اجرا شوند.

## موارد کاربردی که می‌توان آن را به کار برد چیست؟

نمایندگان هوش مصنوعی می‌توانند از ابزارها برای تکمیل وظایف پیچیده، بازیابی اطلاعات یا اتخاذ تصمیمات استفاده کنند. الگوی طراحی استفاده از ابزار اغلب در سناریوهایی به کار می‌رود که نیاز به تعامل پویا با سیستم‌های خارجی مانند پایگاه داده‌ها، خدمات وب یا مفسرهای کد دارند. این قابلیت برای چندین مورد کاربردی مفید است، از جمله:

- **بازیابی اطلاعات پویا:** نمایندگان می‌توانند به APIها یا پایگاه‌های داده خارجی درخواست دهند تا داده‌های به‌روز را دریافت کنند (مثلاً پرس‌وجو در یک پایگاه داده SQLite برای تحلیل داده، فراخوانی قیمت سهام یا اطلاعات هواشناسی).
- **اجرای کد و تفسیر:** نمایندگان می‌توانند کد یا اسکریپت‌ها را برای حل مسائل ریاضی، تولید گزارش‌ها یا انجام شبیه‌سازی‌ها اجرا کنند.
- **اتوماسیون جریان کاری:** خودکارسازی کارهای تکراری یا چند مرحله‌ای با ترکیب ابزارهایی مانند زمان‌بندهای وظیفه، خدمات ایمیل یا خطوط لوله داده.
- **پشتیبانی مشتری:** نمایندگان می‌توانند با سیستم‌های CRM، پلتفرم‌های تیکتینگ یا پایگاه‌های دانشی تعامل کنند تا سوالات کاربران را پاسخ دهند.
- **تولید و ویرایش محتوا:** نمایندگان می‌توانند از ابزارهایی مانند بررسی دستور زبان، خلاصه‌سازی متن یا ارزیاب ایمنی محتوا برای کمک به وظایف تولید محتوا استفاده کنند.

## عناصر/بخش‌های لازم برای پیاده‌سازی الگوی طراحی استفاده از ابزار چیست؟

این بخش‌ها به نماینده هوش مصنوعی اجازه می‌دهند طیف گسترده‌ای از وظایف را انجام دهد. بیایید به عناصر کلیدی لازم برای پیاده‌سازی الگوی طراحی استفاده از ابزار نگاهی بیندازیم:

- **اسکیمای توابع/ابزارها**: تعاریف دقیق ابزارهای موجود، شامل نام تابع، هدف، پارامترهای لازم و خروجی‌های مورد انتظار. این اسکیم‌ها به LLM کمک می‌کند تا بداند چه ابزارهایی دردسترس هستند و چگونه درخواست‌های معتبر بسازد.

- **منطق اجرای تابع**: تنظیم نحوه و زمان استفاده از ابزارها بر اساس قصد کاربر و زمینه گفتگو. این می‌تواند شامل ماژول‌های برنامه‌ریز، مکانیزم‌های مسیریابی یا جریان‌های شرطی باشد که استفاده از ابزار را به صورت پویا تعیین می‌کنند.

- **سیستم مدیریت پیام‌ها**: اجزایی که جریان مکالمه بین ورودی‌های کاربر، پاسخ‌های LLM، فراخوانی‌های ابزار و خروجی‌های ابزار را مدیریت می‌کنند.

- **چارچوب یکپارچه‌سازی ابزار**: زیرساختی که نماینده را به ابزارهای مختلف متصل می‌کند، خواه آنها توابع ساده باشند یا خدمات خارجی پیچیده.

- **مدیریت خطا و اعتبارسنجی**: مکانیزم‌هایی برای مواجهه با شکست‌های اجرای ابزار، اعتبارسنجی پارامترها و مدیریت پاسخ‌های غیرمنتظره.

- **مدیریت وضعیت**: پیگیری زمینه گفتگو، تعاملات قبلی با ابزارها و داده‌های پایدار برای اطمینان از سازگاری در تعاملات چند مرحله‌ای.

حالا بیایید به جزئیات بیشتر درباره فراخوانی توابع/ابزارها نگاه کنیم.
 
### فراخوانی توابع/ابزارها

فراخوانی تابع راه اصلی است که ما به مدل‌های زبان بزرگ (LLM) امکان تعامل با ابزارها را می‌دهیم. اغلب می‌بینید که 'تابع' و 'ابزار' به جای هم استفاده می‌شوند چون 'توابع' (بخش‌های کد قابل استفاده مجدد) همان 'ابزارهایی' هستند که نمایندگان برای انجام وظایف از آنها استفاده می‌کنند. برای اینکه کد یک تابع فراخوانی شود، LLM باید درخواست کاربر را با توصیف تابع مقایسه کند. برای این کار، اسکیمایی حاوی توصیفات همه توابع موجود به LLM ارسال می‌شود. سپس LLM مناسب‌ترین تابع را برای وظیفه انتخاب کرده و نام و آرگومان‌های آن را برمی‌گرداند. تابع انتخاب شده اجرا می‌شود، پاسخ آن به LLM ارسال می‌شود که از آن اطلاعات برای پاسخ به درخواست کاربر استفاده می‌کند.

برای توسعه‌دهندگان که می‌خواهند فراخوانی تابع را برای نمایندگان پیاده کنند، نیاز دارید به:

1. مدل LLM که از فراخوانی تابع پشتیبانی کند
2. اسکیمایی حاوی توصیف تابع‌ها
3. کد مربوط به هر تابع توصیف شده

اجازه دهید با مثال گرفتن زمان فعلی در یک شهر توضیح دهیم:

1. **یک LLM که از فراخوانی تابع پشتیبانی می‌کند را مقداردهی اولیه کنید:**

    همه مدل‌ها از فراخوانی تابع پشتیبانی نمی‌کنند، بنابراین مهم است که بررسی کنید مدلی که استفاده می‌کنید این قابلیت را دارد.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> از فراخوانی تابع پشتیبانی می‌کند. ما می‌توانیم با ایجاد کلاینت OpenAI در برابر **API پاسخ‌ها** Azure OpenAI شروع کنیم (نقطه پایانی پایدار `/openai/v1/` – نیازی به `api_version` نیست). 

    ```python
    # مقداردهی اولیه کلاینت OpenAI برای Azure OpenAI (API پاسخ‌ها، نقطه پایانی نسخه ۱)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **ایجاد اسکیمای تابع:**

    سپس یک اسکیمای JSON تعریف می‌کنیم که حاوی نام تابع، توضیح کارکرد آن و نام‌ها و توصیفات پارامترهای تابع است.
    سپس این اسکیم را همراه با درخواست کاربر برای پیدا کردن زمان در سان فرانسیسکو به کلاینت ارسال می‌کنیم. نکته مهم این است که آنچه برگشت داده می‌شود یک **فراخوانی ابزار** است، **نه** پاسخ نهایی سوال. همانطور که قبلاً گفتیم، LLM نام تابع انتخاب شده برای وظیفه و آرگومان‌هایی که به آن داده می‌شود را بازمی‌گرداند.

    ```python
    # شرح عملکرد برای مدل جهت خواندن (فرمت ابزار مسطح API پاسخ‌ها)
    tools = [
        {
            "type": "function",
            "name": "get_current_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        }
    ]
    ```
   
    ```python
  
    # پیام اولیه کاربر
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # اولین فراخوانی API: از مدل بخواهید که از تابع استفاده کند
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # API پاسخ‌ها فراخوانی‌های ابزار را به عنوان موارد function_call در response.output برمی‌گرداند.
    # آن‌ها را به گفتگو اضافه کنید تا مدل در نوبت بعدی زمینه کامل را داشته باشد.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **کد تابع لازم برای انجام وظیفه:**

    حالا که LLM تابع مورد نیاز برای اجرا را انتخاب کرده، باید کدی که وظیفه را انجام می‌دهد پیاده‌سازی و اجرا شود.
    می‌توانیم کد گرفتن زمان فعلی را در پایتون پیاده کنیم. همچنین باید کدی برای استخراج نام و آرگومان‌ها از response_message نوشته شود تا نتیجه نهایی به دست بیاید.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
    # مدیریت فراخوانی توابع
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # نتیجه ابزار را به عنوان یک مورد function_call_output بازگردان
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # فراخوانی دوم API: دریافت پاسخ نهایی از مدل
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

فراخوانی تابع در قلب بیشتر، اگر نه همه، طراحی استفاده از ابزار نماینده‌هاست، اما پیاده‌سازی آن از ابتدا گاهی می‌تواند چالش‌برانگیز باشد.
همانطور که در [درس 2](../../../02-explore-agentic-frameworks) یاد گرفتیم، چارچوب‌های نمایندگی بلوک‌های از پیش ساخته شده برای پیاده‌سازی استفاده از ابزار فراهم می‌کنند.
 
## مثال‌های استفاده از ابزار با چارچوب‌های نمایندگی

در اینجا چند مثال از چگونگی پیاده‌سازی الگوی طراحی استفاده از ابزار با استفاده از چارچوب‌های نمایندگی مختلف آورده شده است:

### چارچوب نماینده مایکروسافت

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">چارچوب نماینده مایکروسافت</a> یک چارچوب هوش مصنوعی متن‌باز برای ساخت نمایندگان هوش مصنوعی است. این فرایند استفاده از فراخوانی توابع را با اجازه دادن به شما برای تعریف ابزارها به عنوان توابع پایتون با دکوراتور `@tool` ساده می‌کند. این چارچوب ارتباط رفت و برگشت بین مدل و کد شما را مدیریت می‌کند. همچنین دسترسی به ابزارهای از پیش ساخته مانند جستجوی فایل و مفسر کد را از طریق `FoundryChatClient` فراهم می‌کند.

نمودار زیر فرایند فراخوانی تابع با چارچوب نماینده مایکروسافت را نشان می‌دهد:

![function calling](../../../translated_images/fa/functioncalling-diagram.a84006fc287f6014.webp)

در چارچوب نماینده مایکروسافت، ابزارها به صورت توابع دکورت شده تعریف می‌شوند. می‌توانیم تابع `get_current_time` که قبلاً دیدیم را به وسیله دکوراتور `@tool` به یک ابزار تبدیل کنیم. چارچوب به طور خودکار تابع و پارامترهای آن را سریال‌سازی می‌کند و اسکیمایی برای ارسال به LLM ایجاد می‌کند.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# ایجاد کلاینت
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# یک ایجنت بسازید و با ابزار اجرا کنید
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### سرویس نماینده Microsoft Foundry

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">سرویس نماینده Microsoft Foundry</a> یک چارچوب نمایندگی جدیدتر است که به توسعه‌دهندگان امکان ساخت، استقرار و مقیاس‌دهی امن نمایندگان هوش مصنوعی با کیفیت بالا و قابل توسعه را بدون نیاز به مدیریت منابع محاسبات و ذخیره‌سازی زیرساختی می‌دهد. این سرویس برای کاربردهای سازمانی بسیار مفید است چون کاملاً مدیریت شده است و امنیت سطح سازمانی دارد.

در مقایسه با توسعه مستقیم با API مدل‌های زبان بزرگ، سرویس نماینده Microsoft Foundry مزایایی دارد از جمله:

- فراخوانی خودکار ابزارها – نیازی به تجزیه یک فراخوانی ابزار، اجرای ابزار و مدیریت پاسخ نیست؛ تمام این کارها اکنون در سمت سرور انجام می‌شود
- داده‌های به صورت امن مدیریت شده – به جای مدیریت وضعیت مکالمه خود، می‌توانید روی رشته‌ها (threads) برای ذخیره تمام اطلاعات مورد نیاز خود حساب کنید
- ابزارهای آماده استفاده – ابزاری که می‌توانید برای تعامل با منابع داده خود استفاده کنید مانند بینگ، جستجوی Azure AI و Azure Functions.

ابزارهای موجود در سرویس نماینده Microsoft Foundry به دو دسته تقسیم می‌شوند:

1. ابزارهای دانش:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">ارتباط با جستجوی Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">جستجوی فایل</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">جستجوی Azure AI</a>

2. ابزارهای عملیاتی:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">فراخوانی تابع</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">مفسر کد</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">ابزارهای تعریف شده با OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

سرویس نماینده به ما امکان استفاده همزمان از این ابزارها به صورت یک `مجموعه ابزار` را می‌دهد. همچنین از `رشته‌ها` استفاده می‌کند که سابقه پیام‌های یک مکالمه خاص را پیگیری می‌کنند.

تصور کنید شما نماینده فروش در شرکتی به نام Contoso هستید. می‌خواهید نماینده مکالمه‌ای توسعه دهید که بتواند به سوالات مربوط به داده‌های فروش شما پاسخ دهد.

تصویر زیر نشان می‌دهد چگونه می‌توانید از سرویس نماینده Microsoft Foundry برای تحلیل داده‌های فروش خود استفاده کنید:

![Agentic Service In Action](../../../translated_images/fa/agent-service-in-action.34fb465c9a84659e.webp)

برای استفاده از هر یک از این ابزارها با سرویس، می‌توانیم یک کلاینت ایجاد کرده و یک ابزار یا مجموعه ابزار تعریف کنیم. برای پیاده‌سازی عملی می‌توانیم از کد پایتون زیر استفاده کنیم. LLM قادر خواهد بود مجموعه ابزار را بررسی کند و تصمیم بگیرد که آیا از تابع کاربر ساخته شده `fetch_sales_data_using_sqlite_query` استفاده کند یا مفسر کد از پیش ساخته بسته به درخواست کاربر.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # تابع fetch_sales_data_using_sqlite_query که در فایل fetch_sales_data_functions.py یافت می‌شود.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# مقداردهی اولیه مجموعه ابزار
toolset = ToolSet()

# مقداردهی اولیه عامل فراخوانی تابع با تابع fetch_sales_data_using_sqlite_query و اضافه کردن آن به مجموعه ابزار
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# مقداردهی اولیه ابزار مفسر کد و اضافه کردن آن به مجموعه ابزار
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ملاحظات ویژه در استفاده از الگوی طراحی استفاده از ابزار برای ساخت نمایندگان قابل اعتماد چیست؟

نگرانی رایج درباره SQL که به صورت پویا توسط LLMها ساخته می‌شود، امنیت است، به خصوص خطر حملات تزریق SQL یا اقدامات مخرب مانند حذف یا دستکاری پایگاه داده. در حالی که این نگرانی‌ها معتبر هستند، می‌توان آنها را به طور مؤثر با تنظیم صحیح مجوزهای دسترسی پایگاه داده کاهش داد. برای اکثر پایگاه‌های داده، این شامل تنظیم پایگاه داده به صورت فقط خواندنی است. برای خدمات پایگاه داده‌ای مانند PostgreSQL یا Azure SQL، باید اپلیکیشن نقش فقط خواندنی (SELECT) اختصاص داده شود.

اجرای اپلیکیشن در محیطی امن حفاظت را بیشتر می‌کند. در سناریوهای سازمانی، معمولاً داده‌ها از سیستم‌های عملیاتی استخراج و به پایگاه داده یا انبار داده فقط خواندنی با اسکیمای کاربرپسند منتقل می‌شوند. این روش تضمین می‌کند داده‌ها امن، بهینه شده برای عملکرد و دسترسی‌پذیری هستند و اپلیکیشن دسترسی محدود و فقط خواندنی دارد.

## نمونه کدها

- پایتون: [چارچوب نماینده](./code_samples/04-python-agent-framework.ipynb)
- .NET: [چارچوب نماینده](./code_samples/04-dotnet-agent-framework.md)

## سوال بیشتری درباره الگوهای طراحی استفاده از ابزار دارید؟

به [Discord Microsoft Foundry](https://discord.com/invite/ATgtXmAS5D) بپیوندید تا با سایر یادگیرندگان ملاقات کنید، در ساعت‌های پاسخگویی شرکت کنید و سوالات خود درباره نمایندگان هوش مصنوعی را مطرح کنید.

## منابع بیشتر

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">کارگاه سرویس نمایندگان هوش مصنوعی Azure</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">کارگاه مولتی‌ نماینده نویسنده خلاق Contoso</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">بررسی چارچوب نماینده مایکروسافت</a>


## تست سریع این عامل (اختیاری)

پس از یادگیری استقرار عوامل در [درس ۱۶](../16-deploying-scalable-agents/README.md)، می‌توانید این درس `TravelToolAgent` را به‌صورت تست سریع (آیا هنوز ابزارهایش را صدا می‌زند و پاسخ می‌دهد؟) با استفاده از [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) آزمایش کنید. برای نحوه اجرا به [`tests/README.md`](../tests/README.md) مراجعه کنید.

## درس قبلی

[درک الگوهای طراحی عاملیت](../03-agentic-design-patterns/README.md)

## درس بعدی

[عاملیت RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->