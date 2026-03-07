[![Kaip sukurti gerus AI agentus](../../../translated_images/lt/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Spustelėkite aukščiau esantį paveikslėlį, kad peržiūrėtumėte šio pamokos vaizdo įrašą)_

# Įrankių naudojimo dizaino šablonas

Įrankiai yra įdomūs, nes jie leidžia AI agentams turėti platesnį gebėjimų spektrą. Vietoj to, kad agentas turėtų ribotą veiksmų rinkinį, pridėjus įrankį, agentas dabar gali atlikti platų veiksmų spektrą. Šiame skyriuje nagrinėsime Įrankių naudojimo dizaino šabloną, kuris aprašo, kaip AI agentai gali naudoti specifinius įrankius savo tikslams pasiekti.

## Įvadas

Šioje pamokoje sieksime atsakyti į šiuos klausimus:

- Kas yra įrankių naudojimo dizaino šablonas?
- Kokie yra jo taikymo atvejai?
- Kokie elementai/statybiniai blokai reikalingi dizaino šablonui įgyvendinti?
- Kokie yra ypatingi aspektai naudojant Įrankių naudojimo dizaino šabloną kuriant patikimus AI agentus?

## Mokymosi tikslai

Baigę šią pamoką galėsite:

- Apibrėžti Įrankių naudojimo dizaino šabloną ir jo paskirtį.
- Nustatyti taikymo atvejus, kuriose galima taikyti Įrankių naudojimo dizaino šabloną.
- Suprasti pagrindinius elementus, reikalingus šablonui įgyvendinti.
- Pripažinti aspektus, užtikrinančius patikimumą naudojant šį dizaino šabloną AI agentuose.

## Kas yra Įrankių naudojimo dizaino šablonas?

**Įrankių naudojimo dizaino šablonas** orientuotas į tai, kad LLM galėtų sąveikauti su išoriniais įrankiais tam, kad pasiektų konkrečius tikslus. Įrankiai yra kodas, kurį agentas gali vykdyti, kad atliktų veiksmus. Įrankis gali būti paprasta funkcija, pvz., skaičiuoklė, arba trečiosios šalies paslaugos API kvietimas, pvz., akcijų kainų paieška ar orų prognozė. AI agentų kontekste įrankiai skirti būti vykdomi agentų atsakant į **modelio sukurtus funkcijų kvietimus**.

## Kokiose situacijose jis gali būti taikomas?

AI agentai gali naudoti įrankius sudėtingoms užduotims atlikti, informacijai gauti ar sprendimams priimti. Įrankių naudojimo dizaino šablonas dažnai naudojamas scenarijuose, reikalaujančiuose dinaminės sąveikos su išorinėmis sistemomis, tokiomis kaip duomenų bazės, interneto paslaugos ar kodo interpretatoriai. Ši galimybė yra naudinga daugelyje skirtingų atvejų, įskaitant:

- **Dinaminis informacijos gavimas:** agentai gali kreiptis į išorines API arba duomenų bazes, kad gautų naujausią informaciją (pvz., užklausos SQLite duomenų bazėje duomenų analizei, akcijų kainų ar orų informacijos gavimas).
- **Kodo vykdymas ir interpretacija:** agentai gali vykdyti kodą arba scenarijus, spręsti matematines užduotis, kurti ataskaitas arba vykdyti simuliacijas.
- **Darbo eigų automatizavimas:** automatizuoti pasikartojančias arba daugiažingsnes darbo eigos integruojant įrankius, tokius kaip užduočių tvarkyklės, el. pašto paslaugos ar duomenų srautai.
- **Klientų aptarnavimas:** agentai gali sąveikauti su CRM sistemomis, bilietų platformomis ar žinių bazėmis, siekdami atsakyti į vartotojų užklausas.
- **Turinio kūrimas ir redagavimas:** agentai gali naudoti įrankius, tokius kaip gramatikos tikrintuvai, teksto santraukų kūrėjai ar turinio saugumo vertintojai, padėdami turinio kūrimo užduotyse.

## Kokie elementai/statybiniai blokai reikalingi Įrankių naudojimo dizaino šablonui įgyvendinti?

Šie statybiniai blokai leidžia AI agentui atlikti platų užduočių spektrą. Pažiūrėkime pagrindinius elementus, reikalingus Įrankių naudojimo dizaino šablonui įgyvendinti:

- **Funkcijų/įrankių schemos:** Detalūs galimų įrankių apibrėžimai, įskaitant funkcijos pavadinimą, paskirtį, reikalingus parametrus ir laukiamus rezultatus. Šios schemos leidžia LLM suprasti, kokie įrankiai yra prieinami ir kaip suformuoti galiojančias užklausas.

- **Funkcijų vykdymo logika:** Nustato, kaip ir kada įrankiai kviečiami, remiantis vartotojo ketinimu ir pokalbio kontekstu. Gali apimti planavimo modulius, maršrutų mechanizmus arba sąlyginius srautus, kurie dinamiškai nustato įrankių naudojimą.

- **Pranešimų valdymo sistema:** Komponentai, kurie valdo pokalbio eigą tarp vartotojo įvesties, LLM atsakymų, įrankių kvietimų ir įrankių atsakymų.

- **Įrankių integracijos sistema:** Infrastruktūra, jungianti agentą su įvairiais įrankiais, nesvarbu, ar tai paprastos funkcijos, ar sudėtingos išorinės paslaugos.

- **Klaidų valdymas ir patikra:** Mechanizmai, skirti valdyti įrankių vykdymo klaidas, tikrinti parametrų teisingumą ir tvarkyti netikėtus atsakymus.

- **Būsenos valdymas:** Sekimas pokalbio kontekstu, anksčiau vykdytais įrankių kvietimais ir nuolatiniais duomenimis, kad būtų užtikrintas nuoseklumas daugiasluoksnėse sąveikose.

Toliau išsamiau pažvelgsime į funkcijų/įrankių kvietimą.

### Funkcijų/įrankių kvietimas

Funkcijų kvietimas yra pagrindinis būdas, kuriuo dideli kalbos modeliai (LLM) sąveikauja su įrankiais. Dažnai matysite, kaip „Funkcija“ ir „Įrankis“ vartojami kaip sinonimai, nes „funkcijos“ (pakartotinai naudojamas kodo blokas) yra įrankiai, kuriuos agentai naudoja užduotims atlikti. Kad funkcijos kodas būtų iškviestas, LLM turi palyginti vartotojo užklausą su funkcijos aprašu. Tam skiriama schema, kurioje yra visų turimų funkcijų aprašai ir kuri siunčiama LLM. Tada LLM parenka tinkamiausią funkciją užduočiai ir grąžina jos pavadinimą bei argumentus. Pasirinkta funkcija yra iškviečiama, jos atsakymas gražinamas atgal LLM, kuris naudoja informaciją vartotojo užklausai atsakyti.

Kūrėjams, norintiems įgyvendinti funkcijų kvietimą agentams, reikės:

1. LLM modelio, palaikančio funkcijų kvietimą
2. Schemos, kurioje aprašytos funkcijos
3. Kodo kiekvienai aprašytai funkcijai

Pavyzdžiui, paimkime dabartinio laiko gavimo konkrečiame mieste iliustracijai:

1. **Inicijuokite LLM, palaikantį funkcijų kvietimą:**

    Ne visi modeliai palaiko funkcijų kvietimą, todėl svarbu patikrinti, ar jūsų naudojamas LLM tai palaiko. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> palaiko funkcijų kvietimą. Galime pradėti nuo Azure OpenAI kliento inicijavimo. 

    ```python
    # Inicializuoti Azure OpenAI klientą
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Sukurkite funkcijos schemą:**

    Toliau apibrėšime JSON schemą, kurioje bus funkcijos pavadinimas, jos veiklos aprašymas, funkcijos parametrų pavadinimai ir aprašymai.
    Po to šią schemą perduosime anksčiau sukurtam klientui kartu su vartotojo užklausa surasti laiką San Franciske. Svarbu pažymėti, kad **įrankio kvietimas** yra grąžinamas rezultatas, **o ne** galutinis atsakymas į klausimą. Kaip minėta anksčiau, LLM grąžina užduočiai parinktos funkcijos pavadinimą ir argumentus, kurie bus perduoti funkcijai.

    ```python
    # Funkcijos aprašymas modeliui perskaityti
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
  
    # Pradinis vartotojo pranešimas
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Pirmas API kvietimas: Paprašykite modelio naudoti funkciją
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Apdorokite modelio atsakymą
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

    Dabar, kai LLM pasirinko, kuri funkcija turi būti vykdoma, reikia įgyvendinti ir vykdyti užduotį atliekančią kodo dalį.
    Galime įgyvendinti laikrodis funkciją Python kalba. Taip pat reikės parašyti kodą, kuris iš atsakymo žinutės ištrauktų funkcijos pavadinimą ir argumentus, kad būtų gautas galutinis rezultatas.

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
     # Apdoroti funkcijų kvietimus
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

Funkcijų kvietimas yra daugumos, jei ne visų, agentų įrankių naudojimo dizaino šablono pagrindas, tačiau jo įgyvendinimas nuo nulio kartais gali būti sudėtingas.
Kaip sužinojome [Pamokoje 2](../../../02-explore-agentic-frameworks), agentų karkasai suteikia iš anksto paruoštus statybinius blokus įrankių naudojimui įgyvendinti.

## Įrankių naudojimo pavyzdžiai su agentų karkasais

Štai keletas pavyzdžių, kaip galite įgyvendinti Įrankių naudojimo dizaino šabloną naudojant įvairius agentų karkasus:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> yra atviro kodo AI karkasas AI agentams kurti. Jis palengvina funkcijų kvietimo naudojimą leidžiant apibrėžti įrankius kaip Python funkcijas su `@tool` dekoratoriumi. Karkasas automatiškai tvarko komunikaciją tarp modelio ir jūsų kodo. Taip pat suteikia prieigą prie iš anksto paruoštų įrankių, tokių kaip File Search ir Code Interpreter, per `AzureAIProjectAgentProvider`.

Toliau pateiktas diagramų pavyzdys iliustruoja funkcijų kvietimo procesą su Microsoft Agent Framework:

![function calling](../../../translated_images/lt/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework įrankiai apibrėžiami kaip dekoruotos funkcijos. Galime paversti anksčiau matytą `get_current_time` funkciją į įrankį naudodami `@tool` dekoratorių. Karkasas automatiškai serializuoja funkciją ir jos parametrus, sukūręs schemą atsiuntimui LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Sukurkite klientą
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Sukurkite agentą ir paleiskite su įrankiu
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> yra naujesnis agentų karkasas, kuris skirtas padėti kūrėjams saugiai kurti, diegti ir išplėsti aukštos kokybės ir išplečiamus AI agentus, nereikalaujant valdyti pagrindinių kompiuterių ir saugyklos išteklių. Ypač naudinga verslo programoms, nes tai pilnai valdomas servisas su verslo lygio saugumu.

Lyginant su tiesiogine darbą su LLM API, Azure AI Agent Service suteikia keletą pranašumų, įskaitant:

- Automatinį įrankių kvietimą – nereikia analizuoti įrankio kvietimo, vykdyti įrankio ir tvarkyti atsakymo; visa tai atliekama serverio pusėje
- Saugiai valdomus duomenis – vietoj savo pokalbių būsenos valdymo galite pasikliauti temomis (threads) saugoti visą reikalingą informaciją
- Iš anksto paruoštus įrankius – įrankius, skirtus sąveikai su jūsų duomenų šaltiniais, tokiais kaip Bing, Azure AI Search ir Azure Functions.

Azure AI Agent Service įrankius galima suskirstyti į dvi kategorijas:

1. Žinių įrankiai:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Ryškinimas su Bing paieška</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Failų paieška</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Veiksmų įrankiai:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funkcijų kvietimas</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kodo interpretatorius</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI apibrėžti įrankiai</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure funkcijos</a>

Agentų servisas leidžia naudoti šiuos įrankius kartu kaip `įrankių rinkinį` (toolset). Taip pat naudojamos `temos` (threads), kurios seka konkretaus pokalbio žinučių istoriją.

Įsivaizduokite, kad esate įmonės Contoso pardavimų agentas. Norite sukurti pokalbių agentą, kuris galėtų atsakyti į klausimus apie jūsų pardavimų duomenis.

Toliau pateikta nuotrauka iliustruoja, kaip galite naudoti Azure AI Agent Service analizuojant savo pardavimų duomenis:

![Agentic Service In Action](../../../translated_images/lt/agent-service-in-action.34fb465c9a84659e.webp)

Norėdami naudoti bet kurį iš šių įrankių su servisu, galime sukurti klientą ir apibrėžti įrankį ar įrankių rinkinį. Praktiniam įgyvendinimui galime naudoti šį Python kodą. LLM galės pažvelgti į įrankių rinkinį ir nuspręsti, ar naudoti vartotojo sukurtą funkciją `fetch_sales_data_using_sqlite_query`, ar iš anksto paruoštą Kodo interpretatorių, priklausomai nuo vartotojo užklausos.

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

# Inicializuoti įrankių rinkinį
toolset = ToolSet()

# Inicializuoti funkcijų kvietimo agentą su fetch_sales_data_using_sqlite_query funkcija ir pridėti ją prie įrankių rinkinio
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializuoti Kodo Interpretatoriaus įrankį ir pridėti jį prie įrankių rinkinio.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Kokie ypatingi aspektai naudojant Įrankių naudojimo dizaino šabloną kuriant patikimus AI agentus?

Bendra problema su LLM dinamiškai sugeneruotu SQL yra saugumas, ypač SQL įpurškimo ar žalingų veiksmų, tokių kaip duomenų bazės ištrynimas arba klastojimas, rizika. Nors šios baimės pagrįstos, jas galima veiksmingai sumažinti teisingai sukonfigūravus duomenų bazės prieigos teises. Daugumai duomenų bazių tai reiškia konfigūruoti duomenų bazę kaip prieinamą tik skaitymui. Duomenų bazių paslaugoms, tokioms kaip PostgreSQL ar Azure SQL, programai turėtų būti priskirta tik skaitymo (SELECT) teisė.

Programos paleidimas saugioje aplinkoje dar labiau sustiprina apsaugą. Verslo scenarijuose duomenys paprastai yra išgaunami ir transformuojami iš operacinių sistemų į tik skaitomą duomenų bazę ar duomenų sandėlį su draugiška schema vartotojui. Šis požiūris užtikrina, kad duomenys yra saugūs, optimizuoti veikimui ir prieinamumui bei kad programai būtų suteikta ribota, tik skaitymo prieiga.

## Pavyzdiniai kodai

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Turite daugiau klausimų apie Įrankių naudojimo dizaino šablonus?

Prisijunkite prie [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), susitikite su kitais besimokančiais, dalyvaukite konsultacijose ir gaukite atsakymus į savo AI agentų klausimus.

## Papildomi ištekliai

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Dirbtuvės</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso kūrybinio rašytojo daugiagentinės dirbtuvės</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework apžvalga</a>

## Ankstesnė pamoka

[Agentų dizaino šablonų supratimas](../03-agentic-design-patterns/README.md)

## Kita pamoka
[Agentinis RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogišką vertimą. Mes neprisiimame atsakomybės už bet kokius nesusipratimus ar neteisingus interpretavimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->