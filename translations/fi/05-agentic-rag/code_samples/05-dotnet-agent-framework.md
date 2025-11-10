<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:04:52+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "fi"
}
-->
# 🔍 Enterprise RAG Azure AI Foundrylla (.NET)

## 📋 Oppimistavoitteet

Tämä notebook näyttää, kuinka rakentaa yritystason Retrieval-Augmented Generation (RAG) -järjestelmiä Microsoft Agent Frameworkin avulla .NET:ssä ja Azure AI Foundryssa. Opit luomaan tuotantovalmiita agentteja, jotka voivat etsiä dokumenteista ja tarjota tarkkoja, kontekstitietoisia vastauksia yritystason turvallisuudella ja skaalautuvuudella.

**Rakennettavat yritystason RAG-ominaisuudet:**
- 📚 **Dokumenttien älykkyys**: Kehittynyt dokumenttien käsittely Azure AI -palveluilla
- 🔍 **Semanttinen haku**: Suorituskykyinen vektorihaku yritysominaisuuksilla
- 🛡️ **Turvallisuusintegraatio**: Roolipohjainen pääsy ja tietosuojamallit
- 🏢 **Skaalautuva arkkitehtuuri**: Tuotantovalmiit RAG-järjestelmät valvonnalla

## 🎯 Yritystason RAG-arkkitehtuuri

### Keskeiset yrityskomponentit
- **Azure AI Foundry**: Hallinnoitu yritys-AI-alusta turvallisuudella ja vaatimustenmukaisuudella
- **Pysyvät agentit**: Tilalliset agentit keskusteluhistorialla ja kontekstinhallinnalla
- **Vektorivaraston hallinta**: Yritystason dokumenttien indeksointi ja haku
- **Identiteetti-integraatio**: Azure AD -autentikointi ja roolipohjainen pääsynhallinta

### .NET-yrityshyödyt
- **Tyyppiturvallisuus**: Kääntöaikainen validointi RAG-toiminnoille ja tietorakenteille
- **Asynkroninen suorituskyky**: Ei-blokkaava dokumenttien käsittely ja hakutoiminnot
- **Muistinhallinta**: Tehokas resurssien käyttö suurille dokumenttikokoelmille
- **Integraatiomallit**: Natiivien Azure-palveluiden integrointi riippuvuuksien injektiolla

## 🏗️ Tekninen arkkitehtuuri

### Yritystason RAG-putki
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Keskeiset .NET-komponentit
- **Azure.AI.Agents.Persistent**: Yritysagenttien hallinta tilan pysyvyydellä
- **Azure.Identity**: Integroitu autentikointi turvalliseen Azure-palveluiden käyttöön
- **Microsoft.Agents.AI.AzureAI**: Azure-optimoitu agenttikehys
- **System.Linq.Async**: Suorituskykyiset asynkroniset LINQ-toiminnot

## 🔧 Yritysominaisuudet ja -hyödyt

### Turvallisuus ja vaatimustenmukaisuus
- **Azure AD -integraatio**: Yrityksen identiteetinhallinta ja autentikointi
- **Roolipohjainen pääsy**: Tarkat käyttöoikeudet dokumenttien käyttöön ja toimintoihin
- **Tietosuoja**: Salaus levossa ja siirrossa arkaluontoisille dokumenteille
- **Auditointilokit**: Kattava toiminnan seuranta vaatimustenmukaisuuden varmistamiseksi

### Suorituskyky ja skaalautuvuus
- **Yhteyspoolaus**: Tehokas Azure-palveluiden yhteyksien hallinta
- **Asynkroninen käsittely**: Ei-blokkaavat toiminnot korkean läpimenon skenaarioihin
- **Välimuististrategiat**: Älykäs välimuisti usein käytetyille dokumenteille
- **Kuormantasapainotus**: Hajautettu käsittely suurten järjestelmien käyttöönottoon

### Hallinta ja valvonta
- **Terveystarkistukset**: Sisäänrakennettu valvonta RAG-järjestelmän komponenteille
- **Suorituskykymittarit**: Yksityiskohtainen analytiikka hakujen laadusta ja vasteajoista
- **Virheenkäsittely**: Kattava poikkeusten hallinta ja uudelleenyrittämiskäytännöt
- **Konfiguraation hallinta**: Ympäristökohtaiset asetukset validoinnilla

## ⚙️ Esivaatimukset ja asennus

**Kehitysympäristö:**
- .NET 9.0 SDK tai uudempi
- Visual Studio 2022 tai VS Code C#-laajennuksella
- Azure-tilaus AI Foundry -pääsyllä

**Vaaditut NuGet-paketit:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure-autentikoinnin asennus:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Ympäristön konfiguraatio:**
* Azure AI Foundry -konfiguraatio (automaattisesti Azure CLI:n kautta)
* Varmista, että olet autentikoitunut oikeaan Azure-tilaukseen

## 📊 Yritystason RAG-mallit

### Dokumenttien hallintamallit
- **Massalataus**: Tehokas suurten dokumenttikokoelmien käsittely
- **Inkrementaaliset päivitykset**: Reaaliaikainen dokumenttien lisäys ja muokkaus
- **Versiohallinta**: Dokumenttien versiointi ja muutosten seuranta
- **Metatietojen hallinta**: Rikkaat dokumenttiattribuutit ja taksonomia

### Haku- ja hakumallit
- **Hybridihaku**: Semanttisen ja avainsanahaun yhdistäminen optimaalisiin tuloksiin
- **Fasettihaku**: Moniulotteinen suodatus ja kategorisointi
- **Relevanssin säätö**: Mukautetut pisteytysalgoritmit alakohtaisiin tarpeisiin
- **Tulosten järjestäminen**: Kehittynyt järjestäminen liiketoimintalogiikan integroinnilla

### Turvallisuusmallit
- **Dokumenttikohtainen turvallisuus**: Tarkka käyttöoikeuksien hallinta dokumenttikohtaisesti
- **Tietoluokittelu**: Automaattinen arkaluontoisuuden luokittelu ja suojaus
- **Auditointijäljet**: Kattava lokitus kaikista RAG-toiminnoista
- **Yksityisyyden suoja**: PII-tunnistus ja peittokyky

## 🔒 Yritystason turvallisuusominaisuudet

### Autentikointi ja valtuutus
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
- **Salaus**: Päästä päähän -salaus dokumenteille ja hakemistoille
- **Pääsynhallinta**: Integraatio Azure AD:n kanssa käyttäjä- ja ryhmäoikeuksille
- **Tietojen sijainti**: Maantieteelliset tietojen sijaintikontrollit vaatimustenmukaisuutta varten
- **Varmuuskopiointi ja palautus**: Automaattiset varmuuskopiointi- ja katastrofipalautuskäytännöt

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
- **Suoratoistokäsittely**: Suurten dokumenttien käsittely ilman muistiongelmia
- **Resurssien poolaus**: Kalliiden resurssien tehokas uudelleenkäyttö
- **Roskankeräys**: Optimoidut muistiallokointimallit
- **Yhteyksien hallinta**: Oikea Azure-palveluiden yhteyksien elinkaaren hallinta

### Välimuististrategiat
- **Hakuvälimuisti**: Välimuisti usein suoritetuille hauille
- **Dokumenttivälimuisti**: Muistivälimuisti suosituimmille dokumenteille
- **Indeksivälimuisti**: Optimoitu vektorihakemiston välimuisti
- **Tulosten välimuisti**: Älykäs välimuisti generoituja vastauksia varten

## 📊 Yrityskäyttötapaukset

### Tiedonhallinta
- **Yrityksen wiki**: Älykäs haku yrityksen tietokannoista
- **Politiikat ja menettelytavat**: Automaattinen vaatimustenmukaisuus ja menettelyohjeistus
- **Koulutusmateriaalit**: Älykäs oppimisen ja kehityksen tuki
- **Tutkimustietokannat**: Akateemisten ja tutkimuspapereiden analysointijärjestelmät

### Asiakastuki
- **Tukitietokanta**: Automaattiset asiakaspalveluvastaukset
- **Tuotedokumentaatio**: Älykäs tuotetiedon haku
- **Vianetsintäoppaat**: Kontekstuaalinen ongelmanratkaisun tuki
- **FAQ-järjestelmät**: Dynaaminen FAQ-luonti dokumenttikokoelmista

### Sääntelyn noudattaminen
- **Oikeudellisten dokumenttien analyysi**: Sopimusten ja oikeudellisten dokumenttien älykäs käsittely
- **Vaatimustenmukaisuuden seuranta**: Automaattinen sääntelyn noudattamisen tarkistus
- **Riskien arviointi**: Dokumenttipohjainen riskianalyysi ja raportointi
- **Auditointituki**: Älykäs dokumenttien etsintä auditointeja varten

## 🚀 Tuotantokäyttöönotto

### Valvonta ja näkyvyys
- **Application Insights**: Yksityiskohtainen telemetria ja suorituskyvyn valvonta
- **Mukautetut mittarit**: Liiketoimintakohtainen KPI-seuranta ja hälytykset
- **Hajautettu jäljitys**: Pyyntöjen päästä päähän -seuranta palveluiden välillä
- **Terveysnäkymät**: Reaaliaikainen järjestelmän terveys ja suorituskyvyn visualisointi

### Skaalautuvuus ja luotettavuus
- **Automaattinen skaalautuminen**: Automaattinen skaalautuminen kuormituksen ja suorituskykymittareiden perusteella
- **Korkea käytettävyys**: Monialueinen käyttöönotto varajärjestelyillä
- **Kuormitustestaus**: Suorituskyvyn validointi yritystason kuormitustilanteissa
- **Katastrofipalautus**: Automaattiset varmuuskopiointi- ja palautuskäytännöt

Valmiina rakentamaan yritystason RAG-järjestelmiä, jotka voivat käsitellä arkaluontoisia dokumentteja skaalautuvasti? Suunnitellaan älykkäitä tietojärjestelmiä yrityksille! 🏢📖✨

## Koodin toteutus

Täydellinen toimiva koodiesimerkki tästä oppitunnista löytyy tiedostosta `05-dotnet-agent-framework.cs`. 

Esimerkin suorittamiseksi:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Tai käytä suoraan `dotnet run`:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Koodi näyttää:

1. **Pakettien asennus**: Vaadittujen NuGet-pakettien asennus Azure AI Agentsille
2. **Ympäristön konfiguraatio**: Azure AI Foundry -päätepisteen ja malliasetusten lataus
3. **Dokumenttien lataus**: Dokumentin lataus RAG-käsittelyä varten
4. **Vektorivaraston luonti**: Vektorivaraston luonti semanttista hakua varten
5. **Agentin konfiguraatio**: AI-agentin asennus tiedostohakutoiminnoilla
6. **Hakujen suorittaminen**: Hakujen suorittaminen ladattua dokumenttia vastaan

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.