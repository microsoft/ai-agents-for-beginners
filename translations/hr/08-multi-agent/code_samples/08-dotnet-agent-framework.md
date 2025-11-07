<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:19:13+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "hr"
}
-->
# 🤝 Enterprise sustavi za rad s više agenata (.NET)

## 📋 Ciljevi učenja

Ovaj priručnik pokazuje kako izgraditi sofisticirane sustave za rad s više agenata na razini poduzeća koristeći Microsoft Agent Framework u .NET-u s GitHub modelima. Naučit ćete orkestrirati rad više specijaliziranih agenata koji surađuju kroz strukturirane tijekove rada, koristeći značajke .NET-a za rješenja spremna za proizvodnju.

**Sposobnosti sustava za rad s više agenata koje ćete izgraditi:**
- 👥 **Suradnja agenata**: Sigurna koordinacija agenata s provjerom u vrijeme kompajliranja
- 🔄 **Orkestracija tijeka rada**: Deklarativno definiranje tijeka rada uz asinkrone obrasce .NET-a
- 🎭 **Specijalizacija uloga**: Strogo tipizirane osobnosti agenata i područja stručnosti
- 🏢 **Integracija u poduzeće**: Obrasci spremni za proizvodnju s praćenjem i rukovanjem greškama

## ⚙️ Preduvjeti i postavljanje

**Razvojno okruženje:**
- .NET 9.0 SDK ili noviji
- Visual Studio 2022 ili VS Code s C# ekstenzijom
- Azure pretplata (za trajne agente)

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

## Primjer koda

Kompletan radni kod za ovu lekciju dostupan je u pratećoj C# datoteci: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Za pokretanje primjera:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Ili koristeći .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Što ovaj primjer pokazuje

Ovaj sustav za rad s više agenata stvara uslugu preporuka za hotelska putovanja s dva specijalizirana agenta:

1. **Agent recepcije**: Putnički agent koji pruža preporuke za aktivnosti i lokacije
2. **Agent conciergea**: Pregledava preporuke kako bi osigurao autentična, neturistička iskustva

Agenti surađuju u tijeku rada gdje:
- Agent recepcije prima početni zahtjev za putovanje
- Agent conciergea pregledava i poboljšava preporuku
- Tijek rada prenosi odgovore u stvarnom vremenu

## Ključni koncepti

### Koordinacija agenata
Primjer pokazuje sigurnu koordinaciju agenata koristeći Microsoft Agent Framework s provjerom u vrijeme kompajliranja.

### Orkestracija tijeka rada
Koristi deklarativno definiranje tijeka rada uz asinkrone obrasce .NET-a za povezivanje više agenata u cjevovod.

### Prijenos odgovora
Implementira prijenos odgovora agenata u stvarnom vremenu koristeći asinkrone enumeracije i arhitekturu temeljenu na događajima.

### Integracija u poduzeće
Prikazuje obrasce spremne za proizvodnju, uključujući:
- Konfiguraciju varijabli okruženja
- Sigurno upravljanje vjerodajnicama
- Rukovanje greškama
- Asinkronu obradu događaja

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.