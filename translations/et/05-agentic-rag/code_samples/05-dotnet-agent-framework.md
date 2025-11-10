<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:12:33+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "et"
}
-->
# 🔍 Ettevõtte RAG Azure AI Foundryga (.NET)

## 📋 Õpieesmärgid

See märkmik näitab, kuidas luua ettevõtte tasemel Retrieval-Augmented Generation (RAG) süsteeme, kasutades Microsoft Agent Frameworki .NET-is koos Azure AI Foundryga. Õpid looma tootmisvalmis agente, kes suudavad dokumente otsida ja pakkuda täpseid, kontekstitundlikke vastuseid koos ettevõtte turvalisuse ja skaleeritavusega.

**Ettevõtte RAG võimekused, mida ehitad:**
- 📚 **Dokumendiluure**: Täiustatud dokumenditöötlus Azure AI teenustega
- 🔍 **Semantiline otsing**: Kõrge jõudlusega vektorotsing koos ettevõtte funktsioonidega
- 🛡️ **Turvalisuse integreerimine**: Rollipõhine juurdepääs ja andmekaitse mustrid
- 🏢 **Skaleeritav arhitektuur**: Tootmisvalmis RAG süsteemid koos jälgimisega

## 🎯 Ettevõtte RAG arhitektuur

### Põhilised ettevõtte komponendid
- **Azure AI Foundry**: Hallatud ettevõtte AI platvorm turvalisuse ja vastavusega
- **Püsivad agendid**: Oleku säilitamisega agendid, kes haldavad vestluste ajalugu ja konteksti
- **Vektorite haldamine**: Ettevõtte tasemel dokumentide indekseerimine ja otsing
- **Identiteedi integreerimine**: Azure AD autentimine ja rollipõhine juurdepääsukontroll

### .NET-i ettevõtte eelised
- **Tüübi turvalisus**: Kompileerimise ajal valideerimine RAG operatsioonide ja andmestruktuuride jaoks
- **Asünkroonne jõudlus**: Mitteblokeeriv dokumenditöötlus ja otsinguprotsessid
- **Mälu haldamine**: Tõhus ressursside kasutamine suurte dokumendikogude jaoks
- **Integreerimismustrid**: Natiivne Azure teenuste integreerimine sõltuvuste süstimisega

## 🏗️ Tehniline arhitektuur

### Ettevõtte RAG torujuhe
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Põhilised .NET komponendid
- **Azure.AI.Agents.Persistent**: Ettevõtte agentide haldamine oleku säilitamisega
- **Azure.Identity**: Integreeritud autentimine turvaliseks Azure teenuste kasutamiseks
- **Microsoft.Agents.AI.AzureAI**: Azure'ile optimeeritud agentide raamistik
- **System.Linq.Async**: Kõrge jõudlusega asünkroonsed LINQ operatsioonid

## 🔧 Ettevõtte funktsioonid ja eelised

### Turvalisus ja vastavus
- **Azure AD integreerimine**: Ettevõtte identiteedihaldus ja autentimine
- **Rollipõhine juurdepääs**: Täpne õiguste haldamine dokumentide ja operatsioonide jaoks
- **Andmekaitse**: Krüpteerimine nii salvestamisel kui edastamisel tundlike dokumentide jaoks
- **Auditilogid**: Ulatuslik tegevuste jälgimine vastavusnõuete täitmiseks

### Jõudlus ja skaleeritavus
- **Ühenduste haldamine**: Tõhus Azure teenuste ühenduste haldamine
- **Asünkroonne töötlemine**: Mitteblokeerivad operatsioonid suure läbilaskevõimega stsenaariumide jaoks
- **Vahemälu strateegiad**: Nutikas vahemälu sageli kasutatavate dokumentide jaoks
- **Koormuse tasakaalustamine**: Hajutatud töötlemine suurte juurutuste jaoks

### Haldamine ja jälgimine
- **Tervisekontrollid**: Sisseehitatud jälgimine RAG süsteemi komponentide jaoks
- **Jõudlusmõõdikud**: Üksikasjalik analüüs otsingukvaliteedi ja vastuseaegade kohta
- **Vigade käsitlemine**: Ulatuslik erandite haldamine koos korduspoliitikatega
- **Konfiguratsiooni haldamine**: Keskkonnaspetsiifilised seaded valideerimisega

## ⚙️ Eeltingimused ja seadistamine

**Arenduskeskkond:**
- .NET 9.0 SDK või uuem
- Visual Studio 2022 või VS Code koos C# laiendusega
- Azure tellimus koos AI Foundry juurdepääsuga

**Nõutavad NuGet paketid:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure autentimise seadistamine:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Keskkonna konfiguratsioon:**
* Azure AI Foundry konfiguratsioon (automaatselt hallatud Azure CLI kaudu)
* Veendu, et oled autentitud õige Azure tellimusega

## 📊 Ettevõtte RAG mustrid

### Dokumendihalduse mustrid
- **Massiline üleslaadimine**: Tõhus suurte dokumendikogude töötlemine
- **Järkjärguline uuendamine**: Reaalajas dokumentide lisamine ja muutmine
- **Versioonihaldus**: Dokumentide versioonimine ja muudatuste jälgimine
- **Metaandmete haldamine**: Rikkalikud dokumendi atribuudid ja taksonoomia

### Otsingu ja leidmise mustrid
- **Hübriidotsing**: Semantilise ja märksõnaotsingu kombineerimine parimate tulemuste saavutamiseks
- **Faktoriotsing**: Mitmemõõtmeline filtreerimine ja kategoriseerimine
- **Asjakohasuse häälestamine**: Kohandatud skoorimisalgoritmid valdkonnapõhiste vajaduste jaoks
- **Tulemuste järjestamine**: Täiustatud järjestamine äriloogika integreerimisega

### Turvalisuse mustrid
- **Dokumenditasandi turvalisus**: Täpne juurdepääsukontroll iga dokumendi jaoks
- **Andmete klassifitseerimine**: Automaatne tundlikkuse märgistamine ja kaitse
- **Auditilogid**: Kõigi RAG operatsioonide ulatuslik logimine
- **Privaatsuse kaitse**: PII tuvastamine ja eemaldamine

## 🔒 Ettevõtte turvafunktsioonid

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
- **Krüpteerimine**: Lõpuni krüpteerimine dokumentide ja otsinguindeksite jaoks
- **Juurdepääsukontrollid**: Integreerimine Azure AD-ga kasutaja- ja grupilubade jaoks
- **Andmete asukoht**: Geograafiline andmete asukoha kontroll vastavuse jaoks
- **Varundamine ja taastamine**: Automaatne varundamine ja katastroofide taastamise võimalused

## 📈 Jõudluse optimeerimine

### Asünkroonsed töötlemismustrid
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Mälu haldamine
- **Voogtöötlus**: Suurte dokumentide töötlemine ilma mäluprobleemideta
- **Ressursside jagamine**: Kallite ressursside tõhus taaskasutus
- **Prügikoristus**: Optimeeritud mälukasutuse mustrid
- **Ühenduste haldamine**: Õige Azure teenuste ühenduste elutsükkel

### Vahemälu strateegiad
- **Päringute vahemälu**: Sageli teostatavate otsingute vahemällu salvestamine
- **Dokumentide vahemälu**: Kuumade dokumentide vahemällu salvestamine
- **Indeksi vahemälu**: Optimeeritud vektorindeksi vahemällu salvestamine
- **Tulemuste vahemälu**: Nutikas genereeritud vastuste vahemällu salvestamine

## 📊 Ettevõtte kasutusjuhtumid

### Teadmiste haldamine
- **Ettevõtte Wiki**: Intelligentsed otsingud ettevõtte teadmistebaasides
- **Poliitikad ja protseduurid**: Automaatne vastavus ja protseduuride juhendamine
- **Koolitusmaterjalid**: Intelligentsed õppimise ja arendamise abivahendid
- **Uurimisandmebaasid**: Akadeemiliste ja teaduslike artiklite analüüsi süsteemid

### Klienditugi
- **Tugiteenuste teadmistebaas**: Automaatne klienditeeninduse vastamine
- **Tootedokumentatsioon**: Intelligentsed tooteteabe otsingud
- **Tõrkeotsingu juhendid**: Kontekstipõhine probleemide lahendamise abi
- **KKK süsteemid**: Dünaamiline KKK genereerimine dokumendikogudest

### Regulatiivne vastavus
- **Õigusdokumentide analüüs**: Lepingute ja õigusdokumentide intelligentsus
- **Vastavuse jälgimine**: Automaatne regulatiivse vastavuse kontroll
- **Riskihindamine**: Dokumentide põhine riskianalüüs ja aruandlus
- **Auditi tugi**: Intelligentsed dokumentide avastamise võimalused auditite jaoks

## 🚀 Tootmise juurutamine

### Jälgimine ja nähtavus
- **Application Insights**: Üksikasjalik telemeetria ja jõudluse jälgimine
- **Kohandatud mõõdikud**: Äri-spetsiifiliste KPI-de jälgimine ja hoiatused
- **Hajutatud jälgimine**: Päringute jälgimine teenuste vahel
- **Tervise juhtpaneelid**: Reaalajas süsteemi tervise ja jõudluse visualiseerimine

### Skaleeritavus ja töökindlus
- **Automaatne skaleerimine**: Automaatne skaleerimine koormuse ja jõudlusmõõdikute alusel
- **Kõrge kättesaadavus**: Mitme piirkonna juurutamine koos tõrkesiirde võimalustega
- **Koormustestimine**: Jõudluse valideerimine ettevõtte koormustingimustes
- **Katastroofide taastamine**: Automaatne varundamine ja taastamisprotseduurid

Valmis looma ettevõtte tasemel RAG süsteeme, mis suudavad hallata tundlikke dokumente suurel skaalal? Kujundame intelligentsed teadmiste süsteemid ettevõtetele! 🏢📖✨

## Koodi rakendamine

Selle õppetunni täielik töötav koodinäide on saadaval failis `05-dotnet-agent-framework.cs`. 

Näite käivitamiseks:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Või kasuta otse `dotnet run`:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kood näitab:

1. **Pakettide paigaldamine**: Nõutavate NuGet pakettide paigaldamine Azure AI agentide jaoks
2. **Keskkonna konfiguratsioon**: Azure AI Foundry lõpp-punkti ja mudeli seadete laadimine
3. **Dokumendi üleslaadimine**: Dokumendi üleslaadimine RAG töötlemiseks
4. **Vektorite loomine**: Vektorite loomine semantilise otsingu jaoks
5. **Agendi konfiguratsioon**: AI agendi seadistamine failide otsinguvõimekusega
6. **Päringute täitmine**: Päringute käivitamine üleslaetud dokumendi vastu

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta arusaamatuste või valesti tõlgenduste eest, mis võivad tekkida selle tõlke kasutamisest.