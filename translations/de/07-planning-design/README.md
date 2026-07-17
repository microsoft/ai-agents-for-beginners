[![Planungs-Designmuster](../../../translated_images/de/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

# Planungs-Design

## Einführung

Diese Lektion behandelt

* Das Definieren eines klaren Gesamtziels und das Zerlegen einer komplexen Aufgabe in handhabbare Teilaufgaben.
* Die Nutzung strukturierter Ausgaben für zuverlässigeren und maschinenlesbaren Antworten.
* Die Anwendung eines ereignisgesteuerten Ansatzes zur Behandlung dynamischer Aufgaben und unerwarteter Eingaben.

## Lernziele

Nach Abschluss dieser Lektion werden Sie folgendes verstehen:

* Ein Gesamtziel für einen KI-Agenten identifizieren und festlegen, sodass dieser klar weiß, was erreicht werden muss.
* Eine komplexe Aufgabe in handhabbare Teilaufgaben zerlegen und diese in eine logische Reihenfolge bringen.
* Agenten mit den richtigen Werkzeugen ausstatten (z. B. Suchwerkzeuge oder Datenanalysetools), entscheiden, wann und wie sie eingesetzt werden, und unerwartete Situationen bewältigen.
* Ergebnisse der Teilaufgaben bewerten, die Leistung messen und Aktionen iterativ verbessern, um das Endergebnis zu optimieren.

## Das Gesamtziel definieren und eine Aufgabe aufgliedern

![Ziele und Aufgaben definieren](../../../translated_images/de/defining-goals-tasks.d70439e19e37c47a.webp)

Die meisten Aufgaben in der realen Welt sind zu komplex, um sie in einem einzigen Schritt zu bewältigen. Ein KI-Agent benötigt ein prägnantes Ziel, das seine Planung und Aktionen steuert. Zum Beispiel betrachten wir das Ziel:

    "Erstelle eine 3-tägige Reiseroute."

Obwohl es einfach formuliert ist, bedarf es dennoch einer Verfeinerung. Je klarer das Ziel, desto besser können der Agent (und menschliche Mitarbeiter) sich darauf konzentrieren, das richtige Ergebnis zu erzielen, etwa eine umfassende Reiseroute mit Flugoptionen, Hotelempfehlungen und Aktivitätsvorschlägen zu erstellen.

### Aufgabenzerlegung

Große oder komplexe Aufgaben werden handhabbarer, wenn sie in kleinere, zielorientierte Teilaufgaben unterteilt werden.
Für das Beispiel der Reiseroute könnten Sie das Ziel folgendermaßen aufgliedern:

* Flugbuchung
* Hotelbuchung
* Mietwagen
* Personalisierung

Jede Teilaufgabe kann dann von spezialisierten Agenten oder Prozessen bearbeitet werden. Ein Agent könnte sich auf die Suche nach den besten Flugangeboten spezialisieren, ein anderer auf Hotelbuchungen usw. Ein koordinierender oder „nachgelagerter“ Agent kann diese Ergebnisse dann zu einer zusammenhängenden Reiseroute für den Endnutzer zusammenfassen.

Dieser modulare Ansatz erlaubt auch schrittweise Verbesserungen. Beispielsweise könnten Sie spezialisierte Agenten für Restaurantempfehlungen oder lokale Aktivitätsvorschläge hinzufügen und die Reiseroute im Laufe der Zeit verfeinern.

### Strukturierte Ausgabe

Große Sprachmodelle (LLMs) können strukturierte Ausgaben (z. B. JSON) erzeugen, die für nachgelagerte Agenten oder Dienste leichter zu parsen und zu verarbeiten sind. Dies ist besonders nützlich in einem Multi-Agenten-Kontext, in dem wir Aufgaben nach dem Empfang des Planungsoutputs ausführen können.

Der folgende Python-Ausschnitt zeigt einen einfachen Planungsagenten, der ein Ziel in Teilaufgaben zerlegt und einen strukturierten Plan erzeugt:

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

# Reise-Unteraufgabenmodell
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # Wir wollen die Aufgabe dem Agenten zuweisen

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Definiere die Benutzernachricht
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

### Planungsagent mit Multi-Agent-Orchestrierung

In diesem Beispiel erhält ein Semantic Router Agent eine Nutzeranfrage (z. B. „Ich brauche einen Hotelplan für meine Reise.“).

Der Planer macht dann Folgendes:

* Erhält den Hotelplan: Der Planer nimmt die Nachricht des Nutzers und generiert basierend auf einem Systemprompt (einschließlich verfügbarer Agenteninformationen) einen strukturierten Reiseplan.
* Listet Agenten und ihre Werkzeuge auf: Das Agentenregister enthält eine Liste von Agenten (z. B. für Flug, Hotel, Mietwagen und Aktivitäten) sowie die Funktionen oder Werkzeuge, die sie anbieten.
* Leitet den Plan an die jeweiligen Agenten weiter: Abhängig von der Anzahl der Teilaufgaben sendet der Planer die Nachricht entweder direkt an einen dedizierten Agenten (bei Ein-Aufgaben-Szenarien) oder koordiniert über einen Gruppenchat-Manager für die Zusammenarbeit mehrerer Agenten.
* Fasst das Ergebnis zusammen: Schließlich fasst der Planer den generierten Plan zur besseren Übersicht zusammen.
Der folgende Python-Code illustriert diese Schritte:

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

# Reise-Unteraufgabenmodell

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # Wir wollen die Aufgabe dem Agenten zuweisen

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Erstellen Sie den Client

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# Definieren Sie die Benutzernachricht

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

# Drucken Sie den Antwortinhalt nach dem Laden als JSON aus

pprint(json.loads(response_content))
```

Im Folgenden sehen Sie die Ausgabe des vorherigen Codes und können diese strukturierte Ausgabe nutzen, um sie an `assigned_agent` weiterzuleiten und den Reiseplan dem Endnutzer zusammenzufassen.

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

Ein Beispiel-Notebook mit dem vorherigen Codebeispiel ist [hier](./code_samples/07-python-agent-framework.ipynb) verfügbar.

### Iterative Planung

Manche Aufgaben erfordern ein Hin- und Her oder eine Neuplanung, bei der das Ergebnis einer Teilaufgabe die nächste beeinflusst. Zum Beispiel, wenn der Agent beim Buchen von Flügen ein unerwartetes Datenformat entdeckt, muss er möglicherweise die Strategie anpassen, bevor er mit Hotelbuchungen fortfährt.

Zusätzlich kann Nutzerfeedback (z. B. ein Mensch entscheidet sich für einen früheren Flug) eine Teil-Neuplanung auslösen. Dieser dynamische, iterative Ansatz stellt sicher, dass die endgültige Lösung mit realen Einschränkungen und sich entwickelnden Nutzerpräferenzen übereinstimmt.

z. B. Beispielcode

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. gleich wie im vorherigen Code und Übergabe der Benutzerhistorie, aktueller Plan

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
# .. neu planen und die Aufgaben an die jeweiligen Agenten senden
```

Für umfassendere Planung schauen Sie sich den Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> für die Lösung komplexer Aufgaben an.

## Zusammenfassung

In diesem Artikel haben wir uns ein Beispiel angesehen, wie wir einen Planer erstellen können, der die definierten verfügbaren Agenten dynamisch auswählt. Der Output des Planers zerlegt die Aufgaben und weist die Agenten zu, damit diese ausgeführt werden können. Es wird vorausgesetzt, dass die Agenten Zugriff auf die Funktionen/Werkzeuge haben, die zur Durchführung der Aufgaben erforderlich sind. Zusätzlich zu den Agenten können Sie weitere Muster wie Reflexion, Zusammenfassung und Round-Robin-Chat einbauen, um die Anpassung weiter zu verbessern.

## Zusätzliche Ressourcen

Magentic One - Ein Generalist-Multi-Agent-System zur Lösung komplexer Aufgaben, das beeindruckende Ergebnisse bei mehreren anspruchsvollen agentischen Benchmarks erzielt hat. Referenz: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. In dieser Implementierung erstellt der Orchestrator aufgabenspezifische Pläne und delegiert diese Aufgaben an die verfügbaren Agenten. Neben der Planung verwendet der Orchestrator auch einen Tracking-Mechanismus, um den Fortschritt der Aufgabe zu überwachen und bei Bedarf neu zu planen.

### Haben Sie weitere Fragen zum Planungs-Designmuster?

Treten Sie dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten beantwortet zu bekommen.

## Vorherige Lektion

[Vertrauenswürdige KI-Agenten bauen](../06-building-trustworthy-agents/README.md)

## Nächste Lektion

[Multi-Agent-Designmuster](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->