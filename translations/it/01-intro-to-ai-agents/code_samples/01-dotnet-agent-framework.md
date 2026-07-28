# 🌍 Agente di Viaggi AI con Microsoft Agent Framework (.NET)

## 📋 Panoramica dello Scenario

Questo esempio mostra come costruire un agente intelligente per la pianificazione di viaggi utilizzando il Microsoft Agent Framework per .NET. L'agente può generare automaticamente itinerari personalizzati per gite di un giorno in destinazioni casuali in tutto il mondo.

### Capacità Chiave:

- 🎲 **Selezione Casuale della Destinazione**: Usa uno strumento personalizzato per scegliere le mete delle vacanze
- 🗺️ **Pianificazione Intelligente del Viaggio**: Crea itinerari dettagliati giorno per giorno
- 🔄 **Streaming in Tempo Reale**: Supporta risposte immediate e in streaming
- 🛠️ **Integrazione di Strumenti Personalizzati**: Dimostra come estendere le capacità dell'agente

## 🔧 Architettura Tecnica

### Tecnologie Principali

- **Microsoft Agent Framework**: Ultima implementazione .NET per lo sviluppo di agenti AI
- **Azure OpenAI (Responses API)**: Usa l'API Responses di Azure OpenAI per l'inferenza del modello
- **Azure Identity**: Accesso sicuro tramite `AzureCliCredential` (`az login`)
- **Configurazione Sicura**: Gestione degli endpoint basata sull'ambiente

### Componenti Chiave

1. **AIAgent**: L'orchestratore principale che gestisce il flusso di conversazione
2. **Strumenti Personalizzati**: Funzione `GetRandomDestination()` disponibile per l'agente
3. **Responses Client**: Interfaccia di conversazione basata su Azure OpenAI Responses
4. **Supporto Streaming**: Capacità di generazione risposte in tempo reale

### Modello di Integrazione

```mermaid
graph LR
    A[Richiesta Utente] --> B[Agente AI]
    B --> C[Azure OpenAI (API Risposte)]
    B --> D[Strumento GetRandomDestination]
    C --> E[Itinerario di Viaggio]
    D --> E
```

## 🚀 Primi Passi

### Prerequisiti

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o superiore
- Un [abbonamento Azure](https://azure.microsoft.com/free/) con una risorsa Azure OpenAI e un deployment del modello
- La [CLI di Azure](https://learn.microsoft.com/cli/azure/install-azure-cli) — accedi con `az login`

### Variabili d'Ambiente Necessarie

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Poi esegui l'accesso in modo che AzureCliCredential possa ottenere un token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Quindi accedi in modo che AzureCliCredential possa ottenere un token
az login
```

### Codice di Esempio

Per eseguire l'esempio di codice,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Oppure usando la CLI dotnet:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Vedi [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) per il codice completo.

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

## 🎓 Punti Chiave

1. **Architettura dell'Agente**: Il Microsoft Agent Framework offre un approccio pulito e tipizzato per costruire agenti AI in .NET
2. **Integrazione Strumenti**: Le funzioni decorate con attributi `[Description]` diventano strumenti disponibili per l'agente
3. **Gestione della Configurazione**: Variabili d'ambiente e gestione sicura delle credenziali seguono le migliori pratiche .NET
4. **Azure OpenAI Responses API**: L'agente usa l'API Responses di Azure OpenAI tramite il SDK Azure.AI.OpenAI

## 🔗 Risorse Aggiuntive

- [Documentazione Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI in Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->