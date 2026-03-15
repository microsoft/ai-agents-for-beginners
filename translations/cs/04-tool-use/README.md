[![Jak navrhnout dobré AI agenty](../../../translated_images/cs/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klikněte na obrázek výše pro zobrazení videa této lekce)_

# Vzorec návrhu využití nástrojů

Nástroje jsou zajímavé, protože umožňují AI agentům mít širší škálu schopností. Místo toho, aby agent měl omezenou sadu akcí, které může provádět, přidáním nástroje může agent nyní vykonávat širokou škálu akcí. V této kapitole si prohlédneme vzorec návrhu využití nástrojů, který popisuje, jak AI agenti mohou používat specifické nástroje k dosažení svých cílů.

## Úvod

V této lekci se pokusíme odpovědět na následující otázky:

- Co je vzorec návrhu využití nástrojů?
- Pro jaké případy použití lze tento vzorec aplikovat?
- Jaké prvky/stavební bloky jsou potřeba k implementaci vzorce návrhu?
- Jaká jsou zvláštní opatření pro použití vzorce návrhu využití nástrojů pro budování důvěryhodných AI agentů?

## Výukové cíle

Po dokončení této lekce budete schopni:

- Definovat vzorec návrhu využití nástrojů a jeho účel.
- Identifikovat případy použití, kde je vzorec využití nástrojů aplikovatelný.
- Pochopit klíčové prvky potřebné k implementaci vzorce návrhu.
- Rozpoznat úvahy pro zajištění důvěryhodnosti AI agentů využívajících tento vzorec návrhu.

## Co je vzorec návrhu využití nástrojů?

**Vzorec návrhu využití nástrojů** se zaměřuje na to, aby LLM (velké jazykové modely) měly schopnost interagovat s externími nástroji k dosažení specifických cílů. Nástroje jsou kód, který může agent spustit, aby provedl akce. Nástroj může být jednoduchá funkce, například kalkulačka, nebo volání API na službu třetí strany, jako je vyhledání ceny akcií nebo předpověď počasí. V kontextu AI agentů jsou nástroje navrženy tak, aby byly spouštěny agenty jako odpověď na **funkční volání generovaná modelem**.

## Pro jaké případy použití lze tento vzorec aplikovat?

AI agenti mohou využívat nástroje k dokončení složitých úkolů, získávání informací nebo přijímání rozhodnutí. Vzorec využití nástrojů se často používá v situacích vyžadujících dynamickou interakci s externími systémy, jako jsou databáze, webové služby nebo interpretory kódu. Tato schopnost je užitečná pro řadu různých případů použití včetně:

- **Dynamické získávání informací:** Agenti mohou dotazovat externí API nebo databáze pro získání aktuálních dat (například dotazování SQLite databáze pro analýzu dat, získávání cen akcií nebo informací o počasí).
- **Spouštění a interpretace kódu:** Agenti mohou spouštět kód nebo skripty pro řešení matematických problémů, generování reportů nebo provádění simulací.
- **Automatizace pracovních toků:** Automatizace opakujících se nebo vícestupňových pracovních procesů integrací nástrojů jako plánovačů úkolů, e-mailových služeb nebo datových proudů.
- **Zákaznická podpora:** Agenti mohou interagovat s CRM systémy, platformami pro správu tiketů nebo znalostními databázemi pro vyřešení uživatelských dotazů.
- **Generování a úprava obsahu:** Agenti mohou využívat nástroje jako kontrolory gramatiky, souhrn textu nebo hodnotitele bezpečnosti obsahu pro podporu tvůrčích úkolů.

## Jaké prvky/stavební bloky jsou potřeba k implementaci vzorce návrhu využití nástrojů?

Tyto stavební bloky umožňují AI agentovi provádět širokou škálu úkolů. Pojďme se podívat na klíčové prvky potřebné k implementaci vzorce návrhu využití nástrojů:

- **Schémata funkcí/nástrojů**: Podrobné definice dostupných nástrojů, včetně názvu funkce, účelu, požadovaných parametrů a očekávaných výstupů. Tato schémata umožňují LLM pochopit, jaké nástroje jsou dostupné a jak sestavit platné požadavky.

- **Logika spouštění funkcí**: Řídí, jak a kdy jsou nástroje vyvolávány na základě záměru uživatele a kontextu konverzace. Může zahrnovat plánovací moduly, směrovací mechanismy nebo podmíněné toky, které dynamicky určují použití nástroje.

- **Systém zpracování zpráv**: Komponenty, které spravují tok konverzace mezi uživatelskými vstupy, odpověďmi LLM, voláním nástrojů a výstupy nástrojů.

- **Rámec integrace nástrojů**: Infrastruktura, která propojuje agenta s různými nástroji, ať už jde o jednoduché funkce nebo složité externí služby.

- **Zpracování chyb a validace**: Mechanismy pro řešení selhání při spouštění nástrojů, ověřování parametrů a správu neočekávaných odpovědí.

- **Správa stavu**: Sleduje kontext konverzace, předchozí interakce s nástroji a perzistentní data pro zajištění konzistence napříč víceturnovými interakcemi.

Nyní si podrobněji prohlédneme funkční volání.

### Funkční/volání nástrojů

Volání funkcí je primární způsob, jak umožnit velkým jazykovým modelům (LLM) interakci s nástroji. Často uvidíte, že "funkce" a "nástroj" se používají zaměnitelně, protože "funkce" (bloky znovupoužitelného kódu) jsou "nástroje", které agenti používají k provádění úkolů. Aby mohl být kód funkce vyvolán, musí LLM porovnat požadavek uživatele s popisem funkce. K tomu se LLM posílá schéma obsahující popisy všech dostupných funkcí. LLM pak vybere nejvhodnější funkci pro daný úkol a vrátí její název a argumenty. Vybraná funkce je spuštěna, její odpověď je zaslána zpět LLM, které využije informace k odpovědi na požadavek uživatele.

Pro vývojáře, kteří chtějí implementovat volání funkcí pro agenty, je potřeba:

1. LLM model, který podporuje volání funkcí
2. Schéma obsahující popisy funkcí
3. Kód pro každou popsanou funkci

Jako příklad použijme získání aktuálního času ve městě:

1. **Inicializujte LLM, který podporuje volání funkcí:**

    Ne všechny modely podporují volání funkcí, proto je důležité ověřit, zda váš LLM tuto funkci má. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> volání funkcí podporuje. Můžeme začít inicializací klienta Azure OpenAI.

    ```python
    # Inicializujte klienta Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Vytvořte schéma funkce**:

    Následně definujeme JSON schéma obsahující název funkce, popis toho, co funkce dělá, a názvy a popisy parametrů funkce.
    Toto schéma pak předáme dříve vytvořenému klientu spolu s uživatelským požadavkem na zjištění času v San Franciscu. Důležité je poznamenat, že se vrací **volání nástroje**, **nikoli** konečná odpověď na otázku. Jak již bylo zmíněno, LLM vrací název funkce, kterou vybral pro úkol, a argumenty předávané této funkci.

    ```python
    # Popis funkce pro model k přečtení
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
  
    # Počáteční uživatelská zpráva
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # První volání API: Požádej model, aby použil funkci
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Zpracuj odpověď modelu
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Kód funkce potřebný k vykonání úkolu:**

    Nyní, když LLM vybralo, která funkce má být spuštěna, je potřeba implementovat a spustit kód, který úkol provede.
    Můžeme implementovat kód pro získání aktuálního času v Pythonu. Rovněž bude potřeba napsat kód pro získání názvu a argumentů z response_message pro získání konečného výsledku.

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
  
      # Druhý API požadavek: Získat konečnou odpověď od modelu
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

Volání funkcí je jádrem většiny, ne-li všech, návrhů využití nástrojů agentů, implementace však může být někdy náročná.
Jak jsme se dozvěděli v [Lekci 2](../../../02-explore-agentic-frameworks), agentní frameworky nám poskytují předpřipravené stavební bloky pro implementaci využití nástrojů.
 
## Příklady využití nástrojů s agentními frameworky

Zde jsou některé příklady, jak můžete implementovat vzorec návrhu využití nástrojů pomocí různých agentních frameworků:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> je open-source AI framework pro tvorbu AI agentů. Zjednodušuje proces využití volání funkcí tím, že umožňuje definovat nástroje jako Python funkce s dekorátorem `@tool`. Framework zajišťuje komunikaci mezi modelem a vaším kódem. Také poskytuje přístup k předpřipraveným nástrojům, jako jsou File Search a Code Interpreter přes `AzureAIProjectAgentProvider`.

Následující diagram znázorňuje proces volání funkcí v Microsoft Agent Framework:

![function calling](../../../translated_images/cs/functioncalling-diagram.a84006fc287f6014.webp)

V Microsoft Agent Framework jsou nástroje definovány jako dekorované funkce. Můžeme převést funkci `get_current_time`, kterou jsme viděli dříve, na nástroj pomocí dekorátoru `@tool`. Framework automaticky serializuje funkci a její parametry a vytvoří schéma k odeslání LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Vytvořte klienta
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Vytvořte agenta a spusťte ho s nástrojem
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> je novější agentní framework navržený tak, aby umožnil vývojářům bezpečně vytvářet, nasazovat a škálovat vysoce kvalitní a rozšiřitelné AI agenty bez nutnosti spravovat základní výpočetní a úložné zdroje. Je obzvláště užitečný pro podnikovou sféru, protože jde o plně spravovanou službu s bezpečností na podnikové úrovni.

Ve srovnání s vývojem přímo pomocí LLM API přináší Azure AI Agent Service některé výhody, včetně:

- Automatické volání nástrojů – není třeba analyzovat volání nástroje, spouštět nástroj a zpracovávat odpověď; vše je nyní řešeno na straně serveru
- Bezpečně spravovaná data – místo správy vlastní historie konverzace můžete spoléhat na vlákna (threads), která uchovávají všechny potřebné informace
- Nástroje připravené k použití – nástroje pro interakci s datovými zdroji, jako jsou Bing, Azure AI Search a Azure Functions.

Nástroje dostupné v Azure AI Agent Service lze rozdělit do dvou kategorií:

1. Nástroje pro znalosti:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Propojení s Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Nástroje pro akce:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Volání funkcí</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Nástroje definované OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nám umožňuje používat tyto nástroje společně jako `nástroje` (toolset). Také využívá `vlákna` (threads), která sledují historii zpráv z konkrétní konverzace.

Představte si, že jste obchodní agent ve firmě Contoso. Chcete vyvinout konverzační agenta, který dokáže odpovídat na otázky týkající se vašich prodejních dat.

Následující obrázek ukazuje, jak můžete Azure AI Agent Service využít k analýze vašich prodejních dat:

![Agentic Service In Action](../../../translated_images/cs/agent-service-in-action.34fb465c9a84659e.webp)

Pro použití jakéhokoliv z těchto nástrojů se službou můžeme vytvořit klienta a definovat nástroj nebo sadu nástrojů. Praktická implementace může vypadat následovně v Pythonu. LLM bude moci nahlédnout do sady nástrojů a rozhodnout, zda použije uživatelem vytvořenou funkci `fetch_sales_data_using_sqlite_query`, nebo předem připravený Code Interpreter v závislosti na požadavku uživatele.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # funkce fetch_sales_data_using_sqlite_query, která se nachází v souboru fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inicializovat sadu nástrojů
toolset = ToolSet()

# Inicializovat agenta volání funkcí s funkcí fetch_sales_data_using_sqlite_query a přidat ji do sady nástrojů
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializovat nástroj Code Interpreter a přidat jej do sady nástrojů.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Jaká jsou zvláštní opatření pro použití vzorce návrhu využití nástrojů při budování důvěryhodných AI agentů?

Častou obavou u dynamicky generovaného SQL pomocí LLM je bezpečnost, zejména riziko SQL injection nebo škodlivých akcí, například odstranění nebo poškození databáze. Tyto obavy jsou oprávněné, avšak lze je efektivně zmírnit správnou konfigurací přístupových oprávnění k databázi. U většiny databází to znamená konfiguraci databáze jako jen pro čtení. U databázových služeb jako PostgreSQL nebo Azure SQL by měla být aplikaci přiřazena role pouze pro čtení (SELECT).

Provozování aplikace v bezpečném prostředí dále zvyšuje ochranu. V podnikových scénářích jsou data obvykle extrahována a transformována z provozních systémů do databáze nebo datového skladu pouze pro čtení s uživatelsky přívětivým schématem. Tento přístup zajišťuje, že data jsou bezpečná, optimalizovaná pro výkon a přístupnost, a že aplikace má omezený, pouze čtecí přístup.

## Ukázkové kódy

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Máte další otázky ohledně vzorce návrhu využití nástrojů?

Připojte se k [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kde můžete potkat další studenty, zúčastnit se konzultací a získat odpovědi na vaše otázky týkající se AI agentů.

## Další zdroje

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Workshop Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Přehled Microsoft Agent Framework</a>

## Předchozí lekce

[Porozumění agentním vzorcům návrhu](../03-agentic-design-patterns/README.md)

## Další lekce
[Agentní RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí automatické překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědni za jakékoliv nedorozumění nebo chybné výklady vyplývající z užití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->