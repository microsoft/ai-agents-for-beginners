# Istraživanje Microsoft Agent Frameworka

![Agent Framework](../../../translated_images/hr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Uvod

Ova lekcija će pokriti:

- Razumijevanje Microsoft Agent Frameworka: Ključne značajke i vrijednost  
- Istraživanje ključnih pojmova Microsoft Agent Frameworka
- Napredni MAF obrasci: Radni tokovi, Middleware i memorija

## Ciljevi učenja

Nakon završetka ove lekcije, znat ćete kako:

- Izgraditi spremne za proizvodnju AI agente koristeći Microsoft Agent Framework
- Primijeniti temeljne značajke Microsoft Agent Frameworka na vaše agentične slučajeve upotrebe
- Koristiti napredne obrasce uključujući radne tokove, middleware i promatranje

## Primjeri koda 

Primjere koda za [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) možete pronaći u ovom repozitoriju pod datotekama `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Razumijevanje Microsoft Agent Frameworka

![Framework Intro](../../../translated_images/hr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) je Microsoftov jedinstveni okvir za izgradnju AI agenata. Pruža fleksibilnost za rješavanje širokog spektra agentičnih slučajeva upotrebe viđenih u proizvodnim i istraživačkim okruženjima uključujući:

- **Sekvencijalnu orkestraciju agenata** u scenarijima gdje su potrebni radni tokovi korak-po-korak.
- **Istovremenu orkestraciju** u scenarijima gdje agenti trebaju izvršiti zadatke istovremeno.
- **Orkestraciju grupnog chata** u scenarijima gdje agenti mogu surađivati na jednom zadatku.
- **Orkestraciju predaje zadatka** u scenarijima gdje agenti predaju zadatak jedni drugima kako se podzadatci dovršavaju.
- **Magnetnu orkestraciju** u scenarijima gdje agent upravitelj stvara i modificira popis zadataka i upravlja koordinacijom podagenata da dovrše zadatak.

Za isporuku AI agenata u produkciji, MAF također uključuje značajke za:

- **Promatranje** putem korištenja OpenTelemetry gdje se prati svaka akcija AI agenta uključujući pozive alata, korake orkestracije, tokove rezoniranja i nadzor performansi kroz Microsoft Foundry kontrolnu ploču.
- **Sigurnost** hostanjem agenata nativno na Microsoft Foundry koji uključuje sigurnosne kontrole poput pristupa temeljenog na ulogama, rukovanja privatnim podacima i ugrađene sigurnosti sadržaja.
- **Izdržljivost** jer se Agent niti i radni tokovi mogu pauzirati, nastaviti i oporaviti od pogrešaka što omogućuje duže trajanje procesa.
- **Kontrolu** jer su podržani radni tokovi s ljudima u petlji gdje su zadaci označeni kao zahtijevajući ljudsku odobrenje.

Microsoft Agent Framework također je usredotočen na interoperabilnost kroz:

- **Biti neovisni o oblaku** - Agenti mogu raditi u kontejnerima, lokalno i preko različitih oblaka.
- **Biti neovisni o pružatelju usluge** - Agenti se mogu kreirati korištenjem vašeg omiljenog SDK-a uključujući Azure OpenAI i OpenAI
- **Integraciju otvorenih standarda** - Agenti mogu koristiti protokole poput Agent-to-Agent (A2A) i Model Context Protocol (MCP) za otkrivanje i korištenje drugih agenata i alata.
- **Dodataka i konektora** - Mogu se uspostaviti veze s uslugama podataka i memorije kao što su Microsoft Fabric, SharePoint, Pinecone i Qdrant.

Pogledajmo kako su ove značajke primijenjene na neke od ključnih pojmova Microsoft Agent Frameworka.

## Ključni pojmovi Microsoft Agent Frameworka

### Agenti

![Agent Framework](../../../translated_images/hr/agent-components.410a06daf87b4fef.webp)


**Kreiranje agenata**

Kreiranje agenta odvija se definiranjem usluge zaključivanja (LLM pružatelj), skupa uputa koje AI agent treba slijediti i dodijeljenog `imena`:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Gore se koristi `Azure OpenAI`, ali agenti se mogu kreirati koristeći različite usluge uključujući `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API-jevi

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ili [MiniMax](https://platform.minimaxi.com/), koji pruža API kompatibilan s OpenAI-jem s velikim kontekstnim okvirima (do 204K tokena):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ili udaljene agente koristeći A2A protokol:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Pokretanje agenata**

Agenti se pokreću korištenjem metoda `.run` ili `.run_stream` za odgovore bez strujanja ili sa strujanjem.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Svako pokretanje agenta može također imati opcije za prilagodbu parametara poput `max_tokens` koje agent koristi, `tools` koje agent može pozivati te čak i `model` koji se koristi za agenta.

Ovo je korisno u slučajevima kada su specifični modeli ili alati potrebni za izvršavanje zadatka korisnika.

**Alati**

Alati se mogu definirati i prilikom definiranja agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Prilikom izravnog stvaranja ChatAgenta

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

i također prilikom pokretanja agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Alat dostupan samo za ovo pokretanje )
```

**Agent Threads**

Agent Threads koriste se za upravljanje razgovorima u više koraka. Threadovi se mogu kreirati na dva načina:

- Korištenjem `get_new_thread()` što omogućuje da se thread tijekom vremena sprema
- Automatskim kreiranjem threada prilikom pokretanja agenta gdje thread traje samo tijekom tekućeg pokretanja.

Za kreiranje threada, kod izgleda ovako:

```python
# Kreirajte novu nit.
thread = agent.get_new_thread() # Pokrenite agenta s niti.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Potom možete serijalizirati thread za čuvanje i kasniju upotrebu:

```python
# Kreirajte novu nit.
thread = agent.get_new_thread() 

# Pokrenite agenta s niti.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serijalizirajte nit za pohranu.

serialized_thread = await thread.serialize() 

# Deserijalizirajte stanje niti nakon učitavanja iz pohrane.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agenti surađuju s alatima i LLM-ovima kako bi izvršili zadatke korisnika. U određenim scenarijima želimo izvršiti nešto ili pratiti radnje između ovih interakcija. Agent middleware nam to omogućuje kroz:

*Function Middleware*

Ovaj middleware omogućuje provođenje akcije između agenta i funkcije/alata kojeg agent poziva. Primjer korištenja je kad želite napraviti zapisnik poziva funkcije.

U sljedećem kodu `next` definira treba li se pozvati sljedeći middleware ili stvarna funkcija.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Predobrada: Zabilježi prije izvođenja funkcije
    print(f"[Function] Calling {context.function.name}")

    # Nastavi na sljedeći middleware ili izvođenje funkcije
    await next(context)

    # Obrada nakon: Zabilježi nakon izvođenja funkcije
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Ovaj middleware omogućuje izvršenje ili zapisivanje akcije između agenta i zahtjeva između LLM-a.

Ovo sadrži važne informacije poput `messages` koji se šalju AI usluzi.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Predobrada: Započni zapis prije poziva AI-a
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Nastavi na sljedeći middleware ili AI uslugu
    await next(context)

    # Obrada nakon: Započni zapis nakon AI odgovora
    print("[Chat] AI response received")

```

**Agent Memory**

Kao što je objašnjeno u lekciji `Agentic Memory`, memorija je važan element koji agentu omogućuje rad u različitim kontekstima. MAF nudi nekoliko različitih tipova memorija:

*In-Memory Storage*

Ovo je memorija pohranjena u threadovima tijekom rada aplikacije.

```python
# Kreiraj novu dretvu.
thread = agent.get_new_thread() # Pokreni agenta s dretvom.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

Ova memorija se koristi za pohranu povijesti razgovora kroz različite sesije. Definira se pomoću `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Kreirajte prilagođenu pohranu poruka
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamic Memory*


Ova memorija se dodaje u kontekst prije pokretanja agenata. Ove memorije mogu se pohraniti u vanjskim uslugama poput mem0:

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

**Promatranje agenta**

Promatranje je važno za izgradnju pouzdanih i održivih agentnih sustava. MAF se integrira s OpenTelemetryjem kako bi pružio praćenje i mjerače za bolje promatranje.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # napravi nešto
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Radni tokovi

MAF nudi radne tokove koji su unaprijed definirani koraci za dovršetak zadatka i uključuju AI agente kao komponente u tim koracima.

Radni tokovi se sastoje od različitih komponenti koje omogućuju bolju kontrolu toka. Radni tokovi također omogućuju **orkestraciju više agenata** i **provjeru točke (checkpointing)** za spremanje stanja radnih tokova.

Glavne komponente radnog toka su:

**Izvršitelji**

Izvršitelji primaju ulazne poruke, obavljaju svoje dodijeljene zadatke i zatim stvaraju izlaznu poruku. Ovo pomiče radni tok prema dovršetku većeg zadatka. Izvršitelji mogu biti ili AI agenti ili prilagođena logika.

**Veze**

Veze se koriste za definiranje toka poruka u radnom toku. One mogu biti:

*Izravne veze* - Jednostve veze jedan-na-jedan između izvršitelja:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Uvjetne veze* - Aktiviraju se nakon zadovoljavanja određenog uvjeta. Na primjer, kada sobe u hotelu nisu dostupne, izvršitelj može predložiti druge opcije.

*Switch-case veze* - Usmjeravaju poruke različitim izvršiteljima na temelju definiranih uvjeta. Na primjer, ako putnik ima prioritetni pristup, njegovi će se zadaci obraditi kroz drugi radni tok.

*Fan-out veze* - Šalju jednu poruku na više ciljeva.

*Fan-in veze* - Prikupljaju više poruka od različitih izvršitelja i šalju ih jednom cilju.

**Događaji**

Kako bi se osiguralo bolje promatranje radnih tokova, MAF nudi ugrađene događaje za izvršavanje uključujući:

- `WorkflowStartedEvent`  - Početak izvršavanja radnog toka
- `WorkflowOutputEvent` - Radni tok proizvodi izlaz
- `WorkflowErrorEvent` - Radni tok susreće pogrešku
- `ExecutorInvokeEvent`  - Izvršitelj počinje s obradom
- `ExecutorCompleteEvent`  -  Izvršitelj završava s obradom
- `RequestInfoEvent` - Zahtjev je poslan

## Napredni obrasci MAF-a

Gornji odjeljci pokrivaju ključne koncepte Microsoft Agent Frameworka. Kako gradite složenije agente, evo nekoliko naprednih obrazaca za razmotriti:

- **Složena srednja obrada (Middleware Composition)**: Povežite više srednjih slojeva (logiranje, autentifikacija, ograničenje brzine) koristeći funkcijske i chat srednje slojeve za detaljnu kontrolu ponašanja agenta.
- **Provjera točke unutar radnog toka (Workflow Checkpointing)**: Koristite događaje radnog toka i serijalizaciju za spremanje i nastavak dugotrajnih procesa agenata.
- **Dinamički odabir alata (Dynamic Tool Selection)**: Kombinirajte RAG preko opisa alata s MAF-ovom registracijom alata kako biste prikazali samo relevantne alate za svaki upit.
- **Višestruka predaja između agenata (Multi-Agent Handoff)**: Koristite veze u radnom toku i uvjetno usmjeravanje za orkestraciju predaja između specijaliziranih agenata.

## Hosting LangChain / LangGraph agenata na Microsoft Foundry

Microsoft Agent Framework je **međusobno kompatibilan s drugim okvirima** — niste ograničeni na agente napisane s MAF-om. Ako već imate agenta izgrađenog s **LangChain** ili **LangGraph**, možete ga pokrenuti kao **agenta hostanog na Microsoft Foundry** tako da Foundry upravlja izvršnim vremenom, sesijama, skaliranjem, identitetom i krajnjim točkama protokola za vas, dok vaša logika agenta ostaje u LangGraphu.

To se radi pomoću paketa `langchain_azure_ai.agents.hosting`, koji izlaže kompajlirani LangGraph graf preko istih protokola koje koriste Foundry hostani agenti.

**1. Instalirajte hosting dodatak:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Dodatak `hosting` instalira Foundry biblioteke protokola: `azure-ai-agentserver-responses` (OpenAI-kompatibilna `/responses` krajnja točka) i `azure-ai-agentserver-invocations` (generička `/invocations` krajnja točka).

**2. Odaberite protokol hostinga:**

| Protokol | Klasa hosta | Krajnja točka | Koristi kad |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Želite OpenAI-kompatibilan chat, streaming, povijest odgovora i povezivanje razgovora — preporučeni zadani za razgovorne agente. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Trebate prilagođeni JSON oblik, krajnju točku u stilu webhooka ili ne-razgovornu obradu. |

Budući da je **Responses API glavni API za razvoj agenata u Foundryju**, započnite sa `ResponsesHostServer` za većinu agenata.

**3. Konfigurirajte varijable okoline** (`az login` prvo da se `DefaultAzureCredential` može autentificirati):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Kad agent kasnije radi kao hostani agent u Foundryju, platforma automatski ubrizgava `FOUNDRY_PROJECT_ENDPOINT`.

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI ovdje cilja na Foundry projektov OpenAI-kompatibilni (Responses) endpoint.
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

- **Razgovori**: Klijenti nastavljaju razgovor prosljeđivanjem `previous_response_id` ili ID-a `conversation`. Ako je vaš graf kompajliran s LangGraph checkpointerom, Foundry povezuje stanje razgovora s checkpointom (za produkciju koristite trajni checkpointer; `MemorySaver` je dovoljan za lokalno testiranje).
- **Čovjek-u-petlji (Human-in-the-loop)**: Ako vaš graf koristi LangGraph `interrupt()`, `ResponsesHostServer` prikazuje čekajući prekid kao Responses `function_call` / `mcp_approval_request` stavku, a klijenti nastavljaju s odgovarajućim `function_call_output` / `mcp_approval_response`.
- **Postavljanje u Foundry**: Koristite Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokalno, zahtijeva Docker), zatim `azd provision` i `azd deploy`. Za postavljanje hostanog agenta potrebna je uloga **Foundry Project Manager**.

Izvediva verzija ovog primjera nalazi se u [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Za puni vodič (Invocations protokol, prilagođene sheme zahtjeva i rješavanje problema), pogledajte [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Primjeri koda

Primjere koda za Microsoft Agent Framework možete pronaći u ovom spremištu pod datotekama `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Imate više pitanja o Microsoft Agent Frameworku?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kako biste se upoznali s drugim polaznicima, prisustvovali radnim satima i dobili odgovore na svoja pitanja o AI agentima.
## Prethodna lekcija

[Memorija za AI agente](../13-agent-memory/README.md)

## Sljedeća lekcija


[Izrada agenata za računalnu upotrebu (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->