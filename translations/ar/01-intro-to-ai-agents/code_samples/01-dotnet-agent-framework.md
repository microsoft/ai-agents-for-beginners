# 🌍 عميل سفر ذكي باستخدام Microsoft Agent Framework (.NET)

## 📋 نظرة عامة على السيناريو

يوضح هذا المثال كيفية بناء وكيل تخطيط سفر ذكي باستخدام Microsoft Agent Framework لـ .NET. يمكن للوكيل إنشاء جداول رحلات يومية مخصصة تلقائيًا لوجهات عشوائية حول العالم.

### القدرات الرئيسية:

- 🎲 **اختيار الوجهة العشوائية**: يستخدم أداة مخصصة لاختيار مواقع العطلات
- 🗺️ **تخطيط الرحلات الذكي**: ينشئ جداول تفصيلية يومية للرحلات
- 🔄 **البث المباشر في الوقت الحقيقي**: يدعم الاستجابات الفورية والبث المباشر
- 🛠️ **دمج أدوات مخصصة**: يوضح كيفية توسيع قدرات الوكيل

## 🔧 البنية التقنية

### التقنيات الأساسية

- **Microsoft Agent Framework**: أحدث تنفيذ لـ .NET لتطوير وكلاء الذكاء الاصطناعي
- **Azure OpenAI (استجابات API)**: يستخدم Azure OpenAI Responses API للاستدلال بالنموذج
- **Azure Identity**: تسجيل دخول آمن عبر `AzureCliCredential` (`az login`)
- **تكوين آمن**: إدارة نقاط النهاية بناءً على البيئة

### المكونات الرئيسية

1. **AIAgent**: المنسق الرئيسي للوكيل الذي يتعامل مع سير المحادثة
2. **أدوات مخصصة**: دالة `GetRandomDestination()` متاحة للوكيل
3. **عميل الاستجابات**: واجهة محادثة تعتمد على Azure OpenAI Responses
4. **دعم البث**: قدرات توليد الاستجابات في الوقت الحقيقي

### نمط الدمج

```mermaid
graph LR
    A[طلب المستخدم] --> B[وكيل الذكاء الاصطناعي]
    B --> C[أزور أوبن إيه آي (واجهة برمجة التطبيقات للاستجابات)]
    B --> D[أداة الحصول على وجهة عشوائية]
    C --> E[جدول الرحلة]
    D --> E
```

## 🚀 بدء الاستخدام

### المتطلبات الأساسية

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) أو إصدار أعلى
- اشتراك في [Azure](https://azure.microsoft.com/free/) مع مورد Azure OpenAI ونشر نموذج
- أداة [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — تسجيل الدخول باستخدام `az login`

### المتغيرات البيئية المطلوبة

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# ثم قم بتسجيل الدخول حتى يتمكن AzureCliCredential من الحصول على رمز مميز
az login
```

```powershell
# باورشيل
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# ثم سجّل الدخول حتى يتمكن AzureCliCredential من الحصول على رمز مميز
az login
```

### مثال على الكود

لتشغيل مثال الكود،

```bash
# زد شل/باش
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

أو باستخدام أداة dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

انظر [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) للكود الكامل.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.4.1
#:package Microsoft.Agents.AI.OpenAI@1.1.0
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

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip
// Run the agent with streaming enabled for real-time response display
// Shows the agent's thinking and response as it generates the content
// Provides better user experience with immediate feedback
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 النقاط الرئيسية المستفادة

1. **بنية الوكيل**: يوفر Microsoft Agent Framework نهجًا نظيفًا وآمن النوع لبناء وكلاء الذكاء الاصطناعي في .NET
2. **دمج الأدوات**: الوظائف المزينة بـ `[Description]` تصبح أدوات متاحة للوكيل
3. **إدارة التكوين**: تتبع المتغيرات البيئية والتعامل الآمن مع بيانات الاعتماد أفضل الممارسات في .NET
4. **Azure OpenAI Responses API**: يستخدم الوكيل Azure OpenAI Responses API عبر Azure.AI.OpenAI SDK

## 🔗 موارد إضافية

- [توثيق Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI في Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->