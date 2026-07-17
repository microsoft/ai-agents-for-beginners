# 🎯 التخطيط وأنماط التصميم مع Azure OpenAI (API الاستجابات) (.NET)

## 📋 أهداف التعلم

يُظهر هذا الدفتر أنماط تخطيط وتصميم على مستوى المؤسسات لبناء وكلاء أذكياء باستخدام إطار عمل Microsoft Agent في .NET مع Azure OpenAI (API الاستجابات). ستتعلم كيفية إنشاء وكلاء يمكنهم تحليل المشكلات المعقدة، وتخطيط حلول متعددة الخطوات، وتنفيذ سير عمل متقدم باستخدام ميزات المؤسسات في .NET.

## ⚙️ المتطلبات المسبقة والإعداد

**بيئة التطوير:**
- .NET 9.0 SDK أو أعلى
- Visual Studio 2022 أو VS Code مع ملحق C#
- اشتراك Azure يحتوي على مورد Azure OpenAI ونشر نموذج
- Azure CLI — قم بتسجيل الدخول باستخدام `az login`

**التبعيات المطلوبة:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**تكوين البيئة (ملف .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

## تشغيل الكود

تتضمن هذه الدرس تطبيق تطبيق ملف واحد .NET. لتشغيله:

```bash
# اجعل الملف قابلاً للتنفيذ (لينكس/ماك أو إس)
chmod +x 07-dotnet-agent-framework.cs

# شغّل التطبيق
./07-dotnet-agent-framework.cs
```

أو استخدم أمر dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## تنفيذ الكود

يتوفر التنفيذ الكامل في `07-dotnet-agent-framework.cs`، الذي يوضح:

- تحميل تكوين البيئة باستخدام DotNetEnv
- تكوين عميل Azure OpenAI وإنشاء وكيل ذكاء اصطناعي باستخدام `GetChatClient().AsAIAgent()`
- تعريف نماذج بيانات منظمة (Plan و TravelPlan) مع تسلسل JSON
- إنشاء وكيل ذكاء اصطناعي بمخرجات منظمة باستخدام مخطط JSON
- تنفيذ طلبات التخطيط مع ردود آمنة النوع

## المفاهيم الرئيسية

### التخطيط المنظم باستخدام نماذج آمنة النوع

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

تم تكوين الوكيل لإرجاع استجابات تطابق مخطط TravelPlan:

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

يعمل الوكيل كمنسق، مفوضًا المهام إلى وكلاء متخصصين:

- حجز الرحلات الجوية: لحجز الرحلات وتوفير معلومات الرحلات
- حجز الفنادق: لحجز الفنادق وتوفير معلومات الفنادق
- تأجير السيارات: لحجز السيارات وتوفير معلومات تأجير السيارات
- حجز الأنشطة: لحجز الأنشطة وتوفير معلومات الأنشطة
- معلومات الوجهة: لتوفير معلومات عن الوجهات
- الوكيل الافتراضي: للتعامل مع الطلبات العامة

## المخرجات المتوقعة

عند تشغيل الوكيل مع طلب تخطيط السفر، سيقوم بتحليل الطلب وتوليد خطة منظمة مع تعيينات المهام المناسبة للوكلاء المتخصصين، منسقة بصيغة JSON تتوافق مع مخطط TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->