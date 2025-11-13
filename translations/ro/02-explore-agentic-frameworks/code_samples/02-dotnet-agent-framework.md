<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T14:02:24+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "ro"
}
-->
# 🔍 Explorarea Microsoft Agent Framework - Agent de bază (.NET)

## 📋 Obiective de învățare

Acest exemplu explorează conceptele fundamentale ale Microsoft Agent Framework printr-o implementare de bază a unui agent în .NET. Vei învăța modele agentice de bază și vei înțelege cum funcționează agenții inteligenți în profunzime folosind C# și ecosistemul .NET.

### Ce vei descoperi

- 🏗️ **Arhitectura agentului**: Înțelegerea structurii de bază a agenților AI în .NET  
- 🛠️ **Integrarea instrumentelor**: Cum agenții utilizează funcții externe pentru a-și extinde capabilitățile  
- 💬 **Fluxul conversației**: Gestionarea conversațiilor multi-turn și a contextului cu managementul thread-urilor  
- 🔧 **Modele de configurare**: Cele mai bune practici pentru configurarea și gestionarea agenților în .NET  

## 🎯 Concepte cheie abordate

### Principiile Framework-ului Agentic

- **Autonomie**: Cum agenții iau decizii independente folosind abstracții AI din .NET  
- **Reactivitate**: Răspunsul la schimbările de mediu și la intrările utilizatorului  
- **Proactivitate**: Inițiativa bazată pe obiective și context  
- **Abilitate socială**: Interacțiunea prin limbaj natural cu thread-uri conversaționale  

### Componente tehnice

- **AIAgent**: Orchestrarea principală a agentului și gestionarea conversațiilor (.NET)  
- **Funcții de instrumente**: Extinderea capabilităților agentului cu metode și atribute C#  
- **Integrarea OpenAI**: Utilizarea modelelor de limbaj prin API-uri standardizate .NET  
- **Configurare sigură**: Gestionarea cheilor API bazată pe mediu  

## 🔧 Stack tehnic

### Tehnologii de bază

- Microsoft Agent Framework (.NET)  
- Integrarea API-ului GitHub Models  
- Modele de client compatibile cu OpenAI  
- Configurare bazată pe mediu cu DotNetEnv  

### Capabilitățile agentului

- Înțelegerea și generarea limbajului natural  
- Apelarea funcțiilor și utilizarea instrumentelor cu atribute C#  
- Răspunsuri conștiente de context cu thread-uri conversaționale  
- Arhitectură extensibilă cu modele de injecție de dependențe  

## 📚 Compararea Framework-urilor

Acest exemplu demonstrează abordarea Microsoft Agent Framework comparativ cu alte framework-uri agentice:

| Caracteristică | Microsoft Agent Framework | Alte Framework-uri |
|----------------|---------------------------|--------------------|
| **Integrare** | Ecosistem nativ Microsoft | Compatibilitate variată |
| **Simplitate** | API curat, intuitiv | Configurare adesea complexă |
| **Extensibilitate** | Integrare ușoară a instrumentelor | Dependent de framework |
| **Pregătit pentru enterprise** | Construit pentru producție | Variază în funcție de framework |

## 🚀 Început rapid

### Cerințe preliminare

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) sau mai recent  
- [Token de acces API GitHub Models](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### Variabile de mediu necesare

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
  

### Cod exemplu

Pentru a rula exemplul de cod,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
Sau folosind CLI-ul dotnet:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
Vezi [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) pentru codul complet.

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
  

## 🎓 Concluzii cheie

1. **Arhitectura agentului**: Microsoft Agent Framework oferă o abordare curată și sigură pentru construirea agenților AI în .NET  
2. **Integrarea instrumentelor**: Funcțiile decorate cu atribute `[Description]` devin instrumente disponibile pentru agent  
3. **Contextul conversației**: Managementul thread-urilor permite conversații multi-turn cu conștientizare completă a contextului  
4. **Gestionarea configurării**: Variabilele de mediu și gestionarea sigură a acreditivelor urmează cele mai bune practici .NET  
5. **Compatibilitate OpenAI**: Integrarea GitHub Models funcționează perfect prin API-uri compatibile OpenAI  

## 🔗 Resurse suplimentare

- [Documentația Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)  
- [Marketplace GitHub Models](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->