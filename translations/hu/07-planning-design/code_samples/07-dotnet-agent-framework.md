# 🎯 Tervezés és tervezési minták Azure OpenAI-val (Responses API) (.NET)

## 📋 Tanulási célok

Ez a jegyzetfüzet vállalati szintű tervezési és mintázati megoldásokat mutat be intelligens ügynökök építéséhez a Microsoft Agent Framework használatával .NET-ben, Azure OpenAI-val (Responses API). Megtanulod, hogyan hozhatsz létre olyan ügynököket, amelyek képesek összetett problémákat lebontani, többlépcsős megoldásokat tervezni, és kifinomult munkafolyamatokat végrehajtani a .NET vállalati funkcióival.

## ⚙️ Előfeltételek és beállítás

**Fejlesztői környezet:**
- .NET 9.0 SDK vagy újabb
- Visual Studio 2022 vagy VS Code C# bővítménnyel
- Egy Azure előfizetés Azure OpenAI erőforrással és modell telepítéssel
- Azure CLI — bejelentkezés `az login` paranccsal

**Szükséges függőségek:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Környezeti beállítások (.env fájl):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## A kód futtatása

Ez a lecke egy .NET egységfájl alkalmazás megvalósítást tartalmaz. A futtatáshoz:

```bash
# Tedd futtathatóvá a fájlt (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Futtasd az alkalmazást
./07-dotnet-agent-framework.cs
```

Vagy használd a dotnet run parancsot:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Kód megvalósítása

A teljes megvalósítás elérhető a `07-dotnet-agent-framework.cs` fájlban, amely bemutatja:

- Környezeti beállítások betöltése DotNetEnv segítségével
- Az Azure OpenAI kliens konfigurálása a Responses API-hoz
- Strukturált adatmodellek definiálása (Plan és TravelPlan) JSON szerializációval
- AI ügynök létrehozása strukturált kimenettel JSON sémával
- Tervezési kérések végrehajtása típusbiztos válaszokkal

## Kulcsfogalmak

### Strukturált tervezés típusbiztos modellekkel

Az ügynök C# osztályokat használ a tervezési kimenetek szerkezetének meghatározásához:

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

### JSON séma a strukturált kimenetekhez

Az ügynök úgy van konfigurálva, hogy a TravelPlan sémának megfelelő válaszokat adjon vissza:

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

- FlightBooking: Repülőjegyek foglalására és repülőjárat-információk biztosítására
- HotelBooking: Szállodafoglalásra és szállodai információk nyújtására
- CarRental: Autóbérlés foglalására és autóbérlési információkra
- ActivitiesBooking: Programok foglalására és tevékenység-információkra
- DestinationInfo: Úticél információk biztosítására
- DefaultAgent: Általános kérések kezelésére

## Várt kimenet

Amikor a tervezési kéréssel futtatod az ügynököt, elemezni fogja a kérést és strukturált tervet generál, megfelelő feladatkiosztással a specializált ügynököknek, JSON formátumban, amely megfelel a TravelPlan sémának.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->