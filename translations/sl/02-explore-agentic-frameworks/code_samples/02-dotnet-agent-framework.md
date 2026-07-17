# 🔍 Raziskovanje Microsoft Agent Framework - Osnovni agent (.NET)

## 📋 Cilji učenja

Ta primer raziskuje temeljne pojme Microsoft Agent Framework prek osnovne implementacije agenta v .NET. Naučili se boste osnovnih vzorcev agentov in razumeli, kako delujejo inteligentni agenti pod pokrovom z uporabo C# in .NET ekosistema.

### Kaj boste odkrili

- 🏗️ **Arhitektura agenta**: Razumevanje osnovne strukture AI agentov v .NET
- 🛠️ **Integracija orodij**: Kako agenti uporabljajo zunanje funkcije za razširitev zmogljivosti  
- 💬 **Potek pogovora**: Upravljanje večkratnih pogovorov in konteksta z upravljanjem niti
- 🔧 **Vzorci konfiguracije**: Najboljše prakse za nastavitev in upravljanje agenta v .NET

## 🎯 Ključni pojmi, zajeti

### Principi agentnega okvira

- **Avtonomija**: Kako agenti sprejemajo neodvisne odločitve z uporabo abstrakcij AI v .NET
- **Reaktivnost**: Odzivanje na spremembe v okolju in uporabniške vnose
- **Proaktivnost**: Prevzemanje pobude glede na cilje in kontekst
- **Družabne sposobnosti**: Interakcija prek naravnega jezika z nitmi pogovora

### Tehnične komponente

- **AIAgent**: Osnovna orkestracija agenta in upravljanje pogovorov (.NET)
- **Funkcije orodij**: Razširitev zmožnosti agenta s C# metodami in atributi
- **Integracija Azure OpenAI**: Izraba jezikovnih modelov prek Azure OpenAI Responses API
- **Varnostna konfiguracija**: Upravljanje točk dostopa na podlagi okolja

## 🔧 Tehnični sklad

### Jedrne tehnologije

- Microsoft Agent Framework (.NET)
- Integracija Azure OpenAI (Responses API)
- Vzorci za odjemalca Azure.AI.OpenAI
- Konfiguracija na osnovi okolja z DotNetEnv

### Zmožnosti agenta

- Razumevanje in generiranje naravnega jezika
- Klicanje funkcij in uporaba orodij z atributi C#
- Odzivi, ki upoštevajo kontekst z sejami pogovora
- Razširljiva arhitektura z vzorci injiciranja odvisnosti

## 📚 Primerjava okvirjev

Ta primer prikazuje pristop Microsoft Agent Framework v primerjavi z drugimi agentnimi okviri:

| Značilnost | Microsoft Agent Framework | Drugi okviri |
|---------|-------------------------|------------------|
| **Integracija** | Nativni Microsoft ekosistem | Raznolika združljivost |
| **Preprostost** | Čist, intuitiven API | Pogosto zapletena nastavitev |
| **Razširljivost** | Enostavna integracija orodij | Odvisno od ogrodja |
| **Primeren za podjetja** | Zgrajen za produkcijo | Različno glede na okvir |

## 🚀 Začetek

### Predpogoji

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ali novejši
- [Azure naročnina](https://azure.microsoft.com/free/) z Azure OpenAI virom in nameščeno modelno implementacijo
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — prijavite se z `az login`

### Potrebne okoljske spremenljivke

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# Nato se prijavite, da lahko AzureCliCredential pridobi žeton
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# Nato se prijavite, da bo AzureCliCredential lahko pridobil žeton
az login
```

### Vzorec kode

Za poganjanje primerka kode,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Ali z uporabo ukazne vrstice dotnet:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Oglejte si [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) za popolno kodo.

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4.1-mini";

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

## 🎓 Ključne ugotovitve

1. **Arhitektura agenta**: Microsoft Agent Framework nudi čist, tipno varen pristop k gradnji AI agentov v .NET
2. **Integracija orodij**: Funkcije, opremljene z atributi `[Description]`, postanejo na voljo kot orodja za agenta
3. **Kontekst pogovora**: Upravljanje sej omogoča večkrožne pogovore s popolnim zavedanjem konteksta
4. **Upravljanje konfiguracije**: Okoljske spremenljivke in varno ravnanje s poverilnicami sledijo najboljšim praksam .NET
5. **Azure OpenAI Responses API**: Agent uporablja Azure OpenAI Responses API preko Azure.AI.OpenAI SDK

## 🔗 Dodatni viri

- [Dokumentacija Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI v Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET enojne datoteke aplikacije](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->