# 🎯 ಅಜುರ್ ಓಪನ್‌ಎಐ (ಪ್ರತಿಕ್ರಿಯೆಗಳು API) (.NET) ಜೊತೆ ಯೋಜನೆ ಮತ್ತು ವಿನ್ಯಾಸ ಮಾದರಿಗಳು

## 📋 ಅಧ್ಯಯನ ಉದ್ದೇಶಗಳು

ಈ ನೋಟ್‌ಬುಕ್ ಎಂಟರ್‌ಪ್ರೈಸ್‌-ಗ್ರೇಡ್ ಯೋಜನೆ ಮತ್ತು ವಿನ್ಯಾಸ ಮಾದರಿಗಳನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ, ಇದು Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಮತ್ತು .NET ಮೂಲಕ ಅಜುರ್ ಓಪನ್‌ಎಐ (ಪ್ರತಿಕ್ರಿಯೆಗಳು API) ಬಳಸಿ ಬುದ್ಧಿವಂತ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದಕ್ಕೆ. ನೀವು ಸಂಕೀರ್ಣ ಸಮಸ್ಯೆಗಳನ್ನು ವಿಭಜಿಸುವ, ಬಹು ಹಂತದ ಪರಿಹಾರಗಳನ್ನು ಯೋಜಿಸುವ, ಮತ್ತು .NET ನ ಎಂಟರ್‌ಪ್ರೈಸ್ ವೈಶಿಷ್ಟ್ಯಗಳೊಂದಿಗೆ ಸುಕ್ಷ್ಮ ವರ್ಕ್‌ಫ್ಲೋಗಳನ್ನು ನಡೆಸುವ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸುವುದನ್ನು ಕಲಿತೀರಿ.

## ⚙️ ಪೂರ್ವಶರತ್ತುಗಳು ಮತ್ತು ಸ್ಥಾಪನೆ

**ವಿಕಾಸ ಪರಿಸರ:**  
- .NET 9.0 SDK ಅಥವಾ ಹೆಚ್ಚಿನ ಆವೃತ್ತಿ  
- Visual Studio 2022 ಅಥವಾ C# ವಿಸ್ತರಣೆಸಹ VC Code  
- ಅಜುರ್ OpenAI ಸಂಪನ್ಮೂಲ ಮತ್ತು ಮಾದರಿ ನಿಯೋಜನೆ ಹೊಂದಿರುವ ಅಜುರ್ ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್  
- ಅಜುರ್ CLI — `az login` ನೊಂದಿಗೆ ಲಾಗಿನ್ ಆಗಿರಿ  

**ಅವಶ್ಯಕ ನಿರ್ಭರತೆಗಳು:**  
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**ಪರಿಸರ ಸಂರಚನೆ (.env ಫೈಲ್):**  
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

## ಕೋಡ್ ನಡಿಸುವುದು

ಈ ಪಾಠದಲ್ಲಿ .NET ಸಿಂಗಲ್ ಫೈಲ್ ಆಪ್ ಅನುಷ್ಠಾನ ಸೇರಿದೆ. ಅದನ್ನು ನಡಿಸಲು:  

```bash
# ಫೈಲ್ ಅನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಲು (ಲಿನಕ್ಸ್/ಮ್ಯಾಕ್‌ಒಎಸ್)
chmod +x 07-dotnet-agent-framework.cs

# ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಚಾಲನೆಯಿಡಿ
./07-dotnet-agent-framework.cs
```

ಅಥವಾ dotnet run ಆಜ್ಞೆಯನ್ನು ಬಳಸಿ:  

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## ಕೋಡ್ ಅನುಷ್ಠಾನ

ಸಂಪೂರ್ಣ ಅನುಷ್ಠಾನವು `07-dotnet-agent-framework.cs` ನಲ್ಲಿ ಲಭ್ಯವಿದ್ದು, ಇದು ತೋರಿಸುತ್ತದೆ:  

- DotNetEnv ಮೂಲಕ ಪರಿಸರ ಸಂರಚನೆಯನ್ನು ಲೋಡ್ ಮಾಡುವುದು  
- Azure OpenAI ಕ್ಲೈಂಟ್ ಅನ್ನು ಕಾಂಫಿಗರ್ ಮಾಡಿ ಮತ್ತು `GetChatClient().AsAIAgent()` ಬಳಸಿ AI ಏಜೆಂಟ್ ರಚಿಸುವುದು  
- JSON ಸರಣೀಕರಣದೊಂದಿಗೆ ರೂಪರೇಖಾಬದ್ಧ ಮಾಹಿತಿ ಮಾದರಿಗಳನ್ನು (Plan ಮತ್ತು TravelPlan) ವ್ಯಾಖ್ಯಾನಿಸುವುದು  
- JSON ಸ್ಕಿಮಾ ಬಳಸಿ ರೂಪರೇಖಾಬದ್ಧ ಔಟ್‌ಪುಟ್ ಇರುವ AI ಏಜೆಂಟ್ ರಚಿಸುವುದು  
- ಕೌಟುಂಬಿಕ ಭದ್ರತೆಗೆ ಹೊಂದಿಕೊಂಡ ಪ್ರತಿಕ್ರಿಯೆಗಳಿಂದ ಯೋಜನೆ ವಿನಂತಿಗಳನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸುವುದು  

## ಮುಖ್ಯ ಸಂಪ್ರದಾಯಗಳು

### ರೂಪರೇಖಾಬದ್ಧ ಯೋಜನೆ ಕೌಟುಂಬಿಕ ಮಾದರಿಗಳೊಂದಿಗೆ

ಏಜೆಂಟ್ ಯೋಜನೆ ಔಟ್‌ಪುಟ್ ರಚನೆಯನ್ನು ನಿರ್ಧರಿಸಲು C# ತರಗತಿಗಳನ್ನು ಬಳಸುತ್ತದೆ:  

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

### ರೂಪರೇಖಾಬದ್ಧ ಔಟ್‌ಪುಟ್‌ಗಳಿಗಾಗಿ JSON ಸ್ಕಿಮಾ

ಏಜೆಂಟ್ ಪ್ರತಿಕ್ರಿಯೆಗಳು TravelPlan ಸ್ಕೀಮಾ ಹೊಂದಿದಂತೆ ಹೊಂದಿಕೊಳ್ಳುವಂತೆ ಸಂರಚಿಸಲಾಗಿದೆ:  

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

### ಯೋಜನೆ ಏಜೆಂಟ್ ಸೂಚನೆಗಳು

ಏಜೆಂಟ್ ಸಂಯೋಜಕನಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸಿ, ನಿಪುಣ ಉಪಏಜೆಂಟ್‌ಗಳಿಗೆ ಕಾರ್ಯಗಳನ್ನು ಹಂಚುತ್ತದೆ:  

- FlightBooking: ವಿಮಾನ ಸಂರಕ್ಷಣೆ ಮತ್ತು ವಿಮಾನ ಮಾಹಿತಿ ನೀಡುವುದು  
- HotelBooking: ಹೋಟೆಲ್ ಸಂರಕ್ಷಣೆ ಮತ್ತು ಹೋಟೆಲ್ ಮಾಹಿತಿ ನೀಡುವುದು  
- CarRental: ಕಾರು ಕಿರಾಯಿಗೆ ಪಡೆಯುವುದು ಮತ್ತು ಕಾರು ಭಾಡಿಗೆ ಮಾಹಿತಿ ನೀಡುವುದು  
- ActivitiesBooking: ಚಟುವಟಿಕೆಗಳ ಬುಕ್ಕಿಂಗ್ ಮತ್ತು ಚಟುವಟಿಕೆ ಮಾಹಿತಿ ನೀಡುವುದು  
- DestinationInfo: ಗಮ್ಯತೆಯ ಮಾಹಿತಿ ನೀಡುವುದು  
- DefaultAgent: ಸಾಮಾನ್ಯ ವಿನಂತಿಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು  

## ನಿರೀಕ್ಷಿತ ಔಟ್‌ಪುಟ್

ನೀವು ಯೋಜನೆ ವಿನಂತಿಯನ್ನು ಒಳಗೊಂಡಂತೆ ಏಜೆಂಟ್ ಅನ್ನು ನಡಿಸಿದಾಗ, ಅದು ವಿನಂತಿಯನ್ನು ವಿಶ್ಲೇಷಿಸಿ, ನಿಪುಣ ಏಜೆಂಟ್‌ಗಳಿಗೆ ಸೂಕ್ತ ಕಾರ್ಯ ಹಂಚಿಕೆಗಳೊಂದಿಗೆ ರೂಪರೇಖಾಬದ್ಧ ಯೋಜನೆಯನ್ನು ಉತ್ಪಾದಿಸುತ್ತದೆ, ಇದು JSON ಅನ್ನು TravelPlan ಸ್ಕೀಮಾ ಅನುಗುಣವಾಗಿ ರೂಪಿಸಲ್ಪಡುತ್ತದೆ.  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->