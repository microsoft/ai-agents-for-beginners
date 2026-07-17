# 🎯 Plánovanie a návrhové vzory s Azure OpenAI (Responses API) (.NET)

## 📋 Ciele učenia

Tento notebook ukazuje podnikové plánovanie a návrhové vzory pre tvorbu inteligentných agentov pomocou Microsoft Agent Framework v .NET s Azure OpenAI (Responses API). Naučíte sa vytvárať agentov, ktorí vedia rozložiť zložité problémy, plánovať riešenia v niekoľkých krokoch a vykonávať sofistikované pracovné procesy s podnikateľskými funkciami .NET.

## ⚙️ Predpoklady a nastavenie

**Vývojové prostredie:**
- .NET 9.0 SDK alebo novšie
- Visual Studio 2022 alebo VS Code s rozšírením pre C#
- Predplatné Azure s prostriedkom Azure OpenAI a nasadením modelu
- Azure CLI — prihláste sa pomocou `az login`

**Požadované závislosti:**
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
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

## Spustenie kódu

Táto lekcia obsahuje implementáciu .NET Single File App. Pre spustenie:

```bash
# Nastavte súbor ako spustiteľný (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Spustite aplikáciu
./07-dotnet-agent-framework.cs
```

Alebo použite príkaz dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementácia kódu

Kompletná implementácia je dostupná v `07-dotnet-agent-framework.cs`, ktorá demonštruje:

- Načítanie konfigurácie prostredia pomocou DotNetEnv
- Konfiguráciu Azure OpenAI klienta a vytvorenie AI agenta pomocou `GetChatClient().AsAIAgent()`
- Definovanie štruktúrovaných dátových modelov (Plan a TravelPlan) s JSON serializáciou
- Vytvorenie AI agenta s štruktúrovaným výstupom pomocou JSON schémy
- Spustenie plánovacích požiadaviek s typovo bezpečnými odpoveďami

## Kľúčové koncepty

### Štruktúrované plánovanie s typovo bezpečnými modelmi

Agent používa C# triedy na definovanie štruktúry výstupov plánovania:

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

Agent je nastavený tak, aby vracal odpovede zodpovedajúce schéme TravelPlan:

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

### Inštrukcie pre plánovacieho agenta

Agent funguje ako koordinátor, ktorý deleguje úlohy špecializovaným podagentom:

- FlightBooking: Pre rezervácie letov a poskytovanie informácií o letoch
- HotelBooking: Pre rezervácie hotelov a poskytovanie informácií o hoteloch
- CarRental: Pre prenájom áut a poskytovanie informácií o prenájme áut
- ActivitiesBooking: Pre rezervácie aktivít a poskytovanie informácií o aktivitách
- DestinationInfo: Pre poskytovanie informácií o destináciách
- DefaultAgent: Pre spracovanie všeobecných požiadaviek

## Očakávaný výstup

Keď spustíte agenta s požiadavkou na plánovanie cesty, analyzuje požiadavku a vygeneruje štruktúrovaný plán s vhodným priradením úloh špecializovaným agentom, formátovaný ako JSON v súlade so schémou TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->