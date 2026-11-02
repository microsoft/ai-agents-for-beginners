# 🎯 Azure OpenAI (Responses API) (.NET) ಜೊತೆಗೆ ಯೋಜನೆ & ವಿನ್ಯಾಸ ಮಾದರಿಗಳು

## 📋 ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ನೋಟುಬುಕ್ ಇಂಟೆಲಿಜೆಂಟ್ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ನೊಂದಿಗೆ .NET ನಲ್ಲಿ Azure OpenAI (Responses API) ಬಳಸಿ ಎಂಟರ್‌ಪ್ರೈಸ್ ಮಟ್ಟದ ಯೋಜನೆ ಮತ್ತು ವಿನ್ಯಾಸ ಮಾದರಿಗಳನ್ನು ತೋರಿಸುತ್ತದೆ. ನೀವು ಜಟಿಲ ಸಮಸ್ಯೆಗಳನ್ನು ವಿಭಜಿಸಲು, ಬಹು ಹಂತದ ಪರಿಹಾರಗಳನ್ನು ಯೋಜಿಸಲು ಮತ್ತು .NETನ ಎಂಟರ್‌ಪ್ರೈಸ್ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಉಪಯೋಗಿಸಿ ಸೂಕ್ಷ್ಮ ವರ್ಕ್‌ಫ್ಲೋಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸುವುದು ಹೇಗೆ ಎಂಬುದನ್ನು ಕಲಿಯುತ್ತೀರಿ.

## ⚙️ ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು ಮತ್ತು ಸജ್ಜು

**ವಿಕಸನ ಪರಿಸರ:**
- .NET 9.0 SDK ಅಥವಾ ಅದಕ್ಕಿಂತ ಮೇಲು
- Visual Studio 2022 ಅಥವಾ C# ವಿಸ್ತರಣೆ ಜೊತೆಗೆ VS Code
- Azure OpenAI ಸಂಪನ್ಮೂಲ ಮತ್ತು ಮಾದರಿ ನಿಯೋಜನೆಯೊಂದಿಗೆ ಒಂದು Azure ಚಂದಾದಾರಿಕೆ
- Azure CLI — `az login` ಮೂಲಕ ಸೈನ್ ಇನ್ ಮಾಡಿ

**ಅವಶ್ಯಕ ಅವಲಂಬನಗಳು:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**ಪರಿಸರ ಸಂರಕ್ಷಣಾ ಸಂರಚನೆ (.env ಫೈಲ್):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## ಕೋಡ್ ರನ್ ಮಾಡುವದು

ಈ ಪಾಠದಲ್ಲಿ .NET ಸಿಂಗಲ್ ಫೈಲ್ ಅಪ್ಲಿಕೇಶನ್ ಜಾರಿ ಇದೆ. ಅದನ್ನು ರನ್ ಮಾಡಲು:

```bash
# ಫೈಲ್‌ನ್ನು ಕಾರ್ಯನಿರ್ವಹಿಸಲು ಅನುಮತಿಸಿ (ಲಿನಕ್ಸ/ಮ್ಯಾಕ್ಓಎಸ್)
chmod +x 07-dotnet-agent-framework.cs

# ಅನ್ವಯಿಕೆಯನ್ನು ನಡೆಯಿಸಿ
./07-dotnet-agent-framework.cs
```

ಅಥವಾ dotnet run ಕಮಾಂಡ್ ಬಳಸಿ:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## ಕೋಡ್ ಜಾರಿಗೊಳಿಸುವಿಕೆ

ಸಂಪೂರ್ಣ ಜಾರಿಗೊಳಿಸುವಿಕೆ `07-dotnet-agent-framework.cs` ನಲ್ಲಿ ಲಭ್ಯವಿದ್ದು, ಇದು ತೋರಿಸುತ್ತದೆ:

- DotNetEnv ಬಳಸಿ ಪರಿಸರ ಸಂರಚನೆಯ ಲೋಡಿಂಗ್
- `GetChatClient().AsAIAgent()` ಬಳಸಿ Azure OpenAI ಕ್ಲೈಯಂಟ್ ಸಂರಚನೆ ಮತ್ತು AI ಏಜೆಂಟ್ ರಚನೆ
- JSON ಸಿರಿಯಲೈಸೇಶನ್ ಜೊತೆ ವಿನ್ಯಾಸಿತ ಡೇಟಾ ಮಾದರಿಗಳ (ಪ್ಲಾನ್ ಮತ್ತು ಟ್ರಾವೆಲ್ ಪ್ಲಾನ್) ವ್ಯಾಖ್ಯಾನ
- JSON ಸ್ಕೀಮಾವನ್ನು ಬಳಸಿ ಸTxAceಡ ರಚನೆ ಆಯುತ್ ಏಜೆಂಟ್ ರಚನೆ
- ಪ್ಲ್ಯಾನಿಂಗ್ ವಿನಂತಿಗಳನ್ನು ಪ್ರಕಾರ-ಭದ್ರ ಪ್ರತಿಕ್ರಿಯೆಗಳಿಂದ ನಿಭಾಯಿಸುವುದು

## ಪ್ರಮುಖ ಕಲ್ಪನೆಗಳು

### ಪ್ರಕಾರ-ಭದ್ರ ಮಾದರಿಗಳೊಂದಿಗೆ ವಿನ್ಯಾಸಿತ ಯೋಜನೆ

ಏಜೆಂಟ್ ಯೋಜನಾ ಔಟ್‌ಪುಟ್‌ಗಳ ರಚನೆಯನ್ನು C# ಕ್ಲಾಸ್‌ಗಳ ಮೂಲಕ ವ್ಯಾಖ್ಯಾನಿಸುತ್ತದೆ:

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

### ವಿನ್ಯಾಸಿತ ಔಟ್‌ಪುಟ್‌ಗಳಿಗೆ JSON ಸ್ಕೀಮಾ

ಏಜೆಂಟ್ ಟ್ರಾವೆಲ್ ಪ್ಲಾನ್ ಸ್ಕೀಮಾ ಅನ್ನು ಹೊಂದಿರುವ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ಹಿಂತಿರುಗಿಸಲು ಸಂರಚಿತವಾಗಿದೆ:

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

### ಯೋಜನಾ ಏಜೆಂಟ್ ಸೂಚನೆಗಳು

ಏಜೆಂಟ್ ಸಂಯೋಜಕರಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸಿ, ವಿಶೇಷೀಕೃತ ಉಪ-ಏಜೆಂಟ್‌ಗಳಿಗೆ ಕಾರ್ಯಗಳನ್ನು ಹಂಚುತ್ತದೆ:

- FlightBooking: ಫ್ಲೈಟ್ ಬುಕ್ಕಿಂಗ್ ಮತ್ತು ವಿಮಾನ ಮಾಹಿತಿ ಒದಗಿಸುವುದಕ್ಕಾಗಿ
- HotelBooking: ಹೋಟೆಲ್ ಬುಕ್ಕಿಂಗ್ ಮತ್ತು ಹೋಟೆಲ್ ಮಾಹಿತಿ ಒದಗಿಸುವುದಕ್ಕಾಗಿ
- CarRental: ಕಾರು ಬುಕ್ಕಿಂಗ್ ಮತ್ತು ಕಾರು ಬಾಡಿಗೆ ಮಾಹಿತಿ ಒದಗಿಸುವುದಕ್ಕಾಗಿ
- ActivitiesBooking: ಕ್ರಿಯಾಕಲಾಪಗಳ ಬುಕ್ಕಿಂಗ್ ಮತ್ತು ಮಾಹಿತಿ ಒದಗಿಸುವುದಕ್ಕಾಗಿ
- DestinationInfo: ಗंतವ್ಯಗಳ ಕುರಿತು ಮಾಹಿತಿ ಒದಗಿಸುವುದಕ್ಕಾಗಿ
- DefaultAgent: ಸಾಮಾನ್ಯ պահանջಗಳನ್ನು ನಿರ್ವಹಿಸುವುದಕ್ಕಾಗಿ

## ನಿರೀಕ್ಷಿತ ಔಟ್‌ಪುಟ್

ನೀವು ಪ್ರವಾಸ ಯೋಜನಾ ವಿನಂತಿಯನ್ನು ಏಜೆಂಟ್‌ಗೆ ರನ್ ಮಾಡಿದಾಗ, ಅದು ವಿನಂತಿಯನ್ನು ವಿಶ್ಲೇಷಿಸಿ, ವಿಶೇಷೀಕೃತ ಏಜೆಂಟ್‌ಗಳಿಗೆ ಸೂಕ್ತ ಕಾರ್ಯ ಹಂಚಿಕೆಗಳೊಂದಿಗೆ ವಿನ್ಯಾಸಿತ ಯೋಜನೆಯನ್ನು ರಚಿಸುತ್ತದೆ, ಇದು ಟ್ರಾವೆಲ್ ಪ್ಲಾನ್ ಸ್ಕೀಮಾ ಅನುಗುಣವಿರುವ JSON ರೂಪದಲ್ಲಿರುತ್ತದೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->