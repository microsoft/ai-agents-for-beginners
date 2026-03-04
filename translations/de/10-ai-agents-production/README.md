# KI-Agenten in Produktion: Beobachtbarkeit & Evaluation

[![KI-Agenten in Produktion](../../../translated_images/de/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Da KI-Agenten von experimentellen Prototypen zu realen Anwendungen übergehen, wird die Fähigkeit, ihr Verhalten zu verstehen, ihre Leistung zu überwachen und ihre Ausgaben systematisch zu bewerten, immer wichtiger.

## Lernziele

Nach Abschluss dieser Lektion werden Sie wissen/verstanden haben:
- Kernkonzepte der Beobachtbarkeit und Evaluation von Agenten
- Techniken zur Verbesserung der Leistung, der Kosten und der Effektivität von Agenten
- Was und wie Sie Ihre KI-Agenten systematisch evaluieren
- Wie Sie die Kosten bei der Bereitstellung von KI-Agenten in der Produktion kontrollieren
- Wie Sie Agenten, die mit AutoGen gebaut wurden, instrumentieren

Das Ziel ist es, Sie mit dem Wissen auszustatten, Ihre „Blackbox“-Agenten in transparente, handhabbare und verlässliche Systeme zu verwandeln.

_**Hinweis:** Es ist wichtig, KI-Agenten einzusetzen, die sicher und vertrauenswürdig sind. Sehen Sie sich auch die Lektion [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md) an._

## Traces und Spans

Beobachtbarkeitstools wie [Langfuse](https://langfuse.com/) oder [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) stellen Agentenläufe üblicherweise als Traces und Spans dar.

- **Trace** repräsentiert eine vollständige Agentenaufgabe von Anfang bis Ende (z. B. die Bearbeitung einer Benutzeranfrage).
- **Spans** sind einzelne Schritte innerhalb des Traces (z. B. ein Aufruf eines Sprachmodells oder das Abrufen von Daten).

![Trace-Baum in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Ohne Beobachtbarkeit kann sich ein KI-Agent wie eine „Blackbox“ anfühlen – sein interner Zustand und seine Schlussfolgerungen sind undurchsichtig, was es schwierig macht, Probleme zu diagnostizieren oder die Leistung zu optimieren. Mit Beobachtbarkeit werden Agenten zu „Glasboxen“, die Transparenz bieten, die entscheidend ist, um Vertrauen aufzubauen und sicherzustellen, dass sie wie beabsichtigt funktionieren.

## Warum Beobachtbarkeit in Produktionsumgebungen wichtig ist

Die Überführung von KI-Agenten in Produktionsumgebungen bringt eine neue Reihe von Herausforderungen und Anforderungen mit sich. Beobachtbarkeit ist nicht länger ein „Nice-to-have“, sondern eine kritische Fähigkeit:

*   **Debugging und Root-Cause-Analyse**: Wenn ein Agent fehlschlägt oder unerwartete Ausgaben liefert, liefern Beobachtbarkeitstools die Traces, die benötigt werden, um die Fehlerquelle zu lokalisieren. Das ist besonders wichtig bei komplexen Agenten, die mehrere LLM-Aufrufe, Tool-Interaktionen und bedingte Logik enthalten können.
*   **Latenz- und Kostenmanagement**: KI-Agenten verlassen sich oft auf LLMs und andere externe APIs, die pro Token oder pro Aufruf abgerechnet werden. Beobachtbarkeit ermöglicht eine präzise Verfolgung dieser Aufrufe und hilft dabei, Operationen zu identifizieren, die übermäßig langsam oder teuer sind. Dadurch können Teams Prompts optimieren, effizientere Modelle wählen oder Workflows neu gestalten, um Betriebskosten zu senken und eine gute Benutzererfahrung sicherzustellen.
*   **Vertrauen, Sicherheit und Compliance**: In vielen Anwendungen ist es wichtig sicherzustellen, dass Agenten sich sicher und ethisch verhalten. Beobachtbarkeit liefert eine Prüfspur der Aktionen und Entscheidungen des Agenten. Diese kann verwendet werden, um Probleme wie Prompt-Injection, die Erzeugung schädlicher Inhalte oder den unsachgemäßen Umgang mit personenbezogenen Daten (PII) zu erkennen und zu mindern. Beispielsweise kann man Traces überprüfen, um zu verstehen, warum ein Agent eine bestimmte Antwort gegeben oder ein bestimmtes Tool verwendet hat.
*   **Kontinuierliche Verbesserungszyklen**: Beobachtbarkeitsdaten bilden die Grundlage eines iterativen Entwicklungsprozesses. Durch die Überwachung der Agentenleistung in der realen Welt können Teams Bereiche für Verbesserungen identifizieren, Daten für das Fine-Tuning sammeln und die Auswirkungen von Änderungen validieren. Dies schafft einen Feedback-Loop, bei dem Erkenntnisse aus der Online-Evaluation die Offline-Experimente und Verfeinerungen informieren, was zu einer schrittweisen Verbesserung der Agentenleistung führt.

## Wichtige Metriken zur Überwachung

Um das Verhalten von Agenten zu überwachen und zu verstehen, sollten eine Reihe von Metriken und Signalen verfolgt werden. Die spezifischen Metriken können je nach Zweck des Agenten variieren, einige sind jedoch universell wichtig.

Hier sind einige der am häufigsten von Beobachtbarkeitstools überwachten Metriken:

**Latenz:** Wie schnell reagiert der Agent? Lange Wartezeiten beeinträchtigen die Benutzererfahrung. Sie sollten die Latenz für Aufgaben und einzelne Schritte messen, indem Sie Agentenläufe nachverfolgen. Beispielsweise könnte ein Agent, der für alle Modellaufrufe 20 Sekunden benötigt, durch die Verwendung eines schnelleren Modells oder durch paralleles Ausführen von Modellaufrufen beschleunigt werden.

**Kosten:** Welche Kosten fallen pro Agentenlauf an? KI-Agenten verlassen sich auf LLM-Aufrufe, die pro Token oder externe APIs abgerechnet werden. Häufige Tool-Nutzung oder mehrere Prompts können die Kosten schnell in die Höhe treiben. Wenn ein Agent beispielsweise ein LLM fünfmal aufruft, um eine marginale Qualitätsverbesserung zu erzielen, müssen Sie beurteilen, ob die Kosten gerechtfertigt sind oder ob Sie die Anzahl der Aufrufe reduzieren oder ein günstigeres Modell verwenden können. Echtzeitüberwachung kann auch helfen, unerwartete Spitzen zu identifizieren (z. B. Bugs, die zu übermäßigen API-Schleifen führen).

**Request-Fehler:** Wie viele Anfragen sind fehlgeschlagen? Das kann API-Fehler oder fehlgeschlagene Tool-Aufrufe umfassen. Um Ihren Agenten in der Produktion robuster gegen solche Fehler zu machen, können Sie Fallbacks oder Retries einrichten. Z. B. wenn LLM-Anbieter A ausfällt, wechseln Sie als Backup zu LLM-Anbieter B.

**Benutzerfeedback:** Die Implementierung direkter Benutzerevaluationen liefert wertvolle Einblicke. Dies kann explizite Bewertungen (👍Daumen hoch/👎Daumen runter, ⭐1-5 Sterne) oder textuelle Kommentare umfassen. Konsistent negatives Feedback sollte Sie alarmieren, da dies ein Zeichen dafür ist, dass der Agent nicht wie erwartet funktioniert.

**Implizites Benutzerfeedback:** Benutzerverhalten liefert auch ohne explizite Bewertungen indirektes Feedback. Dazu gehören sofortige Umformulierungen von Fragen, wiederholte Anfragen oder das Klicken auf eine Wiederholen-Schaltfläche. Z. B. wenn Sie feststellen, dass Benutzer dieselbe Frage wiederholt stellen, ist das ein Zeichen dafür, dass der Agent nicht wie erwartet funktioniert.

**Genauigkeit:** Wie häufig liefert der Agent korrekte oder gewünschte Ausgaben? Die Definition von Genauigkeit variiert (z. B. Korrektheit bei Problemlösungen, Genauigkeit der Informationsbeschaffung, Benutzerzufriedenheit). Der erste Schritt ist zu definieren, wie Erfolg für Ihren Agenten aussieht. Sie können die Genauigkeit über automatisierte Prüfungen, Evaluationsscores oder Task-Abschluss-Auszeichnungen verfolgen. Beispielsweise durch Markieren von Traces als „succeeded“ oder „failed“.

**Automatisierte Evaluationsmetriken:** Sie können auch automatisierte Evals einrichten. Beispielsweise können Sie ein LLM verwenden, um die Ausgabe des Agenten zu bewerten, z. B. ob sie hilfreich, korrekt oder nicht ist. Es gibt auch mehrere Open-Source-Bibliotheken, die Ihnen helfen, verschiedene Aspekte des Agenten zu bewerten. Z. B. [RAGAS](https://docs.ragas.io/) für RAG-Agenten oder [LLM Guard](https://llm-guard.com/), um schädliche Sprache oder Prompt-Injection zu erkennen.

In der Praxis bietet eine Kombination dieser Metriken die beste Abdeckung für den Zustand eines KI-Agenten. In diesem Kapitel zeigen wir Ihnen im [Beispiel-Notebook](./code_samples/10_autogen_evaluation.ipynb), wie diese Metriken in realen Beispielen aussehen, aber zuerst lernen wir, wie ein typischer Evaluationsworkflow aussieht.

## Instrumentieren Sie Ihren Agenten

Um Tracing-Daten zu sammeln, müssen Sie Ihren Code instrumentieren. Ziel ist es, den Agenten-Code so zu instrumentieren, dass Traces und Metriken erzeugt werden, die von einer Beobachtbarkeitsplattform erfasst, verarbeitet und visualisiert werden können.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) hat sich als Industriestandard für LLM-Beobachtbarkeit etabliert. Es bietet ein Set von APIs, SDKs und Tools zur Erzeugung, Sammlung und zum Export von Telemetriedaten.

Es gibt viele Instrumentierungsbibliotheken, die vorhandene Agenten-Frameworks umhüllen und das einfache Exportieren von OpenTelemetry-Spans an ein Beobachtbarkeits-Tool ermöglichen. Nachfolgend ein Beispiel zur Instrumentierung eines AutoGen-Agenten mit der [OpenLit-Instrumentierungsbibliothek](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

Das [Beispiel-Notebook](./code_samples/10_autogen_evaluation.ipynb) in diesem Kapitel demonstriert, wie Sie Ihren AutoGen-Agenten instrumentieren.

**Manuelle Span-Erstellung:** Während Instrumentierungsbibliotheken eine gute Basis liefern, gibt es oft Fälle, in denen detailliertere oder benutzerdefinierte Informationen benötigt werden. Sie können Spans manuell erstellen, um benutzerdefinierte Anwendungslogik hinzuzufügen. Wichtiger noch: Sie können automatisch oder manuell erstellte Spans mit benutzerdefinierten Attributen (auch als Tags oder Metadaten bekannt) anreichern. Diese Attribute können geschäftsspezifische Daten, Zwischenberechnungen oder jeden Kontext enthalten, der für Debugging oder Analyse nützlich sein könnte, wie z. B. `user_id`, `session_id` oder `model_version`.

Beispiel zur manuellen Erstellung von Traces und Spans mit dem [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agenten-Evaluation

Beobachtbarkeit liefert uns Metriken, aber Evaluation ist der Prozess der Analyse dieser Daten (und der Durchführung von Tests), um zu bestimmen, wie gut ein KI-Agent arbeitet und wie er verbessert werden kann. Anders gesagt: Sobald Sie diese Traces und Metriken haben, wie nutzen Sie sie, um den Agenten zu bewerten und Entscheidungen zu treffen?

Regelmäßige Evaluation ist wichtig, da KI-Agenten oft nicht-deterministisch sind und sich entwickeln können (durch Updates oder driftendes Modellverhalten) – ohne Evaluation würden Sie nicht wissen, ob Ihr „smarter Agent“ tatsächlich seine Aufgabe gut erfüllt oder ob er sich verschlechtert hat.

Es gibt zwei Kategorien von Evaluationen für KI-Agenten: **Online-Evaluation** und **Offline-Evaluation**. Beide sind wertvoll und ergänzen sich gegenseitig. Üblicherweise beginnen wir mit der Offline-Evaluation, da dies der Mindestschritt ist, bevor ein Agent bereitgestellt wird.

### Offline-Evaluation

![Datensatzeinträge in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dies beinhaltet die Evaluierung des Agenten in einer kontrollierten Umgebung, typischerweise unter Verwendung von Testdatensätzen und nicht mit Live-Benutzeranfragen. Sie verwenden kuratierte Datensätze, bei denen Sie wissen, welche Ausgabe oder welches Verhalten erwartet wird, und führen dann Ihren Agenten darauf aus.

Wenn Sie z. B. einen Agenten für Mathematiktextaufgaben gebaut haben, könnten Sie einen [Testdatensatz](https://huggingface.co/datasets/gsm8k) mit 100 Aufgaben und bekannten Lösungen haben. Offline-Evaluation wird oft während der Entwicklung durchgeführt (und kann Teil von CI/CD-Pipelines sein), um Verbesserungen zu überprüfen oder Regressionen vorzubeugen. Der Vorteil ist, dass sie **wiederholbar ist und Sie klare Genauigkeitsmetriken erhalten, da Sie die Ground-Truth haben**. Sie könnten auch Benutzeranfragen simulieren und die Antworten des Agenten mit idealen Antworten abgleichen oder automatisierte Metriken wie oben beschrieben verwenden.

Die zentrale Herausforderung bei der Offline-Eval besteht darin, sicherzustellen, dass Ihr Testdatensatz umfassend bleibt und relevant ist – der Agent könnte auf einem festen Testset gut abschneiden, aber in der Produktion sehr unterschiedliche Anfragen erhalten. Daher sollten Sie Testsets mit neuen Randfällen und Beispielen aktualisiert halten, die reale Szenarien widerspiegeln. Eine Mischung aus kleinen „Smoke-Test“-Fällen und größeren Evaluationssets ist nützlich: Kleine Sets für schnelle Checks und größere für breitere Leistungsmetriken.

### Online-Evaluation

![Übersicht Beobachtbarkeitsmetriken](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dies bezieht sich auf die Evaluierung des Agenten in einer Live-, realen Umgebung, d. h. während der tatsächlichen Nutzung in der Produktion. Online-Evaluation umfasst die Überwachung der Agentenleistung bei echten Benutzerinteraktionen und die kontinuierliche Analyse der Ergebnisse.

Beispielsweise könnten Sie Erfolgsraten, Benutzerzufriedenheitswerte oder andere Metriken im Live-Traffic verfolgen. Der Vorteil der Online-Evaluation ist, dass sie **Dinge erfasst, die Sie in einer Laborumgebung möglicherweise nicht vorhersehen** – Sie können Modell-Drift im Laufe der Zeit beobachten (wenn die Wirksamkeit des Agenten nachlässt, weil sich Eingabeprofile ändern) und unerwartete Anfragen oder Situationen auffangen, die nicht in Ihren Testdaten enthalten waren. Sie liefert ein echtes Bild davon, wie sich der Agent in freier Wildbahn verhält.

Online-Evaluation umfasst oft das Sammeln impliziten und expliziten Benutzerfeedbacks, wie bereits besprochen, und eventuell das Durchführen von Shadow-Tests oder A/B-Tests (bei denen eine neue Version des Agenten parallel läuft, um sie mit der alten zu vergleichen). Die Herausforderung besteht darin, dass es schwierig sein kann, zuverlässige Labels oder Scores für Live-Interaktionen zu erhalten – Sie müssen sich möglicherweise auf Benutzerfeedback oder Downstream-Metriken stützen (z. B. hat der Benutzer das Ergebnis angeklickt?).

### Kombination der beiden

Online- und Offline-Evaluationen schließen einander nicht aus; sie ergänzen sich stark. Erkenntnisse aus dem Online-Monitoring (z. B. neue Arten von Benutzeranfragen, bei denen der Agent schlecht abschneidet) können zur Erweiterung und Verbesserung der Offline-Testdatensätze verwendet werden. Umgekehrt können Agenten, die in Offline-Tests gut abschneiden, mit höherer Zuversicht in Produktion bereitgestellt und online überwacht werden.

Tatsächlich übernehmen viele Teams eine Schleife:

_evaluieren offline -> bereitstellen -> online überwachen -> neue Fehlfälle sammeln -> zum Offline-Datensatz hinzufügen -> Agent verfeinern -> wiederholen_.

## Häufige Probleme

Beim Einsatz von KI-Agenten in der Produktion können verschiedene Herausforderungen auftreten. Hier sind einige häufige Probleme und mögliche Lösungen:

| **Problem**    | **Mögliche Lösung**   |
| ------------- | ------------------ |
| KI-Agent erfüllt Aufgaben nicht konsistent | - Verfeinern Sie den Prompt für den KI-Agenten; seien Sie klar in den Zielen.<br>- Identifizieren Sie, wo das Aufteilen der Aufgaben in Unteraufgaben und deren Bearbeitung durch mehrere Agenten helfen kann. |
| KI-Agent gerät in Endlosschleifen  | - Stellen Sie sicher, dass Sie klare Abbruchbedingungen haben, damit der Agent weiß, wann der Prozess zu stoppen ist.<br>- Für komplexe Aufgaben, die Schlussfolgern und Planung erfordern, verwenden Sie ein größeres Modell, das auf reasoning-Aufgaben spezialisiert ist. |
| Tool-Aufrufe des KI-Agenten performen nicht gut   | - Testen und validieren Sie die Ausgabe des Tools außerhalb des Agentensystems.<br>- Verfeinern Sie die definierten Parameter, Prompts und die Benennung der Tools.  |
| Multi-Agenten-System verhält sich inkonsistent | - Verfeinern Sie die Prompts für jeden Agenten, damit sie spezifisch und unterscheidbar sind.<br>- Bauen Sie ein hierarchisches System mit einem „Routing“- oder Controller-Agenten auf, der bestimmt, welcher Agent der richtige ist. |

Viele dieser Probleme lassen sich mit Beobachtbarkeit effektiver identifizieren. Die zuvor besprochenen Traces und Metriken helfen dabei, genau den Punkt im Agenten-Workflow zu lokalisieren, an dem Probleme auftreten, was Debugging und Optimierung deutlich effizienter macht.

## Kostenmanagement
Hier sind einige Strategien, um die Kosten für die Bereitstellung von KI-Agenten in der Produktion zu verwalten:

**Verwendung kleinerer Modelle:** Small Language Models (SLMs) können in bestimmten agentischen Anwendungsfällen gute Leistungen erbringen und die Kosten deutlich senken. Wie bereits erwähnt, ist der Aufbau eines Evaluierungssystems zur Bestimmung und zum Vergleich der Leistung im Vergleich zu größeren Modellen der beste Weg, um zu verstehen, wie gut ein SLM in Ihrem Anwendungsfall abschneiden wird. Ziehen Sie in Betracht, SLMs für einfachere Aufgaben wie Intent-Klassifikation oder Parameterextraktion zu verwenden und größere Modelle für komplexes Schlussfolgern vorzubehalten.

**Verwendung eines Router-Modells:** Eine ähnliche Strategie besteht darin, eine Vielfalt von Modellen und Größen zu verwenden. Sie können ein LLM/SLM oder eine serverlose Funktion nutzen, um Anfragen je nach Komplexität an die am besten geeigneten Modelle zu leiten. Dies hilft ebenfalls, die Kosten zu senken und gleichzeitig die Leistung bei den passenden Aufgaben sicherzustellen. Beispielsweise leiten Sie einfache Abfragen an kleinere, schnellere Modelle weiter und verwenden teure große Modelle nur für komplexe Schlussfolgerungsaufgaben.

**Zwischenspeichern von Antworten:** Das Identifizieren häufiger Anfragen und Aufgaben und das Bereitstellen der Antworten, bevor sie durch Ihr agentisches System laufen, ist ein guter Weg, um das Volumen ähnlicher Anfragen zu reduzieren. Sie können sogar einen Ablauf implementieren, um zu erkennen, wie ähnlich eine Anfrage Ihren zwischengespeicherten Anfragen mithilfe einfacherer KI-Modelle ist. Diese Strategie kann die Kosten für häufig gestellte Fragen oder gängige Workflows erheblich reduzieren.

## Schauen wir uns an, wie das in der Praxis funktioniert

In the [example notebook of this section](./code_samples/10_autogen_evaluation.ipynb), wir werden Beispiele dafür sehen, wie wir Observability-Tools nutzen können, um unseren Agenten zu überwachen und zu bewerten.

### Haben Sie weitere Fragen zu KI-Agenten in der Produktion?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Vorherige Lektion

[Metakognition-Designmuster](../09-metacognition/README.md)

## Nächste Lektion

[Agentische Protokolle](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Haftungsausschluss:
Dieses Dokument wurde mit dem KI‑Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Die ursprüngliche Fassung des Dokuments in der Ausgangssprache ist als maßgebliche Quelle zu betrachten. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Verwendung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->