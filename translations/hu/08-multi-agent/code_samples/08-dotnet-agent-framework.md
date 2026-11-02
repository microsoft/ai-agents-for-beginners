# 🤝 Vállalati Többügynökös Munkafolyamat Rendszerek (.NET)

## 📋 Tanulási Célok

Ez a jegyzetfüzet bemutatja, hogyan építsünk kifinomult vállalati szintű többügynökös rendszereket a Microsoft Agent Framework használatával .NET-ben az Azure OpenAI-val (Responses API). Megtanulod, hogyan koordinálj több, specializált ügynököt, amelyek strukturált munkafolyamatokon keresztül együtt dolgoznak, kihasználva a .NET vállalati funkcióit a gyártásra kész megoldásokhoz.

**Az általad építendő vállalati többügynökös képességek:**
- 👥 **Ügynökök együttműködése**: Típusbiztos ügynök koordináció fordítási idejű ellenőrzéssel
- 🔄 **Munkafolyamat irányítás**: Deklaratív munkafolyamat-definíció .NET aszinkron mintáival
- 🎭 **Szerepkör specializáció**: Erősen típusos ügynök személyiségek és szakértelmi területek
- 🏢 **Vállalati integráció**: Gyártásra kész minták monitorozással és hibakezeléssel

## ⚙️ Előfeltételek és Beállítás

**Fejlesztői környezet:**
- .NET 9.0 SDK vagy újabb
- Visual Studio 2022 vagy VS Code C# kiterjesztéssel
- Azure előfizetés (az állandó ügynökökhöz)

**Szükséges NuGet csomagok:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## Kódpélda

A leckéhez tartozó teljes, működő kód elérhető a csatolt C# fájlban: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

A minta futtatásához:

```bash
# Tegye futtathatóvá a fájlt (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Futtassa a példát
./08-dotnet-agent-framework.cs
```

Vagy a .NET CLI használatával:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Mit Mutat Be Ez a Minta

Ez a többügynökös munkafolyamat rendszer egy szállodai utazási ajánló szolgáltatást hoz létre két specializált ügynökkel:

1. **FrontDesk Ügynök**: Egy utazási ügynök, amely tevékenységek és helyszínek ajánlásait nyújtja
2. **Concierge Ügynök**: Áttekinti az ajánlásokat, hogy hiteles, nem turista jellegű élményeket biztosítson

Az ügynökök együtt dolgoznak egy munkafolyamatban, ahol:
- A FrontDesk ügynök fogadja a kezdeti utazási kérést
- A Concierge ügynök átnézi és finomítja az ajánlást
- A munkafolyamat valós időben továbbít válaszokat

## Kulcsfogalmak

### Ügynök koordináció
A minta típusbiztos ügynök koordinációt mutat be a Microsoft Agent Framework használatával, fordítási idejű érvényesítéssel.

### Munkafolyamat irányítás
Deklaratív munkafolyamat-definíciót használ .NET aszinkron mintákkal, hogy több ügynököt kapcsoljon össze egy csővezetékben.

### Válaszok streamelése
Valós idejű válaszstreamelést valósít meg ügynököktől aszinkron enumerálhatókkal és eseményvezérelt architektúrával.

### Vállalati integráció
Gyártásra kész mintákat mutat be, többek között:
- Környezeti változók konfigurálása
- Biztonságos hitelesítő adatok kezelése
- Hibakezelés
- Aszinkron eseményfeldolgozás

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->