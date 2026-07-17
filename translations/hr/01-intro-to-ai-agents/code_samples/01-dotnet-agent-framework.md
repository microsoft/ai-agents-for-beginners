# 🌍 AI Agent za Putovanja s Microsoft Agent Framework (.NET)

## 📋 Pregled Scenarija

Ovaj primjer prikazuje kako izgraditi inteligentnog agenta za planiranje putovanja koristeći Microsoft Agent Framework za .NET. Agent može automatski generirati personalizirane itinerere jednodnevnih izleta za nasumične destinacije širom svijeta.

### Ključne Mogućnosti:

- 🎲 **Nasumični Odabir Destinacije**: Koristi prilagođeni alat za odabir mjesta za odmor
- 🗺️ **Inteligentno Planiranje Putovanja**: Kreira detaljne itinerere po danima
- 🔄 **Real-time Streaming**: Podržava i trenutne i streaming odgovore
- 🛠️ **Integracija Prilagođenog Alata**: Prikazuje kako proširiti mogućnosti agenta

## 🔧 Tehnička Arhitektura

### Osnovne Tehnologije

- **Microsoft Agent Framework**: Najnovija .NET implementacija za razvoj AI agenata
- **Azure OpenAI (Responses API)**: Koristi Azure OpenAI Responses API za izvođenje modela
- **Azure Identity**: Sigurno prijavljivanje putem `AzureCliCredential` (`az login`)
- **Sigurna Konfiguracija**: Upravljanje krajnjom točkom na temelju okoline

### Ključne Komponente

1. **AIAgent**: Glavni agent koji upravlja tokovima konverzacije
2. **Prilagođeni Alati**: funkcija `GetRandomDestination()` dostupna agentu
3. **Responses Klijent**: sučelje za razgovor temeljeno na Azure OpenAI Responses
4. **Podrška za Streaming**: Mogućnosti generiranja odgovora u stvarnom vremenu

### Obrasci Integracije

```mermaid
graph LR
    A[Korisnički Zahtjev] --> B[AI agent]
    B --> C[Azure OpenAI (API za odgovore)]
    B --> D[Alat za Dobivanje Nasumične Destinacije]
    C --> E[Putni Plan]
    D --> E
```

## 🚀 Kako Početi

### Preduvjeti

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ili noviji
- [Pretplata na Azure](https://azure.microsoft.com/free/) s Azure OpenAI resursom i postavljenim modelom
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — prijavite se s `az login`

### Potrebne Varijable Okoline

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# Zatim se prijavite kako bi AzureCliCredential mogao dobiti token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# Zatim se prijavite kako bi AzureCliCredential mogao dobiti token
az login
```

### Primjer Koda

Za pokretanje primjera koda,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Ili koristeći dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Pogledajte [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) za cjelokupan kod.

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4.1-mini";

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

## 🎓 Ključne Lekcije

1. **Arhitektura Agenta**: Microsoft Agent Framework pruža čist, tipično siguran pristup izgradnji AI agenata u .NET-u
2. **Integracija Alata**: Funkcije ukrašene atributima `[Description]` postaju dostupni alati agentu
3. **Upravljanje Konfiguracijom**: Varijable okoline i sigurno upravljanje vjerodajnicama prate najbolje prakse .NET-a
4. **Azure OpenAI Responses API**: Agent koristi Azure OpenAI Responses API preko Azure.AI.OpenAI SDK-a

## 🔗 Dodatni Resursi

- [Dokumentacija Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI u Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Aplikacije](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->