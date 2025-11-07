<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:56:50+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "it"
}
-->
# 🎯 Pianificazione e Design Patterns con i Modelli GitHub (.NET)

## 📋 Obiettivi di Apprendimento

Questo notebook dimostra modelli di pianificazione e design di livello aziendale per la creazione di agenti intelligenti utilizzando il Microsoft Agent Framework in .NET con i Modelli GitHub. Imparerai a creare agenti capaci di scomporre problemi complessi, pianificare soluzioni multi-step e eseguire flussi di lavoro sofisticati con le funzionalità aziendali di .NET.

## ⚙️ Prerequisiti e Configurazione

**Ambiente di Sviluppo:**
- SDK .NET 9.0 o superiore
- Visual Studio 2022 o VS Code con estensione C#
- Accesso all'API dei Modelli GitHub

**Dipendenze Necessarie:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configurazione dell'Ambiente (file .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Esecuzione del Codice

Questa lezione include un'implementazione di un'applicazione .NET Single File. Per eseguirla:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Oppure utilizza il comando dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementazione del Codice

L'implementazione completa è disponibile in `07-dotnet-agent-framework.cs`, che dimostra:

- Caricamento della configurazione dell'ambiente con DotNetEnv
- Configurazione del client OpenAI per i Modelli GitHub
- Definizione di modelli di dati strutturati (Plan e TravelPlan) con serializzazione JSON
- Creazione di un agente AI con output strutturato utilizzando lo schema JSON
- Esecuzione di richieste di pianificazione con risposte tipizzate

## Concetti Chiave

### Pianificazione Strutturata con Modelli Tipizzati

L'agente utilizza classi C# per definire la struttura degli output di pianificazione:

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

L'agente è configurato per restituire risposte che corrispondono allo schema TravelPlan:

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

### Istruzioni per l'Agente di Pianificazione

L'agente agisce come coordinatore, delegando compiti a sub-agenti specializzati:

- FlightBooking: Per prenotare voli e fornire informazioni sui voli
- HotelBooking: Per prenotare hotel e fornire informazioni sugli hotel
- CarRental: Per prenotare auto e fornire informazioni sul noleggio auto
- ActivitiesBooking: Per prenotare attività e fornire informazioni sulle attività
- DestinationInfo: Per fornire informazioni sulle destinazioni
- DefaultAgent: Per gestire richieste generali

## Output Atteso

Quando esegui l'agente con una richiesta di pianificazione di viaggio, analizzerà la richiesta e genererà un piano strutturato con assegnazioni di compiti appropriate agli agenti specializzati, formattato come JSON conforme allo schema TravelPlan.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.