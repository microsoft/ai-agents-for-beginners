# Explorarea Microsoft Agent Framework

![Agent Framework](../../../translated_images/ro/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introducere

Această lecție va acoperi:

- Înțelegerea Microsoft Agent Framework: Caracteristici cheie și valoare  
- Explorarea conceptelor cheie ale Microsoft Agent Framework
- Modele avansate MAF: Fluxuri de lucru, middleware și memorie

## Obiective de învățare

După finalizarea acestei lecții, veți ști cum să:

- Construiți agenți AI gata pentru producție folosind Microsoft Agent Framework
- Aplicați caracteristicile de bază ale Microsoft Agent Framework la cazurile dvs. de utilizare agentică
- Folosiți modele avansate incluzând fluxuri de lucru, middleware și observabilitate

## Exemple de cod 

Exemplele de cod pentru [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) pot fi găsite în acest depozit sub fișierele `xx-python-agent-framework` și `xx-dotnet-agent-framework`.

## Înțelegerea Microsoft Agent Framework

![Framework Intro](../../../translated_images/ro/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) este cadrul unificat al Microsoft pentru construirea agenților AI. Oferă flexibilitatea de a aborda o mare varietate de cazuri de utilizare agentică întâlnite în medii de producție și cercetare inclusiv:

- **Orchestrare secvențială a agenților** în scenarii unde sunt necesare fluxuri de lucru pas cu pas.
- **Orchestrare concurentă** în scenarii unde agenții trebuie să finalizeze sarcini în același timp.
- **Orchestrare conversație de grup** în scenarii unde agenții pot colabora împreună la o singură sarcină.
- **Orchestrare predare** în scenarii unde agenții predau sarcina unul altuia pe măsură ce sub-sarcinile sunt finalizate.
- **Orchestrare magnetică** în scenarii unde un agent manager creează și modifică o listă de sarcini și se ocupă de coordonarea subagenților pentru a finaliza sarcina.

Pentru a livra agenți AI în producție, MAF include și caracteristici pentru:

- **Observabilitate** prin utilizarea OpenTelemetry, unde fiecare acțiune a agentului AI inclusiv invocarea de unelte, pașii de orchestrare, fluxurile de raționament și monitorizarea performanței prin dashboard-urile Microsoft Foundry.
- **Securitate** prin găzduirea agenților nativ pe Microsoft Foundry care include controale de securitate precum acces bazat pe roluri, gestionarea datelor private și siguranță încorporată a conținutului.
- **Durabilitate** deoarece thread-urile și fluxurile de lucru ale agenților pot fi puse pe pauză, reluate și recuperate după erori permițând procese de durată mai lungă.
- **Control** deoarece sunt susținute fluxuri de lucru cu intervenție umană unde sarcinile sunt marcate ca necesitând aprobare umană.

Microsoft Agent Framework se concentrează, de asemenea, pe interoperabilitate prin:

- **Fiind agnostic față de cloud** - Agenții pot rula în containere, on-premises și pe mai multe cloud-uri diferite.
- **Fiind agnostic față de furnizor** - Agenții pot fi creați prin SDK-ul preferat, inclusiv Azure OpenAI și OpenAI.
- **Integrarea standardelor deschise** - Agenții pot utiliza protocoale precum Agent-to-Agent (A2A) și Model Context Protocol (MCP) pentru a descoperi și utiliza alți agenți și unelte.
- **Pluginuri și Conectori** - Se pot face conexiuni la servicii de date și memorie precum Microsoft Fabric, SharePoint, Pinecone și Qdrant.

Să vedem cum aceste caracteristici sunt aplicate la unele dintre conceptele de bază ale Microsoft Agent Framework.

## Concepte cheie ale Microsoft Agent Framework

### Agenți

![Agent Framework](../../../translated_images/ro/agent-components.410a06daf87b4fef.webp)

**Crearea Agenților**

Crearea agenților se face prin definirea serviciului de inferență (Furnizor LLM), 
un set de instrucțiuni pe care agentul AI trebuie să le urmeze și un `nume` asignat:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Exemplul de mai sus folosește `Azure OpenAI`, dar agenții pot fi creați folosind o varietate de servicii inclusiv `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

Aplicațiile OpenAI `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

sau [MiniMax](https://platform.minimaxi.com/), care oferă o API compatibilă cu OpenAI cu ferestre de context mare (până la 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

sau agenți de la distanță folosind protocolul A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Rularea Agenților**

Agenții se rulează folosind metodele `.run` sau `.run_stream` pentru răspunsuri fără streaming sau cu streaming.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Fiecare rulare a agentului poate de asemenea să includă opțiuni pentru personalizarea parametrilor precum `max_tokens` folosiți de agent, `tools` pe care agentul le poate apela și chiar `modelul` folosit de agent.

Acest lucru este util în cazurile în care sunt necesare modele sau unelte specifice pentru finalizarea sarcinii utilizatorului.

**Unelte**

Uneltele pot fi definite atât la definirea agentului:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Atunci când creați un ChatAgent direct

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

cât și la rularea agentului:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Unealtă furnizată doar pentru această rulare )
```

**Thread-uri Agent**

Thread-urile agent sunt folosite pentru a gestiona conversații cu multi-turnuri. Thread-urile pot fi create fie prin:

- Utilizarea `get_new_thread()` care permite salvarea thread-ului în timp
- Crearea automată a unui thread când agentul rulează, iar thread-ul există doar pe durata rulării curente.

Pentru a crea un thread, codul este acesta:

```python
# Creează un fir nou.
thread = agent.get_new_thread() # Rulează agentul cu firul.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Apoi poți serializa thread-ul pentru a fi stocat pentru utilizare ulterioară:

```python
# Creează un fir nou.
thread = agent.get_new_thread() 

# Rulează agentul cu firul.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializează firul pentru stocare.

serialized_thread = await thread.serialize() 

# Deserializează starea firului după încărcarea din stocare.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware Agent**

Agenții interacționează cu unelte și LLM-uri pentru a finaliza sarcinile utilizatorului. În anumite scenarii, dorim să executăm sau să urmărim acțiuni între aceste interacțiuni. Middleware-ul agentului ne permite să facem acest lucru prin:

*Middleware pentru Funcții*

Acest middleware ne permite să executăm o acțiune între agent și o funcție/unelte pe care agentul o va apela. Un exemplu de utilizare este când dorim să facem logarea apelului funcției.

În codul de mai jos, `next` definește dacă middleware-ul următor sau funcția propriu-zisă trebuie apelată.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pre-procesare: Înregistrare în jurnal înainte de execuția funcției
    print(f"[Function] Calling {context.function.name}")

    # Continuă la următorul middleware sau la execuția funcției
    await next(context)

    # Post-procesare: Înregistrare în jurnal după execuția funcției
    print(f"[Function] {context.function.name} completed")
```

*Middleware de Chat*

Acest middleware ne permite să executăm sau să logăm o acțiune între agent și cererile către LLM.

Acesta conține informații importante precum `mesajele` care sunt trimise către serviciul AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pre-procesare: Înregistrare înainte de apelul AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continuă la următorul middleware sau serviciu AI
    await next(context)

    # Post-procesare: Înregistrare după răspunsul AI
    print("[Chat] AI response received")

```

**Memoria Agentului**

După cum s-a discutat în lecția `Agentic Memory`, memoria este un element important care permite agentului să opereze pe contexte diferite. MAF oferă mai multe tipuri de memorii:

*Memorie în Memorie*

Aceasta este memoria stocată în thread-urile din timpul rulării aplicației.

```python
# Creează un fir nou.
thread = agent.get_new_thread() # Rulează agentul cu firul.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Mesaje Persistente*

Această memorie este folosită pentru stocarea istoricului conversațiilor peste diferite sesiuni. Este definită folosind `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Creează un depozit de mesaje personalizat
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Memorie Dinamică*

Această memorie este adăugată în context înainte ca agenții să ruleze. Aceste memorii pot fi stocate în servicii externe precum mem0:

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

Observabilitatea este importantă pentru construirea unor sisteme agentice fiabile și ușor de întreținut. MAF se integrează cu OpenTelemetry pentru a oferi trasabilitate și contorizare pentru o mai bună observabilitate.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # faci ceva
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Fluxuri de lucru

MAF oferă fluxuri de lucru care sunt pași predefiniți pentru completarea unei sarcini și care includ agenți AI ca componente ale acelor pași.

Fluxurile de lucru sunt alcătuite din diferite componente ce permit un control mai bun al fluxului. Fluxurile de lucru permit de asemenea **orchestrarea multi-agent** și **puncte de control** pentru salvarea stărilor fluxului de lucru.

Componentele de bază ale unui flux de lucru sunt:

**Executorii**

Executorii primesc mesaje de intrare, îndeplinesc sarcinile alocate și apoi produc un mesaj de ieșire. Aceasta mișcă fluxul de lucru către finalizarea sarcinii mai mari. Executorii pot fi fie agenți AI, fie logică personalizată.

**Muchii**

Muchiile sunt folosite pentru a defini fluxul de mesaje într-un flux de lucru. Acestea pot fi:

*Muchii directe* - Conexiuni simple unu-la-unu între executori:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Muchii condiționate* - Se activează după ce o condiție anume este îndeplinită. De exemplu, când nu sunt disponibile camere la hotel, un executor poate sugera alte opțiuni.

*Muchii switch-case* - Trimit mesaje către executori diferiți pe baza condițiilor definite. De exemplu, dacă clientul de călătorie are acces prioritar, sarcinile sale vor fi gestionate prin alt flux de lucru.

*Muchii fan-out* - Trimit un singur mesaj către mai multe destinații.

*Muchii fan-in* - Colectează mesaje multiple de la diferiți executori și le trimite unui singur țintă.

**Evenimente**

Pentru a oferi o observabilitate mai bună în fluxurile de lucru, MAF oferă evenimente încorporate pentru execuție incluzând:

- `WorkflowStartedEvent` - Execuția fluxului de lucru începe
- `WorkflowOutputEvent` - Fluxul de lucru produce un rezultat
- `WorkflowErrorEvent` - Fluxul de lucru întâmpină o eroare
- `ExecutorInvokeEvent` - Executorul începe procesarea
- `ExecutorCompleteEvent` - Executorul termină procesarea
- `RequestInfoEvent` - O cerere este emisă

## Modele avansate MAF

Secțiunile de mai sus acoperă conceptele cheie ale Microsoft Agent Framework. Pe măsură ce construiți agenți mai complexi, iată câteva modele avansate de luat în considerare:

- **Compoziția Middleware**: Legarea mai multor handleri middleware (logare, autentificare, limitare de rată) folosind middleware pentru funcții și chat pentru control fin al comportamentului agentului.
- **Puncte de control fluxuri de lucru**: Folosiți evenimentele fluxului de lucru și serializarea pentru a salva și relua procesele agentului de durată lungă.
- **Selecția dinamică a uneltelor**: Combinați RAG peste descrierile uneltelor cu înregistrarea uneltelor din MAF pentru a prezenta doar uneltele relevante pentru fiecare interogare.
- **Predarea multi-agent**: Folosiți muchiile fluxului de lucru și rutarea condiționată pentru a orchestra predările între agenți specializați.

## Găzduirea Agenților LangChain / LangGraph pe Microsoft Foundry

Microsoft Agent Framework este **interoperabil cu alte framework-uri** — nu sunteți limitați la agenți scriși cu MAF. Dacă aveți deja un agent construit cu **LangChain** sau **LangGraph**, îl puteți rula ca **agent găzduit pe Microsoft Foundry** astfel încât Foundry să gestioneze runtime-ul, sesiunile, scalarea, identitatea și endpoint-urile protocolului pentru dvs., în timp ce logica agentului rămâne în LangGraph.

Acest lucru se face cu pachetul `langchain_azure_ai.agents.hosting`, care expune un grafic LangGraph compilat peste aceleași protocoale pe care le folosesc agenții găzduiți Foundry.

**1. Instalați extra hosting:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Extra `hosting` instalează bibliotecile de protocol Foundry: `azure-ai-agentserver-responses` (endpoint-ul `/responses` compatibil OpenAI) și `azure-ai-agentserver-invocations` (endpoint-ul generic `/invocations`).

**2. Alegeți un protocol de hosting:**

| Protocol | Clasa de găzduire | Endpoint | Utilizare când |
|----------|------------------|----------|----------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Doriți chat compatibil OpenAI, streaming, istoric de răspunsuri și thread-uri de conversație — recomandarea implicită pentru agenții conversaționali. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Aveți nevoie de o formulă JSON personalizată, un endpoint webhook-style sau procesare non-conversatională. |

Deoarece **API-ul Responses este API-ul principal pentru dezvoltarea de agenți în Foundry**, începeți cu `ResponsesHostServer` pentru majoritatea agenților.

**3. Configurați variabilele de mediu** (`az login` mai întâi pentru ca `DefaultAzureCredential` să se poată autentifica):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Când agentul rulează ulterior ca agent găzduit în Foundry, platforma injectează automat `FOUNDRY_PROJECT_ENDPOINT`.

**4. Expuneți un agent LangGraph peste protocolul Responses:**

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

    # ChatOpenAI aici țintește endpoint-ul compatibil OpenAI (Responses) al proiectului Foundry.
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

Rulați-l local cu `python main.py`, apoi trimiteți o cerere Responses la `http://localhost:8088/responses`.

**Comportamente cheie:**

- **Conversații**: Clienții continuă o conversație trecând `previous_response_id` sau un ID de `conversation`. Dacă graficul este compilat cu LangGraph checkpointer, Foundry leagă starea conversației de checkpoint (folosiți un checkpointer durabil în producție; `MemorySaver` e potrivit pentru test local).
- **Human-in-the-loop**: Dacă graficul folosește LangGraph `interrupt()`, `ResponsesHostServer` afișează întreruperea în așteptare ca un element Responses `function_call` / `mcp_approval_request`, iar clienții reiau cu un `function_call_output` / `mcp_approval_response` corespunzător.
- **Deploy pe Foundry**: Folosiți Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (local, necesită Docker), apoi `azd provision` și `azd deploy`. Deploy-ul agentului găzduit necesită rolul **Foundry Project Manager**.

O versiune rulabilă a acestui exemplu este în [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pentru un ghid complet (protocol Invocations, scheme de cereri personalizate și depanare), vedeți [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Exemple de cod 

Exemple de cod pentru Microsoft Agent Framework pot fi găsite în acest depozit în fișierele `xx-python-agent-framework` și `xx-dotnet-agent-framework`.

## Aveți mai multe întrebări despre Microsoft Agent Framework?

Alăturați-vă [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la office hours și a vă primi răspunsurile la întrebările despre Agenții AI.
## Lecția precedentă

[Memoria pentru Agenții AI](../13-agent-memory/README.md)

## Lecția următoare

[Construirea Agenților de Utilizare a Calculatorului (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->