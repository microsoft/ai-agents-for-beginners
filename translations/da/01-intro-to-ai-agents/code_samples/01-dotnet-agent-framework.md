# 🌍 AI Rejseagent med Microsoft Agent Framework (.NET)

## 📋 Scenarieoversigt

Denne notebook viser, hvordan man opbygger en intelligent rejseplanlægningsagent ved hjælp af Microsoft Agent Framework for .NET. Agenten kan automatisk generere personlige dagsrejseplaner for tilfældige destinationer rundt om i verden.

**Nøglefunktioner:**
- 🎲 **Tilfældig destinationsvalg**: Bruger et specialværktøj til at vælge feriesteder
- 🗺️ **Intelligent rejseplanlægning**: Skaber detaljerede dagsplaner
- 🔄 **Streaming i realtid**: Understøtter både øjeblikkelige og streamede svar
- 🛠️ **Integration af specialværktøjer**: Viser, hvordan man udvider agentens funktioner

## 🔧 Teknisk arkitektur

### Kerne-teknologier
- **Microsoft Agent Framework**: Seneste .NET-implementering til udvikling af AI-agenter
- **GitHub Models Integration**: Bruger GitHubs AI-model inferenstjeneste
- **OpenAI API-kompatibilitet**: Udnytter OpenAI-klientbiblioteker med brugerdefinerede endpoints
- **Sikker konfiguration**: Miljøbaseret API-nøglehåndtering

### Centrale komponenter
1. **AIAgent**: Den primære agent, der styrer samtaleflowet
2. **Specialværktøjer**: `GetRandomDestination()`-funktionen tilgængelig for agenten
3. **Chatklient**: GitHub Models-baseret samtalegrænseflade
4. **Streaming-understøttelse**: Evne til at generere svar i realtid

### Integrationsmønster
```mermaid
graph LR
    A[User Request] --> B[AI Agent]
    B --> C[GitHub Models API]
    B --> D[GetRandomDestination Tool]
    C --> E[Travel Itinerary]
    D --> E
```

## 🚀 Kom godt i gang

**Forudsætninger:**
- .NET 9.0 eller nyere
- GitHub Models API adgangstoken
- Miljøvariabler konfigureret i `.env`-filen

**Påkrævede miljøvariabler:**
```env
GITHUB_TOKEN=your_github_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Kør cellerne nedenfor i rækkefølge for at se rejseagenten i aktion!

---

## .NET Single File App: AI Travel Agent Example

See `01-dotnet-agent-framework.cs` for the complete runnable code sample.

Kør kodeeksemplet nedenfor:

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
