[![Jak navrhnout dobré AI agenty](../../../translated_images/cs/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klikněte na obrázek výše pro zobrazení videa této lekce)_

# Návrhový vzor použití nástrojů

Nástroje jsou zajímavé, protože umožňují AI agentům mít širší škálu schopností. Místo toho, aby agent měl omezenou sadu akcí, které může provádět, může nyní agent pomocí přidání nástroje vykonávat širokou škálu činností. V této kapitole se podíváme na návrhový vzor použití nástrojů, který popisuje, jak mohou AI agenti využívat konkrétní nástroje k dosažení svých cílů.

## Úvod

V této lekci se zaměříme na zodpovězení následujících otázek:

- Co je návrhový vzor použití nástrojů?
- Na jaké případy použití lze tento vzor aplikovat?
- Jaké jsou prvky/stavební kameny potřebné k implementaci návrhového vzoru?
- Jaká jsou zvláštní opatření při použití návrhového vzoru použití nástrojů k vytváření důvěryhodných AI agentů?

## Výukové cíle

Po dokončení této lekce budete schopni:

- Definovat návrhový vzor použití nástrojů a jeho účel.
- Identifikovat případy použití, kde je návrhový vzor použití nástrojů aplikovatelný.
- Pochopit klíčové prvky potřebné k implementaci návrhového vzoru.
- Rozpoznat úvahy pro zajištění důvěryhodnosti AI agentů používajících tento návrhový vzor.

## Co je návrhový vzor použití nástrojů?

**Návrhový vzor použití nástrojů** se zaměřuje na poskytnutí schopnosti LLM interagovat s externími nástroji za účelem dosažení konkrétních cílů. Nástroje jsou kód, který může agent spustit k provedení akcí. Nástroj může být jednoduchá funkce, například kalkulačka, nebo volání API ke službě třetí strany, například vyhledávání ceny akcií nebo předpověď počasí. V kontextu AI agentů jsou nástroje navrženy tak, aby byly spouštěny agenty v reakci na **funkční volání generovaná modelem**.

## Na jaké případy použití lze tento vzor aplikovat?

AI agenti mohou využívat nástroje k dokončení složitých úkolů, získávání informací nebo přijímání rozhodnutí. Návrhový vzor použití nástrojů se často používá v scénářích vyžadujících dynamickou interakci s externími systémy, jako jsou databáze, webové služby nebo interprety kódu. Tato schopnost je užitečná pro řadu různých případů použití, včetně:

- **Dynamické získávání informací:** Agenti mohou dotazovat externí API nebo databáze pro získání aktuálních dat (např. dotazování SQLite databáze pro analýzu dat, získání cen akcií nebo informací o počasí).
- **Spouštění a interpretace kódu:** Agenti mohou vykonávat kód nebo skripty pro řešení matematických problémů, generování zpráv nebo simulací.
- **Automatizace pracovních postupů:** Automatizace opakujících se nebo vícestupňových úloh integrací nástrojů, jako jsou plánovače úkolů, e-mailové služby nebo datové toky.
- **Zákaznická podpora:** Agenti mohou komunikovat se systémy CRM, platformami pro správu tiketů nebo znalostními databázemi k řešení uživatelských dotazů.
- **Generování a úprava obsahu:** Agenti mohou využívat nástroje jako kontrolu gramatiky, shrnovače textu nebo hodnotitele bezpečnosti obsahu pro asistenci při tvorbě obsahu.

## Jaké jsou prvky/stavební kameny potřebné k implementaci návrhového vzoru použití nástrojů?

Tyto stavební kameny umožňují AI agentovi vykonávat širokou škálu úkolů. Podívejme se na klíčové prvky potřebné k implementaci návrhového vzoru použití nástrojů:

- **Schémata funkcí/nástrojů:** Podrobné definice dostupných nástrojů, zahrnující název funkce, účel, požadované parametry a očekávané výstupy. Tato schémata umožňují LLM porozumět dostupným nástrojům a jak správně sestavit platné požadavky.

- **Logika spouštění funkcí:** Řídí, jak a kdy jsou nástroje volány na základě uživatelova záměru a kontextu konverzace. Může zahrnovat plánovací moduly, směrovací mechanizmy nebo podmíněné toky určující dynamické používání nástrojů.

- **Systém zpracování zpráv:** Komponenty, které spravují tok konverzace mezi vstupy uživatele, odpověďmi LLM, voláními nástrojů a výstupy nástrojů.

- **Rámec integrace nástrojů:** Infrastruktura, která propojuje agenta s různými nástroji, ať už jsou to jednoduché funkce nebo složité externí služby.

- **Zpracování chyb a validace:** Mechanismy pro zvládání selhání při spouštění nástrojů, ověřování parametrů a řízení neočekávaných odpovědí.

- **Správa stavu:** Sleduje kontext konverzace, předchozí interakce s nástroji a perzistentní data, aby zajistila konzistenci v průběhu vícekrokových interakcí.

Dále se podíváme podrobněji na Funkční volání.

### Funkční/Volání nástrojů

Volání funkcí je primární způsob, jak umožňujeme rozsáhlým jazykovým modelům (LLM) interakci s nástroji. Často uvidíte, že 'Funkce' a 'Nástroj' jsou použity zaměnitelně, protože 'funkce' (bloky znovupoužitelného kódu) jsou 'nástroje', které agenti používají k vykonávání úkolů. Aby mohl být kód funkce spuštěn, musí LLM porovnat požadavek uživatele s popisem funkcí. Za tímto účelem je do LLM zasláno schéma obsahující popisy všech dostupných funkcí. LLM pak vybere nejvhodnější funkci pro daný úkol a vrátí její název a argumenty. Vybraná funkce je spuštěna, její odpověď je zaslána zpět do LLM, který využije informace k odpovědi na uživatelův požadavek.

Pro vývojáře, kteří chtějí implementovat funkční volání pro agenty, budete potřebovat:

1. LLM model podporující funkční volání
2. Schéma obsahující popisy funkcí
3. Kód pro každou popsanou funkci

Použijme příklad získání aktuálního času ve městě:

1. **Inicializujte LLM podporující funkční volání:**

    Ne všechny modely podporují funkční volání, proto je důležité ověřit, že používaný LLM to podporuje. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> funkční volání podporuje. Můžeme začít inicializací klienta Azure OpenAI.

    ```python
    # Inicializovat klienta Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Vytvořte funkční schéma:**

    Následně definujeme JSON schéma, které obsahuje název funkce, popis, co funkce dělá, a názvy a popisy parametrů funkce.
    Toto schéma pak předáme klientovi, vytvořenému výše, spolu s uživatelovým požadavkem na čas v San Franciscu. Důležité je poznamenat, že je vráceno **volání nástroje**, **nikoli** konečná odpověď na otázku. Jak bylo zmíněno, LLM vrací název zvolené funkce a argumenty, které jí budou předány.

    ```python
    # Popis funkce pro načtení modelu
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
  
1. **Kód funkce potřebný k vykonání úkolu:**

    Jakmile LLM vybere, která funkce má být spuštěna, musí být kód funkce implementován a vykonán.
    Kód získání aktuálního času můžeme implementovat v Pythonu. Také musíme napsat kód na extrakci názvu a argumentů z response_message, abychom získali konečný výsledek.

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

Volání funkcí je jádrem většiny, ne-li všech návrhových vzorů použití nástrojů agentů, avšak jeho implementace od základů může být někdy náročná.
Jak jsme se naučili v [Lekci 2](../../../02-explore-agentic-frameworks), agentní rámce nám poskytují předpřipravené stavební kameny pro implementaci použití nástrojů.
 
## Příklady použití nástrojů s agentními rámci

Zde jsou některé příklady, jak můžete implementovat návrhový vzor použití nástrojů pomocí různých agentních rámců:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> je open-source AI rámec pro vytváření AI agentů. Zjednodušuje proces používání funkčního volání tím, že umožňuje definovat nástroje jako Python funkce s dekorátorem `@tool`. Rámec zajišťuje zpětnou komunikaci mezi modelem a vaším kódem. Také poskytuje přístup k předpřipraveným nástrojům jako je vyhledávání souborů a interpretr kódu prostřednictvím `AzureAIProjectAgentProvider`.

Následující diagram znázorňuje proces funkčního volání s Microsoft Agent Framework:

![volání funkcí](../../../translated_images/cs/functioncalling-diagram.a84006fc287f6014.webp)

V Microsoft Agent Framework jsou nástroje definovány jako dekorované funkce. Můžeme převést funkci `get_current_time`, kterou jsme viděli dříve, na nástroj použitím dekorátoru `@tool`. Rámec automaticky serializuje funkci a její parametry, vytváří schéma k odeslání do LLM.

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

# Vytvořte agenta a spusťte nástroj
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> je novější agentní rámec navržený tak, aby vývojářům umožnil bezpečně vytvářet, nasazovat a škálovat kvalitní a rozšiřitelné AI agenty bez nutnosti správy základních výpočetních a úložných zdrojů. Je obzvlášť užitečný pro podnikové aplikace, protože je to plně spravovaná služba s podnikové úrovně zabezpečením.

Ve srovnání s přímým vývojem pomocí API LLM poskytuje Azure AI Agent Service několik výhod, včetně:

- Automatické volání nástrojů – není třeba analyzovat volání nástroje, spouštět nástroj a zpracovávat odpověď; vše se nyní děje na straně serveru
- Bezpečně spravovaná data – místo správy vlastního stavu konverzace můžete spoléhat na vlákna, která uchovávají všechny potřebné informace
- Nástroje připravené k použití – nástroje, které můžete použít k interakci se zdroji dat, jako Bing, Azure AI Search a Azure Functions.

Nástroje dostupné v Azure AI Agent Service lze rozdělit do dvou kategorií:

1. Nástroje znalostí:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Vazba na Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Vyhledávání souborů</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Nástroje akcí:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Volání funkcí</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpretr kódu</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Nástroje definované pomocí OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nám umožňuje používat tyto nástroje společně jako `toolset`. Také využívá `vlákna`, která sledují historii zpráv z konkrétní konverzace.

Představte si, že jste obchodním zástupcem ve firmě nazvané Contoso. Chcete vyvinout konverzačního agenta, který dokáže odpovídat na dotazy týkající se vašich prodejních dat.

Následující obrázek znázorňuje, jak byste mohli použít Azure AI Agent Service k analýze vašich prodejních dat:

![Agentní služba v akci](../../../translated_images/cs/agent-service-in-action.34fb465c9a84659e.webp)

Chcete-li použít některý z těchto nástrojů se službou, můžeme vytvořit klienta a definovat nástroj nebo sadu nástrojů. Pro praktickou implementaci můžeme použít následující Python kód. LLM bude moci nahlédnout do sady nástrojů a rozhodnout, zda použít uživatelem vytvořenou funkci `fetch_sales_data_using_sqlite_query` nebo předpřipravený Interpretr kódu podle uživatelského požadavku.

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

# Inicializovat agenta volajícího funkce s funkcí fetch_sales_data_using_sqlite_query a přidat ji do sady nástrojů
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializovat nástroj Code Interpreter a přidat jej do sady nástrojů.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Jaká jsou zvláštní opatření při použití návrhového vzoru použití nástrojů k vytváření důvěryhodných AI agentů?

Běžným problémem u SQL dynamicky generovaného LLM je bezpečnost, zejména riziko SQL injekce nebo škodlivých akcí, jako je mazání nebo manipulace s databází. Přestože jsou tyto obavy oprávněné, lze je efektivně zmírnit správnou konfigurací přístupových oprávnění k databázi. U většiny databází to znamená nakonfigurovat databázi jako pouze pro čtení. U databázových služeb jako PostgreSQL nebo Azure SQL by aplikace měla mít přiřazenou roli pouze pro čtení (SELECT).

Provoz aplikace v zabezpečeném prostředí dále zvyšuje ochranu. V podnikovém prostředí jsou data obvykle extrahována a transformována z provozních systémů do databáze s přístupem pouze pro čtení nebo do datového skladu s uživatelsky přívětivým schématem. Tento přístup zajišťuje, že data jsou bezpečná, optimalizovaná pro výkon a přístupnost a že aplikace má omezený přístup pouze pro čtení.

## Ukázkové kódy

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Máte další otázky ohledně návrhových vzorů použití nástrojů?

Připojte se k [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kde můžete setkat další studenty, zúčastnit se konzultačních hodin a získat odpovědi na otázky týkající se AI agentů.

## Další zdroje

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Přehled Microsoft Agent Framework</a>

## Předchozí lekce

[Porozumění agentním návrhovým vzorům](../03-agentic-design-patterns/README.md)

## Následující lekce
[Agentní RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->