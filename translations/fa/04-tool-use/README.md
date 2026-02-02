[![چگونه عامل‌های هوش مصنوعی خوب طراحی کنیم](../../../translated_images/fa/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(برای مشاهده ویدیوی این درس روی تصویر بالا کلیک کنید)_

# الگوی طراحی استفاده از ابزار

ابزارها جالب هستند چون به عامل‌های هوش مصنوعی امکان می‌دهند دامنه وسیع‌تری از توانمندی‌ها را داشته باشند. به جای اینکه عامل فقط مجموعه محدودی از عملکردها را داشته باشد، با اضافه کردن یک ابزار، عامل اکنون می‌تواند طیف گسترده‌ای از کارها را انجام دهد. در این فصل، به الگوی طراحی استفاده از ابزار خواهیم پرداخت که توضیح می‌دهد چگونه عامل‌های هوش مصنوعی می‌توانند از ابزارهای خاصی برای رسیدن به اهدافشان استفاده کنند.

## مقدمه

در این درس، به سوالات زیر پاسخ می‌دهیم:

- الگوی طراحی استفاده از ابزار چیست؟
- در چه مواردی می‌توان از آن استفاده کرد؟
- عناصر/بلوک‌های ساختمانی لازم برای پیاده‌سازی این الگو چه هستند؟
- ملاحظات خاص برای استفاده از الگوی طراحی استفاده از ابزار برای ساخت عامل‌های هوش مصنوعی قابل اعتماد چیست؟

## اهداف یادگیری

پس از اتمام این درس، شما خواهید توانست:

- تعریف الگوی طراحی استفاده از ابزار و هدف آن را بیان کنید.
- مواردی که الگوی طراحی استفاده از ابزار قابل کاربرد است را شناسایی کنید.
- عناصر کلیدی لازم برای پیاده‌سازی این الگو را درک کنید.
- ملاحظات لازم برای اطمینان از اعتبار عامل‌های هوش مصنوعی که از این الگو استفاده می‌کنند را بشناسید.

## الگوی طراحی استفاده از ابزار چیست؟

**الگوی طراحی استفاده از ابزار** بر این تمرکز دارد که به مدل‌های زبان بزرگ (LLM) قابلیت تعامل با ابزارهای خارجی برای رسیدن به اهداف خاص را بدهد. ابزارها کدهایی هستند که عامل می‌تواند برای انجام کارها اجرا کند. یک ابزار می‌تواند تابع ساده‌ای مانند ماشین‌حساب باشد یا فراخوانی API به سرویس ثالث مانند جستجوی قیمت سهام یا پیش‌بینی وضعیت هوا. در زمینه عامل‌های هوش مصنوعی، ابزارها طوری طراحی شده‌اند که در پاسخ به **فراخوانی‌های تابع تولیدشده توسط مدل** توسط عامل اجرا شوند.

## موارد کاربرد آن چیست؟

عامل‌های هوش مصنوعی می‌توانند از ابزارها برای انجام وظایف پیچیده، بازیابی اطلاعات یا گرفتن تصمیمات استفاده کنند. الگوی طراحی استفاده از ابزار معمولاً در سناریوهایی که نیاز به تعامل پویا با سیستم‌های خارجی دارند به کار می‌رود، مانند پایگاه‌های داده، خدمات وب یا مفسرهای کد. این قابلیت برای کاربردهای مختلفی مفید است از جمله:

- **بازیابی اطلاعات پویا:** عامل‌ها می‌توانند با API‌های خارجی یا پایگاه‌های داده پرس‌وجو کنند تا داده‌های به‌روز شده را دریافت کنند (مثلاً پرس‌وجو در پایگاه داده SQLite برای تحلیل داده، دریافت قیمت سهام یا اطلاعات هواشناسی).
- **اجرای کد و تفسیر آن:** عامل‌ها می‌توانند کد یا اسکریپت اجرا کنند تا مسائل ریاضی را حل، گزارش تولید یا شبیه‌سازی انجام دهند.
- **اتوماسیون گردش کار:** خودکارسازی کارهای تکراری یا چندمرحله‌ای با ادغام ابزارهایی مثل زمان‌بندهای وظیفه، خدمات ایمیل یا خطوط انتقال داده.
- **پشتیبانی مشتری:** عامل‌ها می‌توانند با سیستم‌های CRM، پلتفرم‌های تیکتینگ یا پایگاه‌های دانش تعامل داشته باشند تا به پرسش‌های کاربران پاسخ دهند.
- **تولید و ویرایش محتوا:** عامل‌ها می‌توانند از ابزارهایی مانند بررسی دستور زبان، خلاصه‌سازی متن یا ارزیاب ایمنی محتوا برای کمک به ایجاد محتوا استفاده کنند.

## عناصر/بلوک‌های ساختمانی لازم برای پیاده‌سازی الگوی طراحی استفاده از ابزار چیست؟

این بلوک‌های ساختمانی به عامل هوش مصنوعی اجازه می‌دهند طیف وسیعی از وظایف را انجام دهد. بیایید عناصر کلیدی لازم برای پیاده‌سازی الگوی طراحی استفاده از ابزار را بررسی کنیم:

- **طرحواره‌های تابع/ابزار:** تعاریف دقیق از ابزارهای موجود، شامل نام تابع، هدف، پارامترهای لازم و خروجی‌های مورد انتظار. این طرحواره‌ها به مدل زبان بزرگ کمک می‌کنند تا بفهمد چه ابزارهایی در دسترس هستند و چگونه درخواست‌های معتبر بسازد.

- **منطق اجرای تابع:** کنترل می‌کند که چگونه و چه زمانی ابزارها بر اساس نیت کاربر و زمینه گفتگو فراخوانی شوند. این می‌تواند شامل ماژول‌های برنامه‌ریز، مکانیزم‌های مسیریابی یا جریان‌های شرطی باشد که استفاده از ابزار را به صورت پویا تعیین می‌کنند.

- **سیستم مدیریت پیام:** اجزایی که جریان مکالمه بین ورودی‌های کاربر، پاسخ‌های LLM، فراخوانی‌های ابزار و خروجی ابزار را مدیریت می‌کنند.

- **چارچوب ادغام ابزار:** زیرساختی که عامل را به ابزارهای مختلف متصل می‌کند، چه توابع ساده باشند چه خدمات پیچیده خارجی.

- **مدیریت خطا و اعتبارسنجی:** مکانیزم‌هایی برای مدیریت خطاهای اجرای ابزار، اعتبارسنجی پارامترها و مدیریت پاسخ‌های غیرمنتظره.

- **مدیریت وضعیت:** پیگیری زمینه گفتگو، تعاملات پیشین با ابزار و داده‌های پایدار برای حفظ هماهنگی در تعاملات چند مرحله‌ای.

اکنون بیایید نگاه دقیق‌تری به فراخوانی تابع/ابزار بیندازیم.

### فراخوانی تابع/ابزار

فراخوانی تابع راه اصلی است که به مدل‌های زبان بزرگ (LLM) اجازه تعامل با ابزارها را می‌دهد. اغلب «توابع» و «ابزارها» به جای هم استفاده می‌شوند چون «توابع» (بلوک‌های کد قابل استفاده مجدد) همان «ابزارهایی» هستند که عامل‌ها برای انجام کارها استفاده می‌کنند. برای اینکه کد یک تابع اجرا شود، LLM باید درخواست کاربر را با توصیف توابع مقایسه کند. برای این منظور یک طرحواره شامل توصیفات تمام توابع موجود به LLM ارسال می‌شود. سپس LLM مناسب‌ترین تابع را برای کار انتخاب می‌کند و نام و آرگومان‌های آن را باز می‌گرداند. آن تابع انتخاب‌شده اجرا شده و پاسخ آن به LLM ارسال می‌شود تا از آن برای پاسخ به درخواست کاربر استفاده کند.

برای توسعه‌دهندگان جهت پیاده‌سازی فراخوانی تابع برای عامل‌ها، به موارد زیر نیاز دارید:

1. یک مدل LLM که پشتیبانی از فراخوانی تابع داشته باشد.
2. یک طرحواره حاوی توصیفات توابع.
3. کد هر تابع که توصیف شده است.

بیایید با مثال گرفتن زمان کنونی در یک شهر این موضوع را نشان دهیم:

1. **راه‌اندازی یک مدل LLM که از فراخوانی تابع پشتیبانی کند:**

   همه مدل‌ها فراخوانی تابع را پشتیبانی نمی‌کنند، پس مهم است که بررسی کنید مدل LLM شما این قابلیت را دارد یا خیر. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> فراخوانی تابع را پشتیبانی می‌کند. می‌توانیم با راه‌اندازی کلاینت Azure OpenAI شروع کنیم.

    ```python
    # مقداردهی اولیه‌ی کلاینت Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```
  
1. **ایجاد طرحواره تابع:**

   سپس یک طرحواره JSON تعریف می‌کنیم که شامل نام تابع، توضیح کاری که انجام می‌دهد و نام‌ها و توضیحات پارامترهای آن است. سپس این طرحواره را همراه با درخواست کاربر (برای یافتن زمان در سان‌فرانسیسکو) به کلاینت ارسال می‌کنیم. نکته مهم این است که **فراخوانی ابزار** برگشت داده می‌شود، **نه** پاسخ نهایی سؤال. همان‌طور که قبل‌تر گفته شد، LLM نام تابع انتخاب‌شده و آرگومان‌هایی که به آن داده می‌شوند را برمی‌گرداند.

    ```python
    # توضیح عملکرد برای مدل جهت خواندن
    tools = [
        {
            "type": "function",
            "function": {
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
        }
    ]
    ```
  
    ```python
  
    # پیام اولیه کاربر
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # اولین فراخوانی API: درخواست از مدل برای استفاده از تابع
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # پردازش پاسخ مدل
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```
  
    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **کدی که برای انجام وظیفه لازم است:**

   حال که LLM انتخاب کرده کدام تابع باید اجرا شود، کدی که کار را انجام می‌دهد باید پیاده‌سازی و اجرا شود. می‌توانیم کد گرفتن زمان کنونی را در پایتون پیاده کنیم. همچنین نیاز است کدی نوشته شود که نام و آرگومان‌ها را از response_message استخراج کند تا نتیجه نهایی به دست آید.

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
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # دومین فراخوانی API: دریافت پاسخ نهایی از مدل
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```
  
     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```
  
فراخوانی تابع در هسته بیشتر، اگر نگوییم همه، طراحی استفاده از ابزار عامل‌هاست، اما پیاده‌سازی آن از ابتدا می‌تواند گاهی چالش‌برانگیز باشد. همانطور که در [درس 2](../../../02-explore-agentic-frameworks) یاد گرفتیم، چارچوب‌های عاملی بلوک‌های ساختمانی پیش‌ساخته‌ای برای پیاده‌سازی استفاده از ابزار در اختیار ما می‌گذارند.

## مثال‌هایی از استفاده از ابزار با چارچوب‌های عاملی

در اینجا چند مثال از چگونگی پیاده‌سازی الگوی طراحی استفاده از ابزار با استفاده از چارچوب‌های عاملی مختلف آورده شده است:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> چارچوب هوش مصنوعی متن‌بازی برای توسعه‌دهندگان .NET، پایتون و جاوا است که با مدل‌های زبان بزرگ (LLM) کار می‌کنند. این چارچوب استفاده از فراخوانی تابع را با توصیف خودکار توابع و پارامترهای آنها به مدل از طریق فرایندی به نام <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">سریال‌سازی</a> ساده می‌کند. همچنین ارتباط رفت و برگشت بین مدل و کد شما را مدیریت می‌کند. یکی دیگر از مزایای استفاده از چارچوب عاملی مانند Semantic Kernel این است که به شما اجازه می‌دهد به ابزارهای از پیش ساخته‌ای مانند <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">جستجوی فایل</a> و <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">مفسر کد</a> دسترسی داشته باشید.

نمودار زیر فرایند فراخوانی تابع با Semantic Kernel را نشان می‌دهد:

![function calling](../../../translated_images/fa/functioncalling-diagram.a84006fc287f6014.webp)

در Semantic Kernel توابع/ابزارها <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">افزونه (Plugins)</a> نامیده می‌شوند. می‌توانیم تابع `get_current_time` که قبلاً دیدیم را تبدیل به افزونه کنیم، با تبدیل آن به یک کلاس که درون آن تابع قرار دارد. همچنین می‌توانیم دکوریتور `kernel_function` را وارد کنیم که شرح تابع را دریافت می‌کند. وقتی کرنل را با GetCurrentTimePlugin ایجاد می‌کنید، کرنل به‌صورت خودکار تابع و پارامترهای آن را سریال‌سازی می‌کند و طرحواره‌ای برای ارسال به LLM در فرایند ایجاد می‌کند.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```
  
```python 
from semantic_kernel import Kernel

# کرنل را ایجاد کنید
kernel = Kernel()

# پلاگین را ایجاد کنید
get_current_time_plugin = GetCurrentTimePlugin(location)

# پلاگین را به کرنل اضافه کنید
kernel.add_plugin(get_current_time_plugin)
```
  
### سرویس عامل Azure AI

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">سرویس عامل Azure AI</a> چارچوب عاملی جدیدتری است که به توسعه‌دهندگان امکان می‌دهد عامل‌های هوش مصنوعی با کیفیت و مقیاس‌پذیر بسازند و بدون نیاز به مدیریت منابع محاسبات و ذخیره‌سازی زیرساخت، به صورت ایمن آن‌ها را مستقر کنند. این سرویس به‌ویژه برای برنامه‌های سازمانی مفید است چون سرویس کاملاً مدیریت‌شده با امنیت سازمانی است.

در مقایسه با توسعه مستقیم با API مدل‌های زبان بزرگ، سرویس عامل Azure AI مزایایی دارد از جمله:

- فراخوانی خودکار ابزار – نیازی به تجزیه فراخوانی ابزار، اجرای ابزار و مدیریت پاسخ نیست؛ همه این‌ها اکنون در سمت سرویس انجام می‌شود.
- مدیریت امن داده‌ها – به جای مدیریت وضعیت مکالمه خودتان، می‌توانید روی قابلیت ذخیره داده در Threads حساب کنید.
- ابزارهای آماده استفاده – ابزارهایی برای تعامل با منابع داده شما مثل Bing، جستجوی Azure AI و Azure Functions.

ابزارهای موجود در سرویس عامل Azure AI را می‌توان به دو دسته تقسیم کرد:

1. ابزارهای دانش:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">یکپارچه‌سازی با Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">جستجوی فایل</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">جستجوی Azure AI</a>

2. ابزارهای عملیاتی:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">فراخوانی تابع</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">مفسر کد</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">ابزارهای تعریف‌شده با OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

سرویس عامل به ما اجازه می‌دهد این ابزارها را با هم به عنوان `toolset` استفاده کنیم. همچنین از `threads` استفاده می‌کند که تاریخچه پیام‌ها را از یک مکالمه خاص نگهداری می‌کند.

تصور کنید شما یک نماینده فروش در شرکتی به نام Contoso هستید. می‌خواهید یک عامل مکالمه‌ای توسعه دهید که بتواند به سوالات مربوط به داده‌های فروش شما پاسخ دهد.

تصویر زیر نشان می‌دهد چگونه می‌توانید از سرویس عامل Azure AI برای تحلیل داده‌های فروش خود استفاده کنید:

![Agentic Service In Action](../../../translated_images/fa/agent-service-in-action.34fb465c9a84659e.webp)

برای استفاده از هرکدام از این ابزارها در سرویس، می‌توانیم کلاینت ایجاد کنیم و یک ابزار یا مجموعه ابزار تعریف کنیم. برای پیاده‌سازی این موضوع در عمل می‌توانیم از کد پایتون زیر استفاده کنیم. مدل زبان بزرگ می‌تواند به toolset نگاه کند و تصمیم بگیرد که آیا از تابع ایجاد شده توسط کاربر با نام `fetch_sales_data_using_sqlite_query` استفاده کند یا از مفسر کد پیش‌ساخته بسته به درخواست کاربر.

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

# مقداردهی اولیه عامل فراخوانی تابع با تابع fetch_sales_data_using_sqlite_query و افزودن آن به مجموعه ابزار
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# مقداردهی اولیه ابزار مفسر کد و افزودن آن به مجموعه ابزار
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```
  
## ملاحظات خاص برای استفاده از الگوی طراحی استفاده از ابزار جهت ساخت عامل‌های هوش مصنوعی قابل اعتماد چیست؟

یکی از نگرانی‌های رایج در مورد SQLی که به صورت پویا توسط LLM تولید می‌شود، امنیت است، به‌خصوص ریسک تزریق SQL یا اقدامات مخرب مانند حذف یا دستکاری پایگاه داده. در حالی که این نگرانی‌ها معتبر هستند، می‌توان آن‌ها را به طور موثر با پیکربندی صحیح دسترسی به پایگاه داده کاهش داد. برای بیشتر پایگاه‌های داده این شامل تنظیم پایگاه داده به صورت فقط خواندنی است. برای سرویس‌های پایگاه داده مانند PostgreSQL یا Azure SQL، باید نقش خواندنی (SELECT) به برنامه اختصاص داده شود.
اجرای برنامه در یک محیط امن به حفاظت بیشتر کمک می‌کند. در سناریوهای سازمانی، داده‌ها معمولاً از سیستم‌های عملیاتی استخراج و به یک پایگاه داده یا انبار داده فقط‌خواندنی با یک اسکیما کاربرپسند تبدیل می‌شوند. این رویکرد اطمینان می‌دهد که داده‌ها امن هستند، برای عملکرد و دسترسی بهینه شده‌اند و برنامه دسترسی محدود و فقط‌خواندنی دارد.

## نمونه کدها

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## سوالات بیشتری درباره الگوهای طراحی ابزار دارید؟

به [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) بپیوندید تا با سایر یادگیرندگان ملاقات کنید، در ساعات اداری شرکت کنید و سوالات خود درباره عوامل هوش مصنوعی را مطرح کنید.

## منابع بیشتر

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">کارگاه خدمات عوامل هوش مصنوعی آزور</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">کارگاه چندعاملی نویسنده خلاق کانتوسو</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">آموزش فراخوانی توابع Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">مفسر کد Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">ابزارهای Autogen</a>

## درس قبلی

[درک الگوهای طراحی عاملی](../03-agentic-design-patterns/README.md)

## درس بعدی

[عامل RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**توضیح مهم**:
این سند با استفاده از سرویس ترجمه ماشینی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای ارائه ترجمه‌ای دقیق هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی اشتباهات یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، توصیه می‌شود ترجمه حرفه‌ای انسانی انجام شود. ما مسئول هیچگونه سوءتفاهم یا برداشت نادرستی که ناشی از استفاده از این ترجمه باشد، نمی‌باشیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->