# 🌍 Microsoft Agent Framework (.NET) తో AI ప్రయాణ ఏజెంట్

## 📋 సన్నివేశ అవలోకనం

ఈ ఉదాహరణ Microsoft Agent Framework ను ఉపయోగించి నెప్టివేత్రిక ప్రయాణా పథకం ఏజెంట్‌ను ఎలా నిర్మించాలో చూపిస్తుంది. ఏజెంట్ ప్రపంచవ్యాప్తంగా యాదృచ్ఛిక గమ్యస్థానాల కోసం వ్యక్తిగతీకరించిన రోజు-ప్రయాణ ప్రయాణిక పథకాలను స్వయంచాలకంగా సృష్టించగలదు.

### ముఖ్య సామర్ధ్యాలు:

- 🎲 **యాదృచ్ఛిక గమ్యస్థానం ఎంచుకోవడం**: సెలవు ప్రదేశాలను ఎంచుకోవడానికి అనుకూలీకరించిన సాధనం ఉపయోగిస్తుంది
- 🗺️ **నెప్తివేత్రిక ప్రయాణా ప్లానింగ్**: ప్రతి రోజుకు వివరమైన పథకాలు సృష్టిస్తుంది
- 🔄 **నేరుగా ప్రసారం**: తక్షణ మరియు స్ట్రీమింగ్ ప్రతిస్పందనలను మద్దతు ఇస్తుంది
- 🛠️ **అనుకూల సాధన ఏకీకరణ**: ఏజెంట్ సామర్ధ్యాలను విస్తరించడాన్ని చూపిస్తుంది

## 🔧 సాంకేతిక నిర్మాణం

### ప్రాధాన్య సాంకేతికతలు

- **Microsoft Agent Framework**: AI ఏజెంట్ అభివృద్ధి కోసం తాజా .NET అమలు
- **Azure OpenAI (Response API)**: నమూనా ఊహాజనకానికి Azure OpenAI Responses API ఉపయోగిస్తుంది
- **Azure Identity**: `AzureCliCredential` (`az login`) ద్వారా సురక్షిత సైన్-ఇన్
- **సురక్షిత కాన్ఫిగరేషన్**: పరిసర ఆధారిత ఎండ్‌పాయింట్ నిర్వహణ

### ముఖ్య భాగాలు

1. **AIAgent**: సంభాషణ ప్రవాహాన్ని నిర్వహించే ప్రధాన ఏజెంట్ సంకేతకర్త
2. **అనుకూల సాధనాలు**: ఏజెంట్ కోసం అందుబాటులో ఉన్న `GetRandomDestination()` ఫంక్షన్
3. **Responses Client**: Azure OpenAI Responses ఆధారిత సంభాషణ ఇంటర్‌ఫేస్
4. **స్ట్రీమింగ్ మద్దతు**: నేరుగా ప్రతిస్పందనలు సృష్టించే సామర్థ్యాలు

### ఏకీకరణ నమూనా

```mermaid
graph LR
    A[వినియోగదారు అభ్యర్థన] --> B[AI ఏజెంట్]
    B --> C[ఆజ్యూర్ ఓపెన్AI (స్పందనలు API)]
    B --> D[GetRandomDestination పరికరం]
    C --> E[ప్రయాణ మార్గదర్శిని]
    D --> E
```

## 🚀 ప్రారంభం

### ముందస్తు అవసరాలు

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) లేదా అంతకు మించి
- Azure OpenAI వనరుతో Azure సబ్‌స్క్రిప్షన్ [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/)తో
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` తో సైన్-ఇన్ చేయండి

### అవసరమైన పరిసర వేరియబుల్స్

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# తరువాత AzureCliCredential టోకెన్ పొందడానికి సైన్ ఇన్ చేయండి
az login
```

```powershell
# పవర్‌షెల్
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# తరువాత AzureCliCredential టోకన్ పొందడానికి సైన్ ఇన్ చేయండి
az login
```

### నమూనా కోడ్

కోడ్ ఉదాహరణను నడపడానికి,

```bash
# జెడ్‌ఎస్‌హెచ్/బాష్
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

లేదా dotnet CLI ఉపయోగించి:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

పూర్తి కోడ్ కోసం [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) చూడండి.

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

## 🎓 ప్రధాన విషయాలు

1. **ఏజెంట్ నిర్మాణం**: Microsoft Agent Framework .NET లో AI ఏజెంట్లను నిర్మించడానికి సుస్పష్ట, రక-సురక్షిత పద్ధతిని కల్పిస్తుంది
2. **సాధన ఏకీకరణ**: `[Description]` లక్షణాలతో అలంకరించిన ఫంక్షన్లు ఏజెంట్ కోసం అందుబాటులో ఉండే సాధనాలుగా మారుతాయి
3. **కాన్ఫిగరేషన్ నిర్వహణ**: పరిసర వేరియబుల్స్ మరియు సురక్షిత ప్రమాణపత్రం నిర్వహణ .NET ఉత్తమ ఆచారాలను అనుసరిస్తాయి
4. **Azure OpenAI Responses API**: ఏజెంట్ Azure.AI.OpenAI SDK ద్వారా Azure OpenAI Responses API ఉపయోగిస్తుంది

## 🔗 అదనపు వనరులు

- [Microsoft Agent Framework డాక్యుమెంటేషన్](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry లో Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET సింగిల్ ఫైల్ యాప్స్](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->