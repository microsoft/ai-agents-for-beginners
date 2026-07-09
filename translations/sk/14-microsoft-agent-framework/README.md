# Preskúmanie Microsoft Agent Framework

![Agent Framework](../../../translated_images/sk/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Úvod

Táto lekcia pokryje:

- Pochopenie Microsoft Agent Framework: Kľúčové vlastnosti a hodnota  
- Preskúmanie kľúčových konceptov Microsoft Agent Framework
- Pokročilé vzory MAF: Pracovné toky, middleware a pamäť

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

- Vytvárať produkčne pripravených AI agentov pomocou Microsoft Agent Framework
- Použiť základné vlastnosti Microsoft Agent Framework pre vaše agentné prípady použitia
- Používať pokročilé vzory vrátane pracovných tokov, middleware a pozorovateľnosti

## Ukážky kódu 

Ukážky kódu pre [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) nájdete v tomto repozitári v súboroch `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Pochopenie Microsoft Agent Framework

![Framework Intro](../../../translated_images/sk/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) je jednotný rámec Microsoftu na tvorbu AI agentov. Ponúka flexibilitu riešiť širokú škálu agentných prípadov použitia, ktoré sa vyskytujú v produkcii aj výskumných prostrediach, vrátane:

- **Postupná orchestrácia agentov** v situáciách, kde sú potrebné krok-za-krokom pracovné toky.
- **Súbežná orchestrácia** v situáciách, kde agenti musia vykonať úlohy súčasne.
- **Orchestrácia skupinovej konverzácie** v situáciách, kde agenti môžu spolupracovať na jednej úlohe.
- **Orchestrácia odovzdávania** v situáciách, kde agenti odovzdávajú úlohu jeden druhému, ako sa dokončujú podúlohy.
- **Magnetická orchestrácia** v situáciách, kde manažérsky agent vytvára a modifikuje zoznam úloh a riadi koordináciu podagentov na dokončenie úlohy.

Na dodanie AI agentov v produkcii, MAF tiež obsahuje funkcie pre:

- **Pozorovateľnosť** pomocou OpenTelemetry, kde každá akcia AI agenta vrátane volania nástrojov, orchestrácie krokov, dôvodových tokov a monitorovania výkonu cez Microsoft Foundry panely.
- **Bezpečnosť** hostením agentov natívne na Microsoft Foundry, ktorá zahrňuje bezpečnostné kontroly ako prístup na základe rolí, spracovanie súkromných údajov a zabudovanú bezpečnosť obsahu.
- **Trvácnosť** pretože vlákna a pracovné toky agenta môžu byť pozastavené, obnovené a zotavené z chýb, čo umožňuje dlhšie bežiace procesy.
- **Kontrolu** pretože sú podporované pracovné toky s človekom v slučke, kde sú úlohy označené ako vyžadujúce ľudské schválenie.

Microsoft Agent Framework tiež kladie dôraz na interoperabilitu tým, že:

- **Je cloudovo nezávislý** - agenti môžu bežať v kontajneroch, on-premise a naprieč viacerými rôznymi cloudmi.
- **Je poskytovateľsky nezávislý** - agenti môžu byť vytváraní cez váš preferovaný SDK vrátane Azure OpenAI a OpenAI
- **Integruje otvorené štandardy** - agenti môžu využívať protokoly ako Agent-to-Agent (A2A) a Model Context Protocol (MCP) na objavovanie a používanie iných agentov a nástrojov.
- **Pluginy a konektory** - môžu byť vytvorené pripojenia k dátovým a pamäťovým službám ako Microsoft Fabric, SharePoint, Pinecone a Qdrant.

Pozrime sa, ako sa tieto vlastnosti aplikujú na niektoré kľúčové koncepty Microsoft Agent Framework.

## Kľúčové koncepty Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/sk/agent-components.410a06daf87b4fef.webp)

**Vytváranie agentov**

Vytvorenie agenta sa vykonáva definovaním inferenčnej služby (poskytovateľa LLM), 
sady inštrukcií, ktoré má AI agent nasledovať, a priradeného `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Vyššie uvedené používa `Azure OpenAI`, ale agenti môžu byť vytvorení pomocou rôznych služieb vrátane `Microsoft Foundry Agent Service`:

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

Každé spustenie agenta môže mať tiež možnosti na prispôsobenie parametrov ako `max_tokens` používaných agentom, `tools`, ktoré agent môže volať, a dokonca aj samotný `model` používaný pre agenta.

Toto je užitočné v prípadoch, keď sú potrebné konkrétne modely alebo nástroje na dokončenie úlohy používateľa.

**Nástroje**

Nástroje môžu byť definované pri vytváraní agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Pri priamom vytváraní ChatAgenta

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

a tiež pri spúšťaní agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Nástroj poskytnutý len pre tento beh )
```

**Agentné vlákna**

Agentné vlákna sa používajú na spracovanie viackolových konverzácií. Vlákna môžu byť vytvorené buď:

- Použitím `get_new_thread()` čo umožňuje vlákno ukladať počas času
- Automatickým vytvorením vlákna pri spúšťaní agenta, pričom vlákno trvá iba počas aktuálneho spustenia.

Na vytvorenie vlákna vyzerá kód takto:

```python
# Vytvorte nový vlákno.
thread = agent.get_new_thread() # Spustite agenta s vláknom.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Následne môžete serializovať vlákno na uloženie pre neskoršie použitie:

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

Agenti komunikujú s nástrojmi a LLM, aby dokončili úlohy používateľa. V určitých scenároch chceme vykonať alebo sledovať akcie medzi týmito interakciami. Middleware agenta nám to umožňuje cez:

*Funkčný middleware*

Tento middleware nám umožňuje vykonať akciu medzi agentom a funkciou/nástrojom, ktorý volá. Príklad použitia je v prípade, keď chcete robiť zaznamenávanie volania funkcie.

V nasledujúcom kóde `next` definuje, či sa má zavolať ďalší middleware alebo skutočná funkcia.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Predspracovanie: Zaznamenať pred vykonaním funkcie
    print(f"[Function] Calling {context.function.name}")

    # Pokračovať k ďalšiemu middleware alebo vykonaniu funkcie
    await next(context)

    # Následné spracovanie: Zaznamenať po vykonaní funkcie
    print(f"[Function] {context.function.name} completed")
```

*Chat middleware*

Tento middleware nám umožňuje vykonať alebo zaznamenať akciu medzi agentom a požiadavkami smerujúcimi k LLM.

Obsahuje dôležité informácie ako `messages`, ktoré sú zasielané AI službe.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Predspracovanie: Zaznamenať pred volaním AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Pokračovať k ďalšiemu middleware alebo AI službe
    await next(context)

    # Post-processing: Zaznamenať po odpovedi AI
    print("[Chat] AI response received")

```

**Pamäť agenta**

Ako bolo pokryté v lekcii `Agentic Memory`, pamäť je dôležitým prvkom umožňujúcim agentovi fungovať v rôznych kontextoch. MAF ponúka niekoľko rôznych typov pamäti:

*Pamäť v aplikácii*

Ide o pamäť uloženú vo vláknach počas behu aplikácie.

```python
# Vytvorte nový vlákno.
thread = agent.get_new_thread() # Spustite agenta s vláknom.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Trvalé správy*

Táto pamäť sa používa na uchovávanie histórie konverzácie naprieč rôznymi reláciami. Definuje sa pomocou `chat_message_store_factory`:

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

Táto pamäť sa pridáva do kontextu pred spustením agentov. Táto pamäť môže byť uložená v externých službách ako mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Používanie Mem0 pre pokročilé pamäťové schopnosti
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

Pozorovateľnosť je dôležitá na budovanie spoľahlivých a udržiavateľných agentných systémov. MAF integruje OpenTelemetry na poskytovanie sledovania a meraní pre lepšiu pozorovateľnosť.

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

MAF ponúka pracovné toky, ktoré sú preddefinované kroky na dokončenie úlohy a zahŕňajú AI agentov ako súčasti týchto krokov.

Pracovné toky sa skladajú z rôznych komponentov, ktoré umožňujú lepšiu kontrolu toku. Pracovné toky tiež umožňujú **multi-agentnú orchestráciu** a **checkpointing** na ukladanie stavov pracovného toku.

Hlavné komponenty pracovného toku sú:

**Exekútori**

Exekútori prijímajú vstupné správy, vykonávajú pridelené úlohy a následne produkujú výstupnú správu. Toto posúva pracovný tok smerom k dokončeniu väčšej úlohy. Exekútori môžu byť AI agentmi alebo vlastnou logikou.

**Hrany**

Hrany sa používajú na definovanie toku správ v pracovnom toku. Tieto môžu byť:

*Priame hrany* - jednoduché jednosmerné spojenia medzi exekútormi:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Podmienené hrany* - aktivujú sa, keď je splnená určitá podmienka. Napríklad keď nie sú dostupné hotelové izby, exekútor môže navrhnúť iné možnosti.

*Prepínacie hrany* - smerujú správy k rôznym exekútorom na základe definovaných podmienok. Napríklad ak má cestujúci prioritný prístup, jeho úlohy sa spracovávajú cez iný pracovný tok.

*Fan-out hrany* - pošlú jednu správu na viaceré ciele.

*Fan-in hrany* - zhromažďujú viaceré správy z rôznych exekútorov a posielajú ich na jeden cieľ.

**Udalosti**

Aby sa zabezpečila lepšia pozorovateľnosť pracovných tokov, MAF ponúka zabudované udalosti pre vykonávanie vrátane:

- `WorkflowStartedEvent`  - Spustenie pracovného toku
- `WorkflowOutputEvent` - Pracovný tok vygeneroval výstup
- `WorkflowErrorEvent` - Pracovný tok narazil na chybu
- `ExecutorInvokeEvent`  - Exekútor začína spracovanie
- `ExecutorCompleteEvent`  -  Exekútor dokončil spracovanie
- `RequestInfoEvent` - Vydaná požiadavka

## Pokročilé vzory MAF

Predchádzajúce časti pokrývajú kľúčové koncepty Microsoft Agent Framework. Keď budete vytvárať zložitejších agentov, tu sú niektoré pokročilé vzory na zváženie:

- **Kompozícia middleware**: Reťazenie viacerých middleware handlerov (logovanie, autentifikácia, obmedzovanie rýchlosti) pomocou funkčného a chat middleware pre detailnú kontrolu správania agenta.
- **Checkpointing pracovného toku**: Používajte udalosti pracovného toku a serializáciu na uloženie a obnovenie dlhodobých procesov agenta.
- **Dynamický výber nástrojov**: Kombinujte RAG s popismi nástrojov a registráciou nástrojov MAF na zobrazovanie len relevantných nástrojov pre konkrétnu požiadavku.
- **Odovzdávanie medzi viac agentmi**: Používajte hrany pracovných tokov a podmienené smerovanie na orchestráciu odovzdávaní medzi špecializovanými agentmi.

## Hostovanie LangChain / LangGraph agentov na Microsoft Foundry

Microsoft Agent Framework je **interoperabilný rámec** — nie ste obmedzení na agentov napísaných iba s MAF. Ak už máte agenta vytvoreného pomocou **LangChain** alebo **LangGraph**, môžete ho spustiť ako **hosteného agenta v Microsoft Foundry**, kde Foundry spravuje runtime, relácie, škálovanie, identitu a protokolové endpointy za vás, zatiaľ čo vaša logika agenta zostane v LangGraph.

Toto sa robí pomocou balíka `langchain_azure_ai.agents.hosting`, ktorý vystavuje skompilovaný LangGraph graf cez rovnaké protokoly, ktoré používajú hostení agenti Foundry.

**1. Nainštalujte hostingovú nadstavbu:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Nadstavba `hosting` inštaluje protokolové knižnice Foundry: `azure-ai-agentserver-responses` (OpenAI-kompatibilný endpoint `/responses`) a `azure-ai-agentserver-invocations` (generický endpoint `/invocations`).

**2. Vyberte hostingový protokol:**

| Protokol | Trieda hostiteľa | Endpoint | Použitie kedy |
|----------|-------------------|----------|-------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Chcete OpenAI-kompatibilný chat, streaming, históriu odpovedí a zreťazovanie konverzácií — odporúčaný štandard pre konverzačných agentov. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Potrebujete vlastný JSON tvar, webhook-style endpoint alebo ne-konverzačné spracovanie. |

Keďže **Responses API je primárne API pre agentný vývoj v Foundry**, začnite s `ResponsesHostServer` pre väčšinu agentov.

**3. Nakonfigurujte environmentálne premenné** (`az login` najprv, aby sa `DefaultAzureCredential` mohol autentifikovať):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Keď agent neskôr beží ako hostený agent v Foundry, platforma automaticky injektuje `FOUNDRY_PROJECT_ENDPOINT`.

**4. Vystavte LangGraph agenta cez protokol Responses:**

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

Spustite lokálne pomocou `python main.py`, potom pošlite Requests na `http://localhost:8088/responses`.

**Kľúčové správanie:**

- **Konverzácie**: Klienti pokračujú v konverzácii odoslaním `previous_response_id` alebo `conversation` ID. Ak je váš graf skompilovaný s LangGraph checkpointerom, Foundry viaže stav konverzácie na checkpoint (v produkcii používajte trvácny checkpointer; `MemorySaver` je vhodný pre lokálne testovanie).
- **Človek v slučke**: Ak váš graf používa LangGraph `interrupt()`, `ResponsesHostServer` zobrazí čakajúce prerušenie ako položku `function_call` / `mcp_approval_request` v Responses, a klienti pokračujú s odpoveďou `function_call_output` / `mcp_approval_response`.
- **Deploy do Foundry**: Použite Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokálne, vyžaduje Docker), potom `azd provision` a `azd deploy`. Deploy hosteného agenta vyžaduje rolu **Foundry Project Manager**.

Spustiteľná verzia tohto príkladu je v [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pre kompletný návod (protokol Invocations, vlastné schémy požiadaviek a riešenie problémov) pozrite [Hostovanie LangGraph agentov ako Foundry hostených agentov](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Ukážky kódu 

Ukážky kódu pre Microsoft Agent Framework nájdete v tomto repozitári v súboroch `xx-python-agent-framework` a `xx-dotnet-agent-framework`.

## Máte viac otázok o Microsoft Agent Framework?

Pridajte sa k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby ste sa stretli s ostatnými študentmi, zúčastnili sa konzultačných hodín a získali odpovede na vaše otázky ohľadom AI agentov.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->