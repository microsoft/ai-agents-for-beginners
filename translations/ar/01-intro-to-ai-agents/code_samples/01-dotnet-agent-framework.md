<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "23afd9be7b6ba5b69a44c3b6a78e07f6",
  "translation_date": "2025-11-06T10:01:34+00:00",
  "source_file": "01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.md",
  "language_code": "ar"
}
-->
# 🌍 وكيل السفر الذكي باستخدام إطار عمل Microsoft Agent (.NET)

## 📋 نظرة عامة على السيناريو

يوضح هذا الدفتر كيفية بناء وكيل تخطيط سفر ذكي باستخدام إطار عمل Microsoft Agent لـ .NET. يمكن للوكيل إنشاء خطط رحلات يومية مخصصة تلقائيًا لوجهات عشوائية حول العالم.

**القدرات الرئيسية:**
- 🎲 **اختيار الوجهة العشوائية**: يستخدم أداة مخصصة لاختيار أماكن العطلات
- 🗺️ **تخطيط الرحلات الذكي**: ينشئ خطط يومية مفصلة
- 🔄 **البث في الوقت الحقيقي**: يدعم الاستجابات الفورية والمتدفقة
- 🛠️ **دمج الأدوات المخصصة**: يوضح كيفية توسيع قدرات الوكيل

## 🔧 الهندسة التقنية

### التقنيات الأساسية
- **إطار عمل Microsoft Agent**: أحدث تنفيذ لـ .NET لتطوير وكلاء الذكاء الاصطناعي
- **دمج نماذج GitHub**: يستخدم خدمة استنتاج نماذج الذكاء الاصطناعي من GitHub
- **التوافق مع OpenAI API**: يعتمد على مكتبات عملاء OpenAI مع نقاط نهاية مخصصة
- **التكوين الآمن**: إدارة مفاتيح API بناءً على البيئة

### المكونات الرئيسية
1. **AIAgent**: المنسق الرئيسي للوكيل الذي يتعامل مع تدفق المحادثة
2. **الأدوات المخصصة**: وظيفة `GetRandomDestination()` المتاحة للوكيل
3. **عميل المحادثة**: واجهة محادثة مدعومة بنماذج GitHub
4. **دعم البث**: قدرات إنشاء الاستجابات في الوقت الحقيقي

### نمط التكامل
```mermaid
graph LR
    A[User Request] --> B[AI Agent]
    B --> C[GitHub Models API]
    B --> D[GetRandomDestination Tool]
    C --> E[Travel Itinerary]
    D --> E
```

## 🚀 البدء

**المتطلبات الأساسية:**
- .NET 10.0 أو أعلى
- رمز الوصول إلى API لنماذج GitHub
- متغيرات البيئة مهيأة في ملف `.env`

**متغيرات البيئة المطلوبة:**
```env
GITHUB_TOKEN=your_github_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

قم بتشغيل نموذج الكود أدناه بالتسلسل لرؤية وكيل السفر أثناء العمل!

---

## تطبيق ملف واحد لـ .NET: مثال وكيل السفر الذكي

راجع `01-dotnet-agent-framework.cs` للحصول على نموذج الكود الكامل القابل للتشغيل.

```bash
dotnet run 01-dotnet-agent-framework.cs
```

### نموذج الكود

```csharp
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

// Extract configuration from environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI Client Options
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

// Create AI Agent with Travel Planning Capabilities
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip (Non-Streaming)
Console.WriteLine(await agent.RunAsync("Plan me a day trip"));

// Execute Agent: Plan a Day Trip (Streaming Response)
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    Console.Write(update);
}
```

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.