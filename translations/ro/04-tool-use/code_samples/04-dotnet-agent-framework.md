# 🛠️ Utilizare Avansată a Instrumentelor cu Azure OpenAI (Responses API) (.NET)

## 📋 Obiective de Învățare

Acest notebook demonstrează modele de integrare a instrumentelor de nivel enterprise folosind Microsoft Agent Framework în .NET cu Azure OpenAI (Responses API). Veți învăța să construiți agenți sofisticați cu multiple instrumente specializate, valorificând tipizarea puternică a C# și caracteristicile enterprise ale .NET.

### Capacități Avansate ale Instrumentelor pe care le Veți Stăpâni

- 🔧 **Arhitectură Multi-Instrument**: Construirea de agenți cu multiple capabilități specializate
- 🎯 **Executare Tip-Sigură a Instrumentelor**: Valorificarea validării la compilare în C#
- 📊 **Modele de Instrumente Enterprise**: Proiectarea instrumentelor pregătite pentru producție și gestionarea erorilor
- 🔗 **Compoziția Instrumentelor**: Combinarea instrumentelor pentru fluxuri complexe de lucru de business

## 🎯 Beneficiile Arhitecturii Instrumentelor .NET

### Caracteristici Enterprise ale Instrumentelor

- **Validare la Timp de Compilare**: Tipizare puternică asigurând corectitudinea parametrilor instrumentelor
- **Injecție de Dependență**: Integrarea containerului IoC pentru managementul instrumentelor
- **Modele Async/Await**: Executare non-blocantă a instrumentelor cu management corespunzător al resurselor
- **Logging Structurat**: Integrare încorporată pentru monitorizarea execuției instrumentelor

### Modele Pregătite pentru Producție

- **Gestionarea Excepțiilor**: Management complet al erorilor cu excepții tipizate
- **Managementul Resurselor**: Modele corecte de eliberare și management al memoriei
- **Monitorizarea Performanței**: Metrici încorporate și contorizatoare de performanță
- **Managementul Configurației**: Configurare tip-sigură cu validare

## 🔧 Arhitectura Tehnică

### Componente de Bază ale Instrumentelor .NET

- **Microsoft.Extensions.AI**: Strat unificat de abstractizare a instrumentelor
- **Microsoft.Agents.AI**: Orchestrare de instrumente la nivel enterprise
- **Azure OpenAI (Responses API)**: Client API de înaltă performanță cu connection pooling

### Pipeline-ul de Execuție al Instrumentelor

```mermaid
graph LR
    A[Cerere utilizator] --> B[Analiză agent]
    B --> C[Selecția uneltei]
    C --> D[Validare tip]
    B --> E[Legare parametri]
    E --> F[Executarea uneltei]
    C --> F
    F --> G[Procesarea rezultatului]
    D --> G
    G --> H[Răspuns]
```

## 🛠️ Categorii & Modele de Instrumente

### 1. **Instrumente pentru Procesarea Datelor**

- **Validarea Intrărilor**: Tipizare puternică cu adnotări de date
- **Operațiuni de Transformare**: Conversie și formatare a datelor tip-sigură
- **Logică de Business**: Instrumente de calcul și analiză specifice domeniului
- **Formatarea Ieșirilor**: Generare structurată a răspunsurilor

### 2. **Instrumente de Integrare** 

- **Conectori API**: Integrare servicii RESTful cu HttpClient
- **Instrumente de Bază de Date**: Integrare Entity Framework pentru accesul datelor
- **Operațiuni pe Fișiere**: Operații sigure pe sistemul de fișiere cu validare
- **Servicii Externe**: Modele de integrare a serviciilor terțe

### 3. **Instrumente Utilitare**

- **Procesarea Textului**: Utilitare pentru manipularea și formatarea șirurilor de caractere
- **Operațiuni Data/Timp**: Calculuri date/timp conștiente de cultură
- **Instrumente Matematice**: Calcul precis și operații statistice
- **Instrumente de Validare**: Validarea regulilor de business și verificarea datelor

Pregătit să construiți agenți enterprise cu capabilități puternice, tip-sigure în .NET? Haideți să arhitectăm soluții profesionale! 🏢⚡

## 🚀 Pornirea în Curs

### Cerințe Prealabile

- [SDK .NET 10](https://dotnet.microsoft.com/download/dotnet/10.0) sau versiune superioară
- Un [abonament Azure](https://azure.microsoft.com/free/) cu o resursă Azure OpenAI și un deployment de model
- Azure CLI-ul [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — autentificare cu `az login`

### Variabile de Mediu Necesare

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# Apoi autentifică-te ca AzureCliCredential să poată obține un token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# Apoi autentifică-te pentru ca AzureCliCredential să poată obține un token
az login
```

### Cod Exemplu

Pentru a rula exemplul de cod,

```bash
# zsh/bash
chmod +x ./04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Sau folosind CLI-ul dotnet:

```bash
dotnet run ./04-dotnet-agent-framework.cs
```

Vezi [`04-dotnet-agent-framework.cs`](../../../../04-tool-use/code_samples/04-dotnet-agent-framework.cs) pentru codul complet.

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

// Create New Conversation Session for Context Management
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
await using var session = await agent.CreateSessionAsync();

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->