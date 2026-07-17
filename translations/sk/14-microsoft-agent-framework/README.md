# Preskúmanie rámca Microsoft Agent Framework

![Agent Framework](../../../translated_images/sk/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Úvod

Táto lekcia bude pokrývať:

- Pochopenie Microsoft Agent Framework: kľúčové vlastnosti a hodnota  
- Preskúmanie základných konceptov Microsoft Agent Framework
- Pokročilé vzory MAF: workflow, middleware a pamäť

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

- Vytvárať produkčne pripravených AI agentov pomocou Microsoft Agent Framework
- Aplikovať hlavné vlastnosti Microsoft Agent Framework na vaše agentné použitia
- Používať pokročilé vzory vrátane workflow, middleware a dohľadnosti

## Ukážky kódu 

Ukážky kódu pre [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) nájdete v tomto úložisku v súboroch `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Pochopenie Microsoft Agent Framework

![Framework Intro](../../../translated_images/sk/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) je jednotný rámec Microsoftu na tvorbu AI agentov. Ponúka flexibilitu na riešenie širokého spektra agentných prípadov použitia v produkcii aj vo výskume, vrátane:

- **Sekvenčné orchestrácie agentov** v scenároch, kde sú potrebné krok za krokom workflow.
- **Súbežné orchestrácie** v scenároch, kde agenti potrebujú vykonávať úlohy súčasne.
- **Orchestrácia skupinového chatu** v scenároch, kde agenti môžu spolupracovať na jednej úlohe.
- **Orchestrácia odovzdania** v scenároch, kde agenti odovzdávajú úlohu jeden druhému ako súčasti úloh sú dokončené.
- **Magnetická orchestrácia** v scenároch, kde manažér agent vytvára a upravuje zoznam úloh a koordinuje subagentov k dokončeniu úlohy.

Na doručenie AI agentov v produkcii MAF obsahuje aj funkcie pre:

- **Dohľadnosť** pomocou OpenTelemetry, kde každá akcia AI agenta vrátane volania nástrojov, orchestrácie krokov, toku uvažovania a sledovania výkonu cez Microsoft Foundry dashboardy.
- **Bezpečnosť** hostovaním agentov natívne na Microsoft Foundry, ktorý obsahuje bezpečnostné kontroly ako prístup na základe rolí, spracovanie súkromných údajov a zabudovanú bezpečnosť obsahu.
- **Odolnosť** pretože agentné vlákna a workflow môžu byť pozastavené, obnovené a zotavené z chýb, čo umožňuje dlhšie bežiace procesy.
- **Kontrola** pretože sú podporované human-in-the-loop workflow, kde sú úlohy označené ako vyžadujúce ľudské schválenie.

Microsoft Agent Framework sa tiež zameriava na interoperabilitu tým, že:

- **Je nezávislý od cloudu** - agenti môžu bežať v kontajneroch, on-prem a cez viaceré rôzne cloudy.
- **Je nezávislý od poskytovateľa** - agenti môžu byť vytvorení cez váš preferovaný SDK vrátane Azure OpenAI a OpenAI.
- **Integruje otvorené štandardy** - agenti môžu využívať protokoly ako Agent-to-Agent (A2A) a Model Context Protocol (MCP) na objavovanie a používanie iných agentov a nástrojov.
- **Pluginy a konektory** - možné sú pripojenia k dátovým a pamäťovým službám ako Microsoft Fabric, SharePoint, Pinecone a Qdrant.

Pozrime sa, ako sú tieto vlastnosti aplikované na niektoré základné koncepty Microsoft Agent Framework.

## Kľúčové koncepty Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/sk/agent-components.410a06daf87b4fef.webp)

**Vytváranie agentov**

Vytvorenie agenta sa uskutočňuje definovaním inference služby (poskytovateľ LLM),  
súboru inštrukcií pre AI agenta na dodržiavanie a priradeného `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Vyššie používa `Azure OpenAI`, ale agenti môžu byť vytvorení z rôznych služieb vrátane `Microsoft Foundry Agent Service`:

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

alebo vzdialení agenti používajúci protokol A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Spúšťanie agentov**

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

Každé spustenie agenta môže mať aj možnosti na prispôsobenie parametrov ako `max_tokens` používaných agentom, `tools`, ktoré agent môže volať, a dokonca `model` samotný použitý pre agenta.

Toto je užitočné v prípadoch, keď sú potrebné špecifické modely alebo nástroje na splnenie úlohy používateľa.

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

**Vlákna agenta**

Vlákna agenta sa používajú na spracovanie viacstupňových konverzácií. Vlákna môžu byť vytvorené buď:

- Použitím `get_new_thread()`, ktoré umožňuje uloženie vlákna v čase
- Automatickým vytvorením vlákna pri spustení agenta, pričom vlákno trvá len počas aktuálneho behu.

Na vytvorenie vlákna vyzerá kód takto:

```python
# Vytvorte nový proces.
thread = agent.get_new_thread() # Spustite agenta s procesom.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Vlákno môžete potom serializovať na uloženie pre neskoršie použitie:

```python
# Vytvorte nový vlákno.
thread = agent.get_new_thread() 

# Spustite agenta s vlákno.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializujte vlákno na uloženie.

serialized_thread = await thread.serialize() 

# Deserializujte stav vlákna po načítaní z úložiska.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware agenta**

Agenti interagujú s nástrojmi a LLMmi na dokončenie úloh používateľa. V určitých scenároch chceme vykonať alebo sledovať túto interakciu. Middleware agenta nám to umožňuje prostredníctvom:

*Funkčného middleware*

Tento middleware nám umožňuje vykonať akciu medzi agentom a funkciou/nástrojom, ktorý bude volať. Príkladom použitia je zaznamenávanie (logging) volania funkcie.

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

    # Posprahovanie: Záznam po vykonaní funkcie
    print(f"[Function] {context.function.name} completed")
```

*Chat middleware*

Tento middleware nám umožňuje vykonať alebo zaznamenať akciu medzi agentom a požiadavkami medzi LLM.

Obsahuje dôležité informácie ako `messages`, ktoré sa posielajú AI službe.

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

    # Postspracovanie: Záznam po odpovedi AI
    print("[Chat] AI response received")

```

**Pamäť agenta**

Ako bolo pokryté v lekcii `Agentic Memory`, pamäť je dôležitým prvkom umožňujúcim agentovi pracovať v rôznych kontextoch. MAF ponúka niekoľko typov pamätí:

*Pamäť v skripte*

Toto je pamäť uložená vo vláknach počas behu aplikácie.

```python
# Vytvorte nový vlákno.
thread = agent.get_new_thread() # Spustite agenta vo vlákne.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Trvalé správy*

Táto pamäť sa používa na uloženie histórie konverzácie naprieč rôznymi reláciami. Definuje sa pomocou `chat_message_store_factory`:

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

**Dohľadnosť agenta**

Dohľadnosť je dôležitá pre budovanie spoľahlivých a udržiavateľných agentných systémov. MAF sa integruje s OpenTelemetry pre poskytovanie trasovania a merania pre lepšiu dohľadnosť.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # urobiť niečo
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Workflowy

MAF ponúka workflowy, ktoré sú preddefinované kroky na dokončenie úlohy a zahŕňajú AI agentov ako komponenty týchto krokov.

Workflowy sú zložené z rôznych komponentov, ktoré umožňujú lepšiu kontrolu toku. Tiež umožňujú **multi-agent orchestration** a **checkpointing** na uloženie stavov workflow.

Základné komponenty workflow sú:

**Exekútori**

Exekútori prijímajú vstupné správy, vykonávajú vyhradené úlohy a potom produkujú výstupnú správu. Toto posúva workflow smerom k dokončeniu väčšej úlohy. Exekútori môžu byť buď AI agent alebo vlastná logika.

**Hrany**

Hrany sa používajú na definovanie toku správ vo workflow. Môžu byť:

*Priame hrany* - Jednoduché jedno-na-jedno spojenia medzi exekútormi:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Podmienené hrany* - Aktivujú sa po splnení určitej podmienky. Napríklad, keď nie sú k dispozícii hotelové izby, exekútor môže navrhnúť iné možnosti.

*Prepínačové hrany* - Nasmerujú správy k rôznym exekútorom na základe definovaných podmienok. Napríklad, ak má cestujúci prioritu, jeho úlohy budú spracované iným workflow.

*Rozvetvovacie hrany* - Pošlú jednu správu viacerým cieľom.

*Zlúčovacie hrany* - Zhromaždia viac správ z rôznych exekútorov a pošlú ich jednému cieľu.

**Udalosti**

Na lepšiu dohľadnosť workflow ponúka MAF zabudované udalosti pre spúšťanie vrátane:

- `WorkflowStartedEvent`  - Spustenie workflow
- `WorkflowOutputEvent` - Workflow produkuje výstup
- `WorkflowErrorEvent` - Workflow narazí na chybu
- `ExecutorInvokeEvent`  - Exekútor začína spracovávať
- `ExecutorCompleteEvent`  - Exekútor dokončí spracovanie
- `RequestInfoEvent` - Vydaná žiadosť

## Pokročilé vzory MAF

Predchádzajúce sekcie pokrývajú kľúčové koncepty Microsoft Agent Framework. Pri budovaní zložitejších agentov zvážte tieto pokročilé vzory:

- **Zloženie middleware**: Reťazenie viacerých middleware handlerov (logovanie, autentifikácia, obmedzovanie rýchlosti) pomocou funkčného a chat middleware pre jemnšiu kontrolu správania agenta.
- **Checkpointing workflow**: Použitie udalostí workflow a serializácie na uloženie a obnovenie dlhodobo bežiacich agentných procesov.
- **Dynamický výber nástrojov**: Kombinácia RAG cez popisy nástrojov s registráciou nástrojov MAF na prezentáciu iba relevantných nástrojov pre dotaz.
- **Multi-agent handoff**: Použitie hrán workflow a podmieneného smerovania na orchestráciu odovzdávania medzi špecializovanými agentmi.

## Hostovanie LangChain / LangGraph agentov na Microsoft Foundry

Microsoft Agent Framework je **rámcovo interoperabilný** — nie ste obmedzení iba na agentov napísaných s MAF. Ak už máte agenta vytvoreného pomocou **LangChain** alebo **LangGraph**, môžete ho spustiť ako **Microsoft Foundry hostovaného agenta**, aby Foundry riadilo runtime, relácie, škálovanie, identitu a koncové body protokolov za vás, zatiaľ čo vaša agentná logika zostáva v LangGraph.

Toto sa robí pomocou balíka `langchain_azure_ai.agents.hosting`, ktorý vystavuje skompilovaný LangGraph graf cez rovnaké protokoly, ktoré používajú Foundry hostovaní agenti.

**1. Nainštalujte hostingový extra balík:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Extra `hosting` inštaluje Foundry protokolové knižnice: `azure-ai-agentserver-responses` (OpenAI-kompatibilný `/responses` endpoint) a `azure-ai-agentserver-invocations` (generický `/invocations` endpoint).

**2. Vyberte hostingový protokol:**

| Protokol | Host trieda | Endpoint | Používajte keď |
|----------|--------------|----------|---------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Chcete OpenAI-kompatibilný chat, streamovanie, históriu odpovedí a vlákna konverzácie — odporúčaný default pre konverzačných agentov. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Potrebujete vlastný JSON tvar, webhook-style endpoint alebo nekonverzačné spracovanie. |

Pretože **Responses API je primárne API pre agentný vývoj v Foundry**, začnite s `ResponsesHostServer` pre väčšinu agentov.

**3. Nakonfigurujte environmentálne premenné** (`az login` najprv, aby sa `DefaultAzureCredential` mohol autentifikovať):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Keď agent neskôr beží ako hostovaný agent v Foundry, platforma automaticky injektuje `FOUNDRY_PROJECT_ENDPOINT`.

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-4.1")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI tu cieli na OpenAI-kompatibilný (Responses) endpoint projektu Foundry.
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

Spustite ho lokálne s `python main.py`, potom pošlite Responses požiadavku na `http://localhost:8088/responses`.

**Kľúčové správanie:**

- **Konverzácie**: Klienti pokračujú v konverzácii zaslaním `previous_response_id` alebo `conversation` ID. Ak je váš graf skompilovaný s LangGraph checkpointerom, Foundry spája stav konverzácie s checkpointom (používajte odolný checkpointer v produkcii; `MemorySaver` je vhodný pre lokálne testovanie).
- **Human-in-the-loop**: Ak váš graf používa LangGraph `interrupt()`, `ResponsesHostServer` zobrazí čakajúci interrupt ako Responses `function_call` / `mcp_approval_request` položku a klienti pokračujú s zodpovedajúcim `function_call_output` / `mcp_approval_response`.
- **Deploy do Foundry**: Použite Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokálne, vyžaduje Docker), potom `azd provision` a `azd deploy`. Nasadenie hostovaných agentov vyžaduje rolu **Foundry Project Manager**.

Spustiteľná verzia tohto príkladu je v [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pre plný návod (protokol Invocations, vlastné schémy požiadaviek a riešenie problémov) pozrite [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Ukážky kódu 

Ukážky kódu pre Microsoft Agent Framework nájdete v tomto úložisku v súboroch `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Máte ďalšie otázky ohľadom Microsoft Agent Framework?

Pridajte sa k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby ste sa stretli s ďalšími študentmi, zúčastnili sa na kancelárskych hodinách a získali odpovede na otázky o AI agentoch.
## Predchádzajúca lekcia

[Pamäť pre AI agentov](../13-agent-memory/README.md)

## Nasledujúca lekcia

[Budovanie agentov na používanie počítača (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->