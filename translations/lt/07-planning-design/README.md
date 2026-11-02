[![Planavimo dizaino šablonas](../../../translated_images/lt/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Spustelėkite aukščiau esantį paveikslėlį, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

# Planavimo dizainas

## Įvadas

Šioje pamokoje aptarsime

* Aiškaus bendro tikslo apibrėžimą ir sudėtingos užduoties suskaidymą į valdomas užduotis.
* Struktūruoto išvesties naudojimą patikimesnėms ir mašinai suprantamesnėms atsakymams.
* Įvykiais grįsto požiūrio taikymą dinaminėms užduotims ir netikėtiems įvedimams valdyti.

## Mokymosi tikslai

Baigę šią pamoką suprasite:

* Nustatyti ir apibrėžti bendrą tikslą AI agentui, užtikrinant, kad jis aiškiai žinotų, ką reikia pasiekti.
* Suskaidyti sudėtingą užduotį į valdomas poskyrias ir juos organizuoti į logišką seką.
* Aprūpinti agentus tinkamais įrankiais (pvz., paieškos ar duomenų analizės įrankiais), nuspręsti, kada ir kaip juos naudoti, bei valdyti netikėtas situacijas.
* Įvertinti poskyrių rezultatus, matuoti našumą ir kartoti veiksmus, siekiant pagerinti galutinį rezultatą.

## Bendro tikslo apibrėžimas ir užduoties suskaidymas

![Tikslų ir užduočių apibrėžimas](../../../translated_images/lt/defining-goals-tasks.d70439e19e37c47a.webp)

Daugelis realių užduočių yra pernelyg sudėtingos, kad jas būtų galima spręsti vienu žingsniu. AI agentui reikia glausto tikslo, kuris nukreiptų jo planavimą ir veiksmus. Pavyzdžiui, apsvarstykite tikslą:

    "Sukurti 3 dienų kelionės planą."

Nors tai paprasta išsakyti, vis tiek reikia jį patikslinti. Kuo aiškesnis tikslas, tuo geriau agentas (ir bet kurie žmonių bendradarbiai) gali susitelkti ties tinkamo rezultato pasiekimu, pvz., kurti išsamų maršrutą su skrydžių pasiūlymais, viešbučių rekomendacijomis ir veiklų pasiūlymais.

### Užduoties suskaidymas

Didelės ar sudėtingos užduotys tampa valdomesnės, kai jos suskaidomos į mažesnes, tikslingas poskyrius.
Kelionės plano pavyzdyje tikslą galima suskaidyti į:

* Skrydžio rezervavimą
* Viešbučio rezervavimą
* Automobilio nuomą
* Personalizavimą

Kiekvieną poskyrį tuomet gali vykdyti atskiri agentai ar procesai. Vienas agentas gali specializuotis geriausių skrydžių pasiūlymų paieškoje, kitas – viešbučių rezervavimuose ir pan. Koordinuojantis arba „žemyn srautu“ esantis agentas gali surinkti šiuos rezultatus į vieną darnų maršrutą galutiniam naudotojui.

Šis modulinis požiūris leidžia ir nuosekliai tobulinti sistemą. Pavyzdžiui, galite pridėti specializuotus agentus maisto rekomendacijoms ar vietinėms veikloms ir laikui bėgant tobulinti maršrutą.

### Struktūruotas išvestis

Dideli kalbos modeliai (LLM) gali generuoti struktūruotą išvestį (pvz., JSON), kurią lengviau apdoroti žemyn srauto agentams ar paslaugoms. Tai ypač naudinga daugiaagentinėje aplinkoje, kur po planavimo išvesties gavimo galima vykdyti užduotis.

Toliau pateiktoje Python kodo ištraukoje paprastas planavimo agentas suskaido tikslą į poskyrius ir sugeneruoja struktūruotą planą:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Kelionės posrities modelis
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # norime priskirti užduotį agentui

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Apibrėžti vartotojo žinutę
system_prompt = """You are a planner agent.
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
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text
pprint(json.loads(response_content))
```

### Planavimo agentas su daugiaagentinė orkestracija

Šiame pavyzdyje Semantic Router Agent gauna vartotojo užklausą (pvz., „Man reikia viešbučio plano mano kelionei.“).

Tuomet planuotojas:

* Gauk viešbučių planą: planuotojas paima vartotojo žinutę ir, remdamasis sistemos užklausimu (įskaitant prieinamų agentų informaciją), sukuria struktūruotą kelionės planą.
* Išvardina agentus ir jų įrankius: agentų registras laiko agentų sąrašą (pvz., skrydžio, viešbučio, automobilio nuomos ir veiklų agentus) kartu su jų funkcijomis ar įrankiais.
* Nukreipia planą atitinkamiems agentams: priklausomai nuo poskyrių skaičiaus, planuotojas arba siunčia žinutę tiesiogiai skirto agento valdymui (vienos užduoties atvejais), arba koordinuoja per grupinio pokalbio valdytoją daugiaagentinei sąveikai.
* Apibendrina rezultatą: galiausiai planuotojas pateikia sukurto plano santrauką aiškumui.
Toliau pateiktas Python kodo pavyzdys iliustruoja šiuos žingsnius:

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

# Kelionės po užduotis modelis

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # mes norime priskirti užduotį agentui

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Sukurkite klientą

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# Apibrėžkite vartotojo pranešimą

system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text

# Atspausdinkite atsakymo turinį po jo užkrovimo kaip JSON

pprint(json.loads(response_content))
```

Toliau pateikiama kodo išvestis, kurią galite naudoti norėdami nukreipti į `assigned_agent` ir apibendrinti kelionės planą galutiniam vartotojui.

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

Pavyzdinė užrašų knygelė su ankstesniu kodo pavyzdžiu yra prieinama [čia](./code_samples/07-python-agent-framework.ipynb).

### Pasikartojantis planavimas

Kai kurios užduotys reikalauja bendravimo pirmyn ir atgal arba perplanavimo, kai vienos poskyrio rezultatas įtakoja kitą. Pavyzdžiui, jei agentas aptinka netikėtą duomenų formatą skrydžių rezervavimo metu, jam gali tekti pakeisti strategiją prieš pereinant prie viešbučių rezervavimo.

Be to, vartotojo atsiliepimai (pvz., žmogus nusprendžia, kad pageidauja ankstesnio skrydžio) gali inicijuoti dalinį perplanavimą. Šis dinamiškas, iteratyvus požiūris užtikrina, kad galutinis sprendimas atitiktų realaus pasaulio apribojimus ir besikeičiančius vartotojų pageidavimus.

pvz. kodo pavyzdys

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. tas pats kaip ankstesniame kode ir perduoti naudotojo istoriją, dabartinį planą

system_prompt = """You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(
    input=user_message,
    instructions=system_prompt,
    context=f"Previous travel plan - {TravelPlan}",
)
# .. pertvarkyti planą ir siųsti užduotis atitinkamiems agentams
```

Daugiau išsamų planavimą rasite Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogposte</a>, skirtame sudėtingoms užduotims spręsti.

## Santrauka

Šiame straipsnyje apžvelgėme pavyzdį, kaip sukurti planuotoją, kuris gali dinamiškai pasirinkti apibrėžtus prieinamus agentus. Planavimo išvestis suskaido užduotis ir priskiria agentams, kad jos būtų vykdomos. Laikoma, kad agentai turi prieigą prie reikalingų funkcijų/įrankių užduočiai atlikti. Be agentų galima įtraukti ir kitus modelius, tokius kaip refleksija, santrauka ir round robin pokalbis, siekiant dar labiau pritaikyti sistemą.

## Papildomi šaltiniai

Magnetic One – daugiaagentė sistema, skirta sudėtingoms užduotims spręsti, kuri parodė įspūdingus rezultatus keliuose sudėtinguose agentic testuose. Nuoroda: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. Šioje įgyvendinimo versijoje orkestratorius kuria užduочiai specifinius planus ir deleguoja užduotis prieinamiems agentams. Be planavimo, orkestratorius taip pat naudoja sekimo mechanizmą stebėti užduoties pažangą ir perplanuoja, jei reikia.

### Turite daugiau klausimų apie Planavimo dizaino šabloną?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), susipažinkite su kitais besimokančiaisiais, dalyvaukite konsultacijose ir gaukite atsakymus į savo AI agentų klausimus.

## Ankstesnė pamoka

[Patikimų AI agentų kūrimas](../06-building-trustworthy-agents/README.md)

## Kitoji pamoka

[Daugiaagentinis dizaino šablonas](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->