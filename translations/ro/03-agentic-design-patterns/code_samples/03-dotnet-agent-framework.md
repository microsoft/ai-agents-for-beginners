# 🎨 Tipare de Proiectare Agentice cu Azure OpenAI (Responses API) (.NET)

## 📋 Obiective de Învățare

Acest exemplu demonstrează tipare de proiectare la nivel enterprise pentru construirea de agenți inteligenți folosind Microsoft Agent Framework în .NET cu integrarea Azure OpenAI (Responses API). Veți învăța tipare profesionale și abordări arhitecturale care fac agenții pregătiți pentru producție, ușor de întreținut și scalabili.

### Tipare de Proiectare Enterprise

- 🏭 **Factory Pattern**: Crearea standardizată a agenților cu injecție de dependență
- 🔧 **Builder Pattern**: Configurare și setup fluent al agentului
- 🧵 **Tipare Thread-Safe**: Management concurent al conversațiilor
- 📋 **Repository Pattern**: Management organizat al uneltelor și capabilităților

## 🎯 Beneficii Arhitecturale Specifice .NET

### Funcționalități Enterprise

- **Tipare puternice**: Validare la compilare și asistență IntelliSense
- **Dependență prin Injecție**: Integrare nativă a containerului DI
- **Managementul Configurației**: Pattern-uri IConfiguration și Options
- **Async/Await**: Suport nativ pentru programare asincronă

### Tipare pregătite pentru Producție

- **Integrare Logging**: Suport pentru ILogger și logging structurat
- **Health Checks**: Monitorizare și diagnosticare integrate
- **Validarea Configurației**: Tipare puternice cu adnotări de date
- **Gestionarea Erorilor**: Management structurat al excepțiilor

## 🔧 Arhitectură Tehnică

### Componente Cheie .NET

- **Microsoft.Extensions.AI**: Abstracții unificate pentru servicii AI
- **Microsoft.Agents.AI**: Framework de orchestrare a agenților enterprise
- **Azure OpenAI (Responses API)**: Tipare de client API de înaltă performanță
- **Sistemul de Configurație**: appsettings.json și integrare de mediu

### Implementarea Tiparelor de Proiectare

```mermaid
graph LR
    A[IServiceCollection] --> B[Constructor Agent]
    B --> C[Configurare]
    C --> D[Registrul Instrumentelor]
    D --> E[Agent AI]
```

## 🏗️ Tipare Enterprise Demonstrate

### 1. **Tipare Creationale**

- **Agent Factory**: Crearea centralizată a agenților cu configurare consistentă
- **Builder Pattern**: API fluent pentru configurări complexe ale agentului
- **Singleton Pattern**: Resurse partajate și managementul configurației
- **Dependență prin Injecție**: Decuplare slabă și testabilitate

### 2. **Tipare Comportamentale**

- **Strategy Pattern**: Strategii de execuție a uneltelor schimbabile
- **Command Pattern**: Operațiuni agent encapsulate cu undo/redo
- **Observer Pattern**: Management eveniment-driven al ciclului de viață al agentului
- **Template Method**: Fluxuri de lucru standardizate pentru execuția agentului

### 3. **Tipare Structurale**

- **Adapter Pattern**: Strat de integrare Azure OpenAI (Responses API)
- **Decorator Pattern**: Îmbunătățirea capabilităților agentului
- **Facade Pattern**: Interfețe simplificate pentru interacțiunea cu agentul
- **Proxy Pattern**: Încărcare leneșă și caching pentru performanță

## 📚 Principii de Proiectare .NET

### Principiile SOLID

- **Single Responsibility**: Fiecare componentă are un singur scop clar
- **Open/Closed**: Extensibil fără modificări
- **Liskov Substitution**: Implementări ale uneltelor bazate pe interfețe
- **Interface Segregation**: Interfețe concentrate și coerente
- **Dependency Inversion**: Dependență de abstractizări, nu de concreții

### Arhitectură Curată

- **Layer-ul Domain**: Abstracții de bază ale agenților și uneltelor
- **Layer-ul Aplicație**: Orchestrarea agenților și fluxurile de lucru
- **Layer-ul Infrastructură**: Integrarea Azure OpenAI (Responses API) și servicii externe
- **Layer-ul Prezentare**: Interacțiunea cu utilizatorul și formatarea răspunsurilor

## 🔒 Considerații Enterprise

### Securitate

- **Managementul Credentialelor**: Gestionarea securizată a cheilor API cu IConfiguration
- **Validarea Inputului**: Tipare puternice și validarea adnotărilor de date
- **Sanitizarea Outputului**: Procesare și filtrare securizată a răspunsurilor
- **Audit Logging**: Urmărirea completă a operațiunilor

### Performanță

- **Tipare Async**: Operațiuni I/O neblocante
- **Connection Pooling**: Management eficient al clientului HTTP
- **Caching**: Cache pentru răspunsuri pentru performanță îmbunătățită
- **Managementul Resurselor**: Tipare corecte de eliberare și curățare

### Scalabilitate

- **Siguranța pe Thread-uri**: Suport pentru execuție concurentă a agenților
- **Pooling de Resurse**: Utilizare eficientă a resurselor
- **Managementul Încărcării**: Limitarea ratei și gestionarea presiunii inverse
- **Monitorizare**: Metrici de performanță și verificări de sănătate

## 🚀 Implementare în Producție

- **Managementul Configurației**: Setări specifice mediului
- **Strategie de Logging**: Logging structurat cu ID-uri de corelare
- **Gestionarea Erorilor**: Gestionare globală a excepțiilor cu recuperare adecvată
- **Monitorizare**: Application insights și contoare de performanță
- **Testare**: Teste unitare, teste de integrare și tipare pentru testare de încărcare

Pregătit să construiți agenți inteligenți la nivel enterprise cu .NET? Hai să arhitecturăm ceva robust! 🏢✨

## 🚀 Începutul

### Precondiții

- [SDK .NET 10](https://dotnet.microsoft.com/download/dotnet/10.0) sau versiune superioară
- Un [abonament Azure](https://azure.microsoft.com/free/) cu o resursă Azure OpenAI și o implementare de model
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — autentificare cu `az login`

### Variabile de Mediu Necesare

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Apoi autentifică-te pentru ca AzureCliCredential să poată obține un token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Apoi autentifică-te pentru ca AzureCliCredential să poată obține un token
az login
```

### Cod Exemplu

Pentru a rula exemplul de cod,

```bash
# zsh/bash
chmod +x ./03-dotnet-agent-framework.cs
./03-dotnet-agent-framework.cs
```

Sau folosind CLI dotnet:

```bash
dotnet run ./03-dotnet-agent-framework.cs
```

Vezi [`03-dotnet-agent-framework.cs`](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs) pentru codul complet.

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

// Create New Conversation Session for Context Management
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
var session = await agent.CreateSessionAsync();

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