# 🔍 Vállalati RAG a Microsoft Foundry-val (.NET)

## 📋 Tanulási célok

Ez a jegyzetfüzet bemutatja, hogyan építhetünk vállalati szintű Retrieval-Augmented Generation (RAG) rendszereket a Microsoft Agent Framework használatával .NET-ben és Microsoft Foundry-val. Megtanulod létrehozni a termelésre kész ügynököket, akik dokumentumokat képesek átkutatni és pontos, kontextus-érzékeny válaszokat adni vállalati biztonsággal és skálázhatósággal.

**Vállalati RAG képességek, amelyeket fejleszteni fogsz:**
- 📚 **Dokumentum intelligencia**: fejlett dokumentumfeldolgozás Azure AI szolgáltatásokkal
- 🔍 **Szemantikus keresés**: nagy teljesítményű vektoralapú keresés vállalati funkciókkal
- 🛡️ **Biztonsági integráció**: szerepalapú hozzáférés- és adatvédelmi minták
- 🏢 **Skálázható architektúra**: termelésre kész RAG rendszerek megfigyeléssel

## 🎯 Vállalati RAG architektúra

### Alapvető vállalati elemek
- **Microsoft Foundry**: felügyelt vállalati AI platform biztonsággal és megfeleléssel
- **Állapotmegőrző ügynökök**: állapottal rendelkező ügynökök beszélgetési előzményekkel és kontextuskezeléssel
- **Vektor tároló kezelése**: vállalati szintű dokumentum indexelés és lekérés
- **Identitás integráció**: Azure AD hitelesítés és szerepalapú hozzáférés-vezérlés

### .NET vállalati előnyök
- **Típusbiztonság**: fordítás idejű érvényesítés RAG műveleteknél és adatszerkezeteknél
- **Async teljesítmény**: nem blokkoló dokumentumfeldolgozás és keresési műveletek
- **Memóriakezelés**: hatékony erőforrás-kihasználás nagy dokumentumgyűjteményekhez
- **Integrációs minták**: natív Azure szolgáltatás integráció függőséginjekcióval

## 🏗️ Technikai architektúra

### Vállalati RAG folyamat
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Alapvető .NET elemek
- **Azure.AI.Agents.Persistent**: állapotmegőrző vállalati ügynökmenedzsment
- **Azure.Identity**: integrált hitelesítés biztonságos Azure szolgáltatás hozzáféréshez
- **Microsoft.Agents.AI.AzureAI**: Azure-ra optimalizált ügynök keretrendszer megvalósítás
- **System.Linq.Async**: nagy teljesítményű aszinkron LINQ műveletek

## 🔧 Vállalati funkciók és előnyök

### Biztonság és megfelelés
- **Azure AD integráció**: vállalati identitáskezelés és hitelesítés
- **Szerepalapú hozzáférés**: finomhangolt jogosultságok dokumentum-hozzáféréshez és műveletekhez
- **Adatvédelem**: titkosítás nyugalomban és továbbítás közben érzékeny dokumentumokhoz
- **Ellenőrzési naplózás**: átfogó aktivitáskövetés megfelelési követelményekhez

### Teljesítmény és skálázhatóság
- **Kapcsolat kezelő pool**: hatékony Azure szolgáltatás kapcsolatkezelés
- **Aszinkron feldolgozás**: nem blokkoló műveletek magas áteresztőképességű forgatókönyvekhez
- **Gyorsítótár stratégiák**: intelligens cache-elés gyakran használt dokumentumokhoz
- **Terheléselosztás**: elosztott feldolgozás nagy léptékű telepítésekhez

### Menedzsment és megfigyelés
- **Egészségügyi ellenőrzések**: beépített monitorozás a RAG rendszer összetevőihez
- **Teljesítménymutatók**: részletes elemzés keresési minőségről és válaszidőkről
- **Hiba kezelés**: átfogó kivételkezelés újrapróbálkozási szabályzatokkal
- **Konfiguráció menedzsment**: környezeti beállítások validálással

## ⚙️ Előkészületek és beállítás

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

**Környezeti konfiguráció:**
* Microsoft Foundry konfiguráció (Azure CLI automatikusan kezeli)
* Győződj meg róla, hogy a megfelelő Azure előfizetéshez vagy hitelesítve

## 📊 Vállalati RAG minták

### Dokumentumkezelési minták
- **Tömeges feltöltés**: nagy dokumentumgyűjtemények hatékony feldolgozása
- **Incrementális frissítések**: valós idejű dokumentum hozzáadás és módosítás
- **Verziókövetés**: dokumentum verziózás és változáskövetés
- **Metaadat kezelés**: gazdag dokumentumtulajdonságok és taxonómia

### Keresési és lekérdezési minták
- **Hibrid keresés**: szemantikus és kulcsszó alapú keresés kombinálása optimális eredményekhez
- **Facettált keresés**: többdimenziós szűrés és kategorizálás
- **Relevancia hangolás**: testreszabott pontozási algoritmusok domain-specifikus igényekhez
- **Eredmény rangsorolás**: fejlett rangsorolás üzleti logikai integrációval

### Biztonsági minták
- **Dokumentumszintű biztonság**: finomhangolt hozzáférés vezérlés dokumentumonként
- **Adatosztályozás**: automatikus érzékenységi jelölés és védelem
- **Ellenőrzési nyomvonalak**: átfogó naplózás minden RAG műveletről
- **Adatvédelem**: PII detektálás és kitakarási képességek

## 🔒 Vállalati biztonsági funkciók

### Hitelesítés és engedélyezés
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
- **Titkosítás**: dokumentumok és keresési indexek végponttól végpontig történő titkosítása
- **Hozzáférés-vezérlés**: Azure AD integráció felhasználói és csoport jogosultságokhoz
- **Adatelhely**: földrajzi adathely ellenőrzések megfelelőséghez
- **Mentés és helyreállítás**: automatizált mentési és katasztrófa-helyreállítási képességek

## 📈 Teljesítmény optimalizálás

### Aszinkron feldolgozási minták
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Memóriakezelés
- **Streaming feldolgozás**: nagy dokumentumok kezelése memóriahibák nélkül
- **Erőforrás poolozás**: drága erőforrások hatékony újrahasznosítása
- **Garbage Collection**: optimalizált memóriafoglalási minták
- **Kapcsolat kezelése**: megfelelő Azure szolgáltatás kapcsolat-életciklus

### Gyorsítótár stratégiák
- **Lekérdezés cache**: gyakran végrehajtott keresések gyorsítótárazása
- **Dokumentum cache**: memóriában tárolt gyors elérésű dokumentumok
- **Index cache**: optimalizált vektor index gyorsítótárazás
- **Eredmény cache**: intelligens cache az előállított válaszokhoz

## 📊 Vállalati felhasználási esetek

### Tudásmenedzsment
- **Vállalati Wiki**: intelligens keresés a cég tudásbázisában
- **Szabályzatok és eljárások**: automatizált megfelelés és eljárás-útmutatók
- **Képzési anyagok**: intelligens tanulási és fejlesztési segítség
- **Kutatási adatbázisok**: akadémiai és kutatási dolgozat elemző rendszerek

### Ügyféltámogatás
- **Támogatási tudásbázis**: automatizált ügyfélszolgálati válaszok
- **Termék dokumentáció**: intelligens termékinformáció lekérés
- **Hibakeresési útmutatók**: kontextusfüggő problémamegoldó segítségnyújtás
- **GYIK rendszerek**: dinamikus GYIK generálás dokumentumgyűjteményből

### Szabályozói megfelelés
- **Jogi dokumentum elemzés**: szerződés- és jogi dokumentum intelligencia
- **Megfelelés monitorozás**: automatizált szabályozói megfelelés ellenőrzése
- **Kockázat értékelés**: dokumentumalapú kockázatelemzés és riportálás
- **Ellenőrzési támogatás**: intelligens dokumentumfelderítés auditokhoz

## 🚀 Termelési telepítés

### Megfigyelés és megtekinthetőség
- **Application Insights**: részletes telemetria és teljesítményfigyelés
- **Egyedi mérőszámok**: üzleti KPI-k követése és riasztások
- **Elosztott nyomon követés**: végponttól végpontig történő kéréskövetés szolgáltatások között
- **Egészség műszerfalak**: valós idejű rendszer egészség és teljesítmény vizualizáció

### Skálázhatóság és megbízhatóság
- **Automatikus skálázás**: automatikus skálázódás terhelés és teljesítménymutatók alapján
- **Magas rendelkezésre állás**: több régiós telepítés failover képességekkel
- **Terhelés tesztelés**: teljesítmény validálás vállalati terhelés mellett
- **Katasztrófa helyreállítás**: automatizált mentési és helyreállítási eljárások

Készen állsz vállalati szintű RAG rendszerek építésére, amelyek érzékeny dokumentumokat kezelnek nagy léptékben? Építsünk együtt intelligens tudásmenedzsment rendszereket a vállalat számára! 🏢📖✨

## Kódmegvalósítás

A teljes működő kódminta a leckéhez elérhető a `05-dotnet-agent-framework.cs` fájlban.

A példafuttatáshoz:

```bash
# Tegye futtathatóvá a szkriptet (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Futtassa a .NET egymélyfájlos alkalmazást
./05-dotnet-agent-framework.cs
```

Vagy használd közvetlenül a `dotnet run` parancsot:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

A kód bemutatja:

1. **Csomag telepítés**: szükséges NuGet csomagok telepítése Azure AI Agents-hez
2. **Környezet konfiguráció**: Microsoft Foundry végpont és modell beállítások betöltése
3. **Dokumentum feltöltés**: dokumentum feltöltése RAG feldolgozáshoz
4. **Vektor tároló létrehozás**: vektor tároló létrehozása szemantikus kereséshez
5. **Ügynök konfiguráció**: AI ügynök beállítása fájlkeresési képességekkel
6. **Lekérdezés futtatás**: lekérdezések futtatása a feltöltött dokumentum ellen

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->