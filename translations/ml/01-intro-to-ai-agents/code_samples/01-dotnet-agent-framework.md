# 🌍 Microsoft Agent Framework (.NET) ഉപയോഗിച്ച് AI യാത്രാ ഏജന്റ്

## 📋 സീനാരിയോ അവലോകനം

.NET-നായി Microsoft Agent Framework ഉപയോഗിച്ച് ബുദ്ധിമുട്ടുള്ള ഒരു യാത്രാ പദ്ധതി ഏജന്റ് എങ്ങനെ നിർമ്മിക്കാമെന്ന് ഈ ഉദാഹരണം കാണിക്കുന്നു. ഏജന്റ് ലോകത്തിന്റെ ഏതു ഭാഗത്തിലായാലും വ്യക്തിഗതമായി ഉദ്ദേശിച്ച ദിവസ യാത്രാ പരിപാടികൾ സ്വയം സൃഷ്ടിക്കുമെന്ന് ഈ ഉദാഹരണം പ്രദർശിപ്പിക്കുന്നു.

### പ്രധാനം കഴിവുകൾ:

- 🎲 **ഏകാന്ത ഗമനം തെരഞ്ഞെടുക്കൽ**: അവധി സ്ഥലങ്ങൾ തിരഞ്ഞെടുക്കാൻ ഫലപ്രദമായ ഒരു കസ്റ്റം ഉപകരണം ഉപയോഗിക്കുന്നു
- 🗺️ **ബുദ്ധിമുട്ടുള്ള യാത്രാ പദ്ധതി**: ദിവസപത്രിക രൂപത്തിൽ വിശദമായ യാത്രാ പദ്ധതി സൃഷ്ടിക്കുന്നു
- 🔄 **തത്സമയ സ്‌ട്രിമിങ്**: അധികവും തത്സമയവും മറുപടികൾ ലഭ്യമാക്കുന്നു
- 🛠️ **കസ്റ്റം ഉപകരണ സംയോജനം**: ഏജന്റ് കഴിവുകൾ വളർത്തുന്നതിന് ഉദാഹരണം നൽകുന്നു

## 🔧 സാങ്കേതിക ആർക്കിടെക്ചർ

### പ്രധാനം സാങ്കേതിക വിദ്യകൾ

- **Microsoft Agent Framework**: AI ഏജന്റ് വികസനത്തിനായുള്ള എ.ഐ. ഏറ്റവും പുതിയ .NET നിർവാഹം
- **Azure OpenAI (Responses API)**: മോഡൽ അർത്ഥനം നടത്താൻ Azure OpenAI Responses API ഉപയോഗിക്കുന്നു
- **Azure Identity**: `AzureCliCredential` (`az login`) വഴി സുരക്ഷിത സൈൻ ഇൻ
- **സുരക്ഷിത കോൺഫിഗറേഷൻ**: പരിസ്ഥിതി അടിസ്ഥാനമായ എൻഡ്‌പോയിന്റ് മാനേജ്മെന്റ്

### മുഖ്യ ഘടകങ്ങൾ

1. **AIAgent**: സംഭാഷണ പ്രവാഹം കൈകാര്യം ചെയ്യുന്ന പ്രധാന ഏജന്റ് ഓർക്കസ്ട്രേറ്റർ
2. **Custom Tools**: ഏജന്റിന് ലഭ്യമായ `GetRandomDestination()` ഫംഗ്ഷൻ
3. **Responses Client**: Azure OpenAI Responses അടിസ്ഥാനമാക്കുന്ന സംഭാഷണ ഇന്റർഫേസ്
4. **Streaming Support**: തത്സമയ മറുപടി സൃഷ്ടി കഴിവുകൾ

### സംയോജനം മാതൃക

```mermaid
graph LR
    A[ഉപയോക്തൃ അഭ്യർത്ഥന] --> B[AI ഏജന്റ്]
    B --> C[അഴ്യൂർ ഒപ്പൺഎഐ (ഉത്തരം API)]
    B --> D[GetRandomDestination ഉപകരണം]
    C --> E[യാത്രാ പരിപാടി]
    D --> E
```

## 🚀 തുടങ്ങുക

### ആവശ്യമായ മുൻഷരത്ത്

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) അല്ലെങ്കിൽ അതിലധികം
- Azure OpenAI വിഭവവും മോഡൽ വിന്യാസവുമുള്ള [Azure subscription](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` വഴി സൈൻ ഇൻ ചെയ്യുക

### ആവശ്യമായ പരിസ്ഥിതി വേരിയബിളുകൾ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# പിന്നെ സൈൻ ഇൻ ചെയ്യൂ, যাতে AzureCliCredential ടോക്കൺ ലഭിക്കാം
az login
```

```powershell
# പവർഷെൽ
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# അതിനു ശേഷം AzureCliCredential ഒരു ടോക്കൺ ലഭിക്കാൻ സൈൻ ഇൻ ചെയ്യുക
az login
```

### സാമ്പിള്‍ കോഡ്

കോഡ് ഉദാഹരണം ഓടിക്കാൻ,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

അല്ലെങ്കിൽ dotnet CLI ഉപയോഗിച്ച്:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

സമ്പൂർണ്ണ കോഡിന് [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) കാണുക.

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

## 🎓 പ്രധാന പഠനങ്ങൾ

1. **ഏജന്റ് ആർക്കിടെക്ചർ**: Microsoft Agent Framework, .NET-ൽ AI ഏജന്റുകൾ നിർമ്മിക്കാനായി ക്ലീൻ, തരം-സുരക്ഷിത സമീപനം നൽകുന്നു
2. **ഉപകരണ സംയോജനം**: `[Description]` അടയാളപ്പെടുത്തിയ ഫംഗ്ഷനുകൾ ഏജന്റിനായി ലഭ്യമായ ഉപകരണങ്ങളായി മാറുന്നവയാണ്
3. **കോൺഫിഗറേഷൻ മാനേജ്മെന്റ്**: പരിസ്ഥിതി വേരിയബിളുകൾക്കും സുരക്ഷിത ക്രെഡൻഷ്യൽ കൈകാര്യം ഭരണവുമാണ് .NET മികച്ച പ്രാക്ടിസുകൾ പാലിക്കുന്നത്
4. **Azure OpenAI Responses API**: ഏജന്റ് Azure.AI.OpenAI SDK മുഖാന്തരം Azure OpenAI Responses API ഉപയോഗിക്കുന്നു

## 🔗 അധിക സാമഗ്രികൾ

- [Microsoft Agent Framework ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry-യിൽ Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET സിംഗിൾ ഫയൽ ആപ്പുകൾ](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->