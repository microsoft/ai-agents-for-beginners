# 🔍 ਮਾਈਕਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੀ ਖੋਜ - ਬੇਸਿਕ ਏਜੰਟ (.NET)

## 📋 ਸਿੱਖਣ ਦੇ ਲਕੜੇ

ਇਹ ਉਦਾਹਰਣ .NET ਵਿੱਚ ਇੱਕ ਬੇਸਿਕ ਏਜੰਟ ਦੀ ਅਮਲਦਾਰੀ ਰਾਹੀਂ ਮਾਈਕਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦੇ ਮੂਲ ਤੱਤਾਂ ਨੂੰ ਖੰਗਾਲਦੀ ਹੈ। ਤੁਸੀਂ ਆਧਾਰਿਕ ਏਜੰਟਿਕ ਪੈਟਰਨ ਸਿੱਖੋਗੇ ਅਤੇ ਸਮਝੋਗੇ ਕਿ ਕਿਵੇਂ ਬੁੱਧਿਮਾਨ ਏਜੰਟ C# ਅਤੇ .NET ਪਰਿਸਰੀ ਦਾ ਉਪਯੋਗ ਕਰਦਿਆਂ ਹੇਠਾਂ ਕੰਮ ਕਰਦੇ ਹਨ।

### ਤੁਹਾਡੇ ਲਈ ਕੀ ਖੋਜਣ ਲਈ ਹੈ

- 🏗️ **ਏਜੰਟ ਆਰਕੀਟੈਕਚਰ**: .NET ਵਿੱਚ AI ਏਜੰਟਾਂ ਦੀ ਬੁਨਿਆਦੀ ਬਣਤਰ ਨੂੰ ਸਮਝਣਾ
- 🛠️ **ਟੂਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: ਏਜੰਟ ਕਿਵੇਂ ਬਾਹਰੀ ਫੰਕਸ਼ਨਾਂ ਨਾਲ ਆਪਣੀਆਂ ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਵਧਾਉਂਦੇ ਹਨ  
- 💬 **ਗੱਲਬਾਤ ਦਾ ਪ੍ਰਵਾਹ**: ਮਲਟੀ-ਟਰਨ ਗੱਲਬਾਤਾਂ ਅਤੇ ਧਾਗਾ ਪ੍ਰਬੰਧਨ ਨਾਲ ਸੰਦਰਭ ਪ੍ਰਬੰਧਨ
- 🔧 **ਸੰਰਚਨਾ ਪੈਟਰਨ**: .NET ਵਿੱਚ ਏਜੰਟ ਸੈੱਟਅੱਪ ਅਤੇ ਪ੍ਰਬੰਧਨ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਅਭਿਆਸ

## 🎯 ਮੁੱਖ ਵਿਚਾਰਾਂ ਦੀ ਵਰਣਨਾ

### ਏਜੰਟਿਕ ਫਰੇਮਵਰਕ ਨੀਤੀਆਂ

- **ਸਵੈਤੰਤਰਤਾ**: .NET AI ਸਾਰਾਂਸ਼ ਉਪਯੋਗ ਕਰਕੇ ਏਜੰਟਾਂ ਵਲੋਂ ਸੁਤੰਤਰ ਫੈਸਲੇ ਲੈਣਾ
- **ਪ੍ਰਤੀਕ੍ਰਿਆਸ਼ੀਲਤਾ**: ਵਾਤਾਵਰਣਿਕ ਬਦਲਾਵਾਂ ਅਤੇ ਉਪਭੋਗਤਾ ਦੀਆਂ ਪ੍ਰਵੇਸ਼ਾਂ ਦਾ ਜਵਾਬ ਦੇਣਾ
- **ਪੂਰਵਕਰਤਾ**: ਲਕੜਾਂ ਅਤੇ ਸੰਦਰਭ ਦੇ ਆਧਾਰ 'ਤੇ ਪਹਲ ਕਰਨਾ
- **ਸਮਾਜਿਕ ਯੋਗਤਾ**: ਗੱਲਬਾਤ ਧਾਗਿਆਂ ਰਾਹੀਂ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਨਾਲ ਸੰਵਾਦ

### ਤਕਨੀਕੀ ਭਾਗ

- **AIAgent**: ਮੁੱਖ ਏਜੰਟ ਆਰਕੀਸਟ੍ਰੇਸ਼ਨ ਅਤੇ ਗੱਲਬਾਤ ਪ੍ਰਬੰਧਨ (.NET)
- **ਟੂਲ ਫੰਕਸ਼ਨ**: C# ਮੈਥਡਾਂ ਅਤੇ ਲੱਛਣਾਂ ਨਾਲ ਏਜੰਟ ਦੀ ਸਮਰੱਥਾ ਵਧਾਉਣਾ
- **Azure OpenAI ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: Azure OpenAI Responses API ਰਾਹੀਂ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਦਾ ਲਾਭ ਲੈਣਾ
- **ਸੁਰੱਖਿਅਤ ਸੰਰਚਨਾ**: ਵਾਤਾਵਰਣ ਅਧਾਰਿਤ ਐਂਡਪוਇੰਟ ਪ੍ਰਬੰਧਨ

## 🔧 ਤਕਨੀਕੀ ਸਟੈੱਕ

### ਮੁੱਖ ਤਕਨੀਕਾਂ

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) ਇੰਟੀਗ੍ਰੇਸ਼ਨ
- Azure.AI.OpenAI ਕਲਾਇੰਟ ਪੈਟਰਨ
- DotNetEnv ਨਾਲ ਵਾਤਾਵਰਣ-ਅਧਾਰਿਤ ਸੰਰਚਨਾ

### ਏਜੰਟ ਸਮਰੱਥਾਵਾਂ

- ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਦੀ ਸਮਝ ਅਤੇ ਉਤਪੱਤੀ
- C# ਲੱਛਣਾਂ ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਅਤੇ ਟੂਲ ਦੀ ਵਰਤੋਂ
- ਗੱਲਬਾਤ ਸੈਸ਼ਨਾਂ ਨਾਲ ਸੰਦਰਭ-ਜਾਗਰੂਕ ਜਵਾਬ
- ਡੀਪੈਂਡੈਂਸੀ ਇੰਜੈਕਸ਼ਨ ਪੈਟਰਨ ਨਾਲ ਵਿਸਤਾਰਯੋਗ ਆਰਕੀਟੈਕਚਰ

## 📚 ਫਰੇਮਵਰਕ ਤੁਲਨਾ

ਇਹ ਉਦਾਹਰਣ Microsoft Agent Framework ਦੀ ਪਹੁੰਚ ਦੂਜੇ ਏਜੰਟਿਕ ਫਰੇਮਵਰਕਾਂ ਨਾਲ ਤੁਲਨਾ ਕਰਦੀ ਹੈ:

| ਵਿਸ਼ੇਸ਼ਤਾ | Microsoft Agent Framework | ਹੋਰ ਫਰੇਮਵਰਕ |
|---------|-------------------------|------------------|
| **ਇੰਟੀਗ੍ਰੇਸ਼ਨ** | ਮੂਲ Microsoft ਪਰਿਸਰੀ | ਵੱਖ-ਵੱਖ ਸੰਗਤਤਾ |
| **ਸਧਾਰਣਤਾ** | ਸਾਫ਼, ਸੁਗਮ API | ਅਕਸਰ ਜਟਿਲ ਸੈੱਟਅੱਪ |
| **ਵਿਸਤਾਰਯੋਗਤਾ** | ਆਸਾਨ ਟੂਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ | ਫਰੇਮਵਰਕ-ਨਿਰਭਰ |
| **ਐਂਟਰਪ੍ਰਾਈਜ਼ ਰੇਡੀ** | ਉਤਪਾਦਨ ਲਈ ਬਣਾਇਆ ਗਿਆ | ਫਰੇਮਵਰਕ ਮੁਤਾਬਕ ਫ਼ਰਕ |

## 🚀 ਸ਼ੁਰੂਆਤ ਕਰਨ ਲਈ

### ਲੋੜੀਂਦੇ ਸਾਧਨ

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ਜਾਂ ਉੱਚਾ
- [Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ](https://azure.microsoft.com/free/) ਜਿਸ ਵਿੱਚ Azure OpenAI ਸਰੋਤ ਅਤੇ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਹੋਵੇ
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` ਨਾਲ ਲੌਗਇਨ ਕਰੋ

### ਲੋੜੀਂਦੇ ਵਾਤਾਵਰਣ ਚਲਣ ਯੋਗ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# ਫਿਰ ਸਾਇਨ ਇਨ ਕਰੋ ਤਾਂ ਜੋ AzureCliCredential ਟੋਕਨ ਲੈ ਸਕੇ
az login
```

```powershell
# ਪਾਵਰਸ਼ੈੱਲ
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# ਫਿਰ ਸਾਈਨ ਇਨ ਕਰੋ ਤਾਂ ਜੋ AzureCliCredential ਟੋਕਨ ਪ੍ਰਾਪਤ ਕਰ ਸਕੇ
az login
```

### ਨਮੂਨਾ ਕੋਡ

ਕੋਡ ਉਦਾਹਰਣ ਚਲਾਉਣ ਲਈ,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

ਜਾਂ dotnet CLI ਦੀ ਵਰਤੋਂ ਕਰ ਕੇ:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

ਪੂਰਾ ਕੋਡ ਵੇਖਣ ਲਈ [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) ਨੂੰ ਦੇਖੋ।

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

## 🎓 ਮੁੱਖ ਨਤੀਜੇ

1. **ਏਜੰਟ ਆਰਕੀਟੈਕਚਰ**: Microsoft Agent Framework .NET ਵਿੱਚ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਸਾਫ਼, ਟਾਈਪ-ਸੇਫ਼ ਪਹੁੰਚ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ
2. **ਟੂਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: `[Description]` ਲੱਛਣਾਂ ਨਾਲ ਸਜਾਏ ਗਏ ਫੰਕਸ਼ਨ ਏਜੰਟ ਲਈ ਉਪਲਬਧ ਟੂਲ ਬਣ ਜਾਂਦੇ ਹਨ
3. **ਗੱਲਬਾਤ ਸੰਦਰਭ**: ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ ਮੁਲਟੀ-ਟਰਨ ਗੱਲਬਾਤਾਂ ਨੂੰ ਪੂਰੇ ਸੰਦਰਭ ਸੂਚਨਾ ਨਾਲ ਸੰਭਾਲਦਾ ਹੈ
4. **ਸੰਰਚਨਾ ਪ੍ਰਬੰਧਨ**: ਵਾਤਾਵਰਣ ਚਲਣ ਯੋਗ ਅਤੇ ਸੁਰੱਖਿਅਤ ਪ੍ਰਮਾਣਿਕਤਾ ਸੰਭਾਲ .NET ਦੇ ਸਭ ਤੋਂ ਵਧੀਆ ਅਭਿਆਸਾਂ ਨੂੰ ਫੋਲੋ ਕਰਦੇ ਹਨ
5. **Azure OpenAI Responses API**: ਏਜੰਟ Azure.AI.OpenAI SDK ਰਾਹੀਂ Azure OpenAI Responses API ਦਾ ਉਪਯੋਗ ਕਰਦਾ ਹੈ

## 🔗 ਵਾਧੂ ਸਾਧਨ

- [Microsoft Agent Framework ਦਸਤਾਵੇਜ਼](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry ਵਿੱਚ Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET ਸਿੰਗਲ ਫਾਇਲ ਐਪਸ](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->