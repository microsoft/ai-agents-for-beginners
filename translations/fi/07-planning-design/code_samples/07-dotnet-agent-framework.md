<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:57:58+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "fi"
}
-->
# 🎯 Suunnittelu ja suunnittelumallit GitHub-mallien kanssa (.NET)

## 📋 Oppimistavoitteet

Tämä muistikirja esittelee yritystason suunnittelu- ja suunnittelumalleja älykkäiden agenttien rakentamiseen Microsoft Agent Frameworkin avulla .NET:ssä GitHub-mallien kanssa. Opit luomaan agentteja, jotka voivat purkaa monimutkaisia ongelmia, suunnitella monivaiheisia ratkaisuja ja toteuttaa kehittyneitä työnkulkuja .NET:n yritysominaisuuksilla.

## ⚙️ Esivaatimukset ja asennus

**Kehitysympäristö:**
- .NET 9.0 SDK tai uudempi
- Visual Studio 2022 tai VS Code C#-laajennuksella
- GitHub Models API -pääsy

**Vaaditut riippuvuudet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Ympäristön konfigurointi (.env-tiedosto):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Koodin suorittaminen

Tämä oppitunti sisältää .NET Single File App -toteutuksen. Suorita se seuraavasti:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Tai käytä dotnet run -komentoa:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Koodin toteutus

Täydellinen toteutus löytyy tiedostosta `07-dotnet-agent-framework.cs`, joka esittelee:

- Ympäristön konfiguroinnin lataamisen DotNetEnv:n avulla
- OpenAI-asiakkaan konfiguroinnin GitHub-malleille
- Rakenteellisten tietomallien (Plan ja TravelPlan) määrittelyn JSON-sarjallistuksella
- AI-agentin luomisen rakenteellisella ulostulolla JSON-skeeman avulla
- Suunnittelupyyntöjen suorittamisen tyyppiturvallisilla vastauksilla

## Keskeiset käsitteet

### Rakenteellinen suunnittelu tyyppiturvallisilla malleilla

Agentti käyttää C#-luokkia määrittääkseen suunnittelun ulostulon rakenteen:

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

### JSON-skeema rakenteellisille ulostuloille

Agentti on konfiguroitu palauttamaan vastaukset, jotka vastaavat TravelPlan-skeemaa:

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

Agentti toimii koordinaattorina, delegoiden tehtäviä erikoistuneille alihankkija-agenteille:

- FlightBooking: Lentojen varaamiseen ja lentotietojen tarjoamiseen
- HotelBooking: Hotellien varaamiseen ja hotellitietojen tarjoamiseen
- CarRental: Autojen varaamiseen ja autonvuokraustietojen tarjoamiseen
- ActivitiesBooking: Aktiviteettien varaamiseen ja aktiviteettitietojen tarjoamiseen
- DestinationInfo: Kohdetietojen tarjoamiseen
- DefaultAgent: Yleisten pyyntöjen käsittelyyn

## Odotettu ulostulo

Kun suoritat agentin matkasuunnittelupyynnöllä, se analysoi pyynnön ja tuottaa rakenteellisen suunnitelman, jossa tehtävät jaetaan sopiville erikoistuneille agenteille. Ulostulo on muotoiltu JSON-muotoon, joka vastaa TravelPlan-skeemaa.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.