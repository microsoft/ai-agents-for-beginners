# 🔍 Microsoft Agent Framework ကို မိတ်ဆက်ခြင်း - အခြေခံ Agent (.NET)

## 📋 သင်ယူရမည့် အချက်များ

ဤဥပမာတွင် Microsoft Agent Framework ၏ အခြေခံဆိုင်ရာ အယူအဆများကို .NET တွင် အခြေခံ agent တစ်ခုဖြင့် ဆောင်ရွက်ပုံကို လေ့လာပါမည်။ C# နှင့် .NET ပတ်စပ်ပတ်ဝန်းကျင်ကို အသုံးပြုကာ အခြေခံ agent များ၏ ပုံစံများနှင့် သိပ္ပံနည်း ကျွမ်းကျင် agent များ ဖွံ့ဖြိုးမှုကို နားလည်လိမ့်မည်။

### သင်တွေ့ရှိရမည့် အရာများ

- 🏗️ **Agent ဖွဲ့စည်းပုံ**: .NET တွင် AI agent များ၏ အခြေခံ ဖွဲ့စည်းပုံ ကို နားလည်ခြင်း
- 🛠️ **ကိရိယာ ပေါင်းစည်းခြင်း**: agent များသည် ၎င်းတို့၏ လုပ်ဆောင်နိုင်မှုများကို တိုးချဲ့ရန် ပြင်ပ function များကို မည်သို့အသုံးပြုသည်ကို သင်ယူခြင်း  
- 💬 **စကားဝိုင်း စီးဆင်းမှု**: မျိုးစုံသော စကားပြော ဆက်သွယ်မှုများ နှင့် thread စီမံခန့်ခွဲမှုဖြင့် အကြောင်းအရာ ထိန်းချုပ်မှု
- 🔧 **ဆက်တင် ဖွဲ့စည်းပုံများ**: .NET သုံး agent တည်ဆောက်မှုနှင့် စီမံခန့်ခွဲမှုအတွက် ထိရောက်ဆုံးနည်းလမ်းများ

## 🎯 လေ့လာမည့် အဓိက ကျောင်းသားအချက်များ

### Agent Framework ၏ စည်းမျဉ်းများ

- **လွတ်လပ်ခွင့်**: .NET AI abstraction များကို အသုံးပြုကာ agent များသည် ကိုယ့်တိုင် ဆုံးဖြတ်ချက်များ ကောက်ယူပုံ
- **တုံ့ပြန်မှု**: ပတ်ဝန်းကျင် အခြေအနေများနှင့် အသုံးပြုသူ input များကို တုံ့ပြန်ပုံ
- **ကြိုတင် လုပ်ဆောင်မှု**: ရည်ရွယ်ချက်နှင့် ဇာတ်ကြောင်းအရ လှမ်းခတ်စီမံခြင်း
- **လူမှုဆက်ဆံမှု စွမ်းရည်**: သဘာဝဘာသာစကား ဖြင့် စကားဝိုင်း thread များအား ထိန်းချုပ် ဆက်သွယ်ခြင်း

### နည်းပညာ အစိတ်အပိုင်းများ

- **AIAgent**: Core agent စီမံခန့်ခွဲမှုနှင့် စကားဝိုင်း စီမံခြင်း (.NET)
- **Tool Functions**: Agent ၏ စွမ်းဆောင်ရည်များကို C# method နှင့် attribute များဖြင့် ထပ်ဆောင်း တိုးချဲ့ခြင်း
- **Azure OpenAI ပေါင်းစည်းမှု**: Azure OpenAI Responses API ဖြင့် ဘာသာစကားပုံစံများကို အကျိုးပြုသုံးစွဲခြင်း
- **လုံခြုံသော ဆက်တင်**: ပတ်ဝန်းကျင် အခြေပြု endpoint စီမံခြင်း

## 🔧 နည်းပညာ စံတော်ချိန်များ

### အဓိက နည်းပညာများ

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) ပေါင်းစည်းမှု
- Azure.AI.OpenAI client ပုံစံများ
- DotNetEnv ဖြင့် ပတ်ဝန်းကျင် အခြေပြု ဆက်တင်များ

### Agent ၏ စွမ်းရည်များ

- သဘာဝဘာသာစကား နားလည်မှုနှင့် ဖန်တီးမှု
- C# attributes ဖြင့် function ခေါ်ယူခြင်းနှင့် ကိရိယာ အသုံးပြုခြင်း
- စကားဝိုင်း အဆက်အသွယ်များနှင့် အကြောင်းအရာ ကို နားလည် စူးစမ်း တုံ့ပြန်မှုများ
- dependency injection ပုံစံဖြင့် ထပ်ဆောင်း ဖွဲ့စည်းပုံ

## 📚 Framework နှိုင်းယှဉ်ခြင်း

ဤဥပမာတွင် Microsoft Agent Framework ၏နည်းလမ်းကို အခြား agent framework များနှင့် နှိုင်းယှဉ် ပြသသည်။

| အင်္ဂါရပ် | Microsoft Agent Framework | အခြား Framework များ |
|---------|-------------------------|------------------|
| **ပေါင်းစည်းမှု** | Microsoft သက်ဆိုင်ရာ ပတ်ဝန်းကျင် | မတူညီသော ကိုက်တွယ်နိုင်မှု |
| **ရိုးရွင်းမှု** | ရိုးရှင်း သလောက် API | အများအားဖြင့် ပြင်းထန်သော တပ်ဆင်မှု |
| **တိုးချဲ့နိုင်မှု** | ကိရိယာ အသုံးပြုခြင်းလွယ်ကူမှု | Framework ကို မူတည်ပြီး |
| **စက်မှုလုပ်ငန်း အသင့်ဖြစ်မှု** | ထုတ်လုပ်မှုအတွက် တည်ဆောက်ထား | Framework အလိုက် ကွဲပြားမှုများရှိသည် |

## 🚀 စတင် ပြုလုပ်ရန်

### ကြိုတင် လိုအပ်ချက်များ

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) သို့မဟုတ် အထက်တန်း
- Azure OpenAI resource နှင့် model deployment ပါရှိသော [Azure subscription](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` ဖြင့် အကောင့်ဖြင့် ဝင်ရောက်သည်

### လိုအပ်သော ပတ်ဝန်းကျင်အပြောင်းအလဲများ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# ထို့နောက် AzureCliCredential သည် token ရယူနိုင်ရန် လက်မှတ်ထိုးဝင်ပါ။
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# အဲ့လိုရင် AzureCliCredential က token ရအောင် စာရင်းဝင်ပါ
az login
```

### နမူနာ ကုဒ်

ဒီကုဒ် သို့မဟုတ် နမူနာကို ပြေးရန်

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

ဒါမှမဟုတ် dotnet CLI ကို အသုံးပြု၍

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

ပြည့်စုံသော ကုဒ်များအတွက် [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) ကို ကြည့်ပါ။

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

## 🎓 အဓိက သင်ခန်းစာများ

1. **Agent ဖွဲ့စည်းပုံ**: Microsoft Agent Framework က .NET တွင် AI agent များ တည်ဆောက်ရာတွင် ရိုးရှင်းမြတ်သော၊ type-safe နည်းလမ်းဖြစ်သည်
2. **ကိရိယာ ပေါင်းစည်းခြင်း**: `[Description]` attribute သတ်မှတ်ထားသော function များသည် agent ၏ အသုံးချနိုင်သော ကိရိယာများ ဖြစ်လာသည်
3. **စကားဝိုင်း အကြောင်းအရာ**: Session များ စီမံခြင်းအားဖြင့် မျိုးစုံသော စကားဝိုင်းများကို အပြည့်အစုံ အကြောင်းအရာ နှင့် ထိန်းချုပ်နိုင်သည်
4. **ဆက်တင် စီမံခြင်း**: ပတ်ဝန်းကျင်အပြောင်းအလဲများနှင့် လုံခြုံသော credential ကို မသိမ်းဆည်းဘဲ .NET အကောင်းဆုံး လမ်းညွှန်ချက်များနှင့် လိုက်နာသည်
5. **Azure OpenAI Responses API**: Agent သည် Azure.AI.OpenAI SDK မှတစ်ဆင့် Azure OpenAI Responses API ကို အသုံးပြုသည်

## 🔗 အပို အရင်းအမြစ်များ

- [Microsoft Agent Framework စာရွက်စာတမ်း](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry တွင် Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->