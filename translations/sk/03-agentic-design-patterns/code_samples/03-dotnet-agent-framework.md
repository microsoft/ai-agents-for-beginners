<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:51:06+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "sk"
}
-->
# 🎨 Agentické návrhové vzory s modelmi GitHub (.NET)

## 📋 Ciele učenia

Tento notebook demonštruje návrhové vzory na podnikovej úrovni pre budovanie inteligentných agentov pomocou Microsoft Agent Framework v .NET s integráciou modelov GitHub. Naučíte sa profesionálne vzory a architektonické prístupy, ktoré robia agentov pripravenými na produkciu, udržiavateľnými a škálovateľnými.

**Podnikové návrhové vzory:**
- 🏭 **Factory Pattern**: Štandardizovaná tvorba agentov s využitím dependency injection
- 🔧 **Builder Pattern**: Plynulá konfigurácia a nastavenie agentov
- 🧵 **Thread-Safe Patterns**: Správa súbežných konverzácií
- 📋 **Repository Pattern**: Organizovaná správa nástrojov a schopností

## 🎯 Architektonické výhody .NET

### Podnikové funkcie
- **Silné typovanie**: Validácia počas kompilácie a podpora IntelliSense
- **Dependency Injection**: Integrovaná podpora DI kontajnera
- **Správa konfigurácie**: Vzory IConfiguration a Options
- **Async/Await**: Prvotriedna podpora asynchrónneho programovania

### Vzory pripravené na produkciu
- **Integrácia logovania**: Podpora ILogger a štruktúrovaného logovania
- **Kontroly zdravia**: Integrované monitorovanie a diagnostika
- **Validácia konfigurácie**: Silné typovanie s anotáciami údajov
- **Správa chýb**: Štruktúrované riadenie výnimiek

## 🔧 Technická architektúra

### Základné komponenty .NET
- **Microsoft.Extensions.AI**: Zjednotené abstrakcie AI služieb
- **Microsoft.Agents.AI**: Rámec pre orchestráciu agentov na podnikovej úrovni
- **Integrácia modelov GitHub**: Vzory vysoko výkonných API klientov
- **Systém konfigurácie**: Integrácia appsettings.json a prostredia

### Implementácia návrhových vzorov
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Demonštrované podnikové vzory

### 1. **Kreačné vzory**
- **Agent Factory**: Centralizovaná tvorba agentov s konzistentnou konfiguráciou
- **Builder Pattern**: Plynulé API pre komplexnú konfiguráciu agentov
- **Singleton Pattern**: Správa zdieľaných zdrojov a konfigurácie
- **Dependency Injection**: Voľné prepojenie a testovateľnosť

### 2. **Behaviorálne vzory**
- **Strategy Pattern**: Zameniteľné stratégie vykonávania nástrojov
- **Command Pattern**: Zapuzdrené operácie agentov s možnosťou undo/redo
- **Observer Pattern**: Riadenie životného cyklu agenta na základe udalostí
- **Template Method**: Štandardizované pracovné postupy vykonávania agentov

### 3. **Štrukturálne vzory**
- **Adapter Pattern**: Vrstva integrácie API modelov GitHub
- **Decorator Pattern**: Rozšírenie schopností agenta
- **Facade Pattern**: Zjednodušené rozhrania pre interakciu s agentmi
- **Proxy Pattern**: Lazy loading a caching pre zvýšenie výkonu

## ⚙️ Predpoklady a nastavenie

**Vývojové prostredie:**
- .NET 9.0 SDK alebo vyšší
- Visual Studio 2022 alebo VS Code s rozšírením pre C#
- Prístup k API modelov GitHub

**Závislosti NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurácia (.env súbor):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 Návrhové princípy .NET

### SOLID princípy
- **Jedna zodpovednosť**: Každá komponenta má jeden jasný účel
- **Otvorené/Zatvorené**: Rozšíriteľné bez modifikácie
- **Liskovova substitúcia**: Implementácie nástrojov založené na rozhraniach
- **Segregácia rozhraní**: Zamerané, súdržné rozhrania
- **Inverzia závislostí**: Závislosť na abstrakciách, nie na konkrétnych implementáciách

### Čistá architektúra
- **Doménová vrstva**: Základné abstrakcie agentov a nástrojov
- **Aplikačná vrstva**: Orchestrácia agentov a pracovné postupy
- **Infrastruktúrna vrstva**: Integrácia modelov GitHub a externých služieb
- **Prezentačná vrstva**: Interakcia s používateľom a formátovanie odpovedí

## 🔒 Podnikové úvahy

### Bezpečnosť
- **Správa poverení**: Bezpečné spracovanie API kľúčov pomocou IConfiguration
- **Validácia vstupov**: Silné typovanie a validácia pomocou anotácií údajov
- **Sanitácia výstupov**: Bezpečné spracovanie a filtrovanie odpovedí
- **Audit logovanie**: Komplexné sledovanie operácií

### Výkon
- **Asynchrónne vzory**: Nezablokované I/O operácie
- **Pooling pripojení**: Efektívna správa HTTP klientov
- **Caching**: Ukladanie odpovedí do cache pre zlepšenie výkonu
- **Správa zdrojov**: Správne uvoľňovanie a čistenie zdrojov

### Škálovateľnosť
- **Bezpečnosť vlákien**: Podpora súbežného vykonávania agentov
- **Pooling zdrojov**: Efektívne využívanie zdrojov
- **Správa záťaže**: Obmedzovanie rýchlosti a zvládanie preťaženia
- **Monitorovanie**: Metodiky výkonu a kontroly zdravia

## 🚀 Nasadenie do produkcie

- **Správa konfigurácie**: Nastavenia špecifické pre prostredie
- **Stratégia logovania**: Štruktúrované logovanie s korelačnými ID
- **Správa chýb**: Globálne spracovanie výnimiek s vhodným zotavením
- **Monitorovanie**: Application Insights a výkonnostné počítadlá
- **Testovanie**: Jednotkové testy, integračné testy a vzory záťažového testovania

Pripravení vytvárať inteligentných agentov na podnikovej úrovni s .NET? Poďme navrhnúť niečo robustné! 🏢✨

## Ukážka kódu

Pre kompletný funkčný príklad si pozrite [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.