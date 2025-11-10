<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:48:43+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "fi"
}
-->
# 🎨 Agenttiset suunnittelumallit GitHub-mallien kanssa (.NET)

## 📋 Oppimistavoitteet

Tämä muistikirja esittelee yritystason suunnittelumalleja älykkäiden agenttien rakentamiseen Microsoft Agent Frameworkin avulla .NET-ympäristössä, integroituna GitHub-malleihin. Opit ammattimaisia malleja ja arkkitehtuurilähestymistapoja, jotka tekevät agenteista tuotantovalmiita, ylläpidettäviä ja skaalautuvia.

**Yritystason suunnittelumallit:**
- 🏭 **Tehdasmalli**: Vakioitu agenttien luonti riippuvuuksien injektoinnilla
- 🔧 **Rakentajamalli**: Sujuva agenttien konfigurointi ja asennus
- 🧵 **Lankaturvalliset mallit**: Samanaikainen keskustelunhallinta
- 📋 **Repositoriomalli**: Järjestelmällinen työkalujen ja kyvykkyyksien hallinta

## 🎯 .NET-spesifiset arkkitehtuuriedut

### Yritysominaisuudet
- **Vahva tyypitys**: Kääntöaikainen validointi ja IntelliSense-tuki
- **Riippuvuuksien injektointi**: Sisäänrakennettu DI-kontainerin integrointi
- **Konfiguraation hallinta**: IConfiguration- ja Options-mallit
- **Async/Await**: Ensiluokkainen asynkroninen ohjelmointituki

### Tuotantovalmiit mallit
- **Lokitusintegraatio**: ILogger ja rakenteellinen lokitustuki
- **Terveystarkastukset**: Sisäänrakennettu seuranta ja diagnostiikka
- **Konfiguraation validointi**: Vahva tyypitys ja dataannotaatiot
- **Virheenkäsittely**: Rakenteellinen poikkeusten hallinta

## 🔧 Tekninen arkkitehtuuri

### Keskeiset .NET-komponentit
- **Microsoft.Extensions.AI**: Yhtenäiset AI-palvelujen abstraktiot
- **Microsoft.Agents.AI**: Yritystason agenttien orkestrointikehys
- **GitHub-mallien integrointi**: Suorituskykyiset API-asiakasmallit
- **Konfiguraatiojärjestelmä**: appsettings.json ja ympäristöintegraatio

### Suunnittelumallien toteutus
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Esitellyt yritystason mallit

### 1. **Luontimallit**
- **Agenttitehdas**: Keskitetty agenttien luonti johdonmukaisella konfiguraatiolla
- **Rakentajamalli**: Sujuva API monimutkaiseen agenttien konfigurointiin
- **Singleton-malli**: Jaetut resurssit ja konfiguraation hallinta
- **Riippuvuuksien injektointi**: Löyhä kytkentä ja testattavuus

### 2. **Käyttäytymismallit**
- **Strategiamalli**: Vaihdettavat työkalujen suoritusstrategiat
- **Komento-malli**: Kapseloidut agenttitoiminnot undo/redo-toiminnoilla
- **Havainnoijamalli**: Tapahtumapohjainen agentin elinkaaren hallinta
- **Template Method**: Vakioidut agenttien suoritusprosessit

### 3. **Rakennemallit**
- **Adapterimalli**: GitHub-mallien API-integraatiokerros
- **Dekoraattorimalli**: Agenttien kyvykkyyksien parantaminen
- **Fasadi-malli**: Yksinkertaistetut agenttien vuorovaikutusrajapinnat
- **Proxymalli**: Viivästetty lataus ja välimuisti suorituskyvyn parantamiseksi

## ⚙️ Esivaatimukset ja asennus

**Kehitysympäristö:**
- .NET 9.0 SDK tai uudempi
- Visual Studio 2022 tai VS Code C#-laajennuksella
- GitHub-mallien API-käyttöoikeus

**NuGet-riippuvuudet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguraatio (.env-tiedosto):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 .NET-suunnitteluperiaatteet

### SOLID-periaatteet
- **Yhden vastuun periaate**: Jokaisella komponentilla on yksi selkeä tarkoitus
- **Avoin/Suljettu**: Laajennettavissa ilman muutoksia
- **Liskovin korvausperiaate**: Rajapintapohjaiset työkalutoteutukset
- **Rajapinnan erottelu**: Keskittyneet, yhtenäiset rajapinnat
- **Riippuvuuksien inversio**: Riippuvuus abstraktioista, ei konkreettisista toteutuksista

### Puhdas arkkitehtuuri
- **Domain-kerros**: Keskeiset agentti- ja työkaluabstraktiot
- **Sovelluskerros**: Agenttien orkestrointi ja työnkulut
- **Infrastruktuurikerros**: GitHub-mallien integrointi ja ulkoiset palvelut
- **Esityskerros**: Käyttäjävuorovaikutus ja vastausten muotoilu

## 🔒 Yritystason näkökohdat

### Turvallisuus
- **Tunnusten hallinta**: API-avainten turvallinen käsittely IConfigurationin avulla
- **Syötteen validointi**: Vahva tyypitys ja dataannotaatioiden validointi
- **Tulosten puhdistus**: Vastausten turvallinen käsittely ja suodatus
- **Auditointilokitus**: Kattava toimintojen seuranta

### Suorituskyky
- **Async-mallit**: Ei-blokkaavat I/O-toiminnot
- **Yhteyspoolaus**: Tehokas HTTP-asiakashallinta
- **Välimuisti**: Vastausten välimuisti suorituskyvyn parantamiseksi
- **Resurssien hallinta**: Asianmukaiset hävitys- ja siivousmallit

### Skaalautuvuus
- **Lankaturvallisuus**: Samanaikainen agenttien suorituskyky
- **Resurssipoolaus**: Tehokas resurssien hyödyntäminen
- **Kuormanhallinta**: Nopeusrajoitukset ja vastapaineen käsittely
- **Seuranta**: Suorituskykymittarit ja terveystarkastukset

## 🚀 Tuotantokäyttöön ottaminen

- **Konfiguraation hallinta**: Ympäristökohtaiset asetukset
- **Lokitusstrategia**: Rakenteellinen lokitus korrelaatio-ID:illä
- **Virheenkäsittely**: Globaalit poikkeusten käsittelyt asianmukaisella palautumisella
- **Seuranta**: Application Insights ja suorituskykylaskurit
- **Testaus**: Yksikkötestit, integraatiotestit ja kuormitustestauksen mallit

Valmiina rakentamaan yritystason älykkäitä agentteja .NET-ympäristössä? Suunnitellaan jotain vankkaa! 🏢✨

## Koodiesimerkki

Täydellisen toimivan esimerkin löydät tiedostosta [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi katsoa ensisijaiseksi lähteeksi. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.