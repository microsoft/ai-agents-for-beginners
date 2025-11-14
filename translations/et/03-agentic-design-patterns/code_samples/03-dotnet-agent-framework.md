<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:53:44+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "et"
}
-->
# 🎨 Agentliku disainimustrid GitHubi mudelitega (.NET)

## 📋 Õpieesmärgid

See märkmik tutvustab ettevõtte tasemel disainimustreid intelligentsete agentide loomiseks, kasutades Microsoft Agent Frameworki .NET-is koos GitHubi mudelite integreerimisega. Õpid professionaalseid mustreid ja arhitektuurilisi lähenemisi, mis muudavad agendid tootmisvalmis, hooldatavaks ja skaleeritavaks.

**Ettevõtte disainimustrid:**
- 🏭 **Tehase muster**: Standardiseeritud agentide loomine sõltuvuste süstimisega
- 🔧 **Ehitusmuster**: Sujuv agentide konfigureerimine ja seadistamine
- 🧵 **Lõimeohutud mustrid**: Samaaegne vestluste haldamine
- 📋 **Repository muster**: Tööriistade ja võimekuste organiseeritud haldamine

## 🎯 .NET-i spetsiifilised arhitektuurilised eelised

### Ettevõtte funktsioonid
- **Tugev tüüpimine**: Kogumisaegne valideerimine ja IntelliSense tugi
- **Sõltuvuste süstimine**: Sisseehitatud DI konteineri integreerimine
- **Konfiguratsiooni haldamine**: IConfiguration ja Options mustrid
- **Async/Await**: Esmaklassiline asünkroonne programmeerimise tugi

### Tootmisvalmis mustrid
- **Logimise integreerimine**: ILogger ja struktureeritud logimise tugi
- **Tervisekontrollid**: Sisseehitatud jälgimine ja diagnostika
- **Konfiguratsiooni valideerimine**: Tugev tüüpimine andmeannotatsioonidega
- **Vigade käsitlemine**: Struktureeritud erandite haldamine

## 🔧 Tehniline arhitektuur

### Põhilised .NET komponendid
- **Microsoft.Extensions.AI**: Ühtlustatud AI teenuste abstraktsioonid
- **Microsoft.Agents.AI**: Ettevõtte agentide orkestreerimise raamistik
- **GitHubi mudelite integreerimine**: Kõrge jõudlusega API kliendi mustrid
- **Konfiguratsioonisüsteem**: appsettings.json ja keskkonna integreerimine

### Disainimustri rakendamine
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Näidatud ettevõtte mustrid

### 1. **Loomismustrid**
- **Agent Factory**: Keskne agentide loomine järjepideva konfiguratsiooniga
- **Ehitusmuster**: Sujuv API keerukate agentide konfigureerimiseks
- **Singleton muster**: Jagatud ressursside ja konfiguratsiooni haldamine
- **Sõltuvuste süstimine**: Lõdvalt seotud ja testitav

### 2. **Käitumismustrid**
- **Strateegia muster**: Vahetatavad tööriistade täitmise strateegiad
- **Käsu muster**: Kapseldatud agentide operatsioonid koos undo/redo funktsiooniga
- **Vaatleja muster**: Sündmustepõhine agentide elutsükli haldamine
- **Mallimeetod**: Standardiseeritud agentide täitmise töövood

### 3. **Struktuurimustrid**
- **Adapteri muster**: GitHubi mudelite API integreerimise kiht
- **Dekoraatori muster**: Agentide võimekuse täiustamine
- **Fassaadi muster**: Lihtsustatud agentide interaktsiooni liidesed
- **Proksi muster**: Laisk laadimine ja vahemälu jõudluse parandamiseks

## ⚙️ Eeldused ja seadistamine

**Arenduskeskkond:**
- .NET 9.0 SDK või uuem
- Visual Studio 2022 või VS Code koos C# laiendusega
- GitHubi mudelite API juurdepääs

**NuGet sõltuvused:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguratsioon (.env fail):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 .NET disainiprintsiibid

### SOLID printsiibid
- **Üksiku vastutuse**: Igal komponendil on üks selge eesmärk
- **Avatud/Suletud**: Laiendatav ilma muutmiseta
- **Liskovi asendamine**: Liidese põhised tööriistade rakendused
- **Liidese eraldamine**: Keskendunud, ühtsed liidesed
- **Sõltuvuste inversioon**: Tugineda abstraktsioonidele, mitte konkreetsetele rakendustele

### Puhas arhitektuur
- **Domeeni kiht**: Põhilised agentide ja tööriistade abstraktsioonid
- **Rakenduse kiht**: Agentide orkestreerimine ja töövood
- **Infrastruktuuri kiht**: GitHubi mudelite integreerimine ja välised teenused
- **Esitluse kiht**: Kasutaja interaktsioon ja vastuste vormindamine

## 🔒 Ettevõtte kaalutlused

### Turvalisus
- **Mandaatide haldamine**: Turvaline API võtmete käsitlemine IConfiguration abil
- **Sisendi valideerimine**: Tugev tüüpimine ja andmeannotatsioonide valideerimine
- **Väljundi sanitiseerimine**: Turvaline vastuste töötlemine ja filtreerimine
- **Auditilogimine**: Põhjalik operatsioonide jälgimine

### Jõudlus
- **Asünkroonsed mustrid**: Mitteblokeerivad I/O operatsioonid
- **Ühenduste basseinid**: Tõhus HTTP kliendi haldamine
- **Vahemälu**: Vastuste vahemällu salvestamine jõudluse parandamiseks
- **Ressursside haldamine**: Õige utiliseerimine ja puhastamise mustrid

### Skaleeritavus
- **Lõimeohutus**: Samaaegne agentide täitmise tugi
- **Ressursside basseinid**: Tõhus ressursside kasutamine
- **Koormuse haldamine**: Kiiruse piiramine ja tagasurvestuse käsitlemine
- **Jälgimine**: Jõudlusmõõdikud ja tervisekontrollid

## 🚀 Tootmisele juurutamine

- **Konfiguratsiooni haldamine**: Keskkonnaspetsiifilised seaded
- **Logimise strateegia**: Struktureeritud logimine koos korrelatsiooni ID-dega
- **Vigade käsitlemine**: Globaalne erandite käsitlemine koos õige taastamisega
- **Jälgimine**: Rakenduse ülevaated ja jõudlusloendurid
- **Testimine**: Üksustestid, integratsioonitestid ja koormustestimise mustrid

Valmis looma ettevõtte tasemel intelligentseid agente .NET-is? Kujundame midagi vastupidavat! 🏢✨

## Koodinäide

Täieliku töötava näite jaoks vaata [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.