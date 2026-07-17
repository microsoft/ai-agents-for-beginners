# Speicher für KI-Agenten 
[![Agentenspeicher](../../../translated_images/de/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Beim Diskutieren der einzigartigen Vorteile von KI-Agenten werden hauptsächlich zwei Dinge besprochen: die Fähigkeit, Werkzeuge aufzurufen, um Aufgaben zu erledigen, und die Fähigkeit, sich im Laufe der Zeit zu verbessern. Speicher bildet die Grundlage für die Schaffung eines sich selbst verbessernden Agenten, der bessere Erfahrungen für unsere Benutzer schaffen kann.

In dieser Lektion werden wir uns ansehen, was Speicher für KI-Agenten bedeutet und wie wir ihn verwalten und zum Nutzen unserer Anwendungen einsetzen können.

## Einführung

Diese Lektion behandelt:

• **Verständnis des Speichers von KI-Agenten**: Was Speicher ist und warum er für Agenten unerlässlich ist.

• **Implementierung und Speicherung von Speicher**: Praktische Methoden zur Erweiterung Ihrer KI-Agenten um Speicherfunktionen mit Fokus auf Kurzzeit- und Langzeitspeicher.

• **Selbstverbesserung von KI-Agenten**: Wie Speicher es Agenten ermöglicht, aus vergangenen Interaktionen zu lernen und sich im Laufe der Zeit zu verbessern.

## Verfügbare Implementierungen

Diese Lektion umfasst zwei umfassende Notebook-Tutorials:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementiert Speicher mit Mem0 und Azure AI Search im Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementiert strukturierten Speicher mit Cognee, erstellt automatisch einen wissensgraphgestützten Embedding-Graphen, visualisiert den Graph und ermöglicht intelligente Abfragen

## Lernziele

Nach Abschluss dieser Lektion werden Sie wissen, wie Sie:

• **verschiedene Arten von Speicher für KI-Agenten unterscheiden**, einschließlich Arbeits-, Kurzzeit- und Langzeitspeicher sowie spezialisierte Formen wie Persona- und episodischer Speicher.

• **Kurzzeit- und Langzeitspeicher für KI-Agenten implementieren und verwalten** mit Microsoft Agent Framework, unter Nutzung von Werkzeugen wie Mem0, Cognee, Whiteboard-Speicher und Integration mit Azure AI Search.

• **die Prinzipien hinter selbstverbessernden KI-Agenten verstehen** und wie robuste Speichermanagementsysteme zum kontinuierlichen Lernen und zur Anpassung beitragen.

## Verständnis von Speicher für KI-Agenten

Im Kern bezieht sich **Speicher für KI-Agenten auf Mechanismen, die ihnen erlauben, Informationen zu behalten und abzurufen**. Diese Informationen können spezifische Details über ein Gespräch, Benutzerpräferenzen, vergangene Aktionen oder sogar erlernte Muster sein.

Ohne Speicher sind KI-Anwendungen oft zustandslos, das heißt, jede Interaktion beginnt von vorne. Dies führt zu einer sich wiederholenden und frustrierenden Benutzererfahrung, bei der der Agent den vorherigen Kontext oder Präferenzen "vergisst".

### Warum ist Speicher wichtig?

Die Intelligenz eines Agenten ist eng mit seiner Fähigkeit verbunden, vergangene Informationen abzurufen und zu nutzen. Speicher ermöglicht es Agenten,

• **reflektierend zu sein**: Aus vergangenen Aktionen und Ergebnissen zu lernen.

• **interaktiv zu sein**: Den Kontext eines laufenden Gesprächs aufrechtzuerhalten.

• **proaktiv und reaktiv zu sein**: Bedürfnisse vorherzusehen oder basierend auf historischen Daten angemessen zu reagieren.

• **autonom zu agieren**: Unabhängiger zu arbeiten, indem auf gespeichertes Wissen zurückgegriffen wird.

Das Ziel der Implementierung von Speicher ist es, Agenten **zuverlässiger und leistungsfähiger** zu machen.

### Speicherarten

#### Arbeitsgedächtnis

Stellen Sie sich dies als einen Notizzettel vor, den ein Agent während einer einzelnen, laufenden Aufgabe oder Denkprozess verwendet. Es enthält unmittelbare Informationen, die für den nächsten Schritt benötigt werden.

Für KI-Agenten erfasst das Arbeitsgedächtnis oft die relevantesten Informationen eines Gesprächs, auch wenn die gesamte Chat-Historie lang oder abgeschnitten ist. Es konzentriert sich darauf, Schlüsselelemente wie Anforderungen, Vorschläge, Entscheidungen und Aktionen zu extrahieren.

**Beispiel Arbeitsgedächtnis**

Bei einem Reisebuchungsagenten könnte das Arbeitsgedächtnis die aktuelle Anfrage des Nutzers erfassen, wie „Ich möchte eine Reise nach Paris buchen“. Diese spezifische Anforderung wird im unmittelbaren Kontext des Agenten gehalten, um die aktuelle Interaktion zu steuern.

#### Kurzzeitspeicher

Diese Speicherart behält Informationen für die Dauer eines einzelnen Gesprächs oder einer Sitzung. Es ist der Kontext des aktuellen Chats, der es dem Agenten ermöglicht, auf vorherige Gesprächsabschnitte zurückzugreifen.

In den Beispielen des [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK entspricht dies `AgentSession`, erstellt mit `agent.create_session()`. Die Sitzung ist der eingebaute Kurzzeitspeicher des Frameworks: Sie hält den Gesprächskontext verfügbar, solange dieselbe Sitzung verwendet wird, aber dieser Kontext wird nicht gespeichert, wenn die Sitzung endet oder die Anwendung neu startet. Verwenden Sie Langzeitspeicher für Fakten und Präferenzen, die über Sitzungen hinweg erhalten bleiben müssen, typischerweise über eine Datenbank, einen Vektorindex oder einen anderen persistenten Speicher.

**Beispiel Kurzzeitspeicher**

Wenn ein Nutzer fragt „Wie viel würde ein Flug nach Paris kosten?“ und dann mit „Und die Unterkunft dort?“ nachfragt, stellt der Kurzzeitspeicher sicher, dass der Agent weiß, dass sich „dort“ auf „Paris“ im selben Gespräch bezieht.

#### Langzeitspeicher

Dies ist Information, die über mehrere Gespräche oder Sitzungen hinweg erhalten bleibt. Sie ermöglicht es Agenten, Benutzerpräferenzen, historische Interaktionen oder allgemeines Wissen über längere Zeiträume zu speichern. Dies ist wichtig für die Personalisierung.

**Beispiel Langzeitspeicher**

Ein Langzeitspeicher könnte speichern, dass „Ben gerne Ski fährt und Outdoor-Aktivitäten mag, Kaffee mit Bergblick bevorzugt und fortgeschrittene Skipisten aufgrund einer früheren Verletzung meiden möchte“. Diese aus früheren Interaktionen erlernte Information beeinflusst Empfehlungen in zukünftigen Reiseplanungen und macht sie sehr persönlich.

#### Persona-Speicher

Diese spezialisierte Speicherart hilft einem Agenten, eine konsistente „Persönlichkeit“ oder „Persona“ zu entwickeln. Sie ermöglicht dem Agenten, Details über sich selbst oder seine vorgesehene Rolle zu erinnern, wodurch Interaktionen flüssiger und fokussierter werden.

**Beispiel Persona-Speicher**
Wenn der Reiseagent als „Experte für Skiplanung“ konzipiert ist, könnte der Persona-Speicher diese Rolle verstärken und die Antworten im Ton und Wissen eines Experten gestalten.

#### Workflow/Episodenspeicher

Dieser Speicher enthält die Abfolge von Schritten, die ein Agent während einer komplexen Aufgabe durchläuft, einschließlich Erfolge und Misserfolge. Es ist wie das Erinnern an spezifische „Episoden“ oder vergangene Erfahrungen, um daraus zu lernen.

**Beispiel Episodenspeicher**

Wenn der Agent versucht hat, einen bestimmten Flug zu buchen, dies aber wegen Nichtverfügbarkeit scheiterte, könnte der Episodenspeicher diesen Misserfolg aufzeichnen, sodass der Agent alternative Flüge versucht oder den Nutzer bei einem zukünftigen Versuch besser informiert.

#### Entity Memory (Entitätenspeicher)

Dies beinhaltet das Extrahieren und Erinnern spezifischer Entitäten (wie Personen, Orte oder Dinge) und Ereignisse aus Gesprächen. Es ermöglicht dem Agenten, ein strukturiertes Verständnis von Schlüsselelementen der Unterhaltung aufzubauen.

**Beispiel Entitätenspeicher**

Aus einem Gespräch über eine vergangene Reise könnte der Agent „Paris“, „Eiffelturm“ und „Abendessen im Le Chat Noir Restaurant“ als Entitäten extrahieren. Bei einer zukünftigen Interaktion könnte der Agent „Le Chat Noir“ erinnern und anbieten, dort eine neue Reservierung vorzunehmen.

#### Strukturierte RAG (Retrieval Augmented Generation)

Während RAG eine allgemeinere Technik ist, wird „Strukturierte RAG“ als leistungsstarke Speichertechnologie hervorgehoben. Sie extrahiert dichte, strukturierte Informationen aus verschiedenen Quellen (Gespräche, E-Mails, Bilder) und nutzt diese, um Präzision, Abruf und Geschwindigkeit der Antworten zu verbessern. Im Gegensatz zur klassischen RAG, die sich nur auf semantische Ähnlichkeit stützt, arbeitet Strukturierte RAG mit der inhärenten Struktur der Informationen.

**Beispiel Strukturierte RAG**

Anstatt nur Schlüsselwörter abzugleichen, könnte Strukturierte RAG Flugdaten (Ziel, Datum, Uhrzeit, Fluggesellschaft) aus einer E-Mail parsen und strukturiert speichern. So sind präzise Abfragen möglich wie „Welchen Flug habe ich am Dienstag nach Paris gebucht?“

## Implementierung und Speicherung von Speicher

Die Implementierung von Speicher für KI-Agenten beinhaltet einen systematischen Prozess des **Speichermanagements**, der das Generieren, Speichern, Abrufen, Integrieren, Aktualisieren und sogar „Vergessen“ (oder Löschen) von Informationen umfasst. Das Abrufen ist ein besonders wichtiger Aspekt.

### Spezialisierte Speichertools

#### Mem0

Eine Möglichkeit, den Speicher eines Agenten zu speichern und zu verwalten, ist die Verwendung spezialisierter Werkzeuge wie Mem0. Mem0 fungiert als persistente Speicherschicht, die es Agenten ermöglicht, relevante Interaktionen abzurufen, Benutzerpräferenzen und faktischen Kontext zu speichern und aus Erfolgen und Misserfolgen im Laufe der Zeit zu lernen. Die Idee ist hier, dass zustandslose Agenten zu zustandsbehafteten werden.

Es funktioniert durch eine **zweiphasige Speicherkette: Extraktion und Aktualisierung**. Zuerst werden Nachrichten, die dem Thread eines Agenten hinzugefügt werden, an den Mem0-Dienst gesendet, welcher ein Large Language Model (LLM) nutzt, um Gesprächshistorien zu summarieren und neue Erinnerungen zu extrahieren. Anschließend bestimmt eine LLM-gesteuerte Aktualisierungsphase, ob diese Erinnerungen hinzugefügt, modifiziert oder gelöscht werden, und speichert sie in einem hybriden Datenspeicher, der Vektor-, Graph- und Key-Value-Datenbanken umfassen kann. Dieses System unterstützt auch verschiedene Speicherarten und kann Graphenspeicher zur Verwaltung von Beziehungen zwischen Entitäten einbauen.

#### Cognee

Ein weiterer leistungsfähiger Ansatz ist die Verwendung von **Cognee**, einem Open-Source semantischen Speicher für KI-Agenten, der strukturierte und unstrukturierte Daten in abfragbare Wissensgraphen umwandelt, die von Embeddings gestützt sind. Cognee bietet eine **Dual-Store-Architektur**, die Vektorähnlichkeitssuche mit Graphbeziehungen kombiniert, sodass Agenten nicht nur verstehen, welche Informationen ähnlich sind, sondern auch wie Konzepte miteinander in Beziehung stehen.

Es zeichnet sich durch **hybriden Abruf** aus, der Vektorähnlichkeit, Graphstruktur und LLM-Denken vermischt – von einfachem Chunk-Lookup bis hin zu graphbewusster Fragebeantwortung. Das System pflegt einen **lebenden Speicher**, der sich entwickelt und wächst, während er als ein vernetzter Graph abfragbar bleibt und sowohl kurzzeitigen Sitzungs­kontext als auch langfristigen persistenten Speicher unterstützt.

Das Cognee-Notebook-Tutorial ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstriert den Aufbau dieser einheitlichen Speicherschicht mit praktischen Beispielen zum Einlesen diverser Datenquellen, zur Visualisierung des Wissensgraphen und zur Abfrage mit unterschiedlichen Suchstrategien, die auf spezifische Agentenbedürfnisse zugeschnitten sind.

### Speicherung von Speicher mit RAG

Neben spezialisierten Speichertools wie Mem0 können Sie robuste Suchdienste wie **Azure AI Search als Backend zum Speichern und Abrufen von Erinnerungen nutzen**, insbesondere für strukturierte RAG.

Dies erlaubt es, die Antworten Ihres Agenten mit Ihren eigenen Daten zu untermauern, was relevantere und genauere Antworten sichert. Azure AI Search kann verwendet werden, um benutzerspezifische Reiseerinnerungen, Produktkataloge oder anderes domänenspezifisches Wissen zu speichern.

Azure AI Search unterstützt Funktionen wie **Strukturierte RAG**, die hervorragend darin ist, dichte, strukturierte Informationen aus großen Datenbeständen wie Gesprächshistorien, E-Mails oder sogar Bildern zu extrahieren und abzurufen. Dies bietet „übermenschliche Präzision und Abruf“ verglichen mit traditionellen Text-Chunking- und Embedding-Ansätzen.

## Selbstverbesserung von KI-Agenten

Ein häufiges Muster für selbstverbessernde Agenten ist die Einführung eines **„Wissensagenten“**. Dieser separate Agent beobachtet das Hauptgespräch zwischen dem Nutzer und dem primären Agenten. Seine Rolle ist,

1. **wertvolle Informationen zu identifizieren**: Bestimmen, ob Teile des Gesprächs als allgemeines Wissen oder spezifische Benutzerpräferenz gespeichert werden sollten.

2. **extrahieren und zusammenfassen**: Das Wesentliche aus dem Gespräch destillieren.

3. **in einer Wissensbasis speichern**: Diese extrahierte Information persistieren, oft in einer Vektordatenbank, damit sie später abgerufen werden kann.

4. **zukünftige Abfragen anreichern**: Wenn der Nutzer eine neue Anfrage startet, ruft der Wissensagent relevante gespeicherte Informationen ab und fügt sie dem Nutzereingabe-Prompt hinzu, wodurch dem primären Agenten entscheidender Kontext gegeben wird (ähnlich wie bei RAG).

### Optimierungen für Speicher

• **Latenzmanagement**: Um Verzögerungen bei Nutzerinteraktionen zu vermeiden, kann zunächst ein günstigeres, schnelleres Modell eingesetzt werden, das schnell prüft, ob Informationen wert sind, gespeichert oder abgerufen zu werden, und nur bei Bedarf den komplexeren Extraktions-/Abrufprozess aufruft.

• **Wartung der Wissensbasis**: Für eine wachsende Wissensbasis kann weniger häufig genutzte Information in „Cold Storage“ verschoben werden, um Kosten zu verwalten.

## Haben Sie weitere Fragen zum Agentenspeicher?

Treten Sie dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten beantwortet zu bekommen.
## Vorherige Lektion

[Kontext-Engineering für KI-Agenten](../12-context-engineering/README.md)

## Nächste Lektion

[Erkundung des Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->