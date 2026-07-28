# 🔍 ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಅನ್ವೇಷಣೆ - ಮೂಲ ಏಜೆಂಟ್ (.NET)

## 📋 ಅಧ್ಯಯನ ಉದ್ದೇಶಗಳು

ಈ ಉದಾಹರಣೆ .NET ನಲ್ಲಿ ಮೂಲ ಏಜೆಂಟ್ ಜಾರಿಗೆ ಮೂಲಕ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ನ ಮೂಲ ತತ್ವಗಳನ್ನು ಅನ್ವೇಷಿಸುತ್ತದೆ. ನೀವು ಎಜಂಟಿಕ್ ಮಾದರಿಗಳನ್ನು ಮತ್ತು C# ಮತ್ತು .NET ಪರಿಸರದ ಬಳಕೆಯಿಂದ ಬುದ್ಧಿವಂತ ಏಜೆಂಟ್‌ಗಳು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತವೆ ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುತ್ತೀರಿ.

### ನಿಮ್ಮದು ಕಂಡುಹಿಡಿಯುವುದು

- 🏗️ **ಏಜೆಂಟ್ ಆರ್ಕಿಟೆಕ್ಚರ್**: .NET ನಲ್ಲಿ AI ಏಜೆಂಟ್‌ಗಳ ಮೂಲ ರಚನೆಯನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು
- 🛠️ **ಉಪಕರಣ ಇನ್‌ಟಿಗ್ರೇಷನ್**: ಏಜೆಂಟ್‌ಗಳು ತಮ್ಮ ಶಕ್ತಿಗಳನ್ನು ವಿಸ್ತರಿಸಲು ಹೊರಗಿನ ಕಾರ್ಯಗಳನ್ನು ಹೇಗೆ ಬಳಸುತ್ತವೆ  
- 💬 **ಸಂಭಾಷಣೆ ಹರಿವು**: ಬಹು-ತಿರುಗು ಸಂಭಾಷಣೆ ಮತ್ತು ನೆಲೆತನ ನಿರ್ವಹಣೆಯೊಂದಿಗೆ ಸಂಭಾಷಣೆಯನ್ನು ನಿರ್ವಹಿಸುವುದು
- 🔧 ** ಸೆಟ್ಟಿಂಗ್ ಮಾದರಿಗಳು**: .NET ನಲ್ಲಿ ಏಜೆಂಟ್ ಸೆಟಪ್ ಮತ್ತು ನಿರ್ವಹಣೆಯ ಉತ್ತಮ ಪದ್ಧತಿಗಳು

## 🎯 ಮುಖ್ಯ ತತ್ವಗಳು

### ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ತತ್ವಗಳು

- ** ಸ್ವಾಯತ್ತತೆ**: .NET AI ಅವತಾರಗಳನ್ನು ಬಳಸಿ ಏಜೆಂಟ್‌ಗಳು ಹೇಗೆ ಸ್ವತಂತ್ರ ನಿರ್ಣಯಗಳನ್ನು ಕೈಗೊಂಡಿರುತ್ತವೆ
- **ಪ್ರತಿಕ್ರಿಯಾಶೀಲತೆ**: ಪರಿಸರ ಬದಲಾವಣೆ ಮತ್ತು ಬಳಕೆದಾರ ಇನ್‌ಪುಟ್‌ಗಳಿಗೆ ಪ್ರತಿಕ್ರಿಯಿಸುವುದು
- **ಪ್ರವರ್ತಕತೆ**: ಗುರಿಗಳು ಮತ್ತು ಮೇಲೆ ಆಧಾರಿತವಾಗಿ ಉದ್ಭಾವನೆ ತೆಗೆದುಕೊಳ್ಳುವುದು
- **ಸಾಮಾಜಿಕ ಸಾಮರ್ಥ್ಯ**: ಸಂಭಾಷಣಾ ತಂತುಗಳ ಮೂಲಕ ಸಹಜ ಭಾಷೆಯಲ್ಲಿ ಸಂವಹನ

### ತಾಂತ್ರಿಕ ಘಟಕಗಳು

- **AIAgent**: ಮೂಲ ಏಜೆಂಟ್ ಸಂಘಟನೆ ಮತ್ತು ಸಂಭಾಷಣೆ ನಿರ್ವಹಣೆ (.NET)
- **ಉಪಕರಣ ಕಾರ್ಯಗಳು**: C# ವಿಧಾನಗಳು ಮತ್ತು ಗುಣಲಕ್ಷಣಗಳೊಂದಿಗೆ ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯ ವಿಸ್ತರಣೆ
- **ಅಜೂರ್ ಓಪನ್AI ಇಂಟಿಗ್ರೇಷನ್**: ಅಜೂರ್ ಓಪನ್AI ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಮೂಲಕ ಭಾಷಾ ಮಾದರಿಗಳನ್ನು ಉಪಯೋಗಿಸುವುದು
- **ಭದ್ರತಾ ಸೆಟ್ಟಿಂಗ್**: ಪರಿಸರ ಆಧಾರಿತ ಅಂತಿಮ ಬಿಡ್ ನಿರ್ವಹಣೆ

## 🔧 ತಾಂತ್ರಿಕ ಸ್ಟ್ಯಾಕ್

### ಮೂಲ ತಂತ್ರಜ್ಞಾನಗಳು

- ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ (.NET)
- ಅಜೂರ್ ಓಪನ್AI (ಪ್ರತಿಕ್ರಿಯೆಗಳ API) ಇಂಟಿಗ್ರೇಷನ್
- Azure.AI.OpenAI ಕ್ಲೈಂಟ್ ಮಾದರಿಗಳು
- DotNetEnv ಬಳಸಿ ಪರಿಸರ ಆಧಾರಿತ ಸೆಟ್ಟಿಂಗ್

### ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯಗಳು

- ಸಹಜ ಭಾಷೆ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಮತ್ತು ರಚನೆ
- ಕಾರ್ಯ ಕರೆ ಮತ್ತು C# ಗುಣಲಕ್ಷಣಗಳೊಂದಿಗೆ ಉಪಕರಣ ಬಳಕೆ
- ಸಂಭಾಷಣೆ sessões ಗಳೊಂದಿಗೆ ಸಾಂದರ್ಭಿಕ-ಜಾಗೃತಿ ಪ್ರತಿಕ್ರಿಯೆಗಳು
- ಅವಲಂಬನೆ ಸುರಿದ comunque a um mostrado padrão extensível arquitetura

## 📚 ಫ್ರೇಮ್‌ವರ್ಕ್ ಹೋಲಿಕೆ

ಈ ಉದಾಹರಣೆ ಇವುಳಗಳಲ್ಲಿ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ವಿಧಾನವನ್ನು ತೋರಿಸುತ್ತದೆ:

| ವೈಶಿಷ್ಟ್ಯ | ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ | ಇತರ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳು |
|---------|-------------------------|------------------|
| **ಇಂಟಿಗ್ರೇಷನ್** | ಹುಟ್ಟು Microsoft ಪರಿಸರ | ಬದಲಾಗುವ ಹೊಂದಾಣಿಕೆ |
| **ಸರಳತೆ** | ಸ್ವಚ್ಛ, ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಸುಲಭ API | ಅಕಾಲಿಕವಾಗಿ ಸಂಕೀರ್ಣ ಸೆಟಪ್ |
| **ವಿಸ್ತರಣೀಯತೆ** | ಸುಲಭ ಉಪಕರಣ ಇಂಟಿಗ್ರೇಷನ್ | ಫ್ರೇಮ್‌ವರ್ಕ್ ಆಧಾರಿತ |
| **ಎಂಟರ್‌ಪ್ರೈಸ್ ರೆಡಿ** | ಉತ್ಪಾದನೆಗೆ ನಿರ್ಮಿಸಲಾಗಿದೆ | ಫ್ರೇಮ್‌ವರ್ಕ್ ಪ್ರಕಾರ ವ್ಯತ್ಯಾಸ ಇರುತ್ತದೆ |

## 🚀 ಪ್ರಾರಂಭಿಸುವಿಕೆ

### ಪೂರ್ವಶರತ್ತುಗಳ

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ಅಥವಾ ಹೆಚ್ಚಿನ ಸಂಸ್ಕರಣೆ
- [ಅಜೂರ್ ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್](https://azure.microsoft.com/free/)  ಅಜೂರ್ ಓಪನ್AI ಸಂಪನ್ಮೂಲ ಮತ್ತು ಮಾದರಿ ನಿಯೋಜನೆಯೊಂದಿಗೆ
- [ಅಜೂರ್ CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` ಬಳಸಿ ಸೇರುವುದು

### ಅಗತ್ಯ ಪರಿಸರ ಚರಗಳು

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# ನಂತರ ಸೈನ್ ಇನ್ ಮಾಡಿ ಎದಕ್ಕೆ AzureCliCredential ಟೋಕನ್ ಪಡೆಯಬಹುದು
az login
```

```powershell
# ಪವರ್‌ಶೆಲ್
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# ನಂತರ ಸೈನ್ ಇನ್ ಮಾಡಿ যাতে AzureCliCredential ಟೋಕನ್ ಪಡೆಯಬಹುದು
az login
```

### ಉದಾಹರಣಾ ಕೋಡ್

ಕೋಡ್ ಉದಾಹರಣೆಯನ್ನು ನಿರ್ವಹಿಸಲು,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

ಅಥವಾ ಡಾಟ್‌ನೆಟ್ CLI ಬಳಸಿ:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

ಪೂರ್ಣ ಕೋಡ್‌ಗೆ [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) ಅನ್ನು ನೋಡಿ.

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

## 🎓 ಮುಖ್ಯ ಪಾಠಗಳು

1. **ಏಜೆಂಟ್ ಆರ್ಕಿಟೆಕ್ಚರ್**: ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ .NET ನಲ್ಲಿ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಸ್ವಚ್ಛ, ಟೈಪ್-ಸುರಕ್ಷಿತ ವಿಧಾನ ನೀಡುತ್ತದೆ
2. **ಉಪಕರಣ ಇಂಟಿಗ್ರೇಷನ್**: `[Description]` ಗುಣಲಕ್ಷಣಗಳಿಂದ ಅಲಂಕರಿಸಿದ ಕಾರ್ಯಗಳು ಏಜೆಂಟ್‌ಗೆ ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳಾಗುತ್ತವೆ
3. **ಸಂಭಾಷಣೆ ಸಾಂದರ್ಭಿಕತೆ**: ಸೆಷನ್ ನಿರ್ವಹಣೆ ಸಂಪೂರ್ಣ ಸಾಂದರ್ಭಿಕ ಜಾಗೃತಿ ಹೊಂದಿರುವ ಬಹು-ತಿರುಗು ಸಂಭಾಷಣೆಯನ್ನು ಸಾದ್ಯಮಾಡುತ್ತದೆ
4. **ಸೆಟ್ಟಿಂಗ್ ನಿರ್ವಹಣೆ**: ಪರಿಸರ ಚರಗಳು ಮತ್ತು ಭದ್ರಪಡಿಸಲಾದ ಕ್ರೆಡೆಂಶಿಯಲ್ ನಿರ್ವಹಣೆ .NET ಉತ್ತಮ ಪದ್ಧತಿಗಳನ್ನು ಅನುಸರಿಸುತ್ತದೆ
5. **ಅಜೂರ್ ಓಪನ್AI ಪ್ರತಿಕ್ರಿಯೆಗಳ API**: ಏಜೆಂಟ್ Azure.AI.OpenAI SDK ಮೂಲಕ ಅಜೂರ್ ಓಪನ್AI ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಅನ್ನು ಬಳಸುತ್ತದೆ

## 🔗 ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- [Microsoft Agent Framework ದಸ್ತಾವೇಜು](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry ನಲ್ಲಿ ಅಜೂರ್ ಓಪನ್AI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET ಒಂಟಿ ಫೈಲ್ ಅಪ್ಸ್](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->