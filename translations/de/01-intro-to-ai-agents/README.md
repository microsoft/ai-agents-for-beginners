[![Einführung in KI-Agenten](../../../translated_images/de/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klicken Sie auf das obige Bild, um das Video dieser Lektion anzusehen)_


# Einführung in KI-Agenten und Anwendungsfälle von Agenten

Willkommen zum Kurs "KI-Agenten für Einsteiger"! Dieser Kurs vermittelt grundlegendes Wissen und praxisnahe Beispiele zum Erstellen von KI-Agenten.

Trete der <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord-Community</a> bei, um andere Lernende und KI-Agenten-Entwickler kennenzulernen und Fragen zu diesem Kurs zu stellen.

Um diesen Kurs zu beginnen, starten wir damit, ein besseres Verständnis dafür zu bekommen, was KI-Agenten sind und wie wir sie in den Anwendungen und Workflows, die wir bauen, einsetzen können.

## Introduction

Diese Lektion behandelt:

- Was sind KI-Agenten und welche verschiedenen Agententypen gibt es?
- Für welche Anwendungsfälle eignen sich KI-Agenten am besten und wie können sie uns helfen?
- Was sind einige der grundlegenden Bausteine bei der Gestaltung agentischer Lösungen?

## Learning Goals
Nach Abschluss dieser Lektion sollten Sie in der Lage sein:

- Konzepte von KI-Agenten zu verstehen und wie sie sich von anderen KI-Lösungen unterscheiden.
- KI-Agenten am effizientesten anzuwenden.
- Agentische Lösungen produktiv sowohl für Nutzer als auch für Kunden zu entwerfen.

## Defining AI Agents and Types of AI Agents

### Was sind KI-Agenten?

KI-Agenten sind **Systeme**, die **Große Sprachmodelle(LLMs)** befähigen, **Aktionen auszuführen**, indem sie ihre Fähigkeiten erweitern und den LLMs **Zugriff auf Werkzeuge** und **Wissen** gewähren.

Lassen Sie uns diese Definition in kleinere Teile aufschlüsseln:

- **System** - Es ist wichtig, Agenten nicht nur als eine einzelne Komponente zu betrachten, sondern als ein System aus vielen Komponenten. Auf grundlegender Ebene sind die Komponenten eines KI-Agenten:
  - **Umgebung** - Der definierte Raum, in dem der KI-Agent tätig ist. Zum Beispiel könnte bei einem Reisebuchungs-KI-Agenten die Umgebung das Reisebuchungssystem sein, das der KI-Agent zur Erledigung von Aufgaben nutzt.
  - **Sensoren** - Umgebungen haben Informationen und liefern Rückmeldungen. KI-Agenten verwenden Sensoren, um diese Informationen über den aktuellen Zustand der Umgebung zu sammeln und zu interpretieren. Im Beispiel des Reisebuchungs-Agenten kann das Buchungssystem Informationen wie Hotelverfügbarkeiten oder Flugpreise bereitstellen.
  - **Aktuatoren** - Sobald der KI-Agent den aktuellen Zustand der Umgebung erhalten hat, bestimmt der Agent für die aktuelle Aufgabe, welche Aktion ausgeführt werden soll, um die Umgebung zu verändern. Für den Reisebuchungs-Agenten könnte das beispielsweise das Buchen eines verfügbaren Zimmers für den Benutzer sein.

![Was sind KI-Agenten?](../../../translated_images/de/what-are-ai-agents.1ec8c4d548af601a.webp)

**Große Sprachmodelle** - Das Konzept von Agenten existierte bereits vor der Entstehung von LLMs. Der Vorteil, KI-Agenten mit LLMs zu bauen, liegt in ihrer Fähigkeit, menschliche Sprache und Daten zu interpretieren. Diese Fähigkeit ermöglicht es LLMs, Informationen aus der Umgebung zu interpretieren und einen Plan zu erstellen, um die Umgebung zu verändern.

**Aktionen ausführen** - Außerhalb von KI-Agenten-Systemen sind LLMs auf Situationen beschränkt, in denen die Aktion darin besteht, Inhalte oder Informationen basierend auf einer Benutzereingabe zu erzeugen. Innerhalb von KI-Agenten-Systemen können LLMs Aufgaben erfüllen, indem sie die Anfrage des Benutzers interpretieren und die in ihrer Umgebung verfügbaren Werkzeuge nutzen.

**Zugriff auf Werkzeuge** - Welche Werkzeuge dem LLM zur Verfügung stehen, wird bestimmt durch 1) die Umgebung, in der es operiert, und 2) den Entwickler des KI-Agenten. In unserem Reiseagenten-Beispiel sind die Werkzeuge des Agenten durch die im Buchungssystem verfügbaren Operationen begrenzt, und/oder der Entwickler kann den Werkzeugzugriff des Agenten auf Flüge einschränken.

**Speicher+Wissen** - Der Speicher kann kurzfristig im Kontext der Konversation zwischen dem Benutzer und dem Agenten sein. Langfristig, außerhalb der vom Umfeld bereitgestellten Informationen, können KI-Agenten auch Wissen aus anderen Systemen, Diensten, Werkzeugen und sogar anderen Agenten abrufen. Im Reiseagenten-Beispiel könnten diese Kenntnisse Informationen zu den Reisepräferenzen des Nutzers sein, die in einer Kundendatenbank gespeichert sind.

### Die verschiedenen Agententypen

Nachdem wir eine allgemeine Definition von KI-Agenten haben, schauen wir uns einige spezifische Agententypen an und wie sie auf einen Reisebuchungs-KI-Agenten angewendet würden.

| **Agententyp**                | **Beschreibung**                                                                                                                       | **Beispiel**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Einfache Reflexagenten**      | Führen unmittelbare Aktionen basierend auf vordefinierten Regeln aus.                                                                                  | Der Reiseagent interpretiert den Kontext einer E-Mail und leitet Reisebeschwerden an den Kundenservice weiter.                                                                                                                          |
| **Modellbasierte Reflexagenten** | Führen Aktionen basierend auf einem Modell der Welt und Änderungen dieses Modells aus.                                                              | Der Reiseagent priorisiert Strecken mit erheblichen Preisänderungen basierend auf dem Zugriff auf historische Preisdaten.                                                                                                             |
| **Zielorientierte Agenten**         | Erstellen Pläne zur Erreichung spezifischer Ziele, indem sie das Ziel interpretieren und Aktionen bestimmen, um es zu erreichen.                                  | Der Reiseagent bucht eine Reise, indem er die notwendigen Reisevorkehrungen (Auto, öffentliche Verkehrsmittel, Flüge) vom aktuellen Standort zum Ziel bestimmt.                                                                                |
| **Nutzenbasierte Agenten**      | Berücksichtigen Präferenzen und wägen Kompromisse numerisch ab, um zu bestimmen, wie Ziele erreicht werden.                                               | Der Reiseagent maximiert den Nutzen, indem er Komfort gegenüber Kosten beim Buchen von Reisen abwägt.                                                                                                                                          |
| **Lernende Agenten**           | Verbessern sich im Laufe der Zeit, indem sie auf Feedback reagieren und ihre Aktionen entsprechend anpassen.                                                        | Der Reiseagent verbessert sich durch Nutzung von Kundenfeedback aus Nachreiseumfragen, um zukünftige Buchungen anzupassen.                                                                                                               |
| **Hierarchische Agenten**       | Bestehen aus mehreren Agenten in einem gestuften System, wobei übergeordnete Agenten Aufgaben in Teilaufgaben aufteilen, die von untergeordneten Agenten ausgeführt werden. | Der Reiseagent storniert eine Reise, indem er die Aufgabe in Teilschritte (z. B. Stornierung einzelner Buchungen) aufteilt und untergeordnete Agenten diese ausführen lässt, die dann an den übergeordneten Agenten Bericht erstatten.                                     |
| **Multi-Agenten-Systeme (MAS)** | Agenten erledigen Aufgaben unabhängig, entweder kooperativ oder wettbewerbsorientiert.                                                           | Kooperativ: Mehrere Agenten buchen spezifische Reisedienstleistungen wie Hotels, Flüge und Unterhaltung. Kompetitiv: Mehrere Agenten verwalten und konkurrieren um einen gemeinsamen Hotelbuchungskalender, um Kunden im Hotel unterzubringen. |

## Wann man KI-Agenten einsetzen sollte

Im vorherigen Abschnitt haben wir das Reiseagenten-Anwendungsbeispiel verwendet, um zu erklären, wie die verschiedenen Agententypen in unterschiedlichen Szenarien der Reisebuchung eingesetzt werden können. Wir werden diese Anwendung im Verlauf des Kurses weiter verwenden.

Schauen wir uns die Arten von Anwendungsfällen an, für die KI-Agenten am besten geeignet sind:

![Wann KI-Agenten einsetzen?](../../../translated_images/de/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Offene Probleme** - dem LLM erlauben, die erforderlichen Schritte zur Erledigung einer Aufgabe zu bestimmen, weil diese nicht immer fest in einen Workflow programmiert werden können.
- **Mehrstufige Prozesse** - Aufgaben, die ein Maß an Komplexität erfordern, bei dem der KI-Agent Werkzeuge oder Informationen über mehrere Schritte hinweg anstelle einer einmaligen Abfrage nutzen muss.  
- **Verbesserung über die Zeit** - Aufgaben, bei denen sich der Agent im Laufe der Zeit durch Feedback aus seiner Umgebung oder von Nutzern verbessern kann, um einen besseren Nutzen zu bieten.

Wir behandeln weitere Überlegungen zur Verwendung von KI-Agenten in der Lektion "Vertrauenswürdige KI-Agenten erstellen".

## Basics of Agentic Solutions

### Agent Development

Der erste Schritt bei der Gestaltung eines KI-Agenten-Systems besteht darin, die Werkzeuge, Aktionen und Verhaltensweisen zu definieren. In diesem Kurs konzentrieren wir uns auf die Verwendung des **Azure AI Agent Service**, um unsere Agenten zu definieren. Er bietet Funktionen wie:

- Auswahl offener Modelle wie OpenAI, Mistral und Llama
- Nutzung lizenzierter Daten über Anbieter wie Tripadvisor
- Verwendung standardisierter OpenAPI 3.0-Tools

### Agentic Patterns

Die Kommunikation mit LLMs erfolgt über Prompts. Angesichts der halbautonomen Natur von KI-Agenten ist es nicht immer möglich oder erforderlich, das LLM nach einer Änderung in der Umgebung manuell erneut zu befragen. Wir verwenden **agentische Muster**, die es uns ermöglichen, das LLM über mehrere Schritte auf skalierbarere Weise anzusprechen.

Dieser Kurs ist in einige der derzeit populären agentischen Muster unterteilt.

### Agentic Frameworks

Agentische Frameworks ermöglichen Entwicklern, agentische Muster durch Code zu implementieren. Diese Frameworks bieten Vorlagen, Plugins und Werkzeuge für eine bessere Zusammenarbeit von KI-Agenten. Diese Vorteile schaffen Möglichkeiten für bessere Beobachtbarkeit und Fehlerbehebung von KI-Agentensystemen.

In diesem Kurs werden wir das Microsoft Agent Framework (MAF) zur Erstellung produktionsreifer KI-Agenten erkunden.

## Sample Codes

- Python: [Agenten-Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agenten-Framework](./code_samples/01-dotnet-agent-framework.md)

## Got More Questions about AI Agents?

Treten Sie dem [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Antworten auf Ihre Fragen zu KI-Agenten zu erhalten.

## Previous Lesson

[Kurs-Setup](../00-course-setup/README.md)

## Next Lesson

[Agentische Frameworks erkunden](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Verwendung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->