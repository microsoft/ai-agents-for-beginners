[![Kaip sukurti gerus DI agentus](../../../translated_images/lt/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Spustelėkite aukščiau esantį paveikslėlį, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

# Įrankių naudojimo dizaino šablonas

Įrankiai yra įdomūs, nes leidžia DI agentams turėti platesnį galimybių spektrą. Vietoje to, kad agentas turėtų ribotą veiksmų rinkinį, pridėjus įrankį agentas dabar gali atlikti platų veiksmų spektrą. Šiame skyriuje apžvelgsime Įrankių naudojimo dizaino šabloną, kuris aprašo, kaip DI agentai gali naudoti konkrečius įrankius savo tikslams pasiekti.

## Įvadas

Šioje pamokoje sieksime atsakyti į šiuos klausimus:

- Kas yra įrankių naudojimo dizaino šablonas?
- Kokiose situacijose jis gali būti taikomas?
- Kokie yra elementai/statybiniai blokai, reikalingi šiam dizaino šablonui įgyvendinti?
- Kokie yra specialūs aspektai naudojant Įrankių naudojimo dizaino šabloną kuriant patikimus DI agentus?

## Mokymosi tikslai

Baigę šią pamoką, galėsite:

- Apibrėžti Įrankių naudojimo dizaino šabloną ir jo paskirtį.
- Nustatyti taikymo atvejus, kur Įrankių naudojimo dizaino šablonas yra pritaikomas.
- Suprasti pagrindinius elementus, reikalingus dizaino šablonui įgyvendinti.
- Pripažinti aspektus, užtikrinančius patikimumą DI agentams, naudojantiems šį dizaino šabloną.

## Kas yra Įrankių naudojimo dizaino šablonas?

**Įrankių naudojimo dizaino šablonas** fokusuoja LLM galimybę sąveikauti su išoriniais įrankiais siekiant konkrečių tikslų. Įrankiai yra kodas, kurį agentas gali vykdyti atlikti veiksmams. Įrankis gali būti paprasta funkcija, pavyzdžiui skaičiuotuvas, arba API iškvietimas į trečiosios šalies paslaugą, pavyzdžiui, akcijų kainų patikrinimas ar orų prognozė. DI agentų kontekste įrankiai sukurti tam, kad agentai galėtų vykdyti **modelio sugeneruotus funkcijų iškvietimus**.

## Kokiose situacijose jis gali būti taikomas?

DI agentai gali pasinaudoti įrankiais, kad įvykdytų sudėtingas užduotis, surinktų informaciją ar priimtų sprendimus. Įrankių naudojimo dizaino šablonas dažnai naudojamas scenarijuose, kuriuose reikia dinamiškai sąveikauti su išorinėmis sistemomis, tokiomis kaip duomenų bazės, žiniatinklio paslaugos ar kodo interpretatoriai. Ši galimybė yra naudinga įvairiems taikymo atvejams, įskaitant:

- **Dinaminis informacijos gavimas:** Agentai gali kreiptis į išorinius API arba duomenų bazes, kad gautų naujausius duomenis (pvz., kreiptis į SQLite duomenų bazę duomenų analizei, gauti akcijų kainas ar orų informaciją).
- **Kodo vykdymas ir interpretavimas:** Agentai gali vykdyti kodą ar scenarijus spręsti matematines užduotis, generuoti ataskaitas ar atlikti simuliacijas.
- **Darbo eigos automatizavimas:** Automatizuoti pasikartojančias ar daugiapakopes darbo eigas integruojant tokias priemones kaip užduočių planuotojai, el. pašto paslaugos ar duomenų vamzdynai.
- **Klientų aptarnavimas:** Agentai gali sąveikauti su CRM sistemomis, bilietų platformomis ar žinių bazėmis, kad spręstų vartotojų užklausas.
- **Turinio generavimas ir redagavimas:** Agentai gali naudoti įrankius, tokius kaip gramatikos tikrintuvai, teksto santraukų kūrėjai ar turinio saugumo vertintojai, kad padėtų turinio kūrimo užduotyse.

## Kokie yra elementai/statybiniai blokai, reikalingi įrankių naudojimo dizaino šablonui įgyvendinti?

Šie statybiniai blokai leidžia DI agentui atlikti platų užduočių spektrą. Pažiūrėkime pagrindinius elementus, reikalingus Įrankių naudojimo dizaino šablonui įgyvendinti:

- **Funkcijos/įrankių schemos**: Išsamūs prieinamų įrankių apibrėžimai, įskaitant funkcijos pavadinimą, paskirtį, reikalingus parametrus ir laukiamus rezultatus. Šios schemos leidžia LLM suprasti, kokie įrankiai yra prieinami ir kaip sudaryti galiojančius užklausimus.

- **Funkcijos vykdymo logika**: Nustato, kaip ir kada įrankiai kviečiami, remiantis vartotojo ketinimu ir pokalbio kontekstu. Tai gali apimti planavimo modulius, maršruto pasirinkimo mechanizmus ar sąlyginę logiką, kuri dinamiškai nustato įrankių naudojimą.

- **Žinučių valdymo sistema**: Komponentai, valdantys pokalbio srautą tarp vartotojo įėjimų, LLM atsakymų, įrankių iškvietimų ir jų atsakymų.

- **Įrankių integravimo sistema**: Infrastruktūra, jungianti agentą su įvairiais įrankiais, nepriklausomai nuo to, ar tai paprastos funkcijos, ar sudėtingos išorinės paslaugos.

- **Klaidų tvarkymas ir validacija**: Mechanizmai, skirtos tvarkyti įrankių vykdymo klaidas, tikrinti parametrus ir valdyti netikėtas atsakymų situacijas.

- **Būsenos valdymas**: Stebi pokalbio kontekstą, ankstesnius įrankių veiksmus ir nuolatinę informaciją, užtikrinant nuoseklumą daugiažingsniuose pokalbiuose.

Dabar pažiūrėkime detaliau, kaip vyksta Funkcijų/Įrankių kvietimas.
 
### Funkcijų/Įrankių kvietimas

Funkcijų kvietimas yra pagrindinis būdas, kuriuo leidžiame didelių kalbinių modelių (LLM) sąveikauti su įrankiais. Dažnai matysite terminus „Funkcija“ ir „Įrankis“ vartojamus kaip sinonimus, nes „funkcijos“ (pakartotinai naudojamo kodo blokai) yra įrankiai, kuriuos agentai naudoja užduotims atlikti. Kad funkcijos kodas būtų iškviestas, LLM turi palyginti vartotojo užklausą su funkcijos aprašu. Tam siunčiama schema, kurioje yra visų prieinamų funkcijų aprašai. LLM pasirinks tinkamiausią funkciją užduočiai ir grąžins jos pavadinimą bei argumentus. Pasirinkta funkcija yra iškviečiama, jos atsakymas siunčiamas atgal LLM, kuris naudoja informaciją atsakymui vartotojui suformuoti.

Kūrėjams, norint įgyvendinti funkcijų kvietimą agentams, reikės:

1. LLM modelio, kuris palaiko funkcijų kvietimą
2. Schemos su funkcijų aprašais
3. Kodo kiekvienai aprašytai funkcijai

Pasinaudokime pavyzdžiu, kaip gauti esamą laiką mieste:

1. **Inicijuokite LLM, kuris palaiko funkcijų kvietimą:**

    Ne visi modeliai palaiko funkcijų kvietimą, todėl svarbu patikrinti, ar naudojamas LLM tai atlieka.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> palaiko funkcijų kvietimą. Galime pradėti inicijuodami OpenAI klientą su Azure OpenAI **Responses API** (stabilus `/openai/v1/` endpointas — `api_version` nereikalingas). 

    ```python
    # Inicializuokite OpenAI klientą Azure OpenAI (Responses API, v1 galinis taškas)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Sukurkite funkcijos schemą**:

    Toliau apibrėšime JSON schemą, kurią sudarys funkcijos pavadinimas, aprašymas apie tai, ką funkcija atlieka, bei funkcijos parametrų pavadinimai ir aprašymai.
    Tada jos pagrindu perduosime schemą anksčiau sukurtam klientui, kartu su vartotojo užklausa gauti laiką San Franciske. Svarbu žinoti, kad **įrankio kvietimas** yra grąžinamas, **o ne** galutinis atsakymas į klausimą. Kaip minėta anksčiau, LLM grąžina pasirinktos funkcijos pavadinimą ir jos argumentus.

    ```python
    # Funkcijos aprašymas modeliui skaityti (Atsakymų API plokščio įrankio formatas)
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
  
    # Pradinis vartotojo pranešimas
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Pirmas API kvietimas: paprašykite modelio naudoti funkciją
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API grąžina įrankių kvietimus kaip function_call elementus response.output.
    # Pridėkite juos prie pokalbio, kad modelis turėtų visą kontekstą kitame žingsnyje.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Funkcijos kodas, skirtas atlikti užduotį:**

    Kadangi LLM pasirinko, kuri funkcija turi būti vykdoma, reikia įgyvendinti ir vykdyti tą funkciją atitinkantį kodą.
    Galime įgyvendinti laiką gaunantį kodą Python kalba. Taip pat reikia parašyti kodą, kuris išgautų pavadinimą ir argumentus iš atsakymo žinutės, kad gautume galutinį rezultatą.

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
    # Tvarkyti funkcijų iškvietimus
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Grąžinti įrankio rezultatą kaip function_call_output elementą
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Antrasis API kvietimas: Gauti galutinį atsakymą iš modelio
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

Funkcijų kvietimas yra pagrindinis daugumos, jei ne visų, agentų įrankių naudojimo dizaino šablonų komponentas, tačiau jo įgyvendinimas nuo nulio kartais gali būti sudėtingas.
Kaip sužinojome iš [2 pamokos](../../../02-explore-agentic-frameworks) agentiški karkasai suteikia mums paruoštus statybinius blokus įrankių naudojimui įgyvendinti.
 
## Įrankių naudojimo pavyzdžiai su agentiškais karkasais

Štai keli pavyzdžiai, kaip galite įgyvendinti Įrankių naudojimo dizaino šabloną naudodami skirtingus agentiškus karkasus:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> yra atviro kodo DI karkasas DI agentams kurti. Jis supaprastina funkcijų kvietimo procesą leidžiant apibrėžti įrankius kaip Python funkcijas, pažymėtas dekoratoriumi `@tool`. Karkasas valdo dialogo tarp modelio ir jūsų kodo komunikaciją. Taip pat jis suteikia prieigą prie paruoštų įrankių, tokių kaip Failų paieška ir Kodo interpretatorius, per `FoundryChatClient`.

Šis diagrama iliustruoja funkcijų kvietimo procesą su Microsoft Agent Framework:

![funkcijų kvietimas](../../../translated_images/lt/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework įrankiai yra apibrėžiami kaip dekoruotos funkcijos. Galime paversti anksčiau matytą `get_current_time` funkciją į įrankį naudodami `@tool` dekoratorių. Karkasas automatiškai serializuos funkciją ir jos parametrus, sukurs schemą, kuri bus siunčiama LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Sukurkite klientą
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Sukurkite agentą ir paleiskite su įrankiu
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> yra naujesnis agentiškas karkasas, sukurtas palengvinti kūrėjams saugų, patikimą ir išplečiamą DI agentų kūrimą, diegimą ir mastelį be būtinybės valdyti žemiau esančius skaičiavimo ir saugojimo resursus. Tai ypač naudinga verslo programoms, nes tai visiškai valdomas servisas su įmonių lygio saugumu.

Lyginant su tiesioginiu LLM API naudojimu, Microsoft Foundry Agent Service suteikia šias privalumus:

- Automatinis įrankių kvietimas – nereikia analizuoti įrankio kvietimo, iškviesti įrankį ir tvarkyti atsakymą; visa tai atliekama serveryje
- Saugiai valdoma duomenų valdymas – vietoje savo pokalbio būsenos valdymo galite pasitikėti threads, kurie saugo visą reikalingą informaciją
- Iš karto paruošti įrankiai – Įrankiai, leidžiantys sąveikauti su jūsų duomenų šaltiniais, tokiems kaip Bing, Azure AI Search ir Azure Functions.

Microsoft Foundry Agent Service įrankius galima suskirstyti į dvi kategorijas:

1. Žinių įrankiai:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing paieškos pagrindimas</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Failų paieška</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Veiksmų įrankiai:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funkcijų kvietimas</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kodo interpretatorius</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI apibrėžti įrankiai</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agentų servisas leidžia naudoti šiuos įrankius kartu kaip `įrankių rinkinį`. Taip pat jis naudoja `threads`, kurie seka konkretaus pokalbio žinučių istoriją.

Įsivaizduokite, kad esate pardavimų agentas įmonėje Contoso. Norite sukurti pokalbių agentą, kuris galėtų atsakyti į klausimus apie jūsų pardavimų duomenis.

Toliau pateikta iliustracija rodo, kaip galima panaudoti Microsoft Foundry Agent Service analizuoti pardavimų duomenis:

![Agentų serviso veiksmas](../../../translated_images/lt/agent-service-in-action.34fb465c9a84659e.webp)

Norėdami naudoti bet kurį iš šių įrankių su servisu, galime sukurti klientą ir apibrėžti įrankį arba įrankių rinkinį. Norėdami tai praktiškai įgyvendinti, galime naudoti šį Python kodą. LLM galės pažvelgti į įrankių rinkinį ir nuspręsti, ar naudoti vartotojo sukurtą funkciją `fetch_sales_data_using_sqlite_query`, ar paruoštą Kodo interpretatorių, atsižvelgiant į vartotojo užklausą.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query funkcija, kurią galima rasti faile fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Įrankių rinkinio inicijavimas
toolset = ToolSet()

# Funkcijų kvietimo agento inicijavimas su fetch_sales_data_using_sqlite_query funkcija ir jo pridėjimas prie įrankių rinkinio
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Kodo interpretatoriaus įrankio inicijavimas ir pridėjimas prie įrankių rinkinio.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4.1-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Kokie yra specialūs aspektai naudojant Įrankių naudojimo dizaino šabloną kuriant patikimus DI agentus?

Dažnas rūpestis dėl LLM dinamiškai generuojamo SQL yra saugumas, ypač SQL injekcijų ar kenkėjiškų veiksmų, tokių kaip duomenų bazės ištrynimas ar sugadinimas, rizika. Nors šie rūpesčiai yra pagrįsti, juos galima efektyviai suvaldyti tinkamai sukonfigūravus duomenų bazės prieigos teises. Daugumai duomenų bazių tai reiškia sukonfigūruoti duomenų bazę kaip tik skaitymui skirtą. Tokiems duomenų bazių servisams kaip PostgreSQL ar Azure SQL programėlei turėtų būti priskirta tik skaitymo (SELECT) teisė.

Programėlės vykdymas saugioje aplinkoje dar labiau sustiprina apsaugą. Verslo scenarijuose duomenys dažniausiai yra išgaunami ir transformuojami iš operacinių sistemų į tik skaitymui skirtą duomenų bazę ar duomenų sandėlį su vartotojui draugiška schema. Šis metodas užtikrina, kad duomenys yra saugūs, optimizuoti našumui bei prieinamumui, o programėlė turi ribotą, tik skaitymui skirtą prieigą.

## Pavyzdžių kodai

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Turite daugiau klausimų apie Įrankių naudojimo dizaino šablonus?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), susitikite su kitais mokiniais, dalyvaukite konsultacijose ir gaukite atsakymus į DI agentų klausimus.

## Papildomi ištekliai

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service dirbtuvės</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer daugiagentų dirbtuvės</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework apžvalga</a>


## Šio agento pirminis patikrinimas (pasirinktinai)

Išmokę diegti agentus [16 pamokoje](../16-deploying-scalable-agents/README.md), galite atlikti šios pamokos `TravelToolAgent` pirminį patikrinimą (ar jis vis dar iškviečia savo įrankius ir atsako?) naudodami [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Daugiau apie paleidimą žr. [`tests/README.md`](../tests/README.md).

## Ankstesnė pamoka

[Agentinių dizaino modelių supratimas](../03-agentic-design-patterns/README.md)

## Kitoji pamoka

[Agentinė RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->