<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:31:38+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "fa"
}
-->
# 🔍 بررسی چارچوب‌های عامل - عامل پایه (.NET)

## 📋 اهداف یادگیری

این دفترچه مفاهیم اساسی چارچوب عامل مایکروسافت را از طریق پیاده‌سازی یک عامل پایه در .NET بررسی می‌کند. شما الگوهای اصلی عامل را یاد خواهید گرفت و درک خواهید کرد که عوامل هوشمند چگونه با استفاده از C# و اکوسیستم .NET کار می‌کنند.

**آنچه کشف خواهید کرد:**
- 🏗️ **معماری عامل**: درک ساختار پایه عوامل هوش مصنوعی در .NET  
- 🛠️ **ادغام ابزارها**: نحوه استفاده عوامل از توابع خارجی برای گسترش قابلیت‌ها  
- 💬 **جریان مکالمه**: مدیریت مکالمات چند مرحله‌ای و زمینه با مدیریت رشته  
- 🔧 **الگوهای پیکربندی**: بهترین روش‌ها برای تنظیم و مدیریت عامل در .NET  

## 🎯 مفاهیم کلیدی پوشش داده شده

### اصول چارچوب عامل
- **خودمختاری**: نحوه تصمیم‌گیری مستقل عوامل با استفاده از انتزاعات هوش مصنوعی .NET  
- **واکنش‌پذیری**: پاسخ به تغییرات محیطی و ورودی‌های کاربر  
- **پیش‌فعالیت**: اقدام بر اساس اهداف و زمینه  
- **توانایی اجتماعی**: تعامل از طریق زبان طبیعی با رشته‌های مکالمه  

### اجزای فنی
- **AIAgent**: مدیریت اصلی عامل و مکالمه (.NET)  
- **توابع ابزار**: گسترش قابلیت‌های عامل با روش‌ها و ویژگی‌های C#  
- **ادغام OpenAI**: استفاده از مدل‌های زبان از طریق API‌های استاندارد .NET  
- **مدیریت محیط**: پیکربندی امن و مدیریت اعتبارنامه‌ها با DotNetEnv  

## ⚙️ پیش‌نیازها و تنظیمات

**وابستگی‌های مورد نیاز:**
- .NET 9.0 SDK یا بالاتر  
- Visual Studio 2022 یا VS Code با افزونه C#  

**پکیج‌های NuGet:**
- `Microsoft.Extensions.AI` - انتزاعات اصلی هوش مصنوعی  
- `Microsoft.Extensions.AI.OpenAI` - ادغام OpenAI (پیش‌نمایش)  
- `DotNetEnv` - مدیریت متغیرهای محیطی  

**پیکربندی محیط (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```
  
## 🔧 پشته فنی

**فناوری‌های اصلی:**
- چارچوب عامل مایکروسافت (.NET)  
- ادغام API مدل‌های GitHub  
- الگوهای مشتری سازگار با OpenAI  
- پیکربندی مبتنی بر محیط با DotNetEnv  

**قابلیت‌های عامل:**
- درک و تولید زبان طبیعی  
- فراخوانی توابع و استفاده از ابزارها با ویژگی‌های C#  
- پاسخ‌های آگاه از زمینه با رشته‌های مکالمه  
- معماری قابل گسترش با الگوهای تزریق وابستگی  

## 📚 مقایسه چارچوب‌ها

این مثال رویکرد چارچوب عامل مایکروسافت در .NET را در مقایسه با سایر پلتفرم‌ها نشان می‌دهد:

| ویژگی | چارچوب عامل .NET | معادل‌های پایتون |
|-------|------------------|------------------|
| **ایمنی نوع** | تایپ قوی با C# | تایپ پویا |
| **ادغام** | اکوسیستم بومی .NET | سازگاری متنوع |
| **عملکرد** | عملکرد کد کامپایل شده | اجرای تفسیری |
| **آماده برای سازمان** | طراحی شده برای اپلیکیشن‌های تولیدی .NET | بسته به چارچوب متفاوت است |
| **ابزارها** | ادغام با Visual Studio | وابسته به IDE |

## 🚀 شروع به کار

مراحل زیر را دنبال کنید تا اولین عامل پایه خود را در .NET بسازید و مفاهیم اساسی عامل را درک کنید!

## 📦 نصب و تنظیمات

این مثال به عنوان یک اپلیکیشن تک فایل قابل اجرا .NET در دسترس است. فایل همراه `02-dotnet-agent-framework.cs` را برای پیاده‌سازی کامل مشاهده کنید.

برای اجرای این مثال:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
یا با استفاده از CLI دات‌نت:

```bash
dotnet run 02-dotnet-agent-framework.cs
```
  
## 💡 مرور کد

پیاده‌سازی کامل شامل موارد زیر است:

### 1. وابستگی‌های پکیج

```csharp
// Core AI abstraction layer for .NET applications
#r "nuget: Microsoft.Extensions.AI, 9.9.1"

// Microsoft Agent Framework OpenAI integration
#r "nuget: Microsoft.Agents.AI.OpenAI, 1.0.0-preview.251001.3"

// Core Microsoft Agent Framework library
#r "nuget: Microsoft.Agents.AI, 1.0.0-preview.251001.3"

// Environment variable management
#r "nuget: DotNetEnv, 3.1.1"
```
  
### 2. واردات ضروری

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```
  
### 3. پیکربندی محیط

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```
  
### 4. تعریف توابع ابزار

```csharp
// Random destination generator tool
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
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
    
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}
```
  
### 5. تنظیمات و راه‌اندازی مشتری

```csharp
// Extract environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? 
    throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? 
    throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI client for GitHub Models
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI client
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);
```
  
### 6. پیکربندی عامل

```csharp
const string AGENT_NAME = "TravelAgent";

const string AGENT_INSTRUCTIONS = @"You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
""Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?""

Always prioritize user preferences. If they mention a specific destination like ""Bali"" or ""Paris,"" focus your planning on that location rather than suggesting alternatives.
";
```
  
### 7. راه‌اندازی عامل

```csharp
// Create AI agent with travel planning capabilities
AIAgent agent = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions)
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create((Func<string>)GetRandomDestination)]
    );
```
  
### 8. مدیریت مکالمه

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```
  
## 🎓 نکات کلیدی

1. **معماری عامل**: چارچوب عامل مایکروسافت رویکردی تمیز و ایمن برای ساخت عوامل هوش مصنوعی در .NET ارائه می‌دهد  
2. **ادغام ابزارها**: توابعی که با ویژگی `[Description]` تزئین شده‌اند به عنوان ابزارهای در دسترس برای عامل تبدیل می‌شوند  
3. **زمینه مکالمه**: مدیریت رشته امکان مکالمات چند مرحله‌ای با آگاهی کامل از زمینه را فراهم می‌کند  
4. **مدیریت پیکربندی**: متغیرهای محیطی و مدیریت امن اعتبارنامه‌ها از بهترین روش‌های .NET پیروی می‌کنند  
5. **سازگاری با OpenAI**: ادغام مدل‌های GitHub به طور یکپارچه از طریق API‌های سازگار با OpenAI کار می‌کند  

## 🔗 منابع اضافی

- [مستندات چارچوب عامل مایکروسافت](https://learn.microsoft.com/en-us/dotnet/ai/agents)  
- [بازار مدل‌های GitHub](https://github.com/marketplace/models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)  
- [اپلیکیشن‌های تک فایل .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)  

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.