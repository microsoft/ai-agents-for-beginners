# 🔍 חקר מסגרת הסוכן של מייקרוסופט - סוכן בסיסי (.NET)

## 📋 מטרות הלמידה

דוגמה זו חוקרת את המושגים הבסיסיים של מסגרת הסוכן של מייקרוסופט דרך יישום סוכן בסיסי ב-.NET. תלמדו דפוסי סוכנות מרכזיים ותבינו כיצד סוכנים אינטיליגנטיים פועלים מתחת לפני השטח באמצעות C# ואקוסיסטם ה-.NET.

### מה תגלה

- 🏗️ **ארכיטקטורת סוכן**: הבנת המבנה הבסיסי של סוכני AI ב-.NET
- 🛠️ **שילוב כלים**: כיצד סוכנים משתמשים בפונקציות חיצוניות להרחבת יכולות  
- 💬 **זרימת שיחה**: ניהול שיחות רב-סבביות והקשר עם ניהול תהליכים
- 🔧 **דפוסי תצורה**: שיטות מיטביות להגדרת וניהול סוכנים ב-.NET

## 🎯 מושגים מרכזיים כלולים

### עקרונות מסגרת סוכנות

- **אוטונומיה**: כיצד סוכנים מקבלים החלטות עצמאיות באמצעות הפשטות AI ב-.NET
- **תגובתיות**: תגובה לשינויים בסביבה ולקלטי המשתמש
- **יוזמה**: ייזום פעולות על בסיס מטרות והקשר
- **יכולת חברתית**: אינטראקציה באמצעות שפה טבעית עם שרשורי שיחה

### רכיבים טכניים

- **AIAgent**: תזמור מרכזי וניהול שיחות של הסוכן (.NET)
- **פונקציות כלים**: הרחבת יכולות הסוכן באמצעות מתודות ותכונות ב-C#
- **שילוב Azure OpenAI**: ניצול מודלי שפה דרך API של תגובות Azure OpenAI
- **תצורה בטוחה**: ניהול נקודות קצה מבוסס סביבה

## 🔧 ארכיטקטורה טכנית

### טכנולוגיות מרכזיות

- מסגרת הסוכן של מייקרוסופט (.NET)
- שילוב Azure OpenAI (API תגובות)
- דפוסי לקוח Azure.AI.OpenAI
- תצורה מבוססת סביבה עם DotNetEnv

### יכולות סוכן

- הבנת והפקת שפה טבעית
- קריאת פונקציות ושימוש בכלים עם תכונות ב-C#
- תגובות בהקשר עם מושבי שיחה
- ארכיטקטורה ניתנת להרחבה עם דפוסי הזרקת תלות

## 📚 השוואת מסגרות

דוגמה זו ממחישה את גישת מסגרת הסוכן של מייקרוסופט לעומת מסגרות סוכנות אחרות:

| תכונה | מסגרת הסוכן של מייקרוסופט | מסגרות אחרות |
|---------|-------------------------|------------------|
| **שילוב** | אקוסיסטם מייקרוסופט מקורי | תאימות משתנה |
| **פשטות** | API נקי ואינטואיטיבי | לעיתים הגדרה מורכבת |
| **הרחבה** | שילוב כלים קל | תלוי במסגרת |
| **מוכן לעסקים** | מיועד לפרודקשן | משתנה לפי המסגרת |

## 🚀 התחלה מהירה

### דרישות מוקדמות

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) או גרסה גבוהה יותר
- [מנוי Azure](https://azure.microsoft.com/free/) עם משאב Azure OpenAI ופריסת מודל
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — התחבר עם `az login`

### משתני סביבה דרושים

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# התחבר כדי ש-AzureCliCredential יוכל לקבל אסימון
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

להפעלת דוגמת הקוד,

```bash
# זש/באש
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

או באמצעות ממשק הפקודה dotnet:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

ראה [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) עבור הקוד המלא.

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

// Create New Session for Context Management.
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentSession session = await agent.CreateSessionAsync();

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

## 🎓 נקודות מרכזיות

1. **ארכיטקטורת סוכן**: מסגרת הסוכן של מייקרוסופט מספקת גישה נקייה ובטוחה מבחינת סוגים לבניית סוכני AI ב-.NET
2. **שילוב כלים**: פונקציות המעוטרות בתכונות `[Description]` הופכות לכלים זמינים עבור הסוכן
3. **הקשר שיחה**: ניהול מושבים מאפשר שיחות רב-סבביות עם מודעות מלאה להקשר
4. **ניהול תצורה**: משתני סביבה וטיפול מאובטח באישורים לפי שיטות העבודה הטובות של .NET
5. **API תגובות Azure OpenAI**: הסוכן משתמש ב-API תגובות Azure OpenAI דרך SDK של Azure.AI.OpenAI

## 🔗 משאבים נוספים

- [תיעוד מסגרת הסוכן של מייקרוסופט](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI במייקרוסופט Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [אפליקציות קובץ יחיד ב-.NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->