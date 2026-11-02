---
name: microsoft-docs
description: Durchsuchen Sie die offizielle Microsoft-Dokumentation, um Konzepte,
  Tutorials und Codebeispiele zu Azure, .NET, Agent Framework, Aspire, VS Code, GitHub
  und mehr zu finden. Verwendet Microsoft Learn MCP als Standard, mit Context7 und
  Aspire MCP für Inhalte, die außerhalb von learn.microsoft.com liegen.
---
# Microsoft Docs

Forschungskompetenz für das Microsoft-Technologie-Ökosystem. Bezieht sich auf learn.microsoft.com und Dokumentationen, die außerhalb davon existieren (VS Code, GitHub, Aspire, Agent Framework Repositories).

---

## Standard: Microsoft Learn MCP

Verwenden Sie diese Tools für **alles auf learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows und mehr. Dies ist das primäre Tool für die überwiegende Mehrheit der Microsoft-Dokumentationsanfragen.

| Tool | Zweck |
|------|---------|
| `microsoft_docs_search` | Suche auf learn.microsoft.com — Konzepte, Leitfäden, Tutorials, Konfiguration |
| `microsoft_code_sample_search` | Finden funktionierender Codebeispiele aus den Learn-Dokumentationen. Beste Ergebnisse mit Übergabe von `language` (`python`, `csharp` usw.) |
| `microsoft_docs_fetch` | Vollständiger Seiteninhalt von einer bestimmten URL (wenn Auszüge aus der Suche nicht ausreichen) |

Verwenden Sie `microsoft_docs_fetch` nach der Suche, wenn Sie komplette Tutorials, alle Konfigurationsoptionen benötigen oder wenn Suchauszüge abgeschnitten sind.

---

## Ausnahmen: Wann man andere Tools benutzt

Die folgenden Kategorien leben **außerhalb** von learn.microsoft.com. Verwenden Sie stattdessen das angegebene Tool.

### Aspire — Verwenden Sie Aspire MCP Server (bevorzugt) oder Context7

Aspire-Dokumentationen sind auf **aspire.dev**, nicht auf Learn. Das beste Tool hängt von Ihrer Aspire CLI-Version ab:

**CLI 13.2+** (empfohlen) — Der Aspire MCP-Server enthält integrierte Suchwerkzeuge für Dokumentationen:

| MCP Tool | Beschreibung |
|----------|-------------|
| `list_docs` | Listet alle verfügbaren Dokumentationen von aspire.dev auf |
| `search_docs` | Gewichtete lexikalische Suche über aspire.dev Inhalte |
| `get_doc` | Ruft ein spezielles Dokument per Slug ab |

Diese sind in Aspire CLI 13.2 enthalten ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Zum Aktualisieren: `aspire update --self --channel daily`.

**CLI 13.1** — Der MCP-Server bietet Integrationssuche (`list_integrations`, `get_integration_docs`) aber **keine** Dokumentensuche. Fallback auf Context7:

| Bibliotheks-ID | Verwendung für |
|---|---|
| `/microsoft/aspire.dev` | Primär — Leitfäden, Integrationen, CLI-Referenz, Bereitstellung |
| `/microsoft/aspire` | Laufzeitquelle — API-Interna, Implementierungsdetails |
| `/communitytoolkit/aspire` | Community-Integrationen — Go, Java, Node.js, Ollama |

### VS Code — Verwenden Sie Context7

VS Code-Dokumentationen sind auf **code.visualstudio.com**, nicht auf Learn.

| Bibliotheks-ID | Verwendung für |
|---|---|
| `/websites/code_visualstudio` | Benutzerdokumentation — Einstellungen, Funktionen, Debugging, Remote-Entwicklung |
| `/websites/code_visualstudio_api` | Erweiterungs-API — Webviews, TreeViews, Befehle, Beitragspunkte |

### GitHub — Verwenden Sie Context7

GitHub-Dokumentationen sind auf **docs.github.com** und **cli.github.com**.

| Bibliotheks-ID | Verwendung für |
|---|---|
| `/websites/github_en` | Actions, API, Repositories, Sicherheit, Admin, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) Befehle und Flags |

### Agent Framework — Verwenden Sie Learn MCP + Context7

Agent Framework Tutorials sind auf learn.microsoft.com (verwenden Sie `microsoft_docs_search`), aber das **GitHub-Repository** enthält API-Details, die oft weiter sind als die veröffentlichten Dokumente — besonders DevUI REST API-Referenz, CLI-Optionen und .NET-Integration.

| Bibliotheks-ID | Verwendung für |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorials — DevUI-Leitfäden, Tracing, Workflow-Orchestrierung |
| `/microsoft/agent-framework` | API-Details — DevUI REST-Endpunkte, CLI-Flags, Authentifizierung, .NET `AddDevUI`/`MapDevUI` |

**DevUI-Tipp:** Befragen Sie zuerst die Learn-Webseitenquelle für How-to-Leitfäden und dann die Repository-Quelle für API-spezifische Details (Endpoint-Schemas, Proxy-Konfiguration, Authentifizierungstoken).

---

## Context7 Einrichtung

Für jede Context7-Abfrage ermitteln Sie zuerst die Bibliotheks-ID (einmal pro Sitzung):

1. Rufen Sie `mcp_context7_resolve-library-id` mit dem Technologietnamen auf
2. Rufen Sie `mcp_context7_query-docs` mit der zurückgegebenen Bibliotheks-ID und einer spezifischen Abfrage auf

---

## Effektive Abfragen schreiben

Seien Sie spezifisch — geben Sie Version, Absicht und Sprache an:

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

Kontext einbeziehen:
- **Version** wenn relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Aufgabenabsicht** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Sprache** für polyglootte Dokumentationen (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->