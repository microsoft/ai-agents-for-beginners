# 🎯 Suunnittelu ja suunnittelumallit Azure OpenAI:n kanssa (Vastaus-API) (.NET)

## 📋 Oppimistavoitteet

Tämä muistikirja esittelee yritystason suunnittelu- ja suunnittelumalleja älykkäiden agenttien rakentamiseen Microsoft Agent Frameworkin avulla .NET:llä ja Azure OpenAI:lla (Vastaus-API). Opit luomaan agenteja, jotka osaavat hajottaa monimutkaisia ongelmia, suunnitella monivaiheisia ratkaisuja ja suorittaa kehittyneitä työnkulkuja .NET:n yritysominaisuuksilla.

## ⚙️ Edellytykset ja asennus

**Kehitysympäristö:**
- .NET 9.0 SDK tai uudempi
- Visual Studio 2022 tai VS Code C#-laajennuksella
- Azure-tilaus, jossa on Azure OpenAI -resurssi ja mallin käyttöönotto
- Azure CLI — kirjaudu sisään komennolla `az login`

**Vaaditut riippuvuudet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Ympäristöasetukset (.env-tiedosto):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Koodin suorittaminen

Tämä oppitunti sisältää .NET Single File App -toteutuksen. Suorita se näin:

```bash
# Tee tiedostosta suoritettava (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Suorita sovellus
./07-dotnet-agent-framework.cs
```

Tai käytä komentoa dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Koodin toteutus

Täydellinen toteutus on saatavilla tiedostossa `07-dotnet-agent-framework.cs`, jossa näytetään:

- Ympäristöasetusten lataaminen DotNetEnv:llä
- Azure OpenAI -asiakkaan konfigurointi ja AI-agentin luominen `GetChatClient().AsAIAgent()` avulla
- Rakenteellisten tietomallien (Plan ja TravelPlan) määrittely JSON-serialisoinnilla
- AI-agentin luominen rakenteellisella tuotoksella JSON-skeemalla
- Suunnittelupyyntöjen suorittaminen tyyppiturvallisilla vastauksilla

## Keskeiset käsitteet

### Rakenteellinen suunnittelu tyyppiturvallisilla malleilla

Agentti käyttää C#-luokkia määrittämään suunnittelutuotosten rakenteen:

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

### JSON-skeema rakenteellisille tuotoksille

Agentti on konfiguroitu palauttamaan vastauksia, jotka vastaavat TravelPlan-skeemaa:

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

### Suunnitteluagentin ohjeet

Agentti toimii koordinaattorina ja delegoi tehtäviä erikoistuneille aliagenteille:

- FlightBooking: Lennon varaamiseen ja lentotietojen tarjoamiseen
- HotelBooking: Hotellien varaamiseen ja hotellitietojen tarjoamiseen
- CarRental: Auton vuokraamiseen ja autovuokratietojen tarjoamiseen
- ActivitiesBooking: Aktiviteettien varaamiseen ja aktiviteettitietojen tarjoamiseen
- DestinationInfo: Matkakohteiden tietojen tarjoamiseen
- DefaultAgent: Yleisten pyyntöjen käsittelyyn

## Odotettu tulos

Kun suoritat agentin matkasuunnittelupyynnöllä, se analysoi pyynnön ja luo rakenteellisen suunnitelman sopivilla tehtäväjaoilla erikoistuneille agenteille, muotoiltuna JSONiksi, joka noudattaa TravelPlan-skeemaa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->