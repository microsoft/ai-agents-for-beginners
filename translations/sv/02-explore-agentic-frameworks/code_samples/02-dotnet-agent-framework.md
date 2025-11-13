<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T12:45:36+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "sv"
}
-->
# 🔍 Utforska Microsoft Agent Framework - Grundläggande Agent (.NET)

## 📋 Inlärningsmål

Detta exempel utforskar de grundläggande koncepten i Microsoft Agent Framework genom en grundläggande agentimplementation i .NET. Du kommer att lära dig kärnmönster för agenter och förstå hur intelligenta agenter fungerar bakom kulisserna med hjälp av C# och .NET-ekosystemet.

### Vad du kommer att upptäcka

- 🏗️ **Agentarkitektur**: Förstå den grundläggande strukturen för AI-agenter i .NET  
- 🛠️ **Verktygsintegration**: Hur agenter använder externa funktioner för att utöka sina möjligheter  
- 💬 **Konversationsflöde**: Hantera flervändskonversationer och kontext med trådhantering  
- 🔧 **Konfigurationsmönster**: Bästa praxis för agentinställning och hantering i .NET  

## 🎯 Centrala koncept som täcks

### Principer för Agent Framework

- **Autonomi**: Hur agenter fattar självständiga beslut med hjälp av .NET AI-abstraktioner  
- **Reaktivitet**: Reagera på miljöförändringar och användarinmatningar  
- **Proaktivitet**: Ta initiativ baserat på mål och kontext  
- **Social förmåga**: Interagera genom naturligt språk med konversationstrådar  

### Tekniska komponenter

- **AIAgent**: Kärnan i agentens orkestrering och konversationshantering (.NET)  
- **Verktygsfunktioner**: Utöka agentens möjligheter med C#-metoder och attribut  
- **OpenAI-integration**: Utnyttja språkmodeller genom standardiserade .NET-API:er  
- **Säker konfiguration**: Hantering av API-nycklar baserat på miljövariabler  

## 🔧 Teknisk stack

### Kärnteknologier

- Microsoft Agent Framework (.NET)  
- GitHub Models API-integration  
- OpenAI-kompatibla klientmönster  
- Miljöbaserad konfiguration med DotNetEnv  

### Agentens möjligheter

- Förståelse och generering av naturligt språk  
- Funktionsanrop och verktygsanvändning med C#-attribut  
- Kontextmedvetna svar med konversationstrådar  
- Utbyggbar arkitektur med beroendeinjektionsmönster  

## 📚 Jämförelse av ramverk

Detta exempel visar Microsoft Agent Frameworks tillvägagångssätt jämfört med andra agentramverk:

| Funktion | Microsoft Agent Framework | Andra ramverk |
|----------|---------------------------|---------------|
| **Integration** | Inbyggt i Microsoft-ekosystemet | Varierande kompatibilitet |
| **Enkelhet** | Ren, intuitiv API | Ofta komplex installation |
| **Utbyggbarhet** | Enkel verktygsintegration | Ramverksberoende |
| **Företagsklar** | Byggd för produktion | Varierar beroende på ramverk |

## 🚀 Komma igång

### Förutsättningar

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller senare  
- [GitHub Models API-åtkomsttoken](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### Nödvändiga miljövariabler

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
  

### Exempelkod

För att köra kodexemplet,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
Eller använd dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
Se [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) för den kompletta koden.

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
  

## 🎓 Viktiga insikter

1. **Agentarkitektur**: Microsoft Agent Framework erbjuder ett rent, typsäkert tillvägagångssätt för att bygga AI-agenter i .NET  
2. **Verktygsintegration**: Funktioner dekorerade med `[Description]`-attribut blir tillgängliga verktyg för agenten  
3. **Konversationskontext**: Trådhantering möjliggör flervändskonversationer med full kontextmedvetenhet  
4. **Konfigurationshantering**: Miljövariabler och säker hantering av autentiseringsuppgifter följer .NET:s bästa praxis  
5. **OpenAI-kompatibilitet**: GitHub Models-integration fungerar sömlöst genom OpenAI-kompatibla API:er  

## 🔗 Ytterligare resurser

- [Microsoft Agent Framework-dokumentation](https://learn.microsoft.com/agent-framework)  
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->