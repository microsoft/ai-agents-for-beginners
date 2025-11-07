<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:59:23+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "sk"
}
-->
# 🎯 Plánovanie a návrhové vzory s GitHub Models (.NET)

## 📋 Ciele učenia

Tento notebook demonštruje plánovanie a návrhové vzory na podnikovej úrovni pre vytváranie inteligentných agentov pomocou Microsoft Agent Framework v .NET s GitHub Models. Naučíte sa vytvárať agentov, ktorí dokážu rozložiť zložité problémy, plánovať viacstupňové riešenia a vykonávať sofistikované pracovné postupy s podnikovými funkciami .NET.

## ⚙️ Predpoklady a nastavenie

**Vývojové prostredie:**
- .NET 9.0 SDK alebo vyšší
- Visual Studio 2022 alebo VS Code s rozšírením C#
- Prístup k GitHub Models API

**Požadované závislosti:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurácia prostredia (súbor .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Spustenie kódu

Táto lekcia obsahuje implementáciu .NET Single File App. Na jej spustenie:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Alebo použite príkaz dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementácia kódu

Kompletná implementácia je dostupná v `07-dotnet-agent-framework.cs`, ktorá demonštruje:

- Načítanie konfigurácie prostredia pomocou DotNetEnv
- Konfiguráciu klienta OpenAI pre GitHub Models
- Definovanie štruktúrovaných dátových modelov (Plan a TravelPlan) s JSON serializáciou
- Vytvorenie AI agenta so štruktúrovaným výstupom pomocou JSON schémy
- Vykonávanie plánovacích požiadaviek s typovo bezpečnými odpoveďami

## Kľúčové koncepty

### Štruktúrované plánovanie s typovo bezpečnými modelmi

Agent používa triedy C# na definovanie štruktúry výstupov plánovania:

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

### JSON schéma pre štruktúrované výstupy

Agent je nakonfigurovaný tak, aby vracal odpovede zodpovedajúce schéme TravelPlan:

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

### Inštrukcie pre plánovacieho agenta

Agent funguje ako koordinátor, ktorý deleguje úlohy na špecializovaných sub-agentov:

- FlightBooking: Na rezerváciu letov a poskytovanie informácií o letoch
- HotelBooking: Na rezerváciu hotelov a poskytovanie informácií o hoteloch
- CarRental: Na rezerváciu áut a poskytovanie informácií o prenájme áut
- ActivitiesBooking: Na rezerváciu aktivít a poskytovanie informácií o aktivitách
- DestinationInfo: Na poskytovanie informácií o destináciách
- DefaultAgent: Na spracovanie všeobecných požiadaviek

## Očakávaný výstup

Keď spustíte agenta s požiadavkou na plánovanie cesty, analyzuje požiadavku a vygeneruje štruktúrovaný plán s vhodným priradením úloh špecializovaným agentom, formátovaný ako JSON zodpovedajúci schéme TravelPlan.

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.