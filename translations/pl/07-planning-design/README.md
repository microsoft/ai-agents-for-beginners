[![Planning Design Pattern](../../../translated_images/pl/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

# Projektowanie planu

## Wprowadzenie

Ta lekcja obejmie

* Definiowanie jasnego ogólnego celu i rozbijanie złożonego zadania na wykonalne podzadania.
* Wykorzystywanie ustrukturyzowanego wyjścia dla bardziej niezawodnych i maszynowo czytelnych odpowiedzi.
* Stosowanie podejścia opartego na zdarzeniach do obsługi dynamicznych zadań i nieoczekiwanych danych wejściowych.

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

* Zidentyfikować i ustalić ogólny cel dla agenta AI, zapewniając, że jasno wie, co należy osiągnąć.
* Rozłożyć złożone zadanie na wykonalne podzadania i uporządkować je w logiczną sekwencję.
* Wyposażyć agentów w odpowiednie narzędzia (np. narzędzia wyszukiwania lub analizy danych), zdecydować, kiedy i jak są używane, oraz radzić sobie z nieoczekiwanymi sytuacjami.
* Ocenić wyniki podzadań, zmierzyć wydajność i iterować działania w celu poprawy końcowego rezultatu.

## Definiowanie ogólnego celu i rozkład zadania

![Definiowanie celów i zadań](../../../translated_images/pl/defining-goals-tasks.d70439e19e37c47a.webp)

Większość zadań rzeczywistych jest zbyt złożona, aby rozwiązać je w jednym kroku. Agent AI potrzebuje zwięzłego celu, który poprowadzi jego planowanie i działania. Na przykład rozważ cel:

    "Wygenerować 3-dniowy plan podróży."

Chociaż jest to proste do określenia, wymaga doprecyzowania. Im jaśniejszy cel, tym lepiej agent (i ewentualni współpracujący ludzie) mogą się skupić na osiągnięciu właściwego wyniku, na przykład stworzeniu kompleksowego planu z opcjami lotów, rekomendacjami hoteli i sugestiami aktywności.

### Rozkład zadania

Duże lub złożone zadania stają się łatwiejsze do wykonania, gdy zostaną podzielone na mniejsze, ukierunkowane na cel podzadania.
Dla przykładu planu podróży, można rozłożyć cel na:

* Rezerwacja lotów
* Rezerwacja hoteli
* Wynajem samochodu
* Personalizacja

Każde podzadanie może być następnie realizowane przez dedykowanych agentów lub procesy. Jeden agent może specjalizować się w wyszukiwaniu najlepszych ofert lotów, inny skupia się na rezerwacjach hoteli i tak dalej. Koordynujący lub „dalszy” agent może następnie skompilować te wyniki w jeden spójny plan dla użytkownika końcowego.

To modułowe podejście pozwala także na stopniowe ulepszanie. Na przykład, można dodać specjalistycznych agentów do rekomendacji jedzenia lub sugestii lokalnych atrakcji i z czasem dopracować plan.

### Ustrukturyzowane wyjście

Modele językowe (LLMs) mogą generować ustrukturyzowane wyjście (np. JSON), które łatwiej jest analizować i przetwarzać dalszym agentom lub serwisom. Jest to szczególnie przydatne w kontekście wielu agentów, gdzie można działać na tych zadaniach po otrzymaniu wyniku planowania.

Poniższy fragment Pythona demonstruje prostego agenta planującego, rozkładającego cel na podzadania i generującego ustrukturyzowany plan:

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

# Model Podzadania Podróży
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # chcemy przypisać zadanie do agenta

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Zdefiniuj wiadomość użytkownika
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

### Agent planujący z orkiestracją wielu agentów

W tym przykładzie agent Semantic Router otrzymuje żądanie użytkownika (np. „Potrzebuję planu hotelowego na moją podróż.”).

Planista następnie:

* Otrzymuje plan hotelowy: planista bierze wiadomość od użytkownika i na podstawie wskazówki systemowej (w tym dostępne informacje o agentach) generuje ustrukturyzowany plan podróży.
* Wymienia agentów i ich narzędzia: rejestr agentów zawiera listę agentów (np. do lotów, hoteli, wynajmu samochodów i aktywności) wraz z funkcjami lub narzędziami, które oferują.
* Kieruje plan do odpowiednich agentów: w zależności od liczby podzadań planista albo wysyła wiadomość bezpośrednio do dedykowanego agenta (dla scenariuszy pojedynczych zadań), albo koordynuje przez menedżera czatu grupowego dla współpracy wielu agentów.
* Podsumowuje wynik: ostatecznie planista podsumowuje wygenerowany plan dla przejrzystości.
Następujący przykładowy kod Pythona ilustruje te kroki:

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

# Model podrzędnego zadania podróży

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # chcemy przypisać zadanie agentowi

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Utwórz klienta

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# Zdefiniuj wiadomość użytkownika

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

# Wydrukuj zawartość odpowiedzi po załadowaniu jej jako JSON

pprint(json.loads(response_content))
```

To, co następuje, to wyjście z powyższego kodu, które możesz następnie wykorzystać do kierowania do `assigned_agent` i podsumowania planu podróży dla użytkownika końcowego.

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

Przykładowy notebook z powyższym kodem jest dostępny [tutaj](./code_samples/07-python-agent-framework.ipynb).

### Planowanie iteracyjne

Niektóre zadania wymagają wymiany informacji lub ponownego planowania, gdzie wynik jednego podzadania wpływa na kolejne. Na przykład, jeśli agent odkryje nieoczekiwany format danych podczas rezerwacji lotów, może potrzebować dostosować strategię zanim przejdzie do rezerwacji hoteli.

Dodatkowo, opinie użytkownika (np. gdy osoba decyduje, że woli wcześniejszy lot) mogą wywołać częściowe przeplanowanie. To dynamiczne, iteracyjne podejście zapewnia, że ostateczne rozwiązanie jest zgodne z rzeczywistymi ograniczeniami i zmieniającymi się preferencjami użytkownika.

np. przykładowy kod

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. tak jak w poprzednim kodzie i przekazuj historię użytkownika, aktualny plan

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
# .. przeplanuj i wyślij zadania do odpowiednich agentów
```

Aby uzyskać bardziej kompleksowe planowanie, zapoznaj się z Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> do rozwiązywania złożonych zadań.

## Podsumowanie

W tym artykule przyjrzeliśmy się przykładzie, jak można stworzyć planistę, który może dynamicznie wybierać dostępnych zdefiniowanych agentów. Wynik planisty rozkłada zadania i przypisuje agentów, aby mogli je wykonać. Zakłada się, że agenci mają dostęp do funkcji/narzędzi wymaganych do realizacji zadania. Oprócz agentów można uwzględnić inne wzorce, takie jak refleksja, podsumowujący i rozmowa w trybie round robin, aby jeszcze bardziej dostosować.

## Dodatkowe zasoby

Magnetic One - generalistyczny system multi-agentowy do rozwiązywania złożonych zadań, który osiągnął imponujące wyniki w wielu wymagających benchmarkach agentów. Referencja: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. W tej implementacji orkiestrator tworzy specyficzne plany dla zadań i deleguje je dostępnych agentom. Oprócz planowania orkiestrator stosuje także mechanizm śledzenia postępu zadania i ponownego planowania w razie potrzeby.

### Masz więcej pytań na temat wzorca projektowego planowania?

Dołącz do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby spotkać innych uczących się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów AI.

## Poprzednia lekcja

[Budowanie godnych zaufania agentów AI](../06-building-trustworthy-agents/README.md)

## Następna lekcja

[Wzorzec projektowy wielu agentów](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->