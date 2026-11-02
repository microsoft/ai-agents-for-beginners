# 🤝 מערכות זרימות עבודה מרובות-סוכנים לארגונים (.NET)

## 📋 מטרות הלמידה

פנקס הערות זה מדגים כיצד לבנות מערכות מרובות-סוכנים מתקדמות ברמת ארגון באמצעות Microsoft Agent Framework ב-.NET עם Azure OpenAI (Responses API). תלמד כיצד לתזמר סוכנים מתמחים רבים הפועלים יחד באמצעות זרימות עבודה מובנות, תוך ניצול תכונות ארגוניות של .NET לפתרונות מוכנים לייצור.

**יכולות מרובות-סוכנים לארגון שתבנה:**
- 👥 **שיתוף פעולה בין סוכנים**: תיאום סוכנים בטוח מבחינה טיפוסית עם אימות בזמן התרגום
- 🔄 **תזמור זרימות עבודה**: הגדרת זרימת עבודה הצהרתית עם דפוסי async של .NET
- 🎭 **התמחות בתפקידים**: אישיויות סוכן וסביבות מומחיות מנותחות בחוזקה
- 🏢 **אינטגרציה ארגונית**: דפוסים מוכנים לייצור עם ניטור וטיפול בשגיאות

## ⚙️ דרישות מוקדמות והגדרה

**סביבת פיתוח:**
- .NET 9.0 SDK או גרסה מתקדמת יותר
- Visual Studio 2022 או VS Code עם תוסף C#
- מנוי Azure (לסוכנים מתמשכים)

**חבילות NuGet נדרשות:**
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

## דוגמת קוד

קוד הפעלה מלא לשיעור זה זמין בקובץ ה-C# המצורף: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

כדי להריץ את הדוגמה:

```bash
# להפוך את הקובץ לקובץ הרצה (לינוקס/מק)
chmod +x 08-dotnet-agent-framework.cs

# להריץ את הדוגמה
./08-dotnet-agent-framework.cs
```

או באמצעות CLI של .NET:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## מה הדוגמה הזו מדגימה

מערכת זרימות העבודה מרובת-הסוכנים הזו יוצרת שירות המלצות לטיולי מלונות עם שני סוכנים מתמחים:

1. **סוכן הקבלה**: סוכן טיולים שמספק המלצות לפעילויות ומיקומים
2. **סוכן הקונסיירז'**: בודק המלצות כדי להבטיח חוויות אותנטיות ולא תיירותיות

הסוכנים פועלים יחד בזרימת עבודה שבה:
- סוכן הקבלה מקבל את הבקשה הראשונית לטיול
- סוכן הקונסיירז' בודק ומחדד את ההמלצה
- זרימת העבודה משדרת תגובות בזמן אמת

## מושגים מרכזיים

### תיאום סוכנים
הדוגמה מדגימה תיאום סוכנים בטוח מבחינה טיפוסית באמצעות Microsoft Agent Framework עם אימות בזמן התרגום.

### תזמור זרימות עבודה
משתמש בהגדרת זרימות עבודה הצהרתית עם דפוסי async של .NET לחיבור סוכנים מרובים בקו עבודה.

### שידור תגובות
מיישם שידור בזמן אמת של תגובות סוכנים באמצעות אסינכרוניות עם איטרטורים וארכיטקטורת אירועים.

### אינטגרציה ארגונית
מציג דפוסים מוכנים לייצור כולל:
- הגדרת משתני סביבה
- ניהול מאובטח של אישורים
- טיפול בשגיאות
- עיבוד אירועים אסינכרוני

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->