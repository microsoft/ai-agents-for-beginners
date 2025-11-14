<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:36:40+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "no"
}
-->
# 🔍 Utforsking av Agentiske Rammeverk - Grunnleggende Agent (.NET)

## 📋 Læringsmål

Denne notatboken utforsker de grunnleggende konseptene i Microsoft Agent Framework gjennom en enkel agentimplementering i .NET. Du vil lære kjerneprinsipper for agentisk design og forstå hvordan intelligente agenter fungerer i praksis ved bruk av C# og .NET-økosystemet.

**Hva du vil oppdage:**
- 🏗️ **Agentarkitektur**: Forstå den grunnleggende strukturen til AI-agenter i .NET
- 🛠️ **Verktøyintegrasjon**: Hvordan agenter bruker eksterne funksjoner for å utvide funksjonalitet  
- 💬 **Samtaleflyt**: Administrere samtaler med flere vendinger og kontekst med trådbehandling
- 🔧 **Konfigurasjonsmønstre**: Beste praksis for oppsett og administrasjon av agenter i .NET

## 🎯 Nøkkelkonsepter som dekkes

### Prinsipper for Agentisk Rammeverk
- **Autonomi**: Hvordan agenter tar selvstendige beslutninger ved bruk av .NET AI-abstraksjoner
- **Reaktivitet**: Reagere på miljøendringer og brukerinput
- **Proaktivitet**: Ta initiativ basert på mål og kontekst
- **Sosial evne**: Interagere gjennom naturlig språk med samtaletråder

### Tekniske komponenter
- **AIAgent**: Kjerneagent for orkestrering og samtaleadministrasjon (.NET)
- **Verktøyfunksjoner**: Utvide agentens funksjonalitet med C#-metoder og attributter
- **OpenAI-integrasjon**: Utnytte språkmodeller gjennom standardiserte .NET-APIer
- **Miljøadministrasjon**: Sikker konfigurasjon og håndtering av legitimasjon med DotNetEnv

## ⚙️ Forutsetninger og oppsett

**Nødvendige avhengigheter:**
- .NET 9.0 SDK eller nyere
- Visual Studio 2022 eller VS Code med C#-utvidelse

**NuGet-pakker:**
- `Microsoft.Extensions.AI` - Kjerne AI-abstraksjoner
- `Microsoft.Extensions.AI.OpenAI` - OpenAI-integrasjon (forhåndsvisning)
- `DotNetEnv` - Administrasjon av miljøvariabler

**Miljøkonfigurasjon (.env-fil):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Teknisk stabel

**Kjerneteknologier:**
- Microsoft Agent Framework (.NET)
- GitHub Models API-integrasjon
- OpenAI-kompatible klientmønstre
- Miljøbasert konfigurasjon med DotNetEnv

**Agentens funksjoner:**
- Forståelse og generering av naturlig språk
- Funksjonskalling og verktøybruk med C#-attributter
- Kontekstbevisste svar med samtaletråder
- Utvidbar arkitektur med avhengighetsinjeksjonsmønstre

## 📚 Rammeverkssammenligning

Dette eksemplet demonstrerer tilnærmingen til Microsoft Agent Framework i .NET sammenlignet med andre plattformer:

| Funksjon | .NET Agent Framework | Python-ekvivalenter |
|----------|-----------------------|---------------------|
| **Type-sikkerhet** | Sterk typisering med C# | Dynamisk typisering |
| **Integrasjon** | Naturlig .NET-økosystem | Variert kompatibilitet |
| **Ytelse** | Kompilert kodeytelse | Tolket utførelse |
| **Klar for bedrifter** | Bygget for produksjonsapplikasjoner i .NET | Varierer etter rammeverk |
| **Verktøy** | Integrasjon med Visual Studio | Avhengig av IDE |

## 🚀 Komme i gang

Følg cellene nedenfor for å bygge din første grunnleggende agent i .NET og forstå grunnleggende agentiske konsepter!

## 📦 Installasjon og oppsett

Dette eksemplet er tilgjengelig som en kjørbar .NET Single File App. Se den medfølgende `02-dotnet-agent-framework.cs`-filen for fullstendig implementering.

For å kjøre dette eksemplet:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Eller ved bruk av dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Gjennomgang av kode

Den fullstendige implementeringen inkluderer:

### 1. Pakkeavhengigheter

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

### 2. Essensielle imports

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Miljøkonfigurasjon

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Definisjon av verktøyfunksjoner

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

### 5. Konfigurasjon og klientoppsett

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

### 6. Agentkonfigurasjon

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

### 7. Initialisering av agent

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

### 8. Administrasjon av samtaler

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Viktige lærdommer

1. **Agentarkitektur**: Microsoft Agent Framework gir en ren, type-sikker tilnærming til å bygge AI-agenter i .NET
2. **Verktøyintegrasjon**: Funksjoner dekorert med `[Description]`-attributter blir tilgjengelige verktøy for agenten
3. **Samtalekontekst**: Trådbehandling muliggjør samtaler med flere vendinger og full kontekstbevissthet
4. **Konfigurasjonsadministrasjon**: Miljøvariabler og sikker håndtering av legitimasjon følger beste praksis i .NET
5. **OpenAI-kompatibilitet**: GitHub Models-integrasjon fungerer sømløst gjennom OpenAI-kompatible APIer

## 🔗 Tilleggsressurser

- [Microsoft Agent Framework Dokumentasjon](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.