---
name: microsoft-docs
description: Consultar a documentação oficial da Microsoft para encontrar conceitos,
  tutoriais e exemplos de código sobre Azure, .NET, Agent Framework, Aspire, VS Code,
  GitHub e mais. Utiliza o Microsoft Learn MCP como predefinição, com o Context7 e
  o Aspire MCP para conteúdo que se encontra fora do learn.microsoft.com.
---
# Microsoft Docs

Pesquisa de competências para o ecossistema tecnológico da Microsoft. Abrange learn.microsoft.com e documentação que vive fora dele (VS Code, GitHub, Aspire, repositórios do Agent Framework).

---

## Predefinido: Microsoft Learn MCP

Use estas ferramentas para **tudo em learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows e mais. Esta é a ferramenta principal para a grande maioria das consultas sobre documentação da Microsoft.

| Ferramenta | Finalidade |
|------|---------|
| `microsoft_docs_search` | Pesquisar em learn.microsoft.com — conceitos, guias, tutoriais, configuração |
| `microsoft_code_sample_search` | Encontrar snippets de código funcionais nas docs do Learn. Indique `language` (`python`, `csharp`, etc.) para melhores resultados |
| `microsoft_docs_fetch` | Obter o conteúdo completo da página a partir de uma URL específica (quando os excertos da pesquisa não bastam) |

Use `microsoft_docs_fetch` após a pesquisa quando precisar de tutoriais completos, todas as opções de configuração ou quando os excertos da pesquisa estiverem truncados.

---

## Exceções: Quando Usar Outras Ferramentas

As seguintes categorias vivem **fora** do learn.microsoft.com. Use a ferramenta especificada em vez disso.

### .NET Aspire — Utilize o Aspire MCP Server (preferível) ou o Context7

A documentação do Aspire está em **aspire.dev**, não no Learn. A melhor ferramenta depende da versão do Aspire CLI:

**CLI 13.2+** (recomendado) — O Aspire MCP server inclui ferramentas de pesquisa de documentação integradas:

| Ferramenta MCP | Descrição |
|----------|-------------|
| `list_docs` | Lista toda a documentação disponível em aspire.dev |
| `search_docs` | Pesquisa léxica ponderada no conteúdo do aspire.dev |
| `get_doc` | Recupera um documento específico por slug |

Isto foi incluído no Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Para atualizar: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — O MCP server fornece pesquisa de integrações (`list_integrations`, `get_integration_docs`) mas **não** pesquisa de documentação. Recorra ao Context7:

| ID da Biblioteca | Utilizar para |
|---|---|
| `/microsoft/aspire.dev` | Principal — guias, integrações, referência do CLI, deployment |
| `/dotnet/aspire` | Código-fonte do runtime — internals da API, detalhes de implementação |
| `/communitytoolkit/aspire` | Integrações da comunidade — Go, Java, Node.js, Ollama |

### VS Code — Utilize o Context7

A documentação do VS Code está em **code.visualstudio.com**, não no Learn.

| ID da Biblioteca | Utilizar para |
|---|---|
| `/websites/code_visualstudio` | Docs de utilizador — definições, funcionalidades, debugging, desenvolvimento remoto |
| `/websites/code_visualstudio_api` | API de extensões — webviews, TreeViews, comandos, pontos de contribuição |

### GitHub — Utilize o Context7

A documentação do GitHub está em **docs.github.com** e **cli.github.com**.

| ID da Biblioteca | Utilizar para |
|---|---|
| `/websites/github_en` | Actions, API, repositórios, segurança, administração, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) — comandos e flags |

### Agent Framework — Utilize Learn MCP + Context7

Os tutoriais do Agent Framework estão no learn.microsoft.com (use `microsoft_docs_search`), mas o **repositório GitHub** tem detalhes ao nível da API que muitas vezes estão à frente da documentação publicada — particularmente a referência DevUI REST API, opções do CLI e integração .NET.

| ID da Biblioteca | Utilizar para |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutoriais — guias DevUI, tracing, orquestração de workflows |
| `/microsoft/agent-framework` | Detalhe da API — endpoints REST do DevUI, flags do CLI, autenticação, .NET `AddDevUI`/`MapDevUI` |

**Dica DevUI:** Consulte a fonte do site Learn para guias how-to, depois a fonte do repositório para especificidades ao nível da API (esquemas de endpoints, configuração de proxy, tokens de autenticação).

---

## Configuração do Context7

Para qualquer consulta ao Context7, resolva primeiro o ID da biblioteca (uma vez por sessão):

1. Chame `mcp_context7_resolve-library-id` com o nome da tecnologia
2. Chame `mcp_context7_query-docs` com o ID da biblioteca retornado e uma query específica

---

## Escrever Queries Eficazes

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

Inclua contexto:
- **Versão** quando relevante (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Intenção da tarefa** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Linguagem** para documentação poliglota (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original, na sua língua nativa, deve ser considerado a fonte fidedigna. Para informação crítica, recomenda-se uma tradução profissional efetuada por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->