# Raziščemo Microsoft Agent Framework

![Agent Framework](../../../translated_images/sl/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Uvod

Ta lekcija bo obravnavala:

- Razumevanje Microsoft Agent Framework: Ključne funkcije in vrednost  
- Raziščemo ključne koncepte Microsoft Agent Framework
- Napredni MAF vzorci: delovni tokovi, middleware in spomin

## Cilji učenja

Po zaključku te lekcije boste znali:

- Zgraditi proizvodno pripravljene AI agente z uporabo Microsoft Agent Framework
- Uporabiti osnovne funkcije Microsoft Agent Framework za vaše primere uporabe agentov
- Uporabiti napredne vzorce vključno z delovnimi tokovi, middleware in opazovanjem

## Primeri kode 

Primeri kode za [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) lahko najdete v tem repozitoriju v datotekah `xx-python-agent-framework` in `xx-dotnet-agent-framework`.

## Razumevanje Microsoft Agent Framework

![Framework Intro](../../../translated_images/sl/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) je Microsoftov enotni okvir za izdelavo AI agentov. Ponuja prilagodljivost za reševanje široke palete primerov uporabe agentov, ki jih vidimo tako v proizvodnji kot v raziskovalnih okoljih, vključno z:

- **Zaporedna orkestracija agentov** v scenarijih, kjer so potrebni delovni tokovi korak za korakom.
- **Sodobna orkestracija** v primerih, kjer agenti morajo hkrati opraviti naloge.
- **Orkestracija skupinskega klepeta** v primerih, kjer agenti lahko sodelujejo pri eni nalogi.
- **Orkestracija prenosa nalog** v primerih, kjer agenti predajajo naloge drug drugemu, ko so podnaloge končane.
- **Magnetna orkestracija** v primerih, kjer upravljavec agent ustvari in spreminja seznam nalog ter koordinira podagente za dokončanje naloge.

Za zagotavljanje AI agentov v proizvodnji MAF vključuje tudi funkcije za:

- **Opazovanje** preko uporabe OpenTelemetry, kjer se vsako dejanje AI agenta, vključno z uporabo orodij, koraki orkestracije, tokovi razmišljanja in spremljanjem uspešnosti preko Microsoft Foundry nadzornih plošč, beleži.
- **Varnost** z gostovanjem agentov nativno na Microsoft Foundry, ki vključuje varnostne kontrole, kot so dostop osnovan na vlogah, upravljanje zasebnih podatkov in vgrajena varnost vsebin.
- **Vzdržljivost** saj se lahko niti in delovni tokovi agentov začasno ustavijo, nadaljujejo in obnovijo po napakah, kar omogoča daljše izvajanje procesov.
- **Nadzor** saj so podprti delovni tokovi s človekom v zanki, kjer so naloge označene kot zahtevajo odobritev človeka.

Microsoft Agent Framework se osredotoča tudi na interoperabilnost z:

- **Biti neodvisen od oblaka** - Agentje lahko tečejo v kontejnerjih, lokalno ter preko različnih oblakov.
- **Biti neodvisen od ponudnika** - Agentje lahko ustvarite s svojim priljubljenim SDK, vključno z Azure OpenAI in OpenAI.
- **Integrirati odprte standarde** - Agentje lahko uporabljajo protokole, kot so Agent-to-Agent (A2A) in Model Context Protocol (MCP), da odkrijejo in uporabijo druge agente in orodja.
- **Vtičniki in priključki** - Povezave so možne z bazami podatkov in storitvami spomina, kot so Microsoft Fabric, SharePoint, Pinecone in Qdrant.

Oglejmo si, kako so te funkcije uporabljene pri nekaterih osnovnih konceptih Microsoft Agent Framework.

## Ključni koncepti Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/sl/agent-components.410a06daf87b4fef.webp)

**Ustvarjanje agentov**

Ustvarjanje agenta poteka z definiranjem storitve sklepanja (LLM ponudnik), niza navodil, ki jih mora AI agent upoštevati, in dodeljenega `imena`:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Zgornji primer uporablja `Azure OpenAI`, vendar je mogoče agente ustvarjati z različnimi storitvami, vključno s `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API-ji

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ali [MiniMax](https://platform.minimaxi.com/), ki zagotavlja API združljiv z OpenAI z velikimi kontekstnimi okni (do 204K simbolov):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ali oddaljene agente s protokolom A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Zagon agentov**

Agente zaženemo z metodama `.run` ali `.run_stream` za nestraemirane oziroma strimirane odzive.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Vsak zagon agenta lahko vključuje tudi možnosti za prilagajanje parametrov, kot so `max_tokens`, orodja, ki jih agent lahko uporablja, in celo uporabljeni `model`.

To je uporabno v primerih, ko so za dokončanje naloge uporabnika potrebni specifični modeli ali orodja.

**Orodja**

Orodja je mogoče določiti tako pri definiranju agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Ko ustvarjate ChatAgent neposredno

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

kot tudi pri zagonu agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Orodje na voljo samo za to izvedbo )
```

**Vratni tokovi agentov**

Vratni tokovi agentov se uporabljajo za upravljanje pogovorov z več potezami. Vratne tokove lahko ustvarimo na dva načina:

- Uporaba `get_new_thread()`, ki omogoča shranjevanje vratnega toka s časom
- Samodejno ustvarjanje vrata med izvajanjem agenta, kjer vrata obstajajo samo med tekom

Za ustvarjanje vrat ta koda izgleda takole:

```python
# Ustvari novo nit.
thread = agent.get_new_thread() # Zaženi agenta z nitjo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Vratni tok lahko nato serializirate za poznejšo uporabo:

```python
# Ustvari novo nit.
thread = agent.get_new_thread() 

# Zaženi agenta z nitjo.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serijaliziraj nit za shranjevanje.

serialized_thread = await thread.serialize() 

# Deserijaliziraj stanje niti po nalaganju iz shrambe.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware agentov**

Agenti sodelujejo z orodji in LLM, da izpolnijo naloge uporabnikov. V določenih scenarijih želimo med temi interakcijami izvesti ali slediti nekim dejanjem. Middleware agentov nam omogoča to preko:

*Middleware funkcije*

Ta middleware omogoča izvedbo dejanja med agentom in funkcijo/orodjem, ki jo kliče. Primer uporabe je beleženje klica funkcije.

V spodnji kodi `next` določa, ali naj se pokliče naslednji middleware ali dejanska funkcija.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pred-obdelava: Zabeleži pred izvajanjem funkcije
    print(f"[Function] Calling {context.function.name}")

    # Nadaljuj na naslednji vmesni program ali izvajanje funkcije
    await next(context)

    # Po-obdelava: Zabeleži po izvajanju funkcije
    print(f"[Function] {context.function.name} completed")
```

*Middleware za klepet*

Ta middleware omogoča izvedbo ali beleženje dejanja med agentom in zahtevami med LLM.

Vključuje pomembne podatke, kot so `messages`, ki se pošiljajo AI storitvi.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Predobdelava: Zabeleži pred klicem AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Nadaljuj do naslednjega vmesnega sloja ali AI storitve
    await next(context)

    # Pobiranje po obdelavi: Zabeleži po odgovoru AI
    print("[Chat] AI response received")

```

**Spomin agentov**

Kot je predstavljeno v lekciji `Agentic Memory`, je spomin pomemben za omogočanje delovanja agenta preko različnih kontekstov. MAF ponuja več vrst spomina:

*Shranjevanje v pomnilnik (In-Memory Storage)*

To je spomin, ki se hrani v vratnih tokovih med izvajanjem aplikacije.

```python
# Ustvari novo nit.
thread = agent.get_new_thread() # Zaženi agenta z nitjo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Vzdržna sporočila (Persistent Messages)*

Ta spomin se uporablja za shranjevanje zgodovine pogovorov čez različne seje. Določi se z `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Ustvari prilagojeno skladišče sporočil
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dinamični spomin (Dynamic Memory)*

Ta spomin se doda v kontekst pred zagonom agentov. Lahko se shrani v zunanjih storitvah, kot je mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Uporaba Mem0 za napredne spominske zmogljivosti
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

**Opazovanje agentov (Observability)**

Opazovanje je pomembno za gradnjo zanesljivih in vzdržljivih agentskih sistemov. MAF se integrira z OpenTelemetry za zagotavljanje sledenja in meritev za boljše opazovanje.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # nekaj narediti
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Delovni tokovi (Workflows)

MAF ponuja delovne tokove, ki so prednastavljeni koraki za dokončanje naloge in vključujejo AI agente kot komponente teh korakov.

Delovni tokovi so sestavljeni iz različnih komponent, ki omogočajo boljši nadzor pretoka. Prav tako omogočajo **orkestracijo več agentov** in **checkpointing** za shranjevanje stanj delovnega toka.

Osnovne komponente delovnega toka so:

**Izvrševalci (Executors)**

Izvrševalci prejmejo vhodna sporočila, opravijo dodeljene naloge in nato proizvedejo izhodno sporočilo. Tako se delovni tok premakne proti dokončanju večje naloge. Izvrševalci so lahko AI agent ali po meri izdelana logika.

**Povezave (Edges)**

Povezave se uporabljajo za definicijo toka sporočil v delovnem toku. Te so lahko:

*Neposredne povezave* - enostavne povezave enega na enega med izvrševalci:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Pogojne povezave* - Aktivirajo se ob izpolnitvi določenega pogoja. Na primer, ko sob ni na voljo, izvrševalec lahko predlaga druge možnosti.

*Stikalne povezave* - Usmerjajo sporočila različnim izvrševalcem na podlagi določenih pogojev. Na primer, če ima potnik prioritetni dostop, se njegove naloge obravnavajo skozi drug delovni tok.

*Razvejujoče povezave* - Pošlje eno sporočilo več prejemnikom.

*Zvezujoče povezave* - Zbere več sporočil od različnih izvrševalcev in jih pošlje enemu prejemniku.

**Dogodki**

Za boljše opazovanje delovnih tokov MAF nudi vgrajene dogodke za izvajanje, vključno z:

- `WorkflowStartedEvent`  - Začetek izvajanja delovnega toka
- `WorkflowOutputEvent` - Delovni tok proizvede izhod
- `WorkflowErrorEvent` - Delovni tok zazna napako
- `ExecutorInvokeEvent`  - Izvrševalec začne obdelavo
- `ExecutorCompleteEvent`  - Izvrševalec konča obdelavo
- `RequestInfoEvent` - Izvaja se zahteva

## Napredni MAF vzorci

Zgornji odseki pokrivajo ključne koncepte Microsoft Agent Framework. Ko zgradite kompleksnejše agente, razmislite o teh naprednih vzorcih:

- **Sestavljanje middleware**: Verižite več middleware rokovalcev (beleženje, avtentikacija, omejevanje hitrosti) z uporabo funkcijskega in klepetalnega middleware za natančen nadzor vedenja agenta.
- **Checkpointing delovnega toka**: Uporabite dogodke delovnega toka in serializacijo za shranjevanje in nadaljevanje dolgotrajnih procesov agenta.
- **Dinamična izbira orodij**: Združite RAG nad opisi orodij z MAF registracijo orodij, da prikažete le relevantna orodja za posamezen zahtevek.
- **Prenos med več agenti**: Uporabite robove delovnega toka in pogojno usmerjanje za orkestracijo prenosa nalog med specializiranimi agenti.

## Gostovanje LangChain / LangGraph agentov na Microsoft Foundry

Microsoft Agent Framework je **medframeworksko združljiv** — niste omejeni na agente napisane samo z MAF. Če že imate agenta zgrajenega z **LangChain** ali **LangGraph**, ga lahko zaženete kot **agenta gostovanega na Microsoft Foundry**, tako da Foundry upravlja zagonsko okolje, seje, skaliranje, identiteto in protokolarne končne točke, medtem ko vaša agentna logika ostane v LangGraph.

To se naredi znotraj paketa `langchain_azure_ai.agents.hosting`, ki razkriva sestavljeno LangGraph vozlišče preko enakih protokolov, ki jih uporabljajo Foundry agenti.

**1. Namestite dodatke za gostovanje:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Dodatna funkcija `hosting` namesti Foundry protokolarne knjižnice: `azure-ai-agentserver-responses` (združljiv repozitorij z OpenAI `/responses` končno točko) in `azure-ai-agentserver-invocations` (generična `/invocations` končna točka).

**2. Izberite gostovalni protokol:**

| Protokol | Gostiteljska razreda | Končna točka | Uporaba |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Želite OpenAI-ju združljiv klepet, pretakanje, zgodovino odzivov in večnitno razpravo — priporočen privzeti za pogovorne agente. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Potrebujete prilagojen JSON format, webhook-stilsko končno točko ali ne-pogovorno obdelavo. |

Ker je **API za Responses primarni API za razvoj agentov v Foundry**, začnite z `ResponsesHostServer` za večino agentov.

**3. Konfigurirajte okoljske spremenljivke** (`az login` najprej, da se lahko `DefaultAzureCredential` avtenticira):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Ko agent teče kot gostovani agent v Foundry, platforma samodejno injicira `FOUNDRY_PROJECT_ENDPOINT`.

**4. Razkrijte LangGraph agenta preko protokola Responses:**

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

    # ChatOpenAI tukaj cilja na OpenAI-kompatibilno (Responses) končno točko projekta Foundry.
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

Zaženite ga lokalno z `python main.py`, nato pošljite zahtevek Responses na `http://localhost:8088/responses`.

**Ključna vedenja:**

- **Pogovori**: Stranke nadaljujejo pogovor s prenosom `previous_response_id` ali `conversation` ID. Če je vaš graf sestavljen z LangGraph checkpoint sistemom, Foundry povezuje stanje pogovora s checkpointom (v proizvodnji uporabite vzdržljiv checkpoint, `MemorySaver` je dovolj za lokalno testiranje).
- **Človek v zanki**: Če vaš graf uporablja LangGraph `interrupt()`, `ResponsesHostServer` prikaže čakajoči prekinitev kot item `function_call` / `mcp_approval_request` v Responses, in stranke nadaljujejo z ustreznim `function_call_output` / `mcp_approval_response`.
- **Deploy v Foundry**: Uporabite Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokalno, zahteva Docker), nato `azd provision` in `azd deploy`. Za namestitev gostovanega agenta je potrebna vloga **Foundry Project Manager**.

Za zagon te primere glejte [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Za celoten vodič (protokol Invocations, prilagojeni shemi zahtevkov in odpravljanje težav) glejte [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Primeri kode 

Primeri kode za Microsoft Agent Framework lahko najdete v tem repozitoriju v datotekah `xx-python-agent-framework` in `xx-dotnet-agent-framework`.

## Imate več vprašanj o Microsoft Agent Framework?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da se srečate z drugimi učenci, udeležite uradnih ur in dobite odgovore na svoja vprašanja o AI agentih.
## Prejšnja lekcija

[Memory for AI Agents](../13-agent-memory/README.md)

## Naslednja lekcija

[Izgradnja agentov za uporabo računalnika (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->