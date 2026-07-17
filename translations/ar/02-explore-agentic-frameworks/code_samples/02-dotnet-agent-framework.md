# 🔍 استكشاف إطار عمل Microsoft Agent - العميل الأساسي (.NET)

## 📋 أهداف التعلم

يستكشف هذا المثال المفاهيم الأساسية لإطار عمل Microsoft Agent من خلال تنفيذ عميل أساسي في .NET. ستتعلم الأنماط الأساسية للوكيل وتفهم كيفية عمل الوكلاء الأذكياء تحت الغطاء باستخدام C# ونظام .NET البيئي.

### ما الذي ستكتشفه

- 🏗️ **هيكلية الوكيل**: فهم الهيكل الأساسي لوكلاء الذكاء الاصطناعي في .NET
- 🛠️ **تكامل الأدوات**: كيف يستخدم الوكلاء الوظائف الخارجية لتوسيع القدرات  
- 💬 **تدفق المحادثة**: إدارة المحادثات متعددة الجولات والسياق مع إدارة الخيوط
- 🔧 **أنماط التهيئة**: أفضل الممارسات لإعداد الوكيل وإدارته في .NET

## 🎯 المفاهيم الرئيسية المشمولة

### مبادئ إطار العمل الوكلي

- **الاستقلالية**: كيف يتخذ الوكلاء قرارات مستقلة باستخدام تجريدات الذكاء الاصطناعي في .NET
- **التفاعلية**: الاستجابة لتغيرات البيئة ومدخلات المستخدم
- **المبادرة**: اتخاذ المبادرة بناءً على الأهداف والسياق
- **القدرة الاجتماعية**: التفاعل من خلال اللغة الطبيعية مع خيوط المحادثة

### المكونات التقنية

- **AIAgent**: تنسيق الوكيل الأساسي وإدارة المحادثة (.NET)
- **وظائف الأدوات**: توسيع قدرات الوكيل بواسطة طرق وسمات C#
- **تكامل Azure OpenAI**: الاستفادة من نماذج اللغة عبر API استجابات Azure OpenAI
- **التهيئة الآمنة**: إدارة نقاط النهاية بناءً على البيئة

## 🔧 البنية التقنية

### التقنيات الأساسية

- إطار عمل Microsoft Agent (.NET)
- تكامل Azure OpenAI (API استجابات)
- أنماط عميل Azure.AI.OpenAI
- التهيئة بناءً على البيئة مع DotNetEnv

### قدرات الوكيل

- فهم اللغة الطبيعية وتوليدها
- استدعاء الوظائف واستخدام الأدوات مع سمات C#
- استجابات واعية للسياق مع جلسات المحادثة
- هيكلية قابلة للتوسيع مع أنماط حقن التبعيات

## 📚 مقارنة الإطارات

يعرض هذا المثال نهج إطار عمل Microsoft Agent مقارنة بالإطارات الوكلية الأخرى:

| الميزة | إطار عمل Microsoft Agent | إطارات أخرى |
|---------|-------------------------|------------------|
| **التكامل** | نظام Microsoft البيئي الأصلي | توافق متنوع |
| **البساطة** | API نظيف وبديهي | إعداد غالباً معقد |
| **القابلية للتوسيع** | تكامل الأدوات بسهولة | يعتمد على الإطار |
| **جاهزية المؤسسات** | تم التصميم للإنتاج | يختلف حسب الإطار |

## 🚀 البدء

### المتطلبات الأساسية

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) أو أعلى
- اشتراك [Azure](https://azure.microsoft.com/free/) مع مورد Azure OpenAI ونشر النموذج
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — تسجيل الدخول باستخدام `az login`

### متغيرات البيئة المطلوبة

```bash
# زد شيل/باش
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# ثم قم بتسجيل الدخول حتى يتمكن AzureCliCredential من الحصول على رمز مميز
az login
```

```powershell
# باورشل
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# ثم قم بتسجيل الدخول حتى يتمكن AzureCliCredential من الحصول على رمز مميز
az login
```

### مثال على الكود

لتشغيل مثال الكود،

```bash
# زش/باش
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

أو باستخدام CLI لـ dotnet:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

راجع [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) للكود الكامل.

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4.1-mini";

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

## 🎓 النقاط الرئيسية المستفادة

1. **هيكلية الوكيل**: يوفر إطار عمل Microsoft Agent نهجًا نظيفًا وآمن النوع لبناء وكلاء الذكاء الاصطناعي في .NET
2. **تكامل الأدوات**: تصبح الوظائف المزينة بسمات `[Description]` أدوات متاحة للوكيل
3. **سياق المحادثة**: تُمكن إدارة الجلسات المحادثات متعددة الجولات مع وعي كامل بالسياق
4. **إدارة التهيئة**: تتبع متغيرات البيئة والتعامل الآمن مع بيانات الاعتماد أفضل الممارسات في .NET
5. **API استجابات Azure OpenAI**: يستخدم الوكيل API استجابات Azure OpenAI عبر SDK الخاص بـ Azure.AI.OpenAI

## 🔗 مصادر إضافية

- [توثيق إطار عمل Microsoft Agent](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI في Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [تطبيقات ملف واحد في .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->