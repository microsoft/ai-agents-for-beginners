# 🌍 AI cestovní agent s Microsoft Agent Framework (.NET)

## 📋 Přehled scénáře

Tento příklad ukazuje, jak vytvořit inteligentního agenta pro plánování cest pomocí Microsoft Agent Framework pro .NET. Agent může automaticky generovat personalizované itineráře jednodenních výletů do náhodných destinací po celém světě.

### Klíčové schopnosti:

- 🎲 **Výběr náhodné destinace**: Používá vlastní nástroj pro výběr dovolenkových míst
- 🗺️ **Inteligentní plánování výletu**: Vytváří detailní itineráře po jednotlivých dnech
- 🔄 **Přenos dat v reálném čase**: Podporuje jak okamžité, tak streamované odpovědi
- 🛠️ **Integrace vlastních nástrojů**: Ukazuje, jak rozšířit schopnosti agenta

## 🔧 Technická architektura

### Hlavní technologie

- **Microsoft Agent Framework**: Nejnovější .NET implementace pro vývoj AI agentů
- **Azure OpenAI (Responses API)**: Používá Azure OpenAI Responses API pro inference modelu
- **Azure Identity**: Bezpečné přihlášení přes `AzureCliCredential` (`az login`)
- **Bezpečná konfigurace**: Správa koncových bodů založená na prostředí

### Klíčové komponenty

1. **AIAgent**: Hlavní orchestrátor agenta, který řídí tok konverzace
2. **Vlastní nástroje**: Funkce `GetRandomDestination()` dostupná agentovi
3. **Klient Responses**: Rozhraní pro konverzaci založené na Azure OpenAI Responses
4. **Podpora streamování**: Schopnost generovat odpovědi v reálném čase

### Vzorec integrace

```mermaid
graph LR
    A[Uživatelský požadavek] --> B[AI agent]
    B --> C[Azure OpenAI (API odpovědí)]
    B --> D[Nástroj GetRandomDestination]
    C --> E[Cestovní itinerář]
    D --> E
```

## 🚀 Začínáme

### Požadavky

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) nebo novější
- [Azure předplatné](https://azure.microsoft.com/free/) s Azure OpenAI zdrojem a nasazením modelu
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — přihlaste se pomocí `az login`

### Vyžadované proměnné prostředí

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Přihlaste se, aby AzureCliCredential mohl získat token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Pak se přihlaste, aby AzureCliCredential mohl získat token
az login
```

### Ukázkový kód

Pro spuštění příkladu kódu,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Nebo pomocí dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Kompletní kód naleznete v [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs).

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.4.1
#:package Microsoft.Agents.AI.OpenAI@1.1.0
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

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip
// Run the agent with streaming enabled for real-time response display
// Shows the agent's thinking and response as it generates the content
// Provides better user experience with immediate feedback
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 Hlavní poznatky

1. **Architektura agenta**: Microsoft Agent Framework poskytuje čistý, typově bezpečný přístup k vytváření AI agentů v .NET
2. **Integrace nástrojů**: Funkce opatřené atributy `[Description]` se stanou dostupnými nástroji pro agenta
3. **Správa konfigurace**: Proměnné prostředí a bezpečné zacházení s přihlašovacími údaji odpovídají nejlepším .NET praktikám
4. **Azure OpenAI Responses API**: Agent používá Azure OpenAI Responses API přes Azure.AI.OpenAI SDK

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