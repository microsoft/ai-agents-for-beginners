[![Ako navrhnúť dobrých AI agentov](../../../translated_images/sk/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

# Dizajnový vzor používania nástrojov

Nástroje sú zaujímavé, pretože umožňujú AI agentom mať širší rozsah schopností. Namiesto toho, aby agent mal obmedzený súbor akcií, ktoré môže vykonať, pridaním nástroja môže agent vykonávať širokú škálu akcií. V tejto kapitole sa pozrieme na Dizajnový vzor používania nástrojov, ktorý popisuje, ako môžu AI agenti používať konkrétne nástroje na dosiahnutie svojich cieľov.

## Úvod

V tejto lekcii sa snažíme odpovedať na nasledujúce otázky:

- Čo je to dizajnový vzor používania nástrojov?
- Pre aké prípady použitia sa dá aplikovať?
- Aké prvky/stavebné bloky sú potrebné na implementáciu tohto dizajnového vzoru?
- Aké sú špeciálne úvahy pri používaní dizajnového vzoru používania nástrojov na vybudovanie dôveryhodných AI agentov?

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

- Definovať dizajnový vzor používania nástrojov a jeho účel.
- Identifikovať prípady použitia, kde je dizajnový vzor použitia nástrojov použiteľný.
- Pochopiť kľúčové prvky potrebné na implementáciu dizajnového vzoru.
- Rozoznať úvahy na zabezpečenie dôveryhodnosti AI agentov používajúcich tento dizajnový vzor.

## Čo je dizajnový vzor používania nástrojov?

**Dizajnový vzor používania nástrojov** sa zameriava na poskytnutie schopnosti LLM interagovať s externými nástrojmi na dosiahnutie konkrétnych cieľov. Nástroje sú kód, ktorý môže agent vykonať na realizáciu akcií. Nástroj môže byť jednoduchá funkcia ako kalkulačka, alebo volanie API tretej strany, napríklad vyhľadávanie cien akcií alebo predpoveď počasia. V kontexte AI agentov sú nástroje navrhnuté tak, aby ich agenti vykonávali ako reakciu na **funkčné volania generované modelom**.

## Pre aké prípady použitia sa dá aplikovať?

AI agenti môžu využiť nástroje na dokončenie komplexných úloh, získavanie informácií alebo rozhodovanie. Dizajnový vzor používania nástrojov sa často používa v scenároch vyžadujúcich dynamickú interakciu s externými systémami, ako sú databázy, webové služby alebo interpretery kódu. Táto schopnosť je užitočná pre rôzne prípady použitia, vrátane:

- **Dynamické získavanie informácií:** Agenti môžu vyhľadávať aktuálne údaje prostredníctvom externých API alebo databáz (napr. dotazovanie SQLite databázy na dátovú analýzu, získavanie cien akcií alebo informácií o počasí).
- **Vykonávanie a interpretácia kódu:** Agenti môžu spúšťať kód alebo skripty na riešenie matematických problémov, generovanie správ alebo vykonávanie simulácií.
- **Automatizácia pracovných tokov:** Automatizácia opakujúcich sa alebo viacstupňových pracovných tokov integráciou nástrojov ako plánovače úloh, e-mailové služby alebo dátové pipeline.
- **Zákaznícka podpora:** Agenti môžu interagovať so systémami CRM, ticketovacími platformami alebo databázami znalostí na riešenie používateľských otázok.
- **Generovanie a úprava obsahu:** Agenti môžu využiť nástroje ako korektory gramatiky, zhrnovače textov alebo hodnotiace nástroje bezpečnosti obsahu na pomoc pri tvorbe obsahu.

## Aké prvky/stavebné bloky sú potrebné na implementáciu dizajnového vzoru používania nástrojov?

Tieto stavebné bloky umožňujú AI agentovi vykonávať širokú škálu úloh. Pozrime sa na kľúčové prvky potrebné pre implementáciu dizajnového vzoru používania nástrojov:

- **Schémy funkcií/nástrojov**: Podrobné definície dostupných nástrojov, vrátane názvu funkcie, účelu, požadovaných parametrov a očakávaných výstupov. Tieto schémy umožňujú LLM porozumieť dostupným nástrojom a ako konštruovať platné požiadavky.

- **Logika vykonávania funkcií**: Riadi spôsob a čas vyvolania nástrojov na základe zámeru používateľa a kontextu konverzácie. Môže zahŕňať plánovacie moduly, mechanizmy smerovania alebo podmienené toky, ktoré dynamicky určujú použitie nástroja.

- **Systém spracovania správ**: Komponenty spravujúce tok konverzácie medzi vstupmi používateľa, odpoveďami LLM, volaniami nástrojov a výstupmi z nástrojov.

- **Rámec integrácie nástrojov**: Infraštruktúra, ktorá prepája agenta s rôznymi nástrojmi, či už sú to jednoduché funkcie alebo komplexné externé služby.

- **Riešenie chýb a validácia**: Mechanizmy na zvládanie zlyhaní pri vykonávaní nástrojov, validáciu parametrov a správu neočakávaných odpovedí.

- **Správa stavu**: Sleduje kontext konverzácie, predchádzajúce interakcie s nástrojmi a perzistentné údaje, aby zabezpečila konzistenciu počas viacstupňových interakcií.

Ďalej sa pozrime na Volanie funkcií/nástrojov podrobnejšie.
 
### Volanie funkcií/nástrojov

Volanie funkcií je hlavným spôsobom, ktorým umožňujeme veľkým jazykovým modelom (LLM) interagovať s nástrojmi. Často uvidíte, že „Funkcia“ a „Nástroj“ sa používajú zameniteľne, pretože „funkcie“ (bloky znovupoužiteľného kódu) sú „nástroje“, ktoré agenti používajú na vykonávanie úloh. Aby sa kód funkcie mohol vyvolať, musí LLM porovnať požiadavku používateľa so špecifikáciou funkcie. Na to sa posiela schéma obsahujúca popisy všetkých dostupných funkcií LLM. LLM potom vyberie najvhodnejšiu funkciu pre úlohu a vráti jej názov a argumenty. Vybraná funkcia je vyvolaná, jej odpoveď je zaslaná späť LLM, ktoré používa tieto informácie na odpoveď na požiadavku používateľa.

Pre vývojárov, ktorí chcú implementovať volanie funkcií pre agentov, budete potrebovať:

1. LLM model, ktorý podporuje volanie funkcií
2. Schému obsahujúcu popisy funkcií
3. Kód pre každú popísanú funkciu

Použime príklad získania aktuálneho času v meste ako ilustráciu:

1. **Inicializujte LLM, ktorý podporuje volanie funkcií:**

    Nie všetky modely podporujú volanie funkcií, preto je dôležité skontrolovať, či LLM ktorý používate, túto funkciu má.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podporuje volanie funkcií. Začneme vytvorením klienta Azure OpenAI.

    ```python
    # Inicializujte klienta Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Vytvorte schému funkcie:**

    Ďalej definujeme JSON schému, ktorá obsahuje názov funkcie, popis toho, čo funkcia robí, a názvy a popisy parametrov funkcie.
    Túto schému potom pošleme klientovi vytvorenému vyššie spolu s požiadavkou používateľa na zistenie času v San Franciscu. Dôležité je poznamenať, že sa vráti **volanie nástroja**, **nie** konečná odpoveď na otázku. Ako už bolo spomenuté, LLM vráti názov funkcie vybranej pre úlohu a argumenty, ktoré sa jej predajú.

    ```python
    # Popis funkcie pre načítanie modelu
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
  
    # Počiatočná správa používateľa
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Prvé volanie API: Požiadať model, aby použil funkciu
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Spracovať odpoveď modelu
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Kód funkcie potrebný na vykonanie úlohy:**

    Keď si LLM vyberie, ktorá funkcia sa musí spustiť, je potrebné implementovať a vykonať kód, ktorý úlohu zvládne.
    Môžeme implementovať kód na získanie aktuálneho času v Pythone. Tiež budeme musieť napísať kód na extrakciu názvu a argumentov z response_message, aby sme získali konečný výsledok.

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
     # Spracujte volania funkcií
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
  
      # Druhé volanie API: Získajte konečnú odpoveď od modelu
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

Volanie funkcií je jadrom väčšiny, ak nie všetkých dizajnových vzorov používania nástrojov agentov, avšak jeho implementácia od základov môže byť občas náročná.
Ako sme sa naučili v [Lekcii 2](../../../02-explore-agentic-frameworks), agentové rámce nám poskytujú predpripravené stavebné bloky pre implementáciu používania nástrojov.
 
## Príklady používania nástrojov s agentovými rámcami

Tu sú niektoré príklady, ako môžete implementovať dizajnový vzor používania nástrojov pomocou rôznych agentových rámcov:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> je open-source AI rámec pre .NET, Python a Java vývojárov pracujúcich s veľkými jazykovými modelmi (LLM). Zjednodušuje proces používania volania funkcií automatickým popisovaním vašich funkcií a ich parametrov modelu cez proces nazývaný <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializácia</a>. Tiež rieši komunikáciu tam a späť medzi modelom a vašim kódom. Ďalšou výhodou použitia agentového rámca ako Semantic Kernel je, že umožňuje prístup k predpripraveným nástrojom ako <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Vyhľadávanie súborov</a> a <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Interpret kódu</a>.

Nasledujúci diagram znázorňuje proces volania funkcií so Semantic Kernel:

![volanie funkcie](../../../translated_images/sk/functioncalling-diagram.a84006fc287f6014.webp)

V Semantic Kernel sa funkcie/nástroje nazývajú <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Pluginy</a>. Môžeme previesť funkciu `get_current_time`, ktorú sme videli vyššie, na plugin tým, že ju premeníme na triedu s touto funkciou v nej. Môžeme tiež importovať dekorátor `kernel_function`, ktorý prijíma popis funkcie. Keď potom vytvoríte kernel s GetCurrentTimePlugin, kernel automaticky serializuje funkciu a jej parametre, čím vytvorí schému, ktorá sa pošle LLM.

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

# Vytvorte jadro
kernel = Kernel()

# Vytvorte doplnok
get_current_time_plugin = GetCurrentTimePlugin(location)

# Pridajte doplnok do jadra
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> je novší agentový rámec navrhnutý tak, aby umožnil vývojárom bezpečne vytvárať, nasadzovať a škálovať kvalitných a rozšíriteľných AI agentov bez potreby spravovať základné výpočtové a úložné zdroje. Je obzvlášť užitočný pre podnikové aplikácie, keďže je to plne spravovaná služba s podnikovej úrovne bezpečnosťou.

V porovnaní s priamym vývojom cez LLM API poskytuje Azure AI Agent Service niektoré výhody, vrátane:

- Automatické volanie nástrojov – nie je potrebné analyzovať volanie nástroja, vyvolať ho a spracovať odpoveď; všetko sa deje na strane servera
- Bezpečne spravované údaje – namiesto správy vlastného stavu konverzácie je možné sa spoľahnúť na vlákna, ktoré uchovávajú všetky potrebné informácie
- Nástroje pripravené na použitie – nástroje, ktoré môžete využiť na interakciu s vašimi zdrojmi dát, ako Bing, Azure AI Search a Azure Functions.

Nástroje dostupné v Azure AI Agent Service možno rozdeliť do dvoch kategórií:

1. Nástroje pre vedomosti:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Prepojenie s vyhľadávaním Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Vyhľadávanie súborov</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Nástroje pre akcie:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Volanie funkcií</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpret kódu</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Nástroje definované OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nám umožňuje používať tieto nástroje spoločne ako `toolset`. Tiež využíva `vlákna`, ktoré sledujú históriu správ z konkrétnej konverzácie.

Predstavte si, že ste predajný agent v spoločnosti Contoso. Chcete vyvinúť konverzačného agenta, ktorý dokáže odpovedať na otázky týkajúce sa vašich predajných údajov.

Nasledujúci obrázok ilustruje, ako by ste mohli využiť Azure AI Agent Service na analýzu predajných údajov:

![Agentická služba v akcii](../../../translated_images/sk/agent-service-in-action.34fb465c9a84659e.webp)

Na použitie ktoréhokoľvek z týchto nástrojov so službou môžeme vytvoriť klienta a definovať nástroj alebo sadu nástrojov. Na praktickú implementáciu môžeme použiť nasledujúci Python kód. LLM bude schopný pozrieť sa na toolset a rozhodnúť, či použije používateľom vytvorenú funkciu `fetch_sales_data_using_sqlite_query`, alebo predpripravený Interpret kódu podľa požiadavky používateľa.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # funkcia fetch_sales_data_using_sqlite_query, ktorá sa nachádza v súbore fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inicializovať súpravu nástrojov
toolset = ToolSet()

# Inicializovať agenta na volanie funkcií s funkciou fetch_sales_data_using_sqlite_query a pridať ju do súpravy nástrojov
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializovať nástroj Code Interpreter a pridať ho do súpravy nástrojov.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Aké sú špeciálne úvahy pri používaní dizajnového vzoru používania nástrojov na budovanie dôveryhodných AI agentov?

Bežnou obavou pri dynamicky generovanom SQL prostredníctvom LLM je bezpečnosť, najmä riziko SQL injekcie alebo škodlivých akcií, ako napríklad vymazanie alebo poškodenie databázy. Hoci sú tieto obavy oprávnené, dajú sa účinne zmierniť správnou konfiguráciou prístupových oprávnení k databáze. Pre väčšinu databáz to znamená nastavenie databázy ako len na čítanie. Pre databázové služby ako PostgreSQL alebo Azure SQL by mala aplikácia dostať rolu s prístupom len na čítanie (SELECT).
Spustenie aplikácie v zabezpečenom prostredí ďalej zvyšuje ochranu. V podnikových scenároch sa údaje zvyčajne extrahujú a transformujú z prevádzkových systémov do databázy iba na čítanie alebo dátového skladu s používateľsky prívetivým schématom. Tento prístup zabezpečuje, že dáta sú chránené, optimalizované pre výkon a dostupnosť, a že aplikácia má obmedzený prístup iba na čítanie.

## Ukážkové kódy

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Máte ďalšie otázky o používateľských dizajnových vzoroch nástroja?

Pridajte sa k [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kde sa môžete stretnúť s ostatnými študentmi, zúčastniť sa úradných hodín a získať odpovede na vaše otázky týkajúce sa AI Agentov.

## Dodatočné zdroje

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Návod na volanie funkcií Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Nástroje</a>

## Predchádzajúca lekcia

[Porozumenie agénskym dizajnovým vzorom](../03-agentic-design-patterns/README.md)

## Nasledujúca lekcia

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->