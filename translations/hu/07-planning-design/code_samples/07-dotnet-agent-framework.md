# 🎯 Tervezési és minták az Azure OpenAI-val (Responses API) (.NET)

## 📋 Tanulási célok

Ez a jegyzetfüzet vállalati szintű tervezési és mintákat mutat be intelligens ügynökök építéséhez a Microsoft Agent Framework .NET-ben az Azure OpenAI-val (Responses API). Megtanulod, hogyan hozz létre olyan ügynököket, akik képesek összetett problémákat lebontani, többlépéses megoldásokat tervezni és kifinomult munkafolyamatokat végrehajtani a .NET vállalati funkcióival.

## ⚙️ Előfeltételek és beállítás

**Fejlesztői környezet:**
- .NET 9.0 SDK vagy újabb
- Visual Studio 2022 vagy VS Code C# kiterjesztéssel
- Egy Azure előfizetés Azure OpenAI erőforrással és egy modell telepítéssel
- Az Azure CLI — bejelentkezés `az login` parancsal

**Szükséges függőségek:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Környezet konfiguráció (.env fájl):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## A kód futtatása

Ez a lecke egy .NET Single File App megvalósítást tartalmaz. Futtatáshoz:

```bash
# Tegyük futtathatóvá a fájlt (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Futtassa az alkalmazást
./07-dotnet-agent-framework.cs
```

Vagy használd a dotnet run parancsot:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Kód megvalósítás

A teljes megvalósítás megtalálható a `07-dotnet-agent-framework.cs` fájlban, amely bemutatja:

- A környezet konfiguráció betöltése DotNetEnv-vel
- Az Azure OpenAI kliens konfigurálása és AI ügynök létrehozása `GetChatClient().AsAIAgent()` segítségével
- Strukturált adatmodellek definiálása (Plan és TravelPlan) JSON sorosítással
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
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### Tervezó ügynök utasításai

Az ügynök koordinátorként működik, feladatokat delegálva specializált alügynököknek:

- FlightBooking: Repülőjáratok foglalásáért és repülőjárat információk szolgáltatásáért
- HotelBooking: Szállások foglalásáért és szállás információk szolgáltatásáért
- CarRental: Autóbérlésért és autóbérlési információk szolgáltatásáért
- ActivitiesBooking: Programok foglalásáért és program információk szolgáltatásáért
- DestinationInfo: Úticélokról szóló információk szolgáltatásáért
- DefaultAgent: Általános kérések kezeléséért

## Várt eredmény

Amikor futtatod az ügynököt utazástervezési kéréssel, elemezni fogja a kérést és egy strukturált tervet generál, amely megfelelő feladatkiosztást tartalmaz a specializált ügynököknek, JSON formátumban, amely megfelel a TravelPlan sémának.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->