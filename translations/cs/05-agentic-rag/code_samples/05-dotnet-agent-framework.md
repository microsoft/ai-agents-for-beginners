# 🔍 Podnikový RAG s Microsoft Foundry (.NET)

## 📋 Výukové cíle

Tento notebook demonstruje, jak vytvořit podnikově kvalitní systémy Retrieval-Augmented Generation (RAG) pomocí Microsoft Agent Framework v .NET s Microsoft Foundry. Naučíte se vytvářet produkčně připravené agenty, kteří dokážou prohledávat dokumenty a poskytovat přesné, kontextově uvědomělé odpovědi s podnikovou bezpečností a škálovatelností.

**Podnikové schopnosti RAG, které vytvoříte:**
- 📚 **Inteligence dokumentů**: Pokročilé zpracování dokumentů pomocí Azure AI služeb
- 🔍 **Sémantické vyhledávání**: Výkonné vektorové vyhledávání s podnikovými funkcemi
- 🛡️ **Integrace bezpečnosti**: Řízení přístupu založené na rolích a vzory ochrany dat
- 🏢 **Škálovatelná architektura**: Produkčně připravené RAG systémy s monitoringem

## 🎯 Podniková architektura RAG

### Základní podnikové komponenty
- **Microsoft Foundry**: Spravovaná podniková AI platforma s bezpečností a souladností
- **Perzistentní agenti**: Stavoví agenti s historií konverzace a správou kontextu
- **Správa vektorového úložiště**: Podnikové indexování a vyhledávání dokumentů
- **Integrace identity**: Ověřování Azure AD a řízení přístupu podle rolí

### Výhody .NET pro podnik
- **Typová bezpečnost**: Ověření při kompilaci pro RAG operace a datové struktury
- **Asynchronní výkon**: Nezablokující zpracování dokumentů a vyhledávání
- **Správa paměti**: Efektivní využití zdrojů pro rozsáhlé kolekce dokumentů
- **Vzory integrace**: Nativní integrace Azure služeb s dependency injection

## 🏗️ Technická architektura

### Podnikový RAG pipeline
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Základní .NET komponenty
- **Azure.AI.Agents.Persistent**: Podnikové řízení agentů s ukládáním stavu
- **Azure.Identity**: Integrované ověřování pro bezpečný přístup k Azure službám
- **Microsoft.Agents.AI.AzureAI**: Implementace agentního frameworku optimalizovaná pro Azure
- **System.Linq.Async**: Výkonné asynchronní LINQ operace

## 🔧 Podnikové funkce a výhody

### Bezpečnost a souladnost
- **Integrace Azure AD**: Podniková správa identity a ověřování
- **Řízení přístupu na základě rolí**: Jemnozrnné oprávnění pro přístup k dokumentům a operace
- **Ochrana dat**: Šifrování v klidu i při přenosu pro citlivé dokumenty
- **Auditní protokolování**: Kompletní sledování aktivit pro splnění požadavků na soulad

### Výkon a škálovatelnost
- **Pooling připojení**: Efektivní správa připojení k Azure službám
- **Asynchronní zpracování**: Nezablokující operace pro scénáře s vysokou propustností
- **Strategie cachování**: Inteligentní cachování často přistupovaných dokumentů
- **Load balancing**: Distribuované zpracování pro rozsáhlé nasazení

### Správa a monitoring
- **Kontroly zdraví**: Vestavěný monitoring komponent RAG systému
- **Výkonnostní metriky**: Detailní analytika kvality vyhledávání a doby odezvy
- **Zpracování chyb**: Komplexní správa výjimek s retry politikami
- **Správa konfigurace**: Nastavení specifická pro prostředí s validací

## ⚙️ Požadavky a nastavení

**Vývojové prostředí:**
- .NET 9.0 SDK nebo novější
- Visual Studio 2022 nebo VS Code s rozšířením C#
- Azure předplatné s přístupem k Microsoft Foundry

**Požadované NuGet balíčky:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Nastavení ověřování Azure:**
```bash
# Nainstalujte Azure CLI a ověřte se
az login
az account set --subscription "your-subscription-id"
```

**Konfigurace prostředí:**
* Konfigurace Microsoft Foundry (automaticky spravovaná přes Azure CLI)
* Ujistěte se, že jste přihlášeni k správnému předplatnému Azure

## 📊 Podnikové vzory RAG

### Vzory správy dokumentů
- **Hromadné nahrávání**: Efektivní zpracování rozsáhlých kolekcí dokumentů
- **Postupné aktualizace**: Přidávání a úpravy dokumentů v reálném čase
- **Správa verzí**: Verzování dokumentů a sledování změn
- **Správa metaúdajů**: Bohaté atributy dokumentů a taxonomie

### Vzory vyhledávání a zpětného získávání
- **Hybridní vyhledávání**: Kombinace sémantického a klíčového vyhledávání pro optimální výsledky
- **Facetované vyhledávání**: Mnohorozměrné filtrování a kategorizace
- **Ladění relevance**: Vlastní skóringové algoritmy pro specifické potřeby domény
- **Řazení výsledků**: Pokročilé řazení s integrací byznysové logiky

### Bezpečnostní vzory
- **Bezpečnost na úrovni dokumentů**: Jemnozrnná kontrola přístupu k jednotlivým dokumentům
- **Klasifikace dat**: Automatické označování citlivosti a ochrana
- **Auditní stopy**: Kompletní protokolování všech RAG operací
- **Ochrana soukromí**: Detekce a redakce osobních údajů (PII)

## 🔒 Podnikové bezpečnostní funkce

### Ověřování a autorizace
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
- **Šifrování**: End-to-end šifrování dokumentů a indexů vyhledávání
- **Ovládání přístupu**: Integrace s Azure AD pro oprávnění uživatelů a skupin
- **Lokalizace dat**: Řízení geografické polohy dat pro splnění regulací
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
- **Streaming zpracování**: Práce s velkými dokumenty bez problémů s pamětí
- **Pooling zdrojů**: Efektivní opakované využití nákladných zdrojů
- **Garbage collection**: Optimalizované vzory alokace paměti
- **Správa připojení**: Správný životní cyklus připojení k Azure službám

### Strategie cachování
- **Cachování dotazů**: Cache často prováděných vyhledávání
- **Cachování dokumentů**: In-memory cache pro často používané dokumenty
- **Cachování indexu**: Optimalizované cachování vektorového indexu
- **Cachování výsledků**: Inteligentní cachování generovaných odpovědí

## 📊 Podnikové scénáře použití

### Správa znalostí
- **Firemní wiki**: Inteligentní vyhledávání napříč firemními znalostními bázemi
- **Politiky a postupy**: Automatizovaná podpora dodržování zásad a postupů
- **Školící materiály**: Inteligentní podpora učení a rozvoje
- **Výzkumné databáze**: Systémy analýzy akademických a výzkumných dokumentů

### Zákaznická podpora
- **Znalostní báze podpory**: Automatizované odpovědi zákaznického servisu
- **Produktová dokumentace**: Inteligentní vyhledávání informací o produktu
- **Průvodci řešením problémů**: Kontextuální asistence při řešení problémů
- **FAQ systémy**: Dynamické generování FAQ z kolekcí dokumentů

### Soulad s regulacemi
- **Analýza právních dokumentů**: Inteligence smluv a právních dokumentů
- **Monitorování souladu**: Automatizované kontroly souladu s předpisy
- **Hodnocení rizik**: Analýza rizik a reportování na základě dokumentů
- **Podpora auditů**: Inteligentní objevování dokumentů pro audity

## 🚀 Produkční nasazení

### Monitoring a observabilita
- **Application Insights**: Detailní telemetrie a monitoring výkonu
- **Vlastní metriky**: Sledování a upozornění na byznysově specifické KPI
- **Distribuované trasování**: End-to-end sledování požadavků napříč službami
- **Dashboardy zdraví**: Vizualizace zdraví a výkonu systému v reálném čase

### Škálovatelnost a spolehlivost
- **Auto-scaling**: Automatické škálování podle zatížení a metrik výkonu
- **Vysoká dostupnost**: Nasazení ve více regionech s failover funkcemi
- **Load testing**: Validace výkonu při podnikovém zatížení
- **Obnova po havárii**: Automatizované zálohování a postupy obnovy

Připraveni vytvářet podnikově kvalitní RAG systémy, které zvládnou citlivé dokumenty ve velkém měřítku? Navrhněme inteligentní znalostní systémy pro podnik! 🏢📖✨

## Implementace kódu

Kompletní fungující ukázkový kód k této lekci je dostupný v `05-dotnet-agent-framework.cs`. 

Pro spuštění příkladu:

```bash
# Umožněte spuštění skriptu (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Spusťte .NET Single File aplikaci
./05-dotnet-agent-framework.cs
```

Nebo použijte přímo `dotnet run`:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kód demonstruje:

1. **Instalaci balíčků**: Instalace požadovaných NuGet balíčků pro Azure AI Agenty
2. **Konfiguraci prostředí**: Načtení Microsoft Foundry endpointů a nastavení modelu
3. **Nahrání dokumentu**: Nahrání dokumentu pro RAG zpracování
4. **Vytvoření vektorového úložiště**: Vytvoření vektorového úložiště pro sémantické vyhledávání
5. **Konfiguraci agenta**: Nastavení AI agenta s možností hledání ve souborech
6. **Spuštění dotazů**: Provádění dotazů nad nahraným dokumentem

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->