<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T11:13:57+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "ur"
}
-->
# 🔍 مائیکروسافٹ ایجنٹ فریم ورک کا جائزہ - بنیادی ایجنٹ (.NET)

## 📋 سیکھنے کے مقاصد

یہ مثال مائیکروسافٹ ایجنٹ فریم ورک کے بنیادی تصورات کو .NET میں ایک بنیادی ایجنٹ کے نفاذ کے ذریعے دریافت کرتی ہے۔ آپ ایجنٹک پیٹرنز کے بنیادی اصول سیکھیں گے اور سمجھیں گے کہ ذہین ایجنٹس C# اور .NET ایکو سسٹم کے تحت کیسے کام کرتے ہیں۔

### آپ کیا سیکھیں گے

- 🏗️ **ایجنٹ کی ساخت**: .NET میں AI ایجنٹس کی بنیادی ساخت کو سمجھنا  
- 🛠️ **ٹول انٹیگریشن**: ایجنٹس بیرونی فنکشنز کا استعمال کرکے صلاحیتوں کو کیسے بڑھاتے ہیں  
- 💬 **گفتگو کا بہاؤ**: ملٹی ٹرن گفتگو اور تھریڈ مینجمنٹ کے ذریعے سیاق و سباق کا انتظام  
- 🔧 **کنفیگریشن پیٹرنز**: .NET میں ایجنٹ سیٹ اپ اور مینجمنٹ کے بہترین طریقے  

## 🎯 اہم تصورات

### ایجنٹک فریم ورک کے اصول

- **خود مختاری**: .NET AI ایبسٹریکشنز کا استعمال کرتے ہوئے ایجنٹس خود مختار فیصلے کیسے کرتے ہیں  
- **ردعمل**: ماحولیاتی تبدیلیوں اور صارف کے ان پٹ پر ردعمل دینا  
- **پیش قدمی**: اہداف اور سیاق و سباق کی بنیاد پر پہل کرنا  
- **سماجی صلاحیت**: گفتگو کے تھریڈز کے ذریعے قدرتی زبان میں بات چیت کرنا  

### تکنیکی اجزاء

- **AIAgent**: ایجنٹ کی بنیادی آرکیسٹریشن اور گفتگو کا انتظام (.NET)  
- **ٹول فنکشنز**: C# میتھڈز اور ایٹریبیوٹس کے ذریعے ایجنٹ کی صلاحیتوں کو بڑھانا  
- **OpenAI انٹیگریشن**: معیاری .NET APIs کے ذریعے لینگویج ماڈلز کا استعمال  
- **محفوظ کنفیگریشن**: API کیز کا ماحول پر مبنی انتظام  

## 🔧 تکنیکی اسٹیک

### بنیادی ٹیکنالوجیز

- مائیکروسافٹ ایجنٹ فریم ورک (.NET)  
- GitHub Models API انٹیگریشن  
- OpenAI-کمپیٹیبل کلائنٹ پیٹرنز  
- DotNetEnv کے ساتھ ماحول پر مبنی کنفیگریشن  

### ایجنٹ کی صلاحیتیں

- قدرتی زبان کو سمجھنا اور پیدا کرنا  
- فنکشن کالنگ اور C# ایٹریبیوٹس کے ساتھ ٹول کا استعمال  
- گفتگو کے تھریڈز کے ساتھ سیاق و سباق پر مبنی جوابات  
- ڈپینڈنسی انجیکشن پیٹرنز کے ساتھ قابل توسیع آرکیٹیکچر  

## 📚 فریم ورک کا موازنہ

یہ مثال مائیکروسافٹ ایجنٹ فریم ورک کے طریقے کو دیگر ایجنٹک فریم ورکس کے مقابلے میں ظاہر کرتی ہے:

| خصوصیت | مائیکروسافٹ ایجنٹ فریم ورک | دیگر فریم ورکس |
|---------|-------------------------|------------------|
| **انٹیگریشن** | مائیکروسافٹ ایکو سسٹم کے ساتھ مطابقت | مختلف مطابقت |
| **سادگی** | صاف، آسان API | اکثر پیچیدہ سیٹ اپ |
| **توسیع پذیری** | ٹول انٹیگریشن میں آسانی | فریم ورک پر منحصر |
| **انٹرپرائز ریڈی** | پروڈکشن کے لیے بنایا گیا | فریم ورک کے لحاظ سے مختلف |

## 🚀 شروعات کریں

### ضروریات

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) یا اس سے زیادہ  
- [GitHub Models API ایکسیس ٹوکن](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### مطلوبہ ماحول متغیرات

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
  

### نمونہ کوڈ

کوڈ مثال چلانے کے لیے،  

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
یا dotnet CLI کا استعمال کرتے ہوئے:  

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
مکمل کوڈ کے لیے [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) دیکھیں۔  

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
  

## 🎓 اہم نکات

1. **ایجنٹ کی ساخت**: مائیکروسافٹ ایجنٹ فریم ورک .NET میں AI ایجنٹس بنانے کے لیے صاف، ٹائپ سیف طریقہ فراہم کرتا ہے  
2. **ٹول انٹیگریشن**: `[Description]` ایٹریبیوٹس کے ساتھ سجائے گئے فنکشنز ایجنٹ کے لیے دستیاب ٹولز بن جاتے ہیں  
3. **گفتگو کا سیاق و سباق**: تھریڈ مینجمنٹ ملٹی ٹرن گفتگو کو مکمل سیاق و سباق کے ساتھ فعال بناتا ہے  
4. **کنفیگریشن مینجمنٹ**: ماحول متغیرات اور محفوظ اسناد کا انتظام .NET کے بہترین طریقوں پر عمل کرتا ہے  
5. **OpenAI مطابقت**: GitHub Models انٹیگریشن OpenAI-کمپیٹیبل APIs کے ذریعے بغیر کسی رکاوٹ کے کام کرتا ہے  

## 🔗 اضافی وسائل

- [مائیکروسافٹ ایجنٹ فریم ورک دستاویزات](https://learn.microsoft.com/agent-framework)  
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET سنگل فائل ایپس](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**اعلانِ لاتعلقی**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->