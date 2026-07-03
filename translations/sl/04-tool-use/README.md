[![Kako oblikovati dobre AI agente](../../../translated_images/sl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite na sliko zgoraj, da si ogledate video te lekcije)_

# Vzorec oblikovanja uporabe orodij

Orodja so zanimiva, ker omogočajo AI agentom širši nabor zmožnosti. Namesto da ima agent omejen nabor dejanj, ki jih lahko izvede, lahko z dodajanjem orodij agent zdaj izvaja širok nabor dejanj. V tem poglavju bomo pogledali vzorec oblikovanja uporabe orodij, ki opisuje, kako lahko AI agenti uporabljajo določena orodja za doseganje svojih ciljev.

## Uvod

V tej lekciji bomo poskušali odgovoriti na naslednja vprašanja:

- Kaj je vzorec oblikovanja uporabe orodij?
- Za katere primere uporabe ga lahko uporabimo?
- Kateri elementi/gradniki so potrebni za implementacijo tega vzorca oblikovanja?
- Katere posebne vidike je treba upoštevati pri uporabi vzorca oblikovanja uporabe orodij za izdelavo zaupanja vrednih AI agentov?

## Cilji učenja

Po zaključku te lekcije boste lahko:

- Opredelili vzorec oblikovanja uporabe orodij in njegov namen.
- Prepoznali primere uporabe, kjer je vzorec uporabe orodij uporaben.
- Razumeli ključne elemente, potrebne za implementacijo vzorca oblikovanja.
- Prepoznali vidike za zagotavljanje zaupanja vrednih AI agentov, ki uporabljajo ta vzorec oblikovanja.

## Kaj je vzorec oblikovanja uporabe orodij?

**Vzorec oblikovanja uporabe orodij** se osredotoča na to, da LLM-jem omogoči interakcijo z zunanjimi orodji za dosego določenih ciljev. Orodja so koda, ki jo agent lahko izvede za izvajanje dejanj. Orodje je lahko preprosta funkcija, kot je kalkulator, ali klic API-ju tretje osebe, kot je poizvedba o ceni delnic ali vremenska napoved. V kontekstu AI agentov so orodja zasnovana tako, da jih agenti izvajajo kot odgovor na **klice funkcij, ustvarjene z modelom**.

## Za katere primere uporabe ga lahko uporabimo?

AI agenti lahko izkoriščajo orodja za dokončanje zapletenih nalog, pridobivanje informacij ali sprejemanje odločitev. Vzorec uporabe orodij se pogosto uporablja v scenarijih, ki zahtevajo dinamično interakcijo z zunanjimi sistemi, kot so baze podatkov, spletne storitve ali razlagalniki kode. Ta sposobnost je uporabna za številne različne primere uporabe, vključno z:

- **Dinamično pridobivanje informacij:** Agenti lahko poizvedujejo po zunanjih API-jih ali bazah podatkov za pridobivanje ažurnih podatkov (npr. poizvedba po SQLite bazi za analizo podatkov, pridobivanje cen delnic ali vremenskih informacij).
- **Izvajanje in interpretacija kode:** Agenti lahko izvajajo kodo ali skripte za reševanje matematičnih problemov, generiranje poročil ali izvajanje simulacij.
- **Avtomatizacija delovnih tokov:** Avtomatiziranje ponavljajočih se ali večstopenjskih delovnih tokov z integracijo orodij, kot so načrtovalci nalog, e-poštne storitve ali podatkovni tokovi.
- **Podpora strankam:** Agenti lahko komunicirajo s CRM sistemi, platformami za vstopnice ali bazo znanja za reševanje uporabniških poizvedb.
- **Generiranje in urejanje vsebin:** Agenti lahko uporabijo orodja, kot so preverjevalci slovnice, povzemači besedil ali ocenjevalci varnosti vsebin, za pomoč pri ustvarjanju vsebin.

## Kateri elementi/gradniki so potrebni za implementacijo vzorca uporabe orodij?

Ti gradniki AI agentu omogočajo izvajanje širokega spektra nalog. Poglejmo ključne elemente, potrebne za implementacijo vzorca uporabe orodij:

- **Sheme funkcij/orodij**: Podrobne definicije razpoložljivih orodij, vključno z imenom funkcije, namenom, potrebnimi parametri in pričakovanimi izhodi. Te sheme omogočajo LLM-ju razumevanje, katera orodja so na voljo in kako sestaviti veljavne zahteve.

- **Logika izvajanja funkcij**: Določa, kako in kdaj se orodja kličejo glede na uporabnikovo namero in kontekst pogovora. To lahko vključuje module načrtovalcev, mehanizme usmerjanja ali pogojne tokove, ki dinamično določajo uporabo orodij.

- **Sistem upravljanja sporočil**: Komponente, ki upravljajo potek pogovora med uporabniškimi vnosi, odgovori LLM-ja, klici orodij in izhodi orodij.

- **Okvir za integracijo orodij**: Infrastruktura, ki povezuje agenta z različnimi orodji, naj bodo to preproste funkcije ali kompleksne zunanje storitve.

- **Upravljanje napak in preverjanje veljavnosti**: Mehanizmi za upravljanje z napakami pri izvajanju orodij, preverjanje parametrov in obvladovanje nepričakovanih odgovorov.

- **Upravljanje stanja**: Sledi kontekstu pogovora, prejšnjim interakcijam z orodji in trajnim podatkom za zagotavljanje doslednosti skozi večkrožne interakcije.

Nato si podrobneje poglejmo klic funkcij/orodij.
 
### Klic funkcij/orodij

Klic funkcij je glavni način, s katerim omogočamo velikim jezikovnim modelom (LLM) interakcijo z orodji. Pogosto boste videli, da se 'funkcija' in 'orodje' uporabljata izmenično, ker so 'funkcije' (bloki ponovno uporabne kode) 'orodja', ki jih agenti uporabljajo za izvajanje nalog. Da se lahko koda funkcije izvede, mora LLM primerjati uporabnikovo zahtevo s opisom funkcije. Za to se LLM-ju pošlje shema, ki vsebuje opise vseh razpoložljivih funkcij. LLM nato izbere najprimernejšo funkcijo za nalogo in vrne njeno ime ter argumente. Izbrana funkcija se izvede, njen odgovor pa se pošlje nazaj LLM-ju, ki uporabi informacije za odgovor uporabnikovi zahtevi.

Za razvijalce, ki želijo implementirati klic funkcij za agente, boste potrebovali:

1. Model LLM, ki podpira klic funkcij
2. Shemo, ki vsebuje opise funkcij
3. Kodo za vsako opisano funkcijo

Uporabimo primer pridobivanja trenutnega časa v mestu za ponazoritev:

1. **Inicializirajte LLM, ki podpira klic funkcij:**

    Ne vsi modeli podpirajo klic funkcij, zato je pomembno preveriti, ali vaš LLM to podpira. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podpira klic funkcij. Začnemo lahko z inicializacijo Azure OpenAI odjemalca.

    ```python
    # Inicializirajte odjemalca Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Ustvarite shemo funkcije**:

    Nato bomo definirali JSON shemo, ki vsebuje ime funkcije, opis tega, kaj funkcija počne, in imena ter opise parametrov funkcije.
    To shemo bomo nato posredovali odjemalcu, ki smo ga prej ustvarili, skupaj z uporabnikovo zahtevo, da najde čas v San Franciscu. Pomembno je vedeti, da je **klic orodja** tisto, kar se vrne, **ne** končni odgovor na vprašanje. Kot je bilo omenjeno prej, LLM vrne ime funkcije, ki jo je izbral za nalogo, in argumente, ki mu bodo posredovani.

    ```python
    # Opis funkcije za branje modela
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
  
    # Začetno sporočilo uporabnika
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Prvi klic API-ja: Prosite model, naj uporabi funkcijo
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Obdelava modelovega odgovora
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

    Ko je LLM izbral, katero funkcijo je treba zagnati, je treba implementirati in izvesti kodo, ki nalogo opravi.
    Kodo za pridobitev trenutnega časa bomo implementirali v Pythonu. Prav tako bo treba napisati kodo za izvleček imena in argumentov iz `response_message`, da pridobimo končni rezultat.

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
  
      # Drugi klic API: Pridobi končni odgovor iz modela
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

Klic funkcij je v središču večine, če ne vseh, vzorcev uporabe orodij agentov, vendar je včasih implementacija iz nič lahko zahtevna.
Kot smo se naučili v [Lekcija 2](../../../02-explore-agentic-frameworks) agentni okviru nam ponujajo vnaprej izdelane gradnike za implementacijo uporabe orodij.
 
## Primeri uporabe orodij z agentnimi okviri

Tukaj je nekaj primerov, kako lahko implementirate vzorec oblikovanja uporabe orodij z uporabo različnih agentnih okvirov:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> je odprtokodni AI okvir za izdelavo AI agentov. Poenostavi proces klica funkcij tako, da omogoča definiranje orodij kot Python funkcij z dekoratorjem `@tool`. Okvir upravlja komunikacijo med modelom in vašo kodo. Prav tako omogoča dostop do vnaprej izdelanih orodij, kot sta File Search in Code Interpreter, prek `AzureAIProjectAgentProvider`.

Naslednji diagram ponazarja postopek klica funkcij z Microsoft Agent Framework:

![function calling](../../../translated_images/sl/functioncalling-diagram.a84006fc287f6014.webp)

V Microsoft Agent Framework so orodja definirana kot dekorirane funkcije. Funkcijo `get_current_time`, ki smo jo videli prej, lahko spremenimo v orodje z uporabo dekoratorja `@tool`. Okvir bo samodejno serializiral funkcijo in njene parametre ter ustvaril shemo za pošiljanje LLM-ju.

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

# Ustvari agenta in ga zaženi s orodjem
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> je novejši agentni okvir, zasnovan za omogočanje razvijalcem, da varno gradijo, uvajajo in skalirajo visokokakovostne in razširljive AI agente, brez potrebe po upravljanju osnovnih virov računalništva in shranjevanja. Še posebej je uporaben za poslovne aplikacije, saj gre za popolnoma upravljano storitev z varnostjo na ravni podjetja.

V primerjavi z razvojem neposredno z LLM API-jem Azure AI Agent Service ponuja nekatere prednosti, vključno z:

- Avtomatski klic orodij – ni več potrebe po analizi klica orodja, izvajanju orodja in upravljanju odgovora; vse to se zdaj izvaja na strežniški strani
- Varnostno upravljani podatki – namesto upravljanja lastnega stanja pogovora se lahko zanesete na niti, ki shranjujejo vse potrebne informacije
- Orodja pripravljena za uporabo – orodja, s katerimi lahko komunicirate z vašimi viri podatkov, kot so Bing, Azure AI Search in Azure Functions.

Orodja, na voljo v Azure AI Agent Service, lahko razdelimo v dve kategoriji:

1. Orodja za znanje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Pridobivanje znanja z Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Iskanje datotek</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Orodja za dejanja:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Klic funkcij</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kodu interpretator</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Orodja definirana z OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nam omogoča, da ta orodja uporabljamo skupaj kot `toolset`. Uporablja tudi `niti`, ki beležijo zgodovino sporočil iz določenega pogovora.

Predstavljajte si, da ste prodajni agent v podjetju Contoso. Želite razviti pogovornega agenta, ki lahko odgovarja na vprašanja o vaših prodajnih podatkih.

Naslednja slika ponazarja, kako bi lahko z Azure AI Agent Service analizirali vaše prodajne podatke:

![Agentic Service In Action](../../../translated_images/sl/agent-service-in-action.34fb465c9a84659e.webp)

Za uporabo katerega koli od teh orodij s storitvijo lahko ustvarimo odjemalca in definiramo orodje ali nabor orodij. Za praktično implementacijo lahko uporabimo naslednjo kodo v Pythonu. LLM bo lahko pregledal `toolset` in se odločil, ali bo uporabil uporabniško ustvarjeno funkcijo `fetch_sales_data_using_sqlite_query` ali vnaprej izdelan Code Interpreter glede na zahtevo uporabnika.

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

# Inicializiraj orodja
toolset = ToolSet()

# Inicializiraj funkcijskega agenta klicanja s funkcijo fetch_sales_data_using_sqlite_query in jo dodaj orodnemu naboru
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializiraj orodje za interpretacijo kode in ga dodaj orodnemu naboru.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Katere posebne vidike je treba upoštevati pri uporabi vzorca oblikovanja uporabe orodij za izdelavo zaupanja vrednih AI agentov?

Pogosto skrb glede dinamično generiranega SQL-ja z LLM-ji je varnost, zlasti tveganje SQL inekcij ali zlonamernih dejanj, kot je brisanje ali spreminjanje baze podatkov. Čeprav so te skrbi upravičene, jih je mogoče učinkovito ublažiti z ustrezno konfiguracijo dovoljenj za dostop do baze podatkov. Za večino baz podatkov to vključuje konfiguracijo baze kot samo za branje. Za storitve baz podatkov, kot so PostgreSQL ali Azure SQL, naj ima aplikacija dodeljeno vlogo samo za branje (SELECT).

Zagon aplikacije v varnem okolju še dodatno poveča zaščito. V poslovnih scenarijih se podatki običajno ekstrahirajo in transformirajo iz operativnih sistemov v bazo podatkov samo za branje ali podatkovno skladišče z uporabniku prijazno shemo. Ta pristop zagotavlja, da so podatki varni, optimizirani za zmogljivost in dostopnost, ter da ima aplikacija omejen dostop samo za branje.

## Primeri kode

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Imate več vprašanj o vzorcih uporabe orodij?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kjer se lahko srečate z ostalimi učenci, udeležite ur svetovalcev in dobite odgovore na vaša vprašanja o AI agentih.

## Dodatni viri

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Delavnica Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Delavnica Contoso Creative Writer z več agenti</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Pregled Microsoft Agent Framework</a>

## Prejšnja lekcija

[Razumevanje agentnih vzorcev oblikovanja](../03-agentic-design-patterns/README.md)

## Naslednja lekcija
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->