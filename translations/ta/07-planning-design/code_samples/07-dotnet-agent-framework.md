# 🎯 Azure OpenAI (Responses API) உடன் திட்டமிடல் மற்றும் வடிவமைப்பு மாதிரிகள் (.NET)

## 📋 கற்றல் இலக்குகள்

இந்த நோட்புக் Microsoft Agent Framework ஐ .NET உடன் Azure OpenAI (Responses API) பயன்படுத்தி தாங்கிய முகவர்கள் கட்டமைப்பதற்கான தொழில் தரத்திலான திட்டமிடல் மற்றும் வடிவமைப்பு மாதிரிகளை காட்டுுகிறது. நீங்கள் சிக்கலான பிரச்சனைகளை உடைக்கக்கூடிய, பல அடியடி தீர்வுகளை திட்டமிடக்கூடிய மற்றும் .NET இன் தொழில் அம்சங்களுடன் நுட்பமான வேலைநிரல்களை செயல்படுத்தக்கூடிய முகவர்களை உருவாக்க கற்றுக் கொள்வீர்கள்.

## ⚙️ தேவையானவை மற்றும் அமைப்பு

**வளImmediate Development Environment:**
- .NET 9.0 SDK அல்லது அதற்கும் மேலான பதிப்பு
- Visual Studio 2022 அல்லது C# நீட்டிப்புடன் VS Code
- Azure OpenAI வளம் மற்றும் மாதிரி உருவாக்கம் கொண்ட Azure சந்தா
- Azure CLI — `az login` கொண்டு கையொப்பமிடுக

**தேவையான சார்புகள்:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**சூழல் அமைப்பு (.env கோப்பு):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

## குறியீட்டை இயக்கல்

இந்த பாடம் .NET Single File App நடைமுறையை உள்ளடக்கியது. இதை இயக்க:

```bash
# கோப்பை செயல் திறனாக்கவும் (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# பயன்பாட்டை இயக்கவும்
./07-dotnet-agent-framework.cs
```

அல்லது dotnet run காமண்ட் பயன்படுத்தவும்:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## குறியீட்டு நடைமுறை

முழுமையான நடைமுறை `07-dotnet-agent-framework.cs` இல் கிடைக்கிறது, இதில் காட்டப்பட்டுள்ளவை:

- DotNetEnv கொண்டு சூழல் அமைப்பை ஏற்று கொள்வது
- Azure OpenAI கிளையண்டை உள்ளமைத்து `GetChatClient().AsAIAgent()` மூலம் AI முகவர்களை உருவாக்குதல்
- JSON தொடர் மூலம் கட்டமைக்கப்பட்ட தரவு மாதிரிகள் (Plan மற்றும் TravelPlan) வரையறுத்தல்
- JSON ஸ்கீமாவைக் கொண்டு கட்டமைக்கப்பட்ட வெளியீடு கொண்ட AI முகவர்களை உருவாக்குதல்
- வகை-பாதுகாக்கப்பட்ட பதில்களுடன் திட்டமிடல் கோரிக்கைகளை இயக்குதல்

## முக்கிய கருத்துக்கள்

### வகை-பாதுகாக்கப்பட்ட மாதிரிகளுடன் கட்டமைக்கப்பட்ட திட்டமிடல்

முகவர் திட்டமிடல் வெளியீடுகளின் அமைப்பை C# வகுப்புகளைப் பயன்படுத்தி வரையறுக்கிறார்:

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### கட்டமைக்கப்பட்ட வெளியீடுகளுக்கு JSON ஸ்கீமா

முகவர் TravelPlan ஸ்கீமாவுக்கு பொருந்தும் பதில்களை தர அமைக்கப்பட்டுள்ளது:

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### திட்டமிடல் முகவர் வழிமுறைகள்

முகவர் ஒருங்கிணைப்பாளராக செயல்பட்டு, சிறப்பான துணை முகவர்களுக்கு பணிகளை ஒப்படைக்கிறார்:

- FlightBooking: விமானம் முன்பதிவு மற்றும் விமான விவரங்கள் வழங்க
- HotelBooking: ஹோட்டல் முன்பதிவு மற்றும் ஹோட்டல் விவரங்கள் வழங்க
- CarRental: கார்கள் முன்பதிவு மற்றும் கார் வாடகை தகவல்கள் வழங்க
- ActivitiesBooking: செயல்பாடுகள் முன்பதிவு மற்றும் செயல்பாட்டு தகவல்கள் வழங்க
- DestinationInfo: இடங்களுக்கான தகவல்களை வழங்க
- DefaultAgent: பொதுவான கோரிக்கைகளை கையாள

## எதிர்பார்க்கும் வெளியீடு

நீங்கள் பயணத் திட்டமிடல் கோரிக்கையுடன் முகவரைக் இயக்கும் போது, அது கோரிக்கையை ஆய்வு செய்து சிறப்பான துணை முகவர்களுக்கு தேவையான பணிகளுடன் கட்டமைக்கப்பட்ட திட்டத்தை உருவாக்கும், இது TravelPlan ஸ்கீமாவுக்கேற்ற JSON வடிவத்தில் இருக்கும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->