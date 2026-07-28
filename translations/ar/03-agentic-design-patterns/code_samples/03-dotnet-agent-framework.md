# 🎨 أنماط التصميم الوكيلية مع Azure OpenAI (واجهات برمجة استجابات) (.NET)

## 📋 أهداف التعلم

يوضح هذا المثال أنماط تصميم على مستوى المؤسسات لبناء وكلاء أذكياء باستخدام إطار عمل Microsoft Agent في .NET مع تكامل Azure OpenAI (واجهات برمجة استجابات). ستتعلم أنماطًا احترافية ونهجًا معماريًا تجعل الوكلاء جاهزين للإنتاج، وقابلين للصيانة، وقابلين للتوسع.

### أنماط التصميم المؤسسية

- 🏭 **نمط المصنع**: إنشاء وكيل موحد مع حقن التبعيات
- 🔧 **نمط الباني**: إعداد وتكوين وكيل بطريقة متسلسلة
- 🧵 **أنماط السلامة في الخيوط**: إدارة المحادثات المتزامنة
- 📋 **نمط المستودع**: تنظيم أدوات وإدارة القدرات

## 🎯 فوائد معمارية محددة لـ .NET

### ميزات المؤسسات

- **الكتابة القوية**: التحقق في وقت الترجمة ودعم IntelliSense
- **حقن التبعيات**: تكامل حاوية DI المدمجة
- **إدارة التكوين**: أنماط IConfiguration والخيارات
- **Async/Await**: دعم البرمجة اللامتزامنة من الدرجة الأولى

### أنماط جاهزة للإنتاج

- **تكامل التسجيل**: دعم ILogger والتسجيل الهيكلي
- **فحوصات الصحة**: المراقبة والتشخيص المدمجين
- **التحقق من التكوين**: الكتابة القوية مع تعليقات البيانات
- **معالجة الأخطاء**: إدارة الاستثناءات بشكل منظم

## 🔧 العمارة التقنية

### مكونات .NET الأساسية

- **Microsoft.Extensions.AI**: تجريدات موحدة لخدمات الذكاء الاصطناعي
- **Microsoft.Agents.AI**: إطار عمل تنظيم الوكلاء للمؤسسات
- **Azure OpenAI (واجهات برمجة الاستجابات)**: أنماط عملاء API عالية الأداء
- **نظام التكوين**: appsettings.json والتكامل مع البيئة

### تنفيذ نمط التصميم

```mermaid
graph LR
    A[مجموعة خدمات IIService] --> B[منشئ الوكيل]
    B --> C[الإعدادات]
    C --> D[سجل الأدوات]
    D --> E[وكيل الذكاء الاصطناعي]
```

## 🏗️ أنماط المؤسسات المطبقة

### 1. **أنماط إنشائية**

- **مصنع الوكلاء**: إنشاء مركزي للوكلاء مع تكوين متناسق
- **نمط الباني**: API متسلسلة لتكوين الوكيل المعقد
- **نمط المفرد**: مشاركة الموارد وإدارة التكوين
- **حقن التبعيات**: فصل مرن وقابلية الاختبار

### 2. **أنماط سلوكية**

- **نمط الإستراتيجية**: استراتيجيات تنفيذ أدوات قابلة للتبديل
- **نمط الأمر**: عمليات وكيل مغلفة مع التراجع/الإعادة
- **نمط المراقب**: إدارة دورة حياة الوكيل بالحدث
- **طريقة القالب**: سير عمل تنفيذ وكيل موحد

### 3. **أنماط هيكلية**

- **نمط المحول**: طبقة تكامل Azure OpenAI (واجهات برمجة الاستجابات)
- **نمط الزخرفة**: تعزيز قدرات الوكيل
- **نمط الواجهة الأمامية**: تبسيط واجهات تفاعل الوكيل
- **نمط الوكيل الوكيل**: التحميل الكسول والتخزين المؤقت للأداء

## 📚 مبادئ تصميم .NET

### مبادئ SOLID

- **المسؤولية الفردية**: كل مكون له هدف واضح واحد
- **الفتح/الإغلاق**: القابلية للتوسعة بدون تعديل
- **استبدال ليسكوف**: تنفيذات الأدوات القائمة على الواجهات
- **تقسيم الواجهات**: واجهات مركزة ومتناسقة
- **انعكاس التبعيات**: الاعتماد على التجريدات، لا على التفاصيل

### العمارة النظيفة

- **طبقة النطاق**: التجريدات الأساسية للوكلاء والأدوات
- **طبقة التطبيق**: تنظيم الوكلاء وسير العمل
- **طبقة البنية التحتية**: تكامل Azure OpenAI (واجهات برمجة الاستجابات) والخدمات الخارجية
- **طبقة العرض**: تفاعل المستخدم وتنسيق الاستجابات

## 🔒 اعتبارات المؤسسات

### الأمان

- **إدارة بيانات الاعتماد**: التعامل الآمن مع مفتاح API باستخدام IConfiguration
- **التحقق من الإدخال**: الكتابة القوية والتحقق بتعليقات البيانات
- **تنقية الإخراج**: معالجة وتصفية الاستجابات بأمان
- **تسجيل التدقيق**: تتبع شامل للعمليات

### الأداء

- **أنماط اللامزامنة**: عمليات I/O غير محجوزة
- **تجميع الاتصالات**: إدارة فعالة لعميل HTTP
- **التخزين المؤقت**: تخزين الاستجابات لتحسين الأداء
- **إدارة الموارد**: أنماط التخلص والتنظيف المناسبة

### القابلية للتوسع

- **سلامة الخيوط**: دعم تنفيذ الوكلاء المتزامن
- **تجميع الموارد**: استخدام الموارد بكفاءة
- **إدارة الحمل**: تحديد السرعة والتعامل مع الضغط الخلفي
- **المراقبة**: مؤشرات الأداء وفحوصات الصحة

## 🚀 النشر للإنتاج

- **إدارة التكوين**: إعدادات خاصة بالبيئة
- **استراتيجية التسجيل**: تسجيل هيكلي بمعرفات الترابط
- **معالجة الأخطاء**: التعامل مع الاستثناءات العالمي مع استرداد مناسب
- **المراقبة**: رؤى التطبيقات ومؤشرات الأداء
- **الاختبار**: اختبارات الوحدة، الاختبارات التكاملية، وأنماط اختبار الحمل

هل أنت مستعد لبناء وكلاء أذكياء على مستوى المؤسسات مع .NET؟ هيا لنصمم شيئًا قويًا! 🏢✨

## 🚀 البدء

### المتطلبات المسبقة

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) أو أحدث
- [اشتراك Azure](https://azure.microsoft.com/free/) مع مورد Azure OpenAI ونشر نموذج
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — قم بتسجيل الدخول باستخدام `az login`

### المتغيرات البيئية المطلوبة

```bash
# زد شيل/باش
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# ثم قم بتسجيل الدخول حتى يتمكن AzureCliCredential من الحصول على رمز مميز
az login
```

```powershell
# باور شيل
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# ثم قم بتسجيل الدخول حتى يتمكن AzureCliCredential من الحصول على رمز مميز
az login
```

### مثال على الكود

لتشغيل مثال الكود،

```bash
# زي شيل / باش
chmod +x ./03-dotnet-agent-framework.cs
./03-dotnet-agent-framework.cs
```

أو باستخدام CLI دوت نت:

```bash
dotnet run ./03-dotnet-agent-framework.cs
```

راجع [`03-dotnet-agent-framework.cs`](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs) للكود الكامل.

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
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->