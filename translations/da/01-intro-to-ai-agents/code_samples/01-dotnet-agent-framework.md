# 🌍 AI Rejseagent med Microsoft Agent Framework (.NET)

## 📋 Scenarieoversigt

Dette eksempel demonstrerer, hvordan man bygger en intelligent rejseplanlægningsagent ved hjælp af Microsoft Agent Framework for .NET. Agenten kan automatisk generere personlige dagstursrejseplaner for tilfældige destinationer rundt om i verden.

### Nøglefunktioner:

- 🎲 **Tilfældig destinationsvalg**: Bruger et brugerdefineret værktøj til at vælge feriesteder
- 🗺️ **Intelligent rejseplanlægning**: Opretter detaljerede dags-for-dags rejseplaner
- 🔄 **Realtidsstreaming**: Understøtter både øjeblikkelige og streaming-svar
- 🛠️ **Brugerdefineret værktøjsintegration**: Viser, hvordan man udvider agentens kapaciteter

## 🔧 Teknisk Arkitektur

### Kerneteknologier

- **Microsoft Agent Framework**: Nyeste .NET-implementering til udvikling af AI-agenter
- **Azure OpenAI (Responses API)**: Bruger Azure OpenAI Responses API til modelinferenz
- **Azure Identity**: Sikker login via `AzureCliCredential` (`az login`)
- **Sikker konfiguration**: Endpunkthåndtering baseret på miljø

### Nøglekomponenter

1. **AIAgent**: Hovedagentens orkestrator, der håndterer samtaleflow
2. **Brugerdefinerede værktøjer**: `GetRandomDestination()`-funktion tilgængelig for agenten
3. **Responses Client**: Azure OpenAI Responses-baseret samtaleinterface
4. **Streaming-understøttelse**: Realtidsgenerering af svar

### Integrationsmønster

```mermaid
graph LR
    A[Brugerforespørgsel] --> B[AI Agent]
    B --> C[Azure OpenAI (Responses API)]
    B --> D[GetRandomDestination Værktøj]
    C --> E[Rejseplan]
    D --> E
```

## 🚀 Kom godt i gang

### Forudsætninger

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller nyere
- Et [Azure-abonnement](https://azure.microsoft.com/free/) med en Azure OpenAI-ressource og en modeludrulning
- Azure CLI ([Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)) — log ind med `az login`

### Krævede miljøvariable

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Log derefter ind, så AzureCliCredential kan få en token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Log derefter ind, så AzureCliCredential kan hente et token
az login
```

### Eksempelkode

For at køre kodeeksemplet,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Eller brug dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Se [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) for complete kode.

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

## 🎓 Vigtige pointer

1. **Agentarkitektur**: Microsoft Agent Framework tilbyder en ren, typesikker tilgang til at opbygge AI-agenter i .NET
2. **Værktøjsintegration**: Funktioner dekoreret med `[Description]`-attributter bliver tilgængelige værktøjer for agenten
3. **Konfigurationsstyring**: Miljøvariable og sikker håndtering af legitimationsoplysninger følger .NET bedste praksis
4. **Azure OpenAI Responses API**: Agenten bruger Azure OpenAI Responses API via Azure.AI.OpenAI SDK

## 🔗 Yderligere ressourcer

- [Microsoft Agent Framework Dokumentation](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI i Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->