---
name: jupyter-notebook
description: استخدمه عندما يطلب المستخدم إنشاء أو تهيئة أو تعديل دفاتر Jupyter (`.ipynb`)
  للتجارب أو الاستكشافات أو الدروس التعليمية؛ فضّل القوالب المضمّنة وقم بتشغيل سكربت
  المساعدة `new_notebook.py` لتوليد دفتر بدءٍ نظيف
---
# مهارة Jupyter Notebook

أنشئ دفاتر Jupyter نظيفة وقابلة للتكرار لوضعين أساسيين:

- التجارب والتحليل الاستكشافي
- الدروس والشروحات التعليمية

فضل استخدام القوالب المضمنة والبرنامج النصي المساعد للحصول على هيكل متسق وتقليل أخطاء JSON.

## متى تُستخدم
- أنشئ دفترًا جديدًا `.ipynb` من الصفر.
- حوّل ملاحظات أولية أو سكربتات إلى دفتر منظم.
- أعد هيكلة دفتر موجود ليصبح أكثر قابلية للتكرار وسهولة التصفح.
- بِناء تجارب أو دورات سيتم قراءتها أو إعادة تشغيلها من قبل أشخاص آخرين.

## شجرة القرار
- إذا كان الطلب استكشافيًا أو تحليليًا أو قائمًا على فرضية، اختر `experiment`.
- إذا كان الطلب تعليميًا أو خطوة بخطوة أو مخصصًا لجمهور معين، اختر `tutorial`.
- عند تحرير دفتر قائم، اعتبر ذلك إعادة هيكلة: حافظ على الهدف وحسّن البنية.

## مسار المهارة (يُضبط مرة واحدة)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

يتم تثبيت المهارات على مستوى المستخدم تحت `$CODEX_HOME/skills` (الافتراضي: `~/.codex/skills`).

## سير العمل
1. ثبت النية.
Identify the notebook kind: `experiment` or `tutorial`.
سجّل الهدف والجمهور وما الذي يبدو عليه "الانتهاء".

2. Scaffold from the template.
Use the helper script to avoid hand-authoring raw notebook JSON.

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind experiment \
  --title "Compare prompt variants" \
  --out output/jupyter-notebook/compare-prompt-variants.ipynb
```

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind tutorial \
  --title "Intro to embeddings" \
  --out output/jupyter-notebook/intro-to-embeddings.ipynb
```

3. املأ الدفتر بخطوات صغيرة قابلة للتشغيل.
حافظ على تركيز كل خلية كود على خطوة واحدة.
أضف خلايا Markdown قصيرة تشرح الهدف والنتيجة المتوقعة.
تجنب المخرجات الكبيرة والمزعجة عندما يكفي ملخص قصير.

4. طبق النمط المناسب.
بالنسبة للتجارب، اتبع `references/experiment-patterns.md`.
بالنسبة للدروس، اتبع `references/tutorial-patterns.md`.

5. حرّر بأمان عند العمل على دفاتر موجودة.
حافظ على بنية الدفتر؛ تجنّب إعادة ترتيب الخلايا إلا إذا حسّنت السرد من الأعلى إلى الأسفل.
فضل التعديلات المستهدفة على إعادة الكتابة الكاملة.
إذا اضطررت لتحرير JSON الخام، راجع `references/notebook-structure.md` أولاً.

6. تحقق من النتيجة.
شغل الدفتر من الأعلى إلى الأسفل عندما تسمح البيئة بذلك.
إذا لم يكن التنفيذ ممكنًا، اذكر ذلك صراحة ووضّح كيفية التحقق محليًا.
استخدم قائمة التحقق النهائية في `references/quality-checklist.md`.

## القوالب والبرنامج النصي المساعد
- تُخزَّن القوالب في `assets/experiment-template.ipynb` و `assets/tutorial-template.ipynb`.
- يقوم البرنامج النصي المساعد بتحميل قالب، وتحديث خلية العنوان، وكتابة دفتر ملاحظات.

مسار البرنامج النصي:
- `$JUPYTER_NOTEBOOK_CLI` (المثبت افتراضيًا: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## اتفاقيات الملفات المؤقتة والمخرجات
- استخدم `tmp/jupyter-notebook/` للملفات الوسيطة؛ احذفها عند الانتهاء.
- اكتب المنتج النهائي تحت `output/jupyter-notebook/` عند العمل في هذا المستودع.
- استخدم أسماء ملفات ثابتة ووصفية (على سبيل المثال، `ablation-temperature.ipynb`).

## التبعيات (ثبتها فقط عند الحاجة)
فضل استخدام `uv` لإدارة التبعيات.

حزم Python الاختيارية لتشغيل الدفتر محليًا:

```bash
uv pip install jupyterlab ipykernel
```

يستخدم البرنامج النصي المضمّن لبناء القالب مكتبة Python القياسية فقط ولا يتطلب تبعيات إضافية.

## البيئة
لا توجد متغيرات بيئة مطلوبة.

## خريطة المراجع
- `references/experiment-patterns.md`: بنية التجربة والقواعد الإرشادية.
- `references/tutorial-patterns.md`: بنية الدرس وتدفق التدريس.
- `references/notebook-structure.md`: شكل JSON لدفتر الملاحظات وقواعد التحرير الآمن.
- `references/quality-checklist.md`: قائمة التحقق النهائية.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
إخلاء المسؤولية:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية Co-op Translator (https://github.com/Azure/co-op-translator). بينما نسعى إلى الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المرجعي المعتمد. للمعلومات الحرجة أو المهمة، يُنصح بالاستعانة بترجمة بشرية ومحترفة. نحن غير مسؤولين عن أي سوء فهم أو تأويل ينشأ عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->