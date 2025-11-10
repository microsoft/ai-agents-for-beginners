<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:39:13+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "cs"
}
-->
# 🔍 Zkoumání agentních rámců - Základní agent (.NET)

## 📋 Cíle učení

Tento notebook se zabývá základními koncepty Microsoft Agent Framework prostřednictvím implementace základního agenta v .NET. Naučíte se klíčové agentní vzory a pochopíte, jak inteligentní agenti fungují pod povrchem pomocí C# a ekosystému .NET.

**Co objevíte:**
- 🏗️ **Architektura agenta**: Porozumění základní struktuře AI agentů v .NET
- 🛠️ **Integrace nástrojů**: Jak agenti využívají externí funkce k rozšíření schopností  
- 💬 **Tok konverzace**: Správa vícenásobných konverzací a kontextu pomocí správy vláken
- 🔧 **Konfigurační vzory**: Nejlepší postupy pro nastavení a správu agentů v .NET

## 🎯 Klíčové koncepty

### Principy agentního rámce
- **Autonomie**: Jak agenti činí nezávislá rozhodnutí pomocí abstrakcí AI v .NET
- **Reaktivita**: Reakce na změny prostředí a vstupy uživatelů
- **Proaktivita**: Iniciativa na základě cílů a kontextu
- **Sociální schopnost**: Interakce prostřednictvím přirozeného jazyka s konverzačními vlákny

### Technické komponenty
- **AIAgent**: Orchestrace agenta a správa konverzací (.NET)
- **Funkce nástrojů**: Rozšíření schopností agenta pomocí metod a atributů v C#
- **Integrace OpenAI**: Využití jazykových modelů prostřednictvím standardizovaných API v .NET
- **Správa prostředí**: Bezpečná konfigurace a správa přihlašovacích údajů pomocí DotNetEnv

## ⚙️ Předpoklady a nastavení

**Požadované závislosti:**
- .NET 9.0 SDK nebo vyšší
- Visual Studio 2022 nebo VS Code s rozšířením pro C#

**NuGet balíčky:**
- `Microsoft.Extensions.AI` - Základní AI abstrakce
- `Microsoft.Extensions.AI.OpenAI` - Integrace OpenAI (preview)
- `DotNetEnv` - Správa proměnných prostředí

**Konfigurace prostředí (.env soubor):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Technologický stack

**Klíčové technologie:**
- Microsoft Agent Framework (.NET)
- Integrace GitHub Models API
- Klientské vzory kompatibilní s OpenAI
- Konfigurace založená na prostředí s DotNetEnv

**Schopnosti agenta:**
- Porozumění přirozenému jazyku a jeho generování
- Volání funkcí a používání nástrojů pomocí atributů v C#
- Odpovědi s vědomím kontextu díky konverzačním vláknům
- Rozšiřitelná architektura s vzory závislostí

## 📚 Porovnání rámců

Tento příklad demonstruje přístup Microsoft Agent Framework v .NET ve srovnání s jinými platformami:

| Funkce | .NET Agent Framework | Python ekvivalenty |
|--------|-----------------------|--------------------|
| **Typová bezpečnost** | Silné typování s C# | Dynamické typování |
| **Integrace** | Nativní ekosystém .NET | Různá kompatibilita |
| **Výkon** | Výkon kompilovaného kódu | Interpretovaný výkon |
| **Připravenost pro podniky** | Navrženo pro produkční .NET aplikace | Liší se podle rámce |
| **Nástroje** | Integrace s Visual Studio | Závislé na IDE |

## 🚀 Začínáme

Postupujte podle níže uvedených kroků a vytvořte svého prvního základního agenta v .NET a pochopte základní agentní koncepty!

## 📦 Instalace a nastavení

Tento příklad je dostupný jako spustitelná .NET Single File App. Kompletní implementaci najdete v přiloženém souboru `02-dotnet-agent-framework.cs`.

Pro spuštění tohoto příkladu:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Nebo pomocí dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Prohlídka kódu

Kompletní implementace zahrnuje:

### 1. Závislosti balíčků

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

### 2. Základní importy

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Konfigurace prostředí

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Definice funkcí nástrojů

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

### 5. Nastavení konfigurace a klienta

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

### 6. Konfigurace agenta

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

### 7. Inicializace agenta

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

### 8. Správa konverzací

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Klíčové poznatky

1. **Architektura agenta**: Microsoft Agent Framework poskytuje čistý, typově bezpečný přístup k vytváření AI agentů v .NET
2. **Integrace nástrojů**: Funkce označené atributem `[Description]` se stávají dostupnými nástroji pro agenta
3. **Kontext konverzace**: Správa vláken umožňuje vícenásobné konverzace s plným vědomím kontextu
4. **Správa konfigurace**: Proměnné prostředí a bezpečné nakládání s přihlašovacími údaji odpovídají nejlepším postupům v .NET
5. **Kompatibilita s OpenAI**: Integrace GitHub Models funguje bez problémů prostřednictvím API kompatibilních s OpenAI

## 🔗 Další zdroje

- [Dokumentace Microsoft Agent Framework](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.