<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcc874e190347bd6a095aed56dc16de8",
  "translation_date": "2025-11-13T13:07:12+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "nl"
}
-->
# 🎨 Agentische Ontwerppatronen met GitHub-modellen (.NET)

## 📋 Leerdoelen

Dit voorbeeld demonstreert ontwerpprincipes van ondernemingsniveau voor het bouwen van intelligente agenten met behulp van het Microsoft Agent Framework in .NET, geïntegreerd met GitHub-modellen. Je leert professionele patronen en architecturale benaderingen die agenten productie-klaar, onderhoudbaar en schaalbaar maken.

### Ontwerppatronen voor ondernemingen

- 🏭 **Factory Pattern**: Gestandaardiseerde agentcreatie met dependency injection
- 🔧 **Builder Pattern**: Vloeiende configuratie en opzet van agenten
- 🧵 **Thread-Safe Patterns**: Beheer van gelijktijdige gesprekken
- 📋 **Repository Pattern**: Georganiseerd beheer van tools en mogelijkheden

## 🎯 .NET-specifieke architecturale voordelen

### Kenmerken voor ondernemingen

- **Sterke Typing**: Validatie tijdens compilatie en ondersteuning voor IntelliSense
- **Dependency Injection**: Ingebouwde DI-containerintegratie
- **Configuratiebeheer**: IConfiguration en Options-patronen
- **Async/Await**: Ondersteuning voor asynchrone programmering van topniveau

### Productieklare patronen

- **Logintegratie**: ILogger en ondersteuning voor gestructureerd loggen
- **Gezondheidscontroles**: Ingebouwde monitoring en diagnostiek
- **Configuratievalidatie**: Sterke typing met data-annotaties
- **Foutafhandeling**: Gestructureerd beheer van uitzonderingen

## 🔧 Technische architectuur

### Kerncomponenten van .NET

- **Microsoft.Extensions.AI**: Geünificeerde AI-service-abstracties
- **Microsoft.Agents.AI**: Framework voor ondernemingsagenten
- **GitHub Models Integration**: API-clientpatronen met hoge prestaties
- **Configuratiesysteem**: Integratie van appsettings.json en omgevingen

### Implementatie van ontwerppatronen

```mermaid
graph LR
    A[IServiceCollection] --> B[Agent Builder]
    B --> C[Configuration]
    C --> D[Tool Registry]
    D --> E[AI Agent]
```

## 🏗️ Gedemonstreerde ondernemingspatronen

### 1. **Creational Patterns**

- **Agent Factory**: Gecentraliseerde agentcreatie met consistente configuratie
- **Builder Pattern**: Vloeiende API voor complexe agentconfiguratie
- **Singleton Pattern**: Beheer van gedeelde bronnen en configuratie
- **Dependency Injection**: Losse koppeling en testbaarheid

### 2. **Behavioral Patterns**

- **Strategy Pattern**: Verwisselbare uitvoeringsstrategieën voor tools
- **Command Pattern**: Geïntegreerde agentoperaties met undo/redo
- **Observer Pattern**: Eventgestuurd beheer van de levenscyclus van agenten
- **Template Method**: Gestandaardiseerde workflows voor agentuitvoering

### 3. **Structural Patterns**

- **Adapter Pattern**: Integratielaag voor GitHub Models API
- **Decorator Pattern**: Verbetering van agentmogelijkheden
- **Facade Pattern**: Vereenvoudigde interfaces voor agentinteractie
- **Proxy Pattern**: Lazy loading en caching voor prestaties

## 📚 Ontwerpprincipes in .NET

### SOLID-principes

- **Single Responsibility**: Elk component heeft één duidelijke functie
- **Open/Closed**: Uitbreidbaar zonder aanpassing
- **Liskov Substitution**: Implementaties van tools op basis van interfaces
- **Interface Segregation**: Gerichte, samenhangende interfaces
- **Dependency Inversion**: Afhankelijkheid van abstracties, niet van concreties

### Clean Architecture

- **Domeinlaag**: Kernabstracties voor agenten en tools
- **Applicatielaag**: Orchestratie en workflows van agenten
- **Infrastructuurlaag**: Integratie van GitHub-modellen en externe services
- **Presentatielaag**: Gebruikersinteractie en responsformattering

## 🔒 Overwegingen voor ondernemingen

### Beveiliging

- **Beheer van referenties**: Veilige API-sleutelverwerking met IConfiguration
- **Validatie van invoer**: Sterke typing en validatie met data-annotaties
- **Sanitatie van uitvoer**: Veilige verwerking en filtering van reacties
- **Audit Logging**: Uitgebreide tracking van operaties

### Prestaties

- **Async Patterns**: Niet-blokkerende I/O-operaties
- **Connection Pooling**: Efficiënt beheer van HTTP-clients
- **Caching**: Responscaching voor verbeterde prestaties
- **Beheer van bronnen**: Correcte verwijdering en opruimingspatronen

### Schaalbaarheid

- **Thread Safety**: Ondersteuning voor gelijktijdige uitvoering van agenten
- **Resource Pooling**: Efficiënt gebruik van bronnen
- **Load Management**: Rate limiting en backpressure handling
- **Monitoring**: Prestatiestatistieken en gezondheidscontroles

## 🚀 Productie-implementatie

- **Configuratiebeheer**: Omgevingsspecifieke instellingen
- **Logstrategie**: Gestructureerd loggen met correlatie-ID's
- **Foutafhandeling**: Globale foutafhandeling met correcte herstelmethoden
- **Monitoring**: Application Insights en prestatiecounters
- **Testen**: Unit tests, integratietests en load testing patronen

Klaar om intelligente agenten van ondernemingsniveau te bouwen met .NET? Laten we iets robuusts ontwerpen! 🏢✨

## 🚀 Aan de slag

### Vereisten

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) of hoger
- [GitHub Models API-toegangstoken](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)

### Vereiste omgevingsvariabelen

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

### Voorbeeldcode

Om het codevoorbeeld uit te voeren,

```bash
# zsh/bash
chmod +x ./03-dotnet-agent-framework.cs
./03-dotnet-agent-framework.cs
```

Of gebruik de dotnet CLI:

```bash
dotnet run ./03-dotnet-agent-framework.cs
```

Zie [`03-dotnet-agent-framework.cs`](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs) voor de volledige code.

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
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->