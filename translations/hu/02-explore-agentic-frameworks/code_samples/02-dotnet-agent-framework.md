<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T13:42:54+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "hu"
}
-->
# 🔍 A Microsoft Agent Framework felfedezése - Alapvető ügynök (.NET)

## 📋 Tanulási célok

Ez a példa bemutatja a Microsoft Agent Framework alapvető koncepcióit egy egyszerű ügynök implementációján keresztül .NET-ben. Megismerheted az alapvető ügynöki mintákat, és megértheted, hogyan működnek az intelligens ügynökök a háttérben C# és a .NET ökoszisztéma segítségével.

### Amit felfedezhetsz

- 🏗️ **Ügynök architektúra**: Az AI ügynökök alapvető felépítésének megértése .NET-ben  
- 🛠️ **Eszközintegráció**: Hogyan használják az ügynökök a külső funkciókat képességeik bővítésére  
- 💬 **Beszélgetési folyamat**: Többfordulós beszélgetések és kontextus kezelése szálkezeléssel  
- 🔧 **Konfigurációs minták**: Legjobb gyakorlatok az ügynök beállításához és kezeléséhez .NET-ben  

## 🎯 Főbb lefedett koncepciók

### Ügynöki keretrendszer alapelvei

- **Autonómia**: Hogyan hoznak az ügynökök önálló döntéseket a .NET AI absztrakciók segítségével  
- **Reaktivitás**: Környezeti változásokra és felhasználói bemenetekre való reagálás  
- **Proaktivitás**: Kezdeményezés vállalása célok és kontextus alapján  
- **Társas képesség**: Természetes nyelvű interakció beszélgetési szálakon keresztül  

### Technikai összetevők

- **AIAgent**: Az ügynökök alapvető irányítása és beszélgetéskezelése (.NET)  
- **Eszközfunkciók**: Az ügynök képességeinek bővítése C# metódusokkal és attribútumokkal  
- **OpenAI integráció**: Nyelvi modellek használata szabványosított .NET API-kon keresztül  
- **Biztonságos konfiguráció**: API-kulcsok kezelése környezetalapú beállításokkal  

## 🔧 Technikai háttér

### Alapvető technológiák

- Microsoft Agent Framework (.NET)  
- GitHub Models API integráció  
- OpenAI-kompatibilis kliens minták  
- Környezetalapú konfiguráció DotNetEnv segítségével  

### Ügynöki képességek

- Természetes nyelv megértése és generálása  
- Funkcióhívás és eszközhasználat C# attribútumokkal  
- Kontextusérzékeny válaszok beszélgetési szálakkal  
- Bővíthető architektúra függőséginjektálási mintákkal  

## 📚 Keretrendszerek összehasonlítása

Ez a példa bemutatja a Microsoft Agent Framework megközelítését más ügynöki keretrendszerekkel összehasonlítva:

| Funkció | Microsoft Agent Framework | Egyéb keretrendszerek |
|---------|---------------------------|-----------------------|
| **Integráció** | Natív Microsoft ökoszisztéma | Változó kompatibilitás |
| **Egyszerűség** | Tiszta, intuitív API | Gyakran bonyolult beállítás |
| **Bővíthetőség** | Könnyű eszközintegráció | Keretrendszerfüggő |
| **Vállalati szintű** | Gyártásra tervezve | Keretrendszertől függően változó |

## 🚀 Első lépések

### Előfeltételek

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) vagy újabb  
- [GitHub Models API hozzáférési token](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### Szükséges környezeti változók

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
  

### Példakód

A kód futtatásához:

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
Vagy a dotnet CLI használatával:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
A teljes kódot lásd itt: [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs).

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
  

## 🎓 Főbb tanulságok

1. **Ügynök architektúra**: A Microsoft Agent Framework tiszta, típusbiztos megközelítést kínál AI ügynökök építéséhez .NET-ben  
2. **Eszközintegráció**: A `[Description]` attribútummal ellátott funkciók elérhető eszközökké válnak az ügynök számára  
3. **Beszélgetési kontextus**: A szálkezelés lehetővé teszi a többfordulós beszélgetéseket teljes kontextusérzékenységgel  
4. **Konfigurációkezelés**: A környezeti változók és a biztonságos hitelesítő adatok kezelése a .NET legjobb gyakorlatait követi  
5. **OpenAI kompatibilitás**: A GitHub Models integráció zökkenőmentesen működik az OpenAI-kompatibilis API-kon keresztül  

## 🔗 További források

- [Microsoft Agent Framework dokumentáció](https://learn.microsoft.com/agent-framework)  
- [GitHub Models piactér](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Egyszerű fájlalkalmazások](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->