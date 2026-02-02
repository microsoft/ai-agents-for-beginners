[![Kako oblikovati dobre AI agente](../../../translated_images/sl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite na zgornjo sliko za ogled videoposnetka te lekcije)_

# Vzorec oblikovanja uporabe orodij

Orodja so zanimiva, ker omogočajo AI agentom širši spekter zmogljivosti. Namesto da bi agent imel omejen nabor dejanj, ki jih lahko izvede, lahko z dodajanjem orodja agent zdaj izvede širok spekter dejanj. V tem poglavju si bomo ogledali vzorec oblikovanja uporabe orodij, ki opisuje, kako lahko AI agenti uporabljajo posebna orodja za dosego svojih ciljev.

## Uvod

V tej lekciji želimo odgovoriti na naslednja vprašanja:

- Kaj je vzorec oblikovanja uporabe orodij?
- Za katere primere uporabe ga lahko uporabimo?
- Kateri elementi/gradniki so potrebni za implementacijo tega vzorca oblikovanja?
- Kateri so posebni premisleki za uporabo vzorca oblikovanja uporabe orodij za gradnjo zanesljivih AI agentov?

## Cilji učenja

Po zaključku te lekcije boste znali:

- Določiti vzorec oblikovanja uporabe orodij in njegov namen.
- Prepoznati primere uporabe, kjer je vzorec uporabe orodij uporaben.
- Razumeti ključne elemente, potrebne za implementacijo vzorca oblikovanja.
- Prepoznati premisleke za zagotovitev zanesljivosti AI agentov, ki uporabljajo ta vzorec oblikovanja.

## Kaj je vzorec oblikovanja uporabe orodij?

**Vzorec oblikovanja uporabe orodij** se osredotoča na dajanje zmožnosti večjim jezikovnim modelom (LLM), da komunicirajo z zunanjimi orodji za doseganje določenih ciljev. Orodja so koda, ki jo lahko agent izvede za izvajanje dejanj. Orodje je lahko preprosta funkcija, kot je kalkulator, ali pa klic API-ja tretje osebe, kot je iskanje cene delnic ali vremenska napoved. V kontekstu AI agentov so orodja zasnovana tako, da jih agenti izvajajo kot odziv na **funkcijske klice, ki jih generira model**.

## Za katere primere uporabe ga lahko uporabimo?

AI agenti lahko izkoristijo orodja za dokončanje zapletenih opravil, pridobivanje informacij ali sprejemanje odločitev. Vzorec oblikovanja uporabe orodij se pogosto uporablja v scenarijih, ki zahtevajo dinamično interakcijo z zunanjimi sistemi, kot so podatkovne baze, spletne storitve ali tolmači kode. Ta zmožnost je uporabna za različne primere uporabe, vključno z:

- **Dinamično pridobivanje informacij:** Agenti lahko poizvedujejo zunanje API-je ali podatkovne baze za pridobitev ažurnih podatkov (npr. poizvedba SQLite baze za analizo podatkov, pridobivanje cen delnic ali vremenskih informacij).
- **Izvajanje in tolmačenje kode:** Agenti lahko izvajajo kodo ali skripte za reševanje matematičnih problemov, generiranje poročil ali izvajanje simulacij.
- **Avtomatizacija potekov dela:** Avtomatizacija ponavljajočih se ali večstopenjskih potekov dela z integracijo orodij, kot so urniki opravil, storitve e-pošte ali podatkovne cevi.
- **Podpora strankam:** Agenti lahko komunicirajo s CRM sistemi, platformami za upravljanje zahtevkov ali bazo znanja za reševanje poizvedb uporabnikov.
- **Generiranje in urejanje vsebine:** Agenti lahko uporabijo orodja, kot so preverjevalniki slovnice, povzemalniki besedil ali ocenjevalci varnosti vsebine, za pomoč pri ustvarjanju vsebine.

## Kateri elementi/gradniki so potrebni za implementacijo vzorca oblikovanja uporabe orodij?

Ti gradniki omogočajo AI agentu izvajanje širokega nabora nalog. Oglejmo si ključne elemente, potrebne za implementacijo vzorca oblikovanja uporabe orodij:

- **Sheme funkcij/orodij**: Podrobne definicije razpoložljivih orodij, vključno z imenom funkcije, namenom, potrebnimi parametri in pričakovanimi izhodi. Te sheme omogočajo LLM-u, da razume, katera orodja so na voljo in kako sestaviti veljavne zahteve.

- **Logika izvajanja funkcij**: Določa, kako in kdaj se orodja kličejo glede na uporabnikovo namero in kontekst pogovora. To lahko vključuje module za načrtovanje, mehanizme usmerjanja ali pogojne poti, ki dinamično določajo uporabo orodij.

- **Sistem za upravljanje sporočil**: Komponente, ki upravljajo pogovorni tok med uporabniškimi vnosi, odzivi LLM, klici orodij in izhodi orodij.

- **Okvir za integracijo orodij**: Infrastruktura, ki povezuje agenta z različnimi orodji, ne glede na to, ali gre za preproste funkcije ali kompleksne zunanje storitve.

- **Ravnanje z napakami in validacija**: Mehanizmi za obravnavo neuspehov pri izvrševanju orodij, preverjanje parametrov in upravljanje nepričakovanih odgovorov.

- **Upravljanje stanja**: Sledi kontekstu pogovora, prejšnjim interakcijam z orodji in trajnim podatkom za zagotavljanje doslednosti preko večkrokovnih interakcij.

Nato si podrobneje poglejmo klicanje funkcij/orodij.
 
### Klicanje funkcij/orodij

Klicanje funkcij je glavni način, s katerim omogočamo velikim jezikovnim modelom (LLM) interakcijo z orodji. Pogosto boste videli izraze 'funkcija' in 'orodje' uporabljene zamenjavo, saj so 'funkcije' (bloki večkrat uporabne kode) ta 'orodja', ki jih agenti uporabljajo za opravljanje nalog. Da se koda funkcije izvede, mora LLM primerjati uporabnikovo zahtevo z opisom funkcije. Za to pošljemo shemo, ki vsebuje opise vseh razpoložljivih funkcij LLM-u. LLM potom izbere najprimernejšo funkcijo za nalogo in vrne njeno ime ter argumente. Izbrana funkcija se izvede, njen odziv se pošlje nazaj LLM-u, ki nato uporabi informacije za odgovor na uporabnikovo zahtevo.

Za razvijalce, ki želijo implementirati klicanje funkcij za agente, boste potrebovali:

1. Model LLM, ki podpira klicanje funkcij
2. Shemo, ki vsebuje opise funkcij
3. Kodo za vsako opisano funkcijo

Uporabimo primer pridobitve trenutnega časa v mestu:

1. **Inicializirajte LLM, ki podpira klicanje funkcij:**

    Ne vsi modeli podpirajo klicanje funkcij, zato je pomembno preveriti, ali vaš LLM to omogoča. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podpira klicanje funkcij. Začnemo lahko z inicializacijo Azure OpenAI klienta. 

    ```python
    # Inicializirajte Azure OpenAI odjemalca
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Ustvarite shemo funkcije**:

    Nato bomo definirali JSON shemo, ki vsebuje ime funkcije, opis tega, kaj funkcija počne, ter imena in opise njenih parametrov.
    Nato bomo to shemo poslali prejšnje ustvarjenemu klientu skupaj z uporabnikovo zahtevo o iskanju časa v San Franciscu. Pomembno je opozoriti, da je vrnjen rezultat **klic orodja**, **ne** končni odgovor na vprašanje. Kot že omenjeno, LLM vrne ime funkcije, ki jo je izbral za nalogo, in argumente, ki bodo posredovani funkciji.

    ```python
    # Opis funkcije za model za branje
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
  
    # Prvi klic API: Prosite model, da uporabi funkcijo
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Obdelava odgovora modela
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Koda funkcije, ki izvaja nalogo:**

    Ko LLM izbere, katera funkcija se mora izvesti, je treba implementirati in zagnati kodo, ki opravi nalogo.
    Kodo za pridobitev trenutnega časa lahko implementiramo v Pythonu. Prav tako moramo napisati kodo, ki iz odziva (response_message) izlušči ime funkcije in argumente, da dobimo končni rezultat.

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
     # Obravnavaj klice funkcij
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
  
      # Drugi klic API-ja: Dobi končni odgovor iz modela
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

Klicanje funkcij je jedro večine, če ne vseh, vzorcev uporabe orodij agentov, vendar je včasih implementacija od začetka lahko zahtevna.
Kot smo se naučili v [Lekcija 2](../../../02-explore-agentic-frameworks) agentni okviri nam nudijo vnaprej pripravljene gradnike za implementacijo uporabe orodij.
 
## Primeri uporabe orodij z agentnimi okviri

Tukaj je nekaj primerov, kako lahko implementirate vzorec oblikovanja uporabe orodij z različnimi agentnimi okviri:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> je odprtokodni AI okvir za razvijalce .NET, Python in Java, ki delajo z velikimi jezikovnimi modeli (LLM). Poenostavlja proces klicanja funkcij tako, da avtomatično opisuje vaše funkcije in njihove parametre modelu prek postopka <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">seralizacije</a>. Prav tako upravlja dvosmerno komunikacijo med modelom in vašo kodo. Ena od prednosti uporabe agentnega okvira, kot je Semantic Kernel, je, da omogoča dostop do vnaprej pripravljenih orodij, kot sta <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> in <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

Naslednji diagram ponazarja postopek klicanja funkcij s Semantic Kernel:

![function calling](../../../translated_images/sl/functioncalling-diagram.a84006fc287f6014.webp)

V Semantic Kernel so funkcije/orodja imenovane <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Funkcijo `get_current_time`, ki smo jo videli prej, lahko spremenimo v razširitev s tem, da jo naredimo razred, ki vsebuje funkcijo. Prav tako lahko uvozimo dekorator `kernel_function`, ki sprejema opis funkcije. Ko nato ustvarite kernel z GetCurrentTimePlugin, kernel samodejno seralizira funkcijo in njene parametre ter v postopku ustvari shemo za pošiljanje LLM-u.

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

# Ustvari jedro
kernel = Kernel()

# Ustvari vtičnik
get_current_time_plugin = GetCurrentTimePlugin(location)

# Dodaj vtičnik v jedro
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> je novejši agentni okvir, zasnovan za omogočanje razvijalcem, da varno gradijo, uvajajo in razširjajo kakovostne ter prilagodljive AI agente, brez potrebe po upravljanju osnovnih računalniških in podatkovnih virov. Še posebej uporaben je za podjetniške aplikacije, saj gre za v celoti upravljano storitev s podjetniško varnostjo.

V primerjavi z razvojem neposredno z LLM API-jem Azure AI Agent Service ponuja nekaj prednosti, med drugim:

- Avtomatsko klicanje orodij – ni potrebe po ročnem razčlenjevanju klica orodja, izvajanju orodja in obravnavi odziva; vse to je zdaj opravljeno na strežniški strani
- Varno upravljani podatki – namesto da upravljate lasten pogovorni kontekst, lahko zanesete na "threads" (niti), ki shranjujejo vse informacije, ki jih potrebujete
- Orodja takoj pripravna za uporabo – orodja, ki jih lahko uporabite za interakcijo z viri podatkov kot so Bing, Azure AI Search in Azure Functions.

Orodja, ki so na voljo v Azure AI Agent Service, lahko razdelimo v dve kategoriji:

1. Orodja za znanje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Povezava z iskanjem Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Iskanje datotek</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Orodja za dejanja:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Klicanje funkcij</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Tolmač kode</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Orodja definirana z OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Storitev Agent nam omogoča, da ta orodja uporabljamo skupaj kot `toolset` (nabor orodij). Prav tako uporablja `threads` (niti), ki spremljajo zgodovino sporočil iz določenega pogovora.

Predstavljajte si, da ste prodajni agent v podjetju Contoso. Želite razviti pogovornega agenta, ki lahko odgovarja na vprašanja o vaših prodajnih podatkih.

Naslednja slika ponazarja, kako bi lahko uporabili Azure AI Agent Service za analizo vaših prodajnih podatkov:

![Agentic Service In Action](../../../translated_images/sl/agent-service-in-action.34fb465c9a84659e.webp)

Če želite katerokoli od teh orodij uporabiti s storitvijo, lahko ustvarimo klienta in definiramo orodje ali nabor orodij. Za praktično implementacijo lahko uporabimo naslednjo Python kodo. LLM bo lahko pregledal nabor orodij in se odločil, ali bo uporabil funkcijo, ki jo je ustvaril uporabnik, `fetch_sales_data_using_sqlite_query`, ali predhodno zgrajeni tolmač kode, glede na uporabnikovo zahtevo.

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

# Inicializirajte orodjarno
toolset = ToolSet()

# Inicializirajte agenta za klic funkcij s funkcijo fetch_sales_data_using_sqlite_query in jo dodajte v orodjarno
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializirajte orodje Code Interpreter in ga dodajte v orodjarno.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Kateri so posebni premisleki za uporabo vzorca oblikovanja uporabe orodij za gradnjo zanesljivih AI agentov?

Pogosta skrb pri dinamično generiranem SQL-ju s strani LLM-ov je varnost, zlasti tveganje SQL injekcije ali zlonamernih dejanj, kot so brisanje ali spreminjanje baze podatkov. Čeprav so te skrbi upravičene, jih je mogoče učinkovito ublažiti z ustrezno konfiguracijo dovoljenj za dostop do baze podatkov. Za večino podatkovnih baz to vključuje konfiguracijo baze kot samo za branje. Za storitve podatkovnih baz, kot sta PostgreSQL ali Azure SQL, je treba aplikaciji dodeliti vlogo le za branje (SELECT).
Zagon aplikacije v varnem okolju dodatno izboljša zaščito. V podjetniških scenarijih se podatki običajno izločajo in preoblikujejo iz operativnih sistemov v bazo podatkov samo za branje ali skladišče podatkov s prijazno shemo. Ta pristop zagotavlja, da so podatki varni, optimizirani za zmogljivost in dostopnost ter da ima aplikacija omejen, samo za branje dostop.

## Primeri kode

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Imate več vprašanj o uporabi oblikovalskih vzorcev orodja?

Pridružite se [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), da se srečate z drugimi učenci, spremljate pisarne in dobite odgovore na vaša vprašanja o AI agentih.

## Dodatni viri

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Delavnica Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Delavnica Contoso Creative Writer z več agenti</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Vadnica klicanja funkcij v Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Interpreter kode Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Orodja Autogen</a>

## Prejšnja lekcija

[Razumevanje agentnih oblikovalskih vzorcev](../03-agentic-design-patterns/README.md)

## Naslednja lekcija

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve umetne inteligence za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku velja za uradni vir. Za kritične informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->