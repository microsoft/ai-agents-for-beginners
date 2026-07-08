# 🎨 Agentiske designmønstre med Azure OpenAI (Responses API) (.NET)

## 📋 Læringsmål

Dette eksemplet demonstrerer virksomhetsklassede designmønstre for å bygge intelligente agenter ved bruk av Microsoft Agent Framework i .NET med integrasjon av Azure OpenAI (Responses API). Du vil lære profesjonelle mønstre og arkitekturtilnærminger som gjør agenter produksjonsklare, vedlikeholdbare og skalerbare.

### Virksomhetsdesignmønstre

- 🏭 **Factory Pattern**: Standardisert agentopprettelse med avhengighetsinjeksjon
- 🔧 **Builder Pattern**: Flytende agentkonfigurasjon og oppsett
- 🧵 **Trådsikre mønstre**: Samtidig samtalestyring
- 📋 **Repository Pattern**: Organisert verktøy- og kapabilitetsstyring

## 🎯 .NET-spesifikke arkitekturfordeler

### Virksomhetsfunksjoner

- **Sterk typing**: Kompileringstid-validering og IntelliSense-støtte
- **Avhengighetsinjeksjon**: Innebygd DI-container-integrasjon
- **Konfigurasjonsstyring**: IConfiguration- og Options-mønstre
- **Async/Await**: Førsteklasses asynkron programmeringsstøtte

### Produksjonsklare mønstre

- **Loggintegrasjon**: ILogger og strukturert logg-støtte
- **Helsesjekker**: Innebygd overvåkning og diagnostikk
- **Konfigurasjonsvalidering**: Sterk typing med dataanmerkninger
- **Feilhåndtering**: Strukturert unntakshåndtering

## 🔧 Teknisk arkitektur

### Kjernekomponenter i .NET

- **Microsoft.Extensions.AI**: Enhetlige AI-tjenesteabstraksjoner
- **Microsoft.Agents.AI**: Virksomhetsrammeverk for agentorchestrering
- **Azure OpenAI (Responses API)**: Høyytelses API-klientmønstre
- **Konfigurasjonssystem**: appsettings.json og miljøintegrasjon

### Implementering av designmønstre

```mermaid
graph LR
    A[IServiceCollection] --> B[Agent Bygger]
    B --> C[Konfigurasjon]
    C --> D[Verktøyregister]
    D --> E[AI Agent]
```

## 🏗️ Virksomhetsmønstre demonstrert

### 1. **Opprettelsesmønstre**

- **Agentfabrikk**: Sentralisert agentopprettelse med konsistent konfigurasjon
- **Builder Pattern**: Flytende API for kompleks agentkonfigurasjon
- **Singleton Pattern**: Delte ressurser og konfigurasjonsstyring
- **Avhengighetsinjeksjon**: Løs kobling og testbarhet

### 2. **Atferdsmønstre**

- **Strategimønster**: Utskiftbare strategier for verktøykjøring
- **Kommandomønster**: Innpakkede agentoperasjoner med angre/gjøre om
- **Observatørmønster**: Hendelsesdrevet agentlivssyklusstyring
- **Template Method**: Standardiserte agentutførelsesflyter

### 3. **Strukturelle mønstre**

- **Adaptermønster**: Azure OpenAI (Responses API) integrasjonslag
- **Dekoratørmønster**: Forbedring av agentkapabiliteter
- **Fasadene**: Forenklede grensesnitt for agentinteraksjon
- **Proxy-mønster**: Forsinket lasting og caching for ytelse

## 📚 .NET designprinsipper

### SOLID-prinsipper

- **Enkelt ansvar**: Hver komponent har ett klart formål
- **Åpen/lukket**: Utvidbar uten modifikasjon
- **Liskov substitusjon**: Grensesnittbaserte verktøyimplementasjoner
- **Grensesnitt-segregering**: Fokusert, sammenhengende grensesnitt
- **Avhengighetsinversjon**: Avheng av abstraksjoner, ikke konkrete

### Ren arkitektur

- **Domene-lag**: Kjerneabstraksjoner for agent og verktøy
- **Applikasjonslag**: Agentorchestrering og arbeidsflyter
- **Infrastrukturlag**: Azure OpenAI (Responses API) integrasjon og eksterne tjenester
- **Presentasjonslag**: Brukerinteraksjon og responsformatering

## 🔒 Virksomhetshensyn

### Sikkerhet

- **Håndtering av legitimasjon**: Sikker håndtering av API-nøkler med IConfiguration
- **Inndata-validering**: Sterk typing og validering med dataanmerkninger
- **Utdata-rensing**: Sikker responsbehandling og filtrering
- **Revisjonslogging**: Omfattende operasjonssporing

### Ytelse

- **Asynkrone mønstre**: Ikke-blokkerende I/O-operasjoner
- **Tilkoblingspooling**: Effektiv HTTP-klienthåndtering
- **Caching**: Responscaching for forbedret ytelse
- **Ressurshåndtering**: Korrekte avhendings- og oppryddingsmønstre

### Skalerbarhet

- **Trådsikkerhet**: Samtidig agentutførelsesstøtte
- **Ressurspooling**: Effektiv ressursutnyttelse
- **Laststyring**: Hastighetsbegrensning og backpress-håndtering
- **Overvåkning**: Ytelsesmetrikker og helsesjekker

## 🚀 Produksjonsdistribusjon

- **Konfigurasjonsstyring**: Miljøspesifikke innstillinger
- **Loggstrategi**: Strukturert logging med korrelasjons-IDer
- **Feilhåndtering**: Global unntakshåndtering med korrekt gjenoppretting
- **Overvåkning**: Application Insights og ytelsestellere
- **Testing**: Enhetstester, integrasjonstester og lastetestmønstre

Klar til å bygge virksomhetsklassede intelligente agenter med .NET? La oss arkitektere noe robust! 🏢✨

## 🚀 Komme i gang

### Forutsetninger

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller høyere
- Et [Azure-abonnement](https://azure.microsoft.com/free/) med en Azure OpenAI-ressurs og en modellutrulling
- Azure CLI ([Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)) — logg inn med `az login`

### Påkrevde miljøvariabler

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Logg deretter inn slik at AzureCliCredential kan hente en token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Logg inn så AzureCliCredential kan hente en token
az login
```

### Eksempelkode

For å kjøre kodeeksempelet,

```bash
# zsh/bash
chmod +x ./03-dotnet-agent-framework.cs
./03-dotnet-agent-framework.cs
```

Eller ved bruk av dotnet CLI:

```bash
dotnet run ./03-dotnet-agent-framework.cs
```

Se [`03-dotnet-agent-framework.cs`](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs) for komplett kode.

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
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->