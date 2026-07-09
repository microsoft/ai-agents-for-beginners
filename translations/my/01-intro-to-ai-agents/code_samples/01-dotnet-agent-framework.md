# 🌍 Microsoft Agent Framework (.NET) ဖြင့် AI ခရီးထွက်အေးဂျင့်

## 📋 အကြောင်းအရာ အနှစ်ချုပ်

ဤဥပမာတွင် Microsoft Agent Framework ကို အသုံးပြု၍ .NET အတွက် ထောက်ပံ့သော အေးဂျင့်တစ်ခုဖြင့် ဉာဏ်ရည်ရှိသော ခရီးစဉ် စီမံခန့်ခွဲရေးအေးဂျင့်ကို ဘယ်လိုတည်ဆောက်နိုင်သည်ကို ပြသထားသည်။ ဤအေးဂျင့်သည် ကမ္ဘာအနှံ့ရှိ ပျော်တဲ႕နေရာများအတွက် ကိုယ်ပိုင် အရက်နှင့် နေ့စဉ်ခရီးစဉ်များကို အလိုအလျောက်ဖန်တီးနိုင်သည်။

### အဓိက အင်္ဂါရပ်များ

- 🎲 **Random Destination Selection**: ခရီးသွားနေရာများကို ရွေးချယ်ပေးသည့် စိတ်ကြိုက်ကိရိယာကို အသုံးပြုသည်
- 🗺️ **Intelligent Trip Planning**: နေ့စဉ်အသေးစိတ်ခရီးစဉ်များ ဖန်တီးပေးသည်
- 🔄 **Real-time Streaming**: ချက်ချင်းနှင့် စီးဆင်းနေဆဲ ပြန်လည်ဖြေကြားမှုများကို ထောက်ပံ့သည်
- 🛠️ **Custom Tool Integration**: အေးဂျင့်၏ မျှော်မှန်းထားသော စွမ်းဆောင်ရည်များကို တိုးချဲ့စေသည်

## 🔧 နည်းပညာဖွဲ့စည်းမှု

### အခြေခံ နည်းပညာများ

- **Microsoft Agent Framework**: AI အေးဂျင့်ဖန်တီးရန်အတွက် နောက်ဆုံးပေါ် .NET ပလက်ဖောင်း
- **Azure OpenAI (Responses API)**: တည်ဆောက်မှုအတွက် Azure OpenAI Responses API ကို သုံးသည်
- **Azure Identity**: `AzureCliCredential` (`az login`) ဖြင့် လုံခြုံစိတ်ချစွာ ဝင်ရောက်မှု
- **Secure Configuration**: ပတ်ဝန်းကျင်အခြေပြု endpoint စီမံခန့်ခွဲမှု

### အဓိကအစိတ်အပိုင်းများ

1. **AIAgent**: စကားပြောပွဲကို ထိန်းချုပ်ပေးသော အဓိက အေးဂျင့်
2. **Custom Tools**: အေးဂျင့်အသုံးပြုနိုင်သော `GetRandomDestination()` လုပ်ဆောင်ချက်
3. **Responses Client**: Azure OpenAI Responses နည်းပညာအပေါ် အခြေခံထားသော စကားပြော အင်တာဖေ့စ်
4. **Streaming Support**: အချိန်နောက်ကျမှုမရှိသော ဖြေကြားမှုများ ဖန်တီးနိုင်ခြင်း

### ပေါင်းစပ်ခြင်း ပုံစံ

```mermaid
graph LR
    A[အသုံးပြုသူ တောင်းဆိုချက်] --> B[AI ကိုယ်စားလှယ်]
    B --> C[Azure OpenAI (အဖြေ API)]
    B --> D[GetRandomDestination အရေးပစ္စည်း]
    C --> E[ခရီးသွား အစီအစဉ်]
    D --> E
```

## 🚀 စတင်အသုံးပြုခြင်း

### လိုအပ်ချက်များ

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) သို့မဟုတ် အထက်တန်း
- Azure OpenAI အရင်းအမြစ်နှင့် မော်ဒယ်တပ်ဆင်ချက်ပါရှိသည့် [Azure subscription](https://azure.microsoft.com/free/)
- `az login` ဖြင့် ဝင်ရောက်ရန် လိုသည့် [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

### လိုအပ်သော ပတ်ဝန်းကျင် အပြောင်းအလဲများ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# ဒါမှတဆင့် AzureCliCredential သည် token ရယူနိုင်ရန် သင်အကောင့်တစ်ခုဖြင့် သွင်းထားရမည်။
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# AzureCliCredential သည် token ကိုရရှိနိုင်ရန် ရောင့်ရန်၀င်ပါ။
az login
```

### ဥပမာ ကုဒ်

ဤကုဒ်ဥပမာကို လည်ပတ်ရန်

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

ဒါမှမဟုတ် dotnet CLI ကို အသုံးပြု၍:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

ပြည့်စုံသောကုဒ်အတွက် [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) ကိုကြည့်ပါ။

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

## 🎓 အဓိကသိရှိရန် အချက်များ

1. **Agent Architecture**: Microsoft Agent Framework သည် .NET တွင် AI အေးဂျင့်တည်ဆောက်ရန် သန့်ရှင်း၍ type-safe နည်းဖြစ်သည်
2. **Tool Integration**: `[Description]` attribute ဖြင့် အမှတ်တံဆိပ်ဆွဲထားသည့် လုပ်ဆောင်ချက်များသည် အေးဂျင့်အား အသုံးပြုနိုင်သော ကိရိယာများ ဖြစ်စေသည်
3. **Configuration Management**: ပတ်ဝန်းကျင်အပြောင်းအလဲများနှင့် လုံခြုံသော မှတ်ပုံတင်စနစ်သည် .NET ၏ အကောင်းဆုံး နည်းလမ်းများကို လိုက်နာသည်
4. **Azure OpenAI Responses API**: အေးဂျင့်သည် Azure.AI.OpenAI SDK မှတဆင့် Azure OpenAI Responses API ကို အသုံးပြုသည်

## 🔗 ထပ်မံရရှိနိုင်သော အရင်းအမြစ်များ

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI in Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->