# 🌍 AI Utazási Ügynök a Microsoft Agent Framework-kel (.NET)

## 📋 Forgatókönyv áttekintése

Ez a példa bemutatja, hogyan lehet intelligens utazástervező ügynököt létrehozni a Microsoft Agent Framework .NET-es verziójával. Az ügynök automatikusan képes személyre szabott egynapos útiterveket generálni véletlenszerű úti célokra világszerte.

### Fő képességek:

- 🎲 **Véletlenszerű úti cél kiválasztása**: Egy egyedi eszköz használata üdülőhelyek kiválasztásához
- 🗺️ **Intelligens utazástervezés**: Részletes naponta lebontott útiterv készítése
- 🔄 **Valós idejű adatfolyam**: Mind az azonnali, mind az adatfolyam-alapú válaszok támogatása
- 🛠️ **Egyedi eszköz integrációja**: Bemutatja, hogyan lehet bővíteni az ügynök képességeit

## 🔧 Technikai architektúra

### Alapvető technológiák

- **Microsoft Agent Framework**: A legfrissebb .NET-es megvalósítás AI ügynök fejlesztéshez
- **Azure OpenAI (Responses API)**: Az Azure OpenAI Responses API használata a modell következtetéshez
- **Azure Identity**: Biztonságos bejelentkezés `AzureCliCredential`-lel (`az login`)
- **Biztonságos konfiguráció**: Környezettől függő végpont-kezelés

### Fő összetevők

1. **AIAgent**: A fő ügynök, amely kezeli a beszélgetés folyamatát
2. **Egyedi eszközök**: `GetRandomDestination()` függvény elérhető az ügynök számára
3. **Responses kliens**: Azure OpenAI Responses alapú beszélgetési felület
4. **Adatfolyam támogatás**: Valós idejű válaszgenerálás képessége

### Integrációs minta

```mermaid
graph LR
    A[Felhasználói kérés] --> B[Mesterséges intelligencia ügynök]
    B --> C[Azure OpenAI (Válaszok API)]
    B --> D[GetRandomDestination eszköz]
    C --> E[Utazási útiterv]
    D --> E
```

## 🚀 Első lépések

### Előfeltételek

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) vagy újabb
- Egy [Azure előfizetés](https://azure.microsoft.com/free/) Azure OpenAI erőforrással és modelltelepítéssel
- Az [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — bejelentkezés `az login`-nal

### Kötelező környezeti változók

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Ezután jelentkezzen be, hogy az AzureCliCredential tokenhez juthasson
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Ezután jelentkezzen be, hogy az AzureCliCredential tokenhez juthasson
az login
```

### Mintakód

A kód példa futtatásához,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Vagy dotnet CLI használatával:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

A teljes kódot lásd a [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) fájlban.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@9.*
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

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetOpenAIResponseClient(deployment)
    .CreateAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip
// Run the agent with streaming enabled for real-time response display
// Shows the agent's thinking and response as it generates the content
// Provides better user experience with immediate feedback
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 Fő tanulságok

1. **Ügynök architektúra**: A Microsoft Agent Framework tiszta, típusbiztos megközelítést nyújt AI ügynökök építéséhez .NET-ben
2. **Eszköz integráció**: A `[Description]` attribútummal ellátott függvények elérhető eszközökké válnak az ügynök számára
3. **Konfiguráció menedzsment**: A környezeti változók és a biztonságos hitelesítés a .NET legjobb gyakorlatai szerint működik
4. **Azure OpenAI Responses API**: Az ügynök az Azure.AI.OpenAI SDK-n keresztül használja az Azure OpenAI Responses API-t

## 🔗 További források

- [Microsoft Agent Framework dokumentáció](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI a Microsoft Foundryban](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Egy fájlban futó alkalmazások](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->