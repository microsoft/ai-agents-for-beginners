<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:39:26+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "sk"
}
-->
# 🔍 Preskúmanie Agentických Rámcov - Základný Agent (.NET)

## 📋 Ciele učenia

Tento notebook skúma základné koncepty Microsoft Agent Framework prostredníctvom implementácie základného agenta v .NET. Naučíte sa kľúčové agentické vzory a pochopíte, ako inteligentní agenti fungujú v zákulisí pomocou C# a ekosystému .NET.

**Čo objavíte:**
- 🏗️ **Architektúra agenta**: Pochopenie základnej štruktúry AI agentov v .NET
- 🛠️ **Integrácia nástrojov**: Ako agenti využívajú externé funkcie na rozšírenie schopností  
- 💬 **Tok konverzácie**: Správa viacnásobných konverzácií a kontextu pomocou správy vlákien
- 🔧 **Konfiguračné vzory**: Najlepšie postupy pre nastavenie a správu agenta v .NET

## 🎯 Kľúčové pokryté koncepty

### Princípy agentického rámca
- **Autonómia**: Ako agenti robia nezávislé rozhodnutia pomocou .NET AI abstrakcií
- **Reaktivita**: Reagovanie na zmeny prostredia a vstupy používateľov
- **Proaktivita**: Iniciovanie akcií na základe cieľov a kontextu
- **Sociálna schopnosť**: Interakcia prostredníctvom prirodzeného jazyka s konverzačnými vláknami

### Technické komponenty
- **AIAgent**: Jadro orchestrácie agenta a správy konverzácií (.NET)
- **Funkcie nástrojov**: Rozšírenie schopností agenta pomocou C# metód a atribútov
- **Integrácia OpenAI**: Využitie jazykových modelov prostredníctvom štandardizovaných .NET API
- **Správa prostredia**: Bezpečná konfigurácia a správa poverení pomocou DotNetEnv

## ⚙️ Predpoklady a nastavenie

**Požadované závislosti:**
- .NET 9.0 SDK alebo vyšší
- Visual Studio 2022 alebo VS Code s rozšírením pre C#

**NuGet balíčky:**
- `Microsoft.Extensions.AI` - Základné AI abstrakcie
- `Microsoft.Extensions.AI.OpenAI` - Integrácia OpenAI (preview)
- `DotNetEnv` - Správa environmentálnych premenných

**Konfigurácia prostredia (.env súbor):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Technologický stack

**Hlavné technológie:**
- Microsoft Agent Framework (.NET)
- Integrácia GitHub Models API
- OpenAI-kompatibilné vzory klientov
- Konfigurácia na základe prostredia s DotNetEnv

**Schopnosti agenta:**
- Porozumenie a generovanie prirodzeného jazyka
- Volanie funkcií a používanie nástrojov s C# atribútmi
- Odozvy s vedomím kontextu pomocou konverzačných vlákien
- Rozšíriteľná architektúra s vzormi závislostnej injekcie

## 📚 Porovnanie rámcov

Tento príklad demonštruje prístup Microsoft Agent Framework v .NET v porovnaní s inými platformami:

| Funkcia | .NET Agent Framework | Python Ekvivalenty |
|---------|---------------------|-------------------|
| **Typová bezpečnosť** | Silné typovanie s C# | Dynamické typovanie |
| **Integrácia** | Natívny .NET ekosystém | Rôzna kompatibilita |
| **Výkon** | Výkon kompilovaného kódu | Interpretované vykonávanie |
| **Pripravenosť pre podniky** | Navrhnuté pre produkčné .NET aplikácie | Líši sa podľa rámca |
| **Nástroje** | Integrácia s Visual Studio | Závislé na IDE |

## 🚀 Začíname

Postupujte podľa nasledujúcich krokov na vytvorenie svojho prvého základného agenta v .NET a pochopenie základných agentických konceptov!

## 📦 Inštalácia a nastavenie

Tento príklad je dostupný ako spustiteľná .NET Single File App. Kompletnú implementáciu nájdete v priloženom súbore `02-dotnet-agent-framework.cs`.

Na spustenie tohto príkladu:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Alebo pomocou dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Prehľad kódu

Kompletná implementácia zahŕňa:

### 1. Závislosti balíčkov

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

### 2. Základné importy

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Konfigurácia prostredia

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Definícia funkcií nástrojov

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

### 5. Nastavenie a konfigurácia klienta

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

### 6. Konfigurácia agenta

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

### 7. Inicializácia agenta

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

### 8. Správa konverzácií

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Kľúčové poznatky

1. **Architektúra agenta**: Microsoft Agent Framework poskytuje čistý, typovo bezpečný prístup k vytváraniu AI agentov v .NET
2. **Integrácia nástrojov**: Funkcie označené atribútmi `[Description]` sa stávajú dostupnými nástrojmi pre agenta
3. **Kontext konverzácie**: Správa vlákien umožňuje viacnásobné konverzácie s plným vedomím kontextu
4. **Správa konfigurácie**: Environmentálne premenné a bezpečné spracovanie poverení nasledujú najlepšie postupy .NET
5. **Kompatibilita s OpenAI**: Integrácia GitHub Models funguje bezproblémovo prostredníctvom OpenAI-kompatibilných API

## 🔗 Ďalšie zdroje

- [Microsoft Agent Framework Dokumentácia](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.