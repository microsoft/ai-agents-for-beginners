# 🎯 Pianificazione e Modelli di Design con Azure OpenAI (Responses API) (.NET)

## 📋 Obiettivi di Apprendimento

Questo notebook dimostra modelli di pianificazione e design di livello enterprise per costruire agenti intelligenti utilizzando il Microsoft Agent Framework in .NET con Azure OpenAI (Responses API). Imparerai a creare agenti in grado di scomporre problemi complessi, pianificare soluzioni multi-step ed eseguire workflow sofisticati con le funzionalità enterprise di .NET.

## ⚙️ Prerequisiti e Configurazione

**Ambiente di Sviluppo:**
- SDK .NET 9.0 o superiore
- Visual Studio 2022 o VS Code con estensione C#
- Un abbonamento Azure con una risorsa Azure OpenAI e un deployment di modello
- Azure CLI — effettua il login con `az login`

**Dipendenze Necessarie:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configurazione Ambiente (file .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Esecuzione del Codice

Questa lezione include un'applicazione .NET Single File. Per eseguirla:

```bash
# Rendi il file eseguibile (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Esegui l'applicazione
./07-dotnet-agent-framework.cs
```

Oppure usa il comando dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementazione del Codice

L’implementazione completa è disponibile in `07-dotnet-agent-framework.cs`, che dimostra:

- Caricamento della configurazione ambiente con DotNetEnv
- Configurazione del client Azure OpenAI e creazione di un agente AI usando `GetChatClient().AsAIAgent()`
- Definizione di modelli dati strutturati (Plan e TravelPlan) con serializzazione JSON
- Creazione di un agente AI con output strutturato usando lo schema JSON
- Esecuzione di richieste di pianificazione con risposte tipizzate

## Concetti Chiave

### Pianificazione Strutturata con Modelli Tipizzati

L’agente utilizza classi C# per definire la struttura degli output di pianificazione:

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

### Schema JSON per Output Strutturati

L’agente è configurato per restituire risposte conformi allo schema TravelPlan:

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

### Istruzioni per l’Agente di Pianificazione

L’agente agisce da coordinatore, delegando i compiti a sub-agenti specializzati:

- FlightBooking: Per prenotare voli e fornire informazioni sui voli
- HotelBooking: Per prenotare hotel e fornire informazioni sugli hotel
- CarRental: Per prenotare auto e fornire informazioni sul noleggio auto
- ActivitiesBooking: Per prenotare attività e fornire informazioni sulle attività
- DestinationInfo: Per fornire informazioni sulle destinazioni
- DefaultAgent: Per gestire richieste generali

## Output Previsto

Quando esegui l’agente con una richiesta di pianificazione di viaggio, analizzerà la richiesta e genererà un piano strutturato con assegnazioni appropriate dei compiti agli agenti specializzati, formattato come JSON conforme allo schema TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->