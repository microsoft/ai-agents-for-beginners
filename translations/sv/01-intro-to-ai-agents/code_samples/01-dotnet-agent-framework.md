# 🌍 AI Resebyrå med Microsoft Agent Framework (.NET)

## 📋 Scenarioöversikt

Detta exempel visar hur man bygger en intelligent reseplaneringsagent med Microsoft Agent Framework för .NET. Agenten kan automatiskt generera personliga dagsutflyktsplaner för slumpmässiga destinationer runt om i världen.

### Viktiga funktioner:

- 🎲 **Slumpmässigt destinationsval**: Använder ett eget verktyg för att välja semestermål
- 🗺️ **Intelligent reseplanering**: Skapar detaljerade dag-för-dag-resplaner
- 🔄 **Strömmande i realtid**: Stöder både omedelbara och strömmande svar
- 🛠️ **Integration av egna verktyg**: Visar hur agentens funktioner kan utökas

## 🔧 Teknisk arkitektur

### Kärnteknologier

- **Microsoft Agent Framework**: Senaste .NET-implementeringen för AI-agentutveckling
- **Azure OpenAI (Responses API)**: Använder Azure OpenAI Responses API för modellinferens
- **Azure Identity**: Säker inloggning via `AzureCliCredential` (`az login`)
- **Säker konfiguration**: Miljöbaserad hantering av slutanvändarinställningar

### Viktiga komponenter

1. **AIAgent**: Huvudagent som hanterar samtalsflödet
2. **Egna verktyg**: Funktionen `GetRandomDestination()` tillgänglig för agenten
3. **Responses-klient**: Konversationsgränssnitt baserat på Azure OpenAI Responses
4. **Stöd för strömning**: Möjlighet för realtidsgenerering av svar

### Integrationsmönster

```mermaid
graph LR
    A[Användarförfrågan] --> B[AI-Agent]
    B --> C[Azure OpenAI (Svar API)]
    B --> D[Verktyget GetRandomDestination]
    C --> E[Resplan]
    D --> E
```

## 🚀 Komma igång

### Förutsättningar

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller högre
- En [Azure-prenumeration](https://azure.microsoft.com/free/) med en Azure OpenAI-resurs och en modellutplacering
- Azure CLI ([Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)) — logga in med `az login`

### Nödvändiga miljövariabler

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Logga in sedan så att AzureCliCredential kan få en token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Logga in sedan så att AzureCliCredential kan få en token
az login
```

### Exempelkod

För att köra kodexemplet,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Eller med dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Se [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) för komplett kod.

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

## 🎓 Viktiga insikter

1. **Agentarkitektur**: Microsoft Agent Framework ger ett tydligt och typ-säkert sätt att bygga AI-agenter i .NET
2. **Verktygsintegration**: Funktioner märkta med `[Description]` blir tillgängliga verktyg för agenten
3. **Konfigurationshantering**: Miljövariabler och säker hantering av autentisering följer .NET:s bästa praxis
4. **Azure OpenAI Responses API**: Agenten använder Azure OpenAI Responses API via Azure.AI.OpenAI SDK

## 🔗 Ytterligare resurser

- [Microsoft Agent Framework dokumentation](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI i Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->