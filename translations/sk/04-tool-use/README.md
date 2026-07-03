[![Ako navrhnúť dobrých AI agentov](../../../translated_images/sk/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

# Dizajnový vzor používania nástrojov

Nástroje sú zaujímavé, pretože umožňujú AI agentom mať širší rozsah schopností. Namiesto toho, aby agent mal obmedzený súbor akcií, ktoré môže vykonať, pridaním nástroja môže agent vykonávať širokú škálu akcií. V tejto kapitole si pozrieme dizajnový vzor používania nástrojov, ktorý popisuje, ako môžu AI agenti používať konkrétne nástroje na dosiahnutie svojich cieľov.

## Úvod

V tejto lekcii sa pokúsime odpovedať na nasledujúce otázky:

- Čo je dizajnový vzor používania nástrojov?
- Na aké prípady použitia ho možno aplikovať?
- Aké prvky/stavby sú potrebné na implementáciu tohto dizajnového vzoru?
- Aké sú špeciálne úvahy pri používaní dizajnového vzoru používania nástrojov na vytváranie dôveryhodných AI agentov?

## Ciele učenia

Po dokončení tejto lekcie budete schopní:

- Definovať dizajnový vzor používania nástrojov a jeho účel.
- Identifikovať prípady použitia, kde je vhodný tento dizajnový vzor.
- Pochopiť kľúčové prvky potrebné na implementáciu dizajnového vzoru.
- Rozpoznať úvahy na zaistenie dôveryhodnosti AI agentov používajúcich tento dizajnový vzor.

## Čo je dizajnový vzor používania nástrojov?

**Dizajnový vzor používania nástrojov** sa zameriava na to, aby LLM mali schopnosť interagovať s externými nástrojmi na dosiahnutie konkrétnych cieľov. Nástroje sú kód, ktorý môže agent vykonať na vykonávanie akcií. Nástroj môže byť jednoduchá funkcia, ako kalkulačka, alebo API volanie na službu tretej strany, napríklad vyhľadávanie cien akcií alebo predpoveď počasia. V kontexte AI agentov sú nástroje navrhnuté tak, aby ich agenti vykonávali v reakcii na **funkčné volania generované modelom**.

## Na aké prípady použitia ho možno aplikovať?

AI agenti môžu využiť nástroje na dokončenie zložitých úloh, získavanie informácií alebo rozhodovanie. Dizajnový vzor používania nástrojov sa často používa v situáciách vyžadujúcich dynamickú interakciu s externými systémami, ako sú databázy, webové služby alebo interpretory kódu. Táto schopnosť je užitočná pre rôzne prípady použitia vrátane:

- **Dynamické získavanie informácií:** Agenti môžu dotazovať externé API alebo databázy na získanie aktuálnych dát (napr. dotazovanie SQLite databázy na analýzu dát, získavanie cien akcií alebo informácií o počasí).
- **Vykonávanie a interpretácia kódu:** Agenti môžu vykonávať kód alebo skripty na riešenie matematických problémov, generovanie zpráv alebo vykonávanie simulácií.
- **Automatizácia pracovných tokov:** Automatizácia opakujúcich sa alebo viacstupňových pracovných postupov integráciou nástrojov ako plánovače úloh, emailové služby alebo dátové pipeline.
- **Zákaznícka podpora:** Agenti môžu komunikovať so CRM systémami, platformami pre správu tiketov alebo databázami znalostí na riešenie otázok používateľov.
- **Generovanie a úprava obsahu:** Agenti môžu využiť nástroje ako kontroly gramatiky, zhrnovače textu alebo hodnotiace nástroje bezpečnosti obsahu na pomoc pri tvorbe obsahu.

## Aké sú prvky/stavby potrebné na implementáciu dizajnového vzoru používania nástrojov?

Tieto prvky umožňujú AI agentovi vykonávať širokú škálu úloh. Pozrime sa na kľúčové prvky potrebné na implementáciu dizajnového vzoru používania nástrojov:

- **Schémy funkcií/nástrojov**: Podrobné definície dostupných nástrojov vrátane mena funkcie, účelu, požadovaných parametrov a očakávaných výstupov. Tieto schémy umožňujú LLM porozumieť, aké nástroje sú dostupné a ako konštruovať platné požiadavky.

- **Logika vykonávania funkcií**: Určuje, kedy a ako sa nástroje volajú na základe zámeru používateľa a kontextu rozhovoru. Môže obsahovať plánovacie moduly, mechanizmy smerovania alebo podmienené toky určujúce dynamické používanie nástrojov.

- **Systém spracovania správ**: Komponenty spravujúce konverzačný tok medzi vstupmi používateľa, odpoveďami LLM, volaniami nástrojov a ich výstupmi.

- **Rámec integrácie nástrojov**: Infraštruktúra, ktorá spája agenta s rôznymi nástrojmi, či už sú to jednoduché funkcie alebo komplexné externé služby.

- **Spracovanie chýb a validácia**: Mechanizmy na riešenie chýb pri vykonávaní nástrojov, overovanie parametrov a riadenie neočakávaných odpovedí.

- **Správa stavu**: Sleduje kontext rozhovoru, predchádzajúce interakcie s nástrojmi a perzistentné dáta na zabezpečenie konzistencie v rámci viackrokových interakcií.

Ďalej si pozrime volanie funkcií/nástrojov podrobnejšie.

### Volanie funkcií/nástrojov

Volanie funkcií je primárny spôsob, akým umožňujeme veľkým jazykovým modelom (LLM) interagovať s nástrojmi. Často uvidíte používanie výrazov „Funkcia“ a „Nástroj“ zameniteľne, pretože „funkcie“ (bloky znovupoužiteľného kódu) sú „nástroje“, ktoré agenti používajú na vykonávanie úloh. Aby mohol byť kód funkcie vyvolaný, musí LLM porovnať požiadavku používateľa s popisom funkcií. Na tento účel sa LLM odosiela schéma obsahujúca popisy všetkých dostupných funkcií. LLM potom vyberie najvhodnejšiu funkciu pre danú úlohu a vráti jej meno a argumenty. Vybraná funkcia sa zavolá, jej odpoveď sa odošle späť LLM, ktoré následne použije tieto informácie na odpoveď na požiadavku používateľa.

Pre vývojárov, ktorí chcú implementovať volanie funkcií pre agentov, je potrebné:

1. LLM model, ktorý podporuje volanie funkcií
2. Schéma obsahujúca popisy funkcií
3. Kód pre každú opísanú funkciu

Použime príklad zistenia aktuálneho času v meste na ilustráciu:

1. **Inicializovať LLM, ktoré podporuje volanie funkcií:**

   Nie všetky modely podporujú volanie funkcií, preto je dôležité overiť, či LLM, ktoré používate, túto schopnosť má. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podporuje volanie funkcií. Môžeme začať inicializáciou klienta Azure OpenAI.

    ```python
    # Inicializujte klienta Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Vytvoriť schému funkcie**:

   Ďalej definujeme JSON schému, ktorá obsahuje meno funkcie, popis čo funkcia robí, a mená a popisy jej parametrov.
   Túto schému následne odovzdáme klientovi vytvorenému predtým spolu s požiadavkou používateľa o čas v San Franciscu. Dôležité je poznamenať, že sa vracia **volanie nástroja**, **nie** konečná odpoveď na otázku. Ako už bolo spomenuté, LLM vráti meno vybranej funkcie a argumenty, ktoré sa jej odovzdajú.

    ```python
    # Popis funkcie, aby si ju model prečítal
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
  
    # Prvý volanie API: Požiadať model, aby použil funkciu
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

   Keďže LLM vybralo funkciu, ktorá sa má spustiť, je potrebné implementovať a vykonať kód vykonávajúci danú úlohu.
   Môžeme implementovať kód na získanie aktuálneho času v Pythone. Tiež budeme musieť napísať kód, ktorý extrahuje názov a argumenty z response_message na získanie konečného výsledku.

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

Volanie funkcií je základom väčšiny, ak nie všetkých dizajnov používania nástrojov agentov, avšak jeho implementácia od začiatku môže byť niekedy náročná.
Ako sme sa naučili v [Lekcia 2](../../../02-explore-agentic-frameworks) agentické rámce nám poskytujú pripravené stavby na implementáciu používania nástrojov.

## Príklady používania nástrojov s agentickými rámcami

Tu je niekoľko príkladov, ako môžete implementovať dizajnový vzor používania nástrojov pomocou rôznych agentických rámcov:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> je open-source AI rámec na vytváranie AI agentov. Zjednodušuje proces volania funkcií tým, že umožňuje definovať nástroje ako Python funkcie s dekorátorom `@tool`. Rámec spravuje komunikáciu medzi modelom a vaším kódom. Tiež poskytuje prístup k predpripraveným nástrojom ako vyhľadávanie súborov a interpret kódu cez `AzureAIProjectAgentProvider`.

Nasledujúci diagram znázorňuje proces volania funkcií s Microsoft Agent Framework:

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> je novší agentický rámec navrhnutý na to, aby umožnil vývojárom bezpečne vytvárať, nasadzovať a škálovať vysoko kvalitných a rozšíriteľných AI agentov bez potreby spravovať základné výpočtové a úložné zdroje. Je obzvlášť užitočný pre podnikové aplikácie, keďže ide o plne spravovanú službu s bezpečnosťou na úrovni podniku.

V porovnaní s priamym vývojom cez LLM API poskytuje Azure AI Agent Service určité výhody, vrátane:

- Automatické volanie nástrojov – nie je potrebné spracovávať volanie nástroja, vyvolávať ho a spracovávať odpoveď; všetko sa teraz deje na strane servera
- Bezpečne spravované dáta – namiesto správy vlastného stavu konverzácie môžete spoľahnúť na vlákna, ktoré ukladajú všetky potrebné informácie
- Predpripravené nástroje – nástroje na interakciu s vašimi zdrojmi dát, ako Bing, Azure AI Search a Azure Functions.

Nástroje dostupné v Azure AI Agent Service možno rozdeliť do dvoch kategórií:

1. Nástroje pre znalosti:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Základné vyhľadávanie pomocou Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Vyhľadávanie súborov</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Akčné nástroje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Volanie funkcií</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpret kódu</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Nástroje definované v OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nám umožňuje používať tieto nástroje spolu ako `toolset`. Tiež využíva `threads`, ktoré sledujú históriu správ z konkrétnych konverzácií.

Predstavte si, že ste obchodný zástupca vo firme Contoso. Chcete vyvinúť konverzačného agenta, ktorý dokáže odpovedať na otázky týkajúce sa vašich predajných dát.

Nasledujúci obrázok znázorňuje, ako by ste mohli použiť Azure AI Agent Service na analýzu vašich predajných dát:

![Agentic Service In Action](../../../translated_images/sk/agent-service-in-action.34fb465c9a84659e.webp)

Na použitie niektorého z týchto nástrojov so službou môžeme vytvoriť klienta a definovať nástroj alebo sadu nástrojov. Na praktickú implementáciu môžeme použiť nasledujúci Python kód. LLM bude môcť zvážiť toolset a rozhodnúť, či použije používateľom vytvorenú funkciu `fetch_sales_data_using_sqlite_query`, alebo predpripravený interpret kódu podľa požiadavky používateľa.

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

## Aké sú špeciálne úvahy pri používaní dizajnového vzoru používania nástrojov na vytváranie dôveryhodných AI agentov?

Bežnou obavou pri dynamicky generovanom SQL kóde LLM je bezpečnosť, najmä riziko SQL injekcie alebo škodlivých akcií, ako napríklad vymazanie alebo poškodenie databázy. Hoci sú tieto obavy oprávnené, dajú sa efektívne zmierniť správnou konfiguráciou prístupových práv k databáze. Pre väčšinu databáz to znamená nastavenie databázy ako len na čítanie. Pre databázové služby ako PostgreSQL alebo Azure SQL by mala byť aplikácii pridelená rola len na čítanie (SELECT).

Spustenie aplikácie v bezpečnom prostredí ďalej zvyšuje ochranu. V podnikových scenároch sa dáta typicky extrahujú a transformujú z operačných systémov do databázy len na čítanie alebo dátového skladu s používateľsky prívetivou schémou. Tento prístup zabezpečuje, že dáta sú bezpečné, optimalizované pre výkon a dostupnosť a že aplikácia má obmedzený, len na čítanie, prístup.

## Ukážkové kódy

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Máte ďalšie otázky o dizajnových vzoroch používania nástrojov?

Pridajte sa ku komunite [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde môžete stretávať ďalších študentov, zúčastniť sa office hours a získať odpovede na otázky o AI agentoch.

## Ďalšie zdroje

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshopy Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Prehľad Microsoft Agent Framework</a>

## Predchádzajúca lekcia

[Porozumenie agentickým dizajnovým vzorom](../03-agentic-design-patterns/README.md)

## Nasledujúca lekcia
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->