# 🔍 Podnikový RAG s Microsoft Foundry (.NET)

## 📋 Ciele učenia

Tento zápisník ukazuje, ako vytvoriť podnikové systémy Retrieval-Augmented Generation (RAG) pomocou Microsoft Agent Framework v .NET s Microsoft Foundry. Naučíte sa vytvárať produkčné agenty, ktorí dokážu prehľadávať dokumenty a poskytovať presné, kontextovo uvedomelé odpovede s podnikových zabezpečením a škálovateľnosťou.

**Podnikové schopnosti RAG, ktoré vybudujete:**
- 📚 **Dokumentová inteligencia**: Pokročilé spracovanie dokumentov s Azure AI službami
- 🔍 **Semantické vyhľadávanie**: Vysoko výkonné vektorové vyhľadávanie s podnikateľskými funkciami
- 🛡️ **Integrácia zabezpečenia**: Prístup na základe rolí a vzory ochrany údajov
- 🏢 **Škálovateľná architektúra**: Produkčné RAG systémy s monitorovaním

## 🎯 Architektúra podnikového RAG

### Jadrá podnikových komponentov
- **Microsoft Foundry**: Riadená podniková AI platforma so zabezpečením a súladom
- **Persistentní agenti**: Stavoví agenti s históriou rozhovorov a správou kontextu
- **Správa vektorového úložiska**: Podnikové indexovanie a získavanie dokumentov
- **Integrácia identity**: Autentifikácia Azure AD a kontrola prístupu na základe rolí

### Výhody .NET pre podnik
- **Typová bezpečnosť**: Overenie počas kompilácie pre RAG operácie a dátové štruktúry
- **Asynchrónny výkon**: Nezablokujúce spracovanie dokumentov a vyhľadávacích operácií
- **Správa pamäte**: Efektívne využitie zdrojov pre veľké zbierky dokumentov
- **Integrančné vzory**: Nativná integrácia Azure služieb s dependency injection

## 🏗️ Technická architektúra

### Podniková RAG pipeline
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Jadrá .NET komponentov
- **Azure.AI.Agents.Persistent**: Podniková správa agentov s perzistenciou stavu
- **Azure.Identity**: Integrovaná autentifikácia pre bezpečný prístup k Azure službám
- **Microsoft.Agents.AI.AzureAI**: Azure-optimalizovaná implementácia agent frameworku
- **System.Linq.Async**: Vysoko výkonné asynchrónne LINQ operácie

## 🔧 Podnikové funkcie & výhody

### Zabezpečenie & súlad
- **Integrácia Azure AD**: Podnikové riadenie identít a autentifikácia
- **Prístup na základe rolí**: Detailné povolenia pre prístup a operácie s dokumentmi
- **Ochrana údajov**: Šifrovanie v pokoji aj počas prenosu pre citlivé dokumenty
- **Auditné záznamy**: Komplexné sledovanie aktivít pre požiadavky súladu

### Výkon & škálovateľnosť
- **Pooling pripojení**: Efektívna správa pripojení k Azure službám
- **Asynchrónne spracovanie**: Nezablokujúce operácie pre vysoko zaťažené scenáre
- **Caching stratégie**: Inteligentné cachovanie často pristupovaných dokumentov
- **Load balancing**: Distribuované spracovanie pre rozsiahle nasadenia

### Správa & monitorovanie
- **Health checks**: Vstavané monitorovanie komponentov RAG systému
- **Výkonnostné metriky**: Podrobné analýzy kvality vyhľadávania a časov odozvy
- **Riešenie chýb**: Komplexné spravovanie výnimiek s retry politikami
- **Správa konfigurácie**: Nastavenia špecifické pre prostredie s validáciou

## ⚙️ Predpoklady & nastavenie

**Vývojové prostredie:**
- .NET 9.0 SDK alebo vyšší
- Visual Studio 2022 alebo VS Code s rozšírením pre C#
- Azure predplatné s prístupom k Microsoft Foundry

**Povinné NuGet balíky:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Nastavenie autentifikácie Azure:**
```bash
# Nainštalujte Azure CLI a autentifikujte sa
az login
az account set --subscription "your-subscription-id"
```

**Konfigurácia prostredia:**
* Konfigurácia Microsoft Foundry (automaticky spravovaná cez Azure CLI)
* Uistite sa, že ste prihlásený do správneho Azure predplatného

## 📊 Podnikové RAG vzory

### Vzory správy dokumentov
- **Hromadné nahratie**: Efektívne spracovanie rozsiahlych zbierok dokumentov
- **Inkrementálne aktualizácie**: Pridávanie a modifikácia dokumentov v reálnom čase
- **Správa verzií**: Verzionovanie dokumentov a sledovanie zmien
- **Správa metadát**: Bohaté atribúty dokumentov a taxonómia

### Vzory vyhľadávania & získavania
- **Hybridné vyhľadávanie**: Kombinovanie semantického a kľúčového vyhľadávania pre optimálne výsledky
- **Facetové vyhľadávanie**: Viacdimenziálne filtrovanie a kategorizácia
- **Ladenie relevantnosti**: Vlastné algoritmy skórovania pre doménové potreby
- **Radenie výsledkov**: Pokročilé radenie s integráciou biznis logiky

### Zabezpečovacie vzory
- **Zabezpečenie na úrovni dokumentov**: Detailná kontrola prístupu ku každému dokumentu
- **Klasifikácia údajov**: Automatické označovanie citlivosti a ochrana
- **Auditné stopy**: Komplexné logovanie všetkých RAG operácií
- **Ochrana súkromia**: Detekcia a zakrývanie osobných identifikovateľných informácií (PII)

## 🔒 Podnikové bezpečnostné funkcie

### Autentifikácia & autorizácia
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

### Ochrana údajov
- **Šifrovanie**: End-to-end šifrovanie dokumentov a vyhľadávacích indexov
- **Kontroly prístupu**: Integrácia s Azure AD pre používateľské a skupinové oprávnenia
- **Lokalita údajov**: Geografické riadenie umiestnenia údajov pre súlad
- **Zálohovanie & obnova**: Automatizované zálohovanie a možnosti obnovy po havárii

## 📈 Optimalizácia výkonu

### Vzory asynchrónneho spracovania
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Správa pamäte
- **Streamingové spracovanie**: Spracovanie veľkých dokumentov bez problémov s pamäťou
- **Pooling zdrojov**: Efektívne opätovné použitie nákladných zdrojov
- **Garbage collection**: Optimalizované vzory prideľovania pamäte
- **Správa pripojení**: Správny životný cyklus pripojení k Azure službám

### Caching stratégie
- **Cache dopytov**: Cachovanie často vykonávaných vyhľadávaní
- **Cache dokumentov**: Cachovanie v pamäti pre často používané dokumenty
- **Cache indexov**: Optimalizované cachovanie vektorových indexov
- **Cache výsledkov**: Inteligentné cachovanie generovaných odpovedí

## 📊 Podnikové použitia

### Riadenie znalostí
- **Firemná wiki**: Inteligentné vyhľadávanie v rámci základníc znalostí spoločnosti
- **Politiky & postupy**: Automatizované usmernenia pre súlad a postupy
- **Školenia**: Inteligentná podpora učenia a rozvoja
- **Výskumné databázy**: Systémy analýzy akademických a výskumných prác

### Zákaznícka podpora
- **Znalostná báza podpory**: Automatizované odpovede zákazníkom
- **Produktová dokumentácia**: Inteligentné získavanie informácií o produktoch
- **Návody na riešenie problémov**: Kontextová pomoc pri riešení problémov
- **FAQ systémy**: Dynamická generácia FAQ z kolekcií dokumentov

### Dodržiavanie predpisov
- **Analýza právnych dokumentov**: Inteligencia zmlúv a právnych dokumentov
- **Monitorovanie súladu**: Automatizované kontroly regulačného súladu
- **Hodnotenie rizika**: Analýza rizík a reportovanie na základe dokumentov
- **Podpora auditov**: Inteligentné vyhľadávanie dokumentov pre audity

## 🚀 Nasadenie do produkcie

### Monitorovanie & pozorovateľnosť
- **Application Insights**: Podrobné telemetria a monitorovanie výkonu
- **Vlastné metriky**: Sledovanie a upozornenia na biznis špecifické KPI
- **Distribuované trasovanie**: End-to-end sledovanie požiadaviek cez služby
- **Zdravotné dashboardy**: Vizualizácia stavu systému a výkonu v reálnom čase

### Škálovateľnosť & spoľahlivosť
- **Auto-škálovanie**: Automatické škálovanie podľa zaťaženia a metrík výkonu
- **Vysoká dostupnosť**: Multi-regionálne nasadenie s failover schopnosťami
- **Load testing**: Overenie výkonu pri podnikových zaťaženiach
- **Obnova po havárii**: Automatizované zálohovanie a obnovovacie postupy

Ste pripravení vybudovať podnikové RAG systémy, ktoré zvládnu citlivé dokumenty v škálovateľnom prostredí? Poďme navrhnúť inteligentné znalostné systémy pre podnik! 🏢📖✨

## Implementácia kódu

Kompletný funkčný ukážkový kód pre túto lekciu nájdete v `05-dotnet-agent-framework.cs`. 

Na spustenie príkladu:

```bash
# Nastavte skript ako spustiteľný (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Spustite aplikáciu .NET Single File App
./05-dotnet-agent-framework.cs
```

Alebo použite priamo `dotnet run`:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kód demonštruje:

1. **Inštalácia balíčkov**: Inštalovanie požadovaných NuGet balíčkov pre Azure AI Agentov
2. **Konfigurácia prostredia**: Načítanie Microsoft Foundry endpointu a nastavení modelu
3. **Nahranie dokumentu**: Nahratie dokumentu pre RAG spracovanie
4. **Vytvorenie vektorového úložiska**: Vytvorenie vektorového úložiska pre semantické vyhľadávanie
5. **Konfigurácia agenta**: Nastavenie AI agenta s možnosťami vyhľadávania súborov
6. **Vykonanie dotazov**: Spustenie dotazov voči nahratému dokumentu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->