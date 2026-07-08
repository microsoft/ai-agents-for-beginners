# 🌍 AI Travel Agent gamit ang Microsoft Agent Framework (.NET)

## 📋 Pangkalahatang Tanaw ng Senaryo

Ipinapakita ng halimbawa na ito kung paano bumuo ng isang matalinong ahente sa pagpaplano ng paglalakbay gamit ang Microsoft Agent Framework para sa .NET. Ang ahente ay maaaring awtomatikong gumawa ng mga personalisadong panandaliang itinerary para sa mga random na destinasyon sa buong mundo.

### Pangunahing Kakayahan:

- 🎲 **Random na Pagpili ng Destinasyon**: Gumagamit ng pasadyang kasangkapan para pumili ng mga destinasyon sa bakasyon
- 🗺️ **Matalinong Pagpaplano ng Biyahe**: Lumilikha ng detalyadong araw-araw na itineraryo
- 🔄 **Pag-stream ng Real-time**: Sinuportahan ang parehong agarang at streaming na mga tugon
- 🛠️ **Pagsasama ng Custom Tool**: Ipinapakita kung paano palawakin ang mga kakayahan ng ahente

## 🔧 Teknikal na Arkitektura

### Mga Pangunahing Teknolohiya

- **Microsoft Agent Framework**: Pinakabagong implementasyon ng .NET para sa pagbuo ng AI agent
- **Azure OpenAI (Responses API)**: Gumagamit ng Azure OpenAI Responses API para sa modelong inference
- **Azure Identity**: Ligtas na pag-sign-in gamit ang `AzureCliCredential` (`az login`)
- **Ligtas na Konfigurasyon**: Pamamahala ng endpoint base sa kapaligiran

### Pangunahing Bahagi

1. **AIAgent**: Pangunahing tagapag-organisa ng ahente na humahawak sa daloy ng pag-uusap
2. **Custom Tools**: `GetRandomDestination()` na function na available sa ahente
3. **Responses Client**: Interface ng pag-uusap gamit ang Azure OpenAI Responses
4. **Streaming Support**: Kakayahang gumawa ng tugon sa real-time

### Pattern ng Pagsasama

```mermaid
graph LR
    A[Kahilingan ng Gumagamit] --> B[Ahente ng AI]
    B --> C[Azure OpenAI (API ng mga Tugon)]
    B --> D[Kasangkapang GetRandomDestination]
    C --> E[Itinerarya ng Paglalakbay]
    D --> E
```

## 🚀 Pagsisimula

### Mga Kinakailangan

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o mas mataas pa
- Isang [Azure subscription](https://azure.microsoft.com/free/) na may Azure OpenAI resource at isang deployment ng modelo
- Ang [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — mag-sign in gamit ang `az login`

### Mga Kinakailangang Environment Variables

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Mag-sign in pagkatapos para makakuha ang AzureCliCredential ng token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Mag-sign in muna para makakuha ng token ang AzureCliCredential
az login
```

### Halimbawang Code

Para patakbuhin ang halimbawa ng code,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

O gamit ang dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Tingnan ang [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) para sa buong code.

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

## 🎓 Mga Pangunahing Aral

1. **Arkitektura ng Ahente**: Nagbibigay ang Microsoft Agent Framework ng malinis at type-safe na paraan para bumuo ng mga AI agent sa .NET
2. **Pagsasama ng Tool**: Ang mga function na may `[Description]` na attributes ay nagiging available na mga tool para sa ahente
3. **Pamamahala ng Konfigurasyon**: Ang mga environment variable at ligtas na pangangasiwa ng credential ay sumusunod sa pinakamahusay na kasanayan ng .NET
4. **Azure OpenAI Responses API**: Ginagamit ng ahente ang Azure OpenAI Responses API sa pamamagitan ng Azure.AI.OpenAI SDK

## 🔗 Karagdagang Mga Mapagkukunan

- [Dokumentasyon ng Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI sa Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->