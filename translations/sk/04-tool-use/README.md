[![Ako navrhnúť dobrých AI agentov](../../../translated_images/sk/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

# Dizajnový vzor používania nástrojov

Nástroje sú zaujímavé, pretože umožňujú AI agentom mať širší rozsah schopností. Namiesto toho, aby agent mal obmedzenú sadu akcií, ktoré môže vykonať, pridaním nástroja môže agent teraz vykonávať širokú škálu akcií. V tejto kapitole sa pozrieme na dizajnový vzor používania nástrojov, ktorý popisuje, ako môžu AI agenti používať špecifické nástroje na dosiahnutie svojich cieľov.

## Úvod

V tejto lekcii sa pokúsime odpovedať na nasledujúce otázky:

- Čo je dizajnový vzor používania nástrojov?
- Pre aké prípady použitia sa dá použiť?
- Aké prvky/stavebné bloky sú potrebné na implementáciu dizajnového vzoru?
- Aké sú špeciálne úvahy pri používaní dizajnového vzoru používania nástrojov na budovanie dôveryhodných AI agentov?

## Ciele učenia

Po dokončení tejto lekcie budete schopní:

- Definovať dizajnový vzor používania nástrojov a jeho účel.
- Identifikovať prípady použitia, kde je dizajnový vzor použitia nástrojov vhodný.
- Pochopiť kľúčové prvky potrebné na implementáciu dizajnového vzoru.
- Rozpoznať úvahy na zabezpečenie dôveryhodnosti AI agentov používajúcich tento dizajnový vzor.

## Čo je dizajnový vzor používania nástrojov?

**Dizajnový vzor používania nástrojov** sa zameriava na umožnenie LLM interakcie s externými nástrojmi na dosiahnutie konkrétnych cieľov. Nástroje sú kód, ktorý môže agent vykonať na vykonanie akcií. Nástroj môže byť jednoduchá funkcia, ako napríklad kalkulačka, alebo volanie API tretích strán, napríklad na vyhľadanie ceny akcií alebo predpovede počasia. V kontexte AI agentov sú nástroje navrhnuté tak, aby ich agenti vykonávali ako odpoveď na **funkčné volania generované modelom**.

## Pre aké prípady použitia sa dá použiť?

AI agenti môžu využiť nástroje na dokončenie zložitých úloh, získavanie informácií alebo prijímanie rozhodnutí. Dizajnový vzor používania nástrojov sa často používa v scenároch, ktoré vyžadujú dynamickú interakciu s externými systémami, ako sú databázy, webové služby alebo interpretery kódu. Táto schopnosť je užitočná pre rôzne prípady použitia vrátane:

- **Dynamické získavanie informácií:** Agenti môžu dotazovať externé API alebo databázy na získanie aktuálnych údajov (napr. dotazovanie sa na SQLite databázu pre dátovú analýzu, získavanie cien akcií alebo informácií o počasí).
- **Vykonávanie a interpretácia kódu:** Agenti môžu vykonávať kód alebo skripty na riešenie matematických problémov, generovanie správ alebo vykonávanie simulácií.
- **Automatizácia pracovných tokov:** Automatizovanie opakujúcich sa alebo viacstupňových pracovných postupov integráciou nástrojov ako plánovače úloh, emailové služby alebo dátové pipeline.
- **Zákaznícka podpora:** Agenti môžu komunikovať so CRM systémami, ticketingovými platformami alebo znalosnými databázami na riešenie používateľských otázok.
- **Generovanie a úprava obsahu:** Agenti môžu využiť nástroje ako kontrola gramatiky, sumarizácia textu alebo hodnotenie bezpečnosti obsahu na asistenciu pri tvorbe obsahu.

## Aké sú prvky/stavebné bloky potrebné na implementáciu dizajnového vzoru používania nástrojov?

Tieto stavebné bloky umožňujú AI agentovi vykonávať širokú škálu úloh. Pozrime sa na kľúčové prvky potrebné na implementáciu dizajnového vzoru používania nástrojov:

- **Schémy funkcií/nástrojov:** Podrobné definície dostupných nástrojov, vrátane názvu funkcie, účelu, požadovaných parametrov a očakávaných výstupov. Tieto schémy umožňujú LLM pochopiť, aké nástroje sú dostupné a ako zostaviť platné požiadavky.

- **Logika vykonávania funkcií:** Riadi, ako a kedy sa nástroje vyvolávajú na základe zámeru používateľa a kontextu rozhovoru. Môže zahŕňať plánovacie moduly, mechanizmy smerovania alebo podmienené toky, ktoré dynamicky určujú použitie nástroja.

- **Systém správy správ:** Komponenty, ktoré riadia tok konverzácie medzi vstupmi používateľov, odpoveďami LLM, volaniami nástrojov a výstupmi nástrojov.

- **Rámec pre integráciu nástrojov:** Infraštruktúra, ktorá pripája agenta k rôznym nástrojom, či už sú to jednoduché funkcie alebo komplexné externé služby.

- **Spracovanie chýb a validácia:** Mechanizmy na riešenie zlyhaní pri vykonávaní nástrojov, validáciu parametrov a správu neočakávaných odpovedí.

- **Správa stavu:** Sleduje kontext konverzácie, predchádzajúce interakcie s nástrojmi a perzistentné údaje, aby sa zabezpečila konzistencia pri viackolových interakciách.

Ďalej sa pozrieme podrobnejšie na volanie funkcií/nástrojov.

### Volanie funkcií/nástrojov

Volanie funkcií je primárny spôsob, ako umožniť veľkým jazykovým modelom (LLM) interakciu s nástrojmi. Často uvidíte, že „funkcia“ a „nástroj“ sa používajú zameniteľne, pretože „funkcie“ (bloky znovu použiteľného kódu) sú „nástroje“, ktoré agenti používajú na vykonávanie úloh. Aby mohla byť funkcia vyvolaná, LLM musí porovnať požiadavku používateľa s popisom funkcie. Na to sa posiela schéma obsahujúca popisy všetkých dostupných funkcií do LLM. LLM potom vyberie najvhodnejšiu funkciu pre úlohu a vráti jej názov a argumenty. Vybraná funkcia sa vyvolá, jej odpoveď sa pošle späť do LLM, ktorý použije tieto informácie na odpoveď na požiadavku používateľa.

Pre implementáciu volania funkcií pre agentov budete potrebovať:

1. LLM model, ktorý podporuje volanie funkcií
2. Schému obsahujúcu popisy funkcií
3. Kód pre každú opísanú funkciu

Použime príklad získania aktuálneho času v meste ako ilustráciu:

1. **Inicializujte LLM, ktorý podporuje volanie funkcií:**

    Nie všetky modely podporujú volanie funkcií, preto je dôležité overiť, či váš používaný LLM túto funkciu podporuje.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podporuje volanie funkcií. Začneme vytvorením klienta pre Azure OpenAI.

    ```python
    # Inicializujte klienta Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Vytvorte schému funkcie:**

    Ďalej definujeme JSON schému, ktorá obsahuje názov funkcie, popis toho, čo funkcia robí, a názvy a popisy parametrov funkcie.
    Túto schému potom odovzdáme klientovi vytvorenému predtým spolu s požiadavkou používateľa na zistenie času v San Franciscu. Je dôležité poznamenať, že sa vráti **volanie nástroja**, **nie** konečná odpoveď na otázku. Ako bolo uvedené vyššie, LLM vracia názov funkcie vybranej pre úlohu a argumenty, ktoré sa jej odovzdajú.

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
  
    # Prvý API hovor: Požiadať model, aby použil funkciu
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

    Keďže LLM vybralo, ktorá funkcia sa má spustiť, je potrebné implementovať a vykonať kód, ktorý túto úlohu vykoná.
    Kód na získanie aktuálneho času môžeme implementovať v Pythone. Tiež budeme potrebovať napísať kód na extrahovanie názvu a argumentov z response_message na získanie konečného výsledku.

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
     # Spracovať volania funkcií
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
  
      # Druhé volanie API: Získať konečnú odpoveď od modelu
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

Volanie funkcií je jadrom väčšiny, ak nie všetkých, dizajnových vzorov používania nástrojov agentmi, no jeho implementácia od začiatku môže byť občas náročná.
Ako sme sa naučili v [Lekcii 2](../../../02-explore-agentic-frameworks), agentové rámce nám poskytujú predpripravené stavebné bloky na implementáciu používania nástrojov.

## Príklady používania nástrojov s agentovými rámcami

Tu sú niektoré príklady, ako môžete implementovať dizajnový vzor používania nástrojov pomocou rôznych agentových rámcov:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> je open-source AI rámec na tvorbu AI agentov. Zjednodušuje proces používania volania funkcií tým, že umožňuje definovať nástroje ako Python funkcie s dekorátorom `@tool`. Rámec spravuje komunikáciu medzi modelom a vaším kódom. Poskytuje tiež prístup k predpripraveným nástrojom, ako je File Search a Code Interpreter prostredníctvom `AzureAIProjectAgentProvider`.

Nasledujúci diagram znázorňuje proces volania funkcií v Microsoft Agent Framework:

![function calling](../../../translated_images/sk/functioncalling-diagram.a84006fc287f6014.webp)

V Microsoft Agent Framework sú nástroje definované ako dekorované funkcie. Funkciu `get_current_time`, ktorú sme videli skôr, môžeme previesť na nástroj použitím dekorátora `@tool`. Rámec automaticky serializuje funkciu a jej parametre a vytvorí schému na odoslanie do LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Vytvorte klienta
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Vytvorte agenta a spustite ho s nástrojom
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> je novší agentový rámec navrhnutý tak, aby umožnil vývojárom bezpečne vytvárať, nasadzovať a škálovať kvalitných a rozšíriteľných AI agentov bez potreby spravovať základné výpočtové a úložné zdroje. Je obzvlášť užitočný pre podnikové aplikácie, keďže ide o plne spravovanú službu s podnikovou bezpečnosťou.

V porovnaní s vývojom priamo pomocou LLM API poskytuje Azure AI Agent Service niekoľko výhod, vrátane:

- Automatické volanie nástrojov – nie je potrebné analyzovať volanie nástroja, vyvolávať nástroj a spracovávať odpoveď; toto všetko sa teraz uskutočňuje na strane servera
- Bezpečne spravované údaje – namiesto správy vlastného stavu konverzácie môžete spoliehať na vlákna, ktoré ukladajú všetky potrebné informácie
- Nástroje pripravené na použitie – nástroje, ktoré môžete použiť na interakciu so svojimi zdrojmi dát, ako Bing, Azure AI Search a Azure Functions.

Nástroje dostupné v Azure AI Agent Service sa delia do dvoch kategórií:

1. Nástroje na znalosti:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Základné vyhľadávanie Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Akčné nástroje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Volanie funkcií</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Nástroje definované OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nám umožňuje používať tieto nástroje spolu ako `toolset`. Tiež využíva `vlákna`, ktoré sledujú históriu správ z konkrétneho rozhovoru.

Predstavte si, že ste obchodným zástupcom v spoločnosti Contoso. Chcete vyvinúť konverzačného agenta, ktorý dokáže odpovedať na otázky o vašich predajných údajoch.

Nasledujúci obrázok znázorňuje, ako by ste mohli použiť Azure AI Agent Service na analýzu vašich predajných dát:

![Agentic Service In Action](../../../translated_images/sk/agent-service-in-action.34fb465c9a84659e.webp)

Na použitie ktoréhokoľvek z týchto nástrojov so službou môžeme vytvoriť klienta a definovať nástroj alebo toolset. Pri praktickej implementácii môžeme použiť nasledujúci Python kód. LLM bude môcť pozrieť na toolset a rozhodnúť sa, či použije používateľom vytvorenú funkciu `fetch_sales_data_using_sqlite_query` alebo predpripravený Code Interpreter v závislosti od požiadavky používateľa.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # funkcia fetch_sales_data_using_sqlite_query, ktorú nájdete v súbore fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inicializovať sadu nástrojov
toolset = ToolSet()

# Inicializovať agenta volania funkcií s funkciou fetch_sales_data_using_sqlite_query a pridať ju do sady nástrojov
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializovať nástroj Code Interpreter a pridať ho do sady nástrojov.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Aké sú špeciálne úvahy pri používaní dizajnového vzoru používania nástrojov pre budovanie dôveryhodných AI agentov?

Bežným problémom pri dynamicky generovanom SQL zo strany LLM je bezpečnosť, najmä riziko SQL injection alebo škodlivých akcií, ako je vymazanie alebo manipulačné zásahy do databázy. Hoci sú tieto obavy opodstatnené, dajú sa účinne zmierniť správnou konfiguráciou prístupových práv k databáze. Pre väčšinu databáz to zahŕňa nastavenie databázy ako read-only. Pre databázové služby ako PostgreSQL alebo Azure SQL by mala aplikácia mať priradenú rolu iba na čítanie (SELECT).

Spustenie aplikácie v bezpečnom prostredí navyše zvyšuje ochranu. V podnikovom prostredí sa údaje zvyčajne získavajú a transformujú z operačných systémov do read-only databázy alebo dátového skladu s používateľsky prívetivou schémou. Tento prístup zabezpečuje, že dáta sú bezpečné, optimalizované pre výkon a prístupnosť, a že aplikácia má obmedzený prístup na čítanie.

## Ukážkové kódy

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Máte ďalšie otázky o dizajnových vzoroch používania nástrojov?

Pridajte sa na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kde môžete stretnúť ďalších študentov, zúčastňovať sa office hours a získať odpovede na otázky ohľadom AI agentov.

## Ďalšie zdroje

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Prehľad Microsoft Agent Framework</a>

## Predchádzajúca lekcia

[Porozumenie agentovým dizajnovým vzorom](../03-agentic-design-patterns/README.md)

## Nasledujúca lekcia
[Agentný RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->