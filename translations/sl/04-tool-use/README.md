[![Kako oblikovati dobre AI agente](../../../translated_images/sl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknite zgornjo sliko za ogled videa te lekcije)_

# Vzorec oblikovanja uporabe orodij

Orodja so zanimiva, ker omogočajo AI agentom širši nabor zmogljivosti. Namesto da bi imel agent omejen nabor dejanj, ki jih lahko izvede, lahko z dodajanjem orodja agent zdaj opravlja širok spekter dejanj. V tem poglavju si bomo ogledali Vzorec oblikovanja uporabe orodij, ki opisuje, kako lahko AI agenti uporabljajo določena orodja za doseganje svojih ciljev.

## Uvod

V tej lekciji želimo odgovoriti na naslednja vprašanja:

- Kaj je vzorec oblikovanja uporabe orodij?
- Za katere primere uporabe ga lahko uporabimo?
- Kateri so elementi/gradniki, potrebni za implementacijo vzorca?
- Katere posebne premisleke moramo upoštevati pri uporabi vzorca za gradnjo zaupanja vrednih AI agentov?

## Cilji učenja

Po zaključku te lekcije boste znali:

- Opredeliti vzorec oblikovanja uporabe orodij in njegov namen.
- Prepoznati primere uporabe, kjer je vzorec uporaben.
- Razumeti ključne elemente, potrebne za implementacijo vzorca.
- Prepoznati premisleke za zagotavljanje zaupanja vrednih AI agentov, ki uporabljajo ta vzorec.

## Kaj je vzorec oblikovanja uporabe orodij?

**Vzorec oblikovanja uporabe orodij** se osredotoča na omogočanje LLM-jem, da komunicirajo z zunanjimi orodji za doseganje specifičnih ciljev. Orodja so koda, ki jo lahko agent izvede za opravljanje dejanj. Orodje je lahko preprosta funkcija, kot je kalkulator, ali klic API-ja do zunanje storitve, kot je poizvedba o ceni delnic ali vremenska napoved. V kontekstu AI agentov so orodja zasnovana tako, da jih agenti izvajajo kot odgovor na **klice funkcij, ki jih generira model**.

## Za katere primere uporabe ga lahko uporabimo?

AI agenti lahko izkoristijo orodja za dokončanje kompleksnih nalog, pridobivanje informacij ali sprejemanje odločitev. Vzorec uporabe orodij se pogosto uporablja v scenarijih, kjer je potrebna dinamična interakcija z zunanjimi sistemi, kot so baze podatkov, spletne storitve ali tolmači kode. Ta sposobnost je uporabna za številne primere uporabe, med drugim:

- **Dinamično pridobivanje informacij:** Agenti lahko poizvedujejo zunanje API-je ali baze podatkov za pridobitev ažurnih podatkov (npr. poizvedba SQLite baze za analizo podatkov, pridobivanje cen delnic ali vremenskih informacij).
- **Izvajanje in tolmačenje kode:** Agenti lahko izvajajo kodo ali skripte za reševanje matematičnih problemov, generiranje poročil ali izvajanje simulacij.
- **Avtomatizacija delovnih tokov:** Avtomatizacija ponavljajočih se ali večstopenjskih potekov dela z integracijo orodij, kot so razporejevalci opravil, e-poštne storitve ali podatkovni tokovi.
- **Podpora strankam:** Agenti lahko sodelujejo s CRM sistemi, platformami za podporo ali bazo znanja za reševanje uporabniških vprašanj.
- **Generiranje in urejanje vsebin:** Agenti lahko uporabijo orodja, kot so preverjevalci slovnice, povzemači besedil ali ocenjevalci varnosti vsebine za pomoč pri ustvarjanju vsebin.

## Kateri so elementi/gradniki, potrebni za implementacijo vzorca uporabe orodij?

Ti gradniki omogočajo AI agentu, da opravi širok spekter nalog. Oglejmo si ključne elemente, potrebne za implementacijo vzorca uporabe orodij:

- **Sheme funkcij/orodij**: Podrobne definicije razpoložljivih orodij, vključno z imenom funkcije, namenom, potrebnimi parametri in pričakovanimi izhodi. Te sheme omogočajo LLM, da razume, katera orodja so na voljo in kako sestaviti veljavne zahteve.

- **Logika izvajanja funkcij:** Upravljanje, kako in kdaj se orodja pokličejo glede na uporabnikovo namero in kontekst pogovora. To lahko vključuje gradnike za načrtovanje, usmerjanje ali pogojne tokove, ki dinamično določajo uporabo orodij.

- **Sistem upravljanja sporočil:** Komponente, ki upravljajo potek pogovora med uporabniškimi vnosi, odzivi LLM, klici orodij in rezultati orodij.

- **Okvir za integracijo orodij:** Infrastruktura, ki povezuje agenta z različnimi orodji, bodisi preprostimi funkcijami bodisi zapletenimi zunanjimi storitvami.

- **Upravljanje napak in validacija:** Mehanizmi za obravnavo napak pri izvajanju orodij, preverjanje parametrov in upravljanje nepričakovanih odgovorov.

- **Upravljanje stanja:** Sledenje kontekstu pogovora, prejšnjim interakcijam z orodji in trajnim podatkom za zagotavljanje skladnosti pri večkrokovnih interakcijah.

Naslednje si oglejmo podrobneje klice funkcij/orodij.
 
### Klicanje funkcij/orodij

Klic funkcije je glavni način, s katerim omogočimo velikim jezikovnim modelom (LLM), da komunicirajo z orodji. Pogosto boste videli, da se ‘funkcija’ in ‘orodje’ uporabljata izmenično, ker so 'funkcije' (bloki ponovno uporabne kode) orodja, ki jih agenti uporabljajo za opravljanje nalog. Da se lahko koda funkcije pokliče, mora LLM primerjati uporabnikovo zahtevo z opisom funkcije. Za to se pošlje shema, ki vsebuje opise vseh razpoložljivih funkcij LLM-ju. LLM nato izbere najprimernejšo funkcijo za nalogo in vrne njeno ime ter argumente. Izbrana funkcija se pokliče, njen odgovor se pošlje nazaj LLM-ju, ki informacije uporabi za odgovor uporabniku.

Za razvoj funkcionalnosti klicanja funkcij za agente boste potrebovali:

1. Model LLM, ki podpira klic funkcij
2. Shemo z opisi funkcij
3. Kodo za vsako opisano funkcijo

Uporabimo primer pridobivanja trenutnega časa v mestu za ilustracijo:

1. **Inicializacija LLM, ki podpira klic funkcij:**

    Ne vsi modeli podpirajo klic funkcij, zato je pomembno preveriti, ali vaš LLM to omogoča. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podpira klic funkcij. Začnemo lahko z zagonom OpenAI odjemalca proti storitvi Azure OpenAI **Responses API** (stabilna pot `/openai/v1/` — ni potreben `api_version`).

    ```python
    # Inicializirajte OpenAI odjemalca za Azure OpenAI (API za odgovore, v1 končna točka)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Ustvarite shemo funkcije**:

    Nato definiramo JSON shemo, ki vsebuje ime funkcije, opis, kaj funkcija počne, ter imena in opise funkcijskih parametrov.
    To shemo pošljemo prej ustvarjenemu odjemalcu skupaj z uporabnikovo zahtevo za čas v San Franciscu. Pomembno je poudariti, da je vrnjen **klic orodja**, **ne** končni odgovor na vprašanje. Kot smo že omenili, LLM vrne ime funkcije, ki jo je izbral za nalogo, in argumente, ki jih bo prejel.

    ```python
    # Opis funkcije za branje modela (format orodja API za odzive v ravni obliki)
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

    # Prvi klic API-ja: Prosite model, da uporabi funkcijo
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # API za odgovore vrne klice orodij kot elemente function_call v response.output.
    # Dodajte jih v pogovor, da ima model popoln kontekst v naslednjem koraku.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Koda funkcije, potrebna za izvedbo naloge:**

    Ko LLM izbere, katera funkcija se mora izvesti, je potrebno implementirati in izvesti kodo, ki opravilo izvede.
    Kodo za pridobivanje trenutnega časa lahko napišemo v Pythonu. Prav tako moramo napisati kodo za izluščitev imena in argumentov iz response_message za dobitev končnega rezultata.

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
    # Ravnajte s klici funkcij
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Vrni rezultat orodja kot element function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Drugi klic API-ja: Pridobite končni odgovor modela
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

Klic funkcij je jedro večine, če ne vseh vzorcev uporabe orodij pri agentih, vendar je njegova implementacija iz nič pogosto izziv.
Kot smo se naučili v [Lekcija 2](../../../02-explore-agentic-frameworks) nam agenti okviri ponujajo predpripravljene gradnike za implementacijo uporabe orodij.
 
## Primeri uporabe orodij z agentnimi okviri

Tukaj je nekaj primerov, kako lahko izvedete vzorec uporabe orodij z različnimi agentnimi okviri:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> je odprtokodni AI okvir za gradnjo AI agentov. Poenostavi proces uporabe klica funkcij z možnostjo definiranja orodij kot Python funkcij z dekoratorjem `@tool`. Okvir upravlja komunikacijo med modelom in vašo kodo. Prav tako omogoča dostop do predpripravljenih orodij, kot sta File Search in Code Interpreter prek `FoundryChatClient`.

Naslednji diagram ponazarja proces klica funkcij z Microsoft Agent Framework:

![klic funkcije](../../../translated_images/sl/functioncalling-diagram.a84006fc287f6014.webp)

V Microsoft Agent Framework so orodja definirana kot dekorirane funkcije. Funkcijo `get_current_time`, ki smo jo videli prej, lahko pretvorimo v orodje z dekoratorjem `@tool`. Okvir bo samodejno serializiral funkcijo in njene parametre ter ustvaril shemo za pošiljanje LLM-ju.

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

# Ustvari agenta in ga zaženi s orodjem
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> je novejši agentni okvir, zasnovan za omogočanje razvijalcem varne gradnje, uvajanja in razširitve visokokakovostnih in razširljivih AI agentov brez potrebe po upravljanju osnovnih računalniških in shranjevalnih virov. Še posebej koristen je za podjetniške aplikacije, saj gre za popolnoma upravljano storitev z varnostjo na podjetniški ravni.

V primerjavi z razvojem neposredno prek LLM API-ja, Microsoft Foundry Agent Service ponuja nekaj prednosti, med drugim:

- Samodejno klicanje orodij – ni potrebe po ročnem razčlenjevanju klica orodja, izvajanju orodja in obravnavi odziva; vse to poteka na strežniški strani
- Varnostno upravljani podatki – namesto upravljanja lastnega stanja pogovora se lahko zanesete na niti, ki shranjujejo vse potrebne informacije
- Orodja, pripravljena za uporabo – Orodja za interakcijo z vašimi viri podatkov, kot so Bing, Azure AI Search in Azure Functions.

Orodja, na voljo v Microsoft Foundry Agent Service, lahko razdelimo v dve kategoriji:

1. Orodja za znanje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Povezovanje z iskanjem Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Iskanje datotek</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Orodja za delovanje:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Klicanje funkcij</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Tolmač kode</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Orodja, definirana z OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nam omogoča uporabo teh orodij skupaj kot `orodjarno`. Prav tako uporablja `niti`, ki beležijo zgodovino sporočil posameznega pogovora.

Predstavljajte si, da ste prodajni agent v podjetju Contoso. Želite razviti pogovornega agenta, ki zna odgovarjati na vprašanja o vaših prodajnih podatkih.

Naslednja slika prikazuje, kako lahko uporabite Microsoft Foundry Agent Service za analizo prodajnih podatkov:

![Agentna storitev v akciji](../../../translated_images/sl/agent-service-in-action.34fb465c9a84659e.webp)

Za uporabo katerega koli izmed teh orodij s storitvijo lahko ustvarimo odjemalca in definiramo orodje ali orodjarno. Za praktično izvedbo lahko uporabimo naslednjo Python kodo. LLM bo lahko pogledal orodjarno in odločil, ali bo uporabil uporabniško funkcijo `fetch_sales_data_using_sqlite_query` ali predpripravljeni Tolmač kode, odvisno od uporabnikove zahteve.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query funkcija, ki jo najdete v datoteki fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inicializiraj orodja
toolset = ToolSet()

# Inicializiraj agent za klic funkcij s funkcijo fetch_sales_data_using_sqlite_query in jo dodaj k orodjem
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializiraj orodje za interpretacijo kode in ga dodaj k orodjem.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4.1-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Katere so posebne premisleke pri uporabi vzorca uporabe orodij za gradnjo zaupanja vrednih AI agentov?

Pogosta skrb pri dinamično generirani SQL kodi z LLM-ji je varnost, zlasti tveganje za SQL injekcije ali zlonamerna dejanja, kot so brisanje ali spreminjanje baze podatkov. Čeprav so te skrbi na mestu, jih je mogoče učinkovito ublažiti z ustrezno konfiguracijo dovoljenj za dostop do baze podatkov. Za večino baz podatkov to vključuje nastavitev baze v način samo za branje. Za baze podatkov, kot sta PostgreSQL ali Azure SQL, naj bo aplikaciji dodeljena vloga samo za branje (SELECT).

Zagon aplikacije v varnem okolju še dodatno izboljša zaščito. V podjetniških scenarijih se podatki običajno ekstrahirajo in transformirajo iz operativnih sistemov v bazo podatkov ali podatkovno skladišče samo za branje z uporabniku prijazno shemo. Tak pristop zagotavlja, da so podatki varni, optimizirani za zmogljivost in dostopnost ter da ima aplikacija omejen, samo za branje dostop.

## Primeri kode

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Imate več vprašanj o vzorcu uporabe orodij?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kjer se lahko srečate z drugimi učenci, udeležite ur uradne podpore in dobite odgovore na vprašanja o AI agentih.

## Dodatni viri

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Delavnica Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Delavnica Večagentnega ustvarjalca vsebin Contoso</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Pregled Microsoft Agent Framework</a>


## Osnovno testiranje tega agenta (neobvezno)

Ko se naučite nameščati agente v [Lekcija 16](../16-deploying-scalable-agents/README.md), lahko z osnovnim testiranjem preverite `TravelToolAgent` iz te lekcije (ali še vedno kliče svoje orodje in odgovarja?) s [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Oglejte si [`tests/README.md`](../tests/README.md) za navodila, kako ga zagnati.

## Prejšnja lekcija

[Razumevanje agentnih oblikovalskih vzorcev](../03-agentic-design-patterns/README.md)

## Naslednja lekcija

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->