<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-12-03T17:09:22+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "te"
}
-->
# 🔍 మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ - బేసిక్ ఏజెంట్ (.NET) అన్వేషణ

## 📋 నేర్చుకునే లక్ష్యాలు

ఈ ఉదాహరణ .NET లో బేసిక్ ఏజెంట్ అమలుతో మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ యొక్క ప్రాథమిక భావాలను అన్వేషిస్తుంది. మీరు ప్రధాన ఏజెంటిక్ నమూనాలను నేర్చుకుంటారు మరియు C# మరియు .NET ఎకోసిస్టమ్ ఉపయోగించి తెలివైన ఏజెంట్లు ఎలా పనిచేస్తాయో అర్థం చేసుకుంటారు.

### మీరు ఏమి కనుగొంటారు

- 🏗️ **ఏజెంట్ ఆర్కిటెక్చర్**: .NET లో AI ఏజెంట్ల ప్రాథమిక నిర్మాణాన్ని అర్థం చేసుకోవడం  
- 🛠️ **టూల్ ఇంటిగ్రేషన్**: ఏజెంట్లు సామర్థ్యాలను విస్తరించడానికి బాహ్య ఫంక్షన్లను ఎలా ఉపయోగిస్తారు  
- 💬 **కాన్వర్సేషన్ ఫ్లో**: థ్రెడ్ మేనేజ్‌మెంట్‌తో బహుళ-మలుపు సంభాషణలు మరియు సందర్భాన్ని నిర్వహించడం  
- 🔧 **కాన్ఫిగరేషన్ ప్యాటర్న్స్**: .NET లో ఏజెంట్ సెటప్ మరియు నిర్వహణకు ఉత్తమ పద్ధతులు

## 🎯 కీ కాన్సెప్ట్‌లు

### ఏజెంటిక్ ఫ్రేమ్‌వర్క్ ప్రిన్సిపుల్స్

- **ఆటోనమీ**: .NET AI అబ్స్ట్రాక్షన్లను ఉపయోగించి ఏజెంట్లు స్వతంత్ర నిర్ణయాలు ఎలా తీసుకుంటాయి  
- **రియాక్టివిటీ**: పర్యావరణ మార్పులకు మరియు వినియోగదారు ఇన్‌పుట్‌లకు ప్రతిస్పందించడం  
- **ప్రోయాక్టివిటీ**: లక్ష్యాలు మరియు సందర్భం ఆధారంగా ముందుకు తీసుకోవడం  
- **సోషల్ ఎబిలిటీ**: సంభాషణ థ్రెడ్‌లతో సహజ భాష ద్వారా పరస్పర చర్య

### టెక్నికల్ భాగాలు

- **AIAgent**: కోర్ ఏజెంట్ ఆర్కెస్ట్రేషన్ మరియు సంభాషణ నిర్వహణ (.NET)  
- **టూల్ ఫంక్షన్లు**: C# పద్ధతులు మరియు అట్రిబ్యూట్లతో ఏజెంట్ సామర్థ్యాలను విస్తరించడం  
- **OpenAI ఇంటిగ్రేషన్**: ప్రామాణిక .NET APIs ద్వారా భాషా మోడళ్లను ఉపయోగించడం  
- **సెక్యూర్ కాన్ఫిగరేషన్**: వాతావరణ ఆధారిత API కీ నిర్వహణ

## 🔧 టెక్నికల్ స్టాక్

### ప్రధాన టెక్నాలజీలు

- మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ (.NET)  
- GitHub మోడల్స్ API ఇంటిగ్రేషన్  
- OpenAI-కంపాటిబుల్ క్లయింట్ ప్యాటర్న్స్  
- DotNetEnv తో వాతావరణ ఆధారిత కాన్ఫిగరేషన్

### ఏజెంట్ సామర్థ్యాలు

- సహజ భాషను అర్థం చేసుకోవడం మరియు ఉత్పత్తి చేయడం  
- C# అట్రిబ్యూట్లతో ఫంక్షన్ కాలింగ్ మరియు టూల్ వినియోగం  
- సంభాషణ థ్రెడ్‌లతో సందర్భం-అవగాహన ప్రతిస్పందనలు  
- డిపెండెన్సీ ఇంజెక్షన్ ప్యాటర్న్స్‌తో విస్తరించగల ఆర్కిటెక్చర్

## 📚 ఫ్రేమ్‌వర్క్ పోలిక

ఈ ఉదాహరణ ఇతర ఏజెంటిక్ ఫ్రేమ్‌వర్క్‌లతో పోల్చినప్పుడు మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ దృక్పథాన్ని ప్రదర్శిస్తుంది:

| ఫీచర్ | మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ | ఇతర ఫ్రేమ్‌వర్క్‌లు |
|---------|-------------------------|------------------|
| **ఇంటిగ్రేషన్** | మైక్రోసాఫ్ట్ ఎకోసిస్టమ్‌కు స్వదేశీ | వివిధ అనుకూలత |
| **సింప్లిసిటీ** | క్లీన్గా, ఇంట్యూయిటివ్ API | తరచుగా క్లిష్టమైన సెటప్ |
| **ఎక్స్‌టెన్సిబిలిటీ** | టూల్ ఇంటిగ్రేషన్ సులభం | ఫ్రేమ్‌వర్క్ ఆధారిత |
| **ఎంటర్‌ప్రైజ్ రెడీ** | ప్రొడక్షన్ కోసం రూపొందించబడింది | ఫ్రేమ్‌వర్క్ ఆధారంగా మారుతుంది |

## 🚀 ప్రారంభం

### అవసరమైనవి

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) లేదా అంతకంటే ఎక్కువ  
- [GitHub మోడల్స్ API యాక్సెస్ టోకెన్](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)

### అవసరమైన వాతావరణ వేరియబుల్స్

```bash
# zsh/bash
export GH_TOKEN=<your_github_token>
export GH_ENDPOINT=https://models.github.ai/inference
export GH_MODEL_ID=openai/gpt-5-mini
```
  
```powershell
# పవర్‌షెల్
$env:GH_TOKEN = "<your_github_token>"
$env:GH_ENDPOINT = "https://models.github.ai/inference"
$env:GH_MODEL_ID = "openai/gpt-5-mini"
```
  

### నమూనా కోడ్

కోడ్ ఉదాహరణను అమలు చేయడానికి,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
లేదా dotnet CLI ఉపయోగించి:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
మొత్తం కోడ్ కోసం [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) చూడండి.

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
  

## 🎓 ముఖ్యమైన విషయాలు

1. **ఏజెంట్ ఆర్కిటెక్చర్**: మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ .NET లో AI ఏజెంట్లను నిర్మించడానికి శుభ్రమైన, టైప్-సేఫ్ దృక్పథాన్ని అందిస్తుంది  
2. **టూల్ ఇంటిగ్రేషన్**: `[Description]` అట్రిబ్యూట్లతో అలంకరించిన ఫంక్షన్లు ఏజెంట్‌కు అందుబాటులో ఉన్న టూల్స్‌గా మారతాయి  
3. **కాన్వర్సేషన్ కాంటెక్స్ట్**: థ్రెడ్ మేనేజ్‌మెంట్ బహుళ-మలుపు సంభాషణలను పూర్తి సందర్భ అవగాహనతో సాధ్యమవుతుంది  
4. **కాన్ఫిగరేషన్ మేనేజ్‌మెంట్**: వాతావరణ వేరియబుల్స్ మరియు సురక్షిత క్రెడెన్షియల్ నిర్వహణ .NET ఉత్తమ పద్ధతులను అనుసరిస్తుంది  
5. **OpenAI కంపాటిబిలిటీ**: GitHub మోడల్స్ ఇంటిగ్రేషన్ OpenAI-కంపాటిబుల్ APIs ద్వారా సజావుగా పనిచేస్తుంది  

## 🔗 అదనపు వనరులు

- [మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ డాక్యుమెంటేషన్](https://learn.microsoft.com/agent-framework)  
- [GitHub మోడల్స్ మార్కెట్‌ప్లేస్](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET సింగిల్ ఫైల్ యాప్స్](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**విమర్శ**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించారు. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలలో తప్పులు లేదా అసమగ్రతలు ఉండవచ్చు. దయచేసి, దాని స్వదేశీ భాషలోని అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించండి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదాన్ని ఉపయోగించడం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->