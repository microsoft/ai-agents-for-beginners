# 🛠️ Pažangus įrankių naudojimas su Azure OpenAI (Atsakymai API) (.NET)

## 📋 Mokymosi tikslai

Šiame užraše demonstruojami įmonių lygio įrankių integracijos modeliai, naudojant Microsoft Agent Framework .NET su Azure OpenAI (Atsakymai API). Išmoksite kurti pažangius agentus su keliais specializuotais įrankiais, naudojant C# stiprų tipavimą ir .NET įmonių funkcijas.

### Pažangios įrankių galimybės, kurias įvaldysite

- 🔧 **Daugiainstrumentinė architektūra**: Agentų kūrimas su keliomis specializuotomis galimybėmis
- 🎯 **Tipų saugus įrankių vykdymas**: Naudojant C# vykdymo metu atliekamą patvirtinimą
- 📊 **Įmonių įrankių modeliai**: Produkcijai paruoštas įrankių dizainas ir klaidų valdymas
- 🔗 **Įrankių sudėtis**: Įrankių derinimas sudėtingiems verslo procesams

## 🎯 .NET įrankių architektūros privalumai

### Įmonių įrankių ypatybės

- **Vykdymo laiko tikrinimas**: Stiprus tipavimas užtikrina įrankių parametrų teisingumą
- **Priklausomybių injekcija**: IoC konteinerio integracija įrankių valdymui
- **Async/Await modeliai**: Neblokuojantis įrankių vykdymas su tinkamu išteklių valdymu
- **Struktūruotas žurnalas**: Įmontuota žurnalo integracija įrankių vykdymo stebėjimui

### Produkcijai paruošti modeliai

- **Išimčių valdymas**: Išsamus klaidų valdymas su tipizuotomis išimtimis
- **Išteklių valdymas**: Tinkami išmetimo modeliai ir atminties valdymas
- **Veikimo matavimas**: Integruoti metrikos ir našumo skaitikliai
- **Konfigūracijos valdymas**: Tipų saugi konfigūracija su patvirtinimu

## 🔧 Techninė architektūra

### Pagrindiniai .NET įrankių komponentai

- **Microsoft.Extensions.AI**: Suvienyta įrankių abstrakcijos sluoksnis
- **Microsoft.Agents.AI**: Įmonių lygio įrankių orkestracija
- **Azure OpenAI (Atsakymai API)**: Aukšto našumo API klientas su ryšio talpykla

### Įrankių vykdymo vamzdelis

```mermaid
graph LR
    A[Vartotojo užklausa] --> B[Agentas analizė]
    B --> C[Įrankio pasirinkimas]
    C --> D[Tipo tikrinimas]
    B --> E[Parametrų susiejimas]
    E --> F[Įrankio vykdymas]
    C --> F
    F --> G[Rezultatų apdorojimas]
    D --> G
    G --> H[Atsakymas]
```

## 🛠️ Įrankių kategorijos ir modeliai

### 1. **Duomenų apdorojimo įrankiai**

- **Įvesties patvirtinimas**: Stiprus tipavimas su duomenų anotacijomis
- **Transformavimo operacijos**: Tipų saugus duomenų konvertavimas ir formatavimas
- **Verslo logika**: Domenui būdingi skaičiavimo ir analizės įrankiai
- **Išvesties formatavimas**: Struktūruotas atsakymų generavimas

### 2. **Integracijos įrankiai**

- **API jungtys**: REST paslaugų integracija su HttpClient
- **Duomenų bazės įrankiai**: Entity Framework integracija duomenų prieigai
- **Failų operacijos**: Saugios failų sistemos operacijos su patvirtinimu
- **Išorinės paslaugos**: Trečiųjų šalių paslaugų integracijos modeliai

### 3. **Naudingi įrankiai**

- **Teksto apdorojimas**: Eilučių manipuliavimo ir formatavimo įrankiai
- **Datos/Laiko operacijos**: Kultūrai pritaikyti datos/laiko skaičiavimai
- **Matematiniai įrankiai**: Tikslūs skaičiavimai ir statistinės operacijos
- **Patvirtinimo įrankiai**: Verslo taisyklių patikra ir duomenų tikrinimas

Pasiruošę kurti įmonių lygio agentus su galingomis, tipų saugiomis .NET įrankių galimybėmis? Sukurkime profesionalaus lygio sprendimus! 🏢⚡

## 🚀 Pradžia

### Reikalavimai

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) arba naujesnė versija
- [Azure prenumerata](https://azure.microsoft.com/free/) su Azure OpenAI resursu ir modelio diegimu
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — prisijunkite su `az login`

### Būtini aplinkos kintamieji

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Tada prisijunkite, kad AzureCliCredential galėtų gauti žetoną
az login
```

```powershell
# „PowerShell“
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Tada prisijunkite, kad AzureCliCredential galėtų gauti žetoną
az login
```

### Pavyzdinis kodas

Norėdami paleisti kodo pavyzdį,

```bash
# zsh/bash
chmod +x ./04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Arba naudodami dotnet CLI:

```bash
dotnet run ./04-dotnet-agent-framework.cs
```

Peržiūrėkite [`04-dotnet-agent-framework.cs`](../../../../04-tool-use/code_samples/04-dotnet-agent-framework.cs) pilnam kodui.

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
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->