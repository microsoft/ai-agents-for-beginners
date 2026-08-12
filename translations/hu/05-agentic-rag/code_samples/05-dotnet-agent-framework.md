# 🔍 Vállalati RAG a Microsoft Foundry-val (.NET)

## 📋 Tanulási célok

Ez a jegyzetfüzet bemutatja, hogyan építhetünk vállalati szintű Retrieval-Augmented Generation (RAG) rendszereket a Microsoft Agent Framework és a Microsoft Foundry használatával .NET-ben. Megtanulod, hogyan készíts produkcióra kész ügynököket, amelyek dokumentumok között keresnek és pontos, kontextusérzékeny válaszokat adnak vállalati biztonsággal és skálázhatósággal.

**Vállalati RAG képességek, amelyeket építeni fogsz:**
- 📚 **Dokumentum intelligencia**: Fejlett dokumentumfeldolgozás Azure AI szolgáltatásokkal
- 🔍 **Szemantikus keresés**: Nagy teljesítményű vektoros keresés vállalati funkciókkal
- 🛡️ **Biztonsági integráció**: Szerepalapú hozzáférés és adatvédelmi minták
- 🏢 **Skálázható architektúra**: Produkcióra kész RAG rendszerek monitorozással

## 🎯 Vállalati RAG architektúra

### Fő vállalati komponensek
- **Microsoft Foundry**: Kezelt vállalati AI platform biztonsággal és megfeleléssel
- **Állapotmegőrző ügynökök**: Állapottal rendelkező ügynökök beszélgetési előzményekkel és kontextuskezeléssel
- **Vektortár-kezelés**: Vállalati szintű dokumentumindexelés és lekérdezés
- **Identitás integráció**: Azure AD hitelesítés és szerepalapú hozzáférésvezérlés

### .NET vállalati előnyök
- **Típusbiztonság**: Fordítási időben történő érvényesítés a RAG műveletekhez és adatszerkezetekhez
- **Async teljesítmény**: Nem blokkoló dokumentumfeldolgozás és keresési műveletek
- **Memóriakezelés**: Hatékony erőforrás-kihasználás nagy dokumentumgyűjteményekhez
- **Integrációs minták**: Natív Azure szolgáltatás integráció függőséginjektálással

## 🏗️ Műszaki architektúra

### Vállalati RAG folyamat
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Fő .NET komponensek
- **Azure.AI.Agents.Persistent**: Vállalati ügynök kezelés állapotmegőrzéssel
- **Azure.Identity**: Integrált hitelesítés a biztonságos Azure szolgáltatáshoz
- **Microsoft.Agents.AI.AzureAI**: Azure-optimalizált ügynök keretrendszer megvalósítás
- **System.Linq.Async**: Nagy teljesítményű aszinkron LINQ műveletek

## 🔧 Vállalati jellemzők és előnyök

### Biztonság és megfelelőség
- **Azure AD integráció**: Vállalati identitáskezelés és hitelesítés
- **Szerepalapú hozzáférés**: Finoman szabályozott engedélyek dokumentum eléréshez és műveletekhez
- **Adatvédelem**: Titkosítás pihenő állapotban és adatátvitel közben érzékeny dokumentumok esetén
- **Audit naplózás**: Teljes körű tevékenységkövetés megfelelési követelményekhez

### Teljesítmény és skálázhatóság
- **Kapcsolatkezelés**: Hatékony Azure szolgáltatás kapcsolatkezelés
- **Aszinkron feldolgozás**: Nem blokkoló műveletek nagy áteresztőképességű forgatókönyvekhez
- **Gyorsítótárazási stratégiák**: Intelligens gyorsítótárazás gyakran hozzáfért dokumentumokhoz
- **Terheléselosztás**: Elosztott feldolgozás nagyszabású telepítésekhez

### Kezelés és monitorozás
- **Egészségügyi ellenőrzések**: Beépített monitorozás a RAG rendszer komponenseihez
- **Teljesítménymutatók**: Részletes analitika a keresési minőségről és válaszidőkről
- **Hiba kezelés**: Átfogó kivételkezelés újrapróbálási szabályokkal
- **Konfiguráció-kezelés**: Környezet-specifikus beállítások érvényesítéssel

## ⚙️ Előfeltételek és beállítás

**Fejlesztői környezet:**
- .NET 9.0 SDK vagy újabb
- Visual Studio 2022 vagy VS Code C# kiterjesztéssel
- Azure előfizetés Microsoft Foundry hozzáféréssel

**Szükséges NuGet csomagok:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure hitelesítés beállítása:**
```bash
# Telepítse az Azure CLI-t és hitelesítse magát
az login
az account set --subscription "your-subscription-id"
```

**Környezet konfiguráció:**
* Microsoft Foundry konfiguráció (automatikusan kezelve Azure CLI-val)
* Győződj meg róla, hogy az aktuális Azure előfizetéshez vagy hitelesítve

## 📊 Vállalati RAG minták

### Dokumentumkezelési minták
- **Tömeges feltöltés**: Nagy dokumentumgyűjtemények hatékony feldolgozása
- **Inkrementális frissítések**: Valós idejű dokumentum hozzáadás és módosítás
- **Verziókövetés**: Dokumentumverziók és változáskövetés
- **Metaadat-kezelés**: Gazdag dokumentumattribútumok és taxonómia

### Keresési és lekérdezési minták
- **Hibrid keresés**: Szemantikus és kulcsszavas keresés kombinálása optimális eredményért
- **Facettált keresés**: Többdimenziós szűrés és kategorizálás
- **Relevancia hangolás**: Egyedi pontozási algoritmusok domain-specifikus igényekhez
- **Eredmény rangsorolás**: Fejlett rangsorolás üzleti logika integrációval

### Biztonsági minták
- **Dokumentumszintű biztonság**: Finoman szabályozott hozzáférés dokumentumonként
- **Adatosztályozás**: Automatikus érzékenységi címkézés és védelem
- **Audit nyomvonalak**: Teljes naplózás az összes RAG műveletről
- **Adatvédelem**: Személyes azonosító adatok felismerése és kitakarása

## 🔒 Vállalati biztonsági funkciók

### Hitelesítés és jogosultság
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
- **Titkosítás**: Végpontok közötti titkosítás dokumentumok és keresési indexek esetén
- **Hozzáférés vezérlés**: Integráció Azure AD-vel felhasználói és csoport engedélyekhez
- **Adathely**: Földrajzi adat helyszín vezérlés megfelelőséghez
- **Biztonsági mentés és helyreállítás**: Automatikus mentési és katasztrófa utáni helyreállítási képességek

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
- **Erőforrás medence**: Költséges erőforrások hatékony újrahasznosítása
- **Memória kezelő**: Optimalizált memória allokációs minták
- **Kapcsolatkezelés**: Az Azure szolgáltatás kapcsolatainak megfelelő kezelése

### Gyorsítótárazási stratégiák
- **Lekérdezés gyorsítótár**: Gyakran végrehajtott keresések gyorsítótárazása
- **Dokumentum gyorsítótár**: Memóriában tárolt gyorsítótárazás a gyakori dokumentumokhoz
- **Index gyorsítótár**: Optimalizált vektor index gyorsítótárazás
- **Eredmény gyorsítótár**: Intelligens gyorsítótárazás a generált válaszokhoz

## 📊 Vállalati felhasználási esetek

### Tudáskezelés
- **Vállalati wiki**: Intelligens keresés a vállalati tudásbázisokon át
- **Szabályzatok és eljárások**: Automatikus megfelelés és folyamatvezetés
- **Képzési anyagok**: Intelligens tanulási és fejlődési támogatás
- **Kutatási adatbázisok**: Tudományos és kutatási cikkek elemző rendszerei

### Ügyféltámogatás
- **Támogatási tudásbázis**: Automatikus ügyfélszolgálati válaszok
- **Termék dokumentáció**: Intelligens termékinformáció lekérdezés
- **Hibaelhárítási útmutatók**: Kontextusfüggő problémamegoldó támogatás
- **GYIK rendszerek**: Dinamikus GYIK generálás dokumentumgyűjteményből

### Szabályozói megfelelőség
- **Jogi dokumentumelemzés**: Szerződés- és jogi dokumentum intelligencia
- **Megfelelés monitorozás**: Automatikus szabályozói megfelelés ellenőrzés
- **Kockázatértékelés**: Dokumentum alapú kockázat elemzés és jelentés
- **Audit támogatás**: Intelligens dokumentum felderítés auditokhoz

## 🚀 Produkciós telepítés

### Monitorozás és megfigyelhetőség
- **Application Insights**: Részletes telemetria és teljesítmény monitorozás
- **Egyedi mutatók**: Üzleti specifikus KPI nyomon követés és riasztás
- **Elosztott követés**: Kérések végponttól végpontig történő követése szolgáltatások között
- **Egészségi műszerfalak**: Valós idejű rendszer egészségi és teljesítmény vizualizáció

### Skálázhatóság és megbízhatóság
- **Automatikus skálázás**: Automatikus méretezés terhelés és teljesítmény szerint
- **Magas rendelkezésre állás**: Több régióba telepítés failover képességekkel
- **Terhelés tesztelés**: Teljesítmény validáció vállalati terhelési feltételek mellett
- **Katasztrófa helyreállítás**: Automatikus mentési és helyreállítási eljárások

Készen állsz vállalati szintű RAG rendszerek építésére, amelyek érzékeny dokumentumokat kezelnek nagy léptékben? Építsünk intelligens tudásrendszereket a vállalat számára! 🏢📖✨

## Kód megvalósítás

Ennek az oktatásnak a teljes működő kódmintája elérhető a `05-dotnet-agent-framework.cs` fájlban.

A példafuttatáshoz:

```bash
# Tegye végrehajthatóvá a szkriptet (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Futtassa a .NET Egylépéses Alkalmazást
./05-dotnet-agent-framework.cs
```

Vagy használd közvetlenül a `dotnet run` parancsot:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

A kód bemutatja:

1. **Csomag telepítés**: Szükséges NuGet csomagok telepítése Azure AI ügynökökhöz
2. **Környezet konfiguráció**: Microsoft Foundry végpont és modell beállítások betöltése
3. **Dokumentum feltöltés**: Dokumentum feltöltése RAG feldolgozáshoz
4. **Vektortár létrehozás**: Vektortár létrehozása szemantikus kereséshez
5. **Ügynök konfiguráció**: AI ügynök beállítása fájlkeresési képességekkel
6. **Lekérdezés végrehajtás**: Lekérdezések futtatása a feltöltött dokumentumra

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->