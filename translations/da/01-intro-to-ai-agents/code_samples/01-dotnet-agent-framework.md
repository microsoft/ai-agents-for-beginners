# 🌍 AI Rejseagent med Microsoft Agent Framework (.NET)

## 📋 Scenarie Oversigt

Dette eksempel demonstrerer, hvordan man bygger en intelligent rejseplanlægningsagent ved hjælp af Microsoft Agent Framework for .NET. Agenten kan automatisk generere personlige endagsrejseplaner til tilfældige destinationer rundt om i verden.

### Nøglefunktioner:

- 🎲 **Tilfældig Destination Udvælgelse**: Bruger et brugerdefineret værktøj til at vælge feriesteder
- 🗺️ **Intelligent Rejseplanlægning**: Opretter detaljerede dags-for-dags rejseplaner
- 🔄 **Streaming i Real-tid**: Understøtter både umiddelbare og streamede svar
- 🛠️ **Integration af Brugerdefinerede Værktøjer**: Viser, hvordan agentfunktionalitet kan udvides

## 🔧 Teknisk Arkitektur

### Kerne Teknologier

- **Microsoft Agent Framework**: Seneste .NET-implementering til AI agentudvikling
- **Azure OpenAI (Responses API)**: Bruger Azure OpenAI Responses API til modelinferens
- **Azure Identity**: Sikker login via `AzureCliCredential` (`az login`)
- **Sikker Konfiguration**: Miljøbaseret endpoint-administration

### Nøglekomponenter

1. **AIAgent**: Hovedagenten, der orkestrerer samtaleflowet
2. **Brugerdefinerede Værktøjer**: `GetRandomDestination()` funktion tilgængelig for agenten
3. **Responses Client**: Azure OpenAI Responses-baseret samtaleinterface
4. **Streaming Understøttelse**: Realtidsgenerering af svar

### Integrationsmønster

```mermaid
graph LR
    A[Brugerforespørgsel] --> B[AI Agent]
    B --> C[Azure OpenAI (Svar API)]
    B --> D[GetRandomDestination Værktøj]
    C --> E[Rejseplan]
    D --> E
```

## 🚀 Kom godt i gang

### Forudsætninger

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller nyere
- Et [Azure-abonnement](https://azure.microsoft.com/free/) med en Azure OpenAI-ressource og en modeludrulning
- Azure CLI ([Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)) — log ind med `az login`

### Nødvendige Miljøvariabler

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Log ind, så AzureCliCredential kan få en token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Log ind, så AzureCliCredential kan få et token
az login
```

### Eksempel på kode

For at køre kodeeksemplet,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Eller ved brug af dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Se [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) for den komplette kode.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.4.1
#:package Microsoft.Agents.AI.OpenAI@1.1.0
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

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
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

## 🎓 Vigtige Læringspunkter

1. **Agentarkitektur**: Microsoft Agent Framework giver en ren, type-sikker tilgang til at bygge AI-agenter i .NET
2. **Værktøjsintegration**: Funktioner dekoreret med `[Description]` attributter bliver tilgængelige værktøjer for agenten
3. **Konfigurationsstyring**: Miljøvariabler og sikker håndtering af legitimations-oplysninger følger .NET bedste praksisser
4. **Azure OpenAI Responses API**: Agenten bruger Azure OpenAI Responses API gennem Azure.AI.OpenAI SDK

## 🔗 Yderligere Ressourcer

- [Microsoft Agent Framework Dokumentation](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI i Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->