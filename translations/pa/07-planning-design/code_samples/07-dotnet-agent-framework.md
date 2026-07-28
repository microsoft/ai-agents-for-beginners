# 🎯 ਅਜ਼ੂਰ ਓਪਨਏਆਈ (Responses API) ਨਾਲ ਯੋਜਨਾ ਅਤੇ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ (.NET)

## 📋 ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਹ ਨੋਟਬੁੱਕ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਮਾਇਕਰੋਸੌਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਦਾ ਉਪਯੋਗ ਕਰਕੇ .NET ਨਾਲ ਅਜ਼ੂਰ ਓਪਨਏਆਈ (Responses API) ਦੁਆਰਾ ਬੁੱਧੀਮਾਨ ਏਜੰਟ ਕਿਵੇਂ ਤਿਆਰ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। ਤੁਸੀਂ ਸਿਖੋਗੇ ਕਿ ਏਜੰਟ ਕਿਵੇਂ ਕਠਿਨ ਸਮੱਸਿਆਵਾਂ ਨੂੰ ਟੁੱਟ ਕੇ ਸਮਝ ਸਕਦੇ ਹਨ, ਬਹੁ-ਕਦਮੀ ਹੱਲਾਂ ਦੀ ਯੋਜਨਾ ਬਣਾਉਂਦੇ ਹਨ, ਅਤੇ .NET ਦੀਆਂ ਐਂਟਰਪ੍ਰਾਈਜ਼ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨਾਲ ਸੁਖਦਾਇਕ ਵਰਕਫ਼ਲੋਜ਼ ਨਿਭਾਉਂਦੇ ਹਨ।

## ⚙️ ਲੋੜੀਂਦੇ ਸਧਾਰਨ ਸਾਧਨ ਅਤੇ ਸੈਟਅਪ

**ਡਿਵੈਲਪਮੈਂਟ ਮਾਹੌਲ:**
- .NET 9.0 SDK ਜਾਂ ਇਸ ਤੋਂ ਉੱਪਰ
- Visual Studio 2022 ਜਾਂ VS Code ਸਾਥ C# ਐਕਸਟੈਂਸ਼ਨ
- ਇੱਕ ਅਜ਼ੂਰ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਜਿੱਥੇ ਅਜ਼ੂਰ ਓਪਨਏਆਈ ਸਾਧਨ ਅਤੇ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਮੌਜੂਦ ਹੋਵੇ
- ਅਜ਼ੂਰ CLI — `az login` ਨਾਲ ਸਾਈਨ ਇਨ ਕਰੋ

**ਲੋੜੀਂਦੀਆਂ ਨਿਰਭਰਤਾ:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**ਮਾਹੌਲ ਸੰਰਚਨਾ (.env ਫਾਇਲ):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## ਕੋਡ ਚਲਾਉਣਾ

ਇਸ ਪਾਠ ਵਿੱਚ ਇੱਕ .NET ਸਿੰਗਲ ਫਾਇਲ ਐਪਲੀਕੇਸ਼ਨ ਲਾਗੂ ਕੀਤੀ ਗਈ ਹੈ। ਇਸਨੂੰ ਚਲਾਉਣ ਲਈ:

```bash
# ਫਾਇਲ ਨੂੰ ਚਲਾਉਣ ਯੋਗ ਬਣਾਓ (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਓ
./07-dotnet-agent-framework.cs
```

ਜਾਂ dotnet run ਕਮਾਂਡ ਵਰਤੋਂ:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## ਕੋਡ ਲਾਗੂ ਕਰਨ ਦੀ ਵਿਧੀ

ਪੂਰਾ ਲਾਗੂ ਕੀਤਾ ਕੋਡ `07-dotnet-agent-framework.cs` ਵਿੱਚ ਹੈ, ਜਿੱਥੇ ਇਹਨਾਂ ਗੱਲਾਂ ਦਾ ਪ੍ਰਦਰਸ਼ਨ ਕੀਤਾ ਗਿਆ ਹੈ:

- DotNetEnv ਨਾਲ ਮਾਹੌਲ ਸੰਰਚਨਾ ਨੂੰ ਲੋਡ ਕਰਨਾ
- ਅਜ਼ੂਰ ਓਪਨਏਆਈ ਕਲਾਇੰਟ ਦੀ ਸੰਰਚਨਾ ਅਤੇ `GetChatClient().AsAIAgent()` ਨਾਲ ਏਆਈ ਏਜੰਟ ਬਣਾਉਣਾ
- ਰਚਨਾਤਮਕ ਡਾਟਾ ਮਾਡਲ (Plan ਅਤੇ TravelPlan) ਨੂੰ JSON ਸੀਰੀਅਲਾਈਜ਼ੇਸ਼ਨ ਨਾਲ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨਾ
- JSON schema ਦੀ ਵਰਤੋਂ ਨਾਲ ਰਚਨਾਤਮਕ ਨਤੀਜੇ ਦੇਣ ਵਾਲਾ ਏਜੰਟ ਬਣਾਉਣਾ
- ਟਾਈਪ-ਸੇਫ਼ ਜਵਾਬਾਂ ਨਾਲ ਯੋਜਨਾ ਬਣਾ ਕੇ ਕਮਾਂਡਾਂ ਨੂੰ ਨਿਭਾਉਣਾ

## ਮੁੱਖ ਧਾਰਨਾਵਾਂ

### ਟਾਈਪ-ਸੇਫ਼ ਮਾਡਲਾਂ ਨਾਲ ਰਚਨਾਤਮਕ ਯੋਜਨਾ

ਏਜੰਟ ਯੋਜਨਾ ਨਤੀਜਿਆਂ ਦੀ ਸੰਰਚਨਾ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨ ਲਈ C# ਕਲਾਸਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ:

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

### ਰਚਨਾਤਮਕ ਨਤੀਜਿਆਂ ਲਈ JSON Schema

ਏਜੰਟ ਨੂੰ ਯੋਗ ਬਣਾਇਆ ਗਿਆ ਹੈ ਕਿ ਉਹ TravelPlan schema ਦੇ ਅਨੁਕੂਲ ਜਵਾਬ ਵਾਪਸ ਕਰੇ:

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

### ਯੋਜਨਾ ਬਣਾਉਣ ਵਾਲੇ ਏਜੰਟ ਨਿਰਦੇਸ਼

ਏਜੰਟ ਇੱਕ ਕੋਆਰਡੀਨੇਟਰ ਵਜੋਂ ਕੰਮ ਕਰਦਾ ਹੈ, ਜੋ ਵਿਸ਼ੇਸ਼ ਤੌਰ 'ਤੇ ਵੰਡੇ ਗਏ ਸਬ-ਏਜੰਟਾਂ ਨੂੰ ਕੰਮ ਸੌਂਪਦਾ ਹੈ:

- FlightBooking: ਉਡਾਣਾਂ ਦੀ ਬੁਕਿੰਗ ਅਤੇ ਉਡਾਣ ਦੀ ਜਾਣਕਾਰੀ ਦੇਣ ਲਈ
- HotelBooking: ਹੋਟਲ ਰਿਜ਼ਰਵੇਸ਼ਨ ਅਤੇ ਹੋਟਲ ਜਾਣਕਾਰੀ ਦੇਣ ਲਈ
- CarRental: ਗੱਡੀ ਬੁਕਿੰਗ ਅਤੇ ਕਿਰਾਏ 'ਤੇ ਲੈਣ ਦੀ ਜਾਣਕਾਰੀ ਲਈ
- ActivitiesBooking: ਗਤੀਵਿਧੀਆਂ ਦੀ ਬੁਕਿੰਗ ਅਤੇ ਸਰਗਰਮੀ ਜਾਣਕਾਰੀ ਲਈ
- DestinationInfo: ਮੰਜ਼ਿਲਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਦੇਣ ਲਈ
- DefaultAgent: ਆਮ ਬੇਨਤੀਆਂ ਨੂੰ ਸੰਭਾਲਣ ਲਈ

## ਉਮੀਦ ਕੀਤੀ ਨਤੀਜਾ

ਜਦੋਂ ਤੁਸੀਂ ਯਾਤਰਾ ਯੋਜਨਾ ਬਣਾਉਣ ਦੀ ਬੇਨਤੀ ਨਾਲ ਏਜੰਟ ਚਲਾਂਗੇਗਾ, ਇਹ ਬੇਨਤੀ ਦਾ ਵਿਸਤਾਰ ਨਾਲ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੇਗਾ ਅਤੇ ਵਿਸ਼ੇਸ਼ ਤਜਰਬੇ ਵਾਲੇ ਏਜੰਟਾਂ ਨੂੰ ਕੰਮ ਸੌਂਪ ਕੇ ਸੰਜੋਆ ਹੋਈ ਯੋਜਨਾ ਤਿਆਰ ਕਰੇਗਾ, ਜੋ ਕਿ TravelPlan schema ਦੇ ਅਨੁਕੂਲ JSON ਰੂਪ ਵਿੱਚ ਹੋਵੇਗੀ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->