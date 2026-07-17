[![Ako navrhnúť dobrých AI agentov](../../../translated_images/sk/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite na obrázok vyššie a pozrite si video k tejto lekcii)_

# Dizajnový vzor používania nástrojov

Nástroje sú zaujímavé, pretože umožňujú AI agentom širší rozsah schopností. Namiesto toho, aby mal agent obmedzený súbor akcií, ktoré môže vykonať, pridaním nástroja môže agent teraz vykonávať širokú škálu akcií. V tejto kapitole sa pozrieme na dizajnový vzor používania nástrojov, ktorý popisuje, ako môžu AI agenti používať špecifické nástroje na dosiahnutie svojich cieľov.

## Úvod

V tejto lekcii sa budeme snažiť odpovedať na nasledujúce otázky:

- Čo je dizajnový vzor používania nástrojov?
- Na aké použitia je možné ho aplikovať?
- Aké prvky/stavebné kamene sú potrebné na implementáciu tohto dizajnového vzoru?
- Aké sú špeciálne úvahy pre použitie dizajnového vzoru používania nástrojov na vytvorenie dôveryhodných AI agentov?

## Ciele učenia

Po absolvovaní tejto lekcie budete vedieť:

- Definovať dizajnový vzor používania nástrojov a jeho účel.
- Identifikovať prípady použitia, kde je tento dizajnový vzor vhodný.
- Pochopiť kľúčové prvky potrebné na implementáciu vzoru.
- Rozpoznať úvahy potrebné na zabezpečenie dôveryhodnosti AI agentov používajúcich tento dizajnový vzor.

## Čo je dizajnový vzor používania nástrojov?

**Dizajnový vzor používania nástrojov** sa zameriava na poskytovanie schopnosti LLM pracovať s externými nástrojmi na dosiahnutie špecifických cieľov. Nástroje sú kód, ktorý môže agent vykonať na vykonanie akcií. Nástroj môže byť jednoduchá funkcia, ako kalkulačka, alebo volanie API tretej strany, ako vyhľadávanie cien akcií alebo predpoveď počasia. V kontexte AI agentov sú nástroje navrhnuté tak, aby ich agenti vykonávali v reakcii na **volania funkcií generované modelom**.

## Na aké prípady použitia je možné ho aplikovať?

AI agenti môžu využiť nástroje na dokončenie komplexných úloh, získavanie informácií alebo rozhodovanie. Dizajnový vzor používania nástrojov sa často používa v scenároch vyžadujúcich dynamickú interakciu s externými systémami, ako sú databázy, webové služby alebo interprety kódu. Táto schopnosť je užitočná pre viacero rôznych prípadov použitia vrátane:

- **Dynamické získavanie informácií:** Agent môže vyhľadávať v externých API alebo databázach aktuálne dáta (napr. dotazovanie sa na databázu SQLite pre analýzu dát, získavanie cien akcií alebo informácií o počasí).
- **Vykonávanie a interpretácia kódu:** Agent môže vykonávať kód alebo skripty na riešenie matematických úloh, generovanie správ alebo vykonávanie simulácií.
- **Automatizácia pracovných tokov:** Automatizovanie opakujúcich sa alebo viacstupňových pracovných tokov integráciou nástrojov, ako sú plánovače úloh, e-mailové služby alebo dátové potrubia.
- **Zákaznícka podpora:** Agent môže komunikovať s CRM systémami, ticketovacími platformami alebo vedomostnými databázami na riešenie užívateľských dotazov.
- **Generovanie a úprava obsahu:** Agent môže využívať nástroje ako kontrola gramatiky, sumarizátory textu alebo hodnotiace nástroje bezpečnosti obsahu na pomoc pri tvorbe obsahu.

## Aké prvky/stavebné kamene sú potrebné na implementáciu dizajnového vzoru používania nástrojov?

Tieto stavebné kamene umožňujú AI agentovi vykonávať širokú škálu úloh. Pozrime sa na kľúčové prvky potrebné na implementáciu dizajnového vzoru používania nástrojov:

- **Schémy funkcií/nástrojov**: Podrobné definície dostupných nástrojov vrátane názvu funkcie, účelu, požadovaných parametrov a očakávaných výstupov. Tieto schémy umožňujú LLM pochopiť, aké nástroje sú dostupné a ako zostaviť platné požiadavky.

- **Logika vykonávania funkcií**: Riadi, ako a kedy sa nástroje volajú na základe zámeru používateľa a kontextu konverzácie. Môže zahŕňať moduly plánovania, smerovacie mechanizmy alebo podmienené toky, ktoré dynamicky určujú využívanie nástrojov.

- **Systém spracovania správ**: Komponenty, ktoré riadia tok konverzácie medzi vstupmi používateľa, odpoveďami LLM, volaniami nástrojov a ich výstupmi.

- **Rámec integrácie nástrojov**: Infraštruktúra spájajúca agenta s rôznymi nástrojmi, či už ide o jednoduché funkcie alebo komplexné externé služby.

- **Spracovanie chýb a validácia**: Mechanizmy na riešenie zlyhaní pri vykonávaní nástrojov, overovanie parametrov a spravovanie neočakávaných odpovedí.

- **Správa stavu**: Sleduje kontext konverzácie, predchádzajúce interakcie s nástrojmi a perzistentné dáta, aby sa zabezpečila konzistencia počas viackolových interakcií.

Ďalej sa pozrieme podrobnejšie na volanie funkcií/nástrojov.
 
### Volanie funkcií/nástrojov

Volanie funkcií je primárnym spôsobom, akým umožňujeme veľkým jazykovým modelom (LLM) komunikovať s nástrojmi. Často uvidíte pojmy 'Funkcia' a 'Nástroj' používané zameniteľne, pretože 'funkcie' (bloky znovupoužiteľného kódu) sú 'nástrojmi', ktoré agenti používajú na vykonávanie úloh. Aby mohol byť kód funkcie vyvolaný, LLM musí porovnať požiadavku používateľa s popisom funkcie. Na to sa LLM odošle schéma obsahujúca popisy všetkých dostupných funkcií. LLM potom vyberie najvhodnejšiu funkciu pre danú úlohu a vráti jej názov a argumenty. Vybraná funkcia je vyvolaná, jej odpoveď je zaslaná späť LLM, ktorý následne použije tieto informácie na odpoveď požiadavke používateľa.

Pre vývojárov, ktorí chcú implementovať volanie funkcií pre agentov, budete potrebovať:

1. Model LLM, ktorý podporuje volanie funkcií
2. Schému obsahujúcu popisy funkcií
3. Kód pre každú popísanú funkciu

Použime príklad získania aktuálneho času v meste na ilustráciu:

1. **Inicializujte LLM, ktorý podporuje volanie funkcií:**

    Nie všetky modely podporujú volanie funkcií, preto je dôležité skontrolovať, či váš LLM túto funkcionalitu podporuje.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podporuje volanie funkcií. Môžeme začať inicializáciou klienta OpenAI na Azure OpenAI **Responses API** (stabilný endpoint `/openai/v1/` — nie je potrebná `api_version`).

    ```python
    # Inicializujte klienta OpenAI pre Azure OpenAI (API odpovedí, koncový bod v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Vytvorte schému funkcie**:

    Ďalej definujeme JSON schému, ktorá obsahuje názov funkcie, popis toho, čo funkcia robí, a názvy a popisy parametrov funkcie.
    Túto schému potom odovzdáme klientovi vytvorenému vyššie, spolu s požiadavkou používateľa na zistenie času v San Franciscu. Dôležité je, že sa nevracia **návrat nástroja**, ale **nie finálna odpoveď na otázku**. Ako bolo spomenuté, LLM vráti názov funkcie, ktorú vybral pre úlohu, a argumenty, ktoré jej budú predané.

    ```python
    # Popis funkcie pre model na čítanie (formát nástroja Responses API flat)
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

    # Prvý volanie API: Požiadajte model, aby použil funkciu
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # API odpovedí vracia volania nástrojov ako položky function_call v response.output.
    # Pridajte ich do konverzácie, aby mal model úplný kontext v ďalšom kole.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Kód funkcie potrebný na vykonanie úlohy:**

    Keď LLM vybral, ktorá funkcia má byť spustená, musíme implementovať a vykonať kód, ktorý úlohu splní.
    Implementujeme kód na získanie aktuálneho času v Pythone. Tiež budeme musieť napísať kód na extrahovanie mena a argumentov z odpovedi (response_message), aby sme získali konečný výsledok.

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

    # Druhý API hovor: Získať konečnú odpoveď od modelu
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

Volanie funkcií je v jadre väčšiny, ak nie všetkých, nástrojových dizajnov agentov, avšak implementácia od začiatku môže byť niekedy náročná.
Ako sme sa naučili v [Lekcia 2](../../../02-explore-agentic-frameworks), agentové rámce nám poskytujú predpripravené stavebné kamene na implementáciu používania nástrojov.
 
## Príklady používania nástrojov s agentovými rámcami

Tu sú niektoré príklady, ako môžete implementovať dizajnový vzor používania nástrojov pomocou rôznych agentových rámcov:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> je open-source AI rámec na vývoj AI agentov. Zjednodušuje proces používania volania funkcií tým, že umožňuje definovať nástroje ako Python funkcie s dekorátorom `@tool`. Rámec rieši komunikáciu medzi modelom a vaším kódom. Tiež poskytuje prístup k predpripraveným nástrojom ako File Search a Code Interpreter cez `FoundryChatClient`.

Nasledujúca schéma zobrazuje proces volania funkcií v Microsoft Agent Framework:

![function calling](../../../translated_images/sk/functioncalling-diagram.a84006fc287f6014.webp)

V Microsoft Agent Framework sú nástroje definované ako dekorované funkcie. Môžeme premeniť funkciu `get_current_time`, ktorú sme videli vyššie, na nástroj použitím dekorátora `@tool`. Rámec automaticky serializuje funkciu a jej parametre, čím vytvorí schému na odoslanie LLM.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> je novší agentový rámec navrhnutý tak, aby umožnil vývojárom bezpečne vytvárať, nasadzovať a škálovať vysoko kvalitných a rozšíriteľných AI agentov bez potreby spravovať základné výpočtové a úložné zdroje. Je obzvlášť užitočný v podnikových aplikáciách, pretože ide o plne spravovanú službu s podnikových štandardom zabezpečenia.

V porovnaní s vývojom priamo cez LLM API ponúka Microsoft Foundry Agent Service niekoľko výhod, vrátane:

- Automatické volanie nástrojov – nie je potrebné analyzovať volanie nástroja, vykonať ho a spracovať odpoveď; všetko sa teraz vykonáva na serverovej strane
- Bezpečne spravované dáta – namiesto správy vlastného kontextu konverzácie sa môžete spoľahnúť na "vlákna" na ukladanie všetkých potrebných informácií
- Nástroje pripravené na použitie – Nástroje na interakciu so zdrojmi dát, ako sú Bing, Azure AI Search a Azure Functions.

Nástroje dostupné v Microsoft Foundry Agent Service možno rozdeliť do dvoch kategórií:

1. Nástroje vedomostí:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Zakotvenie s Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Vyhľadávanie súborov</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Akčné nástroje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Volanie funkcií</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpreter kódu</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Nástroje definované OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nám umožňuje používať tieto nástroje spoločne ako `toolset`. Tiež využíva `vlákna`, ktoré sledujú históriu správ z konkrétnej konverzácie.

Predstavte si, že ste obchodný zástupca v spoločnosti Contoso. Chcete vyvinúť konverzačného agenta, ktorý dokáže odpovedať na otázky o vašich predajných údajoch.

Nasledujúci obrázok ilustruje, ako by ste mohli použiť Microsoft Foundry Agent Service na analýzu vašich predajných údajov:

![Agentic Service In Action](../../../translated_images/sk/agent-service-in-action.34fb465c9a84659e.webp)

Na použitie týchto nástrojov so službou môžeme vytvoriť klienta a definovať nástroj alebo sadu nástrojov. Praktická implementácia môže vyzerať nasledovne v Pythone. LLM bude môcť pozrieť na sadu nástrojov a rozhodnúť sa, či použije vlastnú funkciu používateľa `fetch_sales_data_using_sqlite_query`, alebo zabudovaný Code Interpreter podľa požiadavky používateľa.

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

# Inicializujte sadu nástrojov
toolset = ToolSet()

# Inicializujte agenta na volanie funkcií s funkciou fetch_sales_data_using_sqlite_query a pridajte ho do sady nástrojov
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializujte nástroj Code Interpreter a pridajte ho do sady nástrojov.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4.1-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Aké sú špeciálne úvahy pri použití dizajnového vzoru používania nástrojov na vytvorenie dôveryhodných AI agentov?

Bežným problémom pri dynamicky generovanom SQL vytváranom LLM je bezpečnosť, najmä riziko SQL injekcie alebo škodlivých akcií, ako je vymazanie alebo manipulácia s databázou. Aj keď sú tieto obavy oprávnené, dajú sa efektívne zmierniť správnym nastavením prístupových práv k databáze. Pre väčšinu databáz to znamená nastavenie databázy do režimu iba na čítanie. Pre databázové služby ako PostgreSQL alebo Azure SQL by mala byť pre aplikáciu nastavená rola iba na čítanie (SELECT).

Spustenie aplikácie v bezpečnom prostredí ďalej zvyšuje ochranu. V podnikových scenároch sa dáta zvyčajne získavajú a transformujú z operačných systémov do databázy alebo dátového skladu s režimom iba na čítanie a používateľsky prívetivou schémou. Tento prístup zabezpečuje, že dáta sú bezpečné, optimalizované pre výkon a prístupnosť a že aplikácia má obmedzený prístup iba na čítanie.

## Ukážky kódu

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Máte ďalšie otázky o dizajnovom vzore používania nástrojov?

Pridajte sa do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde sa môžete stretnúť s ostatnými študentmi, zúčastniť sa konzultácií a získať odpovede na svoje otázky týkajúce sa AI agentov.

## Dodatočné zdroje

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop Azure AI Agent Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Workshop viacagentového systému Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Prehľad Microsoft Agent Framework</a>


## Rýchle testovanie tohto agenta (voliteľné)

Po tom, čo sa naučíte nasadzovať agentov v [Lekcii 16](../16-deploying-scalable-agents/README.md), môžete rýchlo otestovať tento lekčný `TravelToolAgent` (či ešte volá svoje nástroje a odpovedá?) pomocou [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Pozrite si [`tests/README.md`](../tests/README.md) pre spôsob spustenia.

## Predchádzajúca lekcia

[Porozumenie agentovým dizajnovým vzorcom](../03-agentic-design-patterns/README.md)

## Nasledujúca lekcia

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->