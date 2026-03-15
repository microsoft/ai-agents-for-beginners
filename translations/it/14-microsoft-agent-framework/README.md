# Esplorando Microsoft Agent Framework

![Agent Framework](../../../translated_images/it/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introduzione

Questa lezione coprirà:

- Comprendere Microsoft Agent Framework: Caratteristiche chiave e valore  
- Esplorare i concetti chiave di Microsoft Agent Framework
- Pattern avanzati di MAF: Flussi di lavoro, middleware e memoria

## Obiettivi di apprendimento

Dopo aver completato questa lezione, saprai come:

- Costruire agenti AI pronti per la produzione utilizzando Microsoft Agent Framework
- Applicare le funzionalità principali di Microsoft Agent Framework ai tuoi casi d'uso agentici
- Usare pattern avanzati inclusi flussi di lavoro, middleware e osservabilità

## Esempi di codice

Gli esempi di codice per [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) si trovano in questo repository nei file `xx-python-agent-framework` e `xx-dotnet-agent-framework`.

## Comprendere Microsoft Agent Framework

![Framework Intro](../../../translated_images/it/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) è il framework unificato di Microsoft per costruire agenti AI. Offre la flessibilità per affrontare la grande varietà di casi d'uso agentici osservati sia in ambienti di produzione che di ricerca, inclusi:

- **Orchestrazione sequenziale degli agenti** in scenari dove sono necessari flussi di lavoro passo-passo.
- **Orchestrazione concorrente** in scenari dove gli agenti devono completare i compiti contemporaneamente.
- **Orchestrazione di chat di gruppo** in scenari dove gli agenti possono collaborare insieme su un unico compito.
- **Orchestrazione di passaggio** in scenari dove gli agenti si passano il compito man mano che i sotto-compiti sono completati.
- **Orchestrazione magnetica** in scenari dove un agente manager crea e modifica una lista di compiti e gestisce il coordinamento dei sotto-agenti per completare il lavoro.

Per erogare Agenti AI in Produzione, MAF include anche funzionalità per:

- **Osservabilità** tramite l'uso di OpenTelemetry dove ogni azione dell'agente AI, inclusa l'invocazione degli strumenti, i passaggi di orchestrazione, i flussi di ragionamento e il monitoraggio delle prestazioni attraverso i dashboard di Microsoft Foundry.
- **Sicurezza** ospitando gli agenti nativamente su Microsoft Foundry che include controlli di sicurezza quali accesso basato sui ruoli, gestione dei dati privati e sicurezza del contenuto integrata.
- **Durabilità** poiché i thread e i flussi di lavoro degli agenti possono mettere in pausa, riprendere e riprendersi dagli errori, consentendo processi di lunga durata.
- **Controllo** con workflow human-in-the-loop che supportano compiti contrassegnati come richiedenti approvazione umana.

Microsoft Agent Framework si focalizza inoltre sull'interoperabilità tramite:

- **Essere cloud-agnostico** - Gli agenti possono girare in container, on-premise e su molteplici cloud differenti.
- **Essere provider-agnostico** - Gli agenti possono essere creati tramite il tuo SDK preferito, inclusi Azure OpenAI e OpenAI.
- **Integrare standard aperti** - Gli agenti possono utilizzare protocolli come Agent-to-Agent (A2A) e Model Context Protocol (MCP) per scoprire e usare altri agenti e strumenti.
- **Plugin e connettori** - Connessioni possono essere create a servizi di dati e memoria quali Microsoft Fabric, SharePoint, Pinecone e Qdrant.

Guardiamo come queste funzionalità sono applicate ad alcuni dei concetti chiave di Microsoft Agent Framework.

## Concetti chiave di Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/it/agent-components.410a06daf87b4fef.webp)

**Creare Agenti**

La creazione di agenti si effettua definendo il servizio di inferenza (Provider LLM), un
insieme di istruzioni per l'agente AI da seguire, e un `nome` assegnato:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Quanto sopra usa `Azure OpenAI` ma gli agenti possono essere creati usando diversi servizi inclusi `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, API `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

o agenti remoti usando il protocollo A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Eseguire Agenti**

Gli agenti sono eseguiti con i metodi `.run` o `.run_stream` per risposte non in streaming o in streaming.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Ogni esecuzione dell'agente può anche avere opzioni per personalizzare parametri come `max_tokens` usati dall'agente, `tools` che l'agente può chiamare, e persino il `model` usato dall'agente.

Questo è utile nei casi in cui siano necessari modelli o strumenti specifici per completare il compito dell'utente.

**Strumenti**

Gli strumenti possono essere definiti sia al momento della definizione dell'agente:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Quando si crea direttamente un ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

sia al momento di eseguire l'agente:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Strumento fornito solo per questa esecuzione )
```

**Thread degli Agenti**

I thread degli agenti sono usati per gestire conversazioni multi-turno. I thread possono essere creati in due modi:

- Usando `get_new_thread()` che permette al thread di essere salvato nel tempo
- Creando un thread automaticamente quando si esegue un agente, e il thread dura solo durante l’esecuzione corrente.

Per creare un thread, il codice è il seguente:

```python
# Crea un nuovo thread.
thread = agent.get_new_thread() # Esegui l'agente con il thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Si può quindi serializzare il thread per conservarlo ad uso successivo:

```python
# Crea un nuovo thread.
thread = agent.get_new_thread() 

# Esegui l'agente con il thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializza il thread per l'archiviazione.

serialized_thread = await thread.serialize() 

# Deserializza lo stato del thread dopo il caricamento dall'archivio.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware degli Agenti**

Gli agenti interagiscono con strumenti e LLM per completare i compiti degli utenti. In certi scenari, vogliamo eseguire o tracciare azioni durante queste interazioni. Il middleware degli agenti ci permette di farlo tramite:

*Middleware per Funzioni*

Questo middleware consente di eseguire un'azione tra l'agente e una funzione/strumento che l'agente chiamerà. Un esempio di utilizzo è fare del logging sulla chiamata della funzione.

Nel codice seguente `next` definisce se chiamare il middleware successivo o la funzione vera e propria.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pre-elaborazione: Registrare prima dell'esecuzione della funzione
    print(f"[Function] Calling {context.function.name}")

    # Continua al middleware successivo o all'esecuzione della funzione
    await next(context)

    # Post-elaborazione: Registrare dopo l'esecuzione della funzione
    print(f"[Function] {context.function.name} completed")
```

*Middleware per Chat*

Questo middleware ci consente di eseguire o registrare un’azione tra l’agente e le richieste all'LLM.

Contiene informazioni importanti quali i `messages` inviati al servizio AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pre-elaborazione: registra prima della chiamata all'IA
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continua al middleware o servizio IA successivo
    await next(context)

    # Post-elaborazione: registra dopo la risposta dell'IA
    print("[Chat] AI response received")

```

**Memoria Agente**

Come trattato nella lezione `Agentic Memory`, la memoria è un elemento importante per consentire all'agente di operare su diversi contesti. MAF offre diversi tipi di memoria:

*Memoria In-Memory*

Questa è la memoria conservata nei thread durante l'esecuzione dell'applicazione.

```python
# Crea un nuovo thread.
thread = agent.get_new_thread() # Esegui l'agente con il thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Messaggi Persistenti*

Questa memoria è usata per conservare la cronologia delle conversazioni tra sessioni differenti. È definita usando la `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Crea un archivio messaggi personalizzato
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Memoria Dinamica*

Questa memoria è aggiunta al contesto prima che gli agenti vengano eseguiti. Queste memorie possono essere conservate in servizi esterni come mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Utilizzo di Mem0 per funzionalità di memoria avanzate
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**Osservabilità dell’Agente**

L’osservabilità è importante per costruire sistemi agentici affidabili e manutenibili. MAF si integra con OpenTelemetry per fornire tracing e metriche per una migliore osservabilità.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # fare qualcosa
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Flussi di lavoro

MAF offre flussi di lavoro che sono passaggi predefiniti per completare un compito e includono agenti AI come componenti in quei passaggi.

I flussi di lavoro sono composti da diversi componenti che permettono un miglior controllo del flusso. I flussi di lavoro abilitano inoltre **orchestrazione multi-agente** e **checkpointing** per salvare stati del flusso.

I componenti principali di un flusso di lavoro sono:

**Esecutori**

Gli esecutori ricevono messaggi di input, eseguono i compiti assegnati, e poi producono un messaggio di output. Questo fa avanzare il flusso di lavoro verso il completamento del compito più ampio. Gli esecutori possono essere agenti AI o logica personalizzata.

**Archi**

Gli archi sono usati per definire il flusso dei messaggi in un flusso di lavoro. Questi possono essere:

*Archi Diretti* - Connessioni semplici uno-a-uno tra esecutori:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Archi Condizionali* - Attivati dopo che una certa condizione è soddisfatta. Per esempio, quando camere d'albergo non sono disponibili, un esecutore può suggerire altre opzioni.

*Archi Switch-case* - Instradano messaggi a diversi esecutori basati su condizioni definite. Per esempio, se un cliente viaggiatore ha accesso prioritario e i suoi compiti saranno gestiti tramite un altro flusso di lavoro.

*Archi Fan-out* - Invia un messaggio a più destinatari.

*Archi Fan-in* - Raccoglie messaggi da diversi esecutori e li invia ad un solo destinatario.

**Eventi**

Per fornire migliore osservabilità nei flussi di lavoro, MAF offre eventi integrati per l’esecuzione tra cui:

- `WorkflowStartedEvent`  - Inizio dell'esecuzione del flusso di lavoro
- `WorkflowOutputEvent` - Il flusso di lavoro produce un output
- `WorkflowErrorEvent` - Il flusso di lavoro incontra un errore
- `ExecutorInvokeEvent`  - L’esecutore inizia l’elaborazione
- `ExecutorCompleteEvent`  -  L’esecutore termina l’elaborazione
- `RequestInfoEvent` - Una richiesta viene emessa

## Pattern avanzati di MAF

Le sezioni sopra trattano i concetti chiave di Microsoft Agent Framework. Man mano che costruisci agenti più complessi, ecco alcuni pattern avanzati da considerare:

- **Composizione Middleware**: Collegare più gestori di middleware (logging, auth, rate-limiting) usando middleware per funzione e chat per un controllo granulare sul comportamento dell’agente.
- **Checkpointing dei flussi di lavoro**: Usare eventi di flusso di lavoro e serializzazione per salvare e riprendere processi agentici di lunga durata.
- **Selezione dinamica degli strumenti**: Combinare RAG sulle descrizioni degli strumenti con la registrazione degli strumenti di MAF per presentare solo gli strumenti rilevanti per query.
- **Passaggio multi-agente**: Usare archi di flusso di lavoro e instradamento condizionale per orchestrare passaggi tra agenti specializzati.

## Esempi di codice

Gli esempi di codice per Microsoft Agent Framework si trovano in questo repository nei file `xx-python-agent-framework` e `xx-dotnet-agent-framework`.

## Hai altre domande su Microsoft Agent Framework?

Unisciti al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare alle office hours e ottenere risposte alle tue domande sugli agenti AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->