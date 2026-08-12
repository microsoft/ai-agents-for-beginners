# Agent Smoke Tests

Dieser Ordner enthält **Smoke-Test-Kataloge** für die Agenten, die Sie im Kurs entwickeln.
Ein Smoke-Test ist eine kostengünstige, schnelle Überprüfung, dass ein **bereitgestellter Microsoft Foundry gehosteter
Agent** erreichbar ist, reagiert und seinen grundlegendsten Aufforderungserwartungen folgt. Es ist das erste Tor — kein Ersatz für die vollständige Bewertungs-
pipeline, die Sie in [Lesson 10](../10-ai-agents-production/README.md) und
[Lesson 16](../16-deploying-scalable-agents/README.md) erlernen.


Die Kataloge werden von der [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action über den Workflow [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
verwendet.

## Wie man ausführt

1. **Stellen Sie den Agenten der Lektion** als gehosteten Agenten bei Microsoft Foundry bereit (siehe
   Lektion 16 für den Bereitstellungs-Workflow). Beachten Sie den **Agentennamen** und Ihren
   **Foundry Projekt-Endpunkt**.
2. Fügen Sie diese Repository-Secrets hinzu (Einstellungen → Secrets und Variablen → Aktionen):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Die föderierte
   Identität benötigt die Rolle **Azure AI User** im **Foundry-Projektbereich**.
3. Führen Sie unter dem Tab **Actions** die Aktion **Smoke-test hosted agents** aus und wählen Sie die
   `tests_file` der Lektion aus, geben Sie dann den passenden `agent_name` und
   `project_endpoint` an.

## Katalog → Lektion → Agentenname

| Katalog | Lektion | Agent bereitstellen als |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Einführung in KI-Agenten](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Werkzeugnutzung](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Bereitstellung skalierbarer Agenten](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Welche Lektionen haben Smoke-Tests?

Smoke-Tests gelten für Lektionen, in denen Sie einen **Agenten bereitstellen**, dessen Textantworten
gegen bekannten Inhalt geprüft werden können. Lektionen, die konzeptionell sind, nur lokal ausgeführt werden
oder nicht-deterministische kreative Ausgaben erzeugen, sind absichtlich ausgeschlossen:

- **Lektion 17 (Erstellung lokaler KI-Agenten)** läuft vollständig auf Ihrem Rechner mit
  Foundry Local und stellt **keinen** Foundry Responses-Endpunkt zur Verfügung, daher ist diese
  Aktion nicht anwendbar. Validieren Sie sie, indem Sie das Notebook lokal ausführen.
- Design-Patterns und Theorie-Lektionen (02, 03, 06, 07, 09, 12) liefern keinen einzigen
  bereitstellbaren Agenten für Smoke-Tests.

## Katalogschema (kurze Referenz)

Jeder Katalog ist ein JSON-Dokument mit einem obersten `tests`-Array. Jeder Eintrag sendet per POST
eine Eingabeaufforderung und prüft die Antwort:

| Feld | Bedeutung |
|-------|---------|
| `id` | Eindeutige Schritt-ID, die im Protokoll angezeigt wird. |
| `description` | Für Menschen lesbarer Zweck. |
| `prompt` | Die an den Agenten gesendete Nachricht. |
| `assertions.status` | Erwarteter HTTP-Status (Standard 200). |
| `assertions.contains_any` | Besteht, wenn die Antwort eines dieser Teilstrings enthält. |
| `assertions.contains_all` | Besteht, wenn die Antwort jeden Teilstring enthält. |
| `assertions.contains_none` | Besteht, wenn die Antwort keinen dieser Teilstrings enthält. |
| `save_response_id_as` | Speichert die Antwort-ID für einen späteren Mehrschritt. |
| `use_previous_response_id` | Sendet diese Eingabe verkettet an eine gespeicherte Antwort-ID. |

Assertions sind groß-/kleinschreibungsunabhängige Teilstring-Prüfungen. Siehe die
[Action-Dokumentation](https://github.com/marketplace/actions/ai-smoke-test) für
das vollständige Schema, einschließlich Foundry verwalteter Konversationsressourcen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->