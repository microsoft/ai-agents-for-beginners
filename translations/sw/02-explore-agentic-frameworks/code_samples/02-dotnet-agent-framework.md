# 🔍 Kuchunguza Microsoft Agent Framework - Wakala wa Msingi (.NET)

## 📋 Malengo ya Kujifunza

Mfano huu unachunguza dhana za msingi za Microsoft Agent Framework kupitia utekelezaji wa wakala wa msingi katika .NET. Utafahamu mifumo kuu ya wakala na kuelewa jinsi mawakala wa akili hufanya kazi kwa undani kwa kutumia C# na mfumo wa .NET.

### Utaigundua Nini

- 🏗️ **Majaribio ya Wakala**: Kuelewa muundo wa msingi wa mawakala wa AI katika .NET
- 🛠️ **Uunganisho wa Zana**: Jinsi mawakala wanavyotumia kazi za nje kuongeza uwezo  
- 💬 **Mtiririko wa Mazungumzo**: Kusimamia mazungumzo ya mzunguko wa zaidi ya moja na muktadha kwa kusimamia mipangilio ya mizunguko
- 🔧 **Mifumo ya Upangaji**: Mbinu bora za usanidi na usimamizi wa wakala katika .NET

## 🎯 Dhana Muhimu Zilizoshughulikiwa

### Kanuni za Mfumo wa Wakala

- **Uhuru**: Jinsi mawakala wanavyoamua kwa uhuru kwa kutumia fumbo za AI za .NET
- **Kurekebisha**: Kujibu mabadiliko ya mazingira na maingizo ya mtumiaji
- **Kuchukua Hatua**: Kuchukua hatua kulingana na malengo na muktadha
- **Uwezo wa Kijamii**: Kuingiliana kupitia lugha ya asili na mizunguko ya mazungumzo

### Sehemu za Kiufundi

- **AIAgent**: Udhibiti mkuu wa wakala na usimamizi wa mazungumzo (.NET)
- **Kazi za Zana**: Kuongeza uwezo wa wakala kwa njia za C# na sifa
- **Muunganisho wa Azure OpenAI**: Kutumia mifano ya lugha kupitia Azure OpenAI Responses API
- **Usanidi Salama**: Usimamizi wa sehemu za mwisho kulingana na mazingira

## 🔧 Kano la Kiufundi

### Teknolojia Muhimu

- Microsoft Agent Framework (.NET)
- Muunganisho wa Azure OpenAI (Responses API)
- Mifano ya mteja wa Azure.AI.OpenAI
- Usanidi wa mazingira kwa kutumia DotNetEnv

### Uwezo wa Wakala

- Uelewa na uzalishaji wa lugha ya asili
- Kuitisha kazi na matumizi ya zana kwa sifa za C#
- Majibu yanayojali muktadha kupitia mizunguko ya mazungumzo
- Muundo unaoweza kupanuliwa kwa mifumo ya kuingiza utegemezi

## 📚 Ulinganisho wa Mfumo

Mfano huu unaonyesha mbinu ya Microsoft Agent Framework ikilinganishwa na mifumo mingine ya wakala:

| Kipengele | Microsoft Agent Framework | Mifumo Mengine |
|---------|-------------------------|------------------|
| **Uunganisho** | Mfumo wa asili wa Microsoft | Ulinganifu tofauti |
| **Urahisi** | API safi, rahisi kuelewa | Mara nyingi usanidi mgumu |
| **Upanuzi** | Uunganisho rahisi wa zana | Inategemea mfumo |
| **Tayari kwa Biashara** | Iliyojengwa kwa uzalishaji | Inatofautiana kwa mfumo |

## 🚀 Kuanzia

### Mahitaji Kabla ya Kuanza

- [SDK ya .NET 10](https://dotnet.microsoft.com/download/dotnet/10.0) au zaidi
- [Usajili wa Azure](https://azure.microsoft.com/free/) wenye rasilimali ya Azure OpenAI na utumaji wa mfano
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — ingia na `az login`

### Mabadiliko ya Mazingira Yanayohitajika

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Kisha ingia ili AzureCliCredential ipate tokeni
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Kisha ingia ili AzureCliCredential ipate tokeni
az login
```

### Mfano wa Msimbo

Ili kuendesha mfano wa msimbo,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Au kutumia dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Angalia [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) kwa msimbo kamili.

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

## 🎓 Muhimu wa Kuchukua

1. **Majaribio ya Wakala**: Microsoft Agent Framework hutoa njia safi na salama ya aina ya kujenga mawakala wa AI katika .NET
2. **Uunganisho wa Zana**: Kazi zilizoandikwa na sifa za `[Description]` zinakuwa zana zinazopatikana kwa wakala
3. **Muktadha wa Mazungumzo**: Usimamizi wa mizunguko huruhusu mazungumzo ya mizunguko mingi yenye ufahamu kamili wa muktadha
4. **Usimamizi wa Usanidi**: Vigezo vya mazingira na usimamizi salama wa nyaraka hufuata mbinu bora za .NET
5. **Azure OpenAI Responses API**: Wakala hutumia Azure OpenAI Responses API kupitia Azure.AI.OpenAI SDK

## 🔗 Rasilimali Zaidi

- [Nyaraka za Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI katika Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [Programu za Faili Moja za .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->