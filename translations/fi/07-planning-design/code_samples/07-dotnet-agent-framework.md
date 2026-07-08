# 🎯 Suunnittelu ja suunnittelumallit Azure OpenAI:n (Responses API) kanssa (.NET)

## 📋 Oppimistavoitteet

Tämä muistikirja esittelee yritystason suunnittelu- ja suunnittelumallit älykkäiden agenttien rakentamiseksi Microsoft Agent Frameworkilla .NET:ssä Azure OpenAI:n (Responses API) avulla. Opit luomaan agentteja, jotka pystyvät purkamaan monimutkaisia ongelmia, suunnittelemaan monivaiheisia ratkaisuja ja suorittamaan kehittyneitä työnkulkuja .NET:n yritysominaisuuksilla.

## ⚙️ Vaatimukset ja asennus

**Kehitysympäristö:**
- .NET 9.0 SDK tai uudempi
- Visual Studio 2022 tai VS Code C#-laajennuksella
- Azure-tilaus, jossa on Azure OpenAI -resurssi ja mallin käyttöönotto
- Azure CLI — kirjaudu sisään komennolla `az login`

**Vaaditut riippuvuudet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Ympäristöasetukset (.env-tiedosto):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Koodin suorittaminen

Tämä opetus sisältää .NET-single file -sovelluksen toteutuksen. Suorita se näin:

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

Täydellinen toteutus on tiedostossa `07-dotnet-agent-framework.cs`, joka sisältää:

- Ympäristöasetusten lataamisen DotNetEnv:llä
- Azure OpenAI -asiakkaan konfiguroinnin Responses API:lle
- Rakenteellisten tietomallien (Plan ja TravelPlan) määrittelyn JSON-serialisoinnilla
- AI-agentin luomisen rakenteellisella ulostulolla JSON-skeemalla
- Suunnittelupyyntöjen suorittamisen tyyppiturvallisilla vastauksilla

## Keskeiset käsitteet

### Rakenteellinen suunnittelu tyyppiturvallisilla malleilla

Agentti käyttää C#-luokkia määrittämään suunnittelun tulosten rakenteen:

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

### JSON-skeema rakenteellisille vastauksille

Agentti on konfiguroitu palauttamaan vastauksia, jotka vastaavat TravelPlan-skeemaa:

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

### Suunnitteluagentin ohjeet

Agentti toimii koordinaattorina, ohjaten tehtäviä erikoistuneille ala-agenteille:

- FlightBooking: Lentojen varaukseen ja lentoihin liittyvän tiedon tarjoamiseen
- HotelBooking: Hotellien varaukseen ja hotellitietoihin
- CarRental: Autonvuokraukseen ja autonvuokraustietoihin
- ActivitiesBooking: Aktiviteettien varaukseen ja aktiviteettitietoihin
- DestinationInfo: Kohdetietojen tarjoamiseen
- DefaultAgent: Yleisten pyyntöjen käsittelyyn

## Odotettu tulos

Kun suoritat agentin matkasuunnittelupyynnöllä, se analysoi pyynnön ja luo rakenteellisen suunnitelman sopivin tehtäväjaoin erikoistuneille agenteille, muodossa JSON, joka noudattaa TravelPlan-skeemaa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->