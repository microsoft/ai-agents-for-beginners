# 🔍 माइक्रोसॉफ्ट एजेंट फ़्रेमवर्क का अन्वेषण - बेसिक एजेंट (.NET)

## 📋 सीखने के उद्देश्य

यह उदाहरण .NET में एक बेसिक एजेंट इम्प्लीमेंटेशन के माध्यम से माइक्रोसॉफ्ट एजेंट फ़्रेमवर्क की मूलभूत अवधारणाओं का अन्वेषण करता है। आप कोर एजेंटिक पैटर्न सीखेंगे और समझेंगे कि C# और .NET इकोसिस्टम का उपयोग करके बुद्धिमान एजेंट कैसे काम करते हैं।

### आप क्या खोजेंगे

- 🏗️ **एजेंट आर्किटेक्चर**: .NET में AI एजेंट्स की बेसिक संरचना को समझना
- 🛠️ **टूल इंटिग्रेशन**: एजेंट्स कैसे बाहरी फ़ंक्शंस का उपयोग कर क्षमताओं का विस्तार करते हैं  
- 💬 **संवाद प्रवाह**: मल्टी-टर्न संवादों और संदर्भ के साथ थ्रेड प्रबंधन
- 🔧 **कॉन्फ़िगरेशन पैटर्न्स**: .NET में एजेंट सेटअप और प्रबंधन के लिए सर्वोत्तम अभ्यास

## 🎯 कवर किए गए मुख्य कॉन्सेप्ट्स

### एजेंटिक फ्रेमवर्क सिद्धांत

- **स्वायत्तता**: .NET AI अमूर्तताओं का उपयोग करके एजेंट स्वतंत्र निर्णय कैसे लेते हैं
- **प्रतिक्रियाशीलता**: पर्यावरणीय परिवर्तनों और उपयोगकर्ता इनपुट्स पर प्रतिक्रिया देना
- **सक्रियता**: लक्ष्यों और संदर्भ के आधार पर पहल करना
- **सामाजिक क्षमता**: बातचीत थ्रेड्स के माध्यम से प्राकृतिक भाषा में इंटरैक्शन करना

### तकनीकी घटक

- **AIAgent**: कोर एजेंट ऑर्केस्ट्रेशन और बातचीत प्रबंधन (.NET)
- **टूल फ़ंक्शंस**: C# मेथड्स और एट्रिब्यूट्स के साथ एजेंट क्षमताओं का विस्तार
- **Azure OpenAI इंटिग्रेशन**: Azure OpenAI Responses API के माध्यम से भाषा मॉडलों का लाभ उठाना
- **सुरक्षित कॉन्फ़िगरेशन**: पर्यावरण-आधारित एंडपॉइंट प्रबंधन

## 🔧 तकनीकी स्टैक

### कोर टेक्नोलॉजीज

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) इंटिग्रेशन
- Azure.AI.OpenAI क्लाइंट पैटर्न्स
- DotNetEnv के साथ पर्यावरण-आधारित कॉन्फ़िगरेशन

### एजेंट क्षमताएं

- प्राकृतिक भाषा समझ और उत्पन्न करना
- C# एट्रिब्यूट्स के साथ फ़ंक्शन कॉलिंग और टूल उपयोग
- बातचीत सत्रों के साथ संदर्भ-सचेत प्रतिक्रियाएं
- डिपेंडेंसी इंजेक्शन पैटर्न्स के साथ एक्स्टेंसिबल आर्किटेक्चर

## 📚 फ्रेमवर्क तुलना

यह उदाहरण अन्य एजेंटिक फ्रेमवर्क्स की तुलना में माइक्रोसॉफ्ट एजेंट फ्रेमवर्क के दृष्टिकोण को दर्शाता है:

| फीचर | माइक्रोसॉफ्ट एजेंट फ्रेमवर्क | अन्य फ्रेमवर्क्स |
|---------|-------------------------|------------------|
| **इंटिग्रेशन** | नेटिव माइक्रोसॉफ्ट इकोसिस्टम | विभिन्न संगतता |
| **सरलता** | साफ, सहज API | अक्सर जटिल सेटअप |
| **विस्तारशीलता** | आसान टूल इंटिग्रेशन | फ्रेमवर्क-निर्भर |
| **एंटरप्राइज़ रेडी** | उत्पादन के लिए निर्मित | फ्रेमवर्क के अनुसार भिन्नता |

## 🚀 शुरुआत करना

### आवश्यकताएँ

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) या उच्चतर
- एक [Azure सदस्यता](https://azure.microsoft.com/free/) जिसमें Azure OpenAI संसाधन और मॉडल डिप्लॉयमेंट हो
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` से साइन इन करें

### आवश्यक पर्यावरणीय वेरिएबल्स

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# फिर साइन इन करें ताकि AzureCliCredential एक टोकन प्राप्त कर सके
az login
```

```powershell
# पावरशेल
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# फिर साइन इन करें ताकि AzureCliCredential टोकन प्राप्त कर सके
az login
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

पूर्ण कोड के लिए देखें [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs)। 

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

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

## 🎓 मुख्य बिंदु

1. **एजेंट आर्किटेक्चर**: माइक्रोसॉफ्ट एजेंट फ्रेमवर्क .NET में AI एजेंट बनाने के लिए एक साफ़, टाइप-सेफ अप्रोच प्रदान करता है
2. **टूल इंटिग्रेशन**: `[Description]` एट्रिब्यूट्स से सजाए गए फ़ंक्शंस एजेंट के लिए उपलब्ध टूल बन जाते हैं
3. **संवाद संदर्भ**: सत्र प्रबंधन पूर्ण संदर्भ जागरूकता के साथ मल्टी-टर्न संवाद सक्षम करता है
4. **कॉन्फ़िगरेशन प्रबंधन**: पर्यावरण चर और सुरक्षित क्रेडेंशियल हैंडलिंग .NET सर्वोत्तम प्रथाओं का पालन करते हैं
5. **Azure OpenAI Responses API**: एजेंट Azure.AI.OpenAI SDK के माध्यम से Azure OpenAI Responses API का उपयोग करता है

## 🔗 अतिरिक्त संसाधन

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI in Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->