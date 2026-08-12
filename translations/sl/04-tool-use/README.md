[![Kako oblikovati dobre AI agente](../../../translated_images/sl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite zgornjo sliko za ogled videoposnetka tega gradiva)_

# Vzorec oblikovanja uporabe orodij

Orodja so zanimiva, ker AI agentom omogočajo širši nabor zmožnosti. Namesto da ima agent omejen nabor dejanj, ki jih lahko izvaja, lahko z dodajanjem orodja agent zdaj opravlja širok spekter dejanj. V tem poglavju bomo pogledali vzorec oblikovanja uporabe orodij, ki opisuje, kako lahko AI agenti uporabijo specifična orodja za doseganje svojih ciljev.

## Uvod

V tem gradivu želimo odgovoriti na naslednja vprašanja:

- Kaj je vzorec oblikovanja uporabe orodij?
- V katerih primerih uporabe ga je mogoče uporabiti?
- Kateri so elementi/gradniki, potrebni za izvedbo vzorca oblikovanja?
- Kakšni so posebni premisleki pri uporabi vzorca oblikovanja uporabe orodij za gradnjo zanesljivih AI agentov?

## Cilji učenja

Po zaključku tega gradiva boste lahko:

- Določiti vzorec oblikovanja uporabe orodij in njegov namen.
- Prepoznati primere uporabe, kjer je vzorec oblikovanja uporabe orodij uporaben.
- Razumeti ključne elemente, potrebne za izvedbo vzorca oblikovanja.
- Prepoznati premisleke za zagotavljanje zanesljivosti pri AI agentih, ki uporabljajo ta vzorec oblikovanja.

## Kaj je vzorec oblikovanja uporabe orodij?

**Vzorec oblikovanja uporabe orodij** se osredotoča na omogočanje LLM-jem, da interagirajo z zunanjimi orodji za doseganje specifičnih ciljev. Orodja so koda, ki jo lahko agent izvrši za izvajanje dejanj. Orodje je lahko preprosta funkcija, kot je kalkulator, ali klic API-ja do tretje storitve, kot je iskanje cene delnic ali vremenska napoved. V kontekstu AI agentov so orodja zasnovana tako, da jih agenti izvajajo kot odziv na **klice funkcij, ki jih generira model**.

## V katerih primerih uporabe ga je mogoče uporabiti?

AI agenti lahko uporabijo orodja za dokončanje zapletenih nalog, pridobivanje informacij ali sprejemanje odločitev. Vzorec oblikovanja uporabe orodij se pogosto uporablja v scenarijih, ki zahtevajo dinamično interakcijo z zunanjimi sistemi, kot so baze podatkov, spletne storitve ali tolmači kode. Ta zmožnost je uporabna za številne primere uporabe, vključno z:

- **Dinamično pridobivanje informacij:** Agenti lahko poizvedujejo zunanje API-je ali baze podatkov za pridobivanje posodobljenih podatkov (npr. poizvedba po SQLite bazi za analizo podatkov, pridobivanje cen delnic ali vremenskih podatkov).
- **Izvajanje in tolmačenje kode:** Agenti lahko izvršujejo kodo ali skripte za reševanje matematičnih problemov, generiranje poročil ali izvajanje simulacij.
- **Avtomatizacija potekov dela:** Avtomatizacija ponavljajočih se ali večstopenjskih potekov dela z integracijo orodij, kot so načrtovalci opravil, e-poštne storitve ali podatkovni tokovi.
- **Podpora strankam:** Agenti lahko interagirajo s CRM sistemi, platformami za upravljanje vstopnic ali bazami znanja za reševanje uporabniških poizvedb.
- **Generiranje in urejanje vsebin:** Agenti lahko uporabijo orodja, kot so preverjevalci slovnice, povzemači besedil ali ocenjevalci varnosti vsebin za pomoč pri ustvarjanju vsebin.

## Kateri so elementi/gradniki za izvedbo vzorca oblikovanja uporabe orodij?

Ti gradniki omogočajo AI agentu izvajanje širokega spektra nalog. Poglejmo ključne elemente potrebne za izvedbo vzorca oblikovanja uporabe orodij:

- **Sheme funkcij/orodij**: Podrobne definicije razpoložljivih orodij, vključno z imenom funkcije, namenom, potrebnimi parametri in pričakovanimi izhodi. Te sheme omogočajo LLM-ju razumevanje, katera orodja so na voljo in kako sestaviti veljavne zahteve.

- **Logika izvajanja funkcij**: Določa, kako in kdaj se orodja kličejo glede na uporabnikovo namero in kontekst pogovora. Lahko vključuje načrtovalne module, mehanizme usmerjanja ali pogoje, ki dinamično odločajo o uporabi orodij.

- **Sistem upravljanja sporočil**: Komponente, ki upravljajo tok pogovora med uporabniškimi vnosi, odgovori LLM, klici orodij in izhodi orodij.

- **Okvir za integracijo orodij**: Infrastruktura, ki povezuje agenta z različnimi orodji, naj bodo to preproste funkcije ali kompleksne zunanje storitve.

- **Obravnava napak in validacija**: Mehanizmi za obravnavo napak pri izvajanju orodij, validacijo parametrov in upravljanje nepričakovanih odzivov.

- **Upravljanje stanja**: Sledi kontekstu pogovora, prejšnjim interakcijam z orodji in trajnim podatkom za zagotavljanje doslednosti v večkratnih pogovorih.

Naslednje si poglejmo podrobneje klic funkcij/orodij.
 
### Klic funkcij/orodij

Klic funkcij je glavni način, kako omogočimo velikim jezikovnim modelom (LLM), da interagirajo z orodji. Pogosto boste videli, da se "funkcija" in "orodje" uporabljata izmenično, ker so "funkcije" (bloki ponovno uporabne kode) tista "orodja", ki jih agenti uporabljajo za izvrševanje nalog. Da se izvede koda funkcije, mora LLM primerjati uporabnikovo zahtevo z opisom funkcije. Za to se pošlje shema, ki vsebuje opise vseh razpoložljivih funkcij LLM-ju. LLM nato izbere najprimernejšo funkcijo za nalogo in vrne njeno ime ter argumente. Izbrana funkcija se izvede, njen odziv se pošlje nazaj LLM-ju, ki na podlagi teh informacij odgovori na uporabnikovo zahtevo.

Za razvijalce, ki želijo implementirati klic funkcij za agente, boste potrebovali:

1. Model LLM, ki podpira klic funkcij
2. Shemo z opisi funkcij
3. Kodo za vsako opisano funkcijo

Za ponazoritev uporabimo primer: pridobitev trenutnega časa v mestu.

1. **Inicializirajte LLM, ki podpira klic funkcij:**

    Ne podpirajo vsi modeli klica funkcij, zato je pomembno preveriti, ali LLM, ki ga uporabljate, to podpira. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podpira klic funkcij. Lahko začnemo z inicializacijo OpenAI odjemalca proti Azure OpenAI **Responses API** (stabilna `/openai/v1/` točka — ni potreben `api_version`). 

    ```python
    # Inicializirajte odjemalca OpenAI za Azure OpenAI (API odgovorov, končna točka v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Ustvarite shemo funkcije**:

    Nato bomo definirali JSON shemo, ki vsebuje ime funkcije, opis, kaj funkcija počne, in imena ter opise parametrov funkcije.
    To shemo bomo poslali prej ustvarjenemu klientu skupaj z uporabnikovo zahtevo, da najde čas v San Franciscu. Pomembno je vedeti, da se vrača **klic orodja**, **ne** končni odgovor na vprašanje. Kot smo omenili prej, LLM vrne ime funkcije, ki jo je izbral za nalogo, in argumente, ki mu bodo predani.

    ```python
    # Opis funkcije za model, da prebere (Responses API raven format orodja)
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
  
    # Začetno sporočilo uporabnika
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Prvi klic API: Prosite model, naj uporabi funkcijo
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API vrne klice orodij kot elemente function_call v response.output.
    # Dodajte jih pogovoru, da ima model celoten kontekst v naslednjem koraku.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Koda funkcije, potrebna za izvedbo naloge:**

    Ko je LLM izbral katero funkcijo je treba izvesti, je potrebno implementirati in zagnati kodo, ki izvaja nalogo.
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
    # Obravnava klicev funkcij
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Vrne rezultat orodja kot element function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Drugi klic API-ja: Pridobi končni odgovor iz modela
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

Klic funkcij je v središču večine, če ne vseh, oblikovanj uporabe orodij za agente, vendar pa je lahko njegova izvedba od začetka zahtevna.
Kot smo se naučili v [Lekcija 2](../../../02-explore-agentic-frameworks), agentni ogrodji nam ponujata vnaprej zgrajene gradnike za implementacijo uporabe orodij.
 
## Primeri uporabe orodij z agentnimi ogrodji

Tukaj je nekaj primerov, kako lahko uporabite vzorec oblikovanja uporabe orodij z različnimi agentnimi ogrodji:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> je odprtokodno AI ogrodje za gradnjo AI agentov. Poenostavi postopek uporabe klicev funkcij tako, da omogoča definiranje orodij kot Python funkcije z dekoratorjem `@tool`. Ogrodje upravlja komunikacijo med modelom in vašo kodo. Prav tako omogoča dostop do vnaprej pripravljenih orodij, kot so File Search in Code Interpreter preko `FoundryChatClient`.

Naslednji diagram prikazuje postopek klica funkcij z Microsoft Agent Framework:

![function calling](../../../translated_images/sl/functioncalling-diagram.a84006fc287f6014.webp)

V Microsoft Agent Framework so orodja definirana kot dekorirane funkcije. Funkcijo `get_current_time`, ki smo jo videli prej, lahko pretvorimo v orodje z uporabo dekoratorja `@tool`. Ogrodje bo samodejno serializiralo funkcijo in njene parametre, ter ustvarilo shemo za pošiljanje LLM-ju.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Ustvari odjemalca
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Ustvari agenta in zaženi z orodjem
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> je novejše agentno ogrodje, zasnovano za varno gradnjo, uvajanje in skaliranje visokokakovostnih ter razširljivih AI agentov, brez potrebe po upravljanju osnovnih strojnih in pomnilniških virov. Posebej uporabno je za poslovne aplikacije, saj je to popolnoma upravljana storitev z varnostjo na nivoju podjetja.

V primerjavi z neposrednim razvojem preko LLM API-ja, Microsoft Foundry Agent Service ponuja nekatere prednosti, vključno z:

- Samodejni klic orodij – ni potrebe po ročnem razčlenjevanju klica orodja, izvedbi orodja in obravnavi odziva; vse to se zdaj izvaja na strežniški strani
- Varno upravljani podatki – namesto upravljanja lastnega stanja pogovora lahko zanesete na niti za shranjevanje vseh potrebnih informacij
- Orodja, pripravljena za uporabo – orodja, ki jih lahko uporabite za interakcijo z vašimi podatkovnimi viri, kot so Bing, Azure AI Search in Azure Functions.

Orodja, na voljo v Microsoft Foundry Agent Service, lahko razdelimo v dve kategoriji:

1. Orodja za znanje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Povezava z Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Iskanje po datotekah</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Orodja za dejanja:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Klic funkcij</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Orodja definirana z OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nam omogoča uporabo teh orodij skupaj kot `orodjarno`. Prav tako uporablja `nitke`, ki spremljajo zgodovino sporočil določenega pogovora.

Predstavljajte si, da ste prodajni agent v podjetju Contoso. Želite razviti pogovornega agenta, ki lahko odgovarja na vprašanja o vaših prodajnih podatkih.

Naslednja slika prikazuje, kako bi lahko uporabili Microsoft Foundry Agent Service za analizo vaših prodajnih podatkov:

![Agentna storitev v akciji](../../../translated_images/sl/agent-service-in-action.34fb465c9a84659e.webp)

Za uporabo kateregakoli izmed teh orodij s storitvijo lahko ustvarimo klienta in definiramo orodje ali orodjarno. Da to praktično izvedemo, lahko uporabimo naslednjo kodo v Pythonu. LLM bo lahko pogledal orodjarno in se odločil, ali bo uporabil funkcijo, ki jo je ustvaril uporabnik, `fetch_sales_data_using_sqlite_query`, ali vnaprej izdelan Code Interpreter, glede na uporabnikovo zahtevo.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # funkcija fetch_sales_data_using_sqlite_query, ki jo lahko najdete v datoteki fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inicializiraj nabor orodij
toolset = ToolSet()

# Inicializiraj agent za klic funkcij s funkcijo fetch_sales_data_using_sqlite_query in jo dodaj v nabor orodij
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializiraj Orodje za interpretacijo kode in ga dodaj v nabor orodij.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Kakšni so posebni premisleki pri uporabi vzorca oblikovanja uporabe orodij za gradnjo zanesljivih AI agentov?

Pogosta skrb glede SQL poizvedb, ki jih dinamično generirajo LLM-ji, je varnost, zlasti tveganje SQL injekcij ali zlonamernih dejanj, kot je brisanje ali spreminjanje baze podatkov. Čeprav so te skrbi upravičene, jih lahko učinkovito omilimo z ustrezno konfiguracijo dostopnih dovoljenj do baze podatkov. Za večino baz je to konfiguracija baze kot samo za branje. Pri baznih storitvah kot sta PostgreSQL ali Azure SQL, naj bi bila aplikacija dodeljena vlogi samo za branje (SELECT).

Zagon aplikacije v varnem okolju dodatno izboljša zaščito. V podjetniških scenarijih se podatki običajno pridobivajo in transformirajo iz operativnih sistemov v bazo podatkov samo za branje ali podatkovno skladišče s prijazno shemo. Ta pristop zagotavlja, da so podatki varni, optimizirani za zmogljivost in dostopnost, ter da ima aplikacija omejen, samo za branje dostop.

## Primeri kode

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Imate več vprašanj o vzorcih oblikovanja uporabe orodij?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da se srečate z drugimi učenci, udeležite ur uradnih ur in dobite odgovore na vprašanja o AI agentih.

## Dodatni viri

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Delavnica Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Delavnica Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Pregled Microsoft Agent Framework</a>


## Preizkušanje osnovne funkcionalnosti tega agenta (neobvezno)

Ko se naučite nameščati agente v [Lekcija 16](../16-deploying-scalable-agents/README.md), lahko osnovno preizkusite `TravelToolAgent` iz te lekcije (ali še vedno kliče svoja orodja in odgovarja?) s pomočjo [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Za navodila o zagonu glejte [`tests/README.md`](../tests/README.md).

## Prejšnja lekcija

[Razumevanje agentnih dizajnerskih vzorcev](../03-agentic-design-patterns/README.md)

## Naslednja lekcija

[Agentni RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->