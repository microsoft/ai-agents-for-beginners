<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T13:57:23+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "sk"
}
-->
# 🔍 Preskúmanie Microsoft Agent Framework - Základný Agent (.NET)

## 📋 Ciele učenia

Tento príklad skúma základné koncepty Microsoft Agent Framework prostredníctvom implementácie základného agenta v .NET. Naučíte sa hlavné agentické vzory a pochopíte, ako inteligentní agenti fungujú v zákulisí pomocou C# a ekosystému .NET.

### Čo objavíte

- 🏗️ **Architektúra agenta**: Pochopenie základnej štruktúry AI agentov v .NET
- 🛠️ **Integrácia nástrojov**: Ako agenti využívajú externé funkcie na rozšírenie schopností  
- 💬 **Tok konverzácie**: Správa viacotáčkových konverzácií a kontextu pomocou správy vlákien
- 🔧 **Konfiguračné vzory**: Najlepšie postupy pre nastavenie a správu agenta v .NET

## 🎯 Kľúčové pokryté koncepty

### Princípy Agentického Frameworku

- **Autonómia**: Ako agenti robia nezávislé rozhodnutia pomocou .NET AI abstrakcií
- **Reaktivita**: Reakcia na zmeny prostredia a vstupy používateľov
- **Proaktivita**: Iniciatíva na základe cieľov a kontextu
- **Sociálna schopnosť**: Interakcia prostredníctvom prirodzeného jazyka s konverzačnými vláknami

### Technické komponenty

- **AIAgent**: Orchestrácia agenta a správa konverzácií (.NET)
- **Funkcie nástrojov**: Rozšírenie schopností agenta pomocou C# metód a atribútov
- **Integrácia OpenAI**: Využitie jazykových modelov prostredníctvom štandardizovaných .NET API
- **Bezpečná konfigurácia**: Správa API kľúčov na základe prostredia

## 🔧 Technologický stack

### Hlavné technológie

- Microsoft Agent Framework (.NET)
- Integrácia GitHub Models API
- OpenAI-kompatibilné klientské vzory
- Konfigurácia na základe prostredia s DotNetEnv

### Schopnosti agenta

- Porozumenie a generovanie prirodzeného jazyka
- Volanie funkcií a používanie nástrojov s C# atribútmi
- Odpovede s uvedomením si kontextu pomocou konverzačných vlákien
- Rozšíriteľná architektúra s vzormi závislostnej injekcie

## 📚 Porovnanie frameworkov

Tento príklad demonštruje prístup Microsoft Agent Framework v porovnaní s inými agentickými frameworkmi:

| Funkcia | Microsoft Agent Framework | Iné frameworky |
|---------|-------------------------|------------------|
| **Integrácia** | Natívny Microsoft ekosystém | Rôzna kompatibilita |
| **Jednoduchosť** | Čisté, intuitívne API | Často zložitá inštalácia |
| **Rozšíriteľnosť** | Jednoduchá integrácia nástrojov | Závisí od frameworku |
| **Pripravenosť pre podniky** | Navrhnuté pre produkciu | Líši sa podľa frameworku |

## 🚀 Začíname

### Predpoklady

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) alebo novší
- [Prístupový token GitHub Models API](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)

### Požadované premenné prostredia

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

### Ukážkový kód

Na spustenie ukážky kódu,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Alebo pomocou dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Pozrite si [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) pre kompletný kód.

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

## 🎓 Hlavné poznatky

1. **Architektúra agenta**: Microsoft Agent Framework poskytuje čistý, typovo bezpečný prístup k budovaniu AI agentov v .NET
2. **Integrácia nástrojov**: Funkcie označené atribútmi `[Description]` sa stávajú dostupnými nástrojmi pre agenta
3. **Kontext konverzácie**: Správa vlákien umožňuje viacotáčkové konverzácie s plným uvedomením si kontextu
4. **Správa konfigurácie**: Premenné prostredia a bezpečné spracovanie poverení nasledujú najlepšie postupy .NET
5. **Kompatibilita s OpenAI**: Integrácia GitHub Models funguje bezproblémovo prostredníctvom OpenAI-kompatibilných API

## 🔗 Ďalšie zdroje

- [Dokumentácia Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->