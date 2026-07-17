# 🔍 ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಅನ್ವೇಷಣೆ - ಮೂಲ ಏಜೆಂಟ್ (.NET)

## 📋 ಕಲಿಕೆ ಗುರಿಗಳು

ಈ ಉದಾಹರಣೆ .NET ನಲ್ಲಿ ಸರಳ ಏಜೆಂಟ್ ಅನುಷ್ಠಾನದ ಮೂಲಕ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ನ ಮೂಲತತ್ತ್ವಗಳನ್ನು ಅನ್ವೇಷಿಸುತ್ತದೆ. ನೀವು ಕೋರ್ ಏಜೆಂಟಿಕ್ ಮಾದರಿಗಳನ್ನು ಕಲಿಯುತ್ತೀರಿ ಮತ್ತು C# ಮತ್ತು .NET ಪರಿಸರವನ್ನು ಬಳಸಿಕೊಂಡು ಬುದ್ಧಿವಂತ ಏಜೆಂಟುಗಳು ಹಿಂಬದಿ ಹೇಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತವೆ ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುತ್ತೀರಿ.

### ನೀವು ಕಂಡುಹಿಡಿಯುವವು ಏನು

- 🏗️ **ಏಜೆಂಟ್ ವಾಸ್ತುಶಿಲ್ಪ**: .NET ನಲ್ಲಿ ಏಐ ಏಜೆಂಟುಗಳ ಮೂಲ ರಚನೆಯನ್ನು ಅರಿತುಕೊಳ್ಳುವುದು
- 🛠️ **ಟೂಲ್ ಏಕೀಕರಣ**: ಏಜೆಂಟುಗಳು ಸಾಮರ್ಥ್ಯಗಳನ್ನು ವಿಸ್ತರಿಸಲು ಹೊರಗಿನ ಕಾರ್ಯಗಳನ್ನು ಹೇಗೆ ಉಪಯೋಗಿಸುತ್ತವೆ  
- 💬 **ಸಂವದನ ಹರಿವು**: ಬಹು-ತಿರುವು ಸಂಭಾಷಣೆಗಳನ್ನು ಮತ್ತು ಸಾಂದರ್ಭಿಕ ವಿಷಯಗಳನ್ನು ಥ್ರೆಡ್ ನಿರ್ವಹಣೆಯಿಂದ ನಿಯಂತ್ರಿಸುವುದು
- 🔧 **ವಿನ್ಯಾಸ ಮಾದರಿಗಳು**: .NET ನಲ್ಲಿ ಏಜೆಂಟ್ ಸೆಟ್ ಅಪ್ ಮತ್ತು ನಿರ್ವಹಣೆಗೆ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು

## 🎯 ಪ್ರಮುಖ ತತ್ತ್ವಗಳು

### ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್ವರ್ಕ್ ತತ್ತ್ವಗಳು

- **ಸ್ವಾಯತ್ಯತೆ**: .NET AI ಆಬ್ಸ್ಟ್ರಾಕ್ಶನ್‌ಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಏಜೆಂಟುಗಳು ಸ್ವತಂತ್ರ ನಿರ್ಧಾರಗಳನ್ನು ಹೇಗೆ ತೆಗೆದುಕೊಳ್ಳುತ್ತವೆ
- ** ಪ್ರತಿಕ್ರಿಯಾಶೀಲತೆ**: ಪರಿಸರ ಬದಲಾವಣೆಗಳಿಗೆ ಮತ್ತು ಬಳಕೆದಾರ ಇನ್ಪುಟ್‌ಗಳಿಗೆ ಪ್ರತಿಕ್ರಿಯಿಸುವುದು
- **ಪ್ರೊಆಕ್ಟಿವಿಟಿ**: ಗುರಿಗಳು ಮತ್ತು ಸಾಂದರ್ಭಿಕತೆಗೆ ಆಧಾರಿತವಾಗಿ ಕೈಗೊಂಡು ಉದ್ದೇಶ
- **ಸಾಮಾಜಿಕ ಸಾಮರ್ಥ್ಯ**: ಸಂಭಾಷಣಾ ಥ್ರೆಡ್‌ಗಳ ಮೂಲಕ ನೈಸರ್ಗಿಕ ಭಾಷೆಯಲ್ಲಿ ಸಂವಹನ

### ತಾಂತ್ರಿಕ ഘಟಕಗಳು

- **AIAgent**: ಕೋರ್ ಏಜೆಂಟ್ ಆರ್ಕೆಸ್ಟ್ರೇಷನ್ ಮತ್ತು ಸಂಭಾಷಣೆ ನಿರ್ವಹಣೆ (.NET)
- **ಟೂಲ್ ಕಾರ್ಯಗಳು**: C# ವಿಧಾನಗಳು ಮತ್ತು ಲಕ್ಷಣಗಳೊಂದಿಗೆ ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ವಿಸ್ತರಿಸುವುದು
- **ಆಜೂರ್ ಓಪನ್‌ಏಐ ಏಕೀಕರಣ**: ಆಜೂರ್ ಓಪನ್‌ಏಐ ರೆસ્પಾನ್ಸಸ್ API ಮೂಲಕ ಭಾಷಾ ಮಾದರಿಗಳನ್ನು ಉಪಯೋಗಿಸುವುದು
- **ಸುರಕ್ಷಿತ ವಿನ್ಯಾಸ**: ಪರಿಸರ ಆಧಾರಿತ ಎಂಡ್‌ಪಾಯಿಂಟ್ ನಿರ್ವಹಣೆ

## 🔧 ತಾಂತ್ರಿಕ ಸಾಫ್ಟ್‌ವೇರ್

### ಮುಖ್ಯ ತಂತ್ರಜ್ಞಾನಗಳು

- ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ (.NET)
- ಆಜೂರ್ ಓಪನ್‌ಏಐ (ರೆಸ್ಪಾನ್ಸ್ API) ಏಕೀಕರಣ
- Azure.AI.OpenAI ಕ್ಲೈಂಟ್ ಮಾದರಿಗಳು
- DotNetEnv ಮೂಲಕ ಪರಿಸರ ಆಧಾರಿತ ಸಂರಚನೆ

### ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯಗಳು

- ನೈಸರ್ಗಿಕ ಭಾಷೆ ಅರ್ಥಮಾಡಿಕೆ ಮತ್ತು ತಯಾರಿ
- C# ಲಕ್ಷಣಗಳ ಮೂಲಕ ಕಾರ್ಯವಿಧಾನ ಕರೆ ಮತ್ತು ಸಾಧನ ಬಳಕೆ
- ಸಂಭಾಷಣೆ ಸೆಷನ್‌ಗಳೊಂದಿಗೆ ಸಾಂದರ್ಭಿಕ ಜಾಗೃತ ಪ್ರತಿಕ್ರಿಯೆಗಳು
- ಡಿಪೆಂಡೆನ್ಸಿ ಇಂಜೆಕ್ಷನ್ ಮಾದರಿಗಳೊಂದಿಗೆ ವಿಸ್ತರಿಸಬಹುದಾದ ವಾಸ್ತುಶಿಲ್ಪ

## 📚 ಫ್ರೇಮ್ವರ್ಕ್ ಹೋಲಿಕೆ

ಈ ಉದಾಹರಣೆ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ದೃಷ್ಟಿಕೋನವನ್ನು ಇತರೆ ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳಿಗೆ ಹೋಲಿಕೆ ಮಾಡುತ್ತದೆ:

| ವೈಶಿಷ್ಟ್ಯ | ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ | ಇತರ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು |
|---------|-------------------------|------------------|
| **ಏಕೀಕರಣ** | ಸ್ಥಳೀಯ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಪರಿಸರ | ಬದಲಾಗುವ ಹೊಂದಾಣಿಕೆ |
| **ಸರಳತೆ** | ಸ್ವಚ್ಛ, ಸೂಕ್ಷ್ಮ API | ಹಲವಾರು ಬಾರಿ ಸಂಕೀರ್ಣ ಸೆಟ್ ಅಪ್ |
| **ವಿಸ್ತಾರಯೋಗ್ಯತೆ** | ಸುಲಭವಾದ ಸಾಧನ ಏಕೀಕರಣ | ಫ್ರೇಮ್ವರ್ಕ್-ಆಧಾರಿತ |
| **ಎಂಟರ್ಪ್ರೈಸ್ ತಯಾರಿ** | ಉತ್ಪಾದನಾ ನಿರ್ಮಾಣಕ್ಕೆ | ಫ್ರೇಮ್ವರ್ಕ್ ಪ್ರಕಾರ ಬದಲಾಗುತ್ತದೆ |

## 🚀 ಪ್ರಾರಂಭಿಸುತ್ತಾ

### ಅಗತ್ಯ ಪೂರ್ವಾಪೇಕ್ಷೆಗಳು

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ಅಥವಾ ಹೆಚ್ಚಿನದು
- ಆಜೂರ್ ಒப்பಂದದೊಂದಿಗೆ [ಆಜೂರ್ سب್ಸ್ಕ್ರಿಪ್ಷನ್](https://azure.microsoft.com/free/) ಮತ್ತು ಮಾದರಿ ನಿಯೋಜನೆ
- [ಆಜೂರ್ CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` ಮೂಲಕ ಸೈನ್ ಇನ್ ಮಾಡಿ

### ಅಗತ್ಯ ಪರಿಸರ ವ್ಯತ್ಯಯಗಳು

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# ಆಮೇಲೆ AzureCliCredential ಟೋಕನ್ ಪಡೆಯಲು ಸೈನ್ ಇನ್ ಮಾಡಿ
az login
```

```powershell
# ಪವರ್‌ಶೆಲ್
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# ನಂತರ AzureCliCredential ಟೋಕನ್ ಪಡೆಯಲು ಲಾಗಿನ್ ಮಾಡಿ
az login
```

### ಉದಾಹರಣಾ ಕೋಡ್

ಕೋಡ್ ಉದಾಹರಣೆಯನ್ನು ಚಾಲನೆ ಮಾಡಲು,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

ಅಥವಾ dotnet CLI ಬಳಸಿ:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

ಸಂಪೂರ್ಣ ಕೋಡ್ ಗೆ [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) ನೋಡಿ.

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

## 🎓 ಪ್ರಮುಖ ಅಂಶಗಳು

1. **ಏಜೆಂಟ್ ವಾಸ್ತುಶಿಲ್ಪ**: ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ .NET ನಲ್ಲಿ AI ಏಜೆಂಟುಗಳನ್ನು ನಿರ್ಮಿಸಲು ಸ್ವಚ್ಛ, ಪ್ರಕಾರ-ರಕ್ಷಿತ ಬಳಕೆಯನ್ನು ಒದಗಿಸುತ್ತದೆ
2. **ಟೂಲ್ ಏಕೀಕರಣ**: `[Description]` ಲಕ್ಷಣಗಳೊಂದಿಗೆ ಅಲಂಕರಿಸಲಾದ ಕಾರ್ಯಗಳು ಏಜೆಂಟ್‌ಗೆ ಉಪಯುಕ್ತ ಸಾಧನಗಳಾಗಿ ಪರಿವರ್ತಿತವಾಗುತ್ತವೆ
3. **ಸಂಭಾಷಣಾ ಸಾಂದರ್ಭಿಕತೆ**: ಸೆಷನ್ ನಿರ್ವಹಣೆಯೊಂದಿಗೆ ಬಹು-ತಿರುವು ಸಂಭಾಷಣೆಗಳು ಸಂಪೂರ್ಣ ಸಾಂದರ್ಭಿಕ ಜಾಗೃತಿ ಹೊಂದಿವೆ
4. **ವಿನ್ಯಾಸ ನಿರ್ವಹಣೆ**: ಪರಿಸರ ವ್ಯತ್ಯಯಗಳು ಮತ್ತು ಸುರಕ್ಷಿತ ಪ್ರಮಾಣಪತ್ರ ನಿರ್ವಹಣೆ .NET ಉತ್ತಮ ಅಭ್ಯಾಸಗಳನ್ನು ಅನುಸರಿಸುತ್ತದೆ
5. **ಆಜೂರ್ ಓಪನ್‌ಏಐ ರೆಸ್ಪಾನ್ಸ್ API**: ಏಜೆಂಟ್ ಆಜೂರ್.AI.OpenAI SDK ಮೂಲಕ ಆಜೂರ್ ಓಪನ್‌ಏಐ ರೆಸ್ಪಾನ್ಸ್ API ಅನ್ನು ಬಳಸುತ್ತದೆ

## 🔗 ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- [Microsoft Agent Framework ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry ನಲ್ಲಿ ಆಜೂರ್ ಓಪನ್‌ಏಐ](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET ಸಿಂಗಲ್ ಫೈಲ್ ಅಪ್ಲಿಕೇಶನ್ಸ್](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->