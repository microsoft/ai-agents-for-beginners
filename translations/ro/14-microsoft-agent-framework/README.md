# Explorarea Microsoft Agent Framework

![Agent Framework](../../../translated_images/ro/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introducere

Această lecție va acoperi:

- Înțelegerea Microsoft Agent Framework: Caracteristici cheie și valoare  
- Explorarea conceptele cheie ale Microsoft Agent Framework
- Modele avansate MAF: Fluxuri de lucru, middleware și memorie

## Obiectivele de învățare

După finalizarea acestei lecții, veți ști cum să:

- Construiți agenți AI gata de producție folosind Microsoft Agent Framework
- Aplicați caracteristicile de bază ale Microsoft Agent Framework pentru cazurile dvs. de utilizare agentică
- Utilizați modele avansate, inclusiv fluxuri de lucru, middleware și observabilitate

## Exemple de cod

Exemple de cod pentru [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) pot fi găsite în acest depozit sub fișierele `xx-python-agent-framework` și `xx-dotnet-agent-framework`.

## Înțelegerea Microsoft Agent Framework

![Framework Intro](../../../translated_images/ro/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) este cadrul unificat Microsoft pentru construirea de agenți AI. Oferă flexibilitate pentru a aborda o varietate largă de cazuri de utilizare agentice întâlnite atât în producție, cât și în mediile de cercetare, inclusiv:

- **Orchestrarea secvențială a agenților** în scenarii unde sunt necesare fluxuri de lucru pas cu pas.
- **Orchestrarea concurentă** în scenarii unde agenții trebuie să finalizeze sarcini în același timp.
- **Orchestrarea chat-ului de grup** în scenarii în care agenții pot colabora împreună la o singură sarcină.
- **Orchestrarea transferului** în scenarii în care agenții transferă sarcina între ei pe măsură ce subtasks sunt finalizate.
- **Orchestrarea magnetică** în scenarii în care un agent manager creează și modifică o listă de sarcini și se ocupă de coordonarea subagenților pentru a finaliza sarcina.

Pentru a livra agenți AI în producție, MAF include și caracteristici pentru:

- **Observabilitate** prin utilizarea OpenTelemetry unde fiecare acțiune a agentului AI, inclusiv invocarea unui instrument, pașii de orchestrare, fluxurile de raționament și monitorizarea performanței prin tablourile de bord Microsoft Foundry.
- **Securitate** găzduind agenții nativ pe Microsoft Foundry, care include controale de securitate precum acces bazat pe roluri, gestionarea datelor private și siguranța conținutului integrată.
- **Durabilitate** deoarece firele și fluxurile de lucru ale agenților pot fi puse în pauză, reluate și recuperate după erori, ceea ce permite procese de durată mai lungă.
- **Control** deoarece fluxurile de lucru cu intervenția umană sunt suportate, unde sarcinile sunt marcate ca necesitând aprobare umană.

Microsoft Agent Framework este, de asemenea, axat pe interoperabilitate prin:

- **Fiind agnostic față de cloud** - Agenții pot rula în containere, local sau pe mai multe clouduri diferite.
- **Fiind agnostic față de furnizor** - Agenții pot fi creați prin SDK-ul preferat, inclusiv Azure OpenAI și OpenAI.
- **Integrarea standardelor deschise** - Agenții pot utiliza protocoale precum Agent-to-Agent (A2A) și Model Context Protocol (MCP) pentru a descoperi și folosi alți agenți și instrumente.
- **Pluginuri și conectori** - Se pot face conexiuni la servicii de date și memorie, cum ar fi Microsoft Fabric, SharePoint, Pinecone și Qdrant.

Să vedem cum aceste caracteristici se aplică unor concepte cheie ale Microsoft Agent Framework.

## Concepte cheie ale Microsoft Agent Framework

### Agenți

![Agent Framework](../../../translated_images/ro/agent-components.410a06daf87b4fef.webp)

**Crearea Agenților**

Crearea agenților se face prin definirea serviciului de inferență (furnizor LLM),
un set de instrucțiuni pe care agentul AI trebuie să le urmeze și un `name` atribuit:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Exemplul de mai sus folosește `Azure OpenAI` dar agenții pot fi creați folosind o varietate de servicii, inclusiv `Microsoft Foundry Agent Service`:

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

sau [MiniMax](https://platform.minimaxi.com/), care oferă un API compatibil cu OpenAI, cu ferestre mari de context (până la 204K tokenuri):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

sau agenți la distanță folosind protocolul A2A:

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

Fiecare rulare de agent poate avea și opțiuni pentru personalizarea parametrilor, cum ar fi `max_tokens` folosit de agent, `tools` pe care agentul le poate apela și chiar `model` folosit pentru agent.

Acest lucru este util în cazurile în care sunt necesare modele sau instrumente specifice pentru finalizarea sarcinii utilizatorului.

**Instrumente**

Instrumentele pot fi definite atât în momentul definirii agentului:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Când creați un ChatAgent direct

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

cât și la rularea agentului:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Unealtă oferită doar pentru această execuție )
```

**Fire agenți**

Firele agenților sunt folosite pentru a gestiona conversații cu mai multe schimburi. Firele pot fi create fie prin:

- Folosirea `get_new_thread()` care permite salvarea firului în timp
- Crearea automată a unui fir când agentul este rulat, iar firul durează doar pentru sesiunea curentă.

Pentru a crea un fir, codul arată astfel:

```python
# Creează un nou fir.
thread = agent.get_new_thread() # Rulează agentul cu firul.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Apoi puteți serializa firul pentru a-l stoca și folosi mai târziu:

```python
# Creează un fir nou.
thread = agent.get_new_thread() 

# Rulează agentul cu firul.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializați firul pentru stocare.

serialized_thread = await thread.serialize() 

# Deserializați starea firului după încărcare din stocare.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware pentru agenți**

Agenții interacționează cu instrumentele și LLM-urile pentru a finaliza sarcinile utilizatorului. În anumite scenarii, dorim să executăm sau să urmărim interacțiunile dintre acestea. Middleware-ul agentului ne permite să facem acest lucru prin:

*Middleware funcțional*

Acest middleware ne permite să executăm o acțiune între agent și o funcție/instrument pe care îl va apela. Un exemplu de utilizare este când doriți să faceți logging pentru apelul funcției.

În codul de mai jos `next` definește dacă middleware-ul următor sau funcția efectivă trebuie apelate.

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

Acest middleware ne permite să executăm sau să înregistrăm o acțiune între agent și solicitările către LLM.

Aceasta conține informații importante, cum ar fi `messages` care sunt trimise serviciului AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pre-procesare: Log înainte de apelul AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continuă către următorul middleware sau serviciu AI
    await next(context)

    # Post-procesare: Log după răspunsul AI
    print("[Chat] AI response received")

```

**Memoria agentului**

Așa cum a fost acoperit în lecția `Agentic Memory`, memoria este un element important care permite agentului să funcționeze în contexte diferite. MAF oferă diferite tipuri de memorii:

*Stocarea în memorie*

Aceasta este memoria stocată în fire în timpul execuției aplicației.

```python
# Creează un fir nou.
thread = agent.get_new_thread() # Rulează agentul cu firul.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Mesaje persistente*

Această memorie este utilizată pentru a stoca istoricul conversațiilor între sesiunile diferite. Este definită folosind `chat_message_store_factory` :

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

*Memoria dinamică*

Această memorie este adăugată în context înainte ca agenții să fie rulați. Aceste memorii pot fi stocate în servicii externe precum mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Folosirea Mem0 pentru capabilități avansate de memorie
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

Observabilitatea este importantă pentru construirea de sisteme agentice fiabile și ușor de întreținut. MAF se integrează cu OpenTelemetry pentru a oferi trasabilitate și contoare pentru o observabilitate mai bună.

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

MAF oferă fluxuri de lucru care sunt pași predefiniți pentru a finaliza o sarcină și includ agenți AI ca componente în acești pași.

Fluxurile de lucru sunt realizate din diferite componente care permit un control mai bun al fluxului. De asemenea, fluxurile de lucru permit **orchestrare multi-agent** și **puncte de salvare** pentru a salva stările fluxului de lucru.

Componentele de bază ale unui flux de lucru sunt:

**Executori**

Executorii primesc mesaje de intrare, își realizează sarcinile atribuite și apoi produc un mesaj de ieșire. Aceasta avansează fluxul de lucru către finalizarea sarcinii mai mari. Executorii pot fi fie agenți AI, fie logică personalizată.

**Muchii**

Muchiile sunt folosite pentru a defini fluxul mesajelor într-un flux de lucru. Acestea pot fi:

*Muchii directe* - conexiuni simple unu-la-unu între executori:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Muchii condiționale* - activate după ce o anumită condiție este îndeplinită. De exemplu, când camerele de hotel nu sunt disponibile, un executor poate sugera alte opțiuni.

*Muchii switch-case* - direcționează mesajele către executori diferiți bazat pe condiții definite. De exemplu, dacă un client de călătorie are acces prioritar, sarcinile sa vor fi gestionate printr-un alt flux de lucru.

*Muchii fan-out* - Trimit un mesaj la mai multe ținte.

*Muchii fan-in* - Colectează mai multe mesaje de la executori diferiți și le trimite către o singură țintă.

**Evenimente**

Pentru a oferi o mai bună observabilitate în fluxurile de lucru, MAF oferă evenimente încorporate pentru execuție, inclusiv:

- `WorkflowStartedEvent`  - Execuția fluxului de lucru începe
- `WorkflowOutputEvent` - Fluxul de lucru produce un rezultat
- `WorkflowErrorEvent` - Fluxul de lucru întâmpină o eroare
- `ExecutorInvokeEvent`  - Executorul începe procesarea
- `ExecutorCompleteEvent`  - Executorul termină procesarea
- `RequestInfoEvent` - Este emisă o solicitare

## Modele avansate MAF

Secțiunile de mai sus acoperă conceptele cheie ale Microsoft Agent Framework. Pe măsură ce construiți agenți mai complecși, iată câteva modele avansate de luat în considerare:

- **Compoziția middleware-ului**: Succesiv multe gestionare middleware (logging, autentificare, limitarea ratei) folosind middleware funcțional și de chat pentru un control detaliat al comportamentului agentului.
- **Puncte de salvare pentru fluxuri de lucru**: Folosiți evenimentele fluxului de lucru și serializarea pentru a salva și relua procesele de durată ale agentului.
- **Selecția dinamică a instrumentelor**: Combinați RAG peste descrieri de instrumente cu înregistrarea instrumentelor din MAF pentru a prezenta doar instrumentele relevante pentru fiecare interogare.
- **Transfer multi-agent**: Folosiți muchiile fluxului de lucru și rutarea condiționată pentru a orchestra transferurile între agenți specializați.

## Exemple de cod

Exemplele de cod pentru Microsoft Agent Framework pot fi găsite în acest depozit sub fișierele `xx-python-agent-framework` și `xx-dotnet-agent-framework`.

## Aveți mai multe întrebări despre Microsoft Agent Framework?

Alăturați-vă [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, pentru a participa la sesiuni live și pentru a vă rezolva întrebările despre agenții AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->