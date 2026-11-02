# 🌍 Microsoft Agent Framework (.NET) உடன் AI பயண முகவர்

## 📋 காட்சி வழிகாட்டி

இந்த உதாரணம் Microsoft Agent Framework ஐ பயன்படுத்தி புத்திசாலி பயணத் திட்ட முகவரை .NET இல் எப்படி உருவாக்குவது என்பதை காட்டுகிறது. முகவன் உலகமெங்கும் புறப்படக்கூடிய இடங்களுக்கு தனிப்பட்ட நாள்-பயணம் திட்டங்களை தானாக உருவாக்க முடியும்.

### முக்கிய திறன்கள்:

- 🎲 **சீரற்ற இடத் தேர்வு**: விடுமுறை இடங்களை தேர்ந்தெடுக்க தனிப்பயன் கருவியை பயன்படுத்துகிறது
- 🗺️ **புத்திசாலி பயண திட்டமிடல்**: நாள் நேரடி திட்டங்களைக் கண்காணிக்கிறது
- 🔄 **நேரடி ஸ்ட்ரீமிங்**: உடனடி மற்றும் ஸ்ட்ரீமிங் பதில்களை இரண்டும் ஆதரிக்கிறது
- 🛠️ **தனிப்பயன் கருவி இணைப்பு**: முகவரின் திறன்களை விரிவாக்க எப்படி செய்வது என்பதை காண்பிக்கிறது

## 🔧 தொழில்நுட்ப கட்டமைப்பு

### மைய தொழில்நுட்பங்கள்

- **Microsoft Agent Framework**: .NET இல் AI முகவர் உருவாக்கத்திற்கான சமீபத்திய அமலாக்கம்
- **Azure OpenAI (Responses API)**: மாதிரி முன்மொழிவிற்கு Azure OpenAI Responses API ஐ பயன்படுத்துகிறது
- **Azure Identity**: `AzureCliCredential` (`az login`) மூலம் பாதுகாப்பான உள்நுழைவு
- **பாதுகாப்பான கட்டமைப்பு**: சூழல் அடிப்படையிலான முனைய முகவரி மேலாண்மை

### முக்கிய கூறுகள்

1. **AIAgent**: உரையாடல் ஓட்டத்தை கையாளும் பிரதான முகவர் ஒருங்கிணைப்பாளர்
2. **தனிப்பயன் கருவிகள்**: முகவருக்கு கிடைக்கக்கூடிய `GetRandomDestination()` செயல்பாடு
3. **பதிலளிப்பு கிளையண்ட்**: Azure OpenAI Responses அடிப்படையிலான உரையாடல் இடைமுகம்
4. **ஸ்ட்ரீமிங் ஆதரவு**: நேரடி பதிலளிப்பு உருவாக்கக் குறைந்த

### இணைப்பு மாதிரி

```mermaid
graph LR
    A[பயனர் கோரிக்கை] --> B[AI முகவர்]
    B --> C[ஆஜூர் OpenAI (பதில் API)]
    B --> D[GetRandomDestination கருவி]
    C --> E[பயண திட்டம்]
    D --> E
```

## 🚀 தொடக்க வழிகாட்டி

### தேவையான முன் நிபந்தனைகள்

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) அல்லது அதற்கு மேலான பதிப்பு
- ஒரு [Azure வாடிக்கைப் பதிவு](https://azure.microsoft.com/free/) Azure OpenAI வளம் மற்றும் மாதிரி கைமாற்றம் உடன்
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` கொண்டு உள்நுழையவும்

### தேவையான சூழல் மாறிகள்

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# பிறகு உள்நுழையவும் ताकि AzureCliCredential ஒரு டோக்கனைப் பெற முடியும்
az login
```

```powershell
# பவர் ஷெல்
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# பின்னர் AzureCliCredential டோக்கன் பெற சைன் இன் செய்யவும்
az login
```

### மாதிரி கோடு

கோடு உதாரணத்தை இயக்க,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

அல்லது dotnet CLI ஐப் பயன்படுத்தி:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

முழு கோப்புக்கான குறியீடு [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) ஐ பாருங்கள்.

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

## 🎓 முக்கிய எடுத்துக்காட்டுக்கள்

1. **முகவர் கட்டமைப்பு**: Microsoft Agent Framework .NET இல் AI முகவர்களை உருவாக்க சுத்தமான, வகை-பாதுகாப்பான அணுகுமுறையை வழங்குகிறது
2. **கருவி இணைவு**: `[Description]` பண்பு கொண்ட செயல்பாடுகள் முகவருக்கு கிடைக்கும் கருவிகளாக மாறுகின்றன
3. **கட்டமைப்பு மேலாண்மை**: சூழல் மாறிகள் மற்றும் பாதுகாப்பான கடவுச்சொல் கையாளுதல் .NET சிறந்த நடைமுறைகளை பின்பற்றுகிறது
4. **Azure OpenAI Responses API**: முகவர் Azure.AI.OpenAI SDK மூலமாக Azure OpenAI Responses API ஐ பயன்படுத்துகிறது

## 🔗 கூடுதல் வளங்கள்

- [Microsoft Agent Framework ஆவணம்](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry இல் Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET ஒரு கோப்பு செயலிகள்](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->