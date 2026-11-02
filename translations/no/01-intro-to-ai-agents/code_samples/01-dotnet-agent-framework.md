# 🌍 AI Reiseagent med Microsoft Agent Framework (.NET)

## 📋 Scenariooversikt

Dette eksempelet demonstrerer hvordan bygge en intelligent reiseplanleggingsagent ved bruk av Microsoft Agent Framework for .NET. Agenten kan automatisk generere personlige dagsreiseplaner for tilfeldige reisemål rundt om i verden.

### Nøkkelfunksjoner:

- 🎲 **Tilfeldig reisemålsvalg**: Bruker et tilpasset verktøy for å velge feriesteder
- 🗺️ **Intelligent reiseplanlegging**: Lager detaljerte dagsplaner
- 🔄 **Sanntidsstrømming**: Støtter både umiddelbare og strømmede svar
- 🛠️ **Integrering av tilpassede verktøy**: Demonstrerer hvordan utvide agentens funksjoner

## 🔧 Teknisk arkitektur

### Kjerne-teknologier

- **Microsoft Agent Framework**: Nyeste .NET-implementasjon for utvikling av AI-agenter
- **Azure OpenAI (Responses API)**: Benytter Azure OpenAI Responses API til modellinferens
- **Azure Identity**: Sikker pålogging via `AzureCliCredential` (`az login`)
- **Sikker konfigurasjon**: Endepunktstyring basert på miljøvariabler

### Nøkkelkomponenter

1. **AIAgent**: Hovedagenten som orkestrerer samtaleforløpet
2. **Tilpassede verktøy**: `GetRandomDestination()` funksjon tilgjengelig for agenten
3. **Responses Client**: Samtalegrensesnitt basert på Azure OpenAI Responses
4. **Støtte for strømming**: Muligheter for generering av svar i sanntid

### Integrasjonsmønster

```mermaid
graph LR
    A[Brukerforespørsel] --> B[AI-agent]
    B --> C[Azure OpenAI (Respons-API)]
    B --> D[Verktøy for tilfeldig destinasjon]
    C --> E[Reiseplan]
    D --> E
```

## 🚀 Komme i gang

### Forutsetninger

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller nyere
- Et [Azure-abonnement](https://azure.microsoft.com/free/) med en Azure OpenAI-ressurs og en modellutrulling
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — logg inn med `az login`

### Nødvendige miljøvariabler

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Logg deretter inn slik at AzureCliCredential kan få et token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Logg deretter inn slik at AzureCliCredential kan få en token
az login
```

### Eksempelkode

For å kjøre kodeeksemplet,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Eller ved å bruke dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Se [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) for fullstendig kode.

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

## 🎓 Viktige punkter

1. **Agentarkitektur**: Microsoft Agent Framework tilbyr en ryddig, typetrygg tilnærming til bygging av AI-agenter i .NET
2. **Verktøyintegrasjon**: Funksjoner dekorert med `[Description]`-attributter blir tilgjengelige verktøy for agenten
3. **Konfigurasjonsstyring**: Miljøvariabler og sikker håndtering av legitimasjon følger .NET beste praksis
4. **Azure OpenAI Responses API**: Agenten bruker Azure OpenAI Responses API via Azure.AI.OpenAI SDK

## 🔗 Ytterligere ressurser

- [Microsoft Agent Framework Dokumentasjon](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI i Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->