# 🔍 کاوش در چارچوب Microsoft Agent - عامل پایه (.NET)

## 📋 اهداف یادگیری

این مثال مفاهیم بنیادی چارچوب Microsoft Agent را از طریق پیاده‌سازی یک عامل پایه در .NET بررسی می‌کند. شما الگوهای اصلی عامل‌محور را خواهید آموخت و درک خواهید کرد که چگونه عوامل هوشمند زیرپوستی با استفاده از C# و اکوسیستم .NET کار می‌کنند.

### آنچه کشف خواهید کرد

- 🏗️ **معماری عامل**: درک ساختار پایه عوامل هوش مصنوعی در .NET
- 🛠️ **ادغام ابزار**: چگونه عوامل از توابع خارجی برای گسترش قابلیت‌ها استفاده می‌کنند  
- 💬 **جریان مکالمه**: مدیریت گفتگوهای چند مرحله‌ای و زمینه با مدیریت رشته‌ها
- 🔧 **الگوهای پیکربندی**: بهترین روش‌ها برای راه‌اندازی و مدیریت عامل در .NET

## 🎯 مفاهیم کلیدی پوشش داده شده

### اصول چارچوب عامل‌محور

- **خودمختاری**: چگونه عوامل تصمیمات مستقل با استفاده از انتزاعات هوش مصنوعی در .NET می‌گیرند
- **واکنش‌پذیری**: پاسخ به تغییرات محیطی و ورودی‌های کاربر
- **فعالیت پیشدستانه**: انجام ابتکار بر اساس اهداف و زمینه
- **توانایی اجتماعی**: تعامل از طریق زبان طبیعی با رشته‌های مکالمه

### اجزای فنی

- **AIAgent**: هماهنگی اصلی عامل و مدیریت مکالمه (.NET)
- **توابع ابزار**: گسترش قابلیت‌های عامل با متدها و ویژگی‌های C#
- **ادغام Azure OpenAI**: استفاده از مدل‌های زبانی از طریق API پاسخ‌های Azure OpenAI
- **پیکربندی امن**: مدیریت نقطه پایان مبتنی بر محیط

## 🔧 پشته فنی

### فناوری‌های اصلی

- چارچوب Microsoft Agent (.NET)
- ادغام Azure OpenAI (API پاسخ‌ها)
- الگوهای مشتری Azure.AI.OpenAI
- پیکربندی مبتنی بر محیط با DotNetEnv

### قابلیت‌های عامل

- درک و تولید زبان طبیعی
- فراخوانی تابع و استفاده از ابزار با ویژگی‌های C#
- پاسخ‌های آگاه به زمینه با جلسات مکالمه
- معماری قابل توسعه با الگوهای تزریق وابستگی

## 📚 مقایسه چارچوب‌ها

این مثال رویکرد چارچوب Microsoft Agent را در مقایسه با سایر چارچوب‌های عامل‌محور نشان می‌دهد:

| ویژگی | چارچوب Microsoft Agent | سایر چارچوب‌ها |
|---------|-------------------------|------------------|
| **ادغام** | اکوسیستم بومی مایکروسافت | سازگاری متنوع |
| **سادگی** | API تمیز و شهودی | اغلب راه‌اندازی پیچیده |
| **گسترش‌پذیری** | ادغام آسان ابزار | وابسته به چارچوب |
| **آماده سازمانی** | ساخته شده برای تولید | بسته به چارچوب متفاوت است |

## 🚀 شروع به کار

### پیش‌نیازها

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) یا بالاتر
- یک [اشتراک Azure](https://azure.microsoft.com/free/) با یک منبع Azure OpenAI و استقرار مدل
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — ورود با `az login`

### متغیرهای محیطی لازم

```bash
# زد شل / باش
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# سپس وارد شوید تا AzureCliCredential بتواند توکن دریافت کند
az login
```

```powershell
# پاورشل
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# سپس وارد شوید تا AzureCliCredential بتواند یک توکن دریافت کند
az login
```

### نمونه کد

برای اجرای نمونه کد،

```bash
# زی‌شل/باش
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

یا با استفاده از خط فرمان dotnet:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

کد کامل را در [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) ببینید.

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

// Create New Session for Context Management.
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentSession session = await agent.CreateSessionAsync();

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

## 🎓 نکات کلیدی

1. **معماری عامل**: چارچوب Microsoft Agent رویکردی تمیز و نوع‌امن برای ساخت عوامل هوش مصنوعی در .NET ارائه می‌دهد
2. **ادغام ابزار**: توابعی که با ویژگی‌های `[Description]` تزئین شده‌اند، به ابزارهای در دسترس عامل تبدیل می‌شوند
3. **زمینه مکالمه**: مدیریت جلسه امکان گفتگوهای چند مرحله‌ای با آگاهی کامل از زمینه را فراهم می‌کند
4. **مدیریت پیکربندی**: متغیرهای محیطی و مدیریت امن اعتبارنامه‌ها بهترین شیوه‌های .NET را دنبال می‌کنند
5. **API پاسخ‌های Azure OpenAI**: عامل از API پاسخ‌های Azure OpenAI از طریق SDK Azure.AI.OpenAI استفاده می‌کند

## 🔗 منابع اضافی

- [مستندات چارچوب Microsoft Agent](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI در Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->