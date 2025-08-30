<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a28d30590704ea13b6a08d4793cf9c2b",
  "translation_date": "2025-08-30T10:52:57+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "lt"
}
-->
[![Planavimo dizaino šablonas](../../../translated_images/lesson-7-thumbnail.f7163ac557bea1236242cc86b178c3f1bbf5eb07b87f9cd7c256b366e32bcbb6.lt.png)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Spustelėkite aukščiau esančią nuotrauką, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

# Planavimo dizainas

## Įvadas

Šioje pamokoje aptarsime:

* Aiškaus bendro tikslo nustatymą ir sudėtingos užduoties skaidymą į valdomas dalis.
* Struktūrizuoto išvesties formato naudojimą siekiant patikimesnių ir mašinoms suprantamų atsakymų.
* Įvykių valdomo požiūrio taikymą dinaminėms užduotims ir netikėtiems įvesties duomenims spręsti.

## Mokymosi tikslai

Baigę šią pamoką, suprasite:

* Kaip nustatyti ir apibrėžti bendrą AI agento tikslą, užtikrinant, kad jis aiškiai žinotų, ką reikia pasiekti.
* Kaip suskaidyti sudėtingą užduotį į valdomas dalis ir organizuoti jas logine seka.
* Kaip aprūpinti agentus tinkamais įrankiais (pvz., paieškos ar duomenų analizės įrankiais), nuspręsti, kada ir kaip juos naudoti, ir spręsti netikėtas situacijas.
* Kaip įvertinti subtikslų rezultatus, matuoti našumą ir tobulinti veiksmus siekiant geresnio galutinio rezultato.

## Bendro tikslo nustatymas ir užduoties skaidymas

![Tikslų ir užduočių nustatymas](../../../translated_images/defining-goals-tasks.d70439e19e37c47ac76c48b209a4eb515bea5b8a5207f6b2e7b5e597f09ccf6a.lt.png)

Dauguma realaus pasaulio užduočių yra per daug sudėtingos, kad jas būtų galima išspręsti vienu žingsniu. AI agentui reikia aiškaus tikslo, kuris vadovautų jo planavimui ir veiksmams. Pavyzdžiui, apsvarstykite tikslą:

    "Sukurti 3 dienų kelionės maršrutą."

Nors tai paprasta išsakyti, tikslas vis tiek reikalauja patikslinimo. Kuo aiškesnis tikslas, tuo geriau agentas (ir bet kokie žmonių bendradarbiai) gali sutelkti dėmesį į tinkamo rezultato pasiekimą, pvz., sukurti išsamų maršrutą su skrydžių galimybėmis, viešbučių rekomendacijomis ir veiklų pasiūlymais.

### Užduoties skaidymas

Didelės ar sudėtingos užduotys tampa lengviau valdomos, kai jos suskaidomos į mažesnes, tikslui orientuotas dalis. 
Kelionės maršruto pavyzdžiui, tikslą galima suskaidyti į:

* Skrydžių rezervavimą
* Viešbučių rezervavimą
* Automobilių nuomą
* Personalizavimą

Kiekvieną subtikslą gali vykdyti specializuoti agentai ar procesai. Vienas agentas gali specializuotis ieškant geriausių skrydžių pasiūlymų, kitas – viešbučių rezervavime ir t. t. Koordinuojantis arba „žemyninis“ agentas gali sujungti šiuos rezultatus į vieną nuoseklų maršrutą galutiniam naudotojui.

Šis modulinis požiūris taip pat leidžia palaipsniui tobulinti procesą. Pavyzdžiui, galite pridėti specializuotus agentus maisto rekomendacijoms ar vietinių veiklų pasiūlymams ir laikui bėgant tobulinti maršrutą.

### Struktūrizuota išvestis

Dideli kalbiniai modeliai (LLMs) gali generuoti struktūrizuotą išvestį (pvz., JSON), kurią lengviau analizuoti ir apdoroti kitoms agentų ar paslaugų dalims. Tai ypač naudinga daugiagentėje aplinkoje, kur užduotys gali būti vykdomos po planavimo išvesties gavimo. Greita apžvalga:

Šis Python kodo fragmentas demonstruoja paprastą planavimo agentą, kuris suskaido tikslą į subtikslus ir generuoja struktūrizuotą planą:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.azure import AzureAIChatCompletionClient
from azure.core.credentials import AzureKeyCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Travel SubTask Model
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

client = AzureAIChatCompletionClient(
    model="gpt-4o-mini",
    endpoint="https://models.inference.ai.azure.com",
    # To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
    # Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
    model_info={
        "json_output": False,
        "function_calling": True,
        "vision": True,
        "family": "unknown",
    },
)

# Define the user message
messages = [
    SystemMessage(content="""You are an planner agent.
    Your job is to decide which agents to run based on the user's request.
                      Provide your response in JSON format with the following structure:
{'main_task': 'Plan a family trip from Singapore to Melbourne.',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'Book round-trip flights from Singapore to '
                               'Melbourne.'}
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(
        content="Create a travel plan for a family of 2 kids from Singapore to Melboune", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": 'json_object'})

response_content: Optional[str] = response.content if isinstance(
    response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string" )

pprint(json.loads(response_content))

# # Ensure the response content is a valid JSON string before loading it
# response_content: Optional[str] = response.content if isinstance(
#     response.content, str) else None
# if response_content is None:
#     raise ValueError("Response content is not a valid JSON string")

# # Print the response content after loading it as JSON
# pprint(json.loads(response_content))

# Validate the response content with the MathReasoning model
# TravelPlan.model_validate(json.loads(response_content))
```

### Planavimo agentas su daugiagentės orkestracijos funkcija

Šiame pavyzdyje Semantinis maršrutizavimo agentas gauna naudotojo užklausą (pvz., „Man reikia viešbučio plano mano kelionei.“).

Planavimo procesas:

* Gauti viešbučio planą: planuotojas priima naudotojo žinutę ir, remdamasis sistemos užklausa (įskaitant informaciją apie galimus agentus), generuoja struktūrizuotą kelionės planą.
* Agentų ir jų įrankių sąrašas: agentų registras saugo agentų sąrašą (pvz., skrydžių, viešbučių, automobilių nuomos ir veiklų) kartu su jų siūlomomis funkcijomis ar įrankiais.
* Plano nukreipimas atitinkamiems agentams: priklausomai nuo subtikslų skaičiaus, planuotojas arba siunčia žinutę tiesiogiai specializuotam agentui (vienos užduoties scenarijams), arba koordinuoja per grupės pokalbių valdytoją daugiagentės sąveikos atveju.
* Rezultatų apibendrinimas: galiausiai planuotojas apibendrina sugeneruotą planą aiškumui.

Šis Python kodo pavyzdys iliustruoja šiuos veiksmus:

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Travel SubTask Model

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

# Create the client with type-checked environment variables

client = AzureOpenAIChatCompletionClient(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

from pprint import pprint

# Define the user message

messages = [
    SystemMessage(content="""You are an planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": TravelPlan})

# Ensure the response content is a valid JSON string before loading it

response_content: Optional[str] = response.content if isinstance(response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string")

# Print the response content after loading it as JSON

pprint(json.loads(response_content))
```

Toliau pateikiama ankstesnio kodo išvestis, kurią galite naudoti norėdami nukreipti į `assigned_agent` ir apibendrinti kelionės planą galutiniam naudotojui.

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

Ankstesnio kodo pavyzdžio užrašų knygelę galite rasti [čia](07-autogen.ipynb).

### Iteratyvus planavimas

Kai kurios užduotys reikalauja grįžtamojo ryšio arba perplanavimo, kai vieno subtikslo rezultatas daro įtaką kitam. Pavyzdžiui, jei agentas aptinka netikėtą duomenų formatą rezervuodamas skrydžius, jis gali prireikti pritaikyti savo strategiją prieš pereinant prie viešbučių rezervavimo.

Be to, naudotojo atsiliepimai (pvz., žmogus nusprendžia, kad jam labiau patinka ankstesnis skrydis) gali sukelti dalinį perplanavimą. Šis dinamiškas, iteratyvus požiūris užtikrina, kad galutinis sprendimas atitiktų realaus pasaulio apribojimus ir besikeičiančius naudotojo pageidavimus.

Pvz., kodo pavyzdys:

```python
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
#.. same as previous code and pass on the user history, current plan
messages = [
    SystemMessage(content="""You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
    AssistantMessage(content=f"Previous travel plan - {TravelPlan}", source="assistant")
]
# .. re-plan and send the tasks to respective agents
```

Norėdami išsamiau susipažinti su planavimu, peržiūrėkite Magnetic One sprendimą sudėtingoms užduotims spręsti.

## Santrauka

Šiame straipsnyje aptarėme pavyzdį, kaip sukurti planuotoją, kuris gali dinamiškai pasirinkti apibrėžtus agentus. Planavimo išvestis suskaido užduotis ir priskiria agentus, kad jie galėtų jas vykdyti. Daroma prielaida, kad agentai turi prieigą prie funkcijų/įrankių, reikalingų užduočiai atlikti. Be agentų, galite įtraukti kitus šablonus, tokius kaip refleksija, apibendrinimas ir apvalus pokalbis, kad dar labiau pritaikytumėte procesą.

## Papildomi ištekliai

* AutoGen Magnetic One – universalus daugiagentis sprendimas sudėtingoms užduotims spręsti, pasiekęs įspūdingų rezultatų įvairiuose sudėtinguose agentų veiklos testuose. Nuoroda:

Šioje implementacijoje orkestratorius sukuria užduočiai specifinį planą ir deleguoja šias užduotis prieinamiems agentams. Be planavimo, orkestratorius taip pat naudoja stebėjimo mechanizmą užduoties eigai stebėti ir, jei reikia, perplanuoti.

### Turite daugiau klausimų apie planavimo dizaino šabloną?

Prisijunkite prie [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kad susitiktumėte su kitais besimokančiaisiais, dalyvautumėte konsultacijose ir gautumėte atsakymus į savo klausimus apie AI agentus.

## Ankstesnė pamoka

[Patikimų AI agentų kūrimas](../06-building-trustworthy-agents/README.md)

## Kita pamoka

[Daugiagentis dizaino šablonas](../08-multi-agent/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.