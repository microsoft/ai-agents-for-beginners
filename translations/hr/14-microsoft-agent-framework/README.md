# Istraživanje Microsoft Agent Frameworka

![Agent Framework](../../../translated_images/hr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Uvod

Ova lekcija će pokriti:

- Razumijevanje Microsoft Agent Frameworka: Ključne značajke i vrijednost
- Istraživanje ključnih pojmova Microsoft Agent Frameworka
- Napredni MAF obrasci: Radni tokovi, Middleware i Memorija

## Ciljevi učenja

Nakon završetka ove lekcije, znat ćete kako:

- Izgraditi spremne za proizvodnju AI agente koristeći Microsoft Agent Framework
- Primijeniti osnovne značajke Microsoft Agent Frameworka na vaše agentske slučajeve korištenja
- Koristiti napredne obrasce uključujući radne tokove, middleware i promatranje

## Primjeri koda

Primjeri koda za [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) mogu se pronaći u ovom repozitoriju pod datotekama `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Razumijevanje Microsoft Agent Frameworka

![Framework Intro](../../../translated_images/hr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) je Microsoftov jedinstveni okvir za izgradnju AI agenata. Nudi fleksibilnost za rješavanje raznih agentskih slučajeva korištenja viđenih u proizvodnim i istraživačkim okruženjima uključujući:

- **Sekvencijalnu orkestraciju agenata** u scenarijima gdje su potrebni korak-po-korak radni tokovi.
- **Istovremenu orkestraciju** u scenarijima gdje agenti trebaju istovremeno dovršavati zadatke.
- **Orkestraciju grupnog chata** u scenarijima gdje agenti mogu surađivati na jednom zadatku.
- **Orkestraciju predaje** u scenarijima gdje agenti predaju zadatke jedni drugima kako se podzadaci dovršavaju.
- **Magnetnu orkestraciju** u scenarijima gdje agent-menadžer stvara i mijenja listu zadataka i koordinira pod-agente za dovršetak zadatka.

Za isporuku AI agenata u proizvodnji, MAF također uključuje značajke za:

- **Promatranje** putem korištenja OpenTelemetry gdje svaka radnja AI agenta uključujući pozive alata, korake orkestracije, tokove rezoniranja i nadzor performansi putem Microsoft Foundry nadzornih ploča.
- **Sigurnost** hostanjem agenata nativno na Microsoft Foundry koji uključuje sigurnosne kontrole kao što su pristup temeljen na ulozi, upravljanje privatnim podacima i ugrađena sigurnost sadržaja.
- **Otpornost** jer se niti i radni tokovi agenta mogu pauzirati, nastaviti i oporaviti od pogrešaka što omogućuje duže izvođenje procesa.
- **Kontrolu** jer su podržani radni tokovi s ljudima u petlji gdje su zadaci označeni kao oni koji zahtijevaju ljudsku potvrdu.

Microsoft Agent Framework također je usredotočen na interoperabilnost kroz:

- **Neovisnost o oblaku** - Agenti mogu raditi u kontejnerima, lokalno i preko više različitih oblaka.
- **Neovisnost o pružatelju usluga** - Agenti se mogu kreirati putem vašeg omiljenog SDK-a uključujući Azure OpenAI i OpenAI
- **Integraciju otvorenih standarda** - Agenti mogu koristiti protokole poput Agent-to-Agent (A2A) i Model Context Protocol (MCP) za otkrivanje i korištenje drugih agenata i alata.
- **Dodatke i konektore** - Moguće su veze s uslugama podataka i memorije poput Microsoft Fabric, SharePoint, Pinecone i Qdrant.

Pogledajmo kako se ove značajke primjenjuju na neke od ključnih pojmova Microsoft Agent Frameworka.

## Ključni pojmovi Microsoft Agent Frameworka

### Agenti

![Agent Framework](../../../translated_images/hr/agent-components.410a06daf87b4fef.webp)

**Kreiranje agenata**

Kreiranje agenta odvija se definiranjem usluge za izvođenje zaključivanja (LLM Provider),
skupa uputa koje AI agent slijedi, i dodijeljenim `imenu`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Gornji primjer koristi `Azure OpenAI`, ali agenti se mogu kreirati koristeći različite usluge uključujući `Microsoft Foundry Agent Service`:

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

ili [MiniMax](https://platform.minimaxi.com/), koji pruža OpenAI-kompatibilni API s velikim kontekstnim prozorima (do 204K tokena):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ili udaljene agente koristeći A2A protokol:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Pokretanje agenata**

Agenti se pokreću korištenjem `.run` ili `.run_stream` metoda za ne-streaming ili streaming odgovore.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Svako pokretanje agenta također može imati opcije za prilagodbu parametara poput `max_tokens` koje agent koristi, `alate` koje agent može pozvati, pa čak i sam `model` koji agent koristi.

Ovo je korisno u slučajevima kada su potrebni specifični modeli ili alati za dovršetak korisničkog zadatka.

**Alati**

Alati se mogu definirati i prilikom definiranja agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Prilikom izravnog stvaranja ChatAgenta

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

i također pri pokretanju agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Alat dostupan samo za ovo pokretanje )
```

**Niti agenta**

Niti agenta koriste se za rukovanje razgovorima s više okretaja. Niti se mogu kreirati na dva načina:

- Korištenjem `get_new_thread()` što omogućuje spremanje niti kroz vrijeme
- Automatskim stvaranjem niti prilikom pokretanja agenta gdje nit traje samo tijekom trenutnog pokretanja.

Za kreiranje niti, kôd izgleda ovako:

```python
# Kreiraj novu dretvu.
thread = agent.get_new_thread() # Pokreni agenta s dretvom.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Niti se zatim može serijalizirati i pohraniti za kasniju upotrebu:

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

Agenti komuniciraju s alatima i LLM-ima kako bi dovršili korisničke zadatke. U određenim scenarijima želimo izvršiti radnju ili pratiti interakcije između njih. Middleware agenta nam omogućuje to kroz:

*Middleware funkcije*

Ovaj middleware omogućuje izvršavanje akcije između agenta i funkcije/alata kojeg poziva. Primjer korištenja je kada želimo zapisati poziv funkcije.

U kodu ispod `next` definira treba li pozvati sljedeći middleware ili stvarnu funkciju.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Preprocesiranje: Zapis prije izvođenja funkcije
    print(f"[Function] Calling {context.function.name}")

    # Nastavi na sljedeći middleware ili izvođenje funkcije
    await next(context)

    # Postprocesiranje: Zapis nakon izvođenja funkcije
    print(f"[Function] {context.function.name} completed")
```

*Middleware chata*

Ovaj middleware omogućuje izvršavanje ili zapisivanje akcije između agenta i zahtjeva između LLM-a.

Ovo sadrži važne informacije poput `poruka` koje se šalju AI servisu.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Predobrada: Zapis prije poziva AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Nastavi na sljedeći middleware ili AI uslugu
    await next(context)

    # Obrada nakon: Zapis nakon odgovora AI
    print("[Chat] AI response received")

```

**Memorija agenta**

Kao što je obrađeno u lekciji `Agentic Memory`, memorija je važan element za omogućavanje agentu da djeluje kroz različite kontekste. MAF nudi nekoliko različitih vrsta memorija:

*Memorija u memoriji (In-Memory Storage)*

Ovo je memorija pohranjena u nitima tijekom rada aplikacije.

```python
# Kreirajte novu nit.
thread = agent.get_new_thread() # Pokrenite agenta s niti.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Postojane poruke (Persistent Messages)*

Ova memorija se koristi za pohranu povijesti razgovora kroz različite sesije. Definira se koristeći `chat_message_store_factory`:

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

*Dinamička memorija*

Ova memorija se dodaje u kontekst prije pokretanja agenata. Ove memorije se mogu pohraniti u vanjskim servisima poput mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Koristeći Mem0 za napredne mogućnosti memorije
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


Promatranje (Observability) je važno za izgradnju pouzdanih i održivih agenatskih sustava. MAF se integrira s OpenTelemetry kako bi pružio praćenje i mjerače za bolje promatranje.

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

Radni tokovi se sastoje od različitih komponenti koje omogućuju bolju kontrolu toka. Radni tokovi također omogućuju **orkestraciju više agenata** i **checkpointing** za spremanje stanja radnog toka.

Osnovne komponente radnog toka su:

**Izvršitelji**

Izvršitelji primaju ulazne poruke, izvršavaju svoje dodijeljene zadatke, a zatim proizvode izlaznu poruku. To pokreće radni tok prema dovršetku većeg zadatka. Izvršitelji mogu biti AI agenti ili prilagođena logika.

**Veze (Edges)**

Veze se koriste za definiranje toka poruka u radnom toku. One mogu biti:

*Izravne veze* - Jednostavne veze jedan-na-jedan između izvršitelja:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Uvjetne veze* - Aktiviraju se nakon što je zadovoljen određeni uvjet. Na primjer, ako su sobe u hotelu nedostupne, izvršitelj može predložiti druge opcije.

*Preklopne veze (Switch-case)* - Usmjeravaju poruke različitim izvršiteljima na temelju definiranih uvjeta. Na primjer, ako putnički korisnik ima prioritetni pristup, njihovi će se zadaci obraditi kroz drugi radni tok.

*Veze širenja (Fan-out)* - Šalju jednu poruku na više odredišta.

*Veze skupljanja (Fan-in)* - Prikupljaju više poruka od različitih izvršitelja i šalju na jedno odredište.

**Događaji**

Kako bi se osigurala bolja promatranost procesa, MAF nudi ugrađene događaje za izvršenje koji uključuju:

- `WorkflowStartedEvent`  - Početak izvršavanja radnog toka
- `WorkflowOutputEvent` - Radni tok proizvodi izlaz
- `WorkflowErrorEvent` - Došlo je do pogreške u radnom toku
- `ExecutorInvokeEvent`  - Izvršitelj započinje obradu
- `ExecutorCompleteEvent`  -  Izvršitelj završava obradu
- `RequestInfoEvent` - Zahtjev je poslan

## Napredni obrasci u MAF-u

Gornji odjeljci pokrivaju ključne pojmove Microsoft Agent Frameworka. Kako gradite složenije agente, evo nekoliko naprednih obrazaca za razmatranje:

- **Sastavljanje middlewarea**: Lanca nekoliko middleware handlera (logiranje, autentikacija, ograničavanje brzine) koristeći funkcijske i chat middleware za preciznu kontrolu ponašanja agenta.
- **Checkpointing radnog toka**: Koristite događaje radnog toka i serijalizaciju za spremanje i nastavak dugotrajnih agenatskih procesa.
- **Dinamički odabir alata**: Kombinirajte RAG preko opisa alata s MAF-ovom registracijom alata za prikaz samo relevantnih alata po upitu.
- **Predaja između više agenata**: Koristite veze radnog toka i uvjetno usmjeravanje za orkestraciju predaja između specijaliziranih agenata.

## Hostanje LangChain / LangGraph agenata na Microsoft Foundry

Microsoft Agent Framework je **interoperabilan s drugim okvirima** — niste ograničeni samo na agente napisane s MAF-om. Ako već imate agenta izgrađenog s **LangChain** ili **LangGraph**, možete ga pokrenuti kao **Foundry hostanog agenta** tako da Foundry upravlja runtime-om, sesijama, skaliranjem, identitetom i krajnjim točkama protokola za vas, dok vaša agentska logika ostaje u LangGraphu.

To se radi pomoću paketa `langchain_azure_ai.agents.hosting`, koji izlaže kompajlirani LangGraph graf kroz iste protokole koje Foundry hostani agenti koriste.

**1. Instalirajte hosting ekstru:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Ekstra hosting instalira Foundry protokol biblioteke: `azure-ai-agentserver-responses` (OpenAI-kompatibilna `/responses` krajnja točka) i `azure-ai-agentserver-invocations` (generička `/invocations` krajnja točka).

**2. Odaberite protokol hostanja:**

| Protokol | Host klasa | Krajnja točka | Koristi kada |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Želite OpenAI-kompatibilan chat, streaming, povijest odgovora i upravljanje razgovorima — preporučeni zadani izbor za razgovorne agente. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Trebate prilagođeni JSON oblik, webhook-stil krajnje točke ili nekonverzacijski proces. |

Budući da je **Responses API primarni API za razvoj agenata u Foundryju**, započnite s `ResponsesHostServer` za većinu agenata.

**3. Konfigurirajte varijable okoline** (`az login` prvo da `DefaultAzureCredential` može autentificirati):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Kad agent kasnije radi kao hostani agent u Foundryju, platforma automatski ubacuje `FOUNDRY_PROJECT_ENDPOINT`.

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

    # ChatOpenAI ovdje cilja na OpenAI-kompatibilnu (Responses) krajnju točku Foundry projekta.
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

- **Razgovori**: Klijenti nastavljaju razgovor prosljeđujući `previous_response_id` ili `conversation` ID. Ako je vaš graf kompajliran s LangGraph checkpointerom, Foundry povezuje stanje razgovora s checkpointom (koristite trajni checkpointer u produkciji; `MemorySaver` je dobar za lokalno testiranje).
- **Čovjek u petlji**: Ako vaš graf koristi LangGraph `interrupt()`, `ResponsesHostServer` prikazuje čekajući prekid kao Responses `function_call` / `mcp_approval_request` stavku, a klijenti nastavljaju s odgovarajućim `function_call_output` / `mcp_approval_response`.
- **Deploy u Foundry**: Koristite Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokalno, zahtijeva Docker), zatim `azd provision` i `azd deploy`. Deploy hostanog agenta zahtijeva ulogu **Foundry Project Manager**.

Izvediv primjer ovog primjera nalazi se u [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Za cjelokupni vodič (Invocations protokol, prilagođeni zahtjevi i rješavanje problema), pogledajte [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Primjeri koda

Primjere koda za Microsoft Agent Framework možete pronaći u ovom spremištu pod datotekama `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Imate li više pitanja o Microsoft Agent Frameworku?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) da se povežete s drugim učenicima, sudjelujete na radnim terminima i dobijete odgovore na svoja pitanja o AI agentima.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->