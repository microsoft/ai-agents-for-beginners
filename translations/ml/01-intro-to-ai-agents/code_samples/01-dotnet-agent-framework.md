# 🌍 Microsoft Agent Framework (.NET) ഉപയോഗിച്ച് AI ട്ട്രാവൽ ഏജന്റ്

## 📋 സിനാറിയോ അവലോകനം

.NET യിലെ Microsoft Agent Framework ഉപയോഗിച്ച് ബുദ്ധിമുട്ടുള്ള ട്രാവൽ പ്ലാനിംഗ് ഏജന്റ് എങ്ങനെ നിർമ്മിക്കാമെന്ന് ഈ ഉദാഹരണം കാട്ടുന്നു. ഏജന്റ് ലോകമെമ്പാടുമുള്ള യാദൃച്ഛിക ലക്ഷ്യസ്ഥാനങ്ങൾക്കായി വ്യക്തിഗത ദിനസഞ്ചാര യാത്രാപ്രവൃത്തി സ്വയം സൃഷ്ടിക്കാം.

### മുഖ്യ കഴിവുകൾ:

- 🎲 **യാദൃശ്ചിക ലക്ഷ്യസ്ഥാനം തിരഞ്ഞെടുപ്പ്**: അവധി സ്ഥലങ്ങൾ തിരഞ്ഞെടുക്കാൻ ഒരുപാട് ഉപകരണം ഉപയോഗിക്കുന്നു
- 🗺️ **ബുദ്ധിമുട്ടുള്ള യാത്രാ പദ്ധതീകരണം**: ദിവസേന വിശദമായ യാത്രാപ్రവൃത്തി സൃഷ്ടിക്കുന്നു
- 🔄 **റെൽ-ടൈം സ്ട്രീമിങ്**: നടപ്പിലാക്കലും സ്ട്രീമിംഗ് പ്രതികരണവും പിന്തുണയ്ക്കുന്നു
- 🛠️ **രൂപകൽപന ഉപകരണ സംയോജനം**: ഏജന്റിന്റെ കഴിവുകൾ എങ്ങനെ വികസിപ്പിക്കാം കാണിക്കുന്നു

## 🔧 സാങ്കേതിക ശില്പശാല

### മുഖ്യ സാങ്കേതികവിദ്യകൾ

- **Microsoft Agent Framework**: AI ഏജന്റ് വികസനത്തിനായി ഏറ്റവും പുതിയ .NET നടപ്പാക്കൽ
- **Azure OpenAI (Responses API)**: മോഡൽ പ്രവചനത്തിന് Azure OpenAI Responses API ഉപയോഗിക്കുന്നു
- **Azure Identity**: `AzureCliCredential` ഉപയോഗിച്ച് സുരക്ഷിതമായ സൈൻ ഇൻ (`az login`)
- **സുരക്ഷിത കോൺഫിഗറേഷൻ**: പരിസ്ഥിതി അടിസ്ഥാനമാക്കിയ എൻഡ്പോയിന്റ് മാനേജ്മെന്റ്

### മുഖ്യ ഘടകങ്ങൾ

1. **AIAgent**: സംവാദ പ്രവാഹം കൈകാര്യം ചെയ്യുന്ന പ്രധാന ഏജന്റ് ഓർക്കസ്‌ട്രേറ്റർ
2. **രൂപകൽപന ഉപകരണങ്ങൾ**: ഏജന്റിന് ലഭ്യമായ `GetRandomDestination()` ഫങ്ഷൻ
3. **റസ്പോൺസസ് ക്ലയന്റ്**: Azure OpenAI Responses അടിസ്ഥാനത്തിലുള്ള സംവാദ ഇന്റർഫേസ്
4. **സ്ട്രീമിംഗ് പിന്തുണ**: വാസ്തവകാല പ്രതികരണ സൃഷ്ടി കഴിവുകൾ

### സംയോജനം മാതൃക

```mermaid
graph LR
    A[ഉപഭോക്തൃ അഭ്യർത്ഥന] --> B[AI ഏജന്റ്]
    B --> C[അസ്യൂർ ഓപ്പൺഎഐ (പ്രത്യുത്തരങ്ങൾ API)]
    B --> D[GetRandomDestination ടൂൾ]
    C --> E[യാത്രാപദ്ധതി]
    D --> E
```

## 🚀 ആരംഭിക്കൽ

### മുൻവേലകൾ

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) അല്ലെങ്കിൽ ഉയർന്നത്
- Azure OpenAI വിഭവവും മോഡൽ വിന്യാസവും ഉള്ള [Azure സബ്സ്ക്രിപ്ഷൻ](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` ഉപയോഗിച്ച് സൈൻ ഇൻ ചെയ്യുക

### ആവശ്യമായ പരിസ്ഥിതി ചാരങ്ങൾ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# പിന്നീട് സൈൻ ഇൻ ചെയ്യുക, അതിനാൽ AzureCliCredential ടോക്കൺ ലഭിക്കും
az login
```

```powershell
# പവർഷെൽ
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# പിന്നീട് സൈൻ ഇൻ ചെയ്യുക, അങ്ങനെ AzureCliCredential ടോക്കൺ കിട്ടാൻ കഴിയും
az login
```

### സാമ്പിൾ കോഡ്

കോഡ് ഉദാഹരണം പ്രവർത്തിപ്പിക്കാൻ,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

അല്ലെങ്കിൽ dotnet CLI ഉപയോഗിച്ച്:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

സമ്പൂർണ്ണ കോഡിനായി [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) കാണുക.

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

## 🎓 പ്രധാന പഠിപ്പുകൾ

1. **ഏജന്റ് ശില്പശാല**: Microsoft Agent Framework AI ഏജന്റുകൾ .NET ൽ നിർമ്മിക്കാൻ ശുദ്ധവും ടൈപ്പ്-സേഫും ആയ സമീപനം നൽകുന്നു
2. **ഉപകരണ സംയോജനം**: `[Description]` ഗുണഭാഗങ്ങൾ അലങ്കരിച്ച ഫങ്ക്ഷനുകൾ ഏജന്റിനുള്ള ഉപകരണങ്ങളായി മാറുന്നു
3. **കോൺഫിഗറേഷൻ മാനേജ്മെന്റ്**: പരിസ്ഥിതി ചാരങ്ങളും സുരക്ഷित ക്രെഡൻഷ്യൽ കൈകാര്യം ചെയ്യലും .NET മികച്ച മാർഗ്ഗനിർദ്ദേശങ്ങൾ പാലിക്കുന്നു
4. **Azure OpenAI Responses API**: ഏജന്റ് Azure.AI.OpenAI SDK വഴി Azure OpenAI Responses API ഉപയോഗിക്കുന്നു

## 🔗 അധിക ഉറവിടങ്ങൾ

- [Microsoft Agent Framework ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry ലെ Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->