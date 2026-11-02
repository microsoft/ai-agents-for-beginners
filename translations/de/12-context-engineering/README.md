# Kontext-Engineering für KI-Agenten

[![Kontext-Engineering](../../../translated_images/de/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

Das Verständnis der Komplexität der Anwendung, für die Sie einen KI-Agenten erstellen, ist wichtig, um einen zuverlässigen Agenten zu entwickeln. Wir müssen KI-Agenten bauen, die Informationen effektiv verwalten, um komplexe Anforderungen zu erfüllen, die über die Prompt-Entwicklung hinausgehen.

In dieser Lektion werden wir uns ansehen, was Kontext-Engineering ist und welche Rolle es beim Bau von KI-Agenten spielt.

## Einführung

Diese Lektion behandelt:

• **Was Kontext-Engineering ist** und warum es sich von Prompt-Engineering unterscheidet.

• **Strategien für effektives Kontext-Engineering**, einschließlich wie man Informationen schreibt, auswählt, komprimiert und isoliert.

• **Häufige Kontextfehler**, die Ihren KI-Agenten entgleisen lassen können, und wie man sie behebt.

## Lernziele

Nach Abschluss dieser Lektion werden Sie verstehen, wie man:

• **Kontext-Engineering definiert** und es vom Prompt-Engineering unterscheidet.

• **Die wichtigsten Komponenten von Kontext** in Anwendungen mit großen Sprachmodellen (LLM) identifiziert.

• **Strategien zum Schreiben, Auswählen, Komprimieren und Isolieren von Kontext anwendet**, um die Leistung des Agenten zu verbessern.

• **Häufige Kontextfehler erkennt**, wie Vergiftung, Ablenkung, Verwirrung und Konflikte, und Gegenmaßnahmen umsetzt.

## Was ist Kontext-Engineering?

Für KI-Agenten ist der Kontext das, was die Planung des Agenten steuert, bestimmte Aktionen auszuführen. Kontext-Engineering ist die Praxis, sicherzustellen, dass der KI-Agent die richtigen Informationen hat, um den nächsten Schritt der Aufgabe abzuschließen. Das Kontextfenster ist in seiner Größe begrenzt, daher müssen wir als Entwickler Systeme und Prozesse bauen, um Informationen im Kontextfenster hinzuzufügen, zu entfernen und zu verdichten.

### Prompt-Engineering vs. Kontext-Engineering

Prompt-Engineering konzentriert sich auf eine einzelne statische Anweisung, um die KI-Agenten mit einem Regelwerk effektiv zu leiten. Kontext-Engineering hingegen beschreibt, wie ein dynamischer Informationsbestand, einschließlich der ursprünglichen Eingabeaufforderung, verwaltet wird, um sicherzustellen, dass der KI-Agent im Zeitverlauf alles Nötige hat. Die Hauptidee des Kontext-Engineerings ist, diesen Prozess wiederholbar und zuverlässig zu machen.

### Arten von Kontext

[![Arten von Kontext](../../../translated_images/de/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Es ist wichtig zu bedenken, dass Kontext nicht nur eine Sache ist. Die Informationen, die ein KI-Agent benötigt, können aus verschiedenen Quellen stammen, und es liegt an uns, sicherzustellen, dass der Agent Zugriff auf diese Quellen hat:

Die Arten von Kontext, die ein KI-Agent möglicherweise verwalten muss, umfassen:

• **Anweisungen:** Diese sind wie die „Regeln“ des Agenten – Prompts, Systemnachrichten, Few-Shot-Beispiele (die der KI zeigen, wie etwas gemacht wird) und Beschreibungen von Werkzeugen, die sie verwenden kann. Hier verschneiden sich die Schwerpunkte von Prompt-Engineering und Kontext-Engineering.

• **Wissen:** Dies umfasst Fakten, Informationen aus Datenbanken oder langfristige Erinnerungen, die der Agent gesammelt hat. Dazu gehört auch die Integration eines Retrieval Augmented Generation (RAG)-Systems, falls ein Agent Zugriff auf verschiedene Wissensspeicher und Datenbanken benötigt.

• **Werkzeuge:** Dies sind Definitionen von externen Funktionen, APIs und MCP-Servern, die der Agent aufrufen kann, sowie das Feedback (Ergebnisse), das er durch deren Nutzung erhält.

• **Gesprächshistorie:** Der laufende Dialog mit einem Nutzer. Mit der Zeit werden diese Gespräche länger und komplexer, was bedeutet, dass sie im Kontextfenster Platz einnehmen.

• **Benutzervorlieben:** Informationen über die Vorlieben oder Abneigungen eines Nutzers, die über die Zeit gesammelt wurden. Diese können gespeichert und bei wichtigen Entscheidungen, die dem Nutzer helfen, abgerufen werden.

## Strategien für effektives Kontext-Engineering

### Planungsstrategien

[![Beste Praktiken beim Kontext-Engineering](../../../translated_images/de/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Gutes Kontext-Engineering beginnt mit guter Planung. Hier ist ein Ansatz, der Ihnen hilft, über die Anwendung des Konzepts Kontext-Engineering nachzudenken:

1. **Klare Ergebnisse definieren** – Die Ergebnisse der Aufgaben, die KI-Agenten zugewiesen werden, sollten klar definiert sein. Beantworten Sie die Frage – „Wie wird die Welt aussehen, wenn der KI-Agent seine Aufgabe erledigt hat?“ Anders gesagt, welche Veränderung, Information oder Antwort soll der Benutzer nach der Interaktion mit dem KI-Agenten erhalten.
2. **Den Kontext kartieren** – Sobald Sie die Ergebnisse des KI-Agenten definiert haben, müssen Sie die Frage beantworten: „Welche Informationen benötigt der KI-Agent, um diese Aufgabe abzuschließen?“ So können Sie den Kontext kartieren, wo diese Informationen gefunden werden können.
3. **Kontext-Pipelines erstellen** – Nachdem Sie wissen, wo die Informationen sind, müssen Sie beantworten: „Wie wird der Agent diese Informationen erhalten?“ Dies kann auf verschiedene Weise geschehen, z. B. mit RAG, Einsatz von MCP-Servern und anderen Werkzeugen.

### Praktische Strategien

Planung ist wichtig, aber sobald Informationen in das Kontextfenster unseres Agenten fließen, brauchen wir praktische Strategien, um sie zu verwalten:

#### Verwaltung des Kontexts

Während einige Informationen automatisch zum Kontextfenster hinzugefügt werden, geht es beim Kontext-Engineering darum, eine aktivere Rolle bei dieser Information einzunehmen. Dies kann durch einige Strategien erfolgen:

 1. **Agenten-Kladden**
 Dies erlaubt einem KI-Agenten, während einer einzelnen Sitzung Notizen zu relevanten Informationen über aktuelle Aufgaben und Nutzerinteraktionen zu machen. Dies sollte außerhalb des Kontextfensters in einer Datei oder einem Laufzeitobjekt existieren, das der Agent später in dieser Sitzung bei Bedarf abrufen kann.

 2. **Erinnerungen**
 Kladden sind gut, um Informationen außerhalb des Kontextfensters einer einzelnen Sitzung zu verwalten. Erinnerungen ermöglichen es Agenten, relevante Informationen über mehrere Sitzungen hinweg zu speichern und abzurufen. Dies könnte Zusammenfassungen, Benutzervorlieben und Feedback für zukünftige Verbesserungen umfassen.

 3. **Kontext komprimieren**
  Sobald das Kontextfenster wächst und sich seinem Limit nähert, können Techniken wie Zusammenfassungen und Kürzungen eingesetzt werden. Dazu gehört, entweder nur die relevantesten Informationen zu behalten oder ältere Nachrichten zu entfernen.
  
 4. **Multi-Agenten-Systeme**
  Die Entwicklung von Multi-Agenten-Systemen ist eine Form von Kontext-Engineering, da jeder Agent sein eigenes Kontextfenster hat. Wie dieser Kontext geteilt und an verschiedene Agenten weitergegeben wird, ist eine weitere Planungskomponente beim Bau dieser Systeme.
  
 5. **Sandbox-Umgebungen**
  Wenn ein Agent Code ausführen oder große Mengen an Informationen in einem Dokument verarbeiten muss, kann dies viele Tokens beanspruchen, um die Ergebnisse zu verarbeiten. Anstatt alles im Kontextfenster zu speichern, kann der Agent eine Sandbox-Umgebung verwenden, die diesen Code ausführt und nur die Ergebnisse sowie andere relevante Informationen liest.
  
 6. **Laufzeitstatus-Objekte**
   Dies geschieht durch das Erstellen von Informationscontainern, um Situationen zu verwalten, in denen der Agent auf bestimmte Informationen zugreifen muss. Für eine komplexe Aufgabe würde dies es einem Agenten ermöglichen, Ergebnisse jeder Teilaufgabe Schritt für Schritt zu speichern, wobei der Kontext nur mit dieser spezifischen Teilaufgabe verbunden bleibt.

#### Kontext überprüfen

Nachdem Sie eine dieser Strategien angewandt haben, lohnt es sich zu überprüfen, was der nächste Modellaufruf tatsächlich erhalten hat. Eine nützliche Debugging-Frage lautet:

> Hat der Agent zu viel Kontext geladen, den falschen Kontext oder Kontext, den er brauchte, aber verpasst hat?

Sie müssen keine rohen Prompts, Werkzeugausgaben oder Speicherdaten protokollieren, um diese Frage zu beantworten. In der Produktion bevorzugen Sie kleine Kontextinspektionsprotokolle, die Zählungen, IDs, Hashes und Richtlinienlabels erfassen:

- **Auswahl:** Verfolgen Sie, wie viele Kandidaten-Chunks, Werkzeuge oder Erinnerungen berücksichtigt wurden, wie viele ausgewählt wurden und welche Regel oder Punktzahl die anderen herausfilterte.
- **Kompression:** Protokollieren Sie die Quellbereichs- oder Trace-ID, die Zusammenfassungs-ID, eine geschätzte Tokenanzahl vor und nach der Kompression und ob der rohe Inhalt vom nächsten Aufruf ausgeschlossen wurde.
- **Isolation:** Notieren Sie, welche Teilaufgabe in einem separaten Agenten, einer Sitzung oder Sandbox ausgeführt wurde, welche abgegrenzte Zusammenfassung zurückgegeben wurde und ob große Werkzeugaustritte außerhalb des Kontextes des Hauptagenten blieben.
- **Speicher und RAG:** Speichern Sie IDs von Abrufdokumenten, Speicher-IDs, Scores, ausgewählte IDs und Redaktionsstatus statt des vollständigen abgerufenen Textes.
- **Sicherheit und Datenschutz:** Bevorzugen Sie Hashes, IDs, Token-Buckets und Richtlinienlabels gegenüber sensiblen Prompt-Texten, Werkzeugargumenten, Werkzeugergebnissen oder Benutzer-Speicherinhalten.

Das Ziel ist nicht, mehr Kontext zu behalten. Es ist, genügend Beweise zu hinterlassen, damit ein Entwickler erkennen kann, welche Kontextstrategie ausgeführt wurde und ob sie den nächsten Modellaufruf wie beabsichtigt verändert hat.

### Beispiel für Kontext-Engineering

Angenommen, wir möchten, dass ein KI-Agent **„mir eine Reise nach Paris bucht“**.

• Ein einfacher Agent, der nur Prompt-Engineering nutzt, könnte einfach antworten: **„Okay, wann möchtest du nach Paris reisen?“** Er verarbeitet nur die direkte Frage des Nutzers zum Zeitpunkt der Anfrage.

• Ein Agent, der die in der Lektion beschriebenen Strategien des Kontext-Engineerings nutzt, würde viel mehr tun. Bevor er überhaupt antwortet, könnte sein System:

  ◦ **Ihren Kalender prüfen** auf verfügbare Daten (Echtzeit-Daten abfragen).

 ◦ **Frühere Reisepräferenzen abrufen** (aus Langzeiterinnerung), z. B. Ihre bevorzugte Fluggesellschaft, Budget oder ob Sie Direktflüge bevorzugen.

 ◦ **Verfügbare Werkzeuge identifizieren** für Flug- und Hotelbuchung.

- Dann könnte eine beispielhafte Antwort lauten: „Hey [Ihr Name]! Ich sehe, Sie sind in der ersten Oktoberwoche frei. Soll ich nach Direktflügen nach Paris auf [bevorzugter Fluggesellschaft] innerhalb Ihres üblichen Budgets von [Budget] suchen?“ Diese reichere, kontextbewusste Antwort demonstriert die Kraft des Kontext-Engineerings.

## Häufige Kontextfehler

### Kontextvergiftung

**Was es ist:** Wenn eine Halluzination (falsche Information, die das LLM generiert) oder ein Fehler in den Kontext gelangt und wiederholt referenziert wird, was dazu führt, dass der Agent unmögliche Ziele verfolgt oder unsinnige Strategien entwickelt.

**Was zu tun ist:** Implementieren Sie **Kontextvalidierung** und **Quarantäne**. Überprüfen Sie Informationen, bevor sie in den Langzeitspeicher aufgenommen werden. Wenn eine potenzielle Vergiftung erkannt wird, starten Sie neue Kontextstränge, um die Verbreitung der schlechten Informationen zu verhindern.

**Beispiel Reisebuchung:** Ihr Agent halluziniert einen **Direktflug von einem kleinen lokalen Flughafen zu einer weit entfernten internationalen Stadt**, die tatsächlich keine internationalen Flüge anbietet. Diese nicht existierende Flugangabe wird im Kontext gespeichert. Später, wenn Sie den Agenten mit der Buchung beauftragen, versucht er wiederholt, Tickets für diese unmögliche Route zu finden, was zu fortlaufenden Fehlern führt.

**Lösung:** Implementieren Sie einen Schritt, der **Flugexistenz und Routen mit einer Echtzeit-API überprüft**, _bevor_ die Flugdaten dem Arbeitskontext des Agenten hinzugefügt werden. Wenn die Validierung fehlschlägt, wird die fehlerhafte Information „in Quarantäne“ gestellt und nicht weiter verwendet.

### Kontext-Ablenkung

**Was es ist:** Wenn der Kontext so groß wird, dass sich das Modell zu sehr auf die akkumulierte Historie konzentriert, statt auf das, was es während des Trainings gelernt hat, was zu wiederholten oder unhilfreichen Aktionen führt. Modelle können Fehler machen, noch bevor das Kontextfenster voll ist.

**Was zu tun ist:** Verwenden Sie **Kontextzusammenfassung**. Komprimieren Sie periodisch die angesammelten Informationen zu kürzeren Zusammenfassungen, die wichtige Details behalten und redundante Historie entfernen. Dies hilft, den Fokus „zurückzusetzen“.

**Beispiel Reisebuchung:** Sie haben lange über verschiedene Traumreiseziele gesprochen, inklusive einer detaillierten Schilderung Ihrer Rucksackreise vor zwei Jahren. Wenn Sie schließlich bitten, **„einen günstigen Flug für nächsten Monat zu finden,“** verzettelt sich der Agent in alten, irrelevanten Details und fragt immer wieder nach Ihrer Ausrüstung oder vergangenen Reiserouten, anstatt Ihre aktuelle Anfrage zu berücksichtigen.

**Lösung:** Nach einer bestimmten Anzahl von Interaktionen oder wenn der Kontext zu groß wird, sollte der Agent **die neuesten und relevantesten Teile des Gesprächs zusammenfassen** – mit Fokus auf Ihre aktuellen Reisedaten und das Ziel – und diese kondensierte Zusammenfassung für den nächsten LLM-Aufruf verwenden, während die weniger relevanten historischen Chats verworfen werden.

### Kontext-Verwirrung

**Was es ist:** Wenn unnötiger Kontext, oft in Form von zu vielen verfügbaren Werkzeugen, das Modell dazu bringt, schlechte Antworten zu generieren oder irrelevante Werkzeuge aufzurufen. Kleinere Modelle sind besonders anfällig dafür.

**Was zu tun ist:** Implementieren Sie **Werkzeug-Auswahlmanagement** mit RAG-Techniken. Speichern Sie Werkzeugbeschreibungen in einer Vektor-Datenbank und wählen Sie _nur_ die relevantesten Werkzeuge für jede spezifische Aufgabe aus. Forschungen zeigen, dass die Beschränkung der Werkzeugauswahl auf weniger als 30 optimal ist.

**Beispiel Reisebuchung:** Ihr Agent hat Zugriff auf dutzende Werkzeuge: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations` usw. Sie fragen: **„Wie bewegt man sich am besten in Paris?“** Aufgrund der Vielzahl der Werkzeuge ist der Agent verwirrt und versucht, `book_flight` _innerhalb_ von Paris aufzurufen oder `rent_car`, obwohl Sie öffentlichen Nahverkehr bevorzugen, weil sich die Werkzeugbeschreibungen überschneiden können oder er einfach nicht das beste Werkzeug erkennen kann.

**Lösung:** Verwenden Sie **RAG über Werkzeugbeschreibungen**. Wenn Sie nach Fortbewegungsmöglichkeiten in Paris fragen, ruft das System dynamisch _nur_ die relevantesten Werkzeuge wie `rent_car` oder `public_transport_info` basierend auf Ihrer Anfrage ab und präsentiert eine fokussierte „Ausstattung“ an Werkzeugen für das LLM.

### Kontext-Konflikt

**Was es ist:** Wenn widersprüchliche Informationen im Kontext vorhanden sind, die zu inkonsistentem Denken oder schlechten Endantworten führen. Dies passiert oft, wenn Informationen in mehreren Schritten eingehen und frühe, falsche Annahmen im Kontext bleiben.

**Was zu tun ist:** Verwenden Sie **Kontextbeschneidung** und **Auslagerung**. Beschneidung bedeutet, veraltete oder widersprüchliche Informationen zu entfernen, wenn neue Details eintreffen. Auslagerung gibt dem Modell einen separaten „Kladden“-Arbeitsbereich, um Informationen zu verarbeiten, ohne den Hauptkontext zu überladen.


**Beispiel für Reisebuchung:** Anfangs sagen Sie Ihrem Agenten: **„Ich möchte in der Economy-Klasse fliegen.“** Später im Gespräch ändern Sie Ihre Meinung und sagen: **„Tatsächlich, für diese Reise nehmen wir Business-Class.“** Wenn beide Anweisungen im Kontext bleiben, kann der Agent widersprüchliche Suchergebnisse erhalten oder verwirrt sein, welche Präferenz er priorisieren soll.

**Lösung:** Implementieren Sie **Kontextbereinigung**. Wenn eine neue Anweisung der alten widerspricht, wird die ältere Anweisung aus dem Kontext entfernt oder explizit überschrieben. Alternativ kann der Agent ein **Notizfeld** verwenden, um widersprüchliche Präferenzen vor der Entscheidung abzugleichen, wodurch nur die finale, konsistente Anweisung sein Handeln bestimmt.

## Haben Sie weitere Fragen zur Kontextgestaltung?

Treten Sie dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten beantworten zu lassen.
## Vorherige Lektion

[Agentic Protocols](../11-agentic-protocols/README.md)

## Nächste Lektion

[Memory for AI Agents](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->