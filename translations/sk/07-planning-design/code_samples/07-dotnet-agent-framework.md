# 🎯 Plánovanie a návrhové vzory s Azure OpenAI (Responses API) (.NET)

## 📋 Ciele vzdelávania

Tento zápisník demonštruje podnikové plánovacie a návrhové vzory pre tvorbu inteligentných agentov pomocou Microsoft Agent Framework v .NET s Azure OpenAI (Responses API). Naučíte sa vytvárať agentov, ktorí dokážu rozložiť komplexné problémy, plánovať viacstupňové riešenia a vykonávať sofistikované pracovné postupy s podnikateľskými vlastnosťami .NET.

## ⚙️ Predpoklady a nastavenie

**Vývojové prostredie:**
- .NET 9.0 SDK alebo novší
- Visual Studio 2022 alebo VS Code s rozšírením C#
- Predplatné Azure s Azure OpenAI zdrojom a nasadením modelu
- Azure CLI — prihláste sa pomocou `az login`

**Povinné závislosti:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurácia prostredia (.env súbor):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Spustenie kódu

Táto lekcia obsahuje implementáciu Single File App v .NET. Pre spustenie:

```bash
# Urobte súbor spustiteľným (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Spustite aplikáciu
./07-dotnet-agent-framework.cs
```

Alebo použite príkaz dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementácia kódu

Kompletná implementácia je k dispozícii v `07-dotnet-agent-framework.cs`, ktorý demonštruje:

- Načítanie konfigurácie prostredia s DotNetEnv
- Konfiguráciu klienta Azure OpenAI a vytváranie AI agenta pomocou `GetChatClient().AsAIAgent()`
- Definovanie štruktúrovaných dátových modelov (Plan a TravelPlan) s JSON serializáciou
- Vytváranie AI agenta so štruktúrovaným výstupom pomocou JSON schémy
- Vykonávanie plánovacích požiadaviek s typovo bezpečnými odpoveďami

## Kľúčové pojmy

### Štruktúrované plánovanie s typovo bezpečnými modelmi

Agent používa C# triedy na definovanie štruktúry plánovacích výstupov:

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

### Pokyny plánovacieho agenta

Agent pôsobí ako koordinátor, delegujúci úlohy špecializovaným podagentom:

- FlightBooking: Na rezerváciu letov a poskytovanie informácií o letoch
- HotelBooking: Na rezerváciu hotelov a poskytovanie informácií o hoteloch
- CarRental: Na rezerváciu áut a poskytovanie informácií o požičovni áut
- ActivitiesBooking: Na rezerváciu aktivít a poskytovanie informácií o aktivitách
- DestinationInfo: Na poskytovanie informácií o destináciách
- DefaultAgent: Na spracovanie všeobecných požiadaviek

## Očakávaný výstup

Po spustení agenta s požiadavkou na plánovanie cesty analyzuje požiadavku a vygeneruje štruktúrovaný plán s príslušným priradením úloh špecializovaným agentom vo formáte JSON vyhovujúcom schéme TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->