# Preskúmanie Microsoft Agent Framework

![Agent Framework](../../../translated_images/sk/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Úvod

Táto lekcia pokryje:

- Pochopenie Microsoft Agent Framework: Kľúčové vlastnosti a hodnota  
- Preskúmanie kľúčových konceptov Microsoft Agent Framework
- Pokročilé vzory MAF: pracovné toky, middleware a pamäť

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

- Vytvárať produkčne pripravené AI agentov pomocou Microsoft Agent Framework
- Aplikovať hlavné vlastnosti Microsoft Agent Framework na vaše agentné použitia
- Používať pokročilé vzory vrátane pracovných tokov, middleware a monitorovania

## Ukážky kódu

Ukážky kódu pre [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) nájdete v tomto repozitári v súboroch `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Pochopenie Microsoft Agent Framework

![Framework Intro](../../../translated_images/sk/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) je jednotný framework Microsoftu na tvorbu AI agentov. Ponúka flexibilitu na riešenie širokej škály agentných prípadov použitia, ktoré sa vyskytujú v produkčných aj výskumných prostrediach vrátane:

- **Sekvenčná orchestrácia agentov** v scenároch, kde sú potrebné krok za krokom pracovné toky.
- **Súbežná orchestrácia** v situáciách, kde agenti musia dokončiť úlohy súčasne.
- **Orchestrácia skupinového chatu** v prípadoch, keď agenti môžu spolupracovať na jednej úlohe.
- **Handoff orchestrácia** v scenároch, kde si agenti odovzdávajú úlohu, keď sú čiastkové úlohy dokončené.
- **Magnetická orchestrácia** v prípadoch, keď manažér agent vytvára a modifikuje zoznam úloh a koordinuje subagentov na dokončenie úlohy.

Na doručenie AI agentov do produkcie MAF tiež obsahuje funkcie pre:

- **Monitorovanie** pomocou OpenTelemetry, kde každá akcia AI agenta vrátane volania nástrojov, orchestrácie krokov, tokov uvažovania a monitorovania výkonnosti cez Microsoft Foundry dashboardy je sledovaná.
- **Bezpečnosť** hostovaním agentov natívne na Microsoft Foundry, ktorý obsahuje bezpečnostné kontroly ako prístup založený na rolách, spracovanie súkromných dát a vstavanú bezpečnosť obsahu.
- **Trvácnosť** umožňuje pozastavenie, obnovenie a zotavenie sa z chýb pracovných vlákien a tokov, čo umožňuje dlhšie bežiace procesy.
- **Kontrolu** podporou pracovných tokov so zapojením človeka, kde sú úlohy označené ako vyžadujúce schválenie človekom.

Microsoft Agent Framework sa tiež zameriava na interoperabilitu:

- **Je cloudovo nezávislý** - agenti môžu bežať v kontajneroch, na on-premise a across viacerých cloudoch.
- **Je poskytovateľsky nezávislý** - agenti môžu byť vytvorení cez preferovaný SDK vrátane Azure OpenAI a OpenAI
- **Integruje otvorené štandardy** - agenti môžu využívať protokoly ako Agent-to-Agent (A2A) a Model Context Protocol (MCP) na objavovanie a používanie iných agentov a nástrojov.
- **Pluginy a konektory** - umožňujú pripojenia k dátovým a pamäťovým službám ako Microsoft Fabric, SharePoint, Pinecone a Qdrant.

Pozrime sa, ako sa tieto funkcie aplikujú na niektoré základné koncepty Microsoft Agent Framework.

## Kľúčové koncepty Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/sk/agent-components.410a06daf87b4fef.webp)

**Vytváranie agentov**

Vytváranie agenta sa vykonáva definovaním inference služby (LLM poskytovateľ),  
sady inštrukcií, ktoré má AI agent nasledovať, a prideleným `menom`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Vyššie je použitý `Azure OpenAI`, ale agenti môžu byť vytvorení pomocou rôznych služieb vrátane `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

alebo vzdialených agentov používajúcich protokol A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Spúšťanie agentov**

Agenti sa spúšťajú pomocou metód `.run` alebo `.run_stream` pre ne-streamingové alebo streamingové odpovede.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Každé spustenie agenta môže mať tiež možnosti na prispôsobenie parametrov ako `max_tokens` používané agentom, `tools`, ktoré agent môže volať, a dokonca aj samotný `model`, ktorý agent používa.

To je užitočné v prípadoch, kde sú na vykonanie úlohy používateľa potrebné špecifické modely alebo nástroje.

**Nástroje**

Nástroje sa môžu definovať pri definovaní agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Pri priamom vytváraní ChatAgenta

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

a tiež pri spúšťaní agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Nástroj poskytnutý iba pre tento beh )
```

**Vlákna agentov**

Vlákna agentov sa používajú na spracovanie multi-tur konverzácií. Vlákna môžu byť vytvorené buď:

- Použitím `get_new_thread()`, čo umožňuje vláknu byť uložené v čase
- Automatickým vytvorením vlákna pri spustení agenta, ktoré trvá len počas aktuálneho spustenia.

Na vytvorenie vlákna vyzerá kód takto:

```python
# Vytvorte nový vlákno.
thread = agent.get_new_thread() # Spustite agenta s vláknom.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Vlákno potom môžete serializovať, aby bolo uložené na neskoršie použitie:

```python
# Vytvorte nový vlákno.
thread = agent.get_new_thread() 

# Spustite agenta s vláknom.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serilizujte vlákno na uloženie.

serialized_thread = await thread.serialize() 

# Deserilizujte stav vlákna po načítaní z úložiska.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware agentov**

Agenti interagujú s nástrojmi a LLM na dokončenie úloh používateľa. V určitých scenároch chceme vykonať akciu alebo sledovať tieto interakcie. Middleware agentov nám to umožňuje cez:

*Funkčný middleware*

Tento middleware umožňuje vykonať akciu medzi agentom a funkciou/nástrojom, ktorý volá. Príkladom použitia je, keď chcete robiť logovanie volania funkcie.

V nižšie uvedenom kóde `next` určuje, či má byť volaný ďalší middleware alebo samotná funkcia.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Predspracovanie: Zaznamenanie pred vykonaním funkcie
    print(f"[Function] Calling {context.function.name}")

    # Pokračovať na ďalší middleware alebo vykonanie funkcie
    await next(context)

    # Pospresovanie: Zaznamenanie po vykonaní funkcie
    print(f"[Function] {context.function.name} completed")
```

*Chat middleware*

Tento middleware umožňuje vykonať alebo logovať akciu medzi agentom a požiadavkami medzi LLM.

Obsahuje dôležité informácie ako `messages`, ktoré sú odosielané AI službe.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Predspracovanie: Záznam pred volaním AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Pokračovať na ďalší middleware alebo AI službu
    await next(context)

    # Následné spracovanie: Záznam po odpovedi AI
    print("[Chat] AI response received")

```

**Pamäť agenta**

Ako bolo pokryté v lekcii `Agentic Memory`, pamäť je dôležitý prvok umožňujúci agentovi pracovať v rôznych kontextoch. MAF ponúka niekoľko rôznych typov pamäti:

*In-memory ukladanie*

Toto je pamäť uložená vo vláknach počas behu aplikácie.

```python
# Vytvorte nový vlákno.
thread = agent.get_new_thread() # Spustite agenta s vláknom.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Trvalé správy*

Táto pamäť sa používa pri ukladaní histórie konverzácie naprieč rôznymi reláciami. Definuje sa použitím `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Vytvorte vlastné úložisko správ
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamická pamäť*

Táto pamäť sa pridáva do kontextu pred spustením agentov. Tieto pamäte môžu byť uložené v externých službách ako mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Použitie Mem0 pre pokročilé pamäťové schopnosti
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

**Monitorovanie agentov**

Monitorovanie je dôležité pre budovanie spoľahlivých a udržiavateľných agentných systémov. MAF sa integruje s OpenTelemetry na poskytovanie trasovania a meradiel pre lepšiu sledovateľnosť.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # urob niečo
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Pracovné toky

MAF ponúka pracovné toky, ktoré sú preddefinované kroky na dokončenie úlohy a zahŕňajú AI agentov ako komponenty týchto krokov.

Pracovné toky sa skladajú z rôznych komponentov, ktoré umožňujú lepší riadiaci tok. Tiež umožňujú **multi-agentnú orchestráciu** a **checkpointing** na uloženie stavov pracovného toku.

Hlavné komponenty pracovného toku sú:

**Exekútory**

Exekútory prijímajú vstupné správy, vykonávajú priradené úlohy a produkujú výstupnú správu. To posúva pracovný tok vpred smerom k dokončeniu väčšej úlohy. Exekútory môžu byť buď AI agent alebo vlastná logika.

**Hrany**

Hrany sa používajú na definovanie toku správ v pracovnom toku. Môžu byť:

*Priame hrany* - Jednoduché spojenia jeden na jedného medzi exekútormi:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Podmienené hrany* - Aktivujú sa po splnení určitej podmienky. Napríklad keď nie sú dostupné hotelové izby, exekútor môže navrhnúť iné možnosti.

*Prepínacie hrany* - Smerujú správy k rôznym exekútorom na základe definovaných podmienok. Napríklad ak cestujúci zákazník má prioritný prístup, jeho úlohy budú spracované cez iný pracovný tok.

*Fan-out hrany* - Odošlú jednu správu viacerým cieľom.

*Fan-in hrany* - Zbierajú viacero správ od rôznych exekútorov a odosielajú ich jednému cieľu.

**Udalosti**

Na lepšiu sledovateľnosť pracovných tokov ponúka MAF vstavané udalosti pri vykonávaní vrátane:

- `WorkflowStartedEvent`  - Začiatok vykonávania pracovného toku
- `WorkflowOutputEvent` - Pracovný tok produkuje výstup
- `WorkflowErrorEvent` - Pracovný tok narazí na chybu
- `ExecutorInvokeEvent`  - Exekútor začína spracovanie
- `ExecutorCompleteEvent`  -  Exekútor dokončuje spracovanie
- `RequestInfoEvent` - Vydaná požiadavka

## Pokročilé vzory MAF

Vyššie uvedené sekcie pokrývajú základné koncepty Microsoft Agent Framework. Ako budete vytvárať zložitejších agentov, tu sú niektoré pokročilé vzory na zváženie:

- **Kompozícia middleware**: Reťazenie viacerých middleware handlerov (logovanie, autentifikácia, obmedzovanie rýchlosti) pomocou funkčného a chat middleware pre jemné riadenie správania agenta.
- **Checkpointing pracovných tokov**: Použitie udalostí pracovných tokov a serializácie na uloženie a obnovenie dlhšie bežiacich agentných procesov.
- **Dynamický výber nástrojov**: Kombinácia RAG na popisy nástrojov s registráciou nástrojov MAF na prezentovanie len relevantných nástrojov k dopytu.
- **Multi-agentný handoff**: Použitie hrán pracovného toku a podmieneného smerovania na orchestráciu odovzdávania medzi špecializovanými agentmi.

## Ukážky kódu

Ukážky kódu pre Microsoft Agent Framework nájdete v tomto repozitári v súboroch `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Máte ďalšie otázky o Microsoft Agent Framework?

Pridajte sa na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kde sa stretnete s ostatnými študentmi, môžete sa zúčastniť konzultácií a získať odpovede na vaše otázky ohľadom AI agentov.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->