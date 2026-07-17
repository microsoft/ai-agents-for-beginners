# 🔍 மைக்ரோசாப்ட் ஏஜென்ட் ஃப்ரேம்வொர்க் ஆராய்ச்சி - அடிப்படைக் ஏஜென்ட் (.NET)

## 📋 கற்றல் குறிக்கோள்கள்

இந்த உதாரணம் .NET-இல் அடிப்படைக் ஏஜென்ட் செயல்பாட்டின் மூலம் மைக்ரோசாப்ட் ஏஜென்ட் ஃப்ரேம்வொர்க் அடிப்படை கருத்துகளை ஆய்வு செய்கிறது. நீங்கள் முக்கிய ஏஜென்ட் வடிவங்களை கற்றுக்கொள்வீர்கள் மற்றும் C# மற்றும் .NET சூழலை பயன்படுத்தி புத்திசாலி ஏஜென்ட்கள் எப்படி வேலை செய்கிறார்கள் என்பதை புரிந்துகொள்வீர்கள்.

### நீங்கள் என்ன காணப்போகிறீர்கள்

- 🏗️ **ஏஜென்ட் கட்டமைப்பு**: .NET‑இல் AI ஏஜென்ட்கள் அடிப்படை அமைப்பை புரிந்துகொண்டு
- 🛠️ **கருவி ஒருங்கிணைவு**: திறன்களை விரிவாக்க ஏஜென்ட்கள் வெளிப்புற செயல்பாடுகளைப் எப்படி பயன்படுத்துகிறார்கள்  
- 💬 **संवाद ஓட்டம்**: மின்னணு உரையாடல் மற்றும் தொடரின் மேலாண்மை மூலம் பன்முறை உரையாடலை நிர்வகித்தல்
- 🔧 **கட்டமைப்பு வடிவங்கள்**: .NET-இல் ஏஜென்ட் அமைப்பு மற்றும் நிர்வாகத்துக்கான சிறந்த நடைமுறைகள்

## 🎯 முக்கிய கருத்துகள்

### ஏஜென்டிக் ஃப்ரேம்வொர்க் தத்துவங்கள்

- **சுதந்திரம்**: .NET AI கட்டமைப்புகளைப் பயன்படுத்தி ஏஜென்ட்கள் தன்னிச்சையாக தீர்மானங்களை எடுக்கும் விதம்
- **பதிலளிப்பு**: சுற்றுப்புற மாற்றங்கள் மற்றும் பயனர் உள்ளீடுகளுக்கு பதிலளித்தல்
- **முன்னெச்சரிக்கை**: குறிக்கோள்கள் மற்றும் சூழல் அடிப்படையில் முனைப்பை எடுத்துக்கொள்வது
- **சாமூலி திறன்**: உரையாடல் தொடர்களுடன் இயற்கை மொழியாக தொடர்பு கொள்வது

### தொழில்நுட்ப கூறுகள்

- **AIAgent**: கோர் ஏஜென்ட் ஒருங்குறி மற்றும் உரையாடல் மேலாண்மை (.NET)
- **கருவி செயல்பாடுகள்**: C# முறைகள் மற்றும் பண்புகளோடு ஏஜென்ட் திறன்களை விரிவாக்கல்
- **Azure OpenAI ஒருங்கிணைவு**: Azure OpenAI Responses API மூலமாக மொழி மாதிரிகளை பயன்படுத்தல்
- **பாதுகாப்பான கட்டமைப்பு**: சூழல் அடிப்படையிலான எண்ட்பாயிண்ட் மேலாண்மை

## 🔧 தொழில்நுட்ப மேடைகள்

### முக்கிய தொழில்நுட்பங்கள்

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) ஒருங்கிணைவு
- Azure.AI.OpenAI கிளையண்ட் வடிவங்கள்
- DotNetEnv-ஐப் பயன்படுத்தி சூழல் அடிப்படையிலான கட்டமைப்பு

### ஏஜென்ட் திறன்கள்

- இயற்கை மொழி புரிதல் மற்றும் உருவாக்கல்
- C# பண்புகளுடன் செயல்பாடு அழைப்பு மற்றும் கருவி பயன்பாடு
- உரையாடல் அமர்வுகளோடு சூழல் விழிப்புடன் பதில்கள்
- நேர்மை பொருத்தம் வடிவமைப்புகளோடு விரிவாக்கக்கூடிய கட்டமைப்பு

## 📚 ஃப்ரேம்வொர்க் ஒப்பீடு

இந்த உதாரணம் மைக்ரோசாப்ட் ஏஜென்ட் ஃப்ரேம்வொர்குக்கு பிற ஏஜென்டிக் ஃப்ரேம்வொர்க்களுடன் ஒப்பிடும் முறையை காட்டுகிறது:

| அம்சம் | Microsoft Agent Framework | பிற ஃப்ரேம்வொர்க்கள் |
|---------|-------------------------|------------------|
| **ஒலிைவு** | செல்லுபடியாகும் மைக்ரோசாப்ட் சூழல் | பல்வேறு பொருத்தங்கள் |
| **எளிமை** | சுத்தமான, பரிமாற்றமுள்ள API | பெரும்பாலும் சிக்கலான அமைப்பு |
| **விரிவாக்கம்** | எளிதான கருவி ஒருங்கிணைவு | ஃப்ரேம்வொர்க் சார்ந்தது |
| **நிறுவன தயாரிப்பு** | உற்பத்திக்கான கட்டமைப்பு | ஃப்ரேம்வொர்க்கின் படி மாறுபடும் |

## 🚀 தொடங்குதல்

### தேவையான முன்னோட்டங்கள்

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) அல்லது அதற்கு மேலான பதிப்பு
- [Azure சந்தா](https://azure.microsoft.com/free/) ஒன்றுடன் Azure OpenAI வளமும் மாதிரி அமைப்பும்
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` மூலம் உள்நுழைவு

### தேவையான சூழல் மாறிலிகள்

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# பிறகு AzureCliCredential ஒரு டோக்கனை பெற உள்நுழையவும்
az login
```

```powershell
# பவர் ஷெல்
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# பின்னர் AzureCliCredential ஒரு டோக்கன் பெறுவதற்கு உள்நுழைக
az login
```

### மாதிரி குறியீடு

குறியீடு உதாரணத்தை இயக்க,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

அல்லது dotnet CLI பயன்படுத்தி:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

முழுமையான குறியீட்டுக்காக [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) ஐப் பாருங்கள்.

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

## 🎓 முக்கியப் பாடங்கள்

1. **ஏஜென்ட் கட்டமைப்பு**: மைக்ரோசாப்ட் ஏஜென்ட் ஃப்ரேம்வொர்க் .NET‑இல் AI ஏஜென்ட்களை நிர்மிக்க சுத்தமான, வகுப்புகாப்புள்ள அணுகுமுறையை வழங்குகிறது
2. **கருவி ஒருங்கிணைவு**: `[Description]` பண்புடன் அலங்கரிக்கப்பட்ட செயல்பாடுகள் ஏஜென்டிற்கான கிடைக்கும் கருவிகளாக மாறுகின்றன
3. **உரையாடல் சூழல்**: அமர்வு மேலாண்மை முழு சூழல் விழிப்புடன் பன்முறை உரையாடல்களை இயக்குகிறது
4. **கட்டமைப்பு மேலாண்மை**: சூழல் மாறிலிகள் மற்றும் பாதுகாப்பான சான்றிதழ் கையாளுதல் .NET சிறந்த நடைமுறைகளுக்கு ஏற்ப உள்ளது
5. **Azure OpenAI Responses API**: ஏஜென்ட் Azure.AI.OpenAI SDK மூலமாக Azure OpenAI Responses API-யைப் பயன்படுத்துகிறது

## 🔗 கூடுதல் வளங்கள்

- [Microsoft Agent Framework ஆவணம்](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry-இல் Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET ஒற்றை கோப்பு பயன்பாடுகள்](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->