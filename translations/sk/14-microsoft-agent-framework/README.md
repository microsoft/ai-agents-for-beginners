# Preskúmanie Microsoft Agent Framework

![Agent Framework](../../../translated_images/sk/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Úvod

Táto lekcia pokryje:

- Pochopenie Microsoft Agent Framework: Kľúčové vlastnosti a hodnota  
- Preskúmanie kľúčových konceptov Microsoft Agent Framework
- Pokročilé vzory MAF: Workflowy, middleware a pamäť

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

- Vytvárať AI agentov pripravených do produkcie pomocou Microsoft Agent Framework
- Aplikovať základné vlastnosti Microsoft Agent Framework na vaše agentické prípady použitia
- Používať pokročilé vzory vrátane workflowov, middleware a pozorovateľnosti

## Ukážky kódu 

Ukážky kódu pre [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) nájdete v tomto repozitári v súboroch `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Pochopenie Microsoft Agent Framework

![Framework Intro](../../../translated_images/sk/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) je jednotný rámec Microsoftu na budovanie AI agentov. Ponúka flexibilitu riešiť širokú škálu agentických prípadov použitia, ktoré sa vyskytujú v produkčných aj výskumných prostrediach, vrátane:

- **Sekvenčná orchestrácia agentov** v scenároch, kde sú potrebné krok za krokom workflowy.
- **Súbežná orchestrácia** v scenároch, kde agenti musia dokončiť úlohy súčasne.
- **Orchestrácia skupinových rozhovorov** v scenároch, kde agenti môžu spolupracovať na jednej úlohe.
- **Orchestrácia odovzdávania** v scenároch, kde agenti si odovzdávajú úlohu, keď sú čiastočné úlohy dokončené.
- **Magnetická orchestrácia** v scenároch, kde manažérsky agent vytvára a upravuje zoznam úloh a riadi koordináciu podagentov na dokončenie úlohy.

Na doručenie AI agentov v produkcii má MAF tiež zahrnuté funkcie pre:

- **Pozorovateľnosť** prostredníctvom použitia OpenTelemetry, kde každá akcia AI agenta vrátane volania nástrojov, orchestrácie krokov, tokov rozumovania a monitoringu výkonu cez Microsoft Foundry dashboardy.
- **Bezpečnosť** hostovaním agentov natívne na Microsoft Foundry, ktorá zahŕňa bezpečnostné kontroly ako prístup na základe rolí, spracovanie súkromných údajov a vstavanú bezpečnosť obsahu.
- **Trvácnosť** keďže vlákna a workflowy agentov môžu pauzovať, obnovovať sa a zotavovať sa z chýb, čo umožňuje dlhšie bežiace procesy.
- **Kontrolu** pretože sú podporované workflowy s človekom v slučke, kde sú úlohy označené ako vyžadujúce schválenie človekom.

Microsoft Agent Framework sa tiež zameriava na interoperabilitu tým, že:

- **Je cloudovo nezávislý** - Agenti môžu bežať v kontajneroch, on-premise a cez rôzne cloudové prostredia.
- **Je nezávislý na poskytovateľovi** - Agenti môžu byť vytvorení pomocou vášho preferovaného SDK vrátane Azure OpenAI a OpenAI
- **Integruje otvorené štandardy** - Agenti môžu využívať protokoly ako Agent-to-Agent (A2A) a Model Context Protocol (MCP) na objavovanie a používanie iných agentov a nástrojov.
- **Pluginy a konektory** - Môžu byť vytvorené prepojenia na dáta a pamäťové služby ako Microsoft Fabric, SharePoint, Pinecone a Qdrant.

Pozrime sa, ako sú tieto funkcie aplikované na niektoré z kľúčových konceptov Microsoft Agent Framework.

## Kľúčové koncepty Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/sk/agent-components.410a06daf87b4fef.webp)

**Tvorba agentov**

Vytváranie agentov sa vykonáva definovaním inferenčnej služby (poskytovateľa LLM),  
sady inštrukcií, ktoré AI agent má nasledovať, a priradeného `mena`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Vyššie uvedené používa `Azure OpenAI`, ale agenti môžu byť vytváraní pomocou rôznych služieb vrátane `Microsoft Foundry Agent Service`:

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

alebo [MiniMax](https://platform.minimaxi.com/), ktorý poskytuje OpenAI-kompatibilné API s veľkými kontextovými oknami (až 204K tokenov):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

alebo vzdialení agenti používajúci protokol A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Spúšťanie agentov**

Agenti sa spúšťajú použitím metód `.run` alebo `.run_stream` pre ne-streamované alebo streamované odpovede.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Každé spustenie agenta môže mať aj možnosti na prispôsobenie parametrov ako `max_tokens` používaných agentom, `tools`, ktoré agent môže volať, a dokonca aj samotný `model` použitý pre agenta.

Toto je užitočné v prípadoch, kde sú potrebné konkrétne modely alebo nástroje na dokončenie úlohy používateľa.

**Nástroje**

Nástroje môžu byť definované ako pri definovaní agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Pri priamom vytváraní ChatAgenta

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

tak aj pri spúšťaní agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Nástroj poskytnutý iba pre toto spustenie )
```

**Vlákna agentov**

Vlákna agentov sa používajú na spracovanie viackrokových rozhovorov. Vlákna môžu byť vytvorené buď:

- Použitím `get_new_thread()`, ktoré umožňuje vlákno uložiť na neskoršie použitie
- Automatickým vytvorením vlákna pri spúšťaní agenta, kde vlákno trvá len počas aktuálneho spustenia.

Kód na vytvorenie vlákna vyzerá takto:

```python
# Vytvorte nový vlákno.
thread = agent.get_new_thread() # Spustite agenta vo vlákne.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Vlákno potom môžete serializovať na uloženie na neskoršie použitie:

```python
# Vytvorte nový vláknový proces.
thread = agent.get_new_thread() 

# Spustite agenta s vláknovým procesom.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializujte vlákno na uloženie.

serialized_thread = await thread.serialize() 

# Deserializujte stav vlákna po načítaní z ukladiska.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware agenta**

Agenti komunikujú s nástrojmi a LLM, aby splnili úlohy používateľa. V určitých scenároch chceme vykonať alebo sledovať medzikroky týchto interakcií. Middleware agenta nám to umožňuje prostredníctvom:

*Function Middleware*

Tento middleware nám umožňuje vykonať akciu medzi agentom a funkciou/nástrojom, ktorý bude volať. Príkladom použitia je napríklad vykonanie logovania volania funkcie.

V kóde nižšie `next` definuje, či sa má zavolať ďalší middleware alebo samotná funkcia.

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

    # Pospraovanie: Záznam po vykonaní funkcie
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Tento middleware nám umožňuje vykonať alebo zaznamenať akciu medzi agentom a požiadavkami na LLM.

Obsahuje dôležité informácie, ako sú `messages`, ktoré sa posielajú AI službe.

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

Ako bolo pokryté v lekcii `Agentic Memory`, pamäť je dôležitým prvkom, ktorý umožňuje agentovi pracovať cez rôzne kontexty. MAF ponúka niekoľko rôznych typov pamätí:

*Pamäť v pamäti (In-Memory Storage)*

Ide o pamäť uloženú vo vláknach počas behu aplikácie.

```python
# Vytvorte nový vlákno.
thread = agent.get_new_thread() # Spustite agenta s vláknom.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Trvalé správy (Persistent Messages)*

Táto pamäť sa používa pri ukladaní histórie rozhovorov medzi rôznymi reláciami. Definuje sa pomocou `chat_message_store_factory`:

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


Táto pamäť sa pridáva do kontextu pred spustením agentov. Tieto pamäte môžu byť uložené v externých službách, ako napríklad mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Použitie Mem0 pre pokročilé pamäťové funkcie
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

**Pozorovateľnosť agenta**

Pozorovateľnosť je dôležitá pre budovanie spoľahlivých a udržiavateľných agentových systémov. MAF sa integruje s OpenTelemetry, aby poskytoval sledovanie a metriky pre lepšiu pozorovateľnosť.

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

### Pracovné postupy

MAF ponúka pracovné postupy, ktoré sú preddefinované kroky na dokončenie úlohy a zahŕňajú AI agentov ako súčasti týchto krokov.

Pracovné postupy sa skladajú z rôznych komponentov, ktoré umožňujú lepšiu riadiacu logiku. Pracovné postupy tiež umožňujú **orchestráciu viacerých agentov** a **checkpointovanie** na uloženie stavov pracovných postupov.

Kľúčové komponenty pracovného postupu sú:

**Vykonávacie jednotky**

Vykonávacie jednotky prijímajú vstupné správy, vykonávajú priradené úlohy a potom produkujú výstupnú správu. Tým sa pracovný postup posúva k dokončeniu väčšej úlohy. Vykonávacie jednotky môžu byť AI agenti alebo vlastná logika.

**Hrany**

Hrany sa používajú na definovanie toku správ v pracovnom postupe. Tie môžu byť:

*Priame hrany* - Jednoduché jedno-na-jedno spojenia medzi vykonávacími jednotkami:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Podmienené hrany* - Aktivované po splnení určitej podmienky. Napríklad, keď nie sú k dispozícii hotelové izby, vykonávacia jednotka môže navrhnúť iné možnosti.

*Hrany typu switch-case* - Smerujú správy k rôznym vykonávacím jednotkám na základe definovaných podmienok. Napríklad, ak má cestovný zákazník prioritný prístup, jeho úlohy budú spracované cez iný pracovný postup.

*Fan-out hrany* - Posielajú jednu správu na viacero cieľov.

*Fan-in hrany* - Zbierajú viacero správ od rôznych vykonávacích jednotiek a posielajú ich jednému cieľu.

**Udalosti**

Pre lepšiu pozorovateľnosť pracovných postupov MAF ponúka vstavné udalosti pri vykonávaní vrátane:

- `WorkflowStartedEvent`  - Začatie vykonávania pracovného postupu
- `WorkflowOutputEvent` - Pracovný postup vygeneruje výstup
- `WorkflowErrorEvent` - Pracovný postup sa stretne s chybou
- `ExecutorInvokeEvent`  - Vykonávacia jednotka začína spracovávanie
- `ExecutorCompleteEvent`  -  Vykonávacia jednotka dokončuje spracovanie
- `RequestInfoEvent` - Bola vydaná požiadavka

## Pokročilé vzory MAF

Predchádzajúce sekcie pokrývajú kľúčové koncepty Microsoft Agent Framework. Keď vytvárate komplikovanejších agentov, tu sú niektoré pokročilé vzory na zváženie:

- **Kompozícia middleware**: Reťazenie viacerých middleware handlerov (logovanie, autentifikácia, obmedzovanie rýchlosti) pomocou funkčného a chat middleware pre detailnú kontrolu správania agentov.
- **Checkpointovanie pracovných postupov**: Použitie udalostí pracovného postupu a serializácie na uloženie a obnovenie dlhodobých agentových procesov.
- **Dynamický výber nástrojov**: Kombinovanie RAG cez popisy nástrojov s registráciou nástrojov v MAF tak, aby sa zobrazovali iba relevantné nástroje pre daný dotaz.
- **Handover viacerých agentov**: Použitie hrán pracovných postupov a podmieneného smerovania na orchestráciu odovzdania medzi špecializovanými agentmi.

## Hostovanie agentov LangChain / LangGraph na Microsoft Foundry

Microsoft Agent Framework je **kompatibilný s rôznymi frameworkami** — nie ste limitovaní iba na agentov napísaných v MAF. Ak už máte agenta vytvoreného s **LangChain** alebo **LangGraph**, môžete ho spustiť ako **agenta hosťovaného Microsoft Foundry**, takže Foundry spravuje runtime, relácie, škálovanie, identitu a koncové body protokolu, zatiaľ čo vaša agentová logika zostáva v LangGraph.

Toto je realizované prostredníctvom balíka `langchain_azure_ai.agents.hosting`, ktorý exponuje skompilovaný LangGraph graf cez tie isté protokoly, ktoré používajú Foundry hosťovaní agenti.

**1. Nainštalujte hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Extra `hosting` inštaluje knižnice protokolov Foundry: `azure-ai-agentserver-responses` (OpenAI kompatibilný endpoint `/responses`) a `azure-ai-agentserver-invocations` (generický endpoint `/invocations`).

**2. Vyberte hostingový protokol:**

| Protokol | Trieda hosťa | Endpoint | Použitie |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Chcete OpenAI-kompatibilné chatovanie, streamovanie, históriu odpovedí a prepojenie konverzácií — odporúčaná predvoľba pre konverzačných agentov. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Potrebujete vlastný JSON formát, webhook štýl endpointu, alebo ne-konverzačné spracovanie. |

Pretože **Responses API je primárne API pre vývoj agentov vo Foundry**, začnite s `ResponsesHostServer` pre väčšinu agentov.

**3. Nakonfigurujte environmentálne premenné** (`az login` najprv, aby sa `DefaultAzureCredential` mohol autentifikovať):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Keď agent neskôr beží ako hosťovaný agent vo Foundry, platforma automaticky vloží `FOUNDRY_PROJECT_ENDPOINT`.

**4. Exponujte LangGraph agenta cez protokol Responses:**

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

    # ChatOpenAI tu cieli na OpenAI-kompatibilný (odpovede) koncový bod projektu Foundry.
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

Spustite ho lokálne pomocou `python main.py`, potom odošlite požiadavku Responses na `http://localhost:8088/responses`.

**Kľúčové správanie:**

- **Konverzácie**: Klienti pokračujú v konverzácii odoslaním `previous_response_id` alebo ID `conversation`. Ak je graf skompilovaný s LangGraph checkpointérom, Foundry mapuje stav konverzácie na checkpoint (v produkcii používajte trvalý checkpoint; `MemorySaver` je vhodný pre lokálne testovanie).
- **Človek v slučke**: Ak váš graf používa LangGraph `interrupt()`, `ResponsesHostServer` zviditeľní čakajúci interrupt ako položku `function_call` / `mcp_approval_request` v odpovediach a klienti pokračujú so zodpovedajúcou `function_call_output` / `mcp_approval_response`.
- **Deploy do Foundry**: Použite Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokálne, vyžaduje Docker), potom `azd provision` a `azd deploy`. Deploy hosťovaných agentov vyžaduje rolu **Foundry Project Manager**.

Spustiteľná verzia tohto príkladu je v [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pre kompletný návod (protokol Invocations, vlastné schémy požiadaviek a riešenie problémov) si pozrite [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Ukážky kódu 

Ukážky kódu pre Microsoft Agent Framework nájdete v tomto repozitári pod súbormi `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Máte ďalšie otázky o Microsoft Agent Framework?

Pripojte sa k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby ste sa stretli s ďalšími študentmi, zúčastnili sa konzultácií a dostali odpovede na vaše otázky ohľadom AI agentov.
## Predchádzajúca lekcia

[Pamäť pre AI agentov](../13-agent-memory/README.md)

## Nasledujúca lekcia


[Tvorba agentov pre použitie počítača (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->