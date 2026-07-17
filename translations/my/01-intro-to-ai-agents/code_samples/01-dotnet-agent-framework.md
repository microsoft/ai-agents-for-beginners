# 🌍 Microsoft Agent Framework (.NET) ဖြင့် AI ခရီးသွားအေဂျင့်

## 📋 ဇာတ်ကောင်အကြောင်းအကျဉ်း

ဤဥရောပမှာ Microsoft Agent Framework ကို အသုံးပြု၍ သိပ္ပံပညာရှင် ခရီးစဉ်အစီအစဉ်ရေးဆွဲရေး အေဂျင့်တစ်ခုကို ဘယ်လိုတည်ဆောက်ရမည်ကို ချပြသည်။ အဲဒီ အေဂျင့်က ကမ္ဘာတစ်ဝှမ်းရှိ အကြောင်းမပြောပဲ ခရီးစဉ်တစ်နေ့စာ အစီအစဉ်ကို ကိုယ်ပိုင်အလိုက် လက်ထောက်ဖန်တီးပေးနိုင်ပါသည်။

### အဓိကထူးခြားချက်များ

- 🎲 **ကျပန်းခရီးစဉ်ရွေးချယ်မှု**: အထူးကိရိယာဖြင့် အပန်းဖြေစရာနေရာရွေးချယ်ခြင်း
- 🗺️ **သိပ္ပံပညာရှင် ခရီးစဉ်အစီအစဉ်ရေးဆွဲမှု**: နေ့စဉ်အစီအစဉ်အသေးစိတ် ဖန်တီးခြင်း
- 🔄 **အချိန်နှင့်တပြေးညီ စတီးမင်ထုတ်လွှင့်မှု**: ချက်ချင်း ဖြေကြားမှုနှင့် စတီးမင်ဖြေကြားမှု ပံ့ပိုးမှု
- 🛠️ **စိတ်ကြိုက်ကိရိယာ ပေါင်းစည်းမှု**: အေဂျင့်စွမ်းရည်များချဲ့ထွင်ပုံ ပြသခြင်း

## 🔧 နည်းပညာဆိုင်ရာ ဖွဲ့စည်းမှု

### အခြေခံနည်းပညာများ

- **Microsoft Agent Framework**: AI အေဂျင့် ဖွံ့ဖြိုးရေးအတွက် နောက်ဆုံး .NET လက်တွေ့ကျဆုံးမှု
- **Azure OpenAI (Responses API)**: မော်ဒယ်ဖော်ထုတ်မှုအတွက် Azure OpenAI Responses API ကို အသုံးပြုသည်
- **Azure Identity**: `AzureCliCredential` (`az login`) ဖြင့် လုံခြုံစိတ်ချရသော စာရင်းဝင်ခြင်း
- **လုံခြုံစိတ်ချရသော ဖန်တီးမှု**: ပတ်ဝန်းကျင်အလိုက် endpoint ကို စီမံခန့်ခွဲမှု

### အဓိကအစိတ်အပိုင်းများ

1. **AIAgent**: စကားသွား-လာမှုစီမံခန့်ခွဲသော မူလအေဂျင့်
2. **စိတ်ကြိုက်ကိရိယာများ**: အေဂျင့်အတွက် `GetRandomDestination()` ဖန်တီးထားသောလုပ်ဆောင်ချက်
3. **Responses Client**: Azure OpenAI Responses အခြေခံ စကားလုံးချင်း အင်တာဖေ့စ
4. **စတီးမင်ထောက်ပံ့မှု**: အချိန်နှင့်တပြေးညီ ဖြေကြားမှုလုပ်ဆောင်မှုများ

### ပေါင်းစည်းမှုပုံစံ

```mermaid
graph LR
    A[အသုံးပြုသူ တောင်းဆိုချက်] --> B[AI ကိုယ်စားလှယ်]
    B --> C[Azure OpenAI (တုံ့ပြန်ချက် API)]
    B --> D[ရွေးချယ်ရန် ဦးတည်ချက်ကိရိယာ]
    C --> E[ခရီးသွားအစီအစဉ်]
    D --> E
```

## 🚀 စတင်အသုံးပြုခြင်း

### မလိုအပ်မီက

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) သို့မဟုတ် ထိုထက်မြင့်နည်းပညာ
- Azure OpenAI အရင်းအမြစ်နှင့် မော်ဒယ်တပ်ဆင်မှုပါသော [Azure subscription](https://azure.microsoft.com/free/)
- `az login` ဖြင့် အကောင့်ဝင်ရန် [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

### လိုအပ်သော ပတ်ဝန်းကျင် မပြောင်းလဲ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# ဒါနဲ့ AzureCliCredential က token ရယူနိုင်အောင် အကောင့်ဝင်ပါ
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# ထို့နောက် AzureCliCredential သည် တိုကင်တစ်ခုရရှိနိုင်ရန် အကောင့်ဝင်ပါ
az login
```

### နမူနာကုဒ်

ဥပမာကုဒ်ကို အသုံးပြုရန်

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

ဒါမှမဟုတ် dotnet CLI ကို အသုံးပြုပါ:

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4.1-mini";

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

## 🎓 အဓိကယူဆချက်များ

1. **အေဂျင့် ဖွဲ့စည်းပုံ**: Microsoft Agent Framework သည် .NET တွင် AI အေဂျင့်များ တည်ဆောက်ရန် သန့်ရှင်း၍ type-safe နည်းလမ်းဖြစ်သည်
2. **ကိရိယာ ပေါင်းစည်းမှု**: `[Description]` အင်္ဂါရပ်ဖြင့် ဖော်ပြထားသောလုပ်ဆောင်ချက်များ၊ အေဂျင့်အတွက် အသုံးပြုနိုင်သော ကိရိယာများဖြစ်သည်
3. **ဖန်တီးမှု စီမံခန့်ခွဲမှု**: ပတ်ဝန်းကျင်မပြောင်းလဲများနှင့် လုံခြုံသော အတည်ပြုချက်စီမံခန့်ခွဲမှုသည် .NET ၏ အကောင်းဆုံးလေ့လာမှုများနဲ့ ကိုက်ညီသည်
4. **Azure OpenAI Responses API**: အေဂျင့်သည် Azure AI OpenAI SDK မှတဆင့် Azure OpenAI Responses API ကို အသုံးပြုသည်

## 🔗 ထပ်ဆင့် အရင်းအမြစ်များ

- [Microsoft Agent Framework အသုံးပြုမှု လမ်းညွှန်](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry တွင် Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->