<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:36:28+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "da"
}
-->
# 🔍 Udforskning af Agentiske Rammer - Grundlæggende Agent (.NET)

## 📋 Læringsmål

Denne notebook udforsker de grundlæggende koncepter i Microsoft Agent Framework gennem en simpel agentimplementering i .NET. Du vil lære kerneprincipperne for agentiske mønstre og forstå, hvordan intelligente agenter fungerer bag kulisserne ved hjælp af C# og .NET-økosystemet.

**Hvad du vil opdage:**
- 🏗️ **Agentarkitektur**: Forstå den grundlæggende struktur af AI-agenter i .NET
- 🛠️ **Værktøjsintegration**: Hvordan agenter bruger eksterne funktioner til at udvide kapabiliteter  
- 💬 **Samtaleflow**: Håndtering af samtaler med flere omgange og kontekst med trådstyring
- 🔧 **Konfigurationsmønstre**: Bedste praksis for opsætning og styring af agenter i .NET

## 🎯 Centrale Koncepter

### Principper for Agentiske Rammer
- **Autonomi**: Hvordan agenter træffer selvstændige beslutninger ved hjælp af .NET AI-abstraktioner
- **Reaktivitet**: Reagerer på miljøændringer og brugerinput
- **Proaktivitet**: Tager initiativ baseret på mål og kontekst
- **Social Evne**: Interagerer gennem naturligt sprog med samtaletråde

### Tekniske Komponenter
- **AIAgent**: Kerneagent orkestrering og samtalestyring (.NET)
- **Værktøjsfunktioner**: Udvidelse af agentens kapabiliteter med C#-metoder og attributter
- **OpenAI Integration**: Udnyttelse af sprogmodeller gennem standardiserede .NET API'er
- **Miljøstyring**: Sikker konfiguration og håndtering af legitimationsoplysninger med DotNetEnv

## ⚙️ Forudsætninger og Opsætning

**Nødvendige Afhængigheder:**
- .NET 9.0 SDK eller nyere
- Visual Studio 2022 eller VS Code med C#-udvidelse

**NuGet Pakker:**
- `Microsoft.Extensions.AI` - Kerne AI-abstraktioner
- `Microsoft.Extensions.AI.OpenAI` - OpenAI integration (preview)
- `DotNetEnv` - Håndtering af miljøvariabler

**Miljøkonfiguration (.env-fil):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Teknisk Stak

**Kerneteknologier:**
- Microsoft Agent Framework (.NET)
- GitHub Models API integration
- OpenAI-kompatible klientmønstre
- Miljøbaseret konfiguration med DotNetEnv

**Agentens Kapabiliteter:**
- Forståelse og generering af naturligt sprog
- Funktionskald og værktøjsbrug med C#-attributter
- Kontekstbevidste svar med samtaletråde
- Udvidelig arkitektur med afhængighedsinjektionsmønstre

## 📚 Sammenligning af Rammer

Dette eksempel demonstrerer Microsoft Agent Framework-tilgangen i .NET sammenlignet med andre platforme:

| Funktion | .NET Agent Framework | Python Ækvivalenter |
|----------|-----------------------|---------------------|
| **Type Sikkerhed** | Stærk typning med C# | Dynamisk typning |
| **Integration** | Indbygget .NET-økosystem | Varierende kompatibilitet |
| **Ydeevne** | Kompileret kodeydelse | Fortolket eksekvering |
| **Enterprise Klar** | Bygget til produktions .NET-apps | Varierer efter ramme |
| **Værktøjer** | Visual Studio integration | IDE-afhængig |

## 🚀 Kom i Gang

Følg cellerne nedenfor for at bygge din første grundlæggende agent i .NET og forstå fundamentale agentiske koncepter!

## 📦 Installation og Opsætning

Dette eksempel er tilgængeligt som en kørbar .NET Single File App. Se den medfølgende `02-dotnet-agent-framework.cs`-fil for den komplette implementering.

For at køre dette eksempel:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Eller ved hjælp af dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Gennemgang af Kode

Den komplette implementering inkluderer:

### 1. Pakkeafhængigheder

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

### 2. Nødvendige Imports

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Miljøkonfiguration

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Definition af Værktøjsfunktion

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

### 5. Konfiguration og Klientopsætning

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

### 6. Agentkonfiguration

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

### 7. Agentinitialisering

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

### 8. Samtalestyring

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Vigtige Læringspunkter

1. **Agentarkitektur**: Microsoft Agent Framework giver en ren, type-sikker tilgang til at bygge AI-agenter i .NET
2. **Værktøjsintegration**: Funktioner dekoreret med `[Description]`-attributter bliver tilgængelige værktøjer for agenten
3. **Samtalekontekst**: Trådstyring muliggør samtaler med flere omgange med fuld kontekstbevidsthed
4. **Konfigurationsstyring**: Miljøvariabler og sikker håndtering af legitimationsoplysninger følger .NET bedste praksis
5. **OpenAI-kompatibilitet**: GitHub Models integration fungerer problemfrit gennem OpenAI-kompatible API'er

## 🔗 Yderligere Ressourcer

- [Microsoft Agent Framework Dokumentation](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.