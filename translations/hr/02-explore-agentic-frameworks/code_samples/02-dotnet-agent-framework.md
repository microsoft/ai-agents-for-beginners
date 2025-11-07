<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:40:20+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "hr"
}
-->
# 🔍 Istraživanje Agent Frameworka - Osnovni Agent (.NET)

## 📋 Ciljevi učenja

Ovaj notebook istražuje temeljne koncepte Microsoft Agent Frameworka kroz implementaciju osnovnog agenta u .NET-u. Naučit ćete osnovne obrasce agentičkog rada i razumjeti kako inteligentni agenti funkcioniraju "ispod haube" koristeći C# i .NET ekosustav.

**Što ćete otkriti:**
- 🏗️ **Arhitektura agenta**: Razumijevanje osnovne strukture AI agenata u .NET-u
- 🛠️ **Integracija alata**: Kako agenti koriste vanjske funkcije za proširenje mogućnosti  
- 💬 **Tijek razgovora**: Upravljanje višestrukim razgovorima i kontekstom uz upravljanje nitima
- 🔧 **Obrasci konfiguracije**: Najbolje prakse za postavljanje i upravljanje agentima u .NET-u

## 🎯 Ključni koncepti

### Principi Agent Frameworka
- **Autonomija**: Kako agenti donose neovisne odluke koristeći .NET AI apstrakcije
- **Reaktivnost**: Reagiranje na promjene u okruženju i korisničke unose
- **Proaktivnost**: Preuzimanje inicijative na temelju ciljeva i konteksta
- **Socijalna sposobnost**: Interakcija putem prirodnog jezika s nitima razgovora

### Tehničke komponente
- **AIAgent**: Orkestracija agenta i upravljanje razgovorima (.NET)
- **Funkcije alata**: Proširenje mogućnosti agenta pomoću C# metoda i atributa
- **OpenAI integracija**: Korištenje jezičnih modela putem standardiziranih .NET API-ja
- **Upravljanje okruženjem**: Sigurna konfiguracija i rukovanje vjerodajnicama pomoću DotNetEnv

## ⚙️ Preduvjeti i postavljanje

**Potrebne ovisnosti:**
- .NET 9.0 SDK ili noviji
- Visual Studio 2022 ili VS Code s C# ekstenzijom

**NuGet paketi:**
- `Microsoft.Extensions.AI` - Osnovne AI apstrakcije
- `Microsoft.Extensions.AI.OpenAI` - OpenAI integracija (preview)
- `DotNetEnv` - Upravljanje varijablama okruženja

**Konfiguracija okruženja (.env datoteka):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Tehnički stack

**Osnovne tehnologije:**
- Microsoft Agent Framework (.NET)
- Integracija GitHub Models API-ja
- OpenAI-kompatibilni klijentski obrasci
- Konfiguracija temeljena na okruženju s DotNetEnv

**Mogućnosti agenta:**
- Razumijevanje i generiranje prirodnog jezika
- Pozivanje funkcija i korištenje alata s C# atributima
- Odgovori svjesni konteksta uz niti razgovora
- Proširiva arhitektura s obrascima ubrizgavanja ovisnosti

## 📚 Usporedba frameworka

Ovaj primjer prikazuje pristup Microsoft Agent Frameworka u .NET-u u usporedbi s drugim platformama:

| Značajka | .NET Agent Framework | Python ekvivalenti |
|----------|-----------------------|--------------------|
| **Tipizacija** | Jaka tipizacija s C# | Dinamička tipizacija |
| **Integracija** | Izvorni .NET ekosustav | Različita kompatibilnost |
| **Performanse** | Performanse kompajliranog koda | Interpretirano izvršavanje |
| **Spremnost za poduzeća** | Dizajnirano za produkcijske .NET aplikacije | Varira ovisno o frameworku |
| **Alati** | Integracija s Visual Studiom | Ovisno o IDE-u |

## 🚀 Početak rada

Slijedite dolje navedene korake kako biste izgradili svoj prvi osnovni agent u .NET-u i razumjeli temeljne agentičke koncepte!

## 📦 Instalacija i postavljanje

Ovaj primjer dostupan je kao pokretljiva .NET aplikacija u jednoj datoteci. Pogledajte priloženu datoteku `02-dotnet-agent-framework.cs` za kompletnu implementaciju.

Za pokretanje ovog primjera:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Ili koristeći dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Pregled koda

Kompletna implementacija uključuje:

### 1. Ovisnosti paketa

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

### 2. Osnovni uvozi

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Konfiguracija okruženja

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Definicija funkcije alata

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

### 5. Postavljanje konfiguracije i klijenta

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

### 6. Konfiguracija agenta

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

### 7. Inicijalizacija agenta

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

### 8. Upravljanje razgovorima

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Ključne lekcije

1. **Arhitektura agenta**: Microsoft Agent Framework pruža čist, tipiziran pristup izgradnji AI agenata u .NET-u
2. **Integracija alata**: Funkcije označene atributima `[Description]` postaju dostupni alati za agenta
3. **Kontekst razgovora**: Upravljanje nitima omogućuje višestruke razgovore s punom sviješću o kontekstu
4. **Upravljanje konfiguracijom**: Varijable okruženja i sigurno rukovanje vjerodajnicama slijede najbolje prakse .NET-a
5. **Kompatibilnost s OpenAI**: Integracija GitHub modela radi besprijekorno putem OpenAI-kompatibilnih API-ja

## 🔗 Dodatni resursi

- [Microsoft Agent Framework Dokumentacija](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Aplikacije u jednoj datoteci](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.