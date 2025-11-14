<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:07:47+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "hu"
}
-->
# 🔍 Vállalati RAG az Azure AI Foundry-val (.NET)

## 📋 Tanulási célok

Ez a jegyzetfüzet bemutatja, hogyan lehet vállalati szintű Retrieval-Augmented Generation (RAG) rendszereket építeni a Microsoft Agent Framework segítségével .NET-ben az Azure AI Foundry-val. Megtanulhatod, hogyan hozz létre gyártásra kész ügynököket, amelyek képesek dokumentumok keresésére és pontos, kontextusfüggő válaszok nyújtására vállalati biztonsággal és skálázhatósággal.

**A vállalati RAG képességek, amelyeket kiépítesz:**
- 📚 **Dokumentumintelligencia**: Fejlett dokumentumfeldolgozás az Azure AI szolgáltatásokkal
- 🔍 **Szemantikus keresés**: Nagy teljesítményű vektorkeresés vállalati funkciókkal
- 🛡️ **Biztonsági integráció**: Szerepkör-alapú hozzáférés és adatvédelmi minták
- 🏢 **Skálázható architektúra**: Gyártásra kész RAG rendszerek monitorozással

## 🎯 Vállalati RAG architektúra

### Főbb vállalati komponensek
- **Azure AI Foundry**: Kezelt vállalati AI platform biztonsággal és megfelelőséggel
- **Állandó ügynökök**: Állapotmegőrző ügynökök beszélgetési előzményekkel és kontextuskezeléssel
- **Vektortároló kezelés**: Vállalati szintű dokumentumindexelés és visszakeresés
- **Identitásintegráció**: Azure AD hitelesítés és szerepkör-alapú hozzáférés-vezérlés

### .NET vállalati előnyök
- **Típusbiztonság**: Fordítási időben történő validáció a RAG műveletekhez és adatstruktúrákhoz
- **Aszinkron teljesítmény**: Nem blokkoló dokumentumfeldolgozás és keresési műveletek
- **Memóriakezelés**: Hatékony erőforrás-felhasználás nagy dokumentumgyűjteményekhez
- **Integrációs minták**: Natív Azure szolgáltatásintegráció függőséginjektálással

## 🏗️ Technikai architektúra

### Vállalati RAG folyamat
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Fő .NET komponensek
- **Azure.AI.Agents.Persistent**: Vállalati ügynökkezelés állapotmegőrzéssel
- **Azure.Identity**: Integrált hitelesítés biztonságos Azure szolgáltatáseléréshez
- **Microsoft.Agents.AI.AzureAI**: Azure-optimalizált ügynökkeretrendszer implementáció
- **System.Linq.Async**: Nagy teljesítményű aszinkron LINQ műveletek

## 🔧 Vállalati funkciók és előnyök

### Biztonság és megfelelőség
- **Azure AD integráció**: Vállalati identitáskezelés és hitelesítés
- **Szerepkör-alapú hozzáférés**: Finomhangolt jogosultságok dokumentumhozzáféréshez és műveletekhez
- **Adatvédelem**: Nyugalmi és átvitel közbeni titkosítás érzékeny dokumentumokhoz
- **Audit naplózás**: Átfogó tevékenységkövetés megfelelőségi követelményekhez

### Teljesítmény és skálázhatóság
- **Kapcsolatpooling**: Hatékony Azure szolgáltatáskapcsolat-kezelés
- **Aszinkron feldolgozás**: Nem blokkoló műveletek nagy áteresztőképességű forgatókönyvekhez
- **Gyorsítótárazási stratégiák**: Intelligens gyorsítótárazás gyakran hozzáférhető dokumentumokhoz
- **Terheléselosztás**: Elosztott feldolgozás nagy léptékű telepítésekhez

### Kezelés és monitorozás
- **Egészségellenőrzések**: Beépített monitorozás a RAG rendszerkomponensekhez
- **Teljesítménymutatók**: Részletes analitika a keresési minőségről és válaszidőkről
- **Hibakezelés**: Átfogó kivételkezelés újrapróbálkozási szabályokkal
- **Konfigurációkezelés**: Környezet-specifikus beállítások validációval

## ⚙️ Előfeltételek és beállítás

**Fejlesztési környezet:**
- .NET 9.0 SDK vagy újabb
- Visual Studio 2022 vagy VS Code C# kiterjesztéssel
- Azure előfizetés AI Foundry hozzáféréssel

**Szükséges NuGet csomagok:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure hitelesítési beállítás:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Környezetkonfiguráció:**
* Azure AI Foundry konfiguráció (automatikusan kezelve az Azure CLI által)
* Győződj meg róla, hogy a megfelelő Azure előfizetéshez vagy hitelesítve

## 📊 Vállalati RAG minták

### Dokumentumkezelési minták
- **Tömeges feltöltés**: Nagy dokumentumgyűjtemények hatékony feldolgozása
- **Inkrementális frissítések**: Valós idejű dokumentumhozzáadás és módosítás
- **Verziókezelés**: Dokumentumverziózás és változáskövetés
- **Metaadat-kezelés**: Gazdag dokumentumattribútumok és taxonómia

### Keresési és visszakeresési minták
- **Hibrid keresés**: Szemantikus és kulcsszavas keresés kombinálása optimális eredményekért
- **Facettált keresés**: Többdimenziós szűrés és kategorizálás
- **Relevanciahangolás**: Egyedi pontozási algoritmusok domain-specifikus igényekhez
- **Eredményrangsorolás**: Fejlett rangsorolás üzleti logika integrációval

### Biztonsági minták
- **Dokumentumszintű biztonság**: Finomhangolt hozzáférés-vezérlés dokumentumonként
- **Adatosztályozás**: Automatikus érzékenységi címkézés és védelem
- **Audit nyomvonalak**: Átfogó naplózás minden RAG műveletről
- **Adatvédelem**: PII felismerés és kitakarási képességek

## 🔒 Vállalati biztonsági funkciók

### Hitelesítés és jogosultságkezelés
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

### Adatvédelem
- **Titkosítás**: Végponttól végpontig terjedő titkosítás dokumentumokhoz és keresési indexekhez
- **Hozzáférés-vezérlés**: Integráció az Azure AD-vel felhasználói és csoportjogosultságokhoz
- **Adatrezidencia**: Földrajzi adatlokációs vezérlés megfelelőséghez
- **Biztonsági mentés és helyreállítás**: Automatikus biztonsági mentés és katasztrófa utáni helyreállítási képességek

## 📈 Teljesítményoptimalizálás

### Aszinkron feldolgozási minták
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Memóriakezelés
- **Streaming feldolgozás**: Nagy dokumentumok kezelése memória problémák nélkül
- **Erőforráspooling**: Drága erőforrások hatékony újrafelhasználása
- **Szemétgyűjtés**: Optimalizált memóriaallokációs minták
- **Kapcsolatkezelés**: Megfelelő Azure szolgáltatáskapcsolat életciklus

### Gyorsítótárazási stratégiák
- **Lekérdezés gyorsítótárazása**: Gyakran végrehajtott keresések gyorsítótárazása
- **Dokumentum gyorsítótárazása**: Memóriában történő gyorsítótárazás népszerű dokumentumokhoz
- **Index gyorsítótárazása**: Optimalizált vektorindex gyorsítótárazás
- **Eredmény gyorsítótárazása**: Intelligens gyorsítótárazás generált válaszokhoz

## 📊 Vállalati felhasználási esetek

### Tudásmenedzsment
- **Vállalati Wiki**: Intelligens keresés vállalati tudásbázisokban
- **Irányelvek és eljárások**: Automatikus megfelelőség és eljárásirányítás
- **Képzési anyagok**: Intelligens tanulási és fejlesztési segítség
- **Kutatási adatbázisok**: Akadémiai és kutatási cikkek elemző rendszerei

### Ügyfélszolgálat
- **Támogatási tudásbázis**: Automatikus ügyfélszolgálati válaszok
- **Termékdokumentáció**: Intelligens termékinformáció visszakeresés
- **Hibaelhárítási útmutatók**: Kontextusfüggő problémamegoldási segítség
- **GYIK rendszerek**: Dinamikus GYIK generálás dokumentumgyűjteményekből

### Szabályozási megfelelőség
- **Jogi dokumentumelemzés**: Szerződés- és jogi dokumentumintelligencia
- **Megfelelőség monitorozása**: Automatikus szabályozási megfelelőség ellenőrzés
- **Kockázatelemzés**: Dokumentum-alapú kockázatelemzés és jelentés
- **Audit támogatás**: Intelligens dokumentumfelfedezés auditokhoz

## 🚀 Gyártási telepítés

### Monitorozás és megfigyelhetőség
- **Application Insights**: Részletes telemetria és teljesítményfigyelés
- **Egyedi mutatók**: Üzlet-specifikus KPI követés és riasztás
- **Elosztott nyomkövetés**: Végponttól végpontig terjedő kéréskövetés szolgáltatások között
- **Egészségügyi irányítópultok**: Valós idejű rendszer egészség és teljesítmény vizualizáció

### Skálázhatóság és megbízhatóság
- **Automatikus skálázás**: Automatikus skálázás terhelés és teljesítménymutatók alapján
- **Magas rendelkezésre állás**: Több régiós telepítés hibaátállási képességekkel
- **Terhelés tesztelés**: Teljesítmény validálás vállalati terhelési körülmények között
- **Katasztrófa utáni helyreállítás**: Automatikus biztonsági mentés és helyreállítási eljárások

Készen állsz vállalati szintű RAG rendszerek építésére, amelyek képesek érzékeny dokumentumok kezelésére nagy léptékben? Építsünk intelligens tudásrendszereket a vállalat számára! 🏢📖✨

## Kódimplementáció

A teljes működő kódminta ehhez a leckéhez elérhető a `05-dotnet-agent-framework.cs` fájlban.

A példa futtatásához:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Vagy futtasd közvetlenül a `dotnet run` parancsot:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

A kód bemutatja:

1. **Csomagtelepítés**: Szükséges NuGet csomagok telepítése az Azure AI Agents számára
2. **Környezetkonfiguráció**: Azure AI Foundry végpont és modellbeállítások betöltése
3. **Dokumentumfeltöltés**: Dokumentum feltöltése RAG feldolgozáshoz
4. **Vektortároló létrehozása**: Vektortároló létrehozása szemantikus kereséshez
5. **Ügynökkonfiguráció**: AI ügynök beállítása fájlkeresési képességekkel
6. **Lekérdezés végrehajtása**: Lekérdezések futtatása a feltöltött dokumentum ellen

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.