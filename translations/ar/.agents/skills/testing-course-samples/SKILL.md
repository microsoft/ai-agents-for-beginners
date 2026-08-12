---
name: testing-course-samples
---
# اختبار عينات الدورة

تحقق من أن دفاتر الدروس وعينات الشيفرة تعمل ضد إعداد Microsoft Foundry / Azure OpenAI مباشر.
يشتمل المستودع على مشغل في
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) الذي
ينفذ كل دفتر ملاحظات بايثون بدون واجهة ويطبع مصفوفة تمر/فشل.

## متى تستخدم
- "تحقق من صحة كل دفاتر الملاحظات / العينات مقابل اشتراك Azure الخاص بي."
- "اختبار سريع للدورة بعد تحديث الحزم أو تغيير النماذج."
- "أي الدروس لا تزال تمر / تفشل مباشرة؟"

لا تستخدم هذا لاختبار AI Smoke Test GitHub Action (الذي يتحقق من العملاء *النشرين*
المستضافين — راجع [`tests/README.md`](../../../tests/README.md)). تقوم هذه المهارة
بتشغيل دفاتر الملاحظات محليًا.

## المتطلبات الأساسية (افحص أولاً)
1. **بايثون 3.12+** مع تبعيات الدورة: `python -m pip install -r requirements.txt`
   بالإضافة إلى المشغل: `python -m pip install nbconvert ipykernel`.
2. **`.env` في جذر المستودع** (انسخ من [`.env.example`](../../../../../.env.example)) مع على الأقل:
   - `AZURE_AI_PROJECT_ENDPOINT` — نقطة نهاية مشروع Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — نشر غير مهجور (مثل `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) و `AZURE_OPENAI_DEPLOYMENT`
     للدروس التي تستدعي Azure OpenAI مباشرة (الدرس 06، 02-azure-openai، 14 التسليم/الحلقة البشرية).
3. إتمام **`تسجيل الدخول az`** — تقوم العينات بالمصادقة باستخدام `AzureCliCredential` (Entra ID، بدون مفتاح).
4. تحقق من وجود نشر النموذج:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## تشغيل التحقق
```powershell
# كل دفاتر بايثون (يتجاوز .NET، .venv، site-packages، الترجمات، موارد المهارات)
pwsh scripts/validate-notebooks.ps1

# درس واحد، مع مهلة أطول لكل خلية
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# فقط عرض ما سيتم تشغيله (دون تنفيذ)
pwsh scripts/validate-notebooks.ps1 -List

# مترجم صريح (إذا لم يكن `python` في PATH، مثلًا اسم مستعار لمتجر ويندوز)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
تقوم السكربت بكتابة نسخ منفذة، وسجلات لكل دفتر ملاحظات، و`results.json` إلى
`$env:TEMP\aiab-nbval` وتخرج بعدد حالات الفشل.

يتم إعادة محاولة الإخفاقات المؤقتة (حدود سرعة HTTP 429 لاشتراك مشترك، تعطل
عرضي لـ `AzureCliCredential`، أو انتهاء المهلة) تلقائيًا
(`-Retries`، الافتراضي 2، مع تأخير الإعادة `-RetryDelaySeconds`، الافتراضي 20). إذا كان
نشر النموذج يعاني من 429 بشكل منتظم، تحقق من حصة TPM العالمية للاشتراك
(`az cognitiveservices usage list -l <region>`) — زيادة سعة نشر واحد
لا تساعد عندما يتم استنفاد حصة *الاشتراك*.

## تفسير النتائج
- `PASS` — تم تشغيل دفتر الملاحظات كاملاً بدون خطأ في أي خلية.
- `FAIL` — يتم عرض أول سطر `*Error` / `*Exception`؛ افتح سطر السجل المطابق
  `log_*.txt` في مجلد المخرجات للتمشيط الكامل.
- فشل دفتر ملاحظات واحد مقيد بـ `-Timeout` (لكل خلية)، لذا تظهر خلايا التدخل البشري المتوقفة
  كـ`StdinNotImplementedError` بدلاً من التوقف.

## دروس تحتاج إلى موارد إضافية (من المتوقع أن تفشل بدونها)
| الدرس | متطلب إضافي |
|--------|-------------------|
| 05 Agentic RAG | بحث Azure AI (`AZURE_SEARCH_SERVICE_ENDPOINT`، المفتاح) — يحتوي على مسار احتياطي في الذاكرة |
| 11 MCP / GitHub | خادم GitHub MCP + PAT |
| 13 memory (cognee) | `cognee` مهيأ مع مزود نموذج |
| 15 استخدام المتصفح | متصفحات Playwright مثبتة (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 وكيل محلي | بيئة تنفيذ Foundry المحلية + نموذج Qwen محمل (على الجهاز، بدون سحابة) |
| دفاتر `*-dotnet-*` | نواة .NET Interactive (مستبعدة افتراضيًا؛ استخدم `-IncludeDotnet`) |

## التبليغ
لخّص كجدول PASS/FAIL مجمع حسب الدرس. افصل بين التراجع الحقيقي
(أخطاء الشيفرة / التكوين التي يجب إصلاحها) وفجوات البيئة (فقدان البحث / Foundry المحلية / PAT)،
واستشهد بسجلات `log_*.txt` للفشل الحقيقي.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->