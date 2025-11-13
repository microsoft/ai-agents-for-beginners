<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T13:34:59+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "sw"
}
-->
# 🔍 Kuchunguza Mfumo wa Microsoft Agent - Wakala wa Msingi (.NET)

## 📋 Malengo ya Kujifunza

Mfano huu unachunguza dhana za msingi za Mfumo wa Microsoft Agent kupitia utekelezaji wa wakala wa msingi katika .NET. Utajifunza mifumo ya msingi ya wakala na kuelewa jinsi mawakala wenye akili hufanya kazi kwa undani kwa kutumia C# na mfumo wa .NET.

### Kile Utakachogundua

- 🏗️ **Muundo wa Wakala**: Kuelewa muundo wa msingi wa mawakala wa AI katika .NET  
- 🛠️ **Ujumuishaji wa Zana**: Jinsi mawakala hutumia kazi za nje kupanua uwezo  
- 💬 **Mtiririko wa Mazungumzo**: Kusimamia mazungumzo ya mizunguko mingi na muktadha kwa usimamizi wa nyuzi  
- 🔧 **Mifumo ya Usanidi**: Mbinu bora za usanidi wa wakala na usimamizi katika .NET  

## 🎯 Dhana Muhimu Zinazoshughulikiwa

### Kanuni za Mfumo wa Wakala

- **Uhuru**: Jinsi mawakala wanavyofanya maamuzi huru kwa kutumia dhana za AI za .NET  
- **Uchangamfu**: Kujibu mabadiliko ya mazingira na pembejeo za mtumiaji  
- **Uchukuaji Hatua**: Kuchukua hatua kulingana na malengo na muktadha  
- **Uwezo wa Kijamii**: Kuingiliana kupitia lugha ya asili na nyuzi za mazungumzo  

### Vipengele vya Kiufundi

- **AIAgent**: Usimamizi wa wakala wa msingi na mazungumzo (.NET)  
- **Kazi za Zana**: Kupanua uwezo wa wakala kwa kutumia mbinu na sifa za C#  
- **Ujumuishaji wa OpenAI**: Kutumia mifano ya lugha kupitia API za kawaida za .NET  
- **Usanidi Salama**: Usimamizi wa funguo za API kulingana na mazingira  

## 🔧 Mfumo wa Kiufundi

### Teknolojia za Msingi

- Mfumo wa Microsoft Agent (.NET)  
- Ujumuishaji wa API ya GitHub Models  
- Mifumo inayolingana na OpenAI  
- Usanidi kulingana na mazingira kwa kutumia DotNetEnv  

### Uwezo wa Wakala

- Uelewa wa lugha ya asili na uzalishaji  
- Kuita kazi na kutumia zana kwa sifa za C#  
- Majibu yanayojali muktadha na nyuzi za mazungumzo  
- Muundo unaoweza kupanuliwa kwa mifumo ya sindano ya utegemezi  

## 📚 Ulinganisho wa Mfumo

Mfano huu unaonyesha mbinu ya Mfumo wa Microsoft Agent ikilinganishwa na mifumo mingine ya wakala:

| Kipengele | Mfumo wa Microsoft Agent | Mifumo Mingine |
|-----------|--------------------------|----------------|
| **Ujumuishaji** | Mfumo wa Microsoft wa asili | Ulinganifu tofauti |
| **Urahisi** | API safi, rahisi kuelewa | Mara nyingi usanidi mgumu |
| **Uwezo wa Kupanua** | Ujumuishaji rahisi wa zana | Hutegemea mfumo |
| **Tayari kwa Biashara** | Imejengwa kwa uzalishaji | Inategemea mfumo |

## 🚀 Kuanza

### Mahitaji

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) au ya juu zaidi  
- [Token ya ufikiaji wa API ya GitHub Models](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### Vigezo vya Mazingira Vinavyohitajika

```bash
# zsh/bash
export GH_TOKEN=<your_github_token>
export GH_ENDPOINT=https://models.github.ai/inference
export GH_MODEL_ID=openai/gpt-5-mini
```
  
```powershell
# PowerShell
$env:GH_TOKEN = "<your_github_token>"
$env:GH_ENDPOINT = "https://models.github.ai/inference"
$env:GH_MODEL_ID = "openai/gpt-5-mini"
```
  

### Mfano wa Msimbo

Ili kuendesha mfano wa msimbo,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
Au kwa kutumia CLI ya dotnet:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
Angalia [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) kwa msimbo kamili.

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
  

## 🎓 Mambo Muhimu ya Kujifunza

1. **Muundo wa Wakala**: Mfumo wa Microsoft Agent unatoa mbinu safi, salama kwa aina za kujenga mawakala wa AI katika .NET  
2. **Ujumuishaji wa Zana**: Kazi zilizopambwa na sifa za `[Description]` zinakuwa zana zinazopatikana kwa wakala  
3. **Muktadha wa Mazungumzo**: Usimamizi wa nyuzi unaruhusu mazungumzo ya mizunguko mingi yenye ufahamu kamili wa muktadha  
4. **Usimamizi wa Usanidi**: Vigezo vya mazingira na usimamizi salama wa hati vinazingatia mbinu bora za .NET  
5. **Ulinganifu wa OpenAI**: Ujumuishaji wa GitHub Models unafanya kazi bila matatizo kupitia API zinazolingana na OpenAI  

## 🔗 Rasilimali za Ziada

- [Nyaraka za Mfumo wa Microsoft Agent](https://learn.microsoft.com/agent-framework)  
- [Soko la GitHub Models](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->