# 🌍 Agent de Călătorie AI cu Microsoft Agent Framework (.NET)

## 📋 Prezentarea Scenariului

Acest exemplu demonstrează cum să construiești un agent inteligent de planificare a călătoriilor folosind Microsoft Agent Framework pentru .NET. Agentul poate genera automat itinerarii personalizate pentru excursii de o zi către destinații aleatorii din întreaga lume.

### Capacități Cheie:

- 🎲 **Selectare Destinație Aleatorie**: Folosește un instrument personalizat pentru a alege locuri de vacanță
- 🗺️ **Planificare Inteligentă a Călătoriei**: Creează itinerarii detaliate zi cu zi
- 🔄 **Streaming în Timp Real**: Suportă răspunsuri imediate și streaming
- 🛠️ **Integrare Instrumente Personalizate**: Demonstrează cum să extinzi capacitățile agentului

## 🔧 Arhitectura Tehnică

### Tehnologii de Bază

- **Microsoft Agent Framework**: Implementarea de ultimă oră pentru dezvoltarea agenților AI în .NET
- **Azure OpenAI (Responses API)**: Folosește Azure OpenAI Responses API pentru inferență model
- **Azure Identity**: Autentificare securizată prin `AzureCliCredential` (`az login`)
- **Configurare Securizată**: Gestionarea endpoint-urilor bazată pe mediu

### Componente Cheie

1. **AIAgent**: Agentul principal de orchestrare care gestionează fluxul conversației
2. **Instrumente Personalizate**: Funcția `GetRandomDestination()` disponibilă agentului
3. **Client Responses**: Interfața conversațională bazată pe Azure OpenAI Responses
4. **Suport Streaming**: Capacități de generare a răspunsurilor în timp real

### Tipar de Integrare

```mermaid
graph LR
    A[Cerere utilizator] --> B[Agent AI]
    B --> C[Azure OpenAI (API pentru răspunsuri)]
    B --> D[Unealtă GetRandomDestination]
    C --> E[Itinerar de călătorie]
    D --> E
```

## 🚀 Început Rapid

### Cerințe Prealabile

- [SDK .NET 10](https://dotnet.microsoft.com/download/dotnet/10.0) sau versiune superioară
- Un [abonament Azure](https://azure.microsoft.com/free/) cu o resursă Azure OpenAI și un model implementat
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — autentifică-te cu `az login`

### Variabile de Mediu Necesare

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# Apoi conectați-vă pentru ca AzureCliCredential să poată obține un token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# Apoi autentificați-vă pentru ca AzureCliCredential să poată obține un token
az login
```

### Exemplu de Cod

Pentru a rula exemplul de cod,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Sau folosind CLI dotnet:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Vezi [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) pentru codul complet.

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

## 🎓 Concluzii Cheie

1. **Arhitectura Agentului**: Microsoft Agent Framework oferă o abordare clară și sigură din punct de vedere al tipurilor pentru construirea agenților AI în .NET
2. **Integrarea Instrumentelor**: Funcțiile decorate cu atribute `[Description]` devin instrumente disponibile pentru agent
3. **Gestionarea Configurării**: Variabilele de mediu și manipularea securizată a acreditărilor urmează cele mai bune practici .NET
4. **Azure OpenAI Responses API**: Agentul folosește Azure OpenAI Responses API prin SDK-ul Azure.AI.OpenAI

## 🔗 Resurse Suplimentare

- [Documentația Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI în Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [Aplicații .NET Single File](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->