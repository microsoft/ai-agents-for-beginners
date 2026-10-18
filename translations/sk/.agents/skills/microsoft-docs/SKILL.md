---
name: microsoft-docs
description: Vyhľadajte v oficiálnej dokumentácii Microsoftu koncepty, návody a príklady
  kódu týkajúce sa Azure, .NET, Agent Framework, Aspire, VS Code, GitHub a ďalších.
  Používa Microsoft Learn MCP ako predvolený zdroj, s Context7 a Aspire MCP pre obsah,
  ktorý sa nachádza mimo learn.microsoft.com.
---
# Microsoft Docs

Výskumná zručnosť pre ekosystém technológií Microsoft. Zahŕňa learn.microsoft.com a dokumentáciu, ktorá sa nachádza mimo neho (VS Code, GitHub, Aspire, Agent Framework repozitáre).

---

## Predvolené: Microsoft Learn MCP

Používajte tieto nástroje pre **všetko na learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows a ďalšie. Toto je hlavný nástroj pre väčšinu požiadaviek na dokumentáciu Microsoftu.

| Nástroj | Účel |
|------|---------|
| `microsoft_docs_search` | Vyhľadávanie na learn.microsoft.com — koncepty, návody, tutoriály, konfigurácia |
| `microsoft_code_sample_search` | Nájdi funkčné ukážky kódu z dokumentácie Learn. Pre najlepšie výsledky použite `language` (`python`, `csharp`, atď.) |
| `microsoft_docs_fetch` | Získaj celý obsah stránky z konkrétnej URL (keď výňatky z vyhľadávania nie sú dostatočné) |

Používajte `microsoft_docs_fetch` po vyhľadávaní, keď potrebujete kompletné tutoriály, všetky možnosti konfigurácie, alebo keď sú výňatky z vyhľadávania skrátené.

---

## Výnimky: Kedy použiť iné nástroje

Nasledujúce kategórie sa nachádzajú **mimo** learn.microsoft.com. Namiesto toho použite uvedený nástroj.

### Aspire — Použite Aspire MCP Server (preferované) alebo Context7

Dokumentácia Aspire je na **aspire.dev**, nie na Learn. Najlepší nástroj závisí od verzie Aspire CLI:

**CLI 13.2+** (odporúčané) — Aspire MCP server obsahuje zabudované nástroje na vyhľadávanie dokumentácie:

| MCP Nástroj | Popis |
|----------|-------------|
| `list_docs` | Zoznam všetkej dostupnej dokumentácie z aspire.dev |
| `search_docs` | Vážené lexikálne vyhľadávanie v obsahu aspire.dev |
| `get_doc` | Načíta konkrétny dokument podľa slugu |

Tieto sú súčasťou Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Na aktualizáciu použite: `aspire update --self --channel daily`.

**CLI 13.1** — MCP server poskytuje vyhľadávanie integrácií (`list_integrations`, `get_integration_docs`), ale **nie** vyhľadávanie dokumentácie. Použite Context7:

| ID knižnice | Použitie |
|---|---|
| `/microsoft/aspire.dev` | Primárne — návody, integrácie, referencia CLI, nasadenie |
| `/microsoft/aspire` | Zdroj runtime — API vnútornosti, detaily implementácie |
| `/communitytoolkit/aspire` | Komunitné integrácie — Go, Java, Node.js, Ollama |

### VS Code — Použite Context7

Dokumentácia VS Code je na **code.visualstudio.com**, nie na Learn.

| ID knižnice | Použitie |
|---|---|
| `/websites/code_visualstudio` | Používateľská dokumentácia — nastavenia, funkcie, ladenie, vzdialený vývoj |
| `/websites/code_visualstudio_api` | API rozšírení — webviews, TreeViews, príkazy, body príspevkov |

### GitHub — Použite Context7

Dokumentácia GitHub je na **docs.github.com** a **cli.github.com**.

| ID knižnice | Použitie |
|---|---|
| `/websites/github_en` | Actions, API, repozitáre, zabezpečenie, admin, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) príkazy a prepínače |

### Agent Framework — Použite Learn MCP + Context7

Tutoriály Agent Framework sú na learn.microsoft.com (použite `microsoft_docs_search`), ale **GitHub repozitár** obsahuje API úroveň detailov, ktoré často predbehnú publikovanú dokumentáciu — najmä referencia DevUI REST API, možnosti CLI a integrácia .NET.

| ID knižnice | Použitie |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutoriály — DevUI návody, sledovanie, orchestrácia workflow |
| `/microsoft/agent-framework` | API detaily — DevUI REST koncové body, prepínače CLI, autentifikácia, .NET `AddDevUI`/`MapDevUI` |

**Tip pre DevUI:** Najprv vyhľadajte návody na stránke Learn, potom v repozitári špecifiká na úrovni API (schémy koncových bodov, proxy konfigurácie, autentifikačné tokeny).

---

## Nastavenie Context7

Pre akúkoľvek Context7 otázku najprv zistite ID knižnice (raz na reláciu):

1. Zavolajte `mcp_context7_resolve-library-id` s názvom technológie
2. Zavolajte `mcp_context7_query-docs` s vráteným ID knižnice a konkrétnou otázkou

---

## Písanie efektívnych otázok

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

Pridajte kontext:
- **Verzia** keď je relevantná (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Zámer úlohy** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Jazyk** pre polyglot dokumentáciu (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->