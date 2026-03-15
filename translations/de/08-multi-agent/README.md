[![Multi-Agent Design](../../../translated_images/de/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

# Multi-Agenten-Entwurfsmuster

Sobald Sie an einem Projekt arbeiten, das mehrere Agenten umfasst, müssen Sie das Multi-Agent-Entwurfsmuster berücksichtigen. Allerdings ist nicht sofort klar, wann auf Multi-Agenten umgestiegen werden sollte und welche Vorteile dies bietet.

## Einführung

In dieser Lektion möchten wir folgende Fragen beantworten:

- Für welche Szenarien sind Multi-Agenten anwendbar?
- Welche Vorteile bietet die Verwendung von Multi-Agenten gegenüber einem einzigen Agenten, der mehrere Aufgaben übernimmt?
- Was sind die Bausteine zur Implementierung des Multi-Agent-Entwurfsmusters?
- Wie können wir die Interaktion der mehreren Agenten untereinander sichtbar machen?

## Lernziele

Nach dieser Lektion sollten Sie in der Lage sein:

- Szenarien zu erkennen, in denen Multi-Agenten anwendbar sind
- Die Vorteile der Nutzung von Multi-Agenten gegenüber einem einzelnen Agenten zu verstehen
- Die Bausteine zur Implementierung des Multi-Agent-Entwurfsmusters zu begreifen

Was ist das große Ganze?

*Multi-Agenten sind ein Entwurfsmuster, das ermöglicht, dass mehrere Agenten zusammenarbeiten, um ein gemeinsames Ziel zu erreichen*.

Dieses Muster wird in vielen Bereichen angewendet, darunter Robotik, autonome Systeme und verteiltes Rechnen.

## Szenarien, in denen Multi-Agenten anwendbar sind

Welche Szenarien eignen sich also gut für den Einsatz von Multi-Agenten? Die Antwort ist, dass es viele Szenarien gibt, in denen der Einsatz mehrerer Agenten besonders vorteilhaft ist, insbesondere in folgenden Fällen:

- **Große Arbeitslasten**: Große Arbeitslasten können in kleinere Aufgaben aufgeteilt und verschiedenen Agenten zugewiesen werden, was parallele Verarbeitung und schnellere Fertigstellung ermöglicht. Ein Beispiel hierfür ist eine umfangreiche Datenverarbeitungsaufgabe.
- **Komplexe Aufgaben**: Komplexe Aufgaben können, ähnlich wie große Arbeitslasten, in kleinere Unteraufgaben aufgeteilt werden, die verschiedenen Agenten zugeordnet werden, die jeweils auf einen bestimmten Aspekt der Aufgabe spezialisiert sind. Ein gutes Beispiel hierfür sind autonome Fahrzeuge, bei denen verschiedene Agenten Navigation, Hinderniserkennung und Kommunikation mit anderen Fahrzeugen übernehmen.
- **Verschiedene Fachkompetenzen**: Unterschiedliche Agenten können verschiedene Fachkompetenzen haben, sodass sie unterschiedliche Aspekte einer Aufgabe effektiver als ein einzelner Agent bearbeiten können. Ein Beispiel hierfür ist das Gesundheitswesen, in dem Agenten Diagnostik, Behandlungspläne und Patientenüberwachung verwalten.

## Vorteile der Nutzung von Multi-Agenten gegenüber einem einzelnen Agenten

Ein Ein-Agenten-System könnte für einfache Aufgaben gut funktionieren, aber bei komplexeren Aufgaben bietet der Einsatz mehrerer Agenten verschiedene Vorteile:

- **Spezialisierung**: Jeder Agent kann auf eine spezifische Aufgabe spezialisiert sein. Ein einzelner Agent ohne Spezialisierung müsste alles können, könnte aber bei komplexen Aufgaben überfordert sein und möglicherweise eine Aufgabe übernehmen, für die er nicht am besten geeignet ist.
- **Skalierbarkeit**: Systeme lassen sich einfacher skalieren, indem mehr Agenten hinzugefügt werden, anstatt einen einzelnen Agenten zu überlasten.
- **Fehlertoleranz**: Wenn ein Agent ausfällt, können die anderen weiterhin funktionieren, was die Zuverlässigkeit des Systems sicherstellt.

Nehmen wir als Beispiel die Buchung einer Reise für einen Nutzer. Ein Ein-Agenten-System müsste alle Aspekte des Buchungsprozesses abwickeln, von der Flugfindung bis zur Hotel- und Mietwagenreservierung. Um dies mit einem einzelnen Agenten zu erreichen, müsste dieser Tools für alle diese Aufgaben besitzen. Das könnte zu einem komplexen und monolithischen System führen, das schwer zu warten und zu skalieren ist. Ein Multi-Agenten-System hingegen könnte verschiedene Agenten haben, die jeweils auf Flugfindung, Hotelbuchung und Mietwagenreservierung spezialisiert sind. Das macht das System modularer, leichter wartbar und skalierbar.

Vergleichen Sie dies mit einem Reisebüro, das als Familienbetrieb geführt wird, gegenüber einem Franchise-Reisebüro. Das Familienbetrieb-Reisebüro hätte einen einzigen Agenten, der alle Aspekte der Reisebuchung übernimmt, während das Franchise unterschiedliche Agenten für verschiedene Aspekte des Buchungsprozesses hätte.

## Bausteine zur Implementierung des Multi-Agent-Entwurfsmusters

Bevor Sie das Multi-Agent-Entwurfsmuster implementieren können, müssen Sie die Bausteine verstehen, aus denen das Muster besteht.

Machen wir dies am Beispiel der Reisebuchung für einen Nutzer konkreter. In diesem Fall umfassen die Bausteine:

- **Agentenkommunikation**: Agenten für Flugfindung, Hotel- und Mietwagenbuchung müssen kommunizieren und Informationen über die Präferenzen und Einschränkungen des Nutzers austauschen. Sie müssen die Protokolle und Methoden für diese Kommunikation festlegen. Konkret bedeutet dies, dass der Flugfindungs-Agent mit dem Hotelbuchungs-Agent kommunizieren muss, um sicherzustellen, dass das Hotel zu denselben Daten gebucht wird wie der Flug. Das bedeutet, dass die Agenten Informationen über die Reisedaten des Nutzers teilen müssen, und Sie müssen entscheiden, *welche Agenten welche Informationen austauschen und wie dieser Austausch erfolgt*.
- **Koordinationsmechanismen**: Die Agenten müssen ihre Aktionen koordinieren, um sicherzustellen, dass die Präferenzen und Einschränkungen des Nutzers erfüllt werden. Eine Nutzerpräferenz könnte beispielsweise sein, dass das Hotel nahe am Flughafen liegt, während eine Einschränkung sein könnte, dass Mietwagen nur am Flughafen verfügbar sind. Das bedeutet, dass der Hotelbuchungs-Agent mit dem Mietwagenbuchungs-Agent koordinieren muss, um sicherzugehen, dass die Präferenzen und Einschränkungen des Nutzers eingehalten werden. Sie müssen also entscheiden, *wie die Agenten ihre Aktionen koordinieren*.
- **Agentenarchitektur**: Agenten benötigen eine interne Struktur, um Entscheidungen zu treffen und aus ihren Interaktionen mit dem Nutzer zu lernen. Das bedeutet, der Flugfindungs-Agent benötigt eine interne Struktur, um zu entscheiden, welche Flüge dem Nutzer empfohlen werden. Hier müssen Sie entscheiden, *wie die Agenten Entscheidungen treffen und aus den Interaktionen lernen*. Ein Beispiel dafür, wie ein Agent lernen und sich verbessern kann, ist, dass der Flugfindungs-Agent ein maschinelles Lernmodell verwenden könnte, um Flüge basierend auf den bisherigen Präferenzen des Nutzers zu empfehlen.
- **Sichtbarkeit der Multi-Agenten-Interaktionen**: Sie müssen sichtbar machen können, wie die Agenten miteinander interagieren. Das erfordert Werkzeuge und Techniken zum Nachverfolgen von Aktivitäten und Interaktionen der Agenten. Das kann in Form von Protokollierungs- und Überwachungstools, Visualisierungstools und Leistungskennzahlen geschehen.
- **Multi-Agenten-Muster**: Es gibt verschiedene Muster zur Implementierung von Multi-Agenten-Systemen, z. B. zentralisierte, dezentralisierte und hybride Architekturen. Sie müssen das Muster auswählen, das am besten zu Ihrem Anwendungsfall passt.
- **Mensch im Loop**: In den meisten Fällen ist ein Mensch im Loop, und Sie müssen die Agenten anweisen, wann sie eine menschliche Intervention anfragen sollen. Dies könnte z. B. sein, wenn ein Nutzer ein bestimmtes Hotel oder einen Flug verlangt, den die Agenten nicht empfohlen haben, oder um eine Bestätigung vor der Buchung eines Fluges oder Hotels zu bitten.

## Sichtbarkeit der Multi-Agenten-Interaktionen

Es ist wichtig, dass Sie nachvollziehen können, wie die einzelnen Agenten miteinander interagieren. Diese Transparenz ist entscheidend für das Debugging, die Optimierung und das Sicherstellen der Effektivität des Gesamtsystems. Dazu benötigen Sie Werkzeuge und Techniken zur Verfolgung von Aktivitäten und Interaktionen der Agenten. Dies kann in Form von Protokollierungs- und Überwachungstools, Visualisierungstools oder Leistungskennzahlen erfolgen.

Beispielsweise könnten Sie im Fall der Reisebuchung ein Dashboard haben, das den Status jedes Agenten, die Nutzerpräferenzen und -einschränkungen sowie die Interaktionen zwischen den Agenten zeigt. Dieses Dashboard könnte die Reisedaten des Nutzers anzeigen, die vom Flug-Agent empfohlenen Flüge, die vom Hotel-Agent empfohlenen Hotels und die vom Mietwagen-Agent vorgeschlagenen Mietwagen. So erhalten Sie eine klare Übersicht darüber, wie die Agenten miteinander interagieren und ob die Präferenzen und Einschränkungen des Nutzers eingehalten werden.

Schauen wir uns diese Aspekte genauer an:

- **Protokollierungs- und Überwachungstools**: Für jede vom Agenten ausgeführte Aktion sollte eine Protokollierung erfolgen. Ein Log-Eintrag könnte Informationen über den ausführenden Agenten, die Aktion, den Zeitpunkt der Aktion und das Ergebnis enthalten. Diese Informationen sind hilfreich zum Debuggen, Optimieren und mehr.

- **Visualisierungstools**: Visualisierungstools können helfen, die Interaktionen zwischen Agenten anschaulicher darzustellen. Zum Beispiel könnte ein Graph die Informationsflüsse zwischen Agenten zeigen. Dies hilft, Engpässe, Ineffizienzen und andere Probleme im System zu erkennen.

- **Leistungskennzahlen**: Leistungskennzahlen unterstützen die Nachverfolgung der Effektivität des Multi-Agenten-Systems. Beispielsweise können die benötigte Zeit zur Erledigung einer Aufgabe, die Anzahl der pro Zeiteinheit ausgeführten Aufgaben oder die Genauigkeit der Empfehlungen der Agenten erfasst werden. Diese Daten helfen dabei, Verbesserungsbereiche zu identifizieren und das System zu optimieren.

## Multi-Agenten-Muster

Werfen wir einen Blick auf einige konkrete Muster, die wir zur Erstellung von Multi-Agenten-Anwendungen verwenden können. Hier sind einige interessante Muster, die es zu betrachten gilt:

### Gruppenchat

Dieses Muster ist nützlich, wenn Sie eine Gruppenchat-Anwendung erstellen möchten, in der mehrere Agenten miteinander kommunizieren können. Typische Anwendungsfälle für dieses Muster sind Teamzusammenarbeit, Kundensupport und soziale Netzwerke.

In diesem Muster repräsentiert jeder Agent einen Benutzer im Gruppenchat, und Nachrichten werden zwischen Agenten über ein Nachrichtenprotokoll ausgetauscht. Die Agenten können Nachrichten an den Gruppenchat senden, Nachrichten vom Gruppenchat empfangen und auf Nachrichten anderer Agenten antworten.

Dieses Muster kann mit einer zentralisierten Architektur umgesetzt werden, bei der alle Nachrichten über einen zentralen Server geleitet werden, oder mit einer dezentralisierten Architektur, bei der Nachrichten direkt ausgetauscht werden.

![Group chat](../../../translated_images/de/multi-agent-group-chat.ec10f4cde556babd.webp)

### Übergabe

Dieses Muster ist nützlich, wenn Sie eine Anwendung erstellen möchten, in der mehrere Agenten Aufgaben aneinander übergeben können.

Typische Anwendungsfälle sind Kundensupport, Aufgabenmanagement und Workflow-Automatisierung.

In diesem Muster repräsentiert jeder Agent eine Aufgabe oder einen Schritt in einem Workflow, und Agenten können Aufgaben basierend auf vordefinierten Regeln an andere Agenten übergeben.

![Hand off](../../../translated_images/de/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Collaborative Filtering

Dieses Muster ist hilfreich, wenn Sie eine Anwendung erstellen möchten, in der mehrere Agenten zusammenarbeiten, um Empfehlungen für Nutzer zu erstellen.

Der Grund, warum mehrere Agenten zusammenarbeiten sollten, liegt darin, dass jeder Agent über unterschiedliche Expertise verfügt und so in unterschiedlicher Weise zum Empfehlungsprozess beitragen kann.

Nehmen wir als Beispiel den Wunsch eines Nutzers, eine Empfehlung für die beste Aktie am Aktienmarkt zu erhalten.

- **Branchenexperte**: Ein Agent könnte Experte in einer bestimmten Branche sein.
- **Technische Analyse**: Ein weiterer Agent könnte auf technische Analyse spezialisiert sein.
- **Fundamentalanalyse**: Ein anderer Agent könnte Experte in der Fundamentalanalyse sein. Durch die Zusammenarbeit können diese Agenten dem Nutzer eine umfassendere Empfehlung geben.

![Recommendation](../../../translated_images/de/multi-agent-filtering.d959cb129dc9f608.webp)

## Szenario: Rückerstattungsprozess

Betrachten wir ein Szenario, bei dem ein Kunde versucht, eine Rückerstattung für ein Produkt zu erhalten. In diesem Prozess können viele Agenten beteiligt sein. Unterteilen wir sie in spezifische Agenten für diesen Prozess und allgemeine Agenten, die in anderen Prozessen genutzt werden können.

**Agenten, die spezifisch für den Rückerstattungsprozess sind**:

Folgende Agenten könnten am Rückerstattungsprozess beteiligt sein:

- **Kunden-Agent**: Dieser Agent repräsentiert den Kunden und ist zuständig für das Initiieren des Rückerstattungsprozesses.
- **Verkäufer-Agent**: Dieser Agent repräsentiert den Verkäufer und ist für die Bearbeitung der Rückerstattung zuständig.
- **Zahlungs-Agent**: Dieser Agent repräsentiert den Zahlungsprozess und ist für die Rückzahlung an den Kunden verantwortlich.
- **Lösungs-Agent**: Dieser Agent kümmert sich um die Lösung von Problemen, die während des Rückerstattungsprozesses auftreten können.
- **Compliance-Agent**: Dieser Agent sorgt dafür, dass der Rückerstattungsprozess den Vorschriften und Richtlinien entspricht.

**Allgemeine Agenten**:

Diese Agenten können in anderen Bereichen Ihres Geschäfts verwendet werden.

- **Versand-Agent**: Dieser Agent repräsentiert den Versandprozess und ist für den Rückversand des Produkts an den Verkäufer zuständig. Er kann sowohl im Rückerstattungsprozess als auch im allgemeinen Versand von Produkten bei Käufen genutzt werden.
- **Feedback-Agent**: Dieser Agent kümmert sich um das Sammeln von Kundenfeedback, was zu jeder Zeit erfolgen kann, nicht nur während des Rückerstattungsprozesses.
- **Eskalations-Agent**: Dieser Agent ist für die Eskalation von Problemen an eine höhere Supportebene zuständig. Sie können diesen Agenten für jeden Prozess verwenden, bei dem eine Eskalation nötig ist.
- **Benachrichtigungs-Agent**: Dieser Agent versendet Benachrichtigungen an den Kunden während verschiedener Phasen des Rückerstattungsprozesses.
- **Analyse-Agent**: Dieser Agent ist für die Analyse von Daten im Zusammenhang mit dem Rückerstattungsprozess verantwortlich.
- **Audit-Agent**: Dieser Agent prüft den Rückerstattungsprozess, um sicherzustellen, dass er korrekt durchgeführt wird.
- **Reporting-Agent**: Dieser Agent erstellt Berichte über den Rückerstattungsprozess.
- **Wissens-Agent**: Dieser Agent pflegt eine Wissensdatenbank mit Informationen zum Rückerstattungsprozess. Er könnte sowohl in Bezug auf Rückerstattungen als auch andere Geschäftsbereiche fundiertes Wissen haben.
- **Sicherheits-Agent**: Dieser Agent sorgt für die Sicherheit des Rückerstattungsprozesses.
- **Qualitäts-Agent**: Dieser Agent stellt sicher, dass der Rückerstattungsprozess qualitativ hochwertig abläuft.

Es gibt also eine ganze Reihe von Agenten, sowohl spezifisch für den Rückerstattungsprozess als auch allgemeine Agenten, die in anderen Geschäftsbereichen genutzt werden können. Hoffentlich gibt Ihnen dies eine Vorstellung davon, wie Sie entscheiden können, welche Agenten Sie in Ihrem Multi-Agenten-System einsetzen.

## Aufgabe

Entwerfen Sie ein Multi-Agenten-System für einen Kundenservice-Prozess. Identifizieren Sie die in den Prozess involvierten Agenten, ihre Rollen und Verantwortlichkeiten sowie wie sie miteinander interagieren. Berücksichtigen Sie sowohl agentenspezifische Komponenten für den Kundenservice als auch allgemeine Agenten, die in anderen Geschäftsbereichen eingesetzt werden können.
> Denken Sie nach, bevor Sie die folgende Lösung lesen, möglicherweise benötigen Sie mehr Agenten, als Sie denken.

> TIP: Denken Sie an die verschiedenen Phasen des Kunden-Support-Prozesses und berücksichtigen Sie auch Agenten, die für jedes System benötigt werden.

## Lösung

[Lösung](./solution/solution.md)

## Wissensüberprüfungen

Frage: Wann sollten Sie den Einsatz von Multi-Agenten in Betracht ziehen?

- [ ] A1: Wenn Sie eine geringe Arbeitsbelastung und eine einfache Aufgabe haben.
- [ ] A2: Wenn Sie eine hohe Arbeitsbelastung haben
- [ ] A3: Wenn Sie eine einfache Aufgabe haben.

[Lösungsquiz](./solution/solution-quiz.md)

## Zusammenfassung

In dieser Lektion haben wir uns das Multi-Agenten-Designmuster angesehen, einschließlich der Szenarien, in denen Multi-Agenten anwendbar sind, der Vorteile der Verwendung von Multi-Agenten gegenüber einem einzelnen Agenten, der Bausteine zur Implementierung des Multi-Agenten-Designmusters und wie man Einblick darin erhält, wie die mehreren Agenten miteinander interagieren.

### Haben Sie weitere Fragen zum Multi-Agenten-Designmuster?

Treten Sie dem [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu AI Agents beantwortet zu bekommen.

## Zusätzliche Ressourcen

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Dokumentation</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentische Designmuster</a>

## Vorherige Lektion

[Planung und Design](../07-planning-design/README.md)

## Nächste Lektion

[Metakognition in AI Agents](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatische Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen, übernehmen wir keine Haftung.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->