<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T12:06:40+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "pa"
}
-->
# 🔍 ਮਾਈਕਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀ ਖੋਜ - ਬੇਸਿਕ ਏਜੰਟ (.NET)

## 📋 ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਹ ਉਦਾਹਰਨ .NET ਵਿੱਚ ਇੱਕ ਬੇਸਿਕ ਏਜੰਟ ਦੇ ਨImplementation ਰਾਹੀਂ ਮਾਈਕਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੇ ਮੁੱਢਲੇ ਸਿਧਾਂਤਾਂ ਦੀ ਖੋਜ ਕਰਦੀ ਹੈ। ਤੁਸੀਂ ਮੁੱਖ ਏਜੰਟਿਕ ਪੈਟਰਨ ਸਿੱਖੋਗੇ ਅਤੇ ਸਮਝੋਗੇ ਕਿ C# ਅਤੇ .NET ਈਕੋਸਿਸਟਮ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਮਰਥ ਏਜੰਟ ਕਿਵੇਂ ਕੰਮ ਕਰਦੇ ਹਨ।

### ਤੁਸੀਂ ਕੀ ਖੋਜੋਗੇ

- 🏗️ **ਏਜੰਟ ਆਰਕੀਟੈਕਚਰ**: .NET ਵਿੱਚ AI ਏਜੰਟਾਂ ਦੀ ਬੁਨਿਆਦੀ ਬਣਤਰ ਨੂੰ ਸਮਝਣਾ
- 🛠️ **ਟੂਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: ਏਜੰਟ ਕਿਵੇਂ ਬਾਹਰੀ ਫੰਕਸ਼ਨਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ ਸਮਰਥਾ ਵਧਾਉਣ ਲਈ  
- 💬 **ਕConversation ਫਲੋ**: ਮਲਟੀ-ਟਰਨ ਗੱਲਬਾਤਾਂ ਅਤੇ ਸੰਦਰਭ ਨੂੰ ਥ੍ਰੈਡ ਮੈਨੇਜਮੈਂਟ ਨਾਲ ਸੰਭਾਲਣਾ
- 🔧 **ਕੰਫਿਗਰੇਸ਼ਨ ਪੈਟਰਨ**: .NET ਵਿੱਚ ਏਜੰਟ ਸੈਟਅਪ ਅਤੇ ਮੈਨੇਜਮੈਂਟ ਲਈ ਸ੍ਰੇਸ਼ਠ ਪਦਤੀ

## 🎯 ਮੁੱਖ ਸਿਧਾਂਤ

### ਏਜੰਟਿਕ ਫਰੇਮਵਰਕ ਦੇ ਸਿਧਾਂਤ

- **ਆਟੋਨੋਮੀ**: .NET AI ਅਬਸਟਰੈਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਏਜੰਟ ਕਿਵੇਂ ਸੁਤੰਤਰ ਫੈਸਲੇ ਲੈਂਦੇ ਹਨ
- **ਰੀਐਕਟਿਵਿਟੀ**: ਵਾਤਾਵਰਣ ਵਿੱਚ ਬਦਲਾਅ ਅਤੇ ਯੂਜ਼ਰ ਇਨਪੁਟਸ ਦਾ ਜਵਾਬ ਦੇਣਾ
- **ਪ੍ਰੋਐਕਟਿਵਿਟੀ**: ਲਕਸ਼ਾਂ ਅਤੇ ਸੰਦਰਭ ਦੇ ਆਧਾਰ 'ਤੇ ਪਹਲ ਕਰਨਾ
- **ਸੋਸ਼ਲ ਐਬਿਲਿਟੀ**: ਗੱਲਬਾਤ ਦੇ ਥ੍ਰੈਡਾਂ ਨਾਲ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਰਾਹੀਂ ਸੰਚਾਰ ਕਰਨਾ

### ਤਕਨੀਕੀ ਹਿੱਸੇ

- **AIAgent**: ਕੋਰ ਏਜੰਟ ਓਰਕੇਸਟਰੈਸ਼ਨ ਅਤੇ ਗੱਲਬਾਤ ਮੈਨੇਜਮੈਂਟ (.NET)
- **ਟੂਲ ਫੰਕਸ਼ਨ**: C# ਮੈਥਡਸ ਅਤੇ ਐਟ੍ਰਿਬਿਊਟਸ ਨਾਲ ਏਜੰਟ ਸਮਰਥਾ ਵਧਾਉਣਾ
- **OpenAI ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: .NET APIs ਰਾਹੀਂ ਭਾਸ਼ਾ ਮਾਡਲ ਦੀ ਵਰਤੋਂ
- **ਸੁਰੱਖਿਅਤ ਕੰਫਿਗਰੇਸ਼ਨ**: API ਕੁੰਜੀਆਂ ਦੇ ਮੈਨੇਜਮੈਂਟ ਲਈ ਵਾਤਾਵਰਣ-ਅਧਾਰਿਤ ਪੈਟਰਨ

## 🔧 ਤਕਨੀਕੀ ਸਟੈਕ

### ਕੋਰ ਤਕਨੀਕਾਂ

- ਮਾਈਕਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ (.NET)
- GitHub ਮਾਡਲ API ਇੰਟੀਗ੍ਰੇਸ਼ਨ
- OpenAI-ਅਨੁਕੂਲ ਕਲਾਇੰਟ ਪੈਟਰਨ
- DotNetEnv ਨਾਲ ਵਾਤਾਵਰਣ-ਅਧਾਰਿਤ ਕੰਫਿਗਰੇਸ਼ਨ

### ਏਜੰਟ ਸਮਰਥਾ

- ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਦੀ ਸਮਝ ਅਤੇ ਜਨਰੇਸ਼ਨ
- C# ਐਟ੍ਰਿਬਿਊਟਸ ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਅਤੇ ਟੂਲ ਦੀ ਵਰਤੋਂ
- ਗੱਲਬਾਤ ਦੇ ਥ੍ਰੈਡਾਂ ਨਾਲ ਸੰਦਰਭ-ਜਾਗਰੂਕ ਜਵਾਬ
- ਡਿਪੈਂਡੈਂਸੀ ਇੰਜੈਕਸ਼ਨ ਪੈਟਰਨ ਨਾਲ ਵਧਾਉਣਯੋਗ ਆਰਕੀਟੈਕਚਰ

## 📚 ਫਰੇਮਵਰਕ ਦੀ ਤੁਲਨਾ

ਇਹ ਉਦਾਹਰਨ ਮਾਈਕਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੇ ਦ੍ਰਿਸ਼ਟੀਕੋਣ ਨੂੰ ਹੋਰ ਏਜੰਟਿਕ ਫਰੇਮਵਰਕਸ ਨਾਲ ਤੁਲਨਾ ਕਰਦੀ ਹੈ:

| ਫੀਚਰ | ਮਾਈਕਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ | ਹੋਰ ਫਰੇਮਵਰਕਸ |
|---------|-------------------------|------------------|
| **ਇੰਟੀਗ੍ਰੇਸ਼ਨ** | ਮਾਈਕਰੋਸਾਫਟ ਈਕੋਸਿਸਟਮ ਦੇ ਨਾਲ ਜੁੜਿਆ | ਵੱਖ-ਵੱਖ ਅਨੁਕੂਲਤਾ |
| **ਸਾਦਗੀ** | ਸਾਫ਼, ਸਹਜ API | ਅਕਸਰ ਜਟਿਲ ਸੈਟਅਪ |
| **ਵਧਾਉਣਯੋਗਤਾ** | ਟੂਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਆਸਾਨ | ਫਰੇਮਵਰਕ-ਨਿਰਭਰ |
| **ਇੰਟਰਪ੍ਰਾਈਜ਼ ਤਿਆਰ** | ਉਤਪਾਦਨ ਲਈ ਬਣਾਇਆ ਗਿਆ | ਫਰੇਮਵਰਕ 'ਤੇ ਨਿਰਭਰ |

## 🚀 ਸ਼ੁਰੂਆਤ ਕਰਨਾ

### ਪੂਰਵ ਸ਼ਰਤਾਂ

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ਜਾਂ ਇਸ ਤੋਂ ਉੱਚਾ
- [GitHub ਮਾਡਲ API ਐਕਸੈਸ ਟੋਕਨ](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)

### ਲੋੜੀਂਦੇ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ

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

### ਸੈਂਪਲ ਕੋਡ

ਕੋਡ ਉਦਾਹਰਨ ਚਲਾਉਣ ਲਈ,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

ਜਾਂ dotnet CLI ਦੀ ਵਰਤੋਂ ਕਰਕੇ:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

ਪੂਰੇ ਕੋਡ ਲਈ [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) ਵੇਖੋ।

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

## 🎓 ਮੁੱਖ ਸਿੱਖਣ

1. **ਏਜੰਟ ਆਰਕੀਟੈਕਚਰ**: ਮਾਈਕਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ .NET ਵਿੱਚ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਸਾਫ਼, ਟਾਈਪ-ਸੇਫ਼ ਪਦਤੀ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ
2. **ਟੂਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: `[Description]` ਐਟ੍ਰਿਬਿਊਟ ਨਾਲ ਸਜਾਏ ਫੰਕਸ਼ਨ ਏਜੰਟ ਲਈ ਉਪਲਬਧ ਟੂਲ ਬਣ ਜਾਂਦੇ ਹਨ
3. **ਗੱਲਬਾਤ ਸੰਦਰਭ**: ਥ੍ਰੈਡ ਮੈਨੇਜਮੈਂਟ ਮਲਟੀ-ਟਰਨ ਗੱਲਬਾਤਾਂ ਨੂੰ ਪੂਰੇ ਸੰਦਰਭ ਜਾਗਰੂਕਤਾ ਨਾਲ ਸੰਭਾਲਦਾ ਹੈ
4. **ਕੰਫਿਗਰੇਸ਼ਨ ਮੈਨੇਜਮੈਂਟ**: ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਅਤੇ ਸੁਰੱਖਿਅਤ ਪ੍ਰਮਾਣ ਪੱਤਰ ਸੰਭਾਲ .NET ਦੀਆਂ ਸ੍ਰੇਸ਼ਠ ਪਦਤੀਆਂ ਦੀ ਪਾਲਣਾ ਕਰਦੇ ਹਨ
5. **OpenAI ਅਨੁਕੂਲਤਾ**: GitHub ਮਾਡਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ OpenAI-ਅਨੁਕੂਲ APIs ਰਾਹੀਂ ਬੇਰੁਕਾਵਟ ਕੰਮ ਕਰਦਾ ਹੈ

## 🔗 ਵਾਧੂ ਸਰੋਤ

- [ਮਾਈਕਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦਸਤਾਵੇਜ਼](https://learn.microsoft.com/agent-framework)
- [GitHub ਮਾਡਲ ਮਾਰਕੀਟਪਲੇਸ](https://github.com/marketplace?type=models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET ਸਿੰਗਲ ਫਾਈਲ ਐਪਸ](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੱਜੇਪਣ ਹੋ ਸਕਦੇ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->