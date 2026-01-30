# Creare Applicazioni Multi-Agente con il Workflow del Microsoft Agent Framework

Questo tutorial ti guiderà nella comprensione e nella creazione di applicazioni multi-agente utilizzando il Microsoft Agent Framework. Esploreremo i concetti fondamentali dei sistemi multi-agente, approfondiremo l'architettura del componente Workflow del framework e analizzeremo esempi pratici in Python e .NET per diversi modelli di workflow.

## 1\. Comprendere i Sistemi Multi-Agente

Un agente AI è un sistema che va oltre le capacità di un modello linguistico di grandi dimensioni (LLM). Può percepire l'ambiente, prendere decisioni e compiere azioni per raggiungere obiettivi specifici. Un sistema multi-agente coinvolge diversi di questi agenti che collaborano per risolvere un problema che sarebbe difficile o impossibile da gestire per un singolo agente.

### Scenari Applicativi Comuni

  * **Risoluzione di Problemi Complessi**: Suddividere un grande compito (ad esempio, organizzare un evento aziendale) in sotto-compiti gestiti da agenti specializzati (ad esempio, un agente per il budget, un agente per la logistica, un agente per il marketing).
  * **Assistenti Virtuali**: Un agente principale delega compiti come la pianificazione, la ricerca e le prenotazioni ad altri agenti specializzati.
  * **Creazione Automatica di Contenuti**: Un workflow in cui un agente redige il contenuto, un altro lo rivede per accuratezza e tono, e un terzo lo pubblica.

### Modelli Multi-Agente

I sistemi multi-agente possono essere organizzati in diversi modelli, che determinano come interagiscono:

  * **Sequenziale**: Gli agenti lavorano in un ordine predefinito, come una catena di montaggio. L'output di un agente diventa l'input per il successivo.
  * **Concorrenza**: Gli agenti lavorano in parallelo su diverse parti di un compito, e i loro risultati vengono aggregati alla fine.
  * **Condizionale**: Il workflow segue percorsi diversi in base all'output di un agente, simile a una dichiarazione if-then-else.

## 2\. L'Architettura del Workflow del Microsoft Agent Framework

Il sistema di workflow del Microsoft Agent Framework è un motore di orchestrazione avanzato progettato per gestire interazioni complesse tra più agenti. È costruito su un'architettura basata su grafi che utilizza un [modello di esecuzione stile Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), dove l'elaborazione avviene in passaggi sincronizzati chiamati "supersteps".

### Componenti Principali

L'architettura è composta da tre parti principali:

1.  **Executor**: Questi sono le unità di elaborazione fondamentali. Nei nostri esempi, un `Agent` è un tipo di executor. Ogni executor può avere più gestori di messaggi che vengono automaticamente invocati in base al tipo di messaggio ricevuto.
2.  **Edges**: Questi definiscono il percorso che i messaggi seguono tra gli executor. Gli edges possono avere condizioni, permettendo il routing dinamico delle informazioni attraverso il grafo del workflow.
3.  **Workflow**: Questo componente orchestra l'intero processo, gestendo gli executor, gli edges e il flusso generale di esecuzione. Garantisce che i messaggi vengano elaborati nell'ordine corretto e trasmette eventi per l'osservabilità.

*Un diagramma che illustra i componenti principali del sistema di workflow.*

Questa struttura consente di creare applicazioni robuste e scalabili utilizzando modelli fondamentali come catene sequenziali, fan-out/fan-in per l'elaborazione parallela e logica switch-case per flussi condizionali.

## 3\. Esempi Pratici e Analisi del Codice

Ora esploriamo come implementare diversi modelli di workflow utilizzando il framework. Vedremo codice sia in Python che in .NET per ciascun esempio.

### Caso 1: Workflow Sequenziale Base

Questo è il modello più semplice, in cui l'output di un agente viene passato direttamente a un altro. Il nostro scenario coinvolge un agente `FrontDesk` di un hotel che fa una raccomandazione di viaggio, che viene poi esaminata da un agente `Concierge`.

*Diagramma del workflow base FrontDesk -\> Concierge.*

#### Contesto dello Scenario

Un viaggiatore chiede una raccomandazione per Parigi.

1.  L'agente `FrontDesk`, progettato per essere sintetico, suggerisce di visitare il Museo del Louvre.
2.  L'agente `Concierge`, che dà priorità alle esperienze autentiche, riceve questa raccomandazione. La esamina e fornisce un feedback, suggerendo un'alternativa più locale e meno turistica.

#### Analisi dell'Implementazione in Python

Nel caso Python, definiamo e creiamo i due agenti, ciascuno con istruzioni specifiche.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Define agent roles and instructions
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Create agent instances
reviewer_agent = chat_client.create_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.create_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Successivamente, utilizziamo il `WorkflowBuilder` per costruire il grafo. L'agente `front_desk_agent` è impostato come punto di partenza, e viene creato un edge per collegare il suo output all'agente `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Infine, il workflow viene eseguito con il prompt iniziale dell'utente.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Analisi dell'Implementazione in .NET (C\#)

L'implementazione in .NET segue una logica molto simile. Prima vengono definiti i costanti per i nomi e le istruzioni degli agenti.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Gli agenti vengono creati utilizzando un `OpenAIClient`, e poi il `WorkflowBuilder` definisce il flusso sequenziale aggiungendo un edge dall'agente `frontDeskAgent` all'agente `reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

Il workflow viene quindi eseguito con il messaggio dell'utente, e i risultati vengono trasmessi in streaming.

### Caso 2: Workflow Sequenziale Multi-Step

Questo modello estende la sequenza base includendo più agenti. È ideale per processi che richiedono più fasi di raffinamento o trasformazione.

#### Contesto dello Scenario

Un utente fornisce un'immagine di un soggiorno e chiede un preventivo per i mobili.

1.  **Sales-Agent**: Identifica gli articoli di arredamento nell'immagine e crea un elenco.
2.  **Price-Agent**: Prende l'elenco degli articoli e fornisce un dettaglio dei prezzi, inclusi opzioni economiche, di fascia media e premium.
3.  **Quote-Agent**: Riceve l'elenco con i prezzi e lo formatta in un documento di preventivo formale in Markdown.

*Diagramma del workflow Sales -\> Price -\> Quote.*

#### Analisi dell'Implementazione in Python

Vengono definiti tre agenti, ciascuno con un ruolo specializzato. Il workflow viene costruito utilizzando `add_edge` per creare una catena: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

L'input è un `ChatMessage` che include sia testo che l'URI dell'immagine. Il framework gestisce il passaggio dell'output di ciascun agente al successivo nella sequenza fino a quando il preventivo finale viene generato.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# The user message contains both text and an image
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Run the workflow
async for event in workflow.run_stream(message):
    ...
```

#### Analisi dell'Implementazione in .NET (C\#)

L'esempio in .NET rispecchia la versione Python. Vengono creati tre agenti (`salesagent`, `priceagent`, `quoteagent`). Il `WorkflowBuilder` li collega in sequenza.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent priceagent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent quoteagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

Il messaggio dell'utente viene costruito con i dati dell'immagine (come byte) e il prompt testuale. Il metodo `InProcessExecution.StreamAsync` avvia il workflow, e l'output finale viene catturato dallo stream.

### Caso 3: Workflow Concorrenziale

Questo modello viene utilizzato quando i compiti possono essere eseguiti simultaneamente per risparmiare tempo. Include un "fan-out" verso più agenti e un "fan-in" per aggregare i risultati.

#### Contesto dello Scenario

Un utente chiede di pianificare un viaggio a Seattle.

1.  **Dispatcher (Fan-Out)**: La richiesta dell'utente viene inviata a due agenti contemporaneamente.
2.  **Researcher-Agent**: Ricerca attrazioni, meteo e considerazioni chiave per un viaggio a Seattle a dicembre.
3.  **Plan-Agent**: Crea indipendentemente un itinerario dettagliato giorno per giorno.
4.  **Aggregator (Fan-In)**: Gli output del ricercatore e del pianificatore vengono raccolti e presentati insieme come risultato finale.

*Diagramma del workflow concorrente Researcher e Planner.*

#### Analisi dell'Implementazione in Python

Il `ConcurrentBuilder` semplifica la creazione di questo modello. Basta elencare gli agenti partecipanti, e il builder crea automaticamente la logica necessaria per il fan-out e il fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Il framework garantisce che il `research_agent` e il `plan_agent` vengano eseguiti in parallelo, e i loro output finali vengono raccolti in un elenco.

#### Analisi dell'Implementazione in .NET (C\#)

In .NET, questo modello richiede una definizione più esplicita. Vengono creati executor personalizzati (`ConcurrentStartExecutor` e `ConcurrentAggregationExecutor`) per gestire la logica di fan-out e fan-in.

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

Il `WorkflowBuilder` utilizza `AddFanOutEdge` e `AddFanInEdge` per costruire il grafo con questi executor personalizzati e gli agenti.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Caso 4: Workflow Condizionale

I workflow condizionali introducono logica di ramificazione, permettendo al sistema di seguire percorsi diversi in base ai risultati intermedi.

#### Contesto dello Scenario

Questo workflow automatizza la creazione e la pubblicazione di un tutorial tecnico.

1.  **Evangelist-Agent**: Scrive una bozza del tutorial basandosi su un outline e URL forniti.
2.  **ContentReviewer-Agent**: Rivede la bozza. Controlla se il conteggio delle parole supera le 200.
3.  **Ramificazione Condizionale**:
      * **Se Approvato (`Yes`)**: Il workflow procede verso l'agente `Publisher-Agent`.
      * **Se Respinto (`No`)**: Il workflow si interrompe e fornisce il motivo del rifiuto.
4.  **Publisher-Agent**: Se la bozza è approvata, questo agente salva il contenuto in un file Markdown.

#### Analisi dell'Implementazione in Python

Questo esempio utilizza una funzione personalizzata, `select_targets`, per implementare la logica condizionale. Questa funzione viene passata a `add_multi_selection_edge_group` e dirige il workflow basandosi sul campo `review_result` dell'output del revisore.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# This function determines the next step based on the review result
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # If approved, proceed to the 'save_draft' executor
        return [save_draft_id]
    else:
        # If rejected, proceed to the 'handle_review' executor to report failure
        return [handle_review_id]

# The workflow builder uses the selection function for routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # The multi-selection edge implements the conditional logic
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Executor personalizzati come `to_reviewer_result` vengono utilizzati per analizzare l'output JSON degli agenti e convertirlo in oggetti fortemente tipizzati che la funzione di selezione può ispezionare.

#### Analisi dell'Implementazione in .NET (C\#)

La versione .NET utilizza un approccio simile con una funzione condizionale. Viene definito un `Func<object?, bool>` per controllare la proprietà `Result` dell'oggetto `ReviewResult`.

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

Il parametro `condition` del metodo `AddEdge` consente al `WorkflowBuilder` di creare un percorso ramificato. Il workflow seguirà l'edge verso `publishExecutor` solo se la condizione `GetCondition(expectedResult: "Yes")` restituisce true. Altrimenti, seguirà il percorso verso `sendReviewerExecutor`.

## Conclusione

Il Workflow del Microsoft Agent Framework fornisce una base robusta e flessibile per orchestrare sistemi complessi multi-agente. Sfruttando la sua architettura basata su grafi e i suoi componenti principali, gli sviluppatori possono progettare e implementare workflow sofisticati in Python e .NET. Che la tua applicazione richieda elaborazione sequenziale semplice, esecuzione parallela o logica condizionale dinamica, il framework offre gli strumenti per creare soluzioni AI potenti, scalabili e fortemente tipizzate.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.