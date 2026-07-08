# 🎯 תבניות תכנון ועיצוב עם Azure OpenAI (Responses API) (.NET)

## 📋 מטרות הלמידה

המחברת הזו ממחישה תבניות תכנון ועיצוב ברמת ארגונית לבניית סוכנים אינטיליגנטיים באמצעות Microsoft Agent Framework ב-.NET עם Azure OpenAI (Responses API). תלמדו ליצור סוכנים היכולים לפרק בעיות מורכבות, לתכנן פתרונות מרובי שלבים, ולבצע זרימות עבודה מתוחכמות עם תכונות ארגוניות של .NET.

## ⚙️ דרישות מוקדמות והגדרה

**סביבת פיתוח:**
- .NET 9.0 SDK או גבוה יותר
- Visual Studio 2022 או VS Code עם תוסף C#
- מנוי Azure עם משאב Azure OpenAI ופריסת דגם
- ממשק שורת הפקודה של Azure — התחבר עם `az login`

**תלויות נדרשות:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**קונפיגורציית סביבה (קובץ .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## הפעלת הקוד

שיעור זה כולל יישום אפליקציית קובץ יחיד ב-.NET. להריץ אותו:

```bash
# להפוך את הקובץ להרצה (לינוקס/מק)
chmod +x 07-dotnet-agent-framework.cs

# להריץ את היישום
./07-dotnet-agent-framework.cs
```

או השתמש בפקודת dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## יישום הקוד

היישום המלא זמין ב-`07-dotnet-agent-framework.cs`, ומדגים:

- טעינת קונפיגורציית סביבה עם DotNetEnv
- הגדרת לקוח Azure OpenAI עבור Responses API
- הגדרת מודלי נתונים מובנים (Plan ו-TravelPlan) עם סריאליזציה ל-JSON
- יצירת סוכן AI עם פלט מובנה באמצעות סכמת JSON
- ביצוע בקשות תכנון עם תגובות בטוחות טיפוס

## מושגים מרכזיים

### תכנון מובנה עם מודלים בטוחים טיפוס

הסוכן משתמש במחלקות C# להגדרת מבנה פלט של התכנון:

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

### סכמת JSON לפלט מובנה

הסוכן מוגדר להחזיר תגובות התואמות לסכמת TravelPlan:

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

### הנחיות לסוכן התכנון

הסוכן מתפקד כמנתב, המפנה משימות לתת-סוכנים מומחים:

- FlightBooking: להזמנת טיסות וספק מידע על טיסות
- HotelBooking: להזמנת מלונות וספק מידע על מלונות
- CarRental: להשכרת רכב וספק מידע על השכרה
- ActivitiesBooking: להזמנת פעילויות וספק מידע על פעילויות
- DestinationInfo: לספק מידע על יעדים
- DefaultAgent: לטיפול בבקשות כלליות

## פלט צפוי

כאשר מפעילים את הסוכן עם בקשת תכנון טיול, הוא ינתח את הבקשה וייצור תוכנית מובנית עם הקצאת משימות מתאימות לסוכנים ספציאליים, במבנה JSON התואם לסכמת TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->