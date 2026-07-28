# 🌍 माइक्रोसॉफ्ट एजेंट फ्रेमवर्क (.NET) के साथ AI ट्रैवल एजेंट

## 📋 परिदृश्य अवलोकन

यह उदाहरण दिखाता है कि माइक्रोसॉफ्ट एजेंट फ्रेमवर्क फॉर .NET का उपयोग करके एक बुद्धिमान ट्रैवल प्लानिंग एजेंट कैसे बनाया जाए। एजेंट दुनिया भर के यादृच्छिक गंतव्यों के लिए स्वचालित रूप से व्यक्तिगत दिन की यात्राओं का योजना बना सकता है।

### मुख्य क्षमताएँ:

- 🎲 **यादृच्छिक गंतव्य चयन**: छुट्टियों के स्थान चुनने के लिए एक कस्टम टूल का उपयोग करता है
- 🗺️ **बुद्धिमान यात्रा योजना**: दिन-प्रतिदिन विस्तृत यात्रा योजनाएँ बनाता है
- 🔄 **रियल-टाइम स्ट्रीमिंग**: तत्काल और स्ट्रीमिंग प्रतिक्रियाओं दोनों का समर्थन करता है
- 🛠️ **कस्टम टूल एकीकरण**: एजेंट क्षमताओं को बढ़ाने का तरीका दिखाता है

## 🔧 तकनीकी वास्तुकला

### मुख्य प्रौद्योगिकियां

- **माइक्रोसॉफ्ट एजेंट फ्रेमवर्क**: AI एजेंट विकास के लिए नवीनतम .NET कार्यान्वयन
- **Azure OpenAI (Responses API)**: मॉडल अनुमान के लिए Azure OpenAI Responses API का उपयोग करता है
- **Azure Identity**: `AzureCliCredential` (`az login`) के माध्यम से सुरक्षित साइन-इन
- **सुरक्षित कॉन्फ़िगरेशन**: पर्यावरण-आधारित एंडपॉइंट प्रबंधन

### मुख्य घटक

1. **AIAgent**: मुख्य एजेंट आयोजक जो बातचीत के प्रवाह को संभालता है
2. **कस्टम टूल्स**: `GetRandomDestination()` फ़ंक्शन एजेंट के लिए उपलब्ध
3. **Responses क्लाइंट**: Azure OpenAI Responses-आधारित बातचीत इंटरफ़ेस
4. **स्ट्रीमिंग समर्थन**: रियल-टाइम प्रतिक्रिया उत्पन्न करने की क्षमता

### एकीकरण पैटर्न

```mermaid
graph LR
    A[उपयोगकर्ता अनुरोध] --> B[एआई एजेंट]
    B --> C[अजुर ओपनएआई (प्रतिक्रिया एपीआई)]
    B --> D[GetRandomDestination उपकरण]
    C --> E[यात्रा कार्यक्रम]
    D --> E
```

## 🚀 प्रारंभ करना

### आवश्यकताएँ

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) या उच्चतर
- एक [Azure सदस्यता](https://azure.microsoft.com/free/) जिसमें Azure OpenAI संसाधन और मॉडल तैनाती हो
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` के साथ साइन इन करें

### आवश्यक पर्यावरण चर

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# फिर साइन इन करें ताकि AzureCliCredential टोकन प्राप्त कर सके
az login
```

```powershell
# पावरशेल
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# फिर साइन इन करें ताकि AzureCliCredential एक टोकन प्राप्त कर सके
az login
```

### नमूना कोड

कोड उदाहरण चलाने के लिए,

```bash
# ज़श/बैश
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

या dotnet CLI का उपयोग करके:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

पूरा कोड देखने के लिए [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) देखें।

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.4.1
#:package Microsoft.Agents.AI.OpenAI@1.1.0
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

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip
// Run the agent with streaming enabled for real-time response display
// Shows the agent's thinking and response as it generates the content
// Provides better user experience with immediate feedback
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 मुख्य निष्कर्ष

1. **एजेंट वास्तुकला**: माइक्रोसॉफ्ट एजेंट फ्रेमवर्क .NET में AI एजेंट बनाने के लिए एक साफ, प्रकार-सुरक्षित दृष्टिकोण प्रदान करता है
2. **टूल एकीकरण**: `[Description]` विशेषताओं के साथ सजाए गए फ़ंक्शन एजेंट के लिए उपलब्ध टूल बन जाते हैं
3. **कॉन्फ़िगरेशन प्रबंधन**: पर्यावरण चर और सुरक्षित प्रमाण-पत्र हैंडलिंग .NET सर्वोत्तम प्रथाओं का पालन करती है
4. **Azure OpenAI Responses API**: एजेंट Azure.AI.OpenAI SDK के माध्यम से Azure OpenAI Responses API का उपयोग करता है

## 🔗 अतिरिक्त संसाधन

- [माइक्रोसॉफ्ट एजेंट फ्रेमवर्क प्रलेखन](https://learn.microsoft.com/agent-framework)
- [माइक्रोसॉफ्ट फाउंड्री में Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET सिंगल फ़ाइल ऐप्स](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->