# 🎯 תכנון ודפוסי עיצוב עם Azure OpenAI (Responses API) (.NET)

## 📋 מטרות הלמידה

המחברת הזו מדגימה דפוסי תכנון ועיצוב ברמת ארגונית לבניית סוכנים אינטליגנטיים באמצעות Microsoft Agent Framework ב-.NET עם Azure OpenAI (Responses API). תלמד כיצד ליצור סוכנים היכולים לפרק בעיות מורכבות, לתכנן פתרונות מרובי שלבים, ולבצע זרימות עבודה מתוחכמות עם תכונות ארגוניות של .NET.

## ⚙️ דרישות מוקדמות והתקנה

**סביבת פיתוח:**
- .NET 9.0 SDK או גבוה יותר
- Visual Studio 2022 או VS Code עם תוסף C#
- מנוי Azure עם משאב Azure OpenAI והטמעת מודל
- Azure CLI — התחבר עם `az login`

**תלויות נדרשות:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**קונפיגורציית סביבה (קובץ .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## הרצת הקוד

שיעור זה כולל מימוש אפליקציית קובץ יחיד ב-.NET. כדי להריץ אותה:

```bash
# הפוך את הקובץ לניתן להרצה (לינוקס/macOS)
chmod +x 07-dotnet-agent-framework.cs

# הפעל את היישום
./07-dotnet-agent-framework.cs
```

או השתמש בפקודת dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## מימוש הקוד

המימוש המלא זמין בקובץ `07-dotnet-agent-framework.cs`, ומדגים:

- טעינת הגדרות סביבה עם DotNetEnv
- הגדרת לקוח Azure OpenAI ויצירת סוכן בינה מלאכותית באמצעות `GetChatClient().AsAIAgent()`
- הגדרת מודלים מובנים (Plan ו-TravelPlan) עם סיריאליזציה ב-JSON
- יצירת סוכן בינה מלאכותית עם פלט מובנה באמצעות סכמת JSON
- ביצוע בקשות תכנון עם תגובות בטוחות מבחינה טיפוסית

## מושגים מרכזיים

### תכנון מובנה עם מודלים בטוחים טיפוסית

הסוכן משתמש במחלקות C# להגדרת מבנה הפלט של התכנון:

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

### סכמת JSON לפלטים מובנים

הסוכן מוגדר להחזיר תגובות התואמות לסכמת TravelPlan:

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### הוראות סוכן התכנון

הסוכן פועל כרכז, שמאציל משימות לסוכנים מיוחדים:

- FlightBooking: להזמנת טיסות ומתן מידע על טיסות
- HotelBooking: להזמנת מלונות ומתן מידע על מלונות
- CarRental: להזמנת רכב ומתן מידע על השכרת רכב
- ActivitiesBooking: להזמנת פעילויות ומתן מידע על פעילויות
- DestinationInfo: למתן מידע על יעדים
- DefaultAgent: לטיפול בבקשות כלליות

## פלט צפוי

כשאתה מפעיל את הסוכן עם בקשת תכנון טיול, הוא ינתח את הבקשה ויצור תוכנית מובנית עם הקצאת משימות מתאימה לסוכנים מיוחדים, המעוצבת כ-JSON התואם לסכמת TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->