# 🤝 Podjetniški sistemi za večagentna delovna toka (.NET)

## 📋 Cilji učenja

Ta zvezek prikazuje, kako zgraditi sofisticirane večagentne sisteme podjetniške ravni z uporabo Microsoft Agent Framework v .NET z Azure OpenAI (Responses API). Naučili se boste usklajevati več specializiranih agentov, ki delujejo skupaj prek strukturiranih delovnih tokov, pri čemer boste izkoristili podjetniške zmogljivosti .NET za produkcijsko pripravljene rešitve.

**Podjetniške zmogljivosti večagentnih sistemov, ki jih boste razvili:**
- 👥 **Sodelovanje agentov**: Varnost tipov pri koordinaciji agentov z validacijo ob prevajanju
- 🔄 **Orkestracija delovnih tokov**: Deklarativna definicija delovnega toka z uporabo asinhronih vzorcev .NET
- 🎭 **Specializacija vlog**: Močno tipizirane osebnosti agentov in področja strokovnosti
- 🏢 **Podjetniška integracija**: Produkcijsko pripravljeni vzorci z nadzorom in obravnavo napak

## ⚙️ Zahteve in nastavitev

**Razvojno okolje:**
- .NET 9.0 SDK ali višja različica
- Visual Studio 2022 ali VS Code z razširitvijo za C#
- Azure naročnina (za trajne agente)

**Zahtevani NuGet paketi:**
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

## Vzorec kode

Celotna delujoča koda za to lekcijo je na voljo v pripadajoči C# datoteki: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Za zagon vzorca:

```bash
# Naredite datoteko izvršljivo (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Zaženite primer
./08-dotnet-agent-framework.cs
```

Ali z uporabo .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Kaj prikazuje ta vzorec

Ta večagentni sistem delovnega toka ustvari storitev za priporočila v hotelskem potovanju z dvema specializiranima agentoma:

1. **FrontDesk agent**: Potovalni agent, ki nudi priporočila za dejavnosti in lokacije
2. **Concierge agent**: Pregleduje priporočila za zagotavljanje pristnih, neturističnih doživetij

Agenti delujejo skupaj v delovnem toku, kjer:
- FrontDesk agent prejme začetno potovalno zahtevo
- Concierge agent pregleda in izpopolni priporočilo
- Delovni tok pretaka odgovore v realnem času

## Ključni pojmi

### Koordinacija agentov
Vzorec prikazuje varno tipizirano koordinacijo agentov z uporabo Microsoft Agent Framework z validacijo ob prevajanju.

### Orkestracija delovnih tokov
Uporablja deklarativno definicijo delovnega toka z asinhronimi vzorci .NET za povezovanje več agentov v cevovod.

### Pretakanje odgovorov
Izvaja pretakanje odgovorov agentov v realnem času z uporabo asinhronih enumerable in dogodkovno arhitekturo.

### Podjetniška integracija
Prikazuje produkcijsko pripravljene vzorce, vključno z:
- Nastavitvijo okolijskih spremenljivk
- Varno upravljanje poverilnic
- Obravo napak
- Asinhrono procesiranje dogodkov

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->