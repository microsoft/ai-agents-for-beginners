# 🔍 Enterprise RAG Microsoft Foundryn (.NET) kanssa

## 📋 Oppimistavoitteet

Tämä muistikirja osoittaa, kuinka rakentaa yritysluokan Retrieval-Augmented Generation (RAG) -järjestelmiä käyttämällä Microsoft Agent Frameworkia .NET:ssä Microsoft Foundryn kanssa. Opit luomaan tuotantovalmiita agenteja, jotka voivat hakea asiakirjoja ja tarjota tarkkoja, kontekstintajuisia vastauksia yritysturvallisuudella ja -skaalautuvuudella.

**Yritysluokan RAG-ominaisuudet, jotka rakennat:**
- 📚 **Asiakirjaälykkyys**: Kehittynyt asiakirjojen käsittely Azure AI -palveluilla
- 🔍 **Semanttinen haku**: Korkean suorituskyvyn vektorihaku yritysominaisuuksilla
- 🛡️ **Turvaintegraatio**: Roolipohjainen pääsy ja datan suojausmallit
- 🏢 **Skaalautuva arkkitehtuuri**: Tuotantovalmiit RAG-järjestelmät valvonnalla

## 🎯 Yritysluokan RAG-arkkitehtuuri

### Keskeiset yrityskomponentit
- **Microsoft Foundry**: Hallittu yritys-AI-alusta turvallisuudella ja vaatimustenmukaisuudella
- **Pysyvät agentit**: Tilalliset agentit keskusteluhistorialla ja kontekstinhallinnalla
- **Vektorivaraston hallinta**: Yritysluokan asiakirjojen indeksointi ja haku
- **Identiteetin integrointi**: Azure AD:n todennus ja roolipohjainen pääsynhallinta

### .NET-yritysedut
- **Tyyppiturvallisuus**: Käännösaikainen validointi RAG-toiminnoille ja tietorakenteille
- **Asynkroninen suorituskyky**: Estämätön asiakirjojen käsittely ja hakutoiminnot
- **Muistinhallinta**: Tehokas resurssien käyttö suurissa asiakirjakokoelmissa
- **Integroidut mallit**: Natiivin Azure-palvelun integrointi riippuvuussyötöllä

## 🏗️ Tekninen arkkitehtuuri

### Yritysluokan RAG-putki
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Keskeiset .NET-komponentit
- **Azure.AI.Agents.Persistent**: Yritysagenttien hallinta tilapysyvyyden kanssa
- **Azure.Identity**: Integroitu todennus turvalliseen Azure-palvelujen käyttöön
- **Microsoft.Agents.AI.AzureAI**: Azuren optimoitu agenttikehysimplementaatio
- **System.Linq.Async**: Korkean suorituskyvyn asynkroniset LINQ-toiminnot

## 🔧 Yritysominaisuudet ja edut

### Turvallisuus ja vaatimustenmukaisuus
- **Azure AD -integraatio**: Yrityksen identiteetin hallinta ja todennus
- **Roolipohjainen pääsy**: Tarkat käyttöoikeudet asiakirjojen käyttöön ja toimintoihin
- **Datan suojaus**: Salaus levossa ja siirrossa arkaluontoisille asiakirjoille
- **Auditointilokit**: Laaja toiminnan seuranta vaatimustenmukaisuuden takaamiseksi

### Suorituskyky ja skaalautuvuus
- **Yhteyspoolin hallinta**: Tehokas Azure-palveluyhteyksien hallinta
- **Asynkroninen käsittely**: Estämättömät toiminnot suurikuormitustilanteissa
- **Välimuististrategiat**: Älykäs välimuistitus usein haetuille asiakirjoille
- **Kuormantasapainotus**: Hajautettu käsittely suurissa käyttöönotossa

### Hallinta ja valvonta
- **Kunnon tarkistukset**: Sisäänrakennettu valvonta RAG-järjestelmän komponenteille
- **Suorituskykymittarit**: Yksityiskohtaiset analyysit haun laadusta ja vasteajoista
- **Virheenkäsittely**: Laaja poikkeusten hallinta uudelleenyrittämiskäytännöillä
- **Konfiguraation hallinta**: Ympäristökohtaiset asetukset validoinnilla

## ⚙️ Esivaatimukset ja asennus

**Kehitysympäristö:**
- .NET 9.0 SDK tai uudempi
- Visual Studio 2022 tai VS Code C#-laajennuksella
- Azure-tilaus Microsoft Foundryn käyttöoikeudella

**Vaaditut NuGet-paketit:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure-todennuksen asennus:**
```bash
# Asenna Azure CLI ja todenna käyttäjä
az login
az account set --subscription "your-subscription-id"
```

**Ympäristön konfigurointi:**
* Microsoft Foundryn konfigurointi (hoidetaan automaattisesti Azure CLI:n kautta)
* Varmista, että olet kirjautunut oikeaan Azure-tilaukseen

## 📊 Yritysluokan RAG-mallit

### Asiakirjahallinnan mallit
- **Massalähetys**: Tehokas suurten asiakirjakokoelmien käsittely
- **Inkrementaaliset päivitykset**: Reaaliaikainen asiakirjojen lisääminen ja muokkaus
- **Versionhallinta**: Asiakirjojen versiointi ja muutosten seuranta
- **Metatietojen hallinta**: Rikkaat asiakirjaominaisuudet ja taksonomia

### Haku- ja palautusmallit
- **Hybridi-haku**: Semanttisen ja hakusana-haun yhdistäminen parhaan tuloksen saamiseksi
- **Moniulotteinen haku**: Monidimensioinen suodatus ja luokittelu
- **Merkityksen hienosäätö**: Räätälöidyt pisteytysalgoritmit alakohtaisiin tarpeisiin
- **Tulosten lajittelu**: Kehittynyt lajittelu liiketoimintalogiikan integraatiolla

### Turvamallit
- **Asiakirjatasoinen turvallisuus**: Tarkka pääsynhallinta asiakirjakohtaisesti
- **Datan luokittelu**: Automaattinen herkkyystason merkitseminen ja suojaus
- **Auditointijäljet**: Laaja lokitus kaikista RAG-toiminnoista
- **Yksityisyyden suojaus**: Henkilötietojen tunnistus ja poistamiskyvyt

## 🔒 Yritysturvallisuusominaisuudet

### Todennus ja valtuutus
```csharp
// Azure AD integrated authentication
var credential = new AzureCliCredential();
var agentsClient = new PersistentAgentsClient(endpoint, credential);

// Role-based access validation
if (!await ValidateUserPermissions(user, documentId))
{
    throw new UnauthorizedAccessException("Insufficient permissions");
}
```

### Datan suojaus
- **Salaus**: Päätä päähän -salauksen asiakirjoille ja hakemistoille
- **Pääsynhallinta**: Integrointi Azure AD:n kanssa käyttäjä- ja ryhmäkohtaisille oikeuksille
- **Datakeskuksen sijainti**: Maantieteelliset datapaikannussäädökset vaatimusten täyttämiseksi
- **Varmuuskopiointi ja palautus**: Automaattiset varmuuskopiointi- ja katastrofipalautusominaisuudet

## 📈 Suorituskyvyn optimointi

### Asynkroniset käsittelymallit
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Muistinhallinta
- **Suoratoistokäsittely**: Käsittele suuria asiakirjoja ilman muistiin liittyviä ongelmia
- **Resurssien poolaus**: Tehokas kalliiden resurssien uudelleenkäyttö
- **Roskapostin keruu**: Optimoidut muistinhallintamallit
- **Yhteyksien hallinta**: Azure-palveluyhteyksien elinkaaren oikea hallinta

### Välimuististrategiat
- **Hakuvälimuisti**: Välimuisti usein suoritettaville hauille
- **Asiakirjojen välimuisti**: Muistivälimuisti kuumille asiakirjoille
- **Indeksin välimuisti**: Optimoitu vektori-indeksin välimuisti
- **Tulosten välimuisti**: Älykäs generoitujen vastausten välimuisti

## 📊 Yrityskäyttötapaukset

### Tiedonhallinta
- **Yrityksen Wiki**: Älykäs haku yrityksen tietokannoissa
- **Politiikka ja menettelyt**: Automaattinen vaatimustenmukaisuus ja ohjeistus
- **Koulutusmateriaalit**: Älykäs oppimisen ja kehityksen tuki
- **Tutkimustietokannat**: Akateemisten ja tutkimuspapereiden analyysijärjestelmät

### Asiakastuki
- **Tukitietokanta**: Automaattiset asiakaspalveluvastaukset
- **Tuotedokumentaatio**: Älykäs tuotetiedon hakeminen
- **Vianmääritysohjeet**: Kontekstuaalinen ongelmanratkaisuapu
- **UKK-järjestelmät**: Dynaaminen UKK:n generointi asiakirjakokoelmista

### Sääntelyn noudattaminen
- **Laillisten asiakirjojen analyysi**: Sopimus- ja oikeudellinen asiakirjaälykkyys
- **Vaatimustenmukaisuuden seuranta**: Automaattinen sääntelyvaatimusten tarkastus
- **Riskinarviointi**: Asiakirjoihin perustuva riskiarvio ja raportointi
- **Auditointituki**: Älykäs asiakirjojen löytäminen auditointeja varten

## 🚀 Tuotantokäyttöönotto

### Valvonta ja havainnointi
- **Application Insights**: Yksityiskohtainen telemetria ja suorituskyvyn valvonta
- **Mukautetut mittarit**: Liiketoimintaspecifisten KPI:en seuranta ja hälytys
- **Hajautettu jäljitys**: Pyyntöjen kokonaisvaltainen seuranta palveluissa
- **Kunnon hallintapaneelit**: Reaaliaikainen järjestelmän terveyden ja suorituskyvyn visualisointi

### Skaalautuvuus ja luotettavuus
- **Automaattinen skaalaus**: Kuorman ja suorituskykymittareiden mukainen automaattinen skaalaus
- **Korkea käytettävyys**: Monialueellinen käyttöönotto vikatilanteiden varalta
- **Kuormitustestaus**: Suorituskyvyn validointi yrityskuormitustilanteissa
- **Katastrofipalautus**: Automaattiset varmuuskopiointi- ja palautusprosessit

Valmiina rakentamaan yritysluokan RAG-järjestelmiä, jotka pystyvät käsittelemään arkaluonteisia asiakirjoja suuressa mittakaavassa? Rakennetaan yhdessä älykkäitä tietojärjestelmiä yrityksille! 🏢📖✨

## Koodin toteutus

Tämän oppitunnin täydellinen toimiva koodiesimerkki löytyy tiedostosta `05-dotnet-agent-framework.cs`. 

Suorittaaksesi esimerkin:

```bash
# Tee skriptistä suoritettava (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Suorita .NET-yksittäistiedostosovellus
./05-dotnet-agent-framework.cs
```

Tai käytä suoraan `dotnet run` -komentoa:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Koodi demonstroi:

1. **Paketin asennus**: Tarvittavien NuGet-pakettien asennus Azure AI Agentsia varten
2. **Ympäristön konfigurointi**: Microsoft Foundryn päätepisteen ja malliasetusten lataaminen
3. **Asiakirjan lähetys**: Asiakirjan lataaminen RAG-käsittelyä varten
4. **Vektorivaraston luonti**: Vektorivaraston luominen semanttista hakua varten
5. **Agentin konfigurointi**: AI-agentin määrittely tiedostohakuominaisuuksilla
6. **Kyselyjen suoritus**: Kyselyiden ajaminen ladattua asiakirjaa vastaan

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->