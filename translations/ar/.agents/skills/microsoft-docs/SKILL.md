---
name: microsoft-docs
---
# مستندات مايكروسوفت

مهارة البحث لنظام تكنولوجيا مايكروسوفت. تغطي learn.microsoft.com والمستندات التي تقع خارجها (VS Code، GitHub، Aspire، مستودعات Agent Framework).

---

## الافتراضي: Microsoft Learn MCP

استخدم هذه الأدوات لـ **كل شيء على learn.microsoft.com** — أزور، .NET، M365، Power Platform، Agent Framework، Semantic Kernel، ويندوز، وأكثر. هذه هي الأداة الأساسية لمعظم استعلامات مستندات مايكروسوفت.

| الأداة | الغرض |
|------|---------|
| `microsoft_docs_search` | البحث في learn.microsoft.com — المفاهيم، الأدلة، البرامج التعليمية، التكوين |
| `microsoft_code_sample_search` | إيجاد مقتطفات كود تعمل من مستندات Learn. مرر `language` (`python`، `csharp`، إلخ) لأفضل النتائج |
| `microsoft_docs_fetch` | الحصول على محتوى الصفحة كاملة من عنوان URL محدد (عندما لا تكفي مقتطفات البحث) |

استخدم `microsoft_docs_fetch` بعد البحث عندما تحتاج إلى برامج تعليمية كاملة، كل خيارات التكوين، أو عندما تُقتطع مقتطفات البحث.

---

## استثناءات: متى تستخدم أدوات أخرى

الفئات التالية تقع **خارج** learn.microsoft.com. استخدم الأداة المحددة بدلاً من ذلك.

### Aspire — استخدم Aspire MCP Server (المفضل) أو Context7

مستندات Aspire تقع على **aspire.dev**، ليست في Learn. أفضل أداة تعتمد على إصدار Aspire CLI الخاص بك:

**CLI 13.2+** (مستحسن) — يتضمن خادم Aspire MCP أدوات بحث مستندات مضمنة:

| أداة MCP | الوصف |
|----------|-------------|
| `list_docs` | يعرض كل المستندات المتاحة من aspire.dev |
| `search_docs` | بحث لغوي موزون عبر محتوى aspire.dev |
| `get_doc` | يستعيد مستند معين بواسطة slug |

هذه الأدوات تُشحن مع Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). للتحديث: `aspire update --self --channel daily`.

**CLI 13.1** — يوفر خادم MCP بحث تكامل (`list_integrations`، `get_integration_docs`) لكن **لا** يوفر بحث مستندات. استخدم Context7 بدلاً من ذلك:

| معرف المكتبة | يُستخدم لـ |
|---|---|
| `/microsoft/aspire.dev` | أساسي — أدلة، تكاملات، مرجع CLI، النشر |
| `/microsoft/aspire` | مصادر وقت التشغيل — تفاصيل API، تفاصيل التنفيذ |
| `/communitytoolkit/aspire` | تكاملات المجتمع — Go، Java، Node.js، Ollama |

### VS Code — استخدم Context7

مستندات VS Code تقع على **code.visualstudio.com**، ليست في Learn.

| معرف المكتبة | يُستخدم لـ |
|---|---|
| `/websites/code_visualstudio` | مستندات المستخدم — الإعدادات، الميزات، التصحيح، التطوير عن بُعد |
| `/websites/code_visualstudio_api` | Extension API — webviews، TreeViews، الأوامر، نقاط المساهمة |

### GitHub — استخدم Context7

مستندات GitHub تقع على **docs.github.com** و **cli.github.com**.

| معرف المكتبة | يُستخدم لـ |
|---|---|
| `/websites/github_en` | Actions، API، المستودعات، الأمان، الإدارة، Copilot |
| `/websites/cli_github` | أوامر وعلامات GitHub CLI (`gh`) |

### Agent Framework — استخدم Learn MCP + Context7

برامج Agent Framework التعليمية على learn.microsoft.com (استخدم `microsoft_docs_search`)، لكن **مستودع GitHub** يحتوي على تفاصيل على مستوى API غالبًا ما تتفوق على المستندات المنشورة — خصوصًا مرجع DevUI REST API، خيارات CLI، وتكامل .NET.

| معرف المكتبة | يُستخدم لـ |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | البرامج التعليمية — أدلة DevUI، التتبع، تنظيم سير العمل |
| `/microsoft/agent-framework` | تفاصيل API — نقاط نهاية DevUI REST، علامات CLI، المصادقة، .NET `AddDevUI`/`MapDevUI` |

**نصيحة DevUI:** استعلم أولًا من مصدر موقع Learn لأدلة كيفية العمل، ثم من مصدر المستودع لتفاصيل مستوى API (مخططات النقاط النهائية، تكوين البروكسي، رموز المصادقة).

---

## إعداد Context7

لأي استعلام Context7، حل معرف المكتبة أولاً (مرة واحدة لكل جلسة):

1. استدعِ `mcp_context7_resolve-library-id` مع اسم التكنولوجيا
2. استدعِ `mcp_context7_query-docs` مع معرف المكتبة المُعاد والاستعلام المحدد

---

## كتابة استعلامات فعالة

كن محددًا — ضمن النسخة، الهدف، واللغة:

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

أضف السياق:
- **الإصدار** عندما يكون ذا صلة (`.NET 8`، `Aspire 13`، `VS Code 1.96`)
- **هدف المهمة** (`quickstart`، `tutorial`، `overview`، `limits`، `API reference`)
- **اللغة** لوثائق متعددة اللغات (`Python`، `TypeScript`، `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->