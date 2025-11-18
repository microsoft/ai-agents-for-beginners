<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T14:37:25+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "my"
}
-->
# 🔍 Microsoft Agent Framework ကိုလေ့လာခြင်း - အခြေခံ Agent (.NET)

## 📋 သင်ယူရမည့်အရာများ

ဒီဥပမာမှာ Microsoft Agent Framework ရဲ့ အခြေခံအယူအဆတွေကို .NET မှာ အခြေခံ Agent တစ်ခုအဖြစ် အကောင်အထည်ဖော်ထားတဲ့နည်းလမ်းကို လေ့လာမှာဖြစ်ပါတယ်။ C# နဲ့ .NET ecosystem ကို အသုံးပြုပြီး အတတ်နိုင်ဆုံး Agentic patterns တွေကို သင်ယူပြီး အတတ်နိုင်ဆုံး Intelligent Agents တွေ ဘယ်လိုအလုပ်လုပ်သလဲဆိုတာကို နားလည်နိုင်ပါမယ်။

### သင်ရှာဖွေတွေ့ရှိမယ့်အရာများ

- 🏗️ **Agent Architecture**: .NET မှာ AI Agent တွေရဲ့ အခြေခံဖွဲ့စည်းပုံကို နားလည်ခြင်း  
- 🛠️ **Tool Integration**: Agent တွေက အပြင် function တွေကို အသုံးပြုပြီး စွမ်းရည်တွေ တိုးမြှင့်ပုံ  
- 💬 **Conversation Flow**: Thread management နဲ့ အတူ Multi-turn conversations နဲ့ context ကို စီမံပုံ  
- 🔧 **Configuration Patterns**: .NET မှာ Agent setup နဲ့ စီမံခန့်ခွဲမှုအတွက် အကောင်းဆုံးနည်းလမ်းများ  

## 🎯 အဓိကအကြောင်းအရာများ

### Agentic Framework Principles

- **Autonomy**: .NET AI abstractions ကို အသုံးပြုပြီး Agent တွေ ဘယ်လို ကိုယ်တိုင်ဆုံးဖြတ်ချက်များ ချမှတ်နိုင်သလဲ  
- **Reactivity**: ပတ်ဝန်းကျင်အပြောင်းအလဲများနဲ့ အသုံးပြုသူ input များကို တုံ့ပြန်ပုံ  
- **Proactivity**: ရည်မှန်းချက်များနဲ့ context အပေါ် အခြေခံပြီး အတက်အမြောက် လုပ်ဆောင်ပုံ  
- **Social Ability**: Conversation threads တွေကို အသုံးပြုပြီး သဘာဝဘာသာစကားနဲ့ ဆက်သွယ်ပုံ  

### Technical Components

- **AIAgent**: Core agent orchestration နဲ့ conversation management (.NET)  
- **Tool Functions**: C# methods နဲ့ attributes တွေကို အသုံးပြုပြီး Agent ရဲ့ စွမ်းရည်တွေ တိုးမြှင့်ပုံ  
- **OpenAI Integration**: .NET APIs တွေကို အသုံးပြုပြီး Language models တွေကို အကျိုးရှိစွာ အသုံးချခြင်း  
- **Secure Configuration**: API key management ကို Environment-based နည်းလမ်းနဲ့ လုံခြုံစွာ စီမံခြင်း  

## 🔧 Technical Stack

### Core Technologies

- Microsoft Agent Framework (.NET)  
- GitHub Models API integration  
- OpenAI-compatible client patterns  
- DotNetEnv နဲ့ Environment-based configuration  

### Agent Capabilities

- သဘာဝဘာသာစကား နားလည်ခြင်းနဲ့ ဖန်တီးခြင်း  
- Function calling နဲ့ C# attributes တွေကို အသုံးပြုပြီး tool usage  
- Conversation threads တွေကို အသုံးပြုပြီး context-aware responses  
- Dependency injection patterns တွေကို အသုံးပြုပြီး Extensible architecture  

## 📚 Framework Comparison

ဒီဥပမာမှာ Microsoft Agent Framework ရဲ့ နည်းလမ်းကို အခြား Agentic frameworks တွေနဲ့ နှိုင်းယှဉ်ပြသထားပါတယ်:

| Feature | Microsoft Agent Framework | အခြား Frameworks |
|---------|-------------------------|------------------|
| **Integration** | Microsoft ecosystem နဲ့ သဘာဝကျစွာ တွဲဖက်နိုင်မှု | Compatibility မတူညီမှုများ |
| **Simplicity** | API ရိုးရှင်းပြီး နားလည်ရလွယ်ကူမှု | Setup အဆင့်ဆင့်များ ရှုပ်ထွေးမှု |
| **Extensibility** | Tool integration လွယ်ကူမှု | Framework အပေါ် မူတည်မှု |
| **Enterprise Ready** | Production အတွက် အဆင်ပြေမှု | Framework အပေါ် မူတည်မှု |

## 🚀 စတင်အသုံးပြုခြင်း

### Prerequisites

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) သို့မဟုတ် အထက်  
- [GitHub Models API access token](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### လိုအပ်သော Environment Variables

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
  

### Sample Code

Code ကို run ဖို့,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
dotnet CLI ကို အသုံးပြုခြင်းဖြင့်:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
[`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) မှာ အပြည့်အစုံ code ကို ကြည့်ရှုနိုင်ပါတယ်။

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
  

## 🎓 အဓိက Takeaways

1. **Agent Architecture**: Microsoft Agent Framework က .NET မှာ AI Agent တွေကို type-safe နည်းလမ်းနဲ့ ဖွဲ့စည်းပေးပါတယ်  
2. **Tool Integration**: `[Description]` attributes တွေကို အသုံးပြုထားတဲ့ functions တွေဟာ Agent ရဲ့ tools အဖြစ် အသုံးပြုနိုင်ပါတယ်  
3. **Conversation Context**: Thread management က Multi-turn conversations တွေကို context-aware ဖြစ်စေပါတယ်  
4. **Configuration Management**: Environment variables နဲ့ လုံခြုံ credential handling က .NET best practices တွေကို လိုက်နာပါတယ်  
5. **OpenAI Compatibility**: GitHub Models integration က OpenAI-compatible APIs တွေကို အဆင်ပြေစွာ အသုံးချနိုင်ပါတယ်  

## 🔗 အပိုဆောင်းရင်းမြစ်များ

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/agent-framework)  
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->