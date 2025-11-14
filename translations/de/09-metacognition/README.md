<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-30T13:20:21+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "de"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.de.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_
# Metakognition in KI-Agenten

## Einführung

Willkommen zur Lektion über Metakognition in KI-Agenten! Dieses Kapitel richtet sich an Anfänger, die neugierig darauf sind, wie KI-Agenten über ihre eigenen Denkprozesse nachdenken können. Am Ende dieser Lektion werden Sie die wichtigsten Konzepte verstehen und praktische Beispiele haben, um Metakognition im Design von KI-Agenten anzuwenden.

## Lernziele

Nach Abschluss dieser Lektion werden Sie in der Lage sein:

1. Die Auswirkungen von Denk-Schleifen in Agentendefinitionen zu verstehen.
2. Planungs- und Bewertungstechniken anzuwenden, um selbstkorrigierende Agenten zu unterstützen.
3. Eigene Agenten zu erstellen, die in der Lage sind, Code zu manipulieren, um Aufgaben zu erfüllen.

## Einführung in Metakognition

Metakognition bezieht sich auf die höheren kognitiven Prozesse, die das Nachdenken über das eigene Denken umfassen. Für KI-Agenten bedeutet dies, dass sie in der Lage sind, ihre Handlungen basierend auf Selbstbewusstsein und vergangenen Erfahrungen zu bewerten und anzupassen. Metakognition, oder "über das Denken nachdenken", ist ein wichtiges Konzept bei der Entwicklung agentenbasierter KI-Systeme. Es beinhaltet, dass KI-Systeme sich ihrer eigenen internen Prozesse bewusst sind und in der Lage sind, ihr Verhalten zu überwachen, zu regulieren und anzupassen. Ähnlich wie wir, wenn wir die Stimmung in einem Raum einschätzen oder ein Problem analysieren. Dieses Selbstbewusstsein kann KI-Systemen helfen, bessere Entscheidungen zu treffen, Fehler zu erkennen und ihre Leistung im Laufe der Zeit zu verbessern – was wiederum auf den Turing-Test und die Debatte zurückführt, ob KI die Kontrolle übernehmen wird.

Im Kontext agentenbasierter KI-Systeme kann Metakognition helfen, mehrere Herausforderungen zu bewältigen, wie z. B.:
- Transparenz: Sicherstellen, dass KI-Systeme ihre Überlegungen und Entscheidungen erklären können.
- Schlussfolgerung: Die Fähigkeit von KI-Systemen verbessern, Informationen zu synthetisieren und fundierte Entscheidungen zu treffen.
- Anpassung: KI-Systemen ermöglichen, sich an neue Umgebungen und sich ändernde Bedingungen anzupassen.
- Wahrnehmung: Die Genauigkeit von KI-Systemen bei der Erkennung und Interpretation von Umgebungsdaten verbessern.

### Was ist Metakognition?

Metakognition, oder "über das Denken nachdenken", ist ein höherer kognitiver Prozess, der Selbstbewusstsein und Selbstregulierung der eigenen kognitiven Prozesse umfasst. Im Bereich der KI befähigt Metakognition Agenten, ihre Strategien und Handlungen zu bewerten und anzupassen, was zu verbesserten Problemlösungs- und Entscheidungsfähigkeiten führt. Durch das Verständnis von Metakognition können Sie KI-Agenten entwerfen, die nicht nur intelligenter, sondern auch anpassungsfähiger und effizienter sind. Bei echter Metakognition würde die KI explizit über ihre eigenen Überlegungen nachdenken.

Beispiel: „Ich habe günstigere Flüge priorisiert, weil… Ich könnte Direktflüge übersehen haben, also überprüfe ich das noch einmal.“
Nachverfolgen, wie oder warum eine bestimmte Route gewählt wurde.
- Feststellen, dass Fehler gemacht wurden, weil zu stark auf frühere Nutzerpräferenzen vertraut wurde, und daher nicht nur die endgültige Empfehlung, sondern die gesamte Entscheidungsstrategie anpassen.
- Muster diagnostizieren wie: „Immer wenn der Nutzer ‚zu überfüllt‘ erwähnt, sollte ich nicht nur bestimmte Attraktionen ausschließen, sondern auch erkennen, dass meine Methode, ‚Top-Attraktionen‘ nach Beliebtheit zu bewerten, fehlerhaft ist.“

### Bedeutung der Metakognition in KI-Agenten

Metakognition spielt aus mehreren Gründen eine entscheidende Rolle im Design von KI-Agenten:

![Bedeutung der Metakognition](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.de.png)

- Selbstreflexion: Agenten können ihre eigene Leistung bewerten und Verbesserungsmöglichkeiten identifizieren.
- Anpassungsfähigkeit: Agenten können ihre Strategien basierend auf vergangenen Erfahrungen und sich ändernden Umgebungen anpassen.
- Fehlerkorrektur: Agenten können Fehler eigenständig erkennen und korrigieren, was zu genaueren Ergebnissen führt.
- Ressourcenmanagement: Agenten können den Einsatz von Ressourcen wie Zeit und Rechenleistung durch Planung und Bewertung optimieren.

## Komponenten eines KI-Agenten

Bevor wir uns mit metakognitiven Prozessen befassen, ist es wichtig, die grundlegenden Komponenten eines KI-Agenten zu verstehen. Ein KI-Agent besteht typischerweise aus:

- Persona: Die Persönlichkeit und Eigenschaften des Agenten, die definieren, wie er mit Nutzern interagiert.
- Tools: Die Fähigkeiten und Funktionen, die der Agent ausführen kann.
- Skills: Das Wissen und die Expertise, die der Agent besitzt.

Diese Komponenten arbeiten zusammen, um eine "Expertise-Einheit" zu schaffen, die spezifische Aufgaben ausführen kann.

**Beispiel**:
Betrachten Sie einen Reiseagenten, der nicht nur Ihren Urlaub plant, sondern auch seinen Ansatz basierend auf Echtzeitdaten und Erfahrungen aus früheren Kundenreisen anpasst.

### Beispiel: Metakognition in einem Reiseagenten-Service

Stellen Sie sich vor, Sie entwerfen einen Reiseagenten-Service, der von KI unterstützt wird. Dieser Agent, "Reiseagent", hilft Nutzern bei der Planung ihrer Urlaube. Um Metakognition zu integrieren, muss der Reiseagent seine Handlungen basierend auf Selbstbewusstsein und vergangenen Erfahrungen bewerten und anpassen. So könnte Metakognition eine Rolle spielen:

#### Aktuelle Aufgabe

Die aktuelle Aufgabe besteht darin, einem Nutzer bei der Planung einer Reise nach Paris zu helfen.

#### Schritte zur Erledigung der Aufgabe

1. **Nutzerpräferenzen sammeln**: Den Nutzer nach seinen Reisedaten, Budget, Interessen (z. B. Museen, Küche, Shopping) und spezifischen Anforderungen fragen.
2. **Informationen abrufen**: Nach Flugoptionen, Unterkünften, Attraktionen und Restaurants suchen, die den Präferenzen des Nutzers entsprechen.
3. **Empfehlungen generieren**: Einen personalisierten Reiseplan mit Flugdaten, Hotelreservierungen und vorgeschlagenen Aktivitäten bereitstellen.
4. **Anpassen basierend auf Feedback**: Den Nutzer nach Feedback zu den Empfehlungen fragen und notwendige Anpassungen vornehmen.

#### Benötigte Ressourcen

- Zugriff auf Flug- und Hotelbuchungsdatenbanken.
- Informationen über Pariser Attraktionen und Restaurants.
- Nutzerdaten aus früheren Interaktionen.

#### Erfahrung und Selbstreflexion

Der Reiseagent nutzt Metakognition, um seine Leistung zu bewerten und aus vergangenen Erfahrungen zu lernen. Zum Beispiel:

1. **Analyse des Nutzerfeedbacks**: Der Reiseagent überprüft das Feedback der Nutzer, um festzustellen, welche Empfehlungen gut ankamen und welche nicht. Er passt seine zukünftigen Vorschläge entsprechend an.
2. **Anpassungsfähigkeit**: Wenn ein Nutzer zuvor eine Abneigung gegen überfüllte Orte geäußert hat, wird der Reiseagent in Zukunft vermeiden, beliebte Touristenattraktionen zu Stoßzeiten zu empfehlen.
3. **Fehlerkorrektur**: Wenn der Reiseagent in der Vergangenheit einen Fehler bei einer Buchung gemacht hat, z. B. ein ausgebuchtes Hotel vorgeschlagen hat, lernt er, die Verfügbarkeit vor der Empfehlung gründlicher zu überprüfen.

#### Praktisches Entwicklerbeispiel

Hier ist ein vereinfachtes Beispiel, wie der Code des Reiseagenten aussehen könnte, wenn Metakognition integriert wird:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Search for flights, hotels, and attractions based on preferences
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analyze feedback and adjust future recommendations
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### Warum Metakognition wichtig ist

- **Selbstreflexion**: Agenten können ihre Leistung analysieren und Verbesserungsmöglichkeiten identifizieren.
- **Anpassungsfähigkeit**: Agenten können Strategien basierend auf Feedback und sich ändernden Bedingungen anpassen.
- **Fehlerkorrektur**: Agenten können Fehler eigenständig erkennen und korrigieren.
- **Ressourcenmanagement**: Agenten können den Ressourceneinsatz wie Zeit und Rechenleistung optimieren.

Durch die Integration von Metakognition kann der Reiseagent personalisiertere und genauere Reiseempfehlungen geben und so das Gesamterlebnis des Nutzers verbessern.

---

## 2. Planung in Agenten

Planung ist ein entscheidender Bestandteil des Verhaltens von KI-Agenten. Sie umfasst das Festlegen der Schritte, die zur Erreichung eines Ziels erforderlich sind, unter Berücksichtigung des aktuellen Zustands, der Ressourcen und möglicher Hindernisse.

### Elemente der Planung

- **Aktuelle Aufgabe**: Die Aufgabe klar definieren.
- **Schritte zur Erledigung der Aufgabe**: Die Aufgabe in überschaubare Schritte unterteilen.
- **Benötigte Ressourcen**: Notwendige Ressourcen identifizieren.
- **Erfahrung**: Vergangene Erfahrungen nutzen, um die Planung zu informieren.

**Beispiel**:
Hier sind die Schritte, die der Reiseagent unternehmen muss, um einem Nutzer effektiv bei der Reiseplanung zu helfen:

### Schritte für den Reiseagenten

1. **Nutzerpräferenzen sammeln**
   - Den Nutzer nach Details zu Reisedaten, Budget, Interessen und spezifischen Anforderungen fragen.
   - Beispiele: „Wann planen Sie zu reisen?“ „Was ist Ihr Budgetrahmen?“ „Welche Aktivitäten genießen Sie im Urlaub?“

2. **Informationen abrufen**
   - Nach relevanten Reiseoptionen basierend auf den Präferenzen des Nutzers suchen.
   - **Flüge**: Verfügbare Flüge innerhalb des Budgets und der bevorzugten Reisedaten suchen.
   - **Unterkünfte**: Hotels oder Mietobjekte finden, die den Präferenzen des Nutzers hinsichtlich Lage, Preis und Ausstattung entsprechen.
   - **Attraktionen und Restaurants**: Beliebte Attraktionen, Aktivitäten und Essensmöglichkeiten identifizieren, die den Interessen des Nutzers entsprechen.

3. **Empfehlungen generieren**
   - Die abgerufenen Informationen in einen personalisierten Reiseplan zusammenstellen.
   - Details wie Flugoptionen, Hotelreservierungen und vorgeschlagene Aktivitäten bereitstellen, die auf die Präferenzen des Nutzers zugeschnitten sind.

4. **Reiseplan dem Nutzer präsentieren**
   - Den vorgeschlagenen Reiseplan dem Nutzer zur Überprüfung vorlegen.
   - Beispiel: „Hier ist ein vorgeschlagener Reiseplan für Ihre Reise nach Paris. Er enthält Flugdaten, Hotelbuchungen und eine Liste empfohlener Aktivitäten und Restaurants. Lassen Sie mich wissen, was Sie davon halten!“

5. **Feedback einholen**
   - Den Nutzer nach Feedback zum vorgeschlagenen Reiseplan fragen.
   - Beispiele: „Gefällt Ihnen die Flugauswahl?“ „Ist das Hotel für Ihre Bedürfnisse geeignet?“ „Gibt es Aktivitäten, die Sie hinzufügen oder entfernen möchten?“

6. **Anpassen basierend auf Feedback**
   - Den Reiseplan basierend auf dem Feedback des Nutzers anpassen.
   - Notwendige Änderungen an Flug-, Unterkunfts- und Aktivitätsempfehlungen vornehmen, um die Präferenzen des Nutzers besser zu erfüllen.

7. **Endgültige Bestätigung**
   - Den aktualisierten Reiseplan dem Nutzer zur endgültigen Bestätigung vorlegen.
   - Beispiel: „Ich habe die Anpassungen basierend auf Ihrem Feedback vorgenommen. Hier ist der aktualisierte Reiseplan. Passt alles für Sie?“

8. **Buchungen vornehmen und bestätigen**
   - Nach der Genehmigung des Reiseplans durch den Nutzer Flüge, Unterkünfte und vorgeplante Aktivitäten buchen.
   - Bestätigungsdetails an den Nutzer senden.

9. **Laufende Unterstützung bieten**
   - Verfügbar bleiben, um dem Nutzer bei Änderungen oder zusätzlichen Anfragen vor und während der Reise zu helfen.
   - Beispiel: „Wenn Sie während Ihrer Reise weitere Unterstützung benötigen, können Sie sich jederzeit an mich wenden!“

### Beispielinteraktion

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage within a booing request
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

## 3. Korrektives RAG-System

Zunächst wollen wir den Unterschied zwischen dem RAG-Tool und dem präventiven Kontextladen verstehen.

![RAG vs Kontextladen](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.de.png)

### Retrieval-Augmented Generation (RAG)

RAG kombiniert ein Abrufsystem mit einem generativen Modell. Wenn eine Anfrage gestellt wird, ruft das Abrufsystem relevante Dokumente oder Daten aus einer externen Quelle ab, und diese abgerufenen Informationen werden verwendet, um die Eingabe für das generative Modell zu erweitern. Dies hilft dem Modell, genauere und kontextuell relevante Antworten zu generieren.

In einem RAG-System ruft der Agent relevante Informationen aus einer Wissensdatenbank ab und verwendet diese, um geeignete Antworten oder Aktionen zu generieren.

### Korrektiver RAG-Ansatz

Der korrektive RAG-Ansatz konzentriert sich darauf, RAG-Techniken zu nutzen, um Fehler zu korrigieren und die Genauigkeit von KI-Agenten zu verbessern. Dies umfasst:

1. **Prompting-Technik**: Spezifische Eingabeaufforderungen verwenden, um den Agenten bei der Suche nach relevanten Informationen zu leiten.
2. **Tool**: Algorithmen und Mechanismen implementieren, die es dem Agenten ermöglichen, die Relevanz der abgerufenen Informationen zu bewerten und genaue Antworten zu generieren.
3. **Bewertung**: Die Leistung des Agenten kontinuierlich bewerten und Anpassungen vornehmen, um seine Genauigkeit und Effizienz zu verbessern.

#### Beispiel: Korrektives RAG in einem Suchagenten

Betrachten Sie einen Suchagenten, der Informationen aus dem Internet abruft, um Nutzeranfragen zu beantworten. Der korrektive RAG-Ansatz könnte Folgendes umfassen:

1. **Prompting-Technik**: Suchanfragen basierend auf den Eingaben des Nutzers formulieren.
2. **Tool**: Algorithmen für natürliche Sprachverarbeitung und maschinelles Lernen verwenden, um Suchergebnisse zu bewerten und zu filtern.
3. **Bewertung**: Nutzerfeedback analysieren, um Ungenauigkeiten in den abgerufenen Informationen zu identifizieren und zu korrigieren.

### Korrektives RAG im Reiseagenten

Korrektives RAG (Retrieval-Augmented Generation) verbessert die Fähigkeit einer KI, Informationen abzurufen und zu generieren, während Ungenauigkeiten korrigiert werden. Schauen wir uns an, wie der Reiseagent den korrektiven RAG-Ansatz nutzen kann, um genauere und relevantere Reiseempfehlungen zu geben.

Dies umfasst:

- **Prompting-Technik:** Spezifische Eingabeaufforderungen verwenden, um den Agenten bei der Suche nach relevanten Informationen zu leiten.
- **Tool:** Algorithmen und Mechanismen implementieren, die es dem Agenten ermöglichen, die Relevanz der abgerufenen Informationen zu bewerten und genaue Antworten zu generieren.
- **Bewertung:** Die Leistung des Agenten kontinuierlich bewerten und Anpassungen vornehmen, um seine Genauigkeit und Effizienz zu verbessern.

#### Schritte zur Implementierung von Korrektivem RAG im Reiseagenten

1. **Erste Nutzerinteraktion**
   - Der Reiseagent sammelt erste Präferenzen des Nutzers, wie Zielort, Reisedaten, Budget und Interessen.
   - Beispiel:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Abruf von Informationen**
   - Der Reiseagent ruft Informationen zu Flügen, Unterkünften, Attraktionen und Restaurants basierend auf den Präferenzen des Nutzers ab.
   - Beispiel:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Generierung erster Empfehlungen**
   - Der Reiseagent verwendet die abgerufenen Informationen, um einen personalisierten Reiseplan zu erstellen.
   - Beispiel:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Einholen von Nutzerfeedback**
   - Der Reiseagent fragt den Nutzer nach Feedback zu den ersten Empfehlungen.
   - Beispiel:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Korrektiver RAG-Prozess**
   - **Prompting-Technik**: Der Reiseagent formuliert neue Suchanfragen basierend auf dem Nutzerfeedback.
     - Beispiel:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Tool**: Der Reiseagent verwendet Algorithmen, um neue Suchergebnisse zu bewerten und zu filtern, wobei der Schwerpunkt auf der Relevanz basierend auf dem Nutzerfeedback liegt.
     - Beispiel:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Bewertung**: Der Reiseagent bewertet kontinuierlich die Relevanz und Genauigkeit seiner Empfehlungen, indem er das Nutzerfeedback analysiert und notwendige Anpassungen vornimmt.
     - Beispiel:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Praktisches Beispiel

Hier ist ein vereinfachtes Python-Codebeispiel, das den korrektiven RAG-Ansatz im Reiseagenten integriert:
### Vorab-Kontextladen

Das Vorab-Kontextladen beinhaltet das Laden relevanter Informationen oder Hintergrunddaten in das Modell, bevor eine Anfrage verarbeitet wird. Das bedeutet, dass das Modell von Anfang an Zugriff auf diese Informationen hat, was ihm hilft, fundiertere Antworten zu generieren, ohne während des Prozesses zusätzliche Daten abrufen zu müssen.

Hier ist ein vereinfachtes Beispiel, wie ein Vorab-Kontextladen für eine Reisebüro-Anwendung in Python aussehen könnte:

```python
class TravelAgent:
    def __init__(self):
        # Pre-load popular destinations and their information
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Fetch destination information from pre-loaded context
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Example usage
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Erklärung

1. **Initialisierung (`__init__` Methode)**: Die Klasse `TravelAgent` lädt ein Wörterbuch vorab, das Informationen über beliebte Reiseziele wie Paris, Tokio, New York und Sydney enthält. Dieses Wörterbuch umfasst Details wie Land, Währung, Sprache und Hauptattraktionen für jedes Reiseziel.

2. **Abrufen von Informationen (`get_destination_info` Methode)**: Wenn ein Benutzer nach einem bestimmten Reiseziel fragt, ruft die Methode `get_destination_info` die relevanten Informationen aus dem vorab geladenen Kontext-Wörterbuch ab.

Durch das Vorab-Laden des Kontexts kann die Reisebüro-Anwendung schnell auf Benutzeranfragen reagieren, ohne diese Informationen in Echtzeit aus einer externen Quelle abrufen zu müssen. Dies macht die Anwendung effizienter und reaktionsschneller.

### Den Plan mit einem Ziel vor dem Iterieren starten

Einen Plan mit einem Ziel zu starten bedeutet, mit einem klar definierten Ziel oder Ergebnis zu beginnen. Indem dieses Ziel im Voraus festgelegt wird, kann das Modell es als Leitprinzip während des gesamten iterativen Prozesses nutzen. Dies hilft sicherzustellen, dass jede Iteration dem gewünschten Ergebnis näher kommt, wodurch der Prozess effizienter und fokussierter wird.

Hier ist ein Beispiel, wie ein Reiseplan mit einem Ziel vor dem Iterieren für ein Reisebüro in Python gestartet werden könnte:

### Szenario

Ein Reisebüro möchte einen maßgeschneiderten Urlaub für einen Kunden planen. Das Ziel ist es, eine Reiseplanung zu erstellen, die die Zufriedenheit des Kunden basierend auf seinen Vorlieben und seinem Budget maximiert.

### Schritte

1. Die Vorlieben und das Budget des Kunden definieren.
2. Den initialen Plan basierend auf diesen Vorlieben starten.
3. Iterieren, um den Plan zu verfeinern und die Zufriedenheit des Kunden zu optimieren.

#### Python-Code

```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# Example usage
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```

#### Code-Erklärung

1. **Initialisierung (`__init__` Methode)**: Die Klasse `TravelAgent` wird mit einer Liste potenzieller Reiseziele initialisiert, die Attribute wie Name, Kosten und Aktivitätstyp enthalten.

2. **Den Plan starten (`bootstrap_plan` Methode)**: Diese Methode erstellt einen initialen Reiseplan basierend auf den Vorlieben und dem Budget des Kunden. Sie iteriert durch die Liste der Reiseziele und fügt sie dem Plan hinzu, wenn sie den Vorlieben des Kunden entsprechen und ins Budget passen.

3. **Vorlieben abgleichen (`match_preferences` Methode)**: Diese Methode überprüft, ob ein Reiseziel den Vorlieben des Kunden entspricht.

4. **Den Plan iterieren (`iterate_plan` Methode)**: Diese Methode verfeinert den initialen Plan, indem sie versucht, jedes Reiseziel im Plan durch eine bessere Option zu ersetzen, unter Berücksichtigung der Vorlieben und Budgetbeschränkungen des Kunden.

5. **Kosten berechnen (`calculate_cost` Methode)**: Diese Methode berechnet die Gesamtkosten des aktuellen Plans, einschließlich eines potenziellen neuen Reiseziels.

#### Beispielanwendung

- **Initialer Plan**: Das Reisebüro erstellt einen initialen Plan basierend auf den Vorlieben des Kunden für Sightseeing und einem Budget von 2000 $.
- **Verfeinerter Plan**: Das Reisebüro iteriert den Plan, um ihn an die Vorlieben und das Budget des Kunden anzupassen.

Indem der Plan mit einem klaren Ziel (z. B. Maximierung der Kundenzufriedenheit) gestartet und iterativ verfeinert wird, kann das Reisebüro eine maßgeschneiderte und optimierte Reiseplanung für den Kunden erstellen. Dieser Ansatz stellt sicher, dass der Reiseplan von Anfang an mit den Vorlieben und dem Budget des Kunden übereinstimmt und sich mit jeder Iteration verbessert.

### Nutzung von LLM für Neu-Ranking und Bewertung

Große Sprachmodelle (LLMs) können für Neu-Ranking und Bewertung verwendet werden, indem sie die Relevanz und Qualität abgerufener Dokumente oder generierter Antworten bewerten. So funktioniert es:

**Abruf:** Der erste Abrufschritt holt eine Reihe von Kandidatendokumenten oder Antworten basierend auf der Anfrage.

**Neu-Ranking:** Das LLM bewertet diese Kandidaten und ordnet sie neu basierend auf ihrer Relevanz und Qualität. Dieser Schritt stellt sicher, dass die relevantesten und qualitativ hochwertigsten Informationen zuerst präsentiert werden.

**Bewertung:** Das LLM weist jedem Kandidaten eine Bewertung zu, die seine Relevanz und Qualität widerspiegelt. Dies hilft dabei, die beste Antwort oder das beste Dokument für den Benutzer auszuwählen.

Durch die Nutzung von LLMs für Neu-Ranking und Bewertung kann das System genauere und kontextuell relevante Informationen bereitstellen, was die Benutzererfahrung insgesamt verbessert.

Hier ist ein Beispiel, wie ein Reisebüro ein großes Sprachmodell (LLM) für Neu-Ranking und Bewertung von Reisezielen basierend auf Benutzerpräferenzen in Python verwenden könnte:

#### Szenario - Reisen basierend auf Präferenzen

Ein Reisebüro möchte dem Kunden die besten Reiseziele basierend auf seinen Präferenzen empfehlen. Das LLM hilft dabei, die Reiseziele neu zu ordnen und zu bewerten, um sicherzustellen, dass die relevantesten Optionen präsentiert werden.

#### Schritte:

1. Benutzerpräferenzen sammeln.
2. Eine Liste potenzieller Reiseziele abrufen.
3. Das LLM verwenden, um die Reiseziele basierend auf Benutzerpräferenzen neu zu ordnen und zu bewerten.

Hier ist, wie Sie das vorherige Beispiel mit Azure OpenAI Services aktualisieren können:

#### Anforderungen

1. Sie benötigen ein Azure-Abonnement.
2. Erstellen Sie eine Azure OpenAI-Ressource und erhalten Sie Ihren API-Schlüssel.

#### Beispiel-Python-Code

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generate a prompt for the Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Define headers and payload for the request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Call the Azure OpenAI API to get the re-ranked and scored destinations
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extract and return the recommendations
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# Example usage
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```

#### Code-Erklärung - Präferenzbucher

1. **Initialisierung**: Die Klasse `TravelAgent` wird mit einer Liste potenzieller Reiseziele initialisiert, die Attribute wie Name und Beschreibung enthalten.

2. **Empfehlungen abrufen (`get_recommendations` Methode)**: Diese Methode generiert basierend auf den Benutzerpräferenzen eine Eingabeaufforderung für den Azure OpenAI-Dienst und sendet eine HTTP-POST-Anfrage an die Azure OpenAI-API, um neu geordnete und bewertete Reiseziele zu erhalten.

3. **Eingabeaufforderung generieren (`generate_prompt` Methode)**: Diese Methode erstellt eine Eingabeaufforderung für Azure OpenAI, einschließlich der Benutzerpräferenzen und der Liste der Reiseziele. Die Eingabeaufforderung leitet das Modell an, die Reiseziele basierend auf den angegebenen Präferenzen neu zu ordnen und zu bewerten.

4. **API-Aufruf**: Die Bibliothek `requests` wird verwendet, um eine HTTP-POST-Anfrage an den Azure OpenAI-API-Endpunkt zu senden. Die Antwort enthält die neu geordneten und bewerteten Reiseziele.

5. **Beispielanwendung**: Das Reisebüro sammelt Benutzerpräferenzen (z. B. Interesse an Sightseeing und vielfältiger Kultur) und verwendet den Azure OpenAI-Dienst, um neu geordnete und bewertete Empfehlungen für Reiseziele zu erhalten.

Ersetzen Sie `your_azure_openai_api_key` durch Ihren tatsächlichen Azure OpenAI-API-Schlüssel und `https://your-endpoint.com/...` durch die tatsächliche URL des Endpunkts Ihrer Azure OpenAI-Bereitstellung.

Durch die Nutzung des LLM für Neu-Ranking und Bewertung kann das Reisebüro personalisierte und relevante Reiseempfehlungen für Kunden bereitstellen und deren Gesamterlebnis verbessern.
#### Praktisches Beispiel: Suchen mit Intention im Reisebüro

Nehmen wir das Reisebüro als Beispiel, um zu sehen, wie das Suchen mit Intention umgesetzt werden kann.

1. **Sammeln von Benutzerpräferenzen**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Verstehen der Benutzerintention**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Kontextbewusstsein**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Suchen und Personalisieren von Ergebnissen**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Example search logic for informational intent
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Example search logic for navigational intent
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Example search logic for transactional intent
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Example personalization logic
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Return top 10 personalized results
   ```

5. **Beispielanwendung**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. Code als Werkzeug generieren

Code-generierende Agenten nutzen KI-Modelle, um Code zu schreiben und auszuführen, komplexe Probleme zu lösen und Aufgaben zu automatisieren.

### Code-generierende Agenten

Code-generierende Agenten verwenden generative KI-Modelle, um Code zu schreiben und auszuführen. Diese Agenten können komplexe Probleme lösen, Aufgaben automatisieren und wertvolle Einblicke liefern, indem sie Code in verschiedenen Programmiersprachen generieren und ausführen.

#### Praktische Anwendungen

1. **Automatisierte Codegenerierung**: Erstellen von Code-Snippets für spezifische Aufgaben wie Datenanalyse, Web-Scraping oder maschinelles Lernen.
2. **SQL als RAG**: Verwenden von SQL-Abfragen, um Daten aus Datenbanken abzurufen und zu manipulieren.
3. **Problemlösung**: Erstellen und Ausführen von Code, um spezifische Probleme zu lösen, wie z. B. die Optimierung von Algorithmen oder die Analyse von Daten.

#### Beispiel: Code-generierender Agent für Datenanalyse

Stellen Sie sich vor, Sie entwerfen einen code-generierenden Agenten. So könnte er funktionieren:

1. **Aufgabe**: Analysieren eines Datensatzes, um Trends und Muster zu erkennen.
2. **Schritte**:
   - Laden des Datensatzes in ein Datenanalysetool.
   - Generieren von SQL-Abfragen, um die Daten zu filtern und zu aggregieren.
   - Ausführen der Abfragen und Abrufen der Ergebnisse.
   - Verwenden der Ergebnisse zur Erstellung von Visualisierungen und Einblicken.
3. **Benötigte Ressourcen**: Zugriff auf den Datensatz, Datenanalysetools und SQL-Fähigkeiten.
4. **Erfahrung**: Nutzen vergangener Analyseergebnisse, um die Genauigkeit und Relevanz zukünftiger Analysen zu verbessern.

### Beispiel: Code-generierender Agent für Reisebüro

In diesem Beispiel entwerfen wir einen code-generierenden Agenten, das Reisebüro, um Nutzern bei der Reiseplanung zu helfen, indem er Code generiert und ausführt. Dieser Agent kann Aufgaben wie das Abrufen von Reiseoptionen, das Filtern von Ergebnissen und das Erstellen eines Reiseplans mithilfe generativer KI übernehmen.

#### Überblick über den Code-generierenden Agenten

1. **Sammeln von Benutzerpräferenzen**: Erfasst Benutzereingaben wie Zielort, Reisedaten, Budget und Interessen.
2. **Codegenerierung zum Abrufen von Daten**: Generiert Code-Snippets, um Daten zu Flügen, Hotels und Attraktionen abzurufen.
3. **Ausführen des generierten Codes**: Führt den generierten Code aus, um Echtzeitinformationen abzurufen.
4. **Erstellen eines Reiseplans**: Stellt die abgerufenen Daten zu einem personalisierten Reiseplan zusammen.
5. **Anpassen basierend auf Feedback**: Nimmt Benutzerfeedback entgegen und generiert bei Bedarf neuen Code, um die Ergebnisse zu verfeinern.

#### Schritt-für-Schritt-Implementierung

1. **Sammeln von Benutzerpräferenzen**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Codegenerierung zum Abrufen von Daten**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Example: Generate code to search for flights based on user preferences
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Example: Generate code to search for hotels
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Ausführen des generierten Codes**

   ```python
   def execute_code(code):
       # Execute the generated code using exec
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **Erstellen eines Reiseplans**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **Anpassen basierend auf Feedback**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Adjust preferences based on user feedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerate and execute code with updated preferences
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Nutzung von Umweltbewusstsein und logischem Denken

Das Einbeziehen des Schemas der Tabelle kann den Prozess der Abfragengenerierung verbessern, indem Umweltbewusstsein und logisches Denken genutzt werden.

Hier ist ein Beispiel, wie dies umgesetzt werden kann:

1. **Verstehen des Schemas**: Das System versteht das Schema der Tabelle und nutzt diese Informationen, um die Abfragengenerierung zu untermauern.
2. **Anpassen basierend auf Feedback**: Das System passt Benutzerpräferenzen basierend auf Feedback an und überlegt, welche Felder im Schema aktualisiert werden müssen.
3. **Generieren und Ausführen von Abfragen**: Das System generiert und führt Abfragen aus, um aktualisierte Flug- und Hoteldaten basierend auf den neuen Präferenzen abzurufen.

Hier ist ein aktualisiertes Python-Code-Beispiel, das diese Konzepte integriert:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Adjust preferences based on user feedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Reasoning based on schema to adjust other related preferences
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Custom logic to adjust preferences based on schema and feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generate code to fetch flight data based on updated preferences
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generate code to fetch hotel data based on updated preferences
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulate execution of code and return mock data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generate itinerary based on flights, hotels, and attractions
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Example schema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Example usage
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerate and execute code with updated preferences
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Erklärung – Buchung basierend auf Feedback

1. **Schema-Bewusstsein**: Das `schema`-Dictionary definiert, wie Präferenzen basierend auf Feedback angepasst werden sollen. Es enthält Felder wie `favorites` und `avoid` mit entsprechenden Anpassungen.
2. **Anpassen der Präferenzen (`adjust_based_on_feedback`-Methode)**: Diese Methode passt Präferenzen basierend auf Benutzerfeedback und dem Schema an.
3. **Umweltbasierte Anpassungen (`adjust_based_on_environment`-Methode)**: Diese Methode passt die Anpassungen basierend auf Schema und Feedback an.
4. **Generieren und Ausführen von Abfragen**: Das System generiert Code, um aktualisierte Flug- und Hoteldaten basierend auf den angepassten Präferenzen abzurufen, und simuliert die Ausführung dieser Abfragen.
5. **Erstellen eines Reiseplans**: Das System erstellt einen aktualisierten Reiseplan basierend auf den neuen Flug-, Hotel- und Attraktionsdaten.

Durch die Nutzung von Umweltbewusstsein und logischem Denken basierend auf dem Schema kann das System genauere und relevantere Abfragen generieren, was zu besseren Reiseempfehlungen und einer personalisierten Benutzererfahrung führt.

### Verwendung von SQL als Retrieval-Augmented Generation (RAG)-Technik

SQL (Structured Query Language) ist ein leistungsstarkes Werkzeug zur Interaktion mit Datenbanken. Als Teil eines Retrieval-Augmented Generation (RAG)-Ansatzes kann SQL relevante Daten aus Datenbanken abrufen, um Antworten oder Aktionen in KI-Agenten zu informieren und zu generieren. Schauen wir uns an, wie SQL als RAG-Technik im Kontext des Reisebüros verwendet werden kann.

#### Schlüsselkonzepte

1. **Datenbankinteraktion**:
   - SQL wird verwendet, um Datenbanken abzufragen, relevante Informationen abzurufen und Daten zu manipulieren.
   - Beispiel: Abrufen von Flugdaten, Hotelinformationen und Attraktionen aus einer Reisedatenbank.

2. **Integration mit RAG**:
   - SQL-Abfragen werden basierend auf Benutzereingaben und Präferenzen generiert.
   - Die abgerufenen Daten werden dann verwendet, um personalisierte Empfehlungen oder Aktionen zu generieren.

3. **Dynamische Abfragengenerierung**:
   - Der KI-Agent generiert dynamische SQL-Abfragen basierend auf dem Kontext und den Benutzerbedürfnissen.
   - Beispiel: Anpassen von SQL-Abfragen, um Ergebnisse basierend auf Budget, Daten und Interessen zu filtern.

#### Anwendungen

- **Automatisierte Codegenerierung**: Erstellen von Code-Snippets für spezifische Aufgaben.
- **SQL als RAG**: Verwenden von SQL-Abfragen zur Datenmanipulation.
- **Problemlösung**: Erstellen und Ausführen von Code zur Lösung von Problemen.

**Beispiel**:
Ein Datenanalyse-Agent:

1. **Aufgabe**: Analysieren eines Datensatzes, um Trends zu finden.
2. **Schritte**:
   - Laden des Datensatzes.
   - Generieren von SQL-Abfragen, um Daten zu filtern.
   - Ausführen der Abfragen und Abrufen der Ergebnisse.
   - Erstellen von Visualisierungen und Einblicken.
3. **Ressourcen**: Zugriff auf den Datensatz, SQL-Fähigkeiten.
4. **Erfahrung**: Nutzen vergangener Ergebnisse, um zukünftige Analysen zu verbessern.

#### Praktisches Beispiel: Verwendung von SQL im Reisebüro

1. **Sammeln von Benutzerpräferenzen**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generieren von SQL-Abfragen**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Ausführen von SQL-Abfragen**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **Generieren von Empfehlungen**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### Beispiel-SQL-Abfragen

1. **Flugabfrage**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Hotelabfrage**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Attraktionsabfrage**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Durch die Nutzung von SQL als Teil der Retrieval-Augmented Generation (RAG)-Technik können KI-Agenten wie das Reisebüro dynamisch relevante Daten abrufen und nutzen, um präzise und personalisierte Empfehlungen bereitzustellen.

### Beispiel für Metakognition

Um eine Implementierung von Metakognition zu demonstrieren, erstellen wir einen einfachen Agenten, der *über seinen Entscheidungsprozess nachdenkt*, während er ein Problem löst. In diesem Beispiel wird ein System entwickelt, bei dem ein Agent versucht, die Wahl eines Hotels zu optimieren, dann aber seinen eigenen Entscheidungsprozess evaluiert und seine Strategie anpasst, wenn Fehler oder suboptimale Entscheidungen auftreten.

#### Wie dies Metakognition illustriert:

1. **Erste Entscheidung**: Der Agent wählt das günstigste Hotel, ohne die Auswirkungen auf die Qualität zu berücksichtigen.
2. **Reflexion und Bewertung**: Nach der ersten Wahl überprüft der Agent, ob das Hotel eine "schlechte" Wahl war, basierend auf Benutzerfeedback. Wenn er feststellt, dass die Qualität des Hotels zu niedrig war, reflektiert er über seinen Entscheidungsprozess.
3. **Anpassen der Strategie**: Der Agent passt seine Strategie an, indem er von "günstigstes" zu "höchste Qualität" wechselt, und verbessert so seinen Entscheidungsprozess für zukünftige Iterationen.

Hier ist ein Beispiel:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Stores the hotels chosen previously
        self.corrected_choices = []  # Stores the corrected choices
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Available strategies

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # Let's assume we have some user feedback that tells us whether the last choice was good or not
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Adjust strategy if the previous choice was unsatisfactory
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# Simulate a list of hotels (price and quality)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Create an agent
agent = HotelRecommendationAgent()

# Step 1: The agent recommends a hotel using the "cheapest" strategy
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Step 2: The agent reflects on the choice and adjusts strategy if necessary
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Step 3: The agent recommends again, this time using the adjusted strategy
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Metakognitive Fähigkeiten des Agenten

Der Schlüssel liegt hier in der Fähigkeit des Agenten:
- Seine vorherigen Entscheidungen und den Entscheidungsprozess zu bewerten.
- Seine Strategie basierend auf dieser Reflexion anzupassen, d. h. Metakognition in Aktion.

Dies ist eine einfache Form der Metakognition, bei der das System in der Lage ist, seinen Denkprozess basierend auf internem Feedback anzupassen.

### Fazit

Metakognition ist ein leistungsstarkes Werkzeug, das die Fähigkeiten von KI-Agenten erheblich verbessern kann. Durch die Integration metakognitiver Prozesse können Sie Agenten entwerfen, die intelligenter, anpassungsfähiger und effizienter sind. Nutzen Sie die zusätzlichen Ressourcen, um die faszinierende Welt der Metakognition in KI-Agenten weiter zu erkunden.

### Noch Fragen zum Metakognitions-Designmuster?

Treten Sie dem [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten beantwortet zu bekommen.

## Vorherige Lektion

[Multi-Agent-Designmuster](../08-multi-agent/README.md)

## Nächste Lektion

[KI-Agenten in der Produktion](../10-ai-agents-production/README.md)

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.