[![Kako oblikovati dobre AI agente](../../../translated_images/sl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite zgornjo sliko za ogled videa te lekcije)_

# Vzorec oblikovanja uporabe orodij

Orodja so zanimiva, ker AI agentom omogočajo širši nabor zmožnosti. Namesto da ima agent omejen nabor dejanj, ki jih lahko izvede, lahko z dodajanjem orodja agent zdaj izvaja širok spekter dejanj. V tem poglavju bomo pogledali vzorec oblikovanja uporabe orodij, ki opisuje, kako AI agenti lahko uporabijo določena orodja za doseganje svojih ciljev.

## Uvod

V tej lekciji želimo odgovoriti na naslednja vprašanja:

- Kaj je vzorec oblikovanja uporabe orodij?
- Za katere primere uporabe se lahko uporablja?
- Kateri elementi/gradniki so potrebni za implementacijo vzorca oblikovanja?
- Kateri posebni premisleki so potrebni za uporabo vzorca uporabe orodij za gradnjo zanesljivih AI agentov?

## Cilji učenja

Po zaključku te lekcije boste znali:

- Določiti vzorec oblikovanja uporabe orodij in njegov namen.
- Prepoznati primere uporabe, kjer je vzorec uporabe orodij uporaben.
- Razumeti ključne elemente, potrebne za implementacijo vzorca oblikovanja.
- Prepoznati premisleke za zagotavljanje zanesljivosti AI agentov, ki uporabljajo ta vzorec.

## Kaj je vzorec oblikovanja uporabe orodij?

**Vzorec oblikovanja uporabe orodij** se osredotoča na to, da LLM-jem omogoči interakcijo z zunanjimi orodji za doseganje specifičnih ciljev. Orodja so koda, ki jo agent lahko izvede za izvajanje dejanj. Orodje je lahko preprosta funkcija, kot je kalkulator, ali klic API-ja tretje strani, na primer iskanje cen delnic ali vremenska napoved. V kontekstu AI agentov so orodja zasnovana tako, da jih agenti izvajajo v odziv na **klice funkcij, ki jih generira model**.

## Za katere primere uporabe se lahko uporablja?

AI agenti lahko izkoristijo orodja za dokončanje zapletenih nalog, pridobivanje informacij ali sprejemanje odločitev. Vzorec uporabe orodij se pogosto uporablja v scenarijih, ki zahtevajo dinamično interakcijo z zunanjimi sistemi, kot so baze podatkov, spletne storitve ali tolmači kode. Ta zmožnost je uporabna za številne različne primere uporabe, vključno z:

- **Dinamično pridobivanje informacij:** Agenti lahko poizvedujejo zunanje API-je ali baze podatkov za pridobitev ažurnih podatkov (npr. poizvedbe po SQLite bazi za analizo podatkov, pridobivanje cen delnic ali vremenskih informacij).
- **Izvajanje in interpretacija kode:** Agenti lahko izvajajo kodo ali skripte za reševanje matematičnih problemov, generiranje poročil ali izvajanje simulacij.
- **Avtomatizacija delovnih tokov:** Avtomatizacija ponavljajočih se ali večstopenjskih delovnih tokov z integracijo orodij, kot so načrtovalci opravil, e-poštne storitve ali podatkovni cevovodi.
- **Podpora strankam:** Agenti lahko komunicirajo s CRM sistemi, platformami za ticketing ali bazo znanja za reševanje uporabniških poizvedb.
- **Generiranje in urejanje vsebin:** Agenti lahko uporabijo orodja, kot so preverjevalniki slovnice, povzemalci besedil ali ocenjevalci varnosti vsebine, za pomoč pri ustvarjanju vsebin.

## Kateri elementi/gradniki so potrebni za implementacijo vzorca uporabe orodij?

Ti gradniki agentu AI omogočajo izvajanje širokega spektra nalog. Oglejmo si ključne elemente, potrebne za implementacijo vzorca uporabe orodij:

- **Sheme funkcij/orodij**: Podrobne definicije razpoložljivih orodij, vključno z imenom funkcije, namenom, potrebnimi parametri in pričakovanimi izhodi. Te sheme omogočajo LLM-ju, da razume, katera orodja so na voljo in kako sestaviti veljavne zahteve.

- **Logika izvajanja funkcij**: Določa, kako in kdaj se orodja kličejo glede na uporabnikov namen in kontekst pogovora. Lahko vključuje module načrtovalca, mehanizme usmerjanja ali pogojne poti, ki dinamično določajo uporabo orodij.

- **Sistem za upravljanje sporočil**: Komponente, ki upravljajo potek pogovora med uporabniškimi vnosi, odgovori LLM, klici orodij in izhodi orodij.

- **Okvir za integracijo orodij**: Infrastruktura, ki povezuje agenta z različnimi orodji, ne glede na to, ali gre za preproste funkcije ali kompleksne zunanje storitve.

- **Obdelava napak in validacija**: Mehanizmi za upravljanje z neuspehi pri izvajanju orodij, preverjanje parametrov in upravljanje nepričakovanih odgovorov.

- **Upravljanje stanja**: Sledi kontekstu pogovora, prejšnjim interakcijam z orodji in trajnim podatkom, da zagotovi doslednost v večkrogovnih interakcijah.

Nato si podrobneje poglejmo klic funkcij/orodij.

### Klic funkcij/orodij

Klic funkcij je primarni način, s katerim omogočamo velikim jezikovnim modelom (LLM-jem) interakcijo z orodji. Pojma 'Funkcija' in 'Orodje' se pogosto uporabljata izmenično, ker so 'funkcije' (bloki ponovno uporabne kode) tista 'orodja', ki jih agenti uporabljajo za izvajanje nalog. Da se lahko koda funkcije izvede, mora LLM primerjati uporabnikovo zahtevo s opisom funkcij. Za to se pošlje LLM-ju shema, ki vsebuje opise vseh razpoložljivih funkcij. Nato LLM izbere najbolj primerno funkcijo za nalogo in vrne njeno ime in argumente. Izbrana funkcija se izvede, njen odgovor se pošlje nazaj LLM-ju, ki uporabi informacije za odgovor na uporabnikovo zahtevo.

Za razvijalce, ki želijo implementirati klic funkcij za agente, potrebujete:

1. Model LLM, ki podpira klic funkcij
2. Shemo z opisi funkcij
3. Kodo za vsako opisano funkcijo

Uporabimo primer pridobivanja trenutnega časa v mestu za ponazoritev:

1. **Inicializirajte LLM, ki podpira klic funkcij:**

    Ne vsi modeli podpirajo klic funkcij, zato je pomembno preveriti, ali vaš LLM to podpira. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podpira klic funkcij. Začnemo lahko z inicializacijo Azure OpenAI odjemalca.

    ```python
    # Inicializirajte Azure OpenAI odjemalca
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Ustvarite shemo funkcije**:

    Nato bomo definirali JSON shemo, ki vsebuje ime funkcije, opis, kaj funkcija počne, ter imena in opise parametrov funkcije. To shemo bomo nato posredovali prej ustvarjenemu odjemalcu skupaj z uporabnikovo zahtevo za ugotovitev časa v San Franciscu. Pomembno je, da je vrnjen **klic orodja**, **ne** končni odgovor na vprašanje. Kot smo že omenili, LLM vrne ime funkcije, ki jo je izbral za nalogo, in argumente, ki ji bodo poslani.

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
  
    # Začetno sporočilo uporabnika
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Prvi klic API-ja: Prosi model, naj uporabi funkcijo
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Obdelaj modelov odgovor
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

    Ko je LLM izbral, katero funkcijo je potrebno zagnati, je potrebno implementirati in izvesti kodo, ki izvaja nalogo. Kodo za pridobitev trenutnega časa lahko izvedemo v Pythonu. Prav tako bomo morali napisati kodo za izvlečenje imena in argumentov iz sporočila odgovora, da dobimo končni rezultat.

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
  
      # Drugi klic API-ja: Pridobi končni odgovor od modela
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

Klic funkcij je srce večine, če ne vseh, oblikovanj uporabe orodij agentov, vendar je njegova implementacija iz nič lahko včasih zahtevna. Kot smo se naučili v [Lekcija 2](../../../02-explore-agentic-frameworks) nam agentni okviri nudijo vnaprej pripravljene gradnike za implementacijo uporabe orodij.

## Primeri uporabe orodij z agentnimi okviri

Tukaj je nekaj primerov, kako lahko implementirate vzorec oblikovanja uporabe orodij z različnimi agentnimi okviri:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> je odprtokodni AI okvir za gradnjo AI agentov. Poenostavlja proces klica funkcij, saj vam omogoča definiranje orodij kot Python funkcij z dekoratorjem `@tool`. Okvir upravlja dvosmerno komunikacijo med modelom in vašo kodo. Prav tako omogoča dostop do vnaprej izdelanih orodij, kot sta File Search in Code Interpreter, prek `AzureAIProjectAgentProvider`.

Naslednji diagram ponazarja proces klica funkcij z Microsoft Agent Framework:

![function calling](../../../translated_images/sl/functioncalling-diagram.a84006fc287f6014.webp)

V Microsoft Agent Framework so orodja definirana kot dekorirane funkcije. Funkcijo `get_current_time`, ki smo jo videli prej, lahko spremenimo v orodje z uporabo dekoratorja `@tool`. Okvir bo samodejno serializiral funkcijo in njene parametre ter ustvaril shemo, ki se pošlje LLM-ju.

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

# Ustvari agenta in ga zaženi s pripomočkom
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> je novejši agentni okvir, namenjen razvijalcem za varno gradnjo, uvajanje in skaliranje visokokakovostnih ter razširljivih AI agentov brez potrebe po upravljanju osnovnih računalniških in shrambnih virov. Posebej je uporaben za podjetniške aplikacije, saj gre za popolnoma upravljano storitev s podjetniško varnostjo.

V primerjavi z razvojem neposredno z LLM API-jem, Azure AI Agent Service ponuja nekaj prednosti, vključno z:

- Samodejnim klicem orodij – ni potrebe po analizi klica orodja, njegovi izvedbi in obdelavi odgovora; vse to se zdaj izvaja na strežniku
- Varno upravljanimi podatki – namesto upravljanja lastnega stanja pogovora, lahko zaupate nitim za shranjevanje vseh potrebnih informacij
- Orodja takoj pri roki – Orodja za interakcijo z vašimi podatkovnimi viri, kot so Bing, Azure AI Search in Azure Functions.

Razpoložljiva orodja v Azure AI Agent Service lahko razdelimo v dve kategoriji:

1. Orodja znanja:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Navezava na Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Iskanje datotek</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Orodja akcij:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Klic funkcij</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Orodja definirana z OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nam omogoča uporabo teh orodij skupaj kot `toolset`. Uporablja tudi `niti`, ki sledijo zgodovini sporočil določenega pogovora.

Predstavljajte si, da ste prodajni agent v podjetju Contoso. Želite razviti pogovornega agenta, ki zna odgovarjati na vprašanja o vaših prodajnih podatkih.

Naslednja slika ponazarja, kako bi lahko uporabili Azure AI Agent Service za analizo vaših prodajnih podatkov:

![Agentic Service In Action](../../../translated_images/sl/agent-service-in-action.34fb465c9a84659e.webp)

Za uporabo katerega koli izmed teh orodij z storitvijo lahko ustvarimo odjemalca in definiramo orodje ali nabor orodij. Za praktično implementacijo lahko uporabimo naslednjo Python kodo. LLM bo lahko pogledal nabor orodij in se odločil, ali bo uporabil uporabnikovo funkcijo `fetch_sales_data_using_sqlite_query` ali vnaprej izdelan Code Interpreter, odvisno od uporabnikove zahteve.

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

# Inicializiraj agent za klic funkcij s funkcijo fetch_sales_data_using_sqlite_query in jo dodaj v orodja
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializiraj orodje Code Interpreter in ga dodaj v orodja.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Kateri posebni premisleki so potrebni za uporabo vzorca uporabe orodij za gradnjo zanesljivih AI agentov?

Pogosta skrb pri dinamično generiranem SQL-ju z LLM-ji je varnost, zlasti tveganje SQL vbrizgavanja ali zlonamernih dejanj, kot so brisanje ali spreminjanje baze podatkov. Čeprav so te skrbi upravičene, jih je mogoče učinkovito omiliti z ustreznim konfiguriranjem dovoljenj za dostop do baze podatkov. Za večino baz podatkov to vključuje konfiguracijo baze kot samo za branje. Za storitve baz podatkov, kot so PostgreSQL ali Azure SQL, naj ima aplikacija dodeljeno samo vlogo za branje (SELECT).

Zagon aplikacije v varnem okolju dodatno povečuje zaščito. V podjetniških scenarijih se podatki običajno izločijo in predelajo iz operativnih sistemov v bazo podatkov ali skladišče podatkov samo za branje z uporabniku prijazno shemo. Ta pristop zagotavlja, da so podatki varni, optimizirani za učinkovitost in dostopnost ter da ima aplikacija omejen, samo za branje dostop.

## Primeri kode

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Imate več vprašanj o vzorcih uporabe orodij?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), da se srečate z drugimi učenci, udeležite ur vodenja in dobite odgovore na vaša vprašanja o AI agentih.

## Dodatni viri

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Delavnica Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Delavnica</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Pregled Microsoft Agent Framework</a>

## Prejšnja lekcija

[Razumevanje agentnih vzorcev oblikovanja](../03-agentic-design-patterns/README.md)

## Naslednja lekcija
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo profesionalen prevod, opravljen s strani človeka. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->