# 🔍 മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിനെ എങ്ങനെ ഉപയോഗിക്കാം - ബേസിക് ഏജന്റ് (.NET)

## 📋 শেখൽ ലക്ഷ്യങ്ങൾ

ഈ ഉദാഹരണം മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ അടിസ്ഥാന ആശയങ്ങളെ .NET ൽ ഒരു അടിസ്ഥാന ഏജന്റിന്റെ നടപ്പിലാക്കൽ വഴി അന്വേഷിക്കുന്നു. നിങ്ങൾ കോർ ഏജന്റിക് മാതൃകകൾ പഠിക്കുകയും C# ഉം .NET പരിസ്ഥിതിയും ഉപയോഗിച്ച് ബുദ്ധിമത്തമുള്ള ഏജന്റുകൾ എങ്ങനെ പ്രവർത്തിക്കുന്നുവെന്ന് മനസ്സിലാക്കുകയും ചെയ്യും.

### നിങ്ങൾ അറിയാൻ പോകുന്നത്

- 🏗️ **ഏജന്റ് ആർക്കിടെചർ**: .NET ൽ AI ഏജന്റുകളുടെ അടിസ്ഥാന ഘടന മനസിലാക്കൽ
- 🛠️ **ടൂൾ ഉൾപ്പെടുത്തൽ**: ഏജന്റുകൾ എങ്ങനെ വിദേശ ഫംഗ്ഷനുകൾ ഉപയോഗിച്ച് ശേഷികൾ വർദ്ധിപ്പിക്കുന്നു  
- 💬 **സംഭാഷണ പ്രവാഹം**: മൾട്ടി-ടേൺ സംഭാഷണങ്ങളും കോൺടെക്സ്റ്റും ത്രെഡ് മാനേജ്മെന്റ് ഉപയോഗിച്ച് കൈകാര്യം ചെയ്യൽ
- 🔧 **കോൺഫിഗറേഷൻ മാതൃകകൾ**: .NET ൽ ഏജന്റ് ക്രമീകരണത്തിനും മാനേജ്മെന്റിനും മികച്ച പ്രയോഗങ്ങൾ

## 🎯 ഉൾപ്പെട്ട പ്രധാന ആശയങ്ങൾ

### ഏജന്റിക് ഫ്രെയിംവർക്കിന്റെ സിദ്ധാന്തങ്ങൾ

- **സ്വയംഭരണവാദം**: .NET AI അബ്സ്ട്രാക്ഷനുകൾ ഉപയോഗിച്ച് ഏജന്റുകൾ സ്വതന്ത്ര തീരുമാനങ്ങൾ എടുക്കുന്നത്
- **പ്രതിക്രിയാത്മകത**: പരിസ്ഥിതി മാറ്റങ്ങളുടെയും ഉപയോക്തൃ ഇൻപുട്ടിന്റെയും പ്രതികരണം
- **പ്രോആകർട്ടിവിറ്റി**: ലക്ഷ്യങ്ങളുടെയും കോൺടെക്സ്റ്റിന്റെയും അടിസ്ഥാനത്തിൽ പ്രാരംഭം എടുക്കൽ
- **സാമൂഹിക ശേഷി**: സംഭാഷണ ത്രെഡുകൾ ഉപയോഗിച്ച് സ്വാഭാവിക ഭാഷയിലൂടെ ഇടപെടൽ

### സാങ്കേതിക ഘടകങ്ങൾ

- **AIAgent**: കോർ ഏജന്റ് ഓർക്കസ്‌ട്രേഷൻ, സംഭാഷണ മാനേജ്മെന്റ് (.NET)
- **ടൂൾ ഫംഗ്ഷനുകൾ**: C# മേത്തഡുകളും ആട്രിബ്യൂട്ടുകളും ഉപയോഗിച്ച് ഏജന്റ് ശേഷികൾ വിപുലീകരിക്കൽ
- **Azure OpenAI ഇന്റഗ്രേഷൻ**: Azure OpenAI Responses API വഴി ഭാഷ മോഡലുകൾ ഉപയോഗിക്കൽ
- **സുരക്ഷിത കോൺഫിഗറേഷൻ**: പരിസ്ഥിതി അടിസ്ഥാനമുള്ള എൻഡ്‌പോയിന്റ് മാനേജ്മെന്റ്

## 🔧 സാങ്കേതിക സ്റ്റാക്

### കോർ സാങ്കേതികവിദ്യകൾ

- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് (.NET)
- Azure OpenAI (Responses API) ഇന്റഗ്രേഷൻ
- Azure.AI.OpenAI ക്ലയന്റ് മാതൃകകൾ
- DotNetEnv ഉപയോഗിച്ച് പരിസ്ഥിതിയാനം അടിസ്ഥാനമാക്കിയുള്ള കോൺഫിഗറേഷൻ

### ഏജന്റ് ശേഷികൾ

- സ്വാഭാവിക ഭാഷാ മനസിലാക്കൽ, സൃഷ്ടിക്കൽ
- C# ആട്രിബ്യൂട്ടുകൾ ഉപയോഗിച്ച് ഫംഗ്ഷൻ കോളിങ്ങും ടൂൾ ഉപയോഗവും
- സംഭാഷണ ത്രെഡുകളിലൂടെ കോൺടെക്സ്റ്റ് അവഗാഹനത്തോടെയുള്ള പ്രതികരണങ്ങൾ
- ഡിപ്പൻഡൻസി ഇൻജക്ഷൻ മാതൃകകളോടെ വിപുലീകരിക്കാവുന്ന ആർക്കിടെക്ചർ

## 📚 ഫ്രെയിംവർക്കുകൾ തമ്മിലുള്ള താരതമ്യം

ഈ ഉദാഹരണം മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിനെ മറ്റ് ഏജന്റിക് ഫ്രെയിംവർക്കുകളുമായി താരതമ്യം ചെയ്യുന്നു:

| സവിശേഷത | മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് | മറ്റ് ഫ്രെയിംവർക്കുകൾ |
|---------|-------------------------|------------------|
| **ഇന്റഗ്രേഷൻ** | നേറ്റീവ് മൈക്രോസോഫ്റ്റ് ഇക്കോസിസ്റ്റം | വ്യത്യസ്ത അനുയോജ്യത |
| **സൗന്ദര്യം** | ശുദ്ധവും മനസ്സിലാക്കാൻ എളുപ്പവുമായ API | സാധാരണയായി ജടിലമായ ക്രമീകരണം |
| **വിപുലീകരണശക്തി** | എളുപ്പത്തിലുള്ള ടൂൾ ഇന്റഗ്രേഷൻ | ഫ്രെയിംവർക്ക് ആശ്രിതം |
| **എന്റർപ്രൈസ് റെഡി** | പ്രൊഡക്ഷനായി നിർമ്മിച്ചത് | ഫ്രെയിംവർക്കിനനുസരിച്ച് വ്യത്യാസപ്പെടുന്നു |

## 🚀 ആരംഭിക്കൽ

### മുൻകൂട്ടി വേണ്ടത്

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) അല്ലെങ്കിൽ അതിലധികം
- Azure OpenAI റിസോഴ്സ് കൂടിയ ഒരു [Azure സബ്സ്ക്രിപ്ഷൻ](https://azure.microsoft.com/free/) നിന്നും മോഡൽ ഡിപ്പ്ലോയ്മെന്റ്
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` കൊണ്ട് സൈൻ ഇൻ ചെയ്യുക

### ആവശ്യമായ പരിസ്ഥിതി ചാരങ്ങളിൽ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# പിന്നീട് കാലാകാലങ്ങളിൽ AzureCliCredential ടോക്കൺ നേടാൻ സൈൻ ഇൻ ചെയ്യുക
az login
```

```powershell
# പവർഷെൽ
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# പിന്നീട് സൈന്‍ ഇന്‍ ചെയ്യുക, അതിലൂടെ AzureCliCredential ടോക്കൺ നേടാൻ കഴിയും
az login
```

### സാമ്പിൾ കോഡ്

കോഡിന്റെ ഉദാഹരണം പ്രവർത്തിപ്പിക്കാൻ,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

അല്ലെങ്കിൽ ഡോട്ട്‌നെറ്റ് CLI ഉപയോഗിച്ച്:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

പൂര്‍ണ കോഡ് കാണാൻ [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) കാണുക.

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

## 🎓 പ്രധാന വിഷയങ്ങൾ

1. **ഏജന്റ് ആർക്കിടെക്ചർ**: മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് .NET ൽ AI ഏജന്റുകൾ നിർമ്മിക്കാൻ ശുദ്ധവും ടൈപ്പ്-സേഫും മാർഗം നൽകുന്നു
2. **ടൂൾ ഇന്റഗ്രേഷൻ**: `[Description]` ആട്രിബ്യൂട്ടുകളോടെ അലങ്കരിച്ച ഫംഗ്ഷനുകൾ ഏജന്റിന്റെ ടൂളുകളായി സാദ്ധ്യമാണ്
3. **സംഭാഷണ കോൺടെക്സ്റ്റ്**: ത്രെഡ് മാനേജ്മെന്റ് പൂര്‍ണ്ണ കോൺടെക്സ്റ്റ് അറിവോടെ മൾട്ടി-ടേൺ സംഭാഷണങ്ങൾ സജ്ജമാക്കുന്നു
4. **കോൺഫിഗറേഷൻ മാനേജ്മെന്റ്**: പരിസ്ഥിതി ചാരങ്ങളും സുരക്ഷിത ക്രെഡൻഷ്യൽ ഹാൻഡ്ലിംഗും .NET മികച്ച അനുഷ്ഠാനങ്ങൾ പിന്തുടരുന്നു
5. **Azure OpenAI Responses API**: ഏജന്റ് Azure.AI.OpenAI SDK വഴി Azure OpenAI Responses API ഉപയോഗിക്കുന്നു

## 🔗 അധിക സ്രോതസുകൾ

- [Microsoft Agent Framework ഡോക്യമെന്റേഷൻ](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry ലെ Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET സിംഗിൾ ഫയൽ ആപ്ലിക്കേഷനുകൾ](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->