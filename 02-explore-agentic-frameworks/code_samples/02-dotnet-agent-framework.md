# 🔍 Exploring Agentic Frameworks - Basic Agent (.NET)

## 📋 Learning Objectives

This notebook explores the fundamental concepts of the Microsoft Agent Framework through a basic agent implementation in .NET. You'll learn core agentic patterns and understand how intelligent agents work under the hood using C# and the .NET ecosystem.

**What You'll Discover:**
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
- **OpenAI Integration**: Leveraging language models through standardized .NET APIs
- **Environment Management**: Secure configuration and credential handling with DotNetEnv

## ⚙️ Prerequisites & Setup

**Required Dependencies:**
- .NET 9.0 SDK or higher
- Visual Studio 2022 or VS Code with C# extension

**NuGet Packages:**
- `Microsoft.Extensions.AI` - Core AI abstractions
- `Microsoft.Extensions.AI.OpenAI` - OpenAI integration (preview)
- `DotNetEnv` - Environment variable management

**Environment Configuration (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Technical Stack

**Core Technologies:**
- Microsoft Agent Framework (.NET)
- GitHub Models API integration
- OpenAI-compatible client patterns
- Environment-based configuration with DotNetEnv

**Agent Capabilities:**
- Natural language understanding and generation
- Function calling and tool usage with C# attributes
- Context-aware responses with conversation threads
- Extensible architecture with dependency injection patterns

## 📚 Framework Comparison

This example demonstrates the Microsoft Agent Framework approach in .NET compared to other platforms:

| Feature | .NET Agent Framework | Python Equivalents |
|---------|---------------------|-------------------|
| **Type Safety** | Strong typing with C# | Dynamic typing |
| **Integration** | Native .NET ecosystem | Varied compatibility |
| **Performance** | Compiled code performance | Interpreted execution |
| **Enterprise Ready** | Built for production .NET apps | Varies by framework |
| **Tooling** | Visual Studio integration | IDE-dependent |

## 🚀 Getting Started

Follow the cells below to build your first basic agent in .NET and understand foundational agentic concepts!

## 📦 Installation and Setup

This example is available as a runnable .NET Single File App. See the accompanying `02-dotnet-agent-framework.cs` file for the complete implementation.

To run this example:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Or using the dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Code Walkthrough

The complete implementation includes:

### 1. Package Dependencies

```csharp
// Core AI abstraction layer for .NET applications
#r "nuget: Microsoft.Extensions.AI, 9.9.1"

// Microsoft Agent Framework OpenAI integration
#r "nuget: Microsoft.Agents.AI.OpenAI, 1.0.0-preview.251001.3"

// Core Microsoft Agent Framework library
#r "nuget: Microsoft.Agents.AI, 1.0.0-preview.251001.3"

// Environment variable management
#r "nuget: DotNetEnv, 3.1.1"
```

### 2. Essential Imports

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Environment Configuration

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Tool Function Definition

```csharp
// Random destination generator tool
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
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
    
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}
```

### 5. Configuration and Client Setup

```csharp
// Extract environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? 
    throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? 
    throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI client for GitHub Models
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI client
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);
```

### 6. Agent Configuration

```csharp
const string AGENT_NAME = "TravelAgent";

const string AGENT_INSTRUCTIONS = @"You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
""Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?""

Always prioritize user preferences. If they mention a specific destination like ""Bali"" or ""Paris,"" focus your planning on that location rather than suggesting alternatives.
";
```

### 7. Agent Initialization

```csharp
// Create AI agent with travel planning capabilities
AIAgent agent = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions)
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create((Func<string>)GetRandomDestination)]
    );
```

### 8. Conversation Management

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Key Takeaways

1. **Agent Architecture**: The Microsoft Agent Framework provides a clean, type-safe approach to building AI agents in .NET
2. **Tool Integration**: Functions decorated with `[Description]` attributes become available tools for the agent
3. **Conversation Context**: Thread management enables multi-turn conversations with full context awareness
4. **Configuration Management**: Environment variables and secure credential handling follow .NET best practices
5. **OpenAI Compatibility**: GitHub Models integration works seamlessly through OpenAI-compatible APIs

## 🔗 Additional Resources

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)
