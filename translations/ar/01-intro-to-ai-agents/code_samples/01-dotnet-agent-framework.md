# 🌍 وكيل السفر الذكي باستخدام إطار عمل Microsoft Agent (.NET)

## 📋 نظرة عامة على السيناريو

يوضح هذا المثال كيفية بناء وكيل ذكي لتخطيط السفر باستخدام إطار عمل Microsoft Agent لنظام .NET. يمكن للوكيل إنشاء جداول زمنية مخصصة لرحلات يومية إلى وجهات عشوائية حول العالم تلقائيًا.

### القدرات الرئيسية:

- 🎲 **اختيار وجهة عشوائية**: يستخدم أداة مخصصة لاختيار أماكن الإجازات
- 🗺️ **تخطيط الرحلة الذكي**: ينشئ مسارات يومية مفصلة
- 🔄 **البث في الوقت الفعلي**: يدعم الردود الفورية والبثية
- 🛠️ **تكامل الأدوات المخصصة**: يوضح كيفية توسيع قدرات الوكيل

## 🔧 البنية التقنية

### التقنيات الأساسية

- **إطار عمل Microsoft Agent**: أحدث تطبيق .NET لتطوير وكلاء الذكاء الاصطناعي
- **Azure OpenAI (API الردود)**: يستخدم Azure OpenAI API للردود لاستخلاص النماذج
- **Azure Identity**: تسجيل دخول آمن عبر `AzureCliCredential` (`az login`)
- **التكوين الآمن**: إدارة نقاط النهاية بناءً على البيئة

### المكونات الرئيسية

1. **AIAgent**: منسق الوكيل الرئيسي الذي يدير تدفق المحادثة
2. **الأدوات المخصصة**: دالة `GetRandomDestination()` متاحة للوكيل
3. **عميل الردود**: واجهة المحادثة المعتمدة على Azure OpenAI Responses
4. **دعم البث**: قدرات إنشاء ردود في الوقت الفعلي

### نمط التكامل

```mermaid
graph LR
    A[طلب المستخدم] --> B[وكيل الذكاء الاصطناعي]
    B --> C[أزور OpenAI (واجهة برمجة التطبيقات للردود)]
    B --> D[أداة الحصول على وجهة عشوائية]
    C --> E[مسار السفر]
    D --> E
```

## 🚀 بدء الاستخدام

### المتطلبات الأساسية

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) أو أحدث
- [اشتراك Azure](https://azure.microsoft.com/free/) مع مورد Azure OpenAI ونشر نموذج
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — سجل الدخول باستخدام `az login`

### متغيرات البيئة المطلوبة

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# ثم سجّل الدخول حتى يتمكن AzureCliCredential من الحصول على رمز مميز
az login
```

```powershell
# باورشيل
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# ثم سجل الدخول حتى يتمكن AzureCliCredential من الحصول على رمز مميز
az login
```

### مثال على الكود

لتشغيل مثال الكود،

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

أو باستخدام dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

راجع [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) للكود الكامل.

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4.1-mini";

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

1. **بنية الوكيل**: يوفر إطار عمل Microsoft Agent طريقة نظيفة وآمنة نوعياً لبناء وكلاء الذكاء الاصطناعي في .NET
2. **تكامل الأدوات**: تصبح الدوال المزينة بسمات `[Description]` أدوات متاحة للوكيل
3. **إدارة التكوين**: تتبع متغيرات البيئة والتعامل الآمن مع بيانات الاعتماد أفضل ممارسات .NET
4. **Azure OpenAI Responses API**: يستخدم الوكيل Azure OpenAI Responses API عبر SDK الخاص بـ Azure.AI.OpenAI

## 🔗 مصادر إضافية

- [توثيق إطار عمل Microsoft Agent](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI في Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET تطبيقات الملف الواحد](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->