# 🌍 Microsoft Agent Framework (.NET) सँग AI यात्रा एजेन्ट

## 📋 परिदृश्य अवलोकन

यस उदाहरणले कसरि Microsoft Agent Framework प्रयोग गरी एक बुद्धिमान यात्रा योजना एजेन्ट निर्माण गर्ने देखाउँछ जुन स्वतः विश्वभरका यादृच्छिक गन्तव्यहरूको लागि व्यक्तिगत दिन-यात्रा कार्यक्रमहरु उत्पादन गर्न सक्छ।

### प्रमुख क्षमता:

- 🎲 **यादृच्छिक गन्तव्य चयन**: बिदा स्थलहरू छनोट गर्न एक अनुकूल उपकरण प्रयोग गर्दछ
- 🗺️ **बुद्धिमान यात्रा योजना**: दिनप्रतिदिनको विस्तारमा यात्रा कार्यक्रम बनाउँछ
- 🔄 **रियल-टाइम स्ट्रिमिंग**: तत्काल र स्ट्रिमिङ उत्तरहरू दुवै समर्थन गर्दछ
- 🛠️ **अनुकूल उपकरण एकीकरण**: एजेन्ट क्षमताहरू विस्तार कसरी गर्ने देखाउँछ

## 🔧 प्राविधिक आर्किटेक्चर

### मुख्य प्रविधिहरू

- **Microsoft Agent Framework**: AI एजेन्ट विकासका लागि नवीनतम .NET कार्यान्वयन
- **Azure OpenAI (प्रतिक्रिया API)**: मोडेल पूर्वानुमानका लागि Azure OpenAI प्रतिक्रिया API प्रयोग गर्दछ
- **Azure Identity**: `AzureCliCredential` (`az login`) मार्फत सुरक्षित साइन-इन
- **सुरक्षित कन्फिगरेसन**: वातावरणको आधारमा अन्तिम बिन्दु व्यवस्थापन

### मुख्य कम्पोनेन्टहरू

1. **AIAgent**: मुख्य एजेन्ट संयोजक जो संवाद प्रवाह सम्हाल्छ
2. **अनुकूल उपकरणहरू**: एजेन्टलाई उपलब्ध `GetRandomDestination()` फंक्शन
3. **प्रतिक्रिया क्लाइєн्ट**: Azure OpenAI प्रतिक्रिया आधारित संवाद अन्तरफलक
4. **स्ट्रिमिङ समर्थन**: रियल-टाइम प्रतिक्रिया उत्पादन क्षमता

### एकीकरण ढाँचा

```mermaid
graph LR
    A[प्रयोगकर्ता अनुरोध] --> B[AI एजेन्ट]
    B --> C[Azure OpenAI (प्रतिक्रियाहरू API)]
    B --> D[GetRandomDestination उपकरण]
    C --> E[यात्रा कार्यक्रम]
    D --> E
```

## 🚀 सुरु गर्दै

### आवश्यकताहरू

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) वा सोभन्दा उच्च
- Azure OpenAI स्रोत र मोडेल डिप्लोयमेन्ट भएको [Azure सदस्यता](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` मार्फत साइन-इन गर्नुहोस्

### आवश्यक वातावरण चरहरू

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# त्यसपछि साइन इन गर्नुहोस् ताकि AzureCliCredential टोकन प्राप्त गर्न सकोस्।
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# त्यसपछि साइन इन गर्नुहोस् ताकि AzureCliCredential टोकन प्राप्त गर्न सकोस्
az login
```

### नमुना कोड

कोड उदाहरण चलाउन,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

वा dotnet CLI प्रयोग गर्दै:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

पूर्ण कोडका लागि [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) हेर्नुहोस्।

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

## 🎓 मुख्य सिकाइहरू

1. **एजेन्ट आर्किटेक्चर**: Microsoft Agent Framework ले .NET मा AI एजेन्ट निर्माणका लागि सफा र प्रकार-निश्चित तरिका प्रदान गर्दछ
2. **उपकरण एकीकरण**: `[Description]` विशेषता भएका फंक्शनहरू एजेन्टका लागि उपलब्ध उपकरणहरू हुन्छन्
3. **कन्फिगरेसन व्यवस्थापन**: वातावरण चरहरू र सुरक्षित क्रेडेन्सियल ह्यान्डलिङ .NET उत्तम अभ्यासहरू अनुसरण गर्दछ
4. **Azure OpenAI प्रतिक्रिया API**: एजेन्टले Azure.AI.OpenAI SDK मार्फत Azure OpenAI प्रतिक्रिया API प्रयोग गर्छ

## 🔗 अतिरिक्त स्रोतहरू

- [Microsoft Agent Framework कागजात](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry मा Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET एकल फाइल एपहरू](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->