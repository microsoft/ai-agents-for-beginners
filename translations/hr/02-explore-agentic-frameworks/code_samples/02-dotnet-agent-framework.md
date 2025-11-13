<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T14:24:44+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "hr"
}
-->
# 🔍 Istraživanje Microsoft Agent Frameworka - Osnovni Agent (.NET)

## 📋 Ciljevi učenja

Ovaj primjer istražuje temeljne koncepte Microsoft Agent Frameworka kroz implementaciju osnovnog agenta u .NET-u. Naučit ćete osnovne obrasce agentnog rada i razumjeti kako inteligentni agenti funkcioniraju "ispod haube" koristeći C# i .NET ekosustav.

### Što ćete otkriti

- 🏗️ **Arhitektura agenta**: Razumijevanje osnovne strukture AI agenata u .NET-u  
- 🛠️ **Integracija alata**: Kako agenti koriste vanjske funkcije za proširenje mogućnosti  
- 💬 **Tijek razgovora**: Upravljanje višestrukim razgovorima i kontekstom uz upravljanje nitima  
- 🔧 **Obrasci konfiguracije**: Najbolje prakse za postavljanje i upravljanje agentima u .NET-u  

## 🎯 Ključni koncepti

### Načela Agent Frameworka

- **Autonomija**: Kako agenti donose neovisne odluke koristeći .NET AI apstrakcije  
- **Reaktivnost**: Reagiranje na promjene u okruženju i korisničke unose  
- **Proaktivnost**: Poduzimanje inicijative na temelju ciljeva i konteksta  
- **Društvena sposobnost**: Interakcija putem prirodnog jezika s nitima razgovora  

### Tehničke komponente

- **AIAgent**: Orkestracija agenta i upravljanje razgovorima (.NET)  
- **Funkcije alata**: Proširenje mogućnosti agenta pomoću C# metoda i atributa  
- **Integracija s OpenAI**: Korištenje jezičnih modela putem standardiziranih .NET API-ja  
- **Sigurna konfiguracija**: Upravljanje API ključevima na temelju okruženja  

## 🔧 Tehnički paket

### Osnovne tehnologije

- Microsoft Agent Framework (.NET)  
- Integracija s GitHub Models API  
- OpenAI-kompatibilni klijentski obrasci  
- Konfiguracija na temelju okruženja s DotNetEnv  

### Sposobnosti agenta

- Razumijevanje i generiranje prirodnog jezika  
- Pozivanje funkcija i korištenje alata s C# atributima  
- Odgovori svjesni konteksta s nitima razgovora  
- Proširiva arhitektura s obrascima ubrizgavanja ovisnosti  

## 📚 Usporedba okvira

Ovaj primjer prikazuje pristup Microsoft Agent Frameworka u usporedbi s drugim agentnim okvirima:

| Značajka | Microsoft Agent Framework | Drugi okviri |
|----------|---------------------------|--------------|
| **Integracija** | Izvorni Microsoft ekosustav | Različita kompatibilnost |
| **Jednostavnost** | Čist, intuitivan API | Često složeno postavljanje |
| **Proširivost** | Jednostavna integracija alata | Ovisno o okviru |
| **Spremnost za poduzeća** | Dizajniran za produkciju | Varira ovisno o okviru |

## 🚀 Početak rada

### Preduvjeti

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ili noviji  
- [Pristupni token za GitHub Models API](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### Potrebne varijable okruženja

```bash
# zsh/bash
export GH_TOKEN=<your_github_token>
export GH_ENDPOINT=https://models.github.ai/inference
export GH_MODEL_ID=openai/gpt-5-mini
```
  
```powershell
# PowerShell
$env:GH_TOKEN = "<your_github_token>"
$env:GH_ENDPOINT = "https://models.github.ai/inference"
$env:GH_MODEL_ID = "openai/gpt-5-mini"
```
  

### Primjer koda

Za pokretanje primjera koda,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
Ili pomoću dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
Pogledajte [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) za kompletan kod.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*

using System.ClientModel;
using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using OpenAI;

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

// Extract configuration from environment variables
// Retrieve the GitHub Models API endpoint, defaults to https://models.github.ai/inference if not specified
// Retrieve the model ID, defaults to openai/gpt-5-mini if not specified
// Retrieve the GitHub token for authentication, throws exception if not specified
var github_endpoint = Environment.GetEnvironmentVariable("GH_ENDPOINT") ?? "https://models.github.ai/inference";
var github_model_id = Environment.GetEnvironmentVariable("GH_MODEL_ID") ?? "openai/gpt-5-mini";
var github_token = Environment.GetEnvironmentVariable("GH_TOKEN") ?? throw new InvalidOperationException("GH_TOKEN is not set.");

// Configure OpenAI Client Options
// Create configuration options to point to GitHub Models endpoint
// This redirects OpenAI client calls to GitHub's model inference service
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
// Create OpenAI client using GitHub token for authentication
// Configure it to use GitHub Models endpoint instead of OpenAI directly
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

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
// Initialize complete agent pipeline: OpenAI client → Chat client → AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
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
  

## 🎓 Ključne lekcije

1. **Arhitektura agenta**: Microsoft Agent Framework pruža čist, tip-siguran pristup izgradnji AI agenata u .NET-u  
2. **Integracija alata**: Funkcije označene atributima `[Description]` postaju dostupni alati za agenta  
3. **Kontekst razgovora**: Upravljanje nitima omogućuje višestruke razgovore s potpunom sviješću o kontekstu  
4. **Upravljanje konfiguracijom**: Varijable okruženja i sigurno rukovanje vjerodajnicama slijede najbolje prakse u .NET-u  
5. **Kompatibilnost s OpenAI**: Integracija s GitHub Models radi besprijekorno putem OpenAI-kompatibilnih API-ja  

## 🔗 Dodatni resursi

- [Microsoft Agent Framework Dokumentacija](https://learn.microsoft.com/agent-framework)  
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->