# 🌍 Microsoft Agent Framework (.NET) ഉപയോഗിച്ച് AI യാത്രാ ഏജന്റ്

## 📋 രംഗസംവരണം

.NET-നുമുള്ള Microsoft Agent Framework ഉപയോഗിച്ച് ബുദ്ധിമുട്ടുള്ള യാത്രാ പദ്ധതിയിടൽ ഏജന്റ് എങ്ങനെ നിർമ്മിക്കാമെന്ന് ഈ ഉദാഹരണം കാണിക്കുന്നു. ഏജന്റ് ലോകമെമ്പാടുമുള്ള യാദൃച്ഛിക ലക്ഷ്യസ്ഥാനങ്ങൾക്കായി വ്യക്തിഗത ദിവസ യാത്രാ പരിപാടികൾ സ്വയം സൃഷ്ടിക്കാൻ കഴിയും.

### പ്രധാന കഴിവുകൾ:

- 🎲 **യാദൃച്ഛിക ലക്ഷ്യസ്ഥല തെരഞ്ഞെടുപ്പ്**: അവധി സ്ഥാനങ്ങൾ തിരഞ്ഞെടുക്കാൻ ഒരു കസ്റ്റം ടൂൾ ഉപയോഗിക്കുന്നു
- 🗺️ **ബുദ്ധിമുട്ടുള്ള യാത്രാ പദ്ധതീകരണം**: ദിവസവും വിശദമായ യാത്രാ പരിപാടികൾ സൃഷ്ടിക്കുന്നു
- 🔄 **ക്ഷണിക സ്ട്രീമിംഗ്**: ഉടൻ ലഭിക്കുന്നതും സ്ട്രീമിംഗ് മറുപടികളും പിന്തുണയ്ക്കുന്നു
- 🛠️ **കസ്റ്റം ടൂൾ ഇന്റഗ്രേഷൻ**: ഏജന്റ് കഴിവുകൾ വികസിപ്പിക്കുന്ന വിധം കാണിക്കുന്നു

## 🔧 സാങ്കേതിക രൂപരേഖ

### പ്രാഥമിക സാങ്കേതികവിദ്യകൾ

- **Microsoft Agent Framework**: .NET AI ഏജന്റ് വികസനത്തിനുള്ള ഏറ്റവും പുതിയ നിർവഹണം
- **Azure OpenAI (Responses API)**: മോഡൽ ഫലം ലഭിക്കാനായി Azure OpenAI Responses API-വിനെ ഉപയോഗിക്കുന്നു
- **Azure Identity**: `AzureCliCredential` (`az login`) വഴി സുരക്ഷിത സൈൻ ഇൻ
- **സുരക്ഷിത ക്രമീകരണം**: പരിസ്ഥിതിയനുസരിച്ച് എന്റ്പോയിന്റ് മാനേജ്മെന്റ്

### പ്രധാന ഘടകങ്ങൾ

1. **AIAgent**: സംവാദ പ്രവാഹം കൈകാര്യം ചെയ്യുന്ന പ്രധാന ഏജന്റ് ഓർക്കസ്‌ട്രേറ്റർ
2. **കസ്റ്റം ടൂളുകൾ**: ഏജന്റിനും ലഭ്യമായ `GetRandomDestination()` ഫംഗ്ഷൻ
3. **റെസ്പോൺസസ് ക്ലയന്റ്**: Azure OpenAI Responses അടിസ്ഥാനമാക്കിയുള്ള സംവാദ ഇന്റർഫേസ്
4. **സ്ട്രീമിംഗ് പിന്തുണ**: യാഥാർത്ഥ്യ സമയമുളള മറുപടി സൃഷ്ടി കഴിവുകൾ

### ഇന്റഗ്രേഷൻ മാതൃക

```mermaid
graph LR
    A[ഉപയോക്തൃ അഭ്യർത്ഥന] --> B[AI ഏജന്റ്]
    B --> C[അസ്യൂർ ഓപ്പൺഎഐ (പ്രതികരണ എപിഐ)]
    B --> D[GetRandomDestination ടൂൾ]
    C --> E[യാത്രാ വിവരണം]
    D --> E
```

## 🚀 തുടങ്ങാം

### മുൻവൈദ്യങ്ങൾ

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) അല്ലെങ്കിൽ അതിന് മുകളിൽ
- Azure OpenAI റിസോഴ്‌സ് ഉണ്ടാകുന്ന ഒരു [Azure സബ്‌സ്‌ക്രിപ്ഷൻ](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` ഉപയോഗിച്ച് സൈൻ ഇൻ ചെയ്യുക

### ആവശ്യമായ പരിസ്ഥിതി മാറ്റങ്ങൾ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# AzureCliCredential ഒരു ടോക്കൺ നേടാൻ പിന്നീട് സൈൻ ഇൻ ചെയ്യുക
az login
```

```powershell
# پاورShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# തുടർന്ന് AzureCliCredential ഒരു ടോക്കൺ നേടാൻ സൈൻ ഇൻ ചെയ്യുക
az login
```

### സാമ്പിൾ കോഡ്

കോഡ് ഉദാഹരണം ആരംഭിക്കാൻ,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

അല്ലെങ്കിൽ dotnet CLI ഉപയോഗിച്ച്:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

പൂർണ കോഡിനായി [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) കാണുക.

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

## 🎓 പ്രധാന പഠനങ്ങൾ

1. **ഏജന്റ് രൂപകൽപ്പന**: Microsoft Agent Framework .NET-ൽ AI ഏജന്റുകളെ നിർമ്മിക്കാൻ ശുചിത്വമുള്ള, ടൈപ്പ്-സുരക്ഷിതമായ സമീപനം പകർന്നുകളയുന്നു
2. **ടൂൾ ഇന്റഗ്രേഷൻ**: `[Description]` ആട്രിബ്യൂട്ടുകൾ ലഭ്യമാക്കിയ ഫംഗ്ഷനുകൾ ഏജന്റിന് ടൂൾ ആയി മാറുന്നു
3. **ക്രമീകരണ മാനേജ്മെന്റ്**: പരിസ്ഥിതി മാറ്റങ്ങളും സുരക്ഷിത ക്രെഡൻഷ്യൽ കൈകാര്യം ചെയ്യലും .NET മികച്ച രീതികൾ പിന്തുടരുന്നു
4. **Azure OpenAI Responses API**: ഏജന്റ് Azure.AI.OpenAI SDK വഴി Azure OpenAI Responses API ഉപയോഗിക്കുന്നു

## 🔗 അധിക വിഭവങ്ങൾ

- [Microsoft Agent Framework ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry-യിൽ Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->