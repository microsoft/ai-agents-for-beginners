<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:37:36+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "he"
}
-->
# 🔍 חקר מסגרות סוכנים - סוכן בסיסי (.NET)

## 📋 מטרות למידה

מחברת זו חוקרת את המושגים הבסיסיים של מסגרת הסוכנים של Microsoft באמצעות יישום סוכן בסיסי ב-.NET. תלמדו דפוסי סוכנים מרכזיים ותבינו כיצד סוכנים חכמים פועלים מאחורי הקלעים באמצעות C# ואקוסיסטם .NET.

**מה תלמדו:**
- 🏗️ **ארכיטקטורת סוכן**: הבנת המבנה הבסיסי של סוכני AI ב-.NET  
- 🛠️ **שילוב כלים**: כיצד סוכנים משתמשים בפונקציות חיצוניות להרחבת יכולות  
- 💬 **זרימת שיחה**: ניהול שיחות מרובות סבבים והקשר עם ניהול שרשורים  
- 🔧 **דפוסי תצורה**: שיטות עבודה מומלצות להגדרת וניהול סוכנים ב-.NET  

## 🎯 מושגים מרכזיים

### עקרונות מסגרת סוכנים
- **אוטונומיה**: כיצד סוכנים מקבלים החלטות עצמאיות באמצעות הפשטות AI של .NET  
- **תגובתיות**: תגובה לשינויים בסביבה וקלטי משתמש  
- **יוזמה**: פעולה יזומה בהתבסס על מטרות והקשר  
- **יכולת חברתית**: אינטראקציה באמצעות שפה טבעית עם שרשורי שיחה  

### רכיבים טכניים
- **AIAgent**: תזמור סוכן וניהול שיחות מרכזי (.NET)  
- **פונקציות כלים**: הרחבת יכולות הסוכן עם שיטות ותכונות C#  
- **שילוב OpenAI**: ניצול מודלים שפתיים באמצעות APIs סטנדרטיים של .NET  
- **ניהול סביבה**: תצורה מאובטחת וטיפול באישורים עם DotNetEnv  

## ⚙️ דרישות מוקדמות והגדרה

**תלות נדרשת:**
- .NET 9.0 SDK או גרסה גבוהה יותר  
- Visual Studio 2022 או VS Code עם הרחבת C#  

**חבילות NuGet:**
- `Microsoft.Extensions.AI` - הפשטות AI מרכזיות  
- `Microsoft.Extensions.AI.OpenAI` - שילוב OpenAI (תצוגה מקדימה)  
- `DotNetEnv` - ניהול משתני סביבה  

**תצורת סביבה (קובץ .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```
  
## 🔧 מחסנית טכנית

**טכנולוגיות מרכזיות:**
- מסגרת סוכנים של Microsoft (.NET)  
- שילוב API של מודלים GitHub  
- דפוסי לקוח תואמים OpenAI  
- תצורה מבוססת סביבה עם DotNetEnv  

**יכולות סוכן:**
- הבנה ויצירת שפה טבעית  
- קריאת פונקציות ושימוש בכלים עם תכונות C#  
- תגובות מודעות להקשר עם שרשורי שיחה  
- ארכיטקטורה ניתנת להרחבה עם דפוסי הזרקת תלות  

## 📚 השוואת מסגרות

דוגמה זו מדגימה את גישת מסגרת הסוכנים של Microsoft ב-.NET בהשוואה לפלטפורמות אחרות:

| תכונה | מסגרת סוכנים .NET | מקבילים ב-Python |
|-------|-------------------|------------------|
| **בטיחות סוגים** | טיפוס חזק עם C# | טיפוס דינמי |
| **שילוב** | אקוסיסטם .NET מקורי | תאימות משתנה |
| **ביצועים** | ביצוע קוד מקומפל | ביצוע מפורש |
| **מוכנות ארגונית** | נבנה עבור אפליקציות .NET ייצוריות | משתנה לפי מסגרת |
| **כלים** | שילוב Visual Studio | תלוי ב-IDE |

## 🚀 התחלה

עקבו אחר התאים למטה כדי לבנות את הסוכן הבסיסי הראשון שלכם ב-.NET ולהבין מושגים בסיסיים של סוכנים!

## 📦 התקנה והגדרה

דוגמה זו זמינה כאפליקציית קובץ יחיד .NET שניתן להריץ. ראו את הקובץ המצורף `02-dotnet-agent-framework.cs` עבור היישום המלא.

כדי להריץ את הדוגמה:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
או באמצעות CLI של dotnet:

```bash
dotnet run 02-dotnet-agent-framework.cs
```
  
## 💡 סקירת קוד

היישום המלא כולל:

### 1. תלות חבילות

```csharp
// Core AI abstraction layer for .NET applications
#r "nuget: Microsoft.Extensions.AI, 9.9.1"

// Microsoft Agent Framework OpenAI integration
#r "nuget: Microsoft.Agents.AI.OpenAI, 1.0.0-preview.251001.3"

// Core Microsoft Agent Framework library
#r "nuget: Microsoft.Agents.AI, 1.0.0-preview.251001.3"

// Environment variable management
#r "nuget: DotNetEnv, 3.1.1"
```
  
### 2. ייבוא חיוני

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```
  
### 3. תצורת סביבה

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```
  
### 4. הגדרת פונקציות כלים

```csharp
// Random destination generator tool
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
    var destinations = new List<string>
    {
        "Paris, France",
        "Tokyo, Japan",
        "New York City, USA",
        "Sydney, Australia",
        "Rome, Italy",
        "Barcelona, Spain",
        "Cape Town, South Africa",
        "Rio de Janeiro, Brazil",
        "Bangkok, Thailand",
        "Vancouver, Canada"
    };
    
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}
```
  
### 5. תצורה והגדרת לקוח

```csharp
// Extract environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? 
    throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? 
    throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI client for GitHub Models
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI client
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);
```
  
### 6. תצורת סוכן

```csharp
const string AGENT_NAME = "TravelAgent";

const string AGENT_INSTRUCTIONS = @"You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
""Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?""

Always prioritize user preferences. If they mention a specific destination like ""Bali"" or ""Paris,"" focus your planning on that location rather than suggesting alternatives.
";
```
  
### 7. אתחול סוכן

```csharp
// Create AI agent with travel planning capabilities
AIAgent agent = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions)
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create((Func<string>)GetRandomDestination)]
    );
```
  
### 8. ניהול שיחה

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```
  
## 🎓 נקודות מרכזיות

1. **ארכיטקטורת סוכן**: מסגרת הסוכנים של Microsoft מספקת גישה נקייה ובטוחה לבניית סוכני AI ב-.NET  
2. **שילוב כלים**: פונקציות המעוטרות בתכונות `[Description]` הופכות לכלים זמינים עבור הסוכן  
3. **הקשר שיחה**: ניהול שרשורים מאפשר שיחות מרובות סבבים עם מודעות מלאה להקשר  
4. **ניהול תצורה**: משתני סביבה וטיפול מאובטח באישורים עוקבים אחר שיטות עבודה מומלצות של .NET  
5. **תאימות OpenAI**: שילוב מודלים GitHub עובד בצורה חלקה באמצעות APIs תואמי OpenAI  

## 🔗 משאבים נוספים

- [תיעוד מסגרת סוכנים של Microsoft](https://learn.microsoft.com/en-us/dotnet/ai/agents)  
- [שוק מודלים GitHub](https://github.com/marketplace/models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)  
- [אפליקציות קובץ יחיד .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)  

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא נושאים באחריות לכל אי הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.