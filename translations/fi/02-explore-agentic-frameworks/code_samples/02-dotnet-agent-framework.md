# 🔍 Microsoft Agent Frameworkin tutkiminen - Perusagentti (.NET)

## 📋 Oppimistavoitteet

Tässä esimerkissä tutustutaan Microsoft Agent Frameworkin perustavanlaatuisiin käsitteisiin toteuttamalla perusagentti .NET:ssä. Opit keskeiset agenttimallit ja ymmärrät, miten älykkäät agentit toimivat kulissien takana käyttäen C#:tä ja .NET-ekosysteemiä.

### Mitä Opit

- 🏗️ **Agentin Arkkitehtuuri**: Ymmärtämään AI-agenttien perusrakenne .NET:ssä
- 🛠️ **Työkalujen Integraatio**: Kuinka agentit hyödyntävät ulkopuolisia toimintoja kapasiteetin laajentamiseksi  
- 💬 **Keskustelun Kulku**: Hallitsemaan monivaiheisia keskusteluja ja kontekstia ketjuhallinnan avulla
- 🔧 **Konfigurointimallit**: Parhaat käytännöt agentin konfigurointiin ja hallintaan .NET:ssä

## 🎯 Keskeiset Käsitteet

### Agenttikehikon Periaatteet

- **Autonomia**: Kuinka agentit tekevät itsenäisiä päätöksiä käyttäen .NET AI -abstraktioita
- **Reaktiivisuus**: Reagoiminen ympäristön muutoksiin ja käyttäjän syötteisiin
- **Proaktiivisuus**: Aloitteen ottaminen tavoitteiden ja kontekstin perusteella
- **Sosiaaliset Taidot**: Vuorovaikutus luonnollisella kielellä keskusteluketjujen kautta

### Teknisiä Komponentteja

- **AIAgent**: Keskeinen agentin orkestrointi ja keskustelun hallinta (.NET)
- **Työkaluominaisuudet**: Agentin kykyjen laajentaminen C#-metodeilla ja attribuuteilla
- **Azure OpenAI -integraatio**: Kielen mallien hyödyntäminen Azure OpenAI Responses API:n kautta
- **Turvallinen Konfigurointi**: Ympäristöön perustuva pisteiden hallinta

## 🔧 Tekninen Pino

### Keskeiset Teknologiat

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) -integraatio
- Azure.AI.OpenAI -asiakasmallit
- Ympäristöön perustuva konfigurointi DotNetEnvillä

### Agentin Ominaisuudet

- Luonnollisen kielen ymmärtäminen ja tuottaminen
- Funktiokutsu ja työkalujen käyttö C#-attribuuteilla
- Kontekstin huomioivat vastaukset keskustelusessioissa
- Laajennettava arkkitehtuuri riippuvuuden injektiomalleilla

## 📚 Kehikkojen Vertailu

Tämä esimerkki demonstroi Microsoft Agent Framework -lähestymistapaa verrattuna muihin agenttimallinnuskehyksiin:

| Ominaisuus | Microsoft Agent Framework | Muut Kehikot |
|---------|-------------------------|------------------|
| **Integraatio** | Natiivi Microsoft-ekosysteemi | Vaihteleva yhteensopivuus |
| **Yksinkertaisuus** | Selkeä, intuitiivinen API | Usein monimutkainen asetukset |
| **Laajennettavuus** | Helppo työkalujen liittäminen | Riippuu kehyksestä |
| **Yritysvalmis** | Rakennettu tuotantoon | Vaihtelee kehyksen mukaan |

## 🚀 Aloittaminen

### Esivaatimukset

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) tai uudempi
- Azure-tili [Azure OpenAI -resurssilla](https://azure.microsoft.com/free/) ja malliasennuksella
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — kirjaudu sisään komennolla `az login`

### Vaaditut Ympäristömuuttujat

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Kirjaudu sisään, jotta AzureCliCredential voi hankkia tokenin
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Kirjaudu sitten sisään, jotta AzureCliCredential voi saada tokenin
az login
```

### Esimerkkikoodi

Suorita koodiesimerkki seuraavasti,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Tai käyttämällä dotnet CLI:tä:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Katso koko koodi tiedostosta [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs).

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

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
    .GetChatClient(deployment)
    .AsAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Session for Context Management.
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentSession session = await agent.CreateSessionAsync();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the session parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", session))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation sessions and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", session))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 Keskeiset Oivallukset

1. **Agentin Arkkitehtuuri**: Microsoft Agent Framework tarjoaa selkeän, tyyppiturvallisen lähestymistavan AI-agenttien rakentamiseen .NET:ssä
2. **Työkalujen Integraatio**: [Description]-attribuutilla koristellut funktiot ovat agentille käytettävissä olevia työkaluja
3. **Keskustelukonteksti**: Istunnon hallinta mahdollistaa monivaiheiset keskustelut täydellisellä kontekstihan kalkilla
4. **Konfiguraation Hallinta**: Ympäristömuuttujat ja turvallinen tunnistetietojen käsittely noudattavat .NET:n parhaita käytäntöjä
5. **Azure OpenAI Responses API**: Agentti käyttää Azure OpenAI Responses API:a Azure.AI.OpenAI SDK:n kautta

## 🔗 Lisäresurssit

- [Microsoft Agent Framework -dokumentaatio](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI Microsoft Foundryssa](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Yhden Tiedoston Sovellukset](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->