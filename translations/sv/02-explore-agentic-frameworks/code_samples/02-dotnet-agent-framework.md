<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:36:15+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "sv"
}
-->
# 🔍 Utforska Agentiska Ramverk - Grundläggande Agent (.NET)

## 📋 Lärandemål

Denna notebook utforskar de grundläggande koncepten i Microsoft Agent Framework genom en grundläggande agentimplementering i .NET. Du kommer att lära dig kärnmönster för agentisk design och förstå hur intelligenta agenter fungerar bakom kulisserna med hjälp av C# och .NET-ekosystemet.

**Vad du kommer att upptäcka:**
- 🏗️ **Agentarkitektur**: Förstå den grundläggande strukturen för AI-agenter i .NET
- 🛠️ **Verktygsintegration**: Hur agenter använder externa funktioner för att utöka kapabiliteter  
- 💬 **Konversationsflöde**: Hantera flervändskonversationer och kontext med trådhantering
- 🔧 **Konfigurationsmönster**: Bästa praxis för agentinställning och hantering i .NET

## 🎯 Viktiga Koncept

### Principer för Agentiska Ramverk
- **Autonomi**: Hur agenter fattar självständiga beslut med hjälp av .NET AI-abstraktioner
- **Reaktivitet**: Reagera på miljöförändringar och användarinmatningar
- **Proaktivitet**: Ta initiativ baserat på mål och kontext
- **Social Förmåga**: Interagera genom naturligt språk med konversationstrådar

### Tekniska Komponenter
- **AIAgent**: Kärnan i agentens orkestrering och konversationshantering (.NET)
- **Verktygsfunktioner**: Utöka agentens kapabiliteter med C#-metoder och attribut
- **OpenAI Integration**: Utnyttja språkmodeller genom standardiserade .NET API:er
- **Miljöhantering**: Säker konfiguration och hantering av autentiseringsuppgifter med DotNetEnv

## ⚙️ Förutsättningar & Installation

**Nödvändiga beroenden:**
- .NET 9.0 SDK eller högre
- Visual Studio 2022 eller VS Code med C#-tillägg

**NuGet-paket:**
- `Microsoft.Extensions.AI` - Kärn-AI-abstraktioner
- `Microsoft.Extensions.AI.OpenAI` - OpenAI-integration (förhandsvisning)
- `DotNetEnv` - Hantering av miljövariabler

**Miljökonfiguration (.env-fil):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Teknisk Stack

**Kärnteknologier:**
- Microsoft Agent Framework (.NET)
- GitHub Models API-integration
- OpenAI-kompatibla klientmönster
- Miljöbaserad konfiguration med DotNetEnv

**Agentens Kapabiliteter:**
- Förståelse och generering av naturligt språk
- Funktionsanrop och verktygsanvändning med C#-attribut
- Kontextmedvetna svar med konversationstrådar
- Utbyggbar arkitektur med beroendeinjektionsmönster

## 📚 Jämförelse av Ramverk

Detta exempel demonstrerar Microsoft Agent Framework-ansatsen i .NET jämfört med andra plattformar:

| Funktion | .NET Agent Framework | Python-motsvarigheter |
|----------|-----------------------|-----------------------|
| **Typ Säkerhet** | Starkt typat med C# | Dynamisk typning |
| **Integration** | Inbyggt .NET-ekosystem | Varierande kompatibilitet |
| **Prestanda** | Kompilerad kodprestanda | Tolkat utförande |
| **Färdigt för Företag** | Byggt för produktionsapplikationer i .NET | Varierar beroende på ramverk |
| **Verktyg** | Integration med Visual Studio | Beroende av IDE |

## 🚀 Kom igång

Följ cellerna nedan för att bygga din första grundläggande agent i .NET och förstå grundläggande agentiska koncept!

## 📦 Installation och Inställning

Detta exempel är tillgängligt som en körbar .NET Single File App. Se den medföljande filen `02-dotnet-agent-framework.cs` för den kompletta implementeringen.

För att köra detta exempel:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Eller med hjälp av dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Kodgenomgång

Den kompletta implementeringen inkluderar:

### 1. Paketberoenden

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

### 2. Grundläggande Importer

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Miljökonfiguration

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Definition av Verktygsfunktioner

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

### 5. Konfiguration och Klientinställning

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

### 8. Hantering av Konversationer

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Viktiga Lärdomar

1. **Agentarkitektur**: Microsoft Agent Framework erbjuder ett rent, typ-säkert sätt att bygga AI-agenter i .NET
2. **Verktygsintegration**: Funktioner dekorerade med `[Description]`-attribut blir tillgängliga verktyg för agenten
3. **Konversationskontext**: Trådhantering möjliggör flervändskonversationer med full kontextmedvetenhet
4. **Konfigurationshantering**: Miljövariabler och säker hantering av autentiseringsuppgifter följer bästa praxis i .NET
5. **OpenAI-kompatibilitet**: GitHub Models-integration fungerar sömlöst genom OpenAI-kompatibla API:er

## 🔗 Ytterligare Resurser

- [Microsoft Agent Framework Dokumentation](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.