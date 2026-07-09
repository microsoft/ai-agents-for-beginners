# 🛠️ Pokročilé použití nástrojů s Azure OpenAI (Responses API) (.NET)

## 📋 Výukové cíle

Tento notebook ukazuje podnikové vzory integrace nástrojů pomocí Microsoft Agent Framework v .NET s Azure OpenAI (Responses API). Naučíte se vytvářet sofistikované agenty s více specializovanými nástroji, využívající silné typování C# a podnikové funkce .NET.

### Pokročilé schopnosti nástrojů, které zvládnete

- 🔧 **Architektura s více nástroji**: Vytváření agentů s více specializovanými schopnostmi
- 🎯 **Typově bezpečné spouštění nástrojů**: Využití kompilátorové kontroly v C#
- 📊 **Podnikové vzory nástrojů**: Návrh nástrojů připravených pro produkci a řešení chyb
- 🔗 **Složení nástrojů**: Kombinování nástrojů pro složité obchodní pracovní postupy

## 🎯 Výhody architektury nástrojů v .NET

### Podnikové funkce nástrojů

- **Kontrola při kompilaci**: Silné typování zajišťuje správnost parametrů nástroje
- **Injektáž závislostí**: Integrace IoC kontejneru pro správu nástrojů
- **Vzory Async/Await**: Nezablokované spouštění nástrojů se správou zdrojů
- **Strukturované logování**: Integrované logování pro monitorování spuštění nástrojů

### Vzory připravené pro produkci

- **Zpracování výjimek**: Komplexní správa chyb s typovanými výjimkami
- **Správa zdrojů**: Správné vzory likvidace a správy paměti
- **Monitorování výkonu**: Integrované metriky a počitadla výkonu
- **Správa konfigurace**: Typově bezpečná konfigurace s validací

## 🔧 Technická architektura

### Hlavní komponenty nástrojů v .NET

- **Microsoft.Extensions.AI**: Jednotná abstraktní vrstva nástrojů
- **Microsoft.Agents.AI**: Podniková orchestrace nástrojů
- **Azure OpenAI (Responses API)**: Vysoce výkonný API klient s poolingem připojení

### Pipeline spuštění nástroje

```mermaid
graph LR
    A[Uživatelský požadavek] --> B[Analýza agenta]
    B --> C[Výběr nástroje]
    C --> D[Ověření typu]
    B --> E[Vázání parametrů]
    E --> F[Spuštění nástroje]
    C --> F
    F --> G[Zpracování výsledku]
    D --> G
    G --> H[Odpověď]
```

## 🛠️ Kategorie nástrojů & vzory

### 1. **Nástroje pro zpracování dat**

- **Validace vstupu**: Silné typování s datovými anotacemi
- **Transformační operace**: Typově bezpečná konverze a formátování dat
- **Obchodní logika**: Nástroje pro výpočty a analýzu specifickou pro doménu
- **Formátování výstupu**: Generování strukturovaných odpovědí

### 2. **Integrační nástroje** 

- **API konektory**: Integrace RESTful služeb s HttpClientem
- **Nástroje pro databáze**: Integrace Entity Framework pro přístup k datům
- **Operace se soubory**: Bezpečné operace se soubory s validací
- **Externí služby**: Vzory integrace třetích stran

### 3. **Užitečné nástroje**

- **Zpracování textu**: Manipulace a formátování řetězců
- **Operace s datem/časem**: Výpočty data/času citlivé na kulturu
- **Matematické nástroje**: Precizní výpočty a statistické operace
- **Validace**: Validace obchodních pravidel a ověřování dat

Připraveni vytvářet podnikové agenty s výkonnými, typově bezpečnými nástroji v .NET? Pojďme navrhnout profesionální řešení! 🏢⚡

## 🚀 Začínáme

### Požadavky

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) nebo vyšší
- Předplatné [Azure](https://azure.microsoft.com/free/) s Azure OpenAI zdrojem a nasazením modelu
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — přihlaste se pomocí `az login`

### Požadované proměnné prostředí

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Poté se přihlaste, aby AzureCliCredential mohl získat token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Pak se přihlaste, aby AzureCliCredential mohl získat token
az login
```

### Ukázkový kód

Pro spuštění příkladu kódu,

```bash
# zsh/bash
chmod +x ./04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Nebo použitím dotnet CLI:

```bash
dotnet run ./04-dotnet-agent-framework.cs
```

Kompletní kód najdete v [`04-dotnet-agent-framework.cs`](../../../../04-tool-use/code_samples/04-dotnet-agent-framework.cs).

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
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->