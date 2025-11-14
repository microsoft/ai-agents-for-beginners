<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:08:15+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "cs"
}
-->
# 🔍 Enterprise RAG s Azure AI Foundry (.NET)

## 📋 Cíle učení

Tento notebook ukazuje, jak vytvořit systémy Retrieval-Augmented Generation (RAG) na podnikové úrovni pomocí Microsoft Agent Framework v .NET s Azure AI Foundry. Naučíte se vytvářet produkčně připravené agenty, kteří dokážou prohledávat dokumenty a poskytovat přesné, kontextově relevantní odpovědi s podnikovou bezpečností a škálovatelností.

**Funkce Enterprise RAG, které vytvoříte:**
- 📚 **Inteligence dokumentů**: Pokročilé zpracování dokumentů pomocí služeb Azure AI
- 🔍 **Semantické vyhledávání**: Vysoce výkonné vektorové vyhledávání s podnikovými funkcemi
- 🛡️ **Integrace bezpečnosti**: Role-based přístup a vzory ochrany dat
- 🏢 **Škálovatelná architektura**: Produkčně připravené RAG systémy s monitoringem

## 🎯 Architektura Enterprise RAG

### Klíčové podnikové komponenty
- **Azure AI Foundry**: Spravovaná podniková AI platforma s bezpečností a shodou
- **Persistentní agenti**: Stavoví agenti s historií konverzací a správou kontextu
- **Správa vektorového úložiště**: Podnikové indexování a vyhledávání dokumentů
- **Integrace identity**: Autentizace Azure AD a role-based řízení přístupu

### Výhody .NET pro podniky
- **Typová bezpečnost**: Validace operací RAG a datových struktur při kompilaci
- **Asynchronní výkon**: Nezablokované zpracování dokumentů a vyhledávací operace
- **Správa paměti**: Efektivní využití zdrojů pro velké kolekce dokumentů
- **Vzorové integrace**: Nativní integrace služeb Azure s dependency injection

## 🏗️ Technická architektura

### Pipeline Enterprise RAG
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Klíčové komponenty .NET
- **Azure.AI.Agents.Persistent**: Správa podnikových agentů s uchováním stavu
- **Azure.Identity**: Integrovaná autentizace pro bezpečný přístup ke službám Azure
- **Microsoft.Agents.AI.AzureAI**: Implementace optimalizovaného agentového frameworku pro Azure
- **System.Linq.Async**: Vysoce výkonné asynchronní operace LINQ

## 🔧 Funkce a výhody pro podniky

### Bezpečnost a shoda
- **Integrace Azure AD**: Správa podnikové identity a autentizace
- **Role-Based Access**: Jemně granulované oprávnění pro přístup k dokumentům a operacím
- **Ochrana dat**: Šifrování v klidu i při přenosu pro citlivé dokumenty
- **Auditní logování**: Komplexní sledování aktivit pro požadavky na shodu

### Výkon a škálovatelnost
- **Pooling připojení**: Efektivní správa připojení ke službám Azure
- **Asynchronní zpracování**: Nezablokované operace pro scénáře s vysokou propustností
- **Strategie ukládání do mezipaměti**: Inteligentní ukládání často přistupovaných dokumentů
- **Vyvažování zátěže**: Distribuované zpracování pro rozsáhlé nasazení

### Správa a monitoring
- **Kontroly stavu**: Vestavěný monitoring komponent systému RAG
- **Výkonové metriky**: Podrobné analýzy kvality vyhledávání a doby odezvy
- **Zpracování chyb**: Komplexní správa výjimek s politikami opakování
- **Správa konfigurace**: Nastavení specifická pro prostředí s validací

## ⚙️ Požadavky a nastavení

**Vývojové prostředí:**
- .NET 9.0 SDK nebo novější
- Visual Studio 2022 nebo VS Code s rozšířením pro C#
- Předplatné Azure s přístupem k AI Foundry

**Požadované balíčky NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Nastavení autentizace Azure:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Konfigurace prostředí:**
* Konfigurace Azure AI Foundry (automaticky zajištěna přes Azure CLI)
* Ujistěte se, že jste autentizováni k správnému předplatnému Azure

## 📊 Vzory Enterprise RAG

### Vzory správy dokumentů
- **Hromadné nahrávání**: Efektivní zpracování velkých kolekcí dokumentů
- **Inkrementální aktualizace**: Přidávání a úpravy dokumentů v reálném čase
- **Správa verzí**: Verzování dokumentů a sledování změn
- **Správa metadat**: Bohaté atributy dokumentů a taxonomie

### Vzory vyhledávání a získávání
- **Hybridní vyhledávání**: Kombinace semantického a klíčového vyhledávání pro optimální výsledky
- **Fasetové vyhledávání**: Vícedimenzionální filtrování a kategorizace
- **Ladění relevance**: Vlastní algoritmy skórování pro specifické potřeby oboru
- **Hodnocení výsledků**: Pokročilé hodnocení s integrací obchodní logiky

### Vzory bezpečnosti
- **Bezpečnost na úrovni dokumentů**: Jemně granulované řízení přístupu na úrovni dokumentů
- **Klasifikace dat**: Automatické označování citlivosti a ochrana
- **Auditní stopy**: Komplexní logování všech operací RAG
- **Ochrana soukromí**: Detekce a redakce PII

## 🔒 Funkce bezpečnosti pro podniky

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
- **Rezidence dat**: Geografická kontrola umístění dat pro shodu
- **Zálohování a obnova**: Automatizované zálohování a postupy obnovy po havárii

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
- **Pooling zdrojů**: Efektivní opětovné využití nákladných zdrojů
- **Garbage Collection**: Optimalizované vzory alokace paměti
- **Správa připojení**: Správný životní cyklus připojení ke službám Azure

### Strategie ukládání do mezipaměti
- **Ukládání dotazů**: Ukládání často prováděných vyhledávání
- **Ukládání dokumentů**: Ukládání do paměti pro často používané dokumenty
- **Ukládání indexů**: Optimalizované ukládání vektorových indexů
- **Ukládání výsledků**: Inteligentní ukládání generovaných odpovědí

## 📊 Podnikové případy použití

### Správa znalostí
- **Firemní wiki**: Inteligentní vyhledávání v interních znalostních bázích
- **Politiky a postupy**: Automatizované vedení v oblasti shody a postupů
- **Výukové materiály**: Inteligentní asistence při vzdělávání a rozvoji
- **Výzkumné databáze**: Systémy analýzy akademických a výzkumných prací

### Zákaznická podpora
- **Znalostní báze podpory**: Automatizované odpovědi zákaznické podpory
- **Dokumentace produktů**: Inteligentní vyhledávání informací o produktech
- **Průvodce řešením problémů**: Kontextová asistence při řešení problémů
- **Systémy FAQ**: Dynamické generování FAQ z kolekcí dokumentů

### Regulační shoda
- **Analýza právních dokumentů**: Inteligence smluv a právních dokumentů
- **Monitoring shody**: Automatizované ověřování regulační shody
- **Hodnocení rizik**: Analýza rizik na základě dokumentů a reportování
- **Podpora auditu**: Inteligentní vyhledávání dokumentů pro audity

## 🚀 Produkční nasazení

### Monitoring a pozorovatelnost
- **Application Insights**: Podrobná telemetrie a monitoring výkonu
- **Vlastní metriky**: Sledování a upozorňování na obchodně specifické KPI
- **Distribuované sledování**: Sledování požadavků od začátku do konce mezi službami
- **Dashboardy stavu**: Vizualizace stavu systému a výkonu v reálném čase

### Škálovatelnost a spolehlivost
- **Automatické škálování**: Automatické škálování na základě zátěže a metrik výkonu
- **Vysoká dostupnost**: Nasazení v několika regionech s možností přepnutí při selhání
- **Zátěžové testování**: Validace výkonu při podnikové zátěži
- **Obnova po havárii**: Automatizované zálohování a postupy obnovy

Připraveni vytvořit systémy RAG na podnikové úrovni, které zvládnou citlivé dokumenty ve velkém měřítku? Pojďme navrhnout inteligentní systémy znalostí pro podniky! 🏢📖✨

## Implementace kódu

Kompletní funkční ukázka kódu pro tuto lekci je dostupná v `05-dotnet-agent-framework.cs`. 

Pro spuštění příkladu:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Nebo použijte přímo `dotnet run`:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kód ukazuje:

1. **Instalace balíčků**: Instalace požadovaných balíčků NuGet pro Azure AI Agents
2. **Konfigurace prostředí**: Načítání endpointu Azure AI Foundry a nastavení modelu
3. **Nahrávání dokumentů**: Nahrávání dokumentu pro zpracování RAG
4. **Vytvoření vektorového úložiště**: Vytvoření vektorového úložiště pro semantické vyhledávání
5. **Konfigurace agenta**: Nastavení AI agenta s funkcemi vyhledávání souborů
6. **Provádění dotazů**: Spouštění dotazů na nahraný dokument

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.