<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T11:59:41+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "ne"
}
-->
# 🔍 माइक्रोसफ्ट एजेन्ट फ्रेमवर्क - आधारभूत एजेन्ट (.NET)

## 📋 सिक्ने उद्देश्यहरू

यो उदाहरणले माइक्रोसफ्ट एजेन्ट फ्रेमवर्कका आधारभूत अवधारणाहरूलाई .NET मा एक साधारण एजेन्ट कार्यान्वयन मार्फत अन्वेषण गर्दछ। तपाईंले मुख्य एजेन्टिक ढाँचाहरू सिक्नुहुनेछ र C# र .NET इकोसिस्टम प्रयोग गरेर बौद्धिक एजेन्टहरू कसरी काम गर्छन् भन्ने बुझ्नुहुनेछ।

### तपाईंले के पत्ता लगाउनुहुनेछ

- 🏗️ **एजेन्ट आर्किटेक्चर**: .NET मा AI एजेन्टहरूको आधारभूत संरचना बुझ्ने  
- 🛠️ **टूल एकीकरण**: एजेन्टहरूले क्षमताहरू विस्तार गर्न बाह्य कार्यहरू कसरी प्रयोग गर्छन्  
- 💬 **वार्तालाप प्रवाह**: थ्रेड व्यवस्थापनको साथ बहु-टर्न वार्तालाप र सन्दर्भ व्यवस्थापन  
- 🔧 **कन्फिगरेसन ढाँचाहरू**: .NET मा एजेन्ट सेटअप र व्यवस्थापनका लागि उत्कृष्ट अभ्यासहरू  

## 🎯 मुख्य अवधारणाहरू समेटिएका

### एजेन्टिक फ्रेमवर्क सिद्धान्तहरू

- **स्वायत्तता**: .NET AI अमूर्तता प्रयोग गरेर एजेन्टहरूले स्वतन्त्र निर्णय कसरी लिन्छन्  
- **प्रतिक्रियात्मकता**: वातावरणीय परिवर्तनहरू र प्रयोगकर्ता इनपुटहरूमा प्रतिक्रिया दिने  
- **सक्रियता**: लक्ष्य र सन्दर्भको आधारमा पहल लिने  
- **सामाजिक क्षमता**: वार्तालाप थ्रेडहरू मार्फत प्राकृतिक भाषामा अन्तरक्रिया गर्ने  

### प्राविधिक घटकहरू

- **AIAgent**: मुख्य एजेन्ट समन्वय र वार्तालाप व्यवस्थापन (.NET)  
- **टूल फङ्क्सनहरू**: C# विधिहरू र विशेषताहरूको साथ एजेन्ट क्षमताहरू विस्तार गर्ने  
- **OpenAI एकीकरण**: मानकीकृत .NET API मार्फत भाषा मोडेलहरू प्रयोग गर्ने  
- **सुरक्षित कन्फिगरेसन**: वातावरण-आधारित API कुञ्जी व्यवस्थापन  

## 🔧 प्राविधिक स्ट्याक

### मुख्य प्रविधिहरू

- माइक्रोसफ्ट एजेन्ट फ्रेमवर्क (.NET)  
- GitHub Models API एकीकरण  
- OpenAI-संगत क्लाइन्ट ढाँचाहरू  
- DotNetEnv को साथ वातावरण-आधारित कन्फिगरेसन  

### एजेन्ट क्षमताहरू

- प्राकृतिक भाषा बुझ्ने र उत्पन्न गर्ने  
- C# विशेषताहरूको साथ फङ्क्सन कल र टूल प्रयोग  
- वार्तालाप थ्रेडहरूको साथ सन्दर्भ-सचेत प्रतिक्रिया  
- निर्भरता इन्जेक्शन ढाँचाहरूको साथ विस्तारयोग्य आर्किटेक्चर  

## 📚 फ्रेमवर्क तुलना

यो उदाहरणले अन्य एजेन्टिक फ्रेमवर्कहरूसँग तुलना गर्दा माइक्रोसफ्ट एजेन्ट फ्रेमवर्कको दृष्टिकोण प्रदर्शन गर्दछ:

| विशेषता | माइक्रोसफ्ट एजेन्ट फ्रेमवर्क | अन्य फ्रेमवर्कहरू |
|---------|-------------------------|------------------|
| **एकीकरण** | देशी माइक्रोसफ्ट इकोसिस्टम | विविध अनुकूलता |
| **सरलता** | सफा, सहज API | प्रायः जटिल सेटअप |
| **विस्तारयोग्यता** | सजिलो टूल एकीकरण | फ्रेमवर्क-निर्भर |
| **उद्योग तयार** | उत्पादनको लागि निर्माण गरिएको | फ्रेमवर्क अनुसार फरक |

## 🚀 सुरु गर्ने तरिका

### पूर्वापेक्षाहरू

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) वा उच्च  
- [GitHub Models API पहुँच टोकन](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### आवश्यक वातावरण चरहरू

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

कोड उदाहरण चलाउन,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
वा dotnet CLI प्रयोग गरेर:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
पूरा कोडका लागि [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) हेर्नुहोस्।

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
  

## 🎓 मुख्य निष्कर्षहरू

1. **एजेन्ट आर्किटेक्चर**: माइक्रोसफ्ट एजेन्ट फ्रेमवर्कले .NET मा AI एजेन्ट निर्माण गर्न सफा, प्रकार-सुरक्षित दृष्टिकोण प्रदान गर्दछ  
2. **टूल एकीकरण**: `[Description]` विशेषताहरूले सजाइएको कार्यहरू एजेन्टका लागि उपलब्ध टूलहरू बन्छन्  
3. **वार्तालाप सन्दर्भ**: थ्रेड व्यवस्थापनले पूर्ण सन्दर्भ सचेततासँग बहु-टर्न वार्तालाप सक्षम बनाउँछ  
4. **कन्फिगरेसन व्यवस्थापन**: वातावरण चरहरू र सुरक्षित प्रमाणपत्र ह्यान्डलिङ .NET उत्कृष्ट अभ्यासहरू अनुसरण गर्दछ  
5. **OpenAI अनुकूलता**: GitHub Models एकीकरण OpenAI-संगत API मार्फत सहज रूपमा काम गर्दछ  

## 🔗 थप स्रोतहरू

- [माइक्रोसफ्ट एजेन्ट फ्रेमवर्क दस्तावेज](https://learn.microsoft.com/agent-framework)  
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी यथासम्भव शुद्धताको प्रयास गर्छौं, तर कृपया जानकार रहनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। यसको मूल भाषामा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्त्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->