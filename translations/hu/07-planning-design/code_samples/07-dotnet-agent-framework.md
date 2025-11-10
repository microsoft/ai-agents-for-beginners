<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:59:04+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "hu"
}
-->
# 🎯 Tervezés és tervezési minták GitHub Modellek (.NET) használatával

## 📋 Tanulási célok

Ez a jegyzetfüzet bemutatja a vállalati szintű tervezési és tervezési mintákat intelligens ügynökök létrehozásához a Microsoft Agent Framework segítségével .NET-ben, GitHub Modellek használatával. Megtanulhatod, hogyan hozz létre ügynököket, amelyek képesek összetett problémák lebontására, többlépcsős megoldások tervezésére és kifinomult munkafolyamatok végrehajtására a .NET vállalati funkcióival.

## ⚙️ Előfeltételek és beállítás

**Fejlesztési környezet:**
- .NET 9.0 SDK vagy újabb
- Visual Studio 2022 vagy VS Code C# kiterjesztéssel
- GitHub Models API hozzáférés

**Szükséges függőségek:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Környezet konfiguráció (.env fájl):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## A kód futtatása

Ez a lecke egy .NET Egyszeri Fájl Alkalmazás implementációt tartalmaz. A futtatáshoz:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Vagy használd a dotnet run parancsot:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Kód implementáció

A teljes implementáció elérhető a `07-dotnet-agent-framework.cs` fájlban, amely bemutatja:

- Környezet konfiguráció betöltése DotNetEnv segítségével
- OpenAI kliens konfigurálása GitHub Modellekhez
- Strukturált adatmodellek (Plan és TravelPlan) definiálása JSON sorosítással
- AI ügynök létrehozása strukturált kimenettel JSON séma használatával
- Tervezési kérések végrehajtása típusbiztos válaszokkal

## Kulcsfogalmak

### Strukturált tervezés típusbiztos modellekkel

Az ügynök C# osztályokat használ a tervezési kimenetek struktúrájának meghatározására:

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### JSON séma strukturált kimenetekhez

Az ügynök úgy van konfigurálva, hogy a TravelPlan séma szerinti válaszokat adjon vissza:

```csharp
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### Tervezési ügynök utasításai

Az ügynök koordinátorként működik, feladatokat delegálva specializált alügynököknek:

- FlightBooking: Repülőjegyek foglalására és repülési információk biztosítására
- HotelBooking: Szállodák foglalására és szállodai információk biztosítására
- CarRental: Autók foglalására és autóbérlési információk biztosítására
- ActivitiesBooking: Programok foglalására és programinformációk biztosítására
- DestinationInfo: Úti célokkal kapcsolatos információk biztosítására
- DefaultAgent: Általános kérések kezelésére

## Várható kimenet

Amikor az ügynököt egy utazási tervezési kéréssel futtatod, elemezni fogja a kérést, és strukturált tervet generál megfelelő feladatkiosztásokkal a specializált ügynökök számára, JSON formátumban, amely megfelel a TravelPlan sémának.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.