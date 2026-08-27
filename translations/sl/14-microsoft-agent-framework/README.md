# Raziskovanje Microsoft Agent Framework

![Agent Framework](../../../translated_images/sl/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Uvod

Ta lekcija bo zajemala:

- Razumevanje Microsoft Agent Framework: Ključne funkcije in vrednost  
- Raziskovanje ključnih konceptov Microsoft Agent Framework
- Napredni MAF vzorci: delovni tokovi, middleware in pomnilnik

## Cilji učenja

Po zaključku te lekcije boste znali:

- Zgraditi AI agente, pripravljene za produkcijo, z uporabo Microsoft Agent Framework
- Uporabiti osnovne funkcije Microsoft Agent Framework za vaše primere uporabe agentov
- Uporabiti napredne vzorce, vključno z delovnimi toku, middleware in opaznostjo

## Primeri kode 

Vzorce kode za [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) lahko najdete v tem repozitoriju v datotekah `xx-python-agent-framework` in `xx-dotnet-agent-framework`.

## Razumevanje Microsoft Agent Framework

![Framework Intro](../../../translated_images/sl/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) je Microsoftov enotni okvir za gradnjo AI agentov. Ponuja prilagodljivost za reševanje širokega spektra primerov uporabe agentov, opaženih tako v produkciji kot v raziskovalnih okoljih, vključno z:

- **Zaporedna orkestracija agentov** v scenarijih, kjer so potrebni postopni delovni tokovi.
- **Sočasna orkestracija** v scenarijih, kjer agenti morajo opraviti naloge hkrati.
- **Orkestracija skupinskega klepeta** v scenarijih, kjer lahko agenti sodelujejo na eni nalogi.
- **Orkestracija predaje** v scenarijih, kjer agenti lahko predajo nalogo drug drugemu, ko so podnaloge opravljene.
- **Magnetna orkestracija** v scenarijih, kjer upravljalski agent ustvari in spreminja seznam nalog ter koordinira podagente za izpolnitev naloge.

Za dostavo AI agentov v produkciji ima MAF tudi vključene funkcije za:

- **Opaznost** z uporabo OpenTelemetry, kjer je vsak ukrep AI agenta, vključno z zagonom orodij, koraki orkestracije, tokovi razmišljanja in spremljanje zmogljivosti preko Microsoft Foundry nadzornih plošč.
- **Varnost** s tem, da agenti gostujejo neposredno na Microsoft Foundry, ki vključuje varnostne kontrole, kot so dostop na podlagi vlog, ravnanje z zasebnimi podatki in vgrajena varnost vsebine.
- **Vzdržljivost**, saj se niti agentov in delovni tokovi lahko ustavijo, nadaljujejo in obnovijo po napakah, kar omogoča daljše izvajanje.
- **Nadzor**, saj so podprti delovni tokovi z interakcijo človek-v-zanki, kjer so naloge označene kot zahtevajoče človeško odobritev.

Microsoft Agent Framework je prav tako osredotočen na interoperabilnost z:

- **Neodvisnostjo od oblaka** - agenti lahko tečejo v kontejnerjih, na lokalnih strežnikih in preko več različnih oblakov.
- **Neodvisnostjo od ponudnika** - agenti se lahko ustvarijo preko vašega želenega SDK, vključno z Azure OpenAI in OpenAI
- **Integracijo odprtih standardov** - agenti lahko uporabljajo protokole, kot sta Agent-to-Agent (A2A) in Model Context Protocol (MCP), za odkrivanje in uporabo drugih agentov ter orodij.
- **Vtičniki in povezovalniki** - vzpostavljene so lahko povezave do podatkovnih in pomnilniških storitev, kot so Microsoft Fabric, SharePoint, Pinecone in Qdrant.

Poglejmo, kako se te funkcije uporabljajo pri nekaterih osnovnih konceptih Microsoft Agent Framework.

## Ključni koncepti Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/sl/agent-components.410a06daf87b4fef.webp)

**Ustvarjanje agentov**

Agenti se ustvarjajo z definiranjem storitve sklepanja (LLM ponudnika),  
niza navodil, ki jih mora AI agent slediti, in dodeljenega `imena`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Zgornje uporablja `Azure OpenAI`, vendar lahko agente ustvarjate z različnimi storitvami, vključno z `Microsoft Foundry Agent Service`:

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

ali [MiniMax](https://platform.minimaxi.com/), ki ponuja OpenAI združljiv API z velikimi kontekstnimi okni (do 204K tokenov):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ali oddaljeni agenti, ki uporabljajo A2A protokol:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Zagon agentov**

Agente poganjamo z metodama `.run` ali `.run_stream` za odgovore brez pretoka ali s tokom.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Vsak zagon agenta ima tudi možnosti za prilagajanje parametrov, kot so `max_tokens`, ki jih agent uporablja, `orodja`, ki jih agent lahko kliče, in celo sam `model`, ki ga agent uporablja.

To je uporabno v primerih, ko so za dokončanje uporabnikove naloge potrebni specifični modeli ali orodja.

**Orodja**

Orodja se lahko definirajo tako ob definiranju agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Ko ustvarjate ChatAgent neposredno

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

in tudi ob zagonu agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Orodje zagotovljeno le za to izvajanje )
```

**Niti agentov**

Niti agentov se uporabljajo za obravnavo pogovorov z več obrati. Niti se lahko ustvarijo na dva načina:

- Z uporabo `get_new_thread()`, ki omogoča shranjevanje niti skozi čas
- Avtomatsko ustvarjanje niti med zagonom agenta, pri čemer nit traja le med trenutnim zagonom.

Koda za ustvarjanje niti izgleda takole:

```python
# Ustvari novo nit.
thread = agent.get_new_thread() # Zaženi agenta z nitjo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Nito nato lahko serilizirate za kasnejšo uporabo:

```python
# Ustvari novo nit.
thread = agent.get_new_thread() 

# Zaženi agenta z nitjo.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serijaliziraj nit za shranjevanje.

serialized_thread = await thread.serialize() 

# Deserijaliziraj stanje niti po nalaganju iz shranjevanja.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware agenta**

Agenti sodelujejo z orodji in LLM-ji za dokončanje uporabnikovih nalog. V določenih scenarijih želimo izvesti ali slediti vmesnim interakcijam. Middleware agenta nam to omogoča z:

*Funkcijski middleware*

Ta middleware nam omogoča izvršitev dejanja med agentom in funkcijo/orodjem, ki ga kliče. Primer uporabe je zapisovanje dnevnikov ob klicu funkcije.

V spodnji kodi `next` določa, ali poklicati naslednji middleware ali dejansko funkcijo.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Predobdelava: Beleženje pred izvršitvijo funkcije
    print(f"[Function] Calling {context.function.name}")

    # Nadaljuj na naslednjo vmesno programsko opremo ali izvršitev funkcije
    await next(context)

    # Poprocesiranje: Beleženje po izvršitvi funkcije
    print(f"[Function] {context.function.name} completed")
```

*Chat middleware*

Ta middleware nam omogoča izvršitev ali zapisovanje akcije med agentom in zahtevami do LLM.

Vsebuje pomembne informacije, kot so `messages`, ki se pošiljajo AI storitvi.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Predobdelava: Zabeleži pred klicem AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Nadaljuj na naslednji vmesni program ali AI storitev
    await next(context)

    # Poobdelava: Zabeleži po odgovoru AI
    print("[Chat] AI response received")

```

**Pomnilnik agenta**

Kot je zajeto v lekciji `Agentic Memory`, je pomnilnik pomemben element za omogočanje delovanja agenta skozi različne kontekste. MAF ponuja več različnih vrst pomnilnikov:

*Pomnilnik v pomnilniku (In-Memory Storage)*

To je pomnilnik, shranjen v nitih med izvajanjem aplikacije.

```python
# Ustvari novo nit.
thread = agent.get_new_thread() # Zaženi agenta z nitjo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Vztrajna sporočila*

Ta pomnilnik se uporablja za shranjevanje zgodovine pogovorov skozi različne seje. Določen je z `chat_message_store_factory` :

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

*Dinamični pomnilnik*

Ta pomnilnik se doda v kontekst pred zagonom agentov. Ti pomnilniki se lahko shranjujejo v zunanjih storitvah, kot je mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Uporaba Mem0 za napredne zmogljivosti pomnilnika
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

**Opaznost agenta**

Opaznost je pomembna za gradnjo zanesljivih in vzdržljivih agentnih sistemov. MAF se integrira z OpenTelemetry za zagotavljanje sledenja in meril za boljšo opaznost.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # naredi nekaj
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Delovni tokovi

MAF ponuja delovne tokove, ki so preddefinirani koraki za dokončanje naloge in vključujejo AI agente kot sestavne dele teh korakov.

Delovni tokovi so sestavljeni iz različnih komponent, ki omogočajo boljši nadzor toka. Delovni tokovi omogočajo tudi **orkestracijo več agentov** in **checkpointing** za shranjevanje stanja delovnega toka.

Osnovne komponente delovnega toka so:

**Izvrševalci**

Izvrševalci prejmejo vhodna sporočila, opravijo dodeljene naloge in nato ustvarijo izhodno sporočilo. To premika delovni tok naprej k dokončanju večje naloge. Izvrševalci so lahko AI agenti ali lastna logika.

**Povezave**

Povezave se uporabljajo za določanje toka sporočil v delovnem toku. Lahko so:

*Neposredne povezave* - preproste povezave ena na ena med izvrševalci:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Pogojne povezave* - Aktivirajo se, ko je dosežen določen pogoj. Na primer, ko hotelske sobe niso na voljo, izvrševalec lahko predlaga druge možnosti.

*Preklopne povezave* - Usmerjajo sporočila različnim izvrševalcem glede na definirane pogoje. Na primer, če ima potnik prioriteto in bodo njegove naloge obdelane skozi drug delovni tok.

*Razvejene povezave* - Pošljejo eno sporočilo na več ciljev.

*Združene povezave* - Zberejo več sporočil iz različnih izvrševalcev in jih pošljejo enemu cilju.

**Dogodki**

Za boljšo opaznost delovnih tokov MAF ponuja vgrajene dogodke za izvajanje, kot so:

- `WorkflowStartedEvent`  - Začetek izvajanja delovnega toka
- `WorkflowOutputEvent` - Delovni tok ustvari izhod
- `WorkflowErrorEvent` - Delovni tok naleti na napako
- `ExecutorInvokeEvent`  - Izvrševalec začne obdelavo
- `ExecutorCompleteEvent`  - Izvrševalec konča obdelavo
- `RequestInfoEvent` - Oddana je zahteva

## Napredni MAF vzorci

Zgornji razdelki zajemajo ključne koncepte Microsoft Agent Framework. Ko gradite bolj kompleksne agente, upoštevajte naslednje napredne vzorce:

- **Sestava middleware**: združite več middleware obravnavalcev (logiranje, avtentikacija, omejevanje hitrosti) z uporabo funkcijskega in klepetalnega middleware za natančen nadzor vedenja agenta.
- **Checkpointing delovnega toka**: uporabite dogodke delovnega toka in serilizacijo za shranjevanje in nadaljevanje dolgotrajnih agentnih procesov.
- **Dinamična izbira orodij**: združite RAG preko opisov orodij z MAF registracijo orodij, da prikažete samo relevantna orodja na poizvedbo.
- **Predaja med več agenti**: uporabite povezave delovnega toka in pogojno usmerjanje za orkestracijo predaj med specializiranimi agenti.

## Gostovanje LangChain / LangGraph agentov na Microsoft Foundry

Microsoft Agent Framework je **okvirno interoperabilen** — niste omejeni samo na agente, napisane z MAF. Če že imate agenta zgrajenega z **LangChain** ali **LangGraph**, ga lahko poganjate kot **Microsoft Foundry gostovanega agenta**, tako da Foundry upravlja izvajanje, seje, skaliranje, identiteto in protokolarne končne točke za vas, medtem ko vaša agentska logika ostane v LangGraph.

To se izvaja s paketom `langchain_azure_ai.agents.hosting`, ki razkriva preveden LangGraph graf prek istih protokolov, ki jih uporabljajo Foundry gostovani agenti.

**1. Namestite dodatno paket za gostovanje:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Paket `hosting` namesti Foundry protokolne knjižnice: `azure-ai-agentserver-responses` (združljiva z OpenAI `/responses` končna točka) in `azure-ai-agentserver-invocations` (generična `/invocations` končna točka).

**2. Izberite protokol za gostovanje:**

| Protokol | Razred gostitelja | Končna točka | Uporaba |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Želite klepet, pretakanje, zgodovino odgovorov in nitno poslušanje združljive z OpenAI — priporočena privzeta možnost za pogovorne agente. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Potrebujete prilagojeno JSON obliko, webhook stilsko končno točko ali ne-pogovorno obdelavo. |

Ker je **Responses API primarni API za razvoj agentov v Foundry**, začnite z `ResponsesHostServer` za večino agentov.

**3. Konfigurirajte okoljske spremenljivke** (`az login` najprej, da se `DefaultAzureCredential` lahko avtenticira):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Ko agent pozneje teče kot gostovan agent v Foundry, platforma samodejno vključi `FOUNDRY_PROJECT_ENDPOINT`.

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

    # ChatOpenAI tukaj cilja na OpenAI združljivo (Responses) končno točko projekta Foundry.
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

Zaženite lokalno z `python main.py`, nato pošljite zahtevo Responses na `http://localhost:8088/responses`.

**Ključna vedenja:**

- **Pogovori**: Stranke nadaljujejo pogovor tako, da posredujejo `previous_response_id` ali ID `conversation`. Če je vaš graf preveden s LangGraph checkpointingom, Foundry povezuje stanje pogovora s kontrolno točko (za produkcijo uporabite trajno shranjevanje; `MemorySaver` je dovolj za lokalno testiranje).
- **Človek v zanki**: Če vaš graf uporablja LangGraph `interrupt()`, `ResponsesHostServer` prikaže čakajoče prekinitev kot element v Responses `function_call` / `mcp_approval_request`, stranke pa nadaljujejo z ujemajočim se `function_call_output` / `mcp_approval_response`.
- **Implementacija v Foundry**: Uporabite Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokalno, zahteva Docker), nato `azd provision` in `azd deploy`. Implementacija gostovanega agenta zahteva vlogo **Foundry Project Manager**.

Izvedljiva različica tega primera je na voljo v [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Za celotno razlago (Invocations protokol, prilagojene sheme zahtev in odpravljanje težav) glejte [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Primeri kode 

Vzorce kode za Microsoft Agent Framework lahko najdete v tem repozitoriju v datotekah `xx-python-agent-framework` in `xx-dotnet-agent-framework`.

## Imate še več vprašanj o Microsoft Agent Framework?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da spoznate druge učence, udeležite se uradnih ur in dobite odgovore na vaša vprašanja o AI agentih.
## Prejšnja lekcija

[Pomnilnik za AI agente](../13-agent-memory/README.md)

## Naslednja lekcija

[Gradnja agentov za uporabo računalnika (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->