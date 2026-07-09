# 🔍 Di Basics We Dey Learn About Microsoft Agent Framework - Basic Agent (.NET)

## 📋 Wetin You Go Learn

Dis example go show di main tori dem for Microsoft Agent Framework wit basic agent wey dem implement for .NET. You go sabi di basic pattern dem wey agent dem dey use and you go understand how smart agent dem dey work for back ground using C# and di .NET system dem.

### Wetin You Go Discover

- 🏗️ **Agent Architecture**: How di basic structure of AI agents for .NET be
- 🛠️ **Tool Integration**: How agents dey use outside functions to add beta power
- 💬 **Conversation Flow**: How to manage many-turn talk and context using thread management
- 🔧 **Configuration Patterns**: Best way to setup and manage agent for .NET

## 🎯 Main Tori We Cover

### Agent Framework Principles

- **Autonomy**: How agents dey make their own arrangement using .NET AI abstraction
- **Reactivity**: How agents dey respond when environment or user tori change
- **Proactivity**: How agents dey take action based on their targets and context
- **Social Ability**: How agents dey interact by natural language for conversation threads

### Technical Parts

- **AIAgent**: Di main agent wey dey manage talk and things for .NET
- **Tool Functions**: How to add agent power with C# methods and attributes
- **Azure OpenAI Integration**: How to use language models through Azure OpenAI Responses API
- **Secure Configuration**: How to manage environment endpoints safely

## 🔧 Technical Stuff We Dey Use

### Main Technologies

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) integration
- Azure.AI.OpenAI client patterns
- Environment-based configuration with DotNetEnv

### Agent Capabilities

- Natural language understanding and creation
- Function calling and tool use with C# attributes
- Context-aware responses with talk threads
- Extensible architecture with dependency injection patterns

## 📚 Framework Comparison

Dis example dey show how Microsoft Agent Framework different from other agent frameworks:

| Feature | Microsoft Agent Framework | Other Frameworks |
|---------|-------------------------|------------------|
| **Integration** | Native Microsoft system | Different compatibility |
| **Simplicity** | Clean, easy API | Sometimes complicated setup |
| **Extensibility** | Easy to add tools | Depends on framework |
| **Enterprise Ready** | Made for production use | Depends on framework |

## 🚀 How To Start

### Wetin You Need First

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) or better
- One [Azure subscription](https://azure.microsoft.com/free/) wey get Azure OpenAI resource and model deployment
- Di [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — sign in wit `az login`

### Environment Variables Wey Dem Need

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Den sign in make AzureCliCredential fit get token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Den sign in so AzureCliCredential fit get token
az login
```

### Sample Code

To run di code sample,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Or use di dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Check [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) for di full code.

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

## 🎓 Main Points Wey You For Remember

1. **Agent Architecture**: Microsoft Agent Framework sabi build type-safe and clear AI agents for .NET
2. **Tool Integration**: Function wey dem mark with `[Description]` attribute fit become tools wey agent fit use
3. **Conversation Context**: Thread management make multi-turn talk get correct context for each talk
4. **Configuration Management**: Environment variables and proper secure credential handling follow di best .NET style
5. **Azure OpenAI Responses API**: Agent dey use Azure OpenAI Responses API through Azure.AI.OpenAI SDK

## 🔗 More Resources

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI in Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->