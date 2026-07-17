# 🎯 Planavimo ir Dizaino Šablonai su Azure OpenAI (Atsakymų API) (.NET)

## 📋 Mokymosi Tikslai

Šiame užrašų knygelėje demonstruojami aukščiausio lygio planavimo ir dizaino šablonai kuriant intelektualius agentus naudojant Microsoft Agent Framework .NET su Azure OpenAI (Atsakymų API). Išmoksite kurti agentus, kurie gali detalizuoti sudėtingas problemas, planuoti daugiapakopes sprendimo schemą ir vykdyti pažangias darbo eigas su .NET įmonių funkcijomis.

## ⚙️ Reikalavimai ir Paruošimas

**Plėtros Aplinka:**
- .NET 9.0 SDK arba naujesnė versija
- Visual Studio 2022 arba VS Code su C# plėtiniu
- Azure prenumerata su Azure OpenAI ištekliais ir modelio diegimu
- Azure CLI — prisijunkite naudodami `az login`

**Reikalingos Priklausomybės:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Aplinkos Konfigūracija (.env failas):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

## Kodo Vykdymas

Šioje pamokoje pateikta .NET vieno failo programos implementacija. Norėdami ją paleisti:

```bash
# Padarykite failą vykdomu (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Paleiskite programėlę
./07-dotnet-agent-framework.cs
```

Arba naudokite komandą dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Kodo Įgyvendinimas

Visa implementacija pateikta faile `07-dotnet-agent-framework.cs`, kuri demonstruoja:

- Aplinkos konfigūracijos įkėlimą naudojant DotNetEnv
- Azure OpenAI kliento konfigūravimą ir AI agente kūrimą naudojant `GetChatClient().AsAIAgent()`
- Struktūrizuotų duomenų modelių (Plan ir TravelPlan) apibrėžimą su JSON serializacija
- AI agente kūrimą su struktūruotu išvesties formatu naudojant JSON schemą
- Planavimo užklausų vykdymą su tipais patikrintais atsakymais

## Pagrindinės Sąvokos

### Struktūruotas Planavimas su Tipiškai Patikrintais Modeliais

Agentas naudoja C# klases planavimo išėjimų struktūrai apibrėžti:

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

### JSON Schema Struktūruotoms Išvestims

Agentas sukonfigūruotas grąžinti atsakymus pagal TravelPlan schemą:

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

### Planavimo Agentų Nurodymai

Agentas veikia kaip koordinatorius, paskirstydamas užduotis specializuotiems sub-agentams:

- FlightBooking: Skrydžių rezervavimui ir skrydžių informacijos teikimui
- HotelBooking: Viešbučių rezervavimui ir viešbučių informacijos teikimui
- CarRental: Automobilių nuomai ir nuomos informacijos teikimui
- ActivitiesBooking: Veiklų rezervavimui ir veiklų informacijos teikimui
- DestinationInfo: Informacijos apie kryptis teikimui
- DefaultAgent: Bendrųjų užklausų apdorojimui

## Laukiamas Rezultatas

Paleidus agentą su kelionės planavimo užklausa, jis išanalizuos užklausą ir sugeneruos struktūruotą planą su tinkamu užduočių paskirstymu specializuotiems agentams, suformatuotą kaip JSON, atitinkantį TravelPlan schemą.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->