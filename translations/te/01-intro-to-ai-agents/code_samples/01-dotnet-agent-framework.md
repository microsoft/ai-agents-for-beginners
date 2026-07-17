# 🌍 Microsoft Agent Framework (.NET)తో AI ప్రయాణ ఏజెంట్

## 📋 దృశ్యం అవలోకనం

ఈ ఉదాహరణ Microsoft Agent Framework ఉపయోగించి .NET కోసం బుద్ధిమంతమైన ప్రయాణ ప్రణాళిక ఏజెంట్‌ను ఎలా నిర్మించాలో చూపిస్తుంది. ఏజెంట్ ప్రపంథం అంతటా యాదృచ్ఛిక గమ్యస్థానాల కోసం వ్యక్తిగతీకరించిన దిన-యాత్ర మార్గనిర్దేశకాలను ఆటోమేటిక్‌గా తయారుచేయగలదు.

### ప్రధాన సామర్థ్యాలు:

- 🎲 **యాదృచ్ఛిక గమ్యస్థానం ఎంపిక**: సెలవు ప్రదేశాలు ఎంచుకునేందుకు అనుకూల సాధనాన్ని ఉపయోగిస్తుంది
- 🗺️ **బుద్ధిమంతమైన ట్రిప్ ప్లానింగ్**: ప్రతిరోజూ వివరించిన మార్గనిర్దేశకాలను సృష్టిస్తుంది
- 🔄 **రియల్-టైం స్ట్రీమింగ్**: తక్షణ మరియు స్ట్రీమింగ్ ప్రత్యుత్తరాలను రెండింటి కోసం మద్దతు కలిగి ఉంది
- 🛠️ **అనుకూల సాధన ఇంటిగ్రేషన్**: ఏజెంట్ సామర్థ్యాలను ఎలా విస్తరించాలో చూపిస్తుంది

## 🔧 సాంకేతిక నిర్మాణం

### ప్రాథమిక సాంకేతికతలు

- **Microsoft Agent Framework**: AI ఏజెంట్ అభివృద్ధికి తాజా .NET అమలు
- **Azure OpenAI (Responses API)**: Azure OpenAI Responses APIను మోడల్ అభిప్రాయ కోసం ఉపయోగిస్తుంది
- **Azure Identity**: `AzureCliCredential` (`az login`) ద్వారా సురక్షిత పెట్టుబడి
- **సురక్షిత కాన్ఫిగరేషన్**: పరిసర ఆధారిత ఎండ్‌పాయింట్ నిర్వహణ

### కీలక భాగాలు

1. **AIAgent**: సంభాషణ ప్రవాహాన్ని నిర్వహించే ప్రధాన ఏజెంట్ ఆర్కెస్ట్రేటర్
2. **అనుకూల సాధనాలు**: ఏజెంట్‌కు అందుబాటులో ఉన్న `GetRandomDestination()` ఫంక్షన్
3. **ప్రత్యుత్తర క్లయింట్**: Azure OpenAI Responses ఆధారిత సంభాషణ ఇంటర్‌ఫేస్
4. **స్ట్రీమింగ్ మద్దతు**: రియల్-టైం ప్రత్యుత్తరాల సృష్టి సామర్థ్యాలు

### ఇంటిగ్రేషన్ ప్యాటర్న్

```mermaid
graph LR
    A[వాడుకరి అభ్యర్థన] --> B[AI ఏజెంట్]
    B --> C[Azure OpenAI (ప్రత్యుత్తరాలు API)]
    B --> D[GetRandomDestination టూల్]
    C --> E[ప్రయాణ క్రమవివరణ]
    D --> E
```

## 🚀 ప్రారంభించండి

### ముందస్తు అవసరాలు

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) లేదా అతిస్థాయి
- Azure OpenAI వనరు మరియు మోడల్ డిప్లాయ్‌మెంట్ కలిగిన [Azure.subscription](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login`తో సైన్ ఇన్ అవ్వండి

### అవసరమైన పరిసర వేరియబుల్స్

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# అప్పుడు సైన్ ఇన్ అవ్వండి כדי AzureCliCredential టోకెన్ పొందడానికి
az login
```

```powershell
# పవర్‌షెల్
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# AzureCliCredential టోకన్ పొందడానికి కాబట్టి తర్వాత సైన్ ఇన్ అవ్వండి
az login
```

### నమూనా కోడ్

కోడ్ ఉదాహరణను అమలు చేయడానికి,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

లేకపోతే dotnet CLI ఉపయోగించండి:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

పూర్తి కోడుకు [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) చూడండి.

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4.1-mini";

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

## 🎓 ముఖ్య పాఠాలు

1. **ఏజెంట్ ఆర్కిటెక్షర్**: Microsoft Agent Framework .NETలో AI ఏజెంట్లను నిర్మించడానికి క్లియర్, టైప్-సేఫ్ దృష్టికోణాన్ని అందిస్తుంది
2. **సాధన ఇంటిగ్రేషన్**: `[Description]` లక్షణాలతో అలంకరించబడిన ఫంక్షన్లు ఏజెంట్‌కు అందుబాటులో ఉన్న సాధనాలు అవుతాయి
3. **కాన్ఫిగరేషన్ మేనేజ్మెంట్**: పరిసర వేరియబుల్స్ మరియు సురక్షిత క్రెడెన్షియల్ నిర్వహణ .NET ఉత్తమ అనుసరణలను అనుసరిస్తుంది
4. **Azure OpenAI Responses API**: ఏజెంట్ Azure.AI.OpenAI SDK ద్వారా Azure OpenAI Responses APIని ఉపయోగిస్తుంది

## 🔗 అదనపు వనరులు

- [Microsoft Agent Framework డాక్యుమెంటేషన్](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundryలో Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET సింగిల్ ఫైల్ ఆప్స్](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->