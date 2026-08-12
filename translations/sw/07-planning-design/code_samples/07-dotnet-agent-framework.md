# 🎯 Mipango & Mitindo ya Ubunifu na Azure OpenAI (Responses API) (.NET)

## 📋 Malengo ya Kujifunza

Daftari hili linaonyesha mipango ya daraja la biashara na mitindo ya ubunifu kwa kujenga mawakala wa akili kwa kutumia Microsoft Agent Framework katika .NET na Azure OpenAI (Responses API). Utajifunza kuunda mawakala wanaoweza kugawanya matatizo magumu, kupanga suluhisho za hatua nyingi, na kutekeleza michakato tata kwa kutumia vipengele vya biashara vya .NET.

## ⚙️ Mahitaji ya Awali & Usanidi

**Mazingira ya Maendeleo:**
- .NET 9.0 SDK au ya juu
- Visual Studio 2022 au VS Code na ugani wa C#
- Usajili wa Azure una rasilimali ya Azure OpenAI na usambazaji wa mfano
- Azure CLI — ingia kwa kutumia `az login`

**Mategemeo Yanayohitajika:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Usanidi wa Mazingira (faili la .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Kuendesha Msimbo

Somo hili linajumuisha utekelezaji wa Programu Moja ya Faili ya .NET. Ili kuiendesha:

```bash
# Fanya faili iwe executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Endesha programu
./07-dotnet-agent-framework.cs
```

Au tumia amri ya dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Utekelezaji wa Msimbo

Utekelezaji kamili upo katika `07-dotnet-agent-framework.cs`, unaoonyesha:

- Kupakia usanidi wa mazingira kwa kutumia DotNetEnv
- Kusanidi mteja wa Azure OpenAI na kuunda wakala wa AI kwa kutumia `GetChatClient().AsAIAgent()`
- Kuanza mifano ya data yenye muundo (Plan na TravelPlan) kwa serialization ya JSON
- Kuunda wakala wa AI kwa matokeo yenye muundo kwa kutumia schema ya JSON
- Kutekeleza maombi ya mipango na majibu salama kwa aina

## Dhana Muhimu

### Mipango Yenye Muundo kwa Mifano Salama kwa Aina

Wakala hutumia darasa za C# kufafanua muundo wa matokeo ya mipango:

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

### Schema ya JSON kwa Matokeo Yenye Muundo

Wakala amesanidiwa kurudisha majibu yanayolingana na schema ya TravelPlan:

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

### Maelekezo ya Wakala wa Mipango

Wakala hufanya kama mpatanishi, akigawa kazi kwa mawakala maalum:

- Reservation ya Ndege: Kwa kuhifadhi ndege na kutoa taarifa za ndege
- Reservation ya Hoteli: Kwa kuhifadhi hoteli na kutoa taarifa za hoteli
- Kukodisha Gari: Kwa kukodisha magari na kutoa taarifa za kukodisha gari
- Reservation ya Shughuli: Kwa kuhifadhi shughuli na kutoa taarifa za shughuli
- Taarifa za Marudio: Kwa kutoa taarifa kuhusu marudio
- Wakala wa Kawaida: Kwa kushughulikia maombi ya jumla

## Matokeo Yanayotarajiwa

Unapoendesha wakala na ombi la kupanga safari, atachambua ombi hilo na kuzalisha mpango wenye muundo na ugawaji wa kazi inayofaa kwa mawakala maalum, umeandaliwa kama JSON inayokubaliana na schema ya TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->