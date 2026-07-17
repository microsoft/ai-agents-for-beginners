# 🤝 Enterprise sustavi višestrukih agenata (.NET)

## 📋 Ciljevi učenja

Ovaj bilježnik pokazuje kako izgraditi sofisticirane višestruke sustave agenata za poduzeća koristeći Microsoft Agent Framework u .NET-u s Azure OpenAI (Responses API). Naučit ćete orkestrirati više specijaliziranih agenata koji rade zajedno kroz strukturirane tokove rada, koristeći enterprise funkcionalnosti .NET-a za proizvodna rješenja.

**Sposobnosti višestrukih agenata za poduzeća koje ćete izgraditi:**
- 👥 **Suradnja agenata**: Tip-sigurna koordinacija agenata s validacijom tijekom kompajliranja
- 🔄 **Orkestracija tokova rada**: Deklarativna definicija toka rada s async obrascima .NET-a
- 🎭 **Specijalizacija uloga**: Snažno tipizirane osobnosti agenata i domena ekspertize
- 🏢 **Integracija u poduzeće**: Proizvodno spremni obrasci s nadzorom i rukovanjem pogreškama

## ⚙️ Preduvjeti i postavljanje

**Razvojno okruženje:**
- .NET 9.0 SDK ili noviji
- Visual Studio 2022 ili VS Code s C# ekstenzijom
- Azure pretplata (za trajne agente)

**Potrebni NuGet paketi:**
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

## Primjer koda

Kompletan radni kod za ovu lekciju dostupan je u priloženoj C# datoteci: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Za pokretanje primjera:

```bash
# Napravite datoteku izvršnom (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Pokrenite primjer
./08-dotnet-agent-framework.cs
```

Ili koristeći .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Što ovaj primjer pokazuje

Ovaj sustav rada višestrukih agenata stvara uslugu preporuka za putovanja u hotel sa dva specijalizirana agenta:

1. **FrontDesk agent**: Agent za putovanja koji daje preporuke za aktivnosti i lokacije
2. **Concierge agent**: Pregledava preporuke kako bi osigurao autentična, ne-turistička iskustva

Agenti rade zajedno u toku rada gdje:
- FrontDesk agent prima početni zahtjev za putovanje
- Concierge agent pregledava i poboljšava preporuku
- Tok rada u stvarnom vremenu šalje odgovore putem streaminga

## Ključni pojmovi

### Koordinacija agenata
Primjer pokazuje tip-sigurnu koordinaciju agenata koristeći Microsoft Agent Framework s validacijom tijekom kompajliranja.

### Orkestracija tokova rada
Koristi deklarativnu definiciju tokova rada s async obrascima .NET-a za povezivanje više agenata u pipeline.

### Streaming odgovora
Implementira streaming odgovora agenata u stvarnom vremenu koristeći async enumerables i arhitekturu vođenu događajima.

### Integracija u poduzeće
Prikazuje proizvodno spremne obrasce uključujući:
- Konfiguraciju varijabli okruženja
- Sigurno upravljanje vjerodajnicama
- Rukovanje pogreškama
- Asinkrono procesiranje događaja

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->