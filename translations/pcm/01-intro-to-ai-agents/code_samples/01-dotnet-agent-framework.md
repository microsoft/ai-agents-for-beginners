# 🌍 AI Travel Agent wit Microsoft Agent Framework (.NET)

## 📋 Scenario Overview

Dis example dey show how to build intelligent travel planning agent using Microsoft Agent Framework for .NET. Di agent fit automatically create personalized day-trip itineraries for random destinations all over di world.

### Key Capabilities:

- 🎲 **Random Destination Selection**: Dey use custom tool to pick vacation spots
- 🗺️ **Intelligent Trip Planning**: Dey create detailed day-by-day itineraries
- 🔄 **Real-time Streaming**: E dey support both immediate and streaming responses
- 🛠️ **Custom Tool Integration**: E dey show how to extend agent capabilities

## 🔧 Technical Architecture

### Core Technologies

- **Microsoft Agent Framework**: Latest .NET implementation for AI agent development
- **Azure OpenAI (Responses API)**: Dey use Azure OpenAI Responses API for model inference
- **Azure Identity**: Secure sign-in with `AzureCliCredential` (`az login`)
- **Secure Configuration**: Environment-based endpoint management

### Key Components

1. **AIAgent**: Na main agent wey dey handle conversation flow
2. **Custom Tools**: `GetRandomDestination()` function wey agent fit use
3. **Responses Client**: Azure OpenAI Responses-based conversation interface
4. **Streaming Support**: Real-time response generation capabilities

### Integration Pattern

```mermaid
graph LR
    A[User Request] --> B[AI Agent]
    B --> C[Azure OpenAI (Responses API)]
    B --> D[GetRandomDestination Tool]
    C --> E[Travel Itinerary]
    D --> E
```

## 🚀 Getting Started

### Prerequisites

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) or higher
- An [Azure subscription](https://azure.microsoft.com/free/) with Azure OpenAI resource and a model deployment
- The [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — sign in wit `az login`

### Required Environment Variables

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Den sign in so AzureCliCredential fit get token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Den sign in make AzureCliCredential fit get token
az login
```

### Sample Code

To run di code example,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Or using di dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

See [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) for di complete code.

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

## 🎓 Key Takeaways

1. **Agent Architecture**: Microsoft Agent Framework dey provide clean, type-safe approach to build AI agents for .NET
2. **Tool Integration**: Functions wey get `[Description]` attributes go be available tools for di agent
3. **Configuration Management**: Environment variables and secure credential handling follow .NET best practices
4. **Azure OpenAI Responses API**: Di agent dey use Azure OpenAI Responses API through Azure.AI.OpenAI SDK

## 🔗 Additional Resources

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI in Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->