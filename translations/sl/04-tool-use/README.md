[![Kako oblikovati dobre AI agente](../../../translated_images/sl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite sliko zgoraj za ogled posnetka tega poglavja)_

# Vzorec oblikovanja uporabe orodij

Orodja so zanimiva, saj AI agentom omogočajo širši nabor zmožnosti. Namesto da bi imel agent omejen nabor dejanj, ki jih lahko izvede, lahko z dodajanjem orodja agent zdaj izvaja širok razpon dejanj. V tem poglavju bomo pogledali vzorec oblikovanja uporabe orodij, ki opisuje, kako lahko AI agenti uporabljajo določena orodja za doseganje svojih ciljev.

## Uvod

V tem poglavju želimo odgovoriti na naslednja vprašanja:

- Kaj je vzorec oblikovanja uporabe orodij?
- Za katere primere uporabe je lahko uporabljen?
- Kateri so elementi/gradniki, potrebni za izvedbo vzorca oblikovanja?
- Kateri so posebni premisleki pri uporabi vzorca oblikovanja uporabe orodij za gradnjo zaupanja vrednih AI agentov?

## Cilji učenja

Po zaključku tega poglavja boste znali:

- Določiti vzorec oblikovanja uporabe orodij in njegov namen.
- Prepoznati primere uporabe, kjer je vzorec uporabe orodij ustrezen.
- Razumeti ključne elemente, potrebne za izvedbo vzorca oblikovanja.
- Prepoznati premisleke za zagotavljanje zaupanja vrednosti AI agentov, ki uporabljajo ta vzorec oblikovanja.

## Kaj je vzorec oblikovanja uporabe orodij?

**Vzorec oblikovanja uporabe orodij** se osredotoča na omogočanje LLM-jem, da komunicirajo z zunanjimi orodji za doseganje določenih ciljev. Orodja so koda, ki jo agent lahko izvrši za izvajanje dejanj. Orodje je lahko preprosta funkcija, kot je kalkulator, ali klic API-ja do storitve tretje osebe, kot je iskanje cen delnic ali vremenska napoved. V kontekstu AI agentov so orodja zasnovana tako, da jih agenti izvedejo kot odziv na **modelom ustvarjene klice funkcij**.

## Za katere primere uporabe je lahko uporabljen?

AI agenti lahko izkoristijo orodja za dokončanje zahtevnih nalog, pridobivanje informacij ali sprejemanje odločitev. Vzorec uporabe orodij se pogosto uporablja v scenarijih, ki zahtevajo dinamično interakcijo z zunanjimi sistemi, kot so podatkovne baze, spletne storitve ali interpretatorji kode. Ta zmožnost je uporabna za več različnih primerov uporabe, vključno z:

- **Dinamično pridobivanje informacij:** Agenti lahko poizvedujejo zunanje API-je ali baze podatkov za pridobitev najnovejših podatkov (npr. poizvedba SQLite baze za analizo podatkov, pridobivanje cen delnic ali informacij o vremenu).
- **Izvajanje in interpretacija kode:** Agenti lahko izvajajo kodo ali skripte za reševanje matematičnih problemov, ustvarjanje poročil ali izvajanje simulacij.
- **Avtomatizacija delovnih tokov:** Avtomatizacija ponavljajočih se ali večstopenjskih delovnih tokov z integracijo orodij, kot so načrtovalci opravil, e-poštne storitve ali podatkovne cevi.
- **Podpora strankam:** Agenti lahko komunicirajo s CRM sistemi, platformami za vnos zahtevkov ali bazami znanja za reševanje poizvedb uporabnikov.
- **Ustvarjanje in urejanje vsebin:** Agenti lahko uporabljajo orodja, kot so preverjevalci slovnice, povzemalniki besedil ali ocenjevalci varnosti vsebin, da pomagajo pri ustvarjanju vsebin.

## Kateri so elementi/gradniki, potrebni za izvedbo vzorca uporabe orodij?

Ti gradniki omogočajo AI agentu izvajanje širokega razpona nalog. Poglejmo ključne elemente, potrebne za implementacijo vzorca uporabe orodij:

- **Sheme funkcij/orodij:** Podrobne definicije razpoložljivih orodij, vključno z imenom funkcije, namenom, zahtevanimi parametri in pričakovanimi izhodi. Te sheme omogočajo LLM-ju razumevanje, katera orodja so na voljo in kako sestaviti veljavne zahteve.

- **Logika izvajanja funkcij:** Ureja, kako in kdaj so orodja klicana glede na uporabnikove namene in kontekst pogovora. Lahko vključuje module načrtovalcev, mehanizme usmerjanja ali pogojne tokove, ki dinamično določajo uporabo orodij.

- **Sistem upravljanja sporočil:** Komponente, ki upravljajo potek pogovora med uporabniškimi vnosi, odgovori LLM, klici orodij in izhodi orodij.

- **Okvir za integracijo orodij:** Infrastruktura, ki povezuje agenta z različnimi orodji, naj bodo to preproste funkcije ali kompleksne zunanje storitve.

- **Upravljanje napak in validacija:** Mehanizmi za obravnavo napak pri izvajanju orodij, preverjanje parametrov in upravljanje nepričakovanih odzivov.

- **Upravljanje stanja:** Spremlja kontekst pogovora, prejšnje interakcije z orodji in trajne podatke za zagotavljanje doslednosti v večkrožnih interakcijah.

Nato si podrobneje oglejmo klic funkcij/orodij.
 
### Klic funkcij/orodij

Klic funkcij je glavni način, kako omogočimo velikim jezikovnim modelom (LLM) interakcijo z orodji. Pogosto boste videli, da se ‘funkcija’ in ‘orodje’ uporabljata zamenljivo, ker so ‘funkcije’ (bloki ponovno uporabne kode) ‘orodja’, ki jih agenti uporabljajo za izvajanje nalog. Da se koda funkcije lahko izvede, mora LLM primerjati uporabnikovo zahtevo z opisom funkcije. Za to se LLM-u pošlje shema z opisi vseh razpoložljivih funkcij. LLM nato izbere najprimernejšo funkcijo za nalogo in vrne njeno ime in argumente. Izbrana funkcija se izvede, njen odziv se pošlje nazaj LLM-ju, ki uporablja te podatke za odgovor na uporabnikovo zahtevo.

Za razvijalce, ki želijo uvesti klic funkcij za agente, potrebujete:

1. LLM model, ki podpira klic funkcij  
2. Shemo z opisi funkcij  
3. Kodo za vsako opisano funkcijo  

Uporabimo primer pridobivanja trenutnega časa v mestu kot ilustracijo:

1. **Inicializacija LLM, ki podpira klic funkcij:**

    Ne vsi modeli podpirajo klic funkcij, zato je pomembno preveriti, da model, ki ga uporabljate, to omogoča. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podpira klic funkcij. Začnemo lahko z inicializacijo Azure OpenAI odjemalca.

    ```python
    # Inicializirajte odjemalca Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Ustvarite shemo funkcije:**

    Nato bomo definirali JSON shemo, ki vsebuje ime funkcije, opis, kaj funkcija počne, in imena ter opise parametrov funkcije.  
    To shemo bomo posredovali predhodno ustvarjenemu odjemalcu skupaj z uporabnikovo zahtevo po času v San Franciscu. Pomembno je vedeti, da je **klic orodja** tisto, kar se vrne, **ne** končni odgovor na vprašanje. Kot smo že omenili, LLM vrne ime funkcije, ki jo je izbral za nalogo, in argumente, ki mu bodo posredovani.

    ```python
    # Opis funkcije za model, da bere
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
  
    # Začetno uporabniško sporočilo
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Prvi klic API-ja: Prosi model, naj uporabi funkcijo
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Obdelaj odgovor modela
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Koda funkcije, potrebna za izvedbo naloge:**

    Zdaj, ko je LLM izbral funkcijo, ki jo je treba izvesti, je treba kodo za izvedbo naloge implementirati in zagnati.  
    Kodo za pridobitev trenutnega časa lahko implementiramo v Pythonu. Prav tako bomo morali napisati kodo za izvleček imena in argumentov iz response_message, da dobimo končni rezultat.

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
     # Obdelaj klice funkcij
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
  
      # Drugi klic API-ja: Pridobi končni odgovor iz modela
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

Klic funkcij je srce večine, če ne vseh, vzorcev uporabe orodij za agente, vendar je njegova implementacija iz nič včasih zahtevna.  
Kot smo se naučili v [Lekcija 2](../../../02-explore-agentic-frameworks) nam agentni okvirji nudijo vnaprej pripravljene gradnike za implementacijo uporabe orodij.
 
## Primeri uporabe orodij z agentnimi okvirji

Tukaj je nekaj primerov, kako lahko implementirate vzorec uporabe orodij z različnimi agentnimi okvirji:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> je odprtokodni AI okvir za gradnjo AI agentov. Poenostavlja proces klica funkcij tako, da omogoča definicijo orodij kot Python funkcij z dekoratorjem `@tool`. Okvir upravlja komunikacijo med modelom in vašo kodo. Prav tako omogoča dostop do vnaprej pripravljenih orodij, kot so Iskanje datotek in Interpretator kode preko `AzureAIProjectAgentProvider`.

Naslednja shema prikazuje proces klica funkcij z Microsoft Agent Framework:

![function calling](../../../translated_images/sl/functioncalling-diagram.a84006fc287f6014.webp)

V Microsoft Agent Framework so orodja definirana kot dekorirane funkcije. Prejšnjo funkcijo `get_current_time`, ki smo jo videli, lahko spremenimo v orodje s pomočjo dekoratorja `@tool`. Okvir bo avtomatsko serializiral funkcijo in njene parametre ter ustvaril shemo za pošiljanje LLM-ju.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Ustvari odjemalca
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Ustvari agenta in zaženi z orodjem
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> je novejši agentni okvir, zasnovan za omogočanje razvijalcem, da varno gradijo, nameščajo in skalirajo visokokakovostne in razširljive AI agente brez potrebe po upravljanju osnovnih računalniških in shranjevalnih virov. Še posebej je uporaben za podjetniške aplikacije, saj gre za popolnoma upravljano storitev z varnostjo na ravni podjetja.

V primerjavi z neposrednim razvojem z LLM API-jem Azure AI Agent Service ponuja nekaj prednosti, med drugim:

- Samodejni klic orodij – ni potrebe po ročnem razčlenjevanju klicev orodij, klicanju orodja in upravljanju odzivov; vse to se zdaj izvaja na strežniški strani
- Varno upravljani podatki – namesto upravljanja lastnega stanja pogovora se lahko zanesete na niti, ki hranijo vse potrebne informacije
- Vnaprej pripravljena orodja – orodja, s katerimi lahko komunicirate z viri podatkov, kot so Bing, Azure AI Search in Azure Functions.

Orodja, ki so na voljo v Azure AI Agent Service, lahko razdelimo v dve kategoriji:

1. Orodja za znanje:  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Povezava z Bing iskanjem</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Iskanje datotek</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>  

2. Orodja za akcijo:  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Klic funkcij</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpretator kode</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Orodja definirana z OpenAPI</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>  

Agent Service nam omogoča uporabo teh orodij skupaj kot `orodjarno`. Prav tako uporablja `niti`, ki sledijo zgodovini sporočil iz določenega pogovora.

Predstavljajte si, da ste prodajni agent v podjetju Contoso. Želite razviti pogovornega agenta, ki lahko odgovarja na vprašanja o vaših prodajnih podatkih.

Naslednja slika prikazuje, kako lahko z uporabo Azure AI Agent Service analizirate vaše prodajne podatke:

![Agentic Service In Action](../../../translated_images/sl/agent-service-in-action.34fb465c9a84659e.webp)

Za uporabo katerega koli od teh orodij s storitvijo lahko ustvarimo odjemalca in definiramo orodje ali komplet orodij. Za praktično izvedbo lahko uporabimo naslednjo Python kodo. LLM bo lahko pogledal komplet orodij in se odločil, ali bo uporabil uporabniško ustvarjeno funkcijo `fetch_sales_data_using_sqlite_query` ali vnaprej pripravljeni Interpretator kode, odvisno od uporabnikove zahteve.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # funkcija fetch_sales_data_using_sqlite_query, ki jo najdete v datoteki fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inicializiraj orodjarno
toolset = ToolSet()

# Inicializiraj agenta za klic funkcij z funkcijo fetch_sales_data_using_sqlite_query in jo dodaj orodjarni
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializiraj orodje za interpretacijo kode in ga dodaj orodjarni.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Kateri so posebni premisleki pri uporabi vzorca oblikovanja uporabe orodij za gradnjo zaupanja vrednih AI agentov?

Pogosta skrb pri dinamično generiranem SQL-ju s strani LLM-jev je varnost, zlasti tveganje SQL injekcij ali zlonamernih dejanj, kot so brisanje ali spreminjanje podatkovne baze. Čeprav so te skrbi upravičene, jih je mogoče učinkovito omiliti z ustrezno konfiguracijo dovoljenj za dostop do baze podatkov. Za večino baz podatkov to pomeni konfiguracijo baze kot samo za branje. Za storitve baz podatkov, kot sta PostgreSQL ali Azure SQL, je treba aplikaciji dodeliti vlogo samo za branje (SELECT).

Zagon aplikacije v varnem okolju dodatno poveča zaščito. V podjetniških scenarijih se podatki običajno izvlečejo in transformirajo iz operativnih sistemov v bazo podatkov samo za branje ali podatkovno skladišče z uporabniku prijazno shemo. Ta pristop zagotavlja, da so podatki varni, optimizirani za zmogljivost in dostopnost ter da ima aplikacija omejen, samo bralni dostop.

## Vzorcne kode

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Imate dodatna vprašanja o vzorcih oblikovanja uporabe orodij?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), da spoznate druge učence, obiskujete uradne ure in dobite odgovore na vaša vprašanja o AI agentih.

## Dodatni viri

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Delavnica Azure AI Agent Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Delavnica Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Pregled Microsoft Agent Frameworka</a>

## Prejšnje poglavje

[Razumevanje agentnih vzorcev oblikovanja](../03-agentic-design-patterns/README.md)

## Naslednje poglavje
[Agentni RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->