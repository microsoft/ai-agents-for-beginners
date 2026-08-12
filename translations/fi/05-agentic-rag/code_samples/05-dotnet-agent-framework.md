# 🔍 Yritystason RAG Microsoft Foundryn (.NET) kanssa

## 📋 Oppimistavoitteet

Tämä muistio näyttää, kuinka rakentaa yritystason Retrieval-Augmented Generation (RAG) -järjestelmiä Microsoft Agent Frameworkilla .NET:ssä Microsoft Foundryn avulla. Opit luomaan tuotantovalmiita agenteja, jotka voivat hakea asiakirjoista ja tarjota tarkkoja, kontekstivitaita vastauksia yritystason turvallisuudella ja skaalautuvuudella.

**Rakennettavat yritystason RAG-ominaisuudet:**
- 📚 **Asiakirjaälykkyys**: Edistynyt asiakirjojen käsittely Azure AI -palveluilla
- 🔍 **Semanttinen haku**: Korkean suorituskyvyn vektorihaku yritysominaisuuksilla
- 🛡️ **Turvallisuuden integrointi**: Roolipohjainen pääsy ja tietosuojamallit
- 🏢 **Skaalautuva arkkitehtuuri**: Tuotantovalmiit RAG-järjestelmät valvonnalla

## 🎯 Yritystason RAG-arkkitehtuuri

### Keskeiset yrityskomponentit
- **Microsoft Foundry**: Hallittu yritystason tekoälyalusta turvallisuudella ja vaatimustenmukaisuudella
- **Persistenttiset agentit**: Tilallisia agenteja, joissa keskusteluhistoria ja kontekstinhallinta
- **Vektorivaraston hallinta**: Yritystason asiakirjojen indeksointi ja haku
- **Identiteetin integrointi**: Azure AD -todennus ja roolipohjainen käyttöoikeushallinta

### .NET:n yritysedut
- **Tyyppiturvallisuus**: Käännösaikainen validointi RAG-toiminnoille ja tietorakenteille
- **Asynkroninen suorituskyky**: Estämätön asiakirjojen käsittely ja hakutoiminnot
- **Muistinhallinta**: Tehokas resurssien käyttö suurissa asiakirjakokoelmissa
- **Integraatiomallit**: Natiivin Azure-palvelun integrointi riippuvuussisällöllä

## 🏗️ Tekninen arkkitehtuuri

### Yritystason RAG-putki
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Keskeiset .NET-komponentit
- **Azure.AI.Agents.Persistent**: Yritysagenttien hallinta tilan säilyttämisellä
- **Azure.Identity**: Integroitu todennus turvalliseen Azure-palveluiden käyttöön
- **Microsoft.Agents.AI.AzureAI**: Azureen optimoitu agenttikehyksen toteutus
- **System.Linq.Async**: Korkean suorituskyvyn asynkroniset LINQ-toiminnot

## 🔧 Yritysominaisuudet & hyödyt

### Turvallisuus & vaatimustenmukaisuus
- **Azure AD -integraatio**: Yrityksen identiteetin hallinta ja todennus
- **Roolipohjainen pääsy**: Tarkkarajaiset oikeudet asiakirjojen käyttöön ja toimintoihin
- **Tietosuoja**: Salaus levossa ja siirrossa arkaluonteisille asiakirjoille
- **Auditointilokit**: Kattava toiminnan seuranta vaatimustenmukaisuutta varten

### Suorituskyky & skaalautuvuus
- **Yhteyksien allokointi**: Tehokas Azure-palvelujen yhteyshallinta
- **Asynkroninen käsittely**: Estämättömät toiminnot suurten kuormitustilanteiden tarpeisiin
- **Välimuististrategiat**: Älykäs välimuistitus usein haetuille asiakirjoille
- **Kuormantasapainotus**: Hajautettu käsittely laajoissa käyttöönotossa

### Hallinta & valvonta
- **Terveystarkastukset**: Sisäänrakennettu valvonta RAG-järjestelmän komponenteille
- **Suoritusmittarit**: Yksityiskohtainen analytiikka haun laadusta ja vasteajoista
- **Virheiden hallinta**: Kattava poikkeusten käsittely uudelleenkäytäntöjen kanssa
- **Konfiguraation hallinta**: Ympäristökohtaiset asetukset validoinnilla

## ⚙️ Esivaatimukset & asennus

**Kehitysympäristö:**
- .NET 9.0 SDK tai uudempi
- Visual Studio 2022 tai VS Code C#-laajennuksella
- Azure-tilaus Microsoft Foundryn käytöllä

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
# Asenna Azure CLI ja varmista kirjautuminen
az login
az account set --subscription "your-subscription-id"
```

**Ympäristöasetukset:**
* Microsoft Foundryn asetukset (hoidetaan automaattisesti Azure CLI:n kautta)
* Varmista, että olet autentikoitunut oikeaan Azure-tilaukseen

## 📊 Yritystason RAG-mallit

### Asiakirjanhallintamallit
- **Massalataus**: Tehokas suurten asiakirjakokoelmien käsittely
- **Inkremementtiset päivitykset**: Reaaliaikainen asiakirjojen lisääminen ja muokkaus
- **Versionhallinta**: Asiakirjojen versiointi ja muutosten seuranta
- **Metatietojen hallinta**: Rikkaat asiakirjaominaisuudet ja taksonomia

### Haku- ja hakumallit
- **Hybridi-haku**: Semanttisen ja avainsanahaun yhdistäminen optimaalisiin tuloksiin
- **Facetoitu haku**: Moniulotteinen suodatus ja luokittelu
- **Relevanssin hienosäätö**: Mukautetut pisteytysalgoritmit toimialakohtaisiin tarpeisiin
- **Tulosten lajittelu**: Kehittynyt lajittelu liiketoimintalogiikan integroinnilla

### Turvallisuusmallit
- **Asiakirjatasoinen turvallisuus**: Tarkkarajainen pääsynhallinta per asiakirja
- **Tietoluokittelu**: Automaattinen arkaluonteisuusluokitus ja suojaus
- **Auditointiketjut**: Kattava lokitus kaikista RAG-toiminnoista
- **Tietosuojan suojaus**: Henkilötietojen tunnistus ja peittäminen

## 🔒 Yritystason turvaominaisuudet

### Todennus & valtuutus
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

### Tietosuoja
- **Salaus**: Päätepisteestä päähän salaaminen asiakirjoille ja hakemistoille
- **Pääsynvalvonta**: Integraatio Azure AD:n kanssa käyttäjien ja ryhmien oikeuksille
- **Tietojen sijainti**: Maantieteelliset tietojen sijaintiohjaukset vaatimustenmukaisuuteen
- **Varmuuskopiointi & palautus**: Automaattiset varmuuskopiointi- ja katastrofipalautusominaisuudet

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
- **Striimauskäsittely**: Suurten asiakirjojen käsittely ilman muistiongelmia
- **Resurssien allokointi**: Tehokas kalliiden resurssien uudelleenkäyttö
- **Roskanpoisto**: Optimoidut muistinhallintamallit
- **Yhteyshallinta**: Azure-palveluliittymien elinkaaren hallinta

### Välimuististrategiat
- **Kyselyvälimuisti**: Usein suoritettujen hakujen välimuistit
- **Asiakirjävlimuisti**: Muistissa pidettävä välimuisti kuumille asiakirjoille
- **Indeksivälimuisti**: Optimoitu vektori-indeksin välimuisti
- **Tulosten välimuisti**: Älykäs välimuistitus generoituja vastauksia varten

## 📊 Yrityskäyttötapaukset

### Tiedonhallinta
- **Yrityksen wiki**: Älykäs haku yrityksen tietopankeissa
- **Politiikat & menettelyt**: Automaattinen vaatimustenmukaisuus ja ohjeistus
- **Koulutusmateriaalit**: Älykäs oppimisen ja kehityksen tuki
- **Tutkimustietokannat**: Akateemisten ja tutkimuspapereiden analysointijärjestelmät

### Asiakastuki
- **Tukitietokanta**: Automaattiset asiakaspalveluvastaukset
- **Tuotedokumentaatio**: Älykäs tuotetietojen haku
- **Vianmääritysohjeet**: Kontekstuaalinen ongelmanratkaisuapu
- **Usein kysytyt kysymykset**: Dynaaminen FAQ:n luonti asiakirjakokoelmista

### Sääntelyn noudattaminen
- **Lakiasiakirja-analyysi**: Sopimus- ja lakiasiakirjaälykkyys
- **Vaatimustenmukaisuuden valvonta**: Automaattinen sääntelyn seuranta
- **Riskinarviointi**: Asiakirjaperusteinen riskianalyysi ja raportointi
- **Auditointituki**: Älykäs asiakirjojen etsintä auditointeja varten

## 🚀 Tuotantoon käyttöönotto

### Valvonta & havaittavuus
- **Application Insights**: Yksityiskohtainen telemetria ja suorituskyvyn valvonta
- **Mukautetut mittarit**: Liiketoimintakohtaisten KPI-mittareiden seuranta ja hälytykset
- **Jäljitettävyys**: Pyynnön jäljitys palveluiden välillä päästä päähän
- **Terveysnäkymät**: Järjestelmän reaaliaikainen terveystila ja suorituskyvyn visualisointi

### Skaalautuvuus & luotettavuus
- **Automaattinen skaalaus**: Kuorman ja suorituskykymittareiden pohjainen automaattinen laajentuminen
- **Korkea käytettävyys**: Monialueasennukset vikasietoisuudella
- **Kuormitustestaus**: Suorituskyvyn vahvistus yritystason kuormituksilla
- **Katastrofipalautus**: Automaattiset varmuuskopiointi- ja palautusmenettelyt

Valmiina rakentamaan yritystason RAG-järjestelmiä, jotka käsittelevät arkaluontoisia asiakirjoja suuressa mittakaavassa? Rakennetaan fiksuja tiedonhallintajärjestelmiä yrityksellesi! 🏢📖✨

## Koodin toteutus

Tämä oppitunti sisältää täydellisen toimivan koodiesimerkin tiedostossa `05-dotnet-agent-framework.cs`.

Esimerkin suorittamiseksi:

```bash
# Tee skriptistä suoritettava (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Suorita .NET-yksittäistiedostosovellus
./05-dotnet-agent-framework.cs
```

Tai käytä suoraan `dotnet run`:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Koodi näyttää:

1. **Paketin asennus**: Tarvittavien Azure AI Agents -NuGet-pakettien asentaminen
2. **Ympäristöasetukset**: Microsoft Foundryn päätepisteen ja malliasetusten lataaminen
3. **Asiakirjan lataus**: Asiakirjan lataaminen RAG-käsittelyä varten
4. **Vektorivaraston luonti**: Vektorivaraston luominen semanttista hakua varten
5. **Agentin konfigurointi**: AI-agentin määrittäminen tiedostohakuominaisuuksilla
6. **Kyselyjen suoritukset**: Kyselyjen ajaminen ladattua asiakirjaa vasten

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->