# 🔍 Ettevõtte RAG Microsoft Foundry (.NET) abil

## 📋 Õpieesmärgid

See märkmik demonstreerib, kuidas ehitada ettevõtte kvaliteediga Retrieval-Augmented Generation (RAG) süsteeme Microsoft Agent Frameworki abil .NET-is koos Microsoft Foundry'ga. Õpid looma tootmiseks valmis agente, kes suudavad dokumente otsida ning pakkuda täpseid, kontekstiteadlikke vastuseid ettevõtte turvalisuse ja skaleeritavusega.

**Ettevõtte RAG võimekused, mida ehitad:**
- 📚 **Dokumendi intelligentsus**: Täiustatud dokumenditöötlus Azure AI teenustega
- 🔍 **Semantiline otsing**: Kõrge jõudlusega vektoripõhine otsing ettevõtte funktsioonidega
- 🛡️ **Turbeintegratsioon**: Rollipõhine ligipääs ja andmekaitse mustrid
- 🏢 **Skaleeritav arhitektuur**: Tootmiskõlblikud RAG süsteemid koos monitorimisega

## 🎯 Ettevõtte RAG arhitektuur

### Põhikomponendid ettevõttele
- **Microsoft Foundry**: Hallatud ettevõtte AI platvorm turve ja vastavusega
- **Püsivad Agendid**: Oleku säilitusega agentid koos vestluste ajaloo ja konteksti haldusega
- **Vektoripoe haldus**: Ettevõtte kvaliteediga dokumendindekseerimine ja otsing
- **Identiteedi integratsioon**: Azure AD autentimine ja rollipõhine ligipääsukontroll

### .NET ettevõtte eelised
- **Tüübikindlus**: Kompileerimisajal valideerimine RAG operatsioonide ja andmestruktuuride jaoks
- **Asünkroonne jõudlus**: Mitteblokeeriv dokumenditöötlus ja otsingutegevused
- **Mälu haldus**: Tõhus ressursikasutus suurte dokumentide kogu jaoks
- **Integratsioonimustrid**: Natiivne Azure teenuste integreerimine sõltuvussüstimisega

## 🏗️ Tehniline arhitektuur

### Ettevõtte RAG torujuhe
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Põhikomponendid .NET-is
- **Azure.AI.Agents.Persistent**: Ettevõtte agentide haldus oleku püsivusega
- **Azure.Identity**: Integreeritud autentimine turvaliseks Azure teenuste ligipääsuks
- **Microsoft.Agents.AI.AzureAI**: Azure-le optimeeritud agentide raamistik
- **System.Linq.Async**: Kõrge jõudlusega asünkroonsed LINQ operatsioonid

## 🔧 Ettevõtte omadused ja eelised

### Turvalisus ja vastavus
- **Azure AD integratsioon**: Ettevõtte identiteedihaldus ja autentimine
- **Rollipõhine ligipääs**: Peenhäälestatud õigused dokumentidele ja toimingutele
- **Andmekaitse**: Krüpteerimine puhkeolekus ja edastuskanalites tundlikele dokumentidele
- **Auditilogimine**: Üldine tegevuste jälgimine vastavuse nõuete tarvis

### Jõudlus ja skaleeritavus
- **Ühenduse mahutamine**: Tõhus Azure teenuste ühenduse haldus
- **Asünkroonne töötlemine**: Mitteblokeerivad toimingud kõrge läbilaskevõime olukordades
- **Vahemällu salvestamise strateegiad**: Nutikas vahemällu salvestamine sageli kasutatavatele dokumentidele
- **Koormuse tasakaalustamine**: Hajutatud töötlemine suurte levitamiste jaoks

### Halduse ja järelevalve funktsioonid
- **Tervisekontrollid**: Sisseehitatud jälgimine RAG süsteemi komponentidele
- **Jõudlusmõõdikud**: Detailne analüütika otsingu kvaliteedi ja vastamisaja kohta
- **Vea käitlemine**: Kõikehõlmav erandite haldus koos taaste poliitikatega
- **Seadistamise haldus**: Keskkonnaspetsiifilised seadistused valideerimisega

## ⚙️ Nõuded ja seadistamine

**Arenduskeskkond:**
- .NET 9.0 SDK või kõrgem
- Visual Studio 2022 või VS Code koos C# laiendusega
- Azure tellimus Microsoft Foundry ligipääsuga

**Nõutavad NuGet paketid:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure autentimise seadistus:**
```bash
# Paigalda Azure CLI ja autentimine
az login
az account set --subscription "your-subscription-id"
```

**Keskkonna konfiguratsioon:**
* Microsoft Foundry seadistus (automaatne haldus Azure CLI kaudu)
* Veendu, et oled autentitud õigele Azure tellimusele

## 📊 Ettevõtte RAG mustrid

### Dokumendihalduse mustrid
- **Massiline üleslaadimine**: Suurte dokumendikogude tõhus töötlemine
- **Tõusvad uuendused**: Reaalajas dokumentide lisamine ja muutmine
- **Versioonihaldus**: Dokumentide versioonide ja muudatuste jälgimine
- **Metaandmete haldus**: Rikkalikud dokumendi atribuudid ja taksonoomia

### Otsingu ja leidmise mustrid
- **Hübriidotsing**: Semantilise ja märksõnalise otsingu ühendamine optimaalseks tulemuseks
- **Faseteerimine**: Mitmepoolne filtreerimine ja kategoriseerimine
- **Relevantsuse häälestus**: Kohandatud skoorimise algoritmid domeenispetsiifiliste vajaduste jaoks
- **Tulemuste järjestamine**: Täiustatud järjestamine äriloogika integratsiooniga

### Turbemustrid
- **Dokumendi tasemel turve**: Peenhäälestatud ligipääsukontroll iga dokumendi kohta
- **Andmete klassifitseerimine**: Automaatne tundlikkuse märgistamine ja kaitse
- **Auditijäljed**: Kõikide RAG operatsioonide ulatuslik logimine
- **Privaatsuskaitse**: Isikuandmete tuvastamine ja peitmine

## 🔒 Ettevõtte turbe funktsioonid

### Autentimine ja autoriseerimine
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

### Andmekaitse
- **Krüpteerimine**: Lõpust-lõpuni krüpteerimine dokumentide ja otsingute indeksite jaoks
- **Ligipääsukontrollid**: Integratsioon Azure AD-ga kasutaja ja grupi õiguste haldamiseks
- **Andmete paiknemine**: Geograafilised andmelokatsiooni kontrollid vastavuse tagamiseks
- **Varundamine ja taastamine**: Automaatne varundamise ja katastroofitaastamise võimekus

## 📈 Jõudluse optimeerimine

### Asünkroonse töötlemise mustrid
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Mälu haldus
- **Striimimine**: Suurte dokumentide töötlemine ilma mälu probleemideta
- **Ressursside mahutamine**: Kulukate ressursside tõhus taaskasutus
- **Mälu kogumine**: Optimeeritud mälu eraldamise mustrid
- **Ühenduse haldus**: Õige Azure teenuse ühenduse elutsükkel

### Vahemällu salvestamise strateegiad
- **Päringu vahemällu salvestamine**: Sageli tehtud otsingute vahemällu salvestamine
- **Dokumendi vahemällu salvestamine**: Mälu vahemälu kuuma dokumendi jaoks
- **Indeksi vahemällu salvestamine**: Optimeeritud vektorindeksi vahemälu
- **Tulemuste vahemällu salvestamine**: Nutikas genereeritud vastuste vahemälu

## 📊 Ettevõtte kasutusjuhtumid

### Teadmiste haldus
- **Ettevõtte vikiraamat**: Intelligentsed otsingud ettevõtte teadmistebaasides
- **Eeskirjad ja protseduurid**: Automaatne vastavuse ja juhendamise tugi
- **Koolitusmaterjalid**: Intelligentsed õppimise ja arengu abivahendid
- **Uurimisandmebaasid**: Akadeemiliste ja uurimistöö dokumentide analüüsisüsteemid

### Klienditugi
- **Tugiteadmiste baas**: Automaatne klienditeeninduse vastamine
- **Tootedokumendid**: Intelligentsed tooteteabe otsingud
- **Veaotsingu juhendid**: Kontekstuaalne probleemide lahendamise abi
- **KKK süsteemid**: Dünaamiline korduma kippuvate küsimuste genereerimine dokumentide põhjal

### Reguleerimisvastavus
- **Õigusdokumentide analüüs**: Lepingu- ja juriidiliste dokumentide intelligentsus
- **Vastavuse jälgimine**: Automaatne regulatiivse vastavuse kontroll
- **Riskihindamine**: Dokumendipõhine riski analüüs ja aruandlus
- **Auditi tugi**: Intelligentsed dokumendiotsingud auditite tarvis

## 🚀 Tootmiselevõtt

### Jälgimine ja nähtavus
- **Application Insights**: Detailne telemeetria ja jõudluse jälgimine
- **Kohandatud mõõdikud**: Ärispetsiifiline KPI jälgimine ja alarmid
- **Jaotatud jälgimine**: Lõpust-lõpuni päringute jälgimine teenuste vahel
- **Tervisemonitorid**: Reaalajas süsteemi tervise ja jõudluse visualiseerimine

### Skaleeritavus ja töökindlus
- **Automaatne skaleerimine**: Automaatne skaleerimine koormuse ja jõudluse põhjal
- **Kõrge saadavus**: Mitmeregiooniline kasutuselevõtt automaatse üleminemisega
- **Koormustestimine**: Jõudluse valideerimine ettevõtte koormuse tingimustes
- **Katastroofitaastamine**: Automaatne varundamine ja taastamisprotseduurid

Kas oled valmis ehitama ettevõtte kvaliteediga RAG süsteeme, mis suudavad skaalas käsitleda tundlikke dokumente? Kujundame ühes intelligentseid teadmiste süsteeme ettevõttele! 🏢📖✨

## Koodi rakendamine

Selle õppetunni täielik toimiv koodinäide on saadaval failis `05-dotnet-agent-framework.cs`. 

Näite käivitamiseks:

```bash
# Tee skript käivitatavaks (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Käivita .NET ühekordne failirakendus
./05-dotnet-agent-framework.cs
```

Või kasuta otse `dotnet run` käsku:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kood demonstreerib:

1. **Paketi paigaldamine**: Nõutavate NuGet pakettide install Azure AI Agentite jaoks
2. **Keskkonna seadistamine**: Microsoft Foundry lõpp-punkti ja mudeli seaded
3. **Dokumendi üleslaadimine**: Dokumendi üleslaadimine RAG töötlemiseks
4. **Vektoripoe loomine**: Vektoripõhise otsingu võimaldamiseks poe loomine
5. **Agendi seadistamine**: AI agendi seadistamine failiotsingu võimekusega
6. **Päringu täitmine**: Päringute käivitamine üleslaaditud dokumendi vastu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->