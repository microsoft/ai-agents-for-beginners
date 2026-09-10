---
name: microsoft-docs
description: Mag-query sa opisyal na dokumentasyon ng Microsoft upang hanapin ang
  mga konsepto, tutorial, at mga halimbawa ng code sa iba't ibang serbisyo tulad ng
  Azure, .NET, Agent Framework, Aspire, VS Code, GitHub, at iba pa. Ginagamit ang
  Microsoft Learn MCP bilang default, kasama ang Context7 at Aspire MCP para sa nilalamang
  nasa labas ng learn.microsoft.com.
---
# Microsoft Docs

Kasanayan sa pananaliksik para sa ekosistema ng teknolohiyang Microsoft. Saklaw ang learn.microsoft.com at dokumentasyong nasa labas nito (VS Code, GitHub, Aspire, Agent Framework repos).

---

## Default: Microsoft Learn MCP

Gamitin ang mga tool na ito para sa **everything on learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, at iba pa. Ito ang pangunahing tool para sa karamihan ng mga tanong tungkol sa dokumentasyon ng Microsoft.

| Tool | Layunin |
|------|---------|
| `microsoft_docs_search` | Maghanap sa learn.microsoft.com — mga konsepto, gabay, tutorial, konfigurasyon |
| `microsoft_code_sample_search` | Hanapin ang mga gumaganang snippet ng code mula sa mga dokumento ng Learn. Ibigay ang `language` (`python`, `csharp`, etc.) para sa pinakamahusay na resulta |
| `microsoft_docs_fetch` | Kunin ang buong nilalaman ng pahina mula sa isang partikular na URL (kapag hindi sapat ang mga excerpt mula sa paghahanap) |

Gamitin ang `microsoft_docs_fetch` pagkatapos mag-search kapag kailangan mo ng kumpletong tutorial, lahat ng opsyon ng konfigurasyon, o kapag ang mga excerpt mula sa paghahanap ay pinutol.

---

## Exceptions: When to Use Other Tools

Ang mga sumusunod na kategorya ay nasa **labas** ng learn.microsoft.com. Gamitin ang tinukoy na tool sa halip.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Ang mga dokumento ng Aspire ay nasa **aspire.dev**, hindi sa Learn. Ang pinakamainam na tool ay depende sa iyong Aspire CLI na bersyon:

**CLI 13.2+** (inirerekomenda) — Kasama sa Aspire MCP server ang mga built-in na tool sa paghahanap ng docs:

| MCP Tool | Paglalarawan |
|----------|-------------|
| `list_docs` | Nililista ang lahat ng magagamit na dokumentasyon mula sa aspire.dev |
| `search_docs` | Lexical search na may bigat sa buong nilalaman ng aspire.dev |
| `get_doc` | Kukunin ang isang partikular na dokumento ayon sa slug |

Kasama ang mga ito sa Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Upang i-update: `aspire update --self --channel daily`. Sanggunian: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — Nagbibigay ang MCP server ng integration lookup (`list_integrations`, `get_integration_docs`) pero **hindi** ng paghahanap ng docs. Gamitin ang Context7 bilang fallback:

| Library ID | Gamit para sa |
|---|---|
| `/microsoft/aspire.dev` | Pangunahing — mga gabay, integrasyon, sanggunian ng CLI, deployment |
| `/dotnet/aspire` | Pinagmulan ng runtime — API internals, detalye ng implementasyon |
| `/communitytoolkit/aspire` | Mga integrasyon ng komunidad — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

Ang mga dokumento ng VS Code ay nasa **code.visualstudio.com**, hindi sa Learn.

| Library ID | Gamit para sa |
|---|---|
| `/websites/code_visualstudio` | Mga dokumento ng user — mga setting, tampok, debugging, remote dev |
| `/websites/code_visualstudio_api` | API ng Extension — webviews, TreeViews, commands, contribution points |

### GitHub — Use Context7

Ang mga dokumento ng GitHub ay nasa **docs.github.com** at **cli.github.com**.

| Library ID | Gamit para sa |
|---|---|
| `/websites/github_en` | Actions, API, repos, security, admin, Copilot |
| `/websites/cli_github` | Mga command at flag ng GitHub CLI (`gh`) |

### Agent Framework — Use Learn MCP + Context7

Ang mga tutorial ng Agent Framework ay nasa learn.microsoft.com (gamitin ang `microsoft_docs_search`), ngunit ang **GitHub repo** ay may detalye sa antas ng API na madalas na nauunang nailathala kaysa sa mga publikadong dokumento — partikular ang DevUI REST API reference, mga opsyon ng CLI, at integrasyon ng .NET.

| Library ID | Gamit para sa |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Mga tutorial — gabay sa DevUI, tracing, orchestration ng workflow |
| `/microsoft/agent-framework` | Detalye ng API — DevUI REST endpoints, CLI flags, auth, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** I-query ang source ng website ng Learn para sa mga how-to guide, pagkatapos ang source ng repo para sa mga API-level na detalye (endpoint schemas, proxy config, auth tokens).

---

## Context7 Setup

Para sa anumang query sa Context7, i-resolve muna ang library ID (isang beses kada session):

1. Tawagan ang `mcp_context7_resolve-library-id` gamit ang pangalan ng teknolohiya
2. Tawagan ang `mcp_context7_query-docs` gamit ang nakuha na library ID at isang tiyak na query

---

## Writing Effective Queries

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
- **Bersyon** kapag may kaugnayan (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Layunin ng gawain** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Wika** para sa polyglot na dokumentasyon (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Paunawa:
Ang dokumentong ito ay isinalin gamit ang serbisyong pagsasalin na pinapagana ng AI na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatumpak. Dapat ituring na opisyal na sanggunian ang orihinal na dokumento sa orihinal nitong wika. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng isang tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring lumitaw mula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->