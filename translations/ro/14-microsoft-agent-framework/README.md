# Explorarea Microsoft Agent Framework

![Componente ale Agent Framework](../../../translated_images/ro/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introducere

Această lecție va acoperi:

- Înțelegerea Microsoft Agent Framework: Funcții cheie și valoare  
- Explorarea conceptelor cheie ale Microsoft Agent Framework
- Modele avansate MAF: Fluxuri de lucru, Middleware și Memorie

## Obiective de învățare

După parcurgerea acestei lecții, veți ști cum să:

- Creați agenți AI pregătiți pentru producție folosind Microsoft Agent Framework
- Aplicați funcțiile de bază ale Microsoft Agent Framework la cazurile dvs. de utilizare agentice
- Utilizați modele avansate, inclusiv fluxuri de lucru, middleware și observabilitate

## Exemple de cod 

Code samples for [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) can be found in this repository under `xx-python-agent-framework` and `xx-dotnet-agent-framework` files.

## Înțelegerea Microsoft Agent Framework

![Introducere în Framework](../../../translated_images/ro/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) este cadrul unificat al Microsoft pentru construirea agenților AI. Oferă flexibilitatea de a aborda o mare varietate de cazuri de utilizare agentice întâlnite atât în producție, cât și în medii de cercetare, inclusiv:

- **Orchestrare secvențială a agenților** în scenarii unde sunt necesare fluxuri de lucru pas cu pas.
- **Orchestrare concurentă** în scenarii în care agenții trebuie să finalizeze sarcini în același timp.
- **Orchestrare pentru chat de grup** în scenarii în care agenții pot colabora împreună la o singură sarcină.
- **Orchestrare de predare (Handoff)** în scenarii în care agenții predau sarcina unul altuia pe măsură ce sub-sarcinile sunt finalizate.
- **Orchestrare Magnetică** în scenarii în care un agent manager creează și modifică o listă de sarcini și se ocupă de coordonarea subagenților pentru a finaliza sarcina.

Pentru a livra agenți AI în producție, MAF include de asemenea funcționalități pentru:

- **Observabilitate** prin utilizarea OpenTelemetry, unde fiecare acțiune a agentului AI, inclusiv invocarea instrumentelor, pașii de orchestrare, fluxurile de raționament și monitorizarea performanței prin tablourile Microsoft Foundry.
- **Securitate** prin găzduirea agenților nativ pe Microsoft Foundry, care include controale de securitate precum acces bazat pe roluri, gestionarea datelor private și securitate integrată a conținutului.
- **Durabilitate** deoarece firele și fluxurile de lucru ale agenților pot fi întrerupte, reluate și recuperate după erori, ceea ce permite procese care rulează mai mult timp.
- **Control** deoarece fluxurile de lucru cu participarea umană sunt acceptate, unde sarcinile sunt marcate ca necesitând aprobarea umană.

Microsoft Agent Framework se concentrează, de asemenea, pe interoperabilitate prin:

- **Fiind agnostic față de cloud** - Agenții pot rula în containere, on-premises și pe diferite cloud-uri.
- **Fiind agnostic față de furnizor** - Agenții pot fi creați prin SDK-ul preferat, inclusiv Azure OpenAI și OpenAI
- **Integrarea standardelor deschise** - Agenții pot utiliza protocoale precum Agent-to-Agent (A2A) și Model Context Protocol (MCP) pentru a descoperi și utiliza alți agenți și instrumente.
- **Pluginuri și conectori** - Se pot realiza conexiuni la servicii de date și memorie precum Microsoft Fabric, SharePoint, Pinecone și Qdrant.

Să vedem cum sunt aplicate aceste funcționalități la unele dintre conceptele de bază ale Microsoft Agent Framework.

## Concepte cheie ale Microsoft Agent Framework

### Agenți

![Agent Framework](../../../translated_images/ro/agent-components.410a06daf87b4fef.webp)

**Crearea agenților**

Crearea unui agent se face prin definirea serviciului de inferență (furnizor LLM), a unui set de instrucțiuni pe care agentul AI trebuie să le urmeze și a unui `name` atribuit:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Exemplul de mai sus folosește `Azure OpenAI`, dar agenții pot fi creați folosind o varietate de servicii, inclusiv `Microsoft Foundry Agent Service`:

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

sau agenți la distanță folosind protocolul A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Rularea agenților**

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

Fiecare rulare a agentului poate avea, de asemenea, opțiuni pentru a personaliza parametri precum `max_tokens` folosit de agent, `tools` pe care agentul le poate apela și chiar `model`-ul utilizat de agent.

Acest lucru este util în cazurile în care sunt necesare modele sau instrumente specifice pentru finalizarea sarcinii unui utilizator.

**Instrumente**

Instrumentele pot fi definite atât în timpul definirii agentului:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Când creați un ChatAgent direct

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

și, de asemenea, la rularea agentului:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Unealtă oferită doar pentru această rulare )
```

**Fire ale agentului**

Firele agentului sunt folosite pentru a gestiona conversații multi-turn. Firele pot fi create fie prin:

- Folosind `get_new_thread()` care permite ca firul să fie salvat în timp
- Crearea unui fir automat la rularea unui agent, iar firul să dureze doar pe durata rulării curente.

Pentru a crea un fir, codul arată astfel:

```python
# Creează un fir nou.
thread = agent.get_new_thread() # Rulează agentul folosind firul.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Puteți apoi serializa firul pentru a fi stocat și folosit mai târziu:

```python
# Creați un fir nou.
thread = agent.get_new_thread() 

# Rulați agentul cu firul.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializați firul pentru stocare.

serialized_thread = await thread.serialize() 

# Deserializați starea firului după încărcarea din stocare.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware pentru agenți**

Agenții interacționează cu instrumente și LLM-uri pentru a îndeplini sarcinile utilizatorilor. În anumite scenarii, dorim să executăm sau să urmărim acțiuni între aceste interacțiuni. Middleware-ul pentru agenți ne permite să facem acest lucru prin:

*Middleware pentru funcții*

Acest middleware ne permite să executăm o acțiune între agent și o funcție/instrument pe care îl va apela. Un exemplu de utilizare este atunci când doriți să înregistrați apelul funcției.

În codul de mai jos, `next` definește dacă ar trebui apelat următorul middleware sau funcția propriu-zisă.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pre-procesare: Înregistrare înainte de executarea funcției
    print(f"[Function] Calling {context.function.name}")

    # Continuați la middleware-ul următor sau la executarea funcției
    await next(context)

    # Post-procesare: Înregistrare după executarea funcției
    print(f"[Function] {context.function.name} completed")
```

*Middleware pentru chat*

Acest middleware ne permite să executăm sau să înregistrăm o acțiune între agent și cererile către LLM.

Aceasta conține informații importante, cum ar fi `messages` care sunt trimise către serviciul AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pre-procesare: Înregistrare înainte de apelul către AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continuați la middleware-ul următor sau la serviciul AI
    await next(context)

    # Post-procesare: Înregistrare după răspunsul de la AI
    print("[Chat] AI response received")

```

**Memoria agentului**

Așa cum s-a discutat în lecția `Agentic Memory`, memoria este un element important pentru a permite agentului să funcționeze pe contexte diferite. MAF oferă mai multe tipuri diferite de memorii:

*Stocare în memorie*

Aceasta este memoria stocată în fire pe durata execuției aplicației.

```python
# Creează un fir nou.
thread = agent.get_new_thread() # Rulează agentul cu firul.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Mesaje persistente*

Această memorie este utilizată pentru stocarea istoricului conversațiilor între diferite sesiuni. Este definită folosind `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Creați un magazin de mesaje personalizat
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

Observabilitatea este importantă pentru construirea unor sisteme agentice fiabile și ușor de întreținut. MAF se integrează cu OpenTelemetry pentru a oferi urmărire și contoare pentru o observabilitate mai bună.

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

Fluxurile de lucru sunt alcătuite din diferite componente care permit un control mai bun al fluxului. Fluxurile de lucru permit, de asemenea, **orchestrare multi-agent** și **checkpointing** pentru a salva stările fluxului de lucru.

Componentele de bază ale unui flux de lucru sunt:

**Executori**

Executorii primesc mesaje de intrare, îndeplinesc sarcinile atribuite și apoi produc un mesaj de ieșire. Acest lucru avansează fluxul de lucru spre finalizarea sarcinii mai mari. Executorii pot fi fie agenți AI, fie logică personalizată.

**Muchii**

Muchiile sunt folosite pentru a defini fluxul mesajelor într-un flux de lucru. Acestea pot fi:

*Muchii directe* - Conexiuni simple unu-la-unu între executori:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Muchii condiționale* - Se activează după îndeplinirea unei anumite condiții. De exemplu, când camerele de hotel nu sunt disponibile, un executor poate sugera alte opțiuni.

*Muchii de tip switch-case* - Direcționează mesajele către diferiți executori în funcție de condițiile definite. De exemplu, dacă clientul de călătorii are acces prioritar, sarcinile sale vor fi gestionate printr-un alt flux de lucru.

*Muchii fan-out* - Trimit un mesaj către mai multe ținte.

*Muchii fan-in* - Colectează mai multe mesaje de la diferiți executori și le trimite către o singură țintă.

**Evenimente**

Pentru a oferi o observabilitate mai bună asupra fluxurilor de lucru, MAF oferă evenimente încorporate pentru execuție, inclusiv:

- `WorkflowStartedEvent`  - Execuția fluxului de lucru începe
- `WorkflowOutputEvent` - Fluxul de lucru produce un rezultat
- `WorkflowErrorEvent` - Fluxul de lucru întâmpină o eroare
- `ExecutorInvokeEvent`  - Executorul începe procesarea
- `ExecutorCompleteEvent`  - Executorul termină procesarea
- `RequestInfoEvent` - Este emisă o cerere

## Modele avansate MAF

Secțiunile de mai sus acoperă conceptele cheie ale Microsoft Agent Framework. Pe măsură ce construiți agenți mai complecși, iată câteva modele avansate de luat în considerare:

- **Compoziția middleware**: Conectați în lanț mai mulți handleri de middleware (logging, auth, rate-limiting) folosind middleware pentru funcții și chat pentru un control fin asupra comportamentului agentului.
- **Checkpointing pentru fluxuri de lucru**: Utilizați evenimentele fluxului de lucru și serializarea pentru a salva și relua procesele agenților care rulează mult timp.
- **Selecție dinamică a instrumentelor**: Combinați RAG peste descrierile instrumentelor cu înregistrarea de instrumente a MAF pentru a prezenta numai instrumentele relevante pentru fiecare interogare.
- **Predare între agenți (Multi-Agent Handoff)**: Utilizați muchiile fluxului de lucru și rutarea condițională pentru a orchestra predările între agenți specializați.

## Exemple de cod 

Exemple de cod pentru Microsoft Agent Framework pot fi găsite în acest depozit în fișierele `xx-python-agent-framework` și `xx-dotnet-agent-framework`.

## Mai aveți întrebări despre Microsoft Agent Framework?

Alăturați-vă [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la ore de consultanță și a obține răspunsuri la întrebările dvs. despre Agenți AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autorizată. Pentru informații critice, se recomandă o traducere profesională realizată de un traducător uman. Nu suntem răspunzători pentru orice neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->