# KI-Agenten in der Produktion: Beobachtbarkeit & Bewertung

[![KI-Agenten in der Produktion](../../../translated_images/de/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Wenn KI-Agenten von experimentellen Prototypen zu Anwendungen in der realen Welt übergehen, wird die Fähigkeit, ihr Verhalten zu verstehen, ihre Leistung zu überwachen und ihre Ergebnisse systematisch zu bewerten, wichtig.

## Lernziele

Nach Abschluss dieser Lektion werden Sie wissen, wie man/was man versteht:
- Kernkonzepte der Beobachtbarkeit und Bewertung von Agenten
- Techniken zur Verbesserung der Leistung, Kosten und Effektivität von Agenten
- Was und wie Sie Ihre KI-Agenten systematisch bewerten
- Wie Sie Kosten bei der Bereitstellung von KI-Agenten in der Produktion kontrollieren
- Wie man Agenten, die mit dem Microsoft Agent Framework gebaut wurden, instrumentiert

Das Ziel ist, Sie mit dem Wissen auszustatten, um Ihre „Black-Box“-Agenten in transparente, verwaltbare und zuverlässige Systeme zu verwandeln.

_**Hinweis:** Es ist wichtig, KI-Agenten bereitzustellen, die sicher und vertrauenswürdig sind. Sehen Sie sich auch die Lektion [Vertrauenswürdige KI-Agenten bauen](../06-building-trustworthy-agents/README.md) an._

## Traces und Spans

Beobachtbarkeitstools wie [Langfuse](https://langfuse.com/) oder [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) repräsentieren Agentenläufe üblicherweise als Traces und Spans.

- **Trace** stellt eine komplette Agentenaufgabe von Anfang bis Ende dar (z. B. das Bearbeiten einer Benutzeranfrage).
- **Spans** sind einzelne Schritte innerhalb des Traces (z. B. das Aufrufen eines Sprachmodells oder das Abrufen von Daten).

![Trace-Baum in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Ohne Beobachtbarkeit kann sich ein KI-Agent wie eine „Black Box“ anfühlen – sein interner Zustand und seine Entscheidungswege sind undurchsichtig, was es schwierig macht, Probleme zu diagnostizieren oder die Leistung zu optimieren. Mit Beobachtbarkeit werden Agenten zu „Glass Boxes“, die eine Transparenz bieten, die wesentlich für den Aufbau von Vertrauen und die Sicherstellung ist, dass sie wie vorgesehen arbeiten.

## Warum Beobachtbarkeit in Produktionsumgebungen wichtig ist

Der Übergang von KI-Agenten in Produktionsumgebungen bringt eine neue Reihe von Herausforderungen und Anforderungen mit sich. Beobachtbarkeit ist kein „Nice-to-have“ mehr, sondern eine kritische Fähigkeit:

*   **Fehlerbehebung und Ursachenanalyse:** Wenn ein Agent ausfällt oder unerwartete Ergebnisse liefert, bieten Beobachtbarkeitstools die Traces, die benötigt werden, um die Fehlerquelle zu finden. Dies ist besonders wichtig bei komplexen Agenten, die mehrere LLM-Aufrufe, Werkzeuginteraktionen und bedingte Logik beinhalten können.
*   **Latenz- und Kostenmanagement:** KI-Agenten basieren oft auf LLMs und anderen externen APIs, die pro Token oder pro Aufruf abgerechnet werden. Beobachtbarkeit ermöglicht eine genaue Nachverfolgung dieser Aufrufe, hilft, langsam oder teuer auszuführende Operationen zu identifizieren, optimiert so Prompts, wählt effizientere Modelle aus oder gestaltet Arbeitsabläufe neu, um Betriebskosten zu steuern und eine gute Benutzererfahrung sicherzustellen.
*   **Vertrauen, Sicherheit und Compliance:** In vielen Anwendungen ist es wichtig, sicherzustellen, dass Agenten sicher und ethisch handeln. Beobachtbarkeit bietet eine Prüfkette der Aktionen und Entscheidungen des Agenten. Diese kann verwendet werden, um Probleme wie Prompt Injection, die Erzeugung schädlicher Inhalte oder den unsachgemäßen Umgang mit personenbezogenen Daten (PII) zu erkennen und zu mindern. Zum Beispiel können Sie Traces überprüfen, um zu verstehen, warum ein Agent eine bestimmte Antwort gab oder ein bestimmtes Werkzeug einsetzte.
*   **Kontinuierliche Verbesserungszyklen:** Beobachtbarkeitsdaten bilden die Grundlage für einen iterativen Entwicklungsprozess. Durch die Überwachung der Leistung von Agenten in der realen Welt können Teams Verbesserungsbereiche identifizieren, Daten zur Feinabstimmung von Modellen sammeln und die Auswirkungen von Änderungen validieren. Dies schafft eine Feedback-Schleife, in der Produktionserkenntnisse aus der Online-Bewertung Offline-Experimente und Verfeinerungen informieren, was zu einer stetig besseren Agentenleistung führt.

## Wichtige Metriken zur Nachverfolgung

Um das Verhalten von Agenten zu überwachen und zu verstehen, sollten verschiedene Metriken und Signale verfolgt werden. Während die spezifischen Metriken je nach Zweck des Agenten variieren können, sind einige universell wichtig.

Hier sind einige der häufigsten Metriken, die Beobachtbarkeitstools überwachen:

**Latenz:** Wie schnell antwortet der Agent? Lange Wartezeiten beeinträchtigen die Benutzererfahrung negativ. Sie sollten die Latenz für Aufgaben und einzelne Schritte durch das Tracing von Agentenläufen messen. Zum Beispiel kann ein Agent, der 20 Sekunden für alle Modellaufrufe benötigt, beschleunigt werden, indem ein schnelleres Modell verwendet wird oder Modellaufrufe parallel ausgeführt werden.

**Kosten:** Wie hoch sind die Kosten pro Agentenlauf? KI-Agenten basieren auf LLM-Aufrufen, die pro Token oder externe APIs abgerechnet werden. Häufige Werkzeugverwendung oder mehrere Prompts können die Kosten schnell erhöhen. Wenn ein Agent beispielsweise ein LLM fünfmal für eine marginale Qualitätsverbesserung aufruft, müssen Sie bewerten, ob die Kosten gerechtfertigt sind oder ob Sie die Anzahl der Aufrufe reduzieren oder ein günstigeres Modell nutzen können. Echtzeitüberwachung kann auch helfen, unerwartete Spitzen zu erkennen (z. B. Fehler, die zu übermäßigen API-Schleifen führen).

**Anfragefehler:** Wie viele Anfragen scheiterten beim Agenten? Dies kann API-Fehler oder fehlgeschlagene Werkzeugaufrufe umfassen. Um Ihren Agenten in der Produktion robuster dagegen zu machen, können Sie Ausweichmechanismen oder Wiederholungen einrichten. Zum Beispiel, wenn LLM-Anbieter A ausfällt, können Sie als Backup zu Anbieter B wechseln.

**Nutzerfeedback:** Die Implementierung direkter Benutzerauswertungen liefert wertvolle Einblicke. Dazu gehören explizite Bewertungen (👍Daumen hoch/👎Daumen runter, ⭐1-5 Sterne) oder Textkommentare. Konsistent negatives Feedback sollte Sie warnen, da dies ein Zeichen dafür ist, dass der Agent nicht wie erwartet funktioniert.

**Implizites Nutzerfeedback:** Benutzerverhalten liefert auch indirektes Feedback, selbst ohne explizite Bewertungen. Dies kann unmittelbares Umschreiben der Fragen, wiederholte Anfragen oder das Klicken eines Wiederholungsbuttons umfassen. Beispielsweise ist es ein Zeichen, dass der Agent nicht wie erwartet funktioniert, wenn Benutzer dieselbe Frage wiederholt stellen.

**Genauigkeit:** Wie häufig erzeugt der Agent korrekte oder gewünschte Ausgaben? Die Definition der Genauigkeit variiert (z. B. Korrektheit der Problemlösung, Genauigkeit der Informationsrückgewinnung, Benutzerzufriedenheit). Der erste Schritt ist, zu definieren, wie Erfolg für Ihren Agenten aussieht. Sie können die Genauigkeit über automatisierte Prüfungen, Bewertungsergebnisse oder Aufgabenabschlussmarkierungen verfolgen. Zum Beispiel durch Markierung von Traces als „erfolgreich“ oder „fehlgeschlagen“.

**Automatisierte Bewertungsmetriken:** Sie können auch automatisierte Bewertungen einrichten. Beispielsweise können Sie ein LLM nutzen, um die Ausgabe des Agenten zu bewerten, z. B. ob sie hilfreich, genau oder nicht ist. Es gibt auch mehrere Open-Source-Bibliotheken, die Ihnen helfen, unterschiedliche Aspekte des Agenten zu bewerten, wie [RAGAS](https://docs.ragas.io/) für RAG-Agenten oder [LLM Guard](https://llm-guard.com/) zur Erkennung schädlicher Sprache oder Prompt Injection.

In der Praxis bietet eine Kombination dieser Metriken die beste Abdeckung des Zustands eines KI-Agenten. Im [Beispielnotebook](./code_samples/10-expense_claim-demo.ipynb) in diesem Kapitel zeigen wir Ihnen, wie diese Metriken in realen Beispielen aussehen, aber zuerst lernen wir, wie ein typischer Bewertungsablauf aussieht.

## Instrumentieren Sie Ihren Agenten

Um Tracing-Daten zu sammeln, müssen Sie Ihren Code instrumentieren. Das Ziel ist, den Agentencode so zu instrumentieren, dass er Traces und Metriken erzeugt, die von einer Beobachtbarkeitsplattform erfasst, verarbeitet und visualisiert werden können.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) hat sich als Industriestandard für die Beobachtbarkeit von LLMs etabliert. Es bietet eine Sammlung von APIs, SDKs und Werkzeugen zur Erzeugung, Sammlung und Export von Telemetriedaten.

Es gibt viele Instrumentierungs-Bibliotheken, die existierende Agentenframeworks umschließen und es einfach machen, OpenTelemetry-Spans zu einem Beobachtbarkeitstool zu exportieren. Microsoft Agent Framework integriert OpenTelemetry nativ. Unten sehen Sie ein Beispiel zur Instrumentierung eines MAF-Agenten:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Die Ausführung des Agenten wird automatisch verfolgt
    pass
```

Das [Beispielnotebook](./code_samples/10-expense_claim-demo.ipynb) in diesem Kapitel demonstriert, wie Sie Ihren MAF-Agenten instrumentieren.

**Manuelle Span-Erstellung:** Während Instrumentierungsbibliotheken eine gute Basis bieten, gibt es oft Fälle, in denen detailliertere oder kundenspezifische Informationen benötigt werden. Sie können Spans manuell erstellen, um kundenspezifische Anwendungslogik hinzuzufügen. Noch wichtiger ist, dass sie automatisch oder manuell erstellte Spans mit benutzerdefinierten Attributen (auch als Tags oder Metadaten bekannt) erweitern können. Diese Attribute können business-spezifische Daten, Zwischenberechnungen oder jeden Kontext enthalten, der für Debugging oder Analyse nützlich sein könnte, wie `user_id`, `session_id` oder `model_version`.

Beispiel für die manuelle Erstellung von Traces und Spans mit dem [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentenbewertung

Beobachtbarkeit liefert uns Metriken, aber Bewertung ist der Prozess der Analyse dieser Daten (und das Durchführen von Tests), um zu bestimmen, wie gut ein KI-Agent arbeitet und wie er verbessert werden kann. Anders gesagt: Sobald Sie diese Traces und Metriken haben, wie nutzen Sie sie, um den Agenten zu beurteilen und Entscheidungen zu treffen?

Regelmäßige Bewertung ist wichtig, weil KI-Agenten oft nicht deterministisch sind und sich entwickeln können (durch Updates oder sich änderndes Modellverhalten) – ohne Bewertung würden Sie nicht wissen, ob Ihr „intelligenter Agent“ seine Arbeit gut macht oder ob es eine Regression gibt.

Es gibt zwei Kategorien von Bewertungen für KI-Agenten: **Online-Bewertung** und **Offline-Bewertung**. Beide sind wertvoll und ergänzen sich. Üblicherweise beginnen wir mit der Offline-Bewertung, da dies der minimale notwendige Schritt vor der Bereitstellung eines Agenten ist.

### Offline-Bewertung

![Datensatz-Einträge in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dies beinhaltet die Bewertung des Agenten in einer kontrollierten Umgebung, typischerweise unter Verwendung von Testdatensätzen, nicht live Benutzeranfragen. Sie verwenden kuratierte Datensätze, bei denen Sie wissen, was die erwartete Ausgabe oder das korrekte Verhalten ist, und führen dann den Agenten darauf aus.

Zum Beispiel, wenn Sie einen Agenten für mathematische Textaufgaben gebaut haben, könnten Sie einen [Testdatensatz](https://huggingface.co/datasets/gsm8k) mit 100 Problemen und bekannten Antworten haben. Offline-Bewertungen werden oft während der Entwicklung durchgeführt (und können Teil von CI/CD-Pipelines sein), um Verbesserungen zu prüfen oder Regressionen vorzubeugen. Der Vorteil ist, dass es **wiederholbar ist und Sie klare Genauigkeitsmetriken haben, da Sie eine Ground Truth besitzen**. Sie können auch Benutzanfragen simulieren und die Antworten des Agenten mit idealen Antworten abgleichen oder automatisierte Metriken wie oben beschrieben verwenden.

Die wichtigste Herausforderung bei der Offline-Bewertung besteht darin, sicherzustellen, dass Ihr Testdatensatz umfassend und relevant bleibt – der Agent könnte auf einem festen Testsatz gut abschneiden, aber in der Produktion auf sehr unterschiedliche Anfragen stoßen. Daher sollten Testsets mit neuen Randfällen und Beispielen, die reale Szenarien widerspiegeln, aktualisiert werden. Eine Mischung aus kleinen „Smoke Tests“ und größeren Bewertungssets ist nützlich: kleine Sets für schnelle Prüfungen und größere für breitere Leistungsmetriken.

### Online-Bewertung

![Übersicht der Beobachtbarkeitsmetriken](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dies bezieht sich darauf, den Agenten in einer live, realen Umgebung zu bewerten, also während des tatsächlichen Einsatzes in der Produktion. Die Online-Bewertung umfasst die Überwachung der Agentenleistung bei echten Benutzerinteraktionen und die kontinuierliche Analyse der Ergebnisse.

Zum Beispiel können Sie Erfolgsraten, Benutzerzufriedenheitswerte oder andere Metriken im Live-Verkehr verfolgen. Der Vorteil der Online-Bewertung ist, dass sie **Aspekte erfasst, die Sie in Laborsituationen möglicherweise nicht vorhersehen** – Sie können Modell-Drift über die Zeit beobachten (wenn die Effektivität des Agenten nachlässt, weil sich Eingabemuster ändern) und unerwartete Anfragen oder Situationen erfassen, die nicht in Ihren Testdaten enthalten waren. Es bietet ein echtes Bild davon, wie der Agent „in freier Wildbahn“ funktioniert.

Die Online-Bewertung umfasst oft das Sammeln impliziten und expliziten Nutzerfeedbacks, wie besprochen, und möglicherweise das Durchführen von Shadow-Tests oder A/B-Tests (bei denen eine neue Agentenversion parallel läuft, um mit der alten zu vergleichen). Die Herausforderung besteht darin, zuverlässige Labels oder Bewertungen für Live-Interaktionen zu erhalten – Sie könnten sich auf Nutzerfeedback oder nachgelagerte Metriken verlassen (z. B. ob der Nutzer das Ergebnis angeklickt hat).

### Kombination der beiden

Online- und Offline-Bewertungen schließen sich nicht aus; sie ergänzen sich sehr gut. Erkenntnisse aus der Online-Überwachung (z. B. neue Arten von Benutzeranfragen, bei denen der Agent schlecht abschneidet) können verwendet werden, um Offline-Testdatensätze zu ergänzen und zu verbessern. Umgekehrt können Agenten, die bei Offline-Tests gut abschneiden, mit größerem Vertrauen online bereitgestellt und überwacht werden.

Tatsächlich übernehmen viele Teams eine Schleife:

_offline bewerten -> bereitstellen -> online überwachen -> neue Fehlerfälle sammeln -> zum Offline-Datensatz hinzufügen -> Agent verfeinern -> wiederholen_.

## Häufige Probleme

Wenn Sie KI-Agenten in der Produktion bereitstellen, können verschiedene Herausforderungen auftreten. Hier sind einige häufige Probleme und mögliche Lösungen:

| **Problem**    | **Mögliche Lösung**   |
| ------------- | ------------------ |
| KI-Agent arbeitet inkonsistent | - Verfeinern Sie das dem KI-Agenten gegebene Prompt; seien Sie klar in Ihren Zielsetzungen.<br>- Ermitteln Sie, wo das Aufteilen in Teilaufgaben und die Bearbeitung durch mehrere Agenten helfen kann. |
| KI-Agent läuft in Endlosschleifen  | - Stellen Sie klare Abbruchbedingungen sicher, damit der Agent weiß, wann er den Prozess stoppen soll.<br>- Für komplexe Aufgaben mit Anforderungen an Logik und Planung verwenden Sie ein größeres, auf solche Aufgaben spezialisiertes Modell. |
| Aufrufe von KI-Agenten-Werkzeugen funktionieren schlecht   | - Testen und validieren Sie die Ausgaben des Werkzeugs außerhalb des Agentensystems.<br>- Verfeinern Sie die definierten Parameter, Prompts und die Benennung der Werkzeuge.  |
| Multi-Agenten-System arbeitet inkonsistent | - Verfeinern Sie die Prompts für jeden Agenten, um sicherzustellen, dass sie spezifisch und voneinander unterscheidbar sind.<br>- Bauen Sie ein hierarchisches System mit einem „Routing“- oder Steueragenten auf, der bestimmt, welcher Agent der richtige ist. |

Viele dieser Probleme können mit implementierter Beobachtbarkeit effektiver identifiziert werden. Die bereits besprochenen Traces und Metriken helfen dabei, genau zu ermitteln, wo im Agenten-Workflow Probleme auftreten, was Fehlerbehebung und Optimierung deutlich effizienter macht.

## Kostenmanagement


Hier sind einige Strategien, um die Kosten für den Einsatz von KI-Agenten in der Produktion zu verwalten:

**Verwendung kleinerer Modelle:** Kleine Sprachmodelle (SLMs) können bei bestimmten agentischen Anwendungsfällen gute Leistungen erbringen und die Kosten erheblich senken. Wie bereits erwähnt, ist der Aufbau eines Bewertungssystems zur Bestimmung und zum Vergleich der Leistung gegenüber größeren Modellen der beste Weg, um zu verstehen, wie gut ein SLM in Ihrem Anwendungsfall abschneiden wird. Erwägen Sie, SLMs für einfachere Aufgaben wie Absichtsklassifizierung oder Parameterextraktion zu verwenden, während Sie größere Modelle für komplexes Denken reservieren.

**Verwendung eines Router-Modells:** Eine ähnliche Strategie besteht darin, eine Vielfalt von Modellen und Größen zu verwenden. Sie können ein LLM/SLM oder eine serverlose Funktion verwenden, um Anfragen basierend auf der Komplexität an die am besten geeigneten Modelle zu leiten. Dies hilft ebenfalls, Kosten zu senken und gleichzeitig die Leistung bei den richtigen Aufgaben sicherzustellen. Leiten Sie zum Beispiel einfache Abfragen an kleinere, schnellere Modelle weiter und verwenden Sie teure große Modelle nur für komplexe Denkaufgaben.

**Zwischenspeicherung von Antworten:** Das Identifizieren häufiger Anfragen und Aufgaben und das Bereitstellen der Antworten, bevor sie Ihr agentisches System durchlaufen, ist eine gute Methode zur Reduzierung der Menge ähnlicher Anfragen. Sie können sogar einen Ablauf implementieren, um zu erkennen, wie ähnlich eine Anfrage Ihren zwischengespeicherten Anfragen ist, indem Sie einfachere KI-Modelle verwenden. Diese Strategie kann die Kosten für häufig gestellte Fragen oder gängige Arbeitsabläufe erheblich senken.

## Schauen wir uns an, wie das in der Praxis funktioniert

Im [Beispiel-Notebook dieses Abschnitts](./code_samples/10-expense_claim-demo.ipynb) sehen wir Beispiele dafür, wie wir Beobachtungs-Tools nutzen können, um unseren Agenten zu überwachen und zu bewerten.


### Haben Sie weitere Fragen zu KI-Agenten in der Produktion?

Treten Sie dem [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten beantwortet zu bekommen.

## Vorherige Lektion

[Metakognition Design Muster](../09-metacognition/README.md)

## Nächste Lektion

[Agentische Protokolle](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->