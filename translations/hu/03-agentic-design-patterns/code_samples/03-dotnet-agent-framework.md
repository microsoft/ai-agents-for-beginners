<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:50:35+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "hu"
}
-->
# 🎨 Agentikus tervezési minták GitHub modellekkel (.NET)

## 📋 Tanulási célok

Ez a jegyzetfüzet bemutatja azokat a vállalati szintű tervezési mintákat, amelyekkel intelligens ügynököket lehet építeni a Microsoft Agent Framework segítségével .NET-ben, GitHub modellek integrációjával. Megtanulhatod azokat a professzionális mintákat és architekturális megközelítéseket, amelyek az ügynököket gyártásra kész, karbantartható és skálázható megoldásokká teszik.

**Vállalati tervezési minták:**
- 🏭 **Factory minta**: Standardizált ügynök létrehozás függőséginjektálással
- 🔧 **Builder minta**: Folyékony ügynök konfiguráció és beállítás
- 🧵 **Szálbiztos minták**: Párhuzamos beszélgetéskezelés
- 📋 **Repository minta**: Eszközök és képességek szervezett kezelése

## 🎯 .NET-specifikus architekturális előnyök

### Vállalati funkciók
- **Erős típusosság**: Fordítási időben történő validáció és IntelliSense támogatás
- **Függőséginjektálás**: Beépített DI konténer integráció
- **Konfigurációkezelés**: IConfiguration és Options minták
- **Async/Await**: Első osztályú aszinkron programozási támogatás

### Gyártásra kész minták
- **Naplózási integráció**: ILogger és strukturált naplózási támogatás
- **Egészségügyi ellenőrzések**: Beépített monitorozás és diagnosztika
- **Konfiguráció validáció**: Erős típusosság adatannotációkkal
- **Hibakezelés**: Strukturált kivételkezelés

## 🔧 Technikai architektúra

### Alapvető .NET komponensek
- **Microsoft.Extensions.AI**: Egységes AI szolgáltatás absztrakciók
- **Microsoft.Agents.AI**: Vállalati ügynökök orchesztrációs keretrendszere
- **GitHub modellek integrációja**: Nagy teljesítményű API kliens minták
- **Konfigurációs rendszer**: appsettings.json és környezeti integráció

### Tervezési minták megvalósítása
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Bemutatott vállalati minták

### 1. **Létrehozási minták**
- **Agent Factory**: Központosított ügynök létrehozás következetes konfigurációval
- **Builder minta**: Folyékony API komplex ügynök konfigurációhoz
- **Singleton minta**: Megosztott erőforrások és konfigurációkezelés
- **Függőséginjektálás**: Laza kapcsolódás és tesztelhetőség

### 2. **Viselkedési minták**
- **Stratégia minta**: Cserélhető eszköz végrehajtási stratégiák
- **Parancs minta**: Ügynök műveletek kapszulázása visszavonás/újra végrehajtás lehetőséggel
- **Megfigyelő minta**: Eseményvezérelt ügynök életciklus-kezelés
- **Sablon metódus**: Standardizált ügynök végrehajtási munkafolyamatok

### 3. **Szerkezeti minták**
- **Adapter minta**: GitHub modellek API integrációs réteg
- **Dekorátor minta**: Ügynök képességek bővítése
- **Homlokzat minta**: Egyszerűsített ügynök interakciós interfészek
- **Proxy minta**: Lusta betöltés és gyorsítótárazás a teljesítmény érdekében

## ⚙️ Előfeltételek és beállítás

**Fejlesztési környezet:**
- .NET 9.0 SDK vagy újabb
- Visual Studio 2022 vagy VS Code C# kiterjesztéssel
- GitHub Models API hozzáférés

**NuGet függőségek:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguráció (.env fájl):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 .NET tervezési elvek

### SOLID elvek
- **Egyetlen felelősség**: Minden komponensnek egyértelmű célja van
- **Nyitott/Zárt**: Bővíthető módosítás nélkül
- **Liskov helyettesítés**: Interfész-alapú eszköz implementációk
- **Interfész szegregáció**: Fókuszált, összetartó interfészek
- **Függőség inversió**: Absztrakciókra támaszkodás, nem konkrétumokra

### Tiszta architektúra
- **Domain réteg**: Alapvető ügynök és eszköz absztrakciók
- **Alkalmazási réteg**: Ügynök orchesztráció és munkafolyamatok
- **Infrastruktúra réteg**: GitHub modellek integrációja és külső szolgáltatások
- **Prezentációs réteg**: Felhasználói interakció és válaszformázás

## 🔒 Vállalati szempontok

### Biztonság
- **Hitelesítő adatok kezelése**: Biztonságos API kulcs kezelés IConfiguration segítségével
- **Bemenet validáció**: Erős típusosság és adatannotáció validáció
- **Kimenet szűrés**: Biztonságos válaszfeldolgozás és szűrés
- **Audit naplózás**: Átfogó műveletkövetés

### Teljesítmény
- **Aszinkron minták**: Nem blokkoló I/O műveletek
- **Kapcsolat pooling**: Hatékony HTTP kliens kezelés
- **Gyorsítótárazás**: Válasz gyorsítótárazása a jobb teljesítmény érdekében
- **Erőforrás-kezelés**: Megfelelő felszabadítás és tisztítási minták

### Skálázhatóság
- **Szálbiztonság**: Párhuzamos ügynök végrehajtási támogatás
- **Erőforrás pooling**: Hatékony erőforrás-használat
- **Terheléskezelés**: Sebességkorlátozás és visszanyomás kezelése
- **Monitorozás**: Teljesítménymérő és egészségügyi ellenőrzések

## 🚀 Gyártási telepítés

- **Konfigurációkezelés**: Környezet-specifikus beállítások
- **Naplózási stratégia**: Strukturált naplózás korrelációs azonosítókkal
- **Hibakezelés**: Globális kivételkezelés megfelelő helyreállítással
- **Monitorozás**: Alkalmazás betekintések és teljesítmény számlálók
- **Tesztelés**: Egységtesztek, integrációs tesztek és terhelési tesztelési minták

Készen állsz vállalati szintű intelligens ügynökök építésére .NET-ben? Tervezzünk valami robusztusat! 🏢✨

## Kódminta

Teljes működő példáért lásd: [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.