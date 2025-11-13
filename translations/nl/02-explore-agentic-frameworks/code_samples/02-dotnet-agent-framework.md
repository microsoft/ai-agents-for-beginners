<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T13:05:56+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "nl"
}
-->
# 🔍 Verkennen van Microsoft Agent Framework - Basisagent (.NET)

## 📋 Leerdoelen

Dit voorbeeld verkent de fundamentele concepten van het Microsoft Agent Framework door middel van een basisimplementatie van een agent in .NET. Je leert de kernpatronen van agenten en begrijpt hoe intelligente agenten werken onder de motorkap met behulp van C# en het .NET-ecosysteem.

### Wat je zult ontdekken

- 🏗️ **Agentarchitectuur**: Begrip van de basisstructuur van AI-agenten in .NET  
- 🛠️ **Toolintegratie**: Hoe agenten externe functies gebruiken om hun mogelijkheden uit te breiden  
- 💬 **Gespreksstroom**: Beheer van meerstapsgesprekken en context met threadbeheer  
- 🔧 **Configuratiepatronen**: Best practices voor het opzetten en beheren van agenten in .NET  

## 🎯 Belangrijke concepten

### Principes van het Agent Framework

- **Autonomie**: Hoe agenten onafhankelijke beslissingen nemen met behulp van .NET AI-abstracties  
- **Reactiviteit**: Reageren op veranderingen in de omgeving en gebruikersinvoer  
- **Proactiviteit**: Initiatief nemen op basis van doelen en context  
- **Sociale vaardigheid**: Interactie via natuurlijke taal met gespreksdraadbeheer  

### Technische componenten

- **AIAgent**: Kernorkestratie van agenten en gespreksbeheer (.NET)  
- **Toolfuncties**: Uitbreiden van agentmogelijkheden met C#-methoden en attributen  
- **OpenAI-integratie**: Gebruik van taalmodellen via gestandaardiseerde .NET API's  
- **Veilige configuratie**: API-sleutelbeheer op basis van omgevingsvariabelen  

## 🔧 Technische stack

### Kerntechnologieën

- Microsoft Agent Framework (.NET)  
- GitHub Models API-integratie  
- OpenAI-compatibele clientpatronen  
- Configuratie op basis van omgevingsvariabelen met DotNetEnv  

### Mogelijkheden van de agent

- Begrip en generatie van natuurlijke taal  
- Functieaanroepen en toolgebruik met C#-attributen  
- Contextbewuste reacties met gespreksdraadbeheer  
- Uitbreidbare architectuur met dependency injection-patronen  

## 📚 Vergelijking van frameworks

Dit voorbeeld laat de aanpak van het Microsoft Agent Framework zien in vergelijking met andere agentframeworks:

| Kenmerk | Microsoft Agent Framework | Andere frameworks |
|---------|---------------------------|-------------------|
| **Integratie** | Native Microsoft-ecosysteem | Variabele compatibiliteit |
| **Eenvoud** | Schone, intuïtieve API | Vaak complexe setup |
| **Uitbreidbaarheid** | Eenvoudige toolintegratie | Afhankelijk van framework |
| **Enterprise-klaar** | Gebouwd voor productie | Verschilt per framework |

## 🚀 Aan de slag

### Vereisten

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) of hoger  
- [GitHub Models API-toegangstoken](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### Vereiste omgevingsvariabelen

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
  

### Voorbeeldcode

Om het codevoorbeeld uit te voeren,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
Of gebruik de dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
Zie [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) voor de volledige code.

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
  

## 🎓 Belangrijke inzichten

1. **Agentarchitectuur**: Het Microsoft Agent Framework biedt een schone, typeveilige aanpak voor het bouwen van AI-agenten in .NET  
2. **Toolintegratie**: Functies met het `[Description]`-attribuut worden beschikbaar als tools voor de agent  
3. **Gesprekscontext**: Threadbeheer maakt meerstapsgesprekken mogelijk met volledige contextbewustzijn  
4. **Configuratiebeheer**: Omgevingsvariabelen en veilig omgaan met referenties volgen de beste praktijken van .NET  
5. **OpenAI-compatibiliteit**: GitHub Models-integratie werkt naadloos via OpenAI-compatibele API's  

## 🔗 Aanvullende bronnen

- [Microsoft Agent Framework Documentatie](https://learn.microsoft.com/agent-framework)  
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->