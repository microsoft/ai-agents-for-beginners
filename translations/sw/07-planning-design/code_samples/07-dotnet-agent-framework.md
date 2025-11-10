<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:58:54+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "sw"
}
-->
# 🎯 Mipango na Mitindo ya Ubunifu na GitHub Models (.NET)

## 📋 Malengo ya Kujifunza

Notebook hii inaonyesha mipango ya kiwango cha biashara na mitindo ya ubunifu kwa ajili ya kujenga mawakala wenye akili kwa kutumia Microsoft Agent Framework katika .NET na GitHub Models. Utajifunza kuunda mawakala wanaoweza kugawa matatizo magumu, kupanga suluhisho za hatua nyingi, na kutekeleza mtiririko wa kazi wa hali ya juu kwa kutumia vipengele vya biashara vya .NET.

## ⚙️ Mahitaji ya Awali na Usanidi

**Mazingira ya Maendeleo:**
- .NET 9.0 SDK au zaidi
- Visual Studio 2022 au VS Code na kiendelezi cha C#
- Ufikiaji wa GitHub Models API

**Vitegemezi Vinavyohitajika:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Usanidi wa Mazingira (Faili ya .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Kuendesha Msimbo

Somu hili linajumuisha utekelezaji wa Programu ya Faili Moja ya .NET. Ili kuiendesha:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Au tumia amri ya dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Utekelezaji wa Msimbo

Utekelezaji kamili unapatikana katika `07-dotnet-agent-framework.cs`, ambayo inaonyesha:

- Kupakia usanidi wa mazingira kwa kutumia DotNetEnv
- Kuseti mteja wa OpenAI kwa GitHub Models
- Kufafanua mifano ya data iliyopangwa (Plan na TravelPlan) kwa kutumia serialization ya JSON
- Kuunda wakala wa AI na matokeo yaliyopangwa kwa kutumia JSON schema
- Kutekeleza maombi ya mipango na majibu salama kwa aina

## Dhana Muhimu

### Mipango Iliyopangwa na Mifano Salama kwa Aina

Wakala hutumia madarasa ya C# kufafanua muundo wa matokeo ya mipango:

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

### JSON Schema kwa Matokeo Yaliyopangwa

Wakala umesetiwa kurudisha majibu yanayolingana na schema ya TravelPlan:

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

### Maelekezo ya Wakala wa Mipango

Wakala hufanya kama mratibu, akigawa kazi kwa mawakala maalum:

- FlightBooking: Kwa kuweka nafasi za ndege na kutoa taarifa za ndege
- HotelBooking: Kwa kuweka nafasi za hoteli na kutoa taarifa za hoteli
- CarRental: Kwa kuweka nafasi za magari na kutoa taarifa za kukodisha magari
- ActivitiesBooking: Kwa kuweka nafasi za shughuli na kutoa taarifa za shughuli
- DestinationInfo: Kwa kutoa taarifa kuhusu maeneo ya safari
- DefaultAgent: Kwa kushughulikia maombi ya jumla

## Matokeo Yanayotarajiwa

Unapoendesha wakala na ombi la kupanga safari, itachambua ombi hilo na kutoa mpango uliopangwa na mgawanyo wa kazi kwa mawakala maalum, uliopangwa kama JSON inayolingana na schema ya TravelPlan.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.