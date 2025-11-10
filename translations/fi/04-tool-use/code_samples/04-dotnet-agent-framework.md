<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:25:54+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "fi"
}
-->
# 🛠️ Edistynyt työkalujen käyttö GitHub-mallien kanssa (.NET)

## 📋 Oppimistavoitteet

Tämä muistikirja esittelee yritystason työkalujen integrointimalleja Microsoft Agent Frameworkin avulla .NET-ympäristössä ja GitHub-mallien kanssa. Opit rakentamaan kehittyneitä agentteja, joissa on useita erikoistuneita työkaluja, hyödyntäen C#:n vahvaa tyypitystä ja .NET:n yritysominaisuuksia.

**Edistyneet työkalukyvyt, jotka hallitset:**
- 🔧 **Monityökaluarkkitehtuuri**: Agenttien rakentaminen useilla erikoistuneilla ominaisuuksilla
- 🎯 **Tyypin turvallinen työkalujen suoritus**: C#:n kääntöaikainen validointi
- 📊 **Yritystason työkalumallit**: Tuotantovalmiiden työkalujen suunnittelu ja virheenkäsittely
- 🔗 **Työkalujen yhdistäminen**: Työkalujen yhdistäminen monimutkaisiin liiketoimintatyönkulkuihin

## 🎯 .NET-työkaluarkkitehtuurin edut

### Yritystason työkalujen ominaisuudet
- **Kääntöaikainen validointi**: Vahva tyypitys varmistaa työkalujen parametrien oikeellisuuden
- **Riippuvuuksien injektio**: IoC-kontainerin integrointi työkalujen hallintaan
- **Async/Await-mallit**: Ei-blokkaava työkalujen suoritus ja resurssien hallinta
- **Rakenteellinen lokitus**: Sisäänrakennettu lokitus työkalujen suoritusvalvontaan

### Tuotantovalmiit mallit
- **Poikkeusten käsittely**: Kattava virheiden hallinta tyypitettyjen poikkeusten avulla
- **Resurssien hallinta**: Oikeat hävitysmallit ja muistinhallinta
- **Suorituskyvyn seuranta**: Sisäänrakennetut mittarit ja suorituskykylaskurit
- **Konfiguraation hallinta**: Tyypin turvallinen konfiguraatio ja validointi

## 🔧 Tekninen arkkitehtuuri

### Keskeiset .NET-työkalukomponentit
- **Microsoft.Extensions.AI**: Yhtenäinen työkalujen abstraktiokerros
- **Microsoft.Agents.AI**: Yritystason työkalujen orkestrointi
- **GitHub-mallien integrointi**: Suorituskykyinen API-asiakas yhteyspoolauksella

### Työkalujen suoritusputki
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Työkalukategoriat ja mallit

### 1. **Datankäsittelytyökalut**
- **Syötteen validointi**: Vahva tyypitys ja data-annotaatiot
- **Muunnostoiminnot**: Tyypin turvallinen datan muuntaminen ja muotoilu
- **Liiketoimintalogiikka**: Alakohtaiset laskenta- ja analyysityökalut
- **Tulosten muotoilu**: Rakenteellinen vastausten generointi

### 2. **Integraatiotyökalut**
- **API-liittimet**: RESTful-palveluiden integrointi HttpClientin avulla
- **Tietokantatyökalut**: Entity Framework -integraatio datan käsittelyyn
- **Tiedosto-operaatiot**: Turvalliset tiedostojärjestelmäoperaatiot validoinnilla
- **Ulkoiset palvelut**: Kolmannen osapuolen palveluiden integrointimallit

### 3. **Apuvälineet**
- **Tekstinkäsittely**: Merkkijonojen muokkaus- ja muotoilutyökalut
- **Päivämäärä/aika-operaatiot**: Kulttuuritietoiset päivämäärä/aikalaskelmat
- **Matemaattiset työkalut**: Tarkat laskelmat ja tilastolliset operaatiot
- **Validointityökalut**: Liiketoimintasääntöjen validointi ja datan tarkistus

## ⚙️ Esivaatimukset ja asennus

**Kehitysympäristö:**
- .NET 9.0 SDK tai uudempi
- Visual Studio 2022 tai VS Code C#-laajennuksella
- GitHub-mallien API-pääsy

**Vaaditut NuGet-paketit:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Ympäristökonfiguraatio (.env-tiedosto):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Valmis rakentamaan yritystason agentteja tehokkailla, tyypin turvallisilla työkaluominaisuuksilla .NET-ympäristössä? Suunnitellaan ammattimaisia ratkaisuja! 🏢⚡

## 💻 Koodin toteutus

Täydellinen C#-toteutus löytyy mukana tulevasta tiedostosta `04-dotnet-agent-framework.cs`. Tämä .NET Single File App -sovellus demonstroi:

- Ympäristömuuttujien lataamisen GitHub-mallien konfiguraatiota varten
- Mukautettujen työkalujen määrittelyn C#-metodeilla ja attribuuteilla
- AI-agentin luomisen työkalujen integroinnilla
- Keskusteluketjujen hallinnan
- Agenttipyyntöjen suorittamisen työkalujen kutsumisella

Esimerkin suorittaminen:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Tai käyttämällä .NET CLI:tä:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.