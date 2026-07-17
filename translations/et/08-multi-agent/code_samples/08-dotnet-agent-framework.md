# 🤝 Ettevõtte mitmeagendi töövoosüsteemid (.NET)

## 📋 Õpieesmärgid

See märkmik näitab, kuidas luua keerukaid ettevõtte tasemel mitmeagendi süsteeme, kasutades Microsoft Agent Frameworki .NET-is koos Azure OpenAI-ga (Responses API). Õpid, kuidas koordineerida mitut spetsialiseerunud agenti, kes töötavad koos struktureeritud töövoogude kaudu, kasutades .NET-i ettevõtte funktsioone tootmisvalmis lahenduste loomisel.

**Ettevõtte mitmeagendi võimekused, mida sa ehitad:**
- 👥 **Agentide koostöö**: Tüübikindel agentide koordineerimine koos kompileerimisaegse valideerimisega
- 🔄 **Töövoo orkestreerimine**: Deklaratiivne töövoo määratlus .NET-i asünkroonsete mustritega
- 🎭 **Rollide spetsialiseerumine**: Tugevalt tüübistatavad agentide isiksused ja eksperdivaldkonnad
- 🏢 **Ettevõtte integratsioon**: Tootmisvalmis mustrid koos monitooringu ja veahaldusega

## ⚙️ Eeldused & Seadistamine

**Arenduskeskkond:**
- .NET 9.0 SDK või uuem
- Visual Studio 2022 või VS Code koos C# laiendusega
- Azure tellimus (püsivate agentide jaoks)

**Nõutavad NuGet paketid:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## Koodi näide

Selle õppetüki täielik tööversioon on saadaval kaasasolevas C# failis: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Näidise käivitamiseks:

```bash
# Tehke fail täidetavaks (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Käivitage näidis
./08-dotnet-agent-framework.cs
```

Või kasutades .NET CLI-d:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Mida see näide demonstreerib

See mitmeagendi töövoosüsteem loob hotellireisi soovitusteenuse kahe spetsialiseerunud agendiga:

1. **FrontDesk Agent**: reisibüroo esindaja, kes annab soovitusi tegevuste ja asukohtade kohta
2. **Concierge Agent**: vaatab soovitused üle, et tagada autentne ja mitte-turistlik kogemus

Agendid töötavad koostöös töövoos, kus:
- FrontDesk agent saab algse reisipäringu
- Concierge agent vaatab soovituse üle ja täiustab seda
- Töövoog edastab vastused reaalajas

## Põhimõisted

### Agentide koordineerimine
Näide demonstreerib tüübikindlat agentide koordineerimist Microsoft Agent Frameworki abil koos kompileerimisaegse valideerimisega.

### Töövoo orkestreerimine
Kasutab deklaratiivset töövoo määratlust koos .NET-i asünkroonsete mustritega, et ühendada mitu agenti jadasse.

### Vastuste voogedastus
Rakendab agendi vastuste reaalajas voogedastust kasutades asünkroonseid loendeid ja sündmustepõhist arhitektuuri.

### Ettevõtte integratsioon
Kuvab tootmisvalmis mustrid, sealhulgas:
- Keskkonnamuutujate konfiguratsioon
- Turvaline volituste haldus
- Veahaldus
- Asünkroonne sündmuste töötlemine

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->