[![Planungs-Entwurfsmuster](../../../translated_images/de/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

# Planungs-Entwurf

## Einführung

Diese Lektion behandelt

* Die Definition eines klaren Gesamtziels und die Aufteilung einer komplexen Aufgabe in überschaubare Aufgaben.
* Die Nutzung strukturierter Ausgaben für zuverlässigere und maschinenlesbare Antworten.
* Die Anwendung eines ereignisgesteuerten Ansatzes zur Handhabung dynamischer Aufgaben und unerwarteter Eingaben.

## Lernziele

Nach Abschluss dieser Lektion werden Sie ein Verständnis darüber haben:

* Ein Gesamtziel für einen KI-Agenten zu identifizieren und festzulegen, damit dieser genau weiß, was erreicht werden soll.
* Eine komplexe Aufgabe in überschaubare Teilaufgaben zu zerlegen und diese in eine logische Reihenfolge zu bringen.
* Agenten mit den richtigen Werkzeugen (z. B. Suchwerkzeuge oder Datenanalysetools) auszustatten, zu entscheiden wann und wie diese eingesetzt werden, und unerwartete Situationen zu bewältigen.
* Teilergebnisse auszuwerten, die Leistung zu messen und Maßnahmen zu iterieren, um das Endergebnis zu verbessern.

## Definition des Gesamtziels und Aufteilung einer Aufgabe

![Ziele und Aufgaben definieren](../../../translated_images/de/defining-goals-tasks.d70439e19e37c47a.webp)

Die meisten Aufgaben im wirklichen Leben sind zu komplex, um sie in einem Schritt zu bewältigen. Ein KI-Agent braucht ein prägnantes Ziel, um seine Planung und Aktionen zu steuern. Betrachten wir zum Beispiel das Ziel:

    "Erstellen Sie eine 3-tägige Reiseroute."

Obwohl es einfach formuliert ist, bedarf es noch einer Verfeinerung. Je klarer das Ziel ist, desto besser können der Agent (und alle menschlichen Mitwirkenden) sich darauf konzentrieren, das gewünschte Ergebnis zu erreichen, wie z. B. eine umfassende Reiseroute mit Flugoptionen, Hotelempfehlungen und Aktivitätstipps zu erstellen.

### Aufgabenzerlegung

Große oder komplexe Aufgaben werden überschaubarer, wenn man sie in kleinere, zielorientierte Teilaufgaben aufteilt.
Für das Beispiel der Reiseroute könnten Sie das Ziel wie folgt zerlegen:

* Flugbuchung
* Hotelbuchung
* Mietwagen
* Personalisierung

Jede Teilaufgabe kann dann von spezialisierten Agenten oder Prozessen bearbeitet werden. Ein Agent könnte sich auf die Suche nach den besten Flugangeboten spezialisieren, ein anderer auf Hotelbuchungen usw. Ein koordinierender oder "nachgelagerter" Agent kann dann diese Ergebnisse zu einer zusammenhängenden Reiseroute für den Endnutzer zusammenführen.

Dieser modulare Ansatz ermöglicht auch inkrementelle Verbesserungen. Zum Beispiel könnten Sie spezialisierte Agenten für Essensempfehlungen oder lokale Aktivitätsvorschläge hinzufügen und die Reiseroute im Laufe der Zeit verfeinern.

### Strukturierte Ausgabe

Große Sprachmodelle (LLMs) können strukturierte Ausgaben (z. B. JSON) erzeugen, die für nachgelagerte Agenten oder Dienste leichter zu parsen und zu verarbeiten sind. Dies ist besonders nützlich in einem Multi-Agenten-Kontext, in dem wir Aufgaben nach Erhalt der Planungs-Ausgabe ausführen können.

Der folgende Python-Schnipsel zeigt einen einfachen Planungsagenten, der ein Ziel in Teilaufgaben zerlegt und einen strukturierten Plan erstellt:

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

# Reise-Unteraufgabenmodell
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # wir möchten die Aufgabe dem Agenten zuweisen

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

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

### Planungsagent mit Multi-Agenten-Orchestrierung

In diesem Beispiel erhält ein Semantic Router Agent eine Benutzeranfrage (z. B. „Ich brauche einen Hotelplan für meine Reise.“).

Der Planer führt dann aus:

* Empfang des Hotelplans: Der Planer nimmt die Nachricht des Benutzers und erstellt basierend auf einem System-Prompt (einschließlich verfügbarer Agenten-Details) einen strukturierten Reiseplan.
* Auflisten der Agenten und deren Werkzeuge: Das Agenten-Register hält eine Liste von Agenten (z. B. für Flug, Hotel, Mietwagen und Aktivitäten) sowie deren Funktionen oder Werkzeuge bereit.
* Weiterleitung des Plans an die jeweiligen Agenten: Abhängig von der Anzahl der Teilaufgaben sendet der Planer entweder die Nachricht direkt an einen spezialisierten Agenten (bei einzelnen Aufgaben) oder koordiniert über einen Gruppenchat-Manager für die Zusammenarbeit mehrerer Agenten.
* Zusammenfassung des Ergebnisses: Abschließend fasst der Planer den erstellten Plan zur besseren Verständlichkeit zusammen.
Der folgende Python-Code demonstriert diese Schritte:

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
    assigned_agent: AgentEnum # Wir möchten die Aufgabe dem Agenten zuweisen

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Erstelle den Client

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Definiere die Benutzer-Nachricht

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

# Gib den Antwortinhalt aus, nachdem er als JSON geladen wurde

pprint(json.loads(response_content))
```

Im Folgenden sehen Sie die Ausgabe des vorherigen Codes, und Sie können diese strukturierte Ausgabe dann verwenden, um an `assigned_agent` weiterzuleiten und die Reiseroute für den Endnutzer zusammenzufassen.

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

Ein Beispiel-Notebook mit dem vorherigen Code-Beispiel ist [hier](07-python-agent-framework.ipynb) verfügbar.

### Iterative Planung

Manche Aufgaben erfordern ein Hin- und Her oder Umplanen, bei dem das Ergebnis einer Teilaufgabe die nächste beeinflusst. Zum Beispiel, wenn der Agent während der Flugbuchung ein unerwartetes Datenformat entdeckt, muss er möglicherweise seine Strategie anpassen, bevor er mit der Hotelbuchung fortfährt.

Zusätzlich kann Benutzerfeedback (z. B. wenn ein Mensch entscheidet, dass er einen früheren Flug bevorzugt) eine Teil-Neuplanung auslösen. Dieser dynamische, iterative Ansatz stellt sicher, dass die endgültige Lösung mit realen Einschränkungen und sich entwickelnden Nutzerpräferenzen übereinstimmt.

z.B. Beispielcode

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. dasselbe wie beim vorherigen Code und Übergabe der Benutzerhistorie, des aktuellen Plans

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
# .. Neuplanung und Senden der Aufgaben an die jeweiligen Agenten
```

Für umfassendere Planungen schauen Sie sich Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> zum Lösen komplexer Aufgaben an.

## Zusammenfassung

In diesem Artikel haben wir ein Beispiel betrachtet, wie wir einen Planer erstellen können, der dynamisch verfügbare Agenten auswählt. Die Ausgabe des Planers zerlegt die Aufgaben und weist die Agenten zu, sodass sie ausgeführt werden können. Es wird davon ausgegangen, dass die Agenten Zugang zu den Funktionen/Werkzeugen haben, die zur Ausführung der Aufgabe erforderlich sind. Zusätzlich zu den Agenten können Sie weitere Muster wie Reflexion, Zusammenfassung und Rundlauf-Chat einbinden, um die Lösung weiter anzupassen.

## Weitere Ressourcen

Magentic One – Ein Generalist-Multi-Agenten-System zur Lösung komplexer Aufgaben, das beeindruckende Ergebnisse bei mehreren herausfordernden agentischen Benchmarks erzielt hat. Referenz: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. In dieser Implementierung erstellt der Orchestrator aufgabenspezifische Pläne und delegiert diese an verfügbare Agenten. Zusätzlich zur Planung nutzt der Orchestrator auch einen Tracking-Mechanismus, um den Fortschritt der Aufgabe zu überwachen und bei Bedarf neu zu planen.

### Haben Sie weitere Fragen zum Planungs-Entwurfsmuster?

Treten Sie dem [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten beantwortet zu bekommen.

## Vorherige Lektion

[Vertrauenswürdige KI-Agenten erstellen](../06-building-trustworthy-agents/README.md)

## Nächste Lektion

[Multi-Agenten-Entwurfsmuster](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->