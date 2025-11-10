<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:35:06+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "it"
}
-->
# 🔍 Esplorare i Framework Agentici - Agente Base (.NET)

## 📋 Obiettivi di Apprendimento

Questo notebook esplora i concetti fondamentali del Microsoft Agent Framework attraverso un'implementazione di un agente base in .NET. Imparerai i modelli agentici principali e comprenderai come funzionano gli agenti intelligenti dietro le quinte utilizzando C# e l'ecosistema .NET.

**Cosa Scoprirai:**
- 🏗️ **Architettura degli Agenti**: Comprendere la struttura di base degli agenti AI in .NET
- 🛠️ **Integrazione degli Strumenti**: Come gli agenti utilizzano funzioni esterne per estendere le capacità  
- 💬 **Flusso di Conversazione**: Gestire conversazioni multi-turno e contesto con la gestione dei thread
- 🔧 **Modelli di Configurazione**: Best practice per la configurazione e gestione degli agenti in .NET

## 🎯 Concetti Chiave Trattati

### Principi del Framework Agentico
- **Autonomia**: Come gli agenti prendono decisioni indipendenti utilizzando astrazioni AI di .NET
- **Reattività**: Rispondere ai cambiamenti ambientali e agli input degli utenti
- **Proattività**: Prendere iniziative basate su obiettivi e contesto
- **Abilità Sociale**: Interagire attraverso il linguaggio naturale con thread di conversazione

### Componenti Tecnici
- **AIAgent**: Orchestrazione principale dell'agente e gestione delle conversazioni (.NET)
- **Funzioni Strumento**: Estendere le capacità dell'agente con metodi e attributi C#
- **Integrazione OpenAI**: Sfruttare i modelli linguistici attraverso API standardizzate .NET
- **Gestione dell'Ambiente**: Configurazione sicura e gestione delle credenziali con DotNetEnv

## ⚙️ Prerequisiti e Configurazione

**Dipendenze Necessarie:**
- .NET 9.0 SDK o superiore
- Visual Studio 2022 o VS Code con estensione C#

**Pacchetti NuGet:**
- `Microsoft.Extensions.AI` - Astrazioni AI principali
- `Microsoft.Extensions.AI.OpenAI` - Integrazione OpenAI (anteprima)
- `DotNetEnv` - Gestione delle variabili d'ambiente

**Configurazione dell'Ambiente (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Stack Tecnico

**Tecnologie Principali:**
- Microsoft Agent Framework (.NET)
- Integrazione API Modelli GitHub
- Modelli compatibili con OpenAI
- Configurazione basata su ambiente con DotNetEnv

**Capacità dell'Agente:**
- Comprensione e generazione del linguaggio naturale
- Chiamata di funzioni e utilizzo di strumenti con attributi C#
- Risposte contestuali con thread di conversazione
- Architettura estensibile con modelli di iniezione delle dipendenze

## 📚 Confronto tra Framework

Questo esempio dimostra l'approccio del Microsoft Agent Framework in .NET rispetto ad altre piattaforme:

| Caratteristica | Framework Agente .NET | Equivalenti in Python |
|----------------|------------------------|-----------------------|
| **Sicurezza dei Tipi** | Tipizzazione forte con C# | Tipizzazione dinamica |
| **Integrazione** | Ecosistema nativo .NET | Compatibilità variabile |
| **Prestazioni** | Prestazioni del codice compilato | Esecuzione interpretata |
| **Pronto per l'Impresa** | Progettato per app .NET di produzione | Varia in base al framework |
| **Strumenti** | Integrazione con Visual Studio | Dipendente dall'IDE |

## 🚀 Iniziare

Segui le sezioni seguenti per costruire il tuo primo agente base in .NET e comprendere i concetti agentici fondamentali!

## 📦 Installazione e Configurazione

Questo esempio è disponibile come un'applicazione eseguibile .NET Single File. Consulta il file `02-dotnet-agent-framework.cs` allegato per l'implementazione completa.

Per eseguire questo esempio:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Oppure utilizzando la CLI di dotnet:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Analisi del Codice

L'implementazione completa include:

### 1. Dipendenze dei Pacchetti

```csharp
// Core AI abstraction layer for .NET applications
#r "nuget: Microsoft.Extensions.AI, 9.9.1"

// Microsoft Agent Framework OpenAI integration
#r "nuget: Microsoft.Agents.AI.OpenAI, 1.0.0-preview.251001.3"

// Core Microsoft Agent Framework library
#r "nuget: Microsoft.Agents.AI, 1.0.0-preview.251001.3"

// Environment variable management
#r "nuget: DotNetEnv, 3.1.1"
```

### 2. Importazioni Essenziali

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Configurazione dell'Ambiente

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Definizione delle Funzioni Strumento

```csharp
// Random destination generator tool
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
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
    
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}
```

### 5. Configurazione e Impostazione del Client

```csharp
// Extract environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? 
    throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? 
    throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI client for GitHub Models
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI client
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);
```

### 6. Configurazione dell'Agente

```csharp
const string AGENT_NAME = "TravelAgent";

const string AGENT_INSTRUCTIONS = @"You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
""Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?""

Always prioritize user preferences. If they mention a specific destination like ""Bali"" or ""Paris,"" focus your planning on that location rather than suggesting alternatives.
";
```

### 7. Inizializzazione dell'Agente

```csharp
// Create AI agent with travel planning capabilities
AIAgent agent = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions)
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create((Func<string>)GetRandomDestination)]
    );
```

### 8. Gestione della Conversazione

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Punti Chiave

1. **Architettura degli Agenti**: Il Microsoft Agent Framework offre un approccio pulito e tipizzato per costruire agenti AI in .NET
2. **Integrazione degli Strumenti**: Le funzioni decorate con attributi `[Description]` diventano strumenti disponibili per l'agente
3. **Contesto della Conversazione**: La gestione dei thread consente conversazioni multi-turno con piena consapevolezza del contesto
4. **Gestione della Configurazione**: Le variabili d'ambiente e la gestione sicura delle credenziali seguono le best practice di .NET
5. **Compatibilità OpenAI**: L'integrazione con i Modelli GitHub funziona senza problemi attraverso API compatibili con OpenAI

## 🔗 Risorse Aggiuntive

- [Documentazione Microsoft Agent Framework](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [Marketplace Modelli GitHub](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [App Singole .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.