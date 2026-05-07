[![Intro to AI Agents](../../../translated_images/de/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

# Einführung in KI-Agenten und Anwendungsfälle von Agenten

Willkommen zum **KI-Agenten für Anfänger**-Kurs! Dieser Kurs vermittelt Ihnen das grundlegende Wissen — und echten funktionierenden Code — um KI-Agenten von Grund auf zu erstellen.

Kommen Sie im <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> vorbei — hier sind viele Lernende und KI-Entwickler, die gerne Fragen beantworten.

Bevor wir mit dem Bauen beginnen, stellen wir sicher, dass wir tatsächlich verstehen, was ein KI-Agent *ist* und wann es sinnvoll ist, einen zu verwenden.

---

## Einführung

Diese Lektion behandelt:

- Was KI-Agenten sind und welche verschiedenen Typen es gibt
- Für welche Arten von Aufgaben KI-Agenten am besten geeignet sind
- Die grundlegenden Bausteine, die Sie bei der Gestaltung einer agentischen Lösung verwenden

## Lernziele

Am Ende dieser Lektion sollten Sie in der Lage sein:

- Erklären, was ein KI-Agent ist und wie er sich von einer herkömmlichen KI-Lösung unterscheidet
- Wissen, wann man einen KI-Agenten einsetzen sollte (und wann nicht)
- Ein grundlegendes Design einer agentischen Lösung für ein reales Problem skizzieren

---

## Definition von KI-Agenten und Arten von KI-Agenten

### Was sind KI-Agenten?

Hier ist eine einfache Möglichkeit, darüber nachzudenken:

> **KI-Agenten sind Systeme, die es großen Sprachmodellen (LLMs) ermöglichen, tatsächlich *etwas zu tun* — indem sie ihnen Werkzeuge und Wissen geben, um in der Welt zu agieren, und nicht nur auf Eingaben zu reagieren.**

Lassen Sie uns das etwas genauer betrachten:

- **System** — Ein KI-Agent ist nicht nur eine einzelne Sache. Es ist eine Sammlung von Teilen, die zusammenarbeiten. Im Kern hat jeder Agent drei Bestandteile:
  - **Umgebung** — Der Raum, in dem der Agent arbeitet. Für einen Reisebuchungsagenten wäre das die Buchungsplattform selbst.
  - **Sensoren** — Wie der Agent den aktuellen Zustand seiner Umgebung liest. Unser Reiseagent könnte die Hotelverfügbarkeit oder Flugpreise prüfen.
  - **Aktuatoren** — Wie der Agent handelt. Der Reiseagent könnte ein Zimmer buchen, eine Bestätigung senden oder eine Reservierung stornieren.

![What Are AI Agents?](../../../translated_images/de/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Große Sprachmodelle** — Agenten gab es schon vor LLMs, aber LLMs machen moderne Agenten so mächtig. Sie können natürliche Sprache verstehen, über den Kontext nachdenken und eine vage Nutzeranfrage in einen konkreten Aktionsplan umsetzen.

- **Aktionen ausführen** — Ohne ein Agentensystem erzeugt ein LLM nur Text. Innerhalb eines Agentensystems kann das LLM tatsächlich *Schritte ausführen* — eine Datenbank durchsuchen, eine API aufrufen, eine Nachricht senden.

- **Zugriff auf Werkzeuge** — Welche Werkzeuge der Agent verwenden kann, hängt davon ab (1) in welcher Umgebung er läuft und (2) was der Entwickler ihm zur Verfügung stellt. Ein Reiseagent könnte Flüge suchen, aber keine Kundendaten ändern — es kommt darauf an, was Sie verbinden.

- **Speicher + Wissen** — Agenten können Kurzzeitgedächtnis (die aktuelle Unterhaltung) und Langzeitgedächtnis (eine Kundendatenbank, frühere Interaktionen) besitzen. Der Reiseagent könnte sich „erinnern“, dass Sie einen Fensterplatz bevorzugen.

---

### Die verschiedenen Arten von KI-Agenten

Nicht alle Agenten sind gleich aufgebaut. Hier ist eine Übersicht der Haupttypen, anhand eines Reisebuchungsagenten als Beispiel:

| **Agententyp** | **Was er tut** | **Beispiel Reiseagent** |
|---|---|---|
| **Einfache Reflex-Agenten** | Folgen festen Regeln — kein Gedächtnis, keine Planung. | Sieht eine Beschwerde-E-Mail → leitet sie an den Kundendienst weiter. Das war’s. |
| **Modellbasierte Reflex-Agenten** | Haben ein internes Modell der Welt und aktualisieren es bei Veränderungen. | Verfolgt historische Flugpreise und markiert plötzlich teure Strecken. |
| **Zielorientierte Agenten** | Haben ein Ziel vor Augen und finden Schritt für Schritt heraus, wie sie es erreichen. | Bucht eine komplette Reise (Flüge, Auto, Hotel) von Ihrem aktuellen Standort bis zum Ziel. |
| **Nutzwertorientierte Agenten** | Finden nicht nur *eine* Lösung, sondern die *beste*, indem sie Kompromisse abwägen. | Balanciert Kosten und Bequemlichkeit, um die Reise zu finden, die am besten zu Ihren Präferenzen passt. |
| **Lernende Agenten** | Werden durch Feedback im Laufe der Zeit besser. | Passt zukünftige Buchungsempfehlungen basierend auf Umfrageergebnissen nach der Reise an. |
| **Hierarchische Agenten** | Ein übergeordneter Agent unterteilt Arbeit in Teilaufgaben und delegiert an untergeordnete Agenten. | Eine "Reise stornieren"-Anfrage wird aufgeteilt in: Flug stornieren, Hotel stornieren, Mietwagen stornieren — jeweils von einem Unteragenten erledigt. |
| **Multi-Agenten-Systeme (MAS)** | Mehrere unabhängige Agenten arbeiten zusammen (oder konkurrieren). | Kooperativ: einzelne Agenten kümmern sich um Hotels, Flüge und Unterhaltung. Wettbewerbsorientiert: mehrere Agenten konkurrieren darum, Hotelzimmer zum besten Preis zu füllen. |

---

## Wann KI-Agenten einsetzen

Nur weil Sie *können* einen KI-Agenten einsetzen, heißt das nicht, dass Sie es immer *sollten*. Hier sind Situationen, in denen Agenten wirklich glänzen:

![When to use AI Agents?](../../../translated_images/de/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Offene Probleme** — Wenn die Schritte zur Lösung eines Problems nicht vorprogrammiert werden können. Das LLM soll den Lösungsweg dynamisch finden.
- **Mehrstufige Prozesse** — Aufgaben, die den Einsatz von Werkzeugen über mehrere Schritte erfordern, nicht nur eine einzelne Abfrage oder Generierung.
- **Verbesserung im Laufe der Zeit** — Wenn das System durch Nutzerfeedback oder Umweltsignale schlauer werden soll.

Wir werden später im Kurs in der Lektion **Vertrauenswürdige KI-Agenten aufbauen** noch genauer darauf eingehen, wann (und wann *nicht*) man KI-Agenten einsetzen sollte.

---

## Grundlagen agentischer Lösungen

### Agent-Entwicklung

Das Erste, was Sie beim Bau eines Agenten tun, ist zu definieren, *was er tun kann* — seine Werkzeuge, Aktionen und Verhaltensweisen.

In diesem Kurs verwenden wir den **Azure AI Agent Service** als unsere Hauptplattform. Er unterstützt:

- Offene Modelle wie OpenAI, Mistral und Llama
- Lizenzierte Daten von Anbietern wie Tripadvisor
- Standardisierte OpenAPI 3.0 Werkzeugdefinitionen

### Agentische Muster

Sie kommunizieren mit LLMs über Prompts. Bei Agenten können Sie nicht immer jeden Prompt manuell erstellen — der Agent muss über viele Schritte hinweg handeln. Hier kommen **Agentische Muster** ins Spiel. Das sind wiederverwendbare Strategien zum Prompten und Orchestrieren von LLMs auf skalierbare und verlässliche Weise.

Dieser Kurs ist um die gebräuchlichsten und nützlichsten agentischen Muster herum strukturiert.

### Agentische Frameworks

Agentische Frameworks geben Entwicklern vorgefertigte Vorlagen, Werkzeuge und Infrastruktur zum Erstellen von Agenten. Sie erleichtern es:

- Werkzeuge und Fähigkeiten zu verknüpfen
- Zu beobachten, was der Agent tut (und Fehler zu beheben)
- Über mehrere Agenten hinweg zusammenzuarbeiten

In diesem Kurs konzentrieren wir uns auf das **Microsoft Agent Framework (MAF)** zum Erstellen von produktionsreifen Agenten.

---

## Codebeispiele

Bereit, es in Aktion zu sehen? Hier sind die Codebeispiele für diese Lektion:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Fragen?

Treten Sie dem [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) bei, um sich mit anderen Lernenden zu verbinden, an Sprechstunden teilzunehmen und Antworten auf Ihre Fragen zu KI-Agenten von der Community zu erhalten.

---

## Vorherige Lektion

[Kurseinrichtung](../00-course-setup/README.md)

## Nächste Lektion

[Erkundung agentischer Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache ist als maßgebliche Quelle anzusehen. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->