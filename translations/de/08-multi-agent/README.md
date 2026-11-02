[![Multi-Agent Design](../../../translated_images/de/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klicken Sie auf das obige Bild, um das Video dieser Lektion anzusehen)_

# Multi-Agent-Designmuster

Sobald Sie mit einem Projekt arbeiten, das mehrere Agenten umfasst, müssen Sie das Multi-Agent-Designmuster berücksichtigen. Es ist jedoch nicht sofort klar, wann man zu Multi-Agenten wechseln sollte und welche Vorteile dies mit sich bringt.

## Einführung

In dieser Lektion wollen wir folgende Fragen beantworten:

- Für welche Szenarien sind Multi-Agenten anwendbar?
- Welche Vorteile hat die Verwendung von Multi-Agenten gegenüber einem einzelnen Agenten, der mehrere Aufgaben erledigt?
- Was sind die Bausteine zur Implementierung des Multi-Agent-Designmusters?
- Wie erhalten wir Einblick darin, wie die mehreren Agenten miteinander interagieren?

## Lernziele

Nach dieser Lektion sollten Sie in der Lage sein:

- Szenarien zu identifizieren, in denen Multi-Agenten anwendbar sind
- Die Vorteile der Verwendung von Multi-Agenten gegenüber einem einzelnen Agenten zu erkennen.
- Die Bausteine zur Implementierung des Multi-Agent-Designmusters zu verstehen.

Was ist das große Ganze?

*Multi-Agenten sind ein Designmuster, das es mehreren Agenten ermöglicht, zusammenzuarbeiten, um ein gemeinsames Ziel zu erreichen*.

Dieses Muster wird in vielen Bereichen eingesetzt, einschließlich Robotik, autonome Systeme und verteiltes Rechnen.

## Szenarien, in denen Multi-Agenten anwendbar sind

Welche Szenarien eignen sich also gut für den Einsatz von Multi-Agenten? Die Antwort ist, dass es viele Szenarien gibt, bei denen der Einsatz mehrerer Agenten besonders vorteilhaft ist, insbesondere in folgenden Fällen:

- **Große Arbeitslasten**: Große Arbeitslasten können in kleinere Aufgaben aufgeteilt und verschiedenen Agenten zugewiesen werden, was parallele Verarbeitung und schnellere Fertigstellung ermöglicht. Ein Beispiel hierfür ist eine große Datenverarbeitungsaufgabe.
- **Komplexe Aufgaben**: Komplexe Aufgaben, wie große Arbeitslasten, können in kleinere Teilaufgaben unterteilt und verschiedenen Agenten zugewiesen werden, die jeweils auf einen spezifischen Aspekt der Aufgabe spezialisiert sind. Ein gutes Beispiel hierfür sind autonome Fahrzeuge, bei denen verschiedene Agenten Navigation, Hinderniserkennung und Kommunikation mit anderen Fahrzeugen steuern.
- **Vielfältige Expertise**: Verschiedene Agenten können über unterschiedliche Expertise verfügen, sodass sie verschiedene Aspekte einer Aufgabe effektiver bewältigen können als ein einzelner Agent. Ein gutes Beispiel hierfür ist der Gesundheitsbereich, in dem Agenten Diagnostik, Behandlungspläne und Patientenüberwachung verwalten können.

## Vorteile der Verwendung von Multi-Agenten gegenüber einem einzelnen Agenten

Ein Ein-Agenten-System kann bei einfachen Aufgaben gut funktionieren, aber bei komplexeren Aufgaben bieten mehrere Agenten mehrere Vorteile:

- **Spezialisierung**: Jeder Agent kann auf eine bestimmte Aufgabe spezialisiert sein. Fehlt die Spezialisierung bei einem einzelnen Agenten, haben Sie einen Agenten, der alles machen kann, aber möglicherweise verwirrt ist, wenn er mit einer komplexen Aufgabe konfrontiert wird. Er könnte zum Beispiel eine Aufgabe erledigen, für die er nicht am besten geeignet ist.
- **Skalierbarkeit**: Es ist einfacher, Systeme zu skalieren, indem mehr Agenten hinzugefügt werden, als einen einzelnen Agenten zu überladen.
- **Fehlertoleranz**: Wenn ein Agent ausfällt, können andere weiterhin funktionieren, wodurch die Systemzuverlässigkeit gewährleistet wird.

Nehmen wir ein Beispiel: Wir buchen eine Reise für einen Benutzer. Ein Ein-Agenten-System müsste alle Aspekte des Reisebuchungsprozesses verwalten, von der Flugsuche bis zur Buchung von Hotels und Mietwagen. Um dies mit einem einzelnen Agenten zu erreichen, müsste der Agent Werkzeuge zur Verwaltung all dieser Aufgaben besitzen. Dies könnte zu einem komplexen und monolithischen System führen, das schwer zu warten und zu skalieren ist. Ein Multi-Agent-System dagegen könnte verschiedene Agenten haben, die auf Flugsuche, Hotel- und Mietwagenbuchungen spezialisiert sind. Dies würde das System modularer, wartungsfreundlicher und skalierbar machen.

Vergleichen Sie dies mit einem Reisebüro, das als Familienbetrieb geführt wird, im Vergleich zu einem Franchise-Reisebüro. Das Familienreisebüro hätte einen einzigen Agenten, der alle Aspekte des Reisebuchungsprozesses verwaltet, während das Franchise verschiedene Agenten hätte, die unterschiedliche Aspekte des Prozesses verwalten.

## Bausteine zur Implementierung des Multi-Agent-Designmusters

Bevor Sie das Multi-Agent-Designmuster implementieren können, müssen Sie die Bausteine verstehen, die das Muster ausmachen.

Lassen Sie uns dies anhand des Beispiels der Reisebuchung für einen Benutzer konkretisieren. In diesem Fall umfassen die Bausteine:

- **Agentenkommunikation**: Agenten für die Flugsuche, Hotel- und Mietwagenbuchung müssen kommunizieren und Informationen über die Präferenzen und Einschränkungen des Benutzers austauschen. Sie müssen die Protokolle und Methoden für diese Kommunikation festlegen. Konkret bedeutet dies, dass der Agent für Flugsuche mit dem Agenten für Hotelbuchungen kommunizieren muss, um sicherzustellen, dass das Hotel für die gleichen Daten wie der Flug gebucht wird. Das bedeutet, dass die Agenten Informationen über die Reisedaten des Benutzers teilen müssen, also müssen Sie entscheiden, *welche Agenten Informationen teilen und wie sie diese teilen*.
- **Koordinationsmechanismen**: Agenten müssen ihre Aktionen koordinieren, um sicherzustellen, dass die Präferenzen und Einschränkungen des Benutzers erfüllt werden. Eine Benutzerpräferenz könnte sein, dass sie ein Hotel in Flughafennähe möchten, während eine Einschränkung sein könnte, dass Mietwagen nur am Flughafen verfügbar sind. Das bedeutet, dass der Agent für Hotelbuchungen mit dem Agenten für Mietwagenbuchung koordinieren muss, um sicherzustellen, dass die Präferenzen und Einschränkungen erfüllt werden. Sie müssen also entscheiden, *wie die Agenten ihre Aktionen koordinieren*.
- **Agentenarchitektur**: Agenten müssen über eine interne Struktur verfügen, um Entscheidungen zu treffen und aus ihren Interaktionen mit dem Benutzer zu lernen. Das bedeutet, dass der Agent für Flugsuche eine interne Struktur besitzen muss, um Entscheidungen darüber zu treffen, welche Flüge dem Benutzer empfohlen werden. Sie müssen entscheiden, *wie die Agenten Entscheidungen treffen und aus ihren Interaktionen mit dem Benutzer lernen*. Beispiele dafür, wie ein Agent lernt und sich verbessert, könnten sein, dass der Flugsuche-Agent ein Machine-Learning-Modell verwendet, um dem Benutzer basierend auf dessen bisherigen Präferenzen Flüge zu empfehlen.
- **Sichtbarkeit der Multi-Agent-Interaktionen**: Sie müssen Einblick darin haben, wie die mehreren Agenten miteinander interagieren. Sie benötigen Werkzeuge und Techniken zur Verfolgung von Agentenaktivitäten und -interaktionen. Dies könnte in Form von Protokollierungs- und Überwachungstools, Visualisierungstools und Leistungskennzahlen erfolgen.
- **Multi-Agenten-Muster**: Es gibt verschiedene Muster zur Implementierung von Multi-Agent-Systemen, wie zentralisierte, dezentralisierte und Hybrid-Architekturen. Sie müssen das Muster auswählen, das am besten zu Ihrem Anwendungsfall passt.
- **Mensch in der Schleife**: In den meisten Fällen wird ein Mensch in den Prozess eingebunden sein, und Sie müssen den Agenten Anweisungen geben, wann sie menschliches Eingreifen anfordern sollen. Dies kann in Form einer Nutzeranfrage für ein bestimmtes Hotel oder einen Flug erfolgen, den die Agenten nicht empfohlen haben, oder durch Anfordern einer Bestätigung vor der Buchung eines Fluges oder Hotels.

## Sichtbarkeit der Multi-Agent-Interaktionen

Es ist wichtig, dass Sie Einblick darin haben, wie die mehreren Agenten miteinander interagieren. Diese Sichtbarkeit ist entscheidend für das Debugging, die Optimierung und die Sicherstellung der Gesamteffektivität des Systems. Um dies zu erreichen, benötigen Sie Tools und Techniken zur Verfolgung von Agentenaktivitäten und -interaktionen. Dies kann in Form von Protokollierungs- und Überwachungstools, Visualisierungstools und Leistungskennzahlen geschehen.

Zum Beispiel könnten Sie im Falle der Reisebuchung für einen Benutzer ein Dashboard haben, das den Status jedes Agenten, die Präferenzen und Einschränkungen des Benutzers sowie die Interaktionen zwischen den Agenten anzeigt. Dieses Dashboard könnte die Reisedaten des Benutzers, die vom Flugsuche-Agent empfohlenen Flüge, die vom Hotel-Agent empfohlenen Hotels und die vom Mietwagen-Agent empfohlenen Mietwagen zeigen. Dies würde Ihnen eine klare Übersicht darüber geben, wie die Agenten miteinander interagieren und ob die Präferenzen und Einschränkungen des Benutzers erfüllt werden.

Schauen wir uns jeden dieser Aspekte noch genauer an.

- **Protokollierungs- und Überwachungstools**: Sie möchten für jede Aktion eines Agenten eine Protokollierung haben. Ein Protokolleintrag könnte Informationen über den Agenten enthalten, der die Aktion ausgeführt hat, die ausgeführte Aktion, den Zeitpunkt der Aktion und das Ergebnis der Aktion. Diese Informationen können dann für Debugging, Optimierung und mehr genutzt werden.

- **Visualisierungstools**: Visualisierungstools können Ihnen helfen, die Interaktionen zwischen Agenten anschaulicher darzustellen. Beispielsweise könnten Sie einen Graphen haben, der den Informationsfluss zwischen Agenten zeigt. Dies kann helfen, Engpässe, Ineffizienzen und andere Probleme im System zu erkennen.

- **Leistungskennzahlen**: Leistungskennzahlen können Ihnen helfen, die Effektivität des Multi-Agenten-Systems zu verfolgen. Sie könnten beispielsweise die Zeit messen, die für die Erledigung einer Aufgabe benötigt wird, die Anzahl der erledigten Aufgaben pro Zeiteinheit und die Genauigkeit der von den Agenten abgegebenen Empfehlungen. Diese Informationen können Ihnen helfen, Verbesserungsbereiche zu identifizieren und das System zu optimieren.

## Multi-Agenten-Muster

Werfen wir einen Blick auf einige konkrete Muster, die wir verwenden können, um Multi-Agenten-Apps zu erstellen. Hier sind einige interessante Muster, die es wert sind, betrachtet zu werden:

### Gruppenchat

Dieses Muster ist nützlich, wenn Sie eine Gruppenchat-Anwendung erstellen möchten, in der mehrere Agenten miteinander kommunizieren können. Typische Anwendungsfälle für dieses Muster sind Teamzusammenarbeit, Kundensupport und soziale Netzwerke.

In diesem Muster repräsentiert jeder Agent einen Benutzer im Gruppenchat, und Nachrichten werden zwischen den Agenten mittels eines Nachrichtenprotokolls ausgetauscht. Die Agenten können Nachrichten an den Gruppenchat senden, Nachrichten vom Gruppenchat empfangen und auf Nachrichten anderer Agenten antworten.

Dieses Muster kann mit einer zentralisierten Architektur umgesetzt werden, bei der alle Nachrichten über einen zentralen Server geleitet werden, oder mit einer dezentralisierten Architektur, bei der Nachrichten direkt ausgetauscht werden.

![Gruppenchat](../../../translated_images/de/multi-agent-group-chat.ec10f4cde556babd.webp)

### Übergabe

Dieses Muster ist nützlich, wenn Sie eine Anwendung erstellen möchten, bei der mehrere Agenten Aufgaben aneinander übergeben können.

Typische Anwendungsfälle für dieses Muster sind Kundensupport, Aufgabenmanagement und Workflow-Automatisierung.

In diesem Muster repräsentiert jeder Agent eine Aufgabe oder einen Schritt in einem Workflow, und Agenten können Aufgaben basierend auf vordefinierten Regeln an andere Agenten übergeben.

![Übergabe](../../../translated_images/de/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Kollaboratives Filtern

Dieses Muster ist nützlich, wenn Sie eine Anwendung erstellen möchten, bei der mehrere Agenten zusammenarbeiten, um Empfehlungen für Benutzer zu geben.

Der Grund, warum mehrere Agenten zusammenarbeiten sollten, ist, dass jeder Agent über unterschiedliche Kenntnisse verfügt und auf verschiedene Weise zum Empfehlungsprozess beitragen kann.

Nehmen wir ein Beispiel, bei dem ein Benutzer eine Empfehlung für die beste Aktie auf dem Aktienmarkt erhalten möchte.

- **Branchenexperte**: Ein Agent könnte Experte für eine bestimmte Branche sein.
- **Technische Analyse**: Ein weiterer Agent könnte Experte für technische Analysen sein.
- **Fundamentalanalyse**: Und ein weiterer Agent könnte Experte für Fundamentalanalyse sein. Durch die Zusammenarbeit können diese Agenten umfassendere Empfehlungen für den Benutzer geben.

![Empfehlung](../../../translated_images/de/multi-agent-filtering.d959cb129dc9f608.webp)

## Szenario: Rückerstattungsprozess

Betrachten Sie ein Szenario, in dem ein Kunde eine Rückerstattung für ein Produkt beantragt. Dabei können recht viele Agenten in diesen Prozess involviert sein, doch wir unterteilen sie in agentenspezifische für diesen Prozess und allgemeine Agenten, die in anderen Prozessen verwendet werden können.

**Agenten spezifisch für den Rückerstattungsprozess**:

Folgende Agenten könnten im Rückerstattungsprozess beteiligt sein:

- **Kunden-Agent**: Dieser Agent repräsentiert den Kunden und ist verantwortlich für die Einleitung des Rückerstattungsprozesses.
- **Verkäufer-Agent**: Dieser Agent repräsentiert den Verkäufer und ist verantwortlich für die Abwicklung der Rückerstattung.
- **Zahlungs-Agent**: Dieser Agent repräsentiert den Zahlungsprozess und ist verantwortlich für die Rückerstattung der Zahlung an den Kunden.
- **Lösungs-Agent**: Dieser Agent repräsentiert den Lösungsprozess und ist verantwortlich für die Behebung von Problemen, die während des Rückerstattungsprozesses auftreten.
- **Compliance-Agent**: Dieser Agent repräsentiert den Compliance-Prozess und ist verantwortlich für die Einhaltung von Vorschriften und Richtlinien im Rückerstattungsprozess.

**Allgemeine Agenten**:

Diese Agenten können in anderen Geschäftsbereichen verwendet werden.

- **Versand-Agent**: Dieser Agent repräsentiert den Versandprozess und ist verantwortlich für die Rücksendung des Produkts an den Verkäufer. Dieser Agent kann sowohl für den Rückerstattungsprozess als auch für den allgemeinen Versand eines Produkts, z.B. bei einem Kauf, verwendet werden.
- **Feedback-Agent**: Dieser Agent repräsentiert den Feedback-Prozess und ist verantwortlich für das Sammeln von Kundenfeedback. Feedback kann jederzeit eingeholt werden und nicht nur während des Rückerstattungsprozesses.
- **Eskaltions-Agent**: Dieser Agent repräsentiert den Eskalationsprozess und ist verantwortlich für die Eskalation von Problemen an eine höhere Supportebene. Sie können diesen Agenten für jeden Prozess verwenden, in dem eine Eskalation erforderlich ist.
- **Benachrichtigungs-Agent**: Dieser Agent repräsentiert den Benachrichtigungsprozess und ist verantwortlich für das Senden von Benachrichtigungen an den Kunden während verschiedener Phasen des Rückerstattungsprozesses.
- **Analyse-Agent**: Dieser Agent repräsentiert den Analyseprozess und ist verantwortlich für die Analyse von Daten im Zusammenhang mit dem Rückerstattungsprozess.
- **Audit-Agent**: Dieser Agent repräsentiert den Prüfprozess und ist verantwortlich für die Prüfung des Rückerstattungsprozesses, um sicherzustellen, dass er korrekt durchgeführt wird.
- **Berichts-Agent**: Dieser Agent repräsentiert den Berichtsprozess und ist verantwortlich für die Erstellung von Berichten über den Rückerstattungsprozess.
- **Wissens-Agent**: Dieser Agent repräsentiert den Wissensprozess und ist verantwortlich für die Pflege einer Wissensdatenbank mit Informationen zum Rückerstattungsprozess. Dieser Agent könnte sowohl über Rückerstattungen als auch andere Bereiche Ihres Geschäfts Bescheid wissen.
- **Sicherheits-Agent**: Dieser Agent repräsentiert den Sicherheitsprozess und ist verantwortlich für die Sicherheit des Rückerstattungsprozesses.
- **Qualitäts-Agent**: Dieser Agent repräsentiert den Qualitätsprozess und ist verantwortlich für die Sicherstellung der Qualität des Rückerstattungsprozesses.

Es sind ziemlich viele Agenten aufgelistet, sowohl spezifisch für den Rückerstattungsprozess als auch allgemeine Agenten, die in anderen Teilen Ihres Geschäfts verwendet werden können. Hoffentlich gibt Ihnen das eine Vorstellung davon, wie Sie entscheiden können, welche Agenten Sie in Ihrem Multi-Agent-System verwenden.

## Aufgabe

Entwerfen Sie ein Multi-Agenten-System für einen Kundensupportprozess. Identifizieren Sie die im Prozess beteiligten Agenten, ihre Rollen und Verantwortlichkeiten sowie wie sie miteinander interagieren. Berücksichtigen Sie sowohl agentspezifische für den Kundensupportprozess als auch allgemeine Agenten, die in anderen Teilen Ihres Geschäfts verwendet werden können.


> Denken Sie nach, bevor Sie die folgende Lösung lesen, möglicherweise benötigen Sie mehr Agenten, als Sie denken.

> TIPP: Denken Sie über die verschiedenen Phasen des Kunden-Support-Prozesses nach und berücksichtigen Sie auch Agenten, die für jedes System benötigt werden.

## Lösung

[Lösung](./solution/solution.md)

## Wissensüberprüfungen

### Frage 1

Welches Szenario ist die beste Passform für ein Multi-Agenten-System?

- [ ] A1: Ein Support-Bot beantwortet häufig gestellte Fragen mit einer Wissensdatenbank und einem kleinen Satz von Werkzeugen.
- [ ] A2: Ein Rückerstattungs-Workflow benötigt separate Rollen für Betrug, Zahlung und Compliance, jede mit eigenen Werkzeugen, und deren Ergebnisse müssen koordiniert werden.
- [ ] A3: Dieselbe einfache Klassifizierungsanfrage kommt tausendfach pro Stunde an.

### Frage 2

Wann ist ein einzelner Agent normalerweise die bessere Wahl?

- [ ] A1: Die Aufgabe kann mit einem Satz von Anweisungen und Werkzeugen bewältigt werden, ohne Spezialistenübergaben.
- [ ] A2: Der Agent hat Zugriff auf mehr als ein Werkzeug.
- [ ] A3: Der Workflow erfordert separate Rollen mit unterschiedlichen Berechtigungen und unabhängigen Audit-Trails.

[Lösung Quiz](./solution/solution-quiz.md)

## Zusammenfassung

In dieser Lektion haben wir uns das Multi-Agenten-Designmuster angesehen, einschließlich der Szenarien, bei denen Multi-Agenten anwendbar sind, der Vorteile der Verwendung von Multi-Agenten im Vergleich zu einem einzelnen Agenten, der Bausteine zur Implementierung des Multi-Agenten-Designmusters und wie man Einblick bekommt, wie die verschiedenen Agenten miteinander interagieren.

### Haben Sie noch mehr Fragen zum Multi-Agenten-Designmuster?

Treten Sie dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu AI-Agenten beantwortet zu bekommen.

## Zusätzliche Ressourcen

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Dokumentation</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentische Designmuster</a>


## Vorherige Lektion

[Planungsentwurf](../07-planning-design/README.md)

## Nächste Lektion

[Metakognition in KI-Agenten](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->