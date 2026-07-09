# 🔍 Podnikový RAG s Microsoft Foundry (.NET)

## 📋 Výukové cíle

Tento notebook ukazuje, jak vybudovat podnikové Retrieval-Augmented Generation (RAG) systémy pomocí Microsoft Agent Framework v .NET s Microsoft Foundry. Naučíte se vytvářet produkční agenty, kteří dokážou prohledávat dokumenty a poskytovat přesné, kontextově uvědomělé odpovědi s podnikovou bezpečností a škálovatelností.

**Podnikové schopnosti RAG, které si vybudujete:**
- 📚 **Inteligence dokumentů**: Pokročilé zpracování dokumentů pomocí služeb Azure AI
- 🔍 **Sémantické vyhledávání**: Vysoce výkonné vektorové vyhledávání s podnikovými funkcemi
- 🛡️ **Integrace bezpečnosti**: Řízení přístupu na základě rolí a vzory ochrany dat
- 🏢 **Škálovatelná architektura**: Produkční RAG systémy s monitorováním

## 🎯 Podniková architektura RAG

### Základní podnikové komponenty
- **Microsoft Foundry**: Spravovaná podniková AI platforma s bezpečností a souladem
- **Perzistentní agenti**: Stavoví agenti s historií konverzace a správou kontextu
- **Správa vektorového úložiště**: Podnikové indexování a vyhledávání dokumentů
- **Integrace identity**: Autentizace Azure AD a řízení přístupu založené na rolích

### Výhody .NET pro podnikání
- **Typová bezpečnost**: Kontrola správnosti během kompilace pro RAG operace a datové struktury
- **Asynchronní výkon**: Nezablokované zpracování dokumentů a vyhledávací operace
- **Správa paměti**: Efektivní využití zdrojů pro rozsáhlé kolekce dokumentů
- **Integrační vzory**: Nativní integrace služeb Azure s dependency injection

## 🏗️ Technická architektura

### Podnikový RAG pipeline
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Základní .NET komponenty
- **Azure.AI.Agents.Persistent**: Správa podnikových agentů s perzistencí stavu
- **Azure.Identity**: Integrovaná autentizace pro zabezpečený přístup ke službám Azure
- **Microsoft.Agents.AI.AzureAI**: Azure-optimalizovaná implementace agent frameworku
- **System.Linq.Async**: Vysoce výkonné asynchronní LINQ operace

## 🔧 Podnikové funkce a výhody

### Bezpečnost a soulad
- **Integrace Azure AD**: Podnikové řízení identity a autentizace
- **Řízení přístupu na základě rolí**: Jemně granulární oprávnění pro přístup k dokumentům a operacím
- **Ochrana dat**: Šifrování v klidu i při přenosu pro citlivé dokumenty
- **Auditní protokolování**: Komplexní sledování aktivit pro požadavky na soulad

### Výkon a škálovatelnost
- **Poolování připojení**: Efektivní správa připojení ke službám Azure
- **Asynchronní zpracování**: Nezablokované operace pro scénáře s vysokou propustností
- **Caching strategie**: Inteligentní cache pro často přistupované dokumenty
- **Vyvažování zátěže**: Distribuované zpracování pro nasazení ve velkém měřítku

### Správa a monitorování
- **Kontroly stavu**: Vestavěné monitorování komponent RAG systému
- **Výkonové metriky**: Podrobné analýzy kvality vyhledávání a doby odezvy
- **Zpracování chyb**: Komplexní správa výjimek s politikami opakování
- **Správa konfigurace**: Nastavení na míru pro prostředí s validací

## ⚙️ Předpoklady a nastavení

**Vývojové prostředí:**
- .NET 9.0 SDK nebo novější
- Visual Studio 2022 nebo VS Code s rozšířením pro C#
- Předplatné Azure s přístupem k Microsoft Foundry

**Požadované NuGet balíčky:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Nastavení autentizace Azure:**
```bash
# Nainstalujte Azure CLI a ověřte se
az login
az account set --subscription "your-subscription-id"
```

**Konfigurace prostředí:**
* Konfigurace Microsoft Foundry (automaticky řízeno přes Azure CLI)
* Ujistěte se, že jste autentizováni ke správnému Azure předplatnému

## 📊 Podnikové vzory RAG

### Vzory správy dokumentů
- **Hromadný upload**: Efektivní zpracování rozsáhlých kolekcí dokumentů
- **Přírůstkové aktualizace**: Real-time přidávání a úprava dokumentů
- **Řízení verzí**: Verzování dokumentů a sledování změn
- **Správa metadat**: Bohaté atributy dokumentů a taxonomie

### Vzory vyhledávání a získávání
- **Hybridní vyhledávání**: Kombinace sémantického a klíčového hledání pro optimální výsledky
- **Facetové vyhledávání**: Vícedimenzionální filtrování a kategorizace
- **Ladění relevance**: Vlastní skórovací algoritmy pro doménové potřeby
- **Řazení výsledků**: Pokročilé řazení s integrací obchodní logiky

### Bezpečnostní vzory
- **Bezpečnost na úrovni dokumentu**: Jemně granulární řízení přístupu k jednotlivým dokumentům
- **Klasifikace dat**: Automatické označování citlivosti a ochrana
- **Auditní stopy**: Komplexní protokolování všech RAG operací
- **Ochrana soukromí**: Detekce a zakrývání osobních údajů (PII)

## 🔒 Podnikové bezpečnostní funkce

### Autentizace a autorizace
```csharp
// Azure AD integrated authentication
var credential = new AzureCliCredential();
var agentsClient = new PersistentAgentsClient(endpoint, credential);

// Role-based access validation
if (!await ValidateUserPermissions(user, documentId))
{
    throw new UnauthorizedAccessException("Insufficient permissions");
}
```

### Ochrana dat
- **Šifrování**: End-to-end šifrování dokumentů a vyhledávacích indexů
- **Řízení přístupu**: Integrace s Azure AD pro oprávnění uživatelů a skupin
- **Umístění dat**: Geografická kontrola umístění dat pro soulad s předpisy
- **Zálohování a obnova**: Automatizované zálohování a schopnosti obnovy po havárii

## 📈 Optimalizace výkonu

### Vzory asynchronního zpracování
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Správa paměti
- **Streamové zpracování**: Zpracování velkých dokumentů bez problémů s pamětí
- **Poolování zdrojů**: Efektivní znovupoužití nákladných zdrojů
- **Garbage Collection**: Optimalizované vzory alokace paměti
- **Správa připojení**: Správný životní cyklus připojení ke službám Azure

### Caching strategie
- **Caching dotazů**: Cache často prováděných vyhledávání
- **Caching dokumentů**: Cache v paměti pro často používané dokumenty
- **Caching indexů**: Optimalizovaný caching vektorových indexů
- **Caching výsledků**: Inteligentní caching generovaných odpovědí

## 📊 Podnikové scénáře použití

### Správa znalostí
- **Firemní wiki**: Inteligentní vyhledávání napříč znalostními bázemi společnosti
- **Politiky a postupy**: Automatizované řízení souladu a navigace v postupech
- **Školící materiály**: Inteligentní podpora učení a rozvoje
- **Výzkumné databáze**: Systémy analýzy akademických a výzkumných prací

### Zákaznická podpora
- **Znalostní báze podpory**: Automatizované odpovědi zákaznického servisu
- **Dokumentace produktů**: Inteligentní vyhledávání informací o produktech
- **Průvodci řešením problémů**: Kontexutální asistence při řešení problémů
- **FAQ systémy**: Dynamická generace FAQ z kolekcí dokumentů

### Soulad s regulacemi
- **Analýza právních dokumentů**: Inteligence smluv a právních dokumentů
- **Monitorování souladu**: Automatizovaná kontrola souladu s předpisy
- **Hodnocení rizik**: Analýza rizik a reportování na základě dokumentů
- **Podpora auditů**: Inteligentní vyhledávání dokumentů pro audity

## 🚀 Nasazení do produkce

### Monitorování a dohledatelnost
- **Application Insights**: Detailní telemetrie a monitorování výkonu
- **Vlastní metriky**: Sledování a upozornění na specifické KPI podnikání
- **Distribuované trasování**: Sledování požadavků napříč službami end-to-end
- **Nástěnky zdraví systému**: Vizualizace stavu a výkonu systému v reálném čase

### Škálovatelnost a spolehlivost
- **Automatické škálování**: Automatické škálování na základě zatížení a metrik výkonu
- **Vysoká dostupnost**: Více regionální nasazení s možnostmi failoveru
- **Testování zátěže**: Validace výkonu při podnikových zatíženích
- **Obnova po havárii**: Automatizované zálohovací a obnovovací postupy

Připraveni vytvářet podnikové RAG systémy, které zvládnou citlivé dokumenty ve velkém měřítku? Pojďme navrhnout inteligentní znalostní systémy pro podnik! 🏢📖✨

## Implementace kódu

Kompletní funkční ukázka kódu k této lekci je dostupná v `05-dotnet-agent-framework.cs`.

Pro spuštění příkladu:

```bash
# Nastavte skript jako spustitelný (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Spusťte .NET aplikaci v jednom souboru
./05-dotnet-agent-framework.cs
```

Nebo použijte přímo `dotnet run`:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kód demonstruje:

1. **Instalace balíčků**: Instalace požadovaných NuGet balíčků pro Azure AI Agenty
2. **Konfigurace prostředí**: Načtení koncových bodů Microsoft Foundry a nastavení modelu
3. **Nahrání dokumentu**: Nahrání dokumentu pro RAG zpracování
4. **Vytvoření vektorového úložiště**: Vytvoření vektorového úložiště pro sémantické vyhledávání
5. **Konfigurace agenta**: Nastavení AI agenta s funkcemi vyhledávání v souborech
6. **Spuštění dotazů**: Provádění dotazů nad nahraným dokumentem

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->