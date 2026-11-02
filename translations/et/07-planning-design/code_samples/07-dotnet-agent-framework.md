# 🎯 Planeerimine ja disainimustrid Azure OpenAI-ga (Responses API) (.NET)

## 📋 Õpieesmärgid

See märkmik demonstreerib ettevõtte tasemel planeerimis- ja disainimustreid intelligentsete agentide loomisel Microsoft Agent Frameworkiga .NET-is, kasutades Azure OpenAI-d (Responses API). Õpid looma agente, kes suudavad keerulisi probleeme lahutada, planeerida mitmeastmelisi lahendusi ning täita keerukaid töövooge, kasutades .NET ettevõtte funktsioone.

## ⚙️ Eeltingimused ja seadistamine

**Arenduskeskkond:**
- .NET 9.0 SDK või uuem
- Visual Studio 2022 või VS Code koos C# laiendusega
- Azure tellimus Azure OpenAI ressursi ja mudeli juurutusega
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
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Koodi käivitamine

Selle õppetüki hulka kuulub .NET Single File App rakendus. Selleks, et seda käivitada:

```bash
# Tee fail käivitatavaks (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Käivita rakendus
./07-dotnet-agent-framework.cs
```

Või kasuta käsku dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Koodi rakendamine

Täielik rakendus on saadaval failis `07-dotnet-agent-framework.cs`, mis demonstreerib:

- Keskkonna konfiguratsiooni laadimist DotNetEnv abil
- Azure OpenAI kliendi seadistamist ja AI agendi loomist kasutades `GetChatClient().AsAIAgent()`
- Struktureeritud andmemudelite (Plan ja TravelPlan) defineerimist JSON serialiseerimisega
- AI agendi loomist struktureeritud väljundiga JSON skeemi abil
- Planeerimispäringute täitmist tüübitundlike vastustega

## Põhimõisted

### Struktureeritud planeerimine tüübitundlike mudelitega

Agent kasutab C# klasse planeerimise väljundite struktuuri määratlemiseks:

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

Agent tegutseb koordinaatorina, delegeerides ülesandeid spetsialiseeritud alagentidele:

- FlightBooking: Lennupiletite broneerimiseks ja lennuinfo andmiseks
- HotelBooking: Hotellide broneerimiseks ja hotelliinfo andmiseks
- CarRental: Autode rentimiseks ja autorendiinfo andmiseks
- ActivitiesBooking: Aktiivsuste broneerimiseks ja aktiivsuste info andmiseks
- DestinationInfo: Sihtkohtade kohta info andmiseks
- DefaultAgent: Üldiste päringute käsitlemiseks

## Oodatav väljund

Kui käivitad agendi reisiplaani päringuga, analüüsib see päringu ja genereerib struktureeritud plaani, kus on asjakohased ülesannete jaotused spetsialiseerunud agentidele, vormindatuna JSON-ina, mis vastab TravelPlan skeemile.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->