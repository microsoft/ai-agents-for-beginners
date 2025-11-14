<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e959fefef991a78e6eb72b5ce8ca58d4",
  "translation_date": "2025-11-11T11:46:11+00:00",
  "source_file": "01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.md",
  "language_code": "my"
}
-->
# 🌍 Microsoft Agent Framework (.NET) ဖြင့် AI ခရီးသွားအကျိုးဆောင်

## 📋 အခြေအနေအကျဉ်းချုပ်

ဒီ notebook က Microsoft Agent Framework for .NET ကို အသုံးပြုပြီး အတတ်နိုင်ဆုံး ခရီးစဉ်အစီအစဉ်ရေးဆွဲနိုင်တဲ့ အကျိုးဆောင်တစ်ခုကို တည်ဆောက်ပုံကို ပြသထားပါတယ်။ ဒီအကျိုးဆောင်က ကမ္ဘာတစ်ဝှမ်းရှိ အခွင့်အလမ်းများအတွက် ကိုယ်ပိုင်နေ့စဉ်ခရီးစဉ်အစီအစဉ်များကို အလိုအလျောက် ဖန်တီးပေးနိုင်ပါတယ်။

### အဓိကစွမ်းရည်များ:

- 🎲 **အခွင့်အလမ်းရွေးချယ်မှု**: အခွင့်အလမ်းရွေးချယ်ရန် custom tool ကို အသုံးပြုသည်
- 🗺️ **အတတ်နိုင်ဆုံး ခရီးစဉ်အစီအစဉ်ရေးဆွဲမှု**: နေ့စဉ်ခရီးစဉ်အစီအစဉ်များကို အသေးစိတ်ဖန်တီးပေးသည်
- 🔄 **အချိန်နှင့်တပြေးညီ Streaming**: ချက်ချင်းနှင့် Streaming အဖြေများကို ပံ့ပိုးပေးသည်
- 🛠️ **Custom Tool ပေါင်းစည်းမှု**: အကျိုးဆောင်စွမ်းရည်များကို တိုးချဲ့ပုံကို ပြသသည်

## 🔧 နည်းပညာဆောက်လုပ်ပုံ

### အဓိကနည်းပညာများ

- **Microsoft Agent Framework**: AI အကျိုးဆောင်ဖွံ့ဖြိုးရေးအတွက် .NET implementation အနောက်ဆုံးပေါ်
- **GitHub Models Integration**: GitHub ရဲ့ AI model inference service ကို အသုံးပြုသည်
- **OpenAI API Compatibility**: OpenAI client libraries ကို custom endpoints ဖြင့် အသုံးပြုသည်
- **Secure Configuration**: API key ကို ပတ်ဝန်းကျင်အခြေခံစနစ်ဖြင့် စီမံခန့်ခွဲသည်

### အဓိကအစိတ်အပိုင်းများ

1. **AIAgent**: စကားဝိုင်းလှုပ်ရှားမှုကို စီမံခန့်ခွဲသော အဓိကအကျိုးဆောင်
2. **Custom Tools**: `GetRandomDestination()` function ကို အကျိုးဆောင်အတွက် ရရှိနိုင်သည်
3. **Chat Client**: GitHub Models-backed စကားဝိုင်း interface
4. **Streaming Support**: အချိန်နှင့်တပြေးညီ အဖြေဖန်တီးမှုစွမ်းရည်

### ပေါင်းစည်းမှုပုံစံ

```mermaid
graph LR
    A[User Request] --> B[AI Agent]
    B --> C[GitHub Models API]
    B --> D[GetRandomDestination Tool]
    C --> E[Travel Itinerary]
    D --> E
```

## 🚀 စတင်အသုံးပြုခြင်း

### လိုအပ်ချက်များ

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) သို့မဟုတ် အထက်
- [GitHub Models API access token](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)

### လိုအပ်သော ပတ်ဝန်းကျင် Variables

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

### နမူနာကုဒ်

ကုဒ်နမူနာကို အလုပ်လုပ်စေလိုပါက၊

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

dotnet CLI ကို အသုံးပြု၍:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

[`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) တွင် အပြည့်အစုံကုဒ်ကို ကြည့်ရှုနိုင်ပါသည်။

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@9.*
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

// Create AI Agent with Travel Planning Capabilities
// Initialize OpenAI client, get chat client for specified model, and create AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->