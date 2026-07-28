# Esplorare Microsoft Agent Framework

![Agent Framework](../../../translated_images/it/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introduzione

Questa lezione tratterà:

- Comprendere Microsoft Agent Framework: Caratteristiche chiave e valore  
- Esplorare i concetti chiave di Microsoft Agent Framework
- Pattern avanzati MAF: Flussi di lavoro, middleware e memoria

## Obiettivi di apprendimento

Al termine di questa lezione, saprai come:

- Costruire agenti AI pronti per la produzione usando Microsoft Agent Framework
- Applicare le funzionalità principali di Microsoft Agent Framework ai tuoi casi d’uso agentici
- Usare pattern avanzati inclusi flussi di lavoro, middleware e osservabilità

## Esempi di codice 

Esempi di codice per [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) si trovano in questo repository sotto i file `xx-python-agent-framework` e `xx-dotnet-agent-framework`.

## Comprendere Microsoft Agent Framework

![Framework Intro](../../../translated_images/it/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) è il framework unificato di Microsoft per costruire agenti AI. Offre la flessibilità per affrontare la vasta gamma di casi d’uso agentici visti sia in produzione che in ambienti di ricerca, tra cui:

- **Orchestrazione sequenziale dell’agente** in scenari dove sono necessari flussi di lavoro passo dopo passo.
- **Orchestrazione concorrente** in scenari dove gli agenti devono completare attività contemporaneamente.
- **Orchestrazione di chat di gruppo** in scenari dove gli agenti possono collaborare insieme su un’unica attività.
- **Orchestrazione del passaggio di consegne** in scenari dove gli agenti si passano l’attività man mano che i sotto-compiti vengono completati.
- **Orchestrazione magnetica** in scenari dove un agente manager crea e modifica una lista di attività e gestisce il coordinamento dei sotto-agenti per completare l’attività.

Per fornire agenti AI in produzione, MAF include inoltre funzionalità per:

- **Osservabilità** tramite l’uso di OpenTelemetry dove ogni azione dell’agente AI, inclusa l’invocazione degli strumenti, i passaggi di orchestrazione, i flussi di ragionamento e il monitoraggio delle prestazioni attraverso i dashboard di Microsoft Foundry.
- **Sicurezza** ospitando agenti nativamente su Microsoft Foundry, che include controlli di sicurezza come accesso basato sui ruoli, gestione dei dati privati e sicurezza del contenuto integrata.
- **Durata** poiché i thread e i flussi di lavoro degli agenti possono essere messi in pausa, ripresi e recuperati da errori, permettendo processi di lunga durata.
- **Controllo** poiché i flussi di lavoro con partecipazione umana sono supportati, dove i compiti sono contrassegnati come richiedenti approvazione umana.

Microsoft Agent Framework si concentra inoltre sull’interoperabilità tramite:

- **Essere Cloud-agnostico** - Gli agenti possono girare in container, on-premise e su diversi cloud.
- **Essere Provider-agnostico** - Gli agenti possono essere creati attraverso il tuo SDK preferito, inclusi Azure OpenAI e OpenAI
- **Integrazione di standard aperti** - Gli agenti possono utilizzare protocolli quali Agent-to-Agent (A2A) e Model Context Protocol (MCP) per scoprire e usare altri agenti e strumenti.
- **Plugin e connettori** - Connessioni possono essere fatte con servizi di dati e memoria come Microsoft Fabric, SharePoint, Pinecone e Qdrant.

Vediamo come queste funzionalità si applicano ad alcuni dei concetti base di Microsoft Agent Framework.

## Concetti chiave di Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/it/agent-components.410a06daf87b4fef.webp)

**Creare Agenti**

La creazione di agenti avviene definendo il servizio di inferenza (fornitore LLM), un
insieme di istruzioni che l’agente AI deve seguire, e un `nome` assegnato:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

L’esempio sopra usa `Azure OpenAI` ma gli agenti possono essere creati usando vari servizi tra cui `Microsoft Foundry Agent Service`:

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

o [MiniMax](https://platform.minimaxi.com/), che offre un’API compatibile con OpenAI con finestre di contesto ampie (fino a 204K token):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

o agenti remoti usando il protocollo A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Eseguire Agenti**

Gli agenti sono eseguiti usando i metodi `.run` o `.run_stream` per risposte rispettivamente non in streaming o in streaming.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Ogni esecuzione dell’agente può avere opzioni per personalizzare parametri come `max_tokens` usati dall’agente, `tools` che l’agente può chiamare, e anche il `model` usato per l’agente.

Questo è utile in casi dove modelli o strumenti specifici sono richiesti per completare un compito dell’utente.

**Strumenti**

Gli strumenti possono essere definiti sia quando si definisce l’agente:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Quando si crea direttamente un ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

e anche quando si esegue l’agente:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Strumento fornito solo per questa esecuzione )
```

**Thread Agente**

I thread degli agenti sono usati per gestire conversazioni multi-turno. I thread possono essere creati tramite:

- Usare `get_new_thread()` che permette di salvare il thread nel tempo
- Creare un thread automaticamente quando si esegue un agente, e avere il thread solo durante l’esecuzione corrente.

Per creare un thread, il codice è come segue:

```python
# Crea un nuovo thread.
thread = agent.get_new_thread() # Esegui l'agente con il thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Puoi quindi serializzare il thread per archiviarlo e usarlo successivamente:

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

**Middleware Agente**

Gli agenti interagiscono con strumenti e LLM per completare i compiti degli utenti. In certi scenari vogliamo eseguire o tracciare le interazioni tra essi. Il middleware agente ci permette di fare questo tramite:

*Middleware Funzione*

Questo middleware ci consente di eseguire un’azione tra l’agente e una funzione/strumento che chiamerà. Un esempio di uso è per fare logging sulla chiamata alla funzione.

Nel codice qui sotto `next` definisce se deve essere chiamato il middleware successivo o la funzione effettiva.

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

*Middleware Chat*

Questo middleware ci consente di eseguire o registrare un’azione tra l’agente e le richieste tra l’LLM.

Questo contiene informazioni importanti come i `messages` che vengono inviati al servizio AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pre-elaborazione: registrare prima della chiamata AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continua al middleware successivo o al servizio AI
    await next(context)

    # Post-elaborazione: registrare dopo la risposta AI
    print("[Chat] AI response received")

```

**Memoria Agente**

Come trattato nella lezione `Memoria Agentica`, la memoria è un elemento importante per permettere all’agente di operare su diversi contesti. MAF offre diversi tipi di memoria:

*Memoria In-Memory*

Questa è la memoria immagazzinata nei thread durante il runtime dell’applicazione.

```python
# Crea un nuovo thread.
thread = agent.get_new_thread() # Esegui l'agente con il thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Messaggi Persistenti*

Questa memoria è usata per conservare la storia della conversazione attraverso diverse sessioni. È definita usando `chat_message_store_factory`:

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

*Memoria Dinamica*

Questa memoria è aggiunta al contesto prima che gli agenti vengano eseguiti. Queste memorie possono essere conservate in servizi esterni come mem0:

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

**Osservabilità Agente**

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

MAF offre flussi di lavoro che sono passaggi predefiniti per completare un’attività e includono agenti AI come componenti in quei passaggi.

I flussi di lavoro sono composti da diversi componenti che permettono un migliore controllo del flusso. I flussi di lavoro abilitano anche **orchestrazione multi-agente** e **checkpointing** per salvare stati dei flussi di lavoro.

I componenti base di un flusso di lavoro sono:

**Esecutori**

Gli esecutori ricevono messaggi di input, eseguono i compiti assegnati e poi producono un messaggio di output. Questo fa avanzare il flusso di lavoro verso il completamento del compito più grande. Gli esecutori possono essere un agente AI o logica personalizzata.

**Archi**

Gli archi sono usati per definire il flusso dei messaggi in un flusso di lavoro. Questi possono essere:

*Archi diretti* - Connessioni semplici uno-a-uno tra esecutori:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Archi condizionali* - Attivati quando si verifica una certa condizione. Per esempio, quando le camere d’albergo non sono disponibili, un esecutore può suggerire altre opzioni.

*Archi switch-case* - Instradano messaggi a diversi esecutori basati su condizioni definite. Per esempio, se un cliente di viaggi ha accesso prioritario, i suoi compiti saranno gestiti tramite un altro flusso di lavoro.

*Archi di fan-out* - Inviano un messaggio a più destinazioni.

*Archi di fan-in* - Raccolgono più messaggi da diversi esecutori e li inviano a una destinazione.

**Eventi**

Per offrire migliore osservabilità nei flussi di lavoro, MAF offre eventi built-in per l’esecuzione inclusi:

- `WorkflowStartedEvent`  - Inizio esecuzione flusso di lavoro
- `WorkflowOutputEvent` - Il flusso di lavoro produce un output
- `WorkflowErrorEvent` - Il flusso di lavoro incontra un errore
- `ExecutorInvokeEvent`  - L’esecutore inizia l’elaborazione
- `ExecutorCompleteEvent`  -  L’esecutore termina l’elaborazione
- `RequestInfoEvent` - Una richiesta viene emessa

## Pattern avanzati di MAF

Le sezioni precedenti coprono i concetti chiave di Microsoft Agent Framework. Quando costruisci agenti più complessi, ecco alcuni pattern avanzati da considerare:

- **Composizione Middleware**: Catena di più gestori middleware (logging, autenticazione, limitazione di velocità) usando middleware funzione e chat per un controllo fine del comportamento dell’agente.
- **Checkpointing del flusso di lavoro**: Usa eventi di flusso di lavoro e serializzazione per salvare e riprendere processi agentici di lunga durata.
- **Selezione dinamica degli strumenti**: Combina RAG sulle descrizioni degli strumenti con la registrazione degli strumenti di MAF per presentare solo gli strumenti rilevanti per ogni query.
- **Passaggio multi-agente**: Usa archi di flusso e instradamenti condizionali per orchestrare passaggi tra agenti specializzati.

## Ospitare agenti LangChain / LangGraph su Microsoft Foundry

Microsoft Agent Framework è **interoperabile tra framework** — non sei limitato ad agenti scritti con MAF. Se hai già un agente costruito con **LangChain** o **LangGraph**, puoi eseguirlo come **agente ospitato su Microsoft Foundry** così Foundry gestisce il runtime, sessioni, scalabilità, identità e endpoint di protocollo per te, mentre la logica del tuo agente rimane in LangGraph.

Questo si fa con il pacchetto `langchain_azure_ai.agents.hosting`, che espone un grafo LangGraph compilato sugli stessi protocolli usati dagli agenti ospitati di Foundry.

**1. Installa l’extra di hosting:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

L’extra `hosting` installa le librerie di protocollo Foundry: `azure-ai-agentserver-responses` (endpoint `/responses` compatibile con OpenAI) e `azure-ai-agentserver-invocations` (endpoint generico `/invocations`).

**2. Scegli un protocollo di hosting:**

| Protocollo | Classe Host | Endpoint | Uso quando |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Vuoi chat compatibile OpenAI, streaming, cronologia risposte e threading conversazionale – il valore predefinito raccomandato per agenti conversazionali. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Hai bisogno di una forma JSON personalizzata, un endpoint stile webhook, o elaborazione non conversazionale. |

Poiché **l’API Responses è l’API primaria per lo sviluppo agentico in Foundry**, inizia con `ResponsesHostServer` per la maggior parte degli agenti.

**3. Configura le variabili ambiente** (`az login` prima così `DefaultAzureCredential` può autenticare):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Quando l’agente gira successivamente come agente ospitato in Foundry, la piattaforma inietta automaticamente `FOUNDRY_PROJECT_ENDPOINT`.

**4. Esporre un agente LangGraph sul protocollo Responses:**

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

    # ChatOpenAI qui mira all'endpoint OpenAI-compatibile (Risposte) del progetto Foundry.
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

Eseguilo localmente con `python main.py`, poi invia una richiesta Responses a `http://localhost:8088/responses`.

**Comportamenti chiave:**

- **Conversazioni**: I client continuano una conversazione passando `previous_response_id` o un ID `conversation`. Se il tuo grafo è compilato con un LangGraph checkpointer, Foundry associa lo stato conversazione al checkpoint (usa un checkpointer duraturo in produzione; `MemorySaver` va bene per test locali).
- **Umano nel ciclo**: Se il tuo grafo usa LangGraph `interrupt()`, `ResponsesHostServer` mostra l’interruzione pendente come un oggetto `function_call` / `mcp_approval_request` di Responses, e i client riprendono con un `function_call_output` / `mcp_approval_response` corrispondente.
- **Deploy su Foundry**: Usa Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (locale, richiede Docker), poi `azd provision` e `azd deploy`. Il deployment agente ospitato richiede ruolo **Foundry Project Manager**.

Una versione eseguibile di questo esempio si trova in [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Per la guida completa (protocollo Invocations, schemi di richiesta personalizzati e risoluzione problemi), vedi [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Esempi di codice 

Esempi di codice per Microsoft Agent Framework si trovano in questo repository sotto i file `xx-python-agent-framework` e `xx-dotnet-agent-framework`.

## Hai altre domande su Microsoft Agent Framework?

Unisciti al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) per incontrare altri studenti, partecipare a office hours e ricevere risposte alle tue domande sugli agenti AI.
## Lezione precedente

[Memoria per agenti AI](../13-agent-memory/README.md)

## Lezione successiva

[Costruire agenti per uso computer (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->