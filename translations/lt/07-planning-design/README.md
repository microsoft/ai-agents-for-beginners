[![Planning Design Pattern](../../../translated_images/lt/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Spustelėkite aukščiau esantį paveikslėlį, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

# Planavimo modelis

## Įvadas

Šioje pamokoje aptarsime

* Aiškaus bendro tikslo apibrėžimą ir sudėtingos užduoties suskaidymą į valdomas užduotis.
* Struktūruoto atsakymo naudojimą patikimesniems ir mašininiam apdorojimui pritaikytiems rezultatams.
* Įvykiais grindžiamo požiūrio taikymą dinamiškoms užduotims ir netikėtiems įvestims valdyti.

## Mokymosi tikslai

Pabaigę šią pamoką, suprasite:

* Kaip identifikuoti ir nustatyti bendrą tikslą AI agentui, kad jis aiškiai žinotų, ką reikia pasiekti.
* Kaip suskaidyti sudėtingą užduotį į valdomas pogrupes ir jas organizuoti į logišką seką.
* Kaip aprūpinti agentus tinkamais įrankiais (pvz., paieškos arba duomenų analizės įrankiais), nuspręsti kada ir kaip juos naudoti, bei kaip valdyti netikėtas situacijas.
* Kaip įvertinti pogrupių rezultatus, matuoti veiksmingumą ir iteruoti veiksmus galutiniam rezultatui pagerinti.

## Bendro tikslo apibrėžimas ir užduoties suskaidymas

![Defining Goals and Tasks](../../../translated_images/lt/defining-goals-tasks.d70439e19e37c47a.webp)

Dauguma realaus pasaulio užduočių yra pernelyg sudėtingos, kad jas būtų galima įvykdyti vienu žingsniu. AI agentui reikia glausto tikslo, kuris nukreiptų jo planavimą ir veiksmus. Pavyzdžiui, apgalvokite tikslą:

    „Sukurkite 3 dienų kelionės maršrutą.“

Nors tai paprasta išsakyti, reikia jį patikslinti. Kuo aiškesnis tikslas, tuo geriau agentas (ir jo bendradarbiai) gali susikoncentruoti į tinkamo rezultato pasiekimą, pvz., sukurti išsamų maršrutą su skrydžių pasirinkimais, viešbučių rekomendacijomis ir veiklų pasiūlymais.

### Užduoties suskaidymas

Didelės ar sudėtingos užduotys tampa valdomesnės, kai jos suskaidomos į mažesnes, tikslingas pogrupes.
Kelionės maršruto pavyzdyje tikslą galite suskaidyti į:

* Skrydžių užsakymas
* Viešbučių užsakymas
* Automobilio nuoma
* Asmeninimas

Kiekvieną pogrupį gali vykdyti specializuoti agentai arba procesai. Vienas agentas gali specializuotis paieškoje geriausių skrydžių pasiūlymų, kitas – viešbučių užsakymuose ir t. t. Koordinuojantis ar „žemesnio lygio“ agentas gali sujungti šiuos rezultatus į vientisą maršrutą galutiniam vartotojui.

Šis modulinis požiūris leidžia palaipsniui tobulinti sistemą. Pavyzdžiui, galite pridėti specializuotus agentus maisto rekomendacijoms ar vietinėms veikloms ir pamažu patobulinti maršrutą.

### Struktūruotas atsakymas

Dideli kalbos modeliai (LLM) gali generuoti struktūruotą atsakymą (pvz., JSON), kurį lengviau analizuoja ir apdoroja vėlesni agentai ar paslaugos. Tai ypač naudinga daugiagentėje aplinkoje, kur užduotys gali būti vykdomos gavus planavimo rezultatą.

Žemiau pateiktas Python kodo fragmentas demonstruoja, kaip paprastas planavimo agentas suskaido tikslą į pogrupes ir generuoja struktūruotą planą:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Kelionės použduoties modelis
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # norime priskirti užduotį agentui

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Apibrėžti naudotojo žinutę
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

### Planavimo agentas su daugiagentine orkestracija

Šiame pavyzdyje Semantinis maršrutizavimo agentas gauna naudotojo užklausą (pvz., „Man reikia viešbučio plano mano kelionei.“).

Planavimo agentas tada:

* Gautas viešbučio planas: gauna naudotojo pranešimą ir, remdamasis sistemos užklausa (kuriame pateikiama informacija apie galimus agentus), generuoja struktūruotą kelionės planą.
* Išnagrinėja agentus ir jų įrankius: agentų registras saugo agentų sąrašą (pvz., skrydžiams, viešbučiams, automobilių nuomai ir veikloms) kartu su jų teikiamomis funkcijomis ar įrankiais.
* Nukreipia planą atitinkamiems agentams: priklausomai nuo pogrupių skaičiaus, planuotojas pranešimą tiesiogiai siunčia specializuotam agentui (vienos užduoties scenarijai) arba koordinuoja per grupinio pokalbio valdytoją, jei veikia keli agentai.
* Apibendrina rezultatą: galiausiai, planuotojas pateikia suformuotą plano santrauką.
Toliau pateiktas Python kodo pavyzdys iliustruoja šiuos veiksmus:

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

# Kelionės posužduoties modelis

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # norime priskirti užduotį agentui

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Sukurti klientą

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Apibrėžti vartotojo žinutę

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

# Išvesti atsakymo turinį po jo užkėlimo kaip JSON

pprint(json.loads(response_content))
```

Toliau pateiktas rezultatas iš ankstesnio kodo, kurį galite naudoti perduoti struktūruotą atsakymą agentui `assigned_agent` ir santraukoti kelionės planą galutiniam naudotojui.

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

Pavyzdinį užrašų knygelės failą su aukščiau pateiktu kodo pavyzdžiu galite rasti [čia](07-python-agent-framework.ipynb).

### Iteratyvus planavimas

Kai kurios užduotys reikalauja derybų ar perplanavimo, kai vieno pogrupio rezultatas veikia kitą. Pavyzdžiui, jei agentas aptinka netikėtą duomenų formatą rezervuojant skrydžius, gali tekti keisti strategiją prieš pereinant prie viešbučių užsakymų.

Be to, naudotojo atsiliepimai (pvz., žmogus pasirenka ankstesnį skrydį) gali inicijuoti dalinį perplanavimą. Šis dinamiškas, iteratyvus požiūris užtikrina, kad galutinis sprendimas atitiktų realaus pasaulio ribojimus ir kintančius vartotojų pageidavimus.

pavyzdinis kodas

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. tas pats kaip ankstesniame kode ir perduoti vartotojo istoriją, dabartinį planą

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
# .. perdaryti planą ir siųsti užduotis atitinkamiems agentams
```

Išsamesniam planavimui peržiūrėkite Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Įrašą tinklaraštyje</a> apie sudėtingų užduočių sprendimą.

## Santrauka

Šiame straipsnyje apžvelgėme, kaip sukurti planuotoją, galintį dinamiškai pasirinkti apibrėžtus prieinamus agentus. Planuotojo išvestis suskaido užduotis ir paskiria agentus, kad jos būtų įvykdytos. Manoma, kad agentai turi prieigą prie funkcijų/įrankių, reikalingų užduočiai įvykdyti. Be agentų, galima naudoti kitus modelius, tokius kaip refleksija, santraukų kūrėjas ir rotacinis pokalbis, siekiant toliau pritaikyti sistemą.

## Papildomi ištekliai

Magentic One – universali daugiagentė sistema sudėtingoms užduotims spręsti, kuri pasiekė įspūdingus rezultatus įvairiuose sudėtinguose agentų vertinimuose. Nuoroda: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. Šioje įgyvendinimo versijoje orkestratorius kuria užduotims specifinius planus ir deleguoja užduotis prieinamiesiems agentams. Be planavimo, orkestratorius taip pat naudoja stebėjimo mechanizmą, kad sektų užduoties eigą ir prireikus pertvarkytų planus.

### Turite daugiau klausimų apie Planavimo modelį?

Prisijunkite prie [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), susitikite su kitais mokiniais, dalyvaukite konsultacijose ir gaukite atsakymus į savo AI agentų klausimus.

## Ankstesnė pamoka

[Patikimų AI agentų kūrimas](../06-building-trustworthy-agents/README.md)

## Kitoji pamoka

[Daugiagentės sistemos modelis](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už jokius nesusipratimus ar klaidingą aiškinimą, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->