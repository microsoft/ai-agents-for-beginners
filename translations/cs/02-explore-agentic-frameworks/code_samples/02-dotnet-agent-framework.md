# 🔍 Prozkoumání Microsoft Agent Framework – Základní agent (.NET)

## 📋 Výukové cíle

Tento příklad zkoumá základní koncepty Microsoft Agent Framework prostřednictvím implementace základního agenta v .NET. Naučíte se klíčové agentní vzory a pochopíte, jak inteligentní agenti fungují pod kapotou pomocí C# a ekosystému .NET.

### Co objevíte

- 🏗️ **Architektura agenta**: Porozumění základní struktuře AI agentů v .NET
- 🛠️ **Integrace nástrojů**: Jak agenti využívají externí funkce pro rozšíření schopností  
- 💬 **Tok konverzace**: Správa vícetahových konverzací a kontextu pomocí správy vláken
- 🔧 **Konfigurační vzory**: Nejlepší postupy pro nastavení a správu agenta v .NET

## 🎯 Klíčové pokryté koncepty

### Principy agentního rámce

- **Autonomie**: Jak agenti dělají nezávislá rozhodnutí pomocí .NET AI abstrakcí
- **Reaktivita**: Reagování na změny v prostředí a vstupy uživatele
- **Proaktivita**: Podnikání iniciativ na základě cílů a kontextu
- **Sociální schopnost**: Interakce přirozeným jazykem s vlákny konverzace

### Technické komponenty

- **AIAgent**: Jádro orchestrace agenta a správa konverzací (.NET)
- **Funkce nástrojů**: Rozšíření schopností agenta pomocí metod a atributů C#
- **Integrace Azure OpenAI**: Využití jazykových modelů přes Azure OpenAI Responses API
- **Bezpečná konfigurace**: Správa endpointů založená na prostředí

## 🔧 Technický stack

### Základní technologie

- Microsoft Agent Framework (.NET)
- Integrace Azure OpenAI (Responses API)
- Vzory klienta Azure.AI.OpenAI
- Konfigurace založená na prostředí s DotNetEnv

### Schopnosti agenta

- Porozumění a generování přirozeného jazyka
- Volání funkcí a používání nástrojů s atributy C#
- Kontextově uvědomělé odpovědi s vlákny konverzací
- Rozšiřitelná architektura se vzory dependency injection

## 📚 Porovnání rámců

Tento příklad ukazuje přístup Microsoft Agent Framework ve srovnání s jinými agentními rámci:

| Vlastnost | Microsoft Agent Framework | Ostatní rámce |
|---------|-------------------------|------------------|
| **Integrace** | Nativní Microsoft ekosystém | Různá kompatibilita |
| **Jednoduchost** | Čisté, intuitivní API | Často složité nastavení |
| **Rozšiřitelnost** | Snadná integrace nástrojů | Závislé na rámci |
| **Připravenost pro podnik** | Postaveno pro produkci | Liší se podle rámce |

## 🚀 Začínáme

### Předpoklady

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) nebo vyšší
- [Azure předplatné](https://azure.microsoft.com/free/) s Azure OpenAI zdrojem a nasazením modelu
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — přihlaste se pomocí `az login`

### Požadované proměnné prostředí

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Poté se přihlaste, aby AzureCliCredential mohl získat token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Poté se přihlaste, aby AzureCliCredential mohl získat token
az login
```

### Ukázkový kód

Pro spuštění příkladu kódu,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Nebo použitím dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Viz [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) pro kompletní kód.

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

## 🎓 Hlavní poznatky

1. **Architektura agenta**: Microsoft Agent Framework poskytuje čistý, typově bezpečný přístup k vytváření AI agentů v .NET
2. **Integrace nástrojů**: Funkce označené atributy `[Description]` se stávají dostupnými nástroji pro agenta
3. **Kontext konverzace**: Správa vláken umožňuje vícetahové konverzace s plným uvědoměním kontextu
4. **Správa konfigurace**: Proměnné prostředí a bezpečné nakládání s přihlašovacími údaji odpovídají nejlepším praktikám .NET
5. **Azure OpenAI Responses API**: Agent využívá Azure OpenAI Responses API přes Azure.AI.OpenAI SDK

## 🔗 Další zdroje

- [Dokumentace Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI v Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->