# 🌍 Agent de Călătorii AI cu Microsoft Agent Framework (.NET)

## 📋 Prezentare Generală a Scenariului

Acest notebook demonstrează cum să construiești un agent inteligent pentru planificarea călătoriilor folosind Microsoft Agent Framework pentru .NET. Agentul poate genera automat itinerarii personalizate pentru excursii de o zi către destinații aleatorii din întreaga lume.

**Capabilități Cheie:**
- 🎲 **Selecție Aleatorie a Destinației**: Utilizează un instrument personalizat pentru a alege locuri de vacanță
- 🗺️ **Planificare Inteligentă a Excursiilor**: Creează itinerarii detaliate zi cu zi
- 🔄 **Streaming în Timp Real**: Suportă răspunsuri imediate și în flux continuu
- 🛠️ **Integrare cu Instrumente Personalizate**: Demonstrează cum să extinzi capabilitățile agentului

## 🔧 Arhitectura Tehnică

### Tehnologii de Bază
- **Microsoft Agent Framework**: Cea mai recentă implementare .NET pentru dezvoltarea agenților AI
- **Integrare cu Modelele GitHub**: Utilizează serviciul de inferență AI al GitHub
- **Compatibilitate cu API-ul OpenAI**: Folosește biblioteci client OpenAI cu puncte de acces personalizate
- **Configurare Securizată**: Gestionarea cheilor API bazată pe mediu

### Componente Cheie
1. **AIAgent**: Orchestratorul principal al agentului care gestionează fluxul conversației
2. **Instrumente Personalizate**: Funcția `GetRandomDestination()` disponibilă pentru agent
3. **Client de Chat**: Interfață de conversație susținută de Modelele GitHub
4. **Suport pentru Streaming**: Capacități de generare a răspunsurilor în timp real

### Model de Integrare
```mermaid
graph LR
    A[User Request] --> B[AI Agent]
    B --> C[GitHub Models API]
    B --> D[GetRandomDestination Tool]
    C --> E[Travel Itinerary]
    D --> E
```

## 🚀 Începeți

**Prerechizite:**
- .NET 9.0 sau mai recent
- Token de acces API pentru Modelele GitHub
- Variabile de mediu configurate în fișierul `.env`

**Variabile de Mediu Necesare:**
```env
GITHUB_TOKEN=your_github_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Rulați celulele de mai jos în ordine pentru a vedea agentul de călătorii în acțiune!

---

## .NET Single File App: AI Travel Agent Example

See `01-dotnet-agent-framework.cs` for the complete runnable code sample.

Rulați exemplul de cod de mai jos:

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
