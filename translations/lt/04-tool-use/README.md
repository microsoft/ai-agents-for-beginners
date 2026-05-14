[![Kaip sukurti gerus AI agentus](../../../translated_images/lt/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Paspauskite aukščiau esantį paveikslėlį, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

# Įrankių naudojimo dizaino šablonas

Įrankiai yra įdomūs, nes jie leidžia AI agentams turėti platesnį gebėjimų spektrą. Vietoj to, kad agentas turėtų ribotą veiksmų rinkinį, pridėjus įrankį, agentas dabar gali atlikti įvairius veiksmus. Šiame skyriuje pažvelgsime į Įrankių naudojimo dizaino šabloną, kuris aprašo, kaip AI agentai gali naudoti konkrečius įrankius, norėdami pasiekti savo tikslus.

## Įvadas

Šioje pamokoje sieksime atsakyti į šiuos klausimus:

- Kas yra įrankių naudojimo dizaino šablonas?
- Kokiuose naudojimo atvejuose jis gali būti pritaikytas?
- Kokie elementai/komponentai reikalingi šablonui įgyvendinti?
- Kokie yra specialūs svarstymai naudojant Įrankių naudojimo dizaino šabloną, kad būtų sukuriami patikimi AI agentai?

## Mokymosi tikslai

Baigę šią pamoką galėsite:

- Apibrėžti Įrankių naudojimo dizaino šabloną ir jo paskirtį.
- Nustatyti naudojimo atvejus, kuriuose taikomas Įrankių naudojimo dizaino šablonas.
- Suprasti pagrindinius elementus, reikalingus šablonui įgyvendinti.
- Atpažinti svarstymus, užtikrinančius AI agentų patikimumą naudojant šį dizaino šabloną.

## Kas yra Įrankių naudojimo dizaino šablonas?

**Įrankių naudojimo dizaino šablonas** orientuotas į LLM galimybę sąveikauti su išoriniais įrankiais, siekiant konkrečių tikslų. Įrankiai yra kodas, kurį agentas gali vykdyti, atlikdamas veiksmus. Įrankis gali būti paprasta funkcija, pavyzdžiui, skaičiuoklė, arba API kvietimas trečiosios šalies paslaugai, pavyzdžiui, akcijų kainų patikrinimas ar orų prognozė. Dirbtinio intelekto agentų kontekste įrankiai sukurti taip, kad agentai galėtų juos vykdyti reaguodami į **modelio sugeneruotus funkcijų kvietimus**.

## Kokiuose naudojimo atvejuose jis gali būti pritaikytas?

AI agentai gali naudoti įrankius sudėtingoms užduotims atlikti, informacijai gauti ar sprendimams priimti. Įrankių naudojimo dizaino šablonas dažnai taikomas situacijose, kur reikalinga dinamiška sąveika su išorinėmis sistemomis, tokiomis kaip duomenų bazės, interneto paslaugos ar kodo interpretuokliai. Ši galimybė naudinga įvairiose srityse, įskaitant:

- **Dinaminis informacijos gavimas:** agentai gali kreiptis į išorines API ar duomenų bazes, kad gautų naujausią informaciją (pvz., užklausos SQLite duomenų bazėje analizei, akcijų kainų ar orų informacijos gavimas).
- **Kodo vykdymas ir interpretavimas:** agentai gali vykdyti kodą ar scenarijus, spręsti matematines problemas, generuoti ataskaitas ar atlikti simuliacijas.
- **Darbo srautų automatizavimas:** pasikartojančių ar daugiapakopių darbo procesų automatizavimas integruojant įrankius, tokius kaip užduočių tvarkyklės, el. pašto paslaugos ar duomenų srautų vamzdynai.
- **Klientų aptarnavimas:** agentai gali sąveikauti su CRM sistemomis, bilietų platformomis ar žinių bazėmis, spręsti vartotojų užklausas.
- **Turinio generavimas ir redagavimas:** agentai gali naudoti gramatikos tikrintuvus, teksto santraukų kūrėjus ar turinio saugumo vertintojus, padedančius kuriant turinį.

## Kokie elementai/komponentai reikalingi įrankių naudojimo dizaino šablonui įgyvendinti?

Šie komponentai leidžia AI agentui atlikti įvairias užduotis. Pažvelkime į pagrindinius elementus, reikalingus įrankių naudojimo dizaino šablonui įgyvendinti:

- **Funkcijų/Įrankių schemos**: Išsamūs aprašymai apie prieinamus įrankius, įskaitant funkcijų pavadinimus, paskirtį, reikiamus parametrus ir numatomus rezultatus. Šios schemos leidžia LLM suprasti, kokie įrankiai yra prieinami ir kaip sudaryti galiojančius užklausimus.

- **Funkcijų vykdymo logika**: Nustato, kaip ir kada įrankiai kviečiami atsižvelgiant į vartotojo ketinimus ir pokalbio kontekstą. Tai gali apimti planavimo modulius, maršruto nustatymo mechanizmus ar sąlyginį srautą, kuris dinamiškai sprendžia įrankių naudojimą.

- **Pranešimų apdorojimo sistema**: Komponentai, tvarkantys pokalbio srautą tarp vartotojo įėjimų, LLM atsakymų, įrankių kvietimų ir jų rezultatų.

- **Įrankių integracijos sistema**: Infrastruktūra, jungianti agentą su įvairiais įrankiais, nesvarbu, ar tai paprastos funkcijos, ar sudėtingos išorinės paslaugos.

- **Klaidų tvarkymas ir validacija**: Mechanizmai, tvarkantys klaidas vykdant įrankius, tikrinantys parametrų teisingumą ir valdantys netikėtus atsakymus.

- **Būsenos valdymas**: Sekimas pokalbio kontekstui, ankstesniems įrankių sąveikoms ir nuolatiniams duomenims, užtikrinant nuoseklumą daugiažingsnėse sąveikose.

Toliau atidžiau pažvelkime į funkcijų/įrankių kvietimą.

### Funkcijų/Įrankių kvietimas

Funkcijų kvietimas yra pagrindinis būdas, leidžiantis didelių kalbos modelių (LLM) sąveikauti su įrankiais. Dažnai vartojami terminai „funkcija“ ir „įrankis“ yra keičiami, nes „funkcijos“ (pernaudojamo kodo blokai) yra „įrankiai“, kuriuos agentai naudoja užduotims atlikti. Kad būtų galima iškviesti funkciją, LLM turi palyginti vartotojo užklausą su funkcijos aprašymu. Tam LLM siunčiamas schema, kurioje pateikti visų prieinamų funkcijų aprašymai. Tada LLM pasirenka tinkamiausią funkciją užduočiai, grąžina jos pavadinimą ir argumentus. Pasirinkta funkcija iškviečiama, jos atsakymas siunčiamas atgal į LLM, kuris naudoja šią informaciją atsakydamas vartotojui.

Kūrėjams, norintiems įgyvendinti funkcijų kvietimą agentams, reikės:

1. LLM modelio, palaikančio funkcijų kvietimą
2. Schemos, kurioje aprašytos funkcijos
3. Kodo kiekvienai aprašytai funkcijai

Pažiūrėkime pavyzdį, kaip gauti esamą laiką mieste:

1. **Inicijuoti LLM, palaikantį funkcijų kvietimą:**

    Ne visi modeliai palaiko funkcijų kvietimą, tad svarbu patikrinti, ar jūsų naudojamas LLM tai palaiko. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> palaiko funkcijų kvietimą. Galime pradėti inicijuoti Azure OpenAI klientą.

    ```python
    # Inicializuoti Azure OpenAI klientą
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Sukurti funkcijos schemą**:

    Toliau apibrėšime JSON schemą, kurioje bus funkcijos pavadinimas, jos veiklos aprašymas ir parametrų pavadinimai bei aprašymai.
    Šią schemą perduosime anksčiau sukurtam klientui kartu su vartotojo užklausa rasti laiką San Franciske. Svarbu pažymėti, kad grąžinamas ne galutinis atsakymas, o **įrankio kvietimas**. Kaip minėta anksčiau, LLM grąžina pasirinktos funkcijos pavadinimą ir argumentus.

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
  
1. **Funkcijos kodas, reikalingas užduočiai atlikti:**

    Kadangi LLM pasirinko, kuri funkcija turi būti vykdoma, dabar reikia įgyvendinti ir vykdyti užduotį atliekančią kodo dalį.
    Galime parašyti Python kodą, kuris gauna esamą laiką. Taip pat reikės parašyti kodą, kuris ištraukia pavadinimą ir argumentus iš response_message, kad gautume galutinį rezultatą.

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

Funkcijų kvietimas yra daugumos, jei ne visų, agentų įrankių naudojimo dizaino šablonų šerdis, tačiau jo įgyvendinimas nuo nulio kartais gali būti sudėtingas.
Kaip sužinojome [2 pamokoje](../../../02-explore-agentic-frameworks), agentų karkasai suteikia iš anksto paruoštus komponentus įrankių naudojimui įgyvendinti.

## Įrankių naudojimo pavyzdžiai su agentų karkasais

Štai keletas pavyzdžių, kaip galite įgyvendinti Įrankių naudojimo dizaino šabloną naudojant skirtingus agentų karkasus:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> yra atviro kodo AI karkasas AI agentams kurti. Jis supaprastina funkcijų kvietimo naudojimą, leidžiant apibrėžti įrankius kaip Python funkcijas su `@tool` dekoratoriumi. Šis karkasas tvarko komunikaciją tarp modelio ir jūsų kodo. Taip pat suteikia prieigą prie paruoštų įrankių, tokių kaip Failų paieška ir Kodo interpretuoklis per `AzureAIProjectAgentProvider`.

Žemiau parodytas funkcijų kvietimo procesas su Microsoft Agent Framework:

![function calling](../../../translated_images/lt/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework įrankiai apibrėžiami kaip dekoruotos funkcijos. Galime ankstesnį `get_current_time` funkcijos pavyzdį paversti įrankiu naudodami `@tool` dekoratorių. Karkasas automatiškai serializuos funkciją ir jos parametrus, sukurs schemą, kuri bus siunčiama LLM.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> yra naujesnis agentų karkasas, sukurtas padėti kūrėjams saugiai kurti, diegti ir plečiant aukštos kokybės bei išplečiamus AI agentus, nereikalaujant rūpintis pagrindiniais skaičiavimo ir saugyklos resursais. Tai ypač naudinga verslo programoms, nes tai yra pilnai valdomas servisas su įmonių klasės saugumu.

Lyginant su tiesioginiu kūrimu naudojant LLM API, Azure AI Agent Service turi pranašumų, tokių kaip:

- Automatinis įrankių kvietimas – nereikia analizuoti įrankio kvietimo, vykdyti įrankio ir tvarkyti atsako; visa tai vykdoma serverio pusėje
- Saugi duomenų valdymas – vietoje savo pokalbio būseno valdymo galima pasikliauti pokalbių sruogomis, kuriose saugoma visa reikalinga informacija
- Paruošti naudoti įrankiai – įrankiai, leidžiantys sąveikauti su jūsų duomenų šaltiniais, tokiais kaip Bing, Azure AI Search ir Azure Functions

Azure AI Agent Service įrankiai skirstomi į dvi kategorijas:

1. Žinių įrankiai:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing paieškos pagrindimas</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Failų paieška</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Veiksmų įrankiai:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funkcijų kvietimas</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kodo interpretuoklis</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI apibrėžti įrankiai</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agentų servisas leidžia naudoti šiuos įrankius kartu kaip `įrankių rinkinį`. Jis taip pat naudoja `threads` (pokalbių gijas), kurios seka konkretaus pokalbio pranešimų istoriją.

Įsivaizduokite, kad esate pardavimų agentas įmonėje Contoso. Norite sukurti pokalbių agentą, kuris galėtų atsakyti į klausimus apie jūsų pardavimų duomenis.

Žemiau pateiktas paveikslėlis iliustruoja, kaip naudojant Azure AI Agent Service galima analizuoti pardavimų duomenis:

![Agentic Service In Action](../../../translated_images/lt/agent-service-in-action.34fb465c9a84659e.webp)

Norėdami naudoti bet kurį iš šių įrankių su servisu, galime sukurti klientą ir apibrėžti įrankį arba įrankių rinkinį. Praktiniam įgyvendinimui galime naudoti šį Python kodą. LLM galės peržiūrėti įrankių rinkinį ir nuspręsti, ar naudoti vartotojo sukurtą funkciją `fetch_sales_data_using_sqlite_query`, ar paruoštą Kodo interpretuoklį, priklausomai nuo vartotojo užklausos.

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

# Inicializuoti įrankių rinkinį
toolset = ToolSet()

# Inicializuoti funkcijų kvietimo agentą su fetch_sales_data_using_sqlite_query funkcija ir pridėti ją prie įrankių rinkinio
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicializuoti kodų interpretatoriaus įrankį ir pridėti jį prie įrankių rinkinio.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Kokie yra specialūs svarstymai naudojant Įrankių naudojimo dizaino šabloną patikimiems AI agentams kurti?

Dažna problema su LLM dinamiškai generuotu SQL yra saugumas, ypač SQL injekcijos ar piktavališkų veiksmų, tokių kaip duomenų bazės ištrynimas ar pažeidimas, rizika. Nors šie rūpesčiai yra pagrįsti, juos galima veiksmingai sumažinti tinkamai sukonfigūravus duomenų bazės prieigos teises. Daugeliu atvejų tai reiškia duomenų bazės nustatymą tik skaitymui. Duomenų bazių paslaugose, tokiose kaip PostgreSQL ar Azure SQL, programai turi būti priskirta tik skaitymo (SELECT) teisė.

Programos vykdymas saugioje aplinkoje dar labiau padidina apsaugą. Verslo scenarijuose duomenys paprastai yra išgaunami ir transformuojami iš operacinių sistemų į tik skaitymui skirtą duomenų bazę arba duomenų sandėlį su vartotojui draugiška schema. Šis požiūris užtikrina, kad duomenys yra saugūs, optimizuoti našumui ir prieinamumui, o programa turi ribotą, tik skaitymo prieigą.

## Pavyzdiniai kodai

- Python: [Agentų karkasas](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agentų karkasas](./code_samples/04-dotnet-agent-framework.md)

## Turite daugiau klausimų apie Įrankių naudojimo dizaino šablonus?

Prisijunkite prie [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kad susitikti su kitais besimokantiesiems, dalyvauti konsultacijose ir gauti atsakymus į savo AI agentų klausimus.

## Papildomi ištekliai

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agent Service dirbtuvės</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso kūrybinio rašytojo daugiaagentinių dirbtuvių medžiaga</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework apžvalga</a>

## Ankstesnė pamoka

[Agentinio dizaino šablonų supratimas](../03-agentic-design-patterns/README.md)

## Kita pamoka
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->