---
name: microsoft-docs
description: Hivatalos Microsoft dokumentáció lekérdezése fogalmak, útmutatók és kódpéldák
  megtalálásához az Azure, .NET, Agent Framework, Aspire, VS Code, GitHub és még sok
  más területén. Alapértelmezés szerint a Microsoft Learn MCP-t használja, a Context7
  és Aspire MCP pedig azokhoz a tartalmakhoz, amelyek a learn.microsoft.com oldalon
  kívül érhetők el.
---
# Microsoft Docs

Kutatási készség a Microsoft technológiai ökoszisztémához. Magában foglalja a learn.microsoft.com-ot és az azon kívül élő dokumentációt (VS Code, GitHub, Aspire, Agent Framework repók).

---

## Alapértelmezett: Microsoft Learn MCP

Használd ezeket az eszközöket **mindenhez a learn.microsoft.com-on** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows és még több. Ez az elsődleges eszköz a Microsoft dokumentációs lekérdezések túlnyomó többségéhez.

| Eszköz | Cél |
|------|---------|
| `microsoft_docs_search` | Keresés a learn.microsoft.com-on — fogalmak, útmutatók, oktatóanyagok, konfiguráció |
| `microsoft_code_sample_search` | Működő kódrészletek keresése a Learn docsból. A legjobb eredményért add át a `language` (`python`, `csharp`, stb.) |
| `microsoft_docs_fetch` | Teljes oldal tartalmának lekérése egy adott URL-ről (amikor a keresési kivonatok nem elegendőek) |

Használd az `microsoft_docs_fetch`-t a keresés után, amikor teljes oktatóanyagokra, minden konfigurációs lehetőségre van szükség, vagy ha a keresési kivonatok rövidítve jelennek meg.

---

## Kivételek: Mikor Használj Más Eszközöket

A következő kategóriák a **learn.microsoft.com-on kívül** élnek. Használd helyette a megjelölt eszközt.

### Aspire — Használd az Aspire MCP Servert (ajánlott) vagy a Context7-et

Az Aspire dokumentációk az **aspire.dev** oldalon találhatók, nem a Learn-en. A legjobb eszköz a te Aspire CLI verziódtól függ:

**CLI 13.2+** (ajánlott) — Az Aspire MCP szerver beépített dokumentációs kereső eszközöket tartalmaz:

| MCP Eszköz | Leírás |
|----------|-------------|
| `list_docs` | Felsorolja az aspire.dev összes elérhető dokumentációját |
| `search_docs` | Súlyozott lexikális keresés az aspire.dev tartalomban |
| `get_doc` | Egy adott dokumentum lekérése slug alapján |

Ezek az Aspire CLI 13.2-ben érkeznek ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Frissítéshez: `aspire update --self --channel daily`.

**CLI 13.1** — Az MCP szerver integrációs lekérdezést biztosít (`list_integrations`, `get_integration_docs`), de **nem** tartalomkeresőt. Ebben az esetben használd a Context7-et:

| Könyvtár ID | Használat |
|---|---|
| `/microsoft/aspire.dev` | Elsődleges — útmutatók, integrációk, CLI referencia, telepítés |
| `/microsoft/aspire` | Futásidejű forrás — API belső részletek, implementációs részletek |
| `/communitytoolkit/aspire` | Közösségi integrációk — Go, Java, Node.js, Ollama |

### VS Code — Használd a Context7-et

A VS Code dokumentációk a **code.visualstudio.com** oldalon találhatók, nem a Learn-en.

| Könyvtár ID | Használat |
|---|---|
| `/websites/code_visualstudio` | Felhasználói dokumentáció — beállítások, funkciók, hibakeresés, távoli fejlesztés |
| `/websites/code_visualstudio_api` | Bővítmény API — webnézetek, TreeViews, parancsok, hozzájárulási pontok |

### GitHub — Használd a Context7-et

A GitHub dokumentációk a **docs.github.com** és **cli.github.com** oldalakon találhatók.

| Könyvtár ID | Használat |
|---|---|
| `/websites/github_en` | Műveletek, API, repo-k, biztonság, adminisztráció, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) parancsok és kapcsolók |

### Agent Framework — Használd a Learn MCP + Context7-et

Az Agent Framework oktatóanyagok a learn.microsoft.com-on vannak (használd `microsoft_docs_search`-t), de a **GitHub repó** API szintű részleteket tartalmaz, amelyek gyakran megelőzik a közzétett dokumentumokat — különösen a DevUI REST API referencia, CLI opciók, és .NET integráció.

| Könyvtár ID | Használat |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Oktatóanyagok — DevUI útmutatók, nyomkövetés, munkafolyamat-irányítás |
| `/microsoft/agent-framework` | API részletek — DevUI REST végpontok, CLI kapcsolók, hitelesítés, .NET `AddDevUI`/`MapDevUI` |

**DevUI tipp:** Lekérdezd először a Learn webhely forrását a használati útmutatókért, majd a repó forrását az API szintű specifikumokért (végpont sémák, proxy konfiguráció, hitelesítő tokenek).

---

## Context7 Beállítás

Bármilyen Context7 lekérdezéshez először oldd fel a könyvtár ID-t (egyszer minden munkamenetben):

1. Hívd meg `mcp_context7_resolve-library-id`-t a technológia nevével
2. Hívd meg `mcp_context7_query-docs`-t a visszakapott könyvtár ID-vel és egy konkrét lekérdezéssel

---

## Hatékony Lekérdezések Írása

Légy konkrét — add meg a verziót, a célt és a nyelvet:

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
- **Verzió** ha releváns (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Feladat célja** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Nyelv** a poliglott dokumentációkhoz (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->