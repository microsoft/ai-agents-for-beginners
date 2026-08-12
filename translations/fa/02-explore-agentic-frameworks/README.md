[![کاوش در چارچوب‌های عامل هوش مصنوعی](../../../translated_images/fa/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(برای مشاهده ویدیوی این درس روی تصویر بالا کلیک کنید)_

# کاوش در چارچوب‌های عامل هوش مصنوعی

چارچوب‌های عامل هوش مصنوعی پلتفرم‌های نرم‌افزاری طراحی شده برای ساده‌سازی ساخت، پیاده‌سازی و مدیریت عوامل هوش مصنوعی هستند. این چارچوب‌ها برای توسعه‌دهندگان اجزای از پیش ساخته شده، انتزاعات و ابزارهایی فراهم می‌کنند که توسعه سیستم‌های پیچیده هوش مصنوعی را تسهیل می‌کنند.

این چارچوب‌ها به توسعه‌دهندگان کمک می‌کنند تا با ارائه رویکردهای استاندارد شده برای چالش‌های رایج در توسعه عامل‌های هوش مصنوعی، روی جنبه‌های منحصر به فرد برنامه‌های خود تمرکز کنند. آن‌ها قابلیت مقیاس‌پذیری، دسترسی‌پذیری و بهره‌وری در ساخت سیستم‌های هوش مصنوعی را افزایش می‌دهند.

## مقدمه

این درس موارد زیر را پوشش می‌دهد:

- چارچوب‌های عوامل هوش مصنوعی چیستند و چه دستاوردهایی برای توسعه‌دهندگان فراهم می‌کنند؟
- تیم‌ها چگونه می‌توانند از آن‌ها برای نمونه‌سازی سریع، تکرار و بهبود قابلیت‌های عامل خود استفاده کنند؟
- تفاوت میان چارچوب‌ها و ابزارهای ساخته شده توسط مایکروسافت (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> و <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) چیست؟
- آیا می‌توانم ابزارهای اکوسیستم Azure موجود خود را مستقیماً ادغام کنم یا نیاز به راه‌حل‌های مستقل دارم؟
- Microsoft Foundry Agent Service چیست و چگونه به من کمک می‌کند؟

## اهداف یادگیری

هدف این درس کمک به شما در درک موارد زیر است:

- نقش چارچوب‌های عامل هوش مصنوعی در توسعه هوش مصنوعی.
- چگونگی بهره‌برداری از چارچوب‌های عامل هوش مصنوعی برای ساخت عوامل هوشمند.
- قابلیت‌های کلیدی که توسط چارچوب‌های عامل هوش مصنوعی فعال می‌شود.
- تفاوت‌های میان Microsoft Agent Framework و Microsoft Foundry Agent Service.

## چارچوب‌های عامل هوش مصنوعی چیستند و چه کاری برای توسعه‌دهندگان امکان‌پذیر می‌کنند؟

چارچوب‌های سنتی هوش مصنوعی می‌توانند به شما کمک کنند AI را در برنامه‌های خود ادغام کنید و این برنامه‌ها را به روش‌های زیر بهبود دهید:

- **شخصی‌سازی**: هوش مصنوعی می‌تواند رفتار و ترجیحات کاربر را تحلیل کند تا توصیه‌ها، محتوا و تجربه‌های شخصی سازی شده ارائه دهد.
مثال: سرویس‌های پخش مانند نتفلیکس از هوش مصنوعی برای پیشنهاد فیلم‌ها و برنامه‌ها بر اساس تاریخچه نمایش استفاده می‌کنند و تعامل و رضایت کاربر را افزایش می‌دهند.
- **اتوماسیون و بهره‌وری**: هوش مصنوعی می‌تواند وظایف تکراری را خودکار کند، جریان‌های کاری را ساده کند و بهره‌وری عملیاتی را بهبود بخشد.
مثال: برنامه‌های خدمات مشتری از چت‌بات‌های مجهز به هوش مصنوعی برای رسیدگی به پرسش‌های متداول استفاده می‌کنند که زمان پاسخ را کاهش داده و عوامل انسانی را برای مسایل پیچیده‌تر آزاد می‌کند.
- **بهبود تجربه کاربر**: هوش مصنوعی می‌تواند تجربه کلی کاربر را با ارائه ویژگی‌های هوشمند مانند تشخیص صدا، پردازش زبان طبیعی و متن پیش‌بینی‌شده ارتقاء دهد.
مثال: دستیارهای مجازی مانند Siri و Google Assistant از هوش مصنوعی برای درک و پاسخ به دستورات صوتی استفاده می‌کنند و تعامل کاربران با دستگاه‌ها را آسان‌تر می‌کنند.

### این همه عالی به نظر می‌رسد، پس چرا به چارچوب عامل هوش مصنوعی نیاز داریم؟

چارچوب‌های عامل هوش مصنوعی چیزی فراتر از چارچوب‌های AI معمولی هستند. آن‌ها طراحی شده‌اند تا ساخت عوامل هوشمند را که می‌توانند با کاربران، دیگر عوامل و محیط تعامل کنند تا اهداف مشخصی را محقق سازند، ممکن کنند. این عوامل می‌توانند رفتار خودمختار نشان دهند، تصمیم‌گیری کنند و به شرایط در حال تغییر سازگار شوند. بیایید به برخی قابلیت‌های کلیدی فعال شده توسط چارچوب‌های عامل هوش مصنوعی نگاه کنیم:

- **همکاری و هماهنگی عوامل**: امکان ساخت چند عامل AI که می‌توانند با هم کار کنند، ارتباط برقرار سازند و هماهنگ شوند تا وظایف پیچیده را حل کنند.
- **اتوماسیون و مدیریت وظایف**: فراهم کردن مکانیزم‌هایی برای اتوماسیون جریان‌های کاری چند مرحله‌ای، واگذاری وظایف و مدیریت پویا در میان عوامل.
- **درک زمینه‌ای و سازگاری**: تجهیز عوامل با توانایی درک زمینه، سازگاری با محیط‌های متغیر و تصمیم‌گیری بر اساس اطلاعات زمان واقعی.

پس به طور خلاصه، عوامل به شما اجازه می‌دهند بیشتر کار کنید، اتوماسیون را به سطح بالاتری ببرید، و سیستم‌های هوشمندتری بسازید که قادر به سازگاری و یادگیری از محیط خود هستند.

## چگونه قابلیت‌های عامل را سریع نمونه‌سازی، تکرار و بهبود دهیم؟

این حوزه سریع در حال پیشرفت است، اما برخی موارد در بیشتر چارچوب‌های عامل هوش مصنوعی مشترک هستند که به شما کمک می‌کنند سریع نمونه‌سازی و تکرار کنید، از جمله اجزای مدولار، ابزارهای همکاری و یادگیری زمان واقعی. بیایید به این موارد بپردازیم:

- **استفاده از اجزای مدولار**: کیت‌های توسعه نرم‌افزار (SDK) هوش مصنوعی اجزای از پیش ساخته شده‌ای مانند اتصال‌دهنده‌های AI و حافظه، فراخوانی تابع با زبان طبیعی یا افزونه‌های کد، قالب‌های پرامپت و غیره ارائه می‌دهند.
- **بهره‌گیری از ابزارهای همکاری**: طراحی عوامل با نقش‌ها و وظایف خاص، که امکان آزمایش و اصلاح جریان‌های کاری مشترک را می‌دهد.
- **یادگیری در زمان واقعی**: اجرای حلقه‌های بازخورد که در آن عوامل از تعاملات یاد می‌گیرند و رفتار خود را به طور پویا تنظیم می‌کنند.

### استفاده از اجزای مدولار

کیت‌های توسعه مانند Microsoft Agent Framework اجزای از پیش ساخته‌ای مانند اتصال‌دهنده‌های AI، تعاریف ابزار و مدیریت عامل ارائه می‌دهند.

**نحوه استفاده تیم‌ها**: تیم‌ها می‌توانند این اجزا را سریع جمع کنند تا نمونه اولیه عملیاتی بسازند بدون شروع از صفر، که این امکان را برای آزمایش و تکرار سریع فراهم می‌کند.

**کارکرد در عمل**: شما می‌توانید از یک پارسر از پیش ساخته شده برای استخراج اطلاعات از ورودی کاربر، یک ماژول حافظه برای ذخیره و بازیابی داده‌ها و یک تولیدکننده پرامپت برای تعامل با کاربران استفاده کنید، همه این‌ها بدون نیاز به ساخت این اجزا از ابتدا.

**نمونه کد**. بیایید نمونه‌ای از استفاده Microsoft Agent Framework با `FoundryChatClient` را ببینیم که مدل به ورودی کاربر با فراخوانی ابزار پاسخ می‌دهد:

``` python
# نمونه چارچوب Microsoft Agent به زبان پایتون

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# تعریف یک تابع نمونه ابزار برای رزرو سفر
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # خروجی نمونه: پرواز شما به نیویورک در اول ژانویه ۲۰۲۵ با موفقیت رزرو شد. سفر خوش! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

آنچه از این مثال می‌بینید این است که چگونه می‌توانید از یک پارسر از پیش ساخته شده برای استخراج اطلاعات کلیدی از ورودی کاربر، مانند مبدا، مقصد و تاریخ درخواست رزرو پرواز استفاده کنید. این رویکرد مدولار به شما اجازه می‌دهد روی منطق در سطح بالا تمرکز کنید.

### بهره‌گیری از ابزارهای همکاری

چارچوب‌هایی مانند Microsoft Agent Framework امکان ساخت چند عامل که می‌توانند با هم کار کنند را فراهم می‌آورند.

**نحوه استفاده تیم‌ها**: تیم‌ها می‌توانند عوامل با نقش‌ها و وظایف خاص طراحی کنند تا بتوانند جریان‌های کاری مشترک را آزمایش و بهبود دهند و بهره‌وری کلی سیستم را افزایش دهند.

**کارکرد در عمل**: شما می‌توانید یک تیم از عوامل بسازید که هر کدام عملکرد تخصصی دارند، مانند بازیابی داده، تحلیل یا تصمیم‌گیری. این عوامل می‌توانند به هم اطلاعات منتقل کنند و همکاری کنند تا هدف مشترکی مانند پاسخ به پرسش کاربر یا تکمیل یک وظیفه را محقق سازند.

**نمونه کد (Microsoft Agent Framework)**:

```python
# ایجاد چندین عامل که با استفاده از چارچوب عامل مایکروسافت با هم کار می‌کنند

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# عامل بازیابی داده
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# عامل تحلیل داده
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# اجرای عوامل به ترتیب بر روی یک وظیفه
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

آنچه در کد قبلی مشاهده می‌کنید این است که چگونه می‌توانید وظیفه‌ای را ایجاد کنید که شامل همکاری چند عامل برای تحلیل داده است. هر عامل عملکرد خاصی دارد و وظیفه از طریق هماهنگی عوامل برای رسیدن به نتیجه مطلوب اجرا می‌شود. با ایجاد عوامل اختصاصی با نقش‌های تخصصی، می‌توانید کارایی و عملکرد وظایف را بهبود دهید.

### یادگیری در زمان واقعی

چارچوب‌های پیشرفته قابلیت‌های درک زمینه و سازگاری در زمان واقعی را فراهم می‌کنند.

**نحوه استفاده تیم‌ها**: تیم‌ها می‌توانند حلقه‌های بازخورد را پیاده‌سازی کنند که در آن عوامل از تعاملات می‌آموزند و رفتار خود را به طور پویا تنظیم می‌کنند که منجر به بهبود و پالایش مستمر قابلیت‌ها می‌شود.

**کارکرد در عمل**: عوامل می‌توانند بازخورد کاربران، داده‌های محیطی و نتایج وظایف را تحلیل کنند تا پایگاه دانش خود را به‌روزرسانی کنند، الگوریتم‌های تصمیم‌گیری را تنظیم کنند و عملکرد را به مرور زمان بهبود بخشند. این فرآیند یادگیری تکراری به عوامل اجازه می‌دهد به شرایط و ترجیحات تغییر یافته کاربران سازگار شوند و اثربخشی کلی سیستم را افزایش دهند.

## تفاوت‌های Microsoft Agent Framework و Microsoft Foundry Agent Service چیست؟

روش‌های زیادی برای مقایسه این دو وجود دارد، اما بیایید به برخی تفاوت‌های کلیدی در طراحی، قابلیت‌ها و موارد استفاده هدفمند آن‌ها نگاه کنیم:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework یک کیت توسعه نرم‌افزار ساده ارائه می‌دهد برای ساخت عوامل هوش مصنوعی با استفاده از `FoundryChatClient`. این چارچوب به توسعه‌دهندگان امکان می‌دهد عوامل بسازند که از مدل‌های Azure OpenAI با فراخوانی ابزار داخلی، مدیریت گفتگو و امنیت سازمانی از طریق هویت Azure بهره‌مند می‌شوند.

**موارد استفاده**: ساخت عوامل هوش مصنوعی آماده تولید با استفاده از ابزارها، جریان‌های کاری چند مرحله‌ای و سناریوهای یکپارچگی سازمانی.

در اینجا برخی مفاهیم کلیدی Microsoft Agent Framework آورده شده است:

- **عوامل**. عامل از طریق `FoundryChatClient` ساخته می‌شود و با نام، دستورالعمل‌ها و ابزارها پیکربندی می‌شود. عامل می‌تواند:
  - **پردازش پیام‌های کاربر** و تولید پاسخ با استفاده از مدل‌های Azure OpenAI.
  - **فراخوانی خودکار ابزارها** بر اساس زمینه گفتگو.
  - **نگهداری وضعیت گفتگو** در تعاملات متعدد.

  این یک قطعه کد است که نحوه ساخت یک عامل را نشان می‌دهد:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **ابزارها**. چارچوب از تعریف ابزارها به عنوان توابع پایتون که عامل می‌تواند به صورت خودکار فراخوانی کند پشتیبانی می‌کند. ابزارها هنگام ایجاد عامل ثبت می‌شوند:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **هماهنگی چند عاملی**. می‌توانید چندین عامل با تخصص‌های مختلف ایجاد کنید و کار آن‌ها را هماهنگ کنید:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **ادغام هویت Azure**. چارچوب از `AzureCliCredential` (یا `DefaultAzureCredential`) برای احراز هویت ایمن و بدون نیاز به مدیریت کلید API استفاده می‌کند.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service افزودنی جدیدتری است که در Microsoft Ignite 2024 معرفی شده است. این امکان توسعه و استقرار عامل‌های AI را با مدل‌های انعطاف‌پذیرتر فراهم می‌کند، مانند فراخوانی مستقیم مدل‌های متن‌باز LLM مانند Llama 3، Mistral و Cohere.

Microsoft Foundry Agent Service مکانیزم‌های امنیتی سازمانی قوی‌تر و روش‌های ذخیره‌سازی داده ارائه می‌دهد که آن را برای برنامه‌های سازمانی مناسب می‌سازد.

این سرویس به صورت یکپارچه با Microsoft Agent Framework برای ساخت و استقرار عوامل کار می‌کند.

این سرویس در حال حاضر در نمایه عمومی (Public Preview) است و پشتیبانی از پایتون و C# برای ساخت عوامل دارد.

با استفاده از کیت توسعه Microsoft Foundry Agent Service برای پایتون، می‌توانیم یک عامل با ابزار تعریف شده توسط کاربر ایجاد کنیم:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# توابع ابزار را تعریف کنید
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### مفاهیم کلیدی

Microsoft Foundry Agent Service مفاهیم کلیدی زیر را دارد:

- **عامل**. Microsoft Foundry Agent Service با Microsoft Foundry ادغام می‌شود. در Microsoft Foundry، یک عامل AI به عنوان یک میکروسرویس "هوشمند" عمل می‌کند که می‌تواند برای پاسخ به سوالات (RAG)، انجام اقدامات یا اتوماسیون کامل جریان‌های کاری استفاده شود. این با ترکیب قدرت مدل‌های تولیدی AI و ابزارهایی که به عامل اجازه می‌دهند به منابع داده دنیای واقعی دسترسی داشته باشد و تعامل کند، محقق می‌شود. در اینجا یک نمونه عامل آورده شده است:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    در این مثال، عاملی با مدل `gpt-5-mini`، نام `my-agent` و دستورالعمل‌ها `You are helpful agent` ساخته شده است. عامل با ابزارها و منابع برای انجام وظایف تفسیر کد مجهز شده است.

- **رشته و پیام‌ها**. رشته (Thread) مفهوم مهم دیگری است. این نشان‌دهنده یک گفتگو یا تعامل بین عامل و کاربر است. رشته‌ها می‌توانند برای پیگیری پیشرفت گفتگو، ذخیره اطلاعات زمینه‌ای و مدیریت وضعیت تعامل استفاده شوند. در اینجا نمونه‌ای از یک رشته آورده شده است:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # از عامل بخواهید تا روی رشته کار انجام دهد
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # تمامی پیام‌ها را واکشی و ثبت کنید تا پاسخ عامل را ببینید
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    در کد قبلی، یک رشته ایجاد شده است. سپس پیامی به این رشته ارسال شده است. با فراخوانی `create_and_process_run` از عامل خواسته شده روی رشته کار انجام دهد. در نهایت، پیام‌ها واکشی و ثبت شده‌اند تا پاسخ عامل مشاهده شود. پیام‌ها پیشرفت گفتگو بین کاربر و عامل را نشان می‌دهند. همچنین مهم است بدانید که پیام‌ها می‌توانند انواع مختلفی مثل متن، تصویر یا فایل باشند، مثلاً کار عامل منجر به ایجاد یک تصویر یا پاسخ متنی شده است. به عنوان توسعه‌دهنده، می‌توانید این اطلاعات را برای پردازش بیشتر پاسخ یا نمایش به کاربر استفاده کنید.

- **ادغام با Microsoft Agent Framework**. Microsoft Foundry Agent Service به طور بدون درز با Microsoft Agent Framework کار می‌کند، به این معنی که می‌توانید عوامل را با استفاده از `FoundryChatClient` بسازید و آن‌ها را برای سناریوهای تولید از طریق Agent Service منتشر کنید.

**موارد استفاده**: Microsoft Foundry Agent Service برای برنامه‌های سازمانی طراحی شده است که نیاز به استقرار عامل هوش مصنوعی ایمن، مقیاس‌پذیر و انعطاف‌پذیر دارند.

## تفاوت این رویکردها چیست؟
 
به نظر می‌رسد که تداخل وجود دارد، اما تفاوت‌های کلیدی در طراحی، قابلیت‌ها و موارد استفاده هدفمند وجود دارد:
 
- **Microsoft Agent Framework (MAF)**: یک کیت توسعه نرم‌افزار آماده تولید برای ساخت عوامل AI است. API ساده‌شده‌ای برای ایجاد عامل‌ها با فراخوانی ابزار، مدیریت گفتگو و یکپارچه‌سازی هویت Azure ارائه می‌دهد.
- **Microsoft Foundry Agent Service**: یک پلتفرم و سرویس استقرار در Microsoft Foundry برای عوامل است. اتصال داخلی به سرویس‌هایی مانند Azure OpenAI، Azure AI Search، Bing Search و اجرای کد فراهم می‌کند.
 
هنوز مطمئن نیستید کدام را انتخاب کنید؟

### موارد استفاده
 
بیایید ببینیم آیا می‌توانیم با مرور برخی موارد استفاده رایج به شما کمک کنیم:
 
> سوال: من در حال ساخت برنامه‌های تولیدی عامل هوش مصنوعی هستم و می‌خواهم سریع شروع کنم
>

> پاسخ: Microsoft Agent Framework انتخاب عالی است. API ساده و پایتونیکی از طریق `FoundryChatClient` ارائه می‌دهد که به شما اجازه می‌دهد عوامل را با ابزارها و دستورالعمل‌ها فقط در چند خط کد تعریف کنید.

> سوال: من به استقرار سازمانی با یکپارچه‌سازی Azure مثل جستجو و اجرای کد نیاز دارم
>
> پاسخ: Microsoft Foundry Agent Service بهترین گزینه است. این یک سرویس پلتفرمی است که قابلیت‌های داخلی برای مدل‌های متعدد، Azure AI Search، Bing Search و Azure Functions دارد. ساخت عوامل در پورتال Foundry و استقرار مقیاس‌پذیر آن‌ها آسان است.
 
> سوال: هنوز گیج هستم، فقط یک گزینه بدهید
>
> پاسخ: با Microsoft Agent Framework شروع کنید تا عوامل خود را بسازید، و سپس هنگام نیاز به استقرار و مقیاس‌بندی در تولید از Microsoft Foundry Agent Service استفاده کنید. این رویکرد به شما امکان می‌دهد روی منطق عامل خود سریع تکرار کنید و مسیر روشنی به استقرار سازمانی داشته باشید.
 
بیایید تفاوت‌های کلیدی را در یک جدول خلاصه کنیم:

| چارچوب | تمرکز | مفاهیم کلیدی | موارد استفاده |
| --- | --- | --- | --- |
| Microsoft Agent Framework | کیت توسعه عامل ساده‌شده با فراخوانی ابزار | عوامل، ابزارها، هویت Azure | ساخت عوامل AI، استفاده از ابزار، جریان‌های کاری چند مرحله‌ای |
| Microsoft Foundry Agent Service | مدل‌های انعطاف‌پذیر، امنیت سازمانی، تولید کد، فراخوانی ابزار | مدولار بودن، همکاری، ارکستراسیون فرآیند | استقرار ایمن، مقیاس‌پذیر و انعطاف‌پذیر عامل‌های AI |

## آیا می‌توانم ابزارهای اکوسیستم Azure موجود خود را مستقیماً ادغام کنم یا نیاز به راه‌حل‌های مستقل دارم؟


بله، می‌توانید ابزارهای موجود در اکوسیستم Azure خود را مستقیماً با سرویس Microsoft Foundry Agent ادغام کنید، به خصوص که این سرویس به‌گونه‌ای ساخته شده است که به صورت بی‌نقص با سایر خدمات Azure کار کند. به عنوان مثال می‌توانید Bing، Azure AI Search و Azure Functions را ادغام کنید. همچنین یک ادغام عمیق با Microsoft Foundry وجود دارد.

چارچوب عامل مایکروسافت همچنین از طریق `FoundryChatClient` و هویت Azure با خدمات Azure ادغام می‌شود و به شما امکان می‌دهد مستقیماً از ابزارهای عامل خود به خدمات Azure فراخوانی کنید.

## نمونه کدها

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## سوالات بیشتری درباره چارچوب‌های عامل هوش مصنوعی دارید؟

به [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) بپیوندید تا با دیگر یادگیرندگان ملاقات کنید، در ساعات اداری شرکت کنید و به سوالات خود درباره عوامل هوش مصنوعی پاسخ بگیرید.

## منابع

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">سرویس عامل Azure</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">چارچوب عامل مایکروسافت - پاسخ‌های Azure OpenAI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">سرویس عامل Microsoft Foundry</a>

## درس قبلی

[معرفی عوامل هوش مصنوعی و موارد استفاده از عامل](../01-intro-to-ai-agents/README.md)

## درس بعدی

[درک الگوهای طراحی عاملی](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->