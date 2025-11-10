<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:18:26+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "cs"
}
-->
# 🤝 Podnikové systémy pracovních postupů s více agenty (.NET)

## 📋 Cíle učení

Tento notebook ukazuje, jak vytvořit sofistikované podnikové systémy s více agenty pomocí Microsoft Agent Framework v .NET s modely GitHub. Naučíte se orchestraci několika specializovaných agentů, kteří spolupracují prostřednictvím strukturovaných pracovních postupů, využívajících podnikové funkce .NET pro řešení připravená k produkci.

**Podnikové schopnosti s více agenty, které vytvoříte:**
- 👥 **Spolupráce agentů**: Typově bezpečná koordinace agentů s validací při kompilaci
- 🔄 **Orchestrace pracovních postupů**: Deklarativní definice pracovních postupů s asynchronními vzory .NET
- 🎭 **Specializace rolí**: Silně typované osobnosti agentů a oblasti odbornosti
- 🏢 **Podniková integrace**: Vzory připravené pro produkci s monitorováním a zpracováním chyb

## ⚙️ Předpoklady a nastavení

**Vývojové prostředí:**
- .NET 9.0 SDK nebo vyšší
- Visual Studio 2022 nebo VS Code s rozšířením pro C#
- Předplatné Azure (pro perzistentní agenty)

**Požadované balíčky NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Ukázka kódu

Kompletní funkční kód pro tuto lekci je dostupný v přiloženém souboru C#: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Pro spuštění ukázky:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Nebo pomocí .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Co tato ukázka demonstruje

Tento systém pracovních postupů s více agenty vytváří službu doporučení pro hotelové cestování se dvěma specializovanými agenty:

1. **Agent recepce**: Cestovní agent, který poskytuje doporučení aktivit a lokalit
2. **Agent concierge**: Přezkoumává doporučení, aby zajistil autentické, neturistické zážitky

Agenti spolupracují v pracovním postupu, kde:
- Agent recepce obdrží počáteční požadavek na cestování
- Agent concierge přezkoumá a upraví doporučení
- Pracovní postup streamuje odpovědi v reálném čase

## Klíčové koncepty

### Koordinace agentů
Ukázka demonstruje typově bezpečnou koordinaci agentů pomocí Microsoft Agent Framework s validací při kompilaci.

### Orchestrace pracovních postupů
Používá deklarativní definici pracovních postupů s asynchronními vzory .NET k propojení více agentů v pipeline.

### Streamování odpovědí
Implementuje streamování odpovědí agentů v reálném čase pomocí asynchronních enumerací a architektury řízené událostmi.

### Podniková integrace
Ukazuje vzory připravené pro produkci, včetně:
- Konfigurace proměnných prostředí
- Bezpečné správy přihlašovacích údajů
- Zpracování chyb
- Asynchronního zpracování událostí

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.