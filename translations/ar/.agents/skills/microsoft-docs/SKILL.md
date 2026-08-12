---
name: microsoft-docs
description: استعلام عن الوثائق الرسمية لشركة Microsoft للعثور على المفاهيم والدروس
  والأمثلة البرمجية عبر Azure و .NET و Agent Framework و Aspire و VS Code و GitHub
  والمزيد. يستخدم Microsoft Learn MCP كالإعداد الافتراضي، مع Context7 و Aspire MCP
  للمحتوى المتواجد خارج learn.microsoft.com.
---
# Microsoft Docs

مهارة بحث لنظام تقنيات Microsoft. تغطي learn.microsoft.com والتوثيق الذي يعيش خارجه (VS Code، GitHub، Aspire، مستودعات Agent Framework).

---

## الافتراضي: Microsoft Learn MCP

Use these tools for **كل شيء على learn.microsoft.com** — Azure، .NET، M365، Power Platform، Agent Framework، Semantic Kernel، Windows، والمزيد. هذه هي الأداة الأساسية لمعظم استعلامات توثيق Microsoft.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | ابحث في learn.microsoft.com — المفاهيم، الأدلة، الدروس التعليمية، التكوين |
| `microsoft_code_sample_search` | اعثر على مقتطفات كود عاملة من مستندات Learn. مرّر `language` (`python`, `csharp`, إلخ) للحصول على أفضل النتائج |
| `microsoft_docs_fetch` | احصل على محتوى الصفحة الكامل من عنوان URL محدد (عندما لا تكفي مقتطفات البحث) |

استخدم `microsoft_docs_fetch` بعد البحث عندما تحتاج إلى أدلة كاملة، كل خيارات التكوين، أو عندما يتم اقتطاع مقتطفات البحث.

---

## استثناءات: متى تستخدم أدوات أخرى

الفئات التالية موجودة **خارج** learn.microsoft.com. استخدم الأداة المحددة بدلاً من ذلك.

### .NET Aspire — استخدم Aspire MCP Server (مُفضّل) أو Context7

توثيق Aspire موجود على **aspire.dev**، وليس على Learn. أفضل أداة تعتمد على إصدار Aspire CLI لديك:

**CLI 13.2+** (موصى به) — يتضمن خادم Aspire MCP أدوات بحث توثيق مدمجة:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | يعرض كل التوثيق المتاح من aspire.dev |
| `search_docs` | بحث لفظي موزون عبر محتوى aspire.dev |
| `get_doc` | يسترجع مستندًا محددًا بواسطة slug |

تتضمن هذه في Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). للتحديث: `aspire update --self --channel daily`. مراجع: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — يوفر خادم MCP البحث عن تكاملات (`list_integrations`, `get_integration_docs`) لكنه **لا** يوفر بحثًا في التوثيق. ارجع إلى Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | أساسي — الأدلة، التكاملات، مرجع CLI، النشر |
| `/dotnet/aspire` | مصدر وقت التشغيل — تفاصيل داخلية للـ API، تفاصيل التنفيذ |
| `/communitytoolkit/aspire` | تكاملات المجتمع — Go، Java، Node.js، Ollama |

### VS Code — استخدم Context7

توثيق VS Code موجود على **code.visualstudio.com**، وليس على Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | توثيق المستخدم — الإعدادات، الميزات، التصحيح، التطوير عن بُعد |
| `/websites/code_visualstudio_api` | Extension API — webviews، TreeViews، الأوامر، نقاط المساهمة |

### GitHub — استخدم Context7

توثيق GitHub موجود على **docs.github.com** و **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions، API، المستودعات، الأمان، الإدارة، Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) — الأوامر والخيارات |

### Agent Framework — استخدم Learn MCP + Context7

دروس Agent Framework موجودة على learn.microsoft.com (استخدم `microsoft_docs_search`)، لكن **مستودع GitHub** يحتوي على تفاصيل على مستوى الـ API غالبًا ما تكون متقدمة على المستندات المنشورة — خصوصًا مرجع DevUI REST API، خيارات CLI، والتكامل مع .NET.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | دروس — أدلة DevUI، التتبع، تنظيم سير العمل |
| `/microsoft/agent-framework` | تفاصيل API — نقاط نهاية DevUI REST، خيارات CLI، المصادقة، .NET `AddDevUI`/`MapDevUI` |

**تلميح DevUI:** استعلم من مصدر موقع Learn للأدلة العملية، ثم من مصدر المستودع لتفاصيل مستوى الـ API (مخططات نقاط النهاية، تكوين الوكيل، رموز المصادقة).

---

## إعداد Context7

بالنسبة لأي استعلام Context7، قم بحل معرّف المكتبة أولاً (مرة واحدة لكل جلسة):

1. استدعي `mcp_context7_resolve-library-id` مع اسم التقنية
2. استدعي `mcp_context7_query-docs` مع معرّف المكتبة المرجع وسؤال محدد

---

## كتابة استعلامات فعّالة

كن محددًا — تضمّن الإصدار، النية، واللغة:

```
# ❌ Too broad
"Azure Functions"
"agent framework"

# ✅ Specific
"Azure Functions Python v2 programming model"
"Cosmos DB partition key design best practices"
"GitHub Actions workflow_dispatch inputs matrix strategy"
"Aspire AddUvicornApp Python FastAPI integration"
"DevUI serve agents tracing OpenTelemetry directory discovery"
"Agent Framework workflow conditional edges branching handoff"
```

ضمّن السياق:
- **الإصدار** عندما يكون ذا صلة (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **هدف المهمة** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **اللغة** للوثائق متعددة اللغات (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
إخلاء مسؤولية:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية Co‑op Translator (https://github.com/Azure/co-op-translator). بينما نسعى إلى الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار الوثيقة الأصلية باللغة الأصلية هي المصدر المعتمد. للمعلومات الحساسة أو الحرجة، يوصى بالاستعانة بترجمة بشرية محترفة. نحن لا نتحمل أي مسؤولية عن سوء الفهم أو التفسيرات الخاطئة الناتجة عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->