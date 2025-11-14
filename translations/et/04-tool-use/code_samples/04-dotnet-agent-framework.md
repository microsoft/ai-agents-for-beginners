<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:30:04+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "et"
}
-->
# 🛠️ Täiustatud tööriistade kasutamine GitHubi mudelitega (.NET)

## 📋 Õpieesmärgid

See märkmik tutvustab ettevõtte tasemel tööriistade integreerimise mustreid, kasutades Microsoft Agent Frameworki .NET-is koos GitHubi mudelitega. Õpid looma keerukaid agente, mis kasutavad mitut spetsialiseeritud tööriista, rakendades C# tugevat tüüpimist ja .NET-i ettevõtte funktsioone.

**Tööriistade täiustatud võimekused, mida omandad:**
- 🔧 **Mitme tööriista arhitektuur**: Agendid, millel on mitmed spetsialiseeritud võimekused
- 🎯 **Tüübikindel tööriistade täitmine**: C# kompileerimiseaegne valideerimine
- 📊 **Ettevõtte tööriistade mustrid**: Tootmiskõlblik tööriistade disain ja veahaldus
- 🔗 **Tööriistade koostamine**: Tööriistade kombineerimine keerukate äriprotsesside jaoks

## 🎯 .NET tööriistade arhitektuuri eelised

### Ettevõtte tööriistade funktsioonid
- **Kompileerimiseaegne valideerimine**: Tugev tüüpimine tagab tööriistade parameetrite korrektsuse
- **Sõltuvuste süstimine**: IoC konteineri integreerimine tööriistade haldamiseks
- **Async/Await mustrid**: Mitteblokeeriv tööriistade täitmine koos ressursside korrektse haldamisega
- **Struktureeritud logimine**: Sisseehitatud logimise integreerimine tööriistade täitmise jälgimiseks

### Tootmiskõlblikud mustrid
- **Erandite käsitlemine**: Põhjalik veahaldus tüübipõhiste eranditega
- **Ressursside haldamine**: Korrektsed utiliseerimismustrid ja mäluhaldus
- **Jõudluse jälgimine**: Sisseehitatud mõõdikud ja jõudluse loendurid
- **Konfiguratsiooni haldamine**: Tüübikindel konfiguratsioon koos valideerimisega

## 🔧 Tehniline arhitektuur

### Põhilised .NET tööriistade komponendid
- **Microsoft.Extensions.AI**: Ühtne tööriistade abstraktsioonikiht
- **Microsoft.Agents.AI**: Ettevõtte tasemel tööriistade orkestreerimine
- **GitHubi mudelite integreerimine**: Kõrge jõudlusega API klient koos ühenduste haldamisega

### Tööriistade täitmise torustik
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Tööriistade kategooriad ja mustrid

### 1. **Andmetöötluse tööriistad**
- **Sisendi valideerimine**: Tugev tüüpimine koos andmeannotatsioonidega
- **Transformatsiooni operatsioonid**: Tüübikindel andmete konverteerimine ja vormindamine
- **Äriloogika**: Valdkonnaspetsiifilised arvutused ja analüüsitööriistad
- **Väljundi vormindamine**: Struktureeritud vastuste genereerimine

### 2. **Integreerimise tööriistad**
- **API ühendused**: RESTful teenuste integreerimine HttpClientiga
- **Andmebaasi tööriistad**: Entity Frameworki integreerimine andmete ligipääsuks
- **Faili operatsioonid**: Turvalised failisüsteemi operatsioonid koos valideerimisega
- **Väliste teenuste integreerimine**: Kolmandate osapoolte teenuste integreerimise mustrid

### 3. **Abitööriistad**
- **Tekstitöötlus**: Stringide manipuleerimise ja vormindamise utiliidid
- **Kuupäeva/kellaaja operatsioonid**: Kultuuriteadlikud kuupäeva/kellaaja arvutused
- **Matemaatilised tööriistad**: Täpsed arvutused ja statistilised operatsioonid
- **Valideerimise tööriistad**: Ärireeglite valideerimine ja andmete kontrollimine

## ⚙️ Eeltingimused ja seadistamine

**Arenduskeskkond:**
- .NET 9.0 SDK või uuem
- Visual Studio 2022 või VS Code koos C# laiendiga
- GitHubi mudelite API ligipääs

**Vajalikud NuGet paketid:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Keskkonna konfiguratsioon (.env fail):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Valmis looma ettevõtte tasemel agente, millel on võimsad, tüübikindlad tööriistade võimekused .NET-is? Kujundame professionaalseid lahendusi! 🏢⚡

## 💻 Koodi rakendamine

Täielik C# rakendus on saadaval kaasnevas failis `04-dotnet-agent-framework.cs`. See .NET ühe faili rakendus demonstreerib:

- Keskkonnamuutujate laadimist GitHubi mudelite konfiguratsiooniks
- Kohandatud tööriistade määratlemist C# meetodite ja atribuutidega
- AI agendi loomist tööriistade integreerimisega
- Vestluste haldamist
- Agendi päringute täitmist tööriistade käivitamisega

Näite käivitamiseks:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Või kasutades .NET CLI-d:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta arusaamatuste või valesti tõlgenduste eest, mis võivad tekkida selle tõlke kasutamise tõttu.