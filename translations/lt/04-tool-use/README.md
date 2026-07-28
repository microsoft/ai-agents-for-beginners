[![Kaip Kurti Gerus DI Agentus](../../../translated_images/lt/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Spustelėkite aukščiau esantį paveikslėlį norėdami peržiūrėti šios pamokos vaizdo įrašą)_

# Įrankių Naudojimo Dizaino Šablonas

Įrankiai yra įdomūs, nes leidžia DI agentams turėti platesnį gebėjimų spektrą. Vietoj to, kad agentas turėtų ribotą veiksmų rinkinį, pridėjus įrankį, agentas dabar gali atlikti platų veiksmų spektrą. Šiame skyriuje apžvelgsime Įrankių Naudojimo Dizaino Šabloną, kuris aprašo, kaip DI agentai gali naudoti specifinius įrankius savo tikslams pasiekti.

## Įvadas

Šioje pamokoje sieksime atsakyti į šiuos klausimus:

- Kas yra įrankių naudojimo dizaino šablonas?
- Kokiais atvejais jis gali būti taikomas?
- Kokios yra būtinos sudedamosios dalys / blokai, reikalingi šiam dizaino šablonui įgyvendinti?
- Kokie yra ypatingi aspektai naudojant Įrankių Naudojimo Dizaino Šabloną kuriant patikimus DI agentus?

## Mokymosi Tikslai

Baigę šią pamoką, gebėsite:

- Apibrėžti Įrankių Naudojimo Dizaino Šabloną ir jo paskirtį.
- Nustatyti atvejus, kur šį šabloną galima taikyti.
- Suprasti pagrindines sudedamąsias dalis, reikalingas šablonui įgyvendinti.
- Atpažinti aspektus, užtikrinančius DI agentų patikimumą naudojant šį dizaino šabloną.

## Kas yra Įrankių Naudojimo Dizaino Šablonas?

**Įrankių Naudojimo Dizaino Šablonas** orientuotas į tai, kad LLM galėtų sąveikauti su išoriniais įrankiais, siekiant specifinių tikslų. Įrankiai yra kodas, kurį agentas gali vykdyti atlikti veiksmams. Įrankis gali būti paprasta funkcija, pavyzdžiui, skaičiuotuvas, arba API kvietimas trečiosios šalies paslaugai, pavyzdžiui, akcijų kainų patikrinimas ar orų prognozė. Dirbtinio intelekto agentų kontekste įrankiai skirti būti vykdomi agentų reaguojant į **modelio sukurtus funkcijų kvietimus**.

## Kokiems atvejams jis gali būti taikomas?

DI agentai gali naudoti įrankius sudėtingoms užduotims atlikti, informacijai gauti ar sprendimams priimti. Įrankių naudojimo dizaino šablonas dažnai taikomas scenarijuose, kuriuose reikia dinamiškai bendrauti su išorinėmis sistemomis, tokiomis kaip duomenų bazės, interneto paslaugos ar kodo interpretatoriai. Ši galimybė naudinga įvairiems atvejams, įskaitant:

- **Dinaminis informacijos gavimas:** agentai gali užklausti išorines API arba duomenų bazes, kad gautų naujausius duomenis (pvz., užklausti SQLite duomenų bazę duomenų analizei, gauti akcijų kainas ar orų informaciją).
- **Kodo vykdymas ir interpretavimas:** agentai gali vykdyti kodą ar scenarijus matematikos problemoms spręsti, ataskaitoms generuoti ar simuliacijoms atlikti.
- **Darbo srautų automatizavimas:** automatizuoti pasikartojančius ar daugiasluoksnius darbo srautus integruojant tokias priemones kaip užduočių planuotojai, el. pašto paslaugos ar duomenų vamzdeliai.
- **Klientų aptarnavimas:** agentai gali sąveikauti su CRM sistemomis, bilietų platformomis ar žinių bazėmis, kad spręstų vartotojų užklausas.
- **Turinio generavimas ir redagavimas:** agentai gali naudoti priemones kaip gramatikos tikrinimo įrankiai, teksto santraukos ar turinio saugos vertintojai, padedančius kuriant turinį.

## Kokios yra būtinos sudedamosios dalys / blokai įrankių naudojimo dizaino šablonui įgyvendinti?

Šios sudedamosios dalys leidžia DI agentui atlikti įvairias užduotis. Pažvelkime į pagrindines dalis, reikalingas Įrankių Naudojimo Dizaino Šablonui įgyvendinti:

- **Funkcijų/Įrankių schemos**: Detalios prieinamų įrankių apibrėžtys, įskaitant funkcijos pavadinimą, paskirtį, reikalingus parametrus ir numatomus išvedamus duomenis. Šios schemos leidžia LLM suprasti, kokie įrankiai yra pasiekiami ir kaip sudaryti galiojančius užklausimus.

- **Funkcijų vykdymo logika**: Nustato, kaip ir kada įrankiai kviečiami, remiantis vartotojo ketinimu ir pokalbio kontekstu. Tai gali apimti planavimo modulius, maršrutizavimo mechanizmus ar sąlyginį srautą, kuris dinamiškai nusprendžia įrankių naudojimą.

- **Žinučių tvarkymo sistema**: Komponentai, valdyti pokalbio eigą tarp vartotojo įvesties, LLM atsakymų, įrankių kvietimų ir atsakymų iš įrankių.

- **Įrankių integracijos sistema**: Infrastruktūra, jungianti agentą su įvairiais įrankiais, ar tai būtų paprastos funkcijos, ar sudėtingos išorinės paslaugos.

- **Klaidos valdymas ir patikra**: Mechanizmai, skirtos įrankių vykdymo klaidoms tvarkyti, parametrų patikrai ir neplanuotų atsakymų valdymui.

- **Būsenos valdymas**: Sekama pokalbio būsena, ankstesni įrankių naudojimai ir nuolatiniai duomenys, užtikrinantys nuoseklumą daugiasluoksniuose pokalbiuose.

Toliau pažvelkime detaliau į funkcijų/įrankių kvietimą.
 
### Funkcijų/Įrankių Kvietimas

Funkcijų kvietimas yra pagrindinis būdas, kuriuo leidžiame Didiesiems Kalbos Modeliams (LLM) sąveikauti su įrankiais. Dažnai matysite, kad „Funkcija“ ir „Įrankis“ vartojami sąmoningai, nes „funkcijos“ (pakartotinai naudojamo kodo blokai) yra tie „įrankiai“, kuriuos agentai naudoja užduotims atlikti. Kad būtų galima iškviesti funkcijos kodą, LLM turi palyginti vartotojo užklausą su funkcijos aprašymu. Tam į LLM siunčiama schema, kurioje pateikti visi galimų funkcijų aprašymai. Tuomet LLM pasirenka tinkamiausią užduočiai funkciją ir grąžina jos pavadinimą bei argumentus. Pasirinkta funkcija yra iškviesta, jos atsakymas siunčiamas atgal LLM, kuris šią informaciją naudoja atsakydamas į vartotojo užklausą.

Kad įgyvendintumėte funkcijų kvietimą agentams, jums reikės:

1. LLM modelio, palaikančio funkcijų kvietimą
2. Schemos, kurioje pateikti funkcijų aprašymai
3. Kodo kiekvienai aprašytai funkcijai

Pažiūrėkime pavyzdį, kaip gauti dabartinį laiką mieste:

1. **Inicijuokite LLM, palaikantį funkcijų kvietimą:**

    Ne visi modeliai palaiko funkcijų kvietimą, todėl svarbu patikrinti, ar jūsų naudojamas LLM tai palaiko. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> palaiko funkcijų kvietimą. Galime pradėti inicijuodami OpenAI klientą, skirtą Azure OpenAI **Responses API** (stabilus `/openai/v1/` galutinis taškas – nereikia `api_version`).

    ```python
    # Inicijuokite OpenAI klientą Azure OpenAI (Atsakymų API, v1 galinis taškas)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Sukurkite Funkcijos Schemos apibrėžimą**:

    Toliau apibrėšime JSON schemą, kurioje pateiktas funkcijos pavadinimas, aprašymas, ką funkcija atlieka, bei funkcijos parametrų pavadinimai ir aprašymai.
    Tada šią schemą perduosime anksčiau sukurtiems klientui, kartu su vartotojo užklausa rasti laiką San Franciske. Svarbu atkreipti dėmesį, kad grąžinama yra ne galutinis atsakymas į klausimą, o **įrankio kvietimas**. Kaip minėta anksčiau, LLM grąžina pasirinktą užduočiai funkcijos pavadinimą ir argumentus, kurie bus jai perduoti.

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

    # Pirmasis API kvietimas: Paprašykite modelio naudoti funkciją
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Atsakymų API grąžina įrankio kvietimus kaip function_call elementus response.output.
    # Pridėkite juos prie pokalbio, kad modelis turėtų pilną kontekstą kitame žingsnyje.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Funkcijos kodas, reikalingas užduočiai atlikti:**

    Kadangi LLM pasirinko, kuri funkcija turi būti įvykdyta, reikia įgyvendinti ir vykdyti kodo dalį, kuri atlieka užduotį.
    Galime įgyvendinti dabartinio laiko gavimo kodą Python kalba. Taip pat reikės parašyti kodą, kuris iš atsakymo žinutės išskirs funkcijos pavadinimą ir argumentus, kad būtų gautas galutinis rezultatas.

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
    # Tvarkykite funkcijų iškvietimus
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Grąžinkite įrankio rezultatą kaip function_call_output elementą
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Antras API kvietimas: gaukite galutinį modelio atsakymą
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

Funkcijų Kvietimas yra pagrindinė daugumos, jei ne visų, agentų įrankių naudojimo dizaino dalis, tačiau jį įgyvendinti nuo nulio kartais gali būti sudėtinga.
Kaip sužinojome [Pamokoje 2](../../../02-explore-agentic-frameworks), agentų sistemos suteikia iš anksto paruoštus blokus, skirtus įrankių naudojimui įgyvendinti.
 
## Įrankių Naudojimo Pavyzdžiai su Agentų Sistemomis

Čia pateikti keli pavyzdžiai, kaip galite įgyvendinti Įrankių Naudojimo Dizaino Šabloną naudojant skirtingas agentų sistemas:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> yra atviro kodo DI sistema, skirta kurti DI agentams. Ji supaprastina funkcijų kvietimo naudojimą, leidžiant apibrėžti įrankius kaip Python funkcijas su `@tool` dekoratoriumi. Sistema tvarko komunikaciją tarp modelio ir jūsų kodo. Taip pat suteikia prieigą prie iš anksto paruoštų įrankių, tokių kaip Failų Paieška ir Kodo Interpretatorius per `FoundryChatClient`.

Toliau pateiktame diagramoje iliustruojamas funkcijų kvietimo procesas su Microsoft Agent Framework:

![function calling](../../../translated_images/lt/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework įrankiai apibrėžiami kaip dekoruotos funkcijos. Galime anksčiau matytą funkciją `get_current_time` paversti įrankiu naudodami `@tool` dekoratorių. Sistema automatiškai serializuos funkciją ir jos parametrus, sukurdama schemą, kuri bus siunčiama LLM.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> yra naujesnė agentų sistema, sukurta siekiant suteikti kūrėjams galimybę saugiai kurti, diegti ir išplėsti aukštos kokybės DI agentus be būtinybės valdyti pagrindines skaičiavimo ir saugojimo išteklius. Ji ypač naudinga įmonių programoms, nes yra visiškai valdomas servisą su įmonių lygio saugumu.

Palyginus su tiesioginiu LLM API naudojimu, Microsoft Foundry Agent Service suteikia keletą privalumų, tokių kaip:

- Automatinis įrankių kvietimas – nereikia analizuoti įrankių kvietimų, vykdyti įrankį ir tvarkyti atsakymus; visa tai dabar vyksta serverio pusėje
- Saugiai valdoma informacija – nereikia valdyti savo pokalbio būsenos, galima pasikliauti temomis (threads), kuriose saugoma visa reikalinga informacija
- Iš karto paruošti įrankiai – įrankiai, leidžiantys bendrauti su duomenų šaltiniais, tokiais kaip Bing, Azure AI Search ir Azure Functions.

Microsoft Foundry Agent Service įrankius galima suskirstyti į dvi kategorijas:

1. Žinių įrankiai:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Paieškos integracija</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Failų Paieška</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Paieška</a>

2. Veiksmų įrankiai:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funkcijų Kvietimas</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kodo Interpretatorius</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI apibrėžti įrankiai</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agentų Servisas leidžia naudoti šiuos įrankius kartu kaip `įrankių rinkinį`. Taip pat naudoja `threads`, kurie seka pranešimų istoriją iš konkretaus pokalbio.

Įsivaizduokite, kad esate pardavimų agentas įmonėje Contoso. Norite sukurti pokalbių agentą, kuris galėtų atsakyti į klausimus apie jūsų pardavimų duomenis.

Toliau pateiktas paveikslėlis iliustruoja, kaip galima naudoti Microsoft Foundry Agent Service analizuoti jūsų pardavimų duomenis:

![Agentų Serviso Veikimas](../../../translated_images/lt/agent-service-in-action.34fb465c9a84659e.webp)

Norėdami naudoti bet kurį iš šių įrankių su servisu, galime sukurti klientą ir apibrėžti įrankį ar įrankių rinkinį. Praktiniam įgyvendinimui galime naudoti šį Python kodą. LLM galės peržiūrėti įrankių rinkinį ir nuspręsti, ar naudoti vartotojo sukurtą funkciją `fetch_sales_data_using_sqlite_query`, ar iš anksto paruoštą Kodo Interpretatorių, priklausomai nuo vartotojo užklausos.

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

# Inicijuoti įrankių rinkinį
toolset = ToolSet()

# Inicijuoti funkcijų iškvietimo agentą su fetch_sales_data_using_sqlite_query funkcija ir pridėti ją prie įrankių rinkinio
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicijuoti Kodo interpreterių įrankį ir pridėti jį prie įrankių rinkinio.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Kokie ypatingi aspektai naudojant Įrankių Naudojimo Dizaino Šabloną kuriant patikimus DI agentus?

Dažnas susirūpinimas dėl dinamiškai generuojamo LLM SQL yra saugumas, ypač SQL injekcijos ar kenkėjiškų veiksmų, tokių kaip duomenų bazės ištrynimas ar pažeidimas, rizika. Nors šie rūpesčiai yra pagrįsti, jie gali būti veiksmingai suvaldyti tinkamai sukonfigūruojant duomenų bazės prieigos teises. Daugumai duomenų bazių tai reiškia konfigūruoti duomenų bazę skaitymo režimu. Tokiose duomenų bazėse kaip PostgreSQL ar Azure SQL programai turi būti priskirta tik skaitymo (SELECT) rolė.

Programos paleidimas saugioje aplinkoje dar labiau pagerina apsaugą. Įmonių scenarijuose duomenys paprastai yra išskiriami ir transformuojami iš operacinių sistemų į skaitymui skirtą duomenų bazę arba duomenų sandėlį su lengvai suprantama schema. Šis metodas užtikrina, kad duomenys yra saugūs, optimizuoti našumui ir prieinamumui, o programai suteikiama ribota, tik skaitymo prieiga.

## Pavyzdiniai Kodai

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Turite daugiau klausimų apie Įrankių Naudojimo Dizaino Šablonus?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), susitikite su kitais besimokančiais, dalyvaukite konsultacijų valandose ir gaukite atsakymus į DI agentų klausimus.

## Papildomi Ištekliai

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agentų Serviso Darbų Dirbtuvės</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Kūrybinio Rašytojo Daugiaprogramių Dirbtuvės</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Apžvalga</a>


## Šio agento „dūmų testavimas“ (pasirinktinai)

Kai išmoksite diegti agentus [16 pamokoje](../16-deploying-scalable-agents/README.md), galite patikrinti šios pamokos `TravelToolAgent` („ar jis vis dar kviečia savo įrankius ir atsako?“) su [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Žr. [`tests/README.md`](../tests/README.md), kaip jį paleisti.

## Ankstesnė pamoka

[Agentinis dizaino modelių supratimas](../03-agentic-design-patterns/README.md)

## Kita pamoka

[Agentinis RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->