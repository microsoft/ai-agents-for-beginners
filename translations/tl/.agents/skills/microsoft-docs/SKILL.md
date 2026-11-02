---
name: microsoft-docs
description: Magsagawa ng pagsasaliksik sa opisyal na dokumentasyon ng Microsoft upang
  makahanap ng mga konsepto, tutorial, at mga halimbawa ng code sa Azure, .NET, Agent
  Framework, Aspire, VS Code, GitHub, at iba pa. Ginagamit ang Microsoft Learn MCP
  bilang default, kasama ang Context7 at Aspire MCP para sa mga nilalamang nasa labas
  ng learn.microsoft.com.
---
# Microsoft Docs

Kasanayan sa pananaliksik para sa ecosystem ng teknolohiyang Microsoft. Saklaw nito ang learn.microsoft.com at dokumentasyon na nasa labas nito (VS Code, GitHub, Aspire, mga repository ng Agent Framework).

---

## Default: Microsoft Learn MCP

Gamitin ang mga tool na ito para sa **lahat ng bagay sa learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, at iba pa. Ito ang pangunahing tool para sa karamihan ng mga tanong tungkol sa dokumentasyon ng Microsoft.

| Tool | Layunin |
|------|---------|
| `microsoft_docs_search` | Maghanap sa learn.microsoft.com — mga konsepto, gabay, tutorial, pagsasaayos |
| `microsoft_code_sample_search` | Hanapin ang mga gumaganang code snippet mula sa Learn docs. Ibigay ang `language` (`python`, `csharp`, atbp.) para sa pinakamahusay na resulta |
| `microsoft_docs_fetch` | Kumuha ng buong nilalaman ng pahina mula sa isang partikular na URL (kapag kulang ang mga excerpt mula sa paghahanap) |

Gamitin ang `microsoft_docs_fetch` pagkatapos maghanap kapag kailangan mo ng kumpletong mga tutorial, lahat ng opsyon sa pagsasaayos, o kapag pinutol ang mga excerpt ng paghahanap.

---

## Mga Ekssepsyon: Kailan Gamitin ang Ibang Mga Tool

Ang mga sumusunod na kategorya ay **nasa labas** ng learn.microsoft.com. Gamitin ang tinukoy na tool bilang kapalit.

### Aspire — Gamitin ang Aspire MCP Server (mas gusto) o Context7

Ang mga dokumento ng Aspire ay nasa **aspire.dev**, hindi sa Learn. Ang pinakamahusay na tool ay depende sa bersyon ng iyong Aspire CLI:

**CLI 13.2+** (inirerekomenda) — Kasama sa Aspire MCP server ang mga built-in na tool sa paghahanap ng dokumentasyon:

| MCP Tool | Paglalarawan |
|----------|-------------|
| `list_docs` | Nagtatala ng lahat ng magagamit na dokumentasyon mula sa aspire.dev |
| `search_docs` | Timbang na lexical na paghahanap sa nilalaman ng aspire.dev |
| `get_doc` | Kumukuha ng isang partikular na dokumento ayon sa slug |

Kasama ito sa Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Upang i-update: `aspire update --self --channel daily`.

**CLI 13.1** — Nagbibigay ang MCP server ng integration lookup (`list_integrations`, `get_integration_docs`) ngunit **hindi** ng dokumentasyon sa paghahanap. Bumalik sa Context7:

| Library ID | Gamitin para sa |
|---|---|
| `/microsoft/aspire.dev` | Pangunahing — mga gabay, integrasyon, sanggunian ng CLI, deployment |
| `/microsoft/aspire` | Runtime source — detalye ng API, mga detalye ng implementasyon |
| `/communitytoolkit/aspire` | Mga integrasyon ng komunidad — Go, Java, Node.js, Ollama |

### VS Code — Gamitin ang Context7

Ang mga dokumento ng VS Code ay nasa **code.visualstudio.com**, hindi sa Learn.

| Library ID | Gamitin para sa |
|---|---|
| `/websites/code_visualstudio` | Mga dokumento ng gumagamit — settings, tampok, debugging, remote dev |
| `/websites/code_visualstudio_api` | Extension API — webviews, TreeViews, commands, mga punto ng kontribusyon |

### GitHub — Gamitin ang Context7

Ang mga dokumento ng GitHub ay nasa **docs.github.com** at **cli.github.com**.

| Library ID | Gamitin para sa |
|---|---|
| `/websites/github_en` | Mga Actions, API, repos, seguridad, admin, Copilot |
| `/websites/cli_github` | Mga utos at flag ng GitHub CLI (`gh`) |

### Agent Framework — Gamitin ang Learn MCP + Context7

Ang mga tutorial ng Agent Framework ay nasa learn.microsoft.com (gamitin ang `microsoft_docs_search`), ngunit ang **GitHub repo** ay may detalye sa antas ng API na madalas na nauuna kaysa sa mga nalathalang dokumento — partikular na ang DevUI REST API reference, mga opsyon ng CLI, at integrasyon ng .NET.

| Library ID | Gamitin para sa |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Mga tutorial — mga gabay sa DevUI, pagsubaybay, workflow orchestration |
| `/microsoft/agent-framework` | Detalye ng API — DevUI REST endpoints, CLI flags, auth, .NET `AddDevUI`/`MapDevUI` |

**Tip para sa DevUI:** Magtanong muna sa source ng website ng Learn para sa mga how-to na gabay, pagkatapos ay sa source ng repo para sa mga detalye sa antas ng API (mga schema ng endpoint, proxy config, auth tokens).

---

## Setup ng Context7

Para sa anumang query sa Context7, alamin muna ang library ID (isang beses lang kada session):

1. Tawagan ang `mcp_context7_resolve-library-id` gamit ang pangalan ng teknolohiya
2. Tawagan ang `mcp_context7_query-docs` gamit ang nakuha na library ID at isang partikular na query

---

## Pagsusulat ng Epektibong Mga Query

Maging tiyak — isama ang bersyon, layunin, at wika:

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

Isama ang konteksto:
- **Bersyon** kapag mahalaga (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Layunin ng gawain** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Wika** para sa mga polyglot na dokumento (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->