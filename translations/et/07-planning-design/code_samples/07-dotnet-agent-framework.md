# 🎯 Plaanimine ja disainimustrid Azure OpenAI-ga (Responses API) (.NET)

## 📋 Õpieesmärgid

See märkmik demonstreerib ettevõtte tasemel planeerimis- ja disainimustreid intelligentsete agentide loomiseks, kasutades Microsoft Agent Frameworki .NET-is Azure OpenAI-ga (Responses API). Õpid looma agente, kes suudavad keerukaid probleeme lagundada, kavandada mitmeastmelisi lahendusi ja täita keerukaid töövooge, kasutades .NET-i ettevõtte funktsionaalsust.

## ⚙️ Eeltingimused ja seadistamine

**Arenduskeskkond:**
- .NET 9.0 SDK või uuem
- Visual Studio 2022 või VS Code koos C# laiendusega
- Azure tellimus koos Azure OpenAI ressursi ja mudeli juurutusega
- Azure CLI — logi sisse käsuga `az login`

**Nõutavad sõltuvused:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Keskkonna konfiguratsioon (.env fail):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

## Koodi käivitamine

See õppetund sisaldab .NET ühe faili rakenduse implementatsiooni. Käivitamiseks:

```bash
# Muuda fail täidetavaks (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Käivita rakendus
./07-dotnet-agent-framework.cs
```

Või kasuta käsku dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Koodi implementatsioon

Täielik implementatsioon on saadaval failis `07-dotnet-agent-framework.cs`, mis demonstreerib:

- Keskkonna konfiguratsiooni laadimist DotNetEnv abil
- Azure OpenAI kliendi seadistamist ja AI agendi loomist kasutades `GetChatClient().AsAIAgent()`
- Struktureeritud andmemudelite (Plan ja TravelPlan) defineerimist JSON serialiseerimisega
- AI agendi loomist struktureeritud väljundiga, kasutades JSON skeemi
- Planeerimisnõudmiste täitmist tüübikindlate vastustega

## Põhikontseptsioonid

### Struktureeritud planeerimine tüübikindlate mudelitega

Agent kasutab C# klasse planeerimisväljundite struktuuri määratlemiseks:

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

### JSON skeem struktureeritud väljunditele

Agent on seadistatud tagastama vastuseid, mis vastavad TravelPlan skeemile:

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

### Planeerimisagendi juhised

Agent tegutseb koordinaatorina, delegeerides ülesanded spetsialiseeritud alamagenditele:

- FlightBooking: lendude broneerimiseks ja lennuinformatsiooni andmiseks
- HotelBooking: hotellide broneerimiseks ja hotelli info andmiseks
- CarRental: autorendi broneerimiseks ja autorendi info andmiseks
- ActivitiesBooking: tegevuste broneerimiseks ja tegevuste info andmiseks
- DestinationInfo: sihtkohtade info andmiseks
- DefaultAgent: üldiste päringute käsitlemiseks

## Oodatav väljund

Kui käivitad agendi reisi planeerimise päringuga, analüüsib ta päringu ja genereerib struktureeritud plaani, kus on sobivad ülesannete jaotused spetsialiseeritud agentidele, vormindatuna JSON-ina, mis vastab TravelPlan skeemile.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->