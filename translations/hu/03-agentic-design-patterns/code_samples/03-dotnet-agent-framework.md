# 🎨 Ügynöki tervezési minták Azure OpenAI-val (Responses API) (.NET)

## 📋 Tanulási célok

Ez a példa vállalati szintű tervezési mintákat mutat be intelligens ügynökök építéséhez a Microsoft Agent Framework .NET környezetében, Azure OpenAI (Responses API) integrációval. Megtanulhatod a professzionális mintákat és architekturális megközelítéseket, amelyek az ügynököket gyártásra készé, karbantarthatóvá és méretezhetővé teszik.

### Vállalati tervezési minták

- 🏭 **Factory Pattern (Gyári minta)**: Szabványosított ügynök létrehozás függőséginjektálással
- 🔧 **Builder Pattern (Építő minta)**: Folyékony ügynök konfiguráció és beállítás
- 🧵 **Szálbiztos minták**: Párhuzamos beszélgetéskezelés
- 📋 **Repository Pattern (Tároló minta)**: Szervezett eszköz- és képességkezelés

## 🎯 .NET-specifikus architekturális előnyök

### Vállalati jellemzők

- **Erős típusosság**: Fordításkori érvényesítés és IntelliSense támogatás
- **Függőséginjekció**: Beépített DI konténer integráció
- **Konfigurációkezelés**: IConfiguration és Options minták
- **Async/Await**: Kiemelt aszinkron programozási támogatás

### Gyártásra kész minták

- **Naplózás integráció**: ILogger és strukturált naplózás támogatás
- **Egészségellenőrzések**: Beépített monitorozás és diagnosztika
- **Konfiguráció érvényesítés**: Erős típusosság adat annotációkkal
- **Hibakezelés**: Strukturált kivételkezelés

## 🔧 Műszaki architektúra

### Alapvető .NET komponensek

- **Microsoft.Extensions.AI**: Egységes AI szolgáltatási absztrakciók
- **Microsoft.Agents.AI**: Vállalati ügynökösszehangoló keretrendszer
- **Azure OpenAI (Responses API)**: Nagyteljesítményű API kliensminták
- **Konfigurációs rendszer**: appsettings.json és környezet integráció

### Tervezési minta megvalósítás

```mermaid
graph LR
    A[IServiceCollection] --> B[Ügynök Építő]
    B --> C[Konfiguráció]
    C --> D[Eszköz Regiszter]
    D --> E[MI Ügynök]
```

## 🏗️ Bemutatott vállalati minták

### 1. **Létrehozási minták**

- **Ügynökgyár**: Központosított ügynöklétrehozás egységes konfigurációval
- **Builder Pattern**: Folyékony API összetett ügynök konfigurációhoz
- **Singleton minta**: Megosztott erőforrás- és konfigurációkezelés
- **Függőséginjektálás**: Laza kapcsolás és tesztelhetőség

### 2. **Viselkedési minták**

- **Stratégia minta**: Felcserélhető eszközvégrehajtási stratégiák
- **Parancs minta**: Kapszulázott ügynök műveletek visszavonással/ismétléssel
- **Megfigyelő minta**: Eseményvezérelt ügynök életcikluskezelés
- **Sablon metódus**: Szabványosított ügynök végrehajtási munkafolyamatok

### 3. **Strukturális minták**

- **Adapter minta**: Azure OpenAI (Responses API) integrációs réteg
- **Dekorátor minta**: Ügynök képességnövelés
- **Függöny minta**: Egyszerűsített ügynök interakciós felületek
- **Proxy minta**: Lusta betöltés és cache-elés a teljesítményért

## 📚 .NET tervezési alapelvek

### SOLID alapelvek

- **Egyetlen felelősség**: Minden komponensnek egyértelmű célja van
- **Nyitott/zárt**: Bővíthető módosítás nélkül
- **Liskov-helyettesítés**: Interfész alapú eszközmegvalósítások
- **Interfész szegregáció**: Fókuszált, összetartó interfészek
- **Függőség megfordítás**: Absztrakciókra, nem konkrétumokra támaszkodás

### Tiszta architektúra

- **Domain réteg**: Alapvető ügynök és eszköz absztrakciók
- **Alkalmazási réteg**: Ügynök összehangolás és munkafolyamatok
- **Infrastruktúra réteg**: Azure OpenAI (Responses API) integráció és külső szolgáltatások
- **Prezentációs réteg**: Felhasználói interakció és válaszformázás

## 🔒 Vállalati megfontolások

### Biztonság

- **Hitelesítő adatok kezelése**: Biztonságos API kulcs kezelése IConfiguration-nal
- **Bemeneti érvényesítés**: Erős típusosság és adat annotáció érvényesítés
- **Kimeneti tisztítás**: Biztonságos válasz feldolgozás és szűrés
- **Audit naplózás**: Átfogó műveletkövetés

### Teljesítmény

- **Aszinkron minták**: Nem blokkoló I/O műveletek
- **Kapcsolatpoolozás**: Hatékony HTTP kliens kezelés
- **Caching**: Válasz cache-elés a jobb teljesítményért
- **Erőforrás-kezelés**: Megfelelő hulladékkezelés és tisztítási minták

### Méretezhetőség

- **Szálbiztonság**: Párhuzamos ügynökvégrehajtás támogatása
- **Erőforrás-poolozás**: Hatékony erőforrás-kihasználás
- **Terhelés menedzsment**: Aránykorlátozás és vissza nyomás kezelése
- **Monitorozás**: Teljesítménymutatók és egészségellenőrzések

## 🚀 Gyártásra való telepítés

- **Konfigurációkezelés**: Környezet-specifikus beállítások
- **Naplózási stratégia**: Strukturált naplózás korrelációs azonosítókkal
- **Hibakezelés**: Globális kivételkezelés megfelelő helyreállítással
- **Monitorozás**: Alkalmazás-információk és teljesítmény számlálók
- **Tesztelés**: Egységtesztek, integrációs tesztek és terheléses tesztelési minták

Készen állsz vállalati szintű intelligens ügynökök építésére .NET-ben? Tervezzünk valami masszívat! 🏢✨

## 🚀 Első lépések

### Előfeltételek

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) vagy újabb
- Egy [Azure előfizetés](https://azure.microsoft.com/free/), Azure OpenAI erőforrással és modell telepítéssel
- Az [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — jelentkezz be az `az login` paranccsal

### Szükséges környezeti változók

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Jelentkezzen be, hogy az AzureCliCredential tokenhez jusson
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Ezután jelentkezzen be, hogy az AzureCliCredential tokenhez juthasson
az login
```

### Minta kód

A kódpélda futtatásához,

```bash
# zsh/bash
chmod +x ./03-dotnet-agent-framework.cs
./03-dotnet-agent-framework.cs
```

Vagy a dotnet CLI használatával:

```bash
dotnet run ./03-dotnet-agent-framework.cs
```

A teljes kód a [`03-dotnet-agent-framework.cs`](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs) fájlban található.

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
var session = await agent.CreateSessionAsync();

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
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->