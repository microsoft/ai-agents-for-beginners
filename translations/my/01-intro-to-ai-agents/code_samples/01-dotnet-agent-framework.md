# 🌍 Microsoft Agent Framework (.NET) ဖြင့် AI ခရီးသွား ကိုယ်စားလှယ်

## 📋 ကိစ္စအချက်အလက် အနှစ်ချုပ်

ဤဥပမာသည် Microsoft Agent Framework ကို အသုံးပြု၍ အခွင့်အလမ်းရရှိသည့် ခရီးစဉ် စီစဉ်တင်ပြခွင့်ရ ကိုယ်စားလှယ် တစ်ဦးကို ဘယ်လို တည်ဆောက်ရမည်ကို ပြသသည်။ ၎င်းကိုကမ္ဘာတဝန်းရှိ အစီအစဉ်မဲ့ ခရီးသွားရောက်ရာနေရာများအတွက် ကိုယ်ပိုင် နေ့စဉ်ခရီးစဉ်များကို အလိုအလျောက် ဖန်တီးပေးနိုင်သည်။

### အဓိက စွမ်းရည်များ

- 🎲 **အစီအစဉ်မဲ့ သွားရောက်မည့်နေရာ ရွေးချယ်မှု**: အထူးသီးသန့် ကိရိယာမှ တစ်ဆင့် နေရာကောင်းများကို ရွေးချယ်ခြင်း
- 🗺️ **တောက်ပသော ခရီးစဉ် စီမံခန့်ခွဲမှု**: နေ့စဉ် အကြောင်းအရာများ အသေးစိတ်ဖန်တီးခြင်း
- 🔄 **Real-time Streaming**: ချက်ချင်း နှင့် စီးဆင်းမှုဖြင့် တုံ့ပြန်မှုများပံ့ပိုးခြင်း
- 🛠️ **စိတ်ကြိုက် ကိရိယာ ပေါင်းစည်းမှု**: ကိုယ်စားလှယ်စွမ်းရည်များ တိုးချဲ့ရခြင်းကို ပြသခြင်း

## 🔧 နည်းပညာဖွဲ့စည်းမှု

### အဓိက နည်းပညာများ

- **Microsoft Agent Framework**: AI ကိုယ်စားလှယ် ဖွံ့ဖြိုးတိုးတက်ရေးအတွက် နောက်ဆုံးထွက် .NET အကောင်အထည်ဖော်မှု
- **Azure OpenAI (Responses API)**: မော်ဒယ် ဇာတ်ဆောင်မှုအတွက် Azure OpenAI Responses API ကို အသုံးပြုသည်
- **Azure Identity**: `AzureCliCredential` (`az login`) ဖြင့် လုံခြုံစွာ ဝင်ရောက်ခြင်း
- **လုံခြုံမှု ပြုပြင်ခြင်း**: ပတ်ဝန်းကျင်အခြေပြု အဆုံးအဖြတ် ထိန်းချုပ်မှု

### အဓိက အစိတ်အပိုင်းများ

1. **AIAgent**: စကားပြော ပွားလည်မှု ကိုင်တွယ်သည့် အဓိက ကိုယ်စားလှယ်
2. **စိတ်ကြိုက် ကိရိယာများ**: ကိုယ်စားလှယ် အသုံးပြုနိုင်သော `GetRandomDestination()` အလုပ်လုပ်ပုံ
3. **Responses Client**: Azure OpenAI Responses အခြေခံ စကားပြောစနစ်
4. **စီးဆင်းမှု ပံ့ပိုးမှု**:အချိန်နဲ့တပြိုင်နက် တုံ့ပြန်မှု ထုတ်ပေးမှု စွမ်းဆောင်ရည်

### ပေါင်းစည်းမှု ပုံစံ

```mermaid
graph LR
    A[အသုံးပြုသူ တောင်းဆိုချက်] --> B[AI ကိုယ်စားလှယ်]
    B --> C[Azure OpenAI (တုံ့ပြန်ချက် API)]
    B --> D[GetRandomDestination ကိရိယာ]
    C --> E[ခရီးသွားအစီအစဉ်]
    D --> E
```

## 🚀 စတင်အသုံးပြုခြင်း

### လိုအပ်ချက်များ

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) သို့မဟုတ် ထို့အထက်
- Azure OpenAI အရင်းအမြစ် နှင့် မော်ဒယ်တပ်ဆင်ထားသည့် [Azure subscription](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` ဖြင့် ဝင်ရောက်ခြင်း

### လိုအပ်သော ပတ်ဝန်းကျင် မထည့်သွင်းချက်များ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# ပြီးမှ AzureCliCredential သည် token ရနိုင်ရန်အတွက် စာရင်းသွင်းပါ
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# ထို့နောက် AzureCliCredential သည် token ရနိုင်ရန် စာရင်းဝင်ပါ။
az login
```

### နမူနာ ကုဒ်

ဥပမာ ကုဒ်ကို run ဖို့,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

ဒါမှမဟုတ် dotnet CLI ကို အသုံးပြု၍

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

ပြည့်စုံသောကုဒ်အတွက် [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) ကို ကြည့်ပါ။

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

## 🎓 အဓိက သင်ခန်းစာများ

1. **ကိုယ်စားလှယ် ဖွဲ့စည်းမှု**: Microsoft Agent Framework သည် .NET တွင် AI ကိုယ်စားလှယ်တွေ ဖန်တီးရာတွင် သန့်ရှင်းပြီး type-safe ဖြစ်အောင် နည်းလမ်းပေးသည်။
2. **ကိရိယာ ပေါင်းစည်းမှု**: `[Description]` attribute ဖြင့် ဖောင်ရှင်များသည် ကိုယ်စားလှယ်အတွက် အသုံးပြုနိုင်သော ကိရိယာများဟု ဖြစ်လာသည်။
3. **ပြုပြင်ထိန်းသိမ်းမှု**: ပတ်ဝန်းကျင် မထည့်သွင်းချက်များနှင့် လုံခြုံစိတ်ချစွာ အတည်ပြုမှုပြုခြင်းသည် .NET၏ အကောင်းဆုံး လေ့လာမှုများနှင့် ကိုက်ညီသည်။
4. **Azure OpenAI Responses API**: ကိုယ်စားလှယ်သည် Azure.AI.OpenAI SDK ကနေ Azure OpenAI Responses API ကို အသုံးပြုသည်။

## 🔗 ထပ်မံ ရရှိနိုင်သော ရင်းမြစ်များ

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry တွင် Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->