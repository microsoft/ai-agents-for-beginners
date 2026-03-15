# KI-Agenten in der Produktion: Beobachtbarkeit & Evaluierung

[![KI-Agenten in Produktion](../../../translated_images/de/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Wenn KI-Agenten von experimentellen Prototypen in reale Anwendungen übergehen, wird die Fähigkeit, ihr Verhalten zu verstehen, ihre Leistung zu überwachen und ihre Ausgaben systematisch zu bewerten, wichtig.

## Lernziele

Nach Abschluss dieser Lektion wissen Sie, wie Sie/verstehen:
- Kernkonzepte der Agenten-Beobachtbarkeit und -Evaluierung
- Techniken zur Verbesserung der Leistung, der Kosten und der Effektivität von Agenten
- Was und wie Sie Ihre KI-Agenten systematisch bewerten
- Wie Sie Kosten kontrollieren, wenn Sie KI-Agenten in die Produktion bringen
- Wie Sie Agenten instrumentieren, die mit dem Microsoft Agent Framework erstellt wurden

Ziel ist es, Ihnen das Wissen zu vermitteln, um Ihre „Blackbox“-Agenten in transparente, verwaltbare und zuverlässige Systeme zu verwandeln.

_**Hinweis:** Es ist wichtig, KI-Agenten bereitzustellen, die sicher und vertrauenswürdig sind. Schauen Sie sich auch die Lektion [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md) an._ 

## Traces and Spans

Beobachtbarkeitstools wie [Langfuse](https://langfuse.com/) oder [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) stellen Agentenläufe üblicherweise als Traces und Spans dar.

- **Trace** stellt eine vollständige Agentenaufgabe von Anfang bis Ende dar (z. B. die Bearbeitung einer Benutzeranfrage).
- **Spans** sind einzelne Schritte innerhalb des Traces (z. B. das Aufrufen eines Sprachmodells oder das Abrufen von Daten).

![Trace-Baum in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Ohne Beobachtbarkeit kann sich ein KI-Agent wie eine "Blackbox" anfühlen – sein interner Zustand und seine Schlussfolgerungen sind undurchsichtig, was die Diagnose von Problemen oder die Leistungsoptimierung erschwert. Mit Beobachtbarkeit werden Agenten zu "Glasboxen", die Transparenz bieten, die entscheidend ist, um Vertrauen aufzubauen und sicherzustellen, dass sie wie beabsichtigt arbeiten. 

## Warum Beobachtbarkeit in Produktionsumgebungen wichtig ist

Die Überführung von KI-Agenten in Produktionsumgebungen bringt eine neue Reihe von Herausforderungen und Anforderungen mit sich. Beobachtbarkeit ist nicht mehr nur ein „Nice-to-have“, sondern eine kritische Fähigkeit:

*   **Debugging und Root-Cause-Analyse**: Wenn ein Agent ausfällt oder unerwartete Ausgaben erzeugt, liefern Beobachtungstools die Traces, die benötigt werden, um die Fehlerquelle zu identifizieren. Dies ist besonders wichtig bei komplexen Agenten, die mehrere LLM-Aufrufe, Tool-Interaktionen und bedingte Logik enthalten können.
*   **Latenz- und Kostenmanagement**: KI-Agenten verlassen sich häufig auf LLMs und andere externe APIs, die pro Token oder pro Aufruf abgerechnet werden. Beobachtbarkeit ermöglicht eine präzise Nachverfolgung dieser Aufrufe und hilft, Operationen zu identifizieren, die übermäßig langsam oder teuer sind. Dadurch können Teams Prompts optimieren, effizientere Modelle auswählen oder Workflows neu gestalten, um Betriebskosten zu steuern und ein gutes Nutzererlebnis sicherzustellen.
*   **Vertrauen, Sicherheit und Compliance**: In vielen Anwendungen ist es wichtig sicherzustellen, dass Agenten sicher und ethisch handeln. Beobachtbarkeit liefert eine Prüfspur der Aktionen und Entscheidungen eines Agenten. Diese kann verwendet werden, um Probleme wie Prompt-Injection, die Erzeugung schädlicher Inhalte oder den unsachgemäßen Umgang mit personenbezogenen Daten (PII) zu erkennen und zu mindern. Beispielsweise können Sie Traces überprüfen, um zu verstehen, warum ein Agent eine bestimmte Antwort gegeben oder ein bestimmtes Tool verwendet hat.
*   **Kontinuierliche Verbesserungszyklen**: Beobachtungsdaten sind die Grundlage eines iterativen Entwicklungsprozesses. Durch die Überwachung der Agentenleistung in der realen Welt können Teams Verbesserungsbereiche identifizieren, Daten für das Feintuning von Modellen sammeln und die Auswirkungen von Änderungen validieren. Dies schafft einen Feedback-Loop, in dem Erkenntnisse aus der Online-Evaluierung die Offline-Experimente und -Verfeinerungen informieren und so zu einer schrittweisen Verbesserung der Agentenleistung führen.

## Wichtige Metriken zur Verfolgung

Um das Verhalten von Agenten zu überwachen und zu verstehen, sollten verschiedene Metriken und Signale verfolgt werden. Während die spezifischen Metriken je nach Zweck des Agenten variieren können, sind einige universell wichtig.

Hier sind einige der am häufigsten von Beobachtungstools überwachten Metriken:

**Latenz:** Wie schnell reagiert der Agent? Lange Wartezeiten wirken sich negativ auf die Benutzererfahrung aus. Sie sollten die Latenz für Aufgaben und einzelne Schritte messen, indem Sie Agentenläufe nachverfolgen. Zum Beispiel könnte ein Agent, der für alle Modellaufrufe 20 Sekunden benötigt, durch die Verwendung eines schnelleren Modells oder durch paralleles Ausführen von Modellaufrufen beschleunigt werden.

**Kosten:** Was kostet ein Agentenlauf? KI-Agenten sind auf LLM-Aufrufe angewiesen, die pro Token oder externe APIs abgerechnet werden. Häufige Tool-Nutzung oder mehrere Prompts können die Kosten schnell in die Höhe treiben. Wenn ein Agent beispielsweise ein LLM fünfmal aufruft, um nur marginale Qualitätsverbesserungen zu erzielen, müssen Sie beurteilen, ob die Kosten gerechtfertigt sind oder ob Sie die Anzahl der Aufrufe reduzieren oder ein günstigeres Modell verwenden können. Echtzeitüberwachung kann auch helfen, unerwartete Spitzen zu erkennen (z. B. Bugs, die zu exzessiven API-Schleifen führen).

**Anforderungsfehler:** Wie viele Anfragen sind fehlgeschlagen? Dies kann API-Fehler oder fehlgeschlagene Tool-Aufrufe umfassen. Um Ihren Agenten in der Produktion robuster gegen solche Fehler zu machen, können Sie Fallbacks oder Retries einrichten. Z. B. wenn LLM-Anbieter A ausfällt, wechseln Sie zu LLM-Anbieter B als Backup.

**Nutzerfeedback:** Die Implementierung direkter Nutzerevaluationen liefert wertvolle Einblicke. Dies kann explizite Bewertungen umfassen (Daumen hoch/👎 Daumen runter, ⭐1–5 Sterne) oder textuelle Kommentare. Konsequent negatives Feedback sollte Sie alarmieren, da dies ein Zeichen dafür ist, dass der Agent nicht wie erwartet funktioniert. 

**Implizites Nutzerfeedback:** Nutzerverhalten liefert indirektes Feedback auch ohne explizite Bewertungen. Dies kann sofortiges Umformulieren von Fragen, wiederholte Anfragen oder das Klicken eines Wiederholungs-Buttons sein. Z. B. wenn Sie sehen, dass Nutzer wiederholt dieselbe Frage stellen, ist das ein Zeichen dafür, dass der Agent nicht wie erwartet funktioniert.

**Genauigkeit:** Wie häufig liefert der Agent korrekte oder gewünschte Ausgaben? Die Definition von Genauigkeit variiert (z. B. Problemlösungsrichtigkeit, Informationsabrufgenauigkeit, Nutzerzufriedenheit). Der erste Schritt ist, zu definieren, wie Erfolg für Ihren Agenten aussieht. Sie können Genauigkeit über automatisierte Prüfungen, Bewertungsscores oder Task-Completion-Labels verfolgen. Zum Beispiel, indem Sie Traces als „succeeded“ oder „failed“ markieren. 

**Automatisierte Evaluierungsmetriken:** Sie können auch automatisierte Evals einrichten. Beispielsweise können Sie ein LLM verwenden, um die Ausgabe des Agenten zu bewerten, z. B. ob sie hilfreich, korrekt oder nicht ist. Es gibt auch mehrere Open-Source-Bibliotheken, die Ihnen helfen, verschiedene Aspekte des Agenten zu bewerten. Z. B. [RAGAS](https://docs.ragas.io/) für RAG-Agenten oder [LLM Guard](https://llm-guard.com/) zur Erkennung schädlicher Sprache oder Prompt-Injection. 

In der Praxis bietet eine Kombination dieser Metriken die beste Abdeckung der Agentengesundheit. In diesem Kapitels [Beispiel-Notebook](./code_samples/10-expense_claim-demo.ipynb) zeigen wir Ihnen, wie diese Metriken in realen Beispielen aussehen, aber zuerst lernen wir, wie ein typischer Evaluierungsworkflow aussieht.

## Instrumentieren Sie Ihren Agenten

Um Tracing-Daten zu sammeln, müssen Sie Ihren Code instrumentieren. Das Ziel ist, den Agentencode so zu instrumentieren, dass Traces und Metriken erzeugt werden, die von einer Beobachtungsplattform erfasst, verarbeitet und visualisiert werden können.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) hat sich als Industriestandard für LLM-Beobachtbarkeit etabliert. Es bietet eine Reihe von APIs, SDKs und Tools zum Erzeugen, Sammeln und Exportieren von Telemetriedaten. 

Es gibt viele Instrumentierungsbibliotheken, die vorhandene Agentenframeworks umhüllen und das Exportieren von OpenTelemetry-Spans zu einem Beobachtungstool erleichtern. Das Microsoft Agent Framework integriert sich nativ mit OpenTelemetry. Unten ein Beispiel zur Instrumentierung eines MAF-Agenten:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Die Ausführung des Agenten wird automatisch protokolliert
    pass
```

Das [Beispiel-Notebook](./code_samples/10-expense_claim-demo.ipynb) in diesem Kapitel zeigt, wie Sie Ihren MAF-Agenten instrumentieren.

**Manuelle Span-Erstellung:** Während Instrumentierungsbibliotheken eine gute Basis bieten, gibt es oft Fälle, in denen detailliertere oder benutzerdefinierte Informationen benötigt werden. Sie können Spans manuell erstellen, um benutzerdefinierte Anwendungslogik hinzuzufügen. Wichtiger ist, dass Sie automatisch oder manuell erstellte Spans mit benutzerdefinierten Attributen (auch bekannt als Tags oder Metadaten) anreichern können. Diese Attribute können geschäftsspezifische Daten, Zwischenberechnungen oder jeglichen Kontext enthalten, der für Debugging oder Analyse nützlich sein könnte, wie `user_id`, `session_id` oder `model_version`.

Beispiel zur manuellen Erstellung von Traces und Spans mit dem [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentenbewertung

Beobachtbarkeit liefert uns Metriken, aber Evaluierung ist der Prozess der Analyse dieser Daten (und der Durchführung von Tests), um zu bestimmen, wie gut ein KI-Agent arbeitet und wie er verbessert werden kann. Mit anderen Worten: Sobald Sie diese Traces und Metriken haben, wie verwenden Sie sie, um den Agenten zu beurteilen und Entscheidungen zu treffen? 

Regelmäßige Evaluierungen sind wichtig, weil KI-Agenten oft nicht deterministisch sind und sich weiterentwickeln können (durch Updates oder driftendes Modellverhalten) – ohne Evaluierung wüssten Sie nicht, ob Ihr „smarter Agent“ seine Aufgabe wirklich gut erfüllt oder ob er sich verschlechtert hat.

Es gibt zwei Kategorien von Evaluierungen für KI-Agenten: **Online-Evaluierung** und **Offline-Evaluierung**. Beide sind wertvoll und ergänzen einander. Normalerweise beginnen wir mit der Offline-Evaluierung, da dies der Mindestschritt ist, bevor ein Agent bereitgestellt wird.

### Offline-Evaluierung

![Datensatzelemente in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dies umfasst die Bewertung des Agenten in einer kontrollierten Umgebung, typischerweise unter Verwendung von Testdatensätzen und nicht mit Live-Benutzeranfragen. Sie verwenden kuratierte Datensätze, bei denen Sie wissen, welche Ausgabe oder welches Verhalten erwartet wird, und lassen dann Ihren Agenten diese durchlaufen. 

Wenn Sie beispielsweise einen Agenten für Mathematiktextaufgaben gebaut haben, könnten Sie einen [Testdatensatz](https://huggingface.co/datasets/gsm8k) mit 100 Aufgaben und bekannten Antworten haben. Offline-Evaluierung wird oft während der Entwicklung durchgeführt (und kann Teil von CI/CD-Pipelines sein), um Verbesserungen zu prüfen oder Regressionen zu verhindern. Der Vorteil ist, dass sie **wiederholbar ist und Sie klare Genauigkeitsmetriken erhalten, da Sie eine Ground Truth haben**. Sie könnten auch Nutzeranfragen simulieren und die Antworten des Agenten mit idealen Antworten vergleichen oder automatisierte Metriken wie oben beschrieben verwenden. 

Die zentrale Herausforderung bei Offline-Evaluierung besteht darin, sicherzustellen, dass Ihr Testdatensatz umfassend und relevant bleibt – der Agent kann bei einem festen Testset gut abschneiden, aber in der Produktion mit sehr unterschiedlichen Anfragen konfrontiert werden. Daher sollten Sie Testsets mit neuen Edge-Cases und Beispielen aktualisieren, die reale Szenarien widerspiegeln​. Eine Mischung aus kleinen „Smoke-Tests“ und größeren Evaluationssätzen ist nützlich: kleine Sets für schnelle Checks und größere für breitere Leistungsmetriken​.

### Online-Evaluierung 

![Übersicht der Observability-Metriken](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dies bezieht sich auf die Bewertung des Agenten in einer Live-, realen Umgebung, d. h. während der tatsächlichen Nutzung in der Produktion. Online-Evaluierung umfasst die Überwachung der Agentenleistung bei echten Nutzerinteraktionen und die kontinuierliche Analyse der Ergebnisse. 

Zum Beispiel könnten Sie Erfolgsraten, Nutzerzufriedenheitswerte oder andere Metriken im Live-Traffic verfolgen. Der Vorteil der Online-Evaluierung ist, dass sie **Dinge erfasst, die Sie im Labor vielleicht nicht vorhersehen** – Sie können Modell-Drift im Laufe der Zeit beobachten (wenn die Effektivität des Agenten abnimmt, weil sich Eingabemuster ändern) und unerwartete Anfragen oder Situationen erfassen, die nicht in Ihren Testdaten enthalten waren​. Sie liefert ein realistisches Bild davon, wie sich der Agent in freier Wildbahn verhält. 

Die Online-Evaluierung umfasst oft das Sammeln impliziten und expliziten Nutzerfeedbacks, wie oben beschrieben, und kann das Durchführen von Shadow-Tests oder A/B-Tests umfassen (wobei eine neue Version des Agenten parallel läuft, um sie mit der alten zu vergleichen). Die Herausforderung besteht darin, zuverlässige Labels oder Scores für Live-Interaktionen zu erhalten – Sie könnten auf Nutzerfeedback oder nachgelagerte Metriken angewiesen sein (z. B. ob der Nutzer auf das Ergebnis geklickt hat). 

### Kombination der beiden

Online- und Offline-Evaluierungen schließen sich nicht gegenseitig aus; sie ergänzen einander stark. Erkenntnisse aus dem Online-Monitoring (z. B. neue Arten von Nutzeranfragen, bei denen der Agent schlecht abschneidet) können verwendet werden, um Offline-Testdatensätze zu erweitern und zu verbessern. Umgekehrt können Agenten, die in Offline-Tests gut abschneiden, mit größerer Zuversicht online bereitgestellt und überwacht werden. 

Tatsächlich verfolgen viele Teams einen Kreislauf: 

_evaluiere offline -> bereitstellen -> online überwachen -> neue Fehlerfälle sammeln -> zum Offline-Datensatz hinzufügen -> Agent verfeinern -> wiederholen_.

## Häufige Probleme

Wenn Sie KI-Agenten in die Produktion bringen, können verschiedene Herausforderungen auftreten. Hier sind einige häufige Probleme und mögliche Lösungen:

| **Problem**    | **Mögliche Lösung**   |
| ------------- | ------------------ |
| KI-Agent erfüllt Aufgaben nicht konsistent | - Verfeinern Sie das Prompt, das dem KI-Agenten gegeben wird; seien Sie klar in den Zielen.<br>- Identifizieren Sie, wo das Aufteilen der Aufgaben in Teilaufgaben und deren Bearbeitung durch mehrere Agenten helfen kann. |
| KI-Agent gerät in Endlosschleifen  | - Stellen Sie sicher, dass Sie klare Abbruchbedingungen haben, damit der Agent weiß, wann der Prozess zu stoppen ist.<br>- Bei komplexen Aufgaben, die Schlussfolgerungen und Planung erfordern, verwenden Sie ein größeres Modell, das auf Reasoning-Aufgaben spezialisiert ist. |
| Tool-Aufrufe des KI-Agenten funktionieren nicht gut   | - Testen und validieren Sie die Ausgabe des Tools außerhalb des Agentensystems.<br>- Verfeinern Sie die definierten Parameter, Prompts und die Benennung der Tools.  |
| Multi-Agenten-System arbeitet nicht konsistent | - Verfeinern Sie die Prompts, die jedem Agenten gegeben werden, um sicherzustellen, dass sie spezifisch und unterscheidbar sind.<br>- Bauen Sie ein hierarchisches System mit einem "Routing"- oder Controller-Agenten auf, der entscheidet, welcher Agent der richtige ist. |

Viele dieser Probleme lassen sich mit implementierter Beobachtbarkeit effektiver identifizieren. Die zuvor besprochenen Traces und Metriken helfen genau zu lokalisieren, wo im Agenten-Workflow Probleme auftreten, wodurch Debugging und Optimierung deutlich effizienter werden.

## Kosten verwalten
Hier sind einige Strategien, um die Kosten beim Einsatz von KI-Agenten in der Produktion zu senken:

**Kleinere Modelle verwenden:** Kleine Sprachmodelle (SLMs) können in bestimmten agentischen Anwendungsfällen gut abschneiden und die Kosten erheblich senken. Wie bereits erwähnt, ist der Aufbau eines Bewertungssystems, um die Leistung im Vergleich zu größeren Modellen zu ermitteln und zu vergleichen, der beste Weg, um zu verstehen, wie gut ein SLM in Ihrem Anwendungsfall abschneiden wird. Erwägen Sie den Einsatz von SLMs für einfachere Aufgaben wie Intent-Klassifizierung oder Parameterextraktion, während Sie größere Modelle für komplexe Schlussfolgerungen reservieren.

**Ein Router-Modell verwenden:** Eine ähnliche Strategie besteht darin, verschiedene Modelle und Größen zu nutzen. Sie können ein LLM/SLM oder eine serverlose Funktion verwenden, um Anfragen je nach Komplexität an die am besten geeigneten Modelle weiterzuleiten. Dies hilft ebenfalls, Kosten zu senken und gleichzeitig bei den richtigen Aufgaben die gewünschte Leistung sicherzustellen. Leiten Sie beispielsweise einfache Anfragen an kleinere, schnellere Modelle weiter und verwenden Sie teure große Modelle nur für komplexe Schlussfolgerungsaufgaben.

**Antworten zwischenspeichern:** Die Identifizierung häufiger Anfragen und Aufgaben und das Vorabbereitstellen der Antworten, bevor sie Ihr agentisches System durchlaufen, ist eine gute Möglichkeit, das Volumen ähnlicher Anfragen zu reduzieren. Sie können sogar einen Ablauf implementieren, um mit einfacheren KI-Modellen zu ermitteln, wie ähnlich eine Anfrage Ihren zwischengespeicherten Anfragen ist. Diese Strategie kann die Kosten für häufig gestellte Fragen oder gängige Workflows erheblich senken.

## Schauen wir uns an, wie das in der Praxis funktioniert

In dem [Beispiel-Notebook dieses Abschnitts](./code_samples/10-expense_claim-demo.ipynb) werden wir Beispiele dafür sehen, wie wir Observability-Tools einsetzen können, um unseren Agenten zu überwachen und zu bewerten.

### Noch Fragen zu KI-Agenten in der Produktion?

Treten Sie dem [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) bei, um andere Lernende zu treffen, an Sprechstunden teilzunehmen und Ihre Fragen zu KI-Agenten beantwortet zu bekommen.

## Vorherige Lektion

[Metakognition-Designmuster](../09-metacognition/README.md)

## Nächste Lektion

[Agentische Protokolle](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Haftungsausschluss:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst Co-op Translator (https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das ursprüngliche Dokument in der Originalsprache ist als maßgebliche Quelle zu betrachten. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Für Missverständnisse oder Fehlinterpretationen, die sich aus der Verwendung dieser Übersetzung ergeben, übernehmen wir keine Haftung.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->