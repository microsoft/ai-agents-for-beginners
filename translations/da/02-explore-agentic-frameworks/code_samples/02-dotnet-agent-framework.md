<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T12:50:29+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "da"
}
-->
# 🔍 Udforskning af Microsoft Agent Framework - Grundlæggende Agent (.NET)

## 📋 Læringsmål

Dette eksempel udforsker de grundlæggende begreber i Microsoft Agent Framework gennem en simpel agentimplementering i .NET. Du vil lære om kerneprincipperne for agentmønstre og forstå, hvordan intelligente agenter fungerer bag kulisserne ved hjælp af C# og .NET-økosystemet.

### Hvad du vil opdage

- 🏗️ **Agentarkitektur**: Forstå den grundlæggende struktur af AI-agenter i .NET  
- 🛠️ **Værktøjsintegration**: Hvordan agenter bruger eksterne funktioner til at udvide deres kapaciteter  
- 💬 **Samtaleflow**: Håndtering af flerdelte samtaler og kontekst med trådadministration  
- 🔧 **Konfigurationsmønstre**: Bedste praksis for opsætning og styring af agenter i .NET  

## 🎯 Centrale begreber

### Principper for Agent Framework

- **Autonomi**: Hvordan agenter træffer selvstændige beslutninger ved hjælp af .NET AI-abstraktioner  
- **Reaktivitet**: Reagerer på miljøændringer og brugerinput  
- **Proaktivitet**: Tager initiativ baseret på mål og kontekst  
- **Social evne**: Interagerer gennem naturligt sprog med samtaletråde  

### Tekniske komponenter

- **AIAgent**: Kerneagentens orkestrering og samtalestyring (.NET)  
- **Værktøjsfunktioner**: Udvidelse af agentens kapaciteter med C#-metoder og attributter  
- **OpenAI-integration**: Udnyttelse af sprogmodeller gennem standardiserede .NET API'er  
- **Sikker konfiguration**: Miljøbaseret API-nøglehåndtering  

## 🔧 Teknisk stak

### Kerne-teknologier

- Microsoft Agent Framework (.NET)  
- GitHub Models API-integration  
- OpenAI-kompatible klientmønstre  
- Miljøbaseret konfiguration med DotNetEnv  

### Agentens kapaciteter

- Forståelse og generering af naturligt sprog  
- Funktionskald og værktøjsbrug med C#-attributter  
- Kontekstbevidste svar med samtaletråde  
- Udvidelig arkitektur med afhængighedsinjektionsmønstre  

## 📚 Sammenligning af frameworks

Dette eksempel demonstrerer Microsoft Agent Frameworks tilgang sammenlignet med andre agentframeworks:

| Funktion | Microsoft Agent Framework | Andre frameworks |
|----------|----------------------------|------------------|
| **Integration** | Indbygget i Microsoft-økosystemet | Varierende kompatibilitet |
| **Enkelhed** | Ren, intuitiv API | Ofte kompleks opsætning |
| **Udvidelighed** | Nem værktøjsintegration | Framework-afhængig |
| **Klar til erhverv** | Bygget til produktion | Varierer efter framework |

## 🚀 Kom godt i gang

### Forudsætninger

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller nyere  
- [GitHub Models API-adgangstoken](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### Påkrævede miljøvariabler

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
  

### Eksempelkode

For at køre kodeeksemplet,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
Eller ved hjælp af dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
Se [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) for den komplette kode.

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
  

## 🎓 Vigtige pointer

1. **Agentarkitektur**: Microsoft Agent Framework giver en ren, typesikker tilgang til at bygge AI-agenter i .NET  
2. **Værktøjsintegration**: Funktioner dekoreret med `[Description]`-attributter bliver tilgængelige værktøjer for agenten  
3. **Samtalekontekst**: Trådadministration muliggør flerdelte samtaler med fuld kontekstbevidsthed  
4. **Konfigurationsstyring**: Miljøvariabler og sikker håndtering af legitimationsoplysninger følger .NET bedste praksis  
5. **OpenAI-kompatibilitet**: GitHub Models-integration fungerer problemfrit gennem OpenAI-kompatible API'er  

## 🔗 Yderligere ressourcer

- [Microsoft Agent Framework Dokumentation](https://learn.microsoft.com/agent-framework)  
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->