[![Jak navrhnout dobré AI agenty](../../../translated_images/cs/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klikněte na obrázek výše pro zobrazení videa této lekce)_

# Návrhový vzor používání nástrojů

Nástroje jsou zajímavé, protože umožňují AI agentům mít širší škálu schopností. Místo toho, aby agent měl omezenou sadu akcí, které může provádět, přidáním nástroje může agent nyní vykonávat širokou škálu akcí. V této kapitole se podíváme na návrhový vzor používání nástrojů, který popisuje, jak AI agenti mohou používat konkrétní nástroje k dosažení svých cílů.

## Úvod

V této lekci chceme odpovědět na následující otázky:

- Co je návrhový vzor používání nástrojů?
- Pro jaké scénáře lze tento vzor použít?
- Jaké prvky/stavební bloky jsou potřeba k implementaci tohoto návrhového vzoru?
- Jaká jsou speciální hlediska použití návrhového vzoru používání nástrojů pro budování důvěryhodných AI agentů?

## Cíle učení

Po dokončení této lekce budete schopni:

- Definovat návrhový vzor používání nástrojů a jeho účel.
- Identifikovat scénáře, kde je možné návrhový vzor použít.
- Pochopit klíčové prvky potřebné k implementaci tohoto návrhového vzoru.
- Rozpoznat aspekty důležité pro zajištění důvěryhodnosti AI agentů používajících tento vzor.

## Co je návrhový vzor používání nástrojů?

**Návrhový vzor používání nástrojů** se zaměřuje na to, aby LLM měly schopnost komunikovat s externími nástroji k dosažení specifických cílů. Nástroje jsou kód, který může agent spustit k provedení akcí. Nástroj může být jednoduchá funkce, například kalkulačka, nebo volání API třetí strany, například vyhledání ceny akcií nebo předpověď počasí. V kontextu AI agentů jsou nástroje navrženy tak, aby je agenti spouštěli jako reakci na **funkční volání generovaná modelem**.

## Pro jaké scénáře lze tento vzor použít?

AI agenti mohou využívat nástroje k dokončení složitých úkolů, zisku informací nebo k rozhodování. Návrhový vzor používání nástrojů se často používá ve scénářích, které vyžadují dynamickou interakci s externími systémy, jako jsou databáze, webové služby nebo interprety kódu. Tato schopnost je užitečná pro řadu různých případů užití, včetně:

- **Dynamické získávání informací:** Agent může dotazovat externí API nebo databáze, aby získal aktuální data (např. dotazování SQLite databáze pro analýzu dat, získávání cen akcií nebo informací o počasí).
- **Spouštění a interpretace kódu:** Agent může spouštět kód nebo skripty k řešení matematických problémů, generování zpráv nebo provádění simulací.
- **Automatizace pracovních toků:** Automatizace opakujících se nebo vícekrokových pracovních procesů integrací nástrojů jako plánovače úkolů, e-mailových služeb nebo datových pipeline.
- **Zákaznická podpora:** Agent může komunikovat s CRM systémy, ticketovacími platformami nebo znalostními databázemi k řešení dotazů uživatelů.
- **Generování a úprava obsahu:** Agent může využívat nástroje jako kontrolu gramatiky, shrnovače textu nebo hodnotitele bezpečnosti obsahu k podpoře tvorby obsahu.

## Jaké prvky/stavební bloky jsou potřeba k implementaci návrhového vzoru používání nástrojů?

Tyto stavební bloky umožňují AI agentovi vykonávat širokou škálu úkolů. Podívejme se na klíčové prvky potřebné k implementaci návrhového vzoru používání nástrojů:

- **Schémata funkcí/nástrojů**: Podrobné definice dostupných nástrojů, včetně názvů funkcí, účelu, požadovaných parametrů a očekávaných výstupů. Tato schémata umožňují LLM pochopit, jaké nástroje jsou dostupné a jak vytvářet platné požadavky.

- **Logika spouštění funkcí**: Řídí, jak a kdy jsou nástroje vyvolány na základě záměru uživatele a kontextu konverzace. Může zahrnovat plánovač, směrovací mechanismy nebo podmíněné toky, které dynamicky rozhodují o použití nástroje.

- **Systém zpracování zpráv**: Komponenty, které spravují konverzační tok mezi vstupy uživatele, odpověďmi LLM, voláním nástrojů a výstupy nástrojů.

- **Rámec integrace nástrojů**: Infrastruktura, která propojuje agenta s různými nástroji, ať už jsou to jednoduché funkce nebo složité externí služby.

- **Zpracování chyb a validace**: Mechanismy pro řešení selhání při spuštění nástrojů, validaci parametrů a správu neočekávaných odpovědí.

- **Správa stavu**: Sleduje kontext konverzace, předchozí interakce s nástroji a perzistentní data, aby zajistila konzistenci napříč vícekrokovými interakcemi.

Nyní se podíváme podrobněji na volání funkcí/nástrojů.
 
### Volání funkcí/nástrojů

Volání funkcí je hlavní způsob, jak umožňujeme rozsáhlým jazykovým modelům (LLM) komunikovat s nástroji. Často uvidíte, že pojmy „funkce“ a „nástroj“ se používají zaměnitelně, protože „funkce“ (bloky znovupoužitelného kódu) jsou ty „nástroje“, které agenti používají k vykonávání úkolů. Aby bylo možné zavolat kód funkce, musí LLM porovnat požadavek uživatele s popisem funkcí. K tomu se do LLM posílá schéma obsahující popisy všech dostupných funkcí. LLM pak vybere nejvhodnější funkci pro úkol a vrátí její název a argumenty. Vybraná funkce je zavolána, její odpověď je poslána zpět LLM, které používá tyto informace k odpovědi na uživatelský požadavek.

Pro vývojáře, kteří chtějí implementovat volání funkcí pro agenty, bude potřeba:

1. Model LLM, který podporuje volání funkcí
2. Schéma obsahující popisy funkcí
3. Kód pro každou popsanou funkci

Pro ilustraci použijme příklad získání aktuálního času ve městě:

1. **Inicializovat LLM, který podporuje volání funkcí:**

    Ne všechny modely podporují volání funkcí, proto je důležité ověřit, že ten, který používáte, tuto podporu má. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podporuje volání funkcí. Můžeme začít inicializací klienta Azure OpenAI.

    ```python
    # Inicializujte klienta Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Vytvořit schéma funkce:**

    Následně definujeme JSON schéma, které obsahuje název funkce, popis toho, co funkce dělá, a názvy a popisy jejích parametrů.
    Toto schéma pak předáme dříve vytvořenému klientovi spolu s uživatelským požadavkem ohledně času v San Franciscu. Co je důležité si uvědomit, je že **vyvolání nástroje** je to, co je vráceno, **nikoli** konečná odpověď na otázku. Jak bylo zmíněno dříve, LLM vrací název funkce vybrané pro úkol a argumenty, které se jí předají.

    ```python
    # Popis funkce pro model ke čtení
    tools = [
        {
            "type": "function",
            "function": {
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
        }
    ]
    ```
   
    ```python
  
    # Počáteční zpráva uživatele
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # První volání API: Požádejte model, aby použil funkci
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Zpracovat odpověď modelu
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Kód funkce potřebný k provedení úkolu:**

    Poté, co LLM vybralo, která funkce má být spuštěna, je třeba implementovat a spustit kód, který úkol vykoná.
    Můžeme implementovat kód pro získání aktuálního času v Pythonu. Také budeme muset napsat kód, který z response_message extrahuje název funkce a argumenty, abychom získali konečný výsledek.

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
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Druhé volání API: Získat konečnou odpověď od modelu
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Volání funkcí je srdcem většiny, pokud ne všech, návrhů používání nástrojů agentů, avšak implementace od základu může být někdy náročná.
Jak jsme se naučili v [Lekci 2](../../../02-explore-agentic-frameworks), agentická prostředí nám poskytují předpřipravené stavební bloky pro implementaci používání nástrojů.
 
## Příklady používání nástrojů s agentickými frameworky

Zde jsou příklady, jak můžete implementovat návrhový vzor používání nástrojů pomocí různých agentických frameworků:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> je open-source AI framework pro vývojáře v .NET, Pythonu a Javě pracující s rozsáhlými jazykovými modely (LLM). Usnadňuje proces volání funkcí automatickým popisem vašich funkcí a jejich parametrů modelu prostřednictvím procesu zvaného <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializace</a>. Také řeší obousměrnou komunikaci mezi modelem a vaším kódem. Další výhodou použití agentického frameworku jako Semantic Kernel je, že umožňuje přístup k předpřipraveným nástrojům, jako je <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Hledání souborů</a> a <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Interpret kódu</a>.

Následující diagram ilustruje proces volání funkcí se Semantic Kernel:

![function calling](../../../translated_images/cs/functioncalling-diagram.a84006fc287f6014.webp)

Ve Semantic Kernel se funkce/nástroje nazývají <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">pluginy</a>. Můžeme převést funkci `get_current_time`, kterou jsme viděli dříve, na plugin tak, že ji převedeme na třídu s touto funkcí uvnitř. Můžeme také importovat dekorátor `kernel_function`, který přijímá popis funkce. Když potom vytvoříte kernel s GetCurrentTimePlugin, kernel automaticky serializuje funkci a její parametry a při tom vytvoří schéma, které se odešle LLM.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Vytvořit jádro
kernel = Kernel()

# Vytvořit plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Přidat plugin do jádra
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> je novější agentický framework navržený tak, aby umožnil vývojářům bezpečně vytvářet, nasazovat a škálovat vysoce kvalitní a rozšiřitelné AI agenty, aniž by museli spravovat základní výpočetní a úložné zdroje. Je obzvlášť užitečný pro podnikové aplikace, protože je plně spravovanou službou s bezpečností na úrovni podnikové třídy.

Ve srovnání s přímým vývojem pomocí LLM API nabízí Azure AI Agent Service několik výhod, včetně:

- Automatické volání nástrojů – není třeba analyzovat volání nástroje, volat nástroj a zpracovávat odpověď; vše je nyní řešeno na straně serveru
- Bezpečně spravovaná data – místo správy vlastního stavu konverzace můžete spoléhat na vlákna, která uchovávají všechny potřebné informace
- Nástroje připravené k použití – nástroje, které můžete použít pro interakci se zdroji dat, jako je Bing, Azure AI Search a Azure Functions.

Nástroje dostupné v Azure AI Agent Service lze rozdělit do dvou kategorií:

1. Nástroje pro znalosti:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Základní data s Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Hledání souborů</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Akční nástroje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Volání funkcí</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpret kódu</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Nástroje definované OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nám umožňuje tyto nástroje používat společně jako `toolset`. Používá také `vlákna`, která sledují historii zpráv v konkrétní konverzaci.

Představte si, že jste obchodní zástupce ve společnosti Contoso. Chcete vyvinout konverzačního agenta, který bude umět odpovídat na otázky týkající se vašich prodejních dat.

Následující obrázek znázorňuje, jak byste mohli použít Azure AI Agent Service k analýze vašich prodejních dat:

![Agentic Service In Action](../../../translated_images/cs/agent-service-in-action.34fb465c9a84659e.webp)

Pro použití kterékoli z těchto nástrojů se službou můžeme vytvořit klienta a definovat nástroj nebo sadu nástrojů. Pro praktickou implementaci můžeme použít následující Python kód. LLM bude moci prohlédnout toolset a rozhodnout, zda použít uživatelem vytvořenou funkci `fetch_sales_data_using_sqlite_query` nebo předpřipravený Code Interpreter v závislosti na požadavku uživatele.

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

# Inicializace sady nástrojů
toolset = ToolSet()

# Inicializace agenta volícího funkce s funkcí fetch_sales_data_using_sqlite_query a přidání do sady nástrojů
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializace nástroje Code Interpreter a jeho přidání do sady nástrojů.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Jaká jsou speciální hlediska použití návrhového vzoru používání nástrojů pro budování důvěryhodných AI agentů?

Běžným problémem u dynamicky generovaného SQL kódu pomocí LLM je bezpečnost, zejména riziko SQL injection nebo škodlivých akcí, jako je například smazání nebo poškození databáze. Ačkoliv jsou tyto obavy oprávněné, lze je efektivně mitigovat správnou konfigurací oprávnění přístupu k databázi. Pro většinu databází to znamená nastavení databáze do režimu pouze pro čtení. U databázových služeb jako PostgreSQL nebo Azure SQL by měla aplikace dostat roli s oprávněním pouze pro čtení (SELECT).
Spuštění aplikace v zabezpečeném prostředí dále zvyšuje ochranu. V podnikových scénářích jsou data obvykle extrahována a transformována z operačních systémů do databáze nebo datového skladu pouze pro čtení s uživatelsky přívětivým schématem. Tento přístup zajišťuje, že data jsou zabezpečená, optimalizovaná pro výkon a přístupnost a že aplikace má omezený přístup pouze pro čtení.

## Ukázkové kódy

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Máte další otázky týkající se návrhových vzorů nástroje?

Připojte se k [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kde se můžete setkat s ostatními studenty, navštěvovat konzultační hodiny a získat odpovědi na své otázky ohledně AI agentů.

## Další zdroje

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Workshop Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Tutoriál Semantic Kernel volání funkcí</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Předchozí lekce

[Porozumění agentním návrhovým vzorům](../03-agentic-design-patterns/README.md)

## Následující lekce

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoliv usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo chybná výkladu vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->