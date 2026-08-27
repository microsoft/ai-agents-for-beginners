# Istraživanje Microsoft Agent Frameworka

![Agent Framework](../../../translated_images/hr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Uvod

Ova lekcija će obuhvatiti:

- Razumijevanje Microsoft Agent Frameworka: Ključne značajke i vrijednost  
- Istraživanje ključnih koncepata Microsoft Agent Frameworka
- Napredni MAF obrasci: Radni tokovi, Middleware i memorija

## Ciljevi učenja

Nakon što završite ovu lekciju, znat ćete kako:

- Izgraditi AI agente spremne za produkciju koristeći Microsoft Agent Framework
- Primijeniti osnovne značajke Microsoft Agent Frameworka na vaše agentne slučajeve korištenja
- Koristiti napredne obrasce uključujući radne tokove, middleware i promatranje

## Primjeri koda

Primjeri koda za [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) mogu se pronaći u ovom repozitoriju pod datotekama `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Razumijevanje Microsoft Agent Frameworka

![Framework Intro](../../../translated_images/hr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) je Microsoftov jedinstveni okvir za izgradnju AI agenata. Nudi fleksibilnost za adresiranje širokog raspona agentno orijentiranih slučajeva korištenja viđenih kako u proizvodnom okruženju tako i u istraživačkim okruženjima uključujući:

- **Sekvencijalna orkestracija agenata** u scenarijima gdje su potrebni korak-po-korak radni tokovi.
- **Istovremena orkestracija** u scenarijima gdje agenti trebaju izvršavati zadatke istovremeno.
- **Orkestracija grupnog chata** u scenarijima gdje agenti mogu surađivati na jednom zadatku.
- **Orkestracija predaje zadataka** u scenarijima gdje agenti predaju zadatke jedan drugome kako podzadatci budu završeni.
- **Magnetna orkestracija** u scenarijima gdje agent menadžer stvara i mijenja listu zadataka i upravlja koordinacijom podagenata za izvršenje zadatka.

Za isporuku AI agenata u produkciji, MAF također uključuje značajke za:

- **Promatranje** kroz korištenje OpenTelemetry gdje se svaka akcija AI agenta uključujući poziv alata, orkestracijske korake, tok razmišljanja i nadzor performansi kroz Microsoft Foundry nadzorne ploče.
- **Sigurnost** hostanjem agenata nativno na Microsoft Foundry koja uključuje sigurnosne kontrole kao što su pristup temeljen na ulogama, rukovanje privatnim podacima i ugrađena sigurnost sadržaja.
- **Izdržljivost** jer se niti i radni tokovi agenata mogu pauzirati, nastaviti i oporaviti od pogrešaka što omogućuje duže trajanje procesa.
- **Kontrola** jer se podupiru radni tokovi sa ljudima u petlji gdje su zadaci označeni kao zahtijevajući ljudsko odobrenje.

Microsoft Agent Framework također je usredotočen na interoperabilnost kroz:

- **Neovisnost o oblaku** - Agenti mogu raditi u kontejnerima, na lokaciji i na različitim oblak servisima.
- **Neovisnost o pružatelju usluga** - Agenti mogu biti kreirani kroz vaš omiljeni SDK uključujući Azure OpenAI i OpenAI
- **Integracija otvorenih standarda** - Agenti mogu koristiti protokole poput Agent-to-Agent (A2A) i Model Context Protocol (MCP) za otkrivanje i korištenje drugih agenata i alata.
- **Dodaci i konektori** - Mogu se uspostaviti veze s podacima i memorijskim servisima poput Microsoft Fabric, SharePoint, Pinecone i Qdrant.

Pogledajmo kako se ove značajke primjenjuju na neke od osnovnih koncepata Microsoft Agent Frameworka.

## Ključni koncepti Microsoft Agent Frameworka

### Agenti

![Agent Framework](../../../translated_images/hr/agent-components.410a06daf87b4fef.webp)

**Kreiranje agenata**

Kreiranje agenta obavlja se definiranjem usluge za izvođenje zaključivanja (LLM Provider), 
skupa uputa koje AI agent treba slijediti, i dodjeljenim `imenu`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Gornji primjer koristi `Azure OpenAI` ali agenti se mogu kreirati koristeći razne usluge uključujući `Microsoft Foundry Agent Service`:

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

Agent se pokreće koristeći `.run` ili `.run_stream` metode za ne-streaming ili streaming odgovore.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Svaki poziv agenta može imati i opcije za prilagođavanje parametara kao što su `max_tokens` koje agent koristi, `tools` koje agent može pozvati, i čak `model` koji se koristi za agenta.

Ovo je korisno u slučajevima kada su specifični modeli ili alati potrebni za dovršetak korisničkog zadatka.

**Alati**

Alati se mogu definirati i pri definiranju agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Prilikom izravnog stvaranja ChatAgenta

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

a također i prilikom pokretanja agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Alat dostupan samo za ovu izvedbu )
```

**Niti agenta**

Niti agenta služe za upravljanje višekratnim razgovorima. Niti se mogu kreirati na dva načina:

- Korištenjem `get_new_thread()` koji omogućuje da se nit pohrani tijekom vremena
- Automatskim stvaranjem niti prilikom pokretanja agenta koja traje samo tijekom trenutnog poziva.

Za kreiranje niti, kôd izgleda ovako:

```python
# Stvori novi thread.
thread = agent.get_new_thread() # Pokreni agenta s threadom.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Nit se potom može serijalizirati za kasniju upotrebu:

```python
# Kreiraj novu nit.
thread = agent.get_new_thread() 

# Pokreni agenta s niti.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serijaliziraj nit za pohranu.

serialized_thread = await thread.serialize() 

# Deserijaliziraj stanje niti nakon učitavanja iz pohrane.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware agenta**

Agenti komuniciraju s alatima i LLM-ovima kako bi izvršavali korisničke zadatke. U određenim scenarijima želimo izvršiti ili pratiti radnje između tih interakcija. Middleware agenta nam to omogućuje kroz:

*Function Middleware*

Ovaj middleware nam omogućuje izvršenje akcije između agenta i funkcije/alata kojeg agent poziva. Primjer kada se to koristi je bilježenje poziva funkcije.

U donjem kodu `next` definira treba li se pozvati sljedeći middleware ili sama funkcija.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pretprocesiranje: Zabilježi prije izvršenja funkcije
    print(f"[Function] Calling {context.function.name}")

    # Nastavi na sljedeći middleware ili izvršenje funkcije
    await next(context)

    # Postprocesiranje: Zabilježi nakon izvršenja funkcije
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Ovaj middleware omogućuje izvršenje ili bilježenje akcije između agenta i zahtjeva između LLM-a.

Ovime se sadrže važne informacije kao što su `messages` koji se šalju AI servisu.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Predobrada: Zapis prije poziva AI-ja
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Nastavi na sljedeći middleware ili AI uslugu
    await next(context)

    # Postobrada: Zapis nakon odgovora AI-ja
    print("[Chat] AI response received")

```

**Memorija agenta**

Kao što je objašnjeno u lekciji `Agentic Memory`, memorija je važan element za omogućavanje rada agenta kroz različite kontekste. MAF nudi nekoliko različitih vrsta memorije:

*Memorija u memoriji*

Ovo je memorija pohranjena u nitima tijekom rada aplikacije.

```python
# Kreiraj novu nit.
thread = agent.get_new_thread() # Pokreni agenta s niti.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Trajne poruke*

Ova memorija se koristi kod pohrane povijesti razgovora tijekom različitih sesija. Definira se pomoću `chat_message_store_factory`:

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


Ova memorija se dodaje u kontekst prije pokretanja agenata. Ove memorije mogu biti pohranjene u vanjskim uslugama kao što je mem0:

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

Radni tokovi se sastoje od različitih komponenti koje omogućuju bolju kontrolu toka. Radni tokovi također omogućuju **višestruku orkestraciju agenata** i **spremanje točaka prekida** za pohranu stanja radnog toka.

Jezgrene komponente radnog toka su:

**Izvršitelji**

Izvršitelji primaju ulazne poruke, izvršavaju dodijeljene zadatke, a zatim proizvode izlaznu poruku. Time se radni tok pomiče prema dovršetku većeg zadatka. Izvršitelji mogu biti AI agenti ili prilagođena logika.

**Ivice**

Ivice se koriste za definiranje toka poruka u radnom toku. One mogu biti:

*Izravne ivice* - Jednostavne veze jedan-na-jedan između izvršitelja:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Uvjetne ivice* - Aktiviraju se kad se ispuni određeni uvjet. Na primjer, kad nema dostupnih hotelskih soba, izvršitelj može predložiti druge opcije.

*Ivice tipa switch-case* - Usmjeravaju poruke različitim izvršiteljima na temelju definiranih uvjeta. Na primjer, ako putnik ima prioritetni pristup, njegovi će zadaci biti obrađeni kroz drugi radni tok.

*Ivice za razdvajanje (fan-out)* - Šalju jednu poruku više odredišta.

*Ivice za spajanje (fan-in)* - Skupljaju više poruka od različitih izvršitelja i šalju ih jednom odredištu.

**Događaji**

Kako bi se omogućilo bolje promatranje radnih tokova, MAF nudi ugrađene događaje za izvršavanje, uključujući:

- `WorkflowStartedEvent`  - Pokretanje izvršavanja radnog toka
- `WorkflowOutputEvent` - Radni tok proizvodi izlaz
- `WorkflowErrorEvent` - Radni tok susreće pogrešku
- `ExecutorInvokeEvent`  - Izvršitelj započinje obradu
- `ExecutorCompleteEvent`  -  Izvršitelj završava obradu
- `RequestInfoEvent` - Izdan je zahtjev

## Napredni MAF obrasci

Gore navedeni odjeljci pokrivaju ključne koncepte Microsoft Agent Frameworka. Kako gradite složenije agente, evo nekoliko naprednih obrazaca za razmatranje:

- **Složena međuslojna obrada**: Spajanje više middleware handlera (logiranje, autentikacija, ograničenje brzine) korištenjem funkcijske i chat middleware za finu kontrolu ponašanja agenta.
- **Spremanje stanja radnog toka**: Korištenje događaja radnog toka i serijalizacije za spremanje i nastavak dugotrajnih procesa agenata.
- **Dinamički odabir alata**: Kombinacija RAG-a nad opisima alata sa MAF-ovom registracijom alata kako bi se prikazali samo relevantni alati po upitu.
- **Prijenos između više agenata**: Korištenje radnih tokova i uvjetnog usmjeravanja za orkestraciju prijenosa zadataka između specijaliziranih agenata.

## Hosting LangChain / LangGraph agenata na Microsoft Foundry

Microsoft Agent Framework je **okvirno interoperabilan** — niste ograničeni na agente napisane u MAF-u. Ako već imate agenta izrađenog s **LangChain** ili **LangGraph**, možete ga pokrenuti kao **genom Microsoft Foundry** gdje Foundry upravlja runtimeom, sesijama, skaliranjem, identitetom i krajnjim točkama protokola za vas, dok vaša logika ostaje u LangGraphu.

To se radi putem paketa `langchain_azure_ai.agents.hosting`, koji izlaže kompajlirani LangGraph graf preko istih protokola koje koriste Foundry hosted agenti.

**1. Instalirajte hosting dodatak:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Dodatak `hosting` instalira Foundry protokol biblioteke: `azure-ai-agentserver-responses` (OpenAI-kompatibilna `/responses` krajnja točka) i `azure-ai-agentserver-invocations` (generička `/invocations` krajnja točka).

**2. Odaberite protokol hostinga:**

| Protokol | Host klasa | Krajnja točka | Koristi se kada |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Želite OpenAI-kompatibilni chat, streaming, povijest odgovora i uvezivanje razgovora — preporučeni zadani za konverzacijske agente. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Trebate prilagođeni JSON format, webhook-stil krajnju točku ili nekonverzacijsku obradu. |

Budući da je **Responses API primarni API za razvoj agenata u Foundryju**, započnite s `ResponsesHostServer` za većinu agenata.

**3. Konfigurirajte varijable okoline** (`az login` prvo da `DefaultAzureCredential` može provjeriti vjerodajnice):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Kad agent kasnije radi kao hosted agent u Foundryju, platforma automatski injektira `FOUNDRY_PROJECT_ENDPOINT`.

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

    # ChatOpenAI ovdje cilja na Foundry projektni OpenAI-kompatibilni (Responses) endpoint.
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

Pokrenite ga lokalno s `python main.py`, zatim pošaljite Responses zahtjev na `http://localhost:8088/responses`.

**Ključna ponašanja:**

- **Razgovori**: Klijenti nastavljaju razgovor prosljeđujući `previous_response_id` ili ID `conversation`. Ako je vaš graf kompajliran s LangGraph checkpointom, Foundry povezuje stanje razgovora s tom točkom (koristite izdržljiv checkpoint u produkciji; `MemorySaver` je dobar za lokalno testiranje).
- **Čovjek u petlji**: Ako vaš graf koristi LangGraph `interrupt()`, `ResponsesHostServer` prikazuje čekajući prekid kao stavku `function_call` / `mcp_approval_request` u Responses, a klijenti nastavljaju s odgovarajućim `function_call_output` / `mcp_approval_response`.
- **Implementacija u Foundry**: Koristite Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokalno, zahtijeva Docker), zatim `azd provision` i `azd deploy`. Implementacija hosted agenta zahtijeva ulogu **Foundry Project Manager**.

Izvediva verzija ovog primjera nalazi se u [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Za cjeloviti vodič (Invocations protokol, prilagođeni zahtjevni schemovi i rješavanje problema), pogledajte [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Primjeri koda 

Primjeri koda za Microsoft Agent Framework mogu se pronaći u ovom repozitoriju pod datotekama `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Imate dodatnih pitanja o Microsoft Agent Frameworku?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) da biste se upoznali s drugim učenicima, prisustvovali uredskim satima i dobili odgovore na pitanja o AI agentima.
## Prethodna lekcija

[Memory for AI Agents](../13-agent-memory/README.md)

## Sljedeća lekcija


[Izrada agenata za korištenje računala (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->