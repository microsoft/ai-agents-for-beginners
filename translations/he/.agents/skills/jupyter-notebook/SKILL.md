---
name: jupyter-notebook
---
# מיומנות Jupyter Notebook

צור מחברות Jupyter נקיות וניתנות לשחזור עבור שני מצבים עיקריים:

- ניסויים וניתוח חקרני
- מדריכים והדרכות למטרות הוראה

העדף את תבניות החבילה ואת סקריפט העזר למבנה עקבי ופחות שגיאות JSON.

## מתי להשתמש
- צור מחברת `.ipynb` חדשה מאפס.
- המר הערות גסות או סקריפטים למחברת מובנית.
- ארגן מחדש מחברת קיימת כדי להפוך אותה לניתנת לשחזור וקלה לסקירה.
- בנה ניסויים או מדריכים שיקראו או ירוצו שוב על ידי אנשים אחרים.

## עץ החלטות
- אם הבקשה חקרנית, אנליטית, או מונחית־השערה, בחר ב־`experiment`.
- אם הבקשה הוראתית, צעד־אחר־צעד, או ממוקדת קהל, בחר ב־`tutorial`.
- אם אתה עורך מחברת קיימת, התייחס לכך כאל רה־ארגון: שמור על הכוונה ושפר את המבנה.

## מסלול המיומנות (הגדר פעם אחת)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

מיומנויות בהיקף משתמש מותקנות תחת `$CODEX_HOME/skills` (ברירת מחדל: `~/.codex/skills`).

## זרימת עבודה
1. קבע את הכוונה.
זהה את סוג המחברת: `experiment` או `tutorial`.
תעד את המטרה, הקהל, ומה נחשב 'גמור'.

2. השתמש בתבנית כשלד.
השתמש בסקריפט העזר כדי להימנע מכתיבה ידנית של JSON הגולמי של המחברת.

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

3. מלא את המחברת בצעדים קטנים שניתנים להרצה.
הקפד שכל תא קוד יתמקד בצעד אחד.
הוסף תאי Markdown קצרים שמסבירים את המטרה והתוצאה המצופה.
הימנע מתוצרים גדולים ורועשים כאשר סיכום קצר מספיק.

4. השתמש בתבנית הנכונה.
לניסויים, פעל לפי `references/experiment-patterns.md`.
למדריכים, פעל לפי `references/tutorial-patterns.md`.

5. ערוך בזהירות בעת עבודה עם מחברות קיימות.
שמור על מבנה המחברת; הימנע מהזזת תאים אלא אם כן זה משפר את הסיפור מלמעלה למטה.
העדף עריכות ממוקדות על פני כתיבה מחדש מלאה.
אם עליך לערוך JSON גולמי, סקור קודם את `references/notebook-structure.md`.

6. אמת את התוצאה.
הרץ את המחברת מלמעלה למטה כאשר הסביבה מאפשרת.
אם הריצה אינה אפשרית, ציין זאת במפורש והסבר כיצד לאמת מקומית.
השתמש ברשימת הבדיקה של המעבר הסופי ב־`references/quality-checklist.md`.

## תבניות וסקריפט העזר
- התבניות נמצאות ב־`assets/experiment-template.ipynb` וב־`assets/tutorial-template.ipynb`.
- סקריפט העזר טוען תבנית, מעדכן את תא הכותרת, וכותב מחברת.

נתיב הסקריפט:
- `$JUPYTER_NOTEBOOK_CLI` (המותקן כברירת מחדל: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## קונבנציות קבצים זמניים ופלט
- השתמש ב־`tmp/jupyter-notebook/` עבור קבצים ביניים; מחק כאשר סיימת.
- כתוב את התוצרים הסופיים תחת `output/jupyter-notebook/` בעת עבודה במאגר זה.
- השתמש בשמות קבצים יציבים ותיאוריים (למשל, `ablation-temperature.ipynb`).

## תלותיות (התקן רק במידת הצורך)
העדף את `uv` לניהול תלותיות.

חבילות Python אופציונליות להפעלת מחברות באופן מקומי:

```bash
uv pip install jupyterlab ipykernel
```

סקריפט השלד החבוי משתמש רק בספריית הסטנדרט של Python ואינו דורש תלויות נוספות.

## סביבה
אין משתני סביבה חובה.

## מפת התייחסות
- `references/experiment-patterns.md`: מבנה ניסוי והיוריסטיקות.
- `references/tutorial-patterns.md`: מבנה מדריך וזרימת הוראה.
- `references/notebook-structure.md`: צורת JSON של המחברת וכללי עריכה בטוחה.
- `references/quality-checklist.md`: רשימת בדיקה לאימות סופי.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
הבהרת אחריות:
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). אמנם אנו שואפים לדייק, אך יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו המקורית כמקור הסמכות. עבור מידע קריטי מומלץ תרגום מקצועי שנעשה בידי מתרגם אנושי. איננו נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->