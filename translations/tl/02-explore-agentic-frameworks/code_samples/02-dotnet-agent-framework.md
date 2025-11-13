<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T13:30:06+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "tl"
}
-->
# 🔍 Paggalugad sa Microsoft Agent Framework - Basic Agent (.NET)

## 📋 Mga Layunin sa Pagkatuto

Ang halimbawang ito ay naglalaman ng mga pangunahing konsepto ng Microsoft Agent Framework sa pamamagitan ng isang simpleng implementasyon ng agent sa .NET. Matututuhan mo ang mga pangunahing pattern ng agentic at mauunawaan kung paano gumagana ang mga intelligent agents gamit ang C# at ang .NET ecosystem.

### Ano ang Iyong Matutuklasan

- 🏗️ **Arkitektura ng Agent**: Pag-unawa sa pangunahing istruktura ng AI agents sa .NET  
- 🛠️ **Integrasyon ng Tool**: Paano ginagamit ng mga agent ang mga panlabas na function upang mapalawak ang kakayahan  
- 💬 **Daloy ng Usapan**: Pamamahala ng multi-turn na usapan at konteksto gamit ang thread management  
- 🔧 **Mga Pattern ng Konfigurasyon**: Mga pinakamahusay na kasanayan para sa pag-setup at pamamahala ng agent sa .NET  

## 🎯 Mga Pangunahing Konseptong Tinalakay

### Mga Prinsipyo ng Agentic Framework

- **Autonomy**: Paano gumagawa ng mga independiyenteng desisyon ang mga agent gamit ang .NET AI abstractions  
- **Reactivity**: Pagtugon sa mga pagbabago sa kapaligiran at input ng user  
- **Proactivity**: Pagsasagawa ng inisyatibo batay sa mga layunin at konteksto  
- **Social Ability**: Pakikipag-ugnayan gamit ang natural na wika sa mga thread ng usapan  

### Mga Teknikal na Komponent

- **AIAgent**: Pangunahing orkestrasyon ng agent at pamamahala ng usapan (.NET)  
- **Tool Functions**: Pagpapalawak ng kakayahan ng agent gamit ang mga C# method at attribute  
- **OpenAI Integration**: Paggamit ng mga language model sa pamamagitan ng standardized .NET APIs  
- **Secure Configuration**: Pamamahala ng API key batay sa environment  

## 🔧 Teknikal na Stack

### Mga Pangunahing Teknolohiya

- Microsoft Agent Framework (.NET)  
- Integrasyon ng GitHub Models API  
- Mga pattern ng OpenAI-compatible client  
- Konfigurasyon batay sa environment gamit ang DotNetEnv  

### Mga Kakayahan ng Agent

- Pag-unawa at pagbuo ng natural na wika  
- Pagtawag ng function at paggamit ng tool gamit ang mga C# attribute  
- Mga tugon na may kamalayan sa konteksto gamit ang mga thread ng usapan  
- Extensible na arkitektura gamit ang mga pattern ng dependency injection  

## 📚 Paghahambing ng Framework

Ipinapakita ng halimbawang ito ang diskarte ng Microsoft Agent Framework kumpara sa iba pang mga agentic framework:

| Tampok | Microsoft Agent Framework | Iba Pang Framework |
|--------|---------------------------|--------------------|
| **Integrasyon** | Katutubong Microsoft ecosystem | Iba-ibang compatibility |
| **Kalinawan** | Malinis, intuitive na API | Madalas komplikadong setup |
| **Extensibility** | Madaling integrasyon ng tool | Depende sa framework |
| **Handa para sa Enterprise** | Ginawa para sa produksyon | Nag-iiba depende sa framework |

## 🚀 Pagsisimula

### Mga Kinakailangan

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o mas mataas  
- [GitHub Models API access token](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### Kinakailangang Environment Variables

```bash
# zsh/bash
export GH_TOKEN=<your_github_token>
export GH_ENDPOINT=https://models.github.ai/inference
export GH_MODEL_ID=openai/gpt-5-mini
```
  
```powershell
# PowerShell
$env:GH_TOKEN = "<your_github_token>"
$env:GH_ENDPOINT = "https://models.github.ai/inference"
$env:GH_MODEL_ID = "openai/gpt-5-mini"
```
  

### Halimbawang Code

Upang patakbuhin ang halimbawa ng code,  

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

using System.ClientModel;
using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using OpenAI;

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

// Extract configuration from environment variables
// Retrieve the GitHub Models API endpoint, defaults to https://models.github.ai/inference if not specified
// Retrieve the model ID, defaults to openai/gpt-5-mini if not specified
// Retrieve the GitHub token for authentication, throws exception if not specified
var github_endpoint = Environment.GetEnvironmentVariable("GH_ENDPOINT") ?? "https://models.github.ai/inference";
var github_model_id = Environment.GetEnvironmentVariable("GH_MODEL_ID") ?? "openai/gpt-5-mini";
var github_token = Environment.GetEnvironmentVariable("GH_TOKEN") ?? throw new InvalidOperationException("GH_TOKEN is not set.");

// Configure OpenAI Client Options
// Create configuration options to point to GitHub Models endpoint
// This redirects OpenAI client calls to GitHub's model inference service
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
// Create OpenAI client using GitHub token for authentication
// Configure it to use GitHub Models endpoint instead of OpenAI directly
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

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
// Initialize complete agent pipeline: OpenAI client → Chat client → AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
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
  

## 🎓 Mga Pangunahing Aral

1. **Arkitektura ng Agent**: Ang Microsoft Agent Framework ay nagbibigay ng malinis, type-safe na diskarte sa paggawa ng AI agents sa .NET  
2. **Integrasyon ng Tool**: Ang mga function na may `[Description]` attributes ay nagiging magagamit na mga tool para sa agent  
3. **Konteksto ng Usapan**: Ang thread management ay nagbibigay-daan sa multi-turn na usapan na may ganap na kamalayan sa konteksto  
4. **Pamamahala ng Konfigurasyon**: Ang mga environment variable at secure na paghawak ng kredensyal ay sumusunod sa pinakamahusay na kasanayan ng .NET  
5. **OpenAI Compatibility**: Ang integrasyon ng GitHub Models ay gumagana nang maayos sa pamamagitan ng OpenAI-compatible APIs  

## 🔗 Karagdagang Mga Mapagkukunan

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/agent-framework)  
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->