<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T14:31:09+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "sl"
}
-->
# 🔍 Raziskovanje Microsoft Agent Framework - Osnovni agent (.NET)

## 📋 Cilji učenja

Ta primer raziskuje temeljne koncepte Microsoft Agent Frameworka skozi implementacijo osnovnega agenta v .NET. Naučili se boste osnovnih vzorcev agentov in razumeli, kako inteligentni agenti delujejo v ozadju z uporabo C# in ekosistema .NET.

### Kaj boste odkrili

- 🏗️ **Arhitektura agenta**: Razumevanje osnovne strukture AI agentov v .NET
- 🛠️ **Integracija orodij**: Kako agenti uporabljajo zunanje funkcije za razširitev zmogljivosti  
- 💬 **Tok pogovora**: Upravljanje večkratnih pogovorov in konteksta z upravljanjem niti
- 🔧 **Vzorce konfiguracije**: Najboljše prakse za nastavitev in upravljanje agentov v .NET

## 🎯 Ključni koncepti

### Načela agentnega okvira

- **Avtonomija**: Kako agenti sprejemajo neodvisne odločitve z uporabo .NET AI abstrakcij
- **Reaktivnost**: Odzivanje na spremembe okolja in uporabniške vnose
- **Proaktivnost**: Pobuda na podlagi ciljev in konteksta
- **Socialna sposobnost**: Interakcija skozi naravni jezik z nitmi pogovora

### Tehnične komponente

- **AIAgent**: Osnovna orkestracija agenta in upravljanje pogovorov (.NET)
- **Funkcije orodij**: Razširitev zmogljivosti agenta z metodami in atributi v C#
- **Integracija OpenAI**: Uporaba jezikovnih modelov preko standardiziranih .NET API-jev
- **Varna konfiguracija**: Upravljanje API ključev na podlagi okolja

## 🔧 Tehnični sklad

### Osnovne tehnologije

- Microsoft Agent Framework (.NET)
- Integracija GitHub Models API
- Vzorec odjemalca, združljiv z OpenAI
- Konfiguracija na podlagi okolja z DotNetEnv

### Zmožnosti agenta

- Razumevanje in generiranje naravnega jezika
- Klicanje funkcij in uporaba orodij z atributi v C#
- Odzivi, ki se zavedajo konteksta, z nitmi pogovora
- Razširljiva arhitektura z vzorci za vbrizgavanje odvisnosti

## 📚 Primerjava okvirov

Ta primer prikazuje pristop Microsoft Agent Frameworka v primerjavi z drugimi agentnimi okviri:

| Funkcija | Microsoft Agent Framework | Drugi okviri |
|----------|---------------------------|--------------|
| **Integracija** | Domači Microsoft ekosistem | Različna združljivost |
| **Enostavnost** | Čist, intuitiven API | Pogosto zapletena nastavitev |
| **Razširljivost** | Enostavna integracija orodij | Odvisno od okvira |
| **Pripravljenost za podjetja** | Zasnovano za produkcijo | Odvisno od okvira |

## 🚀 Začetek

### Predpogoji

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ali novejši
- [Dostopni žeton za GitHub Models API](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)

### Zahtevane okoljske spremenljivke

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

### Vzorčna koda

Za zagon primerne kode,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Ali z uporabo dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Oglejte si [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) za celotno kodo.

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

## 🎓 Ključne ugotovitve

1. **Arhitektura agenta**: Microsoft Agent Framework ponuja čist, tipno varen pristop k gradnji AI agentov v .NET
2. **Integracija orodij**: Funkcije, označene z atributom `[Description]`, postanejo dostopna orodja za agenta
3. **Kontekst pogovora**: Upravljanje niti omogoča večkratne pogovore z popolno zavednostjo konteksta
4. **Upravljanje konfiguracije**: Okoljske spremenljivke in varno upravljanje poverilnic sledijo najboljšim praksam .NET
5. **Združljivost z OpenAI**: Integracija GitHub Models deluje brezhibno preko API-jev, združljivih z OpenAI

## 🔗 Dodatni viri

- [Dokumentacija Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Tržnica GitHub Models](https://github.com/marketplace?type=models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET aplikacije v eni datoteki](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->