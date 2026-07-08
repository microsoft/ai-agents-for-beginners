# 🛠️ Avanceret værktøjsbrug med Azure OpenAI (Responses API) (.NET)

## 📋 Læringsmål

Denne notebook demonstrerer virksomhedsklare integrationsmønstre for værktøjer ved brug af Microsoft Agent Framework i .NET med Azure OpenAI (Responses API). Du vil lære at bygge sofistikerede agenter med flere specialiserede værktøjer ved at udnytte C#'s stærke typesystem og .NET's virksomhedsfunktioner.

### Avancerede værktøjsfunktioner du vil mestre

- 🔧 **Multi-Værktøjs Arkitektur**: Opbygge agenter med flere specialiserede kapaciteter
- 🎯 **Typesikker værktøjsudførelse**: Udnyttelse af C#'s kompileringstid validering
- 📊 **Erhvervsværktøjsmønstre**: Produktionsklar værktøjsdesign og fejlhåndtering
- 🔗 **Værktøjssammensætning**: Kombinere værktøjer til komplekse forretningsworkflows

## 🎯 Fordele ved .NET værktøjsarkitektur

### Virksomhedsværktøjsfunktioner

- **Kompileringstidsvalidering**: Stærk typning sikrer korrekthed af værktøjsparametre
- **Dependency Injection**: IoC-container integration til værktøjsstyring
- **Async/Await-mønstre**: Ikke-blokerende værktøjsudførelse med korrekt ressourcestyring
- **Struktureret logging**: Indbygget logningsintegration til overvågning af værktøjsudførelse

### Produktionsklare mønstre

- **Exception-håndtering**: Omfattende fejlhåndtering med typesikre undtagelser
- **Ressourcestyring**: Korrekta oprydningsmønstre og hukommelsesstyring
- **Ydelsesovervågning**: Indbyggede metrics og ydelsesmålinger
- **Konfigurationsstyring**: Typesikker konfiguration med validering

## 🔧 Teknisk arkitektur

### Kerne .NET værktøjskomponenter

- **Microsoft.Extensions.AI**: Enhedsbaseret værktøjsabstraktionslag
- **Microsoft.Agents.AI**: Virksomhedsklart værktøjsorkestrering
- **Azure OpenAI (Responses API)**: Højtydende API-klient med forbindelse pooling

### Værktøjsudførelsespipeline

```mermaid
graph LR
    A[Brugerforespørgsel] --> B[Agentanalyse]
    B --> C[Værktøjsvalg]
    C --> D[Typevalidering]
    B --> E[Parameterbinding]
    E --> F[Værktøjsudførelse]
    C --> F
    F --> G[Resultatbehandling]
    D --> G
    G --> H[Svar]
```

## 🛠️ Værktøjskategorier & mønstre

### 1. **Databehandlingsværktøjer**

- **Inputvalidering**: Stærk typning med dataannoteringer
- **Transformeringsoperationer**: Typesikker datakonvertering og formatering
- **Forretningslogik**: Domænespecifikke beregnings- og analyseværktøjer
- **Outputformatering**: Struktureret responsgenerering

### 2. **Integrationsværktøjer**

- **API-connectorer**: RESTful serviceintegration med HttpClient
- **Databaseværktøjer**: Entity Framework integration til dataadgang
- **Filoperationer**: Sikker filsystemoperation med validering
- **Eksterne tjenester**: Tredjeparts serviceintegrationsmønstre

### 3. **Nyttige værktøjer**

- **Tekstbehandling**: Strengmanipulation og formatteringsværktøjer
- **Dato/tid operationer**: Kulturbevidste dato/tid-beregninger
- **Matematiske værktøjer**: Præcisionsberegninger og statistiske operationer
- **Valideringsværktøjer**: Forretningsregelvalidering og dataverifikation

Klar til at bygge virksomhedsklare agenter med kraftfulde, typesikre værktøjsfunktioner i .NET? Lad os designe nogle professionelle løsninger! 🏢⚡

## 🚀 Kom godt i gang

### Forudsætninger

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller nyere
- Et [Azure-abonnement](https://azure.microsoft.com/free/) med en Azure OpenAI-ressource og en modeludrulning
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — log ind med `az login`

### Påkrævede miljøvariabler

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Log derefter ind, så AzureCliCredential kan få en token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Log ind, så AzureCliCredential kan få en token
az login
```

### Eksempelkode

For at køre kodeeksemplet,

```bash
# zsh/bash
chmod +x ./04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Eller brug dotnet CLI:

```bash
dotnet run ./04-dotnet-agent-framework.cs
```

Se [`04-dotnet-agent-framework.cs`](../../../../04-tool-use/code_samples/04-dotnet-agent-framework.cs) for komplet kode.

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4o-mini";

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
    .GetOpenAIResponseClient(deployment)
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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->