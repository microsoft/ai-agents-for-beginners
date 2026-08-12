# KI-Agenten für Anfänger - Studienführer

Verwenden Sie diesen Leitfaden als praktischen Begleiter, während Sie den Kurs durchlaufen. Er ist
nicht dazu gedacht, die Lektionen zu ersetzen. Er hilft Ihnen zu entscheiden, wo Sie anfangen sollten, was Sie
in jeder Lektion suchen sollten und wie Sie die Ideen zu einer kleinen funktionierenden Agenten-
Demonstration verbinden.

Wenn Sie zum ersten Mal hier sind, starten Sie einfach:

1. Lesen Sie die [Kurseinrichtung](./00-course-setup/README.md).
2. Schließen Sie die Lektionen 01-06 der Reihe nach ab.
3. Behalten Sie eine kleine Demo-Idee im Kopf, während Sie lernen.
4. Fragen Sie nach jeder Lektion: „Was kann mein Agent jetzt, was er zuvor nicht konnte?“


## Eine einfache Demo zum Behalten im Kopf

Eine gute Möglichkeit, Agenten zu lernen, ist es, eine Demo-Idee durch den Kurs zu verfolgen.

Beispiel-Demo: **ein Kurshelfer-Agent**.

Der Nutzer fragt:

> „Ich möchte lernen, wie Agenten Werkzeuge einsetzen. Finde die richtigen Lektionen, fasse zusammen, was
> ich zuerst lesen sollte, und gib mir eine kurze Übungsaufgabe.“

Ein normaler Chatbot kann aus dem antworten, was er bereits weiß. Ein Agent kann mehr:

1. **Lese oder suche in Kursdateien**, um die richtigen Lektionen zu finden.
2. **Verwende Werkzeuge**, um Lektionen-Links, Beispiele oder unterstützendes Material abzurufen.
3. **Plane** einen kurzen Lernweg, anstatt eine lange Antwort zu geben.
4. **Nutze den Kontext** der aktuellen Unterhaltung, um auf das Ziel des Lernenden fokussiert zu bleiben.
5. **Merke dir nützliche Präferenzen**, wenn die Anwendung Gedächtnis unterstützt.
6. **Zeige Spuren, Zitate oder Protokolle** an, damit der Nutzer versteht, was passiert ist.
7. **Wende Schutzmaßnahmen an**, bevor risikoreiche Aktionen durchgeführt oder sensible Daten verwendet werden.


würde diese Lektion hinzufügen?


## Woran Sie arbeiten

Am Ende des Kurses sollten Sie in der Lage sein, Agentensysteme zu erklären und zu bauen,
die diese Teile kombinieren:

| Teil | Bedeutung in einfacher Sprache | In der Demo |
|------|------------------------------|------------|
| Modell | Die Denkmaschine, die die Anfrage des Nutzers interpretiert | Versteht, dass der Lernende Lektionen zur Werkzeugnutzung möchte |
| Werkzeuge | Funktionen, APIs, Dateien, Browser oder Dienste, die der Agent nutzen kann | Durchsucht das Repository oder ruft Lektionen-Inhalte ab |
| Wissen | Dokumente oder Daten, die die Antwort fundieren | Kurs-README-Dateien und Lernmaterialien |
| Kontext | Informationen, die in den nächsten Modellaufruf einfließen | Das Ziel des Nutzers und die Ergebnisse der Werkzeuge |
| Gedächtnis | Informationen, die für spätere Nutzung gespeichert werden | Der Lernende bevorzugt praxisorientierte Python-Beispiele |
| Planung | Aufteilung eines großen Ziels in kleinere Schritte | Finde Lektionen, fasse sie zusammen, schlage Übung vor |
| Orchestrierung | Verteilung der Arbeit über Werkzeuge, Schritte oder Agenten | Ein Planer ruft eine Suchfunktion, dann eine Zusammenfassung auf |
| Vertrauen | Sicherheit, Schutz, Bewertung und Beobachtbarkeit | Protokolliert Werkzeugaufrufe und fragt vor riskanten Aktionen |

## Modelle und Provider

Der Kurs-Code verwendet das **Microsoft Agent Framework (MAF)** und zielt auf die **Azure OpenAI Responses API** — die empfohlene API für die Zukunft, die Chat-Komplettierungen, Werkzeugaufrufe, multimodale Eingaben und zustandsbehaftete Gespräche in einer einzigen API-Oberfläche kombiniert. Verbinden Sie sich entweder über ein **Microsoft Foundry**-Projekt (mit `FoundryChatClient`) oder direkt mit Azure OpenAI (mit `OpenAIChatClient`).

Während Sie die Lektionen durchgehen, haben Sie einige Provider-Optionen:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — Hauptweg für die Lektionen. Melden Sie sich mit `az login` für schlüsselose Entra-ID-Authentifizierung an.
- **Foundry Local** — führt Modelle vollständig auf dem Gerät über eine OpenAI-kompatible API aus (kein Cloud, keine API-Schlüssel). Ideal für Offline- oder kostenfreie Experimente. Siehe [Kurseinrichtung](./00-course-setup/README.md).
- **MiniMax** — ein OpenAI-kompatibler Provider mit großen Kontextmodellen, nutzbar als Drop-in-Alternative.

> **Hinweis:** GitHub Models wird eingestellt (Ruhestand Juli 2026) und unterstützt nicht die Responses API. Die Beispiele wurden aktualisiert auf Azure OpenAI / Microsoft Foundry.

## Wähle deinen Lernpfad

Sie können den gesamten Kurs der Reihe nach machen oder direkt einen Pfad wählen, basierend darauf, was Sie bauen möchten.


| Wenn Ihr Ziel ist... | Starten Sie mit | Dann lernen Sie |
|-------------------|--------------|--------------|
| Verstehen, was Agenten sind | 01, 02, 03 | 04, 05, 06 |
| Einen Agenten bauen, der Werkzeuge nutzt | 04 | 05, 07, 14 |
| Einen RAG-basierten Agenten bauen | 05 | 04, 06, 12 |
| Mehrschrittige Workflows entwerfen | 07 | 08, 09, 14 |
| Multi-Agenten-Systeme verstehen | 08 | 07, 09, 11 |
| Agenten für den Produktionseinsatz vorbereiten | 06, 10 | 12, 13, 16, 18 |
| Agenten auf Foundry bereitstellen und skalieren | 10, 16 | 06, 13, 18 |
| Lokale / Offline-zuerst-Agenten bauen | 17 | 04, 05, 11 |
| Protokolle und Browser-Automatisierung erkunden | 11, 15 | 10, 18 |

Tipp: Wenn Sie neu in Agenten sind, überspringen Sie nicht die Lektionen 01-06. Sie geben Ihnen den
Wortschatz, den Sie für den Rest des Kurses brauchen.

## Lektion-für-Lektion Leitfaden

| Lektion | Was Sie lernen | Probieren Sie das nach der Lektion |
|---------|--------------|-----------------------------|
| [01 - Einführung in KI-Agenten](./01-intro-to-ai-agents/README.md) | Was Agenten von einem normalen Chatbot unterscheidet. | Erklären Sie Ihre Demo-Idee als Agent, nicht nur als Chat-App. |
| [02 - Agentic Frameworks](./02-explore-agentic-frameworks/README.md) | Wie Frameworks bei Modellen, Werkzeugen, Zustand und Workflows helfen. | Identifizieren Sie, welche Teile Ihrer Demo ein Framework verwalten würde. |
| [03 - Agentic Design Patterns](./03-agentic-design-patterns/README.md) | Häufige Muster für die Gestaltung von Agentenverhalten. | Skizzieren Sie die Nutzerreise, bevor Sie Code schreiben. |
| [04 - Werkzeugnutzung](./04-tool-use/README.md) | Wie Agenten Werkzeuge aufrufen, um Daten zu erhalten oder Aktionen durchzuführen. | Definieren Sie ein Werkzeug, das Ihr Demo-Agent benötigen würde. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | Wie die Abrufunterstützung Antworten des Agenten in Dokumenten oder Daten verankert. | Entscheiden Sie, welche Wissensquelle Ihre Demo durchsuchen sollte. |
| [06 - Vertrauenswürdige Agenten](./06-building-trustworthy-agents/README.md) | Wie man Schutzmaßnahmen, Aufsicht und sicheres Verhalten hinzufügt. | Fügen Sie eine Regel hinzu, wann der Agent zuerst den Nutzer fragen soll. |
| [07 - Planungsdesign](./07-planning-design/README.md) | Wie Agenten größere Ziele in kleinere Schritte zerlegen. | Schreiben Sie einen Drei-Schritte-Plan für Ihre Demo-Anfrage. |
| [08 - Multi-Agent Design](./08-multi-agent/README.md) | Wann Arbeit auf spezialisierte Agenten verteilt wird. | Entscheiden Sie, ob Ihre Demo einen oder mehrere Agenten braucht. |
| [09 - Metakognition](./09-metacognition/README.md) | Wie Agenten ihre eigenen Ergebnisse überprüfen und verbessern können. | Fügen Sie eine abschließende Selbstprüfung vor der Antwort des Agenten hinzu. |
| [10 - KI-Agenten in der Produktion](./10-ai-agents-production/README.md) | Was sich ändert, wenn ein Agent von der Demo in die Produktion geht. | Listen Sie auf, was Sie überwachen würden: Qualität, Kosten, Latenz, Fehler. |
| [11 - Agentic Protocols](./11-agentic-protocols/README.md) | Wie Protokolle Agenten mit Werkzeugen und anderen Agenten verbinden. | Identifizieren Sie, wo ein Standardprotokoll die Integration vereinfachen könnte. |
| [12 - Kontext-Engineering](./12-context-engineering/README.md) | Wie man Kontext auswählt, zuschneidet, isoliert und verwaltet. | Entscheiden Sie, was in den Prompt gehört und was draußen bleiben soll. |
| [13 - Agenten-Gedächtnis](./13-agent-memory/README.md) | Wie Agenten nützliche Informationen über Interaktionen hinweg speichern können. | Wählen Sie eine sichere Präferenz, die Ihre Demo sich merken könnte. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Framework-spezifische Bausteine für Agenten und Workflows, plus Hosting von LangChain/LangGraph Agenten auf Microsoft Foundry. | Ordnen Sie Ihre Demo-Schritte Framework-Konzepten zu. |
| [15 - Computer-Nutzungsagenten](./15-browser-use/README.md) | Wie Agenten mit Browser- oder UI-Oberflächen interagieren, einschließlich realer Beispiele wie Microsoft Project Opal. | Wählen Sie eine Browser-Aufgabe, die weiterhin Nutzerbestätigung erfordert. |
| [16 - Skalierbare Agenten bereitstellen](./16-deploying-scalable-agents/README.md) | Wie man einen Agenten vom Prototyp zu einer skalierbaren, beobachtbaren Produktion auf Microsoft Foundry bringt (gehostete Agenten, Modellrouten, Caching, Evaluierungstore, Rauchtests). | Listen Sie die Produktionsaspekte auf, die Ihre Demo noch braucht: Hosting, Routing, Kosten, Evaluierung. |
| [17 - Lokale KI-Agenten erstellen](./17-creating-local-ai-agents/README.md) | Wie man lokale Agenten baut, die vollständig auf Ihrem Rechner mit Foundry Local und Qwen laufen (lokale Werkzeuge, lokales RAG, lokales MCP). | Entscheiden Sie, welche Teile Ihrer Demo privat bleiben und lokal laufen sollen. |
| [18 - KI-Agenten absichern](./18-securing-ai-agents/README.md) | Wie man Aktionen von Agenten auditierbarer und manipulationssicher macht. | Entscheiden Sie, welche Aktionen in Ihrer Demo protokolliert oder quittiert werden sollten. |

## Validierung bereitgestellter Agenten mit Rauchtests

Wenn Sie einen Agenten bereitstellen (Lektion 16), ist ein **Rauchtest** die günstigste erste
Prüfung, ob die Bereitstellung tatsächlich antwortet. Dieses Repo enthält fertige
Kataloge unter [tests/](./tests/README.md) für die einsatzbereiten Agenten aus den Lektionen
01, 04, 05 und 16, verbunden mit der
[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
Aktion. Führen Sie sie über den **Actions**-Tab nach der Bereitstellung des Lektionen-Agenten aus.
Rauchtests sind ein erstes Tor — offline und online Evaluation (Lektionen 10 und 16)
zeigen Ihnen, wie *gut* der Agent ist.

## Schlüsselideen in anfängerfreundlicher Sprache

### Werkzeuge

Ein Werkzeug ist etwas, das der Agent aufrufen kann, um Arbeit außerhalb des Modells zu erledigen. Ein gutes Werkzeug
hat einen klaren Namen, eine eng gefasste Aufgabe, typisierte Eingaben, vorhersehbare Ausgaben und einen sicheren Weg,
um Fehler zu handhaben.

Für die Kurshelfer-Demo könnte ein Werkzeug sein:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG und Wissen

RAG hilft dem Agenten, Antworten aus Quellmaterial zu geben, anstatt zu raten. In diesem
Kurs könnte dieses Quellmaterial Lektionen-READMEs, Codebeispiele oder externe
Ressourcen umfassen, die aus den Lektionen verlinkt sind.

Verwenden Sie RAG, wenn die Antwort auf Dokumenten, Daten oder aktuellen
Projektdateien basieren sollte.

### Planung

Planung ist nützlich, wenn die Anfrage aus mehr als einem Schritt besteht. Halten Sie Pläne kurz und
sichtbar genug, damit ein Entwickler oder Nutzer sie überprüfen kann.

Für die Demo könnte ein Plan sein:

1. Finde Lektionen zur Werkzeugnutzung.
2. Fasse die relevantesten Lektionen zusammen.
3. Empfehle eine Übungsaufgabe.

### Kontext

Kontext ist das, was das Modell gerade sieht. Zu wenig Kontext kann dazu führen, dass der Agent
wichtige Details übersieht. Zu viel Kontext kann den Agenten langsamer, teurer
oder anfälliger für Verwirrung machen.

Gutes Kontext-Engineering bedeutet, die richtigen Informationen für den nächsten Modellaufruf auszuwählen.




nur, wenn sie nützlich, sicher und einfach zu aktualisieren oder zu löschen sind.


Sensible persönliche Daten zu speichern ist dagegen meist nicht sinnvoll.


### Bewertung und Beobachtbarkeit

Die Bewertung fragt: Hat der Agent das Richtige getan?

Beobachtbarkeit fragt: Können wir sehen, wie es passiert ist?

Für Produktionsagenten verfolgen Sie Modellaufrufe, Werkzeugaufrufe, abgerufenen Kontext,
Latenz, Kosten, Fehler und Nutzerfeedback.

### Vertrauen und Sicherheit

Vertrauenswürdige Agenten brauchen mehr als nur einen hilfreichen Prompt. Verwenden Sie Werkzeuge mit geringstmöglichen Berechtigungen,
menschliche Zustimmung für risikoreiche Aktionen, Datenredaktion wo nötig, sowie Protokolle oder
Quittungen für Aktionen, die geprüft werden müssen.

## Eine 15-Minuten-Review-Routine

Verwenden Sie diese Routine nach jeder Lektion:

1. **Fassen Sie die Lektion in einem Satz zusammen.**
2. **Nennen Sie die neue Agenten-Fähigkeit.** Zum Beispiel: Werkzeugnutzung, Abruf,
   Planung, Gedächtnis, Beobachtbarkeit oder Sicherheit.
3. **Fügen Sie sie der Kurshelfer-Demo hinzu.** Was ändert sich nun in der Demo?
4. **Finden Sie das Risiko.** Was könnte schiefgehen, wenn diese Fähigkeit missbraucht wird?
5. **Schreiben Sie eine Testfrage.** Wie würden Sie prüfen, ob der Agent sich gut verhält?

## Schneller Selbstcheck

Bevor Sie weitermachen, versuchen Sie diese Fragen zu beantworten:

1. Was kann ein Agent, was ein normaler Chatbot nicht allein kann?
2. Welches Werkzeug würde Ihr Agent zuerst brauchen und warum?
3. Welche Wissensquelle sollte die Antwort des Agenten fundieren?
4. Welcher Kontext sollte in den nächsten Modellaufruf einfließen?
5. Was sollte sich der Agent merken und was sollte vermieden werden zu speichern?
6. Wann sollte der Agent um menschliche Zustimmung bitten?
7. Welche Protokolle, Spuren oder Quittungen würden Ihnen helfen, den Agenten später zu debuggen oder zu prüfen?


## Vorgeschlagene Abschlussübung

Am Ende des Kurses bauen Sie einen kleinen Agenten, der einem Lernenden hilft, sich in diesem
Repository zurechtzufinden.

Mindestversion:

- Ein Thema vom Nutzer annehmen.
- Die relevantesten Lektionen finden.
- Zusammenfassen, was zuerst gelesen werden soll.
- Eine praktische Übungsaufgabe vorschlagen.
- Zeigen, welche Lektionen-Dateien oder Links verwendet wurden.

Erweiterte Version:

- Die bevorzugte Programmiersprache des Lernenden merken.
- Vor der Antwort einen einfachen Plan verwenden.
- Einen Selbstkontrollschritt vor der endgültigen Antwort hinzufügen.
- Werkzeugaufrufe und abgerufene Quellen protokollieren.
- Vor dem Öffnen von Browser- oder UI-Automatisierungsaufgaben um Bestätigung bitten.

Dies gibt Ihnen eine kleine, aber realistische Möglichkeit, Werkzeuge, RAG, Planung,
Kontext, Gedächtnis, Beobachtbarkeit und Vertrauen in einem Projekt zu üben.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->