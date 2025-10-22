<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e40fe956ff79462a02a17080b125041",
  "translation_date": "2025-08-30T13:18:14+00:00",
  "source_file": "01-intro-to-ai-agents/README.md",
  "language_code": "de"
}
-->
[![Einführung in KI-Agenten](../../../translated_images/lesson-1-thumbnail.d21b2c34b32d35bbc7f1b4a40a81b031970b6076b4e0c59fb006cf818cac5d4a.de.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

# Einführung in KI-Agenten und Anwendungsfälle

Willkommen zum Kurs "KI-Agenten für Einsteiger"! Dieser Kurs vermittelt grundlegendes Wissen und praktische Beispiele zum Aufbau von KI-Agenten.

Treten Sie der Community bei, um andere Lernende und Entwickler von KI-Agenten zu treffen und alle Fragen zu diesem Kurs zu stellen.

Um mit diesem Kurs zu beginnen, verschaffen wir uns zunächst ein besseres Verständnis darüber, was KI-Agenten sind und wie wir sie in den Anwendungen und Workflows, die wir erstellen, nutzen können.

## Einführung

Diese Lektion behandelt:

- Was sind KI-Agenten und welche verschiedenen Typen gibt es?
- Für welche Anwendungsfälle eignen sich KI-Agenten am besten und wie können sie uns helfen?
- Was sind einige der grundlegenden Bausteine beim Entwerfen agentenbasierter Lösungen?

## Lernziele
Nach Abschluss dieser Lektion sollten Sie in der Lage sein:

- Die Konzepte von KI-Agenten zu verstehen und zu wissen, wie sie sich von anderen KI-Lösungen unterscheiden.
- KI-Agenten effizient einzusetzen.
- Agentenbasierte Lösungen produktiv für Nutzer und Kunden zu gestalten.

## Definition von KI-Agenten und Typen von KI-Agenten

### Was sind KI-Agenten?

KI-Agenten sind **Systeme**, die es **großen Sprachmodellen (LLMs)** ermöglichen, **Aktionen auszuführen**, indem sie deren Fähigkeiten erweitern und ihnen **Zugriff auf Werkzeuge** und **Wissen** geben.

Lassen Sie uns diese Definition in kleinere Teile zerlegen:

- **System** - Es ist wichtig, Agenten nicht nur als einzelne Komponente zu betrachten, sondern als ein System aus vielen Komponenten. Auf der grundlegenden Ebene bestehen die Komponenten eines KI-Agenten aus:
  - **Umgebung** - Der definierte Raum, in dem der KI-Agent operiert. Zum Beispiel könnte bei einem Reisebuchungs-Agenten die Umgebung das Buchungssystem sein, das der Agent nutzt, um Aufgaben zu erledigen.
  - **Sensoren** - Umgebungen enthalten Informationen und geben Rückmeldungen. KI-Agenten nutzen Sensoren, um diese Informationen über den aktuellen Zustand der Umgebung zu sammeln und zu interpretieren. Im Beispiel des Reisebuchungs-Agenten könnte das Buchungssystem Informationen wie Hotelverfügbarkeit oder Flugpreise bereitstellen.
  - **Aktoren** - Sobald der KI-Agent den aktuellen Zustand der Umgebung erfasst hat, bestimmt er für die aktuelle Aufgabe, welche Aktion ausgeführt werden soll, um die Umgebung zu verändern. Für den Reisebuchungs-Agenten könnte dies bedeuten, ein verfügbares Zimmer für den Nutzer zu buchen.

![Was sind KI-Agenten?](../../../translated_images/what-are-ai-agents.1ec8c4d548af601a3a78c6c02e5c355d19c06a4a74fe93e3609a1d08e8c15689.de.png)

**Große Sprachmodelle** - Das Konzept von Agenten existierte bereits vor der Entwicklung von LLMs. Der Vorteil beim Aufbau von KI-Agenten mit LLMs liegt in ihrer Fähigkeit, menschliche Sprache und Daten zu interpretieren. Diese Fähigkeit ermöglicht es LLMs, Umgebungsinformationen zu verstehen und einen Plan zur Veränderung der Umgebung zu erstellen.

**Aktionen ausführen** - Außerhalb von KI-Agenten-Systemen sind LLMs auf Situationen beschränkt, in denen die Aktion darin besteht, Inhalte oder Informationen basierend auf einer Benutzereingabe zu generieren. Innerhalb von KI-Agenten-Systemen können LLMs Aufgaben erledigen, indem sie die Anfrage des Nutzers interpretieren und Werkzeuge nutzen, die in ihrer Umgebung verfügbar sind.

**Zugriff auf Werkzeuge** - Welche Werkzeuge dem LLM zur Verfügung stehen, wird durch 1) die Umgebung, in der es operiert, und 2) den Entwickler des KI-Agenten definiert. Im Beispiel des Reisebuchungs-Agenten sind die Werkzeuge des Agenten durch die im Buchungssystem verfügbaren Operationen begrenzt, und/oder der Entwickler kann den Zugriff des Agenten auf bestimmte Werkzeuge wie Flüge einschränken.

**Gedächtnis + Wissen** - Gedächtnis kann kurzfristig im Kontext des Gesprächs zwischen dem Nutzer und dem Agenten sein. Langfristig, außerhalb der Informationen, die von der Umgebung bereitgestellt werden, können KI-Agenten auch Wissen aus anderen Systemen, Diensten, Werkzeugen und sogar anderen Agenten abrufen. Im Beispiel des Reisebuchungs-Agenten könnte dieses Wissen Informationen über die Reisevorlieben des Nutzers aus einer Kundendatenbank umfassen.

### Die verschiedenen Typen von Agenten

Nachdem wir nun eine allgemeine Definition von KI-Agenten haben, schauen wir uns einige spezifische Agententypen an und wie sie auf einen Reisebuchungs-Agenten angewendet werden könnten.

| **Agententyp**                | **Beschreibung**                                                                                                                       | **Beispiel**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Einfache Reflex-Agenten**   | Führen sofortige Aktionen basierend auf vordefinierten Regeln aus.                                                                     | Der Reiseagent interpretiert den Kontext einer E-Mail und leitet Reisebeschwerden an den Kundenservice weiter.                                                                                                                 |
| **Modellbasierte Reflex-Agenten** | Führen Aktionen basierend auf einem Modell der Welt und Änderungen an diesem Modell aus.                                              | Der Reiseagent priorisiert Routen mit signifikanten Preisänderungen basierend auf historische Preisdaten.                                                                                                                      |
| **Zielbasierte Agenten**      | Erstellen Pläne, um spezifische Ziele zu erreichen, indem sie das Ziel interpretieren und die notwendigen Aktionen bestimmen.           | Der Reiseagent bucht eine Reise, indem er die notwendigen Reisevorkehrungen (Auto, öffentliche Verkehrsmittel, Flüge) vom aktuellen Standort bis zum Zielort ermittelt.                                                         |
| **Nutzenbasierte Agenten**    | Berücksichtigen Präferenzen und wägen numerisch Abwägungen ab, um zu bestimmen, wie Ziele erreicht werden können.                      | Der Reiseagent maximiert den Nutzen, indem er Bequemlichkeit und Kosten bei der Buchung abwägt.                                                                                                                                |
| **Lernende Agenten**          | Verbessern sich im Laufe der Zeit, indem sie auf Feedback reagieren und ihre Aktionen entsprechend anpassen.                           | Der Reiseagent verbessert sich, indem er Kundenfeedback aus Nach-Reise-Umfragen nutzt, um zukünftige Buchungen anzupassen.                                                                                                     |
| **Hierarchische Agenten**     | Bestehen aus mehreren Agenten in einem gestuften System, wobei höherstufige Agenten Aufgaben in Unteraufgaben für untergeordnete Agenten aufteilen. | Der Reiseagent storniert eine Reise, indem er die Aufgabe in Unteraufgaben aufteilt (z. B. spezifische Buchungen stornieren) und diese von untergeordneten Agenten ausführen lässt, die an den übergeordneten Agenten berichten. |
| **Multi-Agenten-Systeme (MAS)** | Agenten erledigen Aufgaben unabhängig, entweder kooperativ oder konkurrierend.                                                        | Kooperativ: Mehrere Agenten buchen spezifische Reisedienstleistungen wie Hotels, Flüge und Unterhaltung. Konkurrenz: Mehrere Agenten verwalten und konkurrieren um einen gemeinsamen Hotelbuchungskalender, um Kunden im Hotel unterzubringen. |

## Wann sollten KI-Agenten eingesetzt werden?

Im vorherigen Abschnitt haben wir das Beispiel des Reiseagenten verwendet, um zu erklären, wie die verschiedenen Agententypen in unterschiedlichen Szenarien der Reisebuchung eingesetzt werden können. Wir werden dieses Beispiel im gesamten Kurs weiter verwenden.

Schauen wir uns die Arten von Anwendungsfällen an, für die KI-Agenten am besten geeignet sind:

![Wann sollten KI-Agenten eingesetzt werden?](../../../translated_images/when-to-use-ai-agents.54becb3bed74a479f5caca9c951132ce81d482a6704bcd22e5a600dbabc9434e.de.png)

- **Offene Probleme** - Ermöglichen es dem LLM, die notwendigen Schritte zur Erledigung einer Aufgabe zu bestimmen, da diese nicht immer in einen Workflow fest einprogrammiert werden können.
- **Mehrstufige Prozesse** - Aufgaben, die ein gewisses Maß an Komplexität erfordern, bei denen der KI-Agent Werkzeuge oder Informationen über mehrere Schritte hinweg nutzen muss, anstatt nur einmalige Abrufe durchzuführen.
- **Verbesserung im Laufe der Zeit** - Aufgaben, bei denen der Agent sich im Laufe der Zeit verbessern kann, indem er Feedback entweder aus seiner Umgebung oder von Nutzern erhält, um einen besseren Nutzen zu bieten.

Weitere Überlegungen zur Nutzung von KI-Agenten behandeln wir in der Lektion "Vertrauenswürdige KI-Agenten entwickeln".

## Grundlagen agentenbasierter Lösungen

### Entwicklung von Agenten

Der erste Schritt beim Entwerfen eines KI-Agenten-Systems besteht darin, die Werkzeuge, Aktionen und Verhaltensweisen zu definieren. In diesem Kurs konzentrieren wir uns auf die Nutzung des **Azure AI Agent Service**, um unsere Agenten zu definieren. Dieser bietet Funktionen wie:

- Auswahl offener Modelle wie OpenAI, Mistral und Llama
- Nutzung lizenzierter Daten durch Anbieter wie Tripadvisor
- Verwendung standardisierter OpenAPI 3.0-Werkzeuge

### Agentenbasierte Muster

Die Kommunikation mit LLMs erfolgt über Prompts. Aufgrund der halbautonomen Natur von KI-Agenten ist es nicht immer möglich oder erforderlich, das LLM nach einer Änderung in der Umgebung manuell neu zu prompten. Wir verwenden **agentenbasierte Muster**, die es uns ermöglichen, das LLM über mehrere Schritte hinweg auf skalierbare Weise zu prompten.

Dieser Kurs ist in einige der derzeit populären agentenbasierten Muster unterteilt.

### Agentenbasierte Frameworks

Agentenbasierte Frameworks ermöglichen es Entwicklern, agentenbasierte Muster durch Code zu implementieren. Diese Frameworks bieten Vorlagen, Plugins und Werkzeuge für eine bessere Zusammenarbeit von KI-Agenten. Diese Vorteile ermöglichen eine bessere Beobachtbarkeit und Fehlerbehebung von KI-Agenten-Systemen.

In diesem Kurs werden wir das forschungsorientierte AutoGen-Framework und das produktionsreife Agent-Framework von Semantic Kernel erkunden.

### Noch Fragen zu KI-Agenten?

Treten Sie dem [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) bei, um sich mit anderen Lernenden auszutauschen, Sprechstunden zu besuchen und Ihre Fragen zu KI-Agenten beantwortet zu bekommen.

## Vorherige Lektion

[Kurs-Setup](../00-course-setup/README.md)

## Nächste Lektion

[Erkundung agentenbasierter Frameworks](../02-explore-agentic-frameworks/README.md)

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.