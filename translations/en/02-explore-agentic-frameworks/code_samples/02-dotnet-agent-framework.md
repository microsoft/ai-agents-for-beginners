# 🔍 Exploring Microsoft Agent Framework - Basic Agent (.NET)

## 📋 Learning Objectives

This example explores the fundamental concepts of the Microsoft Agent Framework through a basic agent implementation in .NET. You'll learn core agentic patterns and understand how intelligent agents work under the hood using C# and the .NET ecosystem.

### What You'll Discover

- 🏗️ **Agent Architecture**: Understanding the basic structure of AI agents in .NET
- 🛠️ **Tool Integration**: How agents use external functions to extend capabilities  
- 💬 **Conversation Flow**: Managing multi-turn conversations and context with thread management
- 🔧 **Configuration Patterns**: Best practices for agent setup and management in .NET

## 🎯 Key Concepts Covered

### Agentic Framework Principles

- **Autonomy**: How agents make independent decisions using .NET AI abstractions
- **Reactivity**: Responding to environmental changes and user inputs
- **Proactivity**: Taking initiative based on goals and context
- **Social Ability**: Interacting through natural language with conversation threads

### Technical Components

- **AIAgent**: Core agent orchestration and conversation management (.NET)
- **Tool Functions**: Extending agent capabilities with C# methods and attributes
- **Azure OpenAI Integration**: Leveraging language models through the Azure OpenAI Responses API
- **Secure Configuration**: Environment-based endpoint management

## 🔧 Technical Stack

### Core Technologies

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) integration
- Azure.AI.OpenAI client patterns
- Environment-based configuration with DotNetEnv

### Agent Capabilities

- Natural language understanding and generation
- Function calling and tool usage with C# attributes
- Context-aware responses with conversation sessions
- Extensible architecture with dependency injection patterns

## 📚 Framework Comparison

This example demonstrates the Microsoft Agent Framework approach compared to other agentic frameworks:

| Feature | Microsoft Agent Framework | Other Frameworks |
|---------|-------------------------|------------------|
| **Integration** | Native Microsoft ecosystem | Varied compatibility |
| **Simplicity** | Clean, intuitive API | Often complex setup |
| **Extensibility** | Easy tool integration | Framework-dependent |
| **Enterprise Ready** | Built for production | Varies by framework |

## 🚀 Getting Started

### Prerequisites

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) or higher
- An [Azure subscription](https://azure.microsoft.com/free/) with an Azure OpenAI resource and a model deployment
- The [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — sign in with `az login`

### Required Environment Variables

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# Then sign in so AzureCliCredential can get a token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# Then sign in so AzureCliCredential can get a token
az login
```

### Sample Code

To run the code example,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Or using the dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

See [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) for the complete code.

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4.1-mini";

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

## 🎓 Key Takeaways

1. **Agent Architecture**: The Microsoft Agent Framework provides a clean, type-safe approach to building AI agents in .NET
2. **Tool Integration**: Functions decorated with `[Description]` attributes become available tools for the agent
3. **Conversation Context**: Session management enables multi-turn conversations with full context awareness
4. **Configuration Management**: Environment variables and secure credential handling follow .NET best practices
5. **Azure OpenAI Responses API**: The agent uses the Azure OpenAI Responses API through the Azure.AI.OpenAI SDK

## 🔗 Additional Resources

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI in Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->