<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:36:54+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "fi"
}
-->
# 🔍 Agenttisten kehysten tutkiminen - Perusagentti (.NET)

## 📋 Oppimistavoitteet

Tämä muistikirja tutkii Microsoft Agent Frameworkin peruskäsitteitä toteuttamalla yksinkertaisen agentin .NET-ympäristössä. Opit agenttisten mallien perusteet ja ymmärrät, miten älykkäät agentit toimivat C#:n ja .NET-ekosysteemin avulla.

**Mitä opit:**
- 🏗️ **Agentin arkkitehtuuri**: AI-agenttien perusrakenne .NET-ympäristössä
- 🛠️ **Työkalujen integrointi**: Kuinka agentit käyttävät ulkoisia funktioita laajentaakseen toimintojaan  
- 💬 **Keskustelun kulku**: Monivaiheisten keskustelujen ja kontekstin hallinta säikeiden avulla
- 🔧 **Konfigurointimallit**: Parhaat käytännöt agentin asetusten ja hallinnan suhteen .NET-ympäristössä

## 🎯 Keskeiset käsitteet

### Agenttisen kehyksen periaatteet
- **Autonomia**: Kuinka agentit tekevät itsenäisiä päätöksiä .NET AI-abstraktioiden avulla
- **Reaktiivisuus**: Ympäristön muutoksiin ja käyttäjän syötteisiin vastaaminen
- **Proaktiivisuus**: Aloitteellisuus tavoitteiden ja kontekstin perusteella
- **Sosiaalinen kyvykkyys**: Luonnollisen kielen käyttö keskustelusäikeiden kautta

### Teknologiset komponentit
- **AIAgent**: Agentin orkestrointi ja keskustelun hallinta (.NET)
- **Työkalufunktiot**: Agentin kyvykkyyksien laajentaminen C#-metodien ja attribuuttien avulla
- **OpenAI-integraatio**: Kielen mallien hyödyntäminen standardoitujen .NET-rajapintojen kautta
- **Ympäristön hallinta**: Turvallinen konfigurointi ja tunnistetietojen käsittely DotNetEnv:n avulla

## ⚙️ Esivaatimukset ja asennus

**Vaaditut riippuvuudet:**
- .NET 9.0 SDK tai uudempi
- Visual Studio 2022 tai VS Code C#-laajennuksella

**NuGet-paketit:**
- `Microsoft.Extensions.AI` - AI-abstraktioiden ydin
- `Microsoft.Extensions.AI.OpenAI` - OpenAI-integraatio (esiversio)
- `DotNetEnv` - Ympäristömuuttujien hallinta

**Ympäristön konfigurointi (.env-tiedosto):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Tekninen kokonaisuus

**Keskeiset teknologiat:**
- Microsoft Agent Framework (.NET)
- GitHub Models API -integraatio
- OpenAI-yhteensopivat asiakasmallit
- Ympäristöön perustuva konfigurointi DotNetEnv:n avulla

**Agentin kyvykkyydet:**
- Luonnollisen kielen ymmärtäminen ja tuottaminen
- Funktioiden kutsuminen ja työkalujen käyttö C#-attribuuttien avulla
- Kontekstin huomioivat vastaukset keskustelusäikeiden avulla
- Laajennettava arkkitehtuuri riippuvuuksien injektointimallien avulla

## 📚 Kehysten vertailu

Tämä esimerkki havainnollistaa Microsoft Agent Frameworkin lähestymistapaa .NET-ympäristössä verrattuna muihin alustoihin:

| Ominaisuus | .NET Agent Framework | Python-vastineet |
|------------|----------------------|------------------|
| **Tyyppiturvallisuus** | Vahva tyyppitarkistus C#:ssa | Dynaaminen tyyppitarkistus |
| **Integraatio** | Natiivi .NET-ekosysteemi | Vaihteleva yhteensopivuus |
| **Suorituskyky** | Käännetyn koodin suorituskyky | Tulkattu suoritus |
| **Yritysvalmius** | Suunniteltu tuotantokäyttöön .NET-sovelluksissa | Vaihtelee kehyksen mukaan |
| **Työkalut** | Visual Studio -integraatio | IDE-riippuvainen |

## 🚀 Aloittaminen

Seuraa alla olevia vaiheita rakentaaksesi ensimmäisen perusagenttisi .NET-ympäristössä ja ymmärtääksesi agenttisten käsitteiden perusteet!

## 📦 Asennus ja käyttöönotto

Tämä esimerkki on saatavilla suoritettavana .NET Single File App -sovelluksena. Katso mukana tuleva `02-dotnet-agent-framework.cs`-tiedosto täydellistä toteutusta varten.

Esimerkin suorittaminen:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Tai dotnet CLI:n avulla:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Koodin läpikäynti

Täydellinen toteutus sisältää:

### 1. Pakettiriippuvuudet

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

### 2. Keskeiset tuonnit

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Ympäristön konfigurointi

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Työkalufunktion määrittely

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

### 5. Konfigurointi ja asiakasasetukset

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

### 6. Agentin konfigurointi

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

### 7. Agentin alustaminen

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

### 8. Keskustelun hallinta

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Keskeiset opit

1. **Agentin arkkitehtuuri**: Microsoft Agent Framework tarjoaa selkeän, tyyppiturvallisen lähestymistavan AI-agenttien rakentamiseen .NET-ympäristössä
2. **Työkalujen integrointi**: Funktiot, joilla on `[Description]`-attribuutit, tulevat agentin käytettävissä oleviksi työkaluiksi
3. **Keskustelukonteksti**: Säikeiden hallinta mahdollistaa monivaiheiset keskustelut täydellä kontekstin huomioinnilla
4. **Konfiguroinnin hallinta**: Ympäristömuuttujat ja turvallinen tunnistetietojen käsittely noudattavat .NET:n parhaita käytäntöjä
5. **OpenAI-yhteensopivuus**: GitHub Models -integraatio toimii saumattomasti OpenAI-yhteensopivien rajapintojen kautta

## 🔗 Lisäresurssit

- [Microsoft Agent Framework -dokumentaatio](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty AI-käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.