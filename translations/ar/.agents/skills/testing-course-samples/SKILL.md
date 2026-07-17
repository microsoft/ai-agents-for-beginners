---
name: testing-course-samples
---
# اختبار عينات الدورة التدريبية

تحقق من أن دفاتر الدروس وعيّنات الأكواد تعمل على إعداد Microsoft Foundry / Azure OpenAI المباشر.
يضم المستودع مشغّلًا في
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) الذي
ينفّذ كل دفتر Python بدون واجهة ويطبع مصفوفة النتيجة PASS/FAIL.

## متى تستخدم
- "تحقق من جميع دفاتر / عينات الدورة مقابل اشتراك Azure الخاص بي."
- "اختبار سريع للدورة بعد ترقية الحزم أو تغيير النماذج."
- "أي الدروس لا تزال تمر / تفشل على الواقع الحي؟"

لا تستخدم هذا لاختبار دخان AI GitHub Action (الذي يتحقق من 
الوكلاء المستضافين *المنتشرين* — راجع [`tests/README.md`](../../../tests/README.md)). هذه المهارة
تشغّل الدفاتر محليًا.

## المتطلبات الأساسية (تحقق أولاً)
1. **Python 3.12+** مع تبعيات الدورة: `python -m pip install -r requirements.txt`
   بالإضافة إلى المنفذ: `python -m pip install nbconvert ipykernel`.
2. **`.env` في جذر المستودع** (انسخ من [`.env.example`](../../../../../.env.example)) مع على الأقل:
   - `AZURE_AI_PROJECT_ENDPOINT` — نقطة النهاية لمشروع Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — نشر غير مهجور (مثل `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) و `AZURE_OPENAI_DEPLOYMENT`
     للدروس التي تستدعي Azure OpenAI مباشرة (الدرس 06، 02-azure-openai، 14 handoff/human-loop).
3. **إتمام `az login`** — العينات تثبت الهوية باستخدام `AzureCliCredential` (Entra ID، بدون مفتاح).
4. تحقق من وجود نشر النموذج:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## تشغيل التحقق
```powershell
# جميع دفاتر بايثون (يتخطى .NET و .venv و site-packages والترجمات وأصول المهارات)
pwsh scripts/validate-notebooks.ps1

# درس واحد، مع مهلة أطول لكل خلية
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# فقط سرد ما سيتم تشغيله (بدون تنفيذ)
pwsh scripts/validate-notebooks.ps1 -List

# مفسر صريح (إذا لم يكن `python` في PATH، مثل كنية متجر ويندوز)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
تكتب السكريبت نسخًا منفذة، سجلات لكل دفتر، و`results.json` في
`$env:TEMP\aiab-nbval` وتخرج بعدد الإخفاقات.

## تفسير النتائج
- `PASS` — نفذ الدفتر من البداية للنهاية بدون أخطاء في الخلايا.
- `FAIL` — يظهر أول خط `*Error` / `*Exception`؛ افتح
  ملف `log_*.txt` المطابق في مجلد الإخراج لرؤية تتبع الأخطاء الكامل.
- فشل دفتر واحد محصور بـ `-Timeout` (لكل خلية)، لذا تظهر خلية متوقفة بسبب تدخل بشري
  كـ `StdinNotImplementedError` بدلًا من التوقف.

## الدروس التي تحتاج إلى موارد إضافية (من المتوقع أن تفشل بدونها)
| الدرس | متطلب إضافي |
|--------|-------------------|
| 05 عامل RAG | بحث Azure AI (`AZURE_SEARCH_SERVICE_ENDPOINT`، مفتاح) — يحتوي على مسار بديل في الذاكرة |
| 11 MCP / GitHub | خادم MCP لـ GitHub + PAT |
| 13 الذاكرة (cognee) | `cognee` مُكوّن مع مزود نموذج |
| 15 استخدام المتصفح | متصفحات Playwright مثبتة (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 وكيل محلي | بيئة تشغيل Foundry Local + نموذج Qwen محمل (على الجهاز، بدون سحابة) |
| دفاتر `*-dotnet-*` | نواة .NET Interactive (مستثناة افتراضيًا؛ استخدم `-IncludeDotnet`) |

## التقرير
لخّص في جدول PASS/FAIL مجمّع حسب الدرس. فصل التراجعات الحقيقية 
(أخطاء البرمجة/التكوين التي يجب إصلاحها) عن فجوات البيئة (البحث المفقود / Foundry Local / PAT)،
واذكر ملف `log_*.txt` الذي يفشل لكل فشل حقيقي.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->