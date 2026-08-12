# Istraživanje Microsoft Agent Frameworka

![Agent Framework](../../../translated_images/hr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Uvod

Ova lekcija će obuhvatiti:

- Razumijevanje Microsoft Agent Frameworka: Ključne značajke i vrijednost  
- Istraživanje ključnih pojmova Microsoft Agent Frameworka
- Napredni MAF obrasci: Radni tokovi, middleware i memorija

## Ciljevi učenja

Nakon završetka ove lekcije, znat ćete kako:

- Izgraditi AI agente spremne za proizvodnju koristeći Microsoft Agent Framework
- Primijeniti osnovne značajke Microsoft Agent Frameworka na vaše agente slučajeve
- Koristiti napredne obrasce uključujući radne tokove, middleware i promatranje

## Primjeri koda

Primjeri koda za [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) mogu se pronaći u ovom spremištu pod datotekama `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Razumijevanje Microsoft Agent Frameworka

![Framework Intro](../../../translated_images/hr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) je jedinstveni okvir Microsofta za izgradnju AI agenata. Nudi fleksibilnost za rješavanje širokog spektra slučajeva uporabe agenata viđenih i u proizvodnim i u istraživačkim okruženjima, uključujući:

- **Sekvencijalna orkestracija agenta** u scenarijima gdje su potrebni radni tokovi korak-po-korak.
- **Istovremena orkestracija** u scenarijima gdje agenti trebaju istovremeno obavljati zadatke.
- **Orkestracija grupnog chata** u scenarijima gdje agenti mogu surađivati na jednom zadatku.
- **Orkestracija prijenosa** u scenarijima gdje agenti predaju zadatak jedan drugome kako se podzadaci dovršavaju.
- **Magnetna orkestracija** u scenarijima gdje agent upravitelj stvara i mijenja popis zadataka te upravlja koordinacijom podagenata za dovršetak zadatka.

Za isporuku AI agenata u proizvodnji, MAF također uključuje značajke za:

- **Promatranje** kroz korištenje OpenTelemetry gdje je svaka akcija AI agenta uključujući pozivanje alata, korake orkestracije, tijekove razmišljanja i nadzor performansi putem Microsoft Foundry nadzornih ploča.
- **Sigurnost** hostanjem agenata izvorno na Microsoft Foundry koja uključuje sigurnosne kontrole poput pristupa temeljenog na ulogama, rukovanja privatnim podacima i ugrađene sigurnosti sadržaja.
- **Otpornost** jer se niti i radni tokovi agenta mogu pauzirati, nastaviti i oporaviti od pogrešaka što omogućuje dulje trajanje procesa.
- **Kontrola** jer su radni tokovi s ljudima u petlji podržani gdje su zadaci označeni kao oni koji zahtijevaju ljudsko odobrenje.

Microsoft Agent Framework je također fokusiran na interoperabilnost tako da:

- **Bude neovisno o oblaku** - Agent može raditi u spremnicima, lokalno i preko više različitih oblaka.
- **Bude neovisno o pružatelju** - Agent može biti stvoren preko vašeg preferiranog SDK-a uključujući Azure OpenAI i OpenAI
- **Integrira otvorene standarde** - Agent može koristiti protokole poput Agent-to-Agent (A2A) i Model Context Protocol (MCP) za otkrivanje i korištenje drugih agenata i alata.
- **Dodaci i konektori** - Moguće su veze s podatkovnim i memorijskim uslugama poput Microsoft Fabric, SharePoint, Pinecone i Qdrant.

Pogledajmo kako se ove značajke primjenjuju na neke od ključnih pojmova Microsoft Agent Frameworka.

## Ključni pojmovi Microsoft Agent Frameworka

### Agenti

![Agent Framework](../../../translated_images/hr/agent-components.410a06daf87b4fef.webp)

**Stvaranje agenata**

Stvaranje agenta se obavlja definiranjem usluge za izvođenje zaključivanja (LLM pružatelj),  
niza uputa koje AI agent treba slijediti, te dodijeljenim `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Gore je prikazano korištenje `Azure OpenAI` ali agenti se mogu stvarati koristeći različite usluge uključujući `Microsoft Foundry Agent Service`:

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

ili [MiniMax](https://platform.minimaxi.com/), koji pruža OpenAI-kompatibilan API s velikim kontekstnim prozorima (do 204K tokena):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ili udaljeni agenti koristeći A2A protokol:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Pokretanje agenata**

Agent se pokreće korištenjem `.run` ili `.run_stream` metoda za ne-streaming ili streaming odgovore.

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

Ovo je korisno u slučajevima kada su za dovršetak zadatka korisnika potrebni specifični modeli ili alati.

**Alati**

Alati se mogu definirati i prilikom definiranja agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Prilikom izravnog stvaranja ChatAgenta

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

kao i prilikom pokretanja agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Alat dostupan samo za ovo pokretanje )
```

**Niti agenta**

Niti agenta koriste se za rukovanje višekratnim okretajima razgovora. Niti se mogu stvoriti na dva načina:

- Korištenjem `get_new_thread()` što omogućuje spremanje niti tijekom vremena
- Automatskim stvaranjem niti prilikom pokretanja agenta koja traje samo tijekom tekućeg pokretanja.

Za stvaranje niti, kod izgleda ovako:

```python
# Kreiraj novu dretvu.
thread = agent.get_new_thread() # Pokreni agenta s dretvom.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Niti se zatim može serijalizirati kako bi se pohranila za kasniju upotrebu:

```python
# Kreirajte novi thread.
thread = agent.get_new_thread() 

# Pokrenite agenta s threadom.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serijalizirajte thread za pohranu.

serialized_thread = await thread.serialize() 

# Deserijalizirajte stanje threada nakon učitavanja iz pohrane.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware agenta**

Agenti komuniciraju s alatima i LLM-ovima za dovršavanje zadataka korisnika. U određenim scenarijima želimo izvršiti ili pratiti radnje između tih interakcija. Middleware agenta nam omogućuje to kroz:

*Funkcijski Middleware*

Ovaj middleware nam omogućuje izvršavanje akcije između agenta i funkcije/alata koji će biti pozvan. Primjer kada bi se ovo koristilo je ako želite evidentirati pozive funkcija.

U donjem kodu `next` definira treba li pozvati sljedeći middleware ili stvarnu funkciju.

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

    # Naknadna obrada: Zabilježi nakon izvođenja funkcije
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Ovaj middleware nam omogućuje izvršavanje ili evidentiranje akcije između agenta i zahtjeva prema LLM-u.

Ovo sadrži važne informacije kao što su `messages` koje se šalju AI servisu.

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

    # Naknadna obrada: Zabilježi nakon AI odgovora
    print("[Chat] AI response received")

```

**Memorija agenta**

Kao što je obrađeno u lekciji `Agentic Memory`, memorija je važan element za omogućavanje agentu rada kroz različite kontekste. MAF nudi nekoliko različitih tipova memorije:

*Memorija u memoriji (in-memory)*

Ovo je memorija pohranjena u nitima tijekom izvođenja aplikacije.

```python
# Stvori novi thread.
thread = agent.get_new_thread() # Pokreni agenta s threadom.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Trajne poruke*

Ova se memorija koristi za čuvanje povijesti razgovora kroz različite sesije. Definira se pomoću `chat_message_store_factory` :

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

*Dinamična memorija*

Ova se memorija dodaje u kontekst prije pokretanja agenata. Ove memorije se mogu pohranjivati u vanjskim uslugama poput mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Koristeći Mem0 za napredne memorijske mogućnosti
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


Promatranje je važno za izgradnju pouzdanih i održivih agenata sustava. MAF se integrira s OpenTelemetryjem kako bi pružio praćenje i mjerače za bolju promatranost.

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

Radni tokovi se sastoje od različitih komponenti koje omogućuju bolju kontrolu tijeka rada. Radni tokovi također omogućuju **orkestraciju više agenata** i **checkpointing** za spremanje stanja radnog toka.

Glavne komponente radnog toka su:

**Izvršitelji**

Izvršitelji primaju ulazne poruke, izvršavaju dodijeljene zadatke, a zatim proizvode izlaznu poruku. To pokreće radni tok prema dovršetku većeg zadatka. Izvršitelji mogu biti AI agenti ili prilagođena logika.

**Ivice**

Ivice se koriste za definiranje tijeka poruka u radnom toku. One mogu biti:

*Izravne Ivice* - Jednostavne veze jedan-na-jedan između izvršitelja:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Uvjetne Ivice* - Aktiviraju se nakon zadovoljenja određenog uvjeta. Na primjer, kada sobe u hotelu nisu dostupne, izvršitelj može predložiti druge opcije.

*Preklopne Ivice* - Usmjeravaju poruke različitim izvršiteljima na temelju definiranim uvjeta. Na primjer, ako korisnik putovanja ima prioritetni pristup, njegovi će se zadaci obrađivati kroz drugi radni tok.

*Razgranate Ivice* - Šalju jednu poruku na više odredišta.

*Sakupljajuće Ivice* - Prikupljaju više poruka od različitih izvršitelja i šalju ih jednome odredištu.

**Događaji**

Za bolje praćenje radnih tokova, MAF nudi ugrađene događaje za izvršenje uključujući:

- `WorkflowStartedEvent`  - Početak izvođenja radnog toka
- `WorkflowOutputEvent` - Radni tok proizvodi izlaz
- `WorkflowErrorEvent` - Radni tok susreće pogrešku
- `ExecutorInvokeEvent`  - Izvršitelj započinje obradu
- `ExecutorCompleteEvent`  - Izvršitelj završava obradu
- `RequestInfoEvent` - Podnosi se zahtjev

## Napredni MAF obrasci

Gornji dijelovi pokrivaju ključne koncepte Microsoft Agent Framework-a. Kako gradite složenije agente, evo nekoliko naprednih obrazaca koje treba razmotriti:

- **Sastavljanje middleware-a**: Spojite više middleware handlera (logiranje, autentifikacija, ograničenje brzine) koristeći funkcijske i chat middleware za detaljnu kontrolu ponašanja agenata.
- **Checkpointing radnog toka**: Koristite događaje radnog toka i serializaciju za spremanje i nastavak dugotrajnih procesa agenata.
- **Dinamički odabir alata**: Kombinirajte RAG preko opisa alata sa MAF registracijom alata kako biste prikazali samo relevantne alate za određeni upit.
- **Prosljeđivanje između više agenata**: Koristite ivice radnog toka i uvjetno usmjeravanje za orkestraciju prosljeđivanja između specijaliziranih agenata.

## Postavljanje LangChain / LangGraph agenata na Microsoft Foundry

Microsoft Agent Framework je **međuračunski kompatibilan** — niste ograničeni samo na agente napisane s MAF. Ako već imate agenta izrađenog s **LangChain** ili **LangGraph**, možete ga pokrenuti kao **Microsoft Foundry hostiranog agenta** gdje Foundry upravlja runtime-om, sesijama, skaliranjem, identitetom i krajnjim točkama protokola, dok vaša agentska logika ostaje u LangGraphu.

To se radi pomoću paketa `langchain_azure_ai.agents.hosting`, koji izlaže kompajlirani LangGraph graf preko istih protokola koje koriste Foundry hostirani agenti.

**1. Instalirajte hosting dodatak:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Dodatak `hosting` instalira Foundry protokolne biblioteke: `azure-ai-agentserver-responses` (OpenAI-kompatibilna `/responses` krajnja tačka) i `azure-ai-agentserver-invocations` (generička `/invocations` krajnja tačka).

**2. Odaberite hosting protokol:**

| Protokol | Razred hosta | Krajnja točka | Koristi kada |
|---------|--------------|--------------|-------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Želite OpenAI-kompatibilan chat, streaming, povijest odgovora i povezivanje razgovora — preporučeni zadani izbor za konverzacijske agente. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Trebate prilagođeni JSON oblik, webhook-stil krajnju točku ili ne-konverzacijsko procesiranje. |

Budući da je **Responses API primarni API za razvoj agenata u Foundry-u**, započnite s `ResponsesHostServer` za većinu agenata.

**3. Konfigurirajte varijable okruženja** (`az login` prvo da `DefaultAzureCredential` može izvršiti autentifikaciju):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Kad agent kasnije radi kao hostirani agent u Foundry-u, platforma automatski ubacuje `FOUNDRY_PROJECT_ENDPOINT`.

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

    # ChatOpenAI ovdje cilja na OpenAI-kompatibilnu (Responses) točku projekta Foundry.
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

Pokrenite ga lokalno s `python main.py`, zatim pošaljite Requests zahtjev na `http://localhost:8088/responses`.

**Ključna ponašanja:**

- **Razgovori**: Klijenti nastavljaju razgovor prosljeđujući `previous_response_id` ili ID `conversation`. Ako je vaš graf kompajliran s LangGraph checkpointerom, Foundry povezuje stanje razgovora s checkpointom (koristite trajni checkpointer u produkciji; `MemorySaver` je dovoljan za lokalno testiranje).
- **Čovjek u petlji**: Ako vaš graf koristi LangGraph `interrupt()`, `ResponsesHostServer` prikazuje očekivani prekid kao Responses `function_call` / `mcp_approval_request` stavku, a klijenti nastavljaju s odgovarajućim `function_call_output` / `mcp_approval_response`.
- **Implementacija na Foundry**: Koristite Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokalno, zahtijeva Docker), zatim `azd provision` i `azd deploy`. Za implementaciju hostiranog agenta potrebna je uloga **Foundry Project Manager**.

Izvršna verzija ovog primjera nalazi se u [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Za potpun vodič (Invocations protokol, prilagođeni zahtjevi i rješavanje problema), pogledajte [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Primjeri koda

Primjeri koda za Microsoft Agent Framework možete pronaći u ovom spremištu pod datotekama `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Imate još pitanja o Microsoft Agent Framework-u?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) gdje možete upoznati druge učenike, sudjelovati na radionicama i dobiti odgovore na vaša pitanja o AI agentima.
## Prethodni lekcija

[Memory for AI Agents](../13-agent-memory/README.md)

## Sljedeća lekcija

[Building Computer Use Agents (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->