# 🛠️ שימוש מתקדם בכלים עם Azure OpenAI (Responses API) (.NET)

## 📋 יעדי הלמידה

פנקס זה ממחיש דפוסי אינטגרציה של כלים ברמה ארגונית באמצעות Microsoft Agent Framework ב-.NET עם Azure OpenAI (Responses API). תלמד לבנות סוכנים מתקדמים עם כמה כלים מקצועיים, תוך ניצול הטיפוס החזק של C# ותכונות הארגון של .NET.

### יכולות כלים מתקדמות שתשלוט בהן

- 🔧 **ארכיטקטורת כלים מרובים**: בניית סוכנים עם יכולות מיוחדות מרובות
- 🎯 **הרצת כלים בטיחותית בטיפוסים**: ניצול אימות בזמן הידור ב-C#
- 📊 **דפוסי כלים ארגוניים**: עיצוב כלים מוכנים לייצור וטיפול בשגיאות
- 🔗 **הרכבת כלים**: שילוב כלים לזרימות עבודה עסקיות מורכבות

## 🎯 יתרונות הארכיטקטורה של כלי .NET

### תכונות כלים ארגוניות

- **אימות בזמן הידור**: טיפוס חזק מבטיח נכונות פרמטרי הכלי
- **הזרקת תלות**: אינטגרציה עם מכולת IoC לניהול הכלים
- **דפוסי Async/Await**: הרצת כלים לא חוסמת עם ניהול משאבים נכון
- **לוג מבנה**: אינטגרציה מובנית ללוגים למעקב הרצת כלים

### דפוסים מוכנים לייצור

- **טיפול בשגיאות**: ניהול שגיאות מקיף עם חריגים מטיפוס
- **ניהול משאבים**: דפוסי סילוק נכונים וניהול זיכרון
- **מעקב ביצועים**: מדדים ומונים מובנים
- **ניהול תצורה**: תצורה בטיחותית בטיפוסים עם אימות

## 🔧 ארכיטקטורה טכנית

### רכיבי כלי ליבה ב-.NET

- **Microsoft.Extensions.AI**: שכבת הפשטה מאוחדת לכלים
- **Microsoft.Agents.AI**: תזמור כלים ברמה ארגונית
- **Azure OpenAI (Responses API)**: לקוח API ביצועים גבוהים עם בריכת חיבורים

### צינור הרצת כלים

```mermaid
graph LR
    A[בקשת משתמש] --> B[ניתוח סוכן]
    B --> C[בחירת כלי]
    C --> D[אימות סוג]
    B --> E[שיוך פרמטרים]
    E --> F[ביצוע כלי]
    C --> F
    F --> G[עיבוד תוצאה]
    D --> G
    G --> H[תגובה]
```

## 🛠️ קטגוריות ודפוסי כלים

### 1. **כלי עיבוד נתונים**

- **אימות קלט**: טיפוס חזק עם הערות נתונים
- **פעולות טרנספורמציה**: המרה ועיצוב נתונים בטיחותיים בטיפוסים
- **לוגיקה עסקית**: כלי חישוב וניתוח ספציפיים לתחום
- **עיצוב פלט**: יצירת תגובה מובנית

### 2. **כלי אינטגרציה**

- **מחברי API**: אינטגרציית שירות RESTful עם HttpClient
- **כלי מסדי נתונים**: אינטגרציית Entity Framework לגישה לנתונים
- **פעולות קבצים**: פעולות מערכת קבצים אבטוחות עם אימות
- **שירותים חיצוניים**: דפוסי אינטגרציה עם צד שלישי

### 3. **כלי עזר**

- **עיבוד טקסט**: מניפולציה ועיצוב מחרוזות
- **פעולות תאריך/שעה**: חישובים מודעי תרבות של תאריך/שעה
- **כלים מתמטיים**: חישובים מדויקים ופעולות סטטיסטיות
- **כלי אימות**: אימות חוקי עסק ואימות נתונים

מוכן לבנות סוכנים ברמת ארגון עם יכולות כלים חזקות ובטוחות טיפוסים ב-.NET? בוא נבנה כמה פתרונות מקצועיים! 🏢⚡

## 🚀 התחלה מהירה

### דרישות מוקדמות

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) או גרסה גבוהה יותר
- מינוי [Azure](https://azure.microsoft.com/free/) עם משאב Azure OpenAI ופריסת מודל
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — התחבר עם `az login`

### משתני סביבה נדרשים

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# לאחר מכן היכנס כדי ש-AzureCliCredential יוכל לקבל אסימון
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# לאחר מכן היכנס כדי ש-AzureCliCredential יוכל לקבל אסימון
az login
```

### דוגמת קוד

להריץ את דוגמת הקוד,

```bash
# זש/באש
chmod +x ./04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

או באמצעות dotnet CLI:

```bash
dotnet run ./04-dotnet-agent-framework.cs
```

ראה [`04-dotnet-agent-framework.cs`](../../../../04-tool-use/code_samples/04-dotnet-agent-framework.cs) עבור הקוד המלא.

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

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
    .GetChatClient(deployment)
    .AsAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Conversation Session for Context Management
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
await using var session = await agent.CreateSessionAsync();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the session parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", session))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation sessions and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", session))
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