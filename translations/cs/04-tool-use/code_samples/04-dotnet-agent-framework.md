<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:27:38+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "cs"
}
-->
# 🛠️ Pokročilé použití nástrojů s modely GitHub (.NET)

## 📋 Cíle učení

Tento notebook ukazuje vzory integrace nástrojů na podnikové úrovni pomocí Microsoft Agent Framework v .NET s modely GitHub. Naučíte se vytvářet sofistikované agenty s více specializovanými nástroji, využívajícími silné typování C# a podnikové funkce .NET.

**Pokročilé schopnosti nástrojů, které si osvojíte:**
- 🔧 **Architektura více nástrojů**: Vytváření agentů s více specializovanými schopnostmi
- 🎯 **Bezpečné provádění nástrojů podle typů**: Využití validace při kompilaci v C#
- 📊 **Podnikové vzory nástrojů**: Návrh nástrojů připravených pro produkci a zpracování chyb
- 🔗 **Kompozice nástrojů**: Kombinace nástrojů pro složité obchodní procesy

## 🎯 Výhody architektury nástrojů v .NET

### Funkce podnikových nástrojů
- **Validace při kompilaci**: Silné typování zajišťuje správnost parametrů nástrojů
- **Dependency Injection**: Integrace IoC kontejneru pro správu nástrojů
- **Async/Await vzory**: Nezablokované provádění nástrojů s řádnou správou zdrojů
- **Strukturované logování**: Vestavěná integrace logování pro monitorování provádění nástrojů

### Vzory připravené pro produkci
- **Zpracování výjimek**: Komplexní správa chyb s typovanými výjimkami
- **Správa zdrojů**: Správné vzory pro uvolňování zdrojů a správu paměti
- **Monitorování výkonu**: Vestavěné metriky a ukazatele výkonu
- **Správa konfigurace**: Typově bezpečná konfigurace s validací

## 🔧 Technická architektura

### Základní komponenty nástrojů v .NET
- **Microsoft.Extensions.AI**: Jednotná abstrakční vrstva nástrojů
- **Microsoft.Agents.AI**: Orchestrace nástrojů na podnikové úrovni
- **Integrace modelů GitHub**: Vysoce výkonný API klient s poolingem připojení

### Pipeline pro provádění nástrojů
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Kategorie nástrojů a vzory

### 1. **Nástroje pro zpracování dat**
- **Validace vstupů**: Silné typování s datovými anotacemi
- **Transformační operace**: Typově bezpečná konverze a formátování dat
- **Obchodní logika**: Nástroje pro výpočty a analýzy specifické pro danou doménu
- **Formátování výstupů**: Generování strukturovaných odpovědí

### 2. **Integrační nástroje**
- **API konektory**: Integrace RESTful služeb pomocí HttpClient
- **Nástroje pro databáze**: Integrace Entity Framework pro přístup k datům
- **Operace se soubory**: Bezpečné operace se souborovým systémem s validací
- **Externí služby**: Vzory integrace služeb třetích stran

### 3. **Pomocné nástroje**
- **Zpracování textu**: Nástroje pro manipulaci a formátování řetězců
- **Operace s daty/časem**: Výpočty dat a času s ohledem na kulturní specifika
- **Matematické nástroje**: Přesné výpočty a statistické operace
- **Nástroje pro validaci**: Validace obchodních pravidel a ověřování dat

## ⚙️ Předpoklady a nastavení

**Vývojové prostředí:**
- .NET 9.0 SDK nebo vyšší
- Visual Studio 2022 nebo VS Code s rozšířením pro C#
- Přístup k API modelů GitHub

**Požadované balíčky NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurace prostředí (.env soubor):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Připraveni na tvorbu agentů na podnikové úrovni s výkonnými, typově bezpečnými schopnostmi nástrojů v .NET? Pojďme navrhnout profesionální řešení! 🏢⚡

## 💻 Implementace kódu

Kompletní implementace v C# je dostupná v doprovodném souboru `04-dotnet-agent-framework.cs`. Tato aplikace v .NET Single File App demonstruje:

- Načítání proměnných prostředí pro konfiguraci modelů GitHub
- Definování vlastních nástrojů pomocí metod C# s atributy
- Vytváření AI agenta s integrací nástrojů
- Správa konverzačních vláken
- Provádění požadavků agenta s voláním nástrojů

Pro spuštění příkladu:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Nebo pomocí .NET CLI:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.