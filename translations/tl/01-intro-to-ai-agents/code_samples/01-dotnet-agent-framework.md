# 🌍 AI Travel Agent gamit ang Microsoft Agent Framework (.NET)

## 📋 Pangkalahatang Tanawin ng Scenario

Ipinapakita ng halimbawang ito kung paano bumuo ng isang intelihenteng ahente sa pagpaplano ng paglalakbay gamit ang Microsoft Agent Framework para sa .NET. Maaari ng awtomatikong bumuo ang ahente ng mga personalisadong day-trip itinerary para sa mga random na destinasyon sa buong mundo.

### Pangunahing Mga Kakayahan:

- 🎲 **Random na Pagpili ng Destinasyon**: Gumagamit ng pasadyang kasangkapan para pumili ng mga lugar-pasyalan
- 🗺️ **Intelihenteng Pagpaplano ng Biyahe**: Lumilikha ng detalyadong araw-araw na mga itinerary
- 🔄 **Real-time Streaming**: Sinusuportahan ang parehong agarang at streaming na mga tugon
- 🛠️ **Integrasyon ng Pasadyang Kasangkapan**: Ipinapakita kung paano palawakin ang mga kakayahan ng ahente

## 🔧 Teknikal na Arkitektura

### Pangunahing Teknolohiya

- **Microsoft Agent Framework**: Pinakabagong .NET na implementasyon para sa pagbuo ng AI agent
- **Azure OpenAI (Responses API)**: Gumagamit ng Azure OpenAI Responses API para sa inference ng modelo
- **Azure Identity**: Ligtas na pag-sign in gamit ang `AzureCliCredential` (`az login`)
- **Secure Configuration**: Pamamahala ng endpoint base sa kapaligiran

### Pangunahing Mga Sangkap

1. **AIAgent**: Pangunahing tagapag-ayos ng ahente na humahawak sa daloy ng pag-uusap
2. **Pasadyang Kasangkapan**: `GetRandomDestination()` na function na magagamit ng ahente
3. **Responses Client**: Azure OpenAI Responses-based na interface para sa pag-uusap
4. **Streaming Support**: Kakayahan sa real-time na paggawa ng tugon

### Pattern ng Integrasyon

```mermaid
graph LR
    A[Kahilingan ng User] --> B[Ahente ng AI]
    B --> C[Azure OpenAI (Responses API)]
    B --> D[Tool para sa Pagkuha ng Random na Destinasyon]
    C --> E[Itineraryo ng Paglalakbay]
    D --> E
```

## 🚀 Pagsisimula

### Mga Kinakailangan

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o mas mataas pa
- Isang [Azure subscription](https://azure.microsoft.com/free/) na may Azure OpenAI resource at model deployment
- Ang [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — mag-sign in gamit ang `az login`

### Mga Kinakailangang Environment Variables

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Mag-sign in muna para makakuha ng token ang AzureCliCredential
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Mag-sign in muna para makakuha ng token ang AzureCliCredential
az login
```

### Halimbawang Code

Para patakbuhin ang halimbawang code,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

O gamit ang dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Tingnan ang [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) para sa kumpletong code.

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

## 🎓 Pangunahing Mga Natutunan

1. **Arkitektura ng Ahente**: Nagbibigay ang Microsoft Agent Framework ng malinis, type-safe na paraan sa pagbuo ng AI agents sa .NET
2. **Integrasyon ng Kasangkapan**: Ang mga function na may `[Description]` attributes ay nagiging magagamit na mga kasangkapan para sa ahente
3. **Pamamahala ng Konfigurasyon**: Ang mga environment variable at ligtas na paghawak ng kredensyal ay sumusunod sa mga pinakamahusay na praktis ng .NET
4. **Azure OpenAI Responses API**: Ginagamit ng ahente ang Azure OpenAI Responses API sa pamamagitan ng Azure.AI.OpenAI SDK

## 🔗 Karagdagang Mga Mapagkukunan

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI sa Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->