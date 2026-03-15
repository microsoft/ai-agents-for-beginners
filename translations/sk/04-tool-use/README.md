[![Ako navrhnúť dobrých AI agentov](../../../translated_images/sk/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

# Dizajnový vzor používania nástrojov

Nástroje sú zaujímavé, pretože umožňujú AI agentom mať širší rozsah schopností. Namiesto toho, aby mal agent obmedzený súbor akcií, ktoré môže vykonať, pridaním nástroja môže agent teraz vykonávať širokú škálu akcií. V tejto kapitole sa pozrieme na dizajnový vzor používania nástrojov, ktorý popisuje, ako môžu AI agenti používať konkrétne nástroje na dosiahnutie svojich cieľov.

## Úvod

V tejto lekcii sa pokúsime odpovedať na nasledujúce otázky:

- Čo je dizajnový vzor používania nástrojov?
- Na aké prípady použitia ho možno aplikovať?
- Aké prvky/stavebné bloky sú potrebné na implementáciu tohto dizajnového vzoru?
- Aké sú špeciálne úvahy pri používaní dizajnového vzoru používania nástrojov na vytváranie dôveryhodných AI agentov?

## Ciele učenia

Po dokončení tejto lekcie budete schopní:

- Definovať dizajnový vzor používania nástrojov a jeho účel.
- Identifikovať prípady použitia, kde je dizajnový vzor používania nástrojov aplikovateľný.
- Pochopiť kľúčové prvky potrebné na implementáciu vzoru.
- Uvedomiť si úvahy na zabezpečenie dôveryhodnosti AI agentov používajúcich tento dizajnový vzor.

## Čo je dizajnový vzor používania nástrojov?

**Dizajnový vzor používania nástrojov** sa zameriava na to, aby LLM mali schopnosť interagovať s externými nástrojmi na dosiahnutie konkrétnych cieľov. Nástroje sú kód, ktorý môže agent spustiť na vykonanie akcií. Nástroj môže byť jednoduchá funkcia, ako napríklad kalkulačka, alebo volanie API na službu tretej strany, napríklad vyhľadávanie cien akcií alebo predpoveď počasia. V kontexte AI agentov sú nástroje navrhnuté tak, aby ich agenti vykonávali v reakcii na **funkčné volania generované modelom**.

## Na aké prípady použitia ho možno aplikovať?

AI agenti môžu využiť nástroje na dokončenie zložitých úloh, získavanie informácií alebo prijímanie rozhodnutí. Dizajnový vzor používania nástrojov sa často používa v scenároch vyžadujúcich dynamickú interakciu s externými systémami, ako napríklad databázy, webové služby alebo interpretery kódu. Táto schopnosť je užitočná pri rôznych prípadoch použitia vrátane:

- **Dynamické získavanie informácií:** Agent môže dotazovať externé API alebo databázy na získanie aktuálnych údajov (napr. dotazovanie SQLite databázy na analýzu dát, získavanie cien akcií alebo informácií o počasí).
- **Spúšťanie a interpretácia kódu:** Agent môže spustiť kód alebo skripty na riešenie matematických problémov, generovanie reportov alebo vykonávanie simulácií.
- **Automatizácia pracovných tokov:** Automatizácia opakujúcich sa alebo viacstupňových pracovných tokov integráciou nástrojov ako plánovače úloh, e-mailové služby alebo dátové pipeline.
- **Zákaznícka podpora:** Agent môže interagovať so systémami CRM, platformami na spravovanie lístkov alebo znalosťovými databázami na riešenie požiadaviek používateľov.
- **Generovanie a úprava obsahu:** Agent môže využiť nástroje ako kontrolóri gramatiky, zhrňovače textov alebo hodnotiace nástroje bezpečnosti obsahu na pomoc pri tvorbe obsahu.

## Aké prvky/stavebné bloky sú potrebné na implementáciu dizajnového vzoru používania nástrojov?

Tieto stavebné bloky umožňujú AI agentovi vykonávať širokú škálu úloh. Pozrime sa na kľúčové prvky potrebné na implementáciu dizajnového vzoru používania nástrojov:

- **Schémy funkcií/nástrojov**: Detailné definície dostupných nástrojov vrátane názvu funkcie, účelu, požadovaných parametrov a očakávaných výstupov. Tieto schémy umožňujú LLM pochopiť, aké nástroje sú dostupné a ako zostaviť platné požiadavky.

- **Logika vykonávania funkcií**: Určuje, ako a kedy sa nástroje volajú na základe zámeru používateľa a kontextu konverzácie. Toto môže zahŕňať moduly plánovača, mechanizmy smerovania alebo podmienené toky, ktoré dynamicky určujú použitie nástrojov.

- **Systém spracovania správ**: Komponenty spravujúce konverzačný tok medzi vstupmi používateľa, odpoveďami LLM, volaniami nástrojov a výstupmi nástrojov.

- **Rámec integrácie nástrojov**: Infraštuktúra, ktorá prepája agenta s rôznymi nástrojmi, či už ide o jednoduché funkcie alebo komplexné externé služby.

- **Spracovanie chýb a validácia**: Mechanizmy na spracovanie zlyhaní pri vykonávaní nástroja, validáciu parametrov a riadenie neočakávaných odpovedí.

- **Správa stavu**: Sleduje kontext konverzácie, predchádzajúce interakcie s nástrojmi a perzistentné dáta, aby bola zabezpečená konzistencia počas viackrokových interakcií.

Ďalej sa pozrieme podrobnejšie na volanie funkcií/nástrojov.
 
### Volanie funkcie/nástroja

Volanie funkcie je primárny spôsob, ako umožniť veľkým jazykovým modelom (LLM) interagovať s nástrojmi. Často uvidíte, že 'Funkcia' a 'Nástroj' sa používajú zameniteľne, pretože 'funkcie' (bloky opakovane použiteľného kódu) sú 'nástroje', ktoré agenti používajú na vykonanie úloh. Aby mohol byť kód funkcie spustený, LLM musí porovnať požiadavku používateľa s popisom funkcie. Na to sa odošle schéma obsahujúca popisy všetkých dostupných funkcií do LLM. LLM následne vyberie najvhodnejšiu funkciu pre úlohu a vráti jej názov a argumenty. Vybraná funkcia sa zavolá, jej odpoveď sa pošle späť do LLM, ktoré použije informácie na odpoveď na požiadavku používateľa.

Pre vývojárov, ktorí chcú implementovať volanie funkcií pre agentov, budete potrebovať:

1. LLM model, ktorý podporuje volanie funkcií
2. Schému obsahujúcu popisy funkcií
3. Kód pre každú opísanú funkciu

Použime príklad získania aktuálneho času v meste na ilustráciu:

1. **Inicializujte LLM, ktorý podporuje volanie funkcií:**

    Nie všetky modely podporujú volanie funkcií, preto je dôležité overiť, že LLM, ktorý používate, to podporuje. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podporuje volanie funkcií. Môžeme začať inicializáciou Azure OpenAI klienta. 

    ```python
    # Inicializujte klienta Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Vytvorte schému funkcie**:

    Ďalej definujeme JSON schému, ktorá obsahuje názov funkcie, popis toho, čo funkcia robí, a názvy a popisy parametrov funkcie.
    Následne túto schému odovzdáme klientovi vytvorenému vyššie spolu s požiadavkou používateľa na získanie času v San Franciscu. Dôležité je poznamenať, že sa vracia **volanie nástroja**, **nie** konečná odpoveď na otázku. Ako bolo spomenuté vyššie, LLM vráti názov funkcie, ktorú si vybral pre úlohu, a argumenty, ktoré do nej budú predané.

    ```python
    # Popis funkcie pre model na prečítanie
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
  
    # Prvý volanie API: Požiadajte model, aby použil funkciu
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Spracovanie odpovede modelu
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

    Teraz, keď LLM vybral funkciu, ktorá má byť spustená, musí byť implementovaný a vykonaný kód, ktorý úlohu vykoná.
    Môžeme implementovať kód na získanie aktuálneho času v Pythone. Tiež budeme potrebovať napísať kód, ktorý z výstupu `response_message` extrahuje názov a argumenty na získanie konečného výsledku.

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
  
      # Druhý volanie API: Získať konečnú odpoveď od modelu
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

Volanie funkcie je jadrom väčšiny, ak nie všetkých, dizajnov používania nástrojov agentov, avšak jeho implementácia od nuly môže byť niekedy náročná.
Ako sme sa naučili v [Lekcii 2](../../../02-explore-agentic-frameworks), agentné rámce nám poskytujú predpripravené stavebné bloky na implementáciu používania nástrojov.
 
## Príklady používania nástrojov s agentnými rámcami

Tu je niekoľko príkladov, ako môžete implementovať dizajnový vzor používania nástrojov pomocou rôznych agentných rámcov:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> je open-source AI rámec na tvorbu AI agentov. Zjednodušuje proces používania volania funkcií umožnením definovať nástroje ako Python funkcie s dekorátorom `@tool`. Rámec rieši komunikáciu medzi modelom a vašim kódom. Tiež poskytuje prístup k predpripraveným nástrojom, ako File Search a Code Interpreter, cez `AzureAIProjectAgentProvider`.

Nasledujúci diagram ilustruje proces volania funkcie s Microsoft Agent Framework:

![function calling](../../../translated_images/sk/functioncalling-diagram.a84006fc287f6014.webp)

V Microsoft Agent Framework sú nástroje definované ako dekorované funkcie. Môžeme previesť funkciu `get_current_time`, ktorú sme videli skôr, na nástroj použitím dekorátora `@tool`. Rámec automaticky serializuje funkciu a jej parametre, čím vytvorí schému na odoslanie do LLM.

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

# Vytvorte agenta a spustite nástroj
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> je novší agentný rámec navrhnutý tak, aby umožnil vývojárom bezpečne vytvárať, nasadzovať a škálovať kvalitných a rozšíriteľných AI agentov bez potreby spravovať základné výpočtové a úložné zdroje. Je obzvlášť užitočný pre podnikové aplikácie, pretože je to plne spravovaná služba s podnikovej úrovne zabezpečením.

V porovnaní s vývojom priamo cez LLM API poskytuje Azure AI Agent Service niekoľko výhod, vrátane:

- Automatické volanie nástrojov – nie je potrebné parsovať volanie nástroja, spúšťať nástroj a spracovávať odpoveď; toto je všetko teraz riešené na strane servera
- Bezpečne spravované dáta – namiesto správy vlastného stavu konverzácie môžete spoľahnúť na vlákna (threads) na ukladanie všetkých potrebných informácií
- Nástroje pripravené na použitie – nástroje, ktoré môžete použiť na interakciu s vašimi dátovými zdrojmi, ako sú Bing, Azure AI Search a Azure Functions.

Nástroje dostupné v Azure AI Agent Service možno rozdeliť do dvoch kategórií:

1. Nástroje poznatkov:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Zakotvenie cez Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Akčné nástroje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Volanie funkcií</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Nástroje definované OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nám umožňuje používať tieto nástroje spoločne ako `toolset`. Tiež využíva `threads`, ktoré sledujú históriu správ zo špecifickej konverzácie.

Predstavte si, že ste predajný agent v spoločnosti Contoso. Chcete vyvinúť konverzačného agenta, ktorý bude odpovedať na otázky o vašich predajných dátach.

Nasledujúci obrázok ilustruje, ako by ste mohli použiť Azure AI Agent Service na analýzu vašich predajných dát:

![Agentic Service In Action](../../../translated_images/sk/agent-service-in-action.34fb465c9a84659e.webp)

Na použitie ktoréhokoľvek z týchto nástrojov so službou môžeme vytvoriť klienta a definovať nástroj alebo sadu nástrojov. Na praktickú implementáciu môžeme použiť nasledujúci Python kód. LLM bude schopný pozrieť sa na sadu nástrojov a rozhodnúť, či použiť používateľom vytvorenú funkciu `fetch_sales_data_using_sqlite_query` alebo predpripravený Code Interpreter v závislosti od požiadavky používateľa.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # funkcia fetch_sales_data_using_sqlite_query, ktorú možno nájsť v súbore fetch_sales_data_functions.py.
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

# Inicializovať nástroj Kódový interpret a pridať ho do súpravy nástrojov.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Aké sú špeciálne úvahy pri používaní dizajnového vzoru používania nástrojov na vytváranie dôveryhodných AI agentov?

Bežnou obavou pri dynamicky generovanom SQL od LLM je bezpečnosť, najmä riziko SQL injection alebo škodlivých akcií, ako je zmazanie alebo manipulácia s databázou. Aj keď sú tieto obavy oprávnené, dajú sa efektívne zmierniť správnym nastavením prístupových oprávnení do databázy. Pre väčšinu databáz to znamená nastavenie databázy ako len na čítanie. Pre databázové služby ako PostgreSQL alebo Azure SQL by mala byť aplikácii pridelená rola s právami na čítanie (SELECT).

Spustenie aplikácie v bezpečnom prostredí ešte viac zvyšuje ochranu. V podnikových scenároch sa zvyčajne extrahujú a transformujú dáta z operačných systémov do databázy alebo dátového skladu len na čítanie s používateľsky priateľskou schémou. Tento prístup zabezpečuje, že dáta sú bezpečné, optimalizované pre výkon a dostupnosť a aplikácia má obmedzený prístup len na čítanie.

## Ukážkové kódy

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Máte ďalšie otázky o dizajnových vzoroch používania nástrojov?

Pridajte sa do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kde sa stretnete s inými študentmi, zúčastníte sa kancelárskych hodín a získate odpovede na vaše otázky o AI agentech.

## Dodatočné zdroje

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Workshop Multi-Agent Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Prehľad Microsoft Agent Framework</a>

## Predchádzajúca lekcia

[Porozumenie agentným dizajnovým vzorom](../03-agentic-design-patterns/README.md)

## Nasledujúca lekcia
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornenie**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, berte, prosím, na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Neručíme za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->