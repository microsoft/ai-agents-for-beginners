# 🔍 Explorarea Microsoft Agent Framework - Agent de bază (.NET)

## 📋 Obiective de învățare

Acest exemplu explorează conceptele fundamentale ale Microsoft Agent Framework printr-o implementare de agent de bază în .NET. Vei învăța modelele esențiale ale agenților și vei înțelege cum funcționează agenții inteligenți „sub capotă” folosind C# și ecosistemul .NET.

### Ce vei descoperi

- 🏗️ **Arhitectura Agentului**: Înțelegerea structurii de bază a agenților AI în .NET
- 🛠️ **Integrare cu unelte**: Cum folosesc agenții funcții externe pentru a-și extinde capabilitățile  
- 💬 **Fluxul conversației**: Gestionarea conversațiilor multi-turn și a contextului prin managementul firelor
- 🔧 **Modele de configurare**: Cele mai bune practici pentru configurarea și gestionarea agenților în .NET

## 🎯 Concepte cheie acoperite

### Principiile cadrului agentic

- **Autonomie**: Cum iau agenții decizii independente folosind abstracții AI din .NET
- **Reactivitate**: Răspunderea la schimbările din mediu și la intrările utilizatorilor
- **Proactivitate**: Inițiativa bazată pe obiective și context
- **Abilitate socială**: Interacțiunea prin limbaj natural în fire de conversație

### Componente tehnice

- **AIAgent**: Orchestrarea principală a agentului și gestionarea conversațiilor (.NET)
- **Funcții Tool**: Extinderea capabilităților agentului cu metode și atribute C#
- **Integrare Azure OpenAI**: Folosirea modelelor de limbaj prin Azure OpenAI Responses API
- **Configurare securizată**: Gestionarea punctelor finale pe baza mediului

## 🔧 Stivă tehnologică

### Tehnologii de bază

- Microsoft Agent Framework (.NET)
- Integrare Azure OpenAI (Responses API)
- Modele client Azure.AI.OpenAI
- Configurare pe bază de mediu cu DotNetEnv

### Capabilități ale agentului

- Înțelegerea și generarea limbajului natural
- Apelarea funcțiilor și utilizarea uneltelor cu atribute C#
- Răspunsuri conștiente de context prin sesiuni conversaționale
- Arhitectură extensibilă cu modele de injecție de dependență

## 📚 Compararea cadrelor

Acest exemplu demonstrează abordarea Microsoft Agent Framework comparativ cu alte cadre agentice:

| Caracteristică | Microsoft Agent Framework | Alte cadre |
|---------|-------------------------|------------------|
| **Integrare** | Ecosistem Microsoft nativ | Compatibilitate variată |
| **Simplitate** | API curat, intuitiv | Configurare adesea complexă |
| **Extensibilitate** | Integrare ușoară a uneltelor | Depinde de cadru |
| **Pregătit pentru întreprinderi** | Conceput pentru producție | Varietate în funcție de cadru |

## 🚀 Început rapid

### Cerințe preliminare

- [SDK .NET 10](https://dotnet.microsoft.com/download/dotnet/10.0) sau versiune mai nouă
- Un [abonament Azure](https://azure.microsoft.com/free/) cu o resursă Azure OpenAI și o implementare a modelului
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — conectare cu `az login`

### Variabile de mediu necesare

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Apoi conectați-vă pentru ca AzureCliCredential să poată obține un token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Apoi autentificați-vă pentru ca AzureCliCredential să poată obține un token
az login
```

### Exemplu de cod

Pentru a rula exemplul de cod,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Sau folosind dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Vezi [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) pentru codul complet.

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

## 🎓 Concluzii cheie

1. **Arhitectura agentului**: Microsoft Agent Framework oferă o abordare curată și sigură tipizat pentru construirea agenților AI în .NET
2. **Integrarea uneltelor**: Funcțiile decorate cu atribute `[Description]` devin unelte disponibile pentru agent
3. **Contextul conversației**: Managementul sesiunilor permite conversații multi-turn cu conștientizare completă a contextului
4. **Gestionarea configurației**: Variabilele de mediu și gestionarea securizată a acreditărilor respectă cele mai bune practici .NET
5. **Azure OpenAI Responses API**: Agentul folosește Azure OpenAI Responses API prin SDK-ul Azure.AI.OpenAI

## 🔗 Resurse suplimentare

- [Documentația Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI în Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [Aplicații .NET Single File](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->