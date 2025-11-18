<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T11:03:30+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "ar"
}
-->
# 🔍 استكشاف إطار عمل Microsoft Agent - الوكيل الأساسي (.NET)

## 📋 أهداف التعلم

يستعرض هذا المثال المفاهيم الأساسية لإطار عمل Microsoft Agent من خلال تنفيذ وكيل بسيط باستخدام .NET. ستتعلم أنماط الوكلاء الأساسية وتفهم كيفية عمل الوكلاء الذكيين خلف الكواليس باستخدام C# ونظام .NET.

### ما ستكتشفه

- 🏗️ **هيكل الوكيل**: فهم الهيكل الأساسي لوكلاء الذكاء الاصطناعي في .NET  
- 🛠️ **تكامل الأدوات**: كيفية استخدام الوكلاء للوظائف الخارجية لتوسيع القدرات  
- 💬 **تدفق المحادثة**: إدارة المحادثات متعددة الأدوار والسياق باستخدام إدارة الخيوط  
- 🔧 **أنماط التكوين**: أفضل الممارسات لإعداد الوكلاء وإدارتهم في .NET  

## 🎯 المفاهيم الرئيسية المغطاة

### مبادئ إطار عمل الوكلاء

- **الاستقلالية**: كيفية اتخاذ الوكلاء قرارات مستقلة باستخدام تجريدات الذكاء الاصطناعي في .NET  
- **التفاعل**: الاستجابة للتغيرات البيئية ومدخلات المستخدم  
- **المبادرة**: اتخاذ الإجراءات بناءً على الأهداف والسياق  
- **القدرة الاجتماعية**: التفاعل من خلال اللغة الطبيعية باستخدام خيوط المحادثة  

### المكونات التقنية

- **AIAgent**: إدارة الوكيل الأساسية وتنظيم المحادثات (.NET)  
- **وظائف الأدوات**: توسيع قدرات الوكلاء باستخدام طرق وسمات C#  
- **تكامل OpenAI**: الاستفادة من نماذج اللغة من خلال واجهات برمجة التطبيقات القياسية لـ .NET  
- **التكوين الآمن**: إدارة مفاتيح API بناءً على البيئة  

## 🔧 البنية التقنية

### التقنيات الأساسية

- إطار عمل Microsoft Agent (.NET)  
- تكامل واجهة برمجة تطبيقات نماذج GitHub  
- أنماط العميل المتوافقة مع OpenAI  
- التكوين المستند إلى البيئة باستخدام DotNetEnv  

### قدرات الوكيل

- فهم اللغة الطبيعية وتوليدها  
- استدعاء الوظائف واستخدام الأدوات باستخدام سمات C#  
- استجابات مدركة للسياق باستخدام خيوط المحادثة  
- هيكل قابل للتوسيع باستخدام أنماط حقن التبعيات  

## 📚 مقارنة الإطارات

يوضح هذا المثال نهج إطار عمل Microsoft Agent مقارنةً بإطارات الوكلاء الأخرى:

| الميزة | إطار عمل Microsoft Agent | الإطارات الأخرى |
|--------|--------------------------|-----------------|
| **التكامل** | نظام Microsoft الأصلي | توافق متنوع |
| **البساطة** | واجهة برمجة تطبيقات نظيفة وبديهية | إعداد غالبًا معقد |
| **التوسعية** | تكامل الأدوات بسهولة | يعتمد على الإطار |
| **جاهزية المؤسسات** | مصمم للإنتاج | يختلف حسب الإطار |

## 🚀 البدء

### المتطلبات الأساسية

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) أو أعلى  
- [رمز الوصول لواجهة برمجة تطبيقات نماذج GitHub](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### متغيرات البيئة المطلوبة

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
  

### نموذج الكود

لتشغيل مثال الكود،  

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
أو باستخدام CLI الخاص بـ dotnet:  

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
راجع [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) للحصول على الكود الكامل.  

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
  

## 🎓 النقاط الرئيسية

1. **هيكل الوكيل**: يوفر إطار عمل Microsoft Agent نهجًا نظيفًا وآمنًا من النوع لبناء وكلاء الذكاء الاصطناعي في .NET  
2. **تكامل الأدوات**: الوظائف المزينة بسمات `[Description]` تصبح أدوات متاحة للوكيل  
3. **سياق المحادثة**: إدارة الخيوط تمكن المحادثات متعددة الأدوار مع إدراك كامل للسياق  
4. **إدارة التكوين**: متغيرات البيئة ومعالجة بيانات الاعتماد الآمنة تتبع أفضل ممارسات .NET  
5. **التوافق مع OpenAI**: يعمل تكامل نماذج GitHub بسلاسة من خلال واجهات برمجة التطبيقات المتوافقة مع OpenAI  

## 🔗 موارد إضافية

- [وثائق إطار عمل Microsoft Agent](https://learn.microsoft.com/agent-framework)  
- [سوق نماذج GitHub](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->