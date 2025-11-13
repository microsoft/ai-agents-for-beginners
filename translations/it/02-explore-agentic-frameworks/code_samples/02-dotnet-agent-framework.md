<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T12:18:07+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "it"
}
-->
# 🔍 Esplorare il Microsoft Agent Framework - Agente Base (.NET)

## 📋 Obiettivi di Apprendimento

Questo esempio esplora i concetti fondamentali del Microsoft Agent Framework attraverso un'implementazione di un agente base in .NET. Imparerai i modelli agentici principali e comprenderai come funzionano gli agenti intelligenti dietro le quinte utilizzando C# e l'ecosistema .NET.

### Cosa Scoprirai

- 🏗️ **Architettura degli Agenti**: Comprendere la struttura di base degli agenti AI in .NET  
- 🛠️ **Integrazione degli Strumenti**: Come gli agenti utilizzano funzioni esterne per ampliare le capacità  
- 💬 **Flusso Conversazionale**: Gestire conversazioni multi-turno e contesto con la gestione dei thread  
- 🔧 **Modelli di Configurazione**: Best practice per la configurazione e gestione degli agenti in .NET  

## 🎯 Concetti Chiave Trattati

### Principi del Framework Agentico

- **Autonomia**: Come gli agenti prendono decisioni indipendenti utilizzando astrazioni AI di .NET  
- **Reattività**: Rispondere ai cambiamenti ambientali e agli input degli utenti  
- **Proattività**: Agire in base agli obiettivi e al contesto  
- **Abilità Sociale**: Interagire attraverso il linguaggio naturale con thread conversazionali  

### Componenti Tecnici

- **AIAgent**: Orchestrazione centrale dell'agente e gestione delle conversazioni (.NET)  
- **Funzioni Strumentali**: Estendere le capacità dell'agente con metodi e attributi C#  
- **Integrazione OpenAI**: Utilizzare modelli linguistici attraverso API standardizzate .NET  
- **Configurazione Sicura**: Gestione delle chiavi API basata sull'ambiente  

## 🔧 Stack Tecnologico

### Tecnologie Principali

- Microsoft Agent Framework (.NET)  
- Integrazione API dei modelli GitHub  
- Pattern client compatibili con OpenAI  
- Configurazione basata sull'ambiente con DotNetEnv  

### Capacità dell'Agente

- Comprensione e generazione del linguaggio naturale  
- Chiamata di funzioni e utilizzo di strumenti con attributi C#  
- Risposte consapevoli del contesto con thread conversazionali  
- Architettura estensibile con modelli di iniezione delle dipendenze  

## 📚 Confronto tra Framework

Questo esempio dimostra l'approccio del Microsoft Agent Framework rispetto ad altri framework agentici:

| Caratteristica | Microsoft Agent Framework | Altri Framework |
|----------------|---------------------------|-----------------|
| **Integrazione** | Ecosistema Microsoft nativo | Compatibilità variabile |
| **Semplicità** | API pulita e intuitiva | Configurazione spesso complessa |
| **Estensibilità** | Integrazione degli strumenti semplice | Dipendente dal framework |
| **Pronto per l'Impresa** | Progettato per la produzione | Varia in base al framework |

## 🚀 Per Iniziare

### Prerequisiti

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o superiore  
- [Token di accesso API dei modelli GitHub](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### Variabili d'Ambiente Necessarie

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
  

### Codice di Esempio

Per eseguire l'esempio di codice,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
Oppure utilizzando la CLI di dotnet:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
Consulta [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) per il codice completo.

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
  

## 🎓 Punti Chiave

1. **Architettura degli Agenti**: Il Microsoft Agent Framework offre un approccio pulito e type-safe per costruire agenti AI in .NET  
2. **Integrazione degli Strumenti**: Le funzioni decorate con attributi `[Description]` diventano strumenti disponibili per l'agente  
3. **Contesto Conversazionale**: La gestione dei thread consente conversazioni multi-turno con piena consapevolezza del contesto  
4. **Gestione della Configurazione**: Le variabili d'ambiente e la gestione sicura delle credenziali seguono le best practice di .NET  
5. **Compatibilità OpenAI**: L'integrazione dei modelli GitHub funziona perfettamente attraverso API compatibili con OpenAI  

## 🔗 Risorse Aggiuntive

- [Documentazione Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)  
- [Marketplace dei Modelli GitHub](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->