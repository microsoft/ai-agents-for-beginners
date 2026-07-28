[![Jak navrhnout dobré AI agenty](../../../translated_images/cs/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klikněte na obrázek výše pro zobrazení videa této lekce)_

# Vzor návrhu použití nástroje

Nástroje jsou zajímavé, protože AI agentům umožňují mít širší škálu schopností. Místo toho, aby agent měl omezenou sadu akcí, které může vykonat, přidáním nástroje může agent nyní provádět širokou škálu akcí. V této kapitole se podíváme na vzor návrhu použití nástroje, který popisuje, jak mohou AI agenti používat specifické nástroje k dosažení svých cílů.

## Úvod

V této lekci se pokusíme odpovědět na následující otázky:

- Co je vzor návrhu použití nástroje?
- Na jaké případy použití lze tento vzor aplikovat?
- Jaké prvky/stavební kameny jsou potřeba k implementaci tohoto vzoru návrhu?
- Jaká jsou zvláštní opatření pro použití vzoru návrhu použití nástroje k vytvoření důvěryhodných AI agentů?

## Cíle učení

Po dokončení této lekce budete schopni:

- Definovat vzor návrhu použití nástroje a jeho účel.
- Identifikovat případy použití, kde je vzor použití nástroje použitelný.
- Porozumět klíčovým prvkům potřebným k implementaci vzoru návrhu.
- Uvědomit si úvahy pro zajištění důvěryhodnosti AI agentů používajících tento vzor návrhu.

## Co je vzor návrhu použití nástroje?

**Vzor návrhu použití nástroje** se zaměřuje na umožnění LLM interakce s externími nástroji k dosažení specifických cílů. Nástroje jsou kódy, které může agent spustit, aby provedl akce. Nástrojem může být jednoduchá funkce jako kalkulačka nebo volání API třetí strany, například kontrola ceny akcií nebo předpověď počasí. V kontextu AI agentů jsou nástroje navrženy tak, aby je agenti spouštěli v reakci na **modely generované volání funkcí**.

## Na jaké případy použití lze tento vzor aplikovat?

AI agenti mohou využívat nástroje k dokončení složitých úkolů, získávání informací nebo rozhodování. Vzor návrhu použití nástroje se často používá ve scénářích vyžadujících dynamickou interakci s externími systémy, jako jsou databáze, webové služby nebo interprety kódu. Tato schopnost je užitečná pro různé případy použití, včetně:

- **Dynamické získávání informací:** Agent může dotazovat externí API nebo databáze pro získání aktuálních dat (např. dotaz na databázi SQLite pro analýzu dat, získání cen akcií nebo informací o počasí).
- **Spouštění a interpretace kódu:** Agent může spouštět kód nebo skripty k řešení matematických problémů, generování zpráv nebo provádění simulací.
- **Automatizace pracovních postupů:** Automatizace opakujících se nebo vícestupňových pracovních postupů integrací nástrojů jako plánovače úkolů, e-mailových služeb nebo datových pipeline.
- **Podpora zákazníků:** Agent může komunikovat se systémy CRM, platformami pro správu tiketů nebo znalostními databázemi, aby vyřešil dotazy uživatelů.
- **Generování a úprava obsahu:** Agent může využívat nástroje jako korektory gramatiky, shrnovače textu nebo vyhodnocovače bezpečnosti obsahu, aby pomohl s úkoly tvorby obsahu.

## Jaké jsou prvky/stavební kameny potřebné k implementaci vzoru použití nástroje?

Tyto stavební kameny umožňují AI agentovi plnit širokou škálu úkolů. Podívejme se na klíčové prvky potřebné k implementaci vzoru návrhu použití nástroje:

- **Schémata funkcí/nástrojů**: Detailní definice dostupných nástrojů, včetně názvu funkce, účelu, požadovaných parametrů a očekávaných výstupů. Tato schémata umožňují LLM pochopit, jaké nástroje jsou k dispozici a jak sestavit platné požadavky.

- **Logika spouštění funkcí**: Řídí, jak a kdy jsou nástroje vyvolány na základě uživatelského záměru a kontextu konverzace. To může zahrnovat plánovací moduly, směrovací mechanismy nebo podmíněné toky, které dynamicky určují použití nástroje.

- **Systém zpracování zpráv**: Komponenty, které spravují konverzační tok mezi uživatelskými vstupy, odpověďmi LLM, voláním nástrojů a výstupy nástrojů.

- **Rámec integrace nástrojů**: Infrastruktura, která spojuje agenta s různými nástroji, ať už jde o jednoduché funkce nebo složité externí služby.

- **Zpracování chyb a validace**: Mechanismy pro řešení selhání při spouštění nástrojů, ověřování parametrů a řízení neočekávaných odpovědí.

- **Správa stavu**: Sleduje kontext konverzace, předchozí interakce s nástroji a trvalá data, aby byla zajištěna konzistence během vícetahových interakcí.

Dále si podrobněji probereme volání funkcí/nástrojů.
 
### Volání funkcí/nástrojů

Volání funkcí je primární způsob, jak umožnit velkým jazykovým modelům (LLM) interagovat s nástroji. Často uvidíte výrazy „funkce“ a „nástroj“ používané zaměnitelně, protože „funkce“ (bloky znovupoužitelného kódu) jsou „nástroje“, které agenti používají k vykonávání úkolů. Aby mohla být spuštěna funkce, musí LLM porovnat požadavek uživatele s popisem funkcí. K tomu je odesláno schéma obsahující popisy všech dostupných funkcí. LLM poté vybere nejvhodnější funkci pro úkol a vrátí její název a argumenty. Vybraná funkce je spuštěna, její odpověď je odeslána zpět do LLM, které použije informace k odpovědi na požadavek uživatele.

Pro vývojáře, kteří chtějí implementovat volání funkcí pro agenty, budete potřebovat:

1. LLM model, který podporuje volání funkcí
2. Schéma obsahující popisy funkcí
3. Kód pro každou popsanou funkci

Použijme příklad získání aktuálního času v nějakém městě jako ilustraci:

1. **Inicializujte LLM, které podporuje volání funkcí:**

    Ne všechny modely volání funkcí podporují, proto je důležité zkontrolovat, zda to LLM, které používáte, dělá.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podporuje volání funkcí. Můžeme začít inicializací OpenAI klienta vůči Azure OpenAI **Responses API** (stabilní endpoint `/openai/v1/` — není třeba `api_version`). 

    ```python
    # Inicializujte klienta OpenAI pro Azure OpenAI (Responses API, koncový bod v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Vytvořte schéma funkce**:

    Dále definujeme JSON schéma, které obsahuje název funkce, popis toho, co funkce dělá, a názvy a popisy parametrů funkce.
    Toto schéma pak předáme klientovi vytvořenému dříve spolu s uživatelským požadavkem na zjištění času v San Franciscu. Co je důležité poznamenat, je to, že je vrácen **volání nástroje**, **nikoliv** konečná odpověď na otázku. Jak bylo zmíněno dříve, LLM vrátí název funkce, kterou vybral pro úkol, a argumenty, které jí budou předány.

    ```python
    # Popis funkce pro načtení modelu (formát plochého nástroje Responses API)
    tools = [
        {
            "type": "function",
            "name": "get_current_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        }
    ]
    ```
   
    ```python
  
    # Počáteční uživatelská zpráva
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # První API volání: Požádejte model, aby použil funkci
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API vrací volání nástrojů jako položky function_call v response.output.
    # Připojte je ke konverzaci, aby měl model plný kontext při dalším tahu.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Kód funkce potřebný k vykonání úkolu:**

    Nyní, když LLM vybralo, kterou funkci spustit, je potřeba implementovat a vykonat kód, který úkol vykoná.
    Můžeme implementovat kód pro zjištění aktuálního času v Pythonu. Budeme také potřebovat napsat kód pro extrahování názvu a argumentů z response_message pro získání konečného výsledku.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
    # Zpracovat volání funkcí
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Vrátit výsledek nástroje jako položku function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Druhý API volání: Získat konečnou odpověď od modelu
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Volání funkcí je jádrem většiny, pokud ne všech agentních použití nástrojů, ale jeho implementace od nuly může být někdy náročná.
Jak jsme se naučili v [Lekci 2](../../../02-explore-agentic-frameworks), agentní rámce nám poskytují předpřipravené stavební kameny pro implementaci použití nástrojů.
 
## Příklady použití nástroje s agentními rámci

Zde je několik příkladů, jak můžete implementovat vzor návrhu použití nástroje pomocí různých agentních rámců:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> je open-source AI rámec pro tvorbu AI agentů. Zjednodušuje proces používání volání funkcí tím, že umožňuje definovat nástroje jako Python funkce s dekorátorem `@tool`. Rámec zajišťuje obousměrnou komunikaci mezi modelem a vaším kódem. Nabízí také přístup k předpřipraveným nástrojům jako File Search a Code Interpreter přes `FoundryChatClient`.

Následující diagram znázorňuje proces volání funkcí v Microsoft Agent Framework:

![function calling](../../../translated_images/cs/functioncalling-diagram.a84006fc287f6014.webp)

V Microsoft Agent Framework jsou nástroje definovány jako dekorované funkce. Můžeme převést funkci `get_current_time`, kterou jsme viděli dříve, na nástroj použitím dekorátoru `@tool`. Rámec automaticky serializuje funkci a její parametry, vytváří schéma pro odeslání LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Vytvořit klienta
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Vytvořit agenta a spustit nástrojem
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> je novější agentní rámec, navržený pro umožnění vývojářům bezpečně vytvářet, nasazovat a škálovat vysoce kvalitní a rozšiřitelné AI agenty bez nutnosti spravovat základní výpočetní a úložné zdroje. Je zvláště vhodný pro podnikové aplikace, protože je plně spravovaná služba s bezpečností na úrovni podniku.

V porovnání s vývojem přímo pomocí LLM API poskytuje Microsoft Foundry Agent Service některé výhody, včetně:

- Automatické volání nástrojů – není třeba analyzovat volání nástroje, vyvolávat nástroj a zpracovávat odpověď; vše se nyní provádí na straně serveru
- Bezpečně spravovaná data – místo správy vlastního stavu konverzace se můžete spolehnout na vlákna, která ukládají všechny potřebné informace
- Nástroje připravené k použití – nástroje, které můžete používat k interakci se zdroji dat, jako jsou Bing, Azure AI Search a Azure Functions.

Nástroje dostupné v Microsoft Foundry Agent Service lze rozdělit do dvou kategorií:

1. Nástroje znalostí:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Základ pomocí Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Akční nástroje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Volání funkcí</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Nástroje definované OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nám umožňuje používat tyto nástroje společně jako `sadu nástrojů`. Také využívá `vlákna`, která sledují historii zpráv z konkrétní konverzace.

Představte si, že jste obchodní agent ve firmě Contoso. Chcete vyvinout konverzačního agenta, který může odpovídat na otázky o vašich prodejních datech.

Následující obrázek znázorňuje, jak byste mohli použít Microsoft Foundry Agent Service k analýze vašich prodejních dat:

![Agentní služba v akci](../../../translated_images/cs/agent-service-in-action.34fb465c9a84659e.webp)

Pro použití těchto nástrojů se službou můžeme vytvořit klienta a definovat nástroj nebo sadu nástrojů. K praktické implementaci můžeme použít následující Python kód. LLM bude schopné nahlédnout na sadu nástrojů a rozhodnout, zda použije uživatelem vytvořenou funkci `fetch_sales_data_using_sqlite_query` nebo předpřipravený Code Interpreter v závislosti na uživatelské žádosti.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # funkce fetch_sales_data_using_sqlite_query, kterou najdete v souboru fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inicializovat nástroje
toolset = ToolSet()

# Inicializovat agenta volajícího funkce s функí fetch_sales_data_using_sqlite_query a přidat ji do nástrojů
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializovat nástroj Code Interpreter a přidat ho do nástrojů.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Jaká jsou zvláštní opatření pro použití vzoru návrhu použití nástroje k vytvoření důvěryhodných AI agentů?

Častou obavou u SQL dynamicky generovaného LLM je bezpečnost, zejména riziko SQL injekce nebo škodlivých akcí, jako je odstranění nebo úprava databáze. I když jsou tyto obavy oprávněné, lze je účinně zmírnit správným nastavením oprávnění přístupu k databázi. U většiny databází to zahrnuje nastavení databáze jako pouze pro čtení. U databázových služeb jako PostgreSQL nebo Azure SQL by měla mít aplikace přiřazenou roli pouze pro čtení (SELECT).

Spuštění aplikace v zabezpečeném prostředí dále zvyšuje ochranu. V podnikových scénářích se data typicky extrahují a transformují z provozních systémů do databáze nebo datového skladu pouze pro čtení s uživatelsky přívětivým schématem. Tento přístup zajišťuje, že data jsou bezpečná, optimalizovaná pro výkon a přístupnost, a že aplikace má omezený, jen pro čtení přístup.

## Ukázkové kódy

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Máte další otázky ohledně vzoru návrhu použití nástroje?

Připojte se k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde se můžete setkat s dalšími studenty, zúčastnit se konzultací a získat odpovědi na své otázky o AI agentech.

## Dodatečné zdroje

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Přehled Microsoft Agent Framework</a>


## Rychlý test tohoto agenta (volitelné)

Poté, co se naučíte nasazovat agenty v [Lekci 16](../16-deploying-scalable-agents/README.md), můžete rychle otestovat `TravelToolAgent` z této lekce (zda stále volá své nástroje a odpovídá) pomocí [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Viz [`tests/README.md`](../tests/README.md) pro návod, jak jej spustit.

## Předchozí lekce

[Porozumění agentním návrhovým vzorům](../03-agentic-design-patterns/README.md)

## Následující lekce

[Agentní RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->