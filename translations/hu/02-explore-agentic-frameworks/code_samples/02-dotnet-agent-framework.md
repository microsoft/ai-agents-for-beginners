# 🔍 A Microsoft Agent Framework felfedezése - Alap ügynök (.NET)

## 📋 Tanulási célok

Ez a példa a Microsoft Agent Framework alapfogalmait vizsgálja meg egy alap ügynök megvalósításán keresztül .NET-ben. Megtanulod a fő ügynökös mintákat és megérted, hogyan működnek az intelligens ügynökök a háttérben C# és a .NET ökoszisztéma használatával.

### Amit felfedezel

- 🏗️ **Ügynök architektúra**: Az AI ügynökök alapstruktúrájának megértése .NET-ben
- 🛠️ **Eszközintegráció**: Hogyan használják az ügynökök a külső funkciókat képességeik kibővítésére  
- 💬 **Párbeszédfolyam**: Többfordulós beszélgetések kezelése és a kontextus menedzsmentje szál kezeléssel
- 🔧 **Konfigurációs minták**: Ügynök beállításának és kezelésének legjobb gyakorlatai .NET-ben

## 🎯 Főbb lefedett fogalmak

### Ügynökkeretelvek alapjai

- **Autonómia**: Az ügynökök hogyan hoznak önálló döntéseket .NET AI absztrakciók segítségével
- **Reaktivitás**: Reagálás a környezeti változásokra és a felhasználói bemenetekre
- **Proaktivitás**: Kezdeményezés vállalása célok és kontextus alapján
- **Társas képesség**: Természetes nyelven való kommunikáció beszélgetési szálakon keresztül

### Műszaki összetevők

- **AIAgent**: Az ügynök fő szervezése és a beszélgetés menedzsmentje (.NET)
- **Eszközfunkciók**: Az ügynök képességeinek kiterjesztése C# metódusokkal és attribútumokkal
- **Azure OpenAI integráció**: Nyelvi modellek használata az Azure OpenAI Responses API-n keresztül
- **Biztonságos konfiguráció**: Környezet-alapú végpont menedzsment

## 🔧 Műszaki háttér

### Alapvető technológiák

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) integráció
- Azure.AI.OpenAI kliensminták
- Környezeti konfiguráció DotNetEnv segítségével

### Ügynök képességek

- Természetes nyelv megértése és generálása
- Funkcióhívás és eszközhasználat C# attribútumokkal
- Kontextus-érzékeny válaszok beszélgetési munkamenetekkel
- Kiterjeszthető architektúra függőséginjektálási mintákkal

## 📚 Keretrendszer összehasonlítás

Ez a példa bemutatja a Microsoft Agent Framework megközelítését más ügynökkeretekhez képest:

| Jellemző | Microsoft Agent Framework | Egyéb keretrendszerek |
|---------|-------------------------|------------------|
| **Integráció** | Natív Microsoft ökoszisztéma | Változó kompatibilitás |
| **Egyszerűség** | Tiszta, intuitív API | Gyakran bonyolult beállítás |
| **Kiterjeszthetőség** | Könnyű eszközintegráció | Keretrendszer-függő |
| **Vállalati használatra kész** | Termelésre tervezve | Keretrendszerenként változó |

## 🚀 Első lépések

### Előfeltételek

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) vagy újabb
- Egy [Azure előfizetés](https://azure.microsoft.com/free/) Azure OpenAI erőforrással és modell telepítéssel
- Az [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — bejelentkezés `az login` parancssal

### Szükséges környezeti változók

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Jelentkezzen be, hogy az AzureCliCredential beszerezhessen egy tokent
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Ezután jelentkezzen be, hogy az AzureCliCredential tokenhez juthasson
az login
```

### Mintakód

A példa kód futtatásához,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Vagy a dotnet CLI használatával:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

A teljes kód a [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) fájlban.

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

## 🎓 Főbb tanulságok

1. **Ügynök architektúra**: A Microsoft Agent Framework tiszta, típusbiztos megközelítést nyújt AI ügynökök építéséhez .NET-ben
2. **Eszközintegráció**: A `[Description]` attribútummal ellátott függvények az ügynök számára elérhető eszközökké válnak
3. **Beszélgetési kontextus**: A munkamenet-kezelés lehetővé teszi a többfordulós párbeszédeket teljes kontextus észleléssel
4. **Konfiguráció menedzsment**: A környezeti változók és a biztonságos hitelesítő kezelése a .NET legjobb gyakorlatait követi
5. **Azure OpenAI Responses API**: Az ügynök az Azure OpenAI Responses API-t használja az Azure.AI.OpenAI SDK-n keresztül

## 🔗 További források

- [Microsoft Agent Framework dokumentáció](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI a Microsoft Foundry-ban](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Egyszeri fájl alkalmazások](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->