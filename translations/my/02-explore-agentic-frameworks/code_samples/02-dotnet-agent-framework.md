<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:40:48+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "my"
}
-->
# 🔍 Agentic Frameworks ကိုလေ့လာခြင်း - အခြေခံ Agent (.NET)

## 📋 သင်ယူရမည့်အရာများ

ဒီ notebook မှာ Microsoft Agent Framework ရဲ့ အခြေခံအယူအဆတွေကို .NET မှာ အခြေခံ agent တစ်ခုအဖြစ် အကောင်အထည်ဖော်ထားတဲ့ နမူနာကို အသုံးပြုပြီး လေ့လာပါမယ်။ C# နဲ့ .NET ecosystem ကို အသုံးပြုပြီး အတတ်ပညာရှိတဲ့ agent တွေ ဘယ်လိုအလုပ်လုပ်သလဲဆိုတာကို နားလည်သိရှိနိုင်ပါမယ်။

**သင်ရှာဖွေတွေ့ရှိမယ့်အရာများ:**
- 🏗️ **Agent Architecture**: .NET မှာ AI agent တွေရဲ့ အခြေခံဖွဲ့စည်းပုံကို နားလည်ခြင်း
- 🛠️ **Tool Integration**: Agent တွေက အပြင် function တွေကို အသုံးပြုပြီး စွမ်းရည်တွေကို တိုးမြှင့်ပုံ  
- 💬 **Conversation Flow**: Thread management ကို အသုံးပြုပြီး multi-turn conversations နဲ့ context ကို စီမံပုံ
- 🔧 **Configuration Patterns**: .NET မှာ agent setup နဲ့ စီမံခန့်ခွဲမှုအတွက် အကောင်းဆုံးနည်းလမ်းများ

## 🎯 အဓိကအယူအဆများ

### Agentic Framework Principles
- **Autonomy**: .NET AI abstractions ကို အသုံးပြုပြီး agent တွေ ဘယ်လို ကိုယ်တိုင်ဆုံးဖြတ်ချက်လုပ်နိုင်သလဲ
- **Reactivity**: ပတ်ဝန်းကျင်အပြောင်းအလဲနဲ့ အသုံးပြုသူ input တွေကို တုံ့ပြန်ပုံ
- **Proactivity**: ရည်မှန်းချက်နဲ့ context အပေါ် အခြေခံပြီး အစီအစဉ်ဆောင်ရွက်ပုံ
- **Social Ability**: Conversation threads ကို အသုံးပြုပြီး သဘာဝဘာသာစကားနဲ့ ဆက်သွယ်ပုံ

### Technical Components
- **AIAgent**: Core agent orchestration နဲ့ conversation management (.NET)
- **Tool Functions**: C# methods နဲ့ attributes တွေကို အသုံးပြုပြီး agent ရဲ့ စွမ်းရည်တွေကို တိုးမြှင့်ခြင်း
- **OpenAI Integration**: .NET APIs တွေကို အသုံးပြုပြီး language models တွေကို ချိတ်ဆက်ခြင်း
- **Environment Management**: DotNetEnv ကို အသုံးပြုပြီး configuration နဲ့ credential တွေကို လုံခြုံစွာ စီမံခြင်း

## ⚙️ လိုအပ်ချက်များနှင့် Setup

**လိုအပ်သော Dependencies:**
- .NET 9.0 SDK သို့မဟုတ် အထက်
- Visual Studio 2022 သို့မဟုတ် VS Code (C# extension ပါ)

**NuGet Packages:**
- `Microsoft.Extensions.AI` - Core AI abstractions
- `Microsoft.Extensions.AI.OpenAI` - OpenAI integration (preview)
- `DotNetEnv` - Environment variable management

**Environment Configuration (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Technical Stack

**Core Technologies:**
- Microsoft Agent Framework (.NET)
- GitHub Models API integration
- OpenAI-compatible client patterns
- DotNetEnv ကို အသုံးပြုတဲ့ environment-based configuration

**Agent Capabilities:**
- သဘာဝဘာသာစကားကို နားလည်ခြင်းနဲ့ ဖန်တီးပေးခြင်း
- C# attributes တွေကို အသုံးပြုပြီး function တွေကို ခေါ်ယူခြင်း
- Conversation threads တွေကို အသုံးပြုပြီး context-aware response ပေးခြင်း
- Dependency injection patterns တွေကို အသုံးပြုပြီး architecture ကို တိုးမြှင့်ခြင်း

## 📚 Framework Comparison

ဒီနမူနာက Microsoft Agent Framework ရဲ့ .NET မှာ အသုံးပြုပုံကို အခြား platform တွေနဲ့ နှိုင်းယှဉ်ပြသထားပါတယ်:

| Feature | .NET Agent Framework | Python Equivalents |
|---------|---------------------|-------------------|
| **Type Safety** | C# ရဲ့ strong typing | Dynamic typing |
| **Integration** | .NET ecosystem နဲ့ သဘာဝချိတ်ဆက်မှု | Compatibility များစွာရှိခြင်း |
| **Performance** | Compiled code performance | Interpreted execution |
| **Enterprise Ready** | Production .NET apps အတွက် အထူးသင့်လျော် | Framework အလိုက် မတူညီမှုရှိခြင်း |
| **Tooling** | Visual Studio integration | IDE အပေါ် မူတည်မှု |

## 🚀 စတင်အသုံးပြုခြင်း

အောက်ပါ cell တွေကို လိုက်နာပြီး .NET မှာ သင့်ရဲ့ ပထမဆုံး အခြေခံ agent ကို တည်ဆောက်ပြီး အခြေခံ agentic အယူအဆတွေကို နားလည်ပါ။

## 📦 Installation and Setup

ဒီနမူနာကို .NET Single File App အနေနဲ့ အလွယ်တကူ run လို့ရပါတယ်။ အပြည့်အစုံ implementation ကို `02-dotnet-agent-framework.cs` ဖိုင်မှာ ကြည့်ရှုနိုင်ပါတယ်။

ဒီနမူနာကို run ဖို့:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

သို့မဟုတ် dotnet CLI ကို အသုံးပြုပါ:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Code Walkthrough

အပြည့်အစုံ implementation မှာ ပါဝင်တာတွေက:

### 1. Package Dependencies

```csharp
// Core AI abstraction layer for .NET applications
#r "nuget: Microsoft.Extensions.AI, 9.9.1"

// Microsoft Agent Framework OpenAI integration
#r "nuget: Microsoft.Agents.AI.OpenAI, 1.0.0-preview.251001.3"

// Core Microsoft Agent Framework library
#r "nuget: Microsoft.Agents.AI, 1.0.0-preview.251001.3"

// Environment variable management
#r "nuget: DotNetEnv, 3.1.1"
```

### 2. Essential Imports

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Environment Configuration

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Tool Function Definition

```csharp
// Random destination generator tool
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
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
    
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}
```

### 5. Configuration and Client Setup

```csharp
// Extract environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? 
    throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? 
    throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI client for GitHub Models
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI client
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);
```

### 6. Agent Configuration

```csharp
const string AGENT_NAME = "TravelAgent";

const string AGENT_INSTRUCTIONS = @"You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
""Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?""

Always prioritize user preferences. If they mention a specific destination like ""Bali"" or ""Paris,"" focus your planning on that location rather than suggesting alternatives.
";
```

### 7. Agent Initialization

```csharp
// Create AI agent with travel planning capabilities
AIAgent agent = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions)
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create((Func<string>)GetRandomDestination)]
    );
```

### 8. Conversation Management

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 အဓိကအကျဉ်းချုပ်

1. **Agent Architecture**: Microsoft Agent Framework က .NET မှာ AI agent တွေကို type-safe နည်းလမ်းနဲ့ တည်ဆောက်နိုင်စေပါတယ်
2. **Tool Integration**: `[Description]` attributes တွေကို အသုံးပြုပြီး function တွေကို agent ရဲ့ tools အဖြစ် အသုံးပြုနိုင်ပါတယ်
3. **Conversation Context**: Thread management က multi-turn conversations တွေကို context-aware ဖြစ်အောင် စီမံပေးပါတယ်
4. **Configuration Management**: Environment variables နဲ့ credential တွေကို .NET best practices အတိုင်း လုံခြုံစွာ စီမံနိုင်ပါတယ်
5. **OpenAI Compatibility**: GitHub Models integration က OpenAI-compatible APIs တွေကို အလွယ်တကူ ချိတ်ဆက်နိုင်ပါတယ်

## 🔗 အပိုဆောင်းရင်းမြစ်များ

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။