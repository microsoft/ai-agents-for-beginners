[![Ako navrhnúť dobrých AI agentov](../../../translated_images/sk/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

# Dizajnový vzor použitia nástrojov

Nástroje sú zaujímavé, pretože umožňujú AI agentom mať širší rozsah schopností. Namiesto toho, aby agent mal obmedzený súbor akcií, ktoré môže vykonať, pridaním nástroja môže agent teraz vykonať široké spektrum akcií. V tejto kapitole sa pozrieme na dizajnový vzor použitia nástrojov, ktorý popisuje, ako môžu AI agenti využívať špecifické nástroje na dosiahnutie svojich cieľov.

## Úvod

V tejto lekcii sa snažíme odpovedať na nasledujúce otázky:

- Čo je dizajnový vzor použitia nástrojov?
- Na aké prípady použitia sa dá aplikovať?
- Aké prvky/stavebné bloky sú potrebné na implementáciu tohto vzoru?
- Aké sú špeciálne úvahy pri používaní dizajnového vzoru použitia nástrojov na vytvorenie dôveryhodných AI agentov?

## Výučbové ciele

Po absolvovaní tejto lekcie budete schopní:

- Definovať dizajnový vzor použitia nástrojov a jeho účel.
- Identifikovať prípady použitia, kde je dizajnový vzor použitia nástrojov použiteľný.
- Pochopiť kľúčové prvky potrebné na implementáciu vzoru.
- Rozpoznať úvahy na zabezpečenie dôveryhodnosti AI agentov používajúcich tento dizajnový vzor.

## Čo je dizajnový vzor použitia nástrojov?

**Dizajnový vzor použitia nástrojov** sa zameriava na umožnenie LLM interakcie s externými nástrojmi na dosiahnutie konkrétnych cieľov. Nástroje sú kód, ktorý môže agent vykonať na realizáciu akcií. Nástroj môže byť jednoduchá funkcia, ako napríklad kalkulačka, alebo volanie API na tretiu stranu, napríklad vyhľadávanie cien akcií alebo predpoveď počasia. V kontexte AI agentov sú nástroje navrhnuté tak, aby ich agenti vykonávali v reakcii na **funkčné volania generované modelom**.

## Na aké prípady použitia sa dá aplikovať?

AI agenti môžu využiť nástroje na dokončenie zložitých úloh, získavanie informácií alebo prijímanie rozhodnutí. Dizajnový vzor použitia nástrojov sa často používa v scénach vyžadujúcich dynamickú interakciu s externými systémami, ako sú databázy, webové služby alebo interprety kódu. Táto schopnosť je užitočná pre rôzne prípady použitia, vrátane:

- **Dynamické získavanie informácií:** Agent môže dotazovať externé API alebo databázy na získanie aktuálnych údajov (napr. dotazovanie SQLite databázy pre analýzu dát, získavanie cien akcií alebo informácií o počasí).
- **Vykonávanie kódu a interpretácia:** Agent môže spustiť kód alebo skripty na riešenie matematických problémov, generovanie správ alebo vykonávanie simulácií.
- **Automatizácia pracovných postupov:** Automatizácia opakujúcich sa alebo viac-krokových pracovných postupov integráciou nástrojov ako plánovače úloh, emailové služby alebo dátové kanály.
- **Zákaznícka podpora:** Agent môže komunikovať so systémami CRM, platformami pre správu ticketov alebo vedomostnými bázami na riešenie dotazov používateľov.
- **Generovanie a úprava obsahu:** Agent môže využiť nástroje ako kontrola gramatiky, sumarizátory textov alebo hodnotiace nástroje bezpečnosti obsahu na pomoc pri tvorbe obsahu.

## Aké sú prvky/stavebné bloky potrebné na implementáciu dizajnového vzoru použitia nástrojov?

Tieto stavebné bloky umožňujú AI agentovi vykonávať široké spektrum úloh. Pozrime sa na kľúčové prvky potrebné na implementáciu dizajnového vzoru použitia nástrojov:

- **Schémy funkcií/nástrojov**: Podrobné definície dostupných nástrojov, vrátane názvu funkcie, účelu, požadovaných parametrov a očakávaných výstupov. Tieto schémy umožňujú LLM pochopiť, aké nástroje sú dostupné a ako vytvoriť platné požiadavky.

- **Logika vykonávania funkcií**: Riadi, kedy a ako sa nástroje vyvolávajú na základe zámeru používateľa a kontextu konverzácie. Môže to zahŕňať moduly plánovača, mechanizmy smerovania alebo podmienené toky, ktoré dynamicky určujú používanie nástrojov.

- **Systém spracovania správ**: Komponenty spravujúce tok konverzácie medzi vstupmi používateľov, odpoveďami LLM, volaniami nástrojov a ich výstupmi.

- **Rámec integrácie nástrojov**: Infraštruktúra, ktorá prepája agenta s rôznymi nástrojmi, či už sú to jednoduché funkcie alebo komplexné externé služby.

- **Spracovanie chýb a validácia**: Mechanizmy na riešenie neúspechov pri vykonávaní nástrojov, validáciu parametrov a riadenie neočakávaných odpovedí.

- **Správa stavu**: Sleduje kontext konverzácie, predchádzajúce interakcie s nástrojmi a trvalé dáta na zabezpečenie konzistencie v multi-krokových interakciách.

Teraz sa pozrime podrobnejšie na volanie funkcií/nástrojov.
 
### Volanie funkcií/nástrojov

Volanie funkcií je primárny spôsob, akým umožňujeme veľkým jazykovým modelom (LLM) interakciu s nástrojmi. Často uvidíte, že 'funkcia' a 'nástroj' sa používajú zameniteľne, pretože 'funkcie' (bloky znovupoužiteľného kódu) sú 'nástroje', ktoré agenti používajú na vykonávanie úloh. Aby bol kód funkcie vyvolaný, musí LLM porovnať požiadavku používateľa s popisom funkcie. Na tento účel sa LLM odosiela schéma obsahujúca popisy všetkých dostupných funkcií. LLM potom vyberie najvhodnejšiu funkciu pre úlohu a vráti jej názov a argumenty. Vybraná funkcia sa vyvolá, jej odpoveď sa odošle späť LLM, ktoré použije informácie na odpoveď používateľovi.

Vývojári, ktorí chcú implementovať volanie funkcií pre agentov, budú potrebovať:

1. LLM model, ktorý podporuje volanie funkcií
2. Schému obsahujúcu popisy funkcií
3. Kód pre každú popísanú funkciu

Na ilustráciu použijeme príklad zistenia aktuálneho času v meste:

1. **Inicializujte LLM, ktorý podporuje volanie funkcií:**

    Nie všetky modely podporujú volanie funkcií, preto je dôležité skontrolovať, či používaný LLM túto funkcionalitu má.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podporuje volanie funkcií. Môžeme začať inicializáciou klienta OpenAI voči Azure OpenAI **Responses API** (stabilný endpoint `/openai/v1/` — `api_version` nie je potrebný). 

    ```python
    # Inicializujte klienta OpenAI pre Azure OpenAI (Responses API, v1 koncový bod)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Vytvorte schému funkcie**:

    Ďalej definujeme JSON schému, ktorá obsahuje názov funkcie, popis toho, čo funkcia robí, a názvy a popisy parametrov funkcie.
    Túto schému následne pošleme klientovi vytvorenému vyššie spolu s požiadavkou používateľa, ktorý chce zistiť čas v San Franciscu. Dôležité je poznamenať, že **výsledkom je volanie nástroja**, **nie** konečná odpoveď na otázku. Ako už bolo spomenuté, LLM vráti názov vybratej funkcie a argumenty, ktoré sa jej predajú.

    ```python
    # Popis funkcie pre model na čítanie (formát plochého nástroja Responses API)
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
  
    # Počiatočná správa používateľa
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Prvý API volanie: Požiadajte model, aby použil funkciu
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API vracia volania nástrojov ako položky function_call v response.output.
    # Pripojte ich do konverzácie, aby mal model kompletný kontext pri ďalšom kole.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Kód funkcie potrebný na vykonanie úlohy:**

    Keďže LLM vybral funkciu, ktorú treba spustiť, je potrebné implementovať a vykonať kód, ktorý úlohu splní.
    Môžeme implementovať kód na získanie aktuálneho času v Pythone. Tiež budeme musieť napísať kód na extrahovanie názvu a argumentov z response_message, aby sme získali konečný výsledok.

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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Vrátiť výsledok nástroja ako položku function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Druhé volanie API: Získať finálnu odpoveď od modelu
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

Volanie funkcií je jadrom väčšiny, ak nie všetkých, dizajnov použitia nástrojov agentov, avšak jeho implementácia od základov môže byť niekedy náročná.
Ako sme sa naučili v [Lekcii 2](../../../02-explore-agentic-frameworks), agentové rámce nám poskytujú predpripravené stavebné bloky na implementáciu použitia nástrojov.
 
## Príklady použitia nástrojov s agentovými rámcami

Tu sú niektoré príklady, ako implementovať dizajnový vzor použitia nástrojov pomocou rôznych agentových rámcov:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> je open-source AI rámec na tvorbu AI agentov. Zjednodušuje proces používania volania funkcií tým, že umožňuje definovať nástroje ako Python funkcie s dekorátorom `@tool`. Rámec spravuje komunikáciu medzi modelom a vaším kódom. Tiež poskytuje prístup k predpripraveným nástrojom ako File Search a Code Interpreter cez `FoundryChatClient`.

Nasledujúca schéma znázorňuje proces volania funkcií s Microsoft Agent Framework:

![function calling](../../../translated_images/sk/functioncalling-diagram.a84006fc287f6014.webp)

V Microsoft Agent Framework sú nástroje definované ako dekorované funkcie. Náš príklad funkcie `get_current_time` môžeme previesť na nástroj použitím dekorátora `@tool`. Rámec automaticky serializuje funkciu a jej parametre, čím vytvorí schému na odoslanie LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Vytvorte klienta
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Vytvorte agenta a spustite ho s nástrojom
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> je modernejší agentový rámec navrhnutý tak, aby umožnil vývojárom bezpečne vytvárať, nasadzovať a škálovať kvalitných a rozšíriteľných AI agentov bez potreby správy podkladových výpočtových a úložných zdrojov. Je obzvlášť užitočný pre podnikové aplikácie, pretože je plne spravovanou službou s podnikou úrovňou zabezpečenia.

V porovnaní s priamym vývojom cez LLM API poskytuje Microsoft Foundry Agent Service niekoľko výhod, vrátane:

- Automatické volanie nástrojov – nie je potrebné analyzovať volanie nástroja, vyvolávať ho a spracovávať odpoveď; všetko sa teraz robí na serverovej strane.
- Bezpečne spravované údaje – namiesto správy vlastného stavu konverzácie sa môžete spoľahnúť na vlákna, ktoré ukladajú všetky potrebné informácie.
- Nástroje ihneď použiteľné – nástroje, ktoré umožňujú interagovať s dátovými zdrojmi, ako Bing, Azure AI Search a Azure Functions.

Nástroje dostupné v Microsoft Foundry Agent Service sa dajú rozdeliť do dvoch kategórií:

1. Nástroje znalostí:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding s Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Akčné nástroje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Volanie funkcií</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Nástroje definované OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nám umožňuje používať tieto nástroje spoločne ako `toolset`. Tiež využíva `vlákna`, ktoré sledujú históriu správ z konkrétnej konverzácie.

Predstavte si, že ste predajný agent v spoločnosti Contoso. Chcete vytvoriť konverzačného agenta, ktorý dokáže odpovedať na otázky o vašich predajných dátach.

Nasledujúci obrázok ilustruje, ako by ste mohli použiť Microsoft Foundry Agent Service na analýzu vašich predajných dát:

![Agentic Service In Action](../../../translated_images/sk/agent-service-in-action.34fb465c9a84659e.webp)

Na používanie týchto nástrojov so službou môžeme vytvoriť klienta a definovať nástroj alebo toolset. Na praktickú implementáciu môžeme použiť nasledujúci Python kód. LLM potom dokáže pri pohľade na toolset rozhodnúť, či použije užívateľom vytvorenú funkciu `fetch_sales_data_using_sqlite_query` alebo predpripravený Code Interpreter podľa požiadavky používateľa.

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

# Inicializovať nástrojový set
toolset = ToolSet()

# Inicializovať agenta volajúceho funkcie s funkciou fetch_sales_data_using_sqlite_query a pridať ho do nástrojového setu
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializovať nástroj Code Interpreter a pridať ho do nástrojového setu.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Aké sú špeciálne úvahy pri použití dizajnového vzoru použitia nástrojov na vytvorenie dôveryhodných AI agentov?

Bežnou obavou pri SQL dynamicky generovanom LLM je bezpečnosť, najmä riziko SQL injekcie alebo škodlivých akcií, ako je vymazanie alebo manipulácia s databázou. Hoci tieto obavy sú oprávnené, dajú sa účinne zmierniť správnym nastavením oprávnení na prístup k databáze. Pre väčšinu databáz to znamená nastavenie databázy ako iba na čítanie. Pre databázové služby ako PostgreSQL alebo Azure SQL by mala mať aplikácia rolu iba na čítanie (SELECT).

Spustenie aplikácie v bezpečnom prostredí ďalej zvyšuje ochranu. V podnikových scénároch sa dáta zvyčajne extrahujú a transformujú z operačných systémov do databázy alebo dátového skladu iba na čítanie s používateľsky prívetivou schémou. Tento prístup zabezpečuje, že dáta sú chránené, optimalizované pre výkon a prístupnosť, a aplikácia má obmedzený, iba na čítanie prístup.

## Ukážkové kódy

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Máte ďalšie otázky o dizajnových vzoroch použitia nástrojov?

Pridajte sa na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde sa môžete stretnúť s inými študentmi, zúčastniť sa konzultačných hodín a získať odpovede na svoje otázky o AI agentoch.

## Ďalšie zdroje

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Dielňa služieb Azure AI Agents</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Prehľad Microsoft Agent Framework</a>


## Rýchle testovanie tohto agenta (voliteľné)

Po tom, čo sa naučíte nasadzovať agentov v [Lekcia 16](../16-deploying-scalable-agents/README.md), môžete rýchlo otestovať `TravelToolAgent` z tejto lekcie (či stále volá svoje nástroje a odpovedá) pomocou [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Pozrite si [`tests/README.md`](../tests/README.md), ako ho spustiť.

## Predchádzajúca lekcia

[Pochopenie agentových návrhových vzorov](../03-agentic-design-patterns/README.md)

## Nasledujúca lekcia

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->