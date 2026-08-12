---
name: microsoft-docs
description: Consultar a documentação oficial da Microsoft para encontrar conceitos,
  tutoriais e exemplos de código sobre Azure, .NET, Agent Framework, Aspire, VS Code,
  GitHub e muito mais. Usa o Microsoft Learn MCP como padrão, com Context7 e Aspire
  MCP para conteúdo que esteja fora do learn.microsoft.com.
---
# Microsoft Docs

Habilidade de pesquisa para o ecossistema de tecnologia da Microsoft. Abrange learn.microsoft.com e documentação que fica fora dele (repositórios do VS Code, GitHub, Aspire, Agent Framework).

---

## Default: Microsoft Learn MCP

Use estas ferramentas para **tudo no learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows e mais. Esta é a ferramenta principal para a grande maioria das consultas sobre documentação da Microsoft.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Pesquisar learn.microsoft.com — conceitos, guias, tutoriais, configuração |
| `microsoft_code_sample_search` | Encontre trechos de código funcionais na documentação do Learn. Passe `language` (`python`, `csharp`, etc.) para melhores resultados |
| `microsoft_docs_fetch` | Obter o conteúdo completo da página de uma URL específica (quando os trechos de busca não são suficientes) |

Use `microsoft_docs_fetch` após a busca quando precisar de tutoriais completos, todas as opções de configuração ou quando os trechos de busca estiverem truncados.

---

## Exceptions: When to Use Other Tools

As seguintes categorias ficam **fora** do learn.microsoft.com. Use a ferramenta especificada em vez disso.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

A documentação do Aspire está em **aspire.dev**, não no Learn. A melhor ferramenta depende da sua versão do Aspire CLI:

**CLI 13.2+** (recommended) — O servidor Aspire MCP inclui ferramentas de busca de documentação integradas:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Lista toda a documentação disponível em aspire.dev |
| `search_docs` | Busca lexical ponderada no conteúdo do aspire.dev |
| `get_doc` | Recupera um documento específico pelo slug |

Essas funcionalidades são entregues no Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Para atualizar: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — O servidor MCP fornece consulta de integrações (`list_integrations`, `get_integration_docs`) mas **não** busca na documentação. Recorrer ao Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Principal — guias, integrações, referência do CLI, implantação |
| `/dotnet/aspire` | Fonte de runtime — internos da API, detalhes de implementação |
| `/communitytoolkit/aspire` | Integrações da comunidade — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

A documentação do VS Code está em **code.visualstudio.com**, não no Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Documentação do usuário — configurações, recursos, depuração, desenvolvimento remoto |
| `/websites/code_visualstudio_api` | API de extensões — webviews, TreeViews, comandos, pontos de contribuição |

### GitHub — Use Context7

A documentação do GitHub está em **docs.github.com** e **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, repositórios, segurança, administração, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) — comandos e flags |

### Agent Framework — Use Learn MCP + Context7

Os tutoriais do Agent Framework estão em learn.microsoft.com (use `microsoft_docs_search`), mas o **repositório do GitHub** contém detalhes em nível de API que frequentemente estão à frente da documentação publicada — particularmente referência da API REST do DevUI, opções do CLI e integração com .NET.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutoriais — guias do DevUI, rastreamento, orquestração de fluxos de trabalho |
| `/microsoft/agent-framework` | Detalhes da API — endpoints REST do DevUI, flags do CLI, autenticação, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Consulte a origem do site Learn para guias de como-fazer, depois a origem do repositório para especificidades em nível de API (esquemas de endpoint, configuração de proxy, tokens de autenticação).

---

## Context7 Setup

Para qualquer consulta ao Context7, resolva o ID da biblioteca primeiro (uma vez por sessão):

1. Chame `mcp_context7_resolve-library-id` com o nome da tecnologia
2. Chame `mcp_context7_query-docs` com o ID da biblioteca retornado e uma consulta específica

---

## Writing Effective Queries

Seja específico — inclua versão, intenção e linguagem:

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
Isenção de responsabilidade:

Este documento foi traduzido usando o serviço de tradução por IA Co-op Translator (https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se uma tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->