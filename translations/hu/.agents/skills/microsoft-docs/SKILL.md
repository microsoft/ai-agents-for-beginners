---
name: microsoft-docs
description: Hivatalos Microsoft-dokumentáció lekérdezése a fogalmak, oktatóanyagok
  és kódpéldák megtalálásához az Azure, .NET, Agent Framework, Aspire, VS Code, GitHub
  és még sok más területén. Alapértelmezettként a Microsoft Learn MCP-t használja,
  a learn.microsoft.com-on kívül található tartalmak esetén pedig a Context7-et és
  az Aspire MCP-t.
---
# Microsoft Docs

Kutatási tudás a Microsoft technológiai ökoszisztémához. Lefedi a learn.microsoft.com oldalt és az azon kívül található dokumentációt (VS Code, GitHub, Aspire, Agent Framework tárolók).

---

## Alapértelmezett: Microsoft Learn MCP

Használd ezeket az eszközöket a **learn.microsoft.com teljes tartalmához** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows és még sok más. Ez az elsődleges eszköz a Microsoft dokumentációs lekérdezések túlnyomó többségéhez.

| Eszköz | Cél |
|------|---------|
| `microsoft_docs_search` | Keresés a learn.microsoft.com-on — fogalmak, útmutatók, oktatóanyagok, konfiguráció |
| `microsoft_code_sample_search` | Találj működő kódrészleteket a Learn dokumentációból. Add át a `language` paramétert (`python`, `csharp`, stb.) a legjobb eredményért |
| `microsoft_docs_fetch` | Teljes oldal tartalmának lekérése egy adott URL-ről (amikor a keresési kivonatok nem elegendőek) |

Használd a `microsoft_docs_fetch` eszközt a keresés után, ha teljes oktatóanyagokra, minden konfigurációs lehetőségre van szükséged, vagy ha a keresési kivonatok le vannak vágva.

---

## Kivételek: Mikor használj más eszközöket

A következő kategóriák a **learn.microsoft.com-on kívül** találhatók. Használd helyettük a megadott eszközt.

### .NET Aspire — Használd az Aspire MCP szervert (ajánlott) vagy a Context7-et

Az Aspire dokumentáció az **aspire.dev** oldalon található, nem a Learn-en. A legjobb eszköz az Aspire CLI verziójától függ:

**CLI 13.2+** (ajánlott) — Az Aspire MCP szerver beépített dokumentáció-kereső eszközöket tartalmaz:

| MCP eszköz | Leírás |
|----------|-------------|
| `list_docs` | Felsorolja az aspire.dev-en elérhető összes dokumentációt |
| `search_docs` | Súlyozott lexikális keresés az aspire.dev tartalmában |
| `get_doc` | Lekéri egy adott dokumentumot slug alapján |

Ezek az Aspire CLI 13.2-ben érkeznek ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Frissítéshez: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — Az MCP szerver integráció-keresést biztosít (`list_integrations`, `get_integration_docs`), de **nem** biztosít dokumentáció-keresést. Használj Context7-et:

| Library ID | Használat |
|---|---|
| `/microsoft/aspire.dev` | Elsődleges — útmutatók, integrációk, CLI referencia, telepítés |
| `/dotnet/aspire` | Futási idő forrás — API belső részei, megvalósítási részletek |
| `/communitytoolkit/aspire` | Közösségi integrációk — Go, Java, Node.js, Ollama |

### VS Code — Használd a Context7-et

A VS Code dokumentáció a **code.visualstudio.com** oldalon található, nem a Learn-en.

| Library ID | Használat |
|---|---|
| `/websites/code_visualstudio` | Felhasználói dokumentáció — beállítások, funkciók, hibakeresés, távoli fejlesztés |
| `/websites/code_visualstudio_api` | Bővítmény API — webviews, TreeView-k, parancsok, hozzájárulási pontok |

### GitHub — Használd a Context7-et

A GitHub dokumentáció a **docs.github.com** és a **cli.github.com** oldalakon található.

| Library ID | Használat |
|---|---|
| `/websites/github_en` | Actions, API, repo-k, biztonság, adminisztráció, Copilot |
| `/websites/cli_github` | A GitHub CLI (`gh`) parancsai és kapcsolói |

### Agent Framework — Használd a Learn MCP-t + Context7-et

Az Agent Framework oktatóanyagai a learn.microsoft.com oldalon vannak (használd a `microsoft_docs_search`-t), de a **GitHub repo** API-szintű részleteket tartalmaz, amelyek gyakran megelőzik a publikált dokumentációt — különösen a DevUI REST API referencia, a CLI opciók és a .NET integráció terén.

| Library ID | Használat |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Oktatóanyagok — DevUI útmutatók, nyomkövetés, munkafolyamat-orchesztráció |
| `/microsoft/agent-framework` | API részletek — DevUI REST végpontok, CLI kapcsolók, hitelesítés, .NET `AddDevUI`/`MapDevUI` |

**DevUI tipp:** Lekérdezd a Learn weboldal forrását a lépésről lépésre útmutatókért, majd a repo forrását az API-szintű részletekért (végpont-sémák, proxy konfiguráció, hitelesítési tokenek).

---

## Context7 beállítása

Bármilyen Context7 lekérdezéshez először oldd fel a library ID-t (egyszeri művelet munkamenetenként):

1. Hívd meg a `mcp_context7_resolve-library-id`-t a technológia nevével
2. Hívd meg a `mcp_context7_query-docs`-t a visszaadott library ID-vel és egy konkrét lekérdezéssel

---

## Hatékony lekérdezések írása

Legyél konkrét — tüntesd fel a verziót, a szándékot és a nyelvet:

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

Add meg a kontextust:
- **Verzió** amikor releváns (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Feladat célja** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Nyelv** többnyelvű dokumentáció esetén (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felelősségkizárás**:
Ez a dokumentum az AI-alapú fordítószolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár igyekszünk pontosak lenni, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelven tekintendő hiteles forrásnak. Kritikus információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget az e fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->