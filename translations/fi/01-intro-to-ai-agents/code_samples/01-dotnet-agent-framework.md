# 🌍 AI-matkatoimisto Microsoft Agent Frameworkilla (.NET)

## 📋 Käsikirjoituksen yleiskatsaus

Tässä esimerkissä näytetään, miten rakentaa älykäs matkan suunnitteluagentti Microsoft Agent Frameworkin avulla .NET:lle. Agentti voi automaattisesti luoda henkilökohtaisia päivämatka-reittejä satunnaisiin kohteisiin ympäri maailmaa.

### Keskeiset ominaisuudet:

- 🎲 **Satunnainen kohteen valinta**: Käyttää mukautettua työkalua lomakohteiden valintaan
- 🗺️ **Älykäs matkan suunnittelu**: Luo yksityiskohtaiset päiväkohtaiset matkasuunnitelmat
- 🔄 **Reaaliaikainen suoratoisto**: Tukee sekä välittömiä että suoratoistovastauksia
- 🛠️ **Mukautetun työkalun integrointi**: Havainnollistaa agentin kykyjen laajentamista

## 🔧 Tekninen arkkitehtuuri

### Keskeiset teknologiat

- **Microsoft Agent Framework**: Uusin .NET-toteutus tekoälyagenttien kehitykseen
- **Azure OpenAI (Responses API)**: Käyttää Azure OpenAI Responses API:a mallin päätelmille
- **Azure Identity**: Turvallinen kirjautuminen `AzureCliCredential`in (`az login`) kautta
- **Turvallinen konfigurointi**: Ympäristöön perustuva päätepisteiden hallinta

### Keskeiset komponentit

1. **AIAgent**: Pääagentti, joka hallinnoi keskustelun kulkua
2. **Mukautetut työkalut**: `GetRandomDestination()` -funktio agentin käytettävissä
3. **Responses Client**: Azure OpenAI Responses -pohjainen keskustelurajapinta
4. **Suoratoistotuki**: Reaaliaikainen vastausten generointi

### Integraatiokaava

```mermaid
graph LR
    A[Käyttäjän pyyntö] --> B[tekoälyagentti]
    B --> C[Azure OpenAI (Vastaus-API)]
    B --> D[GetRandomDestination-työkalu]
    C --> E[Matkaohjelma]
    D --> E
```

## 🚀 Aloittaminen

### Vaatimukset

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) tai uudempi
- [Azure-tilaus](https://azure.microsoft.com/free/) sisältäen Azure OpenAI -resurssin ja mallin käyttöönoton
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — kirjaudu sisään `az login` -komennolla

### Vaaditut ympäristömuuttujat

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Kirjaudu sitten sisään, jotta AzureCliCredential voi saada tokenin
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

Koodiesimerkin suorittamiseksi,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Tai käyttäen dotnet CLI:tä:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Katso koko koodi tiedostosta [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs).

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.4.1
#:package Microsoft.Agents.AI.OpenAI@1.1.0
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

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip
// Run the agent with streaming enabled for real-time response display
// Shows the agent's thinking and response as it generates the content
// Provides better user experience with immediate feedback
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 Tärkeimmät opit

1. **Agentin arkkitehtuuri**: Microsoft Agent Framework tarjoaa selkeän ja tyyppiturvallisen tavan rakentaa tekoälyagentteja .NET:ssä
2. **Työkalujen integrointi**: `[Description]`-attribuutilla merkityt funktiot tulevat agentin käyttöön työkaluina
3. **Konfiguraation hallinta**: Ympäristömuuttujat ja turvallinen valtuustenkäsittely noudattavat .NET:n parhaita käytäntöjä
4. **Azure OpenAI Responses API**: Agentti käyttää Azure OpenAI Responses API:a Azure.AI.OpenAI SDK:n kautta

## 🔗 Lisäresurssit

- [Microsoft Agent Frameworkin dokumentaatio](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI Microsoft Foundryssa](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET yhden tiedoston sovellukset](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->