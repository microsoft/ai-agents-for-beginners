<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:58:15+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "he"
}
-->
# 🎯 תכנון ותבניות עיצוב עם מודלים של GitHub (.NET)

## 📋 מטרות למידה

מחברת זו מציגה תכנון ותבניות עיצוב ברמה ארגונית לבניית סוכנים חכמים באמצעות Microsoft Agent Framework ב-.NET עם מודלים של GitHub. תלמדו ליצור סוכנים שיכולים לפרק בעיות מורכבות, לתכנן פתרונות רב-שלביים ולהפעיל תהליכי עבודה מתקדמים עם תכונות ארגוניות של .NET.

## ⚙️ דרישות מוקדמות והגדרות

**סביבת פיתוח:**
- .NET 9.0 SDK או גרסה גבוהה יותר
- Visual Studio 2022 או VS Code עם הרחבת C#
- גישה ל-API של מודלים של GitHub

**תלויות נדרשות:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**הגדרת סביבה (קובץ .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## הפעלת הקוד

שיעור זה כולל יישום של אפליקציה בודדת ב-.NET. להפעלתה:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

או השתמשו בפקודת dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## יישום קוד

היישום המלא זמין בקובץ `07-dotnet-agent-framework.cs`, שמדגים:

- טעינת הגדרות סביבה עם DotNetEnv
- הגדרת לקוח OpenAI עבור מודלים של GitHub
- הגדרת מודלים של נתונים מובנים (Plan ו-TravelPlan) עם סריאליזציה ל-JSON
- יצירת סוכן AI עם פלט מובנה באמצעות JSON schema
- ביצוע בקשות תכנון עם תגובות בטוחות מסוג

## מושגים מרכזיים

### תכנון מובנה עם מודלים בטוחים מסוג

הסוכן משתמש במחלקות C# כדי להגדיר את מבנה פלטי התכנון:

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### JSON Schema לפלטים מובנים

הסוכן מוגדר להחזיר תגובות התואמות את הסכמה של TravelPlan:

```csharp
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### הוראות לסוכן תכנון

הסוכן פועל כמתאם, ומאציל משימות לסוכנים תת-מומחים:

- FlightBooking: להזמנת טיסות ומתן מידע על טיסות
- HotelBooking: להזמנת מלונות ומתן מידע על מלונות
- CarRental: להזמנת רכבים ומתן מידע על השכרת רכבים
- ActivitiesBooking: להזמנת פעילויות ומתן מידע על פעילויות
- DestinationInfo: למתן מידע על יעדים
- DefaultAgent: לטיפול בבקשות כלליות

## פלט צפוי

כאשר תפעילו את הסוכן עם בקשת תכנון נסיעה, הוא ינתח את הבקשה וייצור תוכנית מובנית עם הקצאת משימות מתאימה לסוכנים תת-מומחים, בפורמט JSON התואם את הסכמה של TravelPlan.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו אחראים לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.