# 🔍 Microsoft Agent Framework ကို ရှာဖွေတွေ့ရှိခြင်း – အခြေခံ Agent (.NET)

## 📋 သင်ယူရန် ရည်ရွယ်ချက်များ

ဤဥပမာသည် Microsoft Agent Framework ၏ အခြေခံ แนวคิดများကို .NET တွင် အခြေခံ agent တည်ဆောက်ခြင်းမှတဆင့် ရှာဖွေသုံးသပ်ပေးပါသည်။ သင်သည် အဓိက agent နည်းဗျူဟာများကို လေ့လာပြီး C# နှင့် .NET ပတ်ဝန်းကျင်ကို အသုံးပြု၍ အတွင်းနက်ပြတ်ပြာသော agent များ အဖြေရှာပုံကို နားလည်မိပါလိမ့်မည်။

### သင်ရှာဖွေတွေ့ရှိမည့်အရာများ

- 🏗️ **Agent ပုံသဏ္ဍာန်**: .NET တွင် AI agent များ၏ အခြေခံဖွဲ့စည်းပုံနားလည်ခြင်း
- 🛠️ **ကိရိယာ ပေါင်းစပ်ခြင်း**: ချဲ့ထွင်နိုင်စွမ်းများအတွက် agent များသည် ပြင်ပ function များကို မည်သို့အသုံးပြုသည်
- 💬 **စကားပြောစီးဆင်းမှု**: Multi-turn စကားပြောများနှင့် context ကို thread စီမံခန့်ခွဲမှုဖြင့် စီမံခြင်း
- 🔧 **ဖွဲ့စည်းပုံ စနစ်များ**: .NET တွင် agent တပ်ဆင်ခြင်းနှင့် စီမံခန့်ခွဲမှုအတွက် အကောင်းဆုံး လေ့လာမှုများ

## 🎯 ပါဝင်သော အဓိကအမြင်များ

### Agentic Framework ၏ သဘောတရားများ

- **အလိုအလျောက် မူးမြတ်မှု**: .NET AI abstraction များအသုံးပြု၍ agent များသည် လွတ်လပ်စွာ ဆုံးဖြတ်ချက်ချခြင်း
- **တုံ့ပြန်မှု**: ပတ်ဝန်းကျင်ပြောင်းလဲမှုများနှင့် အသုံးပြုသူ input များကို တုံ့ပြန်ခြင်း
- **ကြိုတင်လုပ်ဆောင်မှု**: ရည်ရွယ်ချက်များနှင့် context အပေါ် အခြေခံပြီး initiative ယူခြင်း
- **လူမှုဆက်ဆံရေးစွမ်းအား**: သဘာဝဘာသာစကားဖြင့် စကားပြောလမ်းကြောင်းများသုံးပြီး ဆက်ဆံခြင်း

### နည်းပညာဆိုင်ရာ အစိတ်အပိုင်းများ

- **AIAgent**: အဓိက agent စီမံခန့်ခွဲမှုနှင့် စကားပြောစီမံခြင်း (.NET)
- **ကိရိယာ function များ**: C# method များနှင့် attribute များဖြင့် agent ၏ စွမ်းဆောင်ရည် ချဲ့ထွင်ခြင်း
- **Azure OpenAI ပေါင်းစပ်မှု**: Azure OpenAI Responses API မှတဆင့် ဘာသာစကား မော်ဒယ်များကို လက်ခံအသုံးပြုခြင်း
- **လုံခြုံစိတ်ချရသော ဖွဲ့စည်းခြင်း**: ပတ်ဝန်းကျင်အခြေခံ endpoint စီမံခန့်ခွဲမှု

## 🔧 နည်းပညာ Stack

### အဓိက နည်းပညာများ

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) ပေါင်းစပ်မှု
- Azure.AI.OpenAI client နည်းဗျူဟာများ
- DotNetEnv ဖြင့် ပတ်ဝန်းကျင်အခြေခံ ဖွဲ့စည်းမှု

### Agent ၏ စွမ်းရည်များ

- သဘာဝဘာသာစကား နားလည်မှုနှင့် ထုတ်လုပ်မှု
- C# attribute များနှင့် function call နှင့် ကိရိယာအသုံးပြုခြင်း
- စကားပြောအစည်းအဝေးများနှင့် context အသိပညာရှိတုံ့ပြန်မှု
- Dependency injection နည်းဗျူဟာများဖြင့် ချဲ့ထွင်နိုင်သော ဖွဲ့စည်းပုံ

## 📚 Framework နှိုင်းယှဉ်ခြင်း

ဤဥပမာသည် Microsoft Agent Framework နှင့် အခြား agentic frameworks များကို နှိုင်းယှဉ်ဖော်ပြပေးပါသည်။

| Feature | Microsoft Agent Framework | အခြား Framework များ |
|---------|-------------------------|------------------|
| **ပေါင်းစပ်မှု** | Microsoft ပတ်ဝန်းကျင်လိုက်ဖက်မှု native | မတူညီသည့်လိုက်ဖက်မှုများ |
| **ရိုးရှင်းမှု** | သန့်ရှင်းပြီး လွယ်ကူသည့် API | မကြာခဏ ပြင်ဆင်ရန်ရှုပ်ထွေးမှုများ |
| **ချဲ့ထွင်နိုင်မှု** | ကိရိယာများလွယ်ကူစွာ ပေါင်းစပ်နိုင်ခြင်း | Framework အပေါ်တွင် အခြေခံသည် |
| **လုပ်ငန်းအသုံးပြုမှု** | ထုတ်လုပ်မှုအတွက် တည်ဆောက်ထားသည် | Framework အလိုက် မတူကွဲပြားမှုရှိသည် |

## 🚀 စတင် အသုံးပြုခြင်း

### လိုအပ်ချက်များ

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) သို့မဟုတ် အထက်ပိုင်း
- [Azure subscription](https://azure.microsoft.com/free/) တစ်ခု ဂရုပြုထားပြီး Azure OpenAI resource နှင့် မော်ဒယ် တပ်ဆင်မှုပါရှိရန်
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` ဖြင့် စာရင်းဝင်ရန်

### လိုအပ်သော ပတ်ဝန်းကျင် မူဝါဒများ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# ပြီးတော့ AzureCliCredential သည် token တစ်ခုပြုလို့ရအောင် လက်မှတ်လက်မှတ်ဝင်ပါ
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# ထို့နောက် AzureCliCredential သည် token ကို ရနိုင်ရန် အကောင့်ဝင်ပါ။
az login
```

### နမူနာ ကုဒ်

ကုဒ် ဥပမာကို လည်ပတ်ရန်

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

ဒါမှမဟုတ် dotnet CLI အသုံးပြု၍

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

ပြည့်စုံသောကုဒ်ကို [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) တွင် ကြည့်ရှုနိုင်သည်။

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4.1-mini";

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

1. **Agent ပုံသဏ္ဍာန်**: Microsoft Agent Framework သည် .NET တွင် AI agent များ တည်ဆောက်ရန် ရိုးရှင်းပြီး type-safe နည်းလမ်းပေးသည်
2. **ကိရိယာ ပေါင်းစပ်ခြင်း**: `[Description]` attribute ဖြင့်ကပ်ထားသော function များကို agent ၏ အသုံးပြုနိုင်သော ကိရိယာများအဖြစ် သတ်မှတ်ပေးသည်
3. **စကားပြော Context**: session စီမံခန့်ခွဲမှုသည် multi-turn စကားပြောများအတွက် context အသိပညာနှင့်အတူ ခွင့်ပြုသည်
4. **ဖွဲ့စည်းမှု စီမံခန့်ခွဲမှု**: ပတ်ဝန်းကျင် variable များနှင့် လုံခြုံသော credential ကို .NET ၏ အကောင်းဆုံး လေ့ကျင့်မှုများနှင့်လိုက်နာသည်
5. **Azure OpenAI Responses API**: agent သည် Azure.AI.OpenAI SDK မှတဆင့် Azure OpenAI Responses API ကို အသုံးပြုသည်

## 🔗 ထပ်မံ အသုံးဝင် မူရင်းများ

- [Microsoft Agent Framework စာရွက်စာတမ်းများ](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry တွင် Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->