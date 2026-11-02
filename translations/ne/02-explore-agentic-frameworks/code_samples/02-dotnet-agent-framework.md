# 🔍 Microsoft Agent Framework अन्वेषण गर्दै - आधारभूत एजेन्ट (.NET)

## 📋 सिक्ने उद्देश्यहरू

यो उदाहरणले Microsoft Agent Framework का मौलिक अवधारणाहरूलाई .NET मा आधारभूत एजेन्ट कार्यान्वयन मार्फत अन्वेषण गर्छ। तपाईंले मुख्य एजेन्टिक ढाँचाहरू सिक्नुहुनेछ र C# र .NET पारिस्थितिकी प्रणाली प्रयोग गरी कसरी बौद्धिक एजेन्टहरूले काम गर्छन् थाहा पाउनुहुनेछ।

### तपाईंले के पत्ता लगाउनुहुनेछ

- 🏗️ **एजेन्ट वास्तुकला**: .NET मा AI एजेन्टहरूको आधारभूत संरचना बुझ्ने
- 🛠️ **उपकरण एकीकरण**: एजेन्टहरूले क्षमताहरू विस्तार गर्न बाह्य कार्यहरू कसरी प्रयोग गर्छन्  
- 💬 **संवाद प्रवाह**: थ्रेड व्यवस्थापनसहित बहु-चरण संवाद र सन्दर्भ व्यवस्थापन
- 🔧 **कन्फिगरेसन ढाँचाहरू**: .NET मा एजेन्ट सेटअप र व्यवस्थापनका लागि उत्तम अभ्यासहरू

## 🎯 समेटिएका प्रमुख अवधारणाहरू

### एजेन्टिक फ्रेमवर्क सिद्धान्तहरू

- **स्वायत्तता**: .NET AI अमूर्तिकरणहरू प्रयोग गरी एजेन्टहरूले स्वतन्त्र निर्णय कसरी गर्छन्
- **प्रतिक्रियाशीलता**: वातावरणीय परिवर्तन र प्रयोगकर्ता इनपुटहरूमा जवाफ दिने
- **प्रोएक्टिभिटी**: उद्देश्यहरू र सन्दर्भका आधारमा पहल गर्ने
- **सामाजिक क्षमता**: प्राकृतिक भाषामार्फत संवाद थ्रेडहरूको अन्तरक्रिया गर्ने

### प्राविधिक कम्पोनेन्टहरू

- **AIAgent**: मुख्य एजेन्ट समन्वयन र संवाद व्यवस्थापन (.NET)
- **उपकरण कार्यहरू**: C# विधिहरू र विशेषताहरू साथ एजेन्ट क्षमताहरू विस्तार गर्ने
- **Azure OpenAI एकीकरण**: Azure OpenAI Responses API मार्फत भाषा मोडलहरू प्रयोग गर्ने
- **सुरक्षित कन्फिगरेसन**: वातावरण-आधारित इन्डपोइन्ट व्यवस्थापन

## 🔧 प्राविधिक स्ट्याक

### मुख्य प्रविधिहरू

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) एकीकरण
- Azure.AI.OpenAI क्लाइन्ट ढाँचाहरू
- DotNetEnv द्वारा वातावरण-आधारित कन्फिगरेसन

### एजेन्ट क्षमताहरू

- प्राकृतिक भाषा बुझ्ने र उत्पादन गर्ने
- C# विशेषताहरूको साथ कार्य कल र उपकरण प्रयोग
- संवाद सत्रहरूसँग सन्दर्भ-सचेत प्रतिक्रियाहरू
- निर्भरता इन्जेक्सन ढाँचाहरू सहित विस्तार योग्य वास्तुकला

## 📚 फ्रेमवर्क तुलना

यो उदाहरणले Microsoft Agent Framework लाई अन्य एजेन्टिक फ्रेमवर्कसँग तुलना गरी देखाउँछ:

| सुविधा | Microsoft Agent Framework | अन्य फ्रेमवर्कहरू |
|---------|-------------------------|------------------|
| **एकीकरण** | नेटिभ Microsoft पारिस्थितिकी प्रणाली | विविध अनुकूलता |
| **सरलता** | सफा, सहज API | प्रायः जटिल सेटअप |
| **विस्तारयोग्यता** | सजिलो उपकरण एकीकरण | फ्रेमवर्क-निर्भर |
| **उद्यम तयार** | उत्पादनका लागि बनेको | फ्रेमवर्क अनुसार फरक |

## 🚀 सुरु गरौं

### पूर्व-आवश्यकताहरू

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) वा उच्च संस्करण
- Azure OpenAI स्रोत र मोडल तैनाती संग [Azure सदस्यता](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` बाट साइन इन गर्नुहोस्

### आवश्यक वातावरण चरहरू

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# त्यसपछि लगइन गर्नुहोस् ताकि AzureCliCredentialले टोकन प्राप्त गर्न सकोस्
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# त्यसपछि साइन इन गर्नुहोस् ताकि AzureCliCredential टोकन प्राप्त गर्न सक्छ।
az login
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

पुरा कोडको लागि [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) हेर्नुहोस्।

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

## 🎓 प्रमुख निष्कर्षहरू

1. **एजेन्ट वास्तुकला**: Microsoft Agent Framework ले .NET मा AI एजेन्टहरू निर्माण गर्न सफा, प्रकार-सुरक्षित दृष्टिकोण प्रदान गर्छ
2. **उपकरण एकीकरण**: `[Description]` विशेषताले सजाइएको कार्यहरू एजेन्टको लागि उपलब्ध उपकरणहरू बन्छन्
3. **संवाद सन्दर्भ**: सत्र व्यवस्थापनले पूर्ण सन्दर्भ सचेततासहित बहु-चरण संवाद सक्षम बनाउँछ
4. **कन्फिगरेसन व्यवस्थापन**: वातावरण चरहरू र सुरक्षित क्रेडेन्शियल ह्यान्डलिङ .NET उत्तम अभ्यासहरू अनुरूप छ
5. **Azure OpenAI Responses API**: एजेन्टले Azure.AI.OpenAI SDK मार्फत Azure OpenAI Responses API प्रयोग गर्छ

## 🔗 थप स्रोतहरू

- [Microsoft Agent Framework कागजात](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry मा Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET सिंगल फाइल एप्स](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->