# Esplorando Microsoft Agent Framework

![Agent Framework](../../../translated_images/it/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introduzione

Questa lezione tratterà:

- Comprendere Microsoft Agent Framework: caratteristiche chiave e valore  
- Esplorare i concetti chiave di Microsoft Agent Framework
- Modelli avanzati MAF: Workflows, Middleware e Memoria

## Obiettivi di apprendimento

Dopo aver completato questa lezione, saprai come:

- Costruire agenti AI pronti per la produzione usando Microsoft Agent Framework
- Applicare le caratteristiche principali di Microsoft Agent Framework ai tuoi casi d'uso agentici
- Usare modelli avanzati inclusi workflows, middleware e osservabilità

## Esempi di codice 

Gli esempi di codice per [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) possono essere trovati in questo repository sotto i file `xx-python-agent-framework` e `xx-dotnet-agent-framework`.

## Comprendere Microsoft Agent Framework

![Framework Intro](../../../translated_images/it/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) è il framework unificato di Microsoft per la costruzione di agenti AI. Offre la flessibilità per affrontare la grande varietà di casi d'uso agentici visti sia in ambienti di produzione che di ricerca, inclusi:

- **Orchestrazione sequenziale** in scenari dove sono necessari workflow passo-passo.
- **Orchestrazione concorrente** in scenari in cui gli agenti devono completare compiti contemporaneamente.
- **Orchestrazione di chat di gruppo** in scenari in cui gli agenti possono collaborare insieme su un unico compito.
- **Orchestrazione di consegna** in scenari in cui gli agenti passano il compito l'uno all'altro man mano che i subtasks vengono completati.
- **Orchestrazione magnetica** in scenari in cui un agente manager crea e modifica una lista di compiti e gestisce il coordinamento di sottoagenti per completare il compito.

Per fornire agenti AI in produzione, MAF include anche funzionalità per:

- **Osservabilità** tramite l'uso di OpenTelemetry dove ogni azione dell'agente AI, inclusa l'invocazione degli strumenti, i passi di orchestrazione, i flussi di ragionamento e il monitoraggio delle prestazioni tramite dashboard Microsoft Foundry.
- **Sicurezza** ospitando agenti nativamente su Microsoft Foundry, che include controlli di sicurezza come accesso basato sui ruoli, gestione dei dati privati e sicurezza dei contenuti integrata.
- **Durabilità** in quanto i thread e i workflow degli agenti possono mettere in pausa, riprendere e recuperare dagli errori, permettendo processi a lungo termine.
- **Controllo** supportato da workflow con intervento umano dove i compiti sono contrassegnati come richiedenti approvazione umana.

Microsoft Agent Framework è anche focalizzato sull'interoperabilità tramite:

- **Essere cloud-agnostico** - Gli agenti possono girare in container, on-premise e su diversi cloud.
- **Essere provider-agnostico** - Gli agenti possono essere creati tramite il tuo SDK preferito, incluso Azure OpenAI e OpenAI.
- **Integrare standard aperti** - Gli agenti possono utilizzare protocolli come Agent-to-Agent (A2A) e Model Context Protocol (MCP) per scoprire e usare altri agenti e strumenti.
- **Plugin e connettori** - Connessioni possibili a servizi di dati e memoria come Microsoft Fabric, SharePoint, Pinecone e Qdrant.

Vediamo come queste funzionalità sono applicate ad alcuni dei concetti chiave di Microsoft Agent Framework.

## Concetti chiave di Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/it/agent-components.410a06daf87b4fef.webp)

**Creazione di Agenti**

La creazione di un agente avviene definendo il servizio di inferenza (fornitore LLM), un
insieme di istruzioni da seguire per l'agente AI, e un `name` assegnato:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

L'esempio sopra utilizza `Azure OpenAI` ma gli agenti possono essere creati utilizzando una varietà di servizi incluso `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

API OpenAI `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

o [MiniMax](https://platform.minimaxi.com/), che fornisce un'API compatibile OpenAI con finestre di contesto grandi (fino a 204K token):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

o agenti remoti usando il protocollo A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Esecuzione degli Agenti**

Gli agenti vengono eseguiti usando i metodi `.run` o `.run_stream` per risposte non streaming o in streaming.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Ogni esecuzione dell'agente può anche avere opzioni per personalizzare parametri come `max_tokens` utilizzati dall'agente, `tools` che l'agente è in grado di chiamare, e persino il `model` stesso utilizzato per l'agente.

Questo è utile in casi in cui sono richiesti modelli o strumenti specifici per completare un compito dell'utente.

**Strumenti**

Gli strumenti possono essere definiti sia al momento della definizione dell'agente:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Quando si crea direttamente un ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

e anche durante l'esecuzione dell'agente:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Strumento fornito solo per questa esecuzione )
```

**Thread degli Agenti**

I thread degli agenti sono usati per gestire conversazioni multi-turno. I thread possono essere creati in due modi:

- Usando `get_new_thread()` che permette al thread di essere salvato nel tempo
- Creando un thread automaticamente quando si esegue un agente con il thread che dura solo durante l'esecuzione corrente.

Per creare un thread, il codice è questo:

```python
# Crea un nuovo thread.
thread = agent.get_new_thread() # Esegui l'agente con il thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Puoi poi serializzare il thread per conservarlo e usarlo dopo:

```python
# Crea un nuovo thread.
thread = agent.get_new_thread() 

# Esegui l'agente con il thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializza il thread per l'archiviazione.

serialized_thread = await thread.serialize() 

# Deserializza lo stato del thread dopo il caricamento dall'archiviazione.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware degli Agenti**

Gli agenti interagiscono con strumenti e LLM per completare i compiti dell'utente. In certi scenari, vogliamo eseguire o tracciare ciò che avviene tra queste interazioni. Il middleware degli agenti ci permette di farlo tramite:

*Middleware per Funzioni*

Questo middleware ci permette di eseguire un'azione tra l'agente e una funzione/strumento che chiamerà. Un esempio di uso è quando si vuole fare il logging della chiamata della funzione.

Nel codice sotto `next` definisce se si deve chiamare il middleware successivo o la funzione effettiva.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pre-elaborazione: Registra prima dell'esecuzione della funzione
    print(f"[Function] Calling {context.function.name}")

    # Continua al prossimo middleware o all'esecuzione della funzione
    await next(context)

    # Post-elaborazione: Registra dopo l'esecuzione della funzione
    print(f"[Function] {context.function.name} completed")
```

*Middleware per Chat*

Questo middleware permette di eseguire o registrare un'azione tra l'agente e le richieste tra l'LLM.

Contiene informazioni importanti come i `messages` inviati al servizio AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pre-elaborazione: Registrazione prima della chiamata all'IA
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continua al middleware successivo o al servizio IA
    await next(context)

    # Post-elaborazione: Registrazione dopo la risposta dell'IA
    print("[Chat] AI response received")

```

**Memoria degli Agenti**

Come trattato nella lezione `Agentic Memory`, la memoria è un elemento importante per permettere all'agente di operare su contesti differenti. MAF offre diversi tipi di memorie:

*Memorizzazione in memoria volatile*

Questa è la memoria immagazzinata nei thread durante il runtime dell'applicazione.

```python
# Crea un nuovo thread.
thread = agent.get_new_thread() # Esegui l'agente con il thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Messaggi persistenti*

Questa memoria è usata per conservare la cronologia della conversazione tra sessioni diverse. È definita usando `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Crea un archivio di messaggi personalizzato
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Memoria dinamica*

Questa memoria viene aggiunta al contesto prima che gli agenti vengano eseguiti. Queste memorie possono essere conservate in servizi esterni come mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Utilizzo di Mem0 per funzionalità avanzate di memoria
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

**Osservabilità degli Agenti**

L'osservabilità è importante per costruire sistemi agentici affidabili e manutenibili. MAF si integra con OpenTelemetry per fornire tracing e metriche per una migliore osservabilità.

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

### Workflows

MAF offre workflows che sono passi predefiniti per completare un compito e includono agenti AI come componenti in quei passi.

I workflows sono composti da diversi componenti che permettono un migliore controllo del flusso. I workflows abilitano anche **orchestrazione multi-agente** e **checkpointing** per salvare stati del workflow.

I componenti centrali di un workflow sono:

**Esecutori**

Gli esecutori ricevono messaggi di input, eseguono i loro compiti assegnati e poi producono un messaggio di output. Questo muove il workflow verso il completamento del compito più grande. Gli esecutori possono essere agenti AI o logica personalizzata.

**Collegamenti (Edges)**

I collegamenti sono usati per definire il flusso dei messaggi in un workflow. Possono essere:

*Collegamenti Diretti* - Connessioni semplici uno a uno tra esecutori:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Collegamenti Condizionali* - Attivati dopo che una certa condizione è soddisfatta. Per esempio, quando non ci sono camere d'albergo disponibili, un esecutore può suggerire altre opzioni.

*Collegamenti Switch-case* - Inoltrano messaggi a esecutori diversi basati su condizioni definite. Per esempio, se un cliente di viaggio ha accesso prioritario, i suoi compiti saranno gestiti tramite un altro workflow.

*Collegamenti Fan-out* - Invia un messaggio a molteplici destinazioni.

*Collegamenti Fan-in* - Raccoglie molteplici messaggi da esecutori diversi e li invia a un unico destinatario.

**Eventi**

Per fornire una migliore osservabilità nei workflow, MAF offre eventi incorporati per l'esecuzione tra cui:

- `WorkflowStartedEvent`  - Inizio dell'esecuzione del workflow
- `WorkflowOutputEvent` - Il workflow produce un output
- `WorkflowErrorEvent` - Il workflow incontra un errore
- `ExecutorInvokeEvent`  - L'esecutore inizia il processamento
- `ExecutorCompleteEvent`  -  L'esecutore termina il processamento
- `RequestInfoEvent` - Viene effettuata una richiesta

## Modelli Avanzati MAF

Le sezioni sopra trattano i concetti chiave di Microsoft Agent Framework. Man mano che costruisci agenti più complessi, ecco alcuni modelli avanzati da considerare:

- **Composizione di Middleware**: Catena di diversi gestori middleware (logging, autenticazione, limitazione di velocità) usando middleware per funzione e per chat per un controllo granulare sul comportamento degli agenti.
- **Checkpointing del Workflow**: Usa eventi del workflow e serializzazione per salvare e riprendere processi agentici a lunga durata.
- **Selezione Dinamica degli Strumenti**: Combina RAG su descrizioni degli strumenti con la registrazione degli strumenti di MAF per presentare solo quelli rilevanti per ogni query.
- **Consegna Multi-Agente**: Usa collegamenti del workflow e instradamento condizionale per orchestrare passaggi tra agenti specializzati.

## Ospitare Agenti LangChain / LangGraph su Microsoft Foundry

Microsoft Agent Framework è **interoperabile tra framework** — non sei limitato ad agenti scritti con MAF. Se hai già un agente costruito con **LangChain** o **LangGraph**, puoi eseguirlo come **agente ospitato da Microsoft Foundry** così Foundry gestisce runtime, sessioni, scalabilità, identità e endpoint di protocollo per te, mentre la logica del tuo agente resta in LangGraph.

Questo viene fatto con il pacchetto `langchain_azure_ai.agents.hosting`, che espone un grafo compilato LangGraph sugli stessi protocolli usati dagli agenti ospitati Foundry.

**1. Installa la dipendenza hosting:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

La dipendenza `hosting` installa le librerie di protocollo Foundry: `azure-ai-agentserver-responses` (l'endpoint `/responses` compatibile OpenAI) e `azure-ai-agentserver-invocations` (l'endpoint generico `/invocations`).

**2. Scegli un protocollo di hosting:**

| Protocollo | Classe Host | Endpoint | Usare quando |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Vuoi chat compatibile OpenAI, streaming, cronologia risposte e threading conversazioni — il default raccomandato per agenti conversazionali. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Hai bisogno di uno schema JSON personalizzato, un endpoint stile webhook o processamento non conversazionale. |

Poiché **Responses API è l'API primaria per lo sviluppo di agenti in Foundry**, inizia con `ResponsesHostServer` per la maggior parte degli agenti.

**3. Configura le variabili d'ambiente** (`az login` prima affinché `DefaultAzureCredential` possa autenticarsi):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Quando l'agente gira come agente ospitato in Foundry, la piattaforma inietta automaticamente `FOUNDRY_PROJECT_ENDPOINT`.

**4. Esporre un agente LangGraph tramite il protocollo Responses:**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI qui punta all'endpoint (Responses) compatibile con OpenAI del progetto Foundry.
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

Eseguire in locale con `python main.py`, quindi inviare una richiesta Responses a `http://localhost:8088/responses`.

**Comportamenti chiave:**

- **Conversazioni**: I client continuano una conversazione passando `previous_response_id` o un ID `conversation`. Se il tuo grafo è compilato con un checkpointer LangGraph, Foundry associa lo stato della conversazione al checkpoint (usa un checkpointer durevole in produzione; `MemorySaver` va bene per test locali).
- **Intervento umano al ciclo**: Se il tuo grafo usa `interrupt()` di LangGraph, `ResponsesHostServer` presenta l'interruzione pendente come un elemento `function_call` / `mcp_approval_request` di Responses, e i client riprendono con un `function_call_output` / `mcp_approval_response` corrispondente.
- **Deploy su Foundry**: Usa Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (locale, richiede Docker), poi `azd provision` e `azd deploy`. Il deploy di agenti ospitati richiede il ruolo **Foundry Project Manager**.

Una versione eseguibile di questo esempio si trova in [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Per la guida completa (protocollo Invocations, schemi di richieste personalizzati e risoluzione problemi), vedi [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Esempi di codice 

Gli esempi di codice per Microsoft Agent Framework possono essere trovati in questo repository sotto i file `xx-python-agent-framework` e `xx-dotnet-agent-framework`.

## Hai altre domande su Microsoft Agent Framework?

Unisciti a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) per incontrare altri studenti, partecipare a sessioni di assistenza e ottenere risposte alle tue domande sugli agenti AI.
## Lezione precedente

[Memoria per agenti AI](../13-agent-memory/README.md)

## Lezione successiva

[Costruire agenti per uso del computer (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->