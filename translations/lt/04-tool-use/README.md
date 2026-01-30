[![Kaip sukurti gerus AI agentus](../../../translated_images/lt/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Spustelėkite aukščiau esančią nuotrauką norėdami peržiūrėti šios pamokos vaizdo įrašą)_

# Įrankių naudojimo dizaino šablonas

Įrankiai yra įdomūs, nes jie leidžia AI agentams turėti platesnį gebėjimų spektrą. Vietoj to, kad agentas turėtų ribotą veiksmų rinkinį, pridėjus įrankį, agentas dabar gali atlikti platų veiksmų spektrą. Šiame skyriuje aptarsime Įrankių naudojimo dizaino šabloną, kuris aprašo, kaip AI agentai gali naudoti tam tikrus įrankius savo tikslams pasiekti.

## Įvadas

Šioje pamokoje sieksime atsakyti į šiuos klausimus:

- Kas yra įrankių naudojimo dizaino šablonas?
- Kokiais atvejais jis gali būti taikomas?
- Kokie elementai/komponentai reikalingi dizaino šablonui įgyvendinti?
- Kokie yra specialūs aspektai naudojant Įrankių naudojimo dizaino šabloną kuriant patikimus AI agentus?

## Mokymosi tikslai

Baigus šią pamoką, gebėsite:

- Apibrėžti Įrankių naudojimo dizaino šabloną ir jo paskirtį.
- Nustatyti atvejus, kur galima taikyti Įrankių naudojimo dizaino šabloną.
- Suprasti pagrindinius elementus, reikalingus dizaino šablonui įgyvendinti.
- Pripažinti svarbias aplinkybes, užtikrinančias patikimumą naudojant šį dizaino šabloną AI agentams.

## Kas yra Įrankių naudojimo dizaino šablonas?

**Įrankių naudojimo dizaino šablonas** orientuotas į tai, kad LLM galėtų sąveikauti su išoriniais įrankiais, siekiant pasiekti konkrečius tikslus. Įrankiai yra kodas, kurį agentas gali vykdyti, kad atliktų veiksmus. Įrankis gali būti paprasta funkcija, tokia kaip skaičiuoklė, arba API kvietimas trečiosios šalies paslaugai, pavyzdžiui, akcijų kainų paieškai ar orų prognozėms. Dirbtinio intelekto agentų kontekste įrankiai sukurti taip, kad agentai juos vykdytų atsakydami į **modelio sugeneruotus funkcijų kvietimus**.

## Kokiems atvejams tai taikoma?

AI agentai gali naudoti įrankius sudėtingoms užduotims atlikti, informacijai gauti ar sprendimams priimti. Įrankių naudojimo dizaino šablonas dažnai taikomas scenarijuose, kuriuose reikalinga dinamiška sąveika su išorinėmis sistemomis, tokiomis kaip duomenų bazės, žiniatinklio paslaugos ar kodo interpretatoriai. Ši galimybė naudinga daugeliui panaudojimo atvejų, įskaitant:

- **Dinaminis informacijos gavimas:** agentai gali užklausti išorinių API ar duomenų bazių, kad gautų aktualius duomenis (pvz., užklausos SQLite duomenų bazėje duomenų analizei, akcijų kainų ar orų informacijos gavimui).
- **Kodo vykdymas ir interpretavimas:** agentai gali vykdyti kodą ar scenarijus spręsti matematikos uždaviniams, generuoti ataskaitas ar atlikti simuliacijas.
- **Darbo eigos automatizavimas:** automatizuoti pasikartojančias ar daugiapakopes darbo eigos, integruojant įrankius, tokius kaip užduočių tvarkyklės, el. pašto paslaugos ar duomenų vamzdynai.
- **Klientų aptarnavimas:** agentai gali sąveikauti su CRM sistemomis, bilietų platformomis ar žinių bazėmis, kad išspręstų vartotojų klausimus.
- **Turinio kūrimas ir redagavimas:** agentai gali naudoti įrankius, tokius kaip gramatikos tikrintuvai, teksto santraukos ar turinio saugumo vertintojai, kad padėtų kurti turinį.

## Kokie elementai/komponentai reikalingi įrankių naudojimo dizaino šablonui įgyvendinti?

Šie komponentai leidžia AI agentui atlikti platų užduočių spektrą. Pažvelkime į pagrindinius elementus, reikalingus Įrankių naudojimo dizaino šablonui įgyvendinti:

- **Funkcijų/Įrankių schemos**: Išsamūs prieinamų įrankių aprašymai, įskaitant funkcijos pavadinimą, paskirtį, reikiamus parametrus ir numatomus rezultatus. Šios schemos leidžia LLM suprasti, kokie įrankiai yra prieinami ir kaip sudaryti galiojančias užklausas.

- **Funkcijų vykdymo logika**: Valdo, kaip ir kada įrankiai kviečiami, atsižvelgiant į vartotojo ketinimą ir pokalbio kontekstą. Tai gali apimti planavimo modulius, maršrutizavimo mechanizmus ar sąlyginį srautą, dinamiškai nusprendžiantį įrankių naudojimą.

- **Pranešimų apdorojimo sistema**: Komponentai, valdomi pokalbio srauto tarp vartotojo įvesties, LLM atsakymų, įrankių kvietimų ir jų rezultatų.

- **Įrankių integracijos sistema**: Infrastruktūra, jungiantis agentą su įvairiais įrankiais, nesvarbu, ar tai paprastos funkcijos, ar sudėtingos išorinės paslaugos.

- **Klaidų valdymas ir patikra**: Mechanizmai, tvarkantys įrankių vykdymo klaidas, patikrinantys parametrus ir valdantys netikėtas atsakymų situacijas.

- **Būsenos valdymas**: Sekimas pokalbio kontekste, ankstesnėse įrankių sąveikose ir nuolatinės duomenų saugyklos valdymas, siekiant užtikrinti nuoseklumą daugelių turų sąveikose.

Dabar pažvelkime detaliau į Funkcijų/Įrankių kvietimą.

### Funkcijų/Įrankių kvietimas

Funkcijų kvietimas yra pagrindinis būdas, kuriuo leidžiame Dideliems kalbos modeliams (LLM) sąveikauti su įrankiais. Dažnai matysite, kad "Funkcija" ir "Įrankis" vartojami sinonimiškai, nes "funkcijos" (daugiakartinio naudojimo kodo blokai) yra tie „įrankiai“, kuriuos agentai naudoja užduotims atlikti. Kad funkcijos kodas būtų iškviečiamas, LLM turi palyginti vartotojo užklausą su funkcijos aprašymu. Tam siunčiama schema, kurioje yra visų galimų funkcijų aprašymai. Tada LLM parenka tinkamiausią funkciją užduočiai ir grąžina jos pavadinimą bei argumentus. Išrinkta funkcija yra iškviečiama, jo atsakymas siunčiamas atgal LLM, kuris panaudoja informaciją atsakydamas vartotojui.

Norint kūrėjams įgyvendinti funkcijų kvietimą agentams, reikės:

1. LLM modelio, palaikančio funkcijų kvietimą
2. Schemos su funkcijų aprašymais
3. Kiekvienos aprašytos funkcijos kodo

Pažiūrėkime pavyzdį, kaip gauti dabartinį laiką mieste:

1. **Inicijuokite LLM, palaikantį funkcijų kvietimą:**

    Nepalaiko visi modeliai funkcijų kvietimo, todėl svarbu patikrinti, ar naudojamas LLM tai palaiko.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> palaiko funkcijų kvietimą. Galime pradėti inicijuodami Azure OpenAI klientą. 

    ```python
    # Inicializuoti Azure OpenAI klientą
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Sukurkite funkcijų schemą**:

    Tada aprašysime JSON schemą, kurioje bus funkcijos pavadinimas, aprašymas, ką funkcija daro, bei funkcijos parametrų pavadinimai ir aprašymai.
    Šią schemą perduosime anksčiau sukurtam klientui kartu su vartotojo užklausa surasti laiką San Franciske. Svarbu paminėti, kad grąžinama yra **įrankio kvietimas**, **ne** galutinis atsakymas į klausimą. Kaip minėta anksčiau, LLM grąžina pasirinktą funkcijos pavadinimą ir argumentus.

    ```python
    # Funkcijos aprašymas modeliui skaityti
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
  
    # Pradinis naudotojo pranešimas
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Pirmasis API kvietimas: Paprašykite modelio naudoti funkciją
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Apdorokite modeli atsakymą
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Funkcijos kodas užduočiai atlikti:**

    Kadangi LLM pasirinko, kurią funkciją reikia vykdyti, reikalingas kodas turi būti įgyvendintas ir vykdomas.
    Galime įgyvendinti kodą, kuris gauna dabartinį laiką Python kalba. Taip pat reikės parašyti kodą, kuris ištrauks pavadinimą ir argumentus iš response_message, norint gauti galutinį rezultatą.

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
     # Tvarkyti funkcijų kvietimus
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
  
      # Antras API kvietimas: Gauti galutinį modelio atsakymą
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

Funkcijų kvietimas yra pagrindinis daugumos, jei ne visų agentų įrankių naudojimo dizaino šablonų branduolys, tačiau jį įgyvendinti nuo nulio kartais gali būti sudėtinga.
Kaip sužinojome [Pamokoje 2](../../../02-explore-agentic-frameworks) agentiniai karkasai suteikia mums iš anksto paruoštus komponentus įrankių naudojimui įgyvendinti.

## Įrankių naudojimo pavyzdžiai su agentiniais karkasais

Štai keli pavyzdžiai, kaip galima įgyvendinti Įrankių naudojimo dizaino šabloną, naudojant skirtingus agentinius karkasus:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> yra atvirojo kodo AI karkasas .NET, Python ir Java kūrėjams, dirbantiems su Dideliais kalbos modeliais (LLM). Jis supaprastina funkcijų kvietimo procesą automatiškai aprašydamas jūsų funkcijas ir jų parametrus modeliui per procesą, vadinamą <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializavimu</a>. Taip pat jis valdo abi puses - komunikaciją tarp modelio ir jūsų kodo. Kitas Semantic Kernel naudojimo privalumas yra tas, kad jis leidžia naudotis paruoštais įrankiais, pvz., <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Failų paieška</a> ir <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Kodo interpretatorius</a>.

Toliau pateiktas diagrama iliustruoja funkcijų kvietimo procesą su Semantic Kernel:

![function calling](../../../translated_images/lt/functioncalling-diagram.a84006fc287f6014.webp)

Semantic Kernel funkcijos/įrankiai vadinami <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">įskiepiais</a>. Galime paversti anksčiau matytą `get_current_time` funkciją į įskiepį, pakeisdami ją į klasę su ta funkcija. Taip pat galime importuoti `kernel_function` dekoratorių, kuris priima funkcijos aprašymą. Sukūrus branduolį su GetCurrentTimePlugin, branduolys automatiškai serializuos funkciją ir jos parametrus, tuo pačiu sukuriant schemą, kuri bus siunčiama LLM.

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

# Sukurkite branduolį
kernel = Kernel()

# Sukurkite papildinį
get_current_time_plugin = GetCurrentTimePlugin(location)

# Pridėkite papildinį prie branduolio
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> yra naujesnis agentinis karkasas, sukurtas, kad padėtų kūrėjams saugiai kurti, diegti ir keisti aukštos kokybės bei išplečiamus AI agentus neprivalant valdyti pagrindinių skaičiavimo ar saugojimo išteklių. Tai ypač naudinga įmonių programoms, nes tai visiškai valdomas, verslo klasės saugumo turintis servisais.

Palyginti su tiesioginiu vystymu naudojant LLM API, Azure AI Agent Service suteikia tam tikrų privalumų, įskaitant:

- Automatinis įrankių kvietimas – nereikia analizuoti įrankio kvietimo, vykdyti įrankio ir tvarkyti atsakymų; visa tai dabar vykdoma serverio pusėje
- Saugiai valdomi duomenys – vietoje savo pokalbių būsenos valdymo galite pasikliauti temomis (threads), kurios saugo visą reikalingą informaciją
- Out-of-the-box įrankiai – įrankiai, leidžiantys sąveikauti su jūsų duomenų šaltiniais, tokie kaip Bing, Azure AI Search ir Azure Functions.

Azure AI Agent Service įrankiai yra suskirstyti į dvi kategorijas:

1. Žinių įrankiai:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Pagrindimas su Bing paieška</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Failų paieška</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI paieška</a>

2. Veiksmų įrankiai:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funkcijų kvietimas</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kodo interpretatorius</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI apibrėžti įrankiai</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agentų servisas leidžia naudoti šiuos įrankius kartu kaip `įrankių rinkinį`. Jis taip pat naudoja `threads`, kurie seka konkrečių pokalbių žinučių istoriją.

Įsivaizduokite, kad esate prekybos agentas kompanijoje Contoso. Norite sukurti pokalbių agentą, galintį atsakyti į klausimus apie jūsų pardavimų duomenis.

Toliau pateikta iliustracija rodo, kaip galite naudoti Azure AI Agent Service, analizuodami savo pardavimų duomenis:

![Agentic Service In Action](../../../translated_images/lt/agent-service-in-action.34fb465c9a84659e.webp)

Norėdami naudoti bet kurį iš šių įrankių su servisu, galime sukurti klientą ir apibrėžti įrankį arba įrankių rinkinį. Praktiniam įgyvendinimui galime naudoti šį Python kodą. LLM galės pažvelgti į įrankių rinkinį ir nuspręsti, ar naudoti vartotojo sukurtą funkciją `fetch_sales_data_using_sqlite_query`, ar iš anksto sukurtą Kodo interpretatorių, priklausomai nuo vartotojo užklausos.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query funkcija, kurią galima rasti fetch_sales_data_functions.py faile.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Įdiegti įrankių rinkinį
toolset = ToolSet()

# Inicializuoti funkcijų kvietimo agentą su fetch_sales_data_using_sqlite_query funkcija ir pridėti jį prie įrankių rinkinio
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializuoti kodo interpretuotojo įrankį ir pridėti jį prie įrankių rinkinio.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Kokie yra specialūs aspektai naudojant Įrankių naudojimo dizaino šabloną kuriant patikimus AI agentus?

Dažna problema su SQL, dinamiškai generuojamu LLM, yra saugumas, ypač SQL injekcijos rizika ar kenkėjiškos veiksmai, tokie kaip duomenų bazės ištrynimas ar klastojimas. Nors šios problemos yra aktualios, jas galima veiksmingai sumažinti tinkamai sukonfigūravus duomenų bazės prieigos teises. Daugumai duomenų bazių tai reiškia duomenų bazės konfigūravimą kaip tik skaitymui. Duomenų bazių paslaugoms, tokioms kaip PostgreSQL ar Azure SQL, programai turėtų būti priskirta tik skaitymo (SELECT) teisė.
Programėlės paleidimas saugioje aplinkoje dar labiau sustiprina apsaugą. Įmonių scenarijuose duomenys paprastai yra paimami ir transformuojami iš operacinių sistemų į tik skaitymui skirtą duomenų bazę arba duomenų sandėlį su patogiu vartotojui schemomis. Šis požiūris užtikrina, kad duomenys yra saugūs, optimizuoti našumui ir prieinamumui, o programėlė turi ribotą, tik skaitymui skirtą prieigą.

## Pavyzdiniai kodai

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Turite daugiau klausimų apie Įrankių naudojimo dizaino šablonus?

Prisijunkite prie [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), susipažinkite su kitais besimokančiais, dalyvaukite konsultacijose ir gaukite atsakymus į savo AI agentų klausimus.

## Papildomi ištekliai

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Ankstesnė pamoka

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Kitoji pamoka

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės atsisakymas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinėje informacijoje rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus traktavimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->