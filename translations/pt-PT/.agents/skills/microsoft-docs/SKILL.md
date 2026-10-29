---
name: microsoft-docs
description: Consultar documentação oficial da Microsoft para encontrar conceitos,
  tutoriais e exemplos de código sobre Azure, .NET, Agent Framework, Aspire, VS Code,
  GitHub e mais. Utiliza o Microsoft Learn MCP como padrão, com o Context7 e Aspire
  MCP para conteúdos que se encontram fora do learn.microsoft.com.
---
# Microsoft Docs

Competência de pesquisa para o ecossistema tecnológico Microsoft. Abrange learn.microsoft.com e documentação que está fora dele (VS Code, GitHub, Aspire, repositórios do Agent Framework).

---

## Padrão: Microsoft Learn MCP

Utilize estas ferramentas para **tudo em learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows e mais. Esta é a ferramenta principal para a grande maioria das pesquisas de documentação Microsoft.

| Ferramenta | Propósito |
|------|---------|
| `microsoft_docs_search` | Pesquisar em learn.microsoft.com — conceitos, guias, tutoriais, configuração |
| `microsoft_code_sample_search` | Encontrar snippets de código funcionais a partir dos documentos Learn. Passe `language` (`python`, `csharp`, etc.) para melhores resultados |
| `microsoft_docs_fetch` | Obter conteúdo completo da página a partir de uma URL específica (quando os excertos de pesquisa não são suficientes) |

Use `microsoft_docs_fetch` após a pesquisa quando precisar de tutoriais completos, todas as opções de configuração ou quando os excertos da pesquisa estiverem truncados.

---

## Exceções: Quando Usar Outras Ferramentas

As seguintes categorias estão **fora** do learn.microsoft.com. Use a ferramenta especificada em vez disso.

### Aspire — Use Aspire MCP Server (preferido) ou Context7

A documentação do Aspire encontra-se em **aspire.dev**, não no Learn. A melhor ferramenta depende da sua versão do Aspire CLI:

**CLI 13.2+** (recomendado) — O servidor Aspire MCP inclui ferramentas integradas de pesquisa de documentação:

| Ferramenta MCP | Descrição |
|----------|-------------|
| `list_docs` | Lista toda a documentação disponível em aspire.dev |
| `search_docs` | Pesquisa lexicográfica ponderada através do conteúdo de aspire.dev |
| `get_doc` | Recupera um documento específico pelo slug |

Estes estão incluídos no Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Para atualizar: `aspire update --self --channel daily`.

**CLI 13.1** — O servidor MCP oferece pesquisa de integrações (`list_integrations`, `get_integration_docs`) mas **não** pesquisa de documentação. Use Context7 como alternativa:

| ID da Biblioteca | Utilização |
|---|---|
| `/microsoft/aspire.dev` | Principal — guias, integrações, referência do CLI, deployment |
| `/microsoft/aspire` | Fonte runtime — internals da API, detalhes de implementação |
| `/communitytoolkit/aspire` | Integrações da comunidade — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

A documentação do VS Code está em **code.visualstudio.com**, não no Learn.

| ID da Biblioteca | Utilização |
|---|---|
| `/websites/code_visualstudio` | Documentação do utilizador — definições, funcionalidades, debugging, desenvolvimento remoto |
| `/websites/code_visualstudio_api` | API de Extensão — webviews, TreeViews, comandos, pontos de contribuição |

### GitHub — Use Context7

A documentação do GitHub está em **docs.github.com** e **cli.github.com**.

| ID da Biblioteca | Utilização |
|---|---|
| `/websites/github_en` | Actions, API, repositórios, segurança, administração, Copilot |
| `/websites/cli_github` | Comandos e flags do GitHub CLI (`gh`) |

### Agent Framework — Use Learn MCP + Context7

Os tutoriais do Agent Framework estão em learn.microsoft.com (use `microsoft_docs_search`), mas o **repositório GitHub** tem detalhes ao nível da API que frequentemente estão à frente dos documentos publicados — particularmente referência REST API do DevUI, opções do CLI e integração .NET.

| ID da Biblioteca | Utilização |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutoriais — guias DevUI, tracing, orquestração do workflow |
| `/microsoft/agent-framework` | Detalhes da API — endpoints REST do DevUI, flags do CLI, autenticação, .NET `AddDevUI`/`MapDevUI` |

**Dica DevUI:** Pesquise primeiro no website Learn para guias práticos, depois no repositório para especificações ao nível da API (esquemas de endpoints, config proxy, tokens de autenticação).

---

## Configuração do Context7

Para qualquer pesquisa Context7, obtenha primeiro o ID da biblioteca (uma vez por sessão):

1. Chame `mcp_context7_resolve-library-id` com o nome da tecnologia
2. Chame `mcp_context7_query-docs` com o ID da biblioteca retornado e uma consulta específica

---

## Como Escrever Consultas Eficazes

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
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->