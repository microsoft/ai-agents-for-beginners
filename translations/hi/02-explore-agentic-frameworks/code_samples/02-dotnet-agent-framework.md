<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T11:41:13+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "hi"
}
-->
# 🔍 Microsoft Agent Framework - बेसिक एजेंट (.NET) का अन्वेषण

## 📋 सीखने के उद्देश्य

यह उदाहरण Microsoft Agent Framework के मूलभूत अवधारणाओं को .NET में एक बेसिक एजेंट के कार्यान्वयन के माध्यम से समझाता है। आप मुख्य एजेंटिक पैटर्न सीखेंगे और समझेंगे कि C# और .NET इकोसिस्टम का उपयोग करके बुद्धिमान एजेंट कैसे काम करते हैं।

### आप क्या जानेंगे

- 🏗️ **एजेंट आर्किटेक्चर**: .NET में AI एजेंट्स की बुनियादी संरचना को समझना  
- 🛠️ **टूल इंटीग्रेशन**: एजेंट्स बाहरी फंक्शन्स का उपयोग करके अपनी क्षमताओं को कैसे बढ़ाते हैं  
- 💬 **संवाद प्रवाह**: मल्टी-टर्न संवाद और थ्रेड प्रबंधन के साथ संदर्भ को संभालना  
- 🔧 **कॉन्फ़िगरेशन पैटर्न**: .NET में एजेंट सेटअप और प्रबंधन के लिए सर्वोत्तम प्रथाएं  

## 🎯 कवर किए गए मुख्य अवधारणाएं

### एजेंटिक फ्रेमवर्क सिद्धांत

- **स्वायत्तता**: .NET AI अमूर्तताओं का उपयोग करके एजेंट्स स्वतंत्र निर्णय कैसे लेते हैं  
- **प्रतिक्रियाशीलता**: पर्यावरणीय परिवर्तनों और उपयोगकर्ता इनपुट्स पर प्रतिक्रिया देना  
- **प्रोएक्टिविटी**: लक्ष्यों और संदर्भ के आधार पर पहल करना  
- **सामाजिक क्षमता**: संवाद थ्रेड्स के माध्यम से प्राकृतिक भाषा में बातचीत करना  

### तकनीकी घटक

- **AIAgent**: मुख्य एजेंट ऑर्केस्ट्रेशन और संवाद प्रबंधन (.NET)  
- **टूल फंक्शन्स**: C# मेथड्स और एट्रिब्यूट्स के साथ एजेंट क्षमताओं का विस्तार  
- **OpenAI इंटीग्रेशन**: मानकीकृत .NET APIs के माध्यम से भाषा मॉडल्स का उपयोग  
- **सुरक्षित कॉन्फ़िगरेशन**: पर्यावरण-आधारित API कुंजी प्रबंधन  

## 🔧 तकनीकी स्टैक

### मुख्य तकनीकें

- Microsoft Agent Framework (.NET)  
- GitHub Models API इंटीग्रेशन  
- OpenAI-संगत क्लाइंट पैटर्न  
- DotNetEnv के साथ पर्यावरण-आधारित कॉन्फ़िगरेशन  

### एजेंट क्षमताएं

- प्राकृतिक भाषा को समझना और उत्पन्न करना  
- C# एट्रिब्यूट्स के साथ फंक्शन कॉलिंग और टूल उपयोग  
- संवाद थ्रेड्स के साथ संदर्भ-संवेदनशील प्रतिक्रियाएं  
- निर्भरता इंजेक्शन पैटर्न के साथ विस्तारित आर्किटेक्चर  

## 📚 फ्रेमवर्क तुलना

यह उदाहरण Microsoft Agent Framework दृष्टिकोण को अन्य एजेंटिक फ्रेमवर्क्स के साथ तुलना करता है:

| विशेषता | Microsoft Agent Framework | अन्य फ्रेमवर्क्स |
|---------|-------------------------|------------------|
| **इंटीग्रेशन** | नेटिव Microsoft इकोसिस्टम | विविध संगतता |
| **सरलता** | साफ़, सहज API | अक्सर जटिल सेटअप |
| **विस्तारशीलता** | आसान टूल इंटीग्रेशन | फ्रेमवर्क-निर्भर |
| **एंटरप्राइज रेडी** | उत्पादन के लिए निर्मित | फ्रेमवर्क के अनुसार भिन्न |

## 🚀 शुरुआत करना

### आवश्यकताएं

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) या उच्चतर  
- [GitHub Models API एक्सेस टोकन](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### आवश्यक पर्यावरण वेरिएबल्स

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
  

### नमूना कोड

कोड उदाहरण चलाने के लिए,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
या dotnet CLI का उपयोग करके:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
पूरा कोड [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) में देखें।

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
  

## 🎓 मुख्य निष्कर्ष

1. **एजेंट आर्किटेक्चर**: Microsoft Agent Framework .NET में AI एजेंट्स बनाने के लिए एक साफ़, टाइप-सुरक्षित दृष्टिकोण प्रदान करता है  
2. **टूल इंटीग्रेशन**: `[Description]` एट्रिब्यूट्स के साथ सजाए गए फंक्शन्स एजेंट के लिए उपलब्ध टूल बन जाते हैं  
3. **संवाद संदर्भ**: थ्रेड प्रबंधन मल्टी-टर्न संवादों को पूर्ण संदर्भ जागरूकता के साथ सक्षम बनाता है  
4. **कॉन्फ़िगरेशन प्रबंधन**: पर्यावरण वेरिएबल्स और सुरक्षित क्रेडेंशियल हैंडलिंग .NET सर्वोत्तम प्रथाओं का पालन करते हैं  
5. **OpenAI संगतता**: GitHub Models इंटीग्रेशन OpenAI-संगत APIs के माध्यम से सहजता से काम करता है  

## 🔗 अतिरिक्त संसाधन

- [Microsoft Agent Framework दस्तावेज़](https://learn.microsoft.com/agent-framework)  
- [GitHub Models मार्केटप्लेस](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET सिंगल फाइल ऐप्स](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->