[![Einführung in KI-Agenten](../../../translated_images/de/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klicke auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

# Einführung in KI-Agenten und Anwendungsfälle von Agenten

Willkommen zum Kurs **KI-Agenten für Anfänger**! Dieser Kurs vermittelt dir das grundlegende Wissen — und echten funktionierenden Code — um von Grund auf KI-Agenten zu bauen.

Sag gern Hallo in der <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — dort tummeln sich Lernende und KI-Entwickler, die gerne Fragen beantworten.

Bevor wir mit dem Bauen beginnen, stellen wir sicher, dass wir wirklich verstehen, was ein KI-Agent *ist* und wann es Sinn macht, einen zu verwenden.

---

## Einführung

Diese Lektion behandelt:

- Was KI-Agenten sind und welche verschiedenen Typen es gibt
- Für welche Aufgaben KI-Agenten am besten geeignet sind
- Die zentralen Bausteine, die du beim Entwerfen einer Agentenlösung verwendest

## Lernziele

Am Ende dieser Lektion solltest du:

- Erklären können, was ein KI-Agent ist und wie er sich von einer regulären KI-Lösung unterscheidet
- Wissen, wann man zu einem KI-Agenten greift (und wann nicht)
- Einen einfachen Entwurf einer agentenbasierten Lösung für ein reales Problem skizzieren können

---

## Definition von KI-Agenten und Arten von KI-Agenten

### Was sind KI-Agenten?

So kannst du dir das einfach vorstellen:

> **KI-Agenten sind Systeme, die es großen Sprachmodellen (LLMs) ermöglichen, *aktiv zu handeln* — indem sie ihnen Werkzeuge und Wissen bereitstellen, um auf die Welt einzuwirken, statt nur Eingaben zu beantworten.**

Schauen wir uns das etwas genauer an:

- **System** — Ein KI-Agent ist nicht nur eine Sache. Es ist eine Sammlung von Teilen, die zusammenarbeiten. Im Kern hat jeder Agent drei Komponenten:
  - **Umgebung** — Der Bereich, in dem der Agent arbeitet. Für einen Reisebuchungsagenten wäre das die Buchungsplattform selbst.
  - **Sensoren** — Wie der Agent den aktuellen Zustand seiner Umgebung liest. Unser Reiseagent könnte die Verfügbarkeit von Hotels oder Flugpreisen prüfen.
  - **Aktuatoren** — Wie der Agent handelt. Der Reiseagent könnte ein Zimmer buchen, eine Bestätigung senden oder eine Reservierung stornieren.

![Was sind KI-Agenten?](../../../translated_images/de/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Große Sprachmodelle (LLMs)** — Agenten gab es auch vor LLMs, aber die heutigen LLMs machen Agenten viel leistungsfähiger. Sie verstehen natürliche Sprache, können Kontext erfassen und eine vage Benutzeranfrage in einen konkreten Handlungsplan umwandeln.

- **Handlungen ausführen** — Ohne Agentensystem generiert ein LLM nur Text. Innerhalb eines Agentensystems kann das LLM tatsächlich *Schritte ausführen* — Datenbanken durchsuchen, APIs anrufen, Nachrichten senden.

- **Zugriff auf Werkzeuge** — Welche Werkzeuge der Agent nutzen kann, hängt ab von (1) der Umgebung, in der er läuft und (2) was der Entwickler ihm zur Verfügung stellt. Ein Reiseagent kann vielleicht Flüge suchen, aber Kundendaten nicht bearbeiten — es kommt darauf an, was du einbindest.

- **Gedächtnis + Wissen** — Agenten können kurzfristiges Gedächtnis haben (das aktuelle Gespräch) und langfristiges Gedächtnis (Kundendatenbank, vergangene Interaktionen). Der Reiseagent könnte sich „merken“, dass du Fensterplätze bevorzugst.

---

### Die verschiedenen Arten von KI-Agenten

Nicht alle Agenten sind gleich aufgebaut. Hier eine Übersicht der Haupttypen, mit einem Reisebuchungsagenten als Beispiel:

| **Agenten-Typ** | **Was er macht** | **Beispiel Reiseagent** |
|---|---|---|
| **Einfache Reflexagenten** | Befolgt fest programmierte Regeln — kein Gedächtnis, keine Planung. | Sieht eine Beschwerde-Mail → leitet sie an den Kundenservice weiter. Mehr nicht. |
| **Modellbasierte Reflexagenten** | Führt ein internes Modell der Welt und aktualisiert es bei Änderungen. | Verfolgt historische Flugpreise und markiert Routen, die plötzlich teuer sind. |
| **Zielorientierte Agenten** | Hat ein definiertes Ziel und findet Schritt für Schritt den Weg dorthin. | Bucht eine komplette Reise (Flug, Auto, Hotel) von deinem aktuellen Standort zum Zielort. |
| **Nutzenbasierte Agenten** | Findet nicht nur *eine* Lösung, sondern die *beste*, indem es Abwägungen trifft. | Balanciert Kosten gegen Bequemlichkeit, um die Reise mit dem besten Ergebnis für deine Präferenzen zu finden. |
| **Lernende Agenten** | Verbessert sich mit der Zeit durch Feedback. | Passt zukünftige Buchungsempfehlungen basierend auf Umfragen nach der Reise an. |
| **Hierarchische Agenten** | Ein Agent auf hoher Ebene teilt Aufgaben in Unteraufgaben und delegiert an niedrigere Agenten. | Eine Anfrage „Reise stornieren“ wird aufgeteilt in: Flug stornieren, Hotel stornieren, Mietwagen stornieren — jede Aufgabe von einem Unter-Agenten erledigt. |
| **Multi-Agenten-Systeme (MAS)** | Mehrere unabhängige Agenten, die zusammenarbeiten (oder konkurrieren). | Kooperation: verschiedene Agenten kümmern sich um Hotels, Flüge und Unterhaltung. Wettbewerb: mehrere Agenten konkurrieren, um Hotelzimmer zum besten Preis zu füllen. |

---

## Wann KI-Agenten einsetzen

Nur weil du *kannst*, heißt das nicht, dass du immer *solltest*. Hier sind die Situationen, in denen Agenten wirklich ihre Stärken ausspielen:

![Wann KI-Agenten einsetzen?](../../../translated_images/de/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Offene Probleme** — Wenn die Schritte zur Problemlösung nicht vorprogrammiert werden können. Du brauchst, dass das LLM den Weg dynamisch findet.
- **Mehrstufige Prozesse** — Aufgaben, die über mehrere Schritte hinweg Werkzeuge nutzen, nicht nur eine einfache Abfrage oder Textgenerierung.
- **Verbesserung über Zeit** — Wenn das System smarter werden soll, basierend auf Nutzerfeedback oder Umweltinformationen.

Später im Kurs in der Lektion **Vertrauenswürdige KI-Agenten bauen** gehen wir noch genauer darauf ein, wann (und wann *nicht*) man KI-Agenten einsetzen sollte.

---

## Grundlagen agentenbasierter Lösungen

### Agentenentwicklung

Das Erste, was du beim Bau eines Agenten machst, ist zu definieren, *was er tun kann* — seine Werkzeuge, Aktionen und Verhaltensweisen.

In diesem Kurs nutzen wir den **Microsoft Foundry Agent Service** als Hauptplattform. Er unterstützt:

- Modelle von Anbietern wie OpenAI, Mistral und Meta (Llama)
- Lizenzierte Daten von Anbietern wie Tripadvisor
- Standardisierte OpenAPI 3.0 Werkzeugdefinitionen

### Agenten-Muster

Du kommunizierst mit LLMs über Prompts. Bei Agenten kannst du nicht immer jeden Prompt per Hand anfertigen — der Agent muss über viele Schritte hinweg handeln. Hier kommen **Agenten-Muster** ins Spiel. Das sind wiederverwendbare Strategien, um LLMs auf skalierbare und verlässliche Weise zu steuern und zu orchestrieren.

Dieser Kurs ist um die gebräuchlichsten und nützlichsten agentenbasierten Muster herum strukturiert.

### Agenten-Frameworks

Agenten-Frameworks bieten Entwicklern fertige Vorlagen, Werkzeuge und Infrastruktur für den Agentenbau. Sie erleichtern:

- Das Einbinden von Werkzeugen und Fähigkeiten
- Das Beobachten, was der Agent gerade macht (und Debugging bei Problemen)
- Die Zusammenarbeit zwischen mehreren Agenten

In diesem Kurs liegt der Fokus auf dem **Microsoft Agent Framework (MAF)** zum Bau produktionsfähiger Agenten.

---

## Code-Beispiele

Bereit, das in Aktion zu sehen? Hier sind die Code-Beispiele zu dieser Lektion:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Fragen?

Tritt dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um dich mit anderen Lernenden zu verbinden, an offenen Sprechstunden teilzunehmen und deine Fragen zu KI-Agenten von der Community beantworten zu lassen.


---

## Schneller Test dieses Agenten (Optional)

Sobald du gelernt hast, Agenten in [Lektion 16](../16-deploying-scalable-agents/README.md) bereitzustellen, kannst du für diesen Kurs eine schnelle Health-Check-Überprüfung nach der Bereitstellung des `TravelAgent` mit dem fertigen Katalog [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) hinzufügen. Siehe [`tests/README.md`](../tests/README.md) für Anweisungen zur Ausführung.

---

## Vorherige Lektion

[Kurseinrichtung](../00-course-setup/README.md)

## Nächste Lektion

[Erkunden agentenbasierter Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->