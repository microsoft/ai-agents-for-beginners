# 🔍 Utforske Microsoft Agent Framework - Grunnleggende Agent (.NET)

## 📋 Læringsmål

Dette eksemplet utforsker de grunnleggende konseptene i Microsoft Agent Framework gjennom en enkel agentimplementering i .NET. Du vil lære kjerneagentiske mønstre og forstå hvordan intelligente agenter fungerer under panseret ved bruk av C# og .NET-økosystemet.

### Hva du vil oppdage

- 🏗️ **Agentarkitektur**: Forstå den grunnleggende strukturen til AI-agenter i .NET
- 🛠️ **Verktøyintegrasjon**: Hvordan agenter bruker eksterne funksjoner for å utvide muligheter  
- 💬 **Samtaleflyt**: Administrere flertrinns samtaler og kontekst med trådadministrasjon
- 🔧 **Konfigurasjonsmønstre**: Beste praksis for agentoppsett og styring i .NET

## 🎯 Nøkkelkonsepter som dekkes

### Agentiske rammeverksprinsipper

- **Autonomi**: Hvordan agenter tar uavhengige beslutninger ved bruk av .NET AI-abstraksjoner
- **Reaktivitet**: Reagerer på miljøendringer og brukerinnganger
- **Proaktivitet**: Tar initiativ basert på mål og kontekst
- **Sosial evne**: Samhandler gjennom naturlig språk med samtaletråder

### Tekniske komponenter

- **AIAgent**: Kjerneagentorkestrering og samtalestyring (.NET)
- **Verktøyfunksjoner**: Utvide agentens muligheter med C#-metoder og attributter
- **Azure OpenAI-integrasjon**: Utnytte språkmodeller gjennom Azure OpenAI Responses API
- **Sikker konfigurasjon**: Endepunktstyring basert på miljø

## 🔧 Teknologistabel

### Kjerneteknologier

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) integrasjon
- Azure.AI.OpenAI klientmønstre
- Miljøbasert konfigurasjon med DotNetEnv

### Agentkapasiteter

- Naturlig språkforståelse og generering
- Funksjonskalling og verktøybruk med C#-attributter
- Kontekstbevisste svar med samtaletråder
- Utvidbar arkitektur med avhengighetsinjeksjonsmønstre

## 📚 Rammeverkssammenligning

Dette eksemplet demonstrerer tilnærmingen til Microsoft Agent Framework sammenlignet med andre agentiske rammeverk:

| Funksjon | Microsoft Agent Framework | Andre rammeverk |
|---------|-------------------------|------------------|
| **Integrasjon** | Nativt Microsoft-økosystem | Varierende kompatibilitet |
| **Enkelhet** | Rent, intuitivt API | Ofte kompleks oppsett |
| **Utvidbarhet** | Enkel verktøyintegrasjon | Rammeverk-avhengig |
| **Enterprise-klar** | Bygget for produksjon | Varierer etter rammeverk |

## 🚀 Komme i gang

### Forutsetninger

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller nyere
- Et [Azure-abonnement](https://azure.microsoft.com/free/) med en Azure OpenAI-ressurs og en modellutplassering
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — logg inn med `az login`

### Påkrevde miljøvariabler

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Logg inn slik at AzureCliCredential kan få et token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Logg deretter på slik at AzureCliCredential kan hente en token
az login
```

### Eksempelkode

For å kjøre kodeeksemplet,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Eller ved å bruke dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Se [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) for hele koden.

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

## 🎓 Viktige læringspunkter

1. **Agentarkitektur**: Microsoft Agent Framework gir en ren, typesikker tilnærming til å bygge AI-agenter i .NET
2. **Verktøyintegrasjon**: Funksjoner dekorert med `[Description]`-attributter blir tilgjengelige verktøy for agenten
3. **Samtalekontekst**: Trådadministrasjon muliggjør flertrinnssamtaler med full kontekstbevissthet
4. **Konfigurasjonsstyring**: Miljøvariabler og sikker håndtering av legitimasjon følger .NET beste praksis
5. **Azure OpenAI Responses API**: Agenten bruker Azure OpenAI Responses API gjennom Azure.AI.OpenAI SDK

## 🔗 Ytterligere ressurser

- [Microsoft Agent Framework Dokumentasjon](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI i Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->