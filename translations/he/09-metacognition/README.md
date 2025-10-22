<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-29T17:33:24+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "he"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.he.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(לחצו על התמונה למעלה לצפייה בסרטון של השיעור הזה)_
# מטא-קוגניציה בסוכני AI

## הקדמה

ברוכים הבאים לשיעור על מטא-קוגניציה בסוכני AI! פרק זה מיועד למתחילים הסקרנים כיצד סוכני AI יכולים לחשוב על תהליכי החשיבה שלהם עצמם. בסיום השיעור, תבינו מושגים מרכזיים ותהיו מצוידים בדוגמאות מעשיות ליישום מטא-קוגניציה בעיצוב סוכני AI.

## מטרות למידה

לאחר השלמת השיעור, תוכלו:

1. להבין את ההשלכות של לולאות חשיבה בהגדרות סוכנים.
2. להשתמש בטכניקות תכנון והערכה כדי לעזור לסוכנים לתקן את עצמם.
3. ליצור סוכנים משלכם המסוגלים לשנות קוד כדי לבצע משימות.

## הקדמה למטא-קוגניציה

מטא-קוגניציה מתייחסת לתהליכים קוגניטיביים ברמה גבוהה הכוללים חשיבה על החשיבה של עצמך. עבור סוכני AI, המשמעות היא היכולת להעריך ולהתאים את פעולותיהם בהתבסס על מודעות עצמית וניסיון עבר. מטא-קוגניציה, או "חשיבה על חשיבה", היא מושג חשוב בפיתוח מערכות AI סוכניות. היא כוללת מערכות AI שמודעות לתהליכים הפנימיים שלהן ויכולות לנטר, לווסת ולהתאים את התנהגותן בהתאם. בדיוק כמו שאנחנו עושים כשאנחנו קוראים את הסיטואציה או מתמודדים עם בעיה. מודעות עצמית זו יכולה לעזור למערכות AI לקבל החלטות טובות יותר, לזהות טעויות ולשפר את ביצועיהן לאורך זמן - שוב, בהקשר למבחן טיורינג ולדיון האם AI עומד להשתלט.

בהקשר של מערכות AI סוכניות, מטא-קוגניציה יכולה לעזור להתמודד עם מספר אתגרים, כגון:
- שקיפות: הבטחת יכולת של מערכות AI להסביר את ההיגיון וההחלטות שלהן.
- חשיבה: שיפור היכולת של מערכות AI לסנתז מידע ולקבל החלטות מושכלות.
- הסתגלות: מתן אפשרות למערכות AI להתאים את עצמן לסביבות חדשות ולתנאים משתנים.
- תפיסה: שיפור הדיוק של מערכות AI בזיהוי ופרשנות נתונים מהסביבה שלהן.

### מהי מטא-קוגניציה?

מטא-קוגניציה, או "חשיבה על חשיבה", היא תהליך קוגניטיבי ברמה גבוהה הכולל מודעות עצמית ורגולציה עצמית של תהליכים קוגניטיביים. בתחום ה-AI, מטא-קוגניציה מאפשרת לסוכנים להעריך ולהתאים את האסטרטגיות והפעולות שלהם, מה שמוביל לשיפור יכולות פתרון בעיות וקבלת החלטות. על ידי הבנת מטא-קוגניציה, תוכלו לעצב סוכני AI שהם לא רק חכמים יותר אלא גם מסתגלים ויעילים יותר. במטא-קוגניציה אמיתית, תראו את ה-AI מבצע חשיבה מפורשת על החשיבה שלו עצמו.

דוגמה: "נתתי עדיפות לטיסות זולות יותר כי... אולי אני מפספס טיסות ישירות, אז כדאי שאבדוק שוב."
מעקב אחר איך או למה הוא בחר מסלול מסוים.
- ציון שהוא עשה טעויות כי הסתמך יתר על המידה על העדפות משתמש מהפעם הקודמת, ולכן הוא משנה את אסטרטגיית קבלת ההחלטות שלו ולא רק את ההמלצה הסופית.
- אבחון דפוסים כמו, "בכל פעם שאני רואה שהמשתמש מזכיר 'יותר מדי צפוף', אני צריך לא רק להסיר אטרקציות מסוימות אלא גם לשקף שהשיטה שלי לבחירת 'אטרקציות מובילות' פגומה אם אני תמיד מדרג לפי פופולריות."

### חשיבות המטא-קוגניציה בסוכני AI

מטא-קוגניציה משחקת תפקיד קריטי בעיצוב סוכני AI ממספר סיבות:

![חשיבות המטא-קוגניציה](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.he.png)

- רפלקציה עצמית: סוכנים יכולים להעריך את הביצועים שלהם ולזהות תחומים לשיפור.
- הסתגלות: סוכנים יכולים לשנות את האסטרטגיות שלהם בהתבסס על ניסיון עבר וסביבות משתנות.
- תיקון טעויות: סוכנים יכולים לזהות ולתקן טעויות באופן עצמאי, מה שמוביל לתוצאות מדויקות יותר.
- ניהול משאבים: סוכנים יכולים לייעל את השימוש במשאבים, כמו זמן וכוח חישוב, על ידי תכנון והערכת פעולותיהם.

## רכיבי סוכן AI

לפני שנצלול לתהליכי מטא-קוגניציה, חשוב להבין את הרכיבים הבסיסיים של סוכן AI. סוכן AI מורכב בדרך כלל מ:

- פרסונה: האישיות והמאפיינים של הסוכן, שמגדירים כיצד הוא מתקשר עם משתמשים.
- כלים: היכולות והפונקציות שהסוכן יכול לבצע.
- מיומנויות: הידע והמומחיות שהסוכן מחזיק.

רכיבים אלו עובדים יחד כדי ליצור "יחידת מומחיות" שיכולה לבצע משימות ספציפיות.

**דוגמה**:
חשבו על סוכן נסיעות, שירות סוכנים שלא רק מתכנן את החופשה שלכם אלא גם מתאים את המסלול שלו בהתבסס על נתונים בזמן אמת וניסיון מסע לקוחות קודם.

### דוגמה: מטא-קוגניציה בשירות סוכן נסיעות

דמיינו שאתם מעצבים שירות סוכן נסיעות המופעל על ידי AI. סוכן זה, "Travel Agent", מסייע למשתמשים בתכנון החופשות שלהם. כדי לשלב מטא-קוגניציה, Travel Agent צריך להעריך ולהתאים את פעולותיו בהתבסס על מודעות עצמית וניסיון עבר. הנה איך מטא-קוגניציה יכולה לשחק תפקיד:

#### משימה נוכחית

המשימה הנוכחית היא לעזור למשתמש לתכנן טיול לפריז.

#### שלבים להשלמת המשימה

1. **איסוף העדפות משתמש**: שאלו את המשתמש על תאריכי הנסיעה, התקציב, תחומי העניין (למשל, מוזיאונים, אוכל, קניות) וכל דרישה ספציפית.
2. **אחזור מידע**: חפשו אפשרויות טיסה, מקומות לינה, אטרקציות ומסעדות שמתאימות להעדפות המשתמש.
3. **יצירת המלצות**: ספקו מסלול אישי עם פרטי טיסה, הזמנות מלון ופעילויות מוצעות.
4. **התאמה על בסיס משוב**: בקשו מהמשתמש משוב על ההמלצות ובצעו התאמות נחוצות.

#### משאבים נדרשים

- גישה למסדי נתונים של הזמנת טיסות ומלונות.
- מידע על אטרקציות ומסעדות בפריז.
- נתוני משוב משתמשים מאינטראקציות קודמות.

#### ניסיון ורפלקציה עצמית

Travel Agent משתמש במטא-קוגניציה כדי להעריך את ביצועיו וללמוד מניסיון עבר. לדוגמה:

1. **ניתוח משוב משתמשים**: Travel Agent סוקר משוב משתמשים כדי לקבוע אילו המלצות התקבלו היטב ואילו לא. הוא מתאים את ההצעות העתידיות שלו בהתאם.
2. **הסתגלות**: אם משתמש ציין בעבר חוסר חיבה למקומות צפופים, Travel Agent ימנע מלהמליץ על אתרי תיירות פופולריים בשעות שיא בעתיד.
3. **תיקון טעויות**: אם Travel Agent עשה טעות בהזמנה קודמת, כמו המלצה על מלון שהיה בתפוסה מלאה, הוא לומד לבדוק זמינות בצורה יסודית יותר לפני מתן המלצות.

#### דוגמה מעשית למפתחים

הנה דוגמה פשוטה לקוד של Travel Agent שמשלב מטא-קוגניציה:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Search for flights, hotels, and attractions based on preferences
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analyze feedback and adjust future recommendations
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### למה מטא-קוגניציה חשובה

- **רפלקציה עצמית**: סוכנים יכולים לנתח את הביצועים שלהם ולזהות תחומים לשיפור.
- **הסתגלות**: סוכנים יכולים לשנות אסטרטגיות בהתבסס על משוב ותנאים משתנים.
- **תיקון טעויות**: סוכנים יכולים לזהות ולתקן טעויות באופן עצמאי.
- **ניהול משאבים**: סוכנים יכולים לייעל את השימוש במשאבים, כמו זמן וכוח חישוב.

על ידי שילוב מטא-קוגניציה, Travel Agent יכול לספק המלצות נסיעה אישיות ומדויקות יותר, מה שמשפר את חוויית המשתמש הכוללת.

---

## 2. תכנון בסוכנים

תכנון הוא מרכיב קריטי בהתנהגות סוכני AI. הוא כולל תכנון השלבים הדרושים להשגת מטרה, תוך התחשבות במצב הנוכחי, משאבים ומכשולים אפשריים.

### מרכיבי תכנון

- **משימה נוכחית**: הגדרת המשימה בצורה ברורה.
- **שלבים להשלמת המשימה**: פירוק המשימה לשלבים ניתנים לניהול.
- **משאבים נדרשים**: זיהוי המשאבים הנחוצים.
- **ניסיון**: שימוש בניסיון עבר כדי ליידע את התכנון.

**דוגמה**:
הנה השלבים ש-Travel Agent צריך לבצע כדי לעזור למשתמש לתכנן את הטיול שלו בצורה יעילה:

### שלבים עבור Travel Agent

1. **איסוף העדפות משתמש**
   - שאלו את המשתמש על פרטים לגבי תאריכי הנסיעה, התקציב, תחומי העניין וכל דרישה ספציפית.
   - דוגמאות: "מתי אתם מתכננים לנסוע?" "מה טווח התקציב שלכם?" "אילו פעילויות אתם נהנים לעשות בחופשה?"

2. **אחזור מידע**
   - חפשו אפשרויות נסיעה רלוונטיות בהתבסס על העדפות המשתמש.
   - **טיסות**: חפשו טיסות זמינות במסגרת התקציב ותאריכי הנסיעה המועדפים של המשתמש.
   - **מקומות לינה**: מצאו מלונות או נכסים להשכרה שמתאימים להעדפות המשתמש מבחינת מיקום, מחיר ושירותים.
   - **אטרקציות ומסעדות**: זיהוי אטרקציות, פעילויות ואפשרויות אוכל פופולריות שמתאימות לתחומי העניין של המשתמש.

3. **יצירת המלצות**
   - רכזו את המידע שנאסף למסלול אישי.
   - ספקו פרטים כמו אפשרויות טיסה, הזמנות מלון ופעילויות מוצעות, תוך התאמת ההמלצות להעדפות המשתמש.

4. **הצגת המסלול למשתמש**
   - שתפו את המסלול המוצע עם המשתמש לצורך סקירה.
   - דוגמה: "הנה מסלול מוצע לטיול שלכם לפריז. הוא כולל פרטי טיסה, הזמנות מלון ורשימת פעילויות ומסעדות מומלצות. ספרו לי מה דעתכם!"

5. **איסוף משוב**
   - בקשו מהמשתמש משוב על המסלול המוצע.
   - דוגמאות: "האם אתם אוהבים את אפשרויות הטיסה?" "האם המלון מתאים לצרכים שלכם?" "האם יש פעילויות שתרצו להוסיף או להסיר?"

6. **התאמה על בסיס משוב**
   - התאימו את המסלול בהתבסס על משוב המשתמש.
   - בצעו שינויים נחוצים בהמלצות הטיסה, הלינה והפעילויות כדי להתאים טוב יותר להעדפות המשתמש.

7. **אישור סופי**
   - הציגו את המסלול המעודכן למשתמש לאישור סופי.
   - דוגמה: "ביצעתי את ההתאמות בהתבסס על המשוב שלכם. הנה המסלול המעודכן. האם הכל נראה לכם טוב?"

8. **הזמנה ואישור**
   - לאחר שהמשתמש מאשר את המסלול, המשיכו בהזמנת טיסות, מקומות לינה וכל פעילויות מתוכננות מראש.
   - שלחו פרטי אישור למשתמש.

9. **מתן תמיכה מתמשכת**
   - הישארו זמינים לסייע למשתמש עם כל שינוי או בקשה נוספת לפני ובמהלך הטיול.
   - דוגמה: "אם תצטרכו עזרה נוספת במהלך הטיול שלכם, אל תהססו לפנות אליי בכל עת!"

### אינטראקציה לדוגמה

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage within a booing request
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

## 3. מערכת תיקון RAG

ראשית, בואו נתחיל בהבנת ההבדל בין כלי RAG לטעינת הקשר מקדימה.

![RAG לעומת טעינת הקשר](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.he.png)

### יצירה מוגברת אחזור (RAG)

RAG משלב מערכת אחזור עם מודל יצירה. כאשר מתבצע שאילתה, מערכת האחזור שולפת מסמכים או נתונים רלוונטיים ממקור חיצוני, ומידע זה משמש להרחבת הקלט למודל היצירה. זה עוזר למודל ליצור תגובות מדויקות ורלוונטיות מבחינה הקשרית.

במערכת RAG, הסוכן שולף מידע רלוונטי ממאגר ידע ומשתמש בו כדי ליצור תגובות או פעולות מתאימות.

### גישת תיקון RAG

גישת תיקון RAG מתמקדת בשימוש בטכניקות RAG לתיקון טעויות ושיפור דיוק סוכני AI. זה כולל:

1. **טכניקת הנחיה**: שימוש בהנחיות ספציפיות כדי להנחות את הסוכן באחזור מידע רלוונטי.
2. **כלי**: יישום אלגוריתמים ומנגנונים שמאפשרים לסוכן להעריך את הרלוונטיות של המידע שנשלף וליצור תגובות מדויקות.
3. **הערכה**: הערכה מתמשכת של ביצועי הסוכן וביצוע התאמות לשיפור דיוקו ויעילותו.

#### דוגמה: תיקון RAG בסוכן חיפוש

חשבו על סוכן חיפוש ששולף מידע מהאינטרנט כדי לענות על שאילתות משתמשים. גישת תיקון RAG עשויה לכלול:

1. **טכניקת הנחיה**: ניסוח שאילתות חיפוש בהתבסס על קלט המשתמש.
2. **כלי**: שימוש בעיבוד שפה טבעית ואלגוריתמים של למידת מכונה כדי לדרג ולסנן תוצאות חיפוש.
3. **הערכה**: ניתוח משוב משתמשים כדי לזהות ולתקן אי דיוקים במידע שנשלף.

### תיקון RAG ב-Travel Agent

תיקון RAG (יצירה מוגברת אחזור) משפר את יכולת ה-AI לאחזר וליצור מידע תוך תיקון אי דיוקים. בואו נראה איך Travel Agent יכול להשתמש בגישת תיקון RAG כדי לספק המלצות נסיעה מדויקות ורלוונטיות יותר.

זה כולל:

- **טכניקת הנחיה:** שימוש בהנחיות ספציפיות כדי להנחות את הסוכן באחזור מידע רלוונטי.
- **כלי:** יישום אלגוריתמים ומנגנונים שמאפשרים לסוכן להעריך את הרלוונטיות של המידע שנשלף וליצור תגובות מדויקות.
- **הערכה:** הערכה מתמשכת של ביצועי הסוכן וביצוע התאמות לשיפור דיוקו ויעילותו.

#### שלבים ליישום תיקון RAG ב-Travel Agent

1. **אינטראקציה ראשונית עם המשתמש**
   - Travel Agent אוסף העדפות ראשוניות מהמשתמש, כמו יעד, תאריכי נסיעה, תקציב ותחומי עניין.
   - דוגמה:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **אחזור מידע**
   - Travel Agent שולף מידע על טיסות, מקומות לינה, אטרקציות ומסעדות בהתבסס על העדפות המשתמש.
   - דוגמה:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **יצירת המלצות ראשוניות**
   - Travel Agent משתמש במידע שנשלף כדי ליצור מסלול אישי.
   - דוגמה:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **איסוף משוב משתמשים**
   - Travel Agent מבקש מהמשתמש משוב על ההמלצות הראשוניות.
   - דוגמה:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **תהליך תיקון RAG**
   - **טכניקת הנחיה**: Travel Agent מנסח שאילתות חיפוש חדשות בהתבסס על משוב המשתמש.
     - דוגמה:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **כלי**: Travel Agent משתמש באלגוריתמים לדרג ולסנן תוצאות חיפוש חדשות, תוך הדגשת הרלוונטיות בהתבסס על משוב המשתמש.
     - דוגמה:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **הערכה**: Travel Agent מעריך באופן מתמשך את הרלוונטיות והדיוק של המלצותיו על ידי ניתוח משוב משתמשים וביצוע התאמות נחוצות.
     - דוגמה:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```
```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)
        new_itinerary = self.generate_recommendations()
        return new_itinerary

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```

### טעינת הקשר מראש

טעינת הקשר מראש כוללת טעינת מידע רלוונטי או רקע לתוך המודל לפני עיבוד השאילתה. המשמעות היא שלמודל יש גישה למידע זה מההתחלה, מה שעוזר לו לייצר תגובות מושכלות יותר מבלי להזדקק לשליפת נתונים נוספים במהלך התהליך.

הנה דוגמה פשוטה לאופן שבו טעינת הקשר מראש עשויה להיראות באפליקציית סוכן נסיעות ב-Python:

```python
class TravelAgent:
    def __init__(self):
        # Pre-load popular destinations and their information
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Fetch destination information from pre-loaded context
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Example usage
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### הסבר

1. **אתחול (שיטת `__init__`)**: מחלקת `TravelAgent` טוענת מראש מילון המכיל מידע על יעדים פופולריים כמו פריז, טוקיו, ניו יורק וסידני. המילון כולל פרטים כמו מדינה, מטבע, שפה ואטרקציות מרכזיות לכל יעד.

2. **שליפת מידע (שיטת `get_destination_info`)**: כאשר משתמש שואל על יעד מסוים, השיטה `get_destination_info` שולפת את המידע הרלוונטי מהמילון הטעון מראש.

על ידי טעינת ההקשר מראש, אפליקציית סוכן הנסיעות יכולה להגיב במהירות לשאילתות משתמשים מבלי להזדקק לשליפת מידע ממקור חיצוני בזמן אמת. זה הופך את האפליקציה ליעילה ומהירה יותר.

### בניית תוכנית עם מטרה לפני איטרציה

בניית תוכנית עם מטרה כוללת התחלה עם יעד ברור או תוצאה רצויה בראש. על ידי הגדרת המטרה מראש, המודל יכול להשתמש בה כעקרון מנחה לאורך כל תהליך האיטרציה. זה עוזר להבטיח שכל איטרציה מתקדמת לעבר השגת התוצאה הרצויה, מה שהופך את התהליך ליעיל וממוקד יותר.

הנה דוגמה לאופן שבו ניתן לבנות תוכנית נסיעה עם מטרה לפני איטרציה עבור סוכן נסיעות ב-Python:

### תרחיש

סוכן נסיעות רוצה לתכנן חופשה מותאמת אישית עבור לקוח. המטרה היא ליצור מסלול נסיעה שממקסם את שביעות רצון הלקוח בהתבסס על העדפותיו והתקציב שלו.

### שלבים

1. להגדיר את העדפות הלקוח והתקציב.
2. לבנות תוכנית ראשונית בהתבסס על העדפות אלו.
3. לבצע איטרציות לשיפור התוכנית, תוך אופטימיזציה לשביעות רצון הלקוח.

#### קוד Python

```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# Example usage
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```

#### הסבר על הקוד

1. **אתחול (שיטת `__init__`)**: מחלקת `TravelAgent` מאותחלת עם רשימת יעדים פוטנציאליים, שלכל אחד מהם יש מאפיינים כמו שם, עלות וסוג פעילות.

2. **בניית תוכנית ראשונית (שיטת `bootstrap_plan`)**: שיטה זו יוצרת תוכנית נסיעה ראשונית בהתבסס על העדפות הלקוח והתקציב. היא עוברת על רשימת היעדים ומוסיפה אותם לתוכנית אם הם תואמים את העדפות הלקוח ומתאימים לתקציב.

3. **התאמת העדפות (שיטת `match_preferences`)**: שיטה זו בודקת אם יעד מסוים תואם את העדפות הלקוח.

4. **איטרציה על התוכנית (שיטת `iterate_plan`)**: שיטה זו משפרת את התוכנית הראשונית על ידי ניסיון להחליף כל יעד בתוכנית בהתאמה טובה יותר, תוך התחשבות בהעדפות הלקוח ובמגבלות התקציב.

5. **חישוב עלות (שיטת `calculate_cost`)**: שיטה זו מחשבת את העלות הכוללת של התוכנית הנוכחית, כולל יעד חדש פוטנציאלי.

#### דוגמה לשימוש

- **תוכנית ראשונית**: סוכן הנסיעות יוצר תוכנית ראשונית בהתבסס על העדפות הלקוח לטיולים ואתרים תיירותיים ותקציב של $2000.
- **תוכנית משופרת**: סוכן הנסיעות מבצע איטרציות על התוכנית, משפר אותה בהתאם להעדפות הלקוח והתקציב.

על ידי בניית התוכנית עם מטרה ברורה (למשל, מקסום שביעות רצון הלקוח) וביצוע איטרציות לשיפורה, סוכן הנסיעות יכול ליצור מסלול נסיעה מותאם ואופטימלי עבור הלקוח. גישה זו מבטיחה שהתוכנית תואמת את העדפות הלקוח והתקציב מההתחלה ומשתפרת עם כל איטרציה.

### ניצול מודלים גדולים לשפה (LLM) לדירוג מחדש וניקוד

מודלים גדולים לשפה (LLMs) יכולים לשמש לדירוג מחדש וניקוד על ידי הערכת הרלוונטיות והאיכות של מסמכים שנשלפו או תגובות שנוצרו. כך זה עובד:

**שליפה**: שלב השליפה הראשוני מאחזר סט של מסמכים או תגובות מועמדים בהתבסס על השאילתה.

**דירוג מחדש**: ה-LLM מעריך את המועמדים ומדרג אותם מחדש בהתבסס על הרלוונטיות והאיכות שלהם. שלב זה מבטיח שהמידע הרלוונטי והאיכותי ביותר יוצג ראשון.

**ניקוד**: ה-LLM מקצה ניקוד לכל מועמד, המשקף את הרלוונטיות והאיכות שלהם. זה עוזר בבחירת התגובה או המסמך הטוב ביותר עבור המשתמש.

על ידי ניצול LLMs לדירוג מחדש וניקוד, המערכת יכולה לספק מידע מדויק ורלוונטי יותר מבחינה הקשרית, ולשפר את חוויית המשתמש הכוללת.

הנה דוגמה לאופן שבו סוכן נסיעות עשוי להשתמש במודל שפה גדול (LLM) לדירוג מחדש וניקוד של יעדי נסיעה בהתבסס על העדפות משתמש ב-Python:

#### תרחיש - נסיעה לפי העדפות

סוכן נסיעות רוצה להמליץ על יעדי הנסיעה הטובים ביותר ללקוח בהתבסס על העדפותיו. ה-LLM יסייע בדירוג מחדש וניקוד היעדים כדי להבטיח שהאפשרויות הרלוונטיות ביותר יוצגו.

#### שלבים:

1. איסוף העדפות המשתמש.
2. שליפת רשימת יעדי נסיעה פוטנציאליים.
3. שימוש ב-LLM לדירוג מחדש וניקוד היעדים בהתבסס על העדפות המשתמש.

כך ניתן לעדכן את הדוגמה הקודמת לשימוש בשירותי Azure OpenAI:

#### דרישות

1. נדרש מנוי Azure.
2. צור משאב Azure OpenAI וקבל את מפתח ה-API שלך.

#### דוגמת קוד Python

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generate a prompt for the Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Define headers and payload for the request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Call the Azure OpenAI API to get the re-ranked and scored destinations
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extract and return the recommendations
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# Example usage
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```

#### הסבר על הקוד - Preference Booker

1. **אתחול**: מחלקת `TravelAgent` מאותחלת עם רשימת יעדי נסיעה פוטנציאליים, שלכל אחד מהם יש מאפיינים כמו שם ותיאור.

2. **קבלת המלצות (שיטת `get_recommendations`)**: שיטה זו מייצרת פרומפט לשירות Azure OpenAI בהתבסס על העדפות המשתמש ומבצעת בקשת HTTP POST ל-API של Azure OpenAI כדי לקבל יעדים מדורגים ומנוקדים.

3. **יצירת פרומפט (שיטת `generate_prompt`)**: שיטה זו בונה פרומפט עבור Azure OpenAI, הכולל את העדפות המשתמש ורשימת היעדים. הפרומפט מנחה את המודל לדרג מחדש ולנקד את היעדים בהתבסס על ההעדפות שסופקו.

4. **קריאת API**: ספריית `requests` משמשת לביצוע בקשת HTTP POST לנקודת הקצה של Azure OpenAI. התגובה מכילה את היעדים המדורגים והמנוקדים.

5. **דוגמה לשימוש**: סוכן הנסיעות אוסף את העדפות המשתמש (למשל, עניין באתרים תיירותיים ותרבות מגוונת) ומשתמש בשירות Azure OpenAI כדי לקבל המלצות מדורגות ומנוקדות ליעדי נסיעה.

ודא להחליף את `your_azure_openai_api_key` במפתח ה-API האמיתי שלך ואת `https://your-endpoint.com/...` בכתובת ה-URL האמיתית של נקודת הקצה של Azure OpenAI שלך.

על ידי ניצול ה-LLM לדירוג מחדש וניקוד, סוכן הנסיעות יכול לספק המלצות נסיעה מותאמות ורלוונטיות יותר ללקוחות, ולשפר את החוויה הכוללת שלהם.
#### דוגמה מעשית: חיפוש עם כוונה בסוכן נסיעות

בואו ניקח את סוכן הנסיעות כדוגמה כדי לראות כיצד ניתן ליישם חיפוש עם כוונה.

1. **איסוף העדפות משתמש**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **הבנת כוונת המשתמש**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **מודעות להקשר**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **חיפוש והתאמה אישית של תוצאות**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Example search logic for informational intent
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Example search logic for navigational intent
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Example search logic for transactional intent
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Example personalization logic
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Return top 10 personalized results
   ```

5. **שימוש לדוגמה**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. יצירת קוד ככלי

סוכנים ליצירת קוד משתמשים במודלים של בינה מלאכותית לכתיבה והרצת קוד, פתרון בעיות מורכבות ואוטומציה של משימות.

### סוכנים ליצירת קוד

סוכנים ליצירת קוד משתמשים במודלים גנרטיביים של בינה מלאכותית לכתיבה והרצת קוד. סוכנים אלו יכולים לפתור בעיות מורכבות, לאוטומט משימות ולספק תובנות חשובות על ידי יצירה והרצה של קוד בשפות תכנות שונות.

#### יישומים מעשיים

1. **יצירת קוד אוטומטית**: יצירת קטעי קוד למשימות ספציפיות, כמו ניתוח נתונים, גרידת רשת או למידת מכונה.  
2. **SQL כ-RAG**: שימוש בשאילתות SQL לשליפה ולעיבוד נתונים ממסדי נתונים.  
3. **פתרון בעיות**: יצירה והרצה של קוד לפתרון בעיות ספציפיות, כמו אופטימיזציה של אלגוריתמים או ניתוח נתונים.  

#### דוגמה: סוכן ליצירת קוד לניתוח נתונים

דמיינו שאתם מעצבים סוכן ליצירת קוד. כך זה עשוי לעבוד:

1. **משימה**: ניתוח מערך נתונים לזיהוי מגמות ודפוסים.  
2. **שלבים**:  
   - טעינת מערך הנתונים לכלי ניתוח נתונים.  
   - יצירת שאילתות SQL לסינון ואגרגציה של הנתונים.  
   - הרצת השאילתות ושליפת התוצאות.  
   - שימוש בתוצאות ליצירת ויזואליזציות ותובנות.  
3. **משאבים נדרשים**: גישה למערך הנתונים, כלי ניתוח נתונים ויכולות SQL.  
4. **ניסיון**: שימוש בתוצאות ניתוח קודמות לשיפור הדיוק והרלוונטיות של ניתוחים עתידיים.  

### דוגמה: סוכן ליצירת קוד עבור סוכן נסיעות

בדוגמה זו, נעצב סוכן ליצירת קוד, סוכן נסיעות, שיעזור למשתמשים בתכנון נסיעות על ידי יצירה והרצה של קוד. סוכן זה יכול לטפל במשימות כמו שליפת אפשרויות נסיעה, סינון תוצאות והרכבת מסלול באמצעות בינה מלאכותית גנרטיבית.

#### סקירה של סוכן ליצירת קוד

1. **איסוף העדפות משתמש**: איסוף קלט מהמשתמש כמו יעד, תאריכי נסיעה, תקציב ותחומי עניין.  
2. **יצירת קוד לשליפת נתונים**: יצירת קטעי קוד לשליפת נתונים על טיסות, מלונות ואטרקציות.  
3. **הרצת הקוד שנוצר**: הרצת הקוד שנוצר לשליפת מידע בזמן אמת.  
4. **יצירת מסלול נסיעה**: הרכבת הנתונים שנשלפו לתוכנית נסיעה מותאמת אישית.  
5. **התאמה על בסיס משוב**: קבלת משוב מהמשתמש ויצירת קוד מחדש במידת הצורך לשיפור התוצאות.  

#### יישום שלב אחר שלב

1. **איסוף העדפות משתמש**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **יצירת קוד לשליפת נתונים**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Example: Generate code to search for flights based on user preferences
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Example: Generate code to search for hotels
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **הרצת הקוד שנוצר**

   ```python
   def execute_code(code):
       # Execute the generated code using exec
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **יצירת מסלול נסיעה**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **התאמה על בסיס משוב**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Adjust preferences based on user feedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerate and execute code with updated preferences
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### ניצול מודעות סביבתית והסקת מסקנות

שימוש במבנה הטבלה יכול לשפר את תהליך יצירת השאילתות על ידי ניצול מודעות סביבתית והסקת מסקנות.

הנה דוגמה כיצד ניתן לעשות זאת:

1. **הבנת המבנה**: המערכת תבין את מבנה הטבלה ותשתמש במידע זה כדי לבסס את יצירת השאילתות.  
2. **התאמה על בסיס משוב**: המערכת תתאים את העדפות המשתמש על בסיס משוב ותסיק אילו שדות במבנה יש לעדכן.  
3. **יצירה והרצה של שאילתות**: המערכת תיצור ותבצע שאילתות לשליפת נתוני טיסות ומלונות מעודכנים על בסיס העדפות חדשות.  

הנה דוגמת קוד Python מעודכנת שמיישמת את הרעיונות הללו:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Adjust preferences based on user feedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Reasoning based on schema to adjust other related preferences
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Custom logic to adjust preferences based on schema and feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generate code to fetch flight data based on updated preferences
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generate code to fetch hotel data based on updated preferences
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulate execution of code and return mock data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generate itinerary based on flights, hotels, and attractions
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Example schema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Example usage
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerate and execute code with updated preferences
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### הסבר - הזמנה על בסיס משוב

1. **מודעות למבנה**: המילון `schema` מגדיר כיצד יש להתאים העדפות על בסיס משוב. הוא כולל שדות כמו `favorites` ו-`avoid`, עם התאמות מתאימות.  
2. **התאמת העדפות (`adjust_based_on_feedback` method)**: שיטה זו מתאימה העדפות על בסיס משוב משתמש והמבנה.  
3. **התאמות מבוססות סביבה (`adjust_based_on_environment` method)**: שיטה זו מתאימה את ההתאמות על בסיס המבנה והמשוב.  
4. **יצירה והרצה של שאילתות**: המערכת יוצרת קוד לשליפת נתוני טיסות ומלונות מעודכנים על בסיס העדפות מותאמות ומדמה את ביצוע השאילתות.  
5. **יצירת מסלול נסיעה**: המערכת יוצרת מסלול מעודכן על בסיס נתוני טיסות, מלונות ואטרקציות חדשים.  

על ידי הפיכת המערכת למודעת לסביבה והסקת מסקנות על בסיס המבנה, ניתן ליצור שאילתות מדויקות ורלוונטיות יותר, מה שמוביל להמלצות נסיעה טובות יותר וחוויית משתמש מותאמת אישית.

### שימוש ב-SQL כטכניקת RAG (שליפה מוגברת)

SQL (שפת שאילתות מובנית) היא כלי עוצמתי לאינטראקציה עם מסדי נתונים. כאשר משתמשים בה כחלק מגישה של שליפה מוגברת (RAG), SQL יכולה לשלוף נתונים רלוונטיים ממסדי נתונים כדי ליידע וליצור תגובות או פעולות בסוכני בינה מלאכותית. בואו נחקור כיצד SQL יכולה לשמש כטכניקת RAG בהקשר של סוכן נסיעות.

#### מושגים מרכזיים

1. **אינטראקציה עם מסדי נתונים**:  
   - SQL משמשת לשאילת מסדי נתונים, שליפת מידע רלוונטי ועיבוד נתונים.  
   - דוגמה: שליפת פרטי טיסות, מידע על מלונות ואטרקציות ממסד נתונים של נסיעות.  

2. **שילוב עם RAG**:  
   - שאילתות SQL נוצרות על בסיס קלט והעדפות המשתמש.  
   - הנתונים שנשלפו משמשים ליצירת המלצות או פעולות מותאמות אישית.  

3. **יצירת שאילתות דינמית**:  
   - סוכן הבינה המלאכותית יוצר שאילתות SQL דינמיות על בסיס ההקשר וצרכי המשתמש.  
   - דוגמה: התאמת שאילתות SQL לסינון תוצאות על בסיס תקציב, תאריכים ותחומי עניין.  

#### יישומים

- **יצירת קוד אוטומטית**: יצירת קטעי קוד למשימות ספציפיות.  
- **SQL כ-RAG**: שימוש בשאילתות SQL לעיבוד נתונים.  
- **פתרון בעיות**: יצירה והרצה של קוד לפתרון בעיות.  

**דוגמה**:  
סוכן ניתוח נתונים:

1. **משימה**: ניתוח מערך נתונים למציאת מגמות.  
2. **שלבים**:  
   - טעינת מערך הנתונים.  
   - יצירת שאילתות SQL לסינון נתונים.  
   - הרצת שאילתות ושליפת תוצאות.  
   - יצירת ויזואליזציות ותובנות.  
3. **משאבים**: גישה למערך הנתונים, יכולות SQL.  
4. **ניסיון**: שימוש בתוצאות קודמות לשיפור ניתוחים עתידיים.  

#### דוגמה מעשית: שימוש ב-SQL בסוכן נסיעות

1. **איסוף העדפות משתמש**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **יצירת שאילתות SQL**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **הרצת שאילתות SQL**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **יצירת המלצות**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### דוגמאות לשאילתות SQL

1. **שאילתת טיסות**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **שאילתת מלונות**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **שאילתת אטרקציות**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

על ידי שימוש ב-SQL כחלק מטכניקת שליפה מוגברת (RAG), סוכני בינה מלאכותית כמו סוכן נסיעות יכולים לשלוף ולהשתמש בנתונים רלוונטיים באופן דינמי כדי לספק המלצות מדויקות ומותאמות אישית.

### דוגמה למטא-קוגניציה

כדי להדגים יישום של מטא-קוגניציה, ניצור סוכן פשוט ש*משקף את תהליך קבלת ההחלטות שלו* תוך כדי פתרון בעיה. בדוגמה זו, נבנה מערכת שבה סוכן מנסה לבחור מלון אופטימלי, אך לאחר מכן מעריך את ההיגיון שלו ומתאים את האסטרטגיה שלו כאשר הוא מבצע טעויות או בחירות לא אופטימליות.

#### כיצד זה מדגים מטא-קוגניציה:

1. **החלטה ראשונית**: הסוכן יבחר את המלון הזול ביותר, מבלי להבין את ההשפעה על האיכות.  
2. **רפלקציה והערכה**: לאחר הבחירה הראשונית, הסוכן יבדוק אם המלון הוא "בחירה גרועה" על סמך משוב משתמש. אם ימצא שהאיכות נמוכה מדי, הוא ישקף על ההיגיון שלו.  
3. **התאמת אסטרטגיה**: הסוכן יתאים את האסטרטגיה שלו על בסיס הרפלקציה ויעבור מ"זול ביותר" ל"איכות הגבוהה ביותר", ובכך ישפר את תהליך קבלת ההחלטות שלו בעתיד.  

הנה דוגמה:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Stores the hotels chosen previously
        self.corrected_choices = []  # Stores the corrected choices
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Available strategies

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # Let's assume we have some user feedback that tells us whether the last choice was good or not
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Adjust strategy if the previous choice was unsatisfactory
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# Simulate a list of hotels (price and quality)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Create an agent
agent = HotelRecommendationAgent()

# Step 1: The agent recommends a hotel using the "cheapest" strategy
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Step 2: The agent reflects on the choice and adjusts strategy if necessary
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Step 3: The agent recommends again, this time using the adjusted strategy
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### יכולות מטא-קוגניטיביות של הסוכן

הנקודה המרכזית כאן היא יכולתו של הסוכן:  
- להעריך את הבחירות ותהליך קבלת ההחלטות הקודם שלו.  
- להתאים את האסטרטגיה שלו על בסיס הרפלקציה, כלומר, מטא-קוגניציה בפעולה.  

זהו יישום פשוט של מטא-קוגניציה שבו המערכת מסוגלת להתאים את תהליך ההיגיון שלה על בסיס משוב פנימי.

### סיכום

מטא-קוגניציה היא כלי עוצמתי שיכול לשפר משמעותית את היכולות של סוכני בינה מלאכותית. על ידי שילוב תהליכים מטא-קוגניטיביים, ניתן לעצב סוכנים חכמים, גמישים ויעילים יותר. השתמשו במשאבים הנוספים כדי להעמיק בעולם המרתק של מטא-קוגניציה בסוכני בינה מלאכותית.

### יש לכם עוד שאלות על דפוס העיצוב של מטא-קוגניציה?

הצטרפו ל-[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) כדי לפגוש לומדים נוספים, להשתתף בשעות קבלה ולקבל תשובות לשאלות שלכם על סוכני בינה מלאכותית.

## שיעור קודם

[דפוס עיצוב רב-סוכנים](../08-multi-agent/README.md)

## שיעור הבא

[סוכני בינה מלאכותית בסביבת ייצור](../10-ai-agents-production/README.md)

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.