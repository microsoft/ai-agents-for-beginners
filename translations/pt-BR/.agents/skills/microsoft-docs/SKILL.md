---
name: microsoft-docs
description: Consultar a documentação oficial da Microsoft para encontrar conceitos,
  tutoriais e exemplos de código sobre Azure, .NET, Agent Framework, Aspire, VS Code,
  GitHub e mais. Utiliza o Microsoft Learn MCP como padrão, com Context7 e Aspire
  MCP para conteúdo que não está no learn.microsoft.com.
---
# Microsoft Docs

Habilidade de pesquisa para o ecossistema de tecnologia Microsoft. Abrange learn.microsoft.com e documentação que está fora dele (VS Code, GitHub, Aspire, repositórios Agent Framework).

---

## Padrão: Microsoft Learn MCP

Use estas ferramentas para **tudo no learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows e mais. Esta é a ferramenta principal para a grande maioria das consultas de documentação Microsoft.

| Ferramenta | Propósito |
|------|---------|
| `microsoft_docs_search` | Pesquise em learn.microsoft.com — conceitos, guias, tutoriais, configurações |
| `microsoft_code_sample_search` | Encontre trechos de código funcionando na documentação Learn. Passe `language` (`python`, `csharp`, etc.) para melhores resultados |
| `microsoft_docs_fetch` | Obtenha conteúdo de página completo de uma URL específica (quando os trechos da busca não forem suficientes) |

Use `microsoft_docs_fetch` após a pesquisa quando precisar de tutoriais completos, todas as opções de configuração ou quando os trechos de busca estiverem truncados.

---

## Exceções: Quando Usar Outras Ferramentas

As seguintes categorias estão **fora** do learn.microsoft.com. Use a ferramenta especificada em vez disso.

### Aspire — Use Aspire MCP Server (preferido) ou Context7

A documentação do Aspire está em **aspire.dev**, não no Learn. A melhor ferramenta depende da sua versão do Aspire CLI:

**CLI 13.2+** (recomendado) — O servidor Aspire MCP inclui ferramentas internas de busca de documentação:

| Ferramenta MCP | Descrição |
|----------|-------------|
| `list_docs` | Lista toda a documentação disponível do aspire.dev |
| `search_docs` | Busca lexical ponderada no conteúdo aspire.dev |
| `get_doc` | Recupera um documento específico pelo slug |

Estas funcionalidades são entregues no Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Para atualizar: `aspire update --self --channel daily`.

**CLI 13.1** — O servidor MCP fornece pesquisa de integração (`list_integrations`, `get_integration_docs`) mas **não** busca de documentação. Volte ao Context7:

| ID da Biblioteca | Usado para |
|---|---|
| `/microsoft/aspire.dev` | Principal — guias, integrações, referência CLI, implantação |
| `/microsoft/aspire` | Fonte do runtime — detalhes internos da API, implementação |
| `/communitytoolkit/aspire` | Integrações da comunidade — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

A documentação do VS Code está em **code.visualstudio.com**, não no Learn.

| ID da Biblioteca | Usado para |
|---|---|
| `/websites/code_visualstudio` | Documentação do usuário — configurações, recursos, depuração, desenvolvimento remoto |
| `/websites/code_visualstudio_api` | API de extensão — webviews, TreeViews, comandos, pontos de contribuição |

### GitHub — Use Context7

A documentação do GitHub está em **docs.github.com** e **cli.github.com**.

| ID da Biblioteca | Usado para |
|---|---|
| `/websites/github_en` | Actions, API, repositórios, segurança, administração, Copilot |
| `/websites/cli_github` | Comandos e flags do GitHub CLI (`gh`) |

### Agent Framework — Use Learn MCP + Context7

Tutoriais do Agent Framework estão no learn.microsoft.com (use `microsoft_docs_search`), mas o **repositório GitHub** tem detalhes no nível da API que frequentemente estão adiantados em relação à documentação publicada — particularmente referência REST API DevUI, opções CLI e integração .NET.

| ID da Biblioteca | Usado para |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutoriais — guias DevUI, rastreamento, orquestração de workflow |
| `/microsoft/agent-framework` | Detalhes da API — endpoints REST DevUI, flags CLI, autenticação, .NET `AddDevUI`/`MapDevUI` |

**Dica DevUI:** Consulte a fonte do site Learn para guias práticos, depois a fonte do repositório para detalhes nível API (esquemas de endpoints, configuração de proxy, tokens de autenticação).

---

## Configuração do Context7

Para qualquer consulta ao Context7, resolva primeiro o ID da biblioteca (uma única vez por sessão):

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
- **Idioma** para documentação poliglota (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->