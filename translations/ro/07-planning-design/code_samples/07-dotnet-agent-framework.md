<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:59:31+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "ro"
}
-->
# 🎯 Planificare și modele de design cu GitHub Models (.NET)

## 📋 Obiective de învățare

Acest notebook demonstrează modele de planificare și design de nivel enterprise pentru construirea agenților inteligenți utilizând Microsoft Agent Framework în .NET cu GitHub Models. Vei învăța să creezi agenți care pot descompune probleme complexe, planifica soluții în mai mulți pași și executa fluxuri de lucru sofisticate cu funcționalitățile enterprise ale .NET.

## ⚙️ Cerințe preliminare și configurare

**Mediu de dezvoltare:**
- SDK .NET 9.0 sau mai recent
- Visual Studio 2022 sau VS Code cu extensia C#
- Acces la API-ul GitHub Models

**Dependențe necesare:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configurare mediu (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Rularea codului

Această lecție include o implementare .NET Single File App. Pentru a o rula:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Sau folosește comanda dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementarea codului

Implementarea completă este disponibilă în `07-dotnet-agent-framework.cs`, care demonstrează:

- Încărcarea configurației mediului cu DotNetEnv
- Configurarea clientului OpenAI pentru GitHub Models
- Definirea modelelor de date structurate (Plan și TravelPlan) cu serializare JSON
- Crearea unui agent AI cu output structurat utilizând schema JSON
- Executarea cererilor de planificare cu răspunsuri tip-safe

## Concepte cheie

### Planificare structurată cu modele tip-safe

Agentul folosește clase C# pentru a defini structura output-urilor de planificare:

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

### Schema JSON pentru output-uri structurate

Agentul este configurat să returneze răspunsuri care se potrivesc cu schema TravelPlan:

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

### Instrucțiuni pentru agentul de planificare

Agentul acționează ca un coordonator, delegând sarcini agenților specializați:

- FlightBooking: Pentru rezervarea zborurilor și furnizarea informațiilor despre zboruri
- HotelBooking: Pentru rezervarea hotelurilor și furnizarea informațiilor despre hoteluri
- CarRental: Pentru rezervarea mașinilor și furnizarea informațiilor despre închirieri auto
- ActivitiesBooking: Pentru rezervarea activităților și furnizarea informațiilor despre activități
- DestinationInfo: Pentru furnizarea informațiilor despre destinații
- DefaultAgent: Pentru gestionarea cererilor generale

## Output așteptat

Când rulezi agentul cu o cerere de planificare a călătoriei, acesta va analiza cererea și va genera un plan structurat cu atribuirea corespunzătoare a sarcinilor agenților specializați, formatat ca JSON conform schema TravelPlan.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.