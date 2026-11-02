# 🤝 أنظمة سير العمل متعددة الوكلاء للمؤسسات (.NET)

## 📋 أهداف التعلم

يوضح هذا الدفتر كيفية بناء أنظمة متعددة الوكلاء متقدمة على مستوى المؤسسات باستخدام إطار عمل Microsoft Agent في .NET مع Azure OpenAI (واجهات برمجة التطبيقات للردود). ستتعلم كيفية تنسيق عدة وكلاء متخصصين يعملون معًا من خلال سير عمل منظم، مستفيدًا من ميزات .NET للمؤسسات لحلول جاهزة للإنتاج.

**قدرات الأنظمة متعددة الوكلاء للمؤسسات التي ستبنيها:**
- 👥 **تعاون الوكلاء**: تنسيق الوكلاء مع أمان النوع والتحقق وقت التجميع
- 🔄 **تنسيق سير العمل**: تعريف سير عمل إعلاني باستخدام أنماط async في .NET
- 🎭 **تخصص الدور**: شخصيات وقوى الوكلاء ذات النوع القوي ومجالات الخبرة
- 🏢 **تكامل المؤسسة**: أنماط جاهزة للإنتاج مع المراقبة ومعالجة الأخطاء

## ⚙️ المتطلبات والإعداد

**بيئة التطوير:**
- .NET SDK 9.0 أو أعلى
- Visual Studio 2022 أو VS Code مع إضافة C#
- اشتراك Azure (لوكلاء دائمين)

**حزم NuGet المطلوبة:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## نموذج الكود

الكود الكامل للعمل لهذا الدرس متاح في ملف C# المرفق: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

لتشغيل النموذج:

```bash
# اجعل الملف قابلاً للتنفيذ (لينكس/ماك أو إس)
chmod +x 08-dotnet-agent-framework.cs

# تشغيل العينة
./08-dotnet-agent-framework.cs
```

أو باستخدام واجهة سطر أوامر .NET:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## ما الذي يوضحه هذا النموذج

يخلق هذا النظام متعدد الوكلاء خدمة توصيات سفر للفنادق مع وكيلين متخصصين:

1. **وكيل الاستقبال (FrontDesk)**: وكيل سفر يقدم توصيات للأنشطة والمواقع
2. **وكيل الكونسييرج (Concierge)**: يراجع التوصيات لضمان تجارب أصيلة وغير سياحية

يعمل الوكلاء معًا في سير عمل حيث:
- يتلقى وكيل الاستقبال الطلب السفر الأولي
- يراجع وكيل الكونسييرج التوصية ويصقلها
- يبث سير العمل الردود في الوقت الفعلي

## المفاهيم الرئيسية

### تنسيق الوكلاء
يوضح النموذج تنسيق الوكلاء مع أمان النوع باستخدام إطار عمل Microsoft Agent مع التحقق وقت التجميع.

### تنسيق سير العمل
يستخدم تعريف سير عمل إعلاني مع أنماط async في .NET لربط عدة وكلاء في خط أنابيب.

### بث الردود
ينفذ بث الوقت الحقيقي لردود الوكلاء باستخدام enumerable غير متزامنة وبنية مدفوعة بالأحداث.

### تكامل المؤسسة
يعرض أنماط جاهزة للإنتاج بما في ذلك:
- تهيئة متغيرات البيئة
- إدارة الاعتمادات الآمنة
- معالجة الأخطاء
- معالجة الأحداث غير المتزامنة

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->