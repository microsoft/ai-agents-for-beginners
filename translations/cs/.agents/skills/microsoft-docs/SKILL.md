---
name: microsoft-docs
description: Prohledávejte oficiální dokumentaci Microsoftu, abyste našli koncepty,
  návody a ukázky kódu napříč Azure, .NET, Agent Framework, Aspire, VS Code, GitHub
  a dalšími. Jako výchozí používá Microsoft Learn MCP; pro obsah, který se nachází
  mimo learn.microsoft.com, používá Context7 a Aspire MCP.
---
# Microsoft Docs

Výzkumná dovednost pro ekosystém technologií Microsoft. Pokrývá learn.microsoft.com a dokumentaci, která existuje mimo něj (repozitáře VS Code, GitHub, Aspire, Agent Framework).

---

## Výchozí: Microsoft Learn MCP

Použijte tyto nástroje pro **vše na learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows a další. Toto je primární nástroj pro drtivou většinu dotazů ohledně dokumentace Microsoftu.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Hledání na learn.microsoft.com — koncepty, průvodci, tutoriály, konfigurace |
| `microsoft_code_sample_search` | Najděte funkční ukázky kódu z Learn dokumentů. Zadejte `language` (`python`, `csharp`, etc.) pro nejlepší výsledky |
| `microsoft_docs_fetch` | Získejte celý obsah stránky z konkrétní URL (když výpisy z hledání nestačí) |

Použijte `microsoft_docs_fetch` po hledání, když potřebujete kompletní tutoriály, všechny možnosti konfigurace nebo když jsou výpisy z hledání zkrácené.

---

## Výjimky: Kdy použít jiné nástroje

Následující kategorie žijí **mimo** learn.microsoft.com. Použijte místo toho určený nástroj.

### .NET Aspire — Použijte Aspire MCP Server (preferováno) nebo Context7

Aspire dokumentace žije na **aspire.dev**, ne na Learn. Nejlepší nástroj závisí na vaší verzi Aspire CLI:

**CLI 13.2+** (doporučeno) — Aspire MCP server obsahuje vestavěné nástroje pro vyhledávání dokumentace:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Vypíše veškerou dostupnou dokumentaci z aspire.dev |
| `search_docs` | Vážené lexikální vyhledávání napříč obsahem aspire.dev |
| `get_doc` | Získá konkrétní dokument podle slug |

Tyto nástroje jsou součástí Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Aktualizace: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP server poskytuje integraci lookup (`list_integrations`, `get_integration_docs`) ale **ne** vyhledávání dokumentace. Použijte jako zálohu Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Primárně — průvodci, integrace, reference CLI, nasazení |
| `/dotnet/aspire` | Zdroj runtime — interní API, implementační detaily |
| `/communitytoolkit/aspire` | Komunitní integrace — Go, Java, Node.js, Ollama |

### VS Code — Použijte Context7

VS Code dokumentace žije na **code.visualstudio.com**, ne na Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Uživatelská dokumentace — nastavení, funkce, ladění, vzdálený vývoj |
| `/websites/code_visualstudio_api` | Rozhraní pro rozšíření — webview, TreeViews, příkazy, body přispění |

### GitHub — Použijte Context7

GitHub dokumentace žije na **docs.github.com** a **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, repozitáře, bezpečnost, administrace, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) příkazy a přepínače |

### Agent Framework — Použijte Learn MCP + Context7

Agent Framework tutoriály jsou na learn.microsoft.com (použijte `microsoft_docs_search`), ale **GitHub repo** má detail na úrovni API, který často předbíhá publikované dokumenty — zejména DevUI REST API reference, volby CLI a .NET integrace.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutoriály — DevUI průvodci, trasování, orchestraci workflow |
| `/microsoft/agent-framework` | API detaily — DevUI REST endpointy, CLI přepínače, auth, .NET `AddDevUI`/`MapDevUI` |

**Tip pro DevUI:** Nejprve prohow-to průvodce konzultujte zdroj webu Learn, poté zdroj repozitáře pro specifika na úrovni API (schémata endpointů, proxy konfigurace, auth tokeny).

---

## Context7 Nastavení

Pro jakýkoli dotaz do Context7 nejprve vyřešte ID knihovny (jednorázově za sezení):

1. Zavolejte `mcp_context7_resolve-library-id` s názvem technologie
2. Zavolejte `mcp_context7_query-docs` s vráceným ID knihovny a konkrétním dotazem

---

## Psaní efektivních dotazů

Buďte konkrétní — uveďte verzi, záměr a jazyk:

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
- **Version** when relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Task intent** (`rychlý start`, `tutoriál`, `přehled`, `limity`, `referenční dokumentace API`)
- **Language** for polyglot docs (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Prohlášení o vyloučení odpovědnosti:
Tento dokument byl přeložen pomocí služby pro automatický překlad AI (Co-op Translator) (https://github.com/Azure/co-op-translator). Ačkoli usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nezodpovídáme za jakákoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->