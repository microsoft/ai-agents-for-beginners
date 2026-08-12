---
name: microsoft-docs
description: Prehľadávajte oficiálnu dokumentáciu Microsoftu, aby ste našli koncepty,
  návody a ukážky kódu naprieč Azure, .NET, Agent Framework, Aspire, VS Code, GitHub
  a ďalšími. Používa Microsoft Learn MCP ako predvolený zdroj, spolu s Context7 a
  Aspire MCP pre obsah, ktorý sa nachádza mimo learn.microsoft.com.
---
# Microsoft Docs

Výskumná zručnosť pre technologický ekosystém Microsoftu. Zahŕňa learn.microsoft.com a dokumentáciu, ktorá sa nachádza mimo neho (VS Code, GitHub, Aspire, repozitáre Agent Framework).

---

## Predvolené: Microsoft Learn MCP

Použite tieto nástroje pre **všetko na learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows a ďalšie. Toto je hlavný nástroj pre väčšinu otázok týkajúcich sa dokumentácie Microsoftu.

| Nástroj | Účel |
|------|---------|
| `microsoft_docs_search` | Vyhľadávať na learn.microsoft.com — koncepty, príručky, tutoriály, konfigurácie |
| `microsoft_code_sample_search` | Nájdite fungujúce ukážky kódu z Learn dokumentácie. Pre najlepšie výsledky zadajte `language` (`python`, `csharp`, atď.) |
| `microsoft_docs_fetch` | Získať celý obsah stránky z konkrétnej URL (keď výňatky z vyhľadávania nestačia) |

Použite `microsoft_docs_fetch` po vyhľadávaní, keď potrebujete kompletné tutoriály, všetky konfiguračné možnosti alebo keď sú výňatky z vyhľadávania orezané.

---

## Výnimky: Kedy použiť iné nástroje

Nasledujúce kategórie sa nachádzajú **mimo** learn.microsoft.com. Namiesto toho použite určený nástroj.

### .NET Aspire — Použite Aspire MCP Server (preferované) alebo Context7

Dokumentácia Aspire sa nachádza na **aspire.dev**, nie na Learn. Najlepší nástroj závisí od verzie Aspire CLI:

**CLI 13.2+** (odporúčané) — Aspire MCP server obsahuje vstavané nástroje na vyhľadávanie v dokumentácii:

| MCP Tool | Popis |
|----------|-------------|
| `list_docs` | Zoznamuje všetku dostupnú dokumentáciu z aspire.dev |
| `search_docs` | Vážené lexikálne vyhľadávanie v obsahu aspire.dev |
| `get_doc` | Získa konkrétny dokument podľa slugu |

Tieto sú súčasťou Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Na aktualizáciu: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP server poskytuje vyhľadávanie integrácií (`list_integrations`, `get_integration_docs`), ale **nie** vyhľadávanie dokumentácie. V takom prípade použite Context7:

| Library ID | Použitie |
|---|---|
| `/microsoft/aspire.dev` | Primárne — príručky, integrácie, referencia CLI, nasadenie |
| `/dotnet/aspire` | Zdroj runtime — vnútorné API, implementačné detaily |
| `/communitytoolkit/aspire` | Komunitné integrácie — Go, Java, Node.js, Ollama |

### VS Code — Použite Context7

Dokumentácia VS Code sa nachádza na **code.visualstudio.com**, nie na Learn.

| Library ID | Použitie |
|---|---|
| `/websites/code_visualstudio` | Používateľská dokumentácia — nastavenia, funkcie, ladenie, vzdialený vývoj |
| `/websites/code_visualstudio_api` | Extension API — webviews, TreeViews, príkazy, kon‑tribučné body |

### GitHub — Použite Context7

Dokumentácia GitHubu sa nachádza na **docs.github.com** a **cli.github.com**.

| Library ID | Použitie |
|---|---|
| `/websites/github_en` | Actions, API, repozitáre, zabezpečenie, administrácia, Copilot |
| `/websites/cli_github` | Príkazy a prepínače GitHub CLI (`gh`) |

### Agent Framework — Použite Learn MCP + Context7

Tutoriály Agent Framework sú na learn.microsoft.com (použite `microsoft_docs_search`), ale **GitHub repozitár** obsahuje detaily na úrovni API, ktoré sú často pred publikovanou dokumentáciou — najmä referenciu DevUI REST API, možnosti CLI a .NET integráciu.

| Library ID | Použitie |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutoriály — DevUI príručky, trasovanie, orchestrácia pracovných tokov |
| `/microsoft/agent-framework` | Detaily API — DevUI REST endpointy, CLI prepínače, autentifikácia, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Najprv sa pozrite na zdroj na Learn webe pre návodové príručky, potom do repozitára pre API-úrovňové špecifiká (schémy endpointov, konfigurácia proxy, autentifikačné tokeny).

---

## Nastavenie Context7

Pre akýkoľvek dotaz v Context7 najprv vyriešte ID knižnice (jednorazovo na reláciu):

1. Zavolajte `mcp_context7_resolve-library-id` s názvom technológie
2. Zavolajte `mcp_context7_query-docs` s vráteným ID knižnice a konkrétnym dotazom

---

## Písanie efektívnych dotazov

Buďte konkrétni — uveďte verziu, zámer a jazyk:

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
- **Verzia** ak relevantné (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Účel úlohy** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Jazyk** pre polyglot dokumentáciu (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vylúčenie zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by sa mal považovať za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny preklad vykonaný človekom. Za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu nenesieme zodpovednosť.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->