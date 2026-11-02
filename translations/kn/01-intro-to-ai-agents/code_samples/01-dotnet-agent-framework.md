# 🌍 ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ (.NET) ಜೊತೆಗೆ AI ಪ್ರಯಾಣ ಏಜೆಂಟ್

## 📋 ಸನ್ನಿವೇಶ ಅವಲೋಕನ

ಈ ಉದಾಹರಣೆ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಅನ್ನು .NET ನಲ್ಲಿ ಬಳಸಿ ಬುದ್ಧಿವಂತ ಪ್ರಯಾಣ ಯೋಜನೆ ಏಜೆಂಟ್ ಅನ್ನು ಹೇಗೆ ನಿರ್ಮಿಸುವುದು ಎಂದು ತೋರಿಸುತ್ತದೆ. ಏಜೆಂಟ್ ವಿಶ್ವದ ಅನಿಯಮಿತ ಗಂತವ್ಯ ಸ್ಥಳಗಳಿಗೆ ವೈಯಕ್ತಿಕೃತ ದಿವಸ-ಪ್ರಯಾಣ ಯೋಜನೆಗಳನ್ನು ಸ್ವಯಂಕರವಾಗಿ ರಚಿಸಬಹುದು.

### ಮುಖ್ಯ ಸಾಮರ್ಥ್ಯಗಳು:

- 🎲 **ಯಾದೃಚ್ಛಿಕ ಗಂತವ್ಯ ಆಯ್ಕೆ**: ರಜೆ ಸ್ಥಳಗಳನ್ನು ಆರಿಸಲು ಕಸ್ಟಮ್ ಟೂಲನ್ನು ಬಳಸುವುದು
- 🗺️ **ಬುದ್ಧಿವಂತ ಪ್ರಯಾಣ ಯೋಜನೆ**: ದಿನಾಂಕದ ಪ್ರತಿ ದಿನದ ವಿವರವಾದ ಯೋಜನೆಗಳನ್ನು ರಚಿಸುವುದು
- 🔄 **ನಿಖರ ಸಮಯ ಸ್ಟ್ರೀಮಿಂಗ್**: ತಕ್ಷಣದ ಮತ್ತು ಸ್ಟ್ರೀಮಿಂಗ್ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ಬೆಂಬಲಿಸುವುದು
- 🛠️ **ಕಸ್ಟಮ್ ಟೂಲ್ ಎন্টಿಗ್ರೇಷನ್**: ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ವಿಸ್ತರಿಸುವುದನ್ನು ತೋರಿಸುವುದು

## 🔧 ತಾಂತ್ರಿಕ ವಾಸ್ತುಶಿಲ್ಪ

### ಮೂಲ ತಂತ್ರಜ್ಞಾನಗಳು

- **ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್**: AI ಏಜೆಂಟ್ ಅಭಿವೃದ್ಧಿಗೆ ನವೀನ .NET ಅನುಷ್ಠಾನ
- **ಅಜುರ್ ಓಪನ್‌ಎಐ (ಪ್ರತಿಕ್ರಿಯೆಗಳು API)**: ಮಾದರಿ ನಿರ್ಣಯಕ್ಕಾಗಿ ಅಜುರ್ ಓಪನ್‌ಎಐ ಪ್ರತಿಕ್ರಿಯೆಗಳು API ಅನ್ನು ಬಳಸುತ್ತದೆ
- **ಅಜುರ್ ಐಡന്റಿಟಿ**: `AzureCliCredential` (`az login`) ಮೂಲಕ ಸುರಕ್ಷಿತ ಸೈನ್-ಇನ್
- **ಸುರಕ್ಷಿತ ರಚನೆ**: ಪರಿಸರ ಆಧಾರಿತ ಎಂಡ್‌ಪಾಯಿಂಟ್ ನಿರ್ವಹಣೆ

### ಪ್ರಮುಖ ಘಟಕಗಳು

1. **AIAgent**: ಸಂಭಾಷಣೆ ಪ್ರವರ್ತನೆಗಾಗಿ ಮುಖ್ಯ ಏಜೆಂಟ್ ಆರ್ಕೆಸ್ಟ್ರೇಟರ್
2. **ಕಸ್ಟಮ್ ಟೂಲ್ಸ್**: ಏಜೆಂಟ್‌ಗೆ ಲಭ್ಯವಿರುವ `GetRandomDestination()` ಕಾರ್ಯ
3. **ಪ್ರತಿಕ್ರಿಯೆಗಳು ಕ್ಲೈಂಟ್**: ಅಜುರ್ ಓಪನ್‌ಎಐ ಪ್ರತಿಕ್ರಿಯೆ ಆಧಾರಿತ ಸಂಭಾಷಣೆ ಇಂಟರ್ಫೇಸ್
4. **ಸ್ಟ್ರೀಮಿಂಗ್ ಬೆಂಬಲ**: ನಿಖರ ಸಮಯ ಪ್ರತಿಕ್ರಿಯಾ ಉತ್ಪಾದನೆ ಸಾಮರ್ಥ್ಯಗಳು

### ಏಕೀಕರಣ ಮಾದರಿ

```mermaid
graph LR
    A[ಬಳಕೆದಾರದ ವಿನಂತಿ] --> B[ಎಐ ಏಜೆಂಟ್]
    B --> C[ಅಜೂರ್ ಓಪನ್‌ಎಐ (ಪ್ರತಿಕ್ರಿಯೆಗಳು API)]
    B --> D[GetRandomDestination ಉಪಕರಣ]
    C --> E[ಪ್ರವಾಸ ಯೋಜನೆ]
    D --> E
```

## 🚀 ಪ್ರಾರಂಭಿಸುವುದು

### ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ಅಥವಾ ಹೆಚ್ಚು
- ಅಜುರ್ ಓಪನ್‌ಎಐ ಸಂಪನ್ಮೂಲ ಮತ್ತು ಮಾದರಿ ನಿಯೋಜನೆಯೊಂದಿಗೆ [ಅಜುರ್ ಸಬ್‌ಸ್ಕ್ರಿಪ್ಶನ್](https://azure.microsoft.com/free/)
- [ಅಜುರ್ CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` ಮೂಲಕ ಸೈನ್ ಇನ್ ಆಗಿ

### ಅಗತ್ಯವಿರುವ ಪರಿಸರ ವ್ಯತ್ಯಯಗಳು

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# ನಂತರ ಲಾಗಿನ್ ಮಾಡಿ যাতে AzureCliCredential ಟೋಕೆನ್ ಪಡೆಯಬಹುದು
az login
```

```powershell
# ಪವರ್‌ಶೆಲ್
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# ನಂತರ ಚಂದಾ ನೀಡಿ, zodat AzureCliCredential ಟೋಕನ್ ಪಡೆದುಕೊಳ್ಳಬಹುದು
az login
```

### ಮಾದರಿ ಕೋಡ್

ಕೋಡ್ ಉದಾಹರಣೆಯನ್ನು ಚಾಲನೆ ಮಾಡಲು,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

ಅಥವಾ dotnet CLI ಬಳಸಿ:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

ಪೂರ್ಣ ಕೋಡ್‌ಗೆ [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) ನೋಡಿ.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.4.1
#:package Microsoft.Agents.AI.OpenAI@1.1.0
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

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip
// Run the agent with streaming enabled for real-time response display
// Shows the agent's thinking and response as it generates the content
// Provides better user experience with immediate feedback
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 ಪ್ರಮುಖ ಕೊಂಡಿತಣೆಗಳು

1. **ಏಜೆಂಟ್ ವಾಸ್ತುಶಿಲ್ಪ**: ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ .NET ನಲ್ಲಿ AI ಏಜೆಂಟ್ಗಳ ನಿರ್ಮಾಣಕ್ಕೆ ಸ್ವಚ್ಛ, ಟೈಪ್-ಸೇಫ್ ವಿಧಾನವನ್ನು ಒದಗಿಸುತ್ತದೆ
2. **ಟೂಲ್ ಏಕೀಕರಣ**: `[Description]` ಲಕ್ಷಣಗಳಿಂದ ಅಲಂಕರಿಸಿರುವ ಕಾರ್ಯಗಳು ಏಜೆಂಟ್‌ಗೆ ಲಭ್ಯವಿರುವ ಟೂಲ್ಗಳಾಗುತ್ತವೆ
3. **ರಚನೆ ನಿರ್ವಹಣೆ**: ಪರಿಸರ ವ್ಯತ್ಯಯಗಳು ಮತ್ತು ಸುರಕ್ಷಿತ ಕ್ರೆಡೆಶಿಯಲ್ ಹ್ಯಾಂಡ್ಲಿಂಗ್ .NET ಅತ್ಯುತ್ತಮ ಅಭ್ಯಾಸಗಳನ್ನು ಅನುಸರಿಸುತ್ತದೆ
4. **ಅಜುರ್ ಓಪನ್‌ಎಐ ಪ್ರತಿಕ್ರಿಯೆಗಳು API**: ಏಜೆಂಟ್ ಅಜುರ್.AI.OpenAI SDK ಮೂಲಕ ಅಜುರ್ ಓಪನ್‌ಎಐ ಪ್ರತಿಕ್ರಿಯೆ API ಅನ್ನು ಬಳಸುತ್ತದೆ

## 🔗 ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- [ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಡಾಕ್ಯುಮೆಂಟೇಷನ್](https://learn.microsoft.com/agent-framework)
- [ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿಯಲ್ಲಿ ಅಜುರ್ ಓಪನ್‌ಎಐ](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET ಸಿಂಗಲ್ ಫೈಲ್ ಅಪ್‌ಗಳು](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->