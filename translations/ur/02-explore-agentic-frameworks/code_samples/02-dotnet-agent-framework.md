# 🔍 مائیکروسافٹ ایجنٹ فریم ورک کی تلاش - بنیادی ایجنٹ (.NET)

## 📋 سیکھنے کے مقاصد

یہ مثال مائیکروسافٹ ایجنٹ فریم ورک کے بنیادی تصورات کو .NET میں ایک بنیادی ایجنٹ کے نفاذ کے ذریعے دریافت کرتی ہے۔ آپ ایجنٹ کے بنیادی نمونوں کو سیکھیں گے اور سمجھیں گے کہ ذہین ایجنٹ C# اور .NET ایکو سسٹم کا استعمال کرتے ہوئے کیسے کام کرتے ہیں۔

### آپ کیا دریافت کریں گے

- 🏗️ **ایجنٹ کا فن تعمیر**: .NET میں AI ایجنٹس کے بنیادی ڈھانچے کو سمجھنا
- 🛠️ **ٹول انضمام**: ایجنٹس کیسے خارجی افعال کو استعمال کرتے ہوئے صلاحیتوں کو بڑھاتے ہیں  
- 💬 **بات چیت کا بہاؤ**: کثیر دور کی بات چیت اور تھریڈ مینجمنٹ کے ساتھ سیاق و سباق کا انتظام
- 🔧 **ترتیب کے نمونے**: .NET میں ایجنٹ کی ترتیب اور انتظام کے بہترین طریقے

## 🎯 شامل کردہ کلیدی تصورات

### ایجنٹک فریم ورک اصول

- **خودمختاری**: ایجنٹس .NET AI ایبسٹریکشنز کا استعمال کرکے آزادانہ فیصلے کیسے کرتے ہیں
- **ردعمل پذیری**: ماحولیاتی تبدیلیوں اور صارف کی ان پٹ پر ردعمل دینا
- **ابتکار پسندی**: مقاصد اور سیاق و سباق کی بنیاد پر پیش قدمی کرنا
- **سماجی صلاحیت**: بات چیت کے تھریڈز کے ذریعے قدرتی زبان میں تعامل کرنا

### تکنیکی اجزاء

- **AIAgent**: بنیادی ایجنٹ ہم آہنگی اور بات چیت کا انتظام (.NET)
- **ٹول فنکشنز**: C# طریقوں اور صفات کے ساتھ ایجنٹ کی صلاحیتوں میں توسیع
- **Azure OpenAI انضمام**: Azure OpenAI Responses API کے ذریعے زبان کے ماڈلز کا استعمال
- **محفوظ ترتیب**: ماحول پر مبنی اختتامی نقطہ انتظام

## 🔧 تکنیکی اسٹیک

### بنیادی ٹیکنالوجیز

- مائیکروسافٹ ایجنٹ فریم ورک (.NET)
- Azure OpenAI (Responses API) انضمام
- Azure.AI.OpenAI کلائنٹ کے نمونے
- DotNetEnv کے ساتھ ماحولیاتی ترتیب

### ایجنٹ کی صلاحیتیں

- قدرتی زبان کی سمجھ اور تخلیق
- C# صفات کے ساتھ فنکشن کالنگ اور ٹول کا استعمال
- بات چیت کے سیشنز کے ساتھ سیاق و سباق کی آگاہی کے جوابات
- انحصار انجیکشن کے نمونوں کے ساتھ توسیعی فن تعمیر

## 📚 فریم ورک موازنہ

یہ مثال دیگر ایجنٹک فریم ورکس کے مقابلے میں مائیکروسافٹ ایجنٹ فریم ورک کے طریقہ کار کو ظاہر کرتی ہے:

| خصوصیت | مائیکروسافٹ ایجنٹ فریم ورک | دیگر فریم ورکس |
|---------|-------------------------|------------------|
| **انضمام** | مقامی مائیکروسافٹ ایکو سسٹم | مختلف مطابقت |
| **سادگی** | صاف ستھرا، آسان API | اکثر پیچیدہ ترتیب |
| **توسیع پذیری** | آسان ٹول انضمام | فریم ورک پر منحصر |
| **انٹرپرائز کے لیے تیار** | پیداوار کے لیے بنایا گیا | فریم ورک کے لحاظ سے مختلف |

## 🚀 شروعات

### ضروریات

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) یا اس سے زیادہ
- Azure OpenAI وسیلہ اور ماڈل تعیناتی کے ساتھ ایک [Azure سبسکرپشن](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` کے ساتھ سائن ان کریں

### مطلوبہ ماحول کے متغیرات

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# پھر سائن ان کریں تاکہ AzureCliCredential ٹوکن حاصل کر سکے
az login
```

```powershell
# پاور شیل
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# پھر سائن ان کریں تاکہ AzureCliCredential ٹوکن حاصل کر سکے
az login
```

### نمونہ کوڈ

کوڈ کی مثال چلانے کے لیے،

```bash
# زی ایس ایچ/باش
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

یا dotnet CLI استعمال کرتے ہوئے:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

مکمل کوڈ کے لیے [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) دیکھیں۔

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

## 🎓 کلیدی نکات

1. **ایجنٹ کا فن تعمیر**: مائیکروسافٹ ایجنٹ فریم ورک .NET میں AI ایجنٹس بنانے کے لیے صاف، قسم محفوظ نقطہ نظر فراہم کرتا ہے
2. **ٹول انضمام**: `[Description]` صفات سے مزین فنکشنز ایجنٹ کے لیے دستیاب ٹولز بن جاتے ہیں
3. **بات چیت کا سیاق و سباق**: سیشن مینجمنٹ مکمل سیاق و سباق کے ساتھ کثیر دور کی بات چیت کی اجازت دیتی ہے
4. **ترتیب کا انتظام**: ماحول کے متغیرات اور محفوظ سند ہینڈلنگ .NET کے بہترین طریقوں کی پیروی کرتی ہے
5. **Azure OpenAI Responses API**: ایجنٹ Azure.AI.OpenAI SDK کے ذریعے Azure OpenAI Responses API استعمال کرتا ہے

## 🔗 اضافی وسائل

- [مائیکروسافٹ ایجنٹ فریم ورک دستاویزات](https://learn.microsoft.com/agent-framework)
- [مائیکروسافٹ فاونڈری میں Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET سنگل فائل ایپس](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->