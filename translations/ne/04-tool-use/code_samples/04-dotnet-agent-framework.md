# 🛠️ Azure OpenAI (Responses API) संग उन्नत उपकरण प्रयोग (.NET)

## 📋 सिक्ने उद्देश्यहरू

यो नोटबुकले Microsoft Agent Framework प्रयोग गरी .NET मा Azure OpenAI (Responses API) सँग एंटरप्राइज स्तरको उपकरण समाकलन ढाँचाहरू प्रदर्शन गर्छ। तपाईं C# को कडा टाइपिंग र .NET का एंटरप्राइज सुविधाहरूलाई उपयोग गर्दै बहु विशेषीकृत उपकरणहरू सहित जटिल एजेन्टहरू निर्माण गर्न सिक्नुहुनेछ।

### तपाईंले मास्टर गर्ने उन्नत उपकरण क्षमता

- 🔧 **बहु-उपकरण वास्तुकला**: बहु विशेषीकृत क्षमताहरू भएका एजेन्टहरू निर्माण
- 🎯 **प्रकार-सुरक्षित उपकरण सञ्चालन**: C# को कमपाइल-समय प्रमाणीकरण लाभ उठाउने
- 📊 **एंटरप्राइज उपकरण ढाँचाहरू**: उत्पादन-तयार उपकरण डिजाइन र त्रुटि ह्यान्डलिंग
- 🔗 **उपकरण संयोजन**: जटिल व्यवसायिक कार्यप्रवाहहरूको लागि उपकरणहरू संयोजन गर्ने

## 🎯 .NET उपकरण वास्तुकलाका लाभहरू

### एंटरप्राइज उपकरण सुविधाहरू

- **कमपाइल-समय प्रमाणीकरण**: कडाइका साथ टाइपिङले उपकरण प्यारामिटर सहीताको सुनिश्चितता
- **निर्भरता इन्जेक्शन**: उपकरण व्यवस्थापनका लागि IoC कन्टेनर समाकलन
- **असिंक/अवेइट ढाँचाहरू**: स्रोत व्यवस्थापनसहित अवरुद्ध नगर्ने उपकरण सञ्चालन
- **संरचित लगिङ**: उपकरण सञ्चालन निरीक्षणका लागि बिल्ट-इन लगिङ समाकलन

### उत्पादन-तयार ढाँचाहरू

- **अपवाद ह्यान्डलिंग**: प्रकार-सहित व्यापक त्रुटि प्रबंधन
- **स्रोत व्यवस्थापन**: उचित डिस्पोजल ढाँचाहरू र मेमोरी व्यवस्थापन
- **प्रदर्शन अनुगमन**: बिल्ट-इन मेट्रिक्स र प्रदर्शन काउन्टरहरू
- **कन्फिगरेसन व्यवस्थापन**: प्रमाणीकरणसहित प्रकार-सुरक्षित कन्फिगरेसन

## 🔧 प्राविधिक वास्तुकला

### कोर .NET उपकरण कम्पोनेन्टहरू

- **Microsoft.Extensions.AI**: एकीकृत उपकरण अमूर्त तह
- **Microsoft.Agents.AI**: एंटरप्राइज-ग्रेड उपकरण समन्वय
- **Azure OpenAI (Responses API)**: कनेक्शन पूलिंग सहित उच्च प्रदर्शन API क्लाइन्ट

### उपकरण सञ्चालन पाइपलाइन

```mermaid
graph LR
    A[प्रयोगकर्ता अनुरोध] --> B[एजेन्ट विश्लेषण]
    B --> C[उपकरण छनोट]
    C --> D[प्रकार प्रमाणीकरण]
    B --> E[प्यारामिटर बाइन्डिङ]
    E --> F[उपकरण कार्यान्वयन]
    C --> F
    F --> G[परिणाम प्रशोधन]
    D --> G
    G --> H[प्रतिक्रिया]
```

## 🛠️ उपकरण वर्गहरू र ढाँचाहरू

### 1. **डेटा प्रशोधन उपकरणहरू**

- **इनपुट प्रमाणीकरण**: डेटा एनोटेशनसहित कडा टाइपिंग
- **रूपान्तरण अपरेसनहरू**: प्रकार-सुरक्षित डेटा रूपान्तरण र ढाँचा
- **व्यवसायिक तर्क**: डोमेन-विशिष्ट गणना र विश्लेषण उपकरणहरू
- **आउटपुट ढाँचा**: संरचित प्रतिक्रिया उत्पादन

### 2. **समाकलन उपकरणहरू** 

- **API कनेक्टरहरू**: HttpClient सहित RESTful सेवा समाकलन
- **डाटाबेस उपकरणहरू**: डेटा पहुँचका लागि Entity Framework समाकलन
- **फाइल अपरेसनहरू**: प्रमाणीकरणसहित सुरक्षित फाइल सिस्टम अपरेसनहरू
- **बाह्य सेवाहरू**: तेस्रो-पक्ष सेवा समाकलन ढाँचाहरू

### 3. **उपयोगिता उपकरणहरू**

- **पाठ प्रशोधन**: स्ट्रिङ हेरफेर र ढाँचा उपयोगिताहरू
- **मिति/समय अपरेसनहरू**: संस्कृतिअनुसार मिति/समय गणना
- **गणितीय उपकरणहरू**: निश्चित गणना र सांख्यिकीय अपरेसनहरू
- **प्रमाणीकरण उपकरणहरू**: व्यवसायिक नियम प्रमाणीकरण र डेटा जाँच

शक्तिशाली, प्रकार-सुरक्षित उपकरण क्षमताहरू सहित एंटरप्राइज-ग्रेड एजेन्टहरू निर्माण गर्न तयार? हाम्रा पेशेवर-ग्रेड समाधानहरू वास्तुकला गरौं! 🏢⚡

## 🚀 सुरु गर्ने तरिका

### आवश्यकताहरू

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) वा माथिल्लो
- Azure OpenAI स्रोत र मोडेल डिप्लोयमेन्टसहितको [Azure सदस्यता](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` प्रयोग गरी साइन इन गर्नुहोस्

### आवश्यक वातावरण परिवर्तनशीलहरू

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# त्यसपछि साइन इन गर्नुहोस् ताकि AzureCliCredential टोकन प्राप्त गर्न सकून्
az login
```

```powershell
# पावरशेल
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# त्यसपछि साइन इन गर्नुहोस् ताकि AzureCliCredential टोकन प्राप्त गर्न सकून्
az login
```

### नमूना कोड

कोड उदाहरण चलाउन,

```bash
# zsh/bash
chmod +x ./04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

वा dotnet CLI प्रयोगगरि:

```bash
dotnet run ./04-dotnet-agent-framework.cs
```

पूर्ण कोडका लागि [`04-dotnet-agent-framework.cs`](../../../../04-tool-use/code_samples/04-dotnet-agent-framework.cs) स हेर्नुहोस्।

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

// Create New Conversation Session for Context Management
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
await using var session = await agent.CreateSessionAsync();

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->