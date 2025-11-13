<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T14:53:38+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "ta"
}
-->
# 🔍 Microsoft Agent Framework - அடிப்படை Agent (.NET) ஆராய்ச்சி

## 📋 கற்றல் நோக்கங்கள்

இந்த எடுத்துக்காட்டில் Microsoft Agent Framework-இன் அடிப்படை கருத்துகளை .NET-இல் ஒரு அடிப்படை Agent செயல்பாட்டின் மூலம் ஆராய்கிறோம். C# மற்றும் .NET சூழலில் நுண்ணறிவு Agent-கள் எப்படி செயல்படுகின்றன என்பதை நீங்கள் புரிந்துகொள்வீர்கள்.

### நீங்கள் கண்டறியப்போகிறீர்கள்

- 🏗️ **Agent கட்டமைப்பு**: .NET-இல் AI Agent-களின் அடிப்படை அமைப்பை புரிந்துகொள்வது  
- 🛠️ **கருவி ஒருங்கிணைப்பு**: Agent-கள் திறன்களை விரிவாக்க வெளிப்புற செயல்பாடுகளை எப்படி பயன்படுத்துகின்றன  
- 💬 **உரையாடல் ஓட்டம்**: பல முறை உரையாடல்களை மற்றும் சூழலை த_thread_ மேலாண்மையுடன் நிர்வகிக்க  
- 🔧 **கட்டமைப்பு முறை**: .NET-இல் Agent அமைப்பு மற்றும் மேலாண்மைக்கான சிறந்த நடைமுறைகள்  

## 🎯 முக்கிய கருத்துகள்

### Agent Framework கொள்கைகள்

- **தன்னாட்சி**: .NET AI சுருக்கங்களைப் பயன்படுத்தி Agent-கள் சுயமாக முடிவுகளை எடுப்பது  
- **செயல்திறன்**: சூழல் மாற்றங்கள் மற்றும் பயனர் உள்ளீடுகளுக்கு பதிலளிக்க  
- **முன்னோடி செயல்பாடு**: இலக்குகள் மற்றும் சூழலின் அடிப்படையில் முன்வருவது  
- **சமூக திறன்**: உரையாடல் த_thread_களின் மூலம் இயற்கை மொழியில் தொடர்பு கொள்ள  

### தொழில்நுட்ப கூறுகள்

- **AIAgent**: Agent ஒருங்கிணைப்பு மற்றும் உரையாடல் மேலாண்மை (.NET)  
- **Tool Functions**: C# முறை மற்றும் பண்புகளுடன் Agent திறன்களை விரிவாக்குதல்  
- **OpenAI ஒருங்கிணைப்பு**: .NET API-களின் மூலம் மொழி மாதிரிகளைப் பயன்படுத்துதல்  
- **பாதுகாப்பான கட்டமைப்பு**: சூழல் அடிப்படையிலான API விசை மேலாண்மை  

## 🔧 தொழில்நுட்ப அடுக்குகள்

### முக்கிய தொழில்நுட்பங்கள்

- Microsoft Agent Framework (.NET)  
- GitHub Models API ஒருங்கிணைப்பு  
- OpenAI-இன் இணக்கமான கிளையன்ட் முறை  
- DotNetEnv மூலம் சூழல் அடிப்படையிலான கட்டமைப்பு  

### Agent திறன்கள்

- இயற்கை மொழி புரிதல் மற்றும் உருவாக்கம்  
- C# பண்புகளுடன் செயல்பாடுகளை அழைப்பது மற்றும் கருவிகளைப் பயன்படுத்துதல்  
- உரையாடல் த_thread_களுடன் சூழல்-அறிந்த பதில்கள்  
- சார்பு ஊடுருவல் முறைகளுடன் விரிவாக்கக்கூடிய கட்டமைப்பு  

## 📚 Framework ஒப்பீடு

இந்த எடுத்துக்காட்டில் Microsoft Agent Framework-இன் அணுகுமுறை மற்ற Framework-களுடன் ஒப்பிடப்படுகிறது:

| அம்சம் | Microsoft Agent Framework | மற்ற Framework-கள் |
|---------|-------------------------|------------------|
| **ஒருங்கிணைப்பு** | Microsoft சூழல் | மாறுபட்ட இணக்கத்தன்மை |
| **எளிமை** | சுத்தமான, எளிதான API | அடிக்கடி சிக்கலான அமைப்பு |
| **விரிவாக்கம்** | எளிதான கருவி ஒருங்கிணைப்பு | Framework-இல் சார்ந்தது |
| **நிறுவனத்திற்கான தயாரிப்பு** | உற்பத்திக்கானது | Framework-இல் மாறுபடும் |

## 🚀 தொடங்குதல்

### முன் தேவைகள்

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) அல்லது அதற்கு மேல்  
- [GitHub Models API அணுகல் குறியீடு](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### தேவையான சூழல் மாறிகள்

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
  

### மாதிரி குறியீடு

குறியீடு எடுத்துக்காட்டை இயக்க,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
அல்லது dotnet CLI-யைப் பயன்படுத்தி:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
முழு குறியீட்டிற்கான [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) ஐப் பார்க்கவும்.

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
  

## 🎓 முக்கியக் குறிப்புகள்

1. **Agent கட்டமைப்பு**: Microsoft Agent Framework .NET-இல் AI Agent-களை உருவாக்க சுத்தமான, வகை-பாதுகாப்பான அணுகுமுறையை வழங்குகிறது  
2. **கருவி ஒருங்கிணைப்பு**: `[Description]` பண்புகளுடன் அலங்கரிக்கப்பட்ட செயல்பாடுகள் Agent-க்கு கிடைக்கும் கருவிகளாக மாறுகின்றன  
3. **உரையாடல் சூழல்**: த_thread_ மேலாண்மை முழு சூழல்-அறிந்த பல முறை உரையாடல்களை இயக்குகிறது  
4. **கட்டமைப்பு மேலாண்மை**: சூழல் மாறிகள் மற்றும் பாதுகாப்பான சான்று கையாளுதல் .NET சிறந்த நடைமுறைகளைப் பின்பற்றுகிறது  
5. **OpenAI இணக்கத்தன்மை**: GitHub Models ஒருங்கிணைப்பு OpenAI-இன் இணக்கமான API-களின் மூலம் சீராக செயல்படுகிறது  

## 🔗 கூடுதல் வளங்கள்

- [Microsoft Agent Framework ஆவணங்கள்](https://learn.microsoft.com/agent-framework)  
- [GitHub Models சந்தை](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET ஒற்றை கோப்பு பயன்பாடுகள்](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->