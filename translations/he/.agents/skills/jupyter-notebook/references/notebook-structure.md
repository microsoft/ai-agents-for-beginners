# מבנה המחברת

מחברות Jupyter הן מסמכי JSON בעלי מבנה כללי כזה:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (רשימה של תאי markdown ותאי קוד)

When editing `.ipynb` files programmatically:

- שמרו על `nbformat` ו-`nbformat_minor` מהתבנית.
- השאירו את `cells` כרשימה מסודרת; אל תחליפו את הסדר אלא אם בכוונה.
- עבור תאי קוד, קבעו את `execution_count` ל-`null` כאשר אינו ידוע.
- עבור תאי קוד, קבעו את `outputs` לרשימה ריקה בעת יצירת השלד.
- עבור תאי markdown, שמרו על `cell_type="markdown"` ו-`metadata={}`.

העדיפו שימוש בתבניות המצורפות או ב-`new_notebook.py` (לדוגמה, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) במקום כתיבת JSON הגולמי של המחברת באופן ידני.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
הצהרת אחריות:
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית Co-op Translator (https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, שימו לב כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו כמקור הסמכות. עבור מידע קריטי מומלץ תרגום מקצועי על ידי מתרגם אנושי. איננו אחראים לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->