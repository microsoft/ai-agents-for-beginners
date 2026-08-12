# 🤝 Podnikové systémy pracovních toků s více agenty (.NET)

## 📋 Výukové cíle

Tento zápisník ukazuje, jak vytvořit sofistikované podnikové systémy s více agenty pomocí Microsoft Agent Framework v .NET s Azure OpenAI (Responses API). Naučíte se orchestraci několika specializovaných agentů spolupracujících prostřednictvím strukturovaných pracovních toků a využijete podnikové funkce .NET pro řešení připravená do produkce.

**Podnikové schopnosti více agentů, které vybudujete:**
- 👥 **Spolupráce agentů**: typově bezpečná koordinace agentů s validací při překladu
- 🔄 **Orchestrace pracovních toků**: deklarativní definice pracovního toku s asynchronními vzory .NET
- 🎭 **Specializace rolí**: silně typované osobnosti agentů a domény odbornosti
- 🏢 **Podniková integrace**: vzory připravené pro produkci s monitorováním a zpracováním chyb

## ⚙️ Předpoklady a nastavení

**Vývojové prostředí:**
- .NET 9.0 SDK nebo vyšší
- Visual Studio 2022 nebo VS Code s C# rozšířením
- Azure předplatné (pro trvalé agenty)

**Požadované NuGet balíčky:**
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

## Ukázkový kód

Kompletní funkční kód této lekce je dostupný v přiloženém souboru C#: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Pro spuštění ukázky:

```bash
# Nastavte soubor jako spustitelný (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Spusťte ukázku
./08-dotnet-agent-framework.cs
```

Nebo pomocí .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Co tato ukázka demonstruje

Tento systém pracovních toků s více agenty vytváří službu doporučení hotelových cest s dvěma specializovanými agenty:

1. **FrontDesk Agent**: cestovní agent poskytující doporučení aktivit a míst
2. **Concierge Agent**: kontroluje doporučení, aby zajistil autentické, ne-turistické zážitky

Agentky spolupracují ve workflow, kde:
- Agent FrontDesk přijímá počáteční cestovní požadavek
- Agent Concierge kontroluje a zpřesňuje doporučení
- Pracovní tok streamuje odpovědi v reálném čase

## Klíčové koncepty

### Koordinace agentů
Ukázka demonstruje typově bezpečnou koordinaci agentů pomocí Microsoft Agent Framework s validací při překladu.

### Orchestrace pracovních toků
Používá deklarativní definici pracovního toku s asynchronními vzory .NET k propojení více agentů v pipeline.

### Streamování odpovědí
Realizuje streamování odpovědí agentů v reálném čase pomocí asynchronních enumerabilních a událostmi řízené architektury.

### Podniková integrace
Ukazuje vzory připravené do produkce včetně:
- Konfigurace prostředí přes proměnné prostředí
- Bezpečné správy přihlašovacích údajů
- Zpracování chyb
- Asynchronní zpracování událostí

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->