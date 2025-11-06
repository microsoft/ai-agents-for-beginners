# 🌍 AI-matkatoimisto Microsoft Agent Frameworkilla (.NET)

## 📋 Skenaarion yleiskuvaus

Tämä muistikirja näyttää, kuinka rakentaa älykäs matkasuunnittelija-agentti Microsoft Agent Frameworkin avulla .NET-ympäristössä. Agentti voi automaattisesti luoda henkilökohtaisia päiväretkien matkasuunnitelmia satunnaisiin kohteisiin ympäri maailmaa.

**Keskeiset ominaisuudet:**
- 🎲 **Satunnaisen kohteen valinta**: Käyttää mukautettua työkalua lomakohteiden valintaan
- 🗺️ **Älykäs matkasuunnittelu**: Luo yksityiskohtaisia päiväkohtaisia matkasuunnitelmia
- 🔄 **Reaaliaikainen suoratoisto**: Tukee sekä välittömiä että suoratoistovastauksia
- 🛠️ **Mukautettu työkalujen integrointi**: Näyttää, kuinka agentin ominaisuuksia voidaan laajentaa

## 🔧 Tekninen arkkitehtuuri

### Keskeiset teknologiat
- **Microsoft Agent Framework**: Uusin .NET-toteutus tekoälyagenttien kehittämiseen
- **GitHub Models -integraatio**: Käyttää GitHubin tekoälymallien inferenssipalvelua
- **OpenAI API -yhteensopivuus**: Hyödyntää OpenAI:n asiakaskirjastoja mukautetuilla päätepisteillä
- **Turvallinen konfiguraatio**: API-avainten hallinta ympäristömuuttujien avulla

### Keskeiset komponentit
1. **AIAgent**: Pääagentti, joka hallinnoi keskustelun kulkua
2. **Mukautetut työkalut**: `GetRandomDestination()`-funktio agentin käytettävissä
3. **Chat Client**: GitHub Models -pohjainen keskusteluliittymä
4. **Suoratoistotuki**: Reaaliaikainen vastausten generointi

### Integraatiomalli
```mermaid
graph LR
    A[User Request] --> B[AI Agent]
    B --> C[GitHub Models API]
    B --> D[GetRandomDestination Tool]
    C --> E[Travel Itinerary]
    D --> E
```

## 🚀 Aloittaminen

**Edellytykset:**
- .NET 9.0 tai uudempi
- GitHub Models API -pääsytunnus
- Ympäristömuuttujat määritetty `.env`-tiedostossa

**Vaaditut ympäristömuuttujat:**
```env
GITHUB_TOKEN=your_github_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Suorita alla olevat solut järjestyksessä nähdäksesi matkatoimiston toiminnassa!

---

## .NET Single File App: AI Travel Agent Example

See `01-dotnet-agent-framework.cs` for the complete runnable code sample.

Suorita alla oleva koodinäyte:

```bash
dotnet run 01-dotnet-agent-framework.cs
```

### Sample Code

```csharp
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

// Extract configuration from environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI Client Options
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

// Create AI Agent with Travel Planning Capabilities
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip (Non-Streaming)
Console.WriteLine(await agent.RunAsync("Plan me a day trip"));

// Execute Agent: Plan a Day Trip (Streaming Response)
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    Console.Write(update);
}
```
