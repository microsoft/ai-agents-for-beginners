# 🔍 Tyrinėjame Microsoft Agent Framework – Paprastas agentas (.NET)

## 📋 Mokymosi tikslai

Šiame pavyzdyje nagrinėjamos Microsoft Agent Framework pagrindinės koncepcijos per pagrindinę agente įgyvendinimą .NET. Sužinosite pagrindinius agentinius modelius ir suprasite, kaip protingi agentai veikia „po gaubtu“, naudojant C# ir .NET ekosistemą.

### Ką atraskite

- 🏗️ **Agentų architektūra**: suprasti AI agentų pagrindinę struktūrą .NET aplinkoje
- 🛠️ **Įrankių integracija**: kaip agentai naudoja išorines funkcijas galimybėms išplėsti  
- 💬 **Pokalbiai**: valdant daugiapokopius pokalbius ir kontekstą su gijų valdymu
- 🔧 **Konfigūracijos modeliai**: geriausios praktikos agento diegimui ir valdymui .NET

## 🎯 Pagrindinės nagrinėjamos sąvokos

### Agentinio rėmo principai

- **Autonomija**: kaip agentai nepriklausomai priima sprendimus naudodami .NET AI abstrakcijas
- **Reaktyvumas**: reaguoti į aplinkos pokyčius ir naudotojo įvestis
- **Proaktyvumas**: imtis iniciatyvos remiantis tikslais ir kontekstu
- **Socialumas**: sąveikauti natūralia kalba per pokalbių gijas

### Techninės sudedamosios dalys

- **AIAgent**: pagrindinė agento orkestracija ir pokalbių valdymas (.NET)
- **Įrankių funkcijos**: C# metodų ir atributų naudojimas agento galimybėms plėsti
- **Azure OpenAI integracija**: kalbos modelių panaudojimas per Azure OpenAI Responses API
- **Saugaus konfigūravimo**: naudojant aplinkos konfigūracijos galinius taškus

## 🔧 Technologijų rinkinys

### Pagrindinės technologijos

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) integracija
- Azure.AI.OpenAI klientų modeliai
- Aplinkos pagrindu konfigūravimas su DotNetEnv

### Agentų galimybės

- Natūralaus kalbos supratimas ir generavimas
- Funkcijų kvietimas ir įrankių naudojimas per C# atributus
- Kontekstui jautrūs atsakymai su pokalbių sesijomis
- Išplečiama architektūra su priklausomybių įpurškimo modeliais

## 📚 Rėmų palyginimas

Šis pavyzdys demonstruoja Microsoft Agent Framework požiūrį, palyginti su kitais agentiniais rėmais:

| Funkcija | Microsoft Agent Framework | Kiti rėmai |
|---------|-------------------------|------------------|
| **Integracija** | Gimtoji Microsoft ekosistema | Įvairi suderinamumas |
| **Paprastumas** | Aiškus, intuityvus API | Dažnai sudėtinga konfigūracija |
| **Išplečiamumas** | Lengva įrankių integracija | Priklauso nuo rėmo |
| **Verslui paruoštas** | Sukurtas gamybai | Priklauso nuo rėmo |

## 🚀 Pradžia

### Reikalavimai

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) arba naujesnė versija
- [Azure prenumerata](https://azure.microsoft.com/free/) su Azure OpenAI resursu ir modelio diegimu
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — prisijunkite su `az login`

### Reikalingi aplinkos kintamieji

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# Tada prisijunkite, kad AzureCliCredential galėtų gauti tokeną
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# Tada prisijunkite, kad AzureCliCredential galėtų gauti žetoną
az login
```

### Pavyzdinis kodas

Norėdami paleisti pavyzdinį kodą,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Arba naudokite dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Peržiūrėkite [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) pilną kodo versiją.

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

## 🎓 Pagrindinės išvados

1. **Agentų architektūra**: Microsoft Agent Framework suteikia aiškų, tipams saugų požiūrį į AI agentų kūrimą .NET
2. **Įrankių integracija**: Funkcijos su `[Description]` atributais tampa agento prieinamais įrankiais
3. **Pokalbio kontekstas**: Sesijų valdymas leidžia daugiapokopius pokalbius su pilnu konteksto suvokimu
4. **Konfigūracijos valdymas**: Aplinkos kintamieji ir saugus kredencialų valdymas atitinka .NET geriausias praktikas
5. **Azure OpenAI Responses API**: Agentas naudoja Azure OpenAI Responses API per Azure.AI.OpenAI SDK

## 🔗 Papildomi ištekliai

- [Microsoft Agent Framework dokumentacija](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET vieno failo programos](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->