<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:08:36+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "sk"
}
-->
# 🔍 Enterprise RAG s Azure AI Foundry (.NET)

## 📋 Ciele učenia

Tento notebook demonštruje, ako vytvoriť podnikové systémy Retrieval-Augmented Generation (RAG) pomocou Microsoft Agent Framework v .NET s Azure AI Foundry. Naučíte sa vytvárať produkčne pripravených agentov, ktorí dokážu vyhľadávať v dokumentoch a poskytovať presné odpovede s kontextom, pričom zabezpečia podnikové bezpečnostné a škálovateľné riešenia.

**Podnikové schopnosti RAG, ktoré sa naučíte:**
- 📚 **Inteligencia dokumentov**: Pokročilé spracovanie dokumentov pomocou služieb Azure AI
- 🔍 **Semantické vyhľadávanie**: Výkonné vektorové vyhľadávanie s podnikovými funkciami
- 🛡️ **Integrácia bezpečnosti**: Riadenie prístupu na základe rolí a vzory ochrany údajov
- 🏢 **Škálovateľná architektúra**: Produkčne pripravené systémy RAG s monitorovaním

## 🎯 Architektúra Enterprise RAG

### Hlavné podnikové komponenty
- **Azure AI Foundry**: Spravovaná podniková AI platforma s bezpečnosťou a súladom
- **Persistentní agenti**: Stavoví agenti s históriou konverzácií a správou kontextu
- **Správa vektorového úložiska**: Podnikové indexovanie a vyhľadávanie dokumentov
- **Integrácia identity**: Autentifikácia Azure AD a riadenie prístupu na základe rolí

### Výhody .NET pre podniky
- **Typová bezpečnosť**: Validácia operácií RAG a dátových štruktúr počas kompilácie
- **Asynchrónny výkon**: Nezablokované spracovanie dokumentov a vyhľadávacie operácie
- **Správa pamäte**: Efektívne využívanie zdrojov pre veľké kolekcie dokumentov
- **Vzory integrácie**: Natívna integrácia služieb Azure s injekciou závislostí

## 🏗️ Technická architektúra

### Pipeline Enterprise RAG
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Hlavné komponenty .NET
- **Azure.AI.Agents.Persistent**: Správa podnikových agentov s uchovaním stavu
- **Azure.Identity**: Integrovaná autentifikácia pre bezpečný prístup k službám Azure
- **Microsoft.Agents.AI.AzureAI**: Implementácia optimalizovaného agentového rámca pre Azure
- **System.Linq.Async**: Výkonné asynchrónne operácie LINQ

## 🔧 Podnikové funkcie a výhody

### Bezpečnosť a súlad
- **Integrácia Azure AD**: Správa podnikovej identity a autentifikácie
- **Riadenie prístupu na základe rolí**: Jemne zrnité povolenia pre prístup k dokumentom a operáciám
- **Ochrana údajov**: Šifrovanie v pokoji a počas prenosu pre citlivé dokumenty
- **Auditné logovanie**: Komplexné sledovanie aktivít pre požiadavky na súlad

### Výkon a škálovateľnosť
- **Pooling pripojení**: Efektívna správa pripojení k službám Azure
- **Asynchrónne spracovanie**: Nezablokované operácie pre scenáre s vysokou priepustnosťou
- **Stratégie cache**: Inteligentné cache pre často prístupné dokumenty
- **Vyvažovanie záťaže**: Distribuované spracovanie pre veľké nasadenia

### Správa a monitorovanie
- **Kontroly zdravia**: Vstavané monitorovanie komponentov systému RAG
- **Výkonnostné metriky**: Podrobné analýzy kvality vyhľadávania a časov odozvy
- **Správa chýb**: Komplexné riadenie výnimiek s politikami opakovania
- **Správa konfigurácie**: Nastavenia špecifické pre prostredie s validáciou

## ⚙️ Predpoklady a nastavenie

**Vývojové prostredie:**
- .NET 9.0 SDK alebo vyšší
- Visual Studio 2022 alebo VS Code s rozšírením C#
- Predplatné Azure s prístupom k AI Foundry

**Požadované balíčky NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Nastavenie autentifikácie Azure:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Konfigurácia prostredia:**
* Konfigurácia Azure AI Foundry (automaticky spracovaná cez Azure CLI)
* Uistite sa, že ste autentifikovaní k správnemu predplatnému Azure

## 📊 Vzory Enterprise RAG

### Vzory správy dokumentov
- **Hromadné nahrávanie**: Efektívne spracovanie veľkých kolekcií dokumentov
- **Inkrementálne aktualizácie**: Pridávanie a úprava dokumentov v reálnom čase
- **Riadenie verzií**: Verziovanie dokumentov a sledovanie zmien
- **Správa metadát**: Bohaté atribúty dokumentov a taxonómia

### Vzory vyhľadávania a získavania
- **Hybridné vyhľadávanie**: Kombinácia semantického a kľúčového vyhľadávania pre optimálne výsledky
- **Fasetové vyhľadávanie**: Viacdimenzionálne filtrovanie a kategorizácia
- **Ladenie relevantnosti**: Vlastné algoritmy skórovania pre špecifické potreby domény
- **Hodnotenie výsledkov**: Pokročilé hodnotenie s integráciou obchodnej logiky

### Vzory bezpečnosti
- **Bezpečnosť na úrovni dokumentov**: Jemne zrnitá kontrola prístupu na dokument
- **Klasifikácia údajov**: Automatické označovanie citlivosti a ochrana
- **Auditné stopy**: Komplexné logovanie všetkých operácií RAG
- **Ochrana súkromia**: Detekcia a redakcia PII

## 🔒 Funkcie podnikovej bezpečnosti

### Autentifikácia a autorizácia
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
- **Kontroly prístupu**: Integrácia s Azure AD pre povolenia používateľov a skupín
- **Rezidencia údajov**: Geografické kontroly umiestnenia údajov pre súlad
- **Zálohovanie a obnova**: Automatizované zálohovanie a postupy obnovy po havárii

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
- **Streamové spracovanie**: Spracovanie veľkých dokumentov bez problémov s pamäťou
- **Pooling zdrojov**: Efektívne opätovné použitie nákladných zdrojov
- **Zber odpadu**: Optimalizované vzory alokácie pamäte
- **Správa pripojení**: Správny životný cyklus pripojení k službám Azure

### Stratégie cache
- **Cache dotazov**: Cache často vykonávaných vyhľadávaní
- **Cache dokumentov**: Cache v pamäti pre často používané dokumenty
- **Cache indexov**: Optimalizovaná cache vektorových indexov
- **Cache výsledkov**: Inteligentná cache generovaných odpovedí

## 📊 Podnikové prípady použitia

### Správa znalostí
- **Firemná wiki**: Inteligentné vyhľadávanie v znalostných databázach spoločnosti
- **Politiky a postupy**: Automatizované usmernenia pre súlad a postupy
- **Školiace materiály**: Inteligentná pomoc pri vzdelávaní a rozvoji
- **Výskumné databázy**: Systémy analýzy akademických a výskumných prác

### Zákaznícka podpora
- **Znalostná databáza podpory**: Automatizované odpovede zákazníckej podpory
- **Dokumentácia produktov**: Inteligentné získavanie informácií o produktoch
- **Príručky na riešenie problémov**: Kontextová pomoc pri riešení problémov
- **Systémy FAQ**: Dynamická generácia FAQ z kolekcií dokumentov

### Regulačný súlad
- **Analýza právnych dokumentov**: Inteligencia zmlúv a právnych dokumentov
- **Monitorovanie súladu**: Automatizované kontroly regulačného súladu
- **Hodnotenie rizík**: Analýza rizík na základe dokumentov a reportovanie
- **Podpora auditu**: Inteligentné vyhľadávanie dokumentov pre audity

## 🚀 Produkčné nasadenie

### Monitorovanie a pozorovateľnosť
- **Application Insights**: Podrobné telemetrie a monitorovanie výkonu
- **Vlastné metriky**: Sledovanie a upozorňovanie na obchodné KPI
- **Distribuované sledovanie**: Sledovanie požiadaviek od začiatku do konca medzi službami
- **Dashboardy zdravia**: Vizualizácia zdravia systému a výkonu v reálnom čase

### Škálovateľnosť a spoľahlivosť
- **Automatické škálovanie**: Automatické škálovanie na základe záťaže a výkonnostných metrík
- **Vysoká dostupnosť**: Nasadenie vo viacerých regiónoch s možnosťou preklopenia
- **Testovanie záťaže**: Validácia výkonu pod podnikovou záťažou
- **Obnova po havárii**: Automatizované postupy zálohovania a obnovy

Pripravení vytvoriť podnikové systémy RAG, ktoré dokážu spracovať citlivé dokumenty vo veľkom rozsahu? Poďme navrhnúť inteligentné systémy znalostí pre podniky! 🏢📖✨

## Implementácia kódu

Kompletný funkčný vzorový kód pre túto lekciu je dostupný v `05-dotnet-agent-framework.cs`. 

Na spustenie príkladu:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Alebo použite priamo `dotnet run`:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kód demonštruje:

1. **Inštalácia balíčkov**: Inštalácia požadovaných balíčkov NuGet pre Azure AI Agents
2. **Konfigurácia prostredia**: Načítanie koncových bodov Azure AI Foundry a nastavení modelu
3. **Nahrávanie dokumentov**: Nahrávanie dokumentu na spracovanie RAG
4. **Vytvorenie vektorového úložiska**: Vytvorenie vektorového úložiska pre semantické vyhľadávanie
5. **Konfigurácia agenta**: Nastavenie AI agenta s možnosťami vyhľadávania súborov
6. **Vykonanie dotazov**: Spúšťanie dotazov na nahraný dokument

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.