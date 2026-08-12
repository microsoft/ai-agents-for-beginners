# 🌍 AI reisibüroo Microsoft Agent Frameworkiga (.NET)

## 📋 Stsenaariumi ülevaade

See näide demonstreerib, kuidas ehitada nutikas reisiplaanimise agent Microsoft Agent Frameworki abil .NET-is. Agent suudab automaatselt genereerida isikupärastatud päevareise juhuslike sihtkohtade jaoks üle kogu maailma.

### Põhifunktsioonid:

- 🎲 **Juhusliku sihtkoha valik**: Kasutab kohandatud tööriista puhkusekohtade valimiseks
- 🗺️ **Intelligentne reisi planeerimine**: Loob üksikasjalikke päevakavasid
- 🔄 **Reaalajas voogesitus**: Toetab nii koheseid kui ka voogedastusvastuseid
- 🛠️ **Kohandatud tööriista integratsioon**: Näitab, kuidas laiendada agendi võimekust

## 🔧 Tehniline arhitektuur

### Põhilised tehnoloogiad

- **Microsoft Agent Framework**: Viimane .NET-i rakendus AI agentide arendamiseks
- **Azure OpenAI (Responses API)**: Kasutab Azure OpenAI Responses API mudeli arvutamiseks
- **Azure Identity**: Turvaline sisselogimine `AzureCliCredential` abil (`az login`)
- **Turvaline konfiguratsioon**: Keskkonnapõhine lõpp-punktide haldus

### Põhikomponendid

1. **AIAgent**: Peamine agendi orkestreerija vestlusvoo haldamiseks
2. **Kohandatud tööriistad**: `GetRandomDestination()` funktsioon on agendile kättesaadav
3. **Responses klient**: Azure OpenAI Responses-põhine vestlusliides
4. **Voogedastuse tugi**: Reaalajas vastuste genereerimise võimekus

### Integratsioonimudel

```mermaid
graph LR
    A[Kasutaja Päring] --> B[Tehisintellekti Agent]
    B --> C[Azure OpenAI (Vastuste API)]
    B --> D[GetRandomDestination Tööriist]
    C --> E[Reisi Kavad]
    D --> E
```

## 🚀 Alustamine

### Eeltingimused

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) või uuem
- [Azure tellimus](https://azure.microsoft.com/free/) koos Azure OpenAI ressursi ja mudeli kasutuselevõtuga
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — logi sisse käsuga `az login`

### Nõutavad keskkonnamuutujad

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Seejärel logi sisse, et AzureCliCredential saaks tokeni kätte
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Seejärel logi sisse, et AzureCliCredential saaks tokeni saada
az login
```

### Näidiskood

Koodi näite käivitamiseks,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Või kasutades dotnet CLI-t:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Vaata täielikku koodi failist [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs).

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

## 🎓 Peamised õppetunnid

1. **Agendi arhitektuur**: Microsoft Agent Framework pakub puhast, tüübiturvalist lähenemist AI agentide ehitamiseks .NET-is
2. **Tööriistade integratsioon**: Funktsioonid, mis on märgistatud `[Description]` atribuutidega, muutuvad agendi jaoks kättesaadavaks tööriistadeks
3. **Konfiguratsiooni haldus**: Keskkonnamuutujad ja turvaline mandaadi haldus järgivad .NET parimaid tavasid
4. **Azure OpenAI Responses API**: Agent kasutab Azure OpenAI Responses API-d Azure.AI.OpenAI SDK kaudu

## 🔗 Lisamaterjalid

- [Microsoft Agent Frameworki dokumentatsioon](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI Microsoft Foundry's](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET ühe faili rakendused](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->