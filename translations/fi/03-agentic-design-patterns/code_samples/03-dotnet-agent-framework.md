# 🎨 Agenttipohjaiset suunnittelumallit Azure OpenAI:n kanssa (Responses API) (.NET)

## 📋 Oppimistavoitteet

Tämä esimerkki havainnollistaa yritystason suunnittelumalleja älykkäiden agenttien rakentamiseen Microsoft Agent Frameworkin avulla .NET:ssä Azure OpenAI:n (Responses API) integraatiolla. Opit ammattilaismallit ja arkkitehtoniset lähestymistavat, jotka tekevät agenteista tuotantovalmiita, ylläpidettäviä ja skaalautuvia.

### Yritystason suunnittelumallit

- 🏭 **Tehdasmalli**: Vakioitu agenttien luonti riippuvuussisäänruiskutuksella
- 🔧 **Rakentajamalli**: Virtaviivainen agentin konfigurointi ja käyttöönotto
- 🧵 **Säieturvatut mallit**: Samanaikainen keskustelun hallinta
- 📋 **Repositoriomalli**: Työkalujen ja ominaisuuksien järjestelmällinen hallinta

## 🎯 .NET-spesifiset arkkitehtoniset hyödyt

### Yritysominaisuudet

- **Vahva tyypitys**: Käännösaikainen validointi ja IntelliSense-tuki
- **Riippuvuussisäänruiskutus**: Sisäänrakennettu DI-kontainerin tuki
- **Konfiguraation hallinta**: IConfiguration- ja Options-mallit
- **Async/Await**: Ensiluokkainen asynkroninen ohjelmointituki

### Tuotantovalmiit mallit

- **Lokitusintegraatio**: ILogger ja rakenteellinen lokituki
- **Terveystarkistukset**: Sisäänrakennettu valvonta ja diagnostiikka
- **Konfiguraation validointi**: Vahva tyypitys ja dataannotaatiot
- **Virheenkäsittely**: Rakenteellinen poikkeamien hallinta

## 🔧 Tekninen arkkitehtuuri

### Keskeiset .NET-komponentit

- **Microsoft.Extensions.AI**: Yhtenäiset tekoälypalvelujen abstraktiot
- **Microsoft.Agents.AI**: Yritystason agenttien orkestrointikehys
- **Azure OpenAI (Responses API)**: Suorituskykyiset API-asiakasratkaisut
- **Konfiguraatiojärjestelmä**: appsettings.json ja ympäristöintegraatio

### Suunnittelumallin toteutus

```mermaid
graph LR
    A[IServiceCollection] --> B[Agentin Rakentaja]
    B --> C[Konfiguraatio]
    C --> D[Työkalurekisteri]
    D --> E[AI-agentti]
```

## 🏗️ Havainnollistetut yritystason mallit

### 1. **Luomis- eli Creational-mallit**

- **Agenttitehdas**: Keskitetty agenttien luonti yhdenmukaisella konfiguraatiolla
- **Rakentajamalli**: Fluent API monimutkaiseen agenttien konfigurointiin
- **Singleton-malli**: Jaettujen resurssien ja konfiguraation hallinta
- **Riippuvuussisäänruiskutus**: Löysä kytkentä ja testattavuus

### 2. **Käyttäytymismallit**

- **Strategiamalli**: Vaihdettavat työkalusuoritusstrategiat
- **Komentomalli**: Agenttien toiminnot kapseloituna kumoa/tee uudelleen -toiminnoilla
- **Tarkkailijamalli**: Tapahtumapohjainen agenttien elinkaaren hallinta
- **Mallimenetelmä**: Vakioidut agenttien suoritustyönkulut

### 3. **Rakennepohjaiset mallit**

- **Sovitinmalli**: Azure OpenAI (Responses API) -integraatiokerros
- **Koristemalli**: Agenttien kyvykkyyksien lisäys
- **Fasadi**: Yksinkertaistetut agenttien rajapinnat
- **Välittäjä (Proxy)**: Laiska lataus ja välimuisti suorituskyvyn parantamiseksi

## 📚 .NET-suunnitteluperiaatteet

### SOLID-periaatteet

- **Yksivastuuperiaate**: Jokaisella komponentilla on yksi selkeä tehtävä
- **Avoin/Suljettu**: Laajennettavissa ilman muokkauksia
- **Liskovin substituutioperiaate**: Rajapintaperustaiset työkalujen toteutukset
- **Rajapintojen eriyttäminen**: Tarkoituksenmukaiset, koherentit rajapinnat
- **Riippuvuuksien kääntöperiaate**: Riippumattomuus abstraktioista, ei konkreettisuuksista

### Puhtaan arkkitehtuurin periaatteet

- **Domain-kerros**: Keskeiset agentti- ja työkalun abstraktiot
- **Sovelluskerros**: Agenttien orkestrointi ja työnkulut
- **Infrastruktuurikerros**: Azure OpenAI (Responses API) -integraatio ja ulkoiset palvelut
- **Esityskerros**: Käyttäjävuorovaikutus ja vastausten muotoilu

## 🔒 Yritystason näkökulmat

### Turvallisuus

- **Tunnistetietojen hallinta**: Turvallinen API-avainten käsittely IConfigurationin avulla
- **Syötteiden validointi**: Vahva tyypitys ja dataannotaatiovalidointi
- **Tulosten puhdistus**: Turvallinen vastausten käsittely ja suodatus
- **Audit-lokitus**: Laaja operaatioiden seuranta

### Suorituskyky

- **Async-mallit**: Ei-estävät I/O-toiminnot
- **Yhteyspaalaus**: Tehokas HTTP-asiakkaan hallinta
- **Välimuisti**: Vastausten välimuistitus suorituskyvyn parantamiseksi
- **Resurssien hallinta**: Oikea hävitys ja siivousmallit

### Skaalautuvuus

- **Säieturva**: Samanaikainen agenttien suorituskyky
- **Resurssien yhdisteleminen**: Tehokas resurssien hyödyntäminen
- **Kuormanhallinta**: Nopeusrajoitus ja takaisinpaineen hallinta
- **Valvonta**: Suorituskykymittarit ja terveystarkistukset

## 🚀 Tuotantoon käyttöönotto

- **Konfiguraation hallinta**: Ympäristökohtaiset asetukset
- **Lokitusstrategia**: Rakenteellinen lokitus korrelaatio-ID:illä
- **Virheenkäsittely**: Globaali poikkeamien hallinta ja asianmukainen palautuminen
- **Valvonta**: Sovellusinsights ja suorituskykymittarit
- **Testaus**: Yksikkötestit, integraatiotestit ja kuormitustestausmallit

Valmis rakentamaan yritystason älykkäitä agenteja .NETillä? Rakennetaan jotain vankkaa! 🏢✨

## 🚀 Aloittaminen

### Ennakkoedellytykset

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) tai uudempi
- [Azure-tilaus](https://azure.microsoft.com/free/), jossa on Azure OpenAI -resurssi ja mallin käyttöönotto
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — kirjaudu sisään komennolla `az login`

### Vaatimukset ympäristömuuttujille

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
# Kirjaudu sitten sisään, jotta AzureCliCredential voi saada tunnuksen
az login
```

### Esimerkkikoodi

Esimerkkikoodin suorittamiseksi,

```bash
# zsh/bash
chmod +x ./03-dotnet-agent-framework.cs
./03-dotnet-agent-framework.cs
```

Tai dotnet CLI:llä:

```bash
dotnet run ./03-dotnet-agent-framework.cs
```

Katso koko koodi tiedostosta [`03-dotnet-agent-framework.cs`](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

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