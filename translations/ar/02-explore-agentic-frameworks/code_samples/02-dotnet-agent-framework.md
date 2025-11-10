<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:31:13+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "ar"
}
-->
# 🔍 استكشاف أطر العمل الذكية - الوكيل الأساسي (.NET)

## 📋 أهداف التعلم

يستعرض هذا الدليل المفاهيم الأساسية لإطار عمل الوكيل من مايكروسوفت من خلال تنفيذ وكيل بسيط باستخدام .NET. ستتعلم أنماط الوكلاء الأساسية وتفهم كيفية عمل الوكلاء الذكيين خلف الكواليس باستخدام C# ونظام .NET.

**ما ستكتشفه:**
- 🏗️ **هيكلية الوكيل**: فهم الهيكل الأساسي لوكلاء الذكاء الاصطناعي في .NET  
- 🛠️ **تكامل الأدوات**: كيفية استخدام الوكلاء للوظائف الخارجية لتوسيع القدرات  
- 💬 **تدفق المحادثة**: إدارة المحادثات متعددة الأدوار والسياق باستخدام إدارة الخيوط  
- 🔧 **أنماط التكوين**: أفضل الممارسات لإعداد وإدارة الوكلاء في .NET  

## 🎯 المفاهيم الرئيسية المغطاة

### مبادئ إطار العمل الذكي
- **الاستقلالية**: كيفية اتخاذ الوكلاء قرارات مستقلة باستخدام تجريدات الذكاء الاصطناعي في .NET  
- **التفاعل**: الاستجابة للتغيرات البيئية ومدخلات المستخدم  
- **المبادرة**: اتخاذ الإجراءات بناءً على الأهداف والسياق  
- **القدرة الاجتماعية**: التفاعل من خلال اللغة الطبيعية مع خيوط المحادثة  

### المكونات التقنية
- **AIAgent**: إدارة تنظيم الوكيل والمحادثات (.NET)  
- **وظائف الأدوات**: توسيع قدرات الوكيل باستخدام طرق وسمات C#  
- **تكامل OpenAI**: الاستفادة من نماذج اللغة من خلال واجهات برمجة التطبيقات القياسية في .NET  
- **إدارة البيئة**: إعداد آمن ومعالجة بيانات الاعتماد باستخدام DotNetEnv  

## ⚙️ المتطلبات والإعداد

**المتطلبات الأساسية:**
- .NET 9.0 SDK أو أعلى  
- Visual Studio 2022 أو VS Code مع امتداد C#  

**حزم NuGet:**
- `Microsoft.Extensions.AI` - تجريدات الذكاء الاصطناعي الأساسية  
- `Microsoft.Extensions.AI.OpenAI` - تكامل OpenAI (معاينة)  
- `DotNetEnv` - إدارة متغيرات البيئة  

**تكوين البيئة (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```
  
## 🔧 التقنية المستخدمة

**التقنيات الأساسية:**
- إطار عمل الوكيل من مايكروسوفت (.NET)  
- تكامل API لنماذج GitHub  
- أنماط العميل المتوافقة مع OpenAI  
- التكوين المستند إلى البيئة باستخدام DotNetEnv  

**قدرات الوكيل:**
- فهم اللغة الطبيعية وتوليدها  
- استدعاء الوظائف واستخدام الأدوات باستخدام سمات C#  
- استجابات مدركة للسياق مع خيوط المحادثة  
- هيكلية قابلة للتوسيع مع أنماط حقن التبعيات  

## 📚 مقارنة الأطر

يوضح هذا المثال نهج إطار عمل الوكيل من مايكروسوفت في .NET مقارنة بالمنصات الأخرى:

| الميزة | إطار عمل الوكيل في .NET | المكافئات في Python |
|---------|---------------------|-------------------|
| **سلامة النوع** | كتابة قوية باستخدام C# | كتابة ديناميكية |
| **التكامل** | نظام .NET الأصلي | توافق متنوع |
| **الأداء** | أداء الكود المترجم | تنفيذ مفسر |
| **جاهزية المؤسسات** | مصمم لتطبيقات الإنتاج في .NET | يختلف حسب الإطار |
| **الأدوات** | تكامل Visual Studio | يعتمد على بيئة التطوير |

## 🚀 البدء

اتبع الخطوات أدناه لبناء أول وكيل أساسي في .NET وفهم المفاهيم الذكية الأساسية!

## 📦 التثبيت والإعداد

هذا المثال متاح كتطبيق ملف واحد قابل للتشغيل في .NET. راجع الملف المرفق `02-dotnet-agent-framework.cs` للحصول على التنفيذ الكامل.

لتشغيل هذا المثال:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
أو باستخدام dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```
  
## 💡 استعراض الكود

يتضمن التنفيذ الكامل:

### 1. تبعيات الحزم

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
  
### 2. الواردات الأساسية

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```
  
### 3. تكوين البيئة

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```
  
### 4. تعريف وظائف الأدوات

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
  
### 5. إعداد التكوين والعميل

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
  
### 6. تكوين الوكيل

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
  
### 7. تهيئة الوكيل

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
  
### 8. إدارة المحادثة

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```
  
## 🎓 النقاط الرئيسية

1. **هيكلية الوكيل**: يوفر إطار عمل الوكيل من مايكروسوفت نهجًا نظيفًا وآمنًا لبناء وكلاء الذكاء الاصطناعي في .NET  
2. **تكامل الأدوات**: الوظائف المزينة بـ `[Description]` تصبح أدوات متاحة للوكيل  
3. **سياق المحادثة**: إدارة الخيوط تمكن المحادثات متعددة الأدوار مع إدراك كامل للسياق  
4. **إدارة التكوين**: متغيرات البيئة ومعالجة بيانات الاعتماد الآمنة تتبع أفضل ممارسات .NET  
5. **التوافق مع OpenAI**: يعمل تكامل نماذج GitHub بسلاسة من خلال واجهات برمجة التطبيقات المتوافقة مع OpenAI  

## 🔗 موارد إضافية

- [وثائق إطار عمل الوكيل من مايكروسوفت](https://learn.microsoft.com/en-us/dotnet/ai/agents)  
- [سوق نماذج GitHub](https://github.com/marketplace/models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)  
- [تطبيقات ملف واحد في .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)  

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.