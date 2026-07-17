# 🌍 Microsoft Agent Framework (.NET) உடன் எய்ஐ பயண முகவர்

## 📋 கண்ணோட்டம்

இந்த உதாரணம் Microsoft Agent Framework ஐ .NET க்காக பயன்படுத்தி ஒரு புத்திசாலி பயண திட்டமிடும் முகவரை எப்படி உருவாக்குவது என்பது பற்றி காட்டுகிறது. இந்த முகவர் உலகின் விதவிதமான இலக்குகளுக்கான தனிப்பயன் நாள் பயணம் திட்டிகளை தானாகவே உருவாக்க முடியும்.

### முக்கிய திறன்கள்:

- 🎲 **சீர்மான இல்லாத இலக்கு தேர்வு**: விடுமுறை இடங்களை தேர்வு செய்ய தனிப்பயன் கருவி பயன்படுத்துகிறது
- 🗺️ **புத்திசாலி பயணம் திட்டமிடல்**: நாள் தோறும் விரிவான பயண திட்டங்களை உருவாக்குகிறது
- 🔄 **நேரடி ஒளிபரப்பு**: உடனடி மற்றும் ஒளிபரப்பும் பதில்களையும் ஆதரிக்கிறது
- 🛠️ **தனிப்பயன் கருவி இணைப்பு**: முகவர் திறன்களை விரிவாக்க எவ்வாறு செய்யுவது என்பதைக் காட்டுகிறது

## 🔧 தொழில்நுட்ப கட்டமைப்பு

### மைய தொழில்நுட்பங்கள்

- **Microsoft Agent Framework**: AI முகவர் உருவாக்கம் க்கான புதிய .NET அமலாக்கம்
- **Azure OpenAI (பதில் API)**: மாதிரி கணிப்பு க்காக Azure OpenAI பதில்கள் API பயன்படுத்துகிறது
- **Azure அடையாளம்**: `AzureCliCredential` (`az login`) மூலம் பாதுகாப்பான உள்நுழைவு
- **பாதுகாப்பான கட்டமைப்பு**: சுற்றுச்சூழல் அடிப்படையிலான தள முகவரிகள் நிர்வகிப்பு

### முக்கிய கூறுகள்

1. **AIAgent**: உரையாடல் ஓட்டத்தை கையாளும் முக்கிய முகவர் ஒருங்கிணைப்பாளர்
2. **தனிப்பயன் கருவிகள்**: முகவருக்கு கிடைக்கும் `GetRandomDestination()` செயல்பாடு
3. **பதில் கிளையண்ட்**: Azure OpenAI பதில்களால் இயக்கப்படும் உரையாடல் இடைமுகம்
4. **ஒளிபரப்பு ஆதரவு**: நேரடியான பதில் உருவாக்க திறன்கள்

### ஒருங்கிணைப்பு மாதிரி

```mermaid
graph LR
    A[பயனர் கோரிக்கை] --> B[செயற்கை நுண்ணறிவு முகவர்]
    B --> C[Azure OpenAI (பதில் API)]
    B --> D[GetRandomDestination கருவி]
    C --> E[பயணம் திட்டம்]
    D --> E
```

## 🚀 துவக்கம்

### முன்னோட்டங்கள்

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) அல்லது அதற்கும் மேல்
- Azure OpenAI வளத்துடன் கூடிய [Azure சந்தா](https://azure.microsoft.com/free/) மற்றும் மாதிரி 배포ம்
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` மூலம் உள்நுழையவும்

### தேவைப்படுகிற சுற்றுச்சூழல் மாறி

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# பிறகு உள்நுழைக, அப்போது AzureCliCredential ஒரு அடையாளப்பத்திரம் பெறும்
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# பின்னர் AzureCliCredential டோக்கன் பெற உள்நுழைக
az login
```

### மாதிரி குறியீடு

குறியீட்டை இயக்க:

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

அல்லது dotnet CLI பயன்படுத்தவும்:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

முழு குறியீட்டிற்காக [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) ஒட்டி பார்த்து கொள்ளுங்கள்.

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

## 🎓 முக்கியக் கற்றுக்கொள்ளல்

1. **முகவர் கட்டமைப்பு**: Microsoft Agent Framework .NET இல் AI முகவர்களை உருவாக்க ஒரு சுத்தமான, வகை-பாதுகாப்பான அணுகுமுறையை வழங்குகிறது
2. **கருவி ஒருங்கிணைவு**: `[Description]` பண்புகளால் சிறப்பிக்கபட்ட செயல்பாடுகள் முகவருக்கு கிடைக்கும் கருவிகளாக மாறுகின்றன
3. **கட்டமைப்பு நிர்வாகம்**: சுற்றுச்சூழல் மாறிகள் மற்றும் பாதுகாப்பான அங்கீகாரகை .NET சிறந்த நடைமுறைகளுக்கு இணங்க செயல்படுகிறது
4. **Azure OpenAI பதில்கள் API**: முகவர் Azure.AI.OpenAI SDK மூலம் Azure OpenAI பதில்கள் API ஐ பயன்படுத்துகிறது

## 🔗 கூடுதல் வளங்கள்

- [Microsoft Agent Framework ஆவணம்](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry இல் Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET ஒற்றை கோப்பு பயன்பாடுகள்](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->