<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T11:52:58+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "mr"
}
-->
# 🔍 Microsoft Agent Framework - बेसिक एजंट (.NET) एक्सप्लोर करणे

## 📋 शिकण्याचे उद्दिष्ट

या उदाहरणामध्ये Microsoft Agent Framework च्या मूलभूत संकल्पनांचा अभ्यास .NET मधील बेसिक एजंटच्या अंमलबजावणीद्वारे केला जातो. तुम्ही मुख्य एजंटिक पॅटर्न शिकाल आणि C# आणि .NET इकोसिस्टम वापरून बुद्धिमान एजंट कसे कार्य करतात हे समजून घ्याल.

### तुम्ही काय शोधाल

- 🏗️ **एजंट आर्किटेक्चर**: .NET मधील AI एजंट्सची मूलभूत रचना समजून घेणे  
- 🛠️ **टूल इंटिग्रेशन**: एजंट्स कसे बाह्य फंक्शन्स वापरून क्षमता वाढवतात  
- 💬 **संवाद प्रवाह**: मल्टी-टर्न संवाद आणि थ्रेड व्यवस्थापनासह संदर्भ व्यवस्थापन  
- 🔧 **कॉन्फिगरेशन पॅटर्न्स**: .NET मध्ये एजंट सेटअप आणि व्यवस्थापनासाठी सर्वोत्तम पद्धती  

## 🎯 मुख्य संकल्पना

### Agentic Framework चे तत्त्व

- **स्वायत्तता**: .NET AI अब्स्ट्रॅक्शन्स वापरून एजंट्स स्वतंत्र निर्णय कसे घेतात  
- **प्रतिक्रियाशीलता**: पर्यावरणीय बदल आणि वापरकर्त्याच्या इनपुट्सला प्रतिसाद देणे  
- **प्रोएक्टिव्हिटी**: उद्दिष्टे आणि संदर्भावर आधारित पुढाकार घेणे  
- **सामाजिक क्षमता**: संवाद थ्रेड्ससह नैसर्गिक भाषेत संवाद साधणे  

### तांत्रिक घटक

- **AIAgent**: मुख्य एजंट ऑर्केस्ट्रेशन आणि संवाद व्यवस्थापन (.NET)  
- **टूल फंक्शन्स**: C# मेथड्स आणि अॅट्रिब्युट्ससह एजंट क्षमता वाढवणे  
- **OpenAI इंटिग्रेशन**: मानक .NET APIs द्वारे भाषा मॉडेल्सचा लाभ घेणे  
- **सुरक्षित कॉन्फिगरेशन**: पर्यावरण-आधारित API की व्यवस्थापन  

## 🔧 तांत्रिक स्टॅक

### मुख्य तंत्रज्ञान

- Microsoft Agent Framework (.NET)  
- GitHub Models API इंटिग्रेशन  
- OpenAI-सुसंगत क्लायंट पॅटर्न्स  
- DotNetEnv सह पर्यावरण-आधारित कॉन्फिगरेशन  

### एजंट क्षमता

- नैसर्गिक भाषा समज आणि निर्मिती  
- C# अॅट्रिब्युट्ससह फंक्शन कॉलिंग आणि टूल वापर  
- संवाद थ्रेड्ससह संदर्भ-जाणिवा प्रतिसाद  
- डिपेंडन्सी इंजेक्शन पॅटर्न्ससह विस्तारक्षम आर्किटेक्चर  

## 📚 फ्रेमवर्क तुलना

हे उदाहरण Microsoft Agent Framework चा दृष्टिकोन इतर एजंटिक फ्रेमवर्क्सशी तुलना करून दाखवते:

| वैशिष्ट्य | Microsoft Agent Framework | इतर फ्रेमवर्क्स |
|-----------|---------------------------|------------------|
| **इंटिग्रेशन** | नेटिव्ह Microsoft इकोसिस्टम | विविध सुसंगतता |
| **साधेपणा** | स्वच्छ, अंतर्ज्ञानी API | अनेकदा क्लिष्ट सेटअप |
| **विस्तारक्षमता** | सोपी टूल इंटिग्रेशन | फ्रेमवर्क-आधारित |
| **एंटरप्राइझ रेडी** | उत्पादनासाठी तयार | फ्रेमवर्कनुसार बदलते |

## 🚀 सुरुवात कशी करावी

### पूर्वतयारी

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) किंवा त्याहून अधिक  
- [GitHub Models API ऍक्सेस टोकन](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### आवश्यक पर्यावरणीय व्हेरिएबल्स

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
  

### नमुना कोड

कोड उदाहरण चालवण्यासाठी,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
किंवा dotnet CLI वापरून:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
संपूर्ण कोडसाठी [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) पहा.

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
  

## 🎓 मुख्य मुद्दे

1. **एजंट आर्किटेक्चर**: Microsoft Agent Framework .NET मध्ये AI एजंट्स तयार करण्यासाठी स्वच्छ, टाइप-सुरक्षित दृष्टिकोन प्रदान करते  
2. **टूल इंटिग्रेशन**: `[Description]` अॅट्रिब्युट्ससह सजवलेले फंक्शन्स एजंटसाठी उपलब्ध टूल्स बनतात  
3. **संवाद संदर्भ**: थ्रेड व्यवस्थापन मल्टी-टर्न संवादांसह पूर्ण संदर्भ-जाणिवा सक्षम करते  
4. **कॉन्फिगरेशन व्यवस्थापन**: पर्यावरणीय व्हेरिएबल्स आणि सुरक्षित क्रेडेन्शियल हाताळणी .NET च्या सर्वोत्तम पद्धतींचे अनुसरण करते  
5. **OpenAI सुसंगतता**: GitHub Models इंटिग्रेशन OpenAI-सुसंगत APIs द्वारे सहज कार्य करते  

## 🔗 अतिरिक्त संसाधने

- [Microsoft Agent Framework दस्तऐवज](https://learn.microsoft.com/agent-framework)  
- [GitHub Models मार्केटप्लेस](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET सिंगल फाइल अॅप्स](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपयास लक्षात ठेवा की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने युक्त असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->