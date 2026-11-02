# 🎯 Planificare & Modele de Proiectare cu Azure OpenAI (API Răspunsuri) (.NET)

## 📋 Obiective de Învățare

Acest notebook demonstrează modele de planificare și proiectare la nivel enterprise pentru construirea agenților inteligenți folosind Microsoft Agent Framework în .NET cu Azure OpenAI (API Răspunsuri). Vei învăța cum să creezi agenți care pot decomprima probleme complexe, să planifice soluții în pași multipli și să execute fluxuri de lucru sofisticate cu funcționalitățile enterprise ale .NET.

## ⚙️ Cerințe și Configurare

**Mediu de Dezvoltare:**
- .NET 9.0 SDK sau versiune superioară
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
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Rularea Codului

Această lecție include o implementare a unei aplicații Single File .NET. Pentru a o rula:

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

- Încărcarea configurației mediului cu DotNetEnv
- Configurarea clientului Azure OpenAI și crearea unui agent AI folosind `GetChatClient().AsAIAgent()`
- Definirea modelelor de date structurate (Plan și TravelPlan) cu serializare JSON
- Crearea unui agent AI cu output structurat folosind schema JSON
- Executarea cererilor de planificare cu răspunsuri tip-safe

## Concepte Cheie

### Planificare Structurată cu Modele Tip-Sigure

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

### Schema JSON pentru Output-uri Structurate

Agentul este configurat să returneze răspunsuri conforme cu schema TravelPlan:

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

Agentul acționează ca un coordonator, delegând sarcini către sub-agenti specializați:

- FlightBooking: Pentru rezervarea zborurilor și oferirea de informații despre zbor
- HotelBooking: Pentru rezervarea hotelurilor și oferirea de informații despre hoteluri
- CarRental: Pentru rezervarea mașinilor și oferirea de informații despre închirieri auto
- ActivitiesBooking: Pentru rezervarea activităților și oferirea de informații despre activități
- DestinationInfo: Pentru oferirea de informații despre destinații
- DefaultAgent: Pentru gestionarea cererilor generale

## Output Așteptat

Când rulezi agentul cu o cerere de planificare a unei călătorii, acesta va analiza cererea și va genera un plan structurat cu alocări de sarcini corespunzătoare către agenți specializați, formatat ca JSON conform schema TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->