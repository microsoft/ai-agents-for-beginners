<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:19:22+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "sl"
}
-->
# 🤝 Sistemi za večagentne delovne tokove za podjetja (.NET)

## 📋 Cilji učenja

Ta zvezek prikazuje, kako zgraditi napredne večagentne sisteme na ravni podjetja z uporabo Microsoft Agent Framework v .NET in GitHub modelov. Naučili se boste orkestrirati več specializiranih agentov, ki sodelujejo prek strukturiranih delovnih tokov, pri čemer boste izkoristili funkcije .NET za rešitve, pripravljene za produkcijo.

**Zmožnosti večagentnih sistemov za podjetja, ki jih boste razvili:**
- 👥 **Sodelovanje agentov**: Tipno varna koordinacija agentov z validacijo ob času prevajanja
- 🔄 **Orkestracija delovnih tokov**: Deklarativna definicija delovnih tokov z asinhronimi vzorci .NET
- 🎭 **Specializacija vlog**: Močno tipizirane osebnosti agentov in področja strokovnosti
- 🏢 **Integracija v podjetje**: Vzorci, pripravljeni za produkcijo, z nadzorom in obravnavo napak

## ⚙️ Predpogoji in nastavitev

**Razvojno okolje:**
- .NET 9.0 SDK ali novejši
- Visual Studio 2022 ali VS Code z razširitvijo za C#
- Azure naročnina (za trajne agente)

**Potrebni NuGet paketi:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Vzorec kode

Celotna delujoča koda za to lekcijo je na voljo v priloženi datoteki C#: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Za zagon vzorca:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Ali z uporabo .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Kaj prikazuje ta vzorec

Ta sistem za večagentne delovne tokove ustvarja storitev priporočil za hotelska potovanja z dvema specializiranima agentoma:

1. **Agent FrontDesk**: Potovalni agent, ki ponuja priporočila za aktivnosti in lokacije
2. **Agent Concierge**: Pregleduje priporočila, da zagotovi pristne, ne-turistične izkušnje

Agenti sodelujejo v delovnem toku, kjer:
- Agent FrontDesk prejme začetno zahtevo za potovanje
- Agent Concierge pregleda in izpopolni priporočilo
- Delovni tok v realnem času pretaka odgovore

## Ključni koncepti

### Koordinacija agentov
Vzorec prikazuje tipno varno koordinacijo agentov z uporabo Microsoft Agent Framework z validacijo ob času prevajanja.

### Orkestracija delovnih tokov
Uporablja deklarativno definicijo delovnih tokov z asinhronimi vzorci .NET za povezovanje več agentov v cevovod.

### Pretakanje odgovorov
Izvaja pretakanje odgovorov agentov v realnem času z uporabo asinhronih enumerabilnih in dogodkovno usmerjene arhitekture.

### Integracija v podjetje
Prikazuje vzorce, pripravljene za produkcijo, vključno z:
- Konfiguracijo okolijskih spremenljivk
- Varnim upravljanjem poverilnic
- Obravnava napak
- Asinhrona obdelava dogodkov

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.