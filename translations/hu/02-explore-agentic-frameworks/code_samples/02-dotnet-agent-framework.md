<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:38:57+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "hu"
}
-->
# 🔍 Az Agentikus Keretrendszerek Felfedezése - Alapvető Agent (.NET)

## 📋 Tanulási Célok

Ez a jegyzetfüzet bemutatja a Microsoft Agent Keretrendszer alapvető fogalmait egy egyszerű agent implementáción keresztül .NET-ben. Megismerheted az alapvető agentikus mintákat, és megértheted, hogyan működnek az intelligens agentek a háttérben C# és a .NET ökoszisztéma segítségével.

**Amit felfedezhetsz:**
- 🏗️ **Agent Architektúra**: Az AI agentek alapvető felépítésének megértése .NET-ben
- 🛠️ **Eszközintegráció**: Hogyan használják az agentek a külső funkciókat képességeik bővítésére  
- 💬 **Beszélgetési Folyamat**: Többfordulós beszélgetések és kontextus kezelése szálkezeléssel
- 🔧 **Konfigurációs Minták**: Legjobb gyakorlatok az agent beállításához és kezeléséhez .NET-ben

## 🎯 Főbb Témakörök

### Agentikus Keretrendszer Alapelvei
- **Autonómia**: Hogyan hoznak az agentek önálló döntéseket a .NET AI absztrakciók segítségével
- **Reaktivitás**: Környezeti változásokra és felhasználói bemenetekre való reagálás
- **Proaktivitás**: Kezdeményezés célok és kontextus alapján
- **Társas Képesség**: Természetes nyelvű interakció beszélgetési szálakon keresztül

### Technikai Összetevők
- **AIAgent**: Az agentek alapvető működtetése és beszélgetéskezelés (.NET)
- **Eszközfunkciók**: Az agent képességeinek bővítése C# metódusokkal és attribútumokkal
- **OpenAI Integráció**: Nyelvi modellek használata szabványosított .NET API-kon keresztül
- **Környezetkezelés**: Biztonságos konfiguráció és hitelesítő adatok kezelése DotNetEnv segítségével

## ⚙️ Előfeltételek és Beállítás

**Szükséges függőségek:**
- .NET 9.0 SDK vagy újabb
- Visual Studio 2022 vagy VS Code C# bővítménnyel

**NuGet Csomagok:**
- `Microsoft.Extensions.AI` - Alapvető AI absztrakciók
- `Microsoft.Extensions.AI.OpenAI` - OpenAI integráció (előzetes)
- `DotNetEnv` - Környezeti változók kezelése

**Környezeti Konfiguráció (.env fájl):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Technikai Verem

**Alapvető Technológiák:**
- Microsoft Agent Keretrendszer (.NET)
- GitHub Models API integráció
- OpenAI-kompatibilis kliens minták
- Környezetalapú konfiguráció DotNetEnv segítségével

**Agent Képességek:**
- Természetes nyelv megértése és generálása
- Funkcióhívás és eszközhasználat C# attribútumokkal
- Kontextusérzékeny válaszok beszélgetési szálakkal
- Bővíthető architektúra függőséginjektálási mintákkal

## 📚 Keretrendszerek Összehasonlítása

Ez a példa bemutatja a Microsoft Agent Keretrendszer megközelítését .NET-ben más platformokhoz képest:

| Funkció | .NET Agent Keretrendszer | Python Egyenértékek |
|---------|--------------------------|---------------------|
| **Típusbiztonság** | Erős típusosság C#-ban | Dinamikus típusosság |
| **Integráció** | Natív .NET ökoszisztéma | Változó kompatibilitás |
| **Teljesítmény** | Fordított kód teljesítmény | Értelmezett végrehajtás |
| **Vállalati Felkészültség** | Kifejezetten .NET alkalmazásokhoz | Keretrendszertől függ |
| **Eszközök** | Visual Studio integráció | IDE-függő |

## 🚀 Első Lépések

Kövesd az alábbi lépéseket, hogy elkészítsd az első alapvető agentedet .NET-ben, és megértsd az alapvető agentikus fogalmakat!

## 📦 Telepítés és Beállítás

Ez a példa futtatható .NET Egyszerű Fájl Alkalmazásként érhető el. A teljes implementációt lásd a mellékelt `02-dotnet-agent-framework.cs` fájlban.

A példa futtatásához:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Vagy a dotnet CLI használatával:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Kódbemutató

A teljes implementáció tartalmazza:

### 1. Csomagfüggőségek

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

### 2. Alapvető Importok

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Környezeti Konfiguráció

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Eszközfunkció Definíció

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

### 5. Konfiguráció és Kliens Beállítás

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

### 6. Agent Konfiguráció

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

### 7. Agent Inicializálás

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

### 8. Beszélgetéskezelés

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Főbb Tanulságok

1. **Agent Architektúra**: A Microsoft Agent Keretrendszer tiszta, típusbiztos megközelítést kínál AI agentek építéséhez .NET-ben
2. **Eszközintegráció**: `[Description]` attribútummal ellátott funkciók elérhető eszközökké válnak az agent számára
3. **Beszélgetési Kontextus**: A szálkezelés lehetővé teszi a többfordulós beszélgetéseket teljes kontextusérzékenységgel
4. **Konfigurációkezelés**: A környezeti változók és a biztonságos hitelesítő adatok kezelése követi a .NET legjobb gyakorlatait
5. **OpenAI Kompatibilitás**: A GitHub Models integráció zökkenőmentesen működik az OpenAI-kompatibilis API-kon keresztül

## 🔗 További Források

- [Microsoft Agent Keretrendszer Dokumentáció](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Egyszerű Fájl Alkalmazások](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.