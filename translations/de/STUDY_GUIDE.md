# KI-Agenten für Einsteiger - Studienführer & Kurszusammenfassung

Dieser Leitfaden bietet eine Zusammenfassung des Kurses „KI-Agenten für Einsteiger“ und erklärt wichtige Konzepte, Frameworks und Entwurfsmuster zum Aufbau von KI-Agenten.

## 1. Einführung in KI-Agenten

**Was sind KI-Agenten?**  
KI-Agenten sind Systeme, die die Fähigkeiten von Large Language Models (LLMs) erweitern, indem sie ihnen Zugang zu **Werkzeugen**, **Wissen** und **Speicher** geben. Im Gegensatz zu einem normalen LLM-Chatbot, der nur Text basierend auf Trainingsdaten generiert, kann ein KI-Agent:  
- Seine Umgebung **wahrnehmen** (über Sensoren oder Eingaben).  
- **Überlegen**, wie ein Problem gelöst werden kann.  
- **Handeln**, um die Umgebung zu verändern (über Aktuatoren oder Werkzeugausführung).

**Wichtige Komponenten eines Agenten:**  
- **Umgebung**: Der Raum, in dem der Agent operiert (z. B. ein Buchungssystem).  
- **Sensoren**: Mechanismen zum Sammeln von Informationen (z. B. das Auslesen einer API).  
- **Aktuatoren**: Mechanismen zum Ausführen von Aktionen (z. B. das Senden einer E-Mail).  
- **Gehirn (LLM)**: Die logische Einheit, die plant und entscheidet, welche Aktionen durchzuführen sind.

## 2. Agenten-Frameworks

Der Kurs verwendet das **Microsoft Agent Framework (MAF)** mit dem **Azure AI Foundry Agent Service V2** zum Erstellen von Agenten:

| Komponente | Fokus | Am besten geeignet für |
|------------|-------|-----------------------|
| **Microsoft Agent Framework** | Einheitliches Python/C# SDK für Agenten, Werkzeuge und Workflows | Aufbau von Agenten mit Werkzeugen, Multi-Agenten-Workflows und Produktionsmustern. |
| **Azure AI Foundry Agent Service** | Verwalteter Cloud-Runtime | Sichere, skalierbare Bereitstellung mit eingebautem Zustandsmanagement, Beobachtbarkeit und Vertrauen. |

## 3. Agenten-Entwurfsmuster

Entwurfsmuster helfen dabei, die Arbeitsweise von Agenten zu strukturieren, um Probleme zuverlässig zu lösen.

### **Werkzeug-Verwendungsmuster** (Lektion 4)  
Dieses Muster ermöglicht es Agenten, mit der Außenwelt zu interagieren.  
- **Konzept**: Dem Agenten wird ein "Schema" bereitgestellt (eine Liste verfügbarer Funktionen und ihrer Parameter). Das LLM entscheidet, *welches* Werkzeug es aufruft und mit *welchen* Argumenten, basierend auf der Nutzeranfrage.  
- **Ablauf**: Nutzeranfrage -> LLM -> **Werkzeug-Auswahl** -> **Werkzeug-Ausführung** -> LLM (mit Werkzeug-Ausgabe) -> Endantwort.  
- **Anwendungsfälle**: Abruf von Echtzeitdaten (Wetter, Aktienkurse), Durchführung von Berechnungen, Ausführung von Code.

### **Planungsmuster** (Lektion 7)  
Dieses Muster ermöglicht Agenten, komplexe, mehrstufige Aufgaben zu lösen.  
- **Konzept**: Der Agent zerlegt ein übergeordnetes Ziel in eine Folge kleinerer Teilaufgaben.  
- **Ansätze**:  
  - **Aufgabenzerlegung**: „Reise planen“ wird in „Flug buchen“, „Hotel buchen“, „Auto mieten“ aufgeteilt.  
  - **Iterative Planung**: Plan wird basierend auf Ausgaben vorheriger Schritte neu bewertet (z. B. wenn der Flug ausgebucht ist, wähle ein anderes Datum).  
- **Implementierung**: Oft beinhaltet dies einen „Planer“-Agenten, der einen strukturierten Plan (z. B. JSON) generiert, der dann von anderen Agenten ausgeführt wird.

## 4. Gestaltungsprinzipien

Beim Entwurf von Agenten sollten drei Dimensionen berücksichtigt werden:  
- **Raum**: Agenten sollten Menschen und Wissen verbinden, zugänglich, aber unaufdringlich sein.  
- **Zeit**: Agenten sollten aus der *Vergangenheit* lernen, relevante Anstöße in der *Gegenwart* geben und sich für die *Zukunft* anpassen.  
- **Kern**: Akzeptiere Unsicherheit, aber baue Vertrauen durch Transparenz und Nutzerkontrolle auf.

## 5. Zusammenfassung der wichtigsten Lektionen

- **Lektion 1**: Agenten sind Systeme, keine bloßen Modelle. Sie nehmen wahr, denken nach und handeln.  
- **Lektion 2**: Das Microsoft Agent Framework abstrahiert die Komplexität von Werkzeugaufrufen und Zustandsmanagement.  
- **Lektion 3**: Gestalte mit Transparenz und Nutzerkontrolle im Blick.  
- **Lektion 4**: Werkzeuge sind die „Hände“ des Agenten. Die Schema-Definition ist entscheidend, damit das LLM versteht, wie sie genutzt werden.  
- **Lektion 7**: Planung ist die „exekutive Funktion“ des Agenten, die ihm ermöglicht, komplexe Arbeitsabläufe anzugehen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->