# Preskúmavanie Microsoft Agent Framework

![Agent Framework](../../../translated_images/sk/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Úvod

Táto lekcia pokryje:

- Pochopenie Microsoft Agent Framework: kľúčové funkcie a hodnota  
- Preskúmanie kľúčových konceptov Microsoft Agent Framework
- Pokročilé vzory MAF: workflowy, middleware a pamäť

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

- Vytvoriť produkčne pripravených AI agentov pomocou Microsoft Agent Framework
- Aplikovať základné funkcie Microsoft Agent Framework pre vaše agentné prípadové použitia
- Používať pokročilé vzory vrátane workflowov, middleware a observability

## Ukážky kódu 

Ukážky kódu pre [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) sa nachádzajú v tomto repozitári v súboroch `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Pochopenie Microsoft Agent Framework

![Framework Intro](../../../translated_images/sk/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) je jednotný rámec Microsoftu na vytváranie AI agentov. Ponúka flexibilitu riešiť širokú škálu agentných prípadových použití v produkcii aj výskume vrátane:

- **Sekvenčná orchestrácia agentov** v scenároch, kde sú potrebné krok za krokom workflowy.
- **Súbežná orchestrácia** v scenároch, kde agenti potrebujú vykonať úlohy súčasne.
- **Orchestrácia skupinovej komunikácie** v scenároch, kde agenti môžu spolupracovať na jednej úlohe.
- **Orchestrácia odovzdávania úloh** v scenároch, kde si agenti odovzdávajú úlohu, keď sú čiastočné úlohy dokončené.
- **Magnetická orchestrácia** v scenároch, kde manažérsky agent vytvára a modifikuje zoznam úloh a koordinuje podagentov na dokončenie úlohy.

Pre dodanie AI agentov v produkcii má MAF tiež zahrnuté funkcie pre:

- **Observability** pomocou OpenTelemetry, kde každá akcia AI agenta vrátane vyvolania nástrojov, orchestrácie krokov, priebehov uvažovania a monitorovania výkonu cez Microsoft Foundry dashboardy.
- **Bezpečnosť** hostením agentov natívne na Microsoft Foundry, čo zahŕňa bezpečnostné kontroly ako riadenie prístupu na základe rolí, spracovanie súkromných údajov a zabudovanú bezpečnosť obsahu.
- **Trvanlivosť** pretože vlákna agentov a workflowy môžu pauzovať, pokračovať a zotavovať sa z chýb, čo umožňuje dlhšie bežiace procesy.
- **Kontrola** podporou workflowov s človekom v slučke, kde sú úlohy označené ako vyžadujúce schválenie človekom.

Microsoft Agent Framework sa zameriava aj na interoperabilitu:

- **Byť nezávislý na cloude** - agenti môžu bežať v kontajneroch, on-premise aj na viacerých rôznych cloudoch.
- **Byť nezávislý na poskytovateľovi** - agenti môžu byť vytváraní pomocou vášho preferovaného SDK vrátane Azure OpenAI a OpenAI
- **Integrácia otvorených štandardov** - agenti môžu využívať protokoly ako Agent-to-Agent (A2A) a Model Context Protocol (MCP) na objavovanie a využívanie iných agentov a nástrojov.
- **Pluginy a konektory** - pripojenia môžu byť vytvorené k dátovým a pamäťovým službám ako Microsoft Fabric, SharePoint, Pinecone a Qdrant.

Pozrime sa, ako sa tieto funkcie uplatňujú na niektoré základné koncepty Microsoft Agent Framework.

## Kľúčové koncepty Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/sk/agent-components.410a06daf87b4fef.webp)

**Vytváranie agentov**

Vytváranie agenta sa vykonáva definovaním inferenčnej služby (poskytovateľa LLM),  
sady inštrukcií, ktoré má AI agent sledovať, a priradeného `mená`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Vyššie je použité `Azure OpenAI`, ale agenti môžu byť vytvorení pomocou rôznych služieb vrátane `Microsoft Foundry Agent Service`:

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

alebo [MiniMax](https://platform.minimaxi.com/), ktorý poskytuje OpenAI-kompatibilné API s veľkými kontextovými oknami (až do 204K tokenov):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

alebo vzdialených agentov používajúcich protokol A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Spúšťanie agentov**

Agenti sa spúšťajú pomocou metód `.run` alebo `.run_stream` pre buď ne-streamované alebo streamované odpovede.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Každé spustenie agenta môže mať aj možnosti prispôsobenia parametrov ako `max_tokens` používané agentom, nástroje `tools`, ktoré agent môže volať, a dokonca aj samotný `model` používaný agentom.

To je užitočné v prípadoch, kde sú kvôli vykonaniu úlohy používateľa potrebné konkrétne modely alebo nástroje.

**Nástroje**

Nástroje môžu byť definované ako pri definovaní agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Pri priamom vytváraní ChatAgenta

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

tak aj pri spúšťaní agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Nástroj poskytnutý iba pre tento beh )
```

**Vlákna agentov**

Vlákna agentov sa používajú na zvládanie multi-turn konverzácií. Vlákna môžu byť vytvorené buď:

- Použitím `get_new_thread()`, ktorý umožňuje uloženie vlákna v čase
- Automatickým vytvorením vlákna pri spustení agenta s platnosťou vlákna iba počas aktuálneho behu.

Na vytvorenie vlákna vyzerá kód takto:

```python
# Vytvorte nový vlákno.
thread = agent.get_new_thread() # Spustite agenta s vlákno.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Vlákno je potom možné serializovať na uloženie pre neskoršie použitie:

```python
# Vytvorte nový vláknový proces.
thread = agent.get_new_thread() 

# Spustite agenta so vlákno.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializujte vlákno pre uloženie.

serialized_thread = await thread.serialize() 

# Deserializujte stav vlákna po načítaní z uloženia.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware agenta**

Agenti interagujú s nástrojmi a LLM na dokončenie úloh používateľov. V určitých scenároch chceme vykonať alebo sledovať medzistupne týchto interakcií. Agent middleware nám to umožňuje cez:

*Funkčný middleware*

Tento middleware nám umožňuje vykonať akciu medzi agentom a volanou funkciou/nástrojom. Príkladom použitia je logovanie volania funkcie.

V kóde nižšie `next` definuje, či sa má volať ďalší middleware alebo samotná funkcia.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Predspracovanie: Záznam pred vykonaním funkcie
    print(f"[Function] Calling {context.function.name}")

    # Pokračovať na ďalší middleware alebo vykonanie funkcie
    await next(context)

    # Postspracovanie: Záznam po vykonaní funkcie
    print(f"[Function] {context.function.name} completed")
```

*Chat middleware*

Tento middleware umožňuje vykonať alebo logovať akciu medzi agentom a požiadavkami smerujúcimi k LLM.

Obsahuje dôležité informácie ako `messages` zasielané AI službe.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Predspracovanie: Zaznamenanie pred volaním AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Pokračovať k ďalšiemu middleware alebo AI službe
    await next(context)

    # Následné spracovanie: Zaznamenanie po odpovedi AI
    print("[Chat] AI response received")

```

**Pamäť agenta**

Ako bolo pokryté v lekcii `Agentic Memory`, pamäť je dôležitým prvkom umožňujúcim agentovi pracovať s rôznymi kontextami. MAF ponúka niekoľko typov pamätí:

*In-Memory Storage*

Ide o pamäť uloženú vo vláknach počas behu aplikácie.

```python
# Vytvorte nový vlákno.
thread = agent.get_new_thread() # Spustite agenta s vláknom.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Perzistentné správy*

Túto pamäť používame na ukladanie histórie konverzácií v rôznych reláciách. Definuje sa pomocou `chat_message_store_factory`:

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

**Observability agenta**

Observability je dôležitá pre budovanie spoľahlivých a udržiavateľných agentných systémov. MAF sa integruje s OpenTelemetry na poskytovanie trasovania a metrov pre lepšiu observabilitu.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # sprav niečo
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Workflowy

MAF ponúka workflowy, ktoré sú preddefinované kroky na dokončenie úlohy a zahrňujú AI agentov ako komponenty v týchto krokoch.

Workflowy sa skladajú z rôznych komponentov, ktoré umožňujú lepší control flow. Workflowy tiež umožňujú **multi-agent orchestration** a **checkpointing** na ukladanie stavov workflowu.

Hlavné komponenty workflowu sú:

**Executor-y**

Executor-y prijímajú vstupné správy, vykonávajú pridelené úlohy, a potom vytvoria výstupnú správu. Posúvajú workflow smerom k dokončeniu väčšej úlohy. Môžu byť AI agentmi alebo vlastnou logikou.

**Hrany (Edges)**

Hrany definujú tok správ vo workflow. Môžu byť:

*Priame hrany* - Jednoduché spojenia jeden na jedného medzi executormi:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Podmienené hrany* - Aktivované, keď je splnená určitá podmienka. Napríklad ak nie sú k dispozícii hotelové izby, executor môže navrhnúť iné možnosti.

*Prepínacie hrany (Switch-case)* - Smerujú správy k rôznym executorom podľa definovaných podmienok. Napríklad ak má cestujúci prioritu, jeho úlohy budú spracované cez iný workflow.

*Zaťažovacie hrany (Fan-out)* - Odošlú jednu správu na viacero cieľov.

*Zberačové hrany (Fan-in)* - Zbierajú viacero správ z rôznych executorov a posielajú ich na jeden cieľ.

**Udalosti**

Aby sa zlepšila observabilita workflowov, MAF ponúka zabudované udalosti vykonávania zahŕňajúce:

- `WorkflowStartedEvent` - Začiatok vykonávania workflowu
- `WorkflowOutputEvent` - Workflow vygeneruje výstup
- `WorkflowErrorEvent` - Workflow narazí na chybu
- `ExecutorInvokeEvent` - Executor začína spracovanie
- `ExecutorCompleteEvent` - Executor skončil spracovanie
- `RequestInfoEvent` - Vydaná požiadavka

## Pokročilé vzory MAF

Vyššie uvedené časti pokrývajú kľúčové koncepty Microsoft Agent Framework. Pri tvorbe zložitejších agentov zvážte tieto pokročilé vzory:

- **Kompozícia middleware**: Reťazenie viacerých middleware handlerov (logovanie, autentifikácia, rate-limiting) pomocou funkčného a chat middleware pre detailnú kontrolu správania agenta.
- **Checkpointing workflowu**: Použitie udalostí workflowu a serializácie na uloženie a obnovenie dlhodobých procesov agenta.
- **Dynamický výber nástrojov**: Kombinácia RAG nad popismi nástrojov s registráciou nástrojov MAF na prezentáciu len relevantných nástrojov pre dotaz.
- **Odovzdávanie medzi agentmi**: Použitie workflow hrán a podmieneného smerovania na orchestráciu odovzdávania medzi špecializovanými agentmi.

## Hostovanie LangChain / LangGraph agentov na Microsoft Foundry

Microsoft Agent Framework je **framework-interoperabilný** — nie ste obmedzení len na agentov napísaných s MAF. Ak už máte agenta vytvoreného s **LangChain** alebo **LangGraph**, môžete ho spustiť ako **Microsoft Foundry hostovaného agenta**, kde Foundry riadi runtime, relácie, škálovanie, identitu a protokolové endpointy, zatiaľ čo logika agenta zostáva v LangGraph.

Toto sa robí pomocou balíka `langchain_azure_ai.agents.hosting`, ktorý vystavuje skompilovaný LangGraph graf cez tie isté protokoly, aké používajú Foundry hostovaní agenti.

**1. Nainštalujte hostingový extra balík:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Extra `hosting` inštaluje Foundry protokolové knižnice: `azure-ai-agentserver-responses` (OpenAI-kompatibilný `/responses` endpoint) a `azure-ai-agentserver-invocations` (generický `/invocations` endpoint).

**2. Vyberte hostingový protokol:**

| Protokol | Host trieda | Endpoint | Použitie |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Chcete OpenAI-kompatibilný chat, streaming, históriu odpovedí a spracovanie konverzácií — odporúčaný štandard pre konverzačných agentov. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Potrebujete vlastný JSON formát, webhook-štýl endpoint, alebo ne-konverzačné spracovanie. |

Keďže **Responses API je primárne API pre agentný vývoj v Foundry**, začnite s `ResponsesHostServer` pre väčšinu agentov.

**3. Nakonfigurujte environmentálne premenné** (`az login` najprv, aby sa `DefaultAzureCredential` mohol autentifikovať):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Keď agent neskôr beží ako hostovaný agent v Foundry, platforma automaticky injektuje `FOUNDRY_PROJECT_ENDPOINT`.

**4. Exponujte LangGraph agenta cez Responses protokol:**

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

    # ChatOpenAI tu cieli na OpenAI-kompatibilný (Responses) koncový bod projektu Foundry.
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

Spustite lokálne s `python main.py`, potom odošlite požiadavku do Responses na `http://localhost:8088/responses`.

**Kľúčové správanie:**

- **Konverzácie**: Klienti pokračujú v konverzácii zaslaním `previous_response_id` alebo `conversation` ID. Ak je váš graf skompilovaný s LangGraph checkpointerom, Foundry viaže stav konverzácie na checkpoint (pre produkciu používajte vytrvalý checkpointer; `MemorySaver` je vhodný na lokálne testovanie).
- **Človek v slučke**: Ak váš graf používa LangGraph `interrupt()`, `ResponsesHostServer` zobrazuje čakajúci interrupt ako položku `function_call` / `mcp_approval_request` a klienti pokračujú s odpoveďou `function_call_output` / `mcp_approval_response`.
- **Deploy do Foundry**: Použite Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokálne, vyžaduje Docker), potom `azd provision` a `azd deploy`. Nasadenie hostovaného agenta vyžaduje rolu **Foundry Project Manager**.

Bežná verzia tohto príkladu je dostupná v [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pre úplný návod (Invocations protokol, vlastné request schémy a riešenie problémov) pozrite [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Ukážky kódu 

Ukážky kódu pre Microsoft Agent Framework sú v tomto repozitári v súboroch `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Máte viac otázok o Microsoft Agent Framework?

Pridajte sa do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde sa môžete stretnúť s ostatnými študentmi, zúčastniť sa office hours a získať odpovede na vaše otázky o AI agentoch.
## Predchádzajúca lekcia

[Pamäť pre AI agentov](../13-agent-memory/README.md)

## Nasledujúca lekcia

[Vytváranie agentov používajúcich počítač (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->