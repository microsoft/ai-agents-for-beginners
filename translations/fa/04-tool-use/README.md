[![چگونه عامل‌های هوش مصنوعی خوب طراحی کنیم](../../../translated_images/fa/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(برای مشاهده ویدیوی این درس روی تصویر بالا کلیک کنید)_

# الگوی طراحی استفاده از ابزار

ابزارها جالب هستند چون به عامل‌های هوش مصنوعی اجازه می‌دهند مجموعه گسترده‌تری از قابلیت‌ها را داشته باشند. به جای اینکه عامل فقط یک مجموعه محدود از اقدامات را انجام دهد، با افزودن یک ابزار، عامل اکنون می‌تواند طیف وسیعی از اقدامات را انجام دهد. در این فصل، به الگوی طراحی استفاده از ابزار می‌پردازیم که توضیح می‌دهد چگونه عامل‌های هوش مصنوعی می‌توانند از ابزارهای مشخص برای دستیابی به اهدافشان استفاده کنند.

## مقدمه

در این درس، قصد داریم به پرسش‌های زیر پاسخ دهیم:

- الگوی طراحی استفاده از ابزار چیست؟
- این الگو در چه کاربردهایی قابل اعمال است؟
- عناصر/بلوک‌های ساختمانی لازم برای پیاده‌سازی این الگو کدامند؟
- ملاحظات ویژه برای استفاده از الگوی طراحی استفاده از ابزار جهت ساخت عامل‌های هوش مصنوعی قابل اعتماد چیست؟

## اهداف یادگیری

پس از اتمام این درس، شما قادر خواهید بود:

- تعریف الگوی طراحی استفاده از ابزار و هدف آن را بیان کنید.
- کاربردهایی که الگوی طراحی استفاده از ابزار در آن‌ها مناسب است را شناسایی کنید.
- عناصر کلیدی لازم برای پیاده‌سازی این الگو را درک کنید.
- ملاحظات لازم برای تضمین اعتمادپذیری عامل‌های هوش مصنوعی که از این الگو استفاده می‌کنند را تشخیص دهید.

## الگوی طراحی استفاده از ابزار چیست؟

**الگوی طراحی استفاده از ابزار** بر این تمرکز دارد که مدل‌های زبانی بزرگ (LLM) توانایی تعامل با ابزارهای خارجی برای رسیدن به اهداف مشخص را داشته باشند. ابزارها کدهایی هستند که توسط یک عامل اجرا می‌شوند تا کارهایی را انجام دهند. یک ابزار می‌تواند یک تابع ساده مانند ماشین حساب باشد، یا یک فراخوان API به سرویس سوم شخص مانند جستجوی قیمت سهام یا پیش‌بینی آب‌وهوا. در زمینه عامل‌های هوش مصنوعی، ابزارها به گونه‌ای طراحی شده‌اند که در پاسخ به **فراخوان‌های تابع تولید شده توسط مدل** توسط عامل‌ها اجرا شوند.

## کاربردهایی که این الگو می‌تواند در آن‌ها به کار رود چیست؟

عامل‌های هوش مصنوعی می‌توانند از ابزارها برای انجام کارهای پیچیده، بازیابی اطلاعات یا اتخاذ تصمیم استفاده کنند. الگوی طراحی استفاده از ابزار اغلب در سناریوهایی استفاده می‌شود که تعامل پویا با سیستم‌های خارجی مانند پایگاه داده‌ها، وب‌سرویس‌ها یا مفسرهای کد مورد نیاز است. این توانایی در موارد مختلف زیر مفید است:

- **بازیابی اطلاعات پویا:** عامل‌ها می‌توانند با APIهای خارجی یا پایگاه داده‌ها برای گرفتن داده‌های به‌روز ارتباط برقرار کنند (مثلاً پرس و جوی پایگاه داده SQLite برای تحلیل داده‌ها، گرفتن قیمت سهام یا اطلاعات هواشناسی).
- **اجرای کد و تفسیر:** عامل‌ها می‌توانند کد یا اسکریپت اجرا کنند تا مسائل ریاضی حل کنند، گزارش تولید کنند، یا شبیه‌سازی انجام دهند.
- **اتوماسیون فرآیندهای کاری:** خودکارسازی فرآیندهای تکراری یا چند مرحله‌ای با ابزارهایی مانند زمان‌بندهای وظیفه، خدمات ایمیل یا خط لوله‌های داده.
- **پشتیبانی مشتری:** عامل‌ها می‌توانند با سیستم‌های CRM، پلتفرم‌های تیکت و پایگاه‌های دانش برای پاسخ به سوالات کاربران تعامل کنند.
- **تولید و ویرایش محتوا:** عامل‌ها می‌توانند از ابزارهایی مثل چک‌کننده گرامر، خلاصه‌ساز متن یا ارزیاب ایمنی محتوا برای کمک به تولید محتوا استفاده کنند.

## عناصر/بلوک‌های ساختمانی لازم برای پیاده‌سازی الگوی استفاده از ابزار چیست؟

این بلوک‌ها به عامل هوش مصنوعی اجازه می‌دهند طیف گسترده‌ای از وظایف را انجام دهد. بیایید به عناصر کلیدی لازم برای پیاده‌سازی الگوی طراحی استفاده از ابزار نگاهی بیندازیم:

- **شمای توابع/ابزارها:** تعریف‌های دقیق ابزارهای موجود شامل نام تابع، هدف، پارامترهای مورد نیاز و خروجی‌های مورد انتظار. این شمایه‌ها به LLM کمک می‌کنند بفهمد چه ابزارهایی در دسترس است و چگونه درخواست‌های معتبر بسازد.

- **منطق اجرای توابع:** قوانین مربوط به چگونگی و زمان فراخوانی ابزارها مبتنی بر قصد کاربر و محتوای گفتگو. این ممکن است شامل ماژول‌های برنامه‌ریز، مکانیزم‌های مسیردهی یا جریان‌های شرطی باشد که استفاده از ابزار را به صورت پویا تعیین می‌کنند.

- **سیستم مدیریت پیام:** اجزایی که جریان مکالمه بین ورودی‌های کاربر، پاسخ‌های LLM، فراخوانی ابزار و خروجی‌های آن‌ها را مدیریت می‌کنند.

- **چارچوبِ یکپارچه‌سازی ابزار:** زیرساختی که عامل را به ابزارهای مختلف، چه توابع ساده و چه سرویس‌های خارجی پیچیده، متصل می‌کند.

- **مدیریت خطا و اعتبارسنجی:** مکانیزم‌هایی برای مدیریت شکست‌ها در اجرای ابزار، اعتبارسنجی پارامترها و مدیریت پاسخ‌های غیرمنتظره.

- **مدیریت وضعیت:** پیگیری محتوای گفتگو، تعاملات قبلی با ابزارها و داده‌های پایدار برای اطمینان از سازگاری در تعاملات چند مرحله‌ای.

حالا بیایید جزئیات بیشتری درباره فراخوانی توابع/ابزارها بیاموزیم.

### فراخوانی توابع/ابزارها

فراخوانی تابع روش اصلی است که به مدل‌های زبانی بزرگ (LLM) اجازه می‌دهد با ابزارها تعامل داشته باشند. شما اغلب می‌بینید "تابع" و "ابزار" به جای هم استفاده می‌شوند، زیرا "توابع" (بلوک‌های کد قابل استفاده مجدد) همان "ابزارهایی" هستند که عامل‌ها برای انجام وظایف استفاده می‌کنند. برای اینکه کد یک تابع فراخوانی شود، مدل زبانی باید درخواست کاربر را با توصیف توابع مقایسه کند. برای این کار یک شمای شامل توصیف همه توابع موجود به LLM ارسال می‌شود. سپس LLM مناسب‌ترین تابع برای وظیفه را انتخاب کرده و نام و آرگومان‌های آن را بازمی‌گرداند. تابع انتخاب شده اجرا می‌شود، پاسخ آن به LLM ارسال می‌گردد، و LLM با استفاده از این اطلاعات به درخواست کاربر پاسخ می‌دهد.

برای توسعه‌دهندگان جهت پیاده‌سازی فراخوانی تابع برای عامل‌ها، به موارد زیر نیاز دارید:

1. مدل LLM که از فراخوانی تابع پشتیبانی می‌کند
2. یک شمای حاوی توصیف توابع
3. کد هر تابعی که توصیف شده است

اجازه دهید مثال گرفتن زمان فعلی در یک شهر را برای توضیح استفاده کنیم:

1. **راه‌اندازی مدلی که از فراخوانی تابع پشتیبانی می‌کند:**

    همه مدل‌ها از فراخوانی تابع پشتیبانی نمی‌کنند، بنابراین بررسی اینکه LLM شما این قابلیت را دارد مهم است. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> از فراخوانی تابع پشتیبانی می‌کند. می‌توانیم با ایجاد کلاینت Azure OpenAI شروع کنیم.

    ```python
    # مشتری Azure OpenAI را مقداردهی اولیه کنید
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **ایجاد یک شمای تابع:**

    سپس یک شمای JSON تعریف می‌کنیم که شامل نام تابع، شرح کاری که تابع انجام می‌دهد، و نام‌ها و توضیحات پارامترهای آن است.
    سپس این شمایه را همراه با درخواست کاربر برای یافتن زمان در سان‌فرانسیسکو به کلاینت ایجاد شده ارسال می‌کنیم. نکته مهم این است که آنچه بازمی‌گردد یک **فراخوان ابزار** است، **نه** پاسخ نهایی. همانطور که پیش‌تر گفته شد، LLM نام تابع انتخابی برای وظیفه و آرگومان‌هایی که به آن داده می‌شود را بازمی‌گرداند.

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
  
1. **کد تابعی که برای انجام وظیفه لازم است:**

    هنگامی که LLM تصمیم گرفت کدام تابع باید اجرا شود، کدی که وظیفه را انجام می‌دهد باید پیاده‌سازی و اجرا شود.
    ما می‌توانیم کدی در پایتون بنویسیم که زمان فعلی را بگیرد. همچنین باید کد استخراج نام و آرگومان‌ها از response_message را برای گرفتن نتیجه نهایی بنویسیم.

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
     # مدیریت فراخوانی‌های تابع
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

فراخوانی تابع در قلب بسیاری از طراحی‌های استفاده از ابزارهای عامل قرار دارد، اگرچه پیاده‌سازی آن از ابتدا گاهی چالش‌برانگیز است.
همانطور که در [درس ۲](../../../02-explore-agentic-frameworks) آموختیم، چارچوب‌های عاملی بلوک‌های ساختمانی آماده برای پیاده‌سازی استفاده از ابزار فراهم می‌کنند.

## نمونه‌هایی از استفاده از ابزار با چارچوب‌های عاملی

در اینجا چند مثال از چگونگی پیاده‌سازی الگوی طراحی استفاده از ابزار با استفاده از چارچوب‌های عاملی مختلف ارائه شده است:

### چارچوب عامل مایکروسافت

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">چارچوب عامل مایکروسافت</a> یک چارچوب هوش مصنوعی متن‌باز برای ساخت عامل‌های هوش مصنوعی است. این چارچوب فرآیند استفاده از فراخوانی تابع را ساده می‌کند، به گونه‌ای که شما می‌توانید ابزارها را به عنوان توابع پایتون با دکوراتور `@tool` تعریف کنید. چارچوب ارتباط دوطرفه بین مدل و کد شما را مدیریت می‌کند. همچنین دسترسی به ابزارهای پیش‌ساخته مثل جستجوی فایل و مفسر کد را از طریق `AzureAIProjectAgentProvider` فراهم می‌کند.

نمودار زیر فرآیند فراخوانی تابع با چارچوب عامل مایکروسافت را نشان می‌دهد:

![function calling](../../../translated_images/fa/functioncalling-diagram.a84006fc287f6014.webp)

در چارچوب عامل مایکروسافت، ابزارها به عنوان توابع دکوراتور شده تعریف می‌شوند. می‌توانیم تابع `get_current_time` که پیش‌تر دیدیم را به یک ابزار با استفاده از دکوراتور `@tool` تبدیل کنیم. چارچوب به صورت خودکار تابع و پارامترهایش را سریال‌سازی می‌کند و شمایی برای ارسال به LLM ایجاد می‌کند.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# کلاینت را ایجاد کنید
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# یک نماینده ایجاد کرده و با ابزار اجرا کنید
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### سرویس عامل هوش مصنوعی آژور

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">سرویس عامل هوش مصنوعی آژور</a> یک چارچوب عاملی جدید است که توسعه‌دهندگان را قادر می‌سازد تا به صورت امن، عامل‌های هوش مصنوعی متنوع، قابل گسترش و با کیفیت بالا را بدون نیاز به مدیریت منابع محاسباتی و ذخیره‌سازی زیرین بسازند، مستقر کنند و مقیاس دهند. این سرویس به ویژه برای برنامه‌های سازمانی مفید است چون به صورت کاملاً مدیریت شده با امنیت سطح سازمانی ارائه می‌شود.

در مقایسه با توسعه مستقیم با API مدل‌های زبانی بزرگ، سرویس عامل هوش مصنوعی آژور مزایایی دارد مانند:

- فراخوانی خودکار ابزار — نیازی به تجزیه فراخوان ابزار، اجرای ابزار و مدیریت پاسخ نیست؛ همه این‌ها اکنون در طرف سرور انجام می‌شود
- مدیریت امن داده‌ها — به جای مدیریت حالت گفت‌وگو خودتان، می‌توانید روی threads برای ذخیره تمام اطلاعات مورد نیاز حساب کنید
- ابزارهای آماده — ابزارهایی که می‌توانید برای تعامل با منابع داده خود استفاده کنید، مانند Bing، جستجوی Azure AI، و Azure Functions.

ابزارهای موجود در سرویس عامل هوش مصنوعی آژور به دو دسته تقسیم می‌شوند:

1. ابزارهای دانش:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">مبنایابی با جستجوی Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">جستجوی فایل</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">جستجوی Azure AI</a>

2. ابزارهای عملیاتی:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">فراخوانی تابع</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">مفسر کد</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">ابزارهای تعریف شده توسط OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

سرویس عامل به ما اجازه می‌دهد این ابزارها را به صورت یک `مجموعه ابزار` استفاده کنیم. همچنین از `threads` استفاده می‌کند که سابقه پیام‌ها در یک گفت‌وگوی مشخص را پیگیری می‌کند.

تصور کنید شما یک نماینده فروش در شرکتی به نام Contoso هستید. می‌خواهید یک عامل مکالمه‌ای بسازید که بتواند به سوالات مربوط به داده‌های فروش شما پاسخ دهد.

تصویر زیر نشان می‌دهد چگونه می‌توان از سرویس عامل هوش مصنوعی آژور برای تحلیل داده‌های فروش استفاده کرد:

![Agentic Service In Action](../../../translated_images/fa/agent-service-in-action.34fb465c9a84659e.webp)

برای استفاده از هر یک از این ابزارها با سرویس، می‌توانیم یک کلاینت بسازیم و یک ابزار یا مجموعه ابزار تعریف کنیم. برای پیاده‌سازی عملی می‌توانیم از کد پایتون زیر استفاده کنیم. LLM قادر خواهد بود به مجموعه ابزار نگاه کرده و تصمیم بگیرد که آیا از تابع ایجاد شده توسط کاربر، `fetch_sales_data_using_sqlite_query`، یا مفسر کد پیش‌ساخته بسته به درخواست کاربر استفاده کند.

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

# مقداردهی اولیه ابزار مفسر کد و اضافه کردن آن به مجموعه ابزار.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ملاحظات ویژه برای استفاده از الگوی طراحی استفاده از ابزار جهت ساخت عامل‌های هوش مصنوعی قابل اعتماد چیست؟

نگرانی رایج درباره SQL تولید شده به صورت پویا توسط LLMها امنیت است، به خصوص خطر تزریق SQL یا اقدامات مخرب مانند حذف یا دستکاری پایگاه داده. در حالی که این نگرانی‌ها معتبر هستند، می‌توان با تنظیم مناسب مجوزهای دسترسی به پایگاه داده به طور مؤثری آنها را کاهش داد. برای اکثر پایگاه داده‌ها این شامل تنظیم پایگاه داده به حالت فقط خواندنی است. برای سرویس‌های پایگاه داده‌ای مانند PostgreSQL یا Azure SQL، باید به اپلیکیشن نقش فقط خواندنی (SELECT) اختصاص داده شود.

اجرای اپلیکیشن در یک محیط امن، محافظت را بیشتر می‌کند. در سناریوهای سازمانی، داده‌ها معمولاً از سیستم‌های عملیاتی استخراج و تبدیل شده و به یک پایگاه داده یا انبار داده فقط خواندنی با شمایه کاربرپسند منتقل می‌شوند. این رویکرد تضمین می‌کند که داده‌ها امن، بهینه برای کارایی و دسترسی آسان هستند و اپلیکیشن به صورت محدود و فقط خواندنی به داده‌ها دسترسی دارد.

## نمونه کدها

- پایتون: [چارچوب عامل](./code_samples/04-python-agent-framework.ipynb)
- دات‌نت: [چارچوب عامل](./code_samples/04-dotnet-agent-framework.md)

## سوالات بیشتر درباره الگوی طراحی استفاده از ابزار دارید؟

به [دیسکورد Microsoft Foundry](https://aka.ms/ai-agents/discord) بپیوندید تا با سایر یادگیرندگان ملاقات کنید، در ساعات حضور در دفتر شرکت کنید و سوالات خود درباره عامل‌های هوش مصنوعی را مطرح کنید.

## منابع اضافی

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">کارگاه سرویس عامل‌های هوش مصنوعی آژور</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">کارگاه نویسنده خلاق کنتوسو چند عاملی</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">بررسی چارچوب عامل مایکروسافت</a>

## درس قبلی

[درک الگوهای طراحی عاملی](../03-agentic-design-patterns/README.md)

## درس بعدی
[RAG عاملیت‌گرا](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->