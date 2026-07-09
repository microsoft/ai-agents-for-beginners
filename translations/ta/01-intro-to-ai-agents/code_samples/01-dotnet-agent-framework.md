# 🌍 Microsoft Agent Framework (.NET) உடன் ஏ ஐ பயண முகவர்

## 📋 சூழல் கண்ணோட்டம்

இந்த உதாரணம் Microsoft Agent Framework பயன்படுத்தி நுட்பமான பயண திட்டமிடும் முகவரை எவ்வாறு உருவாக்குவது என்பதைக் காண்பிக்கிறது. முகவர் உலகளாவிய இடைவெளிகளுக்கான தனிப்பட்ட நாள் பயண திட்டங்களை தானாக உருவாக்க முடியும்.

### முக்கிய திறன்கள்:

- 🎲 **சீரற்ற இடைவெளி தேர்வு**: custom கருவியைப் பயன்படுத்தி விடுமுறை இடங்களை தேர்ந்தெடுக்கும்
- 🗺️ **நுட்பமான பயண திட்டமிடல்**: நாள்தோறும் விரிவான பயண திட்டங்களை உருவாக்குகிறது
- 🔄 **உண்மை நேர ஸ்டிரீமிங்**: உடனடி மற்றும் ஸ்டிரீமிங் பதில்களை ஆதரிக்கிறது
- 🛠️ **தனிப்பயன் கருவி ஒருங்கிணைவு**: முகவர் திறன்களை விரிவாக்குவது எப்படி என்பதை காட்டுகிறது

## 🔧 தொழில்நுட்ப கட்டமைப்பு

### மைய தொழில்நுட்பங்கள்

- **Microsoft Agent Framework**: AI முகவர் உருவாக்கத்திற்கான புதிய .NET செயலாக்கம்
- **Azure OpenAI (பதில்கள் API)**: மாதிரி ஊக்கமளிப்பிற்கு Azure OpenAI Responses API பயன்படுத்துகிறது
- **Azure அடையாளம்**: `AzureCliCredential` மூலம் பாதுகாப்பான உள்நுழைவு (`az login`)
- **பாதுகாப்பான கட்டமைப்பு**: சூழலுக்கான முனை நிர்வாகம்

### முக்கிய கூறுகள்

1. **AIAgent**: உரையாடல் ஓட்டத்தை கையாளும் முக்கிய முகவர் ஒருவன்
2. **தனிப்பயன் கருவிகள்**: முகவருக்கு கிடைக்கும் `GetRandomDestination()` செயல்பாடு
3. **பதில்கள் கிளையன்ட்**: Azure OpenAI Responses அடிப்படையிலான உரையாடல் இடைமுகம்
4. **ஸ்டிரீமிங் ஆதரவு**: நேரடி பதில் உருவாக்க திறன்கள்

### ஒருங்கிணைவு முறைபாடு

```mermaid
graph LR
    A[பயனர் வேண்டுகோள்] --> B[செயற்கை நுண்ணறிவு முகவர்]
    B --> C[அஜூர் OpenAI (பதில் API)]
    B --> D[GetRandomDestination கருவி]
    C --> E[பயண திட்டம்]
    D --> E
```

## 🚀 துவக்குவது எப்படி

### முன்னிலை தேவைகள்

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) அல்லது அதற்கு மேல்
- Azure OpenAI வளமும் மாதிரி 배포வும் கொண்ட [Azure சந்தா](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` மூலம் உள்நுழையவும்

### தேவையான சூழல் மாறிகள்

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# பின்னர் உள்நுழையவும், இதனால் AzureCliCredential ஒரு டோக்கனைப் பெற முடியும்
az login
```

```powershell
# பவர்ஷெல்
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# பின்னர் AzureCliCredential ஒரு டோக்கனை பெறலாம் என்பதற்காக உள்நுழைக
az login
```

### மாதிரி குறியீடு

குறியீட்டை இயக்க,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

அல்லது dotnet CLI பயன்படுத்தி:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

முழு குறியீட்டிற்கான [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) ஐ பார்க்கவும்.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@9.*
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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4o-mini";

var azureClient = new AzureOpenAIClient(new Uri(azureEndpoint), new AzureCliCredential());

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetOpenAIResponseClient(deployment)
    .CreateAIAgent(
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

## 🎓 முக்கியக் குறிப்புகள்

1. **முகவர் கட்டமைப்பு**: Microsoft Agent Framework .NET இல் AI முகவர்களை கட்டமைக்க சுத்தமான, வகை-பாதுகாப்பு அணுகுமுறையை வழங்குகிறது
2. **கருவி ஒருங்கிணைவு**: `[Description]` பண்புகளால் அலங்கரிக்கப்பட்ட செயல்பாடுகள் முகவருக்கு கிடைக்கக்கூடிய கருவிகளாக மாறுகின்றன
3. **கட்டமைப்பு நிர்வாகம்**: சூழல் மாறிகள் மற்றும் பாதுகாப்பான அடையாள நிர்வாகம் .NET சிறந்த செயல்முறைகளை பின்பற்றுகிறது
4. **Azure OpenAI Responses API**: முகவர் Azure.AI.OpenAI SDK மூலம் Azure OpenAI Responses API-ஐ பயன்படுத்துகிறது

## 🔗 கூடுதல் வளங்கள்

- [Microsoft Agent Framework ஆவணங்கள்](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry இல் Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->