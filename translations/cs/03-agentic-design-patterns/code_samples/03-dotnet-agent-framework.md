<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:50:52+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "cs"
}
-->
# 🎨 Agentické návrhové vzory s GitHub modely (.NET)

## 📋 Cíle učení

Tento notebook demonstruje návrhové vzory na podnikové úrovni pro vytváření inteligentních agentů pomocí Microsoft Agent Framework v .NET s integrací GitHub modelů. Naučíte se profesionální vzory a architektonické přístupy, které činí agenty připravené pro produkci, snadno udržovatelné a škálovatelné.

**Podnikové návrhové vzory:**
- 🏭 **Factory Pattern**: Standardizované vytváření agentů s injekcí závislostí
- 🔧 **Builder Pattern**: Plynulá konfigurace a nastavení agentů
- 🧵 **Thread-Safe Patterns**: Správa konverzací při současném zpracování
- 📋 **Repository Pattern**: Organizovaná správa nástrojů a schopností

## 🎯 Architektonické výhody specifické pro .NET

### Podnikové funkce
- **Silné typování**: Validace při kompilaci a podpora IntelliSense
- **Injekce závislostí**: Integrovaná podpora DI kontejneru
- **Správa konfigurace**: Vzory IConfiguration a Options
- **Async/Await**: Prvotřídní podpora asynchronního programování

### Vzory připravené pro produkci
- **Integrace logování**: Podpora ILogger a strukturovaného logování
- **Kontroly stavu**: Integrované monitorování a diagnostika
- **Validace konfigurace**: Silné typování s datovými anotacemi
- **Zpracování chyb**: Strukturovaná správa výjimek

## 🔧 Technická architektura

### Základní komponenty .NET
- **Microsoft.Extensions.AI**: Jednotné abstrakce AI služeb
- **Microsoft.Agents.AI**: Rámec pro orchestraci podnikových agentů
- **Integrace GitHub modelů**: Vzory klientů API s vysokým výkonem
- **Systém konfigurace**: Integrace appsettings.json a prostředí

### Implementace návrhových vzorů
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Demonstrované podnikové vzory

### 1. **Konstrukční vzory**
- **Agent Factory**: Centralizované vytváření agentů s konzistentní konfigurací
- **Builder Pattern**: Plynulé API pro komplexní konfiguraci agentů
- **Singleton Pattern**: Sdílené zdroje a správa konfigurace
- **Injekce závislostí**: Volné propojení a testovatelnost

### 2. **Behaviorální vzory**
- **Strategy Pattern**: Zaměnitelné strategie provádění nástrojů
- **Command Pattern**: Zapouzdřené operace agentů s možností vrácení zpět
- **Observer Pattern**: Správa životního cyklu agentů řízená událostmi
- **Template Method**: Standardizované pracovní postupy agentů

### 3. **Strukturální vzory**
- **Adapter Pattern**: Integrace API GitHub modelů
- **Decorator Pattern**: Rozšíření schopností agentů
- **Facade Pattern**: Zjednodušené rozhraní pro interakci s agenty
- **Proxy Pattern**: Lazy loading a caching pro výkon

## ⚙️ Předpoklady a nastavení

**Vývojové prostředí:**
- .NET 9.0 SDK nebo vyšší
- Visual Studio 2022 nebo VS Code s rozšířením C#
- Přístup k API GitHub modelů

**NuGet závislosti:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurace (.env soubor):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 Návrhové principy .NET

### SOLID principy
- **Jednoduchá odpovědnost**: Každá komponenta má jeden jasný účel
- **Otevřenost/Zavřenost**: Rozšiřitelnost bez modifikace
- **Liskov substituce**: Implementace nástrojů založené na rozhraní
- **Segregace rozhraní**: Zaměřená, soudržná rozhraní
- **Inverze závislostí**: Závislost na abstrakcích, ne na konkrétních implementacích

### Čistá architektura
- **Doménová vrstva**: Základní abstrakce agentů a nástrojů
- **Aplikační vrstva**: Orchestrace agentů a pracovní postupy
- **Infrastrukturní vrstva**: Integrace GitHub modelů a externích služeb
- **Prezentační vrstva**: Interakce s uživatelem a formátování odpovědí

## 🔒 Podnikové úvahy

### Bezpečnost
- **Správa přihlašovacích údajů**: Bezpečné zacházení s API klíči pomocí IConfiguration
- **Validace vstupů**: Silné typování a validace datovými anotacemi
- **Sanitace výstupů**: Bezpečné zpracování a filtrování odpovědí
- **Audit logování**: Komplexní sledování operací

### Výkon
- **Asynchronní vzory**: Neblokující I/O operace
- **Pooling připojení**: Efektivní správa HTTP klientů
- **Caching**: Ukládání odpovědí pro zlepšení výkonu
- **Správa zdrojů**: Správná likvidace a vzory čištění

### Škálovatelnost
- **Bezpečnost vláken**: Podpora současného provádění agentů
- **Pooling zdrojů**: Efektivní využití zdrojů
- **Správa zátěže**: Omezení rychlosti a zvládání přetížení
- **Monitorování**: Metriky výkonu a kontroly stavu

## 🚀 Nasazení do produkce

- **Správa konfigurace**: Nastavení specifická pro prostředí
- **Strategie logování**: Strukturované logování s korelačními ID
- **Zpracování chyb**: Globální správa výjimek s odpovídajícím zotavením
- **Monitorování**: Application Insights a výkonové čítače
- **Testování**: Jednotkové testy, integrační testy a vzory zátěžového testování

Připraveni vytvořit inteligentní agenty na podnikové úrovni s .NET? Pojďme navrhnout něco robustního! 🏢✨

## Ukázka kódu

Pro kompletní funkční příklad viz [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.