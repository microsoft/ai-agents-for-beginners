<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "23afd9be7b6ba5b69a44c3b6a78e07f6",
  "translation_date": "2025-11-06T10:06:04+00:00",
  "source_file": "01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.md",
  "language_code": "hu"
}
-->
# 🌍 AI Utazási Ügynök a Microsoft Agent Framework (.NET) segítségével

## 📋 Forgatókönyv Áttekintése

Ez a jegyzetfüzet bemutatja, hogyan lehet intelligens utazástervező ügynököt létrehozni a Microsoft Agent Framework for .NET segítségével. Az ügynök automatikusan generál személyre szabott egynapos útitervet véletlenszerű úti célokhoz világszerte.

**Fő képességek:**
- 🎲 **Véletlenszerű úti cél kiválasztása**: Egyedi eszközt használ a nyaralóhelyek kiválasztásához
- 🗺️ **Intelligens utazástervezés**: Részletes napi útitervet készít
- 🔄 **Valós idejű streaming**: Támogatja az azonnali és streaming válaszokat
- 🛠️ **Egyedi eszköz integráció**: Bemutatja, hogyan lehet bővíteni az ügynök képességeit

## 🔧 Technikai Architektúra

### Alapvető technológiák
- **Microsoft Agent Framework**: Legújabb .NET implementáció AI ügynök fejlesztéséhez
- **GitHub Models Integráció**: GitHub AI modell következtetési szolgáltatását használja
- **OpenAI API Kompatibilitás**: OpenAI kliens könyvtárakat használ egyedi végpontokkal
- **Biztonságos Konfiguráció**: Környezetalapú API kulcskezelés

### Fő komponensek
1. **AIAgent**: A fő ügynök, amely a beszélgetés folyamatát kezeli
2. **Egyedi eszközök**: `GetRandomDestination()` funkció elérhető az ügynök számára
3. **Chat kliens**: GitHub Models által támogatott beszélgetési felület
4. **Streaming támogatás**: Valós idejű válaszgenerálási képességek

### Integrációs minta
```mermaid
graph LR
    A[User Request] --> B[AI Agent]
    B --> C[GitHub Models API]
    B --> D[GetRandomDestination Tool]
    C --> E[Travel Itinerary]
    D --> E
```

## 🚀 Első lépések

**Előfeltételek:**
- .NET 10.0 vagy újabb
- GitHub Models API hozzáférési token
- Környezeti változók konfigurálása `.env` fájlban

**Szükséges környezeti változók:**
```env
GITHUB_TOKEN=your_github_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Futtassa az alábbi kódmintát sorrendben, hogy lássa az utazási ügynök működését!

---

## .NET Egyszeri Fájl Alkalmazás: AI Utazási Ügynök Példa

Tekintse meg a `01-dotnet-agent-framework.cs` fájlt a teljes futtatható kódmintáért.

```bash
dotnet run 01-dotnet-agent-framework.cs
```

### Kódminta

```csharp
static string GetRandomDestination()
{
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
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}

// Extract configuration from environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI Client Options
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

// Create AI Agent with Travel Planning Capabilities
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip (Non-Streaming)
Console.WriteLine(await agent.RunAsync("Plan me a day trip"));

// Execute Agent: Plan a Day Trip (Streaming Response)
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    Console.Write(update);
}
```

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.