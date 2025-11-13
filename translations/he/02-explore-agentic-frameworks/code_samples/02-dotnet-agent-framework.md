<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T13:10:06+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "he"
}
-->
# 🔍 חקר Microsoft Agent Framework - סוכן בסיסי (.NET)

## 📋 מטרות למידה

דוגמה זו חוקרת את המושגים הבסיסיים של Microsoft Agent Framework דרך יישום סוכן בסיסי ב-.NET. תלמדו דפוסים סוכניים מרכזיים ותבינו כיצד סוכנים חכמים פועלים מאחורי הקלעים באמצעות C# ואקוסיסטם .NET.

### מה תלמדו

- 🏗️ **ארכיטקטורת סוכן**: הבנת המבנה הבסיסי של סוכני AI ב-.NET  
- 🛠️ **שילוב כלים**: כיצד סוכנים משתמשים בפונקציות חיצוניות להרחבת יכולות  
- 💬 **זרימת שיחה**: ניהול שיחות מרובות שלבים ושמירה על הקשר עם ניהול שרשורים  
- 🔧 **תבניות קונפיגורציה**: שיטות עבודה מומלצות להגדרת סוכן וניהולו ב-.NET  

## 🎯 מושגים מרכזיים

### עקרונות מסגרת סוכנים

- **אוטונומיה**: כיצד סוכנים מקבלים החלטות עצמאיות באמצעות הפשטות AI של .NET  
- **תגובתיות**: תגובה לשינויים בסביבה וקלטי משתמש  
- **יוזמה**: נקיטת פעולה על בסיס מטרות והקשר  
- **יכולת חברתית**: אינטראקציה באמצעות שפה טבעית עם שרשורי שיחה  

### רכיבים טכניים

- **AIAgent**: תזמור סוכן וניהול שיחות מרכזי (.NET)  
- **פונקציות כלים**: הרחבת יכולות הסוכן עם שיטות ותכונות ב-C#  
- **שילוב OpenAI**: ניצול מודלים שפתיים דרך APIs סטנדרטיים של .NET  
- **קונפיגורציה מאובטחת**: ניהול מפתחות API מבוסס סביבה  

## 🔧 מחסנית טכנולוגית

### טכנולוגיות ליבה

- Microsoft Agent Framework (.NET)  
- שילוב API של GitHub Models  
- תבניות לקוח תואמות OpenAI  
- קונפיגורציה מבוססת סביבה עם DotNetEnv  

### יכולות סוכן

- הבנה ויצירת שפה טבעית  
- קריאת פונקציות ושימוש בכלים עם תכונות C#  
- תגובות מודעות להקשר עם שרשורי שיחה  
- ארכיטקטורה ניתנת להרחבה עם תבניות הזרקת תלות  

## 📚 השוואת מסגרות

דוגמה זו מדגימה את הגישה של Microsoft Agent Framework בהשוואה למסגרות סוכנים אחרות:

| תכונה | Microsoft Agent Framework | מסגרות אחרות |
|-------|---------------------------|--------------|
| **שילוב** | אקוסיסטם מקורי של Microsoft | תאימות משתנה |
| **פשטות** | API נקי ואינטואיטיבי | לעיתים הגדרה מורכבת |
| **הרחבה** | שילוב כלים קל | תלוי מסגרת |
| **מוכנות לארגונים** | בנוי לייצור | משתנה לפי מסגרת |

## 🚀 תחילת עבודה

### דרישות מוקדמות

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) או גרסה מתקדמת יותר  
- [אסימון גישה ל-API של GitHub Models](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### משתני סביבה נדרשים

```bash
# zsh/bash
export GH_TOKEN=<your_github_token>
export GH_ENDPOINT=https://models.github.ai/inference
export GH_MODEL_ID=openai/gpt-5-mini
```
  
```powershell
# PowerShell
$env:GH_TOKEN = "<your_github_token>"
$env:GH_ENDPOINT = "https://models.github.ai/inference"
$env:GH_MODEL_ID = "openai/gpt-5-mini"
```
  

### קוד לדוגמה

כדי להריץ את דוגמת הקוד,  

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
או באמצעות CLI של dotnet:  

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
ראו [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) עבור הקוד המלא.  

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*

using System.ClientModel;
using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using OpenAI;

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

// Extract configuration from environment variables
// Retrieve the GitHub Models API endpoint, defaults to https://models.github.ai/inference if not specified
// Retrieve the model ID, defaults to openai/gpt-5-mini if not specified
// Retrieve the GitHub token for authentication, throws exception if not specified
var github_endpoint = Environment.GetEnvironmentVariable("GH_ENDPOINT") ?? "https://models.github.ai/inference";
var github_model_id = Environment.GetEnvironmentVariable("GH_MODEL_ID") ?? "openai/gpt-5-mini";
var github_token = Environment.GetEnvironmentVariable("GH_TOKEN") ?? throw new InvalidOperationException("GH_TOKEN is not set.");

// Configure OpenAI Client Options
// Create configuration options to point to GitHub Models endpoint
// This redirects OpenAI client calls to GitHub's model inference service
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
// Create OpenAI client using GitHub token for authentication
// Configure it to use GitHub Models endpoint instead of OpenAI directly
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

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
// Initialize complete agent pipeline: OpenAI client → Chat client → AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
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
  

## 🎓 תובנות מרכזיות

1. **ארכיטקטורת סוכן**: Microsoft Agent Framework מספק גישה נקייה ובטוחה לבניית סוכני AI ב-.NET  
2. **שילוב כלים**: פונקציות המעוטרות בתכונות `[Description]` הופכות לכלים זמינים עבור הסוכן  
3. **הקשר שיחה**: ניהול שרשורים מאפשר שיחות מרובות שלבים עם מודעות מלאה להקשר  
4. **ניהול קונפיגורציה**: משתני סביבה וטיפול מאובטח באישורים עוקבים אחר שיטות העבודה המומלצות של .NET  
5. **תאימות OpenAI**: שילוב GitHub Models פועל בצורה חלקה דרך APIs תואמי OpenAI  

## 🔗 משאבים נוספים

- [תיעוד Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)  
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו אחראים לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->