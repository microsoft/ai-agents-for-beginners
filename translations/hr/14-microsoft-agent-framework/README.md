# Istraživanje Microsoft Agent Frameworka

![Agent Framework](../../../translated_images/hr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Uvod

Ova lekcija obuhvatit će:

- Razumijevanje Microsoft Agent Frameworka: Ključne značajke i vrijednost  
- Istraživanje ključnih pojmova Microsoft Agent Frameworka
- Napredni MAF obrasci: Radni tokovi, Middleware i Memorija

## Ciljevi učenja

Nakon završetka ove lekcije ćete znati kako:

- Izgraditi AI agente spremne za produkciju koristeći Microsoft Agent Framework
- Primijeniti osnovne značajke Microsoft Agent Frameworka na vaše agentične slučajeve upotrebe
- Koristiti napredne obrasce uključujući radne tokove, middleware i promatranje

## Primjeri koda 

Primjeri koda za [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) mogu se pronaći u ovom spremištu pod datotekama `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Razumijevanje Microsoft Agent Frameworka

![Framework Intro](../../../translated_images/hr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) je jedinstveni okvir tvrtke Microsoft za izgradnju AI agenata. Nudi fleksibilnost za rješavanje širokog spektra agentičnih slučajeva upotrebe viđenih u produkcijskim i istraživačkim okruženjima, uključujući:

- **Sekvencijalnu orkestraciju agenata** u scenarijima gdje su potrebni korak-po-korak radni tokovi.
- **Istovremenu orkestraciju** u scenarijima gdje agenti trebaju istovremeno dovršiti zadatke.
- **Orkestraciju grupnog chata** u scenarijima gdje agenti mogu surađivati na jednom zadatku.
- **Orkestraciju predaje** u scenarijima gdje agenti prenose zadatak jedan drugome kako se podzadaci dovršavaju.
- **Magnetnu orkestraciju** u scenarijima gdje upravljački agent stvara i mijenja popis zadataka i koordinira podagente za dovršetak zadatka.

Za isporuku AI agenata u produkciji, MAF također uključuje značajke za:

- **Promatranje** kroz korištenje OpenTelemetry gdje se prati svaka akcija AI agenta uključujući poziv alata, korake orkestracije, tokove razmišljanja i nadzor performansi putem Microsoft Foundry nadzornih ploča.
- **Sigurnost** hostanjem agenata nativno na Microsoft Foundry koji uključuje sigurnosne kontrole poput pristupa temeljenog na ulogama, rukovanje privatnim podacima i ugrađenu sigurnost sadržaja.
- **Izdržljivost** jer Agentovi threadovi i radni tokovi mogu pauzirati, nastaviti i oporaviti se od pogrešaka što omogućuje dugotrajnije procese.
- **Kontrolu** jer su podržani radni tokovi s ljudima u petlji gdje se zadaci označavaju kao oni koji zahtijevaju ljudsku potvrdu.

Microsoft Agent Framework se također fokusira na interoperabilnost kroz:

- **Biti neovisnim o oblaku** - Agent može raditi u kontejnerima, na lokalnim sustavima i preko više različitih oblaka.
- **Biti neovisnim o davatelju usluga** - Agent se može kreirati putem vašeg preferiranog SDK-a uključujući Azure OpenAI i OpenAI
- **Integriranje otvorenih standarda** - Agent može koristiti protokole poput Agent-to-Agent (A2A) i Model Context Protocol (MCP) za otkrivanje i korištenje drugih agenata i alata.
- **Dodaci i konektori** - Mogu se uspostaviti veze s uslugama podataka i memorije poput Microsoft Fabric, SharePoint, Pinecone i Qdranta.

Pogledajmo kako se ove značajke primjenjuju na neke od ključnih pojmova Microsoft Agent Frameworka.

## Ključni pojmovi Microsoft Agent Frameworka

### Agenti

![Agent Framework](../../../translated_images/hr/agent-components.410a06daf87b4fef.webp)

**Kreiranje agenata**

Kreiranje agenta se ostvaruje definiranjem usluge zaključivanja (LLM Provider), 
skupa uputa koje AI agent treba slijediti, i dodijeljenog `imena`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Gore navedeni primjer koristi `Azure OpenAI`, ali agenti se mogu kreirati koristeći razne usluge uključujući `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API-je

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ili [MiniMax](https://platform.minimaxi.com/), koji pruža OpenAI-kompatibilan API s velikim kontekstnim okvirima (do 204 tisuće tokena):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ili udaljene agente koristeći A2A protokol:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Pokretanje agenata**

Agenti se pokreću koristeći metode `.run` ili `.run_stream` za odgovore bez streaminga ili sa streamingom.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Svako pokretanje agenta također može imati opcije za prilagodbu parametara kao što su `max_tokens` koje agent koristi, `tools` koje agent može pozvati, i čak sam `model` koji agent koristi.

Ovo je korisno u slučajevima kada su potrebni specifični modeli ili alati za dovršetak zadatka korisnika.

**Alati**

Alati se mogu definirati i prilikom definiranja agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Prilikom izravnog stvaranja ChatAgenta

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

i također prilikom pokretanja agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Alat dostavljen samo za ovaj izvođenje )
```

**Threadovi agenata**

Threadovi agenata se koriste za vođenje višekratnih razgovora s više okretaja. Threadovi se mogu kreirati na dva načina:

- Koristeći `get_new_thread()` što omogućuje da se thread sačuva tijekom vremena
- Automatskim kreiranjem threada prilikom pokretanja agenta i trajanja threada samo tijekom trenutnog pokretanja.

Kod za kreiranje threada izgleda ovako:

```python
# Kreirajte novu nit.
thread = agent.get_new_thread() # Pokrenite agenta s niti.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Thread se zatim može serijalizirati za pohranu i kasniju upotrebu:

```python
# Kreirajte novu dretvu.
thread = agent.get_new_thread() 

# Pokrenite agenta s dretvom.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serijalizirajte dretvu za pohranu.

serialized_thread = await thread.serialize() 

# Deserijalizirajte stanje dretve nakon učitavanja iz pohrane.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware agenata**

Agenti komuniciraju s alatima i LLM-ovima za dovršavanje zadataka korisnika. U određenim scenarijima želimo izvršiti ili pratiti interakcije između njih. Middleware agenata omogućuje ovo kroz:

*Middleware funkcija*

Ovaj middleware nam dopušta izvršavanje akcije između agenta i funkcije/alata koji će agent pozvati. Primjer kada se ovo koristi je za vođenje zapisa (log) o pozivu funkcije.

U sljedećem kodu `next` definira treba li se pozvati sljedeći middleware ili stvarna funkcija.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pretprocesiranje: Zabilježi prije izvršavanja funkcije
    print(f"[Function] Calling {context.function.name}")

    # Nastavi na sljedeći middleware ili izvršavanje funkcije
    await next(context)

    # Postprocesiranje: Zabilježi nakon izvršavanja funkcije
    print(f"[Function] {context.function.name} completed")
```

*Middleware razgovora*

Ovaj middleware omogućuje izvršavanje ili bilježenje akcije između agenta i zahtjeva između LLM-a.

Ovo sadrži važne informacije poput `poruka` koje se šalju AI servisu.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Predobrada: Zabilježi prije poziva AI-ja
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Nastavi na sljedeći middleware ili AI servis
    await next(context)

    # Obrada nakon: Zabilježi nakon AI odgovora
    print("[Chat] AI response received")

```

**Memorija agenata**

Kao što je obrađeno u lekciji `Agentic Memory`, memorija je važan element za omogućavanje rada agenta u različitim kontekstima. MAF nudi nekoliko različitih vrsta memorije:

*Memorija u radnom prostoru*

Ovo je memorija pohranjena u threadovima tijekom izvođenja aplikacije.

```python
# Kreirajte novu dretvu.
thread = agent.get_new_thread() # Pokrenite agenta s dretvom.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Postojane poruke*

Ova memorija se koristi za pohranu povijesti razgovora kroz različite sesije. Definira se korištenjem `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Stvori prilagođenu pohranu poruka
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dinamička memorija*

Ova memorija se dodaje u kontekst prije pokretanja agenata. Ova memorija može biti pohranjena u vanjskim uslugama poput mem0:

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

**Promatranje agenata**

Promatranje je važno za izgradnju pouzdanih i održivih agentičnih sustava. MAF se integrira s OpenTelemetry za pružanje praćenja i mjerenja za bolje promatranje.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # učini nešto
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Radni tokovi

MAF nudi radne tokove koji su unaprijed definirani koraci za dovršetak zadatka i uključuju AI agente kao komponente u tim koracima.

Radni tokovi se sastoje od različitih komponenti koje omogućuju bolju kontrolu protoka. Radni tokovi također omogućuju **orkestraciju više agenata** i **checkpointing** za spremanje stanja radnog toka.

Osnovne komponente radnog toka su:

**Izvršitelji**

Izvršitelji primaju ulazne poruke, izvršavaju svoje zadatke i zatim proizvode izlaznu poruku. Ovo pomiče radni tok prema dovršetku većeg zadatka. Izvršitelji mogu biti AI agenti ili prilagođena logika.

**Veze**

Veze se koriste za definiranje protoka poruka u radnom toku. Mogu biti:

*Izravne veze* - Jednostavne veze jedan na jedan između izvršitelja:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Uvjetne veze* - Aktiviraju se nakon što je zadovoljen određeni uvjet. Na primjer, ako sobe u hotelu nisu dostupne, izvršitelj može predložiti druge opcije.

*Switch-case veze* - Usmjeravaju poruke različitim izvršiteljima na temelju definiranih uvjeta. Na primjer, ako putnički korisnik ima prioritetni pristup, njegovi će zadaci biti obrađeni kroz drugi radni tok.

*Fan-out veze* - Šalju jednu poruku na više odredišta.

*Fan-in veze* - Prikupljaju više poruka od različitih izvršitelja i šalju na jedno odredište.

**Događaji**

Za pružanje bolje promatranosti radnih tokova, MAF nudi ugrađene događaje za izvršavanje uključujući:

- `WorkflowStartedEvent`  - Početak izvršavanja radnog toka
- `WorkflowOutputEvent` - Radni tok proizvodi izlaz
- `WorkflowErrorEvent` - Radni tok je naišao na pogrešku
- `ExecutorInvokeEvent`  - Izvršitelj započinje procesiranje
- `ExecutorCompleteEvent`  -  Izvršitelj završava procesiranje
- `RequestInfoEvent` - Izdan je zahtjev

## Napredni MAF obrasci

Gornji odjeljci obuhvaćaju ključne pojmove Microsoft Agent Frameworka. Kako gradite složenije agente, evo nekoliko naprednih obrazaca za razmatranje:

- **Sastavljanje middlewarea**: Povežite više middleware handlera (logiranje, autentifikacija, ograničenje brzine) koristeći middleware funkcija i razgovora za preciznu kontrolu ponašanja agenta.
- **Checkpointing radnog toka**: Koristite događaje radnog toka i serijalizaciju za spremanje i nastavak dugotrajnih procesa agenata.
- **Dinamički odabir alata**: Kombinirajte RAG preko opisa alata s MAF-ovom registracijom alata da biste prikazali samo relevantne alate po upitu.
- **Predaja između više agenata**: Koristite veze radnog toka i uvjetno usmjeravanje za orkestraciju predaja između specijaliziranih agenata.

## Hostanje LangChain / LangGraph agenata na Microsoft Foundry

Microsoft Agent Framework je **interoperabilan s drugim frameworkovima** — niste ograničeni samo na agente napisane s MAF-om. Ako već imate agenta izrađenog s **LangChain** ili **LangGraph**, možete ga pokrenuti kao **Foundry hostanog agenta** tako da Foundry upravlja runtime-om, sesijama, skaliranjem, identitetom i krajnjim točkama protokola, dok vaša logika agenta ostaje u LangGraphu.

To se ostvaruje s paketom `langchain_azure_ai.agents.hosting` koji izlaže kompajlirani LangGraph graf preko iste protokole koje koriste Foundry hostani agenti.

**1. Instalirajte hosting dodatak:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Dodatak `hosting` instalira Foundry protokol biblioteke: `azure-ai-agentserver-responses` (OpenAI-kompatibilnu `/responses` krajnju točku) i `azure-ai-agentserver-invocations` (generičku `/invocations` krajnju točku).

**2. Odaberite hosting protokol:**

| Protokol | Host klasa | Krajnja točka | Koristi kada |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Želite OpenAI-kompatibilan chat, streaming, povijest odgovora i threading razgovora — preporučeni zadani izbor za konverzacijske agente. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Potrebna vam je prilagođena JSON struktura, webhook-stil krajnje točke ili ne-konverzacijsko procesiranje. |

Budući da je **Responses API primarni API za razvoj agenata u Foundryju**, počnite s `ResponsesHostServer` za većinu agenata.

**3. Konfigurirajte varijable okoline** (`az login` prvo kako bi se `DefaultAzureCredential` mogao autentificirati):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Kada agent kasnije radi kao hostani agent u Foundryju, platforma automatski ubrizga `FOUNDRY_PROJECT_ENDPOINT`.

**4. Izložite LangGraph agenta preko Responses protokola:**

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

    # ChatOpenAI ovdje cilja OpenAI-kompatibilnu (Odgovori) točku projekta Foundry.
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

Pokrenite lokalno s `python main.py`, zatim pošaljite Responses zahtjev na `http://localhost:8088/responses`.

**Ključna ponašanja:**

- **Razgovori**: Klijenti nastavljaju razgovor prosljeđivanjem `previous_response_id` ili `conversation` ID-a. Ako je vaš graf kompajliran s LangGraph checkpointerom, Foundry povezuje stanje razgovora s checkpointom (koristite trajni checkpointer u produkciji; `MemorySaver` je dovoljan za lokalno testiranje).
- **Čovjek u petlji**: Ako vaš graf koristi LangGraph `interrupt()`, `ResponsesHostServer` prikazuje čekajući prekid kao Responses `function_call` / `mcp_approval_request` stavku, a klijenti nastavljaju s odgovarajućim `function_call_output` / `mcp_approval_response`.
- **Deploy u Foundry**: Koristite Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokalno, zahtijeva Docker), zatim `azd provision` i `azd deploy`. Deploy hostanog agenta zahtijeva ulogu **Foundry Project Manager**.

Verzija ovog primjera koja se može pokrenuti živi u [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Za cjeloviti vodič (Invocations protokol, prilagođene sheme zahtjeva i rješavanje problema), pogledajte [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Primjeri koda 

Primjeri koda za Microsoft Agent Framework mogu se pronaći u ovom spremištu pod datotekama `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Imate dodatnih pitanja o Microsoft Agent Frameworku?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) da biste upoznali druge učenike, sudjelovali na konzultacijama i dobili odgovore na pitanja o AI agentima.
## Prethodna lekcija

[Memorija za AI agente](../13-agent-memory/README.md)

## Sljedeća lekcija

[Izgradnja agenata za upotrebu računala (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->