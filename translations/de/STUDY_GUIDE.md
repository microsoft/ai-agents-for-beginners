# KI-Agenten für Einsteiger – Studienführer & Kurszusammenfassung

Dieser Leitfaden bietet eine Zusammenfassung des Kurses "KI-Agenten für Einsteiger" und erklärt wichtige Konzepte, Frameworks und Designmuster für den Aufbau von KI-Agenten.

## 1. Einführung in KI-Agenten

**Was sind KI-Agenten?**  
KI-Agenten sind Systeme, die die Fähigkeiten von Large Language Models (LLMs) erweitern, indem sie ihnen Zugriff auf **Werkzeuge**, **Wissen** und **Speicher** geben. Anders als ein Standard-LLM-Chatbot, der nur Text basierend auf Trainingsdaten generiert, kann ein KI-Agent:  
- **Seine Umgebung wahrnehmen** (über Sensoren oder Eingaben).  
- **Überlegen**, wie ein Problem gelöst wird.  
- **Handeln**, um die Umgebung zu verändern (über Aktuatoren oder Werkzeuga usführung).

**Hauptkomponenten eines Agenten:**  
- **Umgebung**: Der Raum, in dem der Agent agiert (z.B. ein Buchungssystem).  
- **Sensoren**: Mechanismen zum Sammeln von Informationen (z.B. das Auslesen einer API).  
- **Aktuatoren**: Mechanismen zur Durchführung von Aktionen (z.B. das Versenden einer E-Mail).  
- **Gehirn (LLM)**: Die Denkmaschine, die plant und entscheidet, welche Aktionen ausgeführt werden.

## 2. Agentische Frameworks

Der Kurs behandelt drei Haupt-Frameworks für den Aufbau von Agenten:

| Framework | Schwerpunkt | Am besten geeignet für |
|-----------|-------------|-----------------------|
| **Semantic Kernel** | Produktionsreifes SDK für .NET/Python | Unternehmensanwendungen, Integration von KI mit bestehendem Code. |
| **AutoGen** | Zusammenarbeit mehrerer Agenten | Komplexe Szenarien, die mehrere spezialisierte Agenten erfordern, die miteinander kommunizieren. |
| **Azure AI Agent Service** | Verwalteter Cloud-Dienst | Sichere, skalierbare Bereitstellung mit integrierter Zustandsverwaltung. |

## 3. Agentische Designmuster

Designmuster helfen dabei, die Funktionsweise von Agenten zu strukturieren, um Probleme zuverlässig zu lösen.

### **Werkzeug-Nutzungsmuster** (Lektion 4)  
Dieses Muster ermöglicht es Agenten, mit der Außenwelt zu interagieren.  
- **Konzept**: Dem Agenten wird ein "Schema" (eine Liste verfügbarer Funktionen und deren Parameter) bereitgestellt. Das LLM entscheidet, *welches* Werkzeug mit *welchen* Argumenten basierend auf der Benutzeranfrage aufgerufen wird.  
- **Ablauf**: Benutzeranfrage -> LLM -> **Werkzeugwahl** -> **Werkzeugausführung** -> LLM (mit Werkzeugausgabe) -> Finale Antwort.  
- **Anwendungsfälle**: Echtzeitdaten abrufen (Wetter, Aktienkurse), Berechnungen durchführen, Code ausführen.

### **Planungsmuster** (Lektion 7)  
Dieses Muster ermöglicht es Agenten, komplexe mehrstufige Aufgaben zu lösen.  
- **Konzept**: Der Agent unterteilt ein übergeordnetes Ziel in eine Abfolge kleinerer Teilaufgaben.  
- **Ansätze**:  
  - **Aufgabenzerlegung**: „Reise planen“ in „Flug buchen“, „Hotel buchen“, „Auto mieten“ aufteilen.  
  - **Iterative Planung**: Den Plan basierend auf den Ergebnissen vorheriger Schritte neu bewerten (z.B. wenn der Flug voll ist, ein anderes Datum wählen).  
- **Umsetzung**: Oft beinhaltet dies einen "Planer"-Agenten, der einen strukturierten Plan (z.B. JSON) erzeugt, der dann von anderen Agenten ausgeführt wird.

## 4. Gestaltungsprinzipien

Bei der Gestaltung von Agenten sind drei Dimensionen zu berücksichtigen:  
- **Raum**: Agenten sollten Menschen und Wissen verbinden, zugänglich, aber unaufdringlich sein.  
- **Zeit**: Agenten sollten aus der *Vergangenheit* lernen, relevante Impulse in der *Gegenwart* geben und sich für die *Zukunft* anpassen.  
- **Kern**: Unsicherheit akzeptieren, aber Vertrauen durch Transparenz und Benutzerkontrolle schaffen.

## 5. Zusammenfassung der wichtigsten Lektionen

- **Lektion 1**: Agenten sind Systeme, nicht nur Modelle. Sie nehmen wahr, denken nach und handeln.  
- **Lektion 2**: Frameworks wie Semantic Kernel und AutoGen abstrahieren die Komplexität von Werkzeugaufrufen und Zustandsverwaltung.  
- **Lektion 3**: Entwurf mit Blick auf Transparenz und Benutzerkontrolle.  
- **Lektion 4**: Werkzeuge sind die „Hände“ des Agenten. Die Schema-Definition ist entscheidend dafür, dass das LLM versteht, wie diese genutzt werden.  
- **Lektion 7**: Planung ist die „Exekutivfunktion“ des Agenten, die es ermöglicht, komplexe Abläufe zu bewältigen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache ist als verbindliche Quelle anzusehen. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->