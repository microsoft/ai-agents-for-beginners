# 🛠️ Edistynyt työkalujen käyttö Azure OpenAI:n kanssa (Responses API) (.NET)

## 📋 Oppimistavoitteet

Tässä muistikirjassa havainnollistetaan yritystason työkalujen integrointimalleja Microsoft Agent Frameworkin avulla .NET:ssä Azure OpenAI:n (Responses API) kanssa. Opit rakentamaan monimutkaisia agenteja, joissa on useita erikoistuneita työkaluja, hyödyntäen C#:n vahvaa tyyppitarkistusta ja .NET:in yritysominaisuuksia.

### Hallitsemasi edistyneet työkalutoiminnot

- 🔧 **Monityökalurakenne**: Rakentamalla agenteja, joilla on useita erikoisominaisuuksia
- 🎯 **Tyyppiturvallinen työkalujen suoritus**: Hyödyntämällä C#:n käännösaikaiset tarkistukset
- 📊 **Yritystason työkalumallit**: Tuotantovalmiin työkalun suunnittelu ja virheenkäsittely
- 🔗 **Työkalujen yhdistäminen**: Työkalujen yhdistäminen monimutkaisiin liiketoimintaprosesseihin

## 🎯 .NET-työkalurakenteen edut

### Yritystason työkalutoiminnot

- **Käännösaikainen validointi**: Vahva tyyppitarkistus varmistaa työkalun parametrien oikeellisuuden
- **Riippuvuuksien injektointi**: IoC-konttainerin integrointi työkalujen hallintaan
- **Async/Await-mallit**: Ei-estävä työkalun suoritus oikealla resurssien hallinnalla
- **Rakennekirjautuminen**: Sisäänrakennettu lokitus integroituna työkalun suorituksen valvontaan

### Tuotantovalmiit mallit

- **Poikkeusten käsittely**: Laaja virheenkäsittely tyypitettyjen poikkeusten avulla
- **Resurssien hallinta**: Oikeat vapautusmallit ja muistin hallinta
- **Suorituskyvyn seuranta**: Sisäänrakennetut mittarit ja suorituskykymittarit
- **Konfiguraation hallinta**: Tyyppiturvallinen konfiguraatio validoinnilla

## 🔧 Tekninen arkkitehtuuri

### Keskeiset .NET-työkalukomponentit

- **Microsoft.Extensions.AI**: Yhtenäistetty työkalujen abstraktiokerros
- **Microsoft.Agents.AI**: Yritystason työkalujen orkestrointi
- **Azure OpenAI (Responses API)**: Korkean suorituskyvyn API-asiakas yhteyksien hallinnalla

### Työkalujen suoritusputki

```mermaid
graph LR
    A[Käyttäjän pyyntö] --> B[Agentin analyysi]
    B --> C[Työkalun valinta]
    C --> D[Tyyppivarmistus]
    B --> E[Parametrin sitominen]
    E --> F[Työkalun suoritus]
    C --> F
    F --> G[Tuloksen käsittely]
    D --> G
    G --> H[Vastaus]
```

## 🛠️ Työkalujen kategoriat ja mallit

### 1. **Tietojen käsittelytyökalut**

- **Syötteen validointi**: Vahva tyyppitarkistus datankoristeiden avulla
- **Muunnostoiminnot**: Tyyppiturvallinen datan muuntaminen ja muotoilu
- **Liiketoimintalogiikka**: Alakohtaiset laskenta- ja analyysityökalut
- **Tulostuksen muotoilu**: Rakenteellinen vastausten generointi

### 2. **Integraatiotyökalut**

- **API-liittimet**: REST-palveluiden integrointi HttpClientilla
- **Tietokantatyökalut**: Entity Framework -integraatio tietojen käsittelyyn
- **Tiedostotoiminnot**: Turvalliset tiedostojärjestelmän toiminnot validoinnilla
- **Ulkoiset palvelut**: Kolmannen osapuolen palveluintegrointimallit

### 3. **Aputyökalut**

- **Tekstinkäsittely**: Merkkijonojen käsittely- ja muotoilutyökalut
- **Päiväys-/Aikatoiminnot**: Kulttuuritietoiset päiväys/aika-laskelmat
- **Matemaattiset työkalut**: Tarkkuuslaskennat ja tilastolliset toiminnot
- **Validointityökalut**: Liiketoimintasääntöjen validointi ja datan tarkastus

Valmiina rakentamaan yritystason agenteja tehokkailla, tyyppiturvallisilla työkalutoiminnoilla .NET:ssä? Luodaanpa ammattimaisia ratkaisuja! 🏢⚡

## 🚀 Aloittaminen

### Esivaatimukset

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) tai uudempi
- [Azure-tilaus](https://azure.microsoft.com/free/), jossa on Azure OpenAI -resurssi ja mallin käyttöönotto
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — kirjaudu sisään komennolla `az login`

### Vaatimuksena olevat ympäristömuuttujat

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Kirjaudu sitten sisään, jotta AzureCliCredential voi saada tokenin
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Kirjaudu sitten sisään, jotta AzureCliCredential voi hakea tunnuksen
az login
```

### Esimerkkikoodi

Koodiesimerkin suorittamiseksi,

```bash
# zsh/bash
chmod +x ./04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Tai dotnet CLI -työkalua käyttäen:

```bash
dotnet run ./04-dotnet-agent-framework.cs
```

Katso kokonainen koodi tiedostosta [`04-dotnet-agent-framework.cs`](../../../../04-tool-use/code_samples/04-dotnet-agent-framework.cs).

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*
#:package Azure.AI.OpenAI@2.1.0
#:package Azure.Identity@1.13.1

using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using Azure.AI.OpenAI;
using Azure.Identity;

// Tool Function: Random Destination Generator
// This static method will be available to the agent as a callable tool
// The [Description] attribute helps the AI understand when to use this function
// This demonstrates how to create custom tools for AI agents
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
    // List of popular vacation destinations around the world
    // The agent will randomly select from these options
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

    // Generate random index and return selected destination
    // Uses System.Random for simple random selection
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}

// Azure OpenAI with the Responses API (stable v1 endpoint). Sign in with `az login`.
var azureEndpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")
    ?? throw new InvalidOperationException("AZURE_OPENAI_ENDPOINT is not set.");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4o-mini";

var azureClient = new AzureOpenAIClient(new Uri(azureEndpoint), new AzureCliCredential());

// Define Agent Identity and Comprehensive Instructions
// Agent name for identification and logging purposes
var AGENT_NAME = "TravelAgent";

// Detailed instructions that define the agent's personality, capabilities, and behavior
// This system prompt shapes how the agent responds and interacts with users
var AGENT_INSTRUCTIONS = """
You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
"Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?"

Always prioritize user preferences. If they mention a specific destination like "Bali" or "Paris," focus your planning on that location rather than suggesting alternatives.
""";

// Create AI Agent with Advanced Travel Planning Capabilities
// Get the Responses client for the deployment and create the AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = azureClient
    .GetOpenAIResponseClient(deployment)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Conversation Thread for Context Management
// Initialize a new conversation thread to maintain context across multiple interactions
// Threads enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentThread thread = agent.GetNewThread();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the thread parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation threads and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->