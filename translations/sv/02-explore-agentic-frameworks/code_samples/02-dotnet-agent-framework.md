# 🔍 Utforska Microsoft Agent Framework - Grundläggande agent (.NET)

## 📋 Läromål

Detta exempel utforskar grundläggande koncept i Microsoft Agent Framework genom en grundläggande agentimplementering i .NET. Du kommer att lära dig kärnmönster för agenter och förstå hur intelligenta agenter fungerar under huven med C# och .NET-ekosystemet.

### Vad du kommer att upptäcka

- 🏗️ **Agentarkitektur**: Förstå den grundläggande strukturen för AI-agenter i .NET
- 🛠️ **Verktygsintegration**: Hur agenter använder externa funktioner för att utöka kapaciteter  
- 💬 **Samtalsflöde**: Hantering av flerstegs-samtal och kontext med trådhantering
- 🔧 **Konfigurationsmönster**: Bästa praxis för agentinställning och hantering i .NET

## 🎯 Viktiga begrepp täckta

### Principer för Agent Framework

- **Autonomi**: Hur agenter fattar självständiga beslut med .NET AI-abstraktioner
- **Reaktivitet**: Respons på miljöförändringar och användarinmatningar
- **Proaktivitet**: Ta initiativ baserat på mål och kontext
- **Social förmåga**: Interagera genom naturligt språk med samtalstrådar

### Tekniska komponenter

- **AIAgent**: Kärnagentorkestrering och samtalshantering (.NET)
- **Verktygsfunktioner**: Utöka agentens kapabiliteter med C#-metoder och attribut
- **Azure OpenAI-integration**: Utnyttja språkmodeller via Azure OpenAI Responses API
- **Säker konfiguration**: Miljöbaserad endpoint-hantering

## 🔧 Teknisk stack

### Kärnteknologier

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) integration
- Azure.AI.OpenAI klientmönster
- Miljöbaserad konfiguration med DotNetEnv

### Agentkapabiliteter

- Naturlig språkförståelse och generering
- Funktionsanrop och verktygsanvändning med C#-attribut
- Kontextmedvetna svar med samtalssessioner
- Utbyggbar arkitektur med beroendeinjektionsmönster

## 📚 Ramverksjämförelse

Detta exempel demonstrerar Microsoft Agent Frameworks tillvägagångssätt jämfört med andra agentramverk:

| Funktion | Microsoft Agent Framework | Andra ramverk |
|---------|-------------------------|------------------|
| **Integration** | Inbyggt i Microsoft-ekosystemet | Varierande kompatibilitet |
| **Enkelhet** | Ren, intuitiv API | Ofta komplex uppsättning |
| **Utbyggbarhet** | Enkel verktygsintegration | Ramverksberoende |
| **Färdig för företagsbruk** | Utvecklad för produktion | Varierar per ramverk |

## 🚀 Komma igång

### Förutsättningar

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller högre
- Ett [Azure-abonnemang](https://azure.microsoft.com/free/) med en Azure OpenAI-resurs och en modellutplacering
- Azure CLI ([Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)) — logga in med `az login`

### Nödvändiga miljövariabler

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Logga in sedan så att AzureCliCredential kan hämta en token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Logga in så att AzureCliCredential kan hämta en token
az login
```

### Exempel på kod

För att köra kodexemplet,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Eller med dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Se [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) för hela koden.

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

## 🎓 Viktiga insikter

1. **Agentarkitektur**: Microsoft Agent Framework erbjuder ett rent, typsäkert tillvägagångssätt för att bygga AI-agenter i .NET
2. **Verktygsintegration**: Funktioner dekorerade med `[Description]`-attribut blir tillgängliga verktyg för agenten
3. **Samtalskontext**: Sessionshantering möjliggör flerstegsamtal med full kontextmedvetenhet
4. **Konfigurationshantering**: Miljövariabler och säker hantering av behörigheter följer .NET:s bästa praxis
5. **Azure OpenAI Responses API**: Agenten använder Azure OpenAI Responses API via Azure.AI.OpenAI SDK

## 🔗 Ytterligare resurser

- [Microsoft Agent Framework-dokumentation](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI i Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->