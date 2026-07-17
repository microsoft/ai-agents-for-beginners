# Verwendung von Agentic Protocols (MCP, A2A und NLWeb)

[![Agentic Protocols](../../../translated_images/de/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

Mit dem wachsenden Einsatz von KI-Agenten steigt auch der Bedarf an Protokollen, die Standardisierung, Sicherheit gewährleisten und offene Innovation unterstützen. In dieser Lektion behandeln wir 3 Protokolle, die diese Anforderungen erfüllen wollen - Model Context Protocol (MCP), Agent to Agent (A2A) und Natural Language Web (NLWeb).

## Einführung

In dieser Lektion behandeln wir:

• Wie **MCP** es KI-Agenten ermöglicht, auf externe Werkzeuge und Daten zuzugreifen, um Benutzeraufgaben zu erfüllen.

• Wie **A2A** Kommunikation und Zusammenarbeit zwischen verschiedenen KI-Agenten ermöglicht.

• Wie **NLWeb** natürliche Sprachschnittstellen auf jeder Webseite ermöglicht, sodass KI-Agenten die Inhalte entdecken und mit ihnen interagieren können.

## Lernziele

• **Erkennen** des Hauptzwecks und der Vorteile von MCP, A2A und NLWeb im Kontext von KI-Agenten.

• **Erklären**, wie jedes Protokoll die Kommunikation und Interaktion zwischen LLMs, Werkzeugen und anderen Agenten erleichtert.

• **Erkennen** der unterschiedlichen Rollen, die jedes Protokoll beim Aufbau komplexer agentischer Systeme spielt.

## Model Context Protocol

Das **Model Context Protocol (MCP)** ist ein offener Standard, der eine standardisierte Methode bereitstellt, damit Anwendungen Kontext und Werkzeuge für LLMs bereitstellen können. Dies ermöglicht einen "universellen Adapter" für verschiedene Datenquellen und Werkzeuge, die KI-Agenten auf konsistente Weise verbinden können.

Sehen wir uns die Komponenten von MCP, die Vorteile gegenüber direkter API-Nutzung und ein Beispiel an, wie KI-Agenten einen MCP-Server verwenden könnten.

### MCP Kernkomponenten

MCP basiert auf einer **Client-Server-Architektur** und die Kernkomponenten sind:

• **Hosts** sind LLM-Anwendungen (zum Beispiel ein Code-Editor wie VSCode), die die Verbindungen zu einem MCP-Server starten.

• **Clients** sind Komponenten innerhalb der Host-Anwendung, die eins-zu-eins-Verbindungen zu Servern pflegen.

• **Server** sind schlanke Programme, die spezifische Fähigkeiten bereitstellen.

Im Protokoll sind drei grundlegende Primitive enthalten, die die Fähigkeiten eines MCP-Servers beschreiben:

• **Werkzeuge (Tools)**: Dies sind einzelne Aktionen oder Funktionen, die ein KI-Agent aufrufen kann, um eine Aktion auszuführen. Ein Wetterdienst könnte beispielsweise ein „Wetter abrufen“-Werkzeug anbieten, oder ein E-Commerce-Server ein „Produkt kaufen“-Werkzeug. MCP-Server veröffentlichen die Namen, Beschreibungen und Ein-/Ausgabe-Schemata jedes Werkzeugs in ihrer Fähigkeitensliste.

• **Ressourcen**: Dies sind schreibgeschützte Datenobjekte oder Dokumente, die ein MCP-Server bereitstellen kann und die Clients bei Bedarf abrufen können. Beispiele sind Dateiinhalte, Datenbankeinträge oder Protokolldateien. Ressourcen können Text (wie Code oder JSON) oder Binärdaten (wie Bilder oder PDFs) sein.

• **Prompts**: Dies sind vordefinierte Vorlagen, die vorgeschlagene Eingaben bereitstellen und komplexere Abläufe ermöglichen.

### Vorteile von MCP

MCP bietet erhebliche Vorteile für KI-Agenten:

• **Dynamische Werkzeugerkennung**: Agenten können dynamisch eine Liste verfügbarer Werkzeuge von einem Server erhalten, inklusive Beschreibungen, was diese tun. Dies steht im Gegensatz zu traditionellen APIs, die oft statische Code-Integration erfordern, sodass jede API-Änderung Codeanpassungen notwendig macht. MCP bietet einen „einmal integrieren“-Ansatz und ermöglicht so mehr Anpassungsfähigkeit.

• **Interoperabilität über LLMs hinweg**: MCP funktioniert über verschiedene LLMs hinweg und bietet Flexibilität beim Wechsel des Kernmodells für bessere Performance.

• **Standardisierte Sicherheit**: MCP enthält eine standardisierte Authentifizierungsmethode, die Skalierbarkeit beim Hinzufügen von Zugriffen auf weitere MCP-Server verbessert. Dies ist einfacher als das Management unterschiedlicher Schlüssel und Authentifizierungstypen für verschiedene traditionelle APIs.

### MCP-Beispiel

![MCP Diagramm](../../../translated_images/de/mcp-diagram.e4ca1cbd551444a1.webp)

Stellen Sie sich vor, ein Nutzer möchte mit einem MCP-gestützten KI-Assistenten einen Flug buchen.

1. **Verbindung**: Der KI-Assistent (der MCP-Client) verbindet sich mit einem MCP-Server einer Fluggesellschaft.

2. **Werkzeug-Erkennung**: Der Client fragt den MCP-Server der Fluggesellschaft: „Welche Werkzeuge bieten Sie an?“ Der Server antwortet mit Werkzeugen wie „Flüge suchen“ und „Flüge buchen“.

3. **Werkzeugaufruf**: Der Nutzer bittet den KI-Assistenten: „Bitte suche einen Flug von Portland nach Honolulu.“ Der KI-Assistent nutzt sein LLM, erkennt, dass das Werkzeug „Flüge suchen“ aufgerufen werden muss, und übergibt die entsprechenden Parameter (Abflugort, Ziel) an den MCP-Server.

4. **Ausführung und Antwort**: Der MCP-Server fungiert als Wrapper und ruft die interne Buchungs-API der Fluggesellschaft auf. Anschließend empfängt er die Fluginformationen (z. B. JSON-Daten) und sendet sie an den KI-Assistenten zurück.

5. **Weitere Interaktion**: Der KI-Assistent präsentiert die Flugoptionen. Wenn der Nutzer einen Flug auswählt, könnte der Assistent das Werkzeug „Flug buchen“ auf demselben MCP-Server aufrufen und die Buchung abschließen.

## Agent-to-Agent-Protokoll (A2A)

Während MCP sich auf die Verbindung von LLMs mit Werkzeugen konzentriert, geht das **Agent-to-Agent (A2A) Protokoll** einen Schritt weiter, indem es Kommunikation und Zusammenarbeit zwischen unterschiedlichen KI-Agenten ermöglicht. A2A verbindet KI-Agenten verschiedener Organisationen, Umgebungen und Technologien, um eine gemeinsame Aufgabe zu erfüllen.

Wir betrachten die Komponenten und Vorteile von A2A sowie ein Beispiel, wie es in unserer Reise-App angewendet werden könnte.

### A2A Kernkomponenten

A2A konzentriert sich darauf, Kommunikation zwischen Agenten zu ermöglichen und sie zusammen Aufgaben eines Nutzers erledigen zu lassen. Jede Komponente des Protokolls trägt dazu bei:

#### Agent Card

Ähnlich wie ein MCP-Server eine Liste von Werkzeugen teilt, enthält eine Agent Card:
- Den Namen des Agenten.
- Eine **Beschreibung der allgemeinen Aufgaben**, die er erfüllt.
- Eine **Liste spezifischer Fähigkeiten** mit Beschreibungen, damit andere Agenten (oder auch Menschen) verstehen, wann und warum sie diesen Agenten anrufen sollten.
- Die **aktuelle Endpoint-URL** des Agenten.
- Die **Version** und **Fähigkeiten** des Agenten, wie Streaming-Antworten und Push-Benachrichtigungen.

#### Agent Executor

Der Agent Executor ist verantwortlich dafür, **den Kontext des Benutzerchats an den entfernten Agenten weiterzuleiten**. Der entfernte Agent benötigt diesen, um die auszuführende Aufgabe zu verstehen. In einem A2A-Server nutzt ein Agent sein eigenes Large Language Model (LLM), um eingehende Anfragen zu analysieren und Aufgaben mit seinen eigenen internen Werkzeugen zu erfüllen.

#### Artefakt

Sobald ein entfernter Agent die angeforderte Aufgabe abgeschlossen hat, wird sein Arbeitsergebnis als Artefakt erstellt. Ein Artefakt **enthält das Ergebnis der Arbeit des Agenten**, eine **Beschreibung des Erledigten** und den **Textkontext**, der über das Protokoll gesendet wird. Nach dem Senden des Artefakts wird die Verbindung zum entfernten Agenten geschlossen, bis sie wieder benötigt wird.

#### Ereigniswarteschlange

Diese Komponente wird zum **Verwalten von Updates und Nachrichtenweiterleitung** genutzt. Sie ist besonders in Produktionssystemen wichtig, um zu verhindern, dass Verbindungen zwischen Agenten vor Abschluss einer Aufgabe geschlossen werden, insbesondere wenn Aufgaben längere Zeit in Anspruch nehmen.

### Vorteile von A2A

• **Verbesserte Zusammenarbeit**: Ermöglicht Agenten verschiedener Anbieter und Plattformen, miteinander zu interagieren, Kontext zu teilen und zusammenzuarbeiten, was nahtlose Automatisierung über traditionell getrennte Systeme hinweg erlaubt.

• **Flexible Modellauswahl**: Jeder A2A-Agent kann selbst entscheiden, welches LLM er zur Bearbeitung seiner Anfragen nutzt, was optimierte oder feingetunte Modelle je Agent erlaubt – im Gegensatz zu einer einzigen LLM-Verbindung in manchen MCP-Szenarien.

• **Integrierte Authentifizierung**: Authentifizierung ist direkt im A2A-Protokoll integriert und bietet einen robusten Sicherheitsrahmen für Agenteninteraktionen.

### A2A Beispiel

![A2A Diagramm](../../../translated_images/de/A2A-Diagram.8666928d648acc26.webp)

Erweitern wir unser Reiseszenario, diesmal mit A2A.

1. **Benutzeranfrage an Multi-Agenten**: Ein Nutzer interagiert mit einem „Reiseagent“ A2A-Client/Agent, zum Beispiel mit der Aussage: „Bitte buche eine gesamte Reise nach Honolulu für nächste Woche, inklusive Flügen, Hotel und Mietwagen“.

2. **Orchestrierung durch den Reiseagenten**: Der Reiseagent erhält diese komplexe Anfrage. Er nutzt sein LLM, um die Aufgabe zu analysieren und festzustellen, dass er mit anderen spezialisierten Agenten interagieren muss.

3. **Kommunikation zwischen Agenten**: Der Reiseagent nutzt dann das A2A-Protokoll, um Verbindungen zu nachgelagerten Agenten herzustellen, wie einem „Fluggesellschaft-Agent“, einem „Hotel-Agent“ und einem „Mietwagen-Agent“, die von verschiedenen Firmen erstellt wurden.

4. **Delegierte Aufgabenausführung**: Der Reiseagent sendet spezifische Aufgaben an diese spezialisierten Agenten (z. B. „Finde Flüge nach Honolulu“, „Buche ein Hotel“, „Miete einen Wagen“). Jeder dieser spezialisierten Agenten, die eigene LLMs verwenden und eigene Werkzeuge nutzen (die selbst MCP-Server sein können), führt seinen Teil der Buchung durch.

5. **Konsolidierte Antwort**: Sobald alle nachgelagerten Agenten ihre Aufgaben erledigt haben, fasst der Reiseagent die Ergebnisse zusammen (Flugdetails, Hotelbestätigung, Mietwagenbuchung) und sendet eine umfassende, Chat-artige Antwort an den Nutzer.

## Natural Language Web (NLWeb)

Webseiten sind seit langem der Hauptweg für Nutzer, um Informationen und Daten im Internet abzurufen.

Sehen wir uns die verschiedenen Komponenten von NLWeb, die Vorteile von NLWeb und ein Beispiel an, wie unser NLWeb anhand unserer Reise-App funktioniert.

### Komponenten von NLWeb

- **NLWeb-Anwendung (Core Service Code)**: Das System, das natürliche Sprachfragen verarbeitet. Es verbindet die verschiedenen Teile der Plattform, um Antworten zu generieren. Man kann es als **Motor ansehen, der die natürlichen Sprachfunktionen einer Webseite antreibt**.

- **NLWeb-Protokoll**: Ein **Grundregelwerk für natürliche Sprachinteraktion** mit einer Webseite. Es liefert Antworten im JSON-Format (oft mit Schema.org). Sein Zweck ist es, eine einfache Basis für das „AI Web“ zu schaffen, ähnlich wie HTML das Teilen von Dokumenten online ermöglichte.

- **MCP-Server (Model Context Protocol Endpoint)**: Jede NLWeb-Installation fungiert auch als **MCP-Server**. Das heißt, sie kann **Werkzeuge (wie eine „ask“-Methode) und Daten** mit anderen KI-Systemen teilen. Praktisch macht dies die Inhalte und Fähigkeiten der Webseite für KI-Agenten nutzbar, wodurch die Seite Teil des größeren „Agenten-Ökosystems“ wird.

- **Embedding-Modelle**: Diese Modelle werden verwendet, um **Webseiteninhalte in numerische Darstellungen, sogenannte Vektoren (Embeddings), umzuwandeln**. Diese Vektoren erfassen Bedeutung auf eine Weise, die Computer vergleichen und durchsuchen können. Sie werden in speziellen Datenbanken gespeichert, und Nutzer können auswählen, welches Embedding-Modell sie verwenden möchten.

- **Vektor-Datenbank (Retrieval-Mechanismus)**: Diese Datenbank **speichert die Embeddings der Webseiteninhalte**. Wenn jemand eine Frage stellt, durchsucht NLWeb die Vektor-Datenbank, um schnell die relevantesten Informationen zu finden. Es liefert eine schnelle Liste möglicher Antworten, sortiert nach Ähnlichkeit. NLWeb funktioniert mit verschiedenen Vektor-Speichersystemen wie Qdrant, Snowflake, Milvus, Azure AI Search und Elasticsearch.

### NLWeb am Beispiel

![NLWeb](../../../translated_images/de/nlweb-diagram.c1e2390b310e5fe4.webp)

Betrachten wir noch einmal unsere Reisebuchungs-Webseite, diesmal angetrieben von NLWeb.

1. **Datenaufnahme**: Die bestehenden Produktkataloge der Reise-Webseite (z. B. Fluglisten, Hotelbeschreibungen, Tourenpakete) werden mit Schema.org formatiert oder über RSS-Feeds geladen. Die NLWeb-Werkzeuge erfassen diese strukturierten Daten, erstellen Embeddings und speichern sie in einer lokalen oder entfernten Vektor-Datenbank.

2. **Natürliche Sprachabfrage (Mensch)**: Ein Nutzer besucht die Webseite und tippt anstelle der Navigation durch Menüs in eine Chat-Schnittstelle: „Finde mir ein familienfreundliches Hotel in Honolulu mit Pool für nächste Woche“.

3. **NLWeb-Verarbeitung**: Die NLWeb-Anwendung empfängt diese Anfrage. Sie sendet die Anfrage an ein LLM zur Verständnisanalyse und sucht gleichzeitig in ihrer Vektor-Datenbank nach passenden Hotelangeboten.

4. **Genauere Ergebnisse**: Das LLM hilft, die Suchergebnisse aus der Datenbank zu interpretieren, die besten Übereinstimmungen basierend auf den Kriterien „familienfreundlich“, „Pool“ und „Honolulu“ zu identifizieren und eine natürlichsprachliche Antwort zu formulieren. Dabei bezieht sich die Antwort auf tatsächliche Hotels aus dem Katalog der Webseite und vermeidet erfundene Informationen.

5. **KI-Agenten-Interaktion**: Da NLWeb als MCP-Server fungiert, könnte sich auch ein externer KI-Reiseagent mit dieser NLWeb-Instanz der Webseite verbinden. Der KI-Agent könnte dann die MCP-Methode `ask` verwenden, um die Webseite direkt abzufragen: `ask("Gibt es von den Hotels empfohlene vegane Restaurants in der Umgebung von Honolulu?")`. Die NLWeb-Instanz würde dies verarbeiten, ihre Datenbank mit Restaurantinformationen (sofern geladen) nutzen und eine strukturierte JSON-Antwort zurückgeben.

### Haben Sie weitere Fragen zu MCP/A2A/NLWeb?

Treten Sie dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten beantwortet zu bekommen.

## Ressourcen

- [MCP für Anfänger](https://aka.ms/mcp-for-beginners)  
- [MCP-Dokumentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Vorherige Lektion

[KI-Agenten in der Produktion](../10-ai-agents-production/README.md)

## Nächste Lektion

[Kontext-Engineering für KI-Agenten](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->