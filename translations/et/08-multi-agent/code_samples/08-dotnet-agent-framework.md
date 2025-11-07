<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:20:13+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "et"
}
-->
# 🤝 Ettevõtte mitmeagendilised töövoosüsteemid (.NET)

## 📋 Õpieesmärgid

See märkmik näitab, kuidas luua keerukaid ettevõtte tasemel mitmeagendilisi süsteeme, kasutades Microsoft Agent Frameworki .NET-is koos GitHubi mudelitega. Õpid korraldama mitme spetsialiseeritud agendi koostööd struktureeritud töövoogude kaudu, kasutades .NET-i ettevõtte funktsioone tootmisvalmis lahenduste jaoks.

**Ettevõtte mitmeagendilised võimekused, mida sa lood:**
- 👥 **Agendi koostöö**: Tüübikindel agendi koordineerimine koos kompileerimisaja valideerimisega
- 🔄 **Töövoo orkestreerimine**: Deklaratiivne töövoo määratlemine .NET-i asünkroonsete mustritega
- 🎭 **Rollide spetsialiseerumine**: Tugevalt tüübitud agendi isiksused ja ekspertvaldkonnad
- 🏢 **Ettevõtte integratsioon**: Tootmisvalmis mustrid koos jälgimise ja veakäsitlusega

## ⚙️ Eeltingimused ja seadistamine

**Arenduskeskkond:**
- .NET 9.0 SDK või uuem
- Visual Studio 2022 või VS Code koos C# laiendusega
- Azure'i tellimus (püsivate agentide jaoks)

**Vajalikud NuGet paketid:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Koodi näidis

Selle õppetunni täielik töötav kood on saadaval kaasasolevas C# failis: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Näidise käivitamiseks:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Või kasutades .NET CLI-d:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Mida see näidis demonstreerib

See mitmeagendiline töövoosüsteem loob hotellireisi soovitusteenuse kahe spetsialiseeritud agendiga:

1. **FrontDesk Agent**: Reisibüroo agent, kes pakub tegevuste ja asukohtade soovitusi
2. **Concierge Agent**: Kontrollib soovitusi, et tagada autentne, mitte-turistlik kogemus

Agentide koostöö töövoos toimub järgmiselt:
- FrontDesk agent võtab vastu algse reisisoovi
- Concierge agent vaatab soovituse üle ja täiustab seda
- Töövoog edastab vastuseid reaalajas

## Põhimõisted

### Agendi koordineerimine
Näidis demonstreerib tüübikindlat agendi koordineerimist, kasutades Microsoft Agent Frameworki koos kompileerimisaja valideerimisega.

### Töövoo orkestreerimine
Kasutab deklaratiivset töövoo määratlemist .NET-i asünkroonsete mustritega, et ühendada mitu agenti torustikus.

### Reaalajas vastuste voog
Rakendab agentide vastuste reaalajas voogesitust, kasutades asünkroonseid loendeid ja sündmustepõhist arhitektuuri.

### Ettevõtte integratsioon
Näitab tootmisvalmis mustreid, sealhulgas:
- Keskkonnamuutujate konfiguratsioon
- Turvaline mandaadi haldamine
- Veakäsitlus
- Asünkroonne sündmuste töötlemine

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.