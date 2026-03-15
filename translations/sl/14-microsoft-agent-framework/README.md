# Raziskovanje Microsoft Agent Framework

![Agent Framework](../../../translated_images/sl/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Uvod

Ta lekcija bo zajemala:

- Razumevanje Microsoft Agent Framework: Ključne funkcije in vrednost  
- Raziskovanje ključnih konceptov Microsoft Agent Framework
- Napredni MAF vzorci: delovni tokovi, middleware in pomnilnik

## Cilji učenja

Po zaključenem tečaju boste znali:

- Graditi rešene AI agente s pomočjo Microsoft Agent Framework
- Uporabiti osnovne funkcije Microsoft Agent Framework za svoje agentske primere uporabe
- Uporabiti napredne vzorce, vključno z delovnimi tokovi, middleware in opazovanjem

## Primeri kode

Primeri kode za [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) lahko najdete v tem repozitoriju pod datotekami `xx-python-agent-framework` in `xx-dotnet-agent-framework`.

## Razumevanje Microsoft Agent Framework

![Framework Intro](../../../translated_images/sl/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) je Microsoftov enotni okvir za gradnjo AI agentov. Ponuja prilagodljivost za različne agentske primere uporabe, ki jih opazimo tako v produkciji kot v raziskovalnih okoljih, vključno z:

- **Zaporedno orkestracijo agentov** v primerih, kjer so potrebni korak-po-korak delovni tokovi.
- **Sočasno orkestracijo** v primerih, kjer morajo agenti dokončati naloge hkrati.
- **Orkestracijo skupinskega pogovora** v primerih, ko agenti sodelujejo pri eni nalogi.
- **Orkestracijo predaje** v primerih, kjer agenti predajajo nalogo drug drugemu, ko so delovne naloge zaključene.
- **Magnetno orkestracijo** v primerih, kjer upravljavski agent ustvarja in ureja seznam nalog ter upravlja koordinacijo podagentov za dokončanje naloge.

Za zagotavljanje AI agentov v produkciji MAF vključuje tudi funkcije za:

- **Opazovanje** preko uporabe OpenTelemetry, kjer so zabeležena vsaka dejanja AI agenta, vključno z izvajanjem orodij, koraki orkestracije, poteki razmišljanja in spremljanjem uspešnosti prek Microsoft Foundry nadzornih plošč.
- **Varnost** z gostovanjem agentov neposredno na Microsoft Foundry, ki vključuje varnostne kontrole, kot so dostop na osnovi vlog, ravnanje z zasebnimi podatki in vgrajena varnost vsebine.
- **Vzdržljivost** saj se niti agentov in delovni tokovi lahko začasno ustavijo, nadaljujejo in obnovijo po napakah, kar omogoča daljše trajanje procesov.
- **Nadzor** saj so podprti delovni tokovi s človekom v zanki, kjer so naloge označene kot potrebne človekove odobritve.

Microsoft Agent Framework se osredotoča tudi na interoperabilnost z:

- **Neodvisnostjo od oblaka** - Agenti lahko tečejo v vsebnikih, lokalno in na več različnih oblakih.
- **Neodvisnostjo od ponudnika** - Agente lahko ustvarite preko svojega priljubljenega SDK-ja vključno z Azure OpenAI in OpenAI
- **Integracijo odprtih standardov** - Agenti lahko uporabljajo protokole, kot sta Agent-to-Agent (A2A) in Model Context Protocol (MCP), da odkrijejo in uporabijo druge agente in orodja.
- **Vtičniki in priključki** - Povezave se lahko ustvarijo do podatkovnih in pomnilniških storitev, kot so Microsoft Fabric, SharePoint, Pinecone in Qdrant.

Poglejmo, kako so te funkcije uporabljene v nekaterih osnovnih konceptih Microsoft Agent Framework.

## Ključni koncepti Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/sl/agent-components.410a06daf87b4fef.webp)

**Ustvarjanje agentov**

Ustvarjanje agenta poteka z definiranjem inferenčne storitve (LLM ponudnik), nabora navodil, ki jih mora AI agent slediti, in dodeljenim `imenom`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Gornji primer uporablja `Azure OpenAI`, a agente lahko ustvarite z različnimi storitvami, vključno z `Microsoft Foundry Agent Service`:

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

ali oddaljenimi agenti preko protokola A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Zagon agentov**

Agent se zažene z metodama `.run` ali `.run_stream` za nereferenčne ali pretočne odgovore.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Vsak zagon agenta ima lahko tudi možnosti za prilagajanje parametrov, kot so `max_tokens`, ki jih agent uporablja, `orodja`, ki jih agent lahko kliče, in celo sam `model`, ki ga agent uporablja.

To je uporabno v primerih, kjer so za dokončanje uporabnikove naloge potrebni določeni modeli ali orodja.

**Orodja**

Orodja lahko določite tako ob definiranju agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Ko neposredno ustvarjate ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

kot tudi ob zagonu agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Orodje na voljo samo za to izvajanje )
```

**Niti agentov**

Niti agentov se uporabljajo za večkratna pogovorna kroženja. Niti se lahko ustvarijo na dva načina:

- Z uporabo `get_new_thread()`, ki omogoča, da se nit shrani skozi čas
- Samodejno ustvarjanje niti med zagonom agenta, pri čemer nit traja samo med trenutnim zagonom.

Za ustvarjanje niti koda izgleda takole:

```python
# Ustvari novo nit.
thread = agent.get_new_thread() # Zaženi agenta z nitjo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Nit lahko nato serializirate za kasnejšo uporabo:

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

**Agent Middleware**

Agenti sodelujejo z orodji in LLM-ji za dokončanje uporabnikovih nalog. V določenih scenarijih želimo izvesti ali spremljati interakcije med njimi. Agent middleware nam to omogoča preko:

*Funkcijski Middleware*

Ta middleware omogoča izvajanje dejanja med agentom in funkcijo/orodjem, ki ga kliče. Primer uporabe je beleženje klica funkcije.

V spodnji kodi `next` določa, ali naj se pokliče naslednji middleware ali funkcija sama.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Predobdelava: Zabeleži pred izvedbo funkcije
    print(f"[Function] Calling {context.function.name}")

    # Nadaljuj do naslednjega vmesnega sloja ali izvedbe funkcije
    await next(context)

    # Poobdelava: Zabeleži po izvedbi funkcije
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Ta middleware omogoča izvajanje ali beleženje dejanja med agentom in zahtevami med LLM-jem.

Vsebuje pomembne informacije, kot so `sporočila`, ki se pošiljajo AI storitvi.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Predobdelava: Zabeleži pred klicem AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Nadaljuj na naslednji vmesni sloj ali AI storitev
    await next(context)

    # Poobdelava: Zabeleži po odgovoru AI
    print("[Chat] AI response received")

```

**Agentov pomnilnik**

Kot je opisano v lekciji `Agentic Memory`, je pomnilnik pomemben element za omogočanje agenta delovanja v različnih kontekstih. MAF ponuja več vrst pomnilnikov:

*Pomnilnik v spominu*

To je pomnilnik, ki se hrani v nitih med izvajanjem aplikacije.

```python
# Ustvari novo nit.
thread = agent.get_new_thread() # Zaženi agenta z nitjo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Trajna sporočila*

Ta pomnilnik se uporablja za shranjevanje zgodovine pogovorov med različnimi sejami. Definira se z uporabo `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Ustvari po meri shrambo sporočil
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dinamični pomnilnik*

Ta pomnilnik se doda v kontekst pred zagonom agentov. Ti pomnilniki so lahko shranjeni v zunanjih storitvah, kot je mem0:

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

**Opazovanje agenta**

Opazovanje je pomembno za gradnjo zanesljivih in vzdržljivih agentskih sistemov. MAF se povezuje z OpenTelemetry za zagotavljanje sledenja in meritev za boljše opazovanje.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # narediti nekaj
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Delovni tokovi

MAF ponuja delovne tokove, ki so vnaprej definirani koraki za dokončanje naloge in vključujejo AI agente kot komponente teh korakov.

Delovni tokovi so sestavljeni iz različnih komponent, ki omogočajo boljši nadzor pretoka. Prav tako omogočajo **orkestracijo več agentov** in **checkpointing** za shranjevanje stanj delovnih tokov.

Glavne komponente delovnega toka so:

**Izvrševalci**

Izvrševalci sprejemajo vhodna sporočila, izvajajo dodeljene naloge in proizvajajo izhodna sporočila. Tako omogočajo napredovanje delovnega toka proti zaključku večje naloge. Izvrševalci so lahko AI agenti ali prilagojena logika.

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

*Pogojne povezave* - aktivirajo se po izpolnitvi določenega pogoja. Na primer, ko sobe v hotelu niso na voljo, izvrševalec lahko predlaga druge možnosti.

*Switch-case povezave* - usmerjajo sporočila različnim izvrševalcem glede na definirane pogoje. Na primer, če ima potovalni kupec prioriteto in se njegove naloge obravnavajo prek drugega delovnega toka.

*Fan-out povezave* - pošljejo eno sporočilo več ciljem.

*Fan-in povezave* - zberejo več sporočil iz različnih izvrševalcev in jih pošljejo enemu cilju.

**Dogodki**

Za boljšo opazljivost delovnih tokov MAF ponuja vgrajene dogodke za izvajanje, vključno z:

- `WorkflowStartedEvent`  - Začetek izvajanja delovnega toka
- `WorkflowOutputEvent` - Delovni tok proizvede izhod
- `WorkflowErrorEvent` - Delovni tok se sreča z napako
- `ExecutorInvokeEvent`  - Izvrševalec začne z obdelavo
- `ExecutorCompleteEvent`  -  Izvrševalec zaključi obdelavo
- `RequestInfoEvent` - Izvedena je bila zahteva

## Napredni MAF vzorci

Prejšnji razdelki zajemajo ključne koncepte Microsoft Agent Framework. Ko gradite bolj kompleksne agente, upoštevajte naslednje napredne vzorce:

- **Sestava middleware**: Zvezno povezovanje več middleware procesorjev (beleženje, avtentikacija, omejevanje hitrosti) z uporabo funkcijskega in chat middleware za natančen nadzor vedenja agenta.
- **Checkpointing delovnih tokov**: Uporaba dogodkov delovnih tokov in serializacije za shranjevanje in nadaljevanje dolgih procesov agentov.
- **Dinamična izbira orodij**: Združevanje RAG preko opisov orodij z registracijo orodij v MAF, da se prikažejo le relevantna orodja za vsak poizvedbo.
- **Predaja med več agenti**: Uporaba povezav delovnih tokov in pogojnih usmeritev za orkestracijo predaj med specializiranimi agenti.

## Primeri kode

Primeri kode za Microsoft Agent Framework lahko najdete v tem repozitoriju pod datotekami `xx-python-agent-framework` in `xx-dotnet-agent-framework`.

## Imate več vprašanj o Microsoft Agent Framework?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) za srečanje z drugimi učenci, udeležbo v urah pomoči in odgovore na vaša vprašanja o AI agentih.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvornih jeziku velja za zavezujoč vir. Za ključne informacije priporočamo strokovni prevod s strani usposobljenega prevajalca. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->