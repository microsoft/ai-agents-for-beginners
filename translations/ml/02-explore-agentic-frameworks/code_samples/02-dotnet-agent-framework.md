<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-12-03T17:10:20+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "ml"
}
-->
# 🔍 Microsoft Agent Framework - അടിസ്ഥാന ഏജന്റ് (.NET) പരിശോധിക്കുന്നു

## 📋 പഠന ലക്ഷ്യങ്ങൾ

ഈ ഉദാഹരണം .NET-ൽ അടിസ്ഥാന ഏജന്റ് നടപ്പാക്കലിലൂടെ Microsoft Agent Framework-ന്റെ അടിസ്ഥാന ആശയങ്ങൾ പരിശോധിക്കുന്നു. C#യും .NET പരിസ്ഥിതിയും ഉപയോഗിച്ച് ബുദ്ധിമാനായ ഏജന്റുകൾ എങ്ങനെ പ്രവർത്തിക്കുന്നു എന്ന് മനസ്സിലാക്കുകയും പ്രധാന ഏജന്റിക് മാതൃകകൾ പഠിക്കുകയും ചെയ്യും.

### നിങ്ങൾ കണ്ടെത്തുന്ന കാര്യങ്ങൾ

- 🏗️ **ഏജന്റ് ആർക്കിടെക്ചർ**: .NET-ൽ AI ഏജന്റുകളുടെ അടിസ്ഥാന ഘടന മനസ്സിലാക്കുക  
- 🛠️ **ടൂൾ ഇന്റഗ്രേഷൻ**: ഏജന്റുകൾ കഴിവുകൾ വികസിപ്പിക്കാൻ ബാഹ്യ ഫംഗ്ഷനുകൾ എങ്ങനെ ഉപയോഗിക്കുന്നു  
- 💬 **സംഭാഷണ പ്രവാഹം**: ത്രെഡ് മാനേജ്മെന്റിലൂടെ മൾട്ടി-ടേൺ സംഭാഷണങ്ങളും കോൺടെക്സ്റ്റും കൈകാര്യം ചെയ്യുക  
- 🔧 **കോണ്ഫിഗറേഷൻ മാതൃകകൾ**: .NET-ൽ ഏജന്റ് സജ്ജീകരണത്തിനും മാനേജ്മെന്റിനും മികച്ച രീതികൾ

## 🎯 പ്രധാന ആശയങ്ങൾ

### ഏജന്റിക് ഫ്രെയിംവർക്കിന്റെ തത്വങ്ങൾ

- **സ്വയംഭരണശേഷി**: .NET AI അബ്സ്ട്രാക്ഷനുകൾ ഉപയോഗിച്ച് ഏജന്റുകൾ സ്വതന്ത്രമായ തീരുമാനങ്ങൾ എടുക്കുന്നത്  
- **പ്രതികരണശേഷി**: പരിസ്ഥിതിയിലെ മാറ്റങ്ങൾക്കും ഉപയോക്തൃ ഇൻപുട്ടുകൾക്കും പ്രതികരിക്കുന്നത്  
- **പ്രോആക്റ്റിവിറ്റി**: ലക്ഷ്യങ്ങളും കോൺടെക്സ്റ്റും അടിസ്ഥാനമാക്കി സ്വയം പ്രവർത്തനങ്ങൾ ആരംഭിക്കുന്നത്  
- **സാമൂഹിക കഴിവ്**: സംഭാഷണ ത്രെഡുകൾ ഉപയോഗിച്ച് സ്വാഭാവിക ഭാഷയിലൂടെ ആശയവിനിമയം നടത്തുക  

### സാങ്കേതിക ഘടകങ്ങൾ

- **AIAgent**: .NET-ൽ കോർ ഏജന്റ് ഓർക്കസ്ട്രേഷൻയും സംഭാഷണ മാനേജ്മെന്റും  
- **ടൂൾ ഫംഗ്ഷനുകൾ**: C# മെത്തഡുകളും ആട്രിബ്യൂട്ടുകളും ഉപയോഗിച്ച് ഏജന്റിന്റെ കഴിവുകൾ വികസിപ്പിക്കുക  
- **OpenAI ഇന്റഗ്രേഷൻ**: .NET API-കളുടെ സ്റ്റാൻഡേർഡ് ഉപയോഗിച്ച് ഭാഷ മോഡലുകൾ പ്രയോജനപ്പെടുത്തുക  
- **സുരക്ഷിത കോൺഫിഗറേഷൻ**: പരിസ്ഥിതി അടിസ്ഥാനമാക്കിയുള്ള API കീ മാനേജ്മെന്റ്  

## 🔧 സാങ്കേതിക സ്റ്റാക്ക്

### പ്രധാന സാങ്കേതികവിദ്യകൾ

- Microsoft Agent Framework (.NET)  
- GitHub Models API ഇന്റഗ്രേഷൻ  
- OpenAI-സഹതുല്യമായ ക്ലയന്റ് മാതൃകകൾ  
- DotNetEnv ഉപയോഗിച്ച് പരിസ്ഥിതി അടിസ്ഥാനമാക്കിയുള്ള കോൺഫിഗറേഷൻ  

### ഏജന്റിന്റെ കഴിവുകൾ

- സ്വാഭാവിക ഭാഷയെ മനസ്സിലാക്കുകയും സൃഷ്ടിക്കുകയും ചെയ്യുക  
- C# ആട്രിബ്യൂട്ടുകൾ ഉപയോഗിച്ച് ഫംഗ്ഷൻ കോളിംഗും ടൂൾ ഉപയോഗവും  
- സംഭാഷണ ത്രെഡുകൾ ഉപയോഗിച്ച് കോൺടെക്സ്റ്റ്-അവബോധമുള്ള പ്രതികരണങ്ങൾ  
- ഡിപ്പൻഡൻസി ഇഞ്ചക്ഷൻ മാതൃകകളുമായി വിപുലീകരിക്കാവുന്ന ആർക്കിടെക്ചർ  

## 📚 ഫ്രെയിംവർക്കിന്റെ താരതമ്യം

ഈ ഉദാഹരണം Microsoft Agent Framework-ന്റെ സമീപനം മറ്റ് ഏജന്റിക് ഫ്രെയിംവർക്കുകളുമായി താരതമ്യം ചെയ്യുന്നു:

| സവിശേഷത | Microsoft Agent Framework | മറ്റ് ഫ്രെയിംവർക്കുകൾ |
|----------|---------------------------|--------------------|
| **ഇന്റഗ്രേഷൻ** | നാടൻ Microsoft പരിസ്ഥിതി | വ്യത്യസ്തമായ അനുയോജ്യത |
| **ലളിതത്വം** | ശുചിത്വമുള്ള, മനസ്സിലാക്കാൻ എളുപ്പമുള്ള API | പലപ്പോഴും സങ്കീർണ്ണമായ സജ്ജീകരണം |
| **വിപുലീകരണശേഷി** | ടൂൾ ഇന്റഗ്രേഷൻ എളുപ്പം | ഫ്രെയിംവർക്കിനെ ആശ്രയിച്ചിരിക്കുന്നു |
| **എന്റർപ്രൈസ് റെഡി** | ഉത്പാദനത്തിനായി നിർമ്മിച്ചത് | ഫ്രെയിംവർക്കിനെ ആശ്രയിച്ചിരിക്കുന്നു |

## 🚀 ആരംഭിക്കുന്നത്

### ആവശ്യമായ മുൻവ്യവസ്ഥകൾ

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) അല്ലെങ്കിൽ അതിനുമുകളിൽ  
- [GitHub Models API ആക്സസ് ടോക്കൺ](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### ആവശ്യമായ പരിസ്ഥിതി വേരിയബിളുകൾ

```bash
# zsh/bash
export GH_TOKEN=<your_github_token>
export GH_ENDPOINT=https://models.github.ai/inference
export GH_MODEL_ID=openai/gpt-5-mini
```
  
```powershell
# പവർഷെൽ
$env:GH_TOKEN = "<your_github_token>"
$env:GH_ENDPOINT = "https://models.github.ai/inference"
$env:GH_MODEL_ID = "openai/gpt-5-mini"
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
  
സമ്പൂർണ്ണ കോഡിനായി [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) കാണുക.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*

using System.ClientModel;
using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using OpenAI;

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

// Extract configuration from environment variables
// Retrieve the GitHub Models API endpoint, defaults to https://models.github.ai/inference if not specified
// Retrieve the model ID, defaults to openai/gpt-5-mini if not specified
// Retrieve the GitHub token for authentication, throws exception if not specified
var github_endpoint = Environment.GetEnvironmentVariable("GH_ENDPOINT") ?? "https://models.github.ai/inference";
var github_model_id = Environment.GetEnvironmentVariable("GH_MODEL_ID") ?? "openai/gpt-5-mini";
var github_token = Environment.GetEnvironmentVariable("GH_TOKEN") ?? throw new InvalidOperationException("GH_TOKEN is not set.");

// Configure OpenAI Client Options
// Create configuration options to point to GitHub Models endpoint
// This redirects OpenAI client calls to GitHub's model inference service
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
// Create OpenAI client using GitHub token for authentication
// Configure it to use GitHub Models endpoint instead of OpenAI directly
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

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
// Initialize complete agent pipeline: OpenAI client → Chat client → AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
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
  

## 🎓 പ്രധാന പഠനങ്ങൾ

1. **ഏജന്റ് ആർക്കിടെക്ചർ**: Microsoft Agent Framework .NET-ൽ AI ഏജന്റുകൾ നിർമ്മിക്കാൻ ശുചിത്വവും ടൈപ്പ്-സേഫും ഉള്ള സമീപനം നൽകുന്നു  
2. **ടൂൾ ഇന്റഗ്രേഷൻ**: `[Description]` ആട്രിബ്യൂട്ടുകൾ ഉപയോഗിച്ച് അലങ്കരിച്ച ഫംഗ്ഷനുകൾ ഏജന്റിന് ലഭ്യമായ ടൂളുകളായി മാറുന്നു  
3. **സംഭാഷണ കോൺടെക്സ്റ്റ്**: ത്രെഡ് മാനേജ്മെന്റ് മൾട്ടി-ടേൺ സംഭാഷണങ്ങൾ മുഴുവൻ കോൺടെക്സ്റ്റ് അവബോധത്തോടെ സാധ്യമാക്കുന്നു  
4. **കോൺഫിഗറേഷൻ മാനേജ്മെന്റ്**: പരിസ്ഥിതി വേരിയബിളുകളും സുരക്ഷിത ക്രെഡൻഷ്യൽ കൈകാര്യം ചെയ്യലും .NET മികച്ച രീതികൾ പിന്തുടരുന്നു  
5. **OpenAI അനുയോജ്യത**: GitHub Models ഇന്റഗ്രേഷൻ OpenAI-സഹതുല്യമായ API-കളിലൂടെ സുതാര്യമായി പ്രവർത്തിക്കുന്നു  

## 🔗 അധിക വിഭവങ്ങൾ

- [Microsoft Agent Framework ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/agent-framework)  
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET സിംഗിൾ ഫയൽ ആപ്പുകൾ](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസത്യവാദം**:  
ഈ രേഖ AI വിവർത്തന സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. കൃത്യതയ്ക്കായി ഞങ്ങൾ ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ മാതൃഭാഷയിലുള്ള മൗലികരേഖയാണ് വിശ്വസനീയമായ ഉറവിടമായി കണക്കാക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മാനവ വിവർത്തനം ശുപാർശ ചെയ്യുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->