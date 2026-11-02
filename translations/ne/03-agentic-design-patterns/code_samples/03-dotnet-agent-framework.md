# 🎨 Azure OpenAI (Responses API) सँग Agentic डिजाइन ढाँचा (.NET)

## 📋 सिकाइका उद्देश्यहरू

यो उदाहरणले .NET मा Microsoft Agent Framework प्रयोग गरी Azure OpenAI (Responses API) एकीकरण सहित बुद्धिमान एजेन्टहरू निर्माण गर्नका लागि उद्यम-स्तरका डिजाइन ढाँचाहरू देखाउँछ। तपाईंले व्यावसायिक ढाँचा र वास्तुकला दृष्टिकोणहरू सिक्नुहुनेछ जसले एजेन्टहरूलाई उत्पादनयोग्य, मर्मतयोग्य, र स्केलेबल बनाउँछ।

### उद्यम डिजाइन ढाँचाहरू

- 🏭 **Factory Pattern**: आश्रितता इंजेक्शनसहित मानकीकृत एजेन्ट सिर्जना
- 🔧 **Builder Pattern**: फ्लुएन्ट एजेन्ट कन्फिगरेसन र सेटअप
- 🧵 **Thread-Safe Patterns**: समवर्ती संवाद व्यवस्थापन
- 📋 **Repository Pattern**: व्यवस्थित उपकरण र क्षमता व्यवस्थापन

## 🎯 .NET-विशेष वास्तुकला लाभहरू

### उद्यम सुविधाहरू

- **Strong Typing**: कम्पाइल-टाइम मान्यकरण र IntelliSense सहयोग
- **Dependency Injection**: बिल्ट-इन DI कन्टेनर एकीकरण
- **Configuration Management**: IConfiguration र Options ढाँचाहरू
- **Async/Await**: प्रथम श्रेणी असिंक्रोनस प्रोग्रामिङ समर्थन

### उत्पादन-तयार ढाँचाहरू

- **Logging Integration**: ILogger र संरचित लगिङ समर्थन
- **Health Checks**: बिल्ट-इन अनुगमन र निदान
- **Configuration Validation**: डाटा एनोटेसनसहितको मजबूत टाइपिङ
- **Error Handling**: संरचित अपवाद व्यवस्थापन

## 🔧 प्राविधिक वास्तुकला

### मूल .NET कम्पोनेन्टहरू

- **Microsoft.Extensions.AI**: एकीकृत AI सेवा अमूर्तता
- **Microsoft.Agents.AI**: उद्यम एजेन्ट अर्गनाइजेसन फ्रेमवर्क
- **Azure OpenAI (Responses API)**: उच्च-प्रदर्शन API क्लाइन्ट ढाँचाहरू
- **Configuration System**: appsettings.json र वातावरण एकीकरण

### डिजाइन ढाँचा कार्यान्वयन

```mermaid
graph LR
    A[IServiceCollection] --> B[एजेन्ट बिल्डर]
    B --> C[कन्फिगरेसन]
    C --> D[टूल रजिष्ट्रि]
    D --> E[एआई एजेन्ट]
```

## 🏗️ प्रदर्शन गरिएको उद्यम ढाँचाहरू

### 1. **सिर्जनात्मक ढाँचाहरू**

- **Agent Factory**: एउटै कन्फिगरेसनसहित केन्द्रीयकृत एजेन्ट सिर्जना
- **Builder Pattern**: जटिल एजेन्ट कन्फिगरेसनका लागि फ्लुएन्ट API
- **Singleton Pattern**: साझा स्रोतहरू र कन्फिगरेसन व्यवस्थापन
- **Dependency Injection**: खुकुलो जोड र परीक्षणयोग्य बनाउने

### 2. **व्यवहारिक ढाँचाहरू**

- **Strategy Pattern**: विनिमेय उपकरण कार्यान्वयन रणनीतिहरू
- **Command Pattern**: अनडू/रिडू सहित समाविष्ट एजेन्ट अपरेसनहरू
- **Observer Pattern**: घटना-आधारित एजेन्ट जीवनचक्र व्यवस्थापन
- **Template Method**: मानकीकृत एजेन्ट कार्यप्रवाहहरू

### 3. **संरचनात्मक ढाँचाहरू**

- **Adapter Pattern**: Azure OpenAI (Responses API) एकीकरण तह
- **Decorator Pattern**: एजेन्ट क्षमताको वृद्धि
- **Facade Pattern**: सरल एजेन्ट अन्तरक्रिया इन्टरफेसहरू
- **Proxy Pattern**: प्रदर्शनका लागि लेजी लोडिंग र क्याचिङ

## 📚 .NET डिजाइन सिद्धान्तहरू

### SOLID सिद्धान्तहरू

- **Single Responsibility**: प्रत्येक कम्पोनेन्टको स्पष्ट उद्देश्य
- **Open/Closed**: संशोधन बिना विस्तारयोग्य
- **Liskov Substitution**: इन्टरफेस-आधारित उपकरण कार्यान्वयनहरू
- **Interface Segregation**: लक्षित, समेकित इन्टरफेसहरू
- **Dependency Inversion**: अमूर्ततामा निर्भर, कंक्रीटमा होइन

### सफा वास्तुकला

- **Domain Layer**: मूल एजेन्ट र उपकरण अमूर्तता
- **Application Layer**: एजेन्ट अर्गनाइजेसन र कार्यप्रवाहहरू
- **Infrastructure Layer**: Azure OpenAI (Responses API) एकीकरण र बाह्य सेवाहरू
- **Presentation Layer**: प्रयोगकर्ता अन्तरक्रिया र जवाफ स्वरूपण

## 🔒 उद्यम विचारणीयताहरू

### सुरक्षा

- **Credential Management**: IConfiguration प्रयोग गरेर सुरक्षित API कुञ्जी ह्यान्डलिङ
- **Input Validation**: दृढ टाइपिङ र डाटा एनोटेसन मान्यकरण
- **Output Sanitization**: सुरक्षित जवाफ प्रक्रिया र छनौट
- **Audit Logging**: समग्र अपरेशन ट्र्याकिङ

### प्रदर्शन

- **Async Patterns**: गैर-रोकिने I/O अपरेसनहरू
- **Connection Pooling**: दक्ष HTTP क्लाइन्ट व्यवस्थापन
- **Caching**: प्रदर्शन सुधारका लागि जवाफ क्याचिङ
- **Resource Management**: उचित नष्ट र सफाइ ढाँचाहरू

### स्केलेबिलिटी

- **Thread Safety**: समवर्ती एजेन्ट कार्यान्वयन समर्थन
- **Resource Pooling**: प्रभावकारी स्रोत उपयोग
- **Load Management**: दर सीमितीकरण र ब्याकप्रेशर ह्यान्डलिङ
- **Monitoring**: प्रदर्शन मेट्रिक्स र स्वास्थ्य जाँच

## 🚀 उत्पादन परिनियोजन

- **Configuration Management**: वातावरण-विशेष सेटिङहरू
- **Logging Strategy**: सहसंबंधित ID हरूसहित संरचित लगिङ
- **Error Handling**: सही पुनःप्राप्तिसहित विश्वव्यापी अपवाद व्यवस्थापन
- **Monitoring**: एप्लिकेसन इनसाइट्स र प्रदर्शन काउन्टरहरू
- **Testing**: युनिट टेस्ट, इंटीग्रेशन टेस्ट र लोड टेस्ट ढाँचाहरू

.NET सँग उद्यम-स्तर बुद्धिमान एजेन्टहरू बनाउन तयार हुनुहुन्छ? केही ठोस वास्तुकला तयार गरौं! 🏢✨

## 🚀 सुरूवात गर्ने तरिका

### आवश्यकताहरू

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) वा माथि
- Azure OpenAI स्रोत र मोडेल डिप्लोयमेन्ट सहितको [Azure सदस्यता](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` सँग साइन इन गर्नुहोस्

### आवश्यक वातावरण भेरिएबलहरू

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# त्यसपछि साइन इन गर्नुहोस् ताकि AzureCliCredential ले टोकन प्राप्त गर्न सकोस्
az login
```

```powershell
# पावरशेल
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# त्यसपछि साइन इन गर्नुहोस् ताकि AzureCliCredential ले टोकन प्राप्त गर्न सकून्
az login
```

### नमुना कोड

कोड उदाहरण चलाउन,

```bash
# zsh/bash
chmod +x ./03-dotnet-agent-framework.cs
./03-dotnet-agent-framework.cs
```

वा dotnet CLI मार्फत:

```bash
dotnet run ./03-dotnet-agent-framework.cs
```

पूर्ण कोडका लागि [`03-dotnet-agent-framework.cs`](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs) हेर्नुहोस्।

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
var session = await agent.CreateSessionAsync();

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