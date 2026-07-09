# 🔍 Microsoft Agent Framework ကိုရှာဖွေခြင်း - Basic Agent (.NET)

## 📋 သင်ယူရမည့်ရည်ရွယ်ချက်များ

ဤဥပမာသည် .NET တွင် basic agent တစ်ခုအား အသုံးပြုသည့်အခါ Microsoft Agent Framework ၏ အခြေခံအယူအဆများကို ရှာဖွေပြသပါသည်။ သင်သည် အဓိက agentic ပုံစံများကို သင်ယူပြီး C# နှင့် .NET ပတ်ဝန်းကျင်ကို အသုံးပြု၍ ဘယ်လိုကောင်းမွန်သော agent များ လည်ပတ်ကြောင်း နားလည်နိုင်ပါလိမ့်မည်။

### သင်ရှာဖွေမည့်အကြောင်းအရာများ

- 🏗️ **Agent ပုံသဏ္ဍာန်**: .NET တွင် AI agent များ၏အခြေခံဖွဲ့စည်းပုံနားလည်ခြင်း
- 🛠️ **ကိရိယာ ပေါင်းစည်းခြင်း**: agent များသည် အပြင် functions များကို ဘယ်လိုအသုံးပြု၍ စွမ်းဆောင်ရည်များ တိုးချဲ့သလဲ  
- 💬 **စကားပြောသွားလာမှု စီမံခန့်ခွဲမှု**: multi-turn စကားပြောမှုများနှင့် context ကို thread စီမံခန့်ခွဲမှုဖြင့်စီစစ်ခြင်း
- 🔧 **ဖွဲ့စည်းမှု ပုံစံများ**: .NET တွင် agent များ၏ တပ်ဆင်မှုနှင့် စီမံခန့်ခွဲမှုအတွက် အကောင်းဆုံးနည်းလမ်းများ

## 🎯 အဓိကအကြောင်းအရာများ

### Agentic Framework နိယာမများ

- ** ကိုယ်ပိုင် လွတ်လပ်ခွင့်**: agent များသည် .NET AI abstraction များကို အသုံးပြုကာ ကိုယ်တိုင် ဆုံးဖြတ်ချက်ချမှုများပြုလုပ်ခြင်း
- **တုံ့ပြန်မှု**: ပတ်ဝန်းကျင်ပြောင်းလဲမှုများနှင့် အသုံးပြုသူထံမှ inputs များကို တုံ့ပြန်ခြင်း
- **ရှေ့ဆောင်လုပ်ဆောင်မှု**: ရည်မှန်းချက်များနှင့် context အပေါ်မှ အစီအစဉ် ရယူခြင်း
- ** လူမှုအသွင်အပြင်**: စကားပြောခြင်း threads များမှတဆင့် သဘာဝဘာသာစကားဖြင့် ဆက်သွယ်ခြင်း

### နည်းပညာ ကဏ္ဍများ

- **AIAgent**: အဓိက agent စီမံခြင်းနှင့် စကားပြောမှု စီမံခန့်ခွဲမှု (.NET)
- **ကိရိယာ functions များ**: C# method များနှင့် attributes များဖြင့် agent စွမ်းဆောင်ရည်များ တိုးချဲ့ခြင်း
- **Azure OpenAI ပေါင်းစည်းခြင်း**: Azure OpenAI Responses API ဖြင့် ဘာသာစကားမော်ဒယ်များ အသုံးပြုခြင်း
- **လုံခြုံသော ဖွဲ့စည်းမှု**: ပတ်ဝန်းကျင်အခြေခံ endpoint စီမံခန့်ခွဲမှု

## 🔧 နည်းပညာအဖွဲ့အစည်း

### အဓိက နည်းပညာများ

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) ပေါင်းစည်းမှု
- Azure.AI.OpenAI client ပုံစံများ
- DotNetEnv ဖြင့် ပတ်ဝန်းကျင်အခြေခံ ဖွဲ့စည်းမှု

### Agent များ၏ စွမ်းဆောင်ရည်များ

- သဘာဝဘာသာစကား နားလည်မှုနှင့် ဖန်တီးမှု
- C# attribute များဖြင့် function ခေါ်ယူခြင်းနှင့် ကိရိယာအသုံးပြုခြင်း
- စကားပြော_threads များဖြင့် context-သိကောင်းမှုဖြင့် တုံ့ပြန်မှုများ
- dependency injection ပုံစံများဖြင့် တိုးချဲ့နိုင်သော ဖွဲ့စည်းမှု

## 📚 Framework နှိုင်းယှဉ်ခြင်း

ဤဥပမာသည် Microsoft Agent Framework ကို အခြား agentic framework များနှင့် နှိုင်းယှဉ်ပြသပါသည်။

| အင်္ဂါရပ် | Microsoft Agent Framework | အခြား Framework များ |
|---------|-------------------------|------------------|
| **ပေါင်းစည်းမှု** | Microsoft စနစ်စုစည်းမှု | ကွဲပြားသောလိုက်ဖက်မှု |
| **ရိုးရှင်းမှု** | သန့်ရှင်းပြီး ထိုက်သင့်သော API | မကြာခဏ ရှုပ်ထွေးသော စတင်ခြင်း |
| **တိုးချဲ့နိုင်မှု** | ကိရိယာ ပေါင်းစည်းမှု လွယ်ကူမှု | Framework အပေါ် မူတည်သည် |
| **လုပ်ငန်းအသုံးပြုရန် သင့်တော်မှု** | ထုတ်လုပ်မှုအတွက်တည်ဆောက်ထားသည် | Framework အလိုက် ကွဲပြားသည် |

## 🚀 စတင် အသုံးပြုခြင်း

### လိုအပ်ချက်များ

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) သို့မဟုတ် အထက်ပါဗားရှင်း
- Azure OpenAI resource နှင့် မော်ဒယ် တပ်ဆင်မှုပါသော [Azure subscription](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` ဖြင့် ဝင်ရောက်မှု

### လိုအပ်သော ပတ်ဝန်းကျင် များ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# ပြီးရင် AzureCliCredential က token ရဖို့အတွက် စာရင်းဝင်ပါ
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# ထို့နောက် AzureCliCredential သည် token ရယူနိုင်ရန်အတွက် လက်မှတ်ထိုးဝင်ပါ
az login
```

### နမူနာ ကုဒ်

 ဤကုဒ် နမူနာကို အောက်ပါအတိုင်း လုပ်ဆောင်နိုင်ပါသည်။

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

ဒါမှမဟုတ် dotnet CLI အသုံးပြု၍-

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

ပြည့်စုံကုဒ်အတွက် [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) ကိုကြည့်ပါ။

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

## 🎓 အဓိက အတွေ့အကြုံများ

1. **Agent ပုံသဏ္ဍာန်**: Microsoft Agent Framework သည် .NET တွင် AI agent များ တည်ဆောက်ရာတွင် သန့်ရှင်းပြီး အမျိုးအစားလုံခြုံသော နည်းလမ်းတစ်ခုကို ပေးဆောင်သည်
2. **ကိရိယာ ပေါင်းစည်းမှု**: `[Description]` attribute ဖြင့် အလှဆင်ထားသော function များသည် agent အတွက် အသုံးပြုနိုင်သည့် ကိရိယာများဖြစ်လာသည်
3. **စကားပြော အကြောင်းအရာ**: thread စီမံခန့်ခွဲမှုဖြင့် context အပြည့်အစုံနားလည်မှုရှိသော multi-turn စကားပြောမှုများကို ခွင့်ပြုသည်
4. **ဖွဲ့စည်းမှု စီမံခန့်ခွဲမှု**: ပတ်ဝန်းကျင် များနှင့် လုံခြုံသော လက်မှတ် စီမံခန့်ခွဲမှုသည် .NET ၏ အကောင်းဆုံး လမ်းညွှန်ချက်များနှင့် ကိုက်ညီသည်
5. **Azure OpenAI Responses API**: Agent သည် Azure.AI.OpenAI SDK မှတဆင့် Azure OpenAI Responses API ကို အသုံးပြုသည်

## 🔗 နောက်ထပ် အရင်းအမြစ်များ

- [Microsoft Agent Framework စာတမ်းများ](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry တွင် Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->