# 🎯 Plánování a návrhové vzory s Azure OpenAI (Responses API) (.NET)

## 📋 Výukové cíle

Tento notebook ukazuje podnikové plánovací a návrhové vzory pro vytváření inteligentních agentů pomocí Microsoft Agent Framework v .NET s Azure OpenAI (Responses API). Naučíte se vytvářet agenty, kteří umějí rozložit složité problémy, plánovat vícestupňová řešení a vykonávat sofistikované pracovní postupy s podnikových funkcemi .NET.

## ⚙️ Požadavky a nastavení

**Vývojové prostředí:**
- .NET 9.0 SDK nebo novější
- Visual Studio 2022 nebo VS Code s rozšířením C#
- Předplatné Azure s prostředkem Azure OpenAI a nasazením modelu
- Azure CLI — přihlaste se pomocí `az login`

**Požadované závislosti:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurace prostředí (soubor .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Spuštění kódu

Tato lekce obsahuje implementaci .NET Single File App. Pro její spuštění:

```bash
# Nastavte soubor jako spustitelný (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Spusťte aplikaci
./07-dotnet-agent-framework.cs
```

Nebo použijte příkaz dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementace kódu

Kompletní implementace je dostupná v `07-dotnet-agent-framework.cs`, která demonstruje:

- Načítání konfigurace prostředí pomocí DotNetEnv
- Konfiguraci klienta Azure OpenAI pro Responses API
- Definování strukturovaných datových modelů (Plan a TravelPlan) s JSON serializací
- Vytváření AI agenta se strukturovaným výstupem pomocí JSON schématu
- Vykonávání plánovacích požadavků s typově bezpečnými odpověďmi

## Klíčové pojmy

### Strukturované plánování s typově bezpečnými modely

Agent používá třídy C# pro definování struktury plánovacích výstupů:

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

### JSON schéma pro strukturované výstupy

Agent je nastaven tak, aby vracel odpovědi odpovídající schématu TravelPlan:

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

### Instrukce pro plánovacího agenta

Agent funguje jako koordinátor, který deleguje úkoly specializovaným podagentům:

- FlightBooking: Pro rezervaci letů a poskytování informací o letech
- HotelBooking: Pro rezervaci hotelů a poskytování informací o hotelech
- CarRental: Pro rezervaci aut a poskytování informací o půjčovnách aut
- ActivitiesBooking: Pro rezervaci aktivit a poskytování informací o aktivitách
- DestinationInfo: Pro poskytování informací o destinacích
- DefaultAgent: Pro zpracování obecný požadavků

## Očekávaný výstup

Při spuštění agenta s požadavkem na plánování cesty analyzuje požadavek a vygeneruje strukturovaný plán s odpovídajícími úkoly přidělenými specializovaným agentům, formátovaný jako JSON odpovídající schématu TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->