<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:41:50+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "et"
}
-->
# 🔍 Agentlike raamistikud - Põhiagent (.NET)

## 📋 Õpieesmärgid

See märkmik uurib Microsofti agentraamistiku põhimõtteid, rakendades lihtsat agenti .NET-is. Õpid agentlike mustreid ja mõistad, kuidas intelligentsed agendid töötavad C# ja .NET ökosüsteemi abil.

**Mida avastad:**
- 🏗️ **Agendi arhitektuur**: AI agentide põhistruktuuri mõistmine .NET-is
- 🛠️ **Tööriistade integreerimine**: Kuidas agendid kasutavad väliseid funktsioone võimekuse laiendamiseks  
- 💬 **Vestluse voog**: Mitme pöördega vestluste ja konteksti haldamine lõimehalduse abil
- 🔧 **Konfiguratsioonimustrid**: Parimad tavad agendi seadistamiseks ja haldamiseks .NET-is

## 🎯 Põhimõisted

### Agentlike raamistikupõhimõtted
- **Autonoomia**: Kuidas agendid teevad iseseisvaid otsuseid, kasutades .NET AI abstraktsioone
- **Reaktiivsus**: Reageerimine keskkonnamuutustele ja kasutaja sisenditele
- **Proaktiivsus**: Algatuse võtmine eesmärkide ja konteksti põhjal
- **Sotsiaalne võimekus**: Suhtlemine loomuliku keele kaudu vestluste lõimede abil

### Tehnilised komponendid
- **AIAgent**: Põhiagendi orkestreerimine ja vestluse haldamine (.NET)
- **Tööriistafunktsioonid**: Agendi võimekuse laiendamine C# meetodite ja atribuutidega
- **OpenAI integratsioon**: Keelemudelite kasutamine standardiseeritud .NET API-de kaudu
- **Keskkonna haldamine**: Turvaline konfiguratsioon ja mandaadi haldamine DotNetEnv abil

## ⚙️ Eeltingimused ja seadistamine

**Nõutavad sõltuvused:**
- .NET 9.0 SDK või uuem
- Visual Studio 2022 või VS Code koos C# laiendiga

**NuGet paketid:**
- `Microsoft.Extensions.AI` - Põhilised AI abstraktsioonid
- `Microsoft.Extensions.AI.OpenAI` - OpenAI integratsioon (eelvaade)
- `DotNetEnv` - Keskkonnamuutujate haldamine

**Keskkonna konfiguratsioon (.env fail):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Tehniline virn

**Põhitehnoloogiad:**
- Microsoft Agent Framework (.NET)
- GitHub Models API integratsioon
- OpenAI-ühilduvad kliendimustrid
- Keskkonnapõhine konfiguratsioon DotNetEnv abil

**Agendi võimekused:**
- Loomuliku keele mõistmine ja genereerimine
- Funktsioonide kutsumine ja tööriistade kasutamine C# atribuutidega
- Kontekstitundlikud vastused vestluste lõimede abil
- Laiendatav arhitektuur sõltuvuste süstimise mustritega

## 📚 Raamistike võrdlus

See näide demonstreerib Microsoft Agent Frameworki lähenemist .NET-is võrreldes teiste platvormidega:

| Funktsioon | .NET Agent Framework | Python ekvivalendid |
|------------|-----------------------|---------------------|
| **Tüübikindlus** | Tugev tüübikindlus C#-ga | Dünaamiline tüüpimine |
| **Integratsioon** | Natiivne .NET ökosüsteem | Erinev ühilduvus |
| **Jõudlus** | Kompileeritud koodi jõudlus | Tõlgitud täitmine |
| **Ettevõttevalmidus** | Loodud tootmiskeskkonna .NET rakenduste jaoks | Sõltub raamistikust |
| **Tööriistad** | Visual Studio integratsioon | IDE-sõltuv |

## 🚀 Alustamine

Järgi allolevaid samme, et luua oma esimene põhiagent .NET-is ja mõista agentlike põhimõtteid!

## 📦 Paigaldamine ja seadistamine

See näide on saadaval käivitatava .NET ühe faili rakendusena. Täieliku rakenduse leiad kaasasolevast failist `02-dotnet-agent-framework.cs`.

Näite käivitamiseks:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Või kasutades dotnet CLI-d:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Koodi ülevaade

Täielik rakendus sisaldab:

### 1. Paketisõltuvused

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

### 2. Olulised impordid

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Keskkonna konfiguratsioon

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Tööriistafunktsiooni määratlus

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

### 5. Konfiguratsiooni ja kliendi seadistamine

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

### 6. Agendi konfiguratsioon

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

### 7. Agendi initsialiseerimine

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

### 8. Vestluse haldamine

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Peamised õppetunnid

1. **Agendi arhitektuur**: Microsoft Agent Framework pakub puhtaid, tüübikindlaid lahendusi AI agentide loomiseks .NET-is
2. **Tööriistade integreerimine**: Funktsioonid, millele on lisatud `[Description]` atribuudid, muutuvad agendi jaoks kättesaadavateks tööriistadeks
3. **Vestluse kontekst**: Lõimehaldus võimaldab mitme pöördega vestlusi täieliku kontekstitundlikkusega
4. **Konfiguratsiooni haldamine**: Keskkonnamuutujad ja turvaline mandaadi haldamine järgivad .NET parimaid tavasid
5. **OpenAI ühilduvus**: GitHub Models integratsioon töötab sujuvalt OpenAI-ühilduvate API-de kaudu

## 🔗 Lisamaterjalid

- [Microsoft Agent Framework dokumentatsioon](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET ühe faili rakendused](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.