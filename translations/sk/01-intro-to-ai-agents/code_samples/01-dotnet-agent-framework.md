# 🌍 AI Cestovný Agent s Microsoft Agent Framework (.NET)

## 📋 Prehľad scenára

Tento notebook ukazuje, ako vytvoriť inteligentného agenta na plánovanie ciest pomocou Microsoft Agent Framework pre .NET. Agent dokáže automaticky generovať personalizované jednodňové itineráre pre náhodné destinácie po celom svete.

**Hlavné schopnosti:**
- 🎲 **Výber náhodnej destinácie**: Používa vlastný nástroj na výber dovolenkových miest
- 🗺️ **Inteligentné plánovanie ciest**: Vytvára podrobné itineráre deň po dni
- 🔄 **Streamovanie v reálnom čase**: Podporuje okamžité aj streamované odpovede
- 🛠️ **Integrácia vlastných nástrojov**: Ukazuje, ako rozšíriť schopnosti agenta

## 🔧 Technická architektúra

### Základné technológie
- **Microsoft Agent Framework**: Najnovšia implementácia .NET pre vývoj AI agentov
- **Integrácia modelov GitHub**: Používa službu inferencie AI modelov od GitHubu
- **Kompatibilita s OpenAI API**: Využíva klientské knižnice OpenAI s vlastnými koncovými bodmi
- **Bezpečná konfigurácia**: Správa API kľúčov na základe prostredia

### Kľúčové komponenty
1. **AIAgent**: Hlavný orchestrátor agenta, ktorý riadi tok konverzácie
2. **Vlastné nástroje**: Funkcia `GetRandomDestination()` dostupná pre agenta
3. **Chat Client**: Rozhranie konverzácie podporované modelmi GitHub
4. **Podpora streamovania**: Schopnosti generovania odpovedí v reálnom čase

### Vzor integrácie
```mermaid
graph LR
    A[User Request] --> B[AI Agent]
    B --> C[GitHub Models API]
    B --> D[GetRandomDestination Tool]
    C --> E[Travel Itinerary]
    D --> E
```

## 🚀 Začíname

**Predpoklady:**
- .NET 9.0 alebo vyšší
- Prístupový token k API modelov GitHub
- Konfigurované environmentálne premenné v súbore `.env`

**Požadované environmentálne premenné:**
```env
GITHUB_TOKEN=your_github_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Spustite bunky nižšie postupne, aby ste videli agenta na plánovanie ciest v akcii!

---

## .NET Single File App: AI Travel Agent Example

See `01-dotnet-agent-framework.cs` for the complete runnable code sample.

Spustite ukážku kódu nižšie:

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
