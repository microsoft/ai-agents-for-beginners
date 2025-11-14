<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:40:34+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "sl"
}
-->
# 🔍 Raziskovanje agentnih ogrodij - Osnovni agent (.NET)

## 📋 Cilji učenja

Ta zvezek raziskuje temeljne koncepte Microsoftovega agentnega ogrodja skozi implementacijo osnovnega agenta v .NET. Naučili se boste osnovnih agentnih vzorcev in razumeli, kako inteligentni agenti delujejo v ozadju z uporabo C# in ekosistema .NET.

**Kaj boste odkrili:**
- 🏗️ **Arhitektura agenta**: Razumevanje osnovne strukture AI agentov v .NET
- 🛠️ **Integracija orodij**: Kako agenti uporabljajo zunanje funkcije za razširitev zmogljivosti  
- 💬 **Tok pogovora**: Upravljanje večkratnih pogovorov in konteksta z upravljanjem niti
- 🔧 **Vzorce konfiguracije**: Najboljše prakse za nastavitev in upravljanje agentov v .NET

## 🎯 Ključni koncepti

### Načela agentnega ogrodja
- **Avtonomija**: Kako agenti sprejemajo neodvisne odločitve z uporabo .NET AI abstrakcij
- **Reaktivnost**: Odzivanje na spremembe okolja in uporabniške vnose
- **Proaktivnost**: Pobuda na podlagi ciljev in konteksta
- **Socialna sposobnost**: Interakcija prek naravnega jezika z nitmi pogovora

### Tehnične komponente
- **AIAgent**: Osnovna orkestracija agenta in upravljanje pogovorov (.NET)
- **Funkcije orodij**: Razširitev zmogljivosti agenta z metodami in atributi C#
- **Integracija OpenAI**: Uporaba jezikovnih modelov prek standardiziranih .NET API-jev
- **Upravljanje okolja**: Varna konfiguracija in upravljanje poverilnic z DotNetEnv

## ⚙️ Predpogoji in nastavitev

**Potrebne odvisnosti:**
- .NET 9.0 SDK ali novejši
- Visual Studio 2022 ali VS Code z razširitvijo za C#

**NuGet paketi:**
- `Microsoft.Extensions.AI` - Osnovne AI abstrakcije
- `Microsoft.Extensions.AI.OpenAI` - Integracija OpenAI (predogled)
- `DotNetEnv` - Upravljanje okoljskih spremenljivk

**Konfiguracija okolja (.env datoteka):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Tehnični sklad

**Osnovne tehnologije:**
- Microsoftovo agentno ogrodje (.NET)
- Integracija API-jev GitHub Models
- Vzorce odjemalcev, združljive z OpenAI
- Konfiguracija na podlagi okolja z DotNetEnv

**Zmožnosti agenta:**
- Razumevanje in generiranje naravnega jezika
- Klicanje funkcij in uporaba orodij z atributi C#
- Odzivi, ki se zavedajo konteksta, z nitmi pogovora
- Razširljiva arhitektura z vzorci za vbrizgavanje odvisnosti

## 📚 Primerjava ogrodij

Ta primer prikazuje pristop Microsoftovega agentnega ogrodja v .NET v primerjavi z drugimi platformami:

| Funkcija | .NET Agent Framework | Python ekvivalenti |
|----------|-----------------------|--------------------|
| **Tipna varnost** | Močno tipiziranje s C# | Dinamično tipiziranje |
| **Integracija** | Domači ekosistem .NET | Raznolika združljivost |
| **Zmogljivost** | Zmogljivost prevedene kode | Interpretirana izvedba |
| **Pripravljenost za podjetja** | Zasnovano za produkcijske .NET aplikacije | Odvisno od ogrodja |
| **Orodja** | Integracija z Visual Studio | Odvisno od IDE |

## 🚀 Začetek

Sledite spodnjim celicam, da zgradite svoj prvi osnovni agent v .NET in razumete temeljne agentne koncepte!

## 📦 Namestitev in nastavitev

Ta primer je na voljo kot izvedljiva .NET aplikacija v eni datoteki. Oglejte si priloženo datoteko `02-dotnet-agent-framework.cs` za celotno implementacijo.

Za zagon tega primera:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Ali z uporabo dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Pregled kode

Celotna implementacija vključuje:

### 1. Odvisnosti paketov

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

### 3. Konfiguracija okolja

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Definicija funkcij orodij

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

### 5. Nastavitev konfiguracije in odjemalca

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

### 7. Inicializacija agenta

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

### 8. Upravljanje pogovorov

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Ključne ugotovitve

1. **Arhitektura agenta**: Microsoftovo agentno ogrodje ponuja čist, tipno varen pristop k gradnji AI agentov v .NET
2. **Integracija orodij**: Funkcije, označene z atributi `[Description]`, postanejo razpoložljiva orodja za agenta
3. **Kontekst pogovora**: Upravljanje niti omogoča večkratne pogovore s popolno zavednostjo konteksta
4. **Upravljanje konfiguracije**: Okoljske spremenljivke in varno upravljanje poverilnic sledijo najboljšim praksam .NET
5. **Združljivost z OpenAI**: Integracija GitHub Models deluje brezhibno prek API-jev, združljivih z OpenAI

## 🔗 Dodatni viri

- [Dokumentacija Microsoft Agent Framework](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [Tržnica GitHub Models](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET aplikacije v eni datoteki](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije je priporočljivo profesionalno človeško prevajanje. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.