# 🔍 Microsoft Agent Framework चा शोध - बेसिक एजंट (.NET)

## 📋 शिकण्याचे उद्दिष्टे

हा उदाहरण Microsoft Agent Framework चे मूलभूत संकल्पना .NET मधील एक बेसिक एजंट अंमलबजावणीद्वारे तपासतो. तुम्ही मुख्य एजंटिक पद्धती शिकाल आणि C# आणि .NET इकोसिस्टम वापरून बुद्धिमान एजंट कसे काम करतात हे समजून घेणार आहात.

### तुम्हाला काय सापडेल

- 🏗️ **एजंट आर्किटेक्चर**: .NET मधील AI एजंटच्या मूलभूत रचनेचा समज
- 🛠️ **टूल इंटिग्रेशन**: एजंट कसे क्षमतांसाठी बाह्य फंक्शन्स वापरतात  
- 💬 **संवाद प्रवाह**: मल्टि-टर्न संभाषणे आणि थ्रेड व्यवस्थापनासह संदर्भ व्यवस्थापन
- 🔧 **कॉन्फिगरेशन पद्धती**: .NET मध्ये एजंट सेटअप आणि व्यवस्थापनासाठी सर्वोत्तम पद्धती

## 🎯 महत्त्वाचे संकल्पना आच्छादित

### एजंटिक फ्रेमवर्क तत्त्वे

- **स्वायत्तता**: एजंट .NET AI अब्स्ट्रॅक्शन्स वापरून स्वतंत्र निर्णय कसे घेतात
- **प्रतिक्रियाशीलता**: पर्यावरणीय बदल आणि वापरकर्ता इनपुटसाठी प्रतिसाद देणे
- **प्रोऍक्टिव्हिटी**: ध्येय आणि संदर्भावर आधारित पुढाकार घेणे
- **सामाजिक क्षमता**: नैसर्गिक भाषेत संभाषण थ्रेड्सद्वारे संवाद साधणे

### तांत्रिक घटक

- **AIAgent**: मुख्य एजंट समन्वय आणि संभाषण व्यवस्थापन (.NET)
- **टूल फंक्शन्स**: C# पद्धती आणि अॅट्रिब्युट्ससह एजंट क्षमतांचा विस्तार
- **Azure OpenAI इंटिग्रेशन**: Azure OpenAI Responses API द्वारे भाषा मॉडेल्सचा लाभ घेणे
- **सुरक्षित कॉन्फिगरेशन**: पर्यावरण-आधारित एंडपॉइंट व्यवस्थापन

## 🔧 तांत्रिक स्टॅक

### मुख्य तंत्रज्ञान

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) इंटिग्रेशन
- Azure.AI.OpenAI क्लायंट पद्धती
- DotNetEnv सह पर्यावरण-आधारित कॉन्फिगरेशन

### एजंट क्षमता

- नैसर्गिक भाषा समज आणि निर्मिती
- C# अॅट्रिब्युट्ससह फंक्शन कॉलिंग आणि टूल वापर
- संभाषण सत्रांसह संदर्भ-सजग प्रतिसाद
- अवलंबित्व इंजेक्शन पद्धतींसह विस्तारयोग्य आर्किटेक्चर

## 📚 फ्रेमवर्क तुलना

हा उदाहरण Microsoft Agent Framework चा इतर एजंटिक फ्रेमवर्क्सशी तुलना कशी होते हे दर्शवतो:

| वैशिष्ट्य | Microsoft Agent Framework | इतर फ्रेमवर्क्स |
|---------|-------------------------|------------------|
| **इंटिग्रेशन** | स्थानिक Microsoft इकोसिस्टम | विविध सुसंगतता |
| **सोपेपणा** | स्वच्छ, सहज समजणारा API | नेहमी गुंतागुंतीचा सेटअप |
| **विस्तारयोग्यता** | सहज टूल इंटिग्रेशन | फ्रेमवर्क-आधारित |
| **एंटरप्राइज रेडी** | उत्पादनासाठी तयार | फ्रेमवर्क नुसार बदलते |

## 🚀 सुरुवात कशी करावी

### पूर्वअटी

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) किंवा त्याहून अधिक
- Azure OpenAI रिसोर्स आणि मॉडेल डिप्लॉयमेंटसह [Azure सबस्क्रिप्शन](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` वापरून साइन इन करा

### आवश्यक पर्यावरण व्हेरिएबल्स

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# मग साइन इन करा जेणेकरून AzureCliCredential टोकन मिळवू शकेल
az login
```

```powershell
# पॉवरशेल
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# मग साइन इन करा जेणेकरून AzureCliCredential टोकन मिळवू शकेल
az login
```

### नमुना कोड

कोड उदाहरण चालवण्यासाठी,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

अथवा dotnet CLI वापरून:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

संपूर्ण कोडसाठी [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) बघा.

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

## 🎓 मुख्य गोष्टी

1. **एजंट आर्किटेक्चर**: Microsoft Agent Framework .NET मध्ये AI एजंट बांधणीसाठी स्वच्छ, टाईप-सेफ दृष्टिकोन प्रदान करतो
2. **टूल इंटिग्रेशन**: `[Description]` अॅट्रिब्युट्ससह सज्ज फंक्शन्स एजंटसाठी उपलब्ध टूल्स होतात
3. **संवाद संदर्भ**: सत्र व्यवस्थापन मल्टि-टर्न संभाषणे संपूर्ण संदर्भज्ञानासह सक्षम करते
4. **कॉन्फिगरेशन व्यवस्थापन**: पर्यावरण व्हेरिएबल्स आणि सुरक्षित क्रेडेन्शियल हाताळणी .NET सर्वोत्तम पद्धतींना अनुसरते
5. **Azure OpenAI Responses API**: एजंट Azure.AI.OpenAI SDK द्वारे Azure OpenAI Responses API वापरतो

## 🔗 अतिरिक्त साधने

- [Microsoft Agent Framework दस्तऐवज](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry मधील Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET सिंगल फाइल अॅप्स](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->