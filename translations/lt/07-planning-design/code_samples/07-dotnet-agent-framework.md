# 🎯 Planavimas ir dizaino šablonai su Azure OpenAI (Atsakymų API) (.NET)

## 📋 Mokymosi tikslai

Ši užrašų knygutė demonstruoja įmonės lygio planavimo ir dizaino šablonus, kaip kurti išmaniuosius agentus naudojant Microsoft Agent Framework .NET su Azure OpenAI (Atsakymų API). Išmoksite kurti agentus, kurie gali suskaidyti sudėtingas problemas, planuoti daugiažingsnius sprendimus ir vykdyti sudėtingus darbo srautus, naudojant .NET įmonės funkcijas.

## ⚙️ Reikalavimai ir nustatymas

**Kūrimo aplinka:**
- .NET 9.0 SDK arba naujesnė versija
- Visual Studio 2022 arba VS Code su C# plėtiniu
- Azure prenumerata su Azure OpenAI ištekliumi ir modelio diegimu
- Azure CLI — prisijunkite su `az login`

**Reikalingos priklausomybės:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Aplinkos konfigūracija (.env failas):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Kodo vykdymas

Šiame pamokoje yra .NET vieno failo programos įgyvendinimas. Norėdami ją paleisti:

```bash
# Padarykite failą vykdomu (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Paleiskite programą
./07-dotnet-agent-framework.cs
```

Arba naudokite dotnet run komandą:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Kodo įgyvendinimas

Pilnas įgyvendinimas yra faile `07-dotnet-agent-framework.cs`, kuris demonstruoja:

- Aplinkos konfigūracijos įkėlimą naudojant DotNetEnv
- Azure OpenAI kliento konfigūravimą ir AI agente kūrimą su `GetChatClient().AsAIAgent()`
- Struktūrinių duomenų modelių (Plan ir TravelPlan) apibrėžimą su JSON serializacija
- AI agente kūrimą su struktūruotu rezultatu naudojant JSON schemą
- Planavimo užklausų vykdymą su tipų saugiais atsakymais

## Pagrindinės sąvokos

### Struktūruotas planavimas su tipų saugiais modeliais

Agentas naudoja C# klases apibrėžti planavimo išvesties struktūrai:

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

Agentas yra sukonfigūruotas grąžinti atsakymus, atitinkančius TravelPlan schemą:

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

### Planavimo agente nurodymai

Agentas veikia kaip koordinatorius, paskirdamas užduotis specializuotiems subagentams:

- FlightBooking: Skrydžių užsakymui ir skrydžių informacijos pateikimui
- HotelBooking: Viešbučių užsakymui ir viešbučių informacijos pateikimui
- CarRental: Automobilių nuomai ir automobilių nuomos informacijos pateikimui
- ActivitiesBooking: Veiklų užsakymui ir veiklų informacijos pateikimui
- DestinationInfo: Turizmo vietovių informacijos pateikimui
- DefaultAgent: Bendrų užklausų tvarkymui

## Tikėtina išvestis

Kai paleisite agentą su kelionės planavimo užklausa, jis analizuos užklausą ir sukurs struktūruotą planą su tinkamu užduočių paskirstymu specializuotiems agentams, suformatuotą JSON formatu, atitinkančiu TravelPlan schemą.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->