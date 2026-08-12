---
name: microsoft-docs
description: Abfrage der offiziellen Microsoft-Dokumentation, um Konzepte, Tutorials
  und Codebeispiele zu Azure, .NET, Agent Framework, Aspire, VS Code, GitHub und mehr
  zu finden. Verwendet Microsoft Learn MCP als Standard, mit Context7 und Aspire MCP
  für Inhalte, die außerhalb von learn.microsoft.com liegen.
---
# Microsoft Docs

Recherche-Fähigkeit für das Microsoft-Technologie-Ökosystem. Behandelt learn.microsoft.com und Dokumentation, die außerhalb davon liegt (VS Code, GitHub, Aspire, Agent Framework Repositories).

---

## Standard: Microsoft Learn MCP

Verwende diese Tools für **alles auf learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows und mehr. Dies ist das primäre Werkzeug für die überwältigende Mehrheit der Anfragen zur Microsoft-Dokumentation.

| Tool | Zweck |
|------|-------|
| `microsoft_docs_search` | Durchsuche learn.microsoft.com — Konzepte, Leitfäden, Tutorials, Konfiguration |
| `microsoft_code_sample_search` | Finde funktionierende Codeausschnitte aus Learn-Dokumenten. Übergebe `language` (`python`, `csharp`, etc.) für beste Ergebnisse |
| `microsoft_docs_fetch` | Hole den vollständigen Seiteninhalt von einer bestimmten URL (wenn Suchauszüge nicht ausreichen) |

Verwende `microsoft_docs_fetch` nach der Suche, wenn du komplette Tutorials, alle Konfigurationsoptionen benötigst oder wenn Suchauszüge abgeschnitten sind.

---

## Ausnahmen: Wann andere Tools verwenden

Die folgenden Kategorien befinden sich **außerhalb** von learn.microsoft.com. Verwende stattdessen das angegebene Tool.

### .NET Aspire — Verwende Aspire MCP Server (bevorzugt) oder Context7

Die Aspire-Dokumentation befindet sich auf **aspire.dev**, nicht auf Learn. Das beste Tool hängt von deiner Aspire-CLI-Version ab:

**CLI 13.2+** (empfohlen) — Der Aspire MCP-Server enthält integrierte Tools zur Dokumentensuche:

| MCP-Tool | Beschreibung |
|----------|--------------|
| `list_docs` | Listet alle verfügbaren Dokumente von aspire.dev auf |
| `search_docs` | Gewichtete lexikalische Suche über Inhalte von aspire.dev |
| `get_doc` | Ruft ein bestimmtes Dokument anhand des Slugs ab |

Diese sind in Aspire CLI 13.2 enthalten ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Zum Aktualisieren: `aspire update --self --channel daily`. Siehe: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — Der MCP-Server bietet Integrationssuche (`list_integrations`, `get_integration_docs`), aber **keine** Dokumentensuche. Fallback zu Context7:

| Library ID | Verwendung |
|---|---|
| `/microsoft/aspire.dev` | Primär — Leitfäden, Integrationen, CLI-Referenz, Bereitstellung |
| `/dotnet/aspire` | Laufzeit-Quellcode — API-Interna, Implementierungsdetails |
| `/communitytoolkit/aspire` | Community-Integrationen — Go, Java, Node.js, Ollama |

### VS Code — Verwende Context7

VS Code-Dokumentation befindet sich auf **code.visualstudio.com**, nicht auf Learn.

| Library ID | Verwendung |
|---|---|
| `/websites/code_visualstudio` | Benutzerdokumentation — Einstellungen, Funktionen, Debugging, Remote-Entwicklung |
| `/websites/code_visualstudio_api` | Erweiterungs-API — Webviews, TreeViews, Befehle, Contribution Points |

### GitHub — Verwende Context7

GitHub-Dokumentation befindet sich auf **docs.github.com** und **cli.github.com**.

| Library ID | Verwendung |
|---|---|
| `/websites/github_en` | Actions, API, Repositories, Sicherheit, Administration, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) Befehle und Flags |

### Agent Framework — Verwende Learn MCP + Context7

Agent Framework-Tutorials befinden sich auf learn.microsoft.com (verwende `microsoft_docs_search`), aber das **GitHub-Repository** enthält API-Detailinformationen, die oft vor den veröffentlichten Dokumenten liegen — insbesondere die DevUI REST-API-Referenz, CLI-Optionen und .NET-Integration.

| Library ID | Verwendung |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorials — DevUI-Anleitungen, Tracing, Workflow-Orchestrierung |
| `/microsoft/agent-framework` | API-Details — DevUI-REST-Endpunkte, CLI-Flags, Auth, .NET `AddDevUI`/`MapDevUI` |

**DevUI-Tipp:** Frage die Learn-Website-Quelle nach How-to-Anleitungen ab, und dann die Repo-Quelle für API-spezifische Details (Endpoint-Schemata, Proxy-Konfiguration, Auth-Tokens).

---

## Context7 Einrichtung

Bei jeder Context7-Anfrage löse zuerst die Library-ID auf (einmal pro Sitzung):

1. Rufe `mcp_context7_resolve-library-id` mit dem Technologienamen auf
2. Rufe `mcp_context7_query-docs` mit der zurückgegebenen Library-ID und einer spezifischen Abfrage auf

---

## Effektive Abfragen formulieren

Sei spezifisch — gib Version, Ziel und Sprache an:

```
# ❌ Too broad
"Azure Functions"
"agent framework"

# ✅ Specific
"Azure Functions Python v2 programming model"
"Cosmos DB partition key design best practices"
"GitHub Actions workflow_dispatch inputs matrix strategy"
"Aspire AddUvicornApp Python FastAPI integration"
"DevUI serve agents tracing OpenTelemetry directory discovery"
"Agent Framework workflow conditional edges branching handoff"
```

Kontext angeben:
- **Version** falls relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Ziel der Aufgabe** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Sprache** für polyglotte Dokumente (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Haftungsausschluss:
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache ist als maßgebliche Quelle zu betrachten. Bei wichtigen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Verwendung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->