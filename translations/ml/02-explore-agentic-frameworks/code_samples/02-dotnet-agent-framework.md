# 🔍 മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് അന്വേഷിച്ച്‌ - അടിസ്ഥാന ഏജന്റ് (.NET)

## 📋 പഠന ലക്ഷ്യങ്ങൾ

ഈ ഉദാഹരണം .NET-ൽ ഒരു അടിസ്ഥാന ഏജന്റ് നടപ്പിലാക്കലിലൂടെ മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ അടിസ്ഥാന ആശയങ്ങൾ അന്വേഷിക്കുന്നു. നിങ്ങൾ അടിസ്ഥാന ഏജന്റ് മാതൃകകൾ പഠിക്കുകയും C# ഒപ്പം .NET പരിസ്ഥിതിയിൽ ഇത്തരം ബുദ്ധിമുട്ടുള്ള ഏജന്റുകൾ എങ്ങനെ പ്രവർത്തിക്കുന്നു എന്ന് മനസ്സിലാക്കുകയും ചെയ്യും.

### നിങ്ങൾ കണ്ടെത്താനുള്ളത്

- 🏗️ **ഏജന്റ് ആർക്കിടെക്ചർ**: .NET-ലെ AI ഏജന്റുകളുടെ അടിസ്ഥാന ഘടന മനസ്സിലാക്കൽ  
- 🛠️ **ഉപകരണം സംയോജനം**: കഴിവുകൾ വിപുലീകരിക്കാൻ ഏജന്റുകൾ എങ്ങനെ പുറംഘടകങ്ങൾ ഉപയോഗിക്കുന്നു  
- 💬 **സംഭാഷണ പ്രവാഹം**: മൾട്ടി-ടേൺ സംഭാഷണങ്ങളും പ്രധാനം കൃത്യമായി കൈകാര്യം ചെയ്യൽ  
- 🔧 **കോൺഫിഗറേഷൻ മാതൃകകൾ**: .NET-ൽ ഏജന്റ് ക്രമീകരണവും മാനേജുമെന്റും മികച്ച രീതി  

## 🎯 പ്രധാന ആശയങ്ങൾ

### ഏജന്റിക് ഫ്രെയിംവർക്കിന്റെ സിദ്ധാന്തങ്ങൾ

- **സ്വാതന്ത്ര്യം**: .NET AI അബ്സ്ട്രാക്ഷനുകൾ ഉപയോഗിച്ച് ഏജന്റുകൾ സ്വതന്ത്രമായി തീരുമാനമെടുക്കുന്നത്  
- **പ്രതിക്രിയാത്മകത**: പരിസ്ഥിതി മാറ്റങ്ങൾക്കും ഉപയോക്തൃ ഇൻപുട്ടിനും പ്രതികരിക്കൽ  
- **പ്രായോഗികത**: ലക്‌ഷ്യങ്ങൾക്കും സാഹചര്യത്തിനും അടിസ്ഥാനമായി മുൻകൂർ നടപടികൾ കൈക്കൊള്ളൽ  
- **സാമൂഹികക്ഷമത**: സംഭാഷണ ത്രെഡുകൾ ഉപയോഗിച്ച് സ്വാഭാവിക ഭാഷയിലൂടെയുള്ള സംവേദനം  

### സാങ്കേതിക ഘടകങ്ങൾ

- **AIAgent**: കേർ ഏജന്റ് ഓർക്കസ്ട്രേഷൻ കൂടാതെ സംഭാഷണ മാനേജുമെന്റ് (.NET)  
- **ഉപകരണം ഫംഗ്ഷനുകൾ**: C# മേധോഡുകളും ആട്രിബ്യൂട്ടുകളും ഉപയോഗിച്ച് ഏജന്റ് കഴിവുകൾ വിപുലീകരിക്കൽ  
- **ആസ്യൂർ OpenAI സംയോജനം**: ആസ്യൂർ OpenAI Responses API വഴി ഭാഷാ മാതൃകകൾ പ്രയോഗിക്കൽ  
- **സുരക്ഷിത കോൺഫിഗറേഷൻ**: പരിസ്ഥിതി അടിസ്ഥാനത്തിലുള്ള എന്റ്പോയിന്റ് മാനേജുമെന്റ്  

## 🔧 സാങ്കേതിക സ്റ്റാക്ക്

### കോർ സാങ്കേതികവിദ്യകൾ

- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് (.NET)  
- ആസ്യൂർ OpenAI (Responses API) സംയോജനം  
- Azure.AI.OpenAI ക്ലയന്റ് പാറ്റേണുകൾ  
- DotNetEnv ഉപയോഗിച്ച് പരിസ്ഥിതി അടിസ്ഥാന കോൺഫിഗറേഷൻ  

### ഏജന്റ് കഴിവുകൾ

- സ്വാഭാവിക ഭാഷയുടെ ഗ്രഹണംയും സൃഷ്ടീകരണവും  
- ഫംഗ്ഷൻ കോൾ ചെയ്യൽ കൂടാതെ C# ആട്രിബ്യൂട്ടുകളുടെ ഉപകരണം ഉപയോഗം  
- രണ്ട് വട്ടം സംഭാഷണ സെഷനുകളുമായി പശ്ചാത്തലം ബോധവത്കരണം  
- ഡിപ്പൻഡൻസിയും ഇൻജക്ഷൻ മാതൃകകളും ഉള്ള വിപുലമായ ആർക്കിടെക്ചർ  

## 📚 ഫ്രെയിംവർക്ക് താരതമ്യം

ഈ ഉദാഹരണം മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ സമീപനം മറ്റു ഏജന്റിക് ഫ്രെയിംവർക്കുകളുമായി താരതമ്യപ്പെടുത്തുന്നു:

| സവിശേഷത | മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് | മറ്റു ഫ്രെയിംവർക്കുകൾ |
|---------|-------------------------|------------------|
| **സംയോജനം** | ദേശിയമായ മൈക്രോസോഫ്റ്റ് പരിസ്ഥിതി | വ്യത്യസ്തമായ അനുയോജ്യത |
| **സൗഹൃദത** | വൃത്തിയുള്ള, ബോധഗമ്യമായ API | പലപ്പോഴും സങ്കീർണ്ണമായ ക്രമീകരണം |
| **വിപുലീകരണക്ഷമത** | എളുപ്പത്തിൽ ഉപകരണം സംയോജനം | ഫ്രെയിംവർക്കിന് അനുസരിച്ചുള്ളത് |
| **എന്റർപ്രൈസ് സജ്ജം** | പ്രൊഡക്ഷൻ പരിപാലനത്തിന് നിർമ്മിച്ചത് | ഫ്രെയിംവർക്കിനു അനുസരിച്ച് വ്യത്യാസം |

## 🚀 ആരംഭിക്കൽ

### മുൻനിലവാരങ്ങൾ

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) അല്ലെങ്കിൽ അതിനുശേഷം  
- ആസ്യൂർ OpenAI ഉൽപ്പന്നവും മാതൃക ഡിപ്ലോയ്മെന്റും ഉള്ള [Azure സബ്‌സ്‌ക്രിപ്ഷൻ](https://azure.microsoft.com/free/)  
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` ഉപയോഗിച്ച് സൈനിൻ ചെയ്യുക  

### ആവശ്യമായ പരിസ്ഥിതി വേരിയബിളുകൾ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# പിന്നെ സൈൻ ഇൻ ചെയ്യുക, അതിലൂടെ AzureCliCredential ഒരു ടോക്കൻ നേടാൻ കഴിയും
az login
```

```powershell
# പവർഷെൽ
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# ശേഷം സൈൻ ഇൻ ചെയ്യൂ, അതിൽ AzureCliCredential ടോക്കൺ നേടാൻ കഴിയും
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

പൂർണ്ണ കോഡിനായി [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) കാണുക.

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

## 🎓 പ്രധാന ഗ്രഹണങ്ങൾ

1. **ഏജന്റ് ആർക്കിടെക്ചർ**: മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് .NET-ൽ AI ഏജന്റുകൾ നിർമ്മിക്കാൻ വൃത്തിയുള്ള, ടൈപ്പ്-സേഫ് സമീപനം നൽകുന്നു  
2. **ഉപകരണം സംയോജനം**: `[Description]` ആട്രിബ്യൂട്ടുകൾ പ്രസാദിപ്പിച്ച ഫംഗ്ഷനുകൾ ഏജന്റിന് ലഭ്യമായ ഉപകരണങ്ങളായി മാറുന്നു  
3. **സംഭാഷണ പശ്ചാത്തലം**: സെഷൻ മാനേജുമെന്റ് മൊത്തം പശ്ചാത്തലം ബോധവത്കരണത്തോടെ മൾട്ടി-ടേൺ സംഭാഷണങ്ങൾ അനുവദിക്കുന്നു  
4. **കോൺഫിഗറേഷൻ മാനേജുമെന്റ്**: പരിസ്ഥിതി വേരിയബിളുകളും സുരക്ഷിത ക്രെഡൻഷ്യൽ കൈകാര്യം ചെയ്യലും .NET മികച്ച രീതി അനുസരിക്കുന്നു  
5. **ആസ്യൂർ OpenAI Responses API**: ഏജന്റ് Azure.AI.OpenAI SDK വഴി ആസ്യൂർ OpenAI Responses API ഉപയോഗിക്കുന്നു  

## 🔗 അധിക ശേഷിയുള്ള വിഭവങ്ങൾ

- [Microsoft Agent Framework ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/agent-framework)  
- [Microsoft Foundry-യിലെ Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->