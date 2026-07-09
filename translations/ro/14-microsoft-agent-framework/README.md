# Explorarea Microsoft Agent Framework

![Agent Framework](../../../translated_images/ro/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introducere

Această lecție va acoperi:

- Înțelegerea Microsoft Agent Framework: Caracteristici cheie și valoare  
- Explorarea conceptelor cheie ale Microsoft Agent Framework
- Modele avansate MAF: fluxuri de lucru, middleware și memorie

## Obiective de învățare

După finalizarea acestei lecții, veți ști cum să:

- Construiți agenți AI gata de producție folosind Microsoft Agent Framework
- Aplicați caracteristicile de bază ale Microsoft Agent Framework la cazurile dvs. de utilizare agentic
- Utilizați modele avansate inclusiv fluxuri de lucru, middleware și observabilitate

## Exemple de cod 

Exemplele de cod pentru [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) pot fi găsite în acest depozit sub fișierele `xx-python-agent-framework` și `xx-dotnet-agent-framework`.

## Înțelegerea Microsoft Agent Framework

![Framework Intro](../../../translated_images/ro/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) este cadrul unificat Microsoft pentru construirea agenților AI. Oferă flexibilitate pentru a aborda o varietate largă de cazuri de utilizare agentic văzute atât în medii de producție, cât și de cercetare, inclusiv:

- **Orchestrare secvențială a agenților** în scenarii unde sunt necesare fluxuri de lucru pas cu pas.
- **Orchestrare concurentă** în scenarii unde agenții trebuie să finalizeze sarcini simultan.
- **Orchestrare de chat în grup** în scenarii unde agenții pot colabora împreună la o singură sarcină.
- **Orchestrare de predare** în scenarii unde agenții predau sarcina unul altuia pe măsură ce sub-sarcinile sunt finalizate.
- **Orchestrare magnetică** în scenarii unde un agent manager creează și modifică o listă de sarcini și se ocupă de coordonarea subagenților pentru a finaliza sarcina.

Pentru a livra agenți AI în producție, MAF include și caracteristici pentru:

- **Observabilitate** prin utilizarea OpenTelemetry unde fiecare acțiune a Agentului AI, inclusiv invocarea uneltei, pașii de orchestrare, fluxurile de raționament și monitorizarea performanței prin tablourile de bord Microsoft Foundry.
- **Securitate** prin găzduirea agenților în mod nativ pe Microsoft Foundry care include controale de securitate precum acces bazat pe rol, gestionarea datelor private și siguranță a conținutului încorporată.
- **Durabilitate** deoarece firele și fluxurile de lucru ale Agentului pot fi puse pauză, reluate și recuperate după erori, ceea ce permite procese de durată mai lungă.
- **Control** deoarece fluxurile de lucru cu intervenție umană sunt suportate unde sarcinile sunt marcate ca necesitând aprobare umană.

Microsoft Agent Framework se concentrează și pe interoperabilitate prin:

- **Faptul că nu este dependent de cloud** - Agenții pot rula în containere, on-premise și pe mai multe cloud-uri diferite.
- **Faptul că nu este dependent de furnizor** - Agenții pot fi creați prin SDK-ul preferat, inclusiv Azure OpenAI și OpenAI
- **Integrarea standardelor deschise** - Agenții pot utiliza protocoale precum Agent-to-Agent (A2A) și Model Context Protocol (MCP) pentru a descoperi și utiliza alți agenți și unelte.
- **Pluginuri și conectori** - Se pot face conexiuni către servicii de date și memorie precum Microsoft Fabric, SharePoint, Pinecone și Qdrant.

Să analizăm cum sunt aplicate aceste caracteristici unor concepte de bază ale Microsoft Agent Framework.

## Concepte cheie ale Microsoft Agent Framework

### Agenți

![Agent Framework](../../../translated_images/ro/agent-components.410a06daf87b4fef.webp)

**Crearea Agenților**

Crearea agentului se face prin definirea serviciului de inferență (furnizor LLM), un set
de instrucțiuni pe care Agentul AI trebuie să le urmeze, și un `name` atribuit:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Exemplul de mai sus folosește `Azure OpenAI` dar agenții pot fi creați folosind o varietate de servicii inclusiv `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, API-urile `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

sau [MiniMax](https://platform.minimaxi.com/), care oferă un API compatibil OpenAI cu ferestre contextuale mari (până la 204K tokeni):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

sau agenți la distanță folosind protocolul A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Rularea Agenților**

Agenții sunt rulați folosind metodele `.run` sau `.run_stream` pentru răspunsuri non-streaming sau streaming.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Fiecare rulare a agentului poate avea opțiuni pentru a personaliza parametri precum `max_tokens` utilizați de agent, `tools` pe care agentul le poate apela, și chiar `modelul` folosit pentru agent.

Acest lucru este util în cazurile în care sunt necesare modele sau unelte specifice pentru completarea sarcinii utilizatorului.

**Unelte**

Uneltele pot fi definite atât în momentul definirii agentului:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Când creați un ChatAgent direct

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

cât și atunci când se rulează agentul:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Instrument furnizat doar pentru această rulare )
```

**Fire ale Agentului**

Firele agentului sunt folosite pentru a gestiona conversații pe mai multe schimburi. Firele pot fi create fie prin:

- Folosind `get_new_thread()` care permite salvarea firului în timp
- Crearea automată a unui fir când agentul este rulat și păstrarea firului doar pe durata rulării curente.

Pentru a crea un fir, codul arată astfel:

```python
# Creează un fir nou.
thread = agent.get_new_thread() # Rulează agentul cu firul.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Apoi puteți serializa firul pentru a fi stocat pentru utilizare ulterioară:

```python
# Creează un fir nou.
thread = agent.get_new_thread() 

# Rulează agentul cu firul.

response = await agent.run("Hello, how are you?", thread=thread) 

# Seriaza firul pentru stocare.

serialized_thread = await thread.serialize() 

# Deseriază starea firului după încărcarea din stocare.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware pentru Agent**

Agenții interacționează cu unelte și LLM-uri pentru a finaliza sarcinile utilizatorului. În anumite scenarii, dorim să executăm sau să urmărim interacțiunile dintre acestea. Middleware-ul pentru agenți ne permite asta prin:

*Middleware de funcție*

Acest middleware ne permite să executăm o acțiune între agent și o funcție/unelte pe care o va apela. Un exemplu de utilizare este atunci când dorim să facem logare la apelul funcției.

În codul de mai jos `next` definește dacă middleware-ul următor sau funcția propriu-zisă trebuie apelată.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pre-procesare: Înregistrare înainte de execuția funcției
    print(f"[Function] Calling {context.function.name}")

    # Continuă la următorul middleware sau execuția funcției
    await next(context)

    # Post-procesare: Înregistrare după execuția funcției
    print(f"[Function] {context.function.name} completed")
```

*Middleware de chat*

Acest middleware ne permite să executăm sau să logăm o acțiune între agent și cererile către LLM.

Aceasta conține informații importante cum ar fi `messages` care sunt trimise către serviciul AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pre-procesare: Înregistrare înainte de apelul AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continuă către următorul middleware sau serviciu AI
    await next(context)

    # Post-procesare: Înregistrare după răspunsul AI
    print("[Chat] AI response received")

```

**Memoria Agentului**

După cum s-a acoperit în lecția `Agentic Memory`, memoria este un element important pentru a permite agentului să opereze pe diferite contexte. MAF oferă mai multe tipuri diferite de memorii:

*Stocare în memorie*

Aceasta este memoria stocată în fire pe durata rulării aplicației.

```python
# Creează un fir nou.
thread = agent.get_new_thread() # Rulează agentul cu firul.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Mesaje persistente*

Această memorie este folosită când se stochează istoricul conversațiilor între sesiuni diferite. Este definită folosind `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Creează un magazin de mesaje personalizat
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Memorie dinamică*

Această memorie este adăugată la context înainte ca agenții să fie rulați. Aceste memorii pot fi stocate în servicii externe cum ar fi mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Utilizarea Mem0 pentru capabilități avansate de memorie
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

**Observabilitatea Agentului**


Observabilitatea este importantă pentru construirea unor sisteme agentice fiabile și ușor de întreținut. MAF se integrează cu OpenTelemetry pentru a furniza urmărire și contoare pentru o observabilitate mai bună.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # fă ceva
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Fluxuri de lucru

MAF oferă fluxuri de lucru care sunt pași predefiniți pentru a finaliza o sarcină și includ agenți AI ca componente în acei pași.

Fluxurile de lucru sunt alcătuite din diferite componente care permit un control mai bun al fluxului. Fluxurile de lucru permit de asemenea **orchestrarea multi-agent** și **checkpointing-ul** pentru a salva stările fluxului de lucru.

Componentele de bază ale unui flux de lucru sunt:

**Executori**

Executorii primesc mesaje de intrare, își îndeplinesc sarcinile atribuite și apoi produc un mesaj de ieșire. Aceasta împinge fluxul de lucru înainte către finalizarea sarcinii mai mari. Executorii pot fi fie un agent AI, fie o logică personalizată.

**Margini (Edges)**

Marginile sunt folosite pentru a defini fluxul mesajelor într-un flux de lucru. Acestea pot fi:

*Margini directe* - Conexiuni simple unu-la-unu între executori:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Margini condiționale* - Se activează după ce o anumită condiție este îndeplinită. De exemplu, când camerele de hotel nu sunt disponibile, un executor poate sugera alte opțiuni.

*Margini switch-case* - Redirecționează mesajele către diferiți executori pe baza condițiilor definite. De exemplu, dacă clientul de travel are acces prioritar, sarcinile lui vor fi gestionate printr-un alt flux de lucru.

*Margini fan-out* - Trimit un mesaj către mai multe ținte.

*Margini fan-in* - Colectează mai multe mesaje de la diverși executori și le trimit către o țintă.

**Evenimente**

Pentru a oferi o observabilitate mai bună asupra fluxurilor de lucru, MAF oferă evenimente încorporate pentru execuție, inclusiv:

- `WorkflowStartedEvent`  - Execuția fluxului de lucru începe
- `WorkflowOutputEvent` - Fluxul de lucru produce o ieșire
- `WorkflowErrorEvent` - Fluxul de lucru întâmpină o eroare
- `ExecutorInvokeEvent`  - Executorul începe procesarea
- `ExecutorCompleteEvent`  -  Executorul termină procesarea
- `RequestInfoEvent` - Se emite o cerere

## Modele avansate MAF

Secțiunile de mai sus acoperă conceptele cheie ale Microsoft Agent Framework. Pe măsură ce construiești agenți mai complecși, iată câteva modele avansate de luat în considerare:

- **Compoziția Middleware**: Leagă mai mulți handleri middleware (logging, autentificare, limitare de rată) folosind funcții middleware și middleware pentru chat pentru un control detaliat al comportamentului agentului.
- **Checkpointing în Fluxul de lucru**: Folosește evenimente de workflow și serializare pentru a salva și relua procesele agentului de lungă durată.
- **Selecție dinamică a uneltelor**: Combină RAG peste descrierile uneltelor cu înregistrarea uneltelor în MAF pentru a prezenta doar uneltele relevante pentru fiecare interogare.
- **Transfer multi-agent**: Folosește marginile fluxului de lucru și rutarea condițională pentru a orchestra transferurile între agenți specializați.

## Găzduirea agenților LangChain / LangGraph pe Microsoft Foundry

Microsoft Agent Framework este **interoperabil în cadrul framework-urilor** — nu ești limitat la agenți scriși cu MAF. Dacă ai deja un agent construit cu **LangChain** sau **LangGraph**, îl poți rula ca un **agent găzduit Microsoft Foundry**, astfel încât Foundry să gestioneze runtime-ul, sesiunile, scalarea, identitatea și punctele finale de protocol pentru tine, în timp ce logica agentului tău rămâne în LangGraph.

Acest lucru se face cu pachetul `langchain_azure_ai.agents.hosting`, care expune un grafic compilat LangGraph prin aceleași protocoale pe care le folosesc agenții găzduiți Foundry.

**1. Instalează extra hosting:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Extra `hosting` instalează bibliotecile de protocol Foundry: `azure-ai-agentserver-responses` (endpoint-ul `/responses` compatibil OpenAI) și `azure-ai-agentserver-invocations` (endpoint-ul generic `/invocations`).

**2. Alege un protocol de hosting:**

| Protocol | Clasa host | Endpoint | Când să folosești |
|----------|------------|----------|------------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Vrei chat compatibil OpenAI, streaming, istoric de răspunsuri și threading de conversații — implicitul recomandat pentru agenții conversaționali. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Ai nevoie de o formă JSON personalizată, un endpoint de tip webhook sau procesare non-conversațională. |

Deoarece **Responses API este API-ul principal pentru dezvoltarea de agenți în Foundry**, începe cu `ResponsesHostServer` pentru majoritatea agenților.

**3. Configurează variabilele de mediu** (`az login` mai întâi pentru ca `DefaultAzureCredential` să se poată autentifica):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Când agentul va rula mai târziu ca agent găzduit în Foundry, platforma injectează automat `FOUNDRY_PROJECT_ENDPOINT`.

**4. Expune un agent LangGraph prin protocolul Responses:**

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-4.1")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI aici țintește punctul final (Responses) compatibil cu OpenAI al proiectului Foundry.
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

Rulează-l local cu `python main.py`, apoi trimite o cerere Responses la `http://localhost:8088/responses`.

**Comportamente cheie:**

- **Conversații**: Clienții continuă o conversație trecând `previous_response_id` sau un ID de `conversation`. Dacă graficul tău este compilat cu un checkpoint LangGraph, Foundry leagă starea conversației de checkpoint (folosește un checkpoint durabil în producție; `MemorySaver` e OK pentru testare locală).
- **Human-in-the-loop**: Dacă graficul tău folosește LangGraph `interrupt()`, `ResponsesHostServer` afișează întreruperea în așteptare ca un element `function_call` / `mcp_approval_request` Responses, iar clienții reiau cu un `function_call_output` / `mcp_approval_response` potrivit.
- **Dezvoltare pe Foundry**: Folosește Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (local, necesită Docker), apoi `azd provision` și `azd deploy`. Implementarea agentului găzduit necesită rolul **Foundry Project Manager**.

O versiune executabilă a acestui exemplu se găsește în [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pentru ghidul complet (protocol Invocations, scheme de cereri personalizate și depanare), vezi [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Exemple de cod 

Exemplele de cod pentru Microsoft Agent Framework pot fi găsite în acest depozit în fișierele `xx-python-agent-framework` și `xx-dotnet-agent-framework`.

## Ai mai multe întrebări despre Microsoft Agent Framework?

Alătură-te [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la sesiuni de consultanță și a primi răspunsuri la întrebările tale despre Agenții AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->