---
name: microsoft-docs
description: Przeszukaj oficjalną dokumentację Microsoft, aby znaleźć koncepcje, samouczki
  i przykłady kodu dotyczące Azure, .NET, Agent Framework, Aspire, VS Code, GitHub
  i innych. Domyślnie używa Microsoft Learn MCP, a dla treści znajdujących się poza
  learn.microsoft.com korzysta z Context7 i Aspire MCP.
---
# Microsoft Docs

Umiejętność wyszukiwania informacji dla ekosystemu technologii Microsoft. Obejmuje learn.microsoft.com oraz dokumentację znajdującą się poza nim (repozytoria VS Code, GitHub, Aspire, Agent Framework).

---

## Default: Microsoft Learn MCP

Użyj tych narzędzi dla **wszystkiego na learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows i inne. To jest podstawowe narzędzie dla zdecydowanej większości zapytań dotyczących dokumentacji Microsoft.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Wyszukaj w learn.microsoft.com — koncepcje, przewodniki, samouczki, konfiguracja |
| `microsoft_code_sample_search` | Znajdź działające przykłady kodu w dokumentacji Learn. Przekaż `language` (`python`, `csharp`, etc.) dla najlepszych rezultatów |
| `microsoft_docs_fetch` | Pobierz pełną zawartość strony z określonego URL (gdy fragmenty z wyszukiwania nie wystarczają) |

Użyj `microsoft_docs_fetch` po wyszukiwaniu, gdy potrzebujesz kompletnych samouczków, wszystkich opcji konfiguracji lub gdy fragmenty wyników wyszukiwania są obcięte.

---

## Exceptions: When to Use Other Tools

Następujące kategorie znajdują się **poza** learn.microsoft.com. Użyj zamiast tego wskazanego narzędzia.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Dokumentacja Aspire znajduje się na **aspire.dev**, a nie w Learn. Najlepsze narzędzie zależy od wersji Aspire CLI:

**CLI 13.2+** (zalecane) — Aspire MCP server zawiera wbudowane narzędzia do wyszukiwania w dokumentacji:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Wyświetla wszystkie dostępne dokumenty z aspire.dev |
| `search_docs` | Ważone wyszukiwanie leksykalne w zawartości aspire.dev |
| `get_doc` | Pobiera konkretny dokument po slug |

Są dostarczane w Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Aby zaktualizować: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP server zapewnia przeszukiwanie integracji (`list_integrations`, `get_integration_docs`), ale **nie** wyszukiwanie dokumentacji. Wróć do Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Główne — przewodniki, integracje, dokumentacja CLI, wdrożenie |
| `/dotnet/aspire` | Źródło runtime — szczegóły wewnętrzne API, implementacji |
| `/communitytoolkit/aspire` | Integracje społecznościowe — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

Dokumentacja VS Code znajduje się na **code.visualstudio.com**, a nie w Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Dokumentacja użytkownika — ustawienia, funkcje, debugowanie, zdalny rozwój |
| `/websites/code_visualstudio_api` | API rozszerzeń — webviews, TreeViews, polecenia, punkty rozszerzeń |

### GitHub — Use Context7

Dokumentacja GitHub znajduje się na **docs.github.com** i **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, repozytoria, bezpieczeństwo, administracja, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) — polecenia i flagi |

### Agent Framework — Use Learn MCP + Context7

Samouczki Agent Framework znajdują się na learn.microsoft.com (użyj `microsoft_docs_search`), ale **repozytorium GitHub** zawiera szczegóły na poziomie API, które często są bardziej aktualne niż opublikowane dokumenty — zwłaszcza odniesienie do DevUI REST API, opcje CLI i integracja z .NET.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Samouczki — przewodniki DevUI, śledzenie, orkiestracja przepływów pracy |
| `/microsoft/agent-framework` | Szczegóły API — endpointy DevUI REST, flagi CLI, uwierzytelnianie, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Najpierw sprawdź źródło Learn dla przewodników "jak to zrobić", a następnie źródło repozytorium dla szczegółów na poziomie API (schematy endpointów, konfiguracja proxy, tokeny uwierzytelniania).

---

## Context7 Setup

Dla każdego zapytania do Context7 najpierw rozwiąż identyfikator biblioteki (jednorazowo na sesję):

1. Wywołaj `mcp_context7_resolve-library-id` z nazwą technologii
2. Wywołaj `mcp_context7_query-docs` z otrzymanym identyfikatorem biblioteki i konkretnym zapytaniem

---

## Writing Effective Queries

Bądź konkretny — uwzględnij wersję, zamiar i język:

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

Include context:
- **Wersja** gdy istotne (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Cel zadania** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Język** dla dokumentacji wielojęzycznej (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia opartej na sztucznej inteligencji [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby zapewnić dokładność, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy uznawać za dokument autorytatywny. W przypadku informacji istotnych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->