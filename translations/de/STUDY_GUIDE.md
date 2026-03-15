# KI-Agenten für Einsteiger – Studienleitfaden & Kurszusammenfassung

Dieser Leitfaden bietet eine Zusammenfassung des Kurses „KI-Agenten für Einsteiger“ und erklärt zentrale Konzepte, Frameworks und Entwurfsmuster zum Aufbau von KI-Agenten.

## 1. Einführung in KI-Agenten

**Was sind KI-Agenten?**  
KI-Agenten sind Systeme, die die Fähigkeiten von Large Language Models (LLMs) erweitern, indem sie ihnen Zugriff auf **Werkzeuge**, **Wissen** und **Gedächtnis** geben. Im Gegensatz zu einem Standard-LLM-Chatbot, der nur Text basierend auf Trainingsdaten generiert, kann ein KI-Agent:  
- Seine Umgebung **wahrnehmen** (über Sensoren oder Eingaben).  
- **Überlegen**, wie ein Problem zu lösen ist.  
- **Handeln**, um die Umgebung zu verändern (über Aktuatoren oder Werkzeugausführung).  

**Hauptkomponenten eines Agenten:**  
- **Umgebung**: Der Raum, in dem der Agent agiert (z. B. ein Buchungssystem).  
- **Sensoren**: Mechanismen zur Informationssammlung (z. B. das Auslesen einer API).  
- **Aktuatoren**: Mechanismen zur Ausführung von Aktionen (z. B. das Versenden einer E-Mail).  
- **Gehirn (LLM)**: Die Denkmaschine, die plant und entscheidet, welche Aktionen ausgeführt werden.  

## 2. Agenten-Frameworks

Der Kurs verwendet das **Microsoft Agent Framework (MAF)** mit dem **Azure AI Foundry Agent Service V2** zum Erstellen von Agenten:

| Komponente | Fokus | Am besten geeignet für |
|------------|-------|-----------------------|
| **Microsoft Agent Framework** | Einheitliches Python/C# SDK für Agenten, Werkzeuge und Workflows | Erstellen von Agenten mit Werkzeugen, Multi-Agenten-Workflows und Produktionsmustern. |
| **Azure AI Foundry Agent Service** | Verwalteter Cloud-Laufzeitdienst | Sichere, skalierbare Bereitstellung mit eingebautem Zustandsmanagement, Beobachtbarkeit und Vertrauen. |

## 3. Agenten-Entwurfsmuster

Entwurfsmuster helfen dabei, die Funktionsweise von Agenten so zu strukturieren, dass Probleme zuverlässig gelöst werden.

### **Werkzeug-Nutzungsmuster** (Lektion 4)  
Dieses Muster ermöglicht es Agenten, mit der Außenwelt zu interagieren.  
- **Konzept**: Dem Agenten wird ein „Schema“ (eine Liste verfügbarer Funktionen und deren Parameter) bereitgestellt. Das LLM entscheidet, *welches* Werkzeug mit *welchen* Argumenten basierend auf der Benutzeranfrage aufgerufen wird.  
- **Ablauf**: Benutzeranfrage -> LLM -> **Werkzeugauswahl** -> **Werkzeugausführung** -> LLM (mit Werkzeugausgabe) -> Endantwort.  
- **Anwendungsfälle**: Abrufen von Echtzeitdaten (Wetter, Aktienkurse), Berechnungen durchführen, Code ausführen.

### **Planungsmuster** (Lektion 7)  
Dieses Muster ermöglicht es Agenten, komplexe Aufgaben mit mehreren Schritten zu lösen.  
- **Konzept**: Der Agent zerlegt ein übergeordnetes Ziel in eine Folge kleinerer Teilaufgaben.  
- **Ansätze**:  
  - **Aufgabenzergliederung**: „Reise planen“ wird aufgeteilt in „Flug buchen“, „Hotel buchen“, „Auto mieten“.  
  - **Iterative Planung**: Neubewertung des Plans basierend auf den Ergebnissen vorheriger Schritte (z. B. bei ausgebuchtem Flug einen anderen Termin wählen).  
- **Umsetzung**: Häufig gibt es einen „Planer“-Agenten, der einen strukturierten Plan (z. B. JSON) erstellt, der dann von anderen Agenten ausgeführt wird.

## 4. Gestaltungsprinzipien

Beim Design von Agenten sind drei Dimensionen zu berücksichtigen:  
- **Raum**: Agenten sollten Menschen und Wissen verbinden, zugänglich aber unaufdringlich sein.  
- **Zeit**: Agenten sollen aus der *Vergangenheit* lernen, im *Jetzt* relevante Anstöße geben und sich für die *Zukunft* anpassen.  
- **Kern**: Unsicherheit akzeptieren, aber Vertrauen durch Transparenz und Benutzerkontrolle schaffen.

## 5. Zusammenfassung der wichtigsten Lektionen

- **Lektion 1**: Agenten sind Systeme, nicht nur Modelle. Sie nehmen wahr, denken nach und handeln.  
- **Lektion 2**: Das Microsoft Agent Framework abstrahiert die Komplexität von Werkzeugaufrufen und Zustandsmanagement.  
- **Lektion 3**: Design mit Fokus auf Transparenz und Benutzerkontrolle.  
- **Lektion 4**: Werkzeuge sind die „Hände“ des Agenten. Schemas sind entscheidend, damit das LLM versteht, wie es sie benutzt.  
- **Lektion 7**: Planung ist die „exekutive Funktion“ des Agenten und ermöglicht das Meistern komplexer Workflows.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle anzusehen. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->