# 🌍 ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ (.NET) ಜೊತೆಗೆ AI ಪ್ರಯಾಣ ಏಜೆಂಟ್

## 📋 ದೃಶ್ಯಾವಳಿ ಅವಲೋಕನ

ಈ ಉದಾಹರಣೆ .NET ಗಾಗಿ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಬಳಸಿಕೊಂಡು ಬುದ್ಧಿಮತ್ತೆಯ ಪ್ರವಾಸ ಯೋಜನಾ ಏಜೆಂಟ್ ಅನ್ನು ಹೇಗೆ ನಿರ್ಮಿಸಲು ಎಂದು ತೋರಿಸುತ್ತದೆ. ಏಜೆಂಟ್ ವಿಶ್ವದ ಸುತ್ತಲೂ ಯಾದೃಚ್ಛಿಕ ಗಮ್ಯಸ್ಥಳಗಳಿಗೆ ವೈಯಕ್ತಿಕೃತ ದಿನ ಪ್ರವಾಸ ಮಾರ್ಗಸೂಚಿಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ರಚಿಸಬಹುದು.

### ಪ್ರಮುಖ ಸಾಮರ್ಥ್ಯಗಳು:

- 🎲 **ಯಾದೃಚ್ಛಿಕ ಗಮ್ಯಸ್ಥಳ ಆಯ್ಕೆ**: ರಜೆ ಸ್ಥಳಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡಲು ಕಸ್ಟಮ್ ಟೂಲ್ ಬಳಸುತ್ತದೆ
- 🗺️ **ಬುದ್ದಿಮತ್ತೆಯ ಪ್ರವಾಸ ಯೋಜನೆ**: ದಿನನಿತ್ಯದ ವಿಸ್ತೃತ ಮಾರ್ಗಸೂಚಿಗಳನ್ನು ಸೃಷ್ಟಿಸುತ್ತದೆ
- 🔄 **ನಿಜಸಮಯ ಸ್ಟ್ರೀಮಿಂಗ್**: ತಕ್ಷಣದ ಮತ್ತು ಸ್ಟ್ರೀಮಿಂಗ್ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ಎರಡನ್ನೂ ಬೆಂಬಲಿಸುತ್ತದೆ
- 🛠️ **ಕಸ್ಟಮ್ ಟೂಲ್ ಏಕೀಕರಣ**: ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ವಿಸ್ತರಿಸುವ ವಿಧಾನವನ್ನು ತೋರಿಸುತ್ತದೆ

## 🔧 ತಾಂತ್ರಿಕ ವಾಸ್ತುಶಿಲ್ಪ

### ಪ್ರಮುಖ ತಂತ್ರಜ್ಞಾನಗಳು

- **ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್**: AI ಏಜೆಂಟ್ ಅಭಿವೃದ್ಧಿಗಾಗಿ ಇತ್ತೀಚಿನ .NET ಅನುಷ್ಠಾನ
- **ಅಜೂರ್ OpenAI (ಪ್ರತಿಕ್ರಿಯೆಗಳ API)**: ಮಾದರಿ ನಿರ್ಣಯಕ್ಕೆ ಅಜೂರ್ OpenAI Responses API ಬಳಸುತ್ತದೆ
- **ಅಜೂರ್ ಗುರುತಿಸು**: `AzureCliCredential` (`az login`) ಮೂಲಕ ಭದ್ರ ಸೈನ್ ಇನ್
- **ಭದ್ರ ಕಾನ್ಫಿಗರೇಶನ್**: ಪರಿಸರ ಆಧಾರಿತ ಎಂಡ್‌ಪಾಯಿಂಟ್ ನಿರ್ವಹಣೆ

### ಪ್ರಮುಖ ಘಟಕಗಳು

1. **AIAgent**: ಸಂಭಾಷಣಾ ಹರಿವನ್ನು ನಿಭಾಯಿಸುವ ಮುಖ್ಯ ಏಜೆಂಟ್ ಸಂಯೋಜಕ
2. **ಕಸ್ಟಮ್ ಟೂಲ್ಸ್**: ಏಜೆಂಟ್‌ಗೆ ಲಭ್ಯವಿರುವ `GetRandomDestination()` ಫಂಕ್ಷನ್
3. **ಪ್ರತಿಕ್ರಿಯೆಗಳ ಕ್ಲೈಂಟ್**: ಅಜೂರ್ OpenAI Responses ಆಧಾರಿತ ಸಂಭಾಷಣಾ ಇಂಟರ್ಫೇಸ್
4. **ಸ್ಟ್ರೀಮಿಂಗ್ ಬೆಂಬಲ**: ನಿಜಸಮಯ ಪ್ರತಿಕ್ರಿಯೆ ರಚನ ಸಾಮರ್ಥ್ಯಗಳು

### ಏಕೀಕರಣ ರೂಪರೇಖೆ

```mermaid
graph LR
    A[ಬಳಕೆದಾರ ವಿನಂತಿ] --> B[ಕೃತ್ರಿಮ ಬುದ್ಧಿಮತ್ತೆ ಏಜೆಂಟ್]
    B --> C[ಅಜೊರ್ ಓಪನ್‌ಎಐ (ಪ್ರತಿಕ್ರಿಯೆಗಳು API)]
    B --> D[GetRandomDestination ಉಪಕರಣ]
    C --> E[ಪ್ರವಾಸಿ ಮಾರ್ಗಪಟ್ಟಿ]
    D --> E
```

## 🚀 ಪ್ರಾರಂಭಿಸುವುದು

### ಅವಶ್ಯಕತೆಗಳು

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ಅಥವಾ ಮೇಲಿನ ಆವೃತ್ತಿ
- ಅಜೂರ್ OpenAI ಸಂಪನ್ಮೂಲ ಮತ್ತು ಮಾದರಿ ನಿಯೋಜನೆಯೊಂದಿಗೆ [ಅಜೂರ್ ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್](https://azure.microsoft.com/free/)
- [ಅಜೂರ್ CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` ಮೂಲಕ ಸೈನ್ ಇನ್

### ಅಗತ್ಯ ಪರಿಸರ ಚರ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# ನಂತರ, AzureCliCredential ටೋಕನ್ ಪಡೆಯಲು ಸೈನ್ ಇನ್ ಮಾಡಿ
az login
```

```powershell
# ಪವರ್‌ಶೆಲ್
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# ನಂತರ ಸೈನ್ ಇನ್ ಮಾಡಿ, ώστε AzureCliCredential ಟೋಕನ್ ಪಡೆಯಬಹುದು
az login
```

### ಮಾದರಿ ಕೋಡ್

ಕೋಡ್ ಉದಾಹರಣೆಯನ್ನು ಚಾಲನೆ ಮಾಡಲು,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

ಅಥವಾ ಡಾಟ್ನೆಟ್ CLI ಉಪಯೋಗಿಸಿ:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

ಸಂಪೂರ್ಣ ಕೋಡ್‌ಗೆ [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) ಭೇಟಿಮಾಡಿ.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@9.*
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

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetOpenAIResponseClient(deployment)
    .CreateAIAgent(
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

## 🎓 ಪ್ರಮುಖ ಪಾಠಗಳು

1. **ಏಜೆಂಟ್ ವಾಸ್ತುಶಿಲ್ಪ**: ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ .NET ನಲ್ಲಿ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಸ್ವಚ್ಛ, ಪ್ರಕಾರ-ಸುರಕ್ಷಿತ 접근ಪಥ ಒದಗಿಸುತ್ತದೆ
2. **ಟೂಲ್ ಏಕೀಕರಣ**: `[Description]` ಗುಣಲಕ್ಷಣಗಳಿಂದ ಅಲಂಕರಿಸಲಾದ ಫಂಕ್ಷನ್‌ಗಳು ಏಜೆಂಟ್‌ಗೆ ಲಭ್ಯವಾಗುವ ಟೂಲ್ಗಳಾಗುತ್ತವೆ
3. **ಕಾನ್ಫಿಗರೇಶನ್ ನಿರ್ವಹಣೆ**: ಪರಿಸರ ಚರ ಮತ್ತು ಭದ್ರ ಪ್ರಮಾಣಿಕರಣ ಹಾಗು ಹ್ಯಾಂಡ್ಲಿಂಗ್ .NET ಅತ್ಯುತ್ತಮ ಪದ್ಧತಿಗಳನ್ನು ಅನುಸರಿಸುತ್ತವೆ
4. **ಅಜೂರ್ OpenAI Responses API**: ಏಜೆಂಟ್ Azure.AI.OpenAI SDK ಮುಖಾಂತರ ಅಜೂರ್ OpenAI Responses API ಬಳ,useರುತ್ತದೆ

## 🔗 ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- [ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://learn.microsoft.com/agent-framework)
- [ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿಯಲ್ಲಿ ಅಜೂರ್ OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET ಸಿಂಗಲ್ ಫೈಲ್ ಅಪ್ಸ್](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->