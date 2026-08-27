# Preskúmanie Microsoft Agent Framework

![Agent Framework](../../../translated_images/sk/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Úvod

Táto lekcia pokryje:

- Pochopenie Microsoft Agent Framework: Kľúčové vlastnosti a hodnota  
- Preskúmanie kľúčových konceptov Microsoft Agent Framework
- Pokročilé MAF vzory: pracovné postupy, middleware a pamäť

## Ciele učenia

Po dokončení tejto lekcie budete vedieť, ako:

- Vytvoriť produkčne pripravených AI agentov pomocou Microsoft Agent Framework
- Aplikovať základné vlastnosti Microsoft Agent Framework na vaše agentné prípadové použitia
- Použiť pokročilé vzory vrátane pracovných postupov, middleware a dohľadateľnosti

## Ukážky kódu 

Ukážky kódu pre [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) nájdete v tomto repozitári v súboroch `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Pochopenie Microsoft Agent Framework

![Framework Intro](../../../translated_images/sk/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) je jednotný rámec spoločnosti Microsoft pre tvorbu AI agentov. Ponúka flexibilitu na riešenie širokej škály agentných prípadov použitia, ktoré sa vyskytujú v produkčnom aj výskumnom prostredí vrátane:

- **Sekvenčnej orchestrácie agentov** v scenároch, kde sú potrebné krok za krokom pracovné postupy.
- **Súbežnej orchestrácie** v scenároch, kde agenti musia vykonať úlohy súčasne.
- **Orchestrácie skupinového chatu** v scenároch, kde agenti môžu spolupracovať na jednej úlohe.
- **Orchestrácie odovzdávania úloh** v scenároch, kde agenti odovzdávajú úlohu jeden druhému počas dokončovania podúloh.
- **Magnetickej orchestrácie** v scenároch, kde manažér agent vytvára a upravuje zoznam úloh a riadi koordináciu podagentov na dokončenie úlohy.

Pre dodanie AI agentov v produkcii MAF tiež obsahuje funkcie pre:

- **Dohľadateľnosť** prostredníctvom použitia OpenTelemetry, kde sa sleduje každá akcia AI agenta vrátane vyvolávania nástrojov, krokov orchestrácie, tokov uvažovania a monitorovania výkonu cez Microsoft Foundry dashboardy.
- **Bezpečnosť** hostovaním agentov natívne v Microsoft Foundry, ktoré zahŕňa bezpečnostné kontroly ako riadenie prístupu na základe rolí, spracovanie súkromných údajov a integrovanú bezpečnosť obsahu.
- **Odolnosť** pretože vlákna agentov a pracovné postupy môžu byť pozastavené, obnovené a zotavené z chýb, čo umožňuje dlhodobo bežiace procesy.
- **Kontrolu** ako sú podporované pracovné postupy s ľudským zásahom, kde sú úlohy označené ako vyžadujúce schválenie človekom.

Microsoft Agent Framework sa tiež zameriava na interoperabilitu tým, že:

- **Je cloudovo nezávislý** - Agenti môžu bežať v kontajneroch, v on-premise prostrediach a cez viaceré rôzne cloudy.
- **Je poskytovateľsky nezávislý** - Agenti môžu byť vytváraní cez preferované SDK vrátane Azure OpenAI a OpenAI.
- **Integruje otvorené štandardy** - Agenti môžu využívať protokoly ako Agent-to-Agent (A2A) a Model Context Protocol (MCP) na objavovanie a používanie iných agentov a nástrojov.
- **Pluginy a konektory** - Môžu sa vytvárať spojenia na dátové a pamäťové služby ako Microsoft Fabric, SharePoint, Pinecone a Qdrant.

Pozrime sa, ako sú tieto funkcie aplikované na niektoré zo základných konceptov Microsoft Agent Framework.

## Kľúčové koncepty Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/sk/agent-components.410a06daf87b4fef.webp)

**Tvorba agentov**

Agent sa vytvára definovaním inferenčnej služby (poskytovateľ LLM),  
súboru inštrukcií, ktoré má AI agent dodržiavať, a prideleným `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Vyššie uvedené používa `Azure OpenAI`, ale agenti môžu byť vytváraní pomocou rôznych služieb vrátane `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI API `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

alebo [MiniMax](https://platform.minimaxi.com/), ktoré poskytuje OpenAI-kompatibilné API s veľkými kontextovými oknami (až do 204K tokenov):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

alebo vzdialených agentov používajúcich protokol A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Spustenie agentov**

Agenti sa spúšťajú pomocou metód `.run` alebo `.run_stream` pre ne-streamované alebo streamované odpovede.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Každé spustenie agenta môže mať tiež možnosti na prispôsobenie parametrov ako `max_tokens` používaných agentom, `tools`, ktoré agent môže volať, a dokonca aj samotný `model` použitý pre agenta.

Toto je užitočné v prípadoch, keď sú na splnenie úlohy používateľa vyžadované špecifické modely alebo nástroje.

**Nástroje**

Nástroje môžu byť definované pri definovaní agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Pri priamom vytváraní ChatAgenta

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

a tiež pri spustení agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Nástroj poskytnutý iba pre tento beh )
```

**Vlákna agentov**

Vlákna agentov sa používajú na spracovanie viackolových rozhovorov. Vlákna môžu byť vytvorené buď:

- Použitím `get_new_thread()`, ktorý umožňuje uloženie vlákna v priebehu času
- Automatickým vytvorením vlákna pri spustení agenta, ktoré trvá len počas aktuálneho behu.

Na vytvorenie vlákna vyzerá kód takto:

```python
# Vytvorte nový vlákno.
thread = agent.get_new_thread() # Spustite agenta s vláknom.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Následne môžete vlákno serializovať a uložiť na neskoršie použitie:

```python
# Vytvorte nový vlákno.
thread = agent.get_new_thread() 

# Spustite agenta s vláknom.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializujte vlákno na ukladanie.

serialized_thread = await thread.serialize() 

# Deserializujte stav vlákna po načítaní z úložiska.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agenti interagujú s nástrojmi a LLM, aby dokončili úlohy používateľov. V určitých scenároch chceme vykonať alebo sledovať medzikroky týchto interakcií. Middleware agenta nám to umožňuje cez:

*Funkčný Middleware*

Tento middleware nám umožňuje vykonať akciu medzi agentom a funkciou/nástrojom, ktorý bude volať. Príkladom použitia môže byť logovanie volania funkcie.

V nasledujúcom kóde `next` určuje, či sa má volať ďalší middleware alebo samotná funkcia.

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

    # Postspracovanie: Zaznamenanie po vykonaní funkcie
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Tento middleware umožňuje vykonať alebo zaznamenať akciu medzi agentom a požiadavkami medzi LLM.

Obsahuje dôležité informácie ako `messages`, ktoré sú odosielané AI službe.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Predspracovanie: Zaznamenať pred volaním AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Pokračovať na ďalší middleware alebo AI službu
    await next(context)

    # Následné spracovanie: Zaznamenať po odpovedi AI
    print("[Chat] AI response received")

```

**Pamäť agenta**

Ako bolo pokryté v lekcii `Agentic Memory`, pamäť je dôležitý prvok umožňujúci agentovi pracovať v rôznych kontextoch. MAF ponúka niekoľko typov pamätí:

*Pamäť v pamäti (In-Memory Storage)*

Toto je pamäť uložená vo vláknach počas behu aplikácie.

```python
# Vytvorte novú vlákno.
thread = agent.get_new_thread() # Spustite agenta s vláknom.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Perzistentné správy*

Táto pamäť sa používa na ukladanie histórie konverzácií medzi rôznymi reláciami. Definuje sa pomocou `chat_message_store_factory`:

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

Táto pamäť sa pridáva do kontextu pred spustením agentov. Môže byť uložená v externých službách ako mem0:

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

**Dohľadateľnosť agenta**

Dohľadateľnosť je dôležitá pre budovanie spoľahlivých a udržiavateľných agentných systémov. MAF integruje OpenTelemetry na poskytovanie sledovania a metrov pre lepšiu dohľadateľnosť.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # niečo urobiť
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Pracovné postupy

MAF ponúka pracovné postupy, ktoré sú preddefinované kroky na dokončenie úlohy a zahŕňajú AI agentov ako súčasti týchto krokov.

Pracovné postupy sa skladajú z rôznych komponentov, ktoré umožňujú lepšiu kontrolu toku. Pracovné postupy tiež umožňujú **multi-agentnú orchestráciu** a **checkpointing** na uloženie stavov pracovného postupu.

Hlavné komponenty pracovného postupu sú:

**Executor-y**

Executor-y prijímajú vstupné správy, vykonávajú pridelené úlohy a potom vytvárajú výstupnú správu. To posúva pracovný postup dopredu k dokončeniu väčšej úlohy. Executor-y môžu byť buď AI agent alebo vlastná logika.

**Hrany (Edges)**

Hrany sa používajú na definovanie toku správ v pracovnom postupe. Môžu byť:

*Priame hrany* - Jednoduché spojenia jeden-na-jeden medzi executormi:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Podmienené hrany* - Aktivované po splnení určitej podmienky. Napríklad, keď nie sú dostupné hotelové izby, executor môže navrhnúť iné možnosti.

*Prepínacie hrany* - Nasmerujú správy k rôznym executorom na základe definovaných podmienok. Napríklad, ak má cestujúci prioritný prístup, jeho úlohy budú spracované cez iný pracovný postup.

*Fan-out hrany* - Posielajú jednu správu viacerým cieľom.

*Fan-in hrany* - Zbierajú viaceré správy od rôznych executorov a posielajú ich jednému cieľu.

**Udalosti**

Na lepšiu dohľadateľnosť pracovných postupov MAF ponúka zabudované udalosti pre vykonávanie vrátane:

- `WorkflowStartedEvent`  - Začiatok vykonávania pracovného postupu
- `WorkflowOutputEvent` - Pracovný postup vytvára výstup
- `WorkflowErrorEvent` - Pracovný postup narazí na chybu
- `ExecutorInvokeEvent`  - Executor začína spracovávať
- `ExecutorCompleteEvent`  -  Executor dokončuje spracovávanie
- `RequestInfoEvent` - Vydaná požiadavka

## Pokročilé MAF vzory

Sekcie vyššie pokrývajú kľúčové koncepty Microsoft Agent Framework. Ako vytvárate zložitejších agentov, tu sú niektoré pokročilé vzory, ktoré treba zvážiť:

- **Kombinácia middleware**: Reťazenie viacerých middleware handlerov (logovanie, autentifikácia, obmedzovanie rýchlosti) pomocou funkčného a chat middleware pre jemnú kontrolu správania agenta.
- **Checkpointing pracovných postupov**: Použitie pracovných udalostí a serializácie na uloženie a obnovenie dlhodobých procesov agenta.
- **Dynamický výber nástrojov**: Kombinovať RAG cez popisy nástrojov s registráciou nástrojov MAF na prezentáciu len relevantných nástrojov pre každý dotaz.
- **Multi-agentné odovzdávanie**: Použiť hrany pracovných postupov a podmienené smerovanie na orchestráciu odovzdávania medzi špecializovanými agentmi.

## Hostovanie LangChain / LangGraph agentov na Microsoft Foundry

Microsoft Agent Framework je **frameworkovo interoperabilný** — nie ste limitovaný len na agentov napísaných s MAF. Ak už máte agenta vytvoreného pomocou **LangChain** alebo **LangGraph**, môžete ho spustiť ako **hostovaného agenta v Microsoft Foundry**, takže Foundry spravuje runtime, relácie, škálovanie, identitu a koncové body protokolu za vás, zatiaľ čo vaša agentná logika zostáva v LangGraph.

Toto je možné pomocou balíka `langchain_azure_ai.agents.hosting`, ktorý vystavuje skompilovaný LangGraph graf cez rovnaké protokoly, ktoré používajú hostovaní agenti Foundry.

**1. Nainštalujte hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Extra `hosting` inštaluje Foundry protokolové knižnice: `azure-ai-agentserver-responses` (OpenAI kompatibilný koncový bod `/responses`) a `azure-ai-agentserver-invocations` (všeobecný koncový bod `/invocations`).

**2. Vyberte hosting protokol:**

| Protokol | Host trieda | Koncový bod | Použitie ak |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Chcete OpenAI-kompatibilný chat, streamovanie, históriu odpovedí a vlákna konverzácií — odporúčaný predvolený pre konverzačných agentov. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Potrebujete vlastný JSON formát, webhook štýl koncový bod alebo ne-konverzačné spracovanie. |

Pretože **Responses API je hlavné API pre vývoj agentov vo Foundry**, začnite s `ResponsesHostServer` pre väčšinu agentov.

**3. Konfigurujte environmentálne premenné** (`az login` najprv, aby sa `DefaultAzureCredential` vedel autentifikovať):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Keď agent neskôr beží ako hostovaný agent vo Foundry, platforma automaticky injektuje `FOUNDRY_PROJECT_ENDPOINT`.

**4. Vystavte LangGraph agenta cez Responses protokol:**

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

    # ChatOpenAI tu cieli na endpoint kompatibilný s OpenAI (Responses) projektu Foundry.
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

Spustite lokálne s `python main.py`, potom pošlite Requests na `http://localhost:8088/responses`.

**Kľúčové správanie:**

- **Konverzácie**: Klienti pokračujú v konverzácii tým, že odovzdávajú `previous_response_id` alebo ID konverzácie `conversation`. Ak je váš graf skompilovaný s LangGraph checkpointerom, Foundry priraďuje stav konverzácie k checkpointu (v produkcii používajte odolný checkpoint; `MemorySaver` je v poriadku na lokálne testovanie).
- **Človek v slučke**: Ak váš graf používa LangGraph `interrupt()`, `ResponsesHostServer` zobrazuje čakajúce prerušenie ako Requests `function_call` / `mcp_approval_request` položku, a klienti pokračujú s zodpovedajúcim `function_call_output` / `mcp_approval_response`.
- **Nasadenie do Foundry**: Použite Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokálne, potrebuje Docker), potom `azd provision` a `azd deploy`. Nasadenie hostovaného agenta vyžaduje rolu **Foundry Project Manager**.

Spustiteľná verzia tohto príkladu je v [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pre kompletný návod (protokol Invocations, vlastné schémy požiadaviek a riešenie problémov) pozrite si [Hostujte LangGraph agentov ako hostovaných agentov Foundry](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Ukážky kódu 

Ukážky kódu pre Microsoft Agent Framework nájdete v tomto repozitári v súboroch `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Máte ďalšie otázky o Microsoft Agent Framework?

Pridajte sa do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), stretnite sa s ostatnými študentmi, navštevujte konzultačné hodiny a získajte odpovede na svoje otázky o AI agentoch.
## Predchádzajúca lekcia

[Pamäť pre AI agentov](../13-agent-memory/README.md)

## Ďalšia lekcia

[Stavanie agentov na používanie počítača (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->