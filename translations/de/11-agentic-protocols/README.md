# Verwendung agentischer Protokolle (MCP, A2A und NLWeb)

[![Agentische Protokolle](../../../translated_images/de/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klicken Sie auf das Bild oben, um das Video zu dieser Lektion anzusehen)_

Mit zunehmender Verbreitung von KI-Agenten wächst auch der Bedarf an Protokollen, die Standardisierung, Sicherheit und offene Innovation gewährleisten. In dieser Lektion behandeln wir drei Protokolle, die diesen Bedarf decken sollen - Model Context Protocol (MCP), Agent to Agent (A2A) und Natural Language Web (NLWeb).

## Einführung

In dieser Lektion behandeln wir:

• Wie **MCP** KI-Agenten ermöglicht, auf externe Tools und Daten zuzugreifen, um Aufgaben für Benutzer zu erledigen.

•  Wie **A2A** Kommunikation und Zusammenarbeit zwischen verschiedenen KI-Agenten ermöglicht.

• Wie **NLWeb** natürliche Sprachschnittstellen für jede Website bereitstellt, wodurch KI-Agenten Inhalte entdecken und mit ihnen interagieren können.

## Lernziele

• **Identifizieren** Sie den Kernzweck und die Vorteile von MCP, A2A und NLWeb im Kontext von KI-Agenten.

• **Erklären** Sie, wie jedes Protokoll die Kommunikation und Interaktion zwischen LLMs, Tools und anderen Agenten erleichtert.

• **Erkennen** Sie die unterschiedlichen Rollen, die jedes Protokoll beim Aufbau komplexer agentischer Systeme spielt.

## Model Context Protocol

Das **Model Context Protocol (MCP)** ist ein offener Standard, der eine standardisierte Möglichkeit bietet, Anwendungen Kontext und Tools für LLMs bereitzustellen. Dadurch wird ein „universeller Adapter“ für verschiedene Datenquellen und Tools ermöglicht, mit dem sich KI-Agenten konsistent verbinden können.

Let’s look at the components of MCP, the benefits compared to direct API usage, and an example of how AI agents might use an MCP server.

### MCP Kernkomponenten

MCP basiert auf einer **Client-Server-Architektur** und die Kernkomponenten sind:

• **Hosts** sind LLM-Anwendungen (zum Beispiel ein Code-Editor wie VSCode), die die Verbindungen zu einem MCP-Server initiieren.

• **Clients** sind Komponenten innerhalb der Host-Anwendung, die Eins-zu-eins-Verbindungen zu Servern aufrechterhalten.

• **Servers** sind leichtgewichtige Programme, die bestimmte Fähigkeiten bereitstellen.

Im Protokoll sind drei Kernprimitive enthalten, die die Fähigkeiten eines MCP-Servers darstellen:

• **Tools**: Dies sind einzelne Aktionen oder Funktionen, die ein KI-Agent aufrufen kann, um eine Aufgabe auszuführen. Beispielsweise könnte ein Wetterdienst ein "get weather"-Tool bereitstellen, oder ein E‑Commerce-Server ein "purchase product"-Tool. MCP-Server veröffentlichen in ihrer Capability-Liste den Namen jedes Tools, die Beschreibung und das Eingabe-/Ausgabe-Schema.

• **Resources**: Dies sind schreibgeschützte Datenelemente oder Dokumente, die ein MCP-Server bereitstellen kann und die Clients bei Bedarf abrufen können. Beispiele sind Dateiinhalte, Datenbankeinträge oder Log-Dateien. Resources können Text (wie Code oder JSON) oder Binärdaten (wie Bilder oder PDFs) sein.

• **Prompts**: Dies sind vordefinierte Vorlagen, die vorgeschlagene Prompt-Texte liefern und komplexere Workflows ermöglichen.

### Vorteile von MCP

MCP bietet erhebliche Vorteile für KI-Agenten:

• **Dynamische Tool-Erkennung**: Agenten können dynamisch eine Liste verfügbarer Tools von einem Server erhalten, zusammen mit Beschreibungen ihrer Funktionen. Dies steht im Gegensatz zu traditionellen APIs, die oft statische Integration per Code erfordern, sodass jede API-Änderung Code-Anpassungen notwendig macht. MCP bietet einen „einmal integrieren“-Ansatz, der zu größerer Anpassungsfähigkeit führt.

• **Interoperabilität zwischen LLMs**: MCP funktioniert über verschiedene LLMs hinweg und bietet die Flexibilität, Kernmodelle auszutauschen, um eine bessere Leistung zu erreichen.

• **Standardisierte Sicherheit**: MCP enthält eine standardisierte Authentifizierungsmethode, die die Skalierbarkeit beim Hinzufügen weiterer MCP-Server verbessert. Das ist einfacher, als verschiedene Schlüssel und Authentifizierungstypen für verschiedene traditionelle APIs zu verwalten.

### MCP-Beispiel

![MCP-Diagramm](../../../translated_images/de/mcp-diagram.e4ca1cbd551444a1.webp)

Stellen Sie sich vor, ein Benutzer möchte mit einem von MCP unterstützten KI-Assistenten einen Flug buchen.

1. **Verbindung**: Der KI-Assistent (der MCP-Client) verbindet sich mit einem von einer Fluggesellschaft bereitgestellten MCP-Server.

2. **Tool-Erkennung**: Der Client fragt den MCP-Server der Fluggesellschaft, "What tools do you have available?" Der Server antwortet mit Tools wie "search flights" und "book flights".

3. **Tool-Aufruf**: Sie bitten dann den KI-Assistenten, "Please search for a flight from Portland to Honolulu." Der KI-Assistent identifiziert unter Nutzung seines LLM, dass er das "search flights"-Tool aufrufen muss, und übergibt dem MCP-Server die relevanten Parameter (Abflugort, Ziel).

4. **Ausführung und Antwort**: Der MCP-Server fungiert als Wrapper und führt den eigentlichen Aufruf an die interne Buchungs-API der Fluggesellschaft aus. Er erhält dann die Fluginformationen (z. B. JSON-Daten) und sendet sie an den KI-Assistenten zurück.

5. **Weitere Interaktion**: Der KI-Assistent stellt die Flugoptionen dar. Sobald Sie einen Flug auswählen, könnte der Assistent auf demselben MCP-Server das "book flight"-Tool aufrufen und die Buchung abschließen.

## Agent-to-Agent-Protokoll (A2A)

Während MCP den Fokus auf die Verbindung von LLMs mit Tools legt, geht das **Agent-to-Agent (A2A) Protokoll** einen Schritt weiter, indem es Kommunikation und Zusammenarbeit zwischen verschiedenen KI-Agenten ermöglicht.  A2A verbindet KI-Agenten über verschiedene Organisationen, Umgebungen und Technologiestacks hinweg, um eine gemeinsame Aufgabe zu erledigen.

We’ll examine the components and benefits of A2A, along with an example of how it could be applied in our travel application.

### A2A Kernkomponenten

A2A konzentriert sich darauf, die Kommunikation zwischen Agenten zu ermöglichen und sie zusammenarbeiten zu lassen, um eine Teilaufgabe des Benutzers zu erledigen. Jede Komponente des Protokolls trägt dazu bei:

#### Agent Card

Ähnlich wie ein MCP-Server eine Liste von Tools teilt, enthält eine Agent Card:
- Den Namen des Agenten .
- Eine **Beschreibung der allgemeinen Aufgaben**, die er erfüllt.
- Eine **Liste spezifischer Fähigkeiten** mit Beschreibungen, um anderen Agenten (oder sogar menschlichen Nutzern) zu helfen zu verstehen, wann und warum sie diesen Agenten aufrufen sollten.
- Die **aktuelle Endpoint-URL** des Agenten
- Die **Version** und **Fähigkeiten** des Agenten, wie Streaming-Antworten und Push-Benachrichtigungen.

#### Agent Executor

Der Agent Executor ist verantwortlich für **das Weitergeben des Kontexts des Benutzerchats an den entfernten Agenten**, der entfernte Agent benötigt dies, um die Aufgabe, die erledigt werden muss, zu verstehen. In einem A2A-Server verwendet ein Agent sein eigenes Large Language Model (LLM), um eingehende Anfragen zu parsen und Aufgaben mit seinen eigenen internen Tools auszuführen.

#### Artifact

Sobald ein entfernter Agent die angeforderte Aufgabe abgeschlossen hat, wird sein Arbeitsergebnis als Artifact erstellt.  Ein Artifact **enthält das Ergebnis der Arbeit des Agenten**, eine **Beschreibung dessen, was erledigt wurde**, und den **Textkontext**, der über das Protokoll gesendet wird. Nachdem das Artifact gesendet wurde, wird die Verbindung zum entfernten Agenten geschlossen, bis sie wieder benötigt wird.

#### Event Queue

Diese Komponente wird für **das Verwalten von Updates und das Weiterleiten von Nachrichten** verwendet. Sie ist insbesondere in der Produktion für agentische Systeme wichtig, um zu verhindern, dass die Verbindung zwischen Agenten geschlossen wird, bevor eine Aufgabe abgeschlossen ist, insbesondere wenn die Aufgabenerledigung längere Zeit in Anspruch nehmen kann.

### Vorteile von A2A

• **Erweiterte Zusammenarbeit**: Es ermöglicht Agenten verschiedener Anbieter und Plattformen, miteinander zu interagieren, Kontext zu teilen und zusammenzuarbeiten, wodurch nahtlose Automatisierung über traditionell getrennte Systeme hinweg erleichtert wird.

• **Flexibilität bei der Modellauswahl**: Jeder A2A-Agent kann entscheiden, welches LLM er zur Bearbeitung seiner Anfragen einsetzt, wodurch pro Agent optimierte oder feinabgestimmte Modelle möglich sind, im Gegensatz zu einer einzelnen LLM-Verbindung in einigen MCP-Szenarien.

• **Integrierte Authentifizierung**: Die Authentifizierung ist direkt in das A2A-Protokoll integriert und bietet einen robusten Sicherheitsrahmen für Agenteninteraktionen.

### A2A-Beispiel

![A2A-Diagramm](../../../translated_images/de/A2A-Diagram.8666928d648acc26.webp)

Erweitern wir unser Szenario zur Reisebuchung, diesmal unter Verwendung von A2A.

1. **Benutzeranfrage an Multi-Agenten**: Ein Benutzer interagiert mit einem "Travel Agent" A2A-Client/Agent, zum Beispiel mit der Bitte: "Please book an entire trip to Honolulu for next week, including flights, a hotel, and a rental car".

2. **Orchestrierung durch den Travel Agent**: Der Travel Agent empfängt diese komplexe Anfrage. Er verwendet sein LLM, um über die Aufgabe zu schließen und festzustellen, dass er mit anderen spezialisierten Agenten interagieren muss.

3. **Inter-Agenten-Kommunikation**: Der Travel Agent verwendet dann das A2A-Protokoll, um sich mit nachgelagerten Agenten zu verbinden, wie einem "Airline Agent," einem "Hotel Agent," und einem "Car Rental Agent" die von verschiedenen Unternehmen erstellt wurden.

4. **Delegierte Aufgabenausführung**: Der Travel Agent sendet spezifische Aufgaben an diese spezialisierten Agenten (z. B. "Find flights to Honolulu," "Book a hotel," "Rent a car"). Jeder dieser spezialisierten Agenten, der sein eigenes LLM betreibt und seine eigenen Tools nutzt (die selbst MCP-Server sein können), führt seinen jeweiligen Teil der Buchung aus.

5. **Konsolidierte Antwort**: Sobald alle nachgelagerten Agenten ihre Aufgaben abgeschlossen haben, fasst der Travel Agent die Ergebnisse zusammen (Flugdetails, Hotelbestätigung, Mietwagenbuchung) und sendet eine umfassende, im Chat-Stil gehaltene Antwort an den Benutzer.

## Natural Language Web (NLWeb)

Websites sind seit langem der primäre Weg für Nutzer, um auf Informationen und Daten im Internet zuzugreifen.

Lassen Sie uns die verschiedenen Komponenten von NLWeb, die Vorteile von NLWeb und ein Beispiel dafür ansehen, wie unser NLWeb anhand unserer Reiseanwendung funktioniert.

### Komponenten von NLWeb

- **NLWeb Application (Core Service Code)**: Das System, das natürliche Sprachfragen verarbeitet. Es verbindet die verschiedenen Teile der Plattform, um Antworten zu erstellen. Sie können es als die **Engine betrachten, die die Funktionen für natürliche Sprache** einer Website antreibt.

- **NLWeb Protocol**: Dies ist ein **grundlegendes Regelwerk für die Interaktion in natürlicher Sprache** mit einer Website. Es sendet Antworten im JSON-Format zurück (oft unter Verwendung von Schema.org). Sein Zweck ist es, eine einfache Grundlage für das „AI Web“ zu schaffen, ähnlich wie HTML das Teilen von Dokumenten online ermöglichte.

- **MCP Server (Model Context Protocol Endpoint)**: Jede NLWeb-Konfiguration fungiert auch als **MCP-Server**. Das bedeutet, dass sie **Tools (wie eine "ask"-Methode) und Daten** mit anderen KI-Systemen teilen kann. In der Praxis macht dies die Inhalte und Fähigkeiten der Website für KI-Agenten nutzbar und erlaubt der Seite, Teil des größeren „Agenten-Ökosystems“ zu werden.

- **Embedding Models**: Diese Modelle werden verwendet, um **Website-Inhalte in numerische Repräsentationen zu konvertieren, die Vektoren genannt werden** (Embeddings). Diese Vektoren erfassen Bedeutung auf eine Weise, die Computer vergleichen und durchsuchen können. Sie werden in einer speziellen Datenbank gespeichert, und Benutzer können wählen, welches Embedding-Modell sie verwenden möchten.

- **Vector Database (Retrieval Mechanism)**: Diese Datenbank **speichert die Embeddings der Website-Inhalte**. Wenn jemand eine Frage stellt, prüft NLWeb die Vektordatenbank, um schnell die relevantesten Informationen zu finden. Sie liefert eine schnelle Liste möglicher Antworten, sortiert nach Ähnlichkeit. NLWeb arbeitet mit verschiedenen Vektor-Speichersystemen wie Qdrant, Snowflake, Milvus, Azure AI Search und Elasticsearch.

### NLWeb am Beispiel

![NLWeb-Diagramm](../../../translated_images/de/nlweb-diagram.c1e2390b310e5fe4.webp)

Betrachten wir erneut unsere Reisebuchungs-Website, die diesmal von NLWeb angetrieben wird.

1. **Datenaufnahme**: Die vorhandenen Produktkataloge der Reise-Website (z. B. Fluglisten, Hotelbeschreibungen, Pauschalangebote) werden mit Schema.org formatiert oder über RSS-Feeds geladen. Die Tools von NLWeb nehmen diese strukturierten Daten auf, erstellen Embeddings und speichern sie in einer lokalen oder entfernten Vektordatenbank.

2. **Natürliche Sprachabfrage (Mensch)**: Ein Benutzer besucht die Website und tippt in ein Chat-Interface, anstatt Menüs zu durchsuchen: "Find me a family-friendly hotel in Honolulu with a pool for next week".

3. **NLWeb-Verarbeitung**: Die NLWeb-Anwendung empfängt diese Anfrage. Sie sendet die Anfrage zur Analyse an ein LLM und durchsucht gleichzeitig ihre Vektordatenbank nach relevanten Hotelangeboten.

4. **Genaue Ergebnisse**: Das LLM hilft dabei, die Suchergebnisse aus der Datenbank zu interpretieren, die besten Treffer anhand der Kriterien „familienfreundlich“, „Pool“ und „Honolulu“ zu identifizieren und dann eine Antwort in natürlicher Sprache zu formatieren. Wichtig ist, dass die Antwort sich auf tatsächliche Hotels aus dem Website-Katalog bezieht und erfundene Informationen vermeidet.

5. **Interaktion mit KI-Agenten**: Da NLWeb als MCP-Server fungiert, könnte sich auch ein externer KI-Reiseagent mit der NLWeb-Instanz dieser Website verbinden. Der KI-Agent könnte dann die `ask` MCP-Methode verwenden, um die Website direkt abzufragen: `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")`. Die NLWeb-Instanz würde dies verarbeiten, ihre Datenbank mit Restaurantinformationen (falls geladen) nutzen und eine strukturierte JSON-Antwort zurückgeben.

### Haben Sie weitere Fragen zu MCP/A2A/NLWeb?

Treten Sie dem [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Antworten auf Ihre Fragen zu KI-Agenten zu erhalten.

## Ressourcen

- [MCP für Einsteiger](https://aka.ms/mcp-for-beginners)  
- [MCP-Dokumentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb-Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Originalsprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Für Missverständnisse oder Fehlinterpretationen, die sich aus der Verwendung dieser Übersetzung ergeben, übernehmen wir keine Haftung.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->