<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "91d6061e402489603f2ec8b528cae59b",
  "translation_date": "2025-11-18T17:38:45+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "sv"
}
-->
# 🛠️ Avancerad Verktygsanvändning med GitHub-modeller (.NET)

## 📋 Inlärningsmål

Den här notebooken visar integrationsmönster för verktyg på företagsnivå med hjälp av Microsoft Agent Framework i .NET tillsammans med GitHub-modeller. Du kommer att lära dig att bygga sofistikerade agenter med flera specialiserade verktyg, och dra nytta av C#'s starka typning och .NET:s företagsfunktioner.

### Avancerade Verktygsfunktioner Du Kommer Behärska

- 🔧 **Multi-verktygsarkitektur**: Bygga agenter med flera specialiserade funktioner
- 🎯 **Typ-säker verktygsanvändning**: Utnyttja C#'s validering vid kompilering
- 📊 **Företagsmönster för verktyg**: Produktionsklara verktygsdesign och felhantering
- 🔗 **Verktygskomposition**: Kombinera verktyg för komplexa affärsarbetsflöden

## 🎯 Fördelar med .NET Verktygsarkitektur

### Funktioner för Företagsverktyg

- **Validering vid kompilering**: Stark typning säkerställer korrekthet i verktygsparametrar
- **Dependency Injection**: IoC-containerintegration för verktygshantering
- **Async/Await-mönster**: Icke-blockerande verktygsanvändning med korrekt resursförvaltning
- **Strukturerad loggning**: Inbyggd loggningsintegration för övervakning av verktygsanvändning

### Produktionsklara Mönster

- **Felhantering**: Omfattande felhantering med typade undantag
- **Resurshantering**: Korrekt hantering av resurser och minnesförvaltning
- **Prestandaövervakning**: Inbyggda mätvärden och prestandaräknare
- **Konfigurationshantering**: Typ-säker konfiguration med validering

## 🔧 Teknisk Arkitektur

### Kärnkomponenter i .NET Verktyg

- **Microsoft.Extensions.AI**: Enhetligt abstraktionslager för verktyg
- **Microsoft.Agents.AI**: Verktygsorkestrering på företagsnivå
- **GitHub-modeller Integration**: Högpresterande API-klient med anslutningspoolning

### Verktygsanvändningspipeline

```mermaid
graph LR
    A[User Request] --> B[Agent Analysis]
    B --> C[Tool Selection]
    C --> D[Type Validation]
    B --> E[Parameter Binding]
    E --> F[Tool Execution]
    C --> F
    F --> G[Result Processing]
    D --> G
    G --> H[Response]
```

## 🛠️ Verktygskategorier & Mönster

### 1. **Databehandlingsverktyg**

- **Inmatningsvalidering**: Stark typning med dataannoteringar
- **Transformationsoperationer**: Typ-säker datakonvertering och formatering
- **Affärslogik**: Domänspecifika beräkningar och analysverktyg
- **Utdataformatering**: Generering av strukturerade svar

### 2. **Integrationsverktyg**

- **API-anslutningar**: RESTful-tjänsteintegration med HttpClient
- **Databasverktyg**: Entity Framework-integration för dataåtkomst
- **Filoperationer**: Säker filsystemhantering med validering
- **Externa tjänster**: Mönster för integration av tredjepartstjänster

### 3. **Hjälpverktyg**

- **Textbehandling**: Strängmanipulation och formateringsverktyg
- **Datum/tidsoperationer**: Kulturmedvetna datum/tidsberäkningar
- **Matematiska verktyg**: Precisionsberäkningar och statistiska operationer
- **Valideringsverktyg**: Validering av affärsregler och dataverifiering

Redo att bygga agenter på företagsnivå med kraftfulla, typ-säkra verktygsfunktioner i .NET? Låt oss skapa professionella lösningar! 🏢⚡

## 🚀 Kom igång

### Förutsättningar

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller senare
- [GitHub Models API åtkomsttoken](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)

### Nödvändiga Miljövariabler

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

### Exempelkod

För att köra kodexemplet,

```bash
# zsh/bash
chmod +x ./04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Eller med hjälp av dotnet CLI:

```bash
dotnet run ./04-dotnet-agent-framework.cs
```

Se [`04-dotnet-agent-framework.cs`](../../../../04-tool-use/code_samples/04-dotnet-agent-framework.cs) för den kompletta koden.

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->