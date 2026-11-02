# 🎯 Azure OpenAI (Responses API) உடன் திட்டமிடல் மற்றும் வடிவமைப்பு முறைமைகள் (.NET)

## 📋 கற்றல் இலக்குகள்

இந்த நோட்புக், Azure OpenAI (Responses API) உடன் .NET இலுள்ள Microsoft Agent Framework ஐப் பயன்படுத்தி நுட்பமான முகவர்களை உருவாக்குவதற்கான தொழிற்சாலை தரமான திட்டமிடல் மற்றும் வடிவமைப்பு முறைமைகளை காண்பிக்கும். நீங்கள் சிக்கலான பிரச்சனைகளை சிறு பகுதிகளாக பிரித்து, பல படி தீர்வுகளை திட்டமிட்டு, .NET இன் தொழிற்சாலை அம்சங்களுடன் நுண்ணறிவான வேலைசெய்தல்களை நடைமுறைப்படுத்தும் முகவர்களை உருவாக்க கற்கலாம்.

## ⚙️ முன் தேவைகள் மற்றும் அமைப்பு

**உருவாக்க சூழல்:**
- .NET 9.0 SDK அல்லது அதற்கு மேல்
- Visual Studio 2022 அல்லது C# விரிவாக்கத்துடன் VS Code
- Azure OpenAI வளமும் மாதிரி பகிர்வு உள்ள Azure சந்தா
- Azure CLI — `az login` மூலம் உள்நுழையவும்

**தேவையான சார்புகள்:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**சூழல் கட்டமைப்பு (.env கோப்பு):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## கோடு இயக்கு

இந்த பாடத்தில் .NET Single File App உடன் செயல்படுத்தல் உள்ளது. அதை இயங்க:

```bash
# கோப்பை செயல்படுத்தக்கூடியதாக மாற்று (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# பயன்பாட்டை இயக்கு
./07-dotnet-agent-framework.cs
```

அல்லது dotnet run கட்டளையைப் பயன்படுத்தவும்:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## கோடு செயல்படுத்தல்

முழுமையான செயல்படுத்தல் `07-dotnet-agent-framework.cs`-ல் உள்ளது, இதில் காணப்படும்:

- DotNetEnv மூலம் சூழல் கட்டமைப்பை ஏற்றுதல்
- Azure OpenAI கிளையன்டை அமைத்து `GetChatClient().AsAIAgent()` பயன்படுத்தி AI முகவர்களை உருவாக்குதல்
- JSON தொடர் இடைமுகத்துடன் கட்டமைக்கப்பட்ட தரவுக் கோப்புறை (Plan மற்றும் TravelPlan) வரையறை
- JSON ஸ்கீமாவுடன் கட்டமைக்கப்பட்ட வெளிப்பாட்டையுள்ள AI முகவர்களை உருவாக்குதல்
- வகை பாதுகாப்பான பதில்களுடன் திட்டமிடல் கோரிக்கைகளை செயல்படுத்துதல்

## முக்கிய கருத்துகள்

### வகை பாதுகாப்பான மாதிரிகள் உடன் கட்டமைக்கப்பட்ட திட்டமிடல்

முகவர், திட்டமிடல் வெளியீட்டின் கட்டமைப்புக்காக C# வகைகளை பயன்படுத்துகிறான்:

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

### கட்டமைக்கப்பட்ட வெளிப்பாடுகளுக்கான JSON ஸ்கீமா

முகவர், TravelPlan ஸ்கீமாவிற்கு இணையான பதில்களை தர அமைக்கப்பட்டுள்ளது:

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

### திட்டமிடல் முகவரின் வழிகள்

முகவர் ஒருங்கிணைப்பாளராக செயல்பட்டு, சிறப்பு வாய்ந்த துணை முகவர்களிடம் பணிகளை ஒப்படைக்கிறான்:

- FlightBooking: விமானங்களைப் இட ஒதுக்கி, விமான தகவல்களை வழங்க
- HotelBooking: ஹோட்டல்களைப் பதிவு செய்து, ஹோட்டல் தகவல்களை கொடுத்து
- CarRental: கார்கள் வாடகைக்கு எடுத்துக் கொடுத்து, வாடகை தகவல்களை வழங்க
- ActivitiesBooking: செயல்பாடுகளைப் பதிவு செய்து, செயல்பாடுகள் தகவலை வழங்க
- DestinationInfo: பயண இடங்களைக் குறித்த தகவல்களை வழங்க
- DefaultAgent: பொதுவான கோரிக்கைகளை கையாள

## எதிர்பார்க்கப்படும் வெளியீடு

பயண திட்டமிடல் கோரிக்கையுடன் முகவரைக் இயக்கும் போது, அது கோரிக்கையை பகுப்பாய்வு செய்து, சிறப்பு வாய்ந்த முகவர்களுக்கு பணி ஒதுக்குமுறையுடன் கட்டமைக்கப்பட்ட JSON வடிவமைப்பில் TravelPlan ஸ்கீமாவிற்கு இணையான திட்டத்தை உருவாக்கும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->