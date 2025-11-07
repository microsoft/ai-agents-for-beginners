<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:18:16+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "hu"
}
-->
# 🤝 Vállalati Többügynökös Munkafolyamat Rendszerek (.NET)

## 📋 Tanulási célok

Ez a jegyzetfüzet bemutatja, hogyan lehet kifinomult, vállalati szintű többügynökös rendszereket építeni a Microsoft Agent Framework segítségével .NET-ben, GitHub modellekkel. Megtanulhatod, hogyan lehet több specializált ügynököt összehangolni strukturált munkafolyamatokon keresztül, kihasználva a .NET vállalati funkcióit a gyártásra kész megoldásokhoz.

**A vállalati többügynökös képességek, amelyeket kiépítesz:**
- 👥 **Ügynökök együttműködése**: Típusbiztos ügynökkoordináció fordítási időben történő validációval
- 🔄 **Munkafolyamat-vezérlés**: Deklaratív munkafolyamat-meghatározás a .NET aszinkron mintáival
- 🎭 **Szerepspecializáció**: Erősen típusos ügynökszemélyiségek és szakértelem területek
- 🏢 **Vállalati integráció**: Gyártásra kész minták monitorozással és hibakezeléssel

## ⚙️ Előfeltételek és beállítás

**Fejlesztési környezet:**
- .NET 9.0 SDK vagy újabb
- Visual Studio 2022 vagy VS Code C# kiterjesztéssel
- Azure előfizetés (állandó ügynökökhöz)

**Szükséges NuGet csomagok:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Kódminta

A teljes működő kód ehhez a leckéhez az alábbi C# fájlban érhető el: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

A minta futtatásához:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Vagy a .NET CLI használatával:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Amit ez a minta bemutat

Ez a többügynökös munkafolyamat-rendszer egy hotel utazási ajánlási szolgáltatást hoz létre két specializált ügynökkel:

1. **Recepciós ügynök**: Egy utazási ügynök, aki tevékenységi és helyszíni ajánlásokat nyújt
2. **Concierge ügynök**: Felülvizsgálja az ajánlásokat, hogy biztosítsa az autentikus, nem turistás élményeket

Az ügynökök együtt dolgoznak egy munkafolyamatban, ahol:
- A Recepciós ügynök megkapja a kezdeti utazási kérést
- A Concierge ügynök felülvizsgálja és finomítja az ajánlást
- A munkafolyamat valós időben közvetíti a válaszokat

## Kulcsfogalmak

### Ügynökök koordinációja
A minta bemutatja a típusbiztos ügynökkoordinációt a Microsoft Agent Framework segítségével fordítási időben történő validációval.

### Munkafolyamat-vezérlés
Deklaratív munkafolyamat-meghatározást használ a .NET aszinkron mintáival, hogy több ügynököt kapcsoljon össze egy csővezetékben.

### Valós idejű válaszok közvetítése
Valós idejű válaszok közvetítését valósítja meg aszinkron enumerálhatókkal és eseményvezérelt architektúrával.

### Vállalati integráció
Gyártásra kész mintákat mutat be, beleértve:
- Környezeti változók konfigurációja
- Biztonságos hitelesítő adatok kezelése
- Hibakezelés
- Aszinkron eseményfeldolgozás

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.