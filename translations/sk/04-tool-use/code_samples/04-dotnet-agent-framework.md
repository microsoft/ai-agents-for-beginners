<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:27:50+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "sk"
}
-->
# 🛠️ Pokročilé používanie nástrojov s GitHub modelmi (.NET)

## 📋 Ciele učenia

Tento notebook demonštruje vzory integrácie nástrojov na podnikovej úrovni pomocou Microsoft Agent Framework v .NET s GitHub modelmi. Naučíte sa vytvárať sofistikovaných agentov s viacerými špecializovanými nástrojmi, využívajúc silné typovanie C# a podnikové funkcie .NET.

**Pokročilé schopnosti nástrojov, ktoré zvládnete:**
- 🔧 **Architektúra viacerých nástrojov**: Vytváranie agentov s viacerými špecializovanými schopnosťami
- 🎯 **Typovo bezpečné vykonávanie nástrojov**: Využívanie validácie počas kompilácie v C#
- 📊 **Vzory podnikových nástrojov**: Návrh nástrojov pripravených na produkciu a spracovanie chýb
- 🔗 **Kompozícia nástrojov**: Kombinovanie nástrojov pre komplexné obchodné procesy

## 🎯 Výhody architektúry nástrojov v .NET

### Funkcie podnikových nástrojov
- **Validácia počas kompilácie**: Silné typovanie zaručuje správnosť parametrov nástrojov
- **Dependency Injection**: Integrácia IoC kontajnera na správu nástrojov
- **Async/Await vzory**: Nezablokované vykonávanie nástrojov s riadením zdrojov
- **Štruktúrované logovanie**: Integrované logovanie na monitorovanie vykonávania nástrojov

### Vzory pripravené na produkciu
- **Spracovanie výnimiek**: Komplexné spracovanie chýb s typovanými výnimkami
- **Riadenie zdrojov**: Správne vzory likvidácie a správa pamäte
- **Monitorovanie výkonu**: Integrované metriky a ukazovatele výkonu
- **Správa konfigurácie**: Typovo bezpečná konfigurácia s validáciou

## 🔧 Technická architektúra

### Základné komponenty nástrojov v .NET
- **Microsoft.Extensions.AI**: Jednotná vrstva abstrakcie nástrojov
- **Microsoft.Agents.AI**: Orchestrácia nástrojov na podnikovej úrovni
- **Integrácia GitHub modelov**: Vysoko výkonný API klient s poolingom pripojení

### Pipeline vykonávania nástrojov
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Kategórie nástrojov a vzory

### 1. **Nástroje na spracovanie dát**
- **Validácia vstupov**: Silné typovanie s anotáciami dát
- **Transformačné operácie**: Typovo bezpečná konverzia a formátovanie dát
- **Obchodná logika**: Nástroje na výpočty a analýzy špecifické pre doménu
- **Formátovanie výstupov**: Generovanie štruktúrovaných odpovedí

### 2. **Integračné nástroje**
- **API konektory**: Integrácia RESTful služieb pomocou HttpClient
- **Nástroje pre databázy**: Integrácia Entity Framework pre prístup k dátam
- **Operácie so súbormi**: Bezpečné operácie so súborovým systémom s validáciou
- **Externé služby**: Vzory integrácie služieb tretích strán

### 3. **Pomocné nástroje**
- **Spracovanie textu**: Manipulácia a formátovanie reťazcov
- **Operácie s dátumom/časom**: Výpočty dátumu/času s ohľadom na kultúru
- **Matematické nástroje**: Presné výpočty a štatistické operácie
- **Nástroje na validáciu**: Validácia obchodných pravidiel a overovanie dát

## ⚙️ Predpoklady a nastavenie

**Vývojové prostredie:**
- .NET 9.0 SDK alebo vyšší
- Visual Studio 2022 alebo VS Code s rozšírením pre C#
- Prístup k GitHub Models API

**Požadované NuGet balíčky:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurácia prostredia (.env súbor):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Pripravení na vytváranie agentov na podnikovej úrovni s výkonnými, typovo bezpečnými schopnosťami nástrojov v .NET? Poďme navrhnúť profesionálne riešenia! 🏢⚡

## 💻 Implementácia kódu

Kompletná implementácia v C# je dostupná v sprievodnom súbore `04-dotnet-agent-framework.cs`. Táto .NET aplikácia v jednom súbore demonštruje:

- Načítanie premenných prostredia pre konfiguráciu GitHub Models
- Definovanie vlastných nástrojov pomocou metód C# s atribútmi
- Vytvorenie AI agenta s integráciou nástrojov
- Správa konverzačných vlákien
- Vykonávanie požiadaviek agenta s volaním nástrojov

Na spustenie príkladu:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Alebo pomocou .NET CLI:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.