# 🛠️ Advanced Tool Use wit Azure OpenAI (Responses API) (.NET)

## 📋 Wetin You Go Learn

Dis notebook dey show how enterprise-grade tool integration patterns dey work wit Microsoft Agent Framework for .NET wit Azure OpenAI (Responses API). You go learn how to build correct agents wey get multiple specialized tools, use C# strong typing and .NET enterprise features well well.

### Advanced Tool Skills Weh You Go Master

- 🔧 **Multi-Tool Architecture**: How to build agents wey get plenty specialized skills
- 🎯 **Type-Safe Tool Execution**: How to use C# compile-time validation sharp sharp
- 📊 **Enterprise Tool Patterns**: How to design production-proof tools and handle errors
- 🔗 **Tool Composition**: How to join tools for complex business waka

## 🎯 .NET Tool Architecture Benefits

### Enterprise Tool Features

- **Compile-Time Validation**: Strong typing make sure tool parameters correct
- **Dependency Injection**: IoC container join to manage tools
- **Async/Await Patterns**: Tools dey run without block and resource management proper
- **Structured Logging**: Built-in logging help monitor tool running

### Production-Ready Patterns

- **Exception Handling**: Complete error management with typed exceptions
- **Resource Management**: Proper disposal and memory management style
- **Performance Monitoring**: Built-in metrics and performance counters
- **Configuration Management**: Type-safe configuration wit validation

## 🔧 Technical Architecture

### Core .NET Tool Parts

- **Microsoft.Extensions.AI**: One tool abstraction level wey unify everything
- **Microsoft.Agents.AI**: Enterprise-grade tool orchestration
- **Azure OpenAI (Responses API)**: High-performance API client wit connection pooling

### Tool Execution Pipeline

```mermaid
graph LR
    A[User Request] --> B[Agent Analysis]
    B --> C[Tool Selection]
    C --> D[Type Validation]
    B --> E[Parameter Binding]
    E --> F[Tool Execution]
    C --> F
    F --> G[Result Processing]
    D --> G
    G --> H[Response]
```

## 🛠️ Tool Categories & Patterns

### 1. **Data Processing Tools**

- **Input Validation**: Strong typing wit data annotations
- **Transform Operations**: Type-safe data conversion and formatting
- **Business Logic**: Domain-special calculation and analysis tools
- **Output Formatting**: Structured response generation

### 2. **Integration Tools** 

- **API Connectors**: RESTful service integration wit HttpClient
- **Database Tools**: Entity Framework integration to access data
- **File Operations**: Secure file system operations wit validation
- **External Services**: Third-party service integration patterns

### 3. **Utility Tools**

- **Text Processing**: String manipulation and formatting utilities
- **Date/Time Operations**: Culture-aware date/time calculations
- **Mathematical Tools**: Precision calculations and statistical operations
- **Validation Tools**: Business rule validation and data verification

Ready to build strong enterprise-grade agents with powerful, type-safe tool skills inside .NET? Make we architect some professional-grade solution! 🏢⚡

## 🚀 How to Start

### Wetin You Need First

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) or higher
- Azure Subscription [https://azure.microsoft.com/free/] wit Azure OpenAI resource plus model deployment
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — sign in wit `az login`

### Environment Variables Weh You Need

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# Den sign in make AzureCliCredential fit get token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# Den sign in so AzureCliCredential fit get token
az login
```

### Sample Code

To run the example code,

```bash
# zsh/bash
chmod +x ./04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Or use the dotnet CLI:

```bash
dotnet run ./04-dotnet-agent-framework.cs
```

Check [`04-dotnet-agent-framework.cs`](../../../../04-tool-use/code_samples/04-dotnet-agent-framework.cs) for the full code.

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

// Create New Conversation Session for Context Management
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
await using var session = await agent.CreateSessionAsync();

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->