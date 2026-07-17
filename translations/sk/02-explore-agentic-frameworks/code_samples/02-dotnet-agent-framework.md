# 🔍 Preskúmanie Microsoft Agent Framework - Základný agent (.NET)

## 📋 Ciele učenia

Tento príklad preskúmava základné koncepty Microsoft Agent Framework prostredníctvom implementácie základného agenta v .NET. Naučíte sa jadrové vzory agentov a pochopíte, ako inteligentní agenti fungujú pod kapotou pomocou C# a ekosystému .NET.

### Čo objavíte

- 🏗️ **Agentová architektúra**: Pochopenie základnej štruktúry AI agentov v .NET
- 🛠️ **Integrácia nástrojov**: Ako agenti používajú externé funkcie na rozšírenie svojich schopností  
- 💬 **Tok konverzácie**: Správa viackolových konverzácií a kontextu pomocou správy vlákien
- 🔧 **Konfiguračné vzory**: Najlepšie praktiky pre nastavenie a správu agentov v .NET

## 🎯 Kľúčové pokryté pojmy

### Zásady agentového rámca

- **Autonómia**: Ako agenti robia nezávislé rozhodnutia pomocou AI abstrakcií v .NET
- **Reaktivita**: Reagovanie na zmeny prostredia a vstupy používateľa
- **Proaktivita**: Prevzatie iniciatívy na základe cieľov a kontextu
- **Sociálna schopnosť**: Interakcia cez prirodzený jazyk pomocou vlákien konverzácií

### Technické komponenty

- **AIAgent**: Jadro orchestrace agenta a správa konverzácie (.NET)
- **Funkcie nástrojov**: Rozšírenie schopností agenta pomocou C# metód a atribútov
- **Integrácia Azure OpenAI**: Využívanie jazykových modelov cez Azure OpenAI Responses API
- **Bezpečná konfigurácia**: Správa koncových bodov založená na prostredí

## 🔧 Technologický stack

### Hlavné technológie

- Microsoft Agent Framework (.NET)
- Integrácia Azure OpenAI (Responses API)
- Vzory klienta Azure.AI.OpenAI
- Konfigurácia založená na prostredí s DotNetEnv

### Schopnosti agenta

- Porozumenie a generovanie prirodzeného jazyka
- Volanie funkcií a používanie nástrojov cez C# atribúty
- Odpovede založené na kontexte s konverzačnými session
- Rozšíriteľná architektúra s vzormi injektáže závislostí

## 📚 Porovnanie rámcov

Tento príklad demonštruje prístup Microsoft Agent Framework v porovnaní s inými agentovými rámcami:

| Funkcia | Microsoft Agent Framework | Iné rámce |
|---------|-------------------------|------------------|
| **Integrácia** | Natívny Microsoft ekosystém | Rozličná kompatibilita |
| **Jednoduchosť** | Čisté, intuitívne API | Často zložité nastavenie |
| **Rozšíriteľnosť** | Jednoduchá integrácia nástrojov | Závislé od rámca |
| **Podniková pripravenosť** | Postavený pre produkciu | Rozdielne podľa rámca |

## 🚀 Začíname

### Predpoklady

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) alebo novší
- [Azure predplatné](https://azure.microsoft.com/free/) s Azure OpenAI zdrojom a nasadením modelu
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — prihláste sa pomocou `az login`

### Požadované premenné prostredia

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# Potom sa prihláste, aby AzureCliCredential mohol získať token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# Potom sa prihláste, aby AzureCliCredential mohol získať token
az login
```

### Ukážkový kód

Na spustenie príkladu kódu,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Alebo použite dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Kompletný kód nájdete v [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs).

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4.1-mini";

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

## 🎓 Kľúčové poznatky

1. **Agentová architektúra**: Microsoft Agent Framework poskytuje čistý a typovo bezpečný prístup k tvorbe AI agentov v .NET
2. **Integrácia nástrojov**: Funkcie označené atribútmi `[Description]` sa stanú dostupnými nástrojmi pre agenta
3. **Kontext konverzácie**: Správa session umožňuje viackolové konverzácie so správou úplného kontextu
4. **Správa konfigurácie**: Premenné prostredia a bezpečné nakladanie s povereniami nasledujú osvedčené postupy .NET
5. **Azure OpenAI Responses API**: Agent používa Azure OpenAI Responses API prostredníctvom Azure.AI.OpenAI SDK

## 🔗 Dodatočné zdroje

- [Dokumentácia Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI v Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->