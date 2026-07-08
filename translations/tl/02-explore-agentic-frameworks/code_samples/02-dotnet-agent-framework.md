# 🔍 Pagsisiyasat sa Microsoft Agent Framework - Pangunahing Ahente (.NET)

## 📋 Mga Layunin sa Pagkatuto

Tinutuklas ng halimbawang ito ang mga pangunahing konsepto ng Microsoft Agent Framework sa pamamagitan ng isang pangunahing implementasyon ng ahente sa .NET. Matututuhan mo ang mga pangunahing pattern ng ahente at mauunawaan kung paano gumagana ang mga intelligent agents sa ilalim gamit ang C# at ang .NET ecosystem.

### Ano ang Iyong Matutuklasan

- 🏗️ **Arkitektura ng Ahente**: Pag-unawa sa pangunahing istruktura ng mga AI agent sa .NET
- 🛠️ **Integrasyon ng Kasangkapan**: Paano gumagamit ang mga ahente ng panlabas na mga function para palawakin ang kakayahan  
- 💬 **Daloy ng Usapan**: Pamamahala ng mga multi-turn na usapan at konteksto gamit ang pamamahala ng thread
- 🔧 **Mga Pattern ng Konfigurasyon**: Pinakamahuhusay na paraan para sa setup at pamamahala ng ahente sa .NET

## 🎯 Mga Pangunahing Konsepto na Tinalakay

### Mga Prinsipyo ng Agentic Framework

- **Autonomy**: Paano gumagawa ang mga ahente ng malayang mga desisyon gamit ang mga abstraction ng AI sa .NET
- **Reactivity**: Pagtugon sa mga pagbabago sa kapaligiran at input ng gumagamit
- **Proactivity**: Pagsisimula batay sa mga layunin at konteksto
- **Social Ability**: Pakikipag-ugnayan gamit ang natural na wika sa mga thread ng usapan

### Mga Teknikal na Bahagi

- **AIAgent**: Pangunahing orchestration ng ahente at pamamahala ng usapan (.NET)
- **Tool Functions**: Pagpapalawak ng mga kakayahan ng ahente gamit ang mga method at attribute ng C#
- **Azure OpenAI Integration**: Paggamit ng mga language model sa pamamagitan ng Azure OpenAI Responses API
- **Secure Configuration**: Pamamahala ng endpoint batay sa kapaligiran

## 🔧 Teknikal na Stack

### Pangunahing Teknolohiya

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) integrasyon
- Mga pattern ng kliyenteng Azure.AI.OpenAI
- Konfigurasyon batay sa kapaligiran gamit ang DotNetEnv

### Mga Kakayahan ng Ahente

- Pag-unawa at pagbuo ng natural na wika
- Pag-tawag ng function at paggamit ng tool gamit ang mga attribute ng C#
- Mga tugon na may kamalayan sa konteksto gamit ang mga thread ng usapan
- Napapalawak na arkitektura gamit ang mga pattern ng dependency injection

## 📚 Paghahambing ng Framework

Ipinapakita ng halimbawang ito ang pamamaraan ng Microsoft Agent Framework kumpara sa iba pang mga agentic framework:

| Tampok | Microsoft Agent Framework | Iba Pang Mga Framework |
|---------|-------------------------|------------------|
| **Integrasyon** | Katutubong ecosystem ng Microsoft | Iba't ibang compatibility |
| **Kalinawan** | Malinis, madaling intindihin na API | Kadalasang kumplikadong setup |
| **Extensibility** | Madaling integrasyon ng tool | Nakasalalay sa framework |
| **Handa para sa Enterprise** | Ginawa para sa produksyon | Nag-iiba-iba depende sa framework |

## 🚀 Pagsisimula

### Mga Kinakailangan

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o mas mataas
- Isang [Azure subscription](https://azure.microsoft.com/free/) na may Azure OpenAI resource at deployment ng modelo
- Ang [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — mag-sign in gamit ang `az login`

### Kinakailangang Mga Variable sa Kapaligiran

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Pagkatapos mag-sign in upang makakuha ng token ang AzureCliCredential
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Pagkatapos mag-sign in upang makuha ng AzureCliCredential ang token
az login
```

### Halimbawang Kodigo

Upang patakbuhin ang halimbawang kodigo,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

O gamit ang dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Tingnan ang [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) para sa kumpletong kodigo.

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4o-mini";

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
    .GetOpenAIResponseClient(deployment)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Conversation Thread for Context Management
// Initialize a new conversation thread to maintain context across multiple interactions
// Threads enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentThread thread = agent.GetNewThread();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the thread parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation threads and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 Pangunahing Mga Natutunan

1. **Arkitektura ng Ahente**: Nagbibigay ang Microsoft Agent Framework ng malinis, type-safe na paraan para bumuo ng AI agents sa .NET
2. **Integrasyon ng Tool**: Ang mga function na may `[Description]` attribute ay nagiging magagamit na mga tool para sa ahente
3. **Konteksto ng Usapan**: Pinapayagan ng pamamahala ng thread ang mga multi-turn na usapan na may ganap na kamalayan sa konteksto
4. **Pamamahala ng Konfigurasyon**: Sinusunod ang mga environment variable at secure credential handling sa pinakamahuhusay na gawi ng .NET
5. **Azure OpenAI Responses API**: Ginagamit ng ahente ang Azure OpenAI Responses API sa pamamagitan ng Azure.AI.OpenAI SDK

## 🔗 Karagdagang Mga Sanggunian

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI sa Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->