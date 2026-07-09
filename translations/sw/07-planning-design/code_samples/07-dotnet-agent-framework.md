# 🎯 Mipango & Mifumo ya Ubunifu na Azure OpenAI (API za Majibu) (.NET)

## 📋 Malengo ya Kujifunza

Daftari hili linaonyesha mifumo ya mipango na ubunifu ya kiwango cha biashara kwa kujenga mawakala wa akili kwa kutumia Microsoft Agent Framework katika .NET na Azure OpenAI (API za Majibu). Utajifunza kuunda mawakala wanaoweza kugawanya matatizo magumu, kupanga suluhisho zenye hatua nyingi, na kutekeleza mtiririko wa kazi mgumu kwa kutumia vipengele vya biashara vya .NET.

## ⚙️ Mahitaji & Usanidi

**Tayari ya Maendeleo:**
- .NET 9.0 SDK au zaidi
- Visual Studio 2022 au VS Code yenye ugani wa C#
- Usajili wa Azure wenye rasilimali ya Azure OpenAI na usambazaji wa mfano
- CLI ya Azure — ingia kwa kutumia `az login`

**Mategemeo Yanayohitajika:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Usanidi wa Mazingira (faili .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Kuendesha Kodi

Somo hili linajumuisha utekelezaji wa Programu ya Faili Moja ya .NET. Ili kuendesha:

```bash
# Fanya faili iweze kutekelezwa (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Endesha programu
./07-dotnet-agent-framework.cs
```

Au tumia amri ya dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Utekelezaji wa Kodi

Utekelezaji kamili upo kwenye `07-dotnet-agent-framework.cs`, unaoonesha:

- Kupakia usanidi wa mazingira kwa DotNetEnv
- Kusanidi mteja wa Azure OpenAI kwa API za Majibu
- Kufafanua mifano ya data iliyopangwa (Plan na TravelPlan) kwa usanifishaji wa JSON
- Kuunda wakala wa AI mwenye matokeo yaliyopangwa kwa kutumia schema ya JSON
- Kutekeleza maombi ya mipango kwa majibu salama kwa aina

## Dhana Muhimu

### Mipango Iliyo Pangiliwa na Mifano Salama kwa Aina

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

### Schema ya JSON kwa Matokeo Yaliyo Pangiliwa

Wakala amesanidiwa kurudisha majibu yanayolingana na schema ya TravelPlan:

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

### Maelekezo ya Wakala wa Upangaji

Wakala hufanya kazi kama mratibu, akigawanya kazi kwa mawakala wadogo maalum:

- Booking ya Ndege: Kwa kuhifadhi tiketi za ndege na kutoa taarifa za ndege
- Booking ya Hoteli: Kwa kuhifadhi hoteli na kutoa taarifa za hoteli
- Kodi ya Magari: Kwa kuhifadhi magari na kutoa taarifa za kukodisha gari
- Booking za Shughuli: Kwa kuhifadhi shughuli na kutoa taarifa za shughuli
- Taarifa za Mwendokasi: Kwa kutoa taarifa kuhusu maeneo ya kusafiri
- Wakala wa Kawaida: Kwa kushughulikia maombi ya jumla

## Matokeo Yanayotarajiwa

Unapomendesha wakala na ombi la kupanga safari, atachambua ombi na kutengeneza mpango uliopangwa kwa mgawanyo sahihi wa kazi kwa mawakala maalum, uliowekwa kwenye muundo wa JSON unaoendana na schema ya TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->