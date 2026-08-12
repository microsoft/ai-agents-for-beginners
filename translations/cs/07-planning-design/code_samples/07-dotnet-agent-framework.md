# 🎯 Plánování a návrhové vzory s Azure OpenAI (Responses API) (.NET)

## 📋 Cíle učení

Tento notebook ukazuje podnikové plánovací a návrhové vzory pro vytváření inteligentních agentů pomocí Microsoft Agent Framework v .NET s Azure OpenAI (Responses API). Naučíte se vytvářet agenty, kteří dokážou rozložit složité problémy, plánovat více kroková řešení a provádět sofistikované pracovní postupy s podnikových funkcemi .NET.

## ⚙️ Požadavky a nastavení

**Vývojové prostředí:**
- .NET 9.0 SDK nebo vyšší
- Visual Studio 2022 nebo VS Code s rozšířením C#
- Předplatné Azure s Azure OpenAI zdrojem a nasazením modelu
- Azure CLI — přihlaste se pomocí `az login`

**Požadované závislosti:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurace prostředí (soubor .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Spuštění kódu

Tato lekce obsahuje implementaci .NET Single File App. Pro její spuštění:

```bash
# Udělejte soubor spustitelným (Linux/macOS)
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
- Konfiguraci Azure OpenAI klienta a vytvoření AI agenta pomocí `GetChatClient().AsAIAgent()`
- Definování strukturovaných datových modelů (Plan a TravelPlan) s JSON serializací
- Vytvoření AI agenta se strukturovaným výstupem pomocí JSON schématu
- Vykonávání plánovacích požadavků s typově bezpečnými odpověďmi

## Klíčové koncepty

### Strukturované plánování s typově bezpečnými modely

Agent používá C# třídy k definování struktury výsledků plánování:

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

### JSON Schéma pro strukturované výstupy

Agent je nakonfigurován tak, aby vracel odpovědi odpovídající schématu TravelPlan:

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

### Instrukce plánovacího agenta

Agent vystupuje jako koordinátor, delegující úkoly specializovaným pod-agentům:

- FlightBooking: Pro rezervaci letů a poskytování informací o letech
- HotelBooking: Pro rezervaci hotelů a poskytování informací o hotelích
- CarRental: Pro rezervaci aut a poskytování informací o půjčení aut
- ActivitiesBooking: Pro rezervaci aktivit a poskytování informací o aktivitách
- DestinationInfo: Pro poskytování informací o destinacích
- DefaultAgent: Pro zpracování obecných požadavků

## Očekávaný výstup

Když spustíte agenta s požadavkem na plánování cesty, analyzuje požadavek a vygeneruje strukturovaný plán s odpovídajícím přidělením úkolů specializovaným agentům, formátovaný jako JSON splňující schéma TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->