# 🔍 Podnikový RAG s Microsoft Foundry (.NET)

## 📋 Ciele učenia

Tento notebook demonštruje, ako vytvoriť podnikové Retrieval-Augmented Generation (RAG) systémy pomocou Microsoft Agent Framework v .NET s Microsoft Foundry. Naučíte sa vytvárať agentov pripravených na produkciu, ktorí dokážu prehľadávať dokumenty a poskytovať presné, kontextovo zamerané odpovede s podnikovou bezpečnosťou a škálovateľnosťou.

**Schopnosti podnikového RAG, ktoré si vybudujete:**
- 📚 **Dokumentová inteligencia**: Pokročilé spracovanie dokumentov s Azure AI službami
- 🔍 **Semantické vyhľadávanie**: Vysokovýkonné vektorové vyhľadávanie s podnikateľskými funkciami
- 🛡️ **Integrácia bezpečnosti**: Riadenie prístupu založené na rolách a vzory ochrany údajov
- 🏢 **Škálovateľná architektúra**: Produkčné RAG systémy s monitorovaním

## 🎯 Architektúra podnikového RAG

### Základné podnikové komponenty
- **Microsoft Foundry**: Spravovaná podniková AI platforma s bezpečnosťou a súladom
- **Persistentní agenti**: Agent s uchovávaním stavu s históriou konverzácie a správou kontextu
- **Správa vektorového úložiska**: Podnikové indexovanie a vyhľadávanie dokumentov
- **Integrácia identity**: Autentifikácia Azure AD a riadenie prístupu založené na roliach

### Výhody .NET pre podnikanie
- **Typová bezpečnosť**: Overovanie počas kompilácie pre RAG operácie a dátové štruktúry
- **Asynchrónny výkon**: Nezablokované spracovanie dokumentov a vyhľadávacie operácie
- **Správa pamäte**: Efektívne využívanie zdrojov pre veľké kolekcie dokumentov
- **Vzory integrácie**: Natívna integrácia Azure služieb s dependency injection

## 🏗️ Technická architektúra

### Pipeline podnikového RAG
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Základné .NET komponenty
- **Azure.AI.Agents.Persistent**: Správa podnikových agentov so zachovaním stavu
- **Azure.Identity**: Integrovaná autentifikácia pre bezpečný prístup ku Azure službám
- **Microsoft.Agents.AI.AzureAI**: Implementácia agentov optimalizovaná pre Azure
- **System.Linq.Async**: Vysokovýkonné asynchrónne LINQ operácie

## 🔧 Podnikové funkcie a výhody

### Bezpečnosť a súlad
- **Integrácia Azure AD**: Podnikové riadenie identity a autentifikácia
- **Prístup založený na rolách**: Jemné nastavenie oprávnení pre prístup k dokumentom a operácie
- **Ochrana údajov**: Šifrovanie v pokoji aj pri prenose pre citlivé dokumenty
- **Auditné protokolovanie**: Komplexné sledovanie aktivít pre požiadavky na súlad

### Výkon a škálovateľnosť
- **Správa pripojení**: Efektívne riadenie pripojení ku Azure službám
- **Asynchrónne spracovanie**: Nezablokované operácie pre vysokopriechodné scenáre
- **Cachingové stratégie**: Inteligentné cachovanie často používaných dokumentov
- **Load balancing**: Distribuované spracovanie pre rozsiahle nasadenia

### Manažment a monitoring
- **Kontroly stavu systému**: Zabudované monitorovanie komponentov RAG systému
- **Výkonnostné metriky**: Detailná analytika kvality vyhľadávania a časov odozvy
- **Správa chýb**: Komplexné riadenie výnimiek s politikami opakovania
- **Správa konfigurácie**: Nastavenia špecifické pre prostredie s validáciou

## ⚙️ Požiadavky a nastavenie

**Vývojové prostredie:**
- .NET 9.0 SDK alebo novšie
- Visual Studio 2022 alebo VS Code s rozšírením C#
- Azure predplatné s prístupom k Microsoft Foundry

**Vyžadované NuGet balíky:**
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
* Konfigurácia Microsoft Foundry (automaticky riešené cez Azure CLI)
* Uistite sa, že ste prihlásený do správneho Azure predplatného

## 📊 Vzory podnikového RAG

### Vzory správy dokumentov
- **Hromadný upload**: Efektívne spracovanie veľkých kolekcií dokumentov
- **Priebežné aktualizácie**: Pridávanie a úpravy dokumentov v reálnom čase
- **Verzionovanie**: Verzovanie dokumentov a sledovanie zmien
- **Správa metadát**: Bohaté atribúty dokumentov a taxonómia

### Vzory vyhľadávania a získavania
- **Hybridné vyhľadávanie**: Kombinácia semantického a kľúčového vyhľadávania pre optimálne výsledky
- **Fasetové vyhľadávanie**: Viacrozmerné filtrovanie a kategorizácia
- **Ladenie relevantnosti**: Vlastné skórovacie algoritmy pre špecifické potreby domény
- **Zoradenie výsledkov**: Pokročilé zoradenie s integráciou obchodnej logiky

### Bezpečnostné vzory
- **Bezpečnosť na úrovni dokumentu**: Jemné riadenie prístupu ku každému dokumentu
- **Klasifikácia údajov**: Automatické označovanie citlivosti a ochrana
- **Auditné stopy**: Komplexné protokolovanie všetkých RAG operácií
- **Ochrana súkromia**: Detekcia a zacenzurovanie osobných identifikovateľných informácií (PII)

## 🔒 Podnikové bezpečnostné funkcie

### Overovanie identity a autorizácia
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
- **Riadenie prístupov**: Integrácia s Azure AD pre oprávnenia používateľov a skupín
- **Umiestnenie údajov**: Geografické riadenie ukladania dát pre súlad
- **Zálohovanie a obnova**: Automatizované zálohovanie a schopnosti obnovy po havárii

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
- **Streamované spracovanie**: Spracovanie veľkých dokumentov bez problémov s pamäťou
- **Zdrojové poolovanie**: Efektívne opätovné využívanie nákladných zdrojov
- **Garbage collection**: Optimalizované vzory prideľovania pamäti
- **Správa pripojení**: Správny životný cyklus pripojení ku Azure službám

### Cachingové stratégie
- **Cache dopytov**: Cache často vykonávaných vyhľadávaní
- **Cache dokumentov**: Pamäťové cachovanie často používaných dokumentov
- **Cache indexov**: Optimalizované cachovanie vektorových indexov
- **Cache výsledkov**: Inteligentné cachovanie generovaných odpovedí

## 📊 Podnikové prípady použitia

### Riadenie znalostí
- **Firemná wiki**: Inteligentné vyhľadávanie naprieč firemnými databázami znalostí
- **Politiky a postupy**: Automatizované dodržiavanie predpisov a usmernenia
- **Výukové materiály**: Inteligentná podpora vzdelávania a rozvoja
- **Výskumné databázy**: Systémy analýzy akademických a výskumných prác

### Zákaznícka podpora
- **Znalostná báza podpory**: Automatizované odpovede zákazníckej podpory
- **Produktová dokumentácia**: Inteligentné získavanie informácií o produktoch
- **Príručky riešenia problémov**: Kontextová pomoc pri riešení problémov
- **FAQ systémy**: Dynamická tvorba FAQ z kolekcií dokumentov

### Regulatórna zhoda
- **Analýza právnych dokumentov**: Inteligencia zmlúv a právnych dokumentov
- **Monitorovanie zhody**: Automatické kontroly regulačných požiadaviek
- **Hodnotenie rizík**: Analýza a reportovanie rizík založené na dokumentoch
- **Podpora auditu**: Inteligentné vyhľadávanie dokumentov pre audity

## 🚀 Produkčné nasadenie

### Monitorovanie a pozorovateľnosť
- **Application Insights**: Detailná telemetria a monitorovanie výkonu
- **Custom Metrics**: Sledovanie a notifikácie KPI špecifických pre biznis
- **Distribuované trasovanie**: End-to-end sledovanie požiadaviek naprieč službami
- **Dashboardy zdravia**: Vizualizácia v reálnom čase stavu systému a výkonu

### Škálovateľnosť a spoľahlivosť
- **Automatické škálovanie**: Automatické prispôsobenie záťaži a výkonnostným metrikám
- **Vysoká dostupnosť**: Nasadenie na viacerých regiónoch s failover schopnosťami
- **Load testing**: Overenie výkonu pod podnikovou záťažou
- **Obnova po havárii**: Automatizované zálohovanie a obnovovacie procesy

Pripravení vybudovať podnikové RAG systémy, ktoré zvládnu citlivé dokumenty vo veľkom? Poďme navrhnúť inteligentné systémy znalostí pre podnik! 🏢📖✨

## Implementácia kódu

Kompletný funkčný príklad kódu pre túto lekciu je dostupný v `05-dotnet-agent-framework.cs`.

Na spustenie príkladu:

```bash
# Urobte skript spustiteľným (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Spustite aplikáciu .NET Single File
./05-dotnet-agent-framework.cs
```

Alebo použite priamo `dotnet run`:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kód demonštruje:

1. **Inštalácia balíkov**: Inštalácia požadovaných NuGet balíkov pre Azure AI Agents
2. **Konfigurácia prostredia**: Načítanie endpointu Microsoft Foundry a nastavení modelu
3. **Nahrávanie dokumentov**: Nahrávanie dokumentu pre RAG spracovanie
4. **Vytvorenie vektorového úložiska**: Vytvorenie vektorového úložiska pre semantické vyhľadávanie
5. **Konfigurácia agenta**: Nastavenie AI agenta s možnosťami vyhľadávania súborov
6. **Vykonávanie dotazov**: Spúšťanie dotazov voči nahranému dokumentu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->