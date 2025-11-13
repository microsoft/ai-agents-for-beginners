<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T11:08:45+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "fa"
}
-->
# 🔍 بررسی چارچوب Microsoft Agent - عامل پایه (.NET)

## 📋 اهداف آموزشی

این مثال مفاهیم اساسی چارچوب Microsoft Agent را از طریق پیاده‌سازی یک عامل پایه در .NET بررسی می‌کند. شما الگوهای اصلی عامل‌محور را یاد خواهید گرفت و درک خواهید کرد که عوامل هوشمند چگونه با استفاده از C# و اکوسیستم .NET کار می‌کنند.

### آنچه خواهید آموخت

- 🏗️ **معماری عامل**: درک ساختار پایه عوامل هوش مصنوعی در .NET  
- 🛠️ **ادغام ابزارها**: نحوه استفاده عوامل از توابع خارجی برای گسترش قابلیت‌ها  
- 💬 **جریان مکالمه**: مدیریت مکالمات چند مرحله‌ای و زمینه با مدیریت رشته  
- 🔧 **الگوهای پیکربندی**: بهترین روش‌ها برای تنظیم و مدیریت عامل در .NET  

## 🎯 مفاهیم کلیدی پوشش داده شده

### اصول چارچوب عامل‌محور

- **خودمختاری**: نحوه تصمیم‌گیری مستقل عوامل با استفاده از انتزاعات هوش مصنوعی .NET  
- **واکنش‌پذیری**: پاسخ به تغییرات محیطی و ورودی‌های کاربر  
- **پیش‌فعالیت**: اقدام بر اساس اهداف و زمینه  
- **توانایی اجتماعی**: تعامل از طریق زبان طبیعی با رشته‌های مکالمه  

### اجزای فنی

- **AIAgent**: مدیریت اصلی عامل و مکالمه (.NET)  
- **توابع ابزار**: گسترش قابلیت‌های عامل با روش‌ها و ویژگی‌های C#  
- **ادغام OpenAI**: استفاده از مدل‌های زبان از طریق API‌های استاندارد .NET  
- **پیکربندی امن**: مدیریت کلیدهای API مبتنی بر محیط  

## 🔧 پشته فنی

### فناوری‌های اصلی

- چارچوب Microsoft Agent (.NET)  
- ادغام API مدل‌های GitHub  
- الگوهای مشتری سازگار با OpenAI  
- پیکربندی مبتنی بر محیط با DotNetEnv  

### قابلیت‌های عامل

- درک و تولید زبان طبیعی  
- فراخوانی توابع و استفاده از ابزارها با ویژگی‌های C#  
- پاسخ‌های آگاه از زمینه با رشته‌های مکالمه  
- معماری قابل گسترش با الگوهای تزریق وابستگی  

## 📚 مقایسه چارچوب‌ها

این مثال رویکرد چارچوب Microsoft Agent را در مقایسه با سایر چارچوب‌های عامل‌محور نشان می‌دهد:

| ویژگی | چارچوب Microsoft Agent | سایر چارچوب‌ها |
|-------|-------------------------|----------------|
| **ادغام** | اکوسیستم بومی Microsoft | سازگاری متنوع |
| **سادگی** | API تمیز و شهودی | اغلب تنظیمات پیچیده |
| **گسترش‌پذیری** | ادغام ابزار آسان | وابسته به چارچوب |
| **آماده برای سازمان** | طراحی شده برای تولید | بسته به چارچوب متفاوت است |

## 🚀 شروع به کار

### پیش‌نیازها

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) یا بالاتر  
- [توکن دسترسی API مدل‌های GitHub](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### متغیرهای محیطی مورد نیاز

```bash
# zsh/bash
export GH_TOKEN=<your_github_token>
export GH_ENDPOINT=https://models.github.ai/inference
export GH_MODEL_ID=openai/gpt-5-mini
```
  
```powershell
# PowerShell
$env:GH_TOKEN = "<your_github_token>"
$env:GH_ENDPOINT = "https://models.github.ai/inference"
$env:GH_MODEL_ID = "openai/gpt-5-mini"
```
  

### کد نمونه

برای اجرای مثال کد،  

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
یا با استفاده از CLI دات‌نت:  

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
کد کامل را در [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) مشاهده کنید.  

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*

using System.ClientModel;
using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using OpenAI;

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

// Extract configuration from environment variables
// Retrieve the GitHub Models API endpoint, defaults to https://models.github.ai/inference if not specified
// Retrieve the model ID, defaults to openai/gpt-5-mini if not specified
// Retrieve the GitHub token for authentication, throws exception if not specified
var github_endpoint = Environment.GetEnvironmentVariable("GH_ENDPOINT") ?? "https://models.github.ai/inference";
var github_model_id = Environment.GetEnvironmentVariable("GH_MODEL_ID") ?? "openai/gpt-5-mini";
var github_token = Environment.GetEnvironmentVariable("GH_TOKEN") ?? throw new InvalidOperationException("GH_TOKEN is not set.");

// Configure OpenAI Client Options
// Create configuration options to point to GitHub Models endpoint
// This redirects OpenAI client calls to GitHub's model inference service
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
// Create OpenAI client using GitHub token for authentication
// Configure it to use GitHub Models endpoint instead of OpenAI directly
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

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
// Initialize complete agent pipeline: OpenAI client → Chat client → AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Conversation Thread for Context Management
// Initialize a new conversation thread to maintain context across multiple interactions
// Threads enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentThread thread = agent.GetNewThread();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the thread parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation threads and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}
```
  

## 🎓 نکات کلیدی

1. **معماری عامل**: چارچوب Microsoft Agent رویکردی تمیز و نوع‌امن برای ساخت عوامل هوش مصنوعی در .NET ارائه می‌دهد  
2. **ادغام ابزار**: توابعی که با ویژگی `[Description]` تزئین شده‌اند به ابزارهای موجود برای عامل تبدیل می‌شوند  
3. **زمینه مکالمه**: مدیریت رشته امکان مکالمات چند مرحله‌ای با آگاهی کامل از زمینه را فراهم می‌کند  
4. **مدیریت پیکربندی**: متغیرهای محیطی و مدیریت امن اعتبارنامه‌ها از بهترین روش‌های .NET پیروی می‌کنند  
5. **سازگاری با OpenAI**: ادغام مدل‌های GitHub به‌طور یکپارچه از طریق API‌های سازگار با OpenAI کار می‌کند  

## 🔗 منابع اضافی

- [مستندات چارچوب Microsoft Agent](https://learn.microsoft.com/agent-framework)  
- [بازار مدل‌های GitHub](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال هرگونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->