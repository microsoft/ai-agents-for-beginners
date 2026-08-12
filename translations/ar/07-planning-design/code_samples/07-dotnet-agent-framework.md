# 🎯 أنماط التخطيط والتصميم مع Azure OpenAI (Responses API) (.NET)

## 📋 أهداف التعلم

يعرض هذا الدفتر أنماط تخطيط وتصميم بمستوى مؤسسي لبناء وكلاء ذكيين باستخدام إطار عمل Microsoft Agent في .NET مع Azure OpenAI (Responses API). ستتعلم كيفية إنشاء وكلاء يمكنهم تفكيك المشكلات المعقدة، والتخطيط لحلول متعددة الخطوات، وتنفيذ سير عمل متقدم باستخدام ميزات المؤسسة في .NET.

## ⚙️ المتطلبات المسبقة والإعداد

**بيئة التطوير:**
- .NET 9.0 SDK أو أعلى
- Visual Studio 2022 أو VS Code مع إضافة C#
- اشتراك Azure مع مورد Azure OpenAI ونشر نموذج
- Azure CLI — سجل الدخول باستخدام `az login`

**المكتبات المطلوبة:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**تهيئة البيئة (ملف .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## تشغيل الكود

تتضمن هذه الدرس تطبيق تطبيق ملف فردي في .NET. لتشغيله:

```bash
# اجعل الملف قابلاً للتنفيذ (لينكس/ماك أو إس)
chmod +x 07-dotnet-agent-framework.cs

# شغل التطبيق
./07-dotnet-agent-framework.cs
```

أو استخدم الأمر dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## تنفيذ الكود

التنفيذ الكامل متاح في `07-dotnet-agent-framework.cs`، والذي يوضح:

- تحميل إعدادات البيئة باستخدام DotNetEnv
- تهيئة عميل Azure OpenAI وإنشاء وكيل ذكاء اصطناعي باستخدام `GetChatClient().AsAIAgent()`
- تعريف نماذج بيانات منظمة (Plan و TravelPlan) مع تسلسل JSON
- إنشاء وكيل ذكاء اصطناعي مع إخراج منظم باستخدام مخطط JSON
- تنفيذ طلبات التخطيط مع ردود آمنة من حيث النوع

## المفاهيم الرئيسية

### التخطيط المنظم باستخدام نماذج آمنة من حيث النوع

يستخدم الوكيل فئات C# لتعريف هيكل مخرجات التخطيط:

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### مخطط JSON للمخرجات المنظمة

تم تهيئة الوكيل لإرجاع ردود تتطابق مع مخطط TravelPlan:

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### تعليمات وكيل التخطيط

يعمل الوكيل كمنسق، مفوضًا المهام لوكلاء فرعيين متخصصين:

- FlightBooking: لحجز الرحلات الجوية وتقديم معلومات الرحلات
- HotelBooking: لحجز الفنادق وتقديم معلومات الفنادق
- CarRental: لحجز السيارات وتقديم معلومات تأجير السيارات
- ActivitiesBooking: لحجز الأنشطة وتقديم معلومات الأنشطة
- DestinationInfo: لتقديم معلومات عن الوجهات
- DefaultAgent: للتعامل مع الطلبات العامة

## الناتج المتوقع

عند تشغيل الوكيل مع طلب تخطيط سفر، سيقوم بتحليل الطلب وتوليد خطة منظمة مع تعيين مهام مناسبة للوكلاء المتخصصين، بصيغة JSON تتوافق مع مخطط TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->