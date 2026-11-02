# 🔍 Istraživanje Microsoft Agent Frameworka - Osnovni agent (.NET)

## 📋 Ciljevi učenja

Ovaj primjer istražuje temeljne koncepte Microsoft Agent Frameworka kroz osnovnu implementaciju agenta u .NET-u. Naučit ćete osnovne agentne uzorke i razumjeti kako inteligentni agenti funkcioniraju „ispod haube“ koristeći C# i .NET ekosustav.

### Što ćete otkriti

- 🏗️ **Arhitektura agenta**: Razumijevanje osnovne strukture AI agenata u .NET-u
- 🛠️ **Integracija alata**: Kako agenti koriste vanjske funkcije za proširenje mogućnosti  
- 💬 **Tok razgovora**: Upravljanje višekratnim okretajima razgovora i kontekstom pomoću upravljanja niti
- 🔧 **Uzorki konfiguracije**: Najbolje prakse za postavljanje i upravljanje agentom u .NET-u

## 🎯 Ključni obrađeni koncepti

### Principi agentnog okvira

- **Autonomija**: Kako agenti donose neovisne odluke koristeći .NET AI apstrakcije
- **Reaktivnost**: Odgovaranje na promjene u okolišu i korisničke unose
- **Proaktivnost**: Preuzimanje inicijative na temelju ciljeva i konteksta
- **Socijalna sposobnost**: Interakcija kroz prirodni jezik s nitima razgovora

### Tehničke komponente

- **AIAgent**: Osnovna orkestracija agenta i upravljanje razgovorom (.NET)
- **Funkcije alata**: Proširenje mogućnosti agenta C# metodama i atributima
- **Integracija Azure OpenAI**: Korištenje jezičnih modela putem Azure OpenAI Responses API-ja
- **Sigurna konfiguracija**: Upravljanje krajnjom točkom na temelju okoline

## 🔧 Tehnička tehnologija

### Osnovne tehnologije

- Microsoft Agent Framework (.NET)
- Integracija Azure OpenAI (Responses API)
- Obrasci klijenta Azure.AI.OpenAI
- Konfiguracija na temelju okoline uz DotNetEnv

### Mogućnosti agenta

- Razumijevanje i generiranje prirodnog jezika
- Pozivanje funkcija i korištenje alata s C# atributima
- Odgovori osviješteni za kontekst uz sesije razgovora
- Proširiva arhitektura s obrascima za injektiranje ovisnosti

## 📚 Usporedba okvira

Ovaj primjer prikazuje pristup Microsoft Agent Frameworka u usporedbi s drugim agentnim okvirima:

| Značajka | Microsoft Agent Framework | Drugi okviri |
|---------|-------------------------|------------------|
| **Integracija** | Izvorni Microsoftov ekosustav | Raznolika kompatibilnost |
| **Jednostavnost** | Čist, intuitivan API | Često složena postava |
| **Proširivost** | Jednostavna integracija alata | Ovisi o okviru |
| **Spreman za poduzeća** | Izgrađen za produkciju | Varira ovisno o okviru |

## 🚀 Početak rada

### Preduvjeti

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ili noviji
- [Pretplata na Azure](https://azure.microsoft.com/free/) s Azure OpenAI resursom i rasporedom modela
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — prijavite se s `az login`

### Potrebne varijable okoline

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Zatim se prijavite kako bi AzureCliCredential mogao dobiti token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Zatim se prijavite kako bi AzureCliCredential mogao dobiti token
az login
```

### Primjer koda

Za pokretanje primjera koda,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Ili korištenjem dotnet CLI-ja:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Pogledajte [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) za kompletan kod.

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

## 🎓 Ključne spoznaje

1. **Arhitektura agenta**: Microsoft Agent Framework nudi čist, tip siguran pristup izgradnji AI agenata u .NET-u
2. **Integracija alata**: Funkcije označene atributima `[Description]` postaju dostupni alati za agenta
3. **Kontekst razgovora**: Upravljanje sesijama omogućuje višekratne okretaje razgovora s punim osvještavanjem konteksta
4. **Upravljanje konfiguracijom**: Varijable okoline i sigurno rukovanje vjerodajnicama prate najbolje prakse .NET-a
5. **Azure OpenAI Responses API**: Agent koristi Azure OpenAI Responses API kroz Azure.AI.OpenAI SDK

## 🔗 Dodatni resursi

- [Dokumentacija Microsoft Agent Frameworka](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI u Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET aplikacije u jednoj datoteci](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->