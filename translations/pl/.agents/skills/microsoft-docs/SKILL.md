---
name: microsoft-docs
---
# Microsoft Docs

Umiejętność wyszukiwania w ekosystemie technologii Microsoft. Obejmuje learn.microsoft.com oraz dokumentację znajdującą się poza nim (VS Code, GitHub, Aspire, repozytoria Agent Framework).

---

## Domyślnie: Microsoft Learn MCP

Używaj tych narzędzi do **wszystkiego na learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows i więcej. To podstawowe narzędzie do zdecydowanej większości zapytań o dokumentację Microsoft.

| Narzędzie | Cel |
|------|---------|
| `microsoft_docs_search` | Przeszukaj learn.microsoft.com — koncepcje, przewodniki, samouczki, konfigurację |
| `microsoft_code_sample_search` | Znajdź działające fragmenty kodu z dokumentacji Learn. Przekaż `language` (`python`, `csharp` itd.) dla najlepszych wyników |
| `microsoft_docs_fetch` | Pobierz pełną zawartość strony z określonego URL (gdy fragmenty z wyszukiwania są niewystarczające) |

Używaj `microsoft_docs_fetch` po wyszukiwaniu, gdy potrzebujesz kompletnych samouczków, wszystkich opcji konfiguracji lub gdy fragmenty w wynikach są obcięte.

---

## Wyjątki: kiedy używać innych narzędzi

Następujące kategorie znajdują się **poza** learn.microsoft.com. Użyj wtedy wskazanego narzędzia.

### Aspire — używaj Aspire MCP Server (preferowane) lub Context7

Dokumentacja Aspire znajduje się na **aspire.dev**, a nie na Learn. Najlepsze narzędzie zależy od wersji Aspire CLI:

**CLI 13.2+** (zalecane) — Serwer Aspire MCP zawiera wbudowane narzędzia do wyszukiwania w dokumentacji:

| Narzędzie MCP | Opis |
|----------|-------------|
| `list_docs` | Wyświetla listę wszystkich dostępnych dokumentów z aspire.dev |
| `search_docs` | Ważone wyszukiwanie leksykalne w zawartości aspire.dev |
| `get_doc` | Pobiera konkretny dokument po slug |

Te narzędzia są dostępne w Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Aby zaktualizować: `aspire update --self --channel daily`.

**CLI 13.1** — Serwer MCP umożliwia przegląd integracji (`list_integrations`, `get_integration_docs`) ale **nie** wyszukiwanie dokumentów. Wróć wtedy do Context7:

| ID biblioteki | Do użycia do |
|---|---|
| `/microsoft/aspire.dev` | Podstawowe — przewodniki, integracje, referencja CLI, wdrożenia |
| `/microsoft/aspire` | Źródło runtime — szczegóły API, implementacja |
| `/communitytoolkit/aspire` | Integracje społeczności — Go, Java, Node.js, Ollama |

### VS Code — użyj Context7

Dokumentacja VS Code znajduje się na **code.visualstudio.com**, a nie na Learn.

| ID biblioteki | Do użycia do |
|---|---|
| `/websites/code_visualstudio` | Dokumentacja użytkownika — ustawienia, funkcje, debugowanie, zdalny rozwój |
| `/websites/code_visualstudio_api` | API rozszerzeń — webview, TreeView, komendy, punkty rozszerzeń |

### GitHub — użyj Context7

Dokumentacja GitHub znajduje się na **docs.github.com** i **cli.github.com**.

| ID biblioteki | Do użycia do |
|---|---|
| `/websites/github_en` | Actions, API, repozytoria, bezpieczeństwo, admin, Copilot |
| `/websites/cli_github` | Komendy i flagi GitHub CLI (`gh`) |

### Agent Framework — użyj Learn MCP + Context7

Samouczki Agent Framework są na learn.microsoft.com (użyj `microsoft_docs_search`), ale **repozytorium GitHub** zawiera szczegóły na poziomie API, często wyprzedzające opublikowaną dokumentację — szczególnie referencje DevUI REST API, opcje CLI oraz integrację .NET.

| ID biblioteki | Do użycia do |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Samouczki — przewodniki DevUI, śledzenie, orkiestracja przepływów pracy |
| `/microsoft/agent-framework` | Szczegóły API — endpointy DevUI REST, flagi CLI, uwierzytelnianie, .NET `AddDevUI`/`MapDevUI` |

**Wskazówka DevUI:** Najpierw zapytaj źródło Learn o przewodniki "how-to", następnie repozytorium o szczegóły API (schematy endpointów, konfiguracja proxy, tokeny uwierzytelniania).

---

## Konfiguracja Context7

Dla dowolnego zapytania w Context7 najpierw ustal ID biblioteki (jednorazowo na sesję):

1. Wywołaj `mcp_context7_resolve-library-id` z nazwą technologii
2. Wywołaj `mcp_context7_query-docs` z otrzymanym ID biblioteki i konkretnym zapytaniem

---

## Pisanie skutecznych zapytań

Bądź precyzyjny — uwzględnij wersję, zamiar i język:

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

Uwzględnij kontekst:
- **Wersja** jeśli istotna (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Zamiar zadania** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Język** dla dokumentacji poliglotycznej (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->