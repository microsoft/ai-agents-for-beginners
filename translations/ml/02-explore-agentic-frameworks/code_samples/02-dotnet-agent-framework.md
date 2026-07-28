# 🔍 മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് അന്വേഷിക്കുന്നു - ബേസിക്ക് ഏജന്റ് (.NET)

## 📋 പഠന ലക്ഷ്യങ്ങൾ

ഈ ഉദാഹരണം .NET-ൽ ഒരു ലളിത ഏജന്റ് നടപ്പാക്കലിന്റെ മുഖേന മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ അടിസ്ഥാന ആശയങ്ങൾ പരിശോധിക്കുന്നു. നിങ്ങൾ വ്യവസ്ഥാപിത ഏജന്റ് പാറ്റേണുകൾ പഠിക്കുകയും C#യും .NET ഇക്കോസിസ്റ്റവും ഉപയോഗിച്ച് ബുദ്ധിമാനായ ഏജൻറുകൾ എങ്ങനെ പ്രവർത്തിക്കുന്നു എന്ന് മനസിലാക്കുകയും ചെയ്യുമെന്ന്.

### നിങ്ങൾ കണ്ടെത്തുക എന്ത്

- 🏗️ **ഏജന്റ് നിർമ്മാണം**: .NET-ൽ AI ഏജന്റുകളുടെ അടിസ്ഥാന ഘടന മനസിലാക്കൽ
- 🛠️ **ടൂൾ ഇന്റഗ്രേഷൻ**: കഴിവുകൾ വർദ്ധിപ്പിക്കാൻ ഏജന്റ് പുറത്തുള്ള ഫംഗ്ഷനുകൾ എങ്ങനെ ഉപയോഗിക്കുന്നു  
- 💬 **സംവാദ പ്രവാഹം**: മൾട്ടി-ടേൺ സംഭാഷണങ്ങളും കോൺടെക്‌സ്‌റ്റ് കൈകാര്യം ചെയ്യലും ത്രെഡ് മാനേജ്മെന്റ് ഉപയോഗിച്ച്
- 🔧 **കോൺഫിഗറേഷൻ പാറ്റേണുകൾ**: .NET-ൽ ഏജന്റ് ക്രമീകരണത്തിനും മാനേജ്മെന്റിനും മികച്ച രീതികൾ

## 🎯 മുഖ്യ ആശയങ്ങൾ ഉൾപ്പെടുന്നു

### ഏജന്റിക് ഫ്രെയിംവർക്ക് സിദ്ധാന്തങ്ങൾ

- **സ്വയം സ്വാതന്ത്ര്യം**: .NET AI അബ്സ്ട്രാക്ഷനുകൾ ഉപയോഗിച്ച് ഏജന്റുകൾ സ്വതന്ത്രമായി തീരുമാനങ്ങൾ എടുക്കുന്നത്
- **പ്രതികരണശേഷി**: പരിസ്ഥിതി മാറ്റങ്ങൾക്കും ഉപയോക്തൃ ഇൻപുട്ടുകൾക്കും പ്രതികരിക്കൽ
- **പ്രവർത്ത്യത്വം**: ലക്ഷ്യങ്ങളും കോൺടെക്‌സ്‌റ്റും അടിസ്ഥാനമാക്കി മുൻകൈ എടുക്കുക
- **സാമൂഹിക കഴിവ്**: സംഭാഷണ ത്രെഡുകൾ വഴി സ്വാഭാവിക ഭാഷയിൽ ഇടപഴകുക

### സാങ്കേതിക ഘടകങ്ങൾ

- **AIAgent**: കോർ ഏജന്റ് ഓർക്കസ്ട്രേഷൻ மற்றும் സംഭാഷണ മാനേജ്മെന്റ് (.NET)
- **ടൂൾ ഫംഗ്ഷനുകൾ**: C# മെത്തഡുകളും ആട്രിബ്യൂട്ട്‌സും ഉപയോഗിച്ച് ഏജന്റ് കഴിവുകൾ വിപുലീകരിക്കൽ
- **അസ്യൂർ ഓപ്പൺഎഐ ഇന്റഗ്രേഷൻ**: Azure OpenAI Responses API വഴി ഭാഷാ മോഡലുകൾ ഉപയോഗിക്കൽ
- **സുരക്ഷിത കോൺഫിഗറേഷൻ**: പരിസ്ഥിതി അടിസ്ഥാനത്തിലുള്ള എൻ്റ്പോയ്ഇന്റ് മാനേജ്മെന്റ്

## 🔧 സാങ്കേതിക സ്റ്റാക്ക്

### കോർ സാങ്കേതികവിദ്യകൾ

- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് (.NET)
- അസ്യൂർ ഓപ്പൺഎഐ (Responses API) ഇന്റഗ്രേഷൻ
- Azure.AI.OpenAI ക്ലയന്റ് പാറ്റേണുകൾ
- DotNetEnv ഉപയോഗിച്ച് പരിസ്ഥിതി അടിസ്ഥാനത്തിലുള്ള കോൺഫിഗറേഷൻ

### ഏജന്റ് കഴിവുകൾ

- സ്വാഭാവിക ഭാഷ മനസ്സിലാക്കലും സൃഷ്‌ടിയuamും
- C# ആട്രിബ്യൂട്ടുകളോടുകൂടിയ ഫംഗ്ഷൻ കോളിംഗും ടൂൾ ഉപയോഗവും
- സംഭാഷണ സെഷനുകളിൽ കോൺടെക്‌സ്‌റ്റ്-അവരെയുള്ള പ്രതികരണങ്ങൾ
- ഡിപ്പെൻഡൻസി ഇൻജക്ഷൻ പാറ്റേണുകൾ ഉപയോഗിച്ച് വിപുലീകരിക്കാൻ കഴിയുന്ന നിർമ്മാണം

## 📚 ഫ്രെയിംവർക്ക് താരതമ്യം

ഈ ഉദാഹരണം മറ്റു ഏജന്റിക് ഫ്രെയിംവർക്കുകളോടുള്ള താരതമ്യത്തിൽ മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ സമീപനം വിശദീകരിക്കുന്നു:

| ഫീച്ചർ | മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് | മറ്റ് ഫ്രെയിംവർക്കുകൾ |
|---------|-------------------------|------------------|
| **ഇന്റഗ്രേഷൻ** | നേറ്റീവ് മൈക്രോസോഫ്റ്റ് ഇക്കോസിസ്റ്റം | വ്യത്യസ്ത അനുയോജ്യത |
| **എളുപ്പം** | ക്ലീൻ, മനസ്സിലാക്കാൻ എളുപ്പമുള്ള API | സാധാരണം കോമ്പ്ലക്‌സ് ക്രമീകരണം |
| **വിപുലീകരണക്ഷമത** | എളുപ്പമുള്ള ടൂൾ ഇന്റഗ്രേഷൻ | ഫ്രെയിംവർക്ക് ആശ്രമിതം |
| **എന്റർപ്രൈസ് റെഡി** | ഉൽപ്പാദനത്തിനായി നിർമ്മിക്കപ്പെട്ടത് | ഫ്രെയിംവർക്കിന്റെ അടിസ്ഥാനത്തിൽ വ്യത്യാസപ്പെടുന്നു |

## 🚀 ആരംഭിക്കുന്നത്

### മുൻകൂറുള്ള ആവശ്യങ്ങൾ

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) അല്ലെങ്കിൽ വലുതായി
- ഒരു [Azure സബ്‌സ്ക്രിപ്ഷൻ](https://azure.microsoft.com/free/) Azure OpenAI റിസോഴ്സ് ഒപ്പം മോഡൽ വിന്യാസം ഉള്ളത്
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` ഉപയോഗിച്ച് ലോഗിൻ ചെയ്യുക

### ആവശ്യമായ പരിസ്ഥിതി വേരിയബിളുകൾ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# തുടർന്ന് AzureCliCredential ഒരു ടോക്കൺ നേടാൻ സൈൻ ഇൻ ചെയ്യുക
az login
```

```powershell
# പവർഷെൽ
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# ആഴ്യൂർക്ലിക്രെഡൻഷ്യൽ ടോക്കൺ നേടാൻ ശേഷം സൈൻ ഇൻ ചെയ്യുക
az login
```

### സാമ്പിൾ കോഡ്

കോഡ് ഉദാഹരണം പ്രവർത്തിപ്പിക്കാൻ,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

അല്ലെങ്കിൽ dotnet CLI ഉപയോഗിച്ച്:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

പൂർണ്ണ കോഡിന് [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) കാണുക.

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

## 🎓 മുഖ്യ പഠനപോയിന്റുകൾ

1. **ഏജന്റ് ആർക്കിടെക്ചർ**: മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് .NET-ൽ AI ഏജന്റുകൾ നിർമ്മിക്കാൻ ക്ലീൻ, ടൈപ്പ്-സേഫ് സമീപനം നൽകുന്നു
2. **ടൂൾ ഇന്റഗ്രേഷൻ**: `[Description]` ആട്രിബ്യൂട്ടുകൾകൊണ്ട് അലങ്കൃതമായ ഫംഗ്ഷനുകൾ ഏജന്റിന് ഉപയോഗപ്രദമായ ടൂളുകളായി മാറുന്നു
3. **സംവാദ കോൺടെക്‌സ്‌റ്റ്**: സെഷൻ മാനേജ്മെന്റ് മൾട്ടി-ടേൺ സംഭാഷണങ്ങളോടൊപ്പം പൂർണ്ണ കോൺടെക്‌സ്‌റ് അവരെയ്നസും സജ്ജമാക്കുന്നു
4. **കോൺഫിഗറേഷൻ മാനേജ്മെന്റ്**: പരിസ്ഥിതി വേരിയബിളുകളും സുരക്ഷിത ക്രെഡൻഷ്യൽ കൈകാര്യം ചെയ്യലും .NET മികച്ച രീതികൾ പാലിക്കുന്നു
5. **അസ്യൂർ ഓപ്പൺഎഐ Responses API**: ഏജന്റ് Azure.AI.OpenAI SDK വഴി Azure OpenAI Responses API ഉപയോഗിക്കുന്നു

## 🔗 അധിക വാസ്തവങ്ങൾ

- [Microsoft Agent Framework ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry-ലുള്ള Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET സിംഗിൾ ഫയൽ അപ്ലിക്കേഷനുകൾ](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->