# 🎨 الگوهای طراحی فعال با Azure OpenAI (API پاسخ‌ها) (.NET)

## 📋 اهداف یادگیری

این مثال الگوهای طراحی سطح سازمانی را برای ساخت عوامل هوشمند با استفاده از چارچوب عامل مایکروسافت در .NET با ادغام Azure OpenAI (API پاسخ‌ها) نشان می‌دهد. شما الگوها و رویکردهای معماری حرفه‌ای را می‌آموزید که عوامل را آماده تولید، قابل نگهداری و مقیاس‌پذیر می‌کند.

### الگوهای طراحی سازمانی

- 🏭 **الگوی کارخانه**: ایجاد عامل استاندارد شده با تزریق وابستگی
- 🔧 **الگوی سازنده**: پیکربندی و راه‌اندازی عامل به صورت Fluent
- 🧵 **الگوهای ایمن در برابر نخ**: مدیریت محاوره همزمان
- 📋 **الگوی مخزن**: مدیریت سازمان‌یافته ابزار و قابلیت

## 🎯 مزایای معماری مخصوص .NET

### ویژگی‌های سازمانی

- **نوع‌دهی قوی**: اعتبارسنجی زمان کامپایل و پشتیبانی IntelliSense
- **تزریق وابستگی**: ادغام ظرف DI داخلی
- **مدیریت پیکربندی**: الگوهای IConfiguration و Options
- **Async/Await**: پشتیبانی برتر از برنامه‌نویسی ناهمزمان

### الگوهای آماده تولید

- **ادغام ثبت لاگ**: پشتیبانی ILogger و ثبت لاگ ساخت‌یافته
- **بررسی‌های سلامت**: نظارت و تشخیص داخلی
- **اعتبارسنجی پیکربندی**: نوع‌دهی قوی با توضیحات داده
- **مدیریت خطا**: مدیریت استثنا سازمان‌یافته

## 🔧 معماری فنی

### اجزای اصلی .NET

- **Microsoft.Extensions.AI**: انتزاعات خدمات هوش مصنوعی یکپارچه
- **Microsoft.Agents.AI**: چارچوب ارکستراسیون عامل سازمانی
- **Azure OpenAI (API پاسخ‌ها)**: الگوهای کلاینت API با عملکرد بالا
- **سیستم پیکربندی**: appsettings.json و ادغام محیطی

### پیاده‌سازی الگوی طراحی

```mermaid
graph LR
    A[مجموعه خدمات (IServiceCollection)] --> B[سازنده عامل]
    B --> C[پیکربندی]
    C --> D[رجیستری ابزارها]
    D --> E[عامل هوش مصنوعی]
```

## 🏗️ الگوهای سازمانی نشان داده شده

### ۱. **الگوهای خلقتی**

- **کارخانه عامل**: ایجاد متمرکز عامل با پیکربندی یکسان
- **الگوی سازنده**: API Fluent برای پیکربندی پیچیده عامل
- **الگوی Singleton**: مدیریت منابع و پیکربندی مشترک
- **تزریق وابستگی**: اتصال سست و قابلیت تست

### ۲. **الگوهای رفتاری**

- **الگوی استراتژی**: استراتژی‌های اجرای ابزار قابل تعویض
- **الگوی فرمان**: عملیات عامل پیچیده با امکان بازگشت/انجام مجدد
- **الگوی ناظر**: مدیریت چرخه عمر عامل مبتنی بر رویداد
- **روش قالب**: جریان‌های کاری اجرای عامل استاندارد شده

### ۳. **الگوهای ساختاری**

- **الگوی تطبیق‌دهنده**: لایه ادغام Azure OpenAI (API پاسخ‌ها)
- **الگوی دکوراتور**: ارتقای قابلیت عامل
- **الگوی نما**: رابط‌های ساده تعامل عامل
- **الگوی پروکسی**: بارگذاری تنبل و کش برای بهبود عملکرد

## 📚 اصول طراحی .NET

### اصول SOLID

- **مسئولیت واحد**: هر مؤلفه یک هدف واضح دارد
- **باز/بسته**: توسعه‌پذیر بدون تغییر
- **جانشینی لیسکوف**: پیاده‌سازی ابزار مبتنی بر رابط
- **جدا سازی رابط**: رابط‌های متمرکز و هم‌بسته
- **معکوس‌سازی وابستگی**: وابستگی به انتزاعات، نه به جزئیات

### معماری تمیز

- **لایه دامنه**: انتزاعات اصلی عوامل و ابزارها
- **لایه برنامه**: ارکستراسیون عامل و جریان‌های کاری
- **لایه زیرساخت**: ادغام Azure OpenAI (API پاسخ‌ها) و خدمات خارجی
- **لایه ارائه**: تعامل کاربر و قالب‌بندی پاسخ

## 🔒 ملاحظات سازمانی

### امنیت

- **مدیریت گواهی‌ها**: مدیریت امن کلید API با IConfiguration
- **اعتبارسنجی ورودی**: نوع‌دهی قوی و اعتبارسنجی توضیحات داده
- **پاک‌سازی خروجی**: پردازش و فیلتر امن پاسخ‌ها
- **ثبت لاگ حسابرسی**: ردیابی جامع عملیات

### عملکرد

- **الگوهای ناهمزمان**: عملیات I/O بدون مسدودسازی
- **جمع‌آوری اتصال**: مدیریت بهینه کلاینت HTTP
- **کشینگ**: کش پاسخ برای بهبود عملکرد
- **مدیریت منابع**: الگوهای دورریزی و پاکسازی مناسب

### مقیاس‌پذیری

- **ایمنی نخ**: پشتیبانی از اجرای همزمان عامل
- **جمع‌آوری منابع**: استفاده بهینه از منابع
- **مدیریت بار**: محدودیت نرخ و مدیریت فشار معکوس
- **نظارت**: معیارهای عملکرد و بررسی سلامت

## 🚀 استقرار در تولید

- **مدیریت پیکربندی**: تنظیمات مخصوص محیط
- **استراتژی ثبت لاگ**: ثبت لاگ ساخت‌یافته با شناسه همبستگی
- **مدیریت خطا**: مدیریت استثنا جهانی با بازیابی مناسب
- **نظارت**: Application Insights و شمارنده‌های عملکرد
- **آزمایش**: تست واحد، تست یکپارچگی و الگوهای تست بار

آماده‌اید عوامل هوشمند سطح سازمانی با .NET بسازید؟ بیایید چیزی قدرتمند طراحی کنیم! 🏢✨

## 🚀 شروع به کار

### پیش‌نیازها

- [SDK دات‌نت ۱۰](https://dotnet.microsoft.com/download/dotnet/10.0) یا بالاتر
- یک [اشتراک Azure](https://azure.microsoft.com/free/) با منبع Azure OpenAI و استقرار مدل
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — با `az login` وارد شوید

### متغیرهای محیطی لازم

```bash
# زد‌اِش/باش
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# سپس وارد شوید تا AzureCliCredential بتواند توکن دریافت کند
az login
```

```powershell
# پاورشل
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# سپس وارد شوید تا AzureCliCredential بتواند توکن دریافت کند
az login
```

### نمونه کد

برای اجرای نمونه کد،

```bash
# زش/باش
chmod +x ./03-dotnet-agent-framework.cs
./03-dotnet-agent-framework.cs
```

یا با استفاده از dotnet CLI:

```bash
dotnet run ./03-dotnet-agent-framework.cs
```

کد کامل را در [`03-dotnet-agent-framework.cs`](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs) ببینید.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*
#:package Azure.AI.OpenAI@2.1.0
#:package Azure.Identity@1.13.1

using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using Azure.AI.OpenAI;
using Azure.Identity;

// Tool Function: Random Destination Generator
// This static method will be available to the agent as a callable tool
// The [Description] attribute helps the AI understand when to use this function
// This demonstrates how to create custom tools for AI agents
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
    // List of popular vacation destinations around the world
    // The agent will randomly select from these options
    var destinations = new List<string>
    {
        "Paris, France",
        "Tokyo, Japan",
        "New York City, USA",
        "Sydney, Australia",
        "Rome, Italy",
        "Barcelona, Spain",
        "Cape Town, South Africa",
        "Rio de Janeiro, Brazil",
        "Bangkok, Thailand",
        "Vancouver, Canada"
    };

    // Generate random index and return selected destination
    // Uses System.Random for simple random selection
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}

// Azure OpenAI with the Responses API (stable v1 endpoint). Sign in with `az login`.
var azureEndpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")
    ?? throw new InvalidOperationException("AZURE_OPENAI_ENDPOINT is not set.");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

var azureClient = new AzureOpenAIClient(new Uri(azureEndpoint), new AzureCliCredential());

// Define Agent Identity and Comprehensive Instructions
// Agent name for identification and logging purposes
var AGENT_NAME = "TravelAgent";

// Detailed instructions that define the agent's personality, capabilities, and behavior
// This system prompt shapes how the agent responds and interacts with users
var AGENT_INSTRUCTIONS = """
You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
"Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?"

Always prioritize user preferences. If they mention a specific destination like "Bali" or "Paris," focus your planning on that location rather than suggesting alternatives.
""";

// Create AI Agent with Advanced Travel Planning Capabilities
// Get the Responses client for the deployment and create the AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Conversation Session for Context Management
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
var session = await agent.CreateSessionAsync();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the session parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", session))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation sessions and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", session))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->