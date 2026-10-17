# Verwendung von Agentischen Protokollen (MCP, A2A und NLWeb)

[![Agentische Protokolle](../../../translated_images/de/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

Mit der zunehmenden Nutzung von KI-Agenten steigt auch der Bedarf an Protokollen, die Standardisierung, Sicherheit gewährleisten und offene Innovation unterstützen. In dieser Lektion behandeln wir 3 Protokolle, die diesen Bedarf decken sollen – das Model Context Protocol (MCP), Agent to Agent (A2A) und Natural Language Web (NLWeb).

## Einführung

In dieser Lektion behandeln wir:

• Wie **MCP** es KI-Agenten ermöglicht, auf externe Werkzeuge und Daten zuzugreifen, um Benutzeraufgaben zu erfüllen.

• Wie **A2A** Kommunikation und Zusammenarbeit zwischen verschiedenen KI-Agenten ermöglicht.

• Wie **NLWeb** natürliche Sprachschnittstellen für jede Webseite bereitstellt, damit KI-Agenten Inhalte entdecken und damit interagieren können.

## Lernziele

• **Kernzweck und Vorteile** von MCP, A2A und NLWeb im Kontext von KI-Agenten identifizieren.

• **Erläutern**, wie jedes Protokoll Kommunikation und Interaktion zwischen LLMs, Werkzeugen und anderen Agenten ermöglicht.

• **Unterscheiden**, welche spezifischen Rollen jedes Protokoll beim Aufbau komplexer agentischer Systeme spielt.

## Model Context Protocol

Das **Model Context Protocol (MCP)** ist ein offener Standard, der eine standardisierte Methode bereitstellt, damit Anwendungen Kontext und Werkzeuge für LLMs bereitstellen können. Dies ermöglicht einen „universellen Adapter“ für verschiedene Datenquellen und Werkzeuge, mit denen KI-Agenten auf konsistente Weise verbunden werden können.

Schauen wir uns die Komponenten von MCP, die Vorteile gegenüber direkter API-Nutzung und ein Beispiel an, wie KI-Agenten einen MCP-Server verwenden könnten.

### Kernkomponenten von MCP

MCP arbeitet auf einer **Client-Server-Architektur** und die Kernkomponenten sind:

• **Hosts** sind LLM-Anwendungen (zum Beispiel ein Code-Editor wie VSCode), die die Verbindungen zu einem MCP-Server starten.

• **Clients** sind Komponenten innerhalb der Host-Anwendung, die Eins-zu-Eins-Verbindungen mit Servern aufrechterhalten.

• **Server** sind leichte Programme, die spezifische Fähigkeiten bereitstellen.

Im Protokoll eingeschlossen sind drei Kernprimitive, die die Fähigkeiten eines MCP-Servers darstellen:

• **Werkzeuge**: Dies sind diskrete Aktionen oder Funktionen, die ein KI-Agent aufrufen kann, um eine Aktion auszuführen. Zum Beispiel könnte ein Wetterdienst ein Werkzeug „Wetter abrufen“ bereitstellen oder ein E-Commerce-Server ein Werkzeug „Produkt kaufen“. MCP-Server werben für den Namen, die Beschreibung und das Eingabe-/Ausgabe-Schema jedes Werkzeugs in ihrer Fähigkeitenübersicht.

• **Ressourcen**: Dies sind schreibgeschützte Datenobjekte oder Dokumente, die ein MCP-Server bereitstellen kann und Clients bei Bedarf abrufen können. Beispiele sind Dateiinhalte, Datenbankeinträge oder Protokolldateien. Ressourcen können Text (wie Code oder JSON) oder Binärdaten (wie Bilder oder PDFs) sein.

• **Prompts**: Dies sind vordefinierte Vorlagen, die vorgeschlagene Eingaben bieten und komplexere Workflows ermöglichen.

### Vorteile von MCP

MCP bietet bedeutende Vorteile für KI-Agenten:

• **Dynamische Werkzeugsuche**: Agenten können dynamisch eine Liste verfügbarer Werkzeuge von einem Server erhalten, zusammen mit Beschreibungen ihrer Funktionen. Im Gegensatz zu traditionellen APIs, die oft statische Codierung für Integrationen erfordern, sodass jede API-Änderung Codeaktualisierungen notwendig macht. MCP bietet einen „einmal integrieren“-Ansatz, der zu mehr Anpassungsfähigkeit führt.

• **Interoperabilität zwischen LLMs**: MCP funktioniert mit verschiedenen LLMs und bietet die Flexibilität, Kernmodelle zu wechseln, um bessere Leistungen zu evaluieren.

• **Standardisierte Sicherheit**: MCP beinhaltet eine standardisierte Authentifizierungsmethode, die die Skalierbarkeit beim Hinzufügen von Zugriffen auf weitere MCP-Server verbessert. Dies ist einfacher als das Verwalten verschiedener Schlüssel und Authentifizierungstypen für verschiedene traditionelle APIs.

### MCP Beispiel

![MCP Diagramm](../../../translated_images/de/mcp-diagram.e4ca1cbd551444a1.webp)

Stellen Sie sich vor, ein Nutzer möchte mit einem KI-Assistenten, der von MCP angetrieben wird, einen Flug buchen.

1. **Verbindung**: Der KI-Assistent (der MCP-Client) verbindet sich mit einem MCP-Server einer Fluggesellschaft.

2. **Werkzeugsuche**: Der Client fragt den MCP-Server der Fluggesellschaft: „Welche Werkzeuge haben Sie verfügbar?“ Der Server antwortet mit Werkzeugen wie „Flüge suchen“ und „Flüge buchen“.

3. **Werkzeugaufruf**: Sie bitten den KI-Assistenten, „Bitte suche einen Flug von Portland nach Honolulu“. Der KI-Assistent verwendet sein LLM, erkennt, dass er das Werkzeug „Flüge suchen“ aufrufen muss, und übergibt die relevanten Parameter (Abflugort, Zielort) an den MCP-Server.

4. **Ausführung und Antwort**: Der MCP-Server fungiert als Wrapper, ruft die interne Buchungs-API der Fluggesellschaft auf. Er empfängt dann die Fluginformationen (z.B. JSON-Daten) und sendet sie zurück an den KI-Assistenten.

5. **Weitere Interaktion**: Der KI-Assistent präsentiert die Flugoptionen. Nachdem Sie einen Flug ausgewählt haben, könnte der Assistent das Werkzeug „Flug buchen“ auf demselben MCP-Server aufrufen, um die Buchung abzuschließen.

## Agent-to-Agent Protokoll (A2A)

Während sich MCP auf die Verbindung von LLMs zu Werkzeugen konzentriert, geht das **Agent-to-Agent (A2A) Protokoll** einen Schritt weiter, indem es Kommunikation und Zusammenarbeit zwischen verschiedenen KI-Agenten ermöglicht. A2A verbindet KI-Agenten über verschiedene Organisationen, Umgebungen und Technologiestacks hinweg, um eine gemeinsame Aufgabe zu erfüllen.

Wir betrachten die Komponenten und Vorteile von A2A sowie ein Beispiel, wie es in unserer Reiseanwendung eingesetzt werden könnte.

### Kernkomponenten von A2A

A2A konzentriert sich darauf, Kommunikation zwischen Agenten zu ermöglichen und sie zusammenarbeiten zu lassen, um eine Teilaufgabe des Nutzers zu erfüllen. Jede Komponente des Protokolls trägt dazu bei:

#### Agentenkarte

Ähnlich wie ein MCP-Server eine Liste von Werkzeugen teilt, hat eine Agentenkarte:
- Den Namen des Agenten.
- Eine **Beschreibung der allgemeinen Aufgaben**, die er erfüllt.
- Eine **Liste spezifischer Fähigkeiten** mit Beschreibungen, die anderen Agenten (oder auch menschlichen Nutzern) helfen zu verstehen, wann und warum sie diesen Agenten aufrufen sollten.
- Die **aktuelle Endpunkt-URL** des Agenten.
- Die **Version** und **Fähigkeiten** des Agenten, wie Streaming-Antworten und Push-Benachrichtigungen.

#### Agenten-Ausführer

Der Agenten-Ausführer ist verantwortlich für das **Übergeben des Kontexts des Benutzerchats an den entfernten Agenten**. Der entfernte Agent benötigt dies, um die auszuführende Aufgabe zu verstehen. In einem A2A-Server verwendet ein Agent sein eigenes Large Language Model (LLM), um eingehende Anfragen zu analysieren und Aufgaben mit seinen eigenen internen Werkzeugen auszuführen.

#### Artefakt

Sobald ein entfernter Agent die angeforderte Aufgabe abgeschlossen hat, wird sein Arbeitsergebnis als Artefakt erstellt. Ein Artefakt **enthält das Ergebnis der Arbeit des Agenten**, eine **Beschreibung dessen, was erledigt wurde**, und den **Textkontext**, der durch das Protokoll gesendet wird. Nachdem das Artefakt gesendet wurde, wird die Verbindung zum entfernten Agenten geschlossen, bis dieser wieder benötigt wird.

#### Ereignis-Warteschlange

Diese Komponente wird zur **Handhabung von Updates und zum Übermitteln von Nachrichten** verwendet. Sie ist besonders in der Produktion agentischer Systeme wichtig, um zu verhindern, dass die Verbindung zwischen Agenten vor Abschluss einer Aufgabe geschlossen wird – vor allem wenn die Erledigung der Aufgabe längere Zeit in Anspruch nehmen kann.

### Vorteile von A2A

• **Verbesserte Zusammenarbeit**: Es ermöglicht Agenten verschiedener Anbieter und Plattformen, miteinander zu interagieren, Kontext zu teilen und zusammenzuarbeiten, was nahtlose Automatisierung über traditionell getrennte Systeme hinweg erleichtert.

• **Flexibilität bei der Modellauswahl**: Jeder A2A-Agent kann entscheiden, welches LLM er zur Bearbeitung seiner Anfragen verwendet, was optimierte oder feinabgestimmte Modelle pro Agent erlaubt – anders als eine einzige LLM-Verbindung in einigen MCP-Szenarien.

• **Integrierte Authentifizierung**: Die Authentifizierung ist direkt im A2A-Protokoll integriert und bietet einen robusten Sicherheitsrahmen für Agenteninteraktionen.

### A2A Beispiel

![A2A Diagramm](../../../translated_images/de/A2A-Diagram.8666928d648acc26.webp)

Erweitern wir unser Reisebuchungsszenario, diesmal mit A2A.

1. **Benutzeranfrage an Multi-Agenten**: Ein Benutzer interagiert mit einem „Reiseagent“-A2A Client/Agent, indem er sagt: „Bitte buche eine komplette Reise nach Honolulu für nächste Woche, inklusive Flüge, Hotel und Mietwagen“.

2. **Orchestrierung durch den Reiseagenten**: Der Reiseagent erhält diese komplexe Anfrage, verwendet sein LLM, um über die Aufgabe nachzudenken und bestimmt, dass er mit anderen spezialisierten Agenten interagieren muss.

3. **Kommunikation zwischen Agenten**: Der Reiseagent nutzt das A2A-Protokoll, um sich mit weiteren Agenten zu verbinden, wie einem „Fluglinien-Agenten“, einem „Hotel-Agenten“ und einem „Mietwagen-Agenten“, die von verschiedenen Unternehmen erstellt wurden.

4. **Delegierte Aufgabenbearbeitung**: Der Reiseagent sendet spezielle Aufgaben an die spezialisierten Agenten (z.B. „Finde Flüge nach Honolulu“, „Buche Hotel“, „Miete Auto“). Jeder dieser spezialisierten Agenten, die eigene LLMs nutzen und eigene Werkzeuge (die selbst MCP-Server sein können), erledigt seinen spezifischen Teil der Buchung.

5. **Konsolidierte Antwort**: Nachdem alle nachgelagerten Agenten ihre Aufgaben abgeschlossen haben, fasst der Reiseagent die Ergebnisse (Flugdetails, Hotelbestätigung, Mietwagenbuchung) zusammen und sendet eine umfassende chat-ähnliche Antwort zurück an den Benutzer.

## Natural Language Web (NLWeb)

Webseiten sind schon lange die primäre Möglichkeit für Nutzer, Informationen und Daten im Internet zuzugreifen.

Schauen wir uns die verschiedenen Komponenten von NLWeb, die Vorteile von NLWeb und ein Beispiel an, wie unser NLWeb durch unsere Reiseanwendung funktioniert.

### Komponenten von NLWeb

- **NLWeb Anwendung (Kern-Service-Code)**: Das System, das natürliche Sprachfragen verarbeitet. Es verbindet die verschiedenen Teile der Plattform, um Antworten zu erstellen. Man kann es sich als **Motor vorstellen, der die natürlichen Sprachfunktionen** einer Webseite antreibt.

- **NLWeb Protokoll**: Dies ist ein **einfaches Regelwerk für natürliche Sprachinteraktionen** mit einer Webseite. Es sendet Antworten im JSON-Format zurück (oft unter Verwendung von Schema.org). Zweck ist es, eine einfache Grundlage für das „KI-Web“ zu schaffen, ähnlich wie HTML das Teilen von Dokumenten online ermöglicht hat.

- **MCP Server (Model Context Protocol Endpunkt)**: Jede NLWeb-Installation arbeitet auch als **MCP-Server**. Das bedeutet, sie kann **Werkzeuge (wie eine „ask“-Methode) und Daten** mit anderen KI-Systemen teilen. Praktisch macht das die Inhalte und Funktionen der Webseite für KI-Agenten nutzbar, sodass die Webseite Teil des größeren „Agenten-Ökosystems“ wird.

- **Embedding-Modelle**: Diese Modelle werden verwendet, um **Webseiteninhalte in numerische Repräsentationen, sogenannte Vektoren (Embeddings), umzuwandeln**. Diese Vektoren erfassen Bedeutungen auf eine Weise, die Computer vergleichen und durchsuchen können. Sie werden in einer speziellen Datenbank gespeichert, und Nutzer können wählen, welches Embedding-Modell sie verwenden möchten.

- **Vektor-Datenbank (Suchmechanismus)**: Diese Datenbank **speichert die Embeddings der Webseiteninhalte**. Wenn jemand eine Frage stellt, durchsucht NLWeb die Vektordatenbank, um schnell die relevantesten Informationen zu finden. Es liefert eine schnelle Liste möglicher Antworten, nach Ähnlichkeit sortiert. NLWeb arbeitet mit verschiedenen Vektorspeichersystemen wie Qdrant, Snowflake, Milvus, Azure AI Search und Elasticsearch.

### NLWeb am Beispiel

![NLWeb](../../../translated_images/de/nlweb-diagram.c1e2390b310e5fe4.webp)

Betrachten wir erneut unsere Reisebuchungswebseite, diesmal von NLWeb angetrieben.

1. **Datenaufnahme**: Die vorhandenen Produktkataloge der Reisewebseite (z.B. Fluglisten, Hotelbeschreibungen, Tourpakete) werden mit Schema.org formatiert oder per RSS-Feeds geladen. Die Tools von NLWeb nehmen diese strukturierten Daten auf, erstellen Embeddings und speichern sie in einer lokalen oder entfernten Vektor-Datenbank.

2. **Natürlichsprachliche Anfrage (Mensch)**: Ein Nutzer besucht die Webseite und gibt statt der Navigation durch Menüs Text in ein Chat-Interface ein: „Finde ein familienfreundliches Hotel in Honolulu mit Pool für nächste Woche“.

3. **NLWeb Verarbeitung**: Die NLWeb-Anwendung erhält diese Anfrage. Sie sendet die Anfrage an ein LLM zur Verständnisanalyse und durchsucht gleichzeitig die Vektordatenbank nach relevanten Hotelangeboten.

4. **Genauere Ergebnisse**: Das LLM hilft bei der Interpretation der Suchergebnisse aus der Datenbank, identifiziert basierend auf „familienfreundlich“, „Pool“ und „Honolulu“ die besten Treffer und formatiert dann eine natürlichsprachliche Antwort. Wichtig ist, dass sich die Antwort auf tatsächliche Hotels aus dem Katalog der Webseite bezieht und keine erfundenen Informationen enthält.

5. **KI-Agent Interaktion**: Da NLWeb als MCP-Server fungiert, könnte ein externer KI-Reiseagent auch eine Verbindung zur NLWeb-Instanz dieser Webseite herstellen. Der KI-Agent könnte dann die `ask`-MCP-Methode verwenden, um die Webseite direkt abzufragen: `ask("Gibt es von Hotel empfohlene vegane Restaurants im Raum Honolulu?")`. Die NLWeb-Instanz würde dies verarbeiten, ihre Datenbank mit Restaurantinformationen (sofern geladen) nutzen und eine strukturierte JSON-Antwort zurückgeben.

### Haben Sie weitere Fragen zu MCP/A2A/NLWeb?

Treten Sie dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten beantwortet zu bekommen.

## Ressourcen

- [MCP für Einsteiger](https://aka.ms/mcp-for-beginners)  
- [MCP Dokumentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Vorherige Lektion

[KI-Agenten in Produktion](../10-ai-agents-production/README.md)

## Nächste Lektion

[Kontext-Engineering für KI-Agenten](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->