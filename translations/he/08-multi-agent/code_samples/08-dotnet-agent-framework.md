<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:17:23+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "he"
}
-->
# 🤝 מערכות עבודה מרובת סוכנים לארגונים (.NET)

## 📋 מטרות למידה

מחברת זו מדגימה כיצד לבנות מערכות מרובות סוכנים מתקדמות ברמת ארגון באמצעות Microsoft Agent Framework ב-.NET עם מודלים של GitHub. תלמדו לתזמר מספר סוכנים מתמחים העובדים יחד דרך תהליכי עבודה מובנים, תוך ניצול תכונות הארגון של .NET לפתרונות מוכנים לייצור.

**יכולות מרובות סוכנים ארגוניות שתבנו:**
- 👥 **שיתוף פעולה בין סוכנים**: תיאום סוכנים עם בדיקת תקינות בזמן קומפילציה
- 🔄 **תזמור תהליכי עבודה**: הגדרת תהליכים דקלרטיבית עם תבניות אסינכרוניות של .NET
- 🎭 **התמחות תפקידים**: אישיות סוכנים מוגדרת היטב ותחומי מומחיות
- 🏢 **אינטגרציה ארגונית**: תבניות מוכנות לייצור עם ניטור וטיפול בשגיאות

## ⚙️ דרישות מוקדמות והגדרות

**סביבת פיתוח:**
- .NET 9.0 SDK או גרסה גבוהה יותר
- Visual Studio 2022 או VS Code עם הרחבת C#
- מנוי Azure (לסוכנים מתמשכים)

**חבילות NuGet נדרשות:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## דוגמת קוד

הקוד המלא לדוגמה זו זמין בקובץ C# המצורף: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

להרצת הדוגמה:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

או באמצעות .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## מה הדוגמה הזו מדגימה

מערכת תהליכי העבודה מרובת הסוכנים יוצרת שירות המלצות לטיולים במלון עם שני סוכנים מתמחים:

1. **סוכן קבלה**: סוכן נסיעות המספק המלצות לפעילויות ומיקומים
2. **סוכן קונסיירז'**: בודק את ההמלצות כדי להבטיח חוויות אותנטיות ולא תיירותיות

הסוכנים עובדים יחד בתהליך עבודה שבו:
- סוכן הקבלה מקבל את בקשת הטיול הראשונית
- סוכן הקונסיירז' בודק ומשפר את ההמלצה
- תהליך העבודה מזרים תגובות בזמן אמת

## מושגים מרכזיים

### תיאום סוכנים
הדוגמה מדגימה תיאום סוכנים עם בדיקת תקינות בזמן קומפילציה באמצעות Microsoft Agent Framework.

### תזמור תהליכי עבודה
משתמש בהגדרת תהליכים דקלרטיבית עם תבניות אסינכרוניות של .NET לחיבור מספר סוכנים בצינור עבודה.

### תגובות בזמן אמת
מיישם זרימה בזמן אמת של תגובות סוכנים באמצעות אסינכרוניות ואדריכלות מבוססת אירועים.

### אינטגרציה ארגונית
מציג תבניות מוכנות לייצור הכוללות:
- הגדרת משתני סביבה
- ניהול אישורים מאובטח
- טיפול בשגיאות
- עיבוד אירועים אסינכרוני

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.