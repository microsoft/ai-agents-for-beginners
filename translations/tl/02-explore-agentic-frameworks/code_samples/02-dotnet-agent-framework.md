# 🔍 Pagsusuri sa Microsoft Agent Framework - Basic Agent (.NET)

## 📋 Mga Layunin ng Pagkatuto

Tinutuklas ng halimbawang ito ang mga pangunahing konsepto ng Microsoft Agent Framework sa pamamagitan ng isang basic agent implementation sa .NET. Matututuhan mo ang mga pangunahing pattern ng mga ahente at maunawaan kung paano gumagana ang mga intelligent agents sa likod ng eksena gamit ang C# at ang .NET ecosystem.

### Ano ang Iyong Matutuklasan

- 🏗️ **Arkitektura ng Ahente**: Pag-unawa sa pangunahing istruktura ng mga AI agent sa .NET
- 🛠️ **Integrasyon ng Tool**: Kung paano ginagamit ng mga ahente ang mga panlabas na function para palawakin ang kakayahan  
- 💬 **Daloy ng Usapan**: Pamamahala ng mga multi-turn na pag-uusap at konteksto gamit ang thread management
- 🔧 **Mga Pattern ng Konfigurasyon**: Pinakamahuhusay na kasanayan para sa setup at pamamahala ng ahente sa .NET

## 🎯 Mga Pangunahing Konsepto na Tinalakay

### Mga Prinsipyo ng Agentic Framework

- **Autonomiya**: Kung paano gumagawa ang mga ahente ng independiyenteng mga desisyon gamit ang .NET AI abstractions
- **Reaktibidad**: Pagtugon sa mga pagbabago sa kapaligiran at mga input ng user
- **Proaktibidad**: Pagsisimula ng aksyon batay sa mga layunin at konteksto
- **Kakayahang Panlipunan**: Pakikipag-ugnayan gamit ang natural na wika sa mga thread ng pag-uusap

### Mga Teknikal na Komponent

- **AIAgent**: Pangunahing orchestration ng ahente at pamamahala ng pag-uusap (.NET)
- **Mga Tool na Function**: Pagpapalawak ng kakayahan ng ahente gamit ang mga C# method at attribute
- **Integrasyon ng Azure OpenAI**: Paggamit ng mga language model sa pamamagitan ng Azure OpenAI Responses API
- **Secure Configuration**: Pamamahala ng endpoint batay sa kapaligiran

## 🔧 Teknikal na Stack

### Pangunahing Teknolohiya

- Microsoft Agent Framework (.NET)
- Integrasyon ng Azure OpenAI (Responses API)
- Patterns ng Azure.AI.OpenAI client
- Konfigurasyon batay sa kapaligiran gamit ang DotNetEnv

### Mga Kakayahan ng Ahente

- Pag-unawa at paglikha ng natural na wika
- Pagtawag ng function at paggamit ng tool gamit ang mga C# attribute
- Mga tugon na may kaalaman sa konteksto gamit ang mga sesyon ng pag-uusap
- Extensible na arkitektura gamit ang mga dependency injection pattern

## 📚 Paghahambing ng Framework

Ipinapakita ng halimbawang ito ang approach ng Microsoft Agent Framework kumpara sa ibang mga agentic framework:

| Feature | Microsoft Agent Framework | Ibang Framework |
|---------|-------------------------|------------------|
| **Integrasyon** | Katutubong Microsoft ecosystem | Iba-ibang compatible |
| **Simple** | Malinis, intuitive na API | Kadalasang komplikadong setup |
| **Extensibility** | Madaling integrasyon ng tool | Nakadepende sa framework |
| **Handa para sa Enterprise** | Ginawa para sa produksyon | Nagbabago depende sa framework |

## 🚀 Pagsisimula

### Mga Kinakailangan

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o mas mataas
- Isang [Azure subscription](https://azure.microsoft.com/free/) na may Azure OpenAI resource at model deployment
- Ang [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — mag-sign in gamit ang `az login`

### Mga Kinakailangang Environment Variable

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Pagkatapos mag-sign in upang makakuha ang AzureCliCredential ng token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Pagkatapos mag-sign in upang makakuha ng token ang AzureCliCredential
az login
```

### Sample Code

Para patakbuhin ang code example,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

O gamit ang dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Tingnan ang [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) para sa kumpletong code.

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

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
    .GetChatClient(deployment)
    .AsAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Session for Context Management.
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentSession session = await agent.CreateSessionAsync();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the session parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", session))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation sessions and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", session))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 Mga Pangunahing Aral

1. **Arkitektura ng Ahente**: Nagbibigay ang Microsoft Agent Framework ng malinis, type-safe na paraan para gumawa ng AI agents sa .NET
2. **Integrasyon ng Tool**: Ang mga function na decorated ng `[Description]` attributes ay nagiging available na tool para sa ahente
3. **Konteksto ng Pag-uusap**: Pinapahintulutan ng session management ang multi-turn na pag-uusap na may buong kaalaman sa konteksto
4. **Pamamahala ng Konfigurasyon**: Sinusunod ang mga environment variable at secure na paghawak ng kredensyal ng pinakamahuhusay na kasanayan ng .NET
5. **Azure OpenAI Responses API**: Ginagamit ng ahente ang Azure OpenAI Responses API sa pamamagitan ng Azure.AI.OpenAI SDK

## 🔗 Karagdagang Mga Sanggunian

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI in Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->