---
name: microsoft-docs
description: Ieškokite oficialios Microsoft dokumentacijos, kad rastumėte koncepcijas,
  pamokas ir kodo pavyzdžius apie Azure, .NET, Agent Framework, Aspire, VS Code, GitHub
  ir daugiau. Numatytoji paieškos sistema yra Microsoft Learn MCP, o turiniui, esantys
  už learn.microsoft.com ribų, naudojami Context7 ir Aspire MCP.
---
# Microsoft Docs

Tyrimų įgūdžiai Microsoft technologijų ekosistemai. Apima learn.microsoft.com ir dokumentaciją, esančią už jo ribų (VS Code, GitHub, Aspire, Agent Framework repozitorijos).

---

## Numatytoji reikšmė: Microsoft Learn MCP

Naudokite šiuos įrankius **viskam, kas susiję su learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows ir daugiau. Tai pagrindinis įrankis daugumai Microsoft dokumentacijos užklausų.

| Įrankis | Paskirtis |
|------|---------|
| `microsoft_docs_search` | Ieškoti learn.microsoft.com — sąvokos, vadovai, pamokos, konfigūracija |
| `microsoft_code_sample_search` | Rasti veikiančius kodo fragmentus Learn dokumentuose. Geriausiems rezultatams naudokite `language` (`python`, `csharp` ir kt.) |
| `microsoft_docs_fetch` | Gauti visą puslapio turinį iš konkretaus URL (kai paieškos ištraukoms nepakanka) |

Naudokite `microsoft_docs_fetch` po paieškos, kai reikia pilnų pamokų, visų konfigūracijos parinkčių arba kai paieškos ištraukos yra sutrumpintos.

---

## Išimtys: Kada naudoti kitus įrankius

Šios kategorijos yra **už** learn.microsoft.com ribų. Vietoj to naudokite nurodytą įrankį.

### Aspire — naudokite Aspire MCP Server (pirmenybė) arba Context7

Aspire dokumentacija yra **aspire.dev**, o ne Learn. Geriausias įrankis priklauso nuo jūsų Aspire CLI versijos:

**CLI 13.2+** (rekomenduojama) — Aspire MCP serveris turi įmontuotus dokumentų paieškos įrankius:

| MCP įrankis | Aprašymas |
|----------|-------------|
| `list_docs` | Išvardina visą aspit.dev dokumentaciją |
| `search_docs` | Svorinė leksinė paieška aspit.dev turinyje |
| `get_doc` | Gauna konkretų dokumentą pagal _slug_ |

Šie įrankiai pateikti Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Norėdami atnaujinti: `aspire update --self --channel daily`.

**CLI 13.1** — MCP serveris siūlo integracijos paiešką (`list_integrations`, `get_integration_docs`), bet **ne** dokumentų paiešką. Tokiu atveju naudokite Context7:

| Bibliotekos ID | Naudojimas |
|---|---|
| `/microsoft/aspire.dev` | Pagrindinė — vadovai, integracijos, CLI nuorodos, diegimas |
| `/microsoft/aspire` | Vykdymo šaltinis — API vidiniai dalykai, įgyvendinimo detalės |
| `/communitytoolkit/aspire` | Bendruomenės integracijos — Go, Java, Node.js, Ollama |

### VS Code — naudokite Context7

VS Code dokumentacija yra **code.visualstudio.com**, o ne Learn.

| Bibliotekos ID | Naudojimas |
|---|---|
| `/websites/code_visualstudio` | Naudotojo dokumentacija — nustatymai, funkcijos, derinimas, nuotolinis kūrimas |
| `/websites/code_visualstudio_api` | Plėtinių API — webviews, TreeViews, komandos, indėlio taškai |

### GitHub — naudokite Context7

GitHub dokumentacija yra **docs.github.com** ir **cli.github.com**.

| Bibliotekos ID | Naudojimas |
|---|---|
| `/websites/github_en` | Actions, API, repozitorijos, saugumas, administravimas, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) komandos ir vėliavėlės |

### Agent Framework — naudokite Learn MCP + Context7

Agent Framework pamokos yra learn.microsoft.com (naudokite `microsoft_docs_search`), tačiau **GitHub repo** turi API lygio detales, kurios dažnai yra pažangesnės nei paskelbta dokumentacija — ypač DevUI REST API nuoroda, CLI parinktys ir .NET integracija.

| Bibliotekos ID | Naudojimas |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Pamokos — DevUI vadovai, sekimas, darbų tvarkaraščio organizavimas |
| `/microsoft/agent-framework` | API detalės — DevUI REST galiniai taškai, CLI vėliavėlės, autentifikavimas, .NET `AddDevUI`/`MapDevUI` |

**DevUI patarimas:** Pirma užduokite klausimą Learn svetainės šaltinyje dėl kaip padaryti vadovų, tada repo šaltinyje dėl API lygio specifikos (galinių taškų schemos, proxy konfigūracija, autentifikavimo raktai).

---

## Context7 nustatymas

Bet kokiai Context7 užklausai pirmiausia išspręskite bibliotekos ID (vienąkart per sesiją):

1. Iškvieskite `mcp_context7_resolve-library-id` su technologijos pavadinimu
2. Iškvieskite `mcp_context7_query-docs` su grąžintu bibliotekos ID ir specifine užklausa

---

## Efektyvių užklausų rašymas

Būkite konkretūs — nurodykite versiją, ketinimą ir kalbą:

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

Įtraukite kontekstą:
- **Versija** kai aktualu (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Užduoties ketinimas** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Kalba** daugiakalbei dokumentacijai (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->