# 🎯 Azure OpenAI உடன் திட்டமிடல் மற்றும் வடிவமைப்பு வடிவங்கள் (Responses API) (.NET)

## 📋 கற்றல் குறிக்கோள்கள்

இந்த நோட்புக் .NET இல் Azure OpenAI (Responses API) பயன்படுத்தி Microsoft Agent Framework மூலம் நுண்ணறிவு ஏஜென்ட்களை உருவாக்குவதற்கான நிறுவன தரம் வாய்ந்த திட்டமிடல் மற்றும் வடிவமைப்பு முறைகளை காட்சிப்படுத்துகிறது. நீங்கள் சிக்கலான பிரச்சனைகளை பிரிக்கும், பல படி தீர்வுகளை திட்டமிடும் மற்றும் .NET நிறுவன அம்சங்களுடன் திறமையான வேலைப்பாட்டை செயல்படுத்தும் ஏஜென்டுகளை உருவாக்க கற்றுக்கொள்ளப் போகிறீர்கள்.

## ⚙️ தேவையான முன் நிலையமைப்புகள் மற்றும் அமைப்பு

**அமைப்பு சூழல்:**
- .NET 9.0 SDK அல்லது அதற்கு மேலான பதிப்பு
- Visual Studio 2022 அல்லது C# நீட்சியுடன் VS Code
- Azure OpenAI வளம் மற்றும் மodel் டிப்பிளுமான்ட் கொண்ட Azure சந்தா
- Azure CLI —  `az login` மூலம் உள்நுழையவும்

**தேவையான சார்புகள்:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**சூழல் கட்டமைப்பு (.env கோப்பு):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## குறியீட்டை இயக்கு

இந்த பாடத்தில் .NET Single File பயன்பாட்டின் செயல்பாடு உள்ளது. இதனை இயக்க:

```bash
# கோப்பை இயங்கு படுத்தக்கூடியதாக மாற்றுக (லினக்ஸ்/மாக்ஓஎஸ்)
chmod +x 07-dotnet-agent-framework.cs

# செயலியை இயக்குக
./07-dotnet-agent-framework.cs
```

அல்லது dotnet run கட்டளையை பயன்படுத்தவும்:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## குறியீட்டு செயலாக்கம்

முழு செயலாக்கம் `07-dotnet-agent-framework.cs` கோப்பில் கிடைக்கிறது, இது பின்வருவனைக் காட்சிப்படுத்துகிறது:

- DotNetEnv உடன் சூழல் கட்டமைப்பை ஏற்றுதல்
- Responses API க்கான Azure OpenAI கிளையனை கட்டமைத்தல்
- JSON serialization உடன் கட்டமைக்கப்பட்ட தரவுக்கட்டுக்கள் (Plan மற்றும் TravelPlan) வரையறுத்தல்
- JSON schema பயன்படுத்தி கட்டமைக்கப்பட்ட வெளியீடுடன் AI ஏஜென்டை உருவாக்குதல்
- வகை பாதுகாப்பு பதில்களுடன் திட்டமிடல் கோரிக்கைகளை செயல்படுத்துதல்

## முக்கிய கருத்துக்கள்

### வகை பாதுகாப்பு மாடல்களுடன் கட்டமைக்கப்பட்ட திட்டமிடல்

ஏஜென்ட் திட்டமிடல் வெளியீடுகளின் அமைப்பை C# வகுப்புகளைப் பயன்படுத்தி வரையறுக்கிறது:

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

### கட்டமைக்கப்பட்ட வெளியீடுகளுக்கான JSON திட்டவட்டம்

ஏஜென்டு TravelPlan திட்டவட்டத்துடன் பொருந்தும் பதில்களை வழங்க கட்டமைக்கப்பட்டுள்ளது:

```csharp
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### திட்டமிடும் ஏஜென்ட் வழிமுறைகள்

ஏஜென்ட் ஒருங்கிணைப்பாளராக செயல்பட்டு, தனிப்பயன் துணை ஏஜென்ட்களுக்கு பணிகளை வழங்குகிறது:

- FlightBooking: விமானங்களை முன்பதிவு செய்வது மற்றும் விமானத் தகவல்களை வழங்குவது
- HotelBooking: விடுதிகளை முன்பதிவு செய்வது மற்றும் விடுதி தகவல்களை வழங்குவது
- CarRental: கார்கள் முன்பதிவு செய்வது மற்றும் கார் வாடகை தகவல்களை வழங்குவது
- ActivitiesBooking: செயல்பாடுகளை முன்பதிவு செய்வது மற்றும் செயல்பாடு தகவல்களை வழங்குவது
- DestinationInfo: பயண இடங்களைப் பற்றிய தகவல்களை வழங்குவது
- DefaultAgent: பொது கோரிக்கைகளை கையாளுவது

## எதிர்பார்க்கப்படும் வெளியீடு

நீங்கள் பயண திட்டமிடல் கோரிக்கையுடன் ஏஜென்டை இயக்கும் பொது, அது கோரிக்கையை பகுப்பாய்வு செய்து, TravelPlan திட்டவட்டத்துடன் பொருந்தும் JSON வடிவில் சிறப்பு ஏஜென்ட்களுக்கு பொருத்தமான பணிகளுடன் கட்டமைக்கப்பட்ட திட்டத்தை உருவாக்கும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->