# 🌍 AI Putnički agent s Microsoft Agent Framework (.NET)

## 📋 Pregled scenarija

Ovaj primjer prikazuje kako izgraditi inteligentnog agenta za planiranje putovanja koristeći Microsoft Agent Framework za .NET. Agent može automatski generirati personalizirane jednodnevne itinerare za nasumične destinacije širom svijeta.

### Ključne mogućnosti:

- 🎲 **Nasumični odabir destinacije**: Koristi prilagođeni alat za odabir destinacija za odmor
- 🗺️ **Inteligentno planiranje putovanja**: Stvara detaljne dnevnike planova po danima
- 🔄 **Streamanje u stvarnom vremenu**: Podržava i trenutne i streaming odgovore
- 🛠️ **Integracija prilagođenih alata**: Pokazuje kako proširiti mogućnosti agenta

## 🔧 Tehnička arhitektura

### Temeljne tehnologije

- **Microsoft Agent Framework**: Najnovija .NET implementacija za razvoj AI agenata
- **Azure OpenAI (Responses API)**: Koristi Azure OpenAI Responses API za model inferenciju
- **Azure Identity**: Sigurna prijava putem `AzureCliCredential` (`az login`)
- **Sigurna konfiguracija**: Upravljanje krajnjim točkama temeljeno na okolišu

### Ključne komponente

1. **AIAgent**: Glavni agent koji koordinira tok konverzacije
2. **Prilagođeni alati**: funkcija `GetRandomDestination()` dostupna agentu
3. **Responses klijent**: Sučelje za konverzaciju temeljeno na Azure OpenAI Responses
4. **Podrška za streaming**: Sposobnosti generiranja odgovora u stvarnom vremenu

### Uzorak integracije

```mermaid
graph LR
    A[Zahtjev korisnika] --> B[AI agent]
    B --> C[Azure OpenAI (Responses API)]
    B --> D[Alat GetRandomDestination]
    C --> E[Putni itinerar]
    D --> E
```

## 🚀 Početak

### Preduvjeti

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ili noviji
- Pretplata na [Azure](https://azure.microsoft.com/free/) s Azure OpenAI resursom i model deploymentom
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — prijavite se s `az login`

### Potrebne varijable okoline

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Zatim se prijavite kako bi AzureCliCredential mogao dobiti token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Zatim se prijavite kako bi AzureCliCredential mogao dobiti token
az login
```

### Primjer koda

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

Pogledajte [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) za kompletan kod.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@9.*
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

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetOpenAIResponseClient(deployment)
    .CreateAIAgent(
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

## 🎓 Ključne lekcije

1. **Arhitektura agenta**: Microsoft Agent Framework pruža čist i tip-siguran pristup izgradnji AI agenata u .NET-u
2. **Integracija alata**: Funkcije ukrašene `[Description]` atributima postaju dostupni alati agentu
3. **Upravljanje konfiguracijom**: Varijable okoline i sigurno upravljanje vjerodajnicama slijede najbolje prakse .NET-a
4. **Azure OpenAI Responses API**: Agent koristi Azure OpenAI Responses API putem Azure.AI.OpenAI SDK-a

## 🔗 Dodatni resursi

- [Microsoft Agent Framework dokumentacija](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI u Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET aplikacije u jednoj datoteci](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->