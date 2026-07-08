# 🎨 דפוסי עיצוב סוכניים עם Azure OpenAI (Responses API) (.NET)

## 📋 יעדי למידה

דוגמה זו ממחישה דפוסי עיצוב ברמת ארגון לבניית סוכנים אינטיליגנטיים באמצעות Microsoft Agent Framework ב-.NET עם אינטגרציה של Azure OpenAI (Responses API). תלמד דפוסים מקצועיים וגישות ארכיטקטוניות שהופכות סוכנים למוכנים לייצור, ניתנים לתחזוקה ומדרגיים.

### דפוסי עיצוב ארגוניים

- 🏭 **דפוס מפעל**: יצירת סוכנים סטנדרטית עם הזרקת תלות
- 🔧 **דפוס בונה**: הגדרת סוכן בשפה זורמת
- 🧵 **דפוסים בטוחים לשרשור**: ניהול שיחות מקביליות
- 📋 **דפוס מאגר**: ניהול כלים ויכולות מאורגן

## 🎯 יתרונות ארכיטקטוניים ב-.NET

### תכונות ארגוניות

- **טיפוס חזק**: אימות בזמן קומפילציה ותמיכה ב-IntelliSense
- **הזרקת תלות**: אינטגרציה מובנית של מיכל DI
- **ניהול תצורה**: דפוסי IConfiguration ואפשרויות
- **Async/Await**: תמיכה מתקדמת בתכנות אסינכרוני

### דפוסים מוכנים לייצור

- **אינטגרציית רישום**: ILogger ותמיכה ברישום מובנה
- **בדיקות מצב בריאות**: ניטור ואבחון מובנה
- **אימות תצורה**: טיפוס חזק עם סימוני נתונים
- **טיפול בשגיאות**: ניהול חריגות מובנה

## 🔧 ארכיטקטורה טכנית

### רכיבי ליבה ב-.NET

- **Microsoft.Extensions.AI**: מופעים אחידים של שירותי AI
- **Microsoft.Agents.AI**: מסגרת לתזמור סוכנים ארגוניים
- **Azure OpenAI (Responses API)**: דפוסי לקוח API גבוהי ביצועים
- **מערכת תצורה**: appsettings.json ואינטגרציית סביבה

### יישום דפוסי עיצוב

```mermaid
graph LR
    A[IServiceCollection] --> B[בונה סוכן]
    B --> C[תצורה]
    C --> D[רישום כלי]
    D --> E[סוכן בינה מלאכותית]
```

## 🏗️ דפוסי ארגון מוצגים

### 1. **דפוסי יצירה**

- **מפעל סוכנים**: יצירת סוכן מרוכזת עם תצורה עקבית
- **דפוס בונה**: API זורם להגדרת סוכן מורכב
- **דפוס סינגלטון**: שיתוף משאבים וניהול תצורה
- **הזרקת תלות**: קישור רופף ויכולת בדיקה

### 2. **דפוסים התנהגותיים**

- **דפוס אסטרטגיה**: אסטרטגיות הפעלה להחלפה של כלים
- **דפוס פקודה**: פעולות סוכן מכוסות עם ביטול/שחזור
- **דפוס משקיף**: ניהול מחזור חיים מונחה אירועים
- **דפוס תבנית**: זרימות עבודה סטנדרטיות לביצוע סוכן

### 3. **דפוסים מבניים**

- **דפוס מתאם**: שכבת אינטגרציה של Azure OpenAI (Responses API)
- **דפוס דקורטור**: שיפור יכולות הסוכן
- **דפוס חזית**: ממשקי אינטראקציה פשוטים לסוכן
- **דפוס נציג**: טעינה עצלה ומטמון לביצועים

## 📚 עקרונות עיצוב ב-.NET

### עקרונות SOLID

- **אחריות יחידה**: כל רכיב בעל מטרה ברורה אחת
- **פתוח/סגור**: ניתן להרחבה ללא שינוי
- **החלפה על פי ליסקוב**: הפעלות כלים מבוססי ממשק
- **הפרדת ממשקים**: ממשקים ממוקדים וקוהרנטיים
- **היפוך תלות**: תלות במופעים מופשטים, לא בממשיים

### ארכיטקטורה נקייה

- **שכבת דומיין**: מופעי ליבה של סוכן וכלים
- **שכבת אפליקציה**: תזמור סוכן וזרימות עבודה
- **שכבת תשתית**: אינטגרציה של Azure OpenAI (Responses API) ושירותים חיצוניים
- **שכבת מצגת**: אינטראקציה עם משתמש ועיצוב תגובות

## 🔒 שיקולים ארגוניים

### אבטחה

- **ניהול אישורים**: טיפול מאובטח במפתחות API באמצעות IConfiguration
- **אימות קלט**: טיפוס חזק ואימות באמצעות סימוני נתונים
- **ניקוי פלט**: עיבוד וסינון תגובות מאובטח
- **רישום ביקורת**: מעקב מקיף אחרי פעולות

### ביצועים

- **דפוסי אסינכרוניות**: פעולות I/O לא חוסמות
- **בריכת קישורים**: ניהול יעיל של לקוח HTTP
- **מטמון**: מטמון תגובות לשיפור ביצועים
- **ניהול משאבים**: דפוסי ניקוי והשלכה נאותים

### מדרגיות

- **בטיחות שרשורים**: תמיכה בהרצת סוכנים מקבילית
- **בריכת משאבים**: ניצול יעיל של משאבים
- **ניהול עומסים**: הגבלת קצב וטיפול בלחץ חוזר
- **ניטור**: מדדי ביצועים ובדיקות מצב בריאות

## 🚀 פריסה בייצור

- **ניהול תצורה**: הגדרות ייעודיות לסביבה
- **אסטרטגיית רישום**: רישום מובנה עם מזהי קורלציה
- **טיפול בשגיאות**: טיפול גלובלי בחריגות עם התאוששות נאותה
- **ניטור**: תובנות אפליקציה ומדדי ביצועים
- **בדיקות**: בדיקות יחידה, בדיקות אינטגרציה ודפוסי בדיקות עומס

מוכן לבנות סוכנים אינטיליגנטיים ברמת ארגון עם .NET? בוא נבנה משהו חזק! 🏢✨

## 🚀 התחלה מהירה

### דרישות מוקדמות

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) או גרסה גבוה יותר
- חשבון [Azure](https://azure.microsoft.com/free/) עם משאב Azure OpenAI ופריסה של מודל
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — התחבר עם `az login`

### משתני סביבה נדרשים

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# לאחר מכן התחבר כדי ש-AzureCliCredential יוכל לקבל אסימון
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# לאחר מכן, היכנס כדי ש-AzureCliCredential יוכל לקבל אסימון
az login
```

### דוגמת קוד

להפעלת דוגמת הקוד,

```bash
# זש/באש
chmod +x ./03-dotnet-agent-framework.cs
./03-dotnet-agent-framework.cs
```

או באמצעות ה-CLI של dotnet:

```bash
dotnet run ./03-dotnet-agent-framework.cs
```

עיין ב-[`03-dotnet-agent-framework.cs`](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs) לקבלת הקוד המלא.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*
#:package Azure.AI.OpenAI@2.1.0
#:package Azure.Identity@1.13.1

using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using Azure.AI.OpenAI;
using Azure.Identity;

// Tool Function: Random Destination Generator
// This static method will be available to the agent as a callable tool
// The [Description] attribute helps the AI understand when to use this function
// This demonstrates how to create custom tools for AI agents
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
    // List of popular vacation destinations around the world
    // The agent will randomly select from these options
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

    // Generate random index and return selected destination
    // Uses System.Random for simple random selection
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}

// Azure OpenAI with the Responses API (stable v1 endpoint). Sign in with `az login`.
var azureEndpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")
    ?? throw new InvalidOperationException("AZURE_OPENAI_ENDPOINT is not set.");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4o-mini";

var azureClient = new AzureOpenAIClient(new Uri(azureEndpoint), new AzureCliCredential());

// Define Agent Identity and Comprehensive Instructions
// Agent name for identification and logging purposes
var AGENT_NAME = "TravelAgent";

// Detailed instructions that define the agent's personality, capabilities, and behavior
// This system prompt shapes how the agent responds and interacts with users
var AGENT_INSTRUCTIONS = """
You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
"Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?"

Always prioritize user preferences. If they mention a specific destination like "Bali" or "Paris," focus your planning on that location rather than suggesting alternatives.
""";

// Create AI Agent with Advanced Travel Planning Capabilities
// Get the Responses client for the deployment and create the AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = azureClient
    .GetOpenAIResponseClient(deployment)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Conversation Thread for Context Management
// Initialize a new conversation thread to maintain context across multiple interactions
// Threads enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentThread thread = agent.GetNewThread();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the thread parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation threads and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->