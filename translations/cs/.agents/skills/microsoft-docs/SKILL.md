---
name: microsoft-docs
description: Prohledávejte oficiální dokumentaci Microsoftu a najděte koncepty, návody
  a ukázky kódu napříč Azure, .NET, Agent Framework, Aspire, VS Code, GitHub a dalšími.
  Používá Microsoft Learn MCP jako výchozí, s Context7 a Aspire MCP pro obsah, který
  se nachází mimo learn.microsoft.com.
---
# Microsoft Docs

Výzkumná dovednost pro ekosystém technologií Microsoft. Pokrývá learn.microsoft.com a dokumentaci mimo něj (VS Code, GitHub, Aspire, repozitáře Agent Framework).

---

## Výchozí: Microsoft Learn MCP

Používejte tyto nástroje pro **vše na learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows a více. Toto je hlavní nástroj pro naprostou většinu dotazů na dokumentaci Microsoft.

| Nástroj | Účel |
|------|---------|
| `microsoft_docs_search` | Vyhledávání na learn.microsoft.com — koncepty, průvodci, návody, konfigurace |
| `microsoft_code_sample_search` | Najděte funkční ukázky kódu z dokumentace Learn. Pro nejlepší výsledky použijte `language` (`python`, `csharp` atd.) |
| `microsoft_docs_fetch` | Získejte obsah celé stránky z konkrétní URL (když výňatky z vyhledávání nestačí) |

Použijte `microsoft_docs_fetch` po vyhledávání, když potřebujete kompletní návody, všechny možnosti konfigurace, nebo když jsou výňatky z vyhledávání zkrácené.

---

## Výjimky: Kdy použít jiné nástroje

Následující kategorie se nacházejí **mimo** learn.microsoft.com. Použijte místo toho specifikovaný nástroj.

### Aspire — Použijte Aspire MCP Server (preferováno) nebo Context7

Dokumentace Aspire je na **aspire.dev**, ne na Learn. Nejlepší nástroj závisí na vaší verzi Aspire CLI:

**CLI 13.2+** (doporučeno) — Aspire MCP server zahrnuje vestavěné nástroje pro vyhledávání v dokumentaci:

| MCP nástroj | Popis |
|----------|-------------|
| `list_docs` | Vypisuje veškerou dostupnou dokumentaci z aspire.dev |
| `search_docs` | Vážené lexikální vyhledávání v obsahu aspire.dev |
| `get_doc` | Získá konkrétní dokument podle slug |

Tyto nástroje jsou součástí Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Pro aktualizaci: `aspire update --self --channel daily`.

**CLI 13.1** — MCP server poskytuje vyhledávání integrací (`list_integrations`, `get_integration_docs`), ale **ne** vyhledávání v dokumentaci. Použijte naopak Context7:

| ID knihovny | Použití |
|---|---|
| `/microsoft/aspire.dev` | Hlavní — průvodci, integrace, reference CLI, nasazení |
| `/microsoft/aspire` | Zdroj běhového prostředí — vnitřnosti API, detaily implementace |
| `/communitytoolkit/aspire` | Komunitní integrace — Go, Java, Node.js, Ollama |

### VS Code — Použijte Context7

Dokumentace VS Code je na **code.visualstudio.com**, ne na Learn.

| ID knihovny | Použití |
|---|---|
| `/websites/code_visualstudio` | Uživatelská dokumentace — nastavení, funkce, ladění, vzdálený vývoj |
| `/websites/code_visualstudio_api` | API rozšíření — webviews, TreeViews, příkazy, přispívající body |

### GitHub — Použijte Context7

Dokumentace GitHub je na **docs.github.com** a **cli.github.com**.

| ID knihovny | Použití |
|---|---|
| `/websites/github_en` | Akce, API, repozitáře, zabezpečení, správa, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) příkazy a příznaky |

### Agent Framework — Použijte Learn MCP + Context7

Návody Agent Framework jsou na learn.microsoft.com (použijte `microsoft_docs_search`), ale **GitHub repozitář** má detaily na úrovni API, které jsou často aktuálnější než publikovaná dokumentace — zejména reference DevUI REST API, možnosti CLI a integrace .NET.

| ID knihovny | Použití |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Návody — průvodci DevUI, trasování, orchestraci workflow |
| `/microsoft/agent-framework` | Detail API — DevUI REST endpointy, příznaky CLI, autentizace, .NET `AddDevUI`/`MapDevUI` |

**Tip DevUI:** Nejprve dotazujte zdroj Learn webu pro návody, pak zdroj repozitáře pro API specifika (schémata endpointů, proxy konfigurace, autentizační tokeny).

---

## Nastavení Context7

Pro jakýkoli dotaz v Context7 nejprve vyhledejte ID knihovny (jednorázově za relaci):

1. Zavolejte `mcp_context7_resolve-library-id` s názvem technologie
2. Zavolejte `mcp_context7_query-docs` s vráceným ID knihovny a konkrétním dotazem

---

## Jak psát efektivní dotazy

Buďte konkrétní — zahrňte verzi, účel a jazyk:

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

Zahrňte kontext:
- **Verzi** pokud je relevantní (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Účel úkolu** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Jazyk** pro polyglot dokumentaci (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->