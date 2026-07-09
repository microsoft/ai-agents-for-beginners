# 🔍 Ettevõtte RAG Microsoft Foundry (.NET) abil

## 📋 Õpieesmärgid

See märkmik näitab, kuidas ehitada ettevõtte tasemel Retrieval-Augmented Generation (RAG) süsteeme Microsoft Agent Frameworki abil .NET-is Microsoft Foundry abil. Õpid looma tootmisele valmis agente, kes suudavad dokumente otsida ja pakkuda täpseid ning kontekstiteadlikke vastuseid koos ettevõtte turvalisuse ja skaleeritavusega.

**Ettevõtte RAG võimekused, mida sa ehitad:**
- 📚 **Dokumendiintelligentsus**: Täiustatud dokumentide töötlemine Azure AI teenustega
- 🔍 **Sisemõtteline otsing**: Kõrge jõudlusega vektorotsing ettevõtte funktsioonidega
- 🛡️ **Turbeintegratsioon**: Rollipõhine ligipääsu- ja andmekaitse mustrid
- 🏢 **Skaleeritav arhitektuur**: Tootmisele valmis RAG süsteemid jälgimisega

## 🎯 Ettevõtte RAG arhitektuur

### Põhilised ettevõtte komponendid
- **Microsoft Foundry**: Hallatud ettevõtte AI platvorm koos turbe ja vastavusega
- **Püsivad agendid**: Oleku säilitava vestlusajaloo ja konteksti haldamisega agendid
- **Vektoriaalse poe haldus**: Ettevõtte tasemel dokumentide indekseerimine ja otsing
- **Identiteedi integratsioon**: Azure AD autentimine ja rollipõhine ligipääsukontroll

### .NET ettevõtte eelised
- **Tüübikindlus**: Kokkupandud ajal toimuv valideerimine RAG operatsioonide ja andmestruktuuride jaoks
- **Asünkroonne jõudlus**: Mitteblokeeriv dokumentide töötlemine ja otsing
- **Mälu haldus**: Tõhus ressursside kasutus suurte dokumentide kogumite jaoks
- **Integratsioonimustrid**: Native Azure teenuste integreerimine sõltuvussüstimisega

## 🏗️ Tehniline arhitektuur

### Ettevõtte RAG torujuhe
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Põhilised .NET komponendid
- **Azure.AI.Agents.Persistent**: Ettevõtte agendi haldus koos oleku säilitamisega
- **Azure.Identity**: Integreeritud autentimine turvaliseks Azure teenustele ligipääsuks
- **Microsoft.Agents.AI.AzureAI**: Azure jaoks optimeeritud agendi raamistik
- **System.Linq.Async**: Kõrge jõudlusega asünkroonsed LINQ operatsioonid

## 🔧 Ettevõtte funktsioonid ja eelised

### Turve ja vastavus
- **Azure AD integratsioon**: Ettevõtte identiteedi haldus ja autentimine
- **Rollipõhine ligipääs**: Peenhäälestatud load dokumentidele ligipääsuks ja toiminguteks
- **Andmekaitse**: Krüpteerimine puhkeolekus ja andmete edastamisel tundlike dokumentide jaoks
- **Auditilogimine**: Töötlemistegevuse põhjalik jälgimine vastavusnõuete täitmiseks

### Jõudlus ja skaleeritavus
- **Ühenduste puhvrid**: Tõhus Azure teenuste ühenduste haldamine
- **Asünkroonne töötlemine**: Mitteblokeerivad operatsioonid suure läbilaskevõime jaoks
- **Vahemälustrateegiad**: Intelligentsed vahemälud tihti kasutatavatele dokumentidele
- **Koormuse tasakaalustamine**: Hajutatud töötlemine suuremahuliste paigalduste jaoks

### Halduse ja jälgimise võimalused
- **Tervisekontrollid**: Sisseehitatud jälgimine RAG süsteemi komponentide jaoks
- **Tulemuslikkuse mõõdikud**: Üksikasjalik analüüs otsingu kvaliteedi ja vastuseaja kohta
- **Vigade käsitlemine**: Põhjalik erandite haldus koos taastepoliitikatega
- **Konfiguratsiooni haldus**: Keskkonnaspetsiifilised seaded koos valideerimisega

## ⚙️ Eeldused ja seadistamine

**Arenduskeskkond:**
- .NET 9.0 SDK või uuem
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
# Installi Azure CLI ja autentimine
az login
az account set --subscription "your-subscription-id"
```

**Keskkonna konfiguratsioon:**
* Microsoft Foundry konfiguratsioon (Azure CLI abil automaatselt hallatud)
* Veendu, et oled autentitud õigele Azure tellimusele

## 📊 Ettevõtte RAG mustrid

### Dokumentide haldamise mustrid
- **Emaltõst**: Suurte dokumentide kogumite tõhus töötlemine
- **Tõusvad uuendused**: Reaalajas dokumentide lisamine ja muutmine
- **Versioonihaldus**: Dokumentide versioonimine ja muudatuste jälgimine
- **Metaandmete haldus**: Rikkalikud dokumendi atribuudid ja taksonoomia

### Otsingu ja andmete päringu mustrid
- **Hübriidotsing**: Semantilise ja märksõnapõhise otsingu ühendamine optimaalse tulemuse jaoks
- **Fasetiseeritud otsing**: Mitmemõõtmeline filtreerimine ja kategooriseerimine
- **Asjakohasuse häälestamine**: Kohandatud hindamisalgoritmid domeenispetsiifiliste vajaduste jaoks
- **Tulemuste järjestamine**: Täiustatud järjestamine äriloogika integreerimisega

### Turbe mustrid
- **Dokumendipõhine turve**: Peenhäälestatud ligipääsukontroll iga dokumendi kohta
- **Andmete klassifitseerimine**: Automaatne tundlikkuse märgistamine ja kaitse
- **Auditirajad**: Kõigi RAG operatsioonide põhjalik logimine
- **Privaatsuse kaitse**: PII tuvastamise ja maskeerimise võimekused

## 🔒 Ettevõtte turbefunktsioonid

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
- **Krüpteerimine**: Lõpp-lõpuni krüpteerimine dokumentidele ja otsingu indeksitele
- **Ligipääsukontrollid**: Azure AD integratsioon kasutaja- ja grupilubade halduseks
- **Andmete paiknemine**: Andmete geograafiline asukohakontroll vastavuse tagamiseks
- **Varundamine ja taastamine**: Automaatne varundus ja katastroofitaastamise võimalused

## 📈 Tulemuste optimeerimine

### Asünkroonsed töötlemise mustrid
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Mälu haldus
- **Striimingutöötlus**: Suurte dokumentide töötlemine ilma mäluprobleemideta
- **Resursside puhverdus**: Kallite ressursside tõhus taaskasutus
- **Jäätmekoristus**: Optimeeritud mälu jaotamise mustrid
- **Ühenduste haldus**: Azure teenuste ühenduste elutsükli korrektne haldamine

### Vahemälu strateegiad
- **Päringu vahemälu**: Tihti kasutatavate otsingute vahemällu salvestamine
- **Dokumendi vahemälu**: Mälus hoitav kuumade dokumentide vahemälu
- **Indeksi vahemälu**: Optimeeritud vektori indeksi vahemällu salvestamine
- **Tulemuste vahemälu**: Intelligentsed genereeritud vastuste vahemälud

## 📊 Ettevõtte kasutusjuhtumid

### Teadmiste haldus
- **Ettevõtte vikiraamat**: Intelligentsed otsingud ettevõtte teadmistebaasides
- **Poliitika ja protseduurid**: Automatiseeritud vastavuse ja protseduuride juhendamine
- **Koolitusmaterjalid**: Intelligentsed õppimise ja arengu abivahendid
- **Uurimiste andmebaasid**: Akadeemiliste ja teadustööde analüüsi süsteemid

### Klienditugi
- **Toetus teadmiste baas**: Automatiseeritud klienditeeninduse vastused
- **Toote dokumentatsioon**: Intelligentsed tooteinfo päringud
- **Tõrkeotsingu juhendid**: Kontekstitundlik probleemilahenduse abi
- **KKK süsteemid**: Dünaamiline KKK loomine dokumentide kogumitest

### Regulatiivne vastavus
- **Õigusdokumentide analüüs**: Lepingute ja juriidiliste dokumentide intelligentsus
- **Vastavuse jälgimine**: Automatiseeritud regulatiivse vastavuse kontroll
- **Riskihindamine**: Dokumentide põhine riskianalüüs ja raporteerimine
- **Auditi tugi**: Intelligentsed dokumentide leidmise võimalused audititeks

## 🚀 Tootmisesse juurutamine

### Jälgimine ja vaadeldavus
- **Application Insights**: Üksikasjalik telemeetria ja jõudluse jälgimine
- **Kohandatud mõõdikud**: Ärispetsiifiline KPI jälgimine ja hoiatused
- **Hajutatud jälgimine**: Taotlustevoolu jälgimine kõigi teenuste vahel
- **Tervise juhtpaneelid**: Reaalaegne süsteemi tervise ja jõudluse visualiseerimine

### Skaleeritavus ja töökindlus
- **Automaatne skaaleerimine**: Automaatne skaleerimine koormuse ja mõõdikute põhjal
- **Kõrge kättesaadavus**: Mitteregiooniline juurutus varukoopia võimalustega
- **Koormustestimine**: Jõudluse valideerimine ettevõtte koormuse tingimustes
- **Katastroofitaastamine**: Automaatne varundus ja taastamise protseduurid

Kas oled valmis ehitama ettevõtte tasemel RAG süsteeme, mis suudavad käsitleda tundlikke dokumente suures mahus? Loome koos arukad teadmiste süsteemid ettevõttele! 🏢📖✨

## Koodi rakendus

Selle õppetunni täielik töötav koodinäide on saadaval failis `05-dotnet-agent-framework.cs`. 

Näidise käivitamiseks:

```bash
# Tee skript täidetavaks (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Käivita .NET ühefaililine rakendus
./05-dotnet-agent-framework.cs
```

Või kasuta otse käsku `dotnet run`:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kood demonstreerib:

1. **Paketi paigaldus**: Nõutavate NuGet pakettide paigaldamine Azure AI Agentide jaoks
2. **Keskkonna konfiguratsioon**: Microsoft Foundry lõpp-punkti ja mudeli seadete laadimine
3. **Dokumendi üleslaadimine**: Dokumendi üleslaadimine RAG töötlemiseks
4. **Vektoriaalse poe loomine**: Vektoriaalse poe loomine semantilise otsingu jaoks
5. **Agendi konfiguratsioon**: AI agendi seadistamine failide otsingu võimekusega
6. **Päringute täitmine**: Päringute jooksutamine üleslaaditud dokumendi vastu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->