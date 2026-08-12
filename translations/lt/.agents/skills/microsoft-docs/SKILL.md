---
name: microsoft-docs
description: Ieškokite oficialioje Microsoft dokumentacijoje sąvokų, pamokų ir kodo
  pavyzdžių apie Azure, .NET, Agent Framework, Aspire, VS Code, GitHub ir dar daugiau.
  Naudoja Microsoft Learn MCP kaip numatytąjį, o Context7 ir Aspire MCP — turiniui,
  esantį už learn.microsoft.com ribų.
---
# Microsoft Docs

Tyrimų įgūdis Microsoft technologijų ekosistemos srityje. Aprėpia learn.microsoft.com ir dokumentaciją, kuri yra už jos ribų (VS Code, GitHub, Aspire, Agent Framework saugyklos).

---

## Default: Microsoft Learn MCP

Naudokite šiuos įrankius **viskam, kas yra learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows ir kt. Tai pagrindinis įrankis daugumai Microsoft dokumentacijos užklausų.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Ieškoti learn.microsoft.com — sąvokos, vadovai, pamokos, konfigūracija |
| `microsoft_code_sample_search` | Rasti veikiančius kodo fragmentus iš Learn dokumentų. Pateikite `language` (`python`, `csharp`, ir kt.) geriausiems rezultatams |
| `microsoft_docs_fetch` | Gauti pilną puslapio turinį iš konkretaus URL (kai paieškos ištraukos nepakankamos) |

Naudokite `microsoft_docs_fetch` po paieškos, kai reikia išsamių pamokų, visų konfigūracijos parinkčių arba kai paieškos ištraukos yra sutrumpintos.

---

## Exceptions: When to Use Other Tools

Tolimesnės kategorijos yra **už** learn.microsoft.com ribų. Vietoj to naudokite nurodytą įrankį.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Aspire dokumentacija yra **aspire.dev**, ne Learn. Geriausias įrankis priklauso nuo jūsų Aspire CLI versijos:

**CLI 13.2+** (rekomenduojama) — Aspire MCP serveris turi įmontuotus dokumentacijos paieškos įrankius:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Išvardina visą prieinamą dokumentaciją iš aspire.dev |
| `search_docs` | Svorinė leksinė paieška per aspire.dev turinį |
| `get_doc` | Gauti konkretų dokumentą pagal slug'ą |

Šios funkcijos pristatomos Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Norėdami atnaujinti: `aspire update --self --channel daily`. Nuoroda: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP serveris suteikia integracijų paiešką (`list_integrations`, `get_integration_docs`), bet **ne** dokumentacijos paieškos. Grįžkite prie Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Pagrindinė — vadovai, integracijos, CLI referencija, diegimas |
| `/dotnet/aspire` | Vykdymo šaltinis — API vidiniai elementai, įgyvendinimo detalės |
| `/communitytoolkit/aspire` | Bendruomenės integracijos — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

VS Code dokumentacija yra **code.visualstudio.com**, ne Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Vartotojo dokumentacija — nustatymai, funkcijos, derinimas, nuotolinis kūrimas |
| `/websites/code_visualstudio_api` | Plėtinių API — webviews, TreeViews, komandos, prisidėjimo taškai |

### GitHub — Use Context7

GitHub dokumentacija yra **docs.github.com** ir **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, saugyklos, sauga, administravimas, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) komandos ir parametrai |

### Agent Framework — Use Learn MCP + Context7

Agent Framework mokymai yra learn.microsoft.com (naudokite `microsoft_docs_search`), tačiau **GitHub saugykla** turi API lygmens detales, kurios dažnai yra priekyje skelbiamų dokumentų — ypač DevUI REST API referencija, CLI parinktys ir .NET integracija.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Mokymai — DevUI vadovai, sekimas, darbo eigos orkestracija |
| `/microsoft/agent-framework` | API detalės — DevUI REST galiniai taškai, CLI žymos, autentifikacija, .NET `AddDevUI`/`MapDevUI` |

**DevUI patarimas:** Užklauskite Learn svetainės šaltinio, kad rastumėte kaip daryti vadovus, o tada saugyklos šaltinį — API lygmens specifikai (galinių taškų schemos, proxy konfigūracija, autentifikacijos žetonai).

---

## Context7 Setup

Kiekvienai Context7 užklausiai pirmiausia nustatykite bibliotekos ID (vieną kartą per sesiją):

1. Iškvieskite `mcp_context7_resolve-library-id` su technologijos pavadinimu
2. Iškvieskite `mcp_context7_query-docs` su gautu bibliotekos ID ir konkrečia užklausa

---

## Writing Effective Queries

Būkite konkretūs — nurodykite versiją, tikslą ir kalbą:

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
- **Task intent** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Language** for polyglot docs (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Atsakomybės apribojimas:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą Co-op Translator (https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Esant svarbiai informacijai, rekomenduojamas profesionalus žmogaus atliekamas vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->