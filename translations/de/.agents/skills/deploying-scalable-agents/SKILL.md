---
name: deploying-scalable-agents
license: MIT
---
# Bereitstellung skalierbarer Agenten mit Microsoft Foundry

> Begleitfähigkeiten für [Lektion 16 – Bereitstellung skalierbarer Agenten](../../../16-deploying-scalable-agents/README.md).
> Verwenden Sie diese, um einem Lernenden zu helfen, einen Agenten vom Prototypen zur skalierbaren, beobachtbaren
> Produktionsbereitstellung zu bringen. Begründen Sie jede Empfehlung durch die Lektionen und
> das ausführbare Notizbuch; erfinden Sie keine Foundry-APIs.

## Auslöser

Aktivieren Sie diese Fähigkeit, wenn ein Lernender:
- Einen Agenten als **gehosteten Agenten** bei Microsoft Foundry bereitstellen und versionieren/beobachtbar machen möchte.
- Zwischen den Bereitstellungsmustern **client-hosted, hosted-agent und agent-workflow** wählen möchte.
- **Modell-Routing**, **Response Caching** oder **begrenzte Parallelität** hinzufügen will, um Latenz und Kosten zu steuern.
- Ein **Bewertungstor** hinzufügen möchte, damit keine schlechte Agentenversion ausgeliefert wird.
- Einen **Schritt zur menschlichen Genehmigung** für risikoreiche Aktionen einfügen möchte.
- Einen Agenten mit **OpenTelemetry** Trace-Instrumentierung für Produktionsbeobachtbarkeit ausstatten möchte.
- Einen bereitgestellten Agenten als schnellen Post-Deploy-Gate **Smoketesten** möchte.

## Kern-Mentales Modell

Ein Produktionsagent ist meist das operative Gerüst *um* das Modell (~80%),
nicht das Modell selbst. Ordnen Sie jede Empfehlung einer dieser Anliegen zu:

| Anliegen | Prototyp → Produktion |
|---------|------------------------|
| Hosting | Notebook → versionierter gehosteter Dienst |
| Identität | Ihr `az login` → Managed Identity + abgegrenztes RBAC |
| Zustand | Im Speicher → externalisierter Thread-/Speicher-Store |
| Fehler | Traceback → Wiederholungen, Fallbacks, Alarme |
| Kosten | „ein paar Cent“ → verfolgt, geroutet, zwischengespeichert, budgetiert |
| Qualität | Auge messen → automatisiertes Bewertungstor |
| Vertrauen | Ihre Freigabe → Richtlinie + Mensch-in-der-Schleife |

## Bereitstellungsmuster (eins wählen oder kombinieren)

1. **Client-hosted** — die Reasoning-Schleife läuft in Ihrem Prozess. Maximale Kontrolle; Sie besitzen Skalierung/Zustand.
2. **Hosted agent (Foundry Agent Service)** — Foundry hostet die Schleife, speichert Threads, setzt RBAC/Content-Sicherheit durch und zeigt den Agenten im Portal. Weniger Kontrolle, weitaus geringere operative Oberfläche.
3. **Agent Workflow** — mehrere Agenten/Tools, die zu einem Graph mit Verzweigungen, Genehmigungsknoten und dauerhaften Checkpoints zusammengesetzt sind.

## Lebenszyklus (die Schleife, die einen Agenten ausliefert)

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`.
**Offline-Bewertung ist ein Tor, kein Nachgedanke** — eine Version wird nicht ausgeliefert,
wenn sie die Schwelle nicht überschreitet. Online-Beobachtbarkeit speist reale Fehler
zurück in das Offline-Testset.

## Skalierungs- und Kostenhebel (in Prioritätsreihenfolge)

1. **Modell passend dimensionieren** — verwenden Sie das kleinste Modell, das das Bewertungstor besteht.
2. **Routing nach Komplexität** — kleines/schnelles Modell für einfache Anfragen, großes Modell für echtes Reasoning (DIY-Klassifizierer oder Foundry Model Router).
3. **Caching** — bediene fast identische Anfragen ohne Modellaufruf.
4. **Zustandsloses Design + begrenzte Parallelität** — Zustand externalisieren; mit Backoff neu versuchen.

## Schlüsselmuster zum Nachahmen

Verweisen Sie den Lernenden im Notebook auf diese
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Request-Handler**: Cache → Routing nach Komplexität → Trace-Span → Ausführen → Cache.
- **Bewertungstor**: Bewerte ein Offline-Testset; gib `pass_rate >= threshold` zurück und deploye nur, wenn true.
- **Menschliche Genehmigung**: `@tool(approval_mode="always_require")` für Aktionen wie große Rückerstattungen.
- **Tracing**: Kapsle jede Anfrage in `tracer.start_as_current_span(...)` und setze Attribute wie `routed.model`, `customer.id`.

## Smoketesten eines bereitgestellten Agenten

Nach der Bereitstellung überprüfen, ob der Endpunkt tatsächlich antwortet (ein grüner Deploy kann
stumm bleiben). Verwenden Sie die [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
Aktion über [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
mit dem Katalog in [`tests/`](../../../tests/README.md). Der Runner sendet jede
Eingabe an `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
und prüft die Antwort. Die Identität benötigt die **Azure AI User**-Rolle im
Foundry-Projektumfang; das Token-Audience muss `https://ai.azure.com/` sein.

Kombinieren Sie die Tore: **Smoketest** (erreichbar/antwortend, bei jeder Bereitstellung) → **Offline-Bewertung** (gut genug für Auslieferung, vor Promotion) → **Online-Bewertung** (wie es sich in der Praxis schlägt, kontinuierlich).



## Unternehmenssteuerungen

- **RBAC**: Geben Sie jedem gehosteten Agenten eine Managed Identity mit minimalen Rechten.
- **MCP in Produktion**: Behandeln Sie jeden MCP-Server als unvertrauenswürdige Grenze — fixieren Sie die Version, begrenzen Sie die Identität, validieren Sie Ausgaben, limitieren Sie die Rate, geben Sie niemals Geheimnisse preis.

## Schutzmaßnahmen für den Assistenten

- Bevorzugen Sie das kanonische `FoundryChatClient(...)` + `provider.as_agent(...)` Muster, das im gesamten Kurs verwendet wird.
- Versprechen Sie keine Live-Azure-Ergebnisse, die Sie nicht verifiziert haben; empfehlen Sie den Smoketest-Workflow zur Bestätigung einer Bereitstellung.
- Halten Sie Evaluations- und Kostenhinweise zusammen: Evaluation setzt die Qualitätsuntergrenze, Routing/Caching halten die Kosten nahe dieser Untergrenze.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->