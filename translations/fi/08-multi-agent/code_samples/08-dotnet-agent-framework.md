<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:17:05+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "fi"
}
-->
# 🤝 Yritystason monen agentin työnkulkujärjestelmät (.NET)

## 📋 Oppimistavoitteet

Tämä muistikirja opastaa, kuinka rakentaa kehittyneitä yritystason monen agentin järjestelmiä Microsoft Agent Frameworkin avulla .NET-ympäristössä ja GitHub-mallien kanssa. Opit orkestroimaan useita erikoistuneita agentteja, jotka työskentelevät yhdessä jäsenneltyjen työnkulkujen kautta, hyödyntäen .NET:n yritysominaisuuksia tuotantovalmiiden ratkaisujen luomiseksi.

**Rakennettavat yritystason monen agentin ominaisuudet:**
- 👥 **Agenttien yhteistyö**: Tyypinmukainen agenttien koordinointi kääntöaikaisella validoinnilla
- 🔄 **Työnkulun orkestrointi**: Deklaratiivinen työnkulun määrittely .NET:n asynkronisten mallien avulla
- 🎭 **Roolien erikoistuminen**: Vahvasti tyypitetyt agenttien persoonallisuudet ja asiantuntija-alueet
- 🏢 **Yritysintegraatio**: Tuotantovalmiit mallit, joissa on valvonta ja virheenkäsittely

## ⚙️ Esivaatimukset ja asennus

**Kehitysympäristö:**
- .NET 9.0 SDK tai uudempi
- Visual Studio 2022 tai VS Code C#-laajennuksella
- Azure-tilaus (pysyviä agentteja varten)

**Vaaditut NuGet-paketit:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Koodiesimerkki

Tämän oppitunnin täydellinen toimiva koodi löytyy mukana olevasta C#-tiedostosta: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Koodin suorittaminen:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Tai käyttämällä .NET CLI:tä:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Mitä tämä esimerkki havainnollistaa

Tämä monen agentin työnkulkujärjestelmä luo hotellimatkasuosituspalvelun, jossa on kaksi erikoistunutta agenttia:

1. **Vastaanottoagentti**: Matka-agentti, joka tarjoaa aktiviteetti- ja sijaintisuosituksia
2. **Concierge-agentti**: Tarkistaa suositukset varmistaakseen autenttiset, ei-turistimaiset kokemukset

Agentit työskentelevät yhdessä työnkulussa, jossa:
- Vastaanottoagentti vastaanottaa alkuperäisen matkapyynnön
- Concierge-agentti tarkistaa ja parantaa suositusta
- Työnkulku välittää vastaukset reaaliajassa

## Keskeiset käsitteet

### Agenttien koordinointi
Esimerkki havainnollistaa tyypinmukaista agenttien koordinointia Microsoft Agent Frameworkin avulla kääntöaikaisella validoinnilla.

### Työnkulun orkestrointi
Käyttää deklaratiivista työnkulun määrittelyä .NET:n asynkronisten mallien avulla yhdistääkseen useita agentteja putkistoon.

### Vastausten suoratoisto
Toteuttaa agenttien vastausten reaaliaikaisen suoratoiston asynkronisten luetteloiden ja tapahtumapohjaisen arkkitehtuurin avulla.

### Yritysintegraatio
Esittelee tuotantovalmiita malleja, jotka sisältävät:
- Ympäristömuuttujien konfiguroinnin
- Turvallisen tunnistetietojen hallinnan
- Virheenkäsittelyn
- Asynkronisen tapahtumien käsittelyn

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.