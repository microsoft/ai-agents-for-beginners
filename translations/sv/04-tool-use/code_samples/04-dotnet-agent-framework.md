# 🛠️ Avancerad verktygsanvändning med Azure OpenAI (Responses API) (.NET)

## 📋 Inlärningsmål

Denna anteckningsbok visar företagsklassade integrationsmönster för verktyg med Microsoft Agent Framework i .NET med Azure OpenAI (Responses API). Du lär dig att bygga sofistikerade agenter med flera specialiserade verktyg, med hjälp av C#'s starka typning och .NET:s företagsfunktioner.

### Avancerade verktygskapaciteter du kommer att behärska

- 🔧 **Multiverktygsarkitektur**: Bygga agenter med flera specialiserade kapaciteter
- 🎯 **Typ-säker verktygsexekvering**: Utnyttja C#’s kompileringstidvalidering
- 📊 **Företagsverktygsmönster**: Produktionsfärdig verktygsdesign och felhantering
- 🔗 **Verktygssammansättning**: Kombinera verktyg för komplexa affärsarbetsflöden

## 🎯 Fördelar med .NET-verktygsarkitektur

### Företagsverktygsfunktioner

- **Kompileringstidsvalidering**: Stark typning säkerställer verktygsparametrars korrekthet
- **Dependency Injection**: IoC-kontainerintegration för verktygshantering
- **Async/Await-mönster**: Icke-blockerande verktygsexekvering med korrekt resursförvaltning
- **Strukturerad loggning**: Inbyggd loggningsintegration för verktygsexekveringsövervakning

### Produktionsfärdiga mönster

- **Undantagshantering**: Omfattande felhantering med typade undantag
- **Resurshantering**: Korrekt avfallshantering och minneshantering
- **Prestandaövervakning**: Inbyggda mätvärden och prestandaräknare
- **Konfigurationshantering**: Typ-säker konfiguration med validering

## 🔧 Teknisk arkitektur

### Kärnkomponenter för .NET-verktyg

- **Microsoft.Extensions.AI**: Enhetligt abstraktionslager för verktyg
- **Microsoft.Agents.AI**: Företagsklassad verktygsorkestrering
- **Azure OpenAI (Responses API)**: Högpresterande API-klient med anslutningspoolning

### Verktygsexekveringspipeline

```mermaid
graph LR
    A[Användarförfrågan] --> B[Agentanalys]
    B --> C[Verktygsval]
    C --> D[Typvalidering]
    B --> E[Parameterbindning]
    E --> F[Verktygsutförande]
    C --> F
    F --> G[Resultatbearbetning]
    D --> G
    G --> H[Svar]
```

## 🛠️ Verktygskategorier & mönster

### 1. **Databehandlingsverktyg**

- **Inmatningsvalidering**: Stark typning med dataannotationer
- **Transformationsoperationer**: Typ-säker datakonvertering och formatering
- **Affärslogik**: Domänspecifika beräknings- och analysverktyg
- **Utdataformatering**: Strukturerad svarsgenerering

### 2. **Integrationsverktyg**

- **API-kopplingar**: RESTful tjänsteintegration med HttpClient
- **Databasverktyg**: Entity Framework-integration för dataåtkomst
- **Filoperationer**: Säker filsystemshantering med validering
- **Externatjänster**: Tredjepartsserviceintegrationsmönster

### 3. **Verktygsverktyg**

- **Textbehandling**: Strängmanipulation och formateringsverktyg
- **Datum/Tid-operationer**: Kulturmedvetna datum/tidsberäkningar
- **Matematiska verktyg**: Precisionsberäkningar och statistiska operationer
- **Valideringsverktyg**: Affärsregelvalidering och dataverifiering

Redo att bygga företagsklassade agenter med kraftfulla, typ-säkra verktygskapaciteter i .NET? Låt oss arkitektera några professionella lösningar! 🏢⚡

## 🚀 Komma igång

### Förutsättningar

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller högre
- En [Azure-prenumeration](https://azure.microsoft.com/free/) med en Azure OpenAI-resurs och en modellutplacering
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — logga in med `az login`

### Nödvändiga miljövariabler

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Logga in sedan så att AzureCliCredential kan få en token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Logga in så att AzureCliCredential kan få en token
az login
```

### Exempelkod

För att köra kodexemplet,

```bash
# zsh/bash
chmod +x ./04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Eller med dotnet CLI:

```bash
dotnet run ./04-dotnet-agent-framework.cs
```

Se [`04-dotnet-agent-framework.cs`](../../../../04-tool-use/code_samples/04-dotnet-agent-framework.cs) för komplett kod.

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
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->