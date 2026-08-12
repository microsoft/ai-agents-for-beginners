[![Multi-Agent Design](../../../translated_images/de/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Klicken Sie auf das obige Bild, um das Video dieser Lektion anzusehen)_
# Metakognition bei KI-Agenten

## Einführung

Willkommen zur Lektion über Metakognition bei KI-Agenten! Dieses Kapitel richtet sich an Anfänger, die neugierig sind, wie KI-Agenten über ihre eigenen Denkprozesse nachdenken können. Am Ende dieser Lektion verstehen Sie wichtige Konzepte und sind mit praktischen Beispielen ausgestattet, um Metakognition im Design von KI-Agenten anzuwenden.

## Lernziele

Nach Abschluss dieser Lektion werden Sie in der Lage sein:

1. Die Auswirkungen von Schlussfolgerungsschleifen in Agentendefinitionen zu verstehen.
2. Planungs- und Bewertungstechniken zu verwenden, um selbstkorrigierende Agenten zu unterstützen.
3. Eigene Agenten zu erstellen, die in der Lage sind, Code zu manipulieren, um Aufgaben zu erfüllen.

## Einführung in die Metakognition

Metakognition bezieht sich auf höherstufige kognitive Prozesse, die das Nachdenken über das eigene Denken umfassen. Für KI-Agenten bedeutet dies, ihre Handlungen auf Basis von Selbstbewusstsein und vergangenen Erfahrungen bewerten und anpassen zu können. Metakognition oder „Nachdenken über das Denken“ ist ein wichtiger Begriff in der Entwicklung agentischer KI-Systeme. Es beinhaltet, dass KI-Systeme sich ihrer eigenen inneren Prozesse bewusst sind und ihr Verhalten entsprechend überwachen, regulieren und anpassen können. So wie wir es tun, wenn wir die Situation einschätzen oder ein Problem betrachten. Dieses Selbstbewusstsein kann KI-Systemen helfen, bessere Entscheidungen zu treffen, Fehler zu erkennen und ihre Leistung mit der Zeit zu verbessern – was wieder auf den Turing-Test und die Debatte zurückführt, ob KI die Kontrolle übernehmen wird.

Im Kontext agentischer KI-Systeme kann Metakognition mehrere Herausforderungen angehen, wie zum Beispiel:
- Transparenz: Sicherstellen, dass KI-Systeme ihre Schlussfolgerungen und Entscheidungen erklären können.
- Schlussfolgerung: Verbesserung der Fähigkeit von KI-Systemen, Informationen zu synthetisieren und fundierte Entscheidungen zu treffen.
- Anpassungsfähigkeit: Ermöglichung, dass KI-Systeme sich an neue Umgebungen und wechselnde Bedingungen anpassen.
- Wahrnehmung: Verbesserung der Genauigkeit von KI-Systemen bei der Erkennung und Interpretation von Daten aus ihrer Umgebung.

### Was ist Metakognition?

Metakognition, oder „Nachdenken über das Denken“, ist ein höherstufiger kognitiver Prozess, der Selbstbewusstsein und Selbstregulierung der eigenen kognitiven Prozesse beinhaltet. Im Bereich der KI befähigt Metakognition Agenten, ihre Strategien und Handlungen zu bewerten und anzupassen, was zu verbesserten Problemlösungs- und Entscheidungsfähigkeiten führt. Durch das Verständnis von Metakognition können Sie KI-Agenten entwerfen, die nicht nur intelligenter, sondern auch anpassungsfähiger und effizienter sind. In echter Metakognition würden Sie die KI explizit über ihr eigenes Denken nachdenken sehen.

Beispiel: „Ich habe billigere Flüge priorisiert, weil… ich könnte Direktflüge verpassen, also überprüfe ich das noch einmal.“
Nachverfolgen, wie oder warum sie eine bestimmte Route gewählt hat.
- Feststellen, dass sie Fehler gemacht hat, weil sie sich zu sehr auf Nutzerpräferenzen vom letzten Mal verlassen hat, also passt sie ihre Entscheidungsstrategie an und nicht nur die endgültige Empfehlung.
- Muster diagnostizieren wie: „Immer wenn ich den Nutzer ‚zu voll‘ sagen höre, sollte ich nicht nur bestimmte Attraktionen entfernen, sondern auch reflektieren, dass meine Methode zur Auswahl der ‚Top-Attraktionen‘ fehlerhaft ist, wenn ich immer nach Beliebtheit sortiere.“

### Bedeutung der Metakognition bei KI-Agenten

Metakognition spielt im Design von KI-Agenten aus mehreren Gründen eine entscheidende Rolle:

![Bedeutung der Metakognition](../../../translated_images/de/importance-of-metacognition.b381afe9aae352f7.webp)

- Selbstreflexion: Agenten können ihre eigene Leistung bewerten und Verbesserungsbereiche identifizieren.
- Anpassungsfähigkeit: Agenten können ihre Strategien basierend auf vergangenen Erfahrungen und sich ändernden Umgebungen anpassen.
- Fehlerkorrektur: Agenten können Fehler autonom erkennen und korrigieren, was zu genaueren Ergebnissen führt.
- Ressourcenmanagement: Agenten können die Nutzung von Ressourcen wie Zeit und Rechenleistung durch Planung und Bewertung optimieren.

## Komponenten eines KI-Agenten

Bevor wir in metakognitive Prozesse eintauchen, ist es wichtig, die Grundkomponenten eines KI-Agenten zu verstehen. Ein KI-Agent besteht typischerweise aus:

- Persona: Die Persönlichkeit und Eigenschaften des Agenten, die definieren, wie er mit Nutzern interagiert.
- Werkzeuge: Die Fähigkeiten und Funktionen, die der Agent ausführen kann.
- Fertigkeiten: Das Wissen und die Expertise, die der Agent besitzt.

Diese Komponenten arbeiten zusammen, um eine „Expertise-Einheit“ zu bilden, die spezifische Aufgaben erfüllen kann.

**Beispiel**:
Betrachten Sie einen Reiseagenten, Agenten-Services, die nicht nur Ihren Urlaub planen, sondern ihren Weg auch basierend auf Echtzeitdaten und vergangenen Kundenerfahrungen anpassen.

### Beispiel: Metakognition in einem Reiseagenten-Service

Stellen Sie sich vor, Sie entwerfen einen KI-Reiseagenten-Service. Dieser Agent „Reiseagent“ unterstützt Nutzer bei der Urlaubsplanung. Um Metakognition einzubeziehen, muss Reiseagent seine Aktionen basierend auf Selbstbewusstsein und vergangenen Erfahrungen bewerten und anpassen. So könnte Metakognition eine Rolle spielen:

#### Aktuelle Aufgabe

Die aktuelle Aufgabe besteht darin, einem Nutzer bei der Planung einer Reise nach Paris zu helfen.

#### Schritte zur Durchführung der Aufgabe

1. **Nutzerpräferenzen sammeln**: Den Nutzer nach Reisedaten, Budget, Interessen (z. B. Museen, Küche, Shopping) und speziellen Anforderungen fragen.
2. **Informationen abrufen**: Nach Flugoptionen, Unterkünften, Sehenswürdigkeiten und Restaurants suchen, die den Nutzerpräferenzen entsprechen.
3. **Empfehlungen generieren**: Eine personalisierte Reiseroute mit Flugdaten, Hotelreservierungen und vorgeschlagenen Aktivitäten bereitstellen.
4. **Anpassung basierend auf Feedback**: Den Nutzer um Feedback zu den Empfehlungen bitten und entsprechende Korrekturen vornehmen.

#### Benötigte Ressourcen

- Zugriff auf Flug- und Hotelbuchungsdatenbanken.
- Informationen zu Pariser Sehenswürdigkeiten und Restaurants.
- Nutzerrückmeldungsdaten aus vorherigen Interaktionen.

#### Erfahrung und Selbstreflexion

Reiseagent verwendet Metakognition, um seine Leistung zu bewerten und aus vergangenen Erfahrungen zu lernen. Zum Beispiel:

1. **Analyse des Nutzerfeedbacks**: Reiseagent überprüft das Nutzerfeedback, um herauszufinden, welche Empfehlungen gut angekommen sind und welche nicht. Er passt seine zukünftigen Vorschläge entsprechend an.
2. **Anpassungsfähigkeit**: Wenn ein Nutzer zuvor erwähnt hat, dass er keine überfüllten Orte mag, wird Reiseagent künftig vermeiden, zu beliebten Touristenzielen in Stoßzeiten zu empfehlen.
3. **Fehlerkorrektur**: Wenn Reiseagent einen Fehler bei einer früheren Buchung gemacht hat, z. B. ein Hotel vorgeschlagen hat, das ausgebucht war, lernt er, die Verfügbarkeit vor Empfehlungen genauer zu prüfen.

#### Praktisches Entwicklerbeispiel

Hier ist ein vereinfachtes Beispiel dafür, wie der Code von Reiseagent aussehen könnte, wenn Metakognition einbezogen wird:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Suche nach Flügen, Hotels und Attraktionen basierend auf Vorlieben
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
        # Analysiere Rückmeldungen und passe zukünftige Empfehlungen an
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Anwendungsbeispiel
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

- **Selbstreflexion**: Agenten können ihre Leistung analysieren und Verbesserungsbereiche identifizieren.
- **Anpassungsfähigkeit**: Agenten können Strategien basierend auf Feedback und sich ändernden Bedingungen ändern.
- **Fehlerkorrektur**: Agenten können Fehler autonom erkennen und korrigieren.
- **Ressourcenmanagement**: Agenten können die Ressourcennutzung wie Zeit und Rechenleistung optimieren.

Durch die Einbindung von Metakognition kann Reiseagent persönlichere und genauere Reiseempfehlungen geben und so das Nutzererlebnis verbessern.

---

## 2. Planung bei Agenten

Planung ist eine kritische Komponente des Verhaltens von KI-Agenten. Sie umfasst das Festlegen der Schritte, die zum Erreichen eines Ziels erforderlich sind, unter Berücksichtigung des aktuellen Zustands, der Ressourcen und möglicher Hindernisse.

### Planungselemente

- **Aktuelle Aufgabe**: Die Aufgabe klar definieren.
- **Schritte zur Durchführung der Aufgabe**: Die Aufgabe in handhabbare Schritte unterteilen.
- **Benötigte Ressourcen**: Notwendige Ressourcen identifizieren.
- **Erfahrung**: Frühere Erfahrungen für die Planung nutzen.

**Beispiel**:
Hier sind die Schritte, die Reiseagent unternehmen muss, um einem Nutzer effektiv bei der Reiseplanung zu helfen:

### Schritte für Reiseagent

1. **Nutzerpräferenzen sammeln**
   - Den Nutzer nach Details zu Reisedaten, Budget, Interessen und speziellen Anforderungen fragen.
   - Beispiele: „Wann planen Sie zu reisen?“ „Wie hoch ist Ihr Budget?“ „Welche Aktivitäten genießen Sie im Urlaub?“

2. **Informationen abrufen**
   - Relevante Reiseoptionen suchen, die den Nutzerpräferenzen entsprechen.
   - **Flüge**: Nach verfügbaren Flügen innerhalb des Nutzerbudgets und der bevorzugten Reisedaten suchen.
   - **Unterkünfte**: Hotels oder Mietobjekte finden, die den Präferenzen hinsichtlich Lage, Preis und Ausstattung entsprechen.
   - **Sehenswürdigkeiten und Restaurants**: Beliebte Attraktionen, Aktivitäten und Restaurants identifizieren, die zu den Interessen des Nutzers passen.

3. **Empfehlungen generieren**
   - Die abgerufenen Informationen zu einer personalisierten Reiseroute zusammenstellen.
   - Details wie Flugoptionen, Hotelreservierungen und vorgeschlagene Aktivitäten bereitstellen und die Empfehlungen an die Präferenzen des Nutzers anpassen.

4. **Reiseroute dem Nutzer präsentieren**
   - Die vorgeschlagene Reiseroute dem Nutzer zur Überprüfung vorlegen.
   - Beispiel: „Hier ist ein vorgeschlagener Reiseplan für Ihre Paris-Reise. Er enthält Flugdaten, Hotelbuchungen und eine Liste empfohlener Aktivitäten und Restaurants. Teilen Sie mir Ihre Meinung mit!“

5. **Feedback sammeln**
   - Den Nutzer nach Feedback zur vorgeschlagenen Reiseroute fragen.
   - Beispiele: „Gefallen Ihnen die Flugoptionen?“ „Ist das Hotel für Ihre Bedürfnisse geeignet?“ „Gibt es Aktivitäten, die Sie hinzufügen oder entfernen möchten?“

6. **Anpassung basierend auf Feedback**
   - Die Reiseroute basierend auf dem Feedback des Nutzers anpassen.
   - Notwendige Änderungen bei Flug-, Unterkunfts- und Aktivitätsempfehlungen vornehmen, um besser zu den Präferenzen des Nutzers zu passen.

7. **Endgültige Bestätigung**
   - Die aktualisierte Reiseroute dem Nutzer zur finalen Bestätigung vorlegen.
   - Beispiel: „Ich habe die Anpassungen basierend auf Ihrem Feedback vorgenommen. Hier ist die aktualisierte Reiseroute. Ist alles zu Ihrer Zufriedenheit?“

8. **Reservierungen buchen und bestätigen**
   - Sobald der Nutzer die Reiseroute genehmigt, Flug-, Unterkunfts- und vorgeplante Aktivitäten buchen.
   - Bestätigungsdetails an den Nutzer senden.

9. **Fortlaufende Unterstützung bieten**
   - Für Änderungen oder zusätzliche Anfragen vor und während der Reise verfügbar bleiben.
   - Beispiel: „Wenn Sie während Ihrer Reise weitere Unterstützung benötigen, können Sie sich jederzeit an mich wenden!“

### Beispielhafte Interaktion

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

# Beispielhafte Verwendung innerhalb einer Buchungsanfrage
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

Zunächst wollen wir den Unterschied zwischen RAG-Tool und präventivem Kontextladen verstehen.

![RAG vs Context Loading](../../../translated_images/de/rag-vs-context.9eae588520c00921.webp)

### Retrieval-Augmented Generation (RAG)

RAG kombiniert ein Retrieval-System mit einem generativen Modell. Wenn eine Anfrage gestellt wird, ruft das Retrieval-System relevante Dokumente oder Daten aus einer externen Quelle ab, und diese abgerufenen Informationen werden als Ergänzung zur Eingabe des generativen Modells verwendet. Dies hilft dem Modell, genauere und kontextuell relevante Antworten zu generieren.

In einem RAG-System ruft der Agent relevante Informationen aus einer Wissensdatenbank ab und nutzt sie, um passende Antworten oder Aktionen zu generieren.

### Korrektiver RAG-Ansatz

Der korrekte RAG-Ansatz konzentriert sich darauf, RAG-Techniken zu verwenden, um Fehler zu korrigieren und die Genauigkeit von KI-Agenten zu erhöhen. Dies umfasst:

1. **Prompting-Technik**: Verwendung spezifischer Eingabeaufforderungen, um den Agenten bei der Informationsbeschaffung zu leiten.
2. **Werkzeug**: Implementierung von Algorithmen und Mechanismen, die es dem Agenten ermöglichen, die Relevanz der abgerufenen Informationen zu bewerten und genaue Antworten zu generieren.
3. **Bewertung**: Kontinuierliche Leistungskontrolle des Agenten und Anpassungen zur Verbesserung von Genauigkeit und Effizienz.

#### Beispiel: Korrektives RAG bei einem Suchagenten

Betrachten Sie einen Suchagenten, der Informationen aus dem Web abruft, um Nutzeranfragen zu beantworten. Der korrigierende RAG-Ansatz könnte beinhalten:

1. **Prompting-Technik**: Formulierung von Suchanfragen basierend auf den Eingaben des Nutzers.
2. **Werkzeug**: Verwendung von NLP- und maschinellen Lernalgorithmen zur Rangfolge und Filterung von Suchergebnissen.
3. **Bewertung**: Analyse des Nutzerfeedbacks, um Ungenauigkeiten in den abgerufenen Informationen zu erkennen und zu korrigieren.

### Korrektives RAG im Reiseagenten

Korrektives RAG (Retrieval-Augmented Generation) verbessert die Fähigkeit einer KI, Informationen abzurufen und zu generieren, während Gleichzeitig Ungenauigkeiten korrigiert werden. Sehen wir, wie Reiseagent den korrigierenden RAG-Ansatz nutzen kann, um genauere und relevantere Reiseempfehlungen zu liefern.

Dies umfasst:

- **Prompting-Technik:** Verwendung spezifischer Eingabeaufforderungen, um den Agenten bei der Informationsbeschaffung zu leiten.
- **Werkzeug:** Implementierung von Algorithmen und Mechanismen, die es dem Agenten ermöglichen, die Relevanz der abgerufenen Informationen zu bewerten und genaue Antworten zu generieren.
- **Bewertung:** Kontinuierliche Leistungskontrolle des Agenten und Anpassungen zur Verbesserung von Genauigkeit und Effizienz.

#### Schritte zur Implementierung von Korrektivem RAG im Reiseagenten

1. **Erstkontakt mit dem Nutzer**
   - Reiseagent sammelt erste Präferenzen des Nutzers, wie Zielort, Reisedaten, Budget und Interessen.
   - Beispiel:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Informationsabruf**
   - Reiseagent ruft basierend auf den Nutzerpräferenzen Informationen zu Flügen, Unterkünften, Attraktionen und Restaurants ab.
   - Beispiel:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Generierung erster Empfehlungen**
   - Reiseagent nutzt die abgerufenen Informationen, um eine personalisierte Reiseroute zu erstellen.
   - Beispiel:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Sammlung von Nutzerfeedback**
   - Reiseagent bittet den Nutzer um Rückmeldung zu den ersten Empfehlungen.
   - Beispiel:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Korrektiver RAG-Prozess**
   - **Prompting-Technik**: Reiseagent formuliert neue Suchanfragen basierend auf dem Nutzerfeedback.
     - Beispiel:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Werkzeug**: Reiseagent verwendet Algorithmen, um neue Suchergebnisse zu bewerten und zu filtern, wobei die Relevanz basierend auf Nutzerfeedback betont wird.
     - Beispiel:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Bewertung**: Reiseagent bewertet kontinuierlich die Relevanz und Genauigkeit seiner Empfehlungen, indem Nutzerfeedback analysiert und notwendige Anpassungen vorgenommen werden.
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

Hier ist ein vereinfachtes Python-Codebeispiel, das den korrigierenden RAG-Ansatz im Reiseagenten integriert:

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
        new_itinerary = self.generate_recommendations()
        return new_itinerary

# Beispielverwendung
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
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```

### Präventives Kontextladen


Pre-emptives Kontextladen bedeutet, relevanten Kontext oder Hintergrundinformationen in das Modell zu laden, bevor eine Anfrage verarbeitet wird. Das bedeutet, dass das Modell von Anfang an Zugriff auf diese Informationen hat, was ihm helfen kann, fundiertere Antworten zu generieren, ohne während des Prozesses zusätzliche Daten abrufen zu müssen.

Hier ist ein vereinfachtes Beispiel, wie ein pre-emptives Kontextladen für eine Reisebüro-Anwendung in Python aussehen könnte:

```python
class TravelAgent:
    def __init__(self):
        # Beliebte Reiseziele und deren Informationen vorab laden
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Abrufen von Reiseziels-Informationen aus dem vorab geladenen Kontext
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Beispielverwendung
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Erklärung

1. **Initialisierung (`__init__`-Methode)**: Die `TravelAgent`-Klasse lädt vorab ein Wörterbuch mit Informationen über beliebte Reiseziele wie Paris, Tokio, New York und Sydney. Dieses Wörterbuch enthält Details wie Land, Währung, Sprache und wichtige Sehenswürdigkeiten für jedes Ziel.

2. **Informationsabfrage (`get_destination_info`-Methode)**: Wenn ein Benutzer eine bestimmte Destination abfragt, holt die `get_destination_info`-Methode die relevanten Informationen aus dem vorab geladenen Kontext-Wörterbuch.

Durch das vorgeladene Kontext kann die Reisebüro-Anwendung schnell auf Benutzeranfragen reagieren, ohne diese Informationen in Echtzeit aus einer externen Quelle abrufen zu müssen. Dies macht die Anwendung effizienter und reaktionsschneller.

### Plan mit Zielsetzung initialisieren vor Iteration

Das Initialisieren eines Plans mit einem Ziel bedeutet, mit einer klaren Zielsetzung oder einem gewünschten Ergebnis zu beginnen. Indem dieses Ziel von Anfang an definiert wird, kann das Modell es als Leitprinzip während des iterativen Prozesses verwenden. Das hilft sicherzustellen, dass jede Iteration dem Erreichen des gewünschten Ergebnisses näherkommt und macht den Prozess effizienter und fokussierter.

Hier ist ein Beispiel, wie man einen Reiseplan mit Zielsetzung initialisieren kann, bevor man für ein Reisebüro in Python iteriert:

### Szenario

Ein Reisebüro möchte einen maßgeschneiderten Urlaub für einen Kunden planen. Das Ziel ist es, eine Reiseroute zu erstellen, die die Zufriedenheit des Kunden basierend auf dessen Vorlieben und Budget maximiert.

### Schritte

1. Definieren Sie die Vorlieben und das Budget des Kunden.
2. Initialisieren Sie den ersten Plan basierend auf diesen Vorlieben.
3. Iterieren Sie, um den Plan zu verfeinern und die Zufriedenheit des Kunden zu optimieren.

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

# Beispielverwendung
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

1. **Initialisierung (`__init__`-Methode)**: Die `TravelAgent`-Klasse wird mit einer Liste möglicher Reiseziele initialisiert, die jeweils Attribute wie Name, Kosten und Aktivitätstyp haben.

2. **Plan initialisieren (`bootstrap_plan`-Methode)**: Diese Methode erstellt einen ersten Reiseplan basierend auf den Vorlieben und dem Budget des Kunden. Sie geht die Liste der Reiseziele durch und fügt sie dem Plan hinzu, wenn sie mit den Vorlieben des Kunden übereinstimmen und ins Budget passen.

3. **Vorlieben abgleichen (`match_preferences`-Methode)**: Diese Methode prüft, ob ein Reiseziel mit den Vorlieben des Kunden übereinstimmt.

4. **Plan iterieren (`iterate_plan`-Methode)**: Diese Methode verfeinert den ursprünglichen Plan, indem sie versucht, jedes Reiseziel durch eine besser passende Option zu ersetzen, unter Berücksichtigung der Vorlieben des Kunden und der Budgetbeschränkungen.

5. **Kosten berechnen (`calculate_cost`-Methode)**: Diese Methode berechnet die Gesamtkosten des aktuellen Plans, einschließlich eines eventuell neuen Reiseziels.

#### Beispielhafte Verwendung

- **Ursprünglicher Plan**: Das Reisebüro erstellt einen ersten Plan basierend auf den Vorlieben des Kunden für Sightseeing und einem Budget von 2000 $.
- **Verfeinerter Plan**: Das Reisebüro iteriert den Plan, um ihn für die Vorlieben und das Budget des Kunden zu optimieren.

Durch das Initialisieren des Plans mit einem klaren Ziel (z. B. Maximierung der Kundenzufriedenheit) und dem iterativen Verfeinern kann das Reisebüro eine maßgeschneiderte und optimierte Reiseroute für den Kunden erstellen. Dieser Ansatz stellt sicher, dass der Reiseplan von Anfang an mit den Vorlieben und dem Budget des Kunden übereinstimmt und sich mit jeder Iteration verbessert.

### Nutzung von LLM für Re-Ranking und Bewertung

Große Sprachmodelle (LLMs) können zum Re-Ranking und zur Bewertung eingesetzt werden, indem sie die Relevanz und Qualität abgerufener Dokumente oder generierter Antworten bewerten. So funktioniert es:

**Abruf:** Der erste Abrufschritt holt eine Menge Kandidatendokumente oder Antworten basierend auf der Anfrage.

**Re-Ranking:** Das LLM bewertet diese Kandidaten und sortiert sie basierend auf ihrer Relevanz und Qualität neu. Dieser Schritt stellt sicher, dass die relevantesten und qualitativ hochwertigsten Informationen zuerst präsentiert werden.

**Bewertung:** Das LLM weist jedem Kandidaten Bewertungspunkte zu, welche deren Relevanz und Qualität widerspiegeln. Dies hilft bei der Auswahl der besten Antwort oder des besten Dokuments für den Benutzer.

Durch die Nutzung von LLMs für Re-Ranking und Bewertung kann das System genauere und kontextuell relevantere Informationen bereitstellen, was die Gesamtbenutzererfahrung verbessert.

Hier ist ein Beispiel, wie ein Reisebüro ein Großes Sprachmodell (LLM) nutzen könnte, um Reiseziele basierend auf Benutzerpräferenzen in Python neu zu bewerten und zu bewerten:

#### Szenario – Reise nach Präferenzen

Ein Reisebüro möchte dem Kunden basierend auf dessen Vorlieben die besten Reiseziele empfehlen. Das LLM hilft dabei, die Reiseziele neu zu bewerten und zu bewerten, um sicherzustellen, dass die relevantesten Optionen präsentiert werden.

#### Schritte:

1. Sammeln der Benutzerpräferenzen.
2. Abrufen einer Liste potentieller Reiseziele.
3. Nutzung des LLM, um die Reiseziele basierend auf den Benutzerpräferenzen neu zu bewerten und zu bewerten.

So können Sie das vorherige Beispiel aktualisieren, um Azure OpenAI Services zu nutzen:

#### Voraussetzungen

1. Sie benötigen ein Azure-Abonnement.
2. Erstellen Sie eine Azure OpenAI-Ressource und erhalten Sie Ihren API-Schlüssel.

#### Beispiel Python-Code

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Erzeuge eine Eingabeaufforderung für Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Definiere Header und Payload für die Anfrage
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Rufe die Azure OpenAI API auf, um die neu bewerteten und bewerteten Ziele zu erhalten
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extrahiere und gib die Empfehlungen zurück
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

# Beispielverwendung
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

#### Code-Erklärung – Präferenzbucher

1. **Initialisierung**: Die `TravelAgent`-Klasse wird mit einer Liste potentieller Reiseziele initialisiert, die jeweils Attribute wie Name und Beschreibung besitzen.

2. **Empfehlungen abrufen (`get_recommendations`-Methode)**: Diese Methode generiert eine Prompt für den Azure OpenAI-Dienst basierend auf den Benutzerpräferenzen und sendet eine HTTP-POST-Anfrage an die Azure OpenAI API, um neu bewertete und bewertete Reiseziele zu erhalten.

3. **Prompt generieren (`generate_prompt`-Methode)**: Diese Methode konstruiert einen Prompt für Azure OpenAI, der die Benutzerpräferenzen und die Liste der Reiseziele enthält. Der Prompt leitet das Modell an, die Reiseziele anhand der angegebenen Präferenzen neu zu bewerten und zu bewerten.

4. **API-Aufruf**: Die `requests`-Bibliothek wird verwendet, um eine HTTP-POST-Anfrage an den Azure OpenAI API-Endpunkt zu senden. Die Antwort enthält die neu bewerteten und bewerteten Reiseziele.

5. **Beispielanwendung**: Der Reisebüro-Agent sammelt Benutzerpräferenzen (z. B. Interesse an Sightseeing und vielfältiger Kultur) und nutzt den Azure OpenAI Service, um neu bewertete und bewertete Empfehlungen für Reiseziele zu erhalten.

Ersetzen Sie unbedingt `your_azure_openai_api_key` durch Ihren tatsächlichen Azure OpenAI API-Schlüssel und `https://your-endpoint.com/...` durch die tatsächliche Endpunkt-URL Ihrer Azure OpenAI-Bereitstellung.

Durch die Nutzung des LLM für Re-Ranking und Bewertung kann das Reisebüro personalisiertere und relevantere Reiseempfehlungen für Kunden bereitstellen und so deren Gesamterlebnis verbessern.

### RAG: Prompting-Technik vs. Werkzeug

Retrieval-Augmented Generation (RAG) kann sowohl eine Prompting-Technik als auch ein Werkzeug bei der Entwicklung von KI-Agenten sein. Das Verständnis dieses Unterschieds kann Ihnen helfen, RAG in Ihren Projekten wirkungsvoller zu nutzen.

#### RAG als Prompting-Technik

**Was ist das?**

- Als Prompting-Technik beinhaltet RAG das Formulieren spezifischer Anfragen oder Prompts, um relevante Informationen aus einem großen Korpus oder einer Datenbank abzurufen. Diese Informationen werden dann verwendet, um Antworten oder Aktionen zu generieren.

**Wie es funktioniert:**

1. **Prompts formulieren**: Erstellen Sie gut strukturierte Prompts oder Anfragen basierend auf der jeweiligen Aufgabe oder der Benutzereingabe.
2. **Informationen abrufen**: Nutzen Sie die Prompts, um relevante Daten aus einer bestehenden Wissensbasis oder einem Datensatz zu suchen.
3. **Antwort generieren**: Kombinieren Sie die abgerufenen Informationen mit generativen KI-Modellen, um eine umfassende und kohärente Antwort zu erstellen.

**Beispiel im Reisebüro**:

- Benutzereingabe: "Ich möchte Museen in Paris besuchen."
- Prompt: "Finde die besten Museen in Paris."
- Abgerufene Informationen: Details über das Louvre-Museum, Musée d'Orsay usw.
- Generierte Antwort: "Hier sind einige der besten Museen in Paris: Louvre-Museum, Musée d'Orsay und Centre Pompidou."

#### RAG als Werkzeug

**Was ist das?**

- Als Werkzeug ist RAG ein integriertes System, das den Abruf- und Generierungsprozess automatisiert und es Entwicklern erleichtert, komplexe KI-Funktionalitäten ohne manuelles Erstellen von Prompts für jede Anfrage umzusetzen.

**Wie es funktioniert:**

1. **Integration**: Integrieren Sie RAG in die Architektur des KI-Agenten, sodass er den Abruf- und Generierungsprozess automatisch steuert.
2. **Automatisierung**: Das Werkzeug verwaltet den gesamten Prozess, von der Benutzereingabe bis zur finalen Antwort, ohne dass für jeden Schritt explizite Prompts nötig sind.
3. **Effizienz**: Verbessert die Leistung des Agenten, indem der Abruf- und Generierungsprozess optimiert wird, was schnellere und präzisere Antworten ermöglicht.

**Beispiel im Reisebüro**:

- Benutzereingabe: "Ich möchte Museen in Paris besuchen."
- RAG-Werkzeug: Ruft automatisch Informationen über Museen ab und generiert eine Antwort.
- Generierte Antwort: "Hier sind einige der besten Museen in Paris: Louvre-Museum, Musée d'Orsay und Centre Pompidou."

### Vergleich

| Aspekt                 | Prompting-Technik                                       | Werkzeug                                                |
|------------------------|--------------------------------------------------------|---------------------------------------------------------|
| **Manuell vs Automatisch**| Manuelles Formulieren von Prompts für jede Anfrage.    | Automatisierter Prozess für Abruf und Generierung.       |
| **Kontrolle**            | Bietet mehr Kontrolle über den Abrufprozess.          | Optimiert und automatisiert den Abruf- und Generierungsprozess.|
| **Flexibilität**          | Ermöglicht angepasste Prompts je nach Bedarf.          | Effizienter für groß angelegte Implementierungen.        |
| **Komplexität**           | Erfordert das Erstellen und Anpassen von Prompts.      | Einfacher in die Architektur eines KI-Agenten zu integrieren. |

### Praktische Beispiele

**Beispiel Prompting-Technik:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Beispiel Werkzeug:**

```python
class Travel_Agent:
    def __init__(self):
        self.rag_tool = RAGTool()

    def get_museums_in_paris(self):
        user_input = "I want to visit museums in Paris."
        response = self.rag_tool.retrieve_and_generate(user_input)
        return response

travel_agent = Travel_Agent()
museums = travel_agent.get_museums_in_paris()
print("Top Museums in Paris:", museums)
```

### Bewertung der Relevanz

Die Bewertung der Relevanz ist ein entscheidender Aspekt der Leistung von KI-Agenten. Sie stellt sicher, dass die vom Agenten abgerufenen und generierten Informationen angemessen, korrekt und nützlich für den Benutzer sind. Lassen Sie uns betrachten, wie man Relevanz bei KI-Agenten bewertet, einschließlich praktischer Beispiele und Techniken.

#### Schlüsselkonzepte zur Bewertung der Relevanz

1. **Kontextbewusstsein**:
   - Der Agent muss den Kontext der Benutzeranfrage verstehen, um relevante Informationen abzurufen und zu generieren.
   - Beispiel: Wenn ein Benutzer nach den "besten Restaurants in Paris" fragt, sollte der Agent die Vorlieben des Benutzers wie Küchenart und Budget berücksichtigen.

2. **Genauigkeit**:
   - Die vom Agenten bereitgestellten Informationen sollten faktisch korrekt und aktuell sein.
   - Beispiel: Empfehlung derzeit geöffneter Restaurants mit guten Bewertungen statt veralteter oder geschlossener Optionen.

3. **Benutzerabsicht**:
   - Der Agent sollte die Absicht des Benutzers hinter der Anfrage ableiten, um die relevantesten Informationen bereitzustellen.
   - Beispiel: Wenn ein Benutzer nach "preiswerten Hotels" fragt, sollte der Agent erschwingliche Optionen priorisieren.

4. **Feedback-Schleife**:
   - Die kontinuierliche Sammlung und Analyse von Benutzerfeedback hilft dem Agenten, seinen Bewertungsprozess zur Relevanz zu verfeinern.
   - Beispiel: Integration von Benutzerbewertungen und Feedback zu vorherigen Empfehlungen zur Verbesserung künftiger Antworten.

#### Praktische Techniken zur Bewertung der Relevanz

1. **Relevanzbewertung**:
   - Weisen Sie jedem abgerufenen Element eine Relevanzpunktzahl zu, basierend darauf, wie gut es zur Benutzeranfrage und den Vorlieben passt.
   - Beispiel:

     ```python
     def relevance_score(item, query):
         score = 0
         if item['category'] in query['interests']:
             score += 1
         if item['price'] <= query['budget']:
             score += 1
         if item['location'] == query['destination']:
             score += 1
         return score
     ```

2. **Filtern und Rangfolge**:
   - Filtern Sie irrelevante Elemente heraus und ordnen Sie die verbleibenden nach ihren Relevanzbewertungspunkten.
   - Beispiel:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Geben Sie die 10 relevantesten Elemente zurück
     ```

3. **Natürliche Sprachverarbeitung (NLP)**:
   - Verwenden Sie NLP-Techniken, um die Benutzeranfrage zu verstehen und relevante Informationen abzurufen.
   - Beispiel:

     ```python
     def process_query(query):
         # Verwenden Sie NLP, um Schlüsselinformationen aus der Benutzeranfrage zu extrahieren
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integration von Benutzer-Feedback**:
   - Sammeln Sie Feedback zu den bereitgestellten Empfehlungen und verwenden Sie es, um zukünftige Relevanzbewertungen anzupassen.
   - Beispiel:

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### Beispiel: Bewertung der Relevanz im Reisebüro

Hier ein praktisches Beispiel, wie das Reisebüro die Relevanz von Reiseempfehlungen bewerten kann:

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
        ranked_hotels = self.filter_and_rank(hotels, self.user_preferences)
        itinerary = create_itinerary(flights, ranked_hotels, attractions)
        return itinerary

    def filter_and_rank(self, items, query):
        ranked_items = sorted(items, key=lambda item: self.relevance_score(item, query), reverse=True)
        return ranked_items[:10]  # Gibt die 10 relevantesten Elemente zurück

    def relevance_score(self, item, query):
        score = 0
        if item['category'] in query['interests']:
            score += 1
        if item['price'] <= query['budget']:
            score += 1
        if item['location'] == query['destination']:
            score += 1
        return score

    def adjust_based_on_feedback(self, feedback, items):
        for item in items:
            if item['name'] in feedback['liked']:
                item['relevance'] += 1
            if item['name'] in feedback['disliked']:
                item['relevance'] -= 1
        return items

# Beispielverwendung
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
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### Suche mit Absicht

Die Suche mit Absicht bedeutet, den zugrundeliegenden Zweck oder das Ziel einer Benutzeranfrage zu verstehen und zu interpretieren, um die relevantesten und nützlichsten Informationen abzurufen und zu generieren. Dieser Ansatz geht über das bloße Finden von Schlüsselwörtern hinaus und konzentriert sich darauf, die tatsächlichen Bedürfnisse und den Kontext des Benutzers zu erfassen.

#### Schlüsselkonzepte in der Suche mit Absicht

1. **Verstehen der Benutzerabsicht**:
   - Benutzerabsichten lassen sich in drei Haupttypen kategorisieren: informationsorientiert, navigationsorientiert und transaktional.
     - **Informationsorientierte Absicht**: Der Benutzer sucht Informationen über ein Thema (z. B. „Was sind die besten Museen in Paris?“).
     - **Navigationsorientierte Absicht**: Der Benutzer möchte zu einer bestimmten Website oder Seite navigieren (z. B. „Offizielle Webseite Louvre-Museum“).
     - **Transaktionale Absicht**: Der Benutzer möchte eine Transaktion ausführen, wie einen Flug buchen oder einen Kauf tätigen (z. B. „Buche einen Flug nach Paris“).

2. **Kontextbewusstsein**:
   - Die Analyse des Kontexts der Benutzeranfrage hilft, die Absicht genau zu identifizieren. Dies beinhaltet die Berücksichtigung vorheriger Interaktionen, Benutzerpräferenzen und spezifischer Details der aktuellen Anfrage.

3. **Natürliche Sprachverarbeitung (NLP)**:
   - NLP-Techniken werden eingesetzt, um die natürliche Sprache der Benutzeranfragen zu verstehen und zu interpretieren. Dazu gehören Aufgaben wie Entitätenerkennung, Sentimentanalyse und Parsing.

4. **Personalisierung**:
   - Die Personalisierung der Suchergebnisse basierend auf der Historie, den Vorlieben und dem Feedback des Benutzers erhöht die Relevanz der abgerufenen Informationen.

#### Praktisches Beispiel: Suche mit Absicht im Reisebüro

Schauen wir uns Travel Agent als Beispiel an, um zu sehen, wie die Suche mit Absicht umgesetzt werden kann.

1. **Sammeln der Benutzerpräferenzen**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Verstehen der Benutzerabsicht**

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
       # Kombinieren Sie die aktuelle Abfrage mit der Benutzerhistorie, um den Kontext zu verstehen
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
       # Beispiel-Suchlogik für Informationsabsicht
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Beispiel-Suchlogik für Navigationsabsicht
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Beispiel-Suchlogik für Transaktionsabsicht
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Beispiel-Personalisierungslogik
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Gibt die Top 10 personalisierten Ergebnisse zurück
   ```

5. **Beispielhafte Verwendung**

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

## 4. Codeerzeugung als Werkzeug

Codeerzeugende Agenten verwenden KI-Modelle, um Code zu schreiben und auszuführen, komplexe Probleme zu lösen und Aufgaben zu automatisieren.

### Codeerzeugende Agenten

Codeerzeugende Agenten verwenden generative KI-Modelle, um Code zu schreiben und auszuführen. Diese Agenten können komplexe Probleme lösen, Aufgaben automatisieren und wertvolle Einsichten durch das Erzeugen und Ausführen von Code in verschiedenen Programmiersprachen bieten.

#### Praktische Anwendungen

1. **Automatisierte Codeerzeugung**: Generieren von Codeschnipseln für spezielle Aufgaben wie Datenanalyse, Webscraping oder maschinelles Lernen.
2. **SQL als RAG**: Verwenden von SQL-Abfragen zum Abrufen und Verarbeiten von Daten aus Datenbanken.
3. **Problemlösung**: Erstellen und Ausführen von Code zur Lösung spezifischer Probleme, wie der Optimierung von Algorithmen oder der Analyse von Daten.

#### Beispiel: Codeerzeugender Agent für Datenanalyse

Stellen Sie sich vor, Sie entwickeln einen codeerzeugenden Agenten. So könnte er funktionieren:

1. **Aufgabe**: Analysieren eines Datensatzes, um Trends und Muster zu erkennen.
2. **Schritte**:
   - Laden des Datensatzes in ein Datenanalysetool.
   - Generieren von SQL-Abfragen zur Filterung und Aggregation der Daten.
   - Ausführen der Abfragen und Abrufen der Ergebnisse.
   - Verwenden der Ergebnisse zur Erstellung von Visualisierungen und Erkenntnissen.
3. **Benötigte Ressourcen**: Zugriff auf den Datensatz, Datenanalysetools und SQL-Fähigkeiten.
4. **Erfahrung**: Nutzen früherer Analyseergebnisse zur Verbesserung der Genauigkeit und Relevanz zukünftiger Analysen.

### Beispiel: Codeerzeugender Agent für Reisebüro

In diesem Beispiel entwerfen wir einen codeerzeugenden Agenten, Travel Agent, der Benutzer bei der Reiseplanung unterstützt, indem er Code generiert und ausführt. Dieser Agent kann Aufgaben wie das Abrufen von Reiseoptionen, das Filtern von Ergebnissen und das Erstellen eines Reiseplans mit Hilfe generativer KI übernehmen.

#### Überblick über den codeerzeugenden Agenten

1. **Sammeln von Benutzerpräferenzen**: Erfassung von Benutzereingaben wie Reiseziel, Reisedaten, Budget und Interessen.
2. **Generieren von Code zum Abrufen von Daten**: Erzeugt Codeschnipsel zum Abrufen von Informationen über Flüge, Hotels und Attraktionen.
3. **Ausführen des generierten Codes**: Führt den generierten Code aus, um Echtzeitinformationen zu sammeln.
4. **Erstellen des Reiseplans**: Fasst die abgerufenen Daten zu einem personalisierten Reiseplan zusammen.
5. **Anpassung basierend auf Feedback**: Nimmt Benutzerfeedback entgegen und generiert bei Bedarf Code neu, um die Ergebnisse zu verfeinern.

#### Schritt-für-Schritt-Implementierung

1. **Sammeln von Benutzerpräferenzen**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generieren von Code zum Abrufen von Daten**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Beispiel: Code generieren, um Flüge basierend auf Benutzerpräferenzen zu suchen
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Beispiel: Code generieren, um nach Hotels zu suchen
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
       # Führen Sie den generierten Code mit exec aus
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

4. **Erstellen des Reiseplans**

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

5. **Anpassung basierend auf Feedback**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Präferenzen basierend auf Benutzerfeedback anpassen
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Code mit aktualisierten Präferenzen neu generieren und ausführen
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Umweltbewusstsein und Schlussfolgerungen nutzen

Die Nutzung des Schemas der Tabelle kann tatsächlich den Prozess der Abfrageerzeugung verbessern, indem Umweltbewusstsein und Schlussfolgerungen angewendet werden.

Hier ist ein Beispiel, wie dies umgesetzt werden kann:

1. **Schema verstehen**: Das System versteht das Schema der Tabelle und nutzt diese Information, um die Abfrageerzeugung zu begründen.
2. **Anpassung basierend auf Feedback**: Das System passt die Benutzerpräferenzen basierend auf Feedback an und schlussfolgert, welche Felder im Schema aktualisiert werden müssen.
3. **Generieren und Ausführen von Abfragen**: Das System generiert und führt Abfragen aus, um aktualisierte Flug- und Hoteldaten basierend auf den neuen Präferenzen abzurufen.

Hier ist ein aktualisiertes Python-Codebeispiel, das diese Konzepte integriert:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Einstellungen basierend auf Benutzerfeedback anpassen
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Begründung basierend auf Schema, um andere verwandte Einstellungen anzupassen
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Benutzerdefinierte Logik zur Anpassung der Einstellungen basierend auf Schema und Feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Code generieren, um Flugdaten basierend auf aktualisierten Einstellungen abzurufen
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Code generieren, um Hoteldaten basierend auf aktualisierten Einstellungen abzurufen
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Ausführung des Codes simulieren und Sachdaten zurückgeben
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Reiseplan basierend auf Flügen, Hotels und Attraktionen generieren
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Beispielschema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Beispielverwendung
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Code mit aktualisierten Einstellungen neu generieren und ausführen
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Erklärung – Buchung basierend auf Feedback

1. **Schema-Bewusstsein**: Das `schema` Dictionary definiert, wie Präferenzen basierend auf Feedback angepasst werden sollten. Es enthält Felder wie `favorites` und `avoid` mit entsprechenden Anpassungen.
2. **Anpassen der Präferenzen (`adjust_based_on_feedback` Methode)**: Diese Methode passt die Präferenzen entsprechend dem Benutzerfeedback und Schema an.
3. **Umweltbasierte Anpassungen (`adjust_based_on_environment` Methode)**: Diese Methode personalisiert die Anpassungen basierend auf dem Schema und Feedback.
4. **Generieren und Ausführen von Abfragen**: Das System erzeugt Code zur Aktualisierung der Flug- und Hoteldaten basierend auf den angepassten Präferenzen und simuliert die Ausführung dieser Abfragen.
5. **Erstellen des Reiseplans**: Das System erstellt einen aktualisierten Reiseplan basierend auf den neuen Flug-, Hotel- und Attraktionsdaten.

Indem das System umweltbewusst gemacht wird und auf dem Schema basiert schlussfolgert, kann es genauere und relevantere Abfragen generieren, was zu besseren Reiseempfehlungen und einer personalisierteren Benutzererfahrung führt.

### Verwendung von SQL als Retrieval-Augmented Generation (RAG) Technik

SQL (Structured Query Language) ist ein mächtiges Werkzeug für die Interaktion mit Datenbanken. Wenn SQL als Bestandteil eines Retrieval-Augmented Generation (RAG) Ansatzes verwendet wird, kann es relevante Daten aus Datenbanken abrufen, um Antworten oder Aktionen in KI-Agenten zu informieren und zu generieren. Lassen Sie uns erkunden, wie SQL als RAG-Technik im Kontext von Travel Agent verwendet werden kann.

#### Schlüsselkonzepte

1. **Datenbankinteraktion**:
   - SQL wird verwendet, um Datenbanken abzufragen, relevante Informationen abzurufen und Daten zu manipulieren.
   - Beispiel: Abrufen von Flugdaten, Hotelinformationen und Attraktionen aus einer Reisedatenbank.

2. **Integration mit RAG**:
   - SQL-Abfragen werden basierend auf Benutzereingaben und Präferenzen generiert.
   - Die abgerufenen Daten werden genutzt, um personalisierte Empfehlungen oder Aktionen zu generieren.

3. **Dynamische Abfragegenerierung**:
   - Der KI-Agent generiert dynamische SQL-Abfragen basierend auf Kontext und Benutzerbedürfnissen.
   - Beispiel: Anpassen von SQL-Abfragen zur Filterung von Ergebnissen basierend auf Budget, Daten und Interessen.

#### Anwendungen

- **Automatisierte Codeerzeugung**: Generieren von Codeschnipseln für spezifische Aufgaben.
- **SQL als RAG**: Verwenden von SQL-Abfragen zur Datenmanipulation.
- **Problemlösung**: Erstellen und Ausführen von Code zur Problemlösung.

**Beispiel**:
Ein Datenanalyse-Agent:

1. **Aufgabe**: Analysieren eines Datensatzes zum Finden von Trends.
2. **Schritte**:
   - Laden des Datensatzes.
   - Generieren von SQL-Abfragen zur Filterung der Daten.
   - Ausführen der Abfragen und Abrufen der Ergebnisse.
   - Generieren von Visualisierungen und Erkennissen.
3. **Ressourcen**: Zugriff auf Datensatz, SQL-Fähigkeiten.
4. **Erfahrung**: Nutzen von früheren Ergebnissen zur Verbesserung zukünftiger Analysen.

#### Praktisches Beispiel: Verwendung von SQL in Travel Agent

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

1. **Flug-Abfrage**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Hotel-Abfrage**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Attraktions-Abfrage**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Durch die Nutzung von SQL als Teil der Retrieval-Augmented Generation (RAG) Technik können KI-Agenten wie Travel Agent dynamisch relevante Daten abrufen und nutzen, um präzise und personalisierte Empfehlungen zu geben.

### Beispiel für Metakognition

Um eine Implementierung von Metakognition zu demonstrieren, erstellen wir einen einfachen Agenten, der *über seinen Entscheidungsprozess nachdenkt*, während er ein Problem löst. Für dieses Beispiel bauen wir ein System, bei dem ein Agent versucht, die Wahl eines Hotels zu optimieren, aber anschließend seine eigene Entscheidungsfindung bewertet und seine Strategie anpasst, wenn er Fehler oder suboptimale Entscheidungen trifft.

Wir simulieren dies anhand eines einfachen Beispiels, bei dem der Agent Hotels basierend auf einer Kombination aus Preis und Qualität auswählt, aber seine Entscheidungen „reflektiert“ und entsprechend anpasst.

#### Wie dies Metakognition veranschaulicht:

1. **Erste Entscheidung**: Der Agent wählt das günstigste Hotel, ohne die Qualitätsauswirkung zu verstehen.
2. **Reflexion und Bewertung**: Nach der ersten Auswahl prüft der Agent anhand von Benutzerfeedback, ob das Hotel eine „schlechte“ Wahl war. Wenn die Qualität zu niedrig ist, reflektiert er über seine Entscheidungsfindung.
3. **Anpassung der Strategie**: Der Agent passt seine Strategie basierend auf der Reflexion an und wechselt von „günstigstes“ zu „höchste_Qualität“, wodurch er seine Entscheidungsfindung in zukünftigen Iterationen verbessert.

Hier ein Beispiel:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Speichert die zuvor gewählten Hotels
        self.corrected_choices = []  # Speichert die korrigierten Auswahlmöglichkeiten
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Verfügbare Strategien

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
        # Nehmen wir an, wir haben einige Benutzerfeedbacks, die uns sagen, ob die letzte Wahl gut war oder nicht
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Strategie anpassen, wenn die vorherige Wahl unzufriedenstellend war
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

# Simuliert eine Liste von Hotels (Preis und Qualität)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Erstellt einen Agenten
agent = HotelRecommendationAgent()

# Schritt 1: Der Agent empfiehlt ein Hotel anhand der „günstigsten“ Strategie
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Schritt 2: Der Agent reflektiert die Wahl und passt die Strategie bei Bedarf an
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Schritt 3: Der Agent empfiehlt erneut, diesmal mit der angepassten Strategie
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Metakognitive Fähigkeiten des Agenten

Entscheidend ist hier die Fähigkeit des Agenten:
- Seine vorherigen Entscheidungen und den Entscheidungsprozess zu bewerten.
- Seine Strategie basierend auf dieser Reflexion anzupassen, also Metakognition in Aktion.

Dies ist eine einfache Form von Metakognition, bei der das System seinen Denkprozess basierend auf internem Feedback anpassen kann.

### Fazit

Metakognition ist ein mächtiges Werkzeug, das die Fähigkeiten von KI-Agenten erheblich verbessern kann. Durch die Integration metakognitiver Prozesse können Sie Agenten entwerfen, die intelligenter, anpassungsfähiger und effizienter sind. Nutzen Sie die zusätzlichen Ressourcen, um die faszinierende Welt der Metakognition in KI-Agenten weiter zu erkunden.

### Haben Sie weitere Fragen zum Metakognitions-Designmuster?

Treten Sie dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um sich mit anderen Lernenden auszutauschen, an Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten zu stellen.

## Vorherige Lektion

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Nächste Lektion

[KI-Agenten in der Produktion](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->