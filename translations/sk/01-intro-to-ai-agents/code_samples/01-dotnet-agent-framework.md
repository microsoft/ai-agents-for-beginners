# 🌍 AI Cestovný agent s Microsoft Agent Framework (.NET)

## 📋 Prehľad scenára

Tento príklad demonštruje, ako vybudovať inteligentného agenta na plánovanie ciest pomocou Microsoft Agent Framework pre .NET. Agent dokáže automaticky vygenerovať personalizované itineráre jednodňových výletov pre náhodné destinácie po celom svete.

### Kľúčové schopnosti:

- 🎲 **Výber náhodnej destinácie**: Používa vlastný nástroj na výber miest na dovolenku
- 🗺️ **Inteligentné plánovanie výletu**: Vytvára podrobné itineráre po jednotlivých dňoch
- 🔄 **Streamovanie v reálnom čase**: Podporuje okamžité aj streamované odpovede
- 🛠️ **Integrácia vlastných nástrojov**: Demonštruje, ako rozšíriť schopnosti agenta

## 🔧 Technická architektúra

### Hlavné technológie

- **Microsoft Agent Framework**: Najnovšia implementácia .NET pre vývoj AI agentov
- **Azure OpenAI (Responses API)**: Používa Azure OpenAI Responses API pre inferenciu modelu
- **Azure Identity**: Bezpečné prihlásenie cez `AzureCliCredential` (`az login`)
- **Bezpečná konfigurácia**: Správa koncových bodov pomocou prostredia

### Kľúčové komponenty

1. **AIAgent**: Hlavný agent riadiaci tok konverzácie
2. **Vlastné nástroje**: Funkcia `GetRandomDestination()` dostupná agentovi
3. **Klient Responses**: Rozhranie konverzácie založené na Azure OpenAI Responses
4. **Podpora streamovania**: Schopnosti generovať odpovede v reálnom čase

### Vzor integrácie

```mermaid
graph LR
    A[Požiadavka používateľa] --> B[AI agent]
    B --> C[Azure OpenAI (Responses API)]
    B --> D[Nástroj GetRandomDestination]
    C --> E[Cestovný plán]
    D --> E
```

## 🚀 Začíname

### Požiadavky

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) alebo novší
- [Predplatné Azure](https://azure.microsoft.com/free/) s Azure OpenAI zdrojom a nasadeným modelom
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — prihláste sa pomocou `az login`

### Povinné premenné prostredia

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Potom sa prihláste, aby AzureCliCredential mohol získať token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Potom sa prihláste, aby AzureCliCredential mohol získať token
az login
```

### Ukážkový kód

Pre spustenie príkladu kódu,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Alebo použite dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Pozrite si [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) pre kompletný kód.

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

## 🎓 Hlavné zistenia

1. **Architektúra agenta**: Microsoft Agent Framework poskytuje čistý, bezpečný a typovo prísny prístup k tvorbe AI agentov v .NET
2. **Integrácia nástrojov**: Funkcie označené atribútmi `[Description]` sa stávajú dostupnými nástrojmi pre agenta
3. **Správa konfigurácie**: Premenné prostredia a bezpečné spracovanie poverení nasledujú najlepšie praktiky .NET
4. **Azure OpenAI Responses API**: Agent používa Azure OpenAI Responses API cez Azure.AI.OpenAI SDK

## 🔗 Ďalšie zdroje

- [Dokumentácia Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI v Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->