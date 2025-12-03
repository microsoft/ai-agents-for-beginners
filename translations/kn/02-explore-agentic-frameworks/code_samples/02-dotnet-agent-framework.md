<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-12-03T17:11:26+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "kn"
}
-->
# 🔍 Microsoft Agent Framework - ಮೂಲ ಏಜೆಂಟ್ (.NET) ಅನ್ವೇಷಣೆ

## 📋 ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಉದಾಹರಣೆ Microsoft Agent Framework ನ ಮೂಲ ತತ್ವಗಳನ್ನು .NET ನಲ್ಲಿ ಮೂಲ ಏಜೆಂಟ್ ಅನುಷ್ಠಾನದ ಮೂಲಕ ಅನ್ವೇಷಿಸುತ್ತದೆ. ನೀವು ಮುಖ್ಯ ಏಜೆಂಟಿಕ್ ಮಾದರಿಗಳನ್ನು ಕಲಿಯುತ್ತೀರಿ ಮತ್ತು C# ಮತ್ತು .NET ಪರಿಸರವನ್ನು ಬಳಸಿಕೊಂಡು ಬುದ್ಧಿವಂತ ಏಜೆಂಟ್‌ಗಳು ಹೇಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತವೆ ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುತ್ತೀರಿ.

### ನೀವು ಏನು ಕಂಡುಹಿಡಿಯುತ್ತೀರಿ

- 🏗️ **ಏಜೆಂಟ್ ಆರ್ಕಿಟೆಕ್ಚರ್**: .NET ನಲ್ಲಿ AI ಏಜೆಂಟ್‌ಗಳ ಮೂಲ ರಚನೆ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು  
- 🛠️ **ಟೂಲ್ ಇಂಟಿಗ್ರೇಶನ್**: ಏಜೆಂಟ್‌ಗಳು ಸಾಮರ್ಥ್ಯಗಳನ್ನು ವಿಸ್ತರಿಸಲು ಬಾಹ್ಯ ಕಾರ್ಯಗಳನ್ನು ಹೇಗೆ ಬಳಸುತ್ತವೆ  
- 💬 **ಸಂವಾದದ ಪ್ರವಾಹ**: ಥ್ರೆಡ್ ನಿರ್ವಹಣೆಯೊಂದಿಗೆ ಬಹು-ಮೋಡ ಸಂಭಾಷಣೆ ಮತ್ತು ಸಂದರ್ಭವನ್ನು ನಿರ್ವಹಿಸುವುದು  
- 🔧 **ಕಾನ್ಫಿಗರೇಶನ್ ಮಾದರಿಗಳು**: .NET ನಲ್ಲಿ ಏಜೆಂಟ್ ಸೆಟಪ್ ಮತ್ತು ನಿರ್ವಹಣೆಗೆ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು  

## 🎯 ಮುಖ್ಯ ತತ್ವಗಳು

### ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ತತ್ವಗಳು

- **ಸ್ವಾಯತ್ತತೆ**: .NET AI ಅಬ್ಸ್ಟ್ರಾಕ್ಷನ್‌ಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಏಜೆಂಟ್‌ಗಳು ಸ್ವತಂತ್ರ ನಿರ್ಧಾರಗಳನ್ನು ಹೇಗೆ ಮಾಡುತ್ತವೆ  
- **ಪ್ರತಿಕ್ರಿಯಾಶೀಲತೆ**: ಪರಿಸರ ಬದಲಾವಣೆಗಳು ಮತ್ತು ಬಳಕೆದಾರರ ಇನ್‌ಪುಟ್‌ಗಳಿಗೆ ಪ್ರತಿಕ್ರಿಯಿಸುವುದು  
- **ಪ್ರೋಆಕ್ಟಿವಿಟಿ**: ಗುರಿಗಳು ಮತ್ತು ಸಂದರ್ಭವನ್ನು ಆಧರಿಸಿ ಮುಂದಾಳತ್ವವನ್ನು ತೆಗೆದುಕೊಳ್ಳುವುದು  
- **ಸಾಮಾಜಿಕ ಸಾಮರ್ಥ್ಯ**: ಸಂಭಾಷಣಾ ಥ್ರೆಡ್‌ಗಳ ಮೂಲಕ ನೈಸರ್ಗಿಕ ಭಾಷೆಯಲ್ಲಿ ಸಂವಹನ ಮಾಡುವುದು  

### ತಾಂತ್ರಿಕ ಘಟಕಗಳು

- **AIAgent**: ಮೂಲ ಏಜೆಂಟ್ ಸಂಯೋಜನೆ ಮತ್ತು ಸಂಭಾಷಣೆ ನಿರ್ವಹಣೆ (.NET)  
- **ಟೂಲ್ ಫಂಕ್ಷನ್‌ಗಳು**: C# ವಿಧಾನಗಳು ಮತ್ತು ಗುಣಲಕ್ಷಣಗಳೊಂದಿಗೆ ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ವಿಸ್ತರಿಸುವುದು  
- **OpenAI ಇಂಟಿಗ್ರೇಶನ್**: ಮಾನದಂಡಿತ .NET API ಗಳ ಮೂಲಕ ಭಾಷಾ ಮಾದರಿಗಳನ್ನು ಬಳಸುವುದು  
- **ಸುರಕ್ಷಿತ ಕಾನ್ಫಿಗರೇಶನ್**: ಪರಿಸರ ಆಧಾರಿತ API ಕೀ ನಿರ್ವಹಣೆ  

## 🔧 ತಾಂತ್ರಿಕ ಸ್ಟಾಕ್

### ಮೂಲ ತಂತ್ರಜ್ಞಾನಗಳು

- Microsoft Agent Framework (.NET)  
- GitHub Models API ಇಂಟಿಗ್ರೇಶನ್  
- OpenAI-ಅನುಕೂಲಕರ ಕ್ಲೈಂಟ್ ಮಾದರಿಗಳು  
- DotNetEnv ಬಳಸಿ ಪರಿಸರ ಆಧಾರಿತ ಕಾನ್ಫಿಗರೇಶನ್  

### ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯಗಳು

- ನೈಸರ್ಗಿಕ ಭಾಷೆ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು ಮತ್ತು ತಯಾರಿಸುವುದು  
- C# ಗುಣಲಕ್ಷಣಗಳೊಂದಿಗೆ ಕಾರ್ಯವನ್ನು ಕರೆದು ಟೂಲ್ ಬಳಕೆ  
- ಸಂಭಾಷಣಾ ಥ್ರೆಡ್‌ಗಳೊಂದಿಗೆ ಸಂದರ್ಭ-ಜಾಗೃತ ಪ್ರತಿಕ್ರಿಯೆಗಳು  
- ಡಿಪೆಂಡೆನ್ಸಿ ಇಂಜೆಕ್ಷನ್ ಮಾದರಿಗಳೊಂದಿಗೆ ವಿಸ್ತರಿಸಬಹುದಾದ ಆರ್ಕಿಟೆಕ್ಚರ್  

## 📚 ಫ್ರೇಮ್‌ವರ್ಕ್ ಹೋಲಿಕೆ

ಈ ಉದಾಹರಣೆ Microsoft Agent Framework ನ ವಿಧಾನವನ್ನು ಇತರ ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳೊಂದಿಗೆ ಹೋಲಿಸುತ್ತದೆ:

| ವೈಶಿಷ್ಟ್ಯ | Microsoft Agent Framework | ಇತರ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳು |
|-----------|---------------------------|-----------------------|
| **ಇಂಟಿಗ್ರೇಶನ್** | ಸ್ಥಳೀಯ Microsoft ಪರಿಸರ | ವೈವಿಧ್ಯಮಯ ಹೊಂದಾಣಿಕೆ |
| **ಸರಳತೆ** | ಸ್ವಚ್ಛ, ಬುದ್ಧಿವಂತ API | ಸಾಮಾನ್ಯವಾಗಿ ಸಂಕೀರ್ಣ ಸೆಟಪ್ |
| **ವಿಸ್ತರಣೀಯತೆ** | ಸುಲಭ ಟೂಲ್ ಇಂಟಿಗ್ರೇಶನ್ | ಫ್ರೇಮ್‌ವರ್ಕ್-ಆಧಾರಿತ |
| **ಎಂಟರ್‌ಪ್ರೈಸ್ ರೆಡಿ** | ಉತ್ಪಾದನೆಗೆ ನಿರ್ಮಿಸಲಾಗಿದೆ | ಫ್ರೇಮ್‌ವರ್ಕ್ ಪ್ರಕಾರ ಬದಲಾಗುತ್ತದೆ |

## 🚀 ಪ್ರಾರಂಭಿಸುವುದು

### ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ಅಥವಾ ಹೆಚ್ಚಿನದು  
- [GitHub Models API access token](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### ಅಗತ್ಯವಿರುವ ಪರಿಸರ ವ್ಯತ್ಯಯಗಳು

```bash
# zsh/ಬ್ಯಾಶ್
export GH_TOKEN=<your_github_token>
export GH_ENDPOINT=https://models.github.ai/inference
export GH_MODEL_ID=openai/gpt-5-mini
```
  
```powershell
# ಪವರ್‌ಶೆಲ್
$env:GH_TOKEN = "<your_github_token>"
$env:GH_ENDPOINT = "https://models.github.ai/inference"
$env:GH_MODEL_ID = "openai/gpt-5-mini"
```
  

### ಮಾದರಿ ಕೋಡ್

ಕೋಡ್ ಉದಾಹರಣೆಯನ್ನು ಚಲಾಯಿಸಲು,  

```bash
# zsh/ಬ್ಯಾಶ್
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
  

## 🎓 ಮುಖ್ಯ ಪಾಠಗಳು

1. **ಏಜೆಂಟ್ ಆರ್ಕಿಟೆಕ್ಚರ್**: Microsoft Agent Framework .NET ನಲ್ಲಿ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಸ್ವಚ್ಛ, ಪ್ರಕಾರ-ಸುರಕ್ಷಿತ ವಿಧಾನವನ್ನು ಒದಗಿಸುತ್ತದೆ  
2. **ಟೂಲ್ ಇಂಟಿಗ್ರೇಶನ್**: `[Description]` ಗುಣಲಕ್ಷಣಗಳೊಂದಿಗೆ ಅಲಂಕರಿಸಲಾದ ಕಾರ್ಯಗಳು ಏಜೆಂಟ್‌ಗಳಿಗೆ ಲಭ್ಯವಿರುವ ಟೂಲ್‌ಗಳಾಗುತ್ತವೆ  
3. **ಸಂಭಾಷಣಾ ಸಂದರ್ಭ**: ಥ್ರೆಡ್ ನಿರ್ವಹಣೆ ಬಹು-ಮೋಡ ಸಂಭಾಷಣೆಯನ್ನು ಸಂಪೂರ್ಣ ಸಂದರ್ಭ ಜಾಗೃತತೆಯೊಂದಿಗೆ ಸಕ್ರಿಯಗೊಳಿಸುತ್ತದೆ  
4. **ಕಾನ್ಫಿಗರೇಶನ್ ನಿರ್ವಹಣೆ**: ಪರಿಸರ ವ್ಯತ್ಯಯಗಳು ಮತ್ತು ಸುರಕ್ಷಿತ ಕ್ರೆಡೆನ್ಷಿಯಲ್ ಹ್ಯಾಂಡ್ಲಿಂಗ್ .NET ಉತ್ತಮ ಅಭ್ಯಾಸಗಳನ್ನು ಅನುಸರಿಸುತ್ತದೆ  
5. **OpenAI ಹೊಂದಾಣಿಕೆ**: GitHub Models ಇಂಟಿಗ್ರೇಶನ್ OpenAI-ಅನುಕೂಲಕರ API ಗಳ ಮೂಲಕ ಸುಲಭವಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ  

## 🔗 ಹೆಚ್ಚುವರಿ ಸಂಪತ್ತುಗಳು

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/agent-framework)  
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:  
ಈ ದಾಖಲೆ AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಾಖಲೆ ಪ್ರಾಮಾಣಿಕ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪುಅರ್ಥಗಳು ಅಥವಾ ತಪ್ಪುಅರ್ಥೈಸುವಿಕೆಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->