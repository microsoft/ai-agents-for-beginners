# Explorarea Microsoft Agent Framework

![Agent Framework](../../../translated_images/ro/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introducere

Această lecție va acoperi:

- Înțelegerea Microsoft Agent Framework: caracteristici cheie și valoare  
- Explorarea conceptelor cheie ale Microsoft Agent Framework
- Modele avansate MAF: fluxuri de lucru, middleware și memorie

## Obiective de învățare

După finalizarea acestei lecții, veți ști cum să:

- Creați agenți AI pregătiți pentru producție folosind Microsoft Agent Framework
- Aplicați caracteristicile de bază ale Microsoft Agent Framework în cazurile dvs. de utilizare agentică
- Utilizați modele avansate inclusiv fluxuri de lucru, middleware și observabilitate

## Exemple de cod 

Exemplele de cod pentru [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) pot fi găsite în acest depozit sub fișierele `xx-python-agent-framework` și `xx-dotnet-agent-framework`.

## Înțelegerea Microsoft Agent Framework

![Framework Intro](../../../translated_images/ro/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) este cadrul unificat al Microsoft pentru construirea agenților AI. Oferă flexibilitatea de a aborda o varietate largă de cazuri de utilizare agentică întâlnite atât în producție, cât și în medii de cercetare, inclusiv:

- **Orchestrarea secvențială a agenților** în scenarii în care sunt necesare fluxuri de lucru pas cu pas.
- **Orchestrarea concurentă** în scenarii în care agenții trebuie să îndeplinească sarcini simultan.
- **Orchestrarea în grup de chat** în scenarii în care agenții pot colabora împreună la o singură sarcină.
- **Orchestrarea transferului** în scenarii în care agenții predau sarcina unul altuia pe măsură ce subtask-urile sunt finalizate.
- **Orchestrarea magnetică** în scenarii în care un agent manager creează și modifică o listă de sarcini și coordonează subagenții pentru a finaliza sarcina.

Pentru a livra agenți AI în producție, MAF include și caracteristici pentru:

- **Observabilitate** prin utilizarea OpenTelemetry unde fiecare acțiune a agentului AI, inclusiv invocarea uneltelor, pașii de orchestrare, fluxurile de raționament și monitorizarea performanței prin panourile Microsoft Foundry.
- **Securitate** prin găzduirea agenților nativ pe Microsoft Foundry care include controale de securitate cum ar fi accesul bazat pe roluri, gestionarea datelor private și siguranța conținutului încorporată.
- **Durabilitate** deoarece firele și fluxurile de lucru ale agenților pot fi puse pe pauză, reluate și recuperate după erori, ceea ce permite procese mai lungi.
- **Control** deoarece sunt suportate fluxuri de lucru cu intervenția umană unde sarcinile sunt marcate ca necesitând aprobarea unui om.

Microsoft Agent Framework este, de asemenea, axat pe interoperabilitate prin:

- **Fiind cloud-agnostic** - Agenții pot rula în containere, on-premise și pe mai multe cloud-uri diferite.
- **Fiind provider-agnostic** - Agenții pot fi creați prin SDK-ul preferat, inclusiv Azure OpenAI și OpenAI.
- **Integrarea standardelor deschise** - Agenții pot utiliza protocoale precum Agent-to-Agent (A2A) și Model Context Protocol (MCP) pentru a descoperi și folosi alți agenți și unelte.
- **Plugin-uri și conectori** - Se pot realiza conexiuni la servicii de date și memorie precum Microsoft Fabric, SharePoint, Pinecone și Qdrant.

Să vedem cum sunt aplicate aceste caracteristici unor dintre conceptele cheie ale Microsoft Agent Framework.

## Concepte cheie ale Microsoft Agent Framework

### Agenți

![Agent Framework](../../../translated_images/ro/agent-components.410a06daf87b4fef.webp)

**Crearea agenților**

Crearea unui agent se face definind serviciul de inferență (furnizorul LLM), un
set de instrucțiuni pe care agentul AI trebuie să le urmeze și un `name` atribuit:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Cel de mai sus folosește `Azure OpenAI`, dar agenții pot fi creați folosind o varietate de servicii, inclusiv `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

API-urile OpenAI `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

sau [MiniMax](https://platform.minimaxi.com/), care oferă un API compatibil OpenAI cu ferestre mari de context (până la 204K tokeni):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

sau agenți la distanță folosind protocolul A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Rularea agenților**

Agenții sunt rulați folosind metodele `.run` sau `.run_stream` pentru răspunsuri fără streaming sau cu streaming.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Fiecare rulare a agentului poate avea opțiuni pentru personalizarea parametrilor precum `max_tokens` folosit de agent, `tools` pe care agentul le poate apela și chiar `model`ul folosit pentru agent.

Acest lucru este util în cazurile în care sunt necesare modele sau unelte specifice pentru a finaliza sarcina utilizatorului.

**Unelte**

Uneltele pot fi definite atât la definirea agentului:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Când creați direct un ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

cât și la rularea agentului:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Instrument oferit doar pentru această execuție )
```

**Fire de execuție ale agentului (Agent Threads)**

Firele de execuție ale agentului sunt folosite pentru a gestiona conversații multi-turn. Firele pot fi create fie prin:

- Folosirea `get_new_thread()` care permite salvarea firului în timp
- Crearea automată a unui fir când rulezi un agent și firul durează doar pe durata rulării curente.

Pentru a crea un fir, codul arată astfel:

```python
# Creează un fir nou.
thread = agent.get_new_thread() # Rulează agentul cu firul.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Poți apoi să serializezi firul pentru a-l stoca pentru utilizare ulterioară:

```python
# Creează un fir nou.
thread = agent.get_new_thread() 

# Rulează agentul cu firul.

response = await agent.run("Hello, how are you?", thread=thread) 

# Seriază firul pentru stocare.

serialized_thread = await thread.serialize() 

# Deserializează starea firului după încărcarea din stocare.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware pentru agenți**

Agenții interacționează cu uneltele și LLM-urile pentru a finaliza sarcinile utilizatorului. În anumite scenarii, dorim să executăm sau să urmărim aceste interacțiuni între ele. Middleware-ul pentru agenți ne permite să facem asta prin:

*Middleware pentru funcții*

Acest middleware ne permite să executăm o acțiune între agent și o funcție/unealtă pe care o va apela. Un exemplu de utilizare este când vrem să facem jurnalizare asupra apelului funcției.

În codul de mai jos `next` definește dacă middleware-ul următor sau funcția propriu-zisă trebuie apelată.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pre-procesare: Log înainte de execuția funcției
    print(f"[Function] Calling {context.function.name}")

    # Continuați la următorul middleware sau execuția funcției
    await next(context)

    # Post-procesare: Log după execuția funcției
    print(f"[Function] {context.function.name} completed")
```

*Middleware pentru chat*

Acest middleware ne permite să executăm sau să jurnalizăm o acțiune între agent și cererile dintre LLM .

Acesta conține informații importante cum ar fi `messages` care sunt trimise către serviciul AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pre-procesare: Jurnal înainte de apelul AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continuă către următorul middleware sau serviciu AI
    await next(context)

    # Post-procesare: Jurnal după răspunsul AI
    print("[Chat] AI response received")

```

**Memoria agentului**

Așa cum am acoperit în lecția `Agentic Memory`, memoria este un element important pentru a permite agentului să opereze în contexte diferite. MAF oferă mai multe tipuri diferite de memorii:

*Stocare în memorie (In-Memory Storage)*

Aceasta este memoria stocată în fire în timpul rulării aplicației.

```python
# Creează un nou fir.
thread = agent.get_new_thread() # Rulează agentul cu firul.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Mesaje persistente*

Această memorie este folosită pentru stocarea istoricului conversației prin diferite sesiuni. Este definită folosind `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Creează un magazin personalizat de mesaje
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Memoria dinamică*

Această memorie este adăugată în context înainte ca agenții să fie rulați. Aceste memorii pot fi stocate în servicii externe precum mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Folosind Mem0 pentru capabilități avansate de memorie
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

**Observabilitatea agentului**

Observabilitatea este importantă pentru construirea sistemelor agentice fiabile și ușor de întreținut. MAF se integrează cu OpenTelemetry pentru a oferi trasări și contoare pentru observabilitate mai bună.

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

### Fluxuri de lucru (Workflows)

MAF oferă fluxuri de lucru care sunt pași predefiniți pentru finalizarea unei sarcini și includ agenți AI ca componente în acești pași.

Fluxurile de lucru sunt compuse din diferite componente care permit un control mai bun al fluxului. Fluxurile de lucru permit, de asemenea, **orchestrarea multi-agent** și **checkpointing-ul** pentru a salva stările fluxurilor de lucru.

Componentele de bază ale unui flux de lucru sunt:

**Executanți (Executors)**

Executanții primesc mesaje de intrare, realizează sarcinile atribuite, apoi produc un mesaj de ieșire. Acest lucru împinge fluxul de lucru spre finalizarea sarcinii mai mari. Executanții pot fi fie agenți AI, fie logică personalizată.

**Conexiuni (Edges)**

Conexiunile sunt folosite pentru a defini fluxul mesajelor într-un flux de lucru. Acestea pot fi:

*Conexiuni directe* - Conexiuni simple unu-la-unu între executanți:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Conexiuni condiționate* - Se activează după ce o condiție anume este îndeplinită. De exemplu, când camerele de hotel nu sunt disponibile, un executant poate sugera alte opțiuni.

*Conexiuni tip switch-case* - Direcționează mesajele către executanți diferiți bazat pe condiții definite. De exemplu, dacă un client de travel are acces prioritar, sarcinile sale vor fi gestionate printr-un alt flux de lucru.

*Conexiuni fan-out* - Trimite un mesaj către mai multe ținte.

*Conexiuni fan-in* - Colectează mesaje multiple de la executanți diferiți și le trimite către o singură țintă.

**Evenimente (Events)**

Pentru a oferi o observabilitate mai bună în fluxurile de lucru, MAF oferă evenimente încorporate pentru execuție, inclusiv:

- `WorkflowStartedEvent`  - Execuția fluxului de lucru începe
- `WorkflowOutputEvent` - Fluxul de lucru produce un rezultat
- `WorkflowErrorEvent` - Fluxul de lucru întâmpină o eroare
- `ExecutorInvokeEvent`  - Executantul începe procesarea
- `ExecutorCompleteEvent`  - Executantul termină procesarea
- `RequestInfoEvent` - O cerere este emisă

## Modele avansate MAF

Secțiunile de mai sus acoperă conceptele cheie ale Microsoft Agent Framework. Pe măsură ce construiți agenți mai complecși, iată câteva modele avansate de luat în considerare:

- **Compoziția middleware-ului**: Lanțuiți mai mulți handleri de middleware (logging, autentificare, limitarea ratei) folosind middleware pentru funcții și chat pentru un control în detaliu al comportamentului agentului.
- **Checkpointing în fluxurile de lucru**: Folosiți evenimentele fluxului de lucru și serializarea pentru a salva și relua procesele agenților de durată lungă.
- **Selecția dinamică a uneltelor**: Combinați RAG peste descrierile uneltelor cu înregistrarea uneltelor din MAF pentru a prezenta doar uneltele relevante la cerere.
- **Transfer multi-agent**: Folosiți conexiunile fluxurilor de lucru și rutarea condiționată pentru a orchestra transferurile între agenți specializați.

## Găzduirea agenților LangChain / LangGraph pe Microsoft Foundry

Microsoft Agent Framework este **interoperabil cu alte cadre** — nu sunteți limitați la agenții scriși cu MAF. Dacă aveți deja un agent construit cu **LangChain** sau **LangGraph**, îl puteți rula ca **agent găzduit de Microsoft Foundry** astfel încât Foundry să se ocupe de runtime, sesiuni, scalare, identitate și endpoint-uri de protocol pentru dvs., în timp ce logica agentului rămâne în LangGraph.

Acest lucru se face cu pachetul `langchain_azure_ai.agents.hosting`, care expune un graf LangGraph compilat prin aceleași protocoale pe care le folosesc agenții găzduiți Foundry.

**1. Instalați extensia de găzduire:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Extensia `hosting` instalează bibliotecile de protocoale Foundry: `azure-ai-agentserver-responses` (endpoint-ul `/responses` compatibil OpenAI) și `azure-ai-agentserver-invocations` (endpoint-ul generic `/invocations`).

**2. Alegeți un protocol de găzduire:**

| Protocol | Clasă host | Endpoint | Când să folosești |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Doriți chat compatibil OpenAI, streaming, istoric al răspunsurilor și fire de conversație — implicitul recomandat pentru agenții conversaționali. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Aveți nevoie de o formă JSON personalizată, un endpoint în stil webhook sau procesare neconversațională. |

Deoarece **Responses API este API-ul principal pentru dezvoltarea de agenți în Foundry**, începeți cu `ResponsesHostServer` pentru majoritatea agenților.

**3. Configurați variabilele de mediu** (`az login` mai întâi pentru ca `DefaultAzureCredential` să se autentifice):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Când agentul rulează mai târziu ca agent găzduit în Foundry, platforma injectează automat `FOUNDRY_PROJECT_ENDPOINT`.

**4. Expuneți un agent LangGraph prin protocolul Responses:**

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

    # ChatOpenAI aici vizează punctul final compatibil OpenAI (Răspunsuri) al proiectului Foundry.
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

Rulați local cu `python main.py`, apoi trimiteți o cerere Responses către `http://localhost:8088/responses`.

**Comportamente cheie:**

- **Conversații**: Clienții continuă o conversație trecând `previous_response_id` sau un ID de `conversation`. Dacă graful dvs. este compilat cu un checkpointer LangGraph, Foundry leagă starea conversației de checkpoint (folosiți un checkpointer durabil în producție; `MemorySaver` este OK pentru testare locală).
- **Intervenția umană**: Dacă graful folosește LangGraph `interrupt()`, `ResponsesHostServer` afișează întreruperea în așteptare ca un element Responses `function_call` / `mcp_approval_request`, iar clienții reiau cu un `function_call_output` / `mcp_approval_response` corespunzător.
- **Deploiere în Foundry**: Folosiți Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (local, necesită Docker), apoi `azd provision` și `azd deploy`. Deploierea agentului găzduit necesită rolul **Foundry Project Manager**.

O versiune rulabilă a acestui exemplu se găsește în [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pentru tutorialul complet (protocolul Invocations, scheme personalizate de cereri și depanare), consultați [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Exemple de cod 

Exemplele de cod pentru Microsoft Agent Framework pot fi găsite în acest depozit sub fișierele `xx-python-agent-framework` și `xx-dotnet-agent-framework`.

## Aveți mai multe întrebări despre Microsoft Agent Framework?

Alăturați-vă [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la ore de birou și a primi răspunsuri la întrebările despre Agenții AI.
## Lecția anterioară

[Memoria pentru agenții AI](../13-agent-memory/README.md)

## Lecția următoare

[Construirea agenților de utilizare a calculatorului (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->