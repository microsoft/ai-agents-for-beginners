[![Wzorzec planowania](../../../translated_images/pl/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Kliknij obraz powyżej, aby obejrzeć wideo z tej lekcji)_

# Wzorzec planowania

## Wprowadzenie

Ta lekcja obejmie

* Określenie jasnego celu ogólnego i rozbicie złożonego zadania na zadania możliwe do wykonania.
* Wykorzystanie ustrukturyzowanego wyjścia dla bardziej niezawodnych i maszynowo czytelnych odpowiedzi.
* Zastosowanie podejścia sterowanego zdarzeniami do obsługi dynamicznych zadań i nieoczekiwanych danych wejściowych.

## Cele nauczania

Po ukończeniu tej lekcji zrozumiesz:

* Zidentyfikować i ustawić ogólny cel dla agenta AI, upewniając się, że dokładnie wie, co trzeba osiągnąć.
* Rozłożyć złożone zadanie na wykonalne podzadania i uporządkować je w logiczną sekwencję.
* Wyposażyć agentów w odpowiednie narzędzia (np. narzędzia do wyszukiwania lub analizy danych), zdecydować kiedy i jak są używane oraz radzić sobie z nieoczekiwanymi sytuacjami, które się pojawią.
* Ocenić wyniki podzadań, mierzyć wydajność i iterować działania w celu poprawy końcowego rezultatu.

## Określanie ogólnego celu i rozbijanie zadania

![Określanie celów i zadań](../../../translated_images/pl/defining-goals-tasks.d70439e19e37c47a.webp)

Większość zadań w rzeczywistym świecie jest zbyt złożona, by rozwiązać ją w jednym kroku. Agent AI potrzebuje zwięzłego celu, aby kierować swoim planowaniem i działaniami. Na przykład rozważ cel:

    "Wygeneruj 3-dniowy plan podróży."

Chociaż łatwo to sformułować, wciąż wymaga dopracowania. Im jaśniejszy cel, tym lepiej agent (i ewentualni ludzcy współpracownicy) mogą skupić się na osiągnięciu właściwego wyniku, takiego jak stworzenie kompleksowego planu z opcjami lotów, rekomendacjami hoteli i propozycjami aktywności.

### Dekompozycja zadania

Duże lub złożone zadania stają się łatwiejsze do zarządzania, gdy są podzielone na mniejsze, ukierunkowane na cel podzadania.
Dla przykładu planu podróży można rozłożyć cel na:

* Rezerwacja lotu
* Rezerwacja hotelu
* Wynajem samochodu
* Personalizacja

Każde podzadanie można następnie powierzyć wyspecjalizowanym agentom lub procesom. Jeden agent może specjalizować się w wyszukiwaniu najlepszych ofert lotów, inny skupi się na rezerwacjach hoteli itd. Koordynujący lub „downstream” agent może potem skompilować te wyniki w spójny plan podróży dla użytkownika końcowego.

Takie modułowe podejście umożliwia także stopniowe udoskonalenia. Na przykład można dodać wyspecjalizowane agenty do rekomendacji kulinarnych lub sugestii lokalnych atrakcji i z czasem udoskonalać plan podróży.

### Ustrukturyzowane wyjście

Duże modele językowe (LLMs) mogą generować ustrukturyzowane wyjście (np. JSON), które jest łatwiejsze do parsowania i przetwarzania przez downstreamowe agenty lub usługi. Jest to szczególnie przydatne w kontekście wieloagentowym, gdzie można wykonać te zadania po otrzymaniu wyniku planowania.

Poniższy fragment Pythona demonstruje prostego agenta planującego, rozkładającego cel na podzadania i generującego ustrukturyzowany plan:

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

# Model podzadania podróży
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # chcemy przypisać zadanie agentowi

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

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

W tym przykładzie Agent Router Semantyczny otrzymuje żądanie użytkownika (np. "Potrzebuję planu hotelowego na moją podróż.").

Planner następnie:

* Otrzymuje plan hotelowy: Planner przyjmuje wiadomość użytkownika i, w oparciu o prompt systemowy (w tym informacje o dostępnych agentach), generuje ustrukturyzowany plan podróży.
* Wymienia agentów i ich narzędzia: Rejestr agentów zawiera listę agentów (np. dla lotów, hoteli, wynajmu samochodów i aktywności) wraz z funkcjami lub narzędziami, które oferują.
* Kieruje plan do odpowiednich agentów: W zależności od liczby podzadań planner albo wysyła wiadomość bezpośrednio do dedykowanego agenta (w scenariuszach jednozadaniowych), albo koordynuje za pomocą menedżera czatu grupowego w przypadku współpracy wielu agentów.
* Podsumowuje wynik: Wreszcie planner podsumowuje wygenerowany plan dla przejrzystości.
Poniższy przykładowy kod Pythona ilustruje te kroki:

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

# Model podzadania podróży

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

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Utwórz klienta

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

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

# Wyświetl zawartość odpowiedzi po załadowaniu jej jako JSON

pprint(json.loads(response_content))
```

Poniżej znajduje się wyjście z poprzedniego kodu i możesz następnie użyć tego ustrukturyzowanego wyjścia, aby skierować je do `assigned_agent` i podsumować plan podróży dla użytkownika końcowego.

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

Przykładowy notatnik z powyższym przykładem kodu jest dostępny [tutaj](07-python-agent-framework.ipynb).

### Iteracyjne planowanie

Niektóre zadania wymagają wymiany informacji lub ponownego planowania, gdzie wynik jednego podzadania wpływa na kolejne. Na przykład, jeśli agent odkryje nieoczekiwany format danych podczas rezerwacji lotów, może być konieczne dostosowanie strategii przed przejściem do rezerwacji hoteli.

Dodatkowo opinia użytkownika (np. człowieka decydującego, że woli wcześniejszy lot) może wywołać częściowe ponowne planowanie. Takie dynamiczne, iteracyjne podejście zapewnia, że końcowe rozwiązanie jest zgodne z rzeczywistymi ograniczeniami i zmieniającymi się preferencjami użytkownika.

np. przykładowy kod

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. tak samo jak w poprzednim kodzie i przekaż historię użytkownika oraz aktualny plan

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
# .. zaplanuj ponownie i wyślij zadania do odpowiednich agentów
```

Dla bardziej kompleksowego planowania sprawdź Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Wpis na blogu</a> dotyczący rozwiązywania złożonych zadań.

## Podsumowanie

W tym artykule przyjrzeliśmy się przykładowi, jak można stworzyć planner, który dynamicznie wybiera dostępnych zdefiniowanych agentów. Wyjście z Plannera dekomponuje zadania i przydziela agentów, aby można je było wykonać. Zakłada się, że agenty mają dostęp do funkcji/narzędzi niezbędnych do wykonania zadania. Oprócz agentów można dodać inne wzorce, takie jak refleksja, narzędzie podsumowujące i czat rotacyjny, aby dodatkowo dostosować działanie.

## Dodatkowe zasoby

Magentic One - generalistyczny system wieloagentowy do rozwiązywania złożonych zadań, który osiągnął imponujące wyniki w wielu wymagających benchmarkach agentowych. Odniesienie: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. W tej implementacji orkiestrator tworzy plany specyficzne dla zadań i deleguje te zadania do dostępnych agentów. Oprócz planowania orkiestrator stosuje również mechanizm śledzenia postępu zadania i ponownego planowania w razie potrzeby.

### Masz więcej pytań dotyczących wzorca projektowego planowania?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać się z innymi uczącymi się, uczestniczyć w konsultacjach i uzyskać odpowiedzi na swoje pytania dotyczące agentów AI.

## Poprzednia lekcja

[Tworzenie godnych zaufania agentów AI](../06-building-trustworthy-agents/README.md)

## Następna lekcja

[Wzorzec wieloagentowy](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Zastrzeżenie:
Ten dokument został przetłumaczony z użyciem usługi tłumaczeń opartych na sztucznej inteligencji [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najdokładniejsze, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy uznać za źródło autorytatywne. W przypadku informacji o znaczeniu krytycznym zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za żadne nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->