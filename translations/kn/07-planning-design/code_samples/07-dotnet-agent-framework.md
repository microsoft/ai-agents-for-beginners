# 🎯 Azure OpenAI (Responses API) ಜೊತೆಗೆ ಯೋಜನೆ ಮತ್ತು ವಿನ್ಯಾಸ ಮಾದರಿಗಳು (.NET)

## 📋 ತಿಳಿಯಬೇಕಾದ ಗುರಿಗಳು

ಈ ನೋಟ್ಬುಕ್ ಮಾಡಕಾಯ ಗ್ರೇಡ್ ಯೋಜನೆ ಮತ್ತು ವಿನ್ಯಾಸ ಮಾದರಿಗಳನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ .NET ನಲ್ಲಿ Microsoft Agent ಫ್ರೇಮ್ವರ್ಕ್ ಬಳಸಿ ಬುದ್ಧಿವಂತ ಅజೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು Azure OpenAI (Responses API) ಬಳಸಿ. ನೀವು ಅಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸುವುದರಲ್ಲಿ ತಜ್ಞರಾಗುತ್ತೀರಿ, ಇದು ಕಠಿಣ ಸಮಸ್ಯೆಗಳನ್ನು ವಿಭಜಿಸಿ, ಬಹು ಹಂತದ ಪರಿಹಾರಗಳನ್ನು ಯೋಜಿಸಿ, ಮತ್ತು .NET ನ ಎಂಟರ್‌ಪ್ರೈಸ್ ವೈಶಿಷ್ಟ್ಯಗಳೊಂದಿಗೆ ಸುಶಿಕ್ಷಿತ ವರ್ಕ್‌ಫ್ಲೋಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ.

## ⚙️ ಪೂರ್ವಾವಶ್ಯಕತೆಗಳು ಮತ್ತು ಸ್ಥಾಪನೆ

**ವಿಕಸನ ಪರಿಸರ:**
- .NET 9.0 SDK ಅಥವಾ ಹೆಚ್ಚಿನದೊಂದು
- Visual Studio 2022 ಅಥವಾ VS Code C# ವಿಸ್ತರಣೆಯೊಂದಿಗೆ
- Azure OpenAI ಸಂಪನ್ಮೂಲ ಮತ್ತು ಮಾದರಿ ನಿಯೋಜನೆ ಇರುವ Azure ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್
- Azure CLI — `az login` ನೊಂದಿಗೆ ಲಾಗಿನ್ ಆಗಿ

**ಅಗತ್ಯ ಅವಲಂಬನೆಗಳು:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**ಪರಿಸರ ಸಂರಚನೆ (.env ಫೈಲ್):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## ಕೋಡ್ ಚಾಲನೆ

ಈ ಪಾಠದಲ್ಲಿ .NET ಸಿಂಗಲ್ ಫೈಲ್ ಆಪ್ ಅನುಷ್ಠಾನ ಸೇರಿದೆ. ಅದನ್ನು ಓಡಿಸಲು:

```bash
# ಫೈಲ್ ಅನ್ನು ನಡೆಸುವರ್ಹವಾಗಿರಿ (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಚಾಲನೆಮಾಡಿ
./07-dotnet-agent-framework.cs
```

ಅಥವಾ dotnet run ಆಜ್ಞೆ ಬಳಸಿ:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## ಕೋಡ್ ಅನುಷ್ಠಾನ

ಸಂಪೂರ್ಣ ಅನುಷ್ಠಾನ `07-dotnet-agent-framework.cs` ನಲ್ಲಿ ಲಭ್ಯವಿದೆ, ಇದು ಈ ಕೆಳಗಿನಂತೆ ಪ್ರದರ್ಶಿಸುತ್ತದೆ:

- DotNetEnv ಬಳಸಿ ಪರಿಸರ ಸಂರಚನೆಯನ್ನು ಲೋಡ್ ಮಾಡುವುದು
- Responses API ಗೆ Azure OpenAI ಗ್ರಾಹಕನನ್ನು ಸಂರಚಿಸುವುದು
- JSON ಸೀರಿಯಲೈಸೇಶನ್ ಸಹಿತ ಸಂರಚಿತ ಡೇಟಾ ಮಾದರಿಗಳನ್ನು (Plan ಮತ್ತು TravelPlan) ವ್ಯಾಖ್ಯಾನಿಸುವುದು
- JSON ಸ್ಕೀಮಾ ಬಳಸಿ ಸಂರಚಿತ ಔಟ್ ಪುಟ್ ಈಯಾಯ್‌ ಅಜೆಂಟ್ ರಚಿಸುವುದು
- ಪ್ರಕಾರ-ಸುರಕ್ಷಿತ ಪ್ರತಿಕ್ರಿಯೆಗಳೊಂದಿಗೆ ಯೋಜನೆ ವಿನಂತಿಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು

## ಪ್ರಮುಖ ತತ್ತ್ವಗಳು

### ಪ್ರಕಾರ-ಸುರಕ್ಷಿತ ಮಾದರಿಗಳೊಂದಿಗೆ ಸಂರಚಿತ ಯೋಜನೆ

ಅಜೆಂಟ್ C# ಕ್ಲಾಸ್‌ಗಳನ್ನು ಬಳಸಿ ಯೋಜನೆ ಔಟ್ ಪುಟ್ ಗಳ ರಚನೆಯನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುತ್ತದೆ:

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

### ಸಂರಚಿತ ಔಟ್ ಪುಟ್ ಗಳಿಗಾಗಿ JSON ಸ್ಕೀಮಾ

ಅಜೆಂಟ್ TravelPlan ಸ್ಕೀಮಾಗೆ ಹೊಂದಿಕೆಯಾಗುವ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನೀಡಲು ಸಂರಚಿತವಾಗಿದೆ:

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

### ಯೋಜನೆ ಅಜೆಂಟ್ ಸೂಚನೆಗಳು

ಅಜೆಂಟ್ ಸಂಯೋಜಕನಾಗಿದ್ದು, ವಿಶಿಷ್ಟ ಉಪ-ಅಜೆಂಟ್‌ಗಳಿಗೆ ಕಾರ್ಯಗಳನ್ನು ಹಂಚುತ್ತದೆ:

- FlightBooking: ವಿಮಾನ ಟಿಕೆಟ್ ಬುಕ್ಕಿಂಗ್ ಮತ್ತು ವಿಮಾನ ಮಾಹಿತಿಗಾಗಿ
- HotelBooking: ಹೋಟೆಲ್ ಬುಕ್ಕಿಂಗ್ ಮತ್ತು ಹೋಟೆಲ್ ಮಾಹಿತಿಗಾಗಿ
- CarRental: ಕಾರ್ ಬುಕಿಂಗ್ ಮತ್ತು ಕಾರ್ ಬಾಡಿಗೆ ಮಾಹಿತಿಗಾಗಿ
- ActivitiesBooking: ಚಟುವಟಿಕೆ ಬುಕ್ಕಿಂಗ್ ಮತ್ತು ಚಟುವಟಿಕೆ ಮಾಹಿತಿಗಾಗಿ
- DestinationInfo: ಗುರಿ ಸ್ಥಳಗಳ ಬಗ್ಗೆ ಮಾಹಿತಿಗಾಗಿ
- DefaultAgent: ಸಾಮಾನ್ಯ ನಿರೀಕ್ಷಣೆಗಳನ್ನು ನಿರ್ವಹಿಸಲು

## ನಿರೀಕ್ಷಿತ ಫಲಿತಾಂಶ

ಅಜೆಂಟ್ ಟ್ರಾವೆಲ್ ಯೋಜನಾ ವಿನಂತಿಯನ್ನು ಚಾಲನೆ ಮಾಡಿದಾಗ, ಅದು ವಿನಂತಿಯನ್ನು ವಿಶ್ಲೇಷಿಸಿ ಮತ್ತು ವಿಶೇಷ ಅಜೆಂಟ್‌ಗಳಿಗೆ ಸೂಕ್ತ ಕಾರ್ಯ ಹಂಚಿಕೆಗಳೊಂದಿಗೆ JSON ರೂಪದಲ್ಲಿ TravelPlan ಸ್ಕೀಮಾ ಅನುಗುಣವಾದ ಸಂರಚಿತ ಯೋಜನೆಯನ್ನು ರಚಿಸಲಿದೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->