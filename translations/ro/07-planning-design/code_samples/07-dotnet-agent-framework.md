# 🎯 Planificare și Tipare de Design cu Azure OpenAI (API Răspunsuri) (.NET)

## 📋 Obiective de Învățare

Acest caiet demonstrează tipare de planificare și design la nivel enterprise pentru construirea agenților inteligenți folosind Microsoft Agent Framework în .NET cu Azure OpenAI (API Răspunsuri). Veți învăța să creați agenți care pot descompune probleme complexe, să planifice soluții în mai mulți pași și să execute fluxuri de lucru sofisticate folosind funcționalitățile enterprise ale .NET.

## ⚙️ Cerințe și Configurare

**Mediu de Dezvoltare:**
- SDK .NET 9.0 sau versiune superioară
- Visual Studio 2022 sau VS Code cu extensia C#
- Un abonament Azure cu o resursă Azure OpenAI și o implementare de model
- Azure CLI — autentificare cu `az login`

**Dependențe Necesare:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configurarea Mediului (.env file):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

## Rularea Codului

Această lecție include o implementare .NET Single File App. Pentru a o rula:

```bash
# Fă fișierul executabil (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Rulează aplicația
./07-dotnet-agent-framework.cs
```

Sau folosește comanda dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementarea Codului

Implementarea completă este disponibilă în `07-dotnet-agent-framework.cs`, care demonstrează:

- Încărcarea configurației de mediu cu DotNetEnv
- Configurarea clientului Azure OpenAI și crearea unui agent AI folosind `GetChatClient().AsAIAgent()`
- Definirea modelelor de date structurate (Plan și TravelPlan) cu serializare JSON
- Crearea unui agent AI cu ieșire structurată utilizând schema JSON
- Executarea cererilor de planificare cu răspunsuri tip-safe

## Concepte Cheie

### Planificare Structurată cu Modele Tip-Sigure

Agentul folosește clase C# pentru a defini structura ieșirilor de planificare:

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

### Schema JSON pentru Ieșiri Structurate

Agentul este configurat să returneze răspunsuri care corespund schemei TravelPlan:

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

### Instrucțiuni pentru Agentul de Planificare

Agentul acționează ca un coordonator, delegând sarcini sub-agente specializate:

- FlightBooking: Pentru rezervarea zborurilor și furnizarea informațiilor despre zboruri
- HotelBooking: Pentru rezervarea hotelurilor și furnizarea informațiilor despre hoteluri
- CarRental: Pentru rezervarea mașinilor și furnizarea informațiilor despre închirieri auto
- ActivitiesBooking: Pentru rezervarea activităților și furnizarea informațiilor despre activități
- DestinationInfo: Pentru a furniza informații despre destinații
- DefaultAgent: Pentru a gestiona solicitările generale

## Rezultatul Așteptat

Când vei rula agentul cu o cerere de planificare a călătoriei, acesta va analiza cererea și va genera un plan structurat cu alocări adecvate ale sarcinilor către agenți specializați, formatat ca JSON conform schemei TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->