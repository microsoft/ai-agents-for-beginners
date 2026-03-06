# Istraživanje Microsoft Agent Framework

![Okvir agenata](../../../translated_images/hr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Uvod

Ova lekcija će obuhvatiti:

- Razumijevanje Microsoft Agent Frameworka: ključne značajke i vrijednost  
- Istraživanje ključnih koncepata Microsoft Agent Frameworka
- Napredni MAF obrasci: tokovi rada, međusloj (middleware) i memorija

## Ciljevi učenja

Nakon završetka ove lekcije, znat ćete kako:

- Izgraditi proizvodom spremne AI agente koristeći Microsoft Agent Framework
- Primijeniti osnovne značajke Microsoft Agent Frameworka na vaše agentske slučajeve uporabe
- Koristiti napredne obrasce uključujući tokove rada, međusloj (middleware) i observabilnost

## Primjeri koda 

Primjeri koda za [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) nalaze se u ovom spremištu pod datotekama `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Razumijevanje Microsoft Agent Frameworka

![Uvod u okvir](../../../translated_images/hr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) je Microsoftov objedinjeni okvir za izgradnju AI agenata. Nudi fleksibilnost za rješavanje širokog raspona agentskih slučajeva uporabe viđenih i u produkciji i u istraživačkom okruženju, uključujući:

- **Sekvencijalna orkestracija agenata** u scenarijima gdje su potrebni postupni tokovi rada.
- **Konkurentna orkestracija** u scenarijima gdje agenti trebaju dovršiti zadatke istovremeno.
- **Orkestracija grupnog chata** u scenarijima gdje agenti mogu surađivati zajedno na jednom zadatku.
- **Orkestracija predaje zadatka (Handoff)** u scenarijima gdje agenti predaju zadatak jedni drugima kako se podzadatci dovrše.
- **Magnetska orkestracija** u scenarijima gdje upravljački agent stvara i mijenja popis zadataka i upravlja koordinacijom podagenata za dovršetak zadatka.

Za isporuku AI agenata u produkciji, MAF također uključuje značajke za:

- **Observabilnost** putem OpenTelemetry gdje svaka radnja AI agenta uključujući pozivanje alata, korake orkestracije, tokove rezoniranja i praćenje performansi kroz Microsoft Foundry nadzorne ploče.
- **Sigurnost** hostanjem agenata izvorno na Microsoft Foundry koji uključuje sigurnosne kontrole poput kontrole pristupa bazirane na ulogama, rukovanja privatnim podacima i ugrađene sigurnosti sadržaja.
- **Otpornost** jer se agentne niti i tokovi rada mogu zaustaviti, nastaviti i oporaviti od pogrešaka, što omogućava dugotrajnije procese.
- **Kontrola** budući da su podržani tokovi rada s čovjekom u petlji gdje su zadaci označeni kao zahtijevajući ljudsko odobrenje.

Microsoft Agent Framework je također usmjeren na interoperabilnost kroz:

- **Neovisnost o oblaku (Cloud-agnostic)** - Agentima se može upravljati u kontejnerima, on-prem i na više različitih oblaka.
- **Neovisnost o pružatelju (Provider-agnostic)** - Agente možete stvoriti kroz željeni SDK uključujući Azure OpenAI i OpenAI
- **Integracija otvorenih standarda** - Agenti mogu koristiti protokole kao što su Agent-to-Agent(A2A) i Model Context Protocol (MCP) za otkrivanje i korištenje drugih agenata i alata.
- **Dodaci i konektori** - Mogu se uspostaviti veze s uslugama podataka i memorije kao što su Microsoft Fabric, SharePoint, Pinecone i Qdrant.

Pogledajmo kako se ove značajke primjenjuju na neke od ključnih koncepata Microsoft Agent Frameworka.

## Ključni koncepti Microsoft Agent Frameworka

### Agenti

![Okvir agenata](../../../translated_images/hr/agent-components.410a06daf87b4fef.webp)

**Stvaranje agenata**

Stvaranje agenta odvija se definiranjem usluge za zaključivanje (LLM Provider), skupa uputa koje AI agent treba slijediti, i dodijeljenog `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Gore se koristi `Azure OpenAI`, ali agenti se mogu stvarati koristeći različite usluge uključujući `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ili udaljeni agenti koristeći A2A protokol:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Pokretanje agenata**

Agenti se pokreću koristeći metode `.run` ili `.run_stream` za ne-streaming ili streaming odgovore.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Svako pokretanje agenta također može imati opcije za prilagodbu parametara kao što su `max_tokens` koje agent koristi, `tools` koje agent može pozivati, pa čak i sam `model` koji agent koristi.

Ovo je korisno u slučajevima kada su specifični modeli ili alati potrebni za dovršetak zadatka korisnika.

**Alati**

Alate je moguće definirati i prilikom definiranja agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Prilikom izravnog stvaranja ChatAgenta

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

i također pri pokretanju agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Alat osiguran samo za ovo izvođenje )
```

**Agentne niti**

Agentne niti koriste se za upravljanje višekratnim razgovorima. Niti se mogu stvoriti na sljedeće načine:

- Korištenjem `get_new_thread()` što omogućuje da se nit sprema tijekom vremena
- Automatskim stvaranjem niti pri pokretanju agenta koja traje samo tijekom trenutnog pokretanja.

Za stvaranje niti, kod izgleda ovako:

```python
# Stvori novu nit.
thread = agent.get_new_thread() # Pokreni agenta s tom niti.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Zatim možete serijalizirati nit kako biste je pohranili za kasniju upotrebu:

```python
# Stvori novu nit.
thread = agent.get_new_thread() 

# Pokreni agenta s nitom.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serijaliziraj nit za pohranu.

serialized_thread = await thread.serialize() 

# Deserijaliziraj stanje niti nakon učitavanja iz pohrane.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agenti komuniciraju s alatima i LLM-ovima kako bi dovršili zadatke korisnika. U određenim scenarijima želimo izvršiti ili pratiti radnje između tih interakcija. Agent middleware nam to omogućava kroz:

*Funkcijski međusloj*

Ovaj međusloj omogućuje nam izvršavanje akcije između agenta i funkcije/alata kojeg će pozivati. Primjer kada bi se koristio je kada želite napraviti zapis (logging) poziva funkcije.

U donjem kodu `next` definira treba li pozvati sljedeći međusloj ili stvarnu funkciju.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Predobrada: Zapisivanje u dnevnik prije izvršavanja funkcije
    print(f"[Function] Calling {context.function.name}")

    # Nastavi na sljedeći middleware ili izvršavanje funkcije
    await next(context)

    # Postobrada: Zapisivanje u dnevnik nakon izvršavanja funkcije
    print(f"[Function] {context.function.name} completed")
```

*Chat međusloj*

Ovaj međusloj omogućuje nam izvršavanje ili zapisivanje akcije između agenta i zahtjeva prema LLM-u.

Ovo sadrži važne informacije poput `messages` koje se šalju AI usluzi.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Predobrada: Zapis prije poziva AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Nastavi na sljedeći međusloj ili AI uslugu
    await next(context)

    # Naknadna obrada: Zapis nakon odgovora AI
    print("[Chat] AI response received")

```

**Memorija agenta**

Kao što je pokriveno u lekciji `Agentic Memory`, memorija je važan element koji omogućuje agentu rad u različitim kontekstima. MAF nudi nekoliko različitih tipova memorije:

*Pohrana u memoriji*

To je memorija pohranjena u nitima tijekom izvođenja aplikacije.

```python
# Stvori novu dretvu.
thread = agent.get_new_thread() # Pokreni agenta s dretvom.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Trajne poruke*

Ova memorija se koristi pri pohranjivanju povijesti razgovora kroz različite sesije. Definira se pomoću `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Stvorite prilagođenu pohranu poruka
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dinamična memorija*

Ova memorija se dodaje u kontekst prije pokretanja agenata. Ove memorije mogu se pohraniti u vanjskim uslugama kao što je mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Korištenje Mem0 za napredne memorijske mogućnosti
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

**Observabilnost agenta**

Observabilnost je važna za izgradnju pouzdanih i održivih agentskih sustava. MAF se integrira s OpenTelemetry za pružanje praćenja i mjera za bolju observabilnost.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # uradi nešto
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Tokovi rada

MAF nudi tokove rada koji su unaprijed definirani koraci za dovršetak zadatka i uključuju AI agente kao komponente tih koraka.

Tokovi rada sastoje se od različitih komponenti koje omogućuju bolji tok kontrole. Tokovi rada također omogućuju **orkestraciju s više agenata (multi-agent orchestration)** i **checkpointing** za spremanje stanja toka rada.

Osnovne komponente toka rada su:

**Izvršitelji**

Izvršitelji primaju ulazne poruke, izvršavaju dodijeljene zadatke i zatim proizvode izlaznu poruku. To pomiče tok rada prema dovršetku većeg zadatka. Izvršitelji mogu biti AI agenti ili prilagođena logika.

**Poveznice (Edges)**

Poveznice služe za definiranje toka poruka u toku rada. Mogu biti:

*Izravne poveznice* - Jednostavne veze jedan-na-jedan između izvršitelja:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Uvjetne poveznice* - Aktiviraju se nakon što je zadovoljen određeni uvjet. Na primjer, kada hotelske sobe nisu dostupne, izvršitelj može predložiti druge opcije.

*Poveznice tipa switch-case* - Usmjeravaju poruke različitim izvršiteljima na temelju definiranih uvjeta. Na primjer, ako putnički korisnik ima prioritetni pristup, njegovi zadaci će se obraditi kroz drugi tok rada.

*Fan-out poveznice* - Šalju jednu poruku na više odredišta.

*Fan-in poveznice* - Sakupljaju više poruka od različitih izvršitelja i šalju ih na jedno odredište.

**Događaji**

Za bolju observabilnost tokova rada, MAF nudi ugrađene događaje za izvođenje uključujući:

- `WorkflowStartedEvent`  - Pokretanje izvršavanja toka rada
- `WorkflowOutputEvent` - Tok rada generira izlaz
- `WorkflowErrorEvent` - Tok rada nailazi na pogrešku
- `ExecutorInvokeEvent`  - Izvršitelj započinje obradu
- `ExecutorCompleteEvent`  -  Izvršitelj završava obradu
- `RequestInfoEvent` - Podnosi se zahtjev

## Napredni MAF obrasci

Gornji odjeljci pokrivaju ključne koncepte Microsoft Agent Frameworka. Kako budete gradili složenije agente, evo nekoliko naprednih obrazaca koje treba razmotriti:

- **Sastavljanje međuslojeva (Middleware Composition)**: Povežite više rukovatelja međuslojevima (logging, auth, rate-limiting) koristeći funkcijski i chat međusloj za detaljnu kontrolu ponašanja agenta.
- **Checkpointiranje tokova rada**: Koristite događaje toka rada i serijalizaciju za spremanje i nastavak dugotrajnih procesa agenata.
- **Dinamički odabir alata**: Kombinirajte RAG preko opisa alata s MAF-ovom registracijom alata kako biste prikazali samo relevantne alate za svaki upit.
- **Predaja između više agenata**: Koristite poveznice toka rada i uvjetno usmjeravanje za orkestraciju predaja između specijaliziranih agenata.

## Primjeri koda 

Primjeri koda za Microsoft Agent Framework mogu se pronaći u ovom spremištu u datotekama `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Imate li još pitanja o Microsoft Agent Frameworku?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) kako biste se susreli s drugim učenicima, sudjelovali u radnim satima i dobili odgovore na pitanja o svojim AI agentima.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Odricanje odgovornosti:
Ovaj dokument preveden je pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->