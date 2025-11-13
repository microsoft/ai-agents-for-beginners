<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T15:02:36+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "pcm"
}
-->
# 🔍 Exploring Microsoft Agent Framework - Basic Agent (.NET)

## 📋 Wetin You Go Learn

Dis example dey show di basic idea of Microsoft Agent Framework wit one simple agent wey dem build for .NET. You go sabi di main agent patterns and understand how smart agents dey work for di background using C# and di .NET system.

### Wetin You Go Discover

- 🏗️ **Agent Structure**: How di basic setup of AI agents for .NET dey work
- 🛠️ **Tool Connection**: How agents dey use external functions to add more power  
- 💬 **Conversation Flow**: How to manage multi-turn talk and keep di context wit thread management
- 🔧 **Setup Patterns**: Di best way to arrange and manage agents for .NET

## 🎯 Main Ideas We Go Cover

### Agent Framework Principles

- **Autonomy**: How agents dey make decisions by demself using .NET AI tools
- **Reactivity**: How dem dey respond to changes for environment and wetin user talk
- **Proactivity**: How dem dey take action based on di goals and di situation
- **Social Ability**: How dem dey interact wit natural language through conversation threads

### Technical Parts

- **AIAgent**: Di main agent wey dey manage di talk and di work (.NET)
- **Tool Functions**: How to add more power to di agent wit C# methods and attributes
- **OpenAI Connection**: How to use language models wit di standard .NET APIs
- **Secure Setup**: How to manage API keys wit environment settings

## 🔧 Technical Stack

### Main Technologies

- Microsoft Agent Framework (.NET)
- GitHub Models API connection
- OpenAI-compatible client patterns
- Environment-based setup wit DotNetEnv

### Agent Powers

- Understanding and creating natural language
- Calling functions and using tools wit C# attributes
- Giving answers wey dey follow di context of di talk
- Flexible setup wey dey use dependency injection patterns

## 📚 Framework Comparison

Dis example dey show how Microsoft Agent Framework dey work compared to other frameworks:

| Feature | Microsoft Agent Framework | Other Frameworks |
|---------|-------------------------|------------------|
| **Integration** | Native Microsoft system | Different compatibility |
| **Simplicity** | Easy-to-use API | Sometimes hard to setup |
| **Extensibility** | Easy to add tools | Depends on di framework |
| **Enterprise Ready** | Made for production | E dey depend on di framework |

## 🚀 How to Start

### Wetin You Need

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) or higher
- [GitHub Models API access token](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)

### Environment Variables We You Go Set

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

### Example Code

To run di code example,

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

## 🎓 Wetin You Go Carry Go

1. **Agent Structure**: Microsoft Agent Framework dey give clean, type-safe way to build AI agents for .NET
2. **Tool Connection**: Functions wey get `[Description]` attributes go turn tools wey di agent fit use
3. **Conversation Context**: Thread management dey help di agent manage multi-turn talk wit full context
4. **Setup Management**: Environment variables and secure credential handling dey follow .NET best practices
5. **OpenAI Connection**: GitHub Models dey work well wit OpenAI-compatible APIs

## 🔗 More Resources

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/agent-framework)
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am accurate, abeg make you sabi say automatik transleshion fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di one wey you go take as di main source. For important mata, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->