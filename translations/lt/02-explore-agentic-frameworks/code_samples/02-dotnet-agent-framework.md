<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T14:47:12+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "lt"
}
-->
# 🔍 Microsoft Agent Framework tyrinėjimas - Pagrindinis agentas (.NET)

## 📋 Mokymosi tikslai

Šiame pavyzdyje nagrinėjami pagrindiniai Microsoft Agent Framework konceptai per paprasto agento įgyvendinimą .NET aplinkoje. Sužinosite pagrindinius agentinius modelius ir suprasite, kaip intelektualūs agentai veikia naudojant C# ir .NET ekosistemą.

### Ką sužinosite

- 🏗️ **Agentų architektūra**: Suprasti pagrindinę AI agentų struktūrą .NET aplinkoje
- 🛠️ **Įrankių integracija**: Kaip agentai naudoja išorines funkcijas, kad išplėstų galimybes  
- 💬 **Pokalbių eiga**: Daugkartinių pokalbių ir konteksto valdymas naudojant gijų valdymą
- 🔧 **Konfigūracijos modeliai**: Geriausios praktikos agentų nustatymui ir valdymui .NET aplinkoje

## 🎯 Pagrindinės aptariamos sąvokos

### Agentinio Framework principai

- **Autonomija**: Kaip agentai priima savarankiškus sprendimus naudojant .NET AI abstrakcijas
- **Reaktyvumas**: Reagavimas į aplinkos pokyčius ir vartotojo įvestis
- **Proaktyvumas**: Iniciatyvos ėmimasis remiantis tikslais ir kontekstu
- **Socialinis gebėjimas**: Sąveika per natūralią kalbą naudojant pokalbių gijas

### Techniniai komponentai

- **AIAgent**: Pagrindinis agento organizavimas ir pokalbių valdymas (.NET)
- **Įrankių funkcijos**: Agentų galimybių plėtra naudojant C# metodus ir atributus
- **OpenAI integracija**: Kalbos modelių panaudojimas per standartizuotus .NET API
- **Saugus konfigūravimas**: API raktų valdymas pagal aplinką

## 🔧 Technologijų rinkinys

### Pagrindinės technologijos

- Microsoft Agent Framework (.NET)
- GitHub Models API integracija
- OpenAI suderinami klientų modeliai
- Konfigūravimas pagal aplinką su DotNetEnv

### Agentų galimybės

- Natūralios kalbos supratimas ir generavimas
- Funkcijų kvietimas ir įrankių naudojimas su C# atributais
- Konteksto suvokimas atsakymuose naudojant pokalbių gijas
- Išplečiama architektūra su priklausomybių injekcijos modeliais

## 📚 Framework palyginimas

Šis pavyzdys demonstruoja Microsoft Agent Framework požiūrį, palyginti su kitais agentiniais framework'ais:

| Funkcija | Microsoft Agent Framework | Kiti framework'ai |
|----------|---------------------------|-------------------|
| **Integracija** | Gimtoji Microsoft ekosistema | Įvairus suderinamumas |
| **Paprastumas** | Švari, intuityvi API | Dažnai sudėtingas nustatymas |
| **Išplečiamumas** | Lengva įrankių integracija | Priklauso nuo framework'o |
| **Paruoštas verslui** | Sukurtas gamybai | Priklauso nuo framework'o |

## 🚀 Pradžia

### Reikalavimai

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) arba naujesnė versija
- [GitHub Models API prieigos raktas](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)

### Reikalingi aplinkos kintamieji

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

### Pavyzdinis kodas

Norėdami paleisti kodo pavyzdį,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Arba naudodami dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Žr. [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) visam kodui.

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

## 🎓 Pagrindinės išvados

1. **Agentų architektūra**: Microsoft Agent Framework suteikia švarų, tipų saugų požiūrį į AI agentų kūrimą .NET aplinkoje
2. **Įrankių integracija**: Funkcijos, pažymėtos `[Description]` atributais, tampa prieinamais įrankiais agentui
3. **Pokalbių kontekstas**: Gijų valdymas leidžia daugkartinius pokalbius su pilnu konteksto suvokimu
4. **Konfigūracijos valdymas**: Aplinkos kintamieji ir saugus kredencialų tvarkymas atitinka .NET geriausias praktikas
5. **OpenAI suderinamumas**: GitHub Models integracija veikia sklandžiai per OpenAI suderinamus API

## 🔗 Papildomi ištekliai

- [Microsoft Agent Framework dokumentacija](https://learn.microsoft.com/agent-framework)
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius naudojant šį vertimą.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->