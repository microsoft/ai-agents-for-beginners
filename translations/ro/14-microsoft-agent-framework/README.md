# Explorarea Microsoft Agent Framework

![Agent Framework](../../../translated_images/ro/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introducere

Această lecție va acoperi:

- Înțelegerea Microsoft Agent Framework: Caracteristici cheie și valoare  
- Explorarea conceptelor cheie ale Microsoft Agent Framework
- Modele avansate MAF: Fluxuri de lucru, Middleware și Memorie

## Obiective de învățare

După finalizarea acestei lecții, veți ști cum să:

- Construiți agenți AI pregătiți pentru producție folosind Microsoft Agent Framework
- Aplicați caracteristicile de bază ale Microsoft Agent Framework pentru cazurile dumneavoastră de utilizare agentică
- Folosiți modele avansate inclusiv fluxuri de lucru, middleware și observabilitate

## Exemple de cod

Exemplele de cod pentru [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) pot fi găsite în acest depozit sub fișierele `xx-python-agent-framework` și `xx-dotnet-agent-framework`.

## Înțelegerea Microsoft Agent Framework

![Framework Intro](../../../translated_images/ro/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) este cadrul unificat al Microsoft pentru construirea agenților AI. Oferă flexibilitatea de a aborda o gamă largă de cazuri de utilizare agentică întâlnite atât în medii de producție, cât și de cercetare, inclusiv:

- **Orchestrarea secvențială a agenților** în scenarii în care sunt necesare fluxuri de lucru pas cu pas.
- **Orchestrarea concurentă** în scenarii în care agenții trebuie să realizeze sarcini în același timp.
- **Orchestrarea chat-ului de grup** în scenarii unde agenții pot colabora împreună la o singură sarcină.
- **Orchestrarea transmiterii** în scenarii în care agenții transferă sarcina unul altuia pe măsură ce subtasks sunt finalizate.
- **Orchestrarea magnetică** în scenarii unde un agent manager creează și modifică o listă de sarcini și gestionează coordonarea subagenților pentru a finaliza sarcina.

Pentru a livra agenți AI în producție, MAF include și funcții pentru:

- **Observabilitate** prin utilizarea OpenTelemetry unde fiecare acțiune a agentului AI, inclusiv invocarea instrumentelor, pașii de orchestrare, fluxurile de raționament și monitorizarea performanței prin dashboard-urile Microsoft Foundry.
- **Securitate** prin găzduirea nativă a agenților pe Microsoft Foundry, care include controale de securitate precum accesul bazat pe roluri, gestionarea datelor private și siguranța conținutului integrată.
- **Durabilitate** deoarece firele agenților și fluxurile de lucru pot fi puse pe pauză, reluate și recuperate din erori, ceea ce permite procese mai lungi.
- **Control** deoarece fluxurile de lucru cu implicarea umană sunt suportate unde sarcinile sunt marcate ca necesitând aprobare umană.

Microsoft Agent Framework este, de asemenea, concentrat pe interoperabilitate prin:

- **Fiind Cloud-agnostic** - Agenții pot rula în containere, on-premise și pe mai multe cloud-uri diferite.
- **Fiind Provider-agnostic** - Agenții pot fi creați prin SDK-ul preferat, inclusiv Azure OpenAI și OpenAI
- **Integrarea standardelor deschise** - Agenții pot utiliza protocoale precum Agent-to-Agent (A2A) și Model Context Protocol (MCP) pentru a descoperi și utiliza alți agenți și instrumente.
- **Plugin-uri și Conectori** - Se pot realiza conexiuni cu servicii de date și memorie precum Microsoft Fabric, SharePoint, Pinecone și Qdrant.

Să vedem cum se aplică aceste caracteristici pentru unele dintre conceptele de bază ale Microsoft Agent Framework.

## Concepte Cheie ale Microsoft Agent Framework

### Agenți

![Agent Framework](../../../translated_images/ro/agent-components.410a06daf87b4fef.webp)

**Crearea Agenților**

Crearea agentului se face prin definirea serviciului de inferență (Furnizor LLM), un
set de instrucțiuni pe care agentul AI să le urmeze, și un `nume` atribuit:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Mai sus se folosește `Azure OpenAI`, dar agenții pot fi creați folosind o varietate de servicii, inclusiv `Microsoft Foundry Agent Service`:

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

sau [MiniMax](https://platform.minimaxi.com/), care oferă un API compatibil OpenAI cu ferestre context mari (până la 204K de tokeni):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

sau agenți remoti folosind protocolul A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Executarea Agenților**

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

Fiecare rulare a agentului poate avea și opțiuni pentru personalizarea parametrilor precum `max_tokens` folosit de agent, `tools` pe care agentul le poate apela și chiar `modelul` folosit de agent.

Acest lucru este util în cazurile în care sunt necesare modele sau instrumente specifice pentru finalizarea sarcinii utilizatorului.

**Instrumente**

Instrumentele pot fi definite atât la definirea agentului:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Când creezi un ChatAgent direct

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

cât și la rularea agentului:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Instrument furnizat doar pentru această rulare )
```

**Fire de Agent**

Firele de agent sunt folosite pentru a gestiona conversații cu mai multe schimburi. Firele pot fi create fie prin:

- Folosirea `get_new_thread()` care permite păstrarea firului în timp
- Crearea automată a unui fir când este rulat un agent și păstrarea firului doar pe durata rulării curente.

Pentru a crea un fir, codul arată așa:

```python
# Creează un fir nou.
thread = agent.get_new_thread() # Rulează agentul cu firul.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Apoi poți serializa firul pentru a fi stocat pentru utilizare ulterioară:

```python
# Creează un fir de execuție nou.
thread = agent.get_new_thread() 

# Rulează agentul cu firul de execuție.

response = await agent.run("Hello, how are you?", thread=thread) 

# Seriază firul de execuție pentru stocare.

serialized_thread = await thread.serialize() 

# Deserializează starea firului după încărcarea din stocare.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware de Agent**

Agenții interacționează cu instrumente și LLM-uri pentru a îndeplini sarcinile utilizatorului. În anumite scenarii, dorim să executăm sau să urmărim între aceste interacțiuni. Middleware-ul agentului ne permite acest lucru prin:

*Middleware funcțional*

Acest middleware ne permite să executăm o acțiune între agent și o funcție/instrument pe care acesta îl va apela. Un exemplu când ar fi folosit este pentru a face logare la apelul funcției.

În codul de mai jos `next` definește dacă middleware-ul următor sau funcția propriu-zisă trebuie apelată.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pre-procesare: Înregistrare înainte de execuția funcției
    print(f"[Function] Calling {context.function.name}")

    # Continuă către următorul middleware sau execuția funcției
    await next(context)

    # Post-procesare: Înregistrare după execuția funcției
    print(f"[Function] {context.function.name} completed")
```

*Middleware pentru chat*

Acest middleware ne permite să executăm sau să logăm o acțiune între agent și cererile dintre LLM.

Acesta conține informații importante precum `messages` care sunt trimise către serviciul AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Preprocesare: Înregistrare înainte de apelul AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continuă la următorul middleware sau serviciu AI
    await next(context)

    # Postprocesare: Înregistrare după răspunsul AI
    print("[Chat] AI response received")

```

**Memoria Agentului**

După cum s-a discutat în lecția `Agentic Memory`, memoria este un element important pentru a permite agentului să opereze pe contexte diferite. MAF oferă mai multe tipuri diferite de memorii:

*Stocare în memorie*

Aceasta este memoria stocată în fire pe durata rulării aplicației.

```python
# Creează un fir nou.
thread = agent.get_new_thread() # Rulează agentul cu firul.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Mesaje persistente*

Această memorie este folosită la stocarea istoricului conversațiilor pe diferite sesiuni. Este definită folosind `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Creează un magazin personalizat pentru mesaje
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Memorie dinamică*

Această memorie este adăugată în context înainte ca agenții să fie rulați. Aceste memorii pot fi stocate în servicii externe precum mem0:

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

Observabilitatea este importantă pentru construirea unor sisteme agentice fiabile și ușor de întreținut. MAF se integrează cu OpenTelemetry pentru a oferi trasare și contoare pentru o mai bună observabilitate.

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

### Fluxuri de Lucru

MAF oferă fluxuri de lucru care sunt pași predefiniți pentru a finaliza o sarcină și includ agenți AI ca componente ale acestor pași.

Fluxurile de lucru sunt compuse din diferite componente care permit un control mai bun al fluxului. Fluxurile de lucru permit și **orchestrarea multi-agent** și **checkpointing** pentru a salva stările fluxului de lucru.

Componentele de bază ale unui flux de lucru sunt:

**Executorii**

Executorii primesc mesaje de intrare, realizează sarcinile atribuite și apoi produc un mesaj de ieșire. Aceasta face ca fluxul de lucru să avanseze spre finalizarea sarcinii mari. Executorii pot fi fie agenți AI, fie logică personalizată.

**Muchii (Edges)**

Muchiile sunt folosite pentru a defini fluxul mesajelor într-un flux de lucru. Acestea pot fi:

*Muchii directe* - Conexiuni simple unu-la-unu între executori:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Muchii condiționale* - Activate după ce o anumită condiție este îndeplinită. De exemplu, când camerele la hotel nu sunt disponibile, un executor poate sugera alte opțiuni.

*Muchii tip switch-case* - Redirectează mesajele către diferiți executori pe baza condițiilor definite. De exemplu, dacă un client de călătorii are acces prioritar, sarcinile lui vor fi gestionate printr-un alt flux de lucru.

*Muchii fan-out* - Trimit un mesaj către mai multe ținte.

*Muchii fan-in* - Colectează mai multe mesaje de la diferiți executori și le trimite către o țintă.

**Evenimente**

Pentru a oferi o mai bună observabilitate asupra fluxurilor de lucru, MAF oferă evenimente încorporate pentru execuție, inclusiv:

- `WorkflowStartedEvent`  - Execuția fluxului de lucru începe
- `WorkflowOutputEvent` - Fluxul de lucru produce un output
- `WorkflowErrorEvent` - Fluxul de lucru întâmpină o eroare
- `ExecutorInvokeEvent`  - Executorul începe procesarea
- `ExecutorCompleteEvent`  -  Executorul termină procesarea
- `RequestInfoEvent` - O cerere este emisă

## Modele Avansate MAF

Secțiunile de mai sus acoperă conceptele cheie ale Microsoft Agent Framework. Pe măsură ce construiți agenți mai complecși, iată câteva modele avansate de luat în considerare:

- **Compoziția Middleware**: Lanțuiți mai mulți handleri middleware (logare, autentificare, limitare de rată) folosind middleware funcțional și de chat pentru un control foarte detaliat al comportamentului agentului.
- **Checkpointing în fluxurile de lucru**: Folosiți evenimentele fluxurilor de lucru și serializarea pentru a salva și relua procesele de agent pe durate lungi.
- **Selecția dinamică a instrumentelor**: Combinați RAG peste descrierile instrumentelor cu înregistrarea instrumentelor MAF pentru a prezenta doar instrumentele relevante per interogare.
- **Transmisie multi-agent**: Folosiți muchiile fluxului de lucru și rutarea condiționată pentru a orchestra transmisia între agenți specializați.

## Găzduirea Agenților LangChain / LangGraph pe Microsoft Foundry

Microsoft Agent Framework este **interoperabil cu alte cadre** — nu sunteți limitat la agenți scriși cu MAF. Dacă aveți deja un agent construit cu **LangChain** sau **LangGraph**, îl puteți rula ca un **agent găzduit Microsoft Foundry** astfel încât Foundry să gestioneze runtime-ul, sesiunile, scalarea, identitatea și punctele finale de protocol pentru dumneavoastră, în timp ce logica agentului rămâne în LangGraph.

Acest lucru se face cu pachetul `langchain_azure_ai.agents.hosting`, care expune un grafic LangGraph compilat prin aceleași protocoale folosite de agenții găzduiți Foundry.

**1. Instalați extra pentru găzduire:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Extra `hosting` instalează bibliotecile protocolului Foundry: `azure-ai-agentserver-responses` (punct final OpenAI-compatible `/responses`) și `azure-ai-agentserver-invocations` (punctul final generic `/invocations`).

**2. Alegeți un protocol de găzduire:**

| Protocol | Clasa host | Punct final | Când se folosește |
|----------|-----------|-------------|-------------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Doriți chat compatibil OpenAI, streaming, istoric de răspuns și fire de conversație — opțiunea recomandată implicită pentru agenții conversaționali. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Aveți nevoie de un format JSON personalizat, un punct final tip webhook sau procesare non-conversațională. |

Deoarece **API-ul Responses este principalul API pentru dezvoltarea agenților în stil Foundry**, începeți cu `ResponsesHostServer` pentru majoritatea agenților.

**3. Configurați variabilele de mediu** (`az login` mai întâi pentru ca `DefaultAzureCredential` să poată autentifica):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Când agentul funcționează ulterior ca agent găzduit în Foundry, platforma injectează automat `FOUNDRY_PROJECT_ENDPOINT`.

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

Rulați-l local cu `python main.py`, apoi trimiteți o cerere Responses către `http://localhost:8088/responses`.

**Comportamente cheie:**

- **Conversații**: Clienții continuă o conversație trecând `previous_response_id` sau un ID de `conversation`. Dacă graficul dvs. este compilat cu un LangGraph checkpointer, Foundry leagă starea conversației de checkpoint (folosiți un checkpointer durabil în producție; `MemorySaver` este ok pentru teste locale).
- **Om în buclă (human-in-the-loop)**: Dacă graficul dvs. folosește LangGraph `interrupt()`, `ResponsesHostServer` expune întreruperea în așteptare ca un item de tip `function_call` / `mcp_approval_request` în Responses, iar clienții reiau cu `function_call_output` / `mcp_approval_response` corespunzător.
- **Dezvoltați pe Foundry**: Folosiți Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (local, necesită Docker), apoi `azd provision` și `azd deploy`. Implementarea agenților găzduiți necesită rolul **Foundry Project Manager**.

O versiune rulabilă a acestui exemplu se găsește în [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pentru ghidul complet (protocolul Invocations, scheme de cereri personalizate și depanare), vedeți [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Exemple de cod

Exemplele de cod pentru Microsoft Agent Framework pot fi găsite în acest depozit sub fișierele `xx-python-agent-framework` și `xx-dotnet-agent-framework`.

## Aveți Mai Multe Întrebări Despre Microsoft Agent Framework?

Alăturați-vă [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la orele de program și a primi răspunsuri la întrebările despre agenții AI.
## Lecția Anterioară

[Memoria pentru Agenții AI](../13-agent-memory/README.md)

## Lecția Următoare

[Construirea Agenților de Utilizare a Calculatorului (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->