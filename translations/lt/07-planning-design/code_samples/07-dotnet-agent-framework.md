<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T10:00:36+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "lt"
}
-->
# 🎯 Planavimas ir dizaino šablonai su GitHub modeliais (.NET)

## 📋 Mokymosi tikslai

Šiame užrašų knygelėje pateikiami įmonės lygio planavimo ir dizaino šablonai, skirti kurti intelektualius agentus naudojant Microsoft Agent Framework .NET aplinkoje su GitHub modeliais. Išmoksite kurti agentus, kurie gali suskaidyti sudėtingas problemas, planuoti daugiapakopius sprendimus ir vykdyti sudėtingus darbo procesus, pasinaudodami .NET įmonės funkcijomis.

## ⚙️ Reikalavimai ir nustatymai

**Kūrimo aplinka:**
- .NET 9.0 SDK ar naujesnė versija
- Visual Studio 2022 arba VS Code su C# plėtiniu
- Prieiga prie GitHub Models API

**Reikalingos priklausomybės:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Aplinkos konfigūracija (.env failas):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Kodo paleidimas

Ši pamoka apima .NET vieno failo programos įgyvendinimą. Norėdami ją paleisti:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Arba naudokite komandą dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Kodo įgyvendinimas

Pilnas įgyvendinimas pateiktas `07-dotnet-agent-framework.cs` faile, kuriame demonstruojama:

- Aplinkos konfigūracijos įkėlimas naudojant DotNetEnv
- OpenAI kliento konfigūravimas GitHub modeliams
- Struktūruotų duomenų modelių (Plan ir TravelPlan) apibrėžimas su JSON serializacija
- AI agento kūrimas su struktūruotu išvestimi naudojant JSON schemą
- Planavimo užklausų vykdymas su tipų saugiais atsakymais

## Pagrindinės sąvokos

### Struktūruotas planavimas su tipų saugiais modeliais

Agentas naudoja C# klases, kad apibrėžtų planavimo išvesties struktūrą:

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

### JSON schema struktūruotoms išvestims

Agentas sukonfigūruotas grąžinti atsakymus, atitinkančius TravelPlan schemą:

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

### Planavimo agento instrukcijos

Agentas veikia kaip koordinatorius, deleguodamas užduotis specializuotiems subagentams:

- FlightBooking: Skrydžių rezervavimui ir informacijos apie skrydžius teikimui
- HotelBooking: Viešbučių rezervavimui ir informacijos apie viešbučius teikimui
- CarRental: Automobilių nuomos rezervavimui ir informacijos apie nuomą teikimui
- ActivitiesBooking: Veiklų rezervavimui ir informacijos apie veiklas teikimui
- DestinationInfo: Informacijos apie kelionės tikslus teikimui
- DefaultAgent: Bendrų užklausų tvarkymui

## Tikėtinas rezultatas

Kai paleisite agentą su kelionės planavimo užklausa, jis analizuos užklausą ir sugeneruos struktūruotą planą su tinkamais užduočių paskyrimais specializuotiems agentams, suformatuotą kaip JSON, atitinkantį TravelPlan schemą.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingą interpretaciją, atsiradusią dėl šio vertimo naudojimo.