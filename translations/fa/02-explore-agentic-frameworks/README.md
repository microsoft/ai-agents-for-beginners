<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T11:07:01+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "fa"
}
-->
[![کاوش در چارچوب‌های عامل هوش مصنوعی](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.fa.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(برای مشاهده ویدئوی این درس روی تصویر بالا کلیک کنید)_

# کاوش در چارچوب‌های عامل هوش مصنوعی

چارچوب‌های عامل هوش مصنوعی پلتفرم‌های نرم‌افزاری هستند که برای ساده‌سازی ایجاد، استقرار و مدیریت عوامل هوش مصنوعی طراحی شده‌اند. این چارچوب‌ها به توسعه‌دهندگان اجزای از پیش ساخته‌شده، انتزاعات و ابزارهایی ارائه می‌دهند که توسعه سیستم‌های پیچیده هوش مصنوعی را تسهیل می‌کنند.

این چارچوب‌ها با ارائه رویکردهای استاندارد برای چالش‌های رایج در توسعه عوامل هوش مصنوعی، به توسعه‌دهندگان کمک می‌کنند تا بر جنبه‌های منحصربه‌فرد برنامه‌های خود تمرکز کنند. آن‌ها مقیاس‌پذیری، دسترسی‌پذیری و کارایی را در ساخت سیستم‌های هوش مصنوعی افزایش می‌دهند.

## مقدمه

این درس شامل موارد زیر خواهد بود:

- چارچوب‌های عامل هوش مصنوعی چیستند و چه قابلیت‌هایی را برای توسعه‌دهندگان فراهم می‌کنند؟
- تیم‌ها چگونه می‌توانند از این چارچوب‌ها برای نمونه‌سازی سریع، تکرار و بهبود قابلیت‌های عامل خود استفاده کنند؟
- تفاوت‌های بین چارچوب‌ها و ابزارهای ایجادشده توسط مایکروسافت <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>، <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a> و <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> چیست؟
- آیا می‌توانم ابزارهای موجود در اکوسیستم Azure خود را مستقیماً ادغام کنم یا به راه‌حل‌های مستقل نیاز دارم؟
- سرویس Azure AI Agents چیست و چگونه به من کمک می‌کند؟

## اهداف یادگیری

اهداف این درس کمک به شما برای درک موارد زیر است:

- نقش چارچوب‌های عامل هوش مصنوعی در توسعه هوش مصنوعی.
- نحوه استفاده از چارچوب‌های عامل هوش مصنوعی برای ساخت عوامل هوشمند.
- قابلیت‌های کلیدی که توسط چارچوب‌های عامل هوش مصنوعی فراهم می‌شوند.
- تفاوت‌های بین AutoGen، Semantic Kernel و Azure AI Agent Service.

## چارچوب‌های عامل هوش مصنوعی چیستند و چه قابلیت‌هایی را برای توسعه‌دهندگان فراهم می‌کنند؟

چارچوب‌های سنتی هوش مصنوعی می‌توانند به شما کمک کنند تا هوش مصنوعی را در برنامه‌های خود ادغام کنید و این برنامه‌ها را به روش‌های زیر بهبود بخشید:

- **شخصی‌سازی**: هوش مصنوعی می‌تواند رفتار و ترجیحات کاربران را تحلیل کند تا پیشنهادات، محتوا و تجربیات شخصی‌سازی‌شده ارائه دهد.  
مثال: سرویس‌های استریم مانند نتفلیکس از هوش مصنوعی برای پیشنهاد فیلم‌ها و برنامه‌ها بر اساس تاریخچه مشاهده استفاده می‌کنند و تعامل و رضایت کاربران را افزایش می‌دهند.
- **اتوماسیون و کارایی**: هوش مصنوعی می‌تواند وظایف تکراری را خودکار کند، جریان‌های کاری را ساده کند و کارایی عملیاتی را بهبود بخشد.  
مثال: برنامه‌های خدمات مشتری از چت‌بات‌های مجهز به هوش مصنوعی برای پاسخگویی به سوالات رایج استفاده می‌کنند، زمان پاسخگویی را کاهش می‌دهند و نمایندگان انسانی را برای مسائل پیچیده‌تر آزاد می‌کنند.
- **تجربه کاربری بهبود‌یافته**: هوش مصنوعی می‌تواند تجربه کلی کاربر را با ارائه ویژگی‌های هوشمند مانند تشخیص صدا، پردازش زبان طبیعی و متن پیش‌بینی‌کننده بهبود بخشد.  
مثال: دستیارهای مجازی مانند سیری و گوگل اسیستنت از هوش مصنوعی برای درک و پاسخ به دستورات صوتی استفاده می‌کنند و تعامل کاربران با دستگاه‌هایشان را آسان‌تر می‌کنند.

### همه این‌ها عالی به نظر می‌رسد، پس چرا به چارچوب عامل هوش مصنوعی نیاز داریم؟

چارچوب‌های عامل هوش مصنوعی چیزی فراتر از چارچوب‌های هوش مصنوعی هستند. آن‌ها برای ایجاد عوامل هوشمندی طراحی شده‌اند که می‌توانند با کاربران، عوامل دیگر و محیط تعامل داشته باشند تا به اهداف خاصی دست یابند. این عوامل می‌توانند رفتار خودمختار نشان دهند، تصمیم‌گیری کنند و به شرایط متغیر سازگار شوند. بیایید به برخی از قابلیت‌های کلیدی که توسط چارچوب‌های عامل هوش مصنوعی فراهم می‌شوند نگاهی بیندازیم:

- **همکاری و هماهنگی عوامل**: امکان ایجاد چندین عامل هوش مصنوعی که می‌توانند با یکدیگر کار کنند، ارتباط برقرار کنند و برای حل وظایف پیچیده هماهنگ شوند.
- **اتوماسیون و مدیریت وظایف**: ارائه مکانیزم‌هایی برای خودکارسازی جریان‌های کاری چندمرحله‌ای، واگذاری وظایف و مدیریت پویا وظایف بین عوامل.
- **درک و سازگاری با زمینه**: تجهیز عوامل به توانایی درک زمینه، سازگاری با محیط‌های متغیر و تصمیم‌گیری بر اساس اطلاعات بلادرنگ.

به طور خلاصه، عوامل به شما امکان می‌دهند کارهای بیشتری انجام دهید، اتوماسیون را به سطح بعدی ببرید و سیستم‌های هوشمندتری ایجاد کنید که می‌توانند از محیط خود یاد بگیرند و سازگار شوند.

## چگونه می‌توان به سرعت قابلیت‌های عامل را نمونه‌سازی، تکرار و بهبود بخشید؟

این حوزه به سرعت در حال پیشرفت است، اما برخی موارد در اکثر چارچوب‌های عامل هوش مصنوعی مشترک هستند که می‌توانند به شما در نمونه‌سازی سریع و تکرار کمک کنند، از جمله اجزای ماژولار، ابزارهای همکاری و یادگیری بلادرنگ. بیایید به این موارد بپردازیم:

- **استفاده از اجزای ماژولار**: SDKهای هوش مصنوعی اجزای از پیش ساخته‌شده‌ای مانند کانکتورهای هوش مصنوعی و حافظه، فراخوانی توابع با استفاده از زبان طبیعی یا افزونه‌های کد، قالب‌های درخواست و موارد دیگر ارائه می‌دهند.
- **استفاده از ابزارهای همکاری**: طراحی عوامل با نقش‌ها و وظایف خاص، که امکان آزمایش و اصلاح جریان‌های کاری همکاری را فراهم می‌کند.
- **یادگیری بلادرنگ**: پیاده‌سازی حلقه‌های بازخورد که در آن عوامل از تعاملات یاد می‌گیرند و رفتار خود را به صورت پویا تنظیم می‌کنند.

### استفاده از اجزای ماژولار

SDKهایی مانند Microsoft Semantic Kernel و LangChain اجزای از پیش ساخته‌شده‌ای مانند کانکتورهای هوش مصنوعی، قالب‌های درخواست و مدیریت حافظه ارائه می‌دهند.

**چگونه تیم‌ها می‌توانند از این موارد استفاده کنند**: تیم‌ها می‌توانند این اجزا را به سرعت مونتاژ کنند تا یک نمونه اولیه کاربردی ایجاد کنند، بدون اینکه از ابتدا شروع کنند، و این امکان را برای آزمایش و تکرار سریع فراهم می‌کند.

**چگونه در عمل کار می‌کند**: شما می‌توانید از یک تجزیه‌کننده از پیش ساخته‌شده برای استخراج اطلاعات از ورودی کاربر، یک ماژول حافظه برای ذخیره و بازیابی داده‌ها و یک تولیدکننده درخواست برای تعامل با کاربران استفاده کنید، بدون اینکه نیاز به ساخت این اجزا از ابتدا داشته باشید.

**کد نمونه**. بیایید به نمونه‌هایی از نحوه استفاده از یک کانکتور هوش مصنوعی از پیش ساخته‌شده با Semantic Kernel Python و .Net که از فراخوانی خودکار توابع برای پاسخ به ورودی کاربر استفاده می‌کند، نگاهی بیندازیم:

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```

آنچه از این مثال می‌بینید این است که چگونه می‌توانید از یک تجزیه‌کننده از پیش ساخته‌شده برای استخراج اطلاعات کلیدی از ورودی کاربر، مانند مبدا، مقصد و تاریخ درخواست رزرو پرواز استفاده کنید. این رویکرد ماژولار به شما امکان می‌دهد بر منطق سطح بالا تمرکز کنید.

### استفاده از ابزارهای همکاری

چارچوب‌هایی مانند CrewAI، Microsoft AutoGen و Semantic Kernel امکان ایجاد چندین عامل که می‌توانند با یکدیگر کار کنند را فراهم می‌کنند.

**چگونه تیم‌ها می‌توانند از این موارد استفاده کنند**: تیم‌ها می‌توانند عواملی با نقش‌ها و وظایف خاص طراحی کنند، که امکان آزمایش و اصلاح جریان‌های کاری همکاری و بهبود کارایی کلی سیستم را فراهم می‌کند.

**چگونه در عمل کار می‌کند**: شما می‌توانید تیمی از عوامل ایجاد کنید که هر عامل دارای یک عملکرد تخصصی باشد، مانند بازیابی داده‌ها، تحلیل یا تصمیم‌گیری. این عوامل می‌توانند برای دستیابی به یک هدف مشترک، مانند پاسخ به یک پرسش کاربر یا تکمیل یک وظیفه، ارتباط برقرار کنند و اطلاعات را به اشتراک بگذارند.

**کد نمونه (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

آنچه در کد قبلی می‌بینید این است که چگونه می‌توانید یک وظیفه را ایجاد کنید که شامل چندین عامل است که با هم برای تحلیل داده‌ها کار می‌کنند. هر عامل یک عملکرد خاص را انجام می‌دهد و وظیفه با هماهنگی عوامل برای دستیابی به نتیجه مطلوب اجرا می‌شود. با ایجاد عوامل اختصاصی با نقش‌های تخصصی، می‌توانید کارایی و عملکرد وظایف را بهبود بخشید.

### یادگیری بلادرنگ

چارچوب‌های پیشرفته قابلیت‌هایی برای درک زمینه بلادرنگ و سازگاری فراهم می‌کنند.

**چگونه تیم‌ها می‌توانند از این موارد استفاده کنند**: تیم‌ها می‌توانند حلقه‌های بازخوردی پیاده‌سازی کنند که در آن عوامل از تعاملات یاد می‌گیرند و رفتار خود را به صورت پویا تنظیم می‌کنند، که منجر به بهبود و اصلاح مداوم قابلیت‌ها می‌شود.

**چگونه در عمل کار می‌کند**: عوامل می‌توانند بازخورد کاربران، داده‌های محیطی و نتایج وظایف را تحلیل کنند تا پایگاه دانش خود را به‌روزرسانی کنند، الگوریتم‌های تصمیم‌گیری را تنظیم کنند و عملکرد خود را در طول زمان بهبود بخشند. این فرآیند یادگیری تکراری به عوامل امکان می‌دهد تا به شرایط متغیر و ترجیحات کاربران سازگار شوند و اثربخشی کلی سیستم را افزایش دهند.

## تفاوت‌های بین چارچوب‌های AutoGen، Semantic Kernel و Azure AI Agent Service چیست؟

راه‌های زیادی برای مقایسه این چارچوب‌ها وجود دارد، اما بیایید به برخی از تفاوت‌های کلیدی از نظر طراحی، قابلیت‌ها و موارد استفاده هدف بپردازیم:

## AutoGen

AutoGen یک چارچوب متن‌باز است که توسط آزمایشگاه AI Frontiers مایکروسافت ریسرچ توسعه یافته است. این چارچوب بر برنامه‌های *عامل‌محور* توزیع‌شده و رویدادمحور تمرکز دارد و امکان استفاده از چندین LLM و SLM، ابزارها و الگوهای طراحی پیشرفته چندعاملی را فراهم می‌کند.

AutoGen حول مفهوم اصلی عوامل ساخته شده است، که موجودیت‌های خودمختاری هستند که می‌توانند محیط خود را درک کنند، تصمیم بگیرند و اقداماتی برای دستیابی به اهداف خاص انجام دهند. عوامل از طریق پیام‌های غیرهمزمان ارتباط برقرار می‌کنند، که به آن‌ها امکان می‌دهد به طور مستقل و موازی کار کنند و مقیاس‌پذیری و پاسخگویی سیستم را افزایش دهند.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">عوامل بر اساس مدل بازیگر</a> هستند. طبق ویکی‌پدیا، یک بازیگر _بلوک اصلی محاسبات همزمان است. در پاسخ به پیامی که دریافت می‌کند، یک بازیگر می‌تواند: تصمیمات محلی بگیرد، بازیگران بیشتری ایجاد کند، پیام‌های بیشتری ارسال کند و تعیین کند که چگونه به پیام بعدی که دریافت می‌کند پاسخ دهد_.

**موارد استفاده**: خودکارسازی تولید کد، وظایف تحلیل داده‌ها و ساخت عوامل سفارشی برای برنامه‌ریزی و عملکردهای تحقیقاتی.

در اینجا برخی از مفاهیم اصلی AutoGen آورده شده است:

- **عوامل**. یک عامل یک موجودیت نرم‌افزاری است که:
  - **از طریق پیام‌ها ارتباط برقرار می‌کند**، این پیام‌ها می‌توانند همزمان یا غیرهمزمان باشند.
  - **وضعیت خود را حفظ می‌کند**، که می‌تواند توسط پیام‌های ورودی تغییر کند.
  - **اقداماتی انجام می‌دهد** در پاسخ به پیام‌های دریافتی یا تغییرات در وضعیت خود. این اقدامات ممکن است وضعیت عامل را تغییر دهند و اثرات خارجی ایجاد کنند، مانند به‌روزرسانی گزارش‌های پیام، ارسال پیام‌های جدید، اجرای کد یا انجام تماس‌های API.

  در اینجا یک قطعه کد کوتاه آورده شده است که در آن عامل خود را با قابلیت‌های چت ایجاد می‌کنید:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAgent(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
    در کد قبلی، `MyAgent` ایجاد شده و از `RoutedAgent` به ارث برده شده است. این عامل دارای یک هندلر پیام است که محتوای پیام را چاپ می‌کند و سپس با استفاده از نماینده `AssistantAgent` یک پاسخ ارسال می‌کند. به ویژه توجه کنید که چگونه به `self._delegate` یک نمونه از `AssistantAgent` اختصاص داده شده است که یک عامل از پیش ساخته‌شده است و می‌تواند تکمیل‌های چت را مدیریت کند.

    بیایید AutoGen را از این نوع عامل مطلع کنیم و برنامه را شروع کنیم:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    در کد قبلی، عوامل با زمان اجرا ثبت شده‌اند و سپس یک پیام به عامل ارسال شده است که منجر به خروجی زیر می‌شود:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **چند عامل**. AutoGen از ایجاد چندین عامل که می‌توانند با هم کار کنند برای انجام وظایف پیچیده پشتیبانی می‌کند. عوامل می‌توانند ارتباط برقرار کنند، اطلاعات را به اشتراک بگذارند و اقدامات خود را برای حل مشکلات به طور کارآمد هماهنگ کنند. برای ایجاد یک سیستم چندعاملی، می‌توانید انواع مختلفی از عوامل با عملکردها و نقش‌های تخصصی تعریف کنید، مانند بازیابی داده‌ها، تحلیل، تصمیم‌گیری و تعامل با کاربر. بیایید ببینیم چنین سیستمی چگونه به نظر می‌رسد تا درک بهتری از آن پیدا کنیم:

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

    در کد قبلی، یک `GroupChatManager` داریم که با زمان اجرا ثبت شده است. این مدیر مسئول هماهنگی تعاملات بین انواع مختلف عوامل، مانند نویسندگان، تصویرگران، ویراستاران و کاربران است.

- **زمان اجرای عامل**. این چارچوب یک محیط زمان اجرا فراهم می‌کند که ارتباط بین عوامل را امکان‌پذیر می‌کند، هویت‌ها و چرخه‌های عمر آن‌ها را مدیریت می‌کند و مرزهای امنیت و حریم خصوصی را اعمال می‌کند. این بدان معناست که شما می‌توانید عوامل خود را در یک محیط امن و کنترل‌شده اجرا کنید و اطمینان حاصل کنید که آن‌ها می‌توانند به صورت ایمن و کارآمد تعامل داشته باشند. دو زمان اجرای مورد توجه وجود دارد:
  - **زمان اجرای مستقل**. این گزینه خوبی برای برنامه‌های تک‌پردازشی است که در آن همه عوامل به یک زبان برنامه‌نویسی پیاده‌سازی شده‌اند و در یک فرآیند اجرا می‌شوند. در اینجا یک تصویر از نحوه کار آن آورده شده است:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">زمان اجرای مستقل</a>   
پشته برنامه

    *عوامل از طریق پیام‌ها از طریق زمان اجرا ارتباط برقرار می‌کنند و زمان اجرا چرخه عمر عوامل را مدیریت می‌کند*

  - **زمان اجرای عامل توزیع‌شده**، برای برنامه‌های چندپردازشی مناسب است که در آن عوامل ممکن است به زبان‌های برنامه‌نویسی مختلف پیاده‌سازی شده باشند و روی ماشین‌های مختلف اجرا شوند. در اینجا یک تصویر از نحوه کار آن آورده شده است:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">زمان اجرای توزیع‌شده</a>

## Semantic Kernel + چارچوب عامل

Semantic Kernel یک SDK ارکستراسیون هوش مصنوعی آماده برای سازمان‌ها است. این SDK شامل کانکتورهای هوش مصنوعی و حافظه، همراه با یک چارچوب عامل است.

ابتدا به برخی از اجزای اصلی بپردازیم:

- **کانکتورهای هوش مصنوعی**: این یک رابط با خدمات هوش مصنوعی خارجی و منابع داده برای استفاده در هر دو زبان Python و C# است.

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  

    ```csharp
    // Semantic Kernel C#
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

    در اینجا یک مثال ساده دارید که چگونه می‌توانید یک کرنل ایجاد کنید و یک سرویس تکمیل چت اضافه کنید. Semantic Kernel یک اتصال به یک سرویس هوش مصنوعی خارجی ایجاد می‌کند، در این مورد، Azure OpenAI Chat Completion.

- **افزونه‌ها**: این‌ها توابعی را که یک برنامه می‌تواند استفاده کند، کپسوله می‌کنند. افزونه‌های آماده و سفارشی وجود دارند که می‌توانید ایجاد کنید. یک مفهوم مرتبط "توابع درخواست" است. به جای ارائه نشانه‌های زبان طبیعی برای فراخوانی توابع، شما برخی توابع را به مدل اعلام می‌کنید. بر اساس زمینه چت فعلی، مدل ممکن است یکی از این توابع را برای تکمیل یک درخواست یا پرسش فراخوانی کند. در اینجا یک مثال آورده شده است:

  ```python
  from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


  async def main():
      from semantic_kernel.functions import KernelFunctionFromPrompt
      from semantic_kernel.kernel import Kernel

      kernel = Kernel()
      kernel.add_service(AzureChatCompletion())

      user_input = input("User Input:> ")

      kernel_function = KernelFunctionFromPrompt(
          function_name="SummarizeText",
          prompt="""
          Summarize the provided unstructured text in a sentence that is easy to understand.
          Text to summarize: {{$user_input}}
          """,
      )

      response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
      print(f"Model Response: {response}")

      """
      Sample Console Output:

      User Input:> I like dogs
      Model Response: The text expresses a preference for dogs.
      """


  if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  ```

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // create the function from the prompt
    KernelFunction summarizeFunc = kernel.CreateFunctionFromPrompt(
        promptTemplate: skPrompt,
        functionName: "SummarizeText"
    );

    //then import into the current kernel
    kernel.ImportPluginFromFunctions("SemanticFunctions", [summarizeFunc]);

    ```

    در اینجا، ابتدا یک قالب درخواست `skPrompt` دارید که فضایی برای ورودی کاربر، `$userInput`، باقی می‌گذارد. سپس تابع کرنل `SummarizeText` را ایجاد می‌کنید و سپس آن را با نام افزونه `SemanticFunctions` به کرنل وارد می‌کنید. به نام تابع توجه کنید که به Semantic Kernel کمک می‌کند بفهمد تابع چه کاری انجام می‌دهد و چه زمانی باید فراخوانی شود.

- **تابع بومی**: همچنین توابع بومی وجود دارند که چارچوب می‌تواند مستقیماً برای انجام وظیفه فراخوانی کند. در اینجا یک مثال از چنین تابعی که محتو
این اطلاعات سپس در مجموعه حافظه `SummarizedAzureDocs` ذخیره می‌شوند. این یک مثال بسیار ساده است، اما می‌توانید ببینید که چگونه می‌توان اطلاعات را در حافظه ذخیره کرد تا توسط LLM استفاده شود.

این اصول اولیه چارچوب Semantic Kernel بود، حالا چارچوب Agent Framework چیست؟

## سرویس Azure AI Agent

سرویس Azure AI Agent یک افزودنی جدیدتر است که در Microsoft Ignite 2024 معرفی شد. این سرویس امکان توسعه و استقرار عوامل هوش مصنوعی با مدل‌های انعطاف‌پذیرتر را فراهم می‌کند، مانند فراخوانی مستقیم LLMهای متن‌باز مثل Llama 3، Mistral و Cohere.

سرویس Azure AI Agent مکانیزم‌های امنیتی قوی‌تر و روش‌های ذخیره‌سازی داده برای سازمان‌ها ارائه می‌دهد که آن را برای کاربردهای سازمانی مناسب می‌سازد.

این سرویس به‌صورت آماده با چارچوب‌های هماهنگی چندعاملی مانند AutoGen و Semantic Kernel کار می‌کند.

این سرویس در حال حاضر در مرحله پیش‌نمایش عمومی است و از زبان‌های Python و C# برای ساخت عوامل پشتیبانی می‌کند.

با استفاده از Semantic Kernel Python، می‌توانیم یک عامل Azure AI با یک افزونه تعریف‌شده توسط کاربر ایجاد کنیم:

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### مفاهیم اصلی

سرویس Azure AI Agent دارای مفاهیم اصلی زیر است:

- **عامل**. سرویس Azure AI Agent با Azure AI Foundry یکپارچه می‌شود. در AI Foundry، یک عامل هوش مصنوعی به‌عنوان یک میکروسرویس "هوشمند" عمل می‌کند که می‌تواند برای پاسخ به سوالات (RAG)، انجام اقدامات یا خودکارسازی کامل جریان‌های کاری استفاده شود. این کار را با ترکیب قدرت مدل‌های تولیدی هوش مصنوعی با ابزارهایی که به آن امکان دسترسی و تعامل با منابع داده واقعی را می‌دهند، انجام می‌دهد. در اینجا یک مثال از یک عامل آورده شده است:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    در این مثال، یک عامل با مدل `gpt-4o-mini`، نام `my-agent` و دستورالعمل‌های `You are helpful agent` ایجاد شده است. این عامل با ابزارها و منابعی تجهیز شده است تا وظایف تفسیر کد را انجام دهد.

- **رشته و پیام‌ها**. رشته یک مفهوم مهم دیگر است. این نمایانگر یک مکالمه یا تعامل بین یک عامل و یک کاربر است. رشته‌ها می‌توانند برای پیگیری پیشرفت مکالمه، ذخیره اطلاعات زمینه‌ای و مدیریت وضعیت تعامل استفاده شوند. در اینجا یک مثال از یک رشته آورده شده است:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    در کد قبلی، یک رشته ایجاد شده است. سپس یک پیام به رشته ارسال می‌شود. با فراخوانی `create_and_process_run`، از عامل خواسته می‌شود که روی رشته کار کند. در نهایت، پیام‌ها بازیابی و ثبت می‌شوند تا پاسخ عامل مشاهده شود. پیام‌ها پیشرفت مکالمه بین کاربر و عامل را نشان می‌دهند. همچنین مهم است که بدانید پیام‌ها می‌توانند انواع مختلفی مانند متن، تصویر یا فایل باشند، به این معنا که کار عامل ممکن است منجر به تولید یک تصویر یا پاسخ متنی شود. به‌عنوان یک توسعه‌دهنده، می‌توانید از این اطلاعات برای پردازش بیشتر پاسخ یا ارائه آن به کاربر استفاده کنید.

- **یکپارچگی با چارچوب‌های دیگر هوش مصنوعی**. سرویس Azure AI Agent می‌تواند با چارچوب‌های دیگر مانند AutoGen و Semantic Kernel تعامل داشته باشد، به این معنا که می‌توانید بخشی از برنامه خود را در یکی از این چارچوب‌ها بسازید و به‌عنوان مثال از سرویس عامل به‌عنوان هماهنگ‌کننده استفاده کنید یا همه چیز را در سرویس عامل بسازید.

**موارد استفاده**: سرویس Azure AI Agent برای کاربردهای سازمانی طراحی شده است که نیاز به استقرار عوامل هوش مصنوعی امن، مقیاس‌پذیر و انعطاف‌پذیر دارند.

## تفاوت این چارچوب‌ها چیست؟

به نظر می‌رسد که این چارچوب‌ها همپوشانی زیادی دارند، اما تفاوت‌های کلیدی در طراحی، قابلیت‌ها و موارد استفاده هدف وجود دارد:

- **AutoGen**: یک چارچوب آزمایشی است که بر تحقیقات پیشرفته در سیستم‌های چندعاملی تمرکز دارد. بهترین مکان برای آزمایش و نمونه‌سازی سیستم‌های پیچیده چندعاملی است.
- **Semantic Kernel**: یک کتابخانه عامل آماده تولید برای ساخت برنامه‌های عامل سازمانی است. بر برنامه‌های عامل مبتنی بر رویداد و توزیع‌شده تمرکز دارد و امکان طراحی الگوهای تک‌عاملی و چندعاملی را فراهم می‌کند.
- **Azure AI Agent Service**: یک پلتفرم و سرویس استقرار در Azure Foundry برای عوامل است. اتصال به خدمات پشتیبانی‌شده توسط Azure مانند Azure OpenAI، Azure AI Search، Bing Search و اجرای کد را ارائه می‌دهد.

هنوز مطمئن نیستید کدام را انتخاب کنید؟

### موارد استفاده

بیایید ببینیم آیا می‌توانیم با مرور برخی موارد استفاده رایج به شما کمک کنیم:

> سوال: من در حال آزمایش، یادگیری و ساخت برنامه‌های عامل نمونه اولیه هستم و می‌خواهم بتوانم سریع بسازم و آزمایش کنم.

> پاسخ: AutoGen برای این سناریو انتخاب خوبی است، زیرا بر برنامه‌های عامل مبتنی بر رویداد و توزیع‌شده تمرکز دارد و از الگوهای طراحی پیشرفته چندعاملی پشتیبانی می‌کند.

> سوال: چه چیزی باعث می‌شود AutoGen برای این مورد استفاده بهتر از Semantic Kernel و Azure AI Agent Service باشد؟

> پاسخ: AutoGen به‌طور خاص برای برنامه‌های عامل مبتنی بر رویداد و توزیع‌شده طراحی شده است، که آن را برای خودکارسازی وظایف تولید کد و تحلیل داده‌ها مناسب می‌سازد. ابزارها و قابلیت‌های لازم برای ساخت سیستم‌های پیچیده چندعاملی را به‌طور کارآمد فراهم می‌کند.

> سوال: به نظر می‌رسد Azure AI Agent Service هم می‌تواند در اینجا کار کند، ابزارهایی برای تولید کد و موارد دیگر دارد؟

> پاسخ: بله، سرویس Azure AI Agent یک سرویس پلتفرم برای عوامل است و قابلیت‌های داخلی برای مدل‌های متعدد، Azure AI Search، Bing Search و Azure Functions اضافه می‌کند. این سرویس ساخت عوامل در پورتال Foundry و استقرار آن‌ها در مقیاس را آسان می‌کند.

> سوال: هنوز گیج هستم، فقط یک گزینه به من بدهید.

> پاسخ: یک انتخاب عالی این است که ابتدا برنامه خود را در Semantic Kernel بسازید و سپس از سرویس Azure AI Agent برای استقرار عامل خود استفاده کنید. این رویکرد به شما امکان می‌دهد عوامل خود را به‌راحتی حفظ کنید و در عین حال از قدرت ساخت سیستم‌های چندعاملی در Semantic Kernel بهره‌مند شوید. علاوه بر این، Semantic Kernel یک اتصال‌دهنده در AutoGen دارد که استفاده از هر دو چارچوب را با هم آسان می‌کند.

بیایید تفاوت‌های کلیدی را در یک جدول خلاصه کنیم:

| چارچوب | تمرکز | مفاهیم اصلی | موارد استفاده |
| --- | --- | --- | --- |
| AutoGen | برنامه‌های عامل مبتنی بر رویداد و توزیع‌شده | عوامل، شخصیت‌ها، توابع، داده‌ها | تولید کد، وظایف تحلیل داده |
| Semantic Kernel | درک و تولید محتوای انسانی | عوامل، اجزای ماژولار، همکاری | درک زبان طبیعی، تولید محتوا |
| Azure AI Agent Service | مدل‌های انعطاف‌پذیر، امنیت سازمانی، تولید کد، فراخوانی ابزار | ماژولاریت، همکاری، هماهنگی فرآیند | استقرار عوامل هوش مصنوعی امن، مقیاس‌پذیر و انعطاف‌پذیر |

موارد استفاده ایده‌آل برای هر یک از این چارچوب‌ها چیست؟

## آیا می‌توانم ابزارهای موجود در اکوسیستم Azure خود را مستقیماً یکپارچه کنم یا به راه‌حل‌های مستقل نیاز دارم؟

پاسخ مثبت است، شما می‌توانید ابزارهای موجود در اکوسیستم Azure خود را مستقیماً با سرویس Azure AI Agent یکپارچه کنید، به‌ویژه به این دلیل که این سرویس برای کار بدون مشکل با سایر خدمات Azure ساخته شده است. به‌عنوان مثال، می‌توانید Bing، Azure AI Search و Azure Functions را یکپارچه کنید. همچنین یکپارچگی عمیق با Azure AI Foundry وجود دارد.

برای AutoGen و Semantic Kernel، شما نیز می‌توانید با خدمات Azure یکپارچه شوید، اما ممکن است نیاز باشد که خدمات Azure را از کد خود فراخوانی کنید. روش دیگر برای یکپارچه‌سازی استفاده از SDKهای Azure برای تعامل با خدمات Azure از عوامل شما است. علاوه بر این، همان‌طور که ذکر شد، می‌توانید از سرویس Azure AI Agent به‌عنوان هماهنگ‌کننده برای عوامل ساخته‌شده در AutoGen یا Semantic Kernel استفاده کنید که دسترسی آسان به اکوسیستم Azure را فراهم می‌کند.

## کدهای نمونه

- Python: [چارچوب عامل](./code_samples/02-python-agent-framework.ipynb)
- .NET: [چارچوب عامل](./code_samples/02-dotnet-agent-framework.md)

## سوالات بیشتری درباره چارچوب‌های عامل هوش مصنوعی دارید؟

به [Discord Azure AI Foundry](https://aka.ms/ai-agents/discord) بپیوندید تا با دیگر یادگیرندگان ملاقات کنید، در ساعات اداری شرکت کنید و سوالات خود درباره عوامل هوش مصنوعی را پاسخ دهید.

## منابع

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">سرویس عامل Azure</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel و AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">چارچوب عامل Semantic Kernel Python</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">چارچوب عامل Semantic Kernel .Net</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">سرویس عامل Azure AI</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">استفاده از سرویس Azure AI Agent با AutoGen / Semantic Kernel برای ساخت راه‌حل چندعاملی</a>

## درس قبلی

[مقدمه‌ای بر عوامل هوش مصنوعی و موارد استفاده عوامل](../01-intro-to-ai-agents/README.md)

## درس بعدی

[درک الگوهای طراحی عامل](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال هرگونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->