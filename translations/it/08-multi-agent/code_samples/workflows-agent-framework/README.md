# Costruire Applicazioni Multi-Agente con il Workflow del Microsoft Agent Framework

Questo tutorial ti guiderà nella comprensione e nella costruzione di applicazioni multi-agente utilizzando il Microsoft Agent Framework. Esploreremo i concetti fondamentali dei sistemi multi-agente, analizzeremo l'architettura del componente Workflow del framework, e attraverseremo esempi pratici sia in Python che in .NET per diversi pattern di workflow.

## 1\. Comprendere i Sistemi Multi-Agente

Un Agente AI è un sistema che va oltre le capacità di un modello linguistico di grandi dimensioni (LLM) standard. Può percepire il suo ambiente, prendere decisioni, e compiere azioni per raggiungere specifici obiettivi. Un sistema multi-agente coinvolge diversi di questi agenti che collaborano per risolvere un problema che sarebbe difficile o impossibile da gestire da un singolo agente da solo.

### Scenari Applicativi Comuni

  * **Risoluzione di Problemi Complessi**: Suddividere un grande compito (ad esempio, pianificare un evento aziendale) in sotto-compiti più piccoli gestiti da agenti specializzati (ad esempio, un agente per il budget, un agente per la logistica, un agente per il marketing).
  * **Assistenti Virtuali**: Un agente assistente principale che delega compiti come la programmazione, la ricerca e le prenotazioni ad altri agenti specializzati.
  * **Creazione Automatica di Contenuti**: Un workflow in cui un agente scrive una bozza di contenuto, un altro la revisiona per accuratezza e tono, e un terzo la pubblica.

### Pattern Multi-Agente

I sistemi multi-agente possono essere organizzati in diversi pattern che determinano come interagiscono:

  * **Sequenziale**: Gli agenti lavorano in un ordine predefinito, come una catena di montaggio. L'output di un agente diventa l'input per il successivo.
  * **Concorrenziale**: Gli agenti lavorano in parallelo su diverse parti di un compito, e i loro risultati sono aggregati alla fine.
  * **Condizionale**: Il workflow segue percorsi diversi basati sull'output di un agente, simile a una istruzione if-then-else.

## 2\. L'Architettura del Workflow del Microsoft Agent Framework

Il sistema di workflow dell'Agent Framework è un motore di orchestrazione avanzato progettato per gestire interazioni complesse tra più agenti. È costruito su un'architettura basata su grafi che utilizza un [modello di esecuzione stile Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), dove l'elaborazione avviene in passi sincronizzati chiamati "supersteps."

### Componenti Principali

L'architettura è composta da tre parti principali:

1.  **Executor**: Questi sono le unità fondamentali di elaborazione. Nei nostri esempi, un `Agent` è un tipo di executor. Ogni executor può avere più handler di messaggi che vengono invocati automaticamente in base al tipo di messaggio ricevuto.
2.  **Edges**: Definiscono il percorso che i messaggi seguono tra gli executor. Gli edges possono avere condizioni, permettendo un instradamento dinamico delle informazioni attraverso il grafo di workflow.
3.  **Workflow**: Questa componente orchestra l'intero processo, gestendo gli executor, gli edges, e il flusso complessivo di esecuzione. Garantisce che i messaggi vengano processati nell'ordine corretto e trasmette eventi per l'osservabilità.

*Un diagramma che illustra i componenti principali del sistema di workflow.*

Questa struttura permette di costruire applicazioni robuste e scalabili utilizzando pattern fondamentali come catene sequenziali, fan-out/fan-in per l'elaborazione parallela, e logica switch-case per flussi condizionali.

## 3\. Esempi Pratici e Analisi del Codice

Ora, esploriamo come implementare diversi pattern di workflow usando il framework. Vedremo sia il codice Python che .NET per ogni esempio.

### Caso 1: Workflow Sequenziale Base

Questo è il pattern più semplice, dove l'output di un agente è passato direttamente a un altro. Il nostro scenario coinvolge un agente `FrontDesk` dell'hotel che fa una raccomandazione di viaggio, che viene poi revisionata da un agente `Concierge`.

*Diagramma del workflow base FrontDesk -\> Concierge.*

#### Contesto dello Scenario

Un viaggiatore chiede una raccomandazione su Parigi.

1.  L'agente `FrontDesk`, pensato per la sintesi, suggerisce di visitare il Museo del Louvre.
2.  L'agente `Concierge`, che dà priorità alle esperienze autentiche, riceve questo suggerimento. Revisiona la raccomandazione e fornisce un feedback, suggerendo un'alternativa più locale e meno turistica.

#### Analisi dell'Implementazione in Python

Nell'esempio Python, definiamo e creiamo prima i due agenti, ciascuno con istruzioni specifiche.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definisci ruoli e istruzioni degli agenti
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Crea istanze di agenti
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Successivamente, `WorkflowBuilder` viene usato per costruire il grafo. L'agente `front_desk_agent` è impostato come punto di partenza, e un edge viene creato per collegare il suo output all'agente `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Infine, il workflow viene eseguito con il prompt iniziale dell'utente.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run esegue il flusso di lavoro; get_outputs() restituisce il risultato dell'esecutore di output.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analisi dell'Implementazione in .NET (C\#)

L'implementazione in .NET segue una logica molto simile. Prima vengono definite costanti per i nomi e le istruzioni degli agenti.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Gli agenti sono creati usando un `AzureOpenAIClient` (API Responses), poi `WorkflowBuilder` definisce il flusso sequenziale aggiungendo un edge dall'agente `frontDeskAgent` a `reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetChatClient(deployment).AsAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

Il workflow viene quindi eseguito con il messaggio dell'utente, e i risultati vengono trasmessi in streaming.

### Caso 2: Workflow Sequenziale a Più Passi

Questo pattern estende la sequenza base includendo più agenti. È ideale per processi che richiedono più fasi di raffinamento o trasformazione.

#### Contesto dello Scenario

Un utente fornisce un'immagine di un soggiorno e chiede un preventivo per i mobili.

1.  **Sales-Agent**: Identifica gli articoli di arredamento nell'immagine e crea una lista.
2.  **Price-Agent**: Prende la lista degli articoli e fornisce una ripartizione dettagliata dei prezzi, includendo opzioni economiche, medie e premium.
3.  **Quote-Agent**: Riceve la lista con i prezzi e la formatta in un documento di preventivo formale in Markdown.

*Diagramma del workflow Sales -\> Price -\> Quote.*

#### Analisi dell'Implementazione in Python

Tre agenti sono definiti, ciascuno con un ruolo specializzato. Il workflow viene costruito usando `add_edge` per creare una catena: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Crea tre agenti specializzati
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Costruisci il flusso di lavoro sequenziale
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

L'input è un `ChatMessage` che include sia testo che l'URI dell'immagine. Il framework gestisce il passaggio dell'output di ogni agente al successivo nella sequenza fino a generare il preventivo finale.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Il messaggio dell'utente contiene sia testo che un'immagine
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Esegui il flusso di lavoro
events = await workflow.run(message)
```

#### Analisi dell'Implementazione in .NET (C\#)

L'esempio .NET rispecchia la versione Python. Tre agenti (`salesagent`, `priceagent`, `quoteagent`) sono creati. `WorkflowBuilder` li collega in sequenza.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent priceagent  = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent quoteagent = azureClient.GetChatClient(deployment).AsAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

Il messaggio dell'utente è costruito con i dati dell'immagine (come byte) e il prompt di testo. Il metodo `InProcessExecution.RunStreamingAsync` avvia il workflow, e l'output finale è catturato dallo stream.

### Caso 3: Workflow Concorrenziale

Questo pattern è usato quando i compiti possono essere eseguiti simultaneamente per risparmiare tempo. Coinvolge un "fan-out" verso più agenti e un "fan-in" per aggregare i risultati.

#### Contesto dello Scenario

Un utente chiede di pianificare un viaggio a Seattle.

1.  **Dispatcher (Fan-Out)**: La richiesta dell'utente viene inviata a due agenti contemporaneamente.
2.  **Researcher-Agent**: Ricerca attrazioni, clima e considerazioni chiave per un viaggio a Seattle a dicembre.
3.  **Plan-Agent**: Crea indipendentemente un itinerario dettagliato giorno per giorno.
4.  **Aggregator (Fan-In)**: Gli output sia del ricercatore che del pianificatore vengono raccolti e presentati insieme come risultato finale.

*Diagramma del workflow concorrente Researcher e Planner.*

#### Analisi dell'Implementazione in Python

`ConcurrentBuilder` semplifica la creazione di questo pattern. Basta elencare gli agenti partecipanti, e il builder crea automaticamente la logica fan-out e fan-in necessaria.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder gestisce la logica di fan-out/fan-in
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Esegui il flusso di lavoro
events = await workflow.run("Plan a trip to Seattle in December")
```

Il framework garantisce che il `research_agent` e il `plan_agent` vengano eseguiti in parallelo, e i loro output finali vengano raccolti in una lista.

#### Analisi dell'Implementazione in .NET (C\#)

In .NET, questo pattern richiede una definizione più esplicita. Executor personalizzati (`ConcurrentStartExecutor` e `ConcurrentAggregationExecutor`) sono creati per gestire la logica di fan-out e fan-in.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

`WorkflowBuilder` usa quindi `AddFanOutEdge` e `AddFanInEdge` per costruire il grafo con questi executor personalizzati e gli agenti.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Caso 4: Workflow Condizionale

I workflow condizionali introducono logiche di ramificazione, permettendo al sistema di prendere percorsi diversi basati sui risultati intermedi.

#### Contesto dello Scenario

Questo workflow automatizza la creazione e pubblicazione di un tutorial tecnico.

1.  **Evangelist-Agent**: Scrive una bozza del tutorial basata su un outline e URL forniti.
2.  **ContentReviewer-Agent**: Revisiona la bozza. Controlla se il conteggio delle parole supera le 200 parole.
3.  **Ramo Condizionale**:
      * **Se Approvato (`Yes`)**: Il workflow procede verso l'agente `Publisher-Agent`.
      * **Se Respinto (`No`)**: Il workflow si ferma e fornisce il motivo del rifiuto.
4.  **Publisher-Agent**: Se la bozza è approvata, questo agente salva il contenuto in un file Markdown.

#### Analisi dell'Implementazione in Python

Questo esempio usa una funzione personalizzata, `select_targets`, per implementare la logica condizionale. Questa funzione è passata a `add_multi_selection_edge_group` e dirige il workflow basandosi sul campo `review_result` dell'output del revisore.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Questa funzione determina il passo successivo basato sul risultato della revisione
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Se approvato, procedi all'esecutore 'save_draft'
        return [save_draft_id]
    else:
        # Se rifiutato, procedi all'esecutore 'handle_review' per segnalare il fallimento
        return [handle_review_id]

# Il costruttore del flusso di lavoro utilizza la funzione di selezione per l'instradamento
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Il bordo a selezione multipla implementa la logica condizionale
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Executor personalizzati come `to_reviewer_result` sono usati per analizzare l'output JSON dagli agenti e convertirlo in oggetti fortemente tipizzati che la funzione di selezione può ispezionare.

#### Analisi dell'Implementazione in .NET (C\#)

La versione .NET usa un approccio simile con una funzione condizionale. Un `Func<object?, bool>` è definito per controllare la proprietà `Result` dell'oggetto `ReviewResult`.

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

Il parametro `condition` del metodo `AddEdge` permette al `WorkflowBuilder` di creare un percorso ramificato. Il workflow seguirà l'edge verso `publishExecutor` solo se la condizione `GetCondition(expectedResult: "Yes")` ritorna true. Altrimenti, seguirà il percorso verso `sendReviewerExecutor`.

## Conclusione

Il Microsoft Agent Framework Workflow fornisce una base robusta e flessibile per orchestrare sistemi complessi multi-agente. Sfruttando la sua architettura basata su grafi e componenti principali, gli sviluppatori possono progettare e implementare workflow sofisticati sia in Python che in .NET. Che la tua applicazione richieda un'elaborazione semplice sequenziale, esecuzione parallela, o logica condizionale dinamica, il framework offre gli strumenti per costruire soluzioni AI potenti, scalabili, e type-safe.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->