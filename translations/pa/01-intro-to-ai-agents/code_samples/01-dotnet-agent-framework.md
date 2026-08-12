# 🌍 ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ (.NET) ਨਾਲ AI ਯਾਤਰਾ ਏਜੰਟ

## 📋 ਦਰਸ਼ਨਾਨੁਮਾ ਸਥਿਤੀ

ਇਹ ਉਦਾਹਰਨ ਸਿਖਾਉਂਦੀ ਹੈ ਕਿ ਕਿਵੇਂ ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਫਰ.NET ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਬੁੱਧੀਮਾਨ ਯਾਤਰਾ ਯੋਜਨਾ ਬਣਾਉਣ ਵਾਲਾ ਏਜੰਟ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ। ਇਹ ਏਜੰਟ ਦੁਨੀਆ ਭਰ ਦੇ ਕਿਤੇ ਵੀ ਗੰਤਵਾਂ ਲਈ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਵਿਅਕਤੀਗਤ ਦਿਨ-ਭਰ ਦੀਆਂ ਯਾਤਰਾ ਯੋਜਨਾਵਾਂ ਤਿਆਰ ਕਰ ਸਕਦਾ ਹੈ।

### ਮੁੱਖ ਸਮਰੱਥਾਵਾਂ:

- 🎲 **ਯਾਦਰਚ ਛਾਂਟਣਾ**: ਛੁੱਟੀ ਵਾਲੀਆਂ ਥਾਂਵਾਂ ਚੁਣਨ ਲਈ ਇੱਕ ਕਸਟਮ ਟੂਲ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ
- 🗺️ **ਬੁੱਧੀਮਾਨ ਯਾਤਰਾ ਯੋਜਨਾ**: ਹਰ ਦਿਨ ਲਈ ਵਿਸਥਾਰ ਵਾਲੀਆਂ ਯੋਜਨਾਵਾਂ ਬਣਾਉਂਦਾ ਹੈ
- 🔄 **ਤੁਰੰਤ ਸਟ੍ਰੀਮਿੰਗ**: ਤੁਰੰਤ ਅਤੇ ਸਟ੍ਰੀਮਿੰਗ ਦੋਹਾਂ ਜਵਾਬਾਂ ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ
- 🛠️ **ਕਸਟਮ ਟੂਲ ਇੰਟੀਗਰੇਸ਼ਨ**: ਏਜੰਟ ਸਮਰੱਥਾਵਾਂ ਵਧਾਉਣ ਦਾ ਤਰੀਕਾ ਦਰਸਾਉਂਦਾ ਹੈ

## 🔧 ਤਕਨੀਕੀ ਵਾਸਤੂਕਲਾ

### ਮੁੱਖ ਤਕਨਾਲੋਜੀਆਂ

- **ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ**: AI ਏਜੰਟ ਵਿਕਾਸ ਲਈ ਆਖਰੀ .NET ਕਾਰਜਾਨੁਸ਼ਠਾਨ
- **ਅਜ਼ੂਰ ਓਪਨAI (Responses API)**: ਮਾਡਲ ਅਨੁਮਾਨ ਲਈ ਅਜ਼ੂਰ ਓਪਨAI Responses API ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ
- **ਅਜ਼ੂਰ ਆਈਡੈਂਟੀਟੀ**: `AzureCliCredential` (`az login`) ਰਾਹੀਂ ਸੁਰੱਖਿਅਤ ਸਾਈਨ-ਇਨ
- **ਸੁਰੱਖਿਅਤ ਕਨਫਿਗਰੇਸ਼ਨ**: ਵਾਤਾਵਰਣ ਅਧਾਰਿਤ ਐਂਡਪਾਇੰਟ ਪ੍ਰਬੰਧਨ

### ਮੁੱਖ ਭਾਗ

1. **AIAgent**: ਮੁੱਖ ਏਜੰਟ ਜੋ ਗੱਲਬਾਤ ਦੇ ਪ੍ਰਵਾਹ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ
2. **ਕਸਟਮ ਟੂਲ**: ਏਜੰਟ ਲਈ ਉਪਲੱਬਧ `GetRandomDestination()` ਫੰਕਸ਼ਨ
3. **Responses ਕਲਾਇੰਟ**: ਅਜ਼ੂਰ ਓਪਨAI Responses-ਅਧਾਰਿਤ ਗੱਲਬਾਤ ਇੰਟਰਫੇਸ
4. **ਸਟ੍ਰੀਮਿੰਗ ਸਮਰਥਨ**: ਤੁਰੰਤ ਜਵਾਬ ਬਣਾਉਣ ਦੀ ਸਮਰਥਾ

### ਇੰਟੀਗਰੇਸ਼ਨ ਪੈਟਰਨ

```mermaid
graph LR
    A[ਯੂਜ਼ਰ ਬਿਨੈ] --> B[ਏਆਈ ਏਜੰਟ]
    B --> C[ਐਜ਼ੂਰ OpenAI (ਜਵਾਬ ਦੇਣ ਵਾਲੀ API)]
    B --> D[GetRandomDestination ਟੂਲ]
    C --> E[ਯਾਤਰਾ ਰੂਟ]
    D --> E
```

## 🚀 ਸ਼ੁਰੂਆਤੀ ਟਿਪਸ

### ਲੋੜੀਂਦੇ ਤੱਤ

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ਜਾਂ ਇਸ ਤੋਂ ਉੱਪਰ
- ਇੱਕ [Azure subscription](https://azure.microsoft.com/free/) ਜਿਸ ਵਿੱਚ ਅਜ਼ੂਰ ਓਪਨAI ਸਰੋਤ ਅਤੇ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਹੋਵੇ
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` ਨਾਲ ਸਾਈਨ-ਇਨ

### ਲੋੜੀਂਦੇ ਵਾਤਾਵਰਣ ਵਰਿਅਬਲ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# ਫਿਰ ਸਾਈਨ ਇਨ ਕਰੋ ਤਾਂ ਜੋ AzureCliCredential ਇੱਕ ਟੋਕਨ ਪ੍ਰਾਪਤ ਕਰ ਸਕੇ
az login
```

```powershell
# ਪਾਵਰਸ਼ੈੱਲ
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# ਫਿਰ ਸਾਈਨ ਇਨ ਕਰੋ ਤਾਂ ਜੋ AzureCliCredential ਟੋਕਨ ਪ੍ਰਾਪਤ ਕਰ ਸਕੇ
az login
```

### ਨਮੂਨਾ ਕੋਡ

ਕੋਡ ਉਦਾਹਰਨ ਚਲਾਉਣ ਲਈ,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

ਜਾਂ dotnet CLI ਦੀ ਵਰਤੋਂ ਕਰਕੇ:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

ਪੂਰਾ ਕੋਡ ਵੇਖਣ ਲਈ [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) ਨੂੰ ਦੇਖੋ।

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

## 🎓 ਮੁੱਖ ਸਿੱਖਣ ਵਾਲੀਆਂ ਗੱਲਾਂ

1. **ਏਜੰਟ ਵਾਸਤੂਕਲਾ**: ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ .NET ਵਿੱਚ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਇੱਕ ਸਾਫ਼, ਟਾਈਪ-ਸੁਰੱਖਿਅਤ ਤਰੀਕਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ
2. **ਟੂਲ ਇੰਟੀਗਰੇਸ਼ਨ**: `[Description]` ਗੁਣਾਂ ਨਾਲ ਸਜਾਇਆ ਗਿਆ ਫੰਕਸ਼ਨ ਏਜੰਟ ਲਈ ਉਪਲੱਬਧ ਟੂਲ ਬਣ ਜਾਂਦਾ ਹੈ
3. **ਕਨਫਿਗਰੇਸ਼ਨ ਪ੍ਰਬੰਧਨ**: ਵਾਤਾਵਰਣ ਵਰਿਅਬਲ ਅਤੇ ਸੁਰੱਖਿਅਤ ਕ੍ਰੈਡੈਂਸ਼ੀਅਲ ਸੰਭਾਲ ਬਿਹਤਰ .NET ਅਭਿਆਸਾਂ ਦੇ ਅਨੁਕੂਲ
4. **ਅਜ਼ੂਰ ਓਪਨAI Responses API**: ਏਜੰਟ ਅਜ਼ੂਰ.AI.OpenAI SDK ਰਾਹੀਂ ਅਜ਼ੂਰ ਓਪਨAI Responses API ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ

## 🔗 ਵਾਧੂ ਸਰੋਤ

- [ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦਸਤਾਵੇਜ਼](https://learn.microsoft.com/agent-framework)
- [ਮਾਈਕ੍ਰੋਸਾਫਟ ਫਾਊਂਡਰੀ ਵਿੱਚ ਅਜ਼ੂਰ ਓਪਨAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET ਸਿੰਗਲ ਫਾਈਲ ਐਪਸ](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->