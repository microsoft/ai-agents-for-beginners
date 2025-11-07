<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:59:14+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "cs"
}
-->
# 🎯 Plánování a návrhové vzory s GitHub Models (.NET)

## 📋 Cíle učení

Tento notebook ukazuje plánování a návrhové vzory na podnikové úrovni pro vytváření inteligentních agentů pomocí Microsoft Agent Framework v .NET s GitHub Models. Naučíte se vytvářet agenty, kteří dokážou rozkládat složité problémy, plánovat vícekroková řešení a provádět sofistikované pracovní postupy s podnikovými funkcemi .NET.

## ⚙️ Předpoklady a nastavení

**Vývojové prostředí:**
- .NET 9.0 SDK nebo vyšší
- Visual Studio 2022 nebo VS Code s rozšířením C#
- Přístup k GitHub Models API

**Požadované závislosti:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurace prostředí (soubor .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Spuštění kódu

Tato lekce obsahuje implementaci .NET Single File App. Pro spuštění:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Nebo použijte příkaz dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementace kódu

Kompletní implementace je dostupná v `07-dotnet-agent-framework.cs`, která ukazuje:

- Načítání konfigurace prostředí pomocí DotNetEnv
- Konfiguraci klienta OpenAI pro GitHub Models
- Definování strukturovaných datových modelů (Plan a TravelPlan) s JSON serializací
- Vytvoření AI agenta se strukturovaným výstupem pomocí JSON schématu
- Provádění plánovacích požadavků s typově bezpečnými odpověďmi

## Klíčové koncepty

### Strukturované plánování s typově bezpečnými modely

Agent používá C# třídy k definování struktury výstupů plánování:

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

Agent je nakonfigurován tak, aby vracel odpovědi odpovídající schématu TravelPlan:

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

Agent funguje jako koordinátor, který deleguje úkoly na specializované pod-agenty:

- FlightBooking: Pro rezervaci letů a poskytování informací o letech
- HotelBooking: Pro rezervaci hotelů a poskytování informací o hotelech
- CarRental: Pro rezervaci aut a poskytování informací o pronájmu aut
- ActivitiesBooking: Pro rezervaci aktivit a poskytování informací o aktivitách
- DestinationInfo: Pro poskytování informací o destinacích
- DefaultAgent: Pro zpracování obecných požadavků

## Očekávaný výstup

Když spustíte agenta s požadavkem na plánování cesty, analyzuje požadavek a vytvoří strukturovaný plán s odpovídajícími přiřazeními úkolů specializovaným agentům, formátovaný jako JSON odpovídající schématu TravelPlan.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.