<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-11T14:16:04+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "pcm"
}
-->
# 🔍 Exploring Agentic Frameworks - Basic Agent (.NET)

## 📋 Wetin You Go Learn

Dis notebook dey show di basic idea of Microsoft Agent Framework wit one simple agent wey dem don build for .NET. You go sabi di main agentic patterns and understand how intelligent agents dey work for di background using C# and di .NET system.

**Wetin You Go Discover:**
- 🏗️ **Agent Architecture**: How di basic structure of AI agents dey work for .NET
- 🛠️ **Tool Integration**: How agents dey use external functions to get more power  
- 💬 **Conversation Flow**: How to manage multi-turn conversations and keep di context wit thread management
- 🔧 **Configuration Patterns**: Di best way to set up and manage agents for .NET

## 🎯 Main Ideas We Go Cover

### Agentic Framework Principles
- **Autonomy**: How agents dey make decisions by demself using .NET AI abstractions
- **Reactivity**: How dem dey respond to changes for environment and wetin user talk
- **Proactivity**: How dem dey take action based on di goals and di context
- **Social Ability**: How dem dey interact wit natural language using conversation threads

### Technical Components
- **AIAgent**: Di main agent wey dey manage conversation and orchestration (.NET)
- **Tool Functions**: How to add more power to di agent using C# methods and attributes
- **OpenAI Integration**: How to use language models wit di standard .NET APIs
- **Environment Management**: How to handle secure configuration and credentials wit DotNetEnv

## ⚙️ Wetin You Need & Setup

**Wetin You Need:**
- .NET 9.0 SDK or higher
- Visual Studio 2022 or VS Code wit C# extension

**NuGet Packages:**
- `Microsoft.Extensions.AI` - Di main AI abstractions
- `Microsoft.Extensions.AI.OpenAI` - OpenAI integration (preview)
- `DotNetEnv` - How to manage environment variables

**Environment Configuration (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Technical Stack

**Main Technologies:**
- Microsoft Agent Framework (.NET)
- GitHub Models API integration
- OpenAI-compatible client patterns
- Environment-based configuration wit DotNetEnv

**Agent Capabilities:**
- Natural language understanding and generation
- Function calling and tool usage wit C# attributes
- Context-aware responses wit conversation threads
- Extensible architecture wit dependency injection patterns

## 📚 Framework Comparison

Dis example dey show how Microsoft Agent Framework for .NET dey work compared to other platforms:

| Feature | .NET Agent Framework | Python Equivalents |
|---------|---------------------|-------------------|
| **Type Safety** | Strong typing wit C# | Dynamic typing |
| **Integration** | Native .NET ecosystem | Varied compatibility |
| **Performance** | Compiled code performance | Interpreted execution |
| **Enterprise Ready** | Built for production .NET apps | E dey depend on framework |
| **Tooling** | Visual Studio integration | E dey depend on IDE |

## 🚀 How to Start

Follow di cells below to build your first simple agent for .NET and understand di basic agentic ideas!

## 📦 Installation and Setup

Dis example dey available as one runnable .NET Single File App. Check di `02-dotnet-agent-framework.cs` file wey dey follow for di full implementation.

To run dis example:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Or use di dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Code Walkthrough

Di full implementation get:

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

## 🎓 Wetin You Go Learn

1. **Agent Architecture**: Microsoft Agent Framework dey give clean, type-safe way to build AI agents for .NET
2. **Tool Integration**: Functions wey get `[Description]` attributes go turn tools wey di agent fit use
3. **Conversation Context**: Thread management dey help manage multi-turn conversations wit full context
4. **Configuration Management**: Environment variables and secure credential handling dey follow .NET best practices
5. **OpenAI Compatibility**: GitHub Models integration dey work well wit OpenAI-compatible APIs

## 🔗 Extra Resources

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even though we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for di language wey dem write am first na di main source wey you go trust. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->