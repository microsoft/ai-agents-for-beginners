# 🔍 ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಅನ್ವೇಷಣೆ - 基本 ಏಜೆಂಟ್ (.NET)

## 📋 ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಉದಾಹರಣೆ .NET ನಲ್ಲಿ ಮೂಲ ಏಜೆಂಟ್ ಅನುಷ್ಟಾನವನ್ನು ಮುಖಾಂತರ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ನ അടിസ്ഥാന ತತ್ವಗಳನ್ನು ಅನ್ವೇಷಿಸುತ್ತದೆ. ನೀವು ಕೇಂದ್ರ ಏಜೆಂಟಿಕ್ ಮಾದರಿಗಳನ್ನು ಕಲಿಯುತ್ತೀರಿ ಮತ್ತು C# ಮತ್ತು .NET ಪರಿಸರವನ್ನು ಬಳಸಿಕೊಂಡು ಬುದ್ಧಿವಂತ ಏಜೆಂಟ್‌ಗಳು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತವೆ ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುತ್ತೀರಿ.

### ನೀವು ಹುಡುಕಲಿರುವುದು ಏನು

- 🏗️ **ಏಜೆಂಟ್ ವಾಸ್ತುಶಿಲ್ಪ**: .NET ನಲ್ಲಿ AI ಏಜೆಂಟ್‌ಗಳ ಮೂಲ ರಚನೆಯನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು
- 🛠️ **ಪರಿಕರ ಏಕೀಕರಣ**: ಏಜೆಂಟ್‌ ಗಳು ಸಾಮರ್ಥ್ಯಗಳನ್ನು ವಿಸ್ತರಿಸಲು ಹೊರಗಿನ ಕಾರ್ಯಗಳನ್ನು ಹೇಗೆ ಬಳಸುತ್ತವೆ  
- 💬 **ಸಂವಾದ ಪ್ರವಾಹ**: ಬಹು-ತಿರುಗು ಸಂವಾದಗಳನ್ನು ಮತ್ತು ಸಂಧರ್ಭವನ್ನು ಥ್ರೆಡ್ ನಿರ್ವಹಣೆಯೊಂದಿಗೆ ನಿರ್ವಹಿಸುವುದು
- 🔧 **ರಚನಾ ಮಾದರಿಗಳು**: .NET ನಲ್ಲಿ ಏಜೆಂಟ್ ಸೆಟ್‌ಅಪ್ ಮತ್ತು ನಿರ್ವಹಣೆಯ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು

## 🎯 ಪ್ರಮುಖ ತತ್ವಗಳು ಒಳಗೊಂಡಿವೆ

### ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್ವರ್ಕ್ ತತ್ವಗಳು

- **ಸ್ವಾಯತ್ತತೆ**: .NET AI ಅಮೂರ್ತಿಗಳೊಂದಿಗೆ ಏಜೆಂಟ್‌ಗಳು ಸ್ವತಂತ್ರ ನಿರ್ಧಾರಗಳನ್ನು ಹೇಗೆ ಮಾಡುತ್ತವೆ
- **ಪ್ರತಿಕ್ರಿಯಾಶೀಲತೆ**: ಪರಿಸರ ಬದಲಾವಣೆಗಳಿಗೆ ಮತ್ತು ಬಳಕೆದಾರರ ಇನ್ಪುಟ್‌ಗಳಿಗೆ ಪ್ರತಿಕ್ರಿಯಿಸುವುದು
- **ಪ್ರೋಅಕ್ಟಿವಿಟಿ**: ಗುರಿಗಳ ಮತ್ತು ಸಂಧರ್ಭ ಆಧಾರಿತ ಪ್ರೇರಣೆ ಪಡೆದುಕೊಳ್ಳುವುದು
- **ಸಾಮಾಜಿಕ ಸಾಮರ್ಥ್ಯ**: ಸಂವಾದ ಥ್ರೆಡ್‌ಗಳ ಮೂಲಕ ಪ್ರಾಕೃತಿಕ ಭಾಷೆಯಲ್ಲಿ ಸಂವಹನ

### ತಾಂತ್ರಿಕ ಘಟಕಗಳು

- **AIAgent**: ಕೋರ್ ಏಜೆಂಟ್ ಸಂಘಟನೆ ಮತ್ತು ಸಂವಾದ ನಿರ್ವಹಣೆ (.NET)
- **ಪರಿಕರ ಕಾರ್ಯಗಳು**: C# ವಿಧಾನಗಳು ಮತ್ತು ಲಕ್ಷಣಗಳ ಮೂಲಕ ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ವಿಸ್ತರಿಸುವುದು
- **ಅಜೂರ್ ಓಪನ್‌ಎಐ ಏಕೀಕರಣ**: ಅಜೂರ್ ಓಪನ್‌ಎಐ ಪ್ರತಿಕ್ರಿಯೆ APIs ಮೂಲಕ ಭಾಷಾ ಮಾದರಿಗಳನ್ನು ಬಳಕೆ ಮಾಡುವುದು
- **ಸುರಕ್ಷಿತ ಕಾನ್ಫಿಗರೇಶನ್**: ಪರಿಸರ ಆಧಾರಿತ ಎಂಡ್ಪಾಯಿಂಟ್ ನಿರ್ವಹಣೆ

## 🔧 ತಾಂತ್ರಿಕ ಸ್ಟ್ಯಾಕ್

### ಕೇಂದ್ರ ತಂತ್ರಜ್ಞಾನಗಳು

- ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ (.NET)
- ಅಜೂರ್ ಓಪನ್‌ಎಐ (ಪ್ರತಿಕ್ರಿಯೆ API) ಏಕೀಕರಣ
- Azure.AI.OpenAI ಕ್ಲಯಿಂಟ್ ಮಾದರಿಗಳು
- DotNetEnv ಸಹ ಪರಿಸರ ಆಧಾರಿತ ಕಾನ್ಫಿಗರೇಶನ್

### ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯಗಳು

- ಪ್ರಾಕೃತಿಕ ಭಾಷೆ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಮತ್ತು ಸೃಷ್ಟಿ
- ಕಾರ್ಯ ಕರೆಮಾಡುವುದು ಮತ್ತು C# ಲಕ್ಷಣಗಳೊಂದಿಗೆ ಪರಿಕರ ಬಳಕೆ
- ಸಂಧರ್ಭ-ಜಾಗರೂಕ ಪ್ರತಿಕ್ರಿಯೆಗಳು ಸಂವಾದ ಥ್ರೆಡ್‌ಗಳೊಂದಿಗೆ
- ಅವಲಂಬನೆ ಬಿದ್ದಾಯಿಕೆ ಮಾದರಿಗಳೊಂದಿಗೆ ವಿಸ್ತರಣೆ ಸಾಧ್ಯವಾದ ವಾಸ್ತುಶಿಲ್ಪ

## 📚 ಫ್ರೇಮ್ವರ್ಕ್ ಹೋಲಿಕೆ

ಈ ಉದಾಹರಣೆ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಬಳಕೆಯನ್ನು ಇತರ ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳೊಂದಿಗೆ ಹೋಲಿಸುತ್ತದೆ:

| ಲಕ್ಷಣ | ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ | ಇತರ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು |
|---------|-------------------------|------------------|
| **ಎಕೀಕರಣ** | ಸ್ಥಳೀಯ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಪರಿಸರ | ವಿಭಿನ್ನ ಹೊಂದಾಣಿಕೆ |
| **ಸರಳತೆ** | ಸ್ವಚ್ಛ, ಬೋಧಿಸಬಹುದಾದ API | ಹೆಚ್ಚಾಗಿ ಸಂಕೀರ್ಣ ಸೆಟ್‌ಅಪ್ |
| **ವಿಸ್ತರಣೆ ಸಾಧ್ಯತೆ** | ಸುಲಭ ಪರಿಕರ ಏಕೀಕರಣ | ಫ್ರೇಮ್ಹವರ್ಕ್-ನಿರ್ಭರ |
| **ಉದ್ಯಮಕ್ಕೆ ಸಿದ್ಧ** | ಉತ್ಪಾದನೆಗೆ ನಿರ್ಮಿತ | ಫ್ರೇಮ್ವರ್ಕ್ ಪ್ರಕಾರ ಬದಲಾಗುತ್ತದೆ |

## 🚀 ಪ್ರಾರಂಭಿಸುವುದು

### ಪೂರ್ವಶರತ್ತುಗಳು

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ಅಥವಾ ಹೆಚ್ಚಿನದು
- [ಅಜೂರ್ ಚಂದಾದಾರಿಕೆ](https://azure.microsoft.com/free/) ಜೊತೆಗೆ ಅಜೂರ್ ಓಪನ್‌ಎಐ ಸಂಪನ್ಮೂಲ ಮತ್ತು ಮಾದರಿ ನಿಯೋಜನೆ
- [ಅಜೂರ್ CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` ಮೂಲಕ ಲಾಗಿನ್ ಆಗಿ

### ಅಗತ್ಯವಿರುವ ಪರಿಸರ ಬದಲಾಗುವರು

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# ನಂತರ ಲಾಗಿನ್ ಮಾಡಿ ताकि AzureCliCredential ಟೋಕನ್ ಪಡೆಯಬಹುದು
az login
```

```powershell
# ಪವರ್‌ಶೆಲ್
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# ನಂತರ ಸೈನ್ ಇನ್ ಮಾಡಿ যাতে AzureCliCredential ಟೋಕನ್ ಪಡೆಯಬಹುದು
az login
```

### ಮಾದರಿ ಕೋಡ್

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

ಪೂರ್ಣ ಕೋಡ್‌ಗಾಗಿ [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) ನೋಡಿ.

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

## 🎓 ಪ್ರಮುಖ ಪಾಠಗಳು

1. **ಏಜೆಂಟ್ ವಾಸ್ತುಶಿಲ್ಪ**: ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ .NET ನಲ್ಲಿ AI ಏಜೆಂಟ್‌ಗಳ ನಿರ್ಮಾಣಕ್ಕೆ ಸ್ವಚ್ಛ, ಟೈಪ್-ಸೇಫ್ ವಿಧಾನವನ್ನು ನೀಡುತ್ತದೆ
2. **ಪರಿಕರ ಏಕೀಕರಣ**: `[Description]` ಲಕ್ಷಣಗಳೊಂದಿಗೆ ಅಲంకೃತ ಕಾರ್ಯಗಳು ಏಜೆಂಟ್‌ಗಾಗಿ ಲಭ್ಯವಿರುವ ಪರಿಕರಗಳಾಗುತ್ತವೆ
3. **ಸಂವಾದ ಸಂಧರ್ಭ**: ಥ್ರೆಡ್ ನಿರ್ವಹಣೆಯ ಮೂಲಕ ಪೂರ್ಣ ಸಂಧರ್ಭ ಜಾಗರೂಕತೆಯೊಂದಿಗೆ ಬಹುತಿರುಗು ಸಂವಾದಗಳು ಸಾಧ್ಯವಾಗುತ್ತವೆ
4. **ಕಾನ್ಫಿಗರೇಶನ್ ನಿರ್ವಹಣೆ**: ಪರಿಸರ ಬದಲಾಗುವರು ಮತ್ತು ಸುರಕ್ಷಿತ ರಹಸ್ಯ ನಿರ್ವಹಣೆ .NET ಉತ್ತಮ ಅಭ್ಯಾಸಗಳನ್ನು ಅನುಸರಿಸುತ್ತದೆ
5. **ಅಜೂರ್ ಓಪನ್‌ಎಐ ಪ್ರತಿಕ್ರಿಯೆ API**: ಏಜೆಂಟ್ ಅಜೂರ್.AI.OpenAI SDK ಮೂಲಕ ಅಜೂರ್ ಓಪನ್‌ಎಐ ಪ್ರತಿಕ್ರಿಯೆ APIs ಅನ್ನು ಬಳಸುತ್ತದೆ

## 🔗 ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- [Microsoft Agent Framework ಡಾಕ್ಯುಮೆಂಟೇಷನ್](https://learn.microsoft.com/agent-framework)
- [ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿಯಲ್ಲಿ ಅಜೂರ್ ಓಪನ್‌ಎಐ](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->