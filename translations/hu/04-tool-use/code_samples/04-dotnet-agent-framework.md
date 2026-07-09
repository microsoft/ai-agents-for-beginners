# 🛠️ Fejlett eszközhasználat Azure OpenAI-vel (Responses API) (.NET)

## 📋 Tanulási célok

Ez a jegyzetfüzet vállalati szintű eszközintegrációs mintákat mutat be a Microsoft Agent Framework használatával .NET-ben, Azure OpenAI-val (Responses API). Megtanulod, hogyan építs összetett ügynököket több specializált eszközzel, kihasználva a C# erős típusosságát és a .NET vállalati funkcióit.

### Fejlett eszközképességek, amelyeket elsajátítasz

- 🔧 **Többeszköz-architektúra**: Több specializált képességgel rendelkező ügynökök létrehozása
- 🎯 **Típusbiztos eszközvégrehajtás**: A C# fordításidő-ellenőrzésének kihasználása
- 📊 **Vállalati eszközminták**: Termelésre kész eszköztervezés és hibakezelés
- 🔗 **Eszközkompozíció**: Eszközök kombinálása összetett üzleti munkafolyamatokhoz

## 🎯 .NET eszközarchitektúra előnyei

### Vállalati eszközfunkciók

- **Fordításidő-ellenőrzés**: Az erős típusosság biztosítja az eszközparaméterek helyességét
- **Függőséginjektálás**: IoC konténer integráció az eszközkezeléshez
- **Async/Await minták**: Nem blokkoló eszközvégrehajtás megfelelő erőforrás-kezeléssel
- **Strukturált naplózás**: Beépített napló integráció az eszközvégrehajtás nyomon követéséhez

### Termelésre kész minták

- **Kivételkezelés**: Átfogó hibakezelés típusos kivételekkel
- **Erőforrás-kezelés**: Megfelelő megszabadulási minták és memória kezelése
- **Teljesítményfigyelés**: Beépített metrikák és teljesítményszámlálók
- **Konfigurációkezelés**: Típusbiztos konfiguráció validálással

## 🔧 Technikai architektúra

### Alapvető .NET eszközkomponensek

- **Microsoft.Extensions.AI**: Egységes eszközabsztrakciós réteg
- **Microsoft.Agents.AI**: Vállalati szintű eszközorchesztráció
- **Azure OpenAI (Responses API)**: Nagy teljesítményű API kliens kapcsolatmegosztással

### Eszközvégrehajtási folyamat

```mermaid
graph LR
    A[Felhasználói kérés] --> B[Ügynök elemzése]
    B --> C[Eszköz kiválasztása]
    C --> D[Típus érvényesítés]
    B --> E[Paraméter kötés]
    E --> F[Eszköz végrehajtása]
    C --> F
    F --> G[Eredmény feldolgozása]
    D --> G
    G --> H[Válasz]
```

## 🛠️ Eszközkategóriák és minták

### 1. **Adatfeldolgozó eszközök**

- **Bemeneti ellenőrzés**: Erős típusosság adatannotációkkal
- **Átalakító műveletek**: Típusbiztos adatkonverzió és formázás
- **Üzleti logika**: Domain-specifikus számítási és elemző eszközök
- **Kimeneti formázás**: Strukturált válaszgenerálás

### 2. **Integrációs eszközök**

- **API csatlakozók**: RESTful szolgáltatás integráció HttpClienttel
- **Adatbázis-eszközök**: Entity Framework integráció adat-hozzáféréshez
- **Fájl műveletek**: Biztonságos fájlrendszer-műveletek validálással
- **Külső szolgáltatások**: Harmadik féltől származó szolgáltatás integrációs minták

### 3. **Hasznos eszközök**

- **Szövegfeldolgozás**: Karakterlánc manipuláció és formázási segédprogramok
- **Dátum/Idő műveletek**: Kultúrafüggő dátum/idő számítások
- **Matematikai eszközök**: Precíziós számítások és statisztikai műveletek
- **Érvényesítő eszközök**: Üzleti szabályok ellenőrzése és adatellenőrzés

Készen állsz arra, hogy vállalati szintű ügynököket építs erős, típusbiztos eszközképességekkel .NET-ben? Álljunk neki professzionális megoldásokat építeni! 🏢⚡

## 🚀 Kezdés

### Előfeltételek

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) vagy újabb
- Egy [Azure előfizetés](https://azure.microsoft.com/free/) Azure OpenAI erőforrással és modell telepítéssel
- Az [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — jelentkezz be `az login` parancsal

### Szükséges környezeti változók

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Jelentkezzen be, hogy az AzureCliCredential tokenhez jusson
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Jelentkezzen be, hogy az AzureCliCredential kaphasson egy tokent
az login
```

### Példakód

A kódpélda futtatásához,

```bash
# zsh/bash
chmod +x ./04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Vagy a dotnet CLI használatával:

```bash
dotnet run ./04-dotnet-agent-framework.cs
```

Lásd a teljes kódot a [`04-dotnet-agent-framework.cs`](../../../../04-tool-use/code_samples/04-dotnet-agent-framework.cs) fájlban.

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
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->