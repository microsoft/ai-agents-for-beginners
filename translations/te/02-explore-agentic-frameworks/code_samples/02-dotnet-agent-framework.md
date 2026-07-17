# 🔍 మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ అన్వేషణ - బేసిక్ ఏజెంట్ (.NET)

## 📋 నేర్చుకునే లక్ష్యాలు

ఈ ఉదాహరణ .NET లో ఒక బేసిక్ ఏజెంట్ అమలు ద్వారా మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ యొక్క ప్రాథమిక సిద్ధాంతాలను అన్వేషిస్తుంది. మీరు మౌలిక ఏజెంటిక్ నమూనాలను నేర్చుకుంటారు మరియు C# మరియు .NET పరిసర వ్యవస్థ ఉపయోగించి తెలివైన ఏజెంట్లు ఎలా పని చేస్తాయో అర్థం చేసుకుంటారు.

### మీరు ఏమి కనుగొంటారు

- 🏗️ **ఏజెంట్ వాస్తుశిల్పం**: .NET లో AI ఏజెంట్ల ప్రాథమిక నిర్మాణాన్ని అర్థం చేసుకోవడం
- 🛠️ **టూల్ ఇంటిగ్రేషన్**: ఏజెంట్లు సామర్థ్యాలను విస్తరించడానికి బాహ్య ఫంక్షన్లను ఎలా ఉపయోగిస్తాయో  
- 💬 ** సంభాషణ ప్రవాహం**: బహు-తిరుగుబాటు సంభాషణలు మరియు థ్రెడ్ నిర్వహణతో సందర్భం నిర్వహించడం
- 🔧 **గుండ్రటి నమూనాలు**: .NET లో ఏజెంట్ సెటప్ మరియు నిర్వహణకు ఉత్తమ పద్ధతులు

## 🎯 కీ సిద్ధాంతాలు కవర్ చేయబడినవి

### ఏజెంటిక్ ఫ్రేమ్‌వర్క్ సిద్దాంతాలు

- **స్వతంత్రత**: .NET AI ఆబ్స్ట్రాక్షన్లను ఉపయోగించి ఏజెంట్లు స్వతంత్ర నిర్ణయాలు తీసుకొనే విధానం
- **ప్రతిస్పందన శీలత**: పర్యావరణ మార్పులు మరియు వినియోగదారుల ఇన్‌పుట్‌లకు స్పందించడం
- **ప్రవాహశీలత**: లక్ష్యాలు మరియు సందర్భం ఆధారంగా పతిష్ట తీసుకోవడం
- **సామాజిక సామర్ధ్యం**: సంభాషణ థ్రెడ్‌లతో సహజ భాష ద్వారా పరస్పర చర్య

### సాంకేతిక భాగాలు

- **AIAgent**: ముఖ్య ఏజెంట్ ఒర్కెస్ట్రేషన్ మరియు సంభాషణ నిర్వహణ (.NET)
- **టూల్ ఫంక్షన్లు**: C# మెథడ్లు మరియు లక్షణాలతో ఏజెంట్ సామర్థ్యాలను విస్తరించడం
- **Azure OpenAI ఇంటిగ్రేషన్**: Azure OpenAI Responses API ద్వారా భాషా మోడల్స్ ను వినియోగించడం
- **సురక్షిత కాన్ఫిగరేషన్**: పర్యావరణ ఆధారిత ఎండ్‌పాయింట్ నిర్వహణ

## 🔧 సాంకేతిక స్టాక్

### కోర్ సాంకేతికతలు

- మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ (.NET)
- Azure OpenAI (Responses API) ఇంటిగ్రేషన్
- Azure.AI.OpenAI క్లయింట్ నమూనాలు
- DotNetEnv తో పర్యావరణాధారిత కాన్ఫిగరేషన్

### ఏజెంట్ సామర్థ్యాలు

- సహజ భాషా అర్థం మరియు సృష్టి
- ఫంక్షన్ కాలింగ్ మరియు C# లక్షణాలతో సాధనాల వినియోగం
- సంభాషణ సెషన్‌లతో సందర్భాన్ని తెలుసుకుని స్పందనలు
- డిపెండెన్సీ ఇంజెక్షన్ నమూనాలతో విస్తరణౌగ్య వాస్తుశిల్పం

## 📚 ఫ్రేమ్‌వర్క్ పోలిక

ఈ ఉదాహరణ ఇతర ఏజెంటిక్ ఫ్రేమ్‌వర్క్‌లతో సరిపోల్చినప్పుడు మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ దృష్టికోణాన్ని చూపిస్తుంది:

| ఫీచర్ | మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ | ఇతర ఫ్రేమ్‌వర్క్‌లు |
|---------|-------------------------|------------------|
| **ఇంటిగ్రేషన్** | స్థానిక మైక్రోసాఫ్ట్ పరిసర వ్యవస్థ | వేరువేరు అనుకూలత |
| **సాదాసీదాగా ఉండటం** | క్లియర్, సులభమైన API | తరచుగా క్లిష్ట సెటప్ |
| **విస్తరణ సామర్ధ్యం** |/tool సమగ్రత సులభం | ఫ్రేమ్‌వర్క్ ఆధారితం |
| **ఎంటర్‌ప్రైజ్ రెడీ** | ఉత్పత్తికి రూపొందించినది | ఫ్రేమ్‌వర్క్ ఆధారంగా మార్తుంది |

## 🚀 ప్రారంభించడం

### ముందస్తు అవసరాలు

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) లేదా అంతకు మించి
- Azure OpenAI వనరుతో Azure సబ్‌స్క్రిప్షన్ ([Azure subscription](https://azure.microsoft.com/free/)) మరియు ఒక మోడల్ డిప్లాయ్‌మెంట్
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` తో సైన్ ఇన్ చేయండి

### అవసరమైన పర్యావరణ వేరియబుల్స్

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# ఆపై AzureCliCredential టోకెన్ పొందడానికి సైన్ ఇన్ అవ్వండి
az login
```

```powershell
# పవర్‌షెల్
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# ఆపై AzureCliCredential టోకెన్ పొందడానికి సైన్ ఇన్ చేయండి
az login
```

### నమూనా కోడ్

కోడ్ ఉదాహరణను నడపడానికి,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

లేక dotnet CLI ఉపయోగించి:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

పూర్తి కోడ్ కోసం [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) చూడండి.

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

## 🎓 ముఖ్యమైన మూలాలను

1. **ఏజెంట్ వాస్తుశిల్పం**: మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ .NET లో AI ఏజెంట్లను నిర్మించడానికి శుభ్రమైన, టైప్-సురక్షిత దృక్పథాన్ని అందిస్తుందని
2. **టూల్ ఇంటిగ్రేషన్**: `[Description]` లక్షణాలతో అలంకరించిన ఫంక్షన్లు ఏజెంట్ కోసం అందుబాటులో ఉన్న సాధనాలు అవుతాయి
3. **సంభాషణ సందర్భం**: సెషన్ నిర్వహణ పూర్తి సందర్భ అవగాహనతో బహుళ-తిరుగుబాటు సంభాషణలను అనుమతిస్తుంది
4. **కాన్ఫిగరేషన్ నిర్వహణ**: పర్యావరణ వేరియబుల్స్ మరియు సురక్షిత క్రెడెన్షియల్స్ నిర్వహణ .NET ఉత్తమ ఆచారాలను అనుసరిస్తుంది
5. **Azure OpenAI Responses API**: ఏజెంట్ Azure.AI.OpenAI SDK ద్వారా Azure OpenAI Responses API ని ఉపయోగిస్తుంది

## 🔗 అదనపు వనరులు

- [Microsoft Agent Framework డాక్యుమెంటేషన్](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundryలో Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET సింగిల్ ఫైల్ యాప్స్](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->