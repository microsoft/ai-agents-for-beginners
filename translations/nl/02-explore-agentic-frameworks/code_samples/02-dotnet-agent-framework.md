<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:37:09+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "nl"
}
-->
# 🔍 Verkennen van Agentic Frameworks - Basisagent (.NET)

## 📋 Leerdoelen

Dit notebook verkent de fundamentele concepten van het Microsoft Agent Framework via een basisimplementatie van een agent in .NET. Je leert de kernpatronen van agenten en begrijpt hoe intelligente agenten werken achter de schermen met behulp van C# en het .NET-ecosysteem.

**Wat je zult ontdekken:**
- 🏗️ **Agentarchitectuur**: Begrip van de basisstructuur van AI-agenten in .NET
- 🛠️ **Toolintegratie**: Hoe agenten externe functies gebruiken om hun mogelijkheden uit te breiden  
- 💬 **Gespreksstroom**: Beheer van meerstapsgesprekken en context met threadbeheer
- 🔧 **Configuratiepatronen**: Best practices voor het instellen en beheren van agenten in .NET

## 🎯 Belangrijke Concepten

### Principes van het Agentic Framework
- **Autonomie**: Hoe agenten zelfstandig beslissingen nemen met behulp van .NET AI-abstracties
- **Reactiviteit**: Reageren op veranderingen in de omgeving en gebruikersinvoer
- **Proactiviteit**: Initiatief nemen op basis van doelen en context
- **Sociale vaardigheid**: Interactie via natuurlijke taal met gespreksthreads

### Technische Componenten
- **AIAgent**: Kernbeheer van agenten en gespreksmanagement (.NET)
- **Toolfuncties**: Uitbreiden van agentmogelijkheden met C#-methoden en attributen
- **OpenAI-integratie**: Gebruik van taalmodellen via gestandaardiseerde .NET-API's
- **Omgevingsbeheer**: Veilige configuratie en beheer van referenties met DotNetEnv

## ⚙️ Vereisten & Installatie

**Benodigde afhankelijkheden:**
- .NET 9.0 SDK of hoger
- Visual Studio 2022 of VS Code met C#-extensie

**NuGet-pakketten:**
- `Microsoft.Extensions.AI` - Kern AI-abstracties
- `Microsoft.Extensions.AI.OpenAI` - OpenAI-integratie (preview)
- `DotNetEnv` - Beheer van omgevingsvariabelen

**Omgevingsconfiguratie (.env-bestand):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Technische Stack

**Kerntechnologieën:**
- Microsoft Agent Framework (.NET)
- GitHub Models API-integratie
- OpenAI-compatibele clientpatronen
- Configuratie op basis van omgeving met DotNetEnv

**Agentmogelijkheden:**
- Begrip en generatie van natuurlijke taal
- Functieaanroepen en toolgebruik met C#-attributen
- Contextbewuste reacties met gespreksthreads
- Uitbreidbare architectuur met dependency injection-patronen

## 📚 Frameworkvergelijking

Dit voorbeeld demonstreert de aanpak van het Microsoft Agent Framework in .NET vergeleken met andere platforms:

| Functie | .NET Agent Framework | Python Equivalenten |
|---------|---------------------|-------------------|
| **Typeveiligheid** | Sterke typing met C# | Dynamische typing |
| **Integratie** | Native .NET-ecosysteem | Gevarieerde compatibiliteit |
| **Prestaties** | Gecompileerde codeprestaties | Interpreteruitvoering |
| **Enterprise Ready** | Ontworpen voor productie .NET-apps | Verschilt per framework |
| **Tools** | Integratie met Visual Studio | Afhankelijk van IDE |

## 🚀 Aan de slag

Volg de onderstaande stappen om je eerste basisagent in .NET te bouwen en fundamentele agentconcepten te begrijpen!

## 📦 Installatie en Setup

Dit voorbeeld is beschikbaar als een uitvoerbare .NET Single File App. Zie het bijbehorende bestand `02-dotnet-agent-framework.cs` voor de volledige implementatie.

Om dit voorbeeld uit te voeren:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Of gebruik de dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Code Uitleg

De volledige implementatie omvat:

### 1. Pakketafhankelijkheden

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

### 2. Essentiële Imports

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Omgevingsconfiguratie

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Definitie van Toolfuncties

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

### 5. Configuratie en Client Setup

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

### 6. Agentconfiguratie

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

### 7. Initialisatie van de Agent

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

### 8. Gespreksbeheer

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Belangrijke Leerpunten

1. **Agentarchitectuur**: Het Microsoft Agent Framework biedt een duidelijke, type-veilige aanpak voor het bouwen van AI-agenten in .NET
2. **Toolintegratie**: Functies met `[Description]`-attributen worden beschikbare tools voor de agent
3. **Gesprekscontext**: Threadbeheer maakt meerstapsgesprekken mogelijk met volledige contextbewustzijn
4. **Configuratiebeheer**: Omgevingsvariabelen en veilig referentiebeheer volgen de beste praktijken van .NET
5. **OpenAI-compatibiliteit**: GitHub Models-integratie werkt naadloos via OpenAI-compatibele API's

## 🔗 Aanvullende Bronnen

- [Microsoft Agent Framework Documentatie](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.