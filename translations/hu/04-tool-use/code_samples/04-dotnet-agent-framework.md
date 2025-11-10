<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:27:26+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "hu"
}
-->
# 🛠️ Fejlett eszközhasználat GitHub Modellekkel (.NET)

## 📋 Tanulási célok

Ez a jegyzetfüzet bemutatja a vállalati szintű eszközintegrációs mintákat a Microsoft Agent Framework használatával .NET-ben, GitHub Modellekkel. Megtanulhatod, hogyan építs kifinomult ügynököket több speciális eszközzel, kihasználva a C# erős típusosságát és a .NET vállalati funkcióit.

**Fejlett eszközhasználati képességek, amelyeket elsajátíthatsz:**
- 🔧 **Többeszközös architektúra**: Ügynökök építése több speciális képességgel
- 🎯 **Típusbiztos eszközvégrehajtás**: A C# fordítási idejű validációjának kihasználása
- 📊 **Vállalati eszközminták**: Gyártásra kész eszköztervezés és hibakezelés
- 🔗 **Eszközkompozíció**: Eszközök kombinálása összetett üzleti munkafolyamatokhoz

## 🎯 .NET eszközarchitektúra előnyei

### Vállalati eszközfunkciók
- **Fordítási idejű validáció**: Az erős típusosság biztosítja az eszközparaméterek helyességét
- **Függőség injektálása**: IoC konténer integráció az eszközkezeléshez
- **Async/Await minták**: Nem blokkoló eszközvégrehajtás megfelelő erőforrás-kezeléssel
- **Strukturált naplózás**: Beépített naplózási integráció az eszközvégrehajtás monitorozásához

### Gyártásra kész minták
- **Kivételkezelés**: Átfogó hibakezelés típusos kivételekkel
- **Erőforrás-kezelés**: Megfelelő felszabadítási minták és memória-kezelés
- **Teljesítményfigyelés**: Beépített metrikák és teljesítményszámlálók
- **Konfigurációkezelés**: Típusbiztos konfiguráció validációval

## 🔧 Technikai architektúra

### Alapvető .NET eszközkomponensek
- **Microsoft.Extensions.AI**: Egységes eszközabsztrakciós réteg
- **Microsoft.Agents.AI**: Vállalati szintű eszközorchesztráció
- **GitHub Modellek integrációja**: Nagy teljesítményű API kliens kapcsolatpoolinggal

### Eszközvégrehajtási folyamat
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Eszközkategóriák és minták

### 1. **Adatfeldolgozó eszközök**
- **Bemenet validációja**: Erős típusosság adatannotációkkal
- **Átalakítási műveletek**: Típusbiztos adatkonverzió és formázás
- **Üzleti logika**: Domain-specifikus számítási és elemzési eszközök
- **Kimenet formázása**: Strukturált válaszgenerálás

### 2. **Integrációs eszközök**
- **API csatlakozók**: RESTful szolgáltatásintegráció HttpClient segítségével
- **Adatbázis eszközök**: Entity Framework integráció az adateléréshez
- **Fájlműveletek**: Biztonságos fájlrendszer-műveletek validációval
- **Külső szolgáltatások**: Harmadik fél szolgáltatási integrációs minták

### 3. **Segédprogramok**
- **Szövegfeldolgozás**: Karakterlánc-manipulációs és formázási segédprogramok
- **Dátum/idő műveletek**: Kultúraérzékeny dátum/idő számítások
- **Matematikai eszközök**: Precíz számítások és statisztikai műveletek
- **Validációs eszközök**: Üzleti szabályok validálása és adatellenőrzés

## ⚙️ Előfeltételek és beállítás

**Fejlesztési környezet:**
- .NET 9.0 SDK vagy újabb
- Visual Studio 2022 vagy VS Code C# kiterjesztéssel
- GitHub Modellek API hozzáférés

**Szükséges NuGet csomagok:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Környezetkonfiguráció (.env fájl):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Készen állsz vállalati szintű ügynökök építésére erőteljes, típusbiztos eszközfunkciókkal .NET-ben? Tervezd meg a professzionális megoldásokat! 🏢⚡

## 💻 Kódmegvalósítás

A teljes C# megvalósítás elérhető a kísérő fájlban: `04-dotnet-agent-framework.cs`. Ez a .NET Egyszeri Fájl Alkalmazás bemutatja:

- Környezeti változók betöltése a GitHub Modellek konfigurációjához
- Egyedi eszközök definiálása C# metódusokkal és attribútumokkal
- AI ügynök létrehozása eszközintegrációval
- Beszélgetési szálak kezelése
- Ügynökkérések végrehajtása eszközmeghívással

Az példa futtatásához:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Vagy a .NET CLI használatával:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.