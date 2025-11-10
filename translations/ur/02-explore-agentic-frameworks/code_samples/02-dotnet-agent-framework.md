<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:31:50+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "ur"
}
-->
# 🔍 ایجنٹک فریم ورک کا جائزہ - بنیادی ایجنٹ (.NET)

## 📋 سیکھنے کے مقاصد

یہ نوٹ بک Microsoft Agent Framework کے بنیادی تصورات کو .NET میں ایک بنیادی ایجنٹ کے نفاذ کے ذریعے دریافت کرتی ہے۔ آپ ایجنٹک پیٹرنز کے بنیادی اصول سیکھیں گے اور سمجھیں گے کہ ذہین ایجنٹس C# اور .NET ایکو سسٹم کے تحت کیسے کام کرتے ہیں۔

**آپ کیا سیکھیں گے:**
- 🏗️ **ایجنٹ کی ساخت**: .NET میں AI ایجنٹس کی بنیادی ساخت کو سمجھنا
- 🛠️ **ٹول انٹیگریشن**: ایجنٹس بیرونی فنکشنز کا استعمال کرکے صلاحیتوں کو کیسے بڑھاتے ہیں  
- 💬 **گفتگو کا بہاؤ**: تھریڈ مینجمنٹ کے ذریعے ملٹی ٹرن گفتگو اور سیاق و سباق کا انتظام
- 🔧 **کنفیگریشن پیٹرنز**: .NET میں ایجنٹ سیٹ اپ اور مینجمنٹ کے بہترین طریقے

## 🎯 کلیدی تصورات

### ایجنٹک فریم ورک کے اصول
- **خود مختاری**: .NET AI ایبسٹریکشنز کا استعمال کرتے ہوئے ایجنٹس کیسے آزاد فیصلے کرتے ہیں
- **ردعمل**: ماحولیاتی تبدیلیوں اور صارف کے ان پٹ پر ردعمل دینا
- **پیش قدمی**: اہداف اور سیاق و سباق کی بنیاد پر پہل کرنا
- **سماجی قابلیت**: گفتگو کے تھریڈز کے ذریعے قدرتی زبان میں بات چیت کرنا

### تکنیکی اجزاء
- **AIAgent**: ایجنٹ کی بنیادی آرکیسٹریشن اور گفتگو کا انتظام (.NET)
- **ٹول فنکشنز**: C# میتھڈز اور ایٹریبیوٹس کے ساتھ ایجنٹ کی صلاحیتوں کو بڑھانا
- **OpenAI انٹیگریشن**: معیاری .NET APIs کے ذریعے لینگویج ماڈلز کا استعمال
- **ماحولیاتی انتظام**: DotNetEnv کے ساتھ محفوظ کنفیگریشن اور کریڈینشل ہینڈلنگ

## ⚙️ ضروریات اور سیٹ اپ

**ضروری ڈپینڈنسیز:**
- .NET 9.0 SDK یا اس سے زیادہ
- Visual Studio 2022 یا VS Code C# ایکسٹینشن کے ساتھ

**NuGet پیکجز:**
- `Microsoft.Extensions.AI` - بنیادی AI ایبسٹریکشنز
- `Microsoft.Extensions.AI.OpenAI` - OpenAI انٹیگریشن (پریویو)
- `DotNetEnv` - ماحولیاتی ویریبل مینجمنٹ

**ماحولیاتی کنفیگریشن (.env فائل):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 تکنیکی اسٹیک

**بنیادی ٹیکنالوجیز:**
- Microsoft Agent Framework (.NET)
- GitHub Models API انٹیگریشن
- OpenAI-کمپیٹیبل کلائنٹ پیٹرنز
- DotNetEnv کے ساتھ ماحولیاتی کنفیگریشن

**ایجنٹ کی صلاحیتیں:**
- قدرتی زبان کو سمجھنا اور پیدا کرنا
- C# ایٹریبیوٹس کے ساتھ فنکشن کالنگ اور ٹول کا استعمال
- گفتگو کے تھریڈز کے ساتھ سیاق و سباق پر مبنی جوابات
- ڈپینڈنسی انجیکشن پیٹرنز کے ساتھ قابل توسیع آرکیٹیکچر

## 📚 فریم ورک کا موازنہ

یہ مثال .NET میں Microsoft Agent Framework کے طریقہ کار کو دوسرے پلیٹ فارمز کے مقابلے میں ظاہر کرتی ہے:

| خصوصیت | .NET ایجنٹ فریم ورک | Python متبادل |
|---------|---------------------|-------------------|
| **ٹائپ سیفٹی** | C# کے ساتھ مضبوط ٹائپنگ | ڈائنامک ٹائپنگ |
| **انٹیگریشن** | .NET ایکو سسٹم کے ساتھ نیٹو | مختلف مطابقت |
| **کارکردگی** | کمپائلڈ کوڈ کی کارکردگی | انٹرپریٹڈ ایگزیکیوشن |
| **انٹرپرائز ریڈی** | پروڈکشن .NET ایپس کے لیے بنایا گیا | فریم ورک کے لحاظ سے مختلف |
| **ٹولنگ** | Visual Studio انٹیگریشن | IDE پر منحصر |

## 🚀 شروعات کریں

نیچے دیے گئے سیلز کو فالو کریں تاکہ آپ .NET میں اپنا پہلا بنیادی ایجنٹ بنا سکیں اور ایجنٹک تصورات کو سمجھ سکیں!

## 📦 انسٹالیشن اور سیٹ اپ

یہ مثال ایک قابل عمل .NET سنگل فائل ایپ کے طور پر دستیاب ہے۔ مکمل نفاذ کے لیے ساتھ دی گئی `02-dotnet-agent-framework.cs` فائل دیکھیں۔

اس مثال کو چلانے کے لیے:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

یا dotnet CLI کا استعمال کرتے ہوئے:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 کوڈ کا جائزہ

مکمل نفاذ میں شامل ہیں:

### 1. پیکج ڈپینڈنسیز

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

### 2. ضروری امپورٹس

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. ماحولیاتی کنفیگریشن

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. ٹول فنکشن کی تعریف

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

### 5. کنفیگریشن اور کلائنٹ سیٹ اپ

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

### 6. ایجنٹ کنفیگریشن

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

### 7. ایجنٹ کی شروعات

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

### 8. گفتگو کا انتظام

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 اہم نکات

1. **ایجنٹ کی ساخت**: Microsoft Agent Framework .NET میں AI ایجنٹس بنانے کے لیے ایک صاف، ٹائپ سیف طریقہ فراہم کرتا ہے
2. **ٹول انٹیگریشن**: `[Description]` ایٹریبیوٹ کے ساتھ سجائے گئے فنکشنز ایجنٹ کے لیے دستیاب ٹولز بن جاتے ہیں
3. **گفتگو کا سیاق و سباق**: تھریڈ مینجمنٹ ملٹی ٹرن گفتگو کو مکمل سیاق و سباق کے ساتھ ممکن بناتا ہے
4. **کنفیگریشن مینجمنٹ**: ماحولیاتی ویریبلز اور محفوظ کریڈینشل ہینڈلنگ .NET کے بہترین طریقوں پر عمل کرتی ہے
5. **OpenAI مطابقت**: GitHub Models انٹیگریشن OpenAI-کمپیٹیبل APIs کے ذریعے بغیر کسی رکاوٹ کے کام کرتا ہے

## 🔗 اضافی وسائل

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔