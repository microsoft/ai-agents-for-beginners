# Speicher für KI-Agenten 
[![Agent Memory](../../../translated_images/de/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Wenn über die einzigartigen Vorteile der Erstellung von KI-Agenten gesprochen wird, werden hauptsächlich zwei Dinge diskutiert: die Fähigkeit, Werkzeuge aufzurufen, um Aufgaben zu erledigen, und die Fähigkeit, sich im Laufe der Zeit zu verbessern. Speicher bildet die Grundlage für die Schaffung selbstverbessernder Agenten, die bessere Erlebnisse für unsere Nutzer schaffen können.

In dieser Lektion sehen wir uns an, was Speicher für KI-Agenten bedeutet und wie wir ihn verwalten und zum Vorteil unserer Anwendungen nutzen können.

## Einführung

Diese Lektion behandelt:

• **Verständnis des Speichers für KI-Agenten**: Was Speicher ist und warum er für Agenten essenziell ist.

• **Implementierung und Speicherung von Speicher**: Praktische Methoden zum Hinzufügen von Speicherfunktionen zu Ihren KI-Agenten, mit Fokus auf Kurzzeit- und Langzeitspeicher.

• **Selbstverbesserung von KI-Agenten**: Wie Speicher es Agenten ermöglicht, aus vergangenen Interaktionen zu lernen und sich im Laufe der Zeit zu verbessern.

## Verfügbare Implementierungen

Diese Lektion enthält zwei ausführliche Notebook-Tutorials:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementiert Speicher mit Mem0 und Azure AI Search im Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementiert strukturierten Speicher mit Cognee, baut automatisch einen wissensgraphgestützten Speicher auf, visualisiert den Graph und ermöglicht intelligente Abfragen

## Lernziele

Nach Abschluss dieser Lektion wissen Sie, wie Sie:

• **Zwischen verschiedenen Arten von KI-Agentenspeicher unterscheiden**, einschließlich Arbeits-, Kurzzeit- und Langzeitspeicher sowie spezialisierten Formen wie Persona- und Episodenspeicher.

• **Kurzzeit- und Langzeitspeicher für KI-Agenten implementieren und verwalten** unter Verwendung des Microsoft Agent Frameworks, mit Werkzeugen wie Mem0, Cognee, Whiteboard-Speicher und Integration mit Azure AI Search.

• **Die Prinzipien hinter selbstverbessernden KI-Agenten verstehen** und wie robuste Speichermanagementsysteme kontinuierliches Lernen und Anpassung ermöglichen.

## Verständnis des Speichers für KI-Agenten

Im Kern bezieht sich **Speicher für KI-Agenten auf Mechanismen, die es ihnen ermöglichen, Informationen zu behalten und wieder abzurufen**. Diese Informationen können spezifische Details über ein Gespräch, Nutzerpräferenzen, vergangene Aktionen oder sogar gelernte Muster sein.

Ohne Speicher sind KI-Anwendungen oft zustandslos, was bedeutet, dass jede Interaktion von vorne beginnt. Das führt zu einer repetitiven und frustrierenden Nutzererfahrung, bei der der Agent den vorherigen Kontext oder Präferenzen "vergisst".

### Warum ist Speicher wichtig?

Die Intelligenz eines Agenten ist eng mit seiner Fähigkeit verknüpft, vergangene Informationen abzurufen und zu nutzen. Speicher ermöglicht es Agenten, 

• **Reflektierend zu sein**: Aus vergangenen Handlungen und Ergebnissen zu lernen.

• **Interaktiv zu sein**: Den Kontext eines laufenden Gesprächs aufrechtzuerhalten.

• **Proaktiv und Reaktiv zu sein**: Bedürfnisse vorauszusehen oder angemessen basierend auf historischen Daten zu reagieren.

• **Autonom zu sein**: Unabhängiger zu agieren, indem sie auf gespeichertes Wissen zurückgreifen.

Das Ziel der Implementierung von Speicher ist es, Agenten zuverlässiger und fähiger zu machen.

### Arten von Speicher

#### Arbeitsgedächtnis

Man kann dies als ein Notizblatt betrachten, das ein Agent während einer einzelnen, laufenden Aufgabe oder Denkprozesses verwendet. Es enthält unmittelbare Informationen, die zur Berechnung des nächsten Schrittes benötigt werden.

Für KI-Agenten erfasst das Arbeitsgedächtnis oft die relevantesten Informationen aus einem Gespräch, selbst wenn der vollständige Chatverlauf lang oder abgeschnitten ist. Es konzentriert sich darauf, Schlüsselelemente wie Anforderungen, Vorschläge, Entscheidungen und Aktionen zu extrahieren.

**Beispiel Arbeitsgedächtnis**

Ein Reisebuchungsagent könnte im Arbeitsgedächtnis die aktuelle Anfrage des Nutzers speichern, etwa „Ich möchte eine Reise nach Paris buchen“. Diese spezifische Anforderung wird im unmittelbaren Kontext des Agenten gehalten, um die aktuelle Interaktion zu steuern.

#### Kurzzeitspeicher

Diese Art von Speicher bewahrt Informationen für die Dauer eines einzelnen Gesprächs oder einer Sitzung. Es ist der Kontext des aktuellen Chats, der es dem Agenten erlaubt, auf vorherige Gesprächsrunden Bezug zu nehmen.

In den Python-Samples des [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) entspricht dies `AgentSession`, erzeugt mit `agent.create_session()`. Die Session ist der eingebaute Kurzzeitspeicher des Frameworks: Er hält den Gesprächskontext verfügbar, solange dieselbe Session wiederverwendet wird, speichert den Kontext aber nicht, wenn die Sitzung endet oder die Anwendung neu startet. Für Fakten und Präferenzen, die über Sessions hinaus erhalten bleiben müssen, sollte Langzeitspeicher verwendet werden, typischerweise über eine Datenbank, Vektorindex oder einen anderen persistenten Speicher.

**Beispiel Kurzzeitspeicher**

Fragt ein Nutzer „Wie viel kostet ein Flug nach Paris?“ und anschließend „Wie sieht es mit der Unterkunft dort aus?“, stellt Kurzzeitspeicher sicher, dass der Agent weiß, dass sich „dort“ innerhalb desselben Gesprächs auf „Paris“ bezieht.

#### Langzeitspeicher

Dies bezeichnet Informationen, die über mehrere Gespräche oder Sessions hinweg erhalten bleiben. Es ermöglicht Agenten, Nutzerpräferenzen, historische Interaktionen oder allgemeines Wissen über längere Zeiträume zu speichern. Dies ist wichtig für die Personalisierung.

**Beispiel Langzeitspeicher**

Ein Langzeitspeicher könnte z.B. abspeichern, dass „Ben Skifahren und Outdoor-Aktivitäten mag, Kaffee mit Bergblick bevorzugt und fortgeschrittene Skiabfahrten wegen einer früheren Verletzung vermeiden möchte“. Diese aus früheren Interaktionen gewonnenen Informationen beeinflussen Empfehlungen in zukünftigen Reiseplanungssitzungen und machen sie hochgradig personalisiert.

#### Persona-Speicher

Diese spezialisierte Speicherart hilft einem Agenten, eine konsistente „Persönlichkeit“ oder „Persona“ zu entwickeln. Sie ermöglicht es dem Agenten, sich an Details über sich selbst oder seine vorgesehene Rolle zu erinnern, wodurch Interaktionen flüssiger und fokussierter werden.

**Beispiel Persona-Speicher**

Ist der Reiseagent als „Experte für Ski-Planung“ konzipiert, könnte der Persona-Speicher diese Rolle verstärken und seine Antworten im Ton und Wissen an einen Experten anpassen.

#### Workflow-/Episodenspeicher

Dieser Speicher erfasst die Abfolge von Schritten, die ein Agent bei einer komplexen Aufgabe durchläuft, einschließlich Erfolgen und Misserfolgen. Es ist wie das Erinnern an spezifische „Episoden“ oder vergangene Erfahrungen, um daraus zu lernen.

**Beispiel Episodenspeicher**

Versuchte der Agent einen bestimmten Flug zu buchen, scheiterte aber wegen Nichtverfügbarkeit, könnte der Episodenspeicher diesen Fehlschlag dokumentieren. So kann der Agent bei einem erneuten Versuch alternative Flüge anbieten oder den Nutzer informierter über das Problem aufklären.

#### Entity-Speicher

Hierbei werden spezifische Entitäten (wie Personen, Orte oder Dinge) und Ereignisse aus Gesprächen extrahiert und gespeichert. Dadurch kann der Agent ein strukturiertes Verständnis der besprochenen Schlüsselaspekte aufbauen.

**Beispiel Entity-Speicher**

Aus einem Gespräch über eine vergangene Reise könnte der Agent „Paris“, „Eiffelturm“ und „Abendessen im Restaurant Le Chat Noir“ als Entitäten extrahieren. In einer späteren Interaktion könnte er „Le Chat Noir“ erinnern und eine neue Reservierung dort anbieten.

#### Strukturierte RAG (Retrieval Augmented Generation)

Während RAG eine breitere Technik ist, wird die „Strukturierte RAG“ als mächtige Speichertechnologie hervorgehoben. Sie extrahiert dichte, strukturierte Informationen aus verschiedenen Quellen (Gespräche, E-Mails, Bilder) und nutzt diese, um Präzision, Ergebnisqualität und Geschwindigkeit von Antworten zu verbessern. Im Gegensatz zu klassischem RAG, das sich ausschließlich auf semantische Ähnlichkeit stützt, arbeitet Strukturierte RAG mit der inhärenten Struktur der Informationen.

**Beispiel Strukturierte RAG**

Anstelle nur Schlüsselwörter zu matchen, könnte Strukturierte RAG Flugdaten (Zielort, Datum, Uhrzeit, Fluggesellschaft) aus einer E-Mail auslesen und strukturiert speichern. So sind präzise Abfragen möglich wie „Welchen Flug habe ich am Dienstag nach Paris gebucht?“

## Implementierung und Speicherung von Speicher

Die Implementierung von Speicher für KI-Agenten beinhaltet einen systematischen Prozess des **Speichermanagements**, der Erzeugung, Speicherung, Abruf, Integration, Aktualisierung und sogar das „Vergessen“ (Löschen) von Informationen umfasst. Besonders wichtig ist der Abruf.

### Spezialisierte Speichertools

#### Mem0

Eine Möglichkeit Speicher zu speichern und zu verwalten ist die Nutzung spezialisierter Tools wie Mem0. Mem0 fungiert als persistente Speicherschicht, die es Agenten ermöglicht, relevante Interaktionen abzurufen, Nutzerpräferenzen und faktischen Kontext zu speichern und aus Erfolgen sowie Misserfolgen im Laufe der Zeit zu lernen. Die Idee ist, dass zustandslose Agenten sich zu zustandsbehafteten Agenten wandeln.

Es arbeitet durch eine **zweiphasige Speicher-Pipeline: Extraktion und Aktualisierung**. Zunächst werden Nachrichten, die einem Agenten-Thread hinzugefügt werden, an den Mem0-Service gesendet, der mit einem großen Sprachmodell (LLM) den Gesprächsverlauf zusammenfasst und neue Erinnerungen extrahiert. Anschließend bestimmt eine LLM-gesteuerte Aktualisierungsphase, ob diese Erinnerungen hinzugefügt, verändert oder gelöscht werden und speichert sie in einem hybriden Datenspeicher, der Vektor-, Graph- und Key-Value-Datenbanken umfassen kann. Das System unterstützt verschiedene Speichertypen und kann Graph-Speicher für die Verwaltung von Beziehungen zwischen Entitäten integrieren.

#### Cognee

Ein weiterer schlagkräftiger Ansatz ist die Nutzung von **Cognee**, einem Open-Source-semantischen Speicher für KI-Agenten, der strukturierte und unstrukturierte Daten in abfragbare Wissensgraphen verwandelt, die auf Embeddings basieren. Cognee bietet eine **Dual-Store-Architektur** aus Vektorähnlichkeitssuche und Graphbeziehungen, die es Agenten erlaubt, nicht nur zu verstehen, welche Informationen ähnlich sind, sondern auch wie Konzepte zueinander in Beziehung stehen.

Es glänzt bei **hybridem Abruf**, der Vektorähnlichkeit, Graphstruktur und LLM-gestützte Logik kombiniert – von rohem Chunk-Lookup bis hin zu graphbewusster Fragebeantwortung. Das System hält einen **lebendigen Speicher** aufrecht, der sich entwickelt und wächst und dabei als ein verbundenes Graphobjekt abfragbar bleibt, unterstützt sowohl kurzfristigen Sitzungs-Kontext als auch langfristigen persistenten Speicher.

Das Cognee-Notebook-Tutorial ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstriert den Aufbau dieser einheitlichen Speicherschicht mit praktischen Beispielen zum Einlesen vielfältiger Datenquellen, Visualisierung des Wissensgraphen und Abfragen mit verschiedenen Suchstrategien, die an die spezifischen Agentenbedürfnisse angepasst sind.

### Speicherung von Speicher mit RAG

Neben spezialisierten Speichertools wie Mem0 können Sie robuste Suchdienste wie **Azure AI Search als Backend zur Speicherung und Abfrage von Erinnerungen** nutzen, insbesondere für strukturierte RAG.

Dies ermöglicht es, die Antworten Ihres Agenten mit den eigenen Daten zu untermauern, was relevantere und genauere Antworten garantiert. Azure AI Search kann verwendet werden, um benutzerspezifische Reisespeicher, Produktkataloge oder beliebiges anderes domänenspezifisches Wissen zu speichern.

Azure AI Search unterstützt Fähigkeiten wie **Strukturierte RAG**, die darin brilliert, dichte, strukturierte Informationen aus großen Datensätzen wie Gesprächsverläufen, E-Mails oder sogar Bildern zu extrahieren und abzurufen. Das bietet eine „übermenschliche Präzision und Ergebnisqualität“ verglichen mit herkömmlichen Text-Chunks und Embedding-Ansätzen.

## KI-Agenten selbst verbessern

Ein gängiges Muster für selbstverbessernde Agenten ist die Einführung eines **„Wissensagenten“**. Dieser separate Agent beobachtet die Hauptunterhaltung zwischen Nutzer und primärem Agenten. Seine Aufgaben sind:

1. **Wertvolle Informationen identifizieren**: Feststellen, ob Teile des Gesprächs als Allgemeinwissen oder spezifische Nutzerpräferenz gespeichert werden sollten.

2. **Extrahieren und zusammenfassen**: Das Wesentliche aus dem Gespräch destillieren.

3. **In Wissensbasis speichern**: Diese extrahierten Informationen, oft in einer Vektordatenbank, persistieren, damit sie später abrufbar sind.

4. **Zukünftige Abfragen anreichern**: Wenn der Nutzer eine neue Anfrage startet, ruft der Wissensagent relevante gespeicherte Informationen ab und ergänzt die Eingabeaufforderung des Nutzers, um dem Hauptagenten wichtigen Kontext bereitzustellen (ähnlich wie bei RAG).

### Optimierungen für Speicher

• **Latenzmanagement**: Um Nutzerinteraktionen nicht zu verlangsamen, kann ein günstigeres, schnelleres Modell initial verwendet werden, um schnell zu prüfen, ob Informationen wertvoll sind zum Speichern oder Abrufen. Der komplexere Extraktions-/Abrufprozess wird nur bei Bedarf aufgerufen.

• **Wartung der Wissensbasis**: Für eine wachsende Wissensbasis können weniger häufig genutzte Informationen in „Cold Storage“ verschoben werden, um Kosten zu optimieren.

## Haben Sie weitere Fragen zum Agentenspeicher?

Treffen Sie in der [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) andere Lernende, nehmen Sie an Sprechstunden teil und erhalten Sie Antworten auf Ihre Fragen zu KI-Agenten.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->