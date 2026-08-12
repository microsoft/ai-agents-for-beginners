# Registro de Alterações

Todas as mudanças notáveis do curso **Agentes de IA para Iniciantes** estão documentadas neste arquivo.

## [Lançado] — 2026-07-14

Esta versão remove o curso de dois modelos recém-descontinuados, migra os notebooks restantes das Lições para a API estável do Microsoft Agent Framework e valida os notebooks Python contra uma implantação ao vivo do Microsoft Foundry.

### Alterações

- **Mudança para fora dos modelos descontinuados (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Ambos `gpt-4.1` e `gpt-4.1-mini` estão agora descontinuados (data oficial de aposentadoria **14 de outubro de 2026**). Substituída toda referência do curso (documentação, `.env.example`, notebooks Python/.NET e exemplos) pelo `gpt-5-mini` não descontinuado. O exemplo de roteamento de modelos da Lição 16 mantém um contraste pequeno/grande usando `gpt-5-nano` (pequeno) e `gpt-5-mini` (grande). Arquivos de terceiros incluídos no repositório ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), texto histórico do GitHub Models e notas de capacidade da skill `azure-openai-to-responses` foram intencionalmente mantidos sem alterações.
- **Notebook de transferência da Lição 14 migrado para a API estável.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) agora utiliza `agent_framework.orchestrations.HandoffBuilder` com `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, streaming baseado em `event.type`, e `FoundryChatClient` (substituindo os símbolos removidos pré-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Notebook de intervenção humana da Lição 14 migrado para a API estável.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) agora pausa via `ctx.request_info(...)` + `@response_handler` (substituindo o removido `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), constrói com `WorkflowBuilder(start_executor=..., output_executors=[...])`, direciona saída estruturada via `default_options={"response_format": ...}`, e utiliza uma resposta scriptada para que o notebook seja executado automaticamente (sem bloqueio de `input()`).
- **Configuração do ambiente** ([.env.example](../../.env.example)): alterados os nomes de implantação dos modelos para `gpt-5-mini`; adicionados `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (roteamento da Lição 16) e o `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` anteriormente ausente (uso do navegador na Lição 15).
- **Dependências** ([requirements.txt](../../requirements.txt)): fixadas as versões de `agent-framework`, `agent-framework-foundry` e `agent-framework-openai` para `~=1.10.0` para um conjunto validado e auto consistente (1.11.0 inclui mudanças experimentais quebrando as superfícies usadas nestas lições).

### Observações e limitações conhecidas

- **Validado contra Microsoft Foundry ao vivo.** Os notebooks Python foram executados sem interface gráfica com `nbconvert` contra um projeto do Microsoft Foundry usando `gpt-5-mini` (e `gpt-5-nano` para roteamento da Lição 16). Implante modelos equivalentes não descontinuados no seu próprio projeto; os notebooks leem o nome da implantação das variáveis `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Requer recursos extras para algumas lições.** A Lição 05 precisa do Azure AI Search; o fluxo de trabalho fundamentado no Bing da Lição 08 (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) precisa de conexão com Bing e ferramentas hospedadas do Microsoft Foundry Agent Service; as Lições 13 (Cognee) e 17 (Foundry Local) precisam de seus próprios ambientes de execução.

## [Lançado] — 2026-07-13

Esta versão adiciona duas novas lições que completam o arco de implantação — escalando agentes até o Microsoft Foundry e redimensionando para uma única estação de trabalho — além de um pipeline de teste rápido, navegação do curso atualizada, novas habilidades para aprendizes e atualização da identidade visual.

### Adições

- **Lição 16 — Implantando Agentes Escaláveis com Microsoft Foundry.** Nova lição [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) e notebook executável [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) construindo um agente de suporte ao cliente em produção (ferramentas, RAG, memória, roteamento de modelo, cache de respostas, aprovação humana, portão de avaliação e rastreamento OpenTelemetry), com diagramas Mermaid para desenvolvimento/implantação/execução, um teste de conhecimento, um exercício e um desafio.
- **Lição 17 — Criando Agentes de IA Locais com Foundry Local e Qwen.** Nova lição [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) e notebook [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) construindo um assistente de engenharia totalmente no dispositivo (chamadas de função Qwen via Foundry Local, ferramentas de arquivo em sandbox, RAG local com Chroma, MCP local opcional), com diagramas de somente local / RAG local / chamada de ferramentas, um teste de conhecimento, um exercício e um desafio.
- **Pipeline de teste rápido.** Novo workflow [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) além de catálogos por lição sob [tests/](./tests/README.md) para os agentes implantáveis nas Lições 01, 04, 05 e 16, com um README índice que mapeia cada catálogo para sua lição e nome do agente hospedado. A Lição 16 ganha uma seção "Validando um Agente Implantado com Testes Rápidos"; as Lições 01/04/05 ganham um apontador opcional para testes rápidos.
- **Habilidades para aprendizes.** Novas Habilidades de Agentes sob `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (consolidando as orientações das Lições 16 e 17), e [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (como validar os exemplos de notebooks contra uma instalação Microsoft Foundry / Azure OpenAI ao vivo).
- **Executor de validação de notebooks.** Novo [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) que executa cada notebook Python sem interface gráfica com `nbconvert` e imprime uma matriz de APROVADO/REPROVADO (além de `results.json`). Ele detecta automaticamente a raiz do repositório e o Python, exclui notebooks fora do curso (`.venv`, `site-packages`, `translations`, recursos de skill templates) e notebooks `.NET` por padrão, e suporta `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` e `-Python`.
- **Navegação do curso.** Adicionados links de Lições Anteriores/Próximas para as Lições 11 a 15 (antes ausentes) para que todo o curso encadeie da 00 à 18 em ambas as direções.
- **Novas miniaturas.** Miniaturas de lição para as Lições 16 e 17, além de uma imagem social atualizada do repositório [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (agora anunciando as duas novas lições e a URL `aka.ms/ai-agents-beginners`).
- **Dependências** ([requirements.txt](../../requirements.txt)): adicionados `foundry-local-sdk` e `chromadb` para a Lição 17.

### Alterações

- **Tabela principal de lições do [README.md](./README.md)**: Lições 16 e 17 agora linkam para seus conteúdos (antes "Em breve"); imagem do repositório atualizada para `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: adicionadas as Lições 16 e 17 no guia lição por lição e percursos de aprendizado, e seção "Validando Agentes Implantados com Testes Rápidos".
- **[AGENTS.md](./AGENTS.md)**: atualizada a contagem/descrição de lições (00–18), adicionada seção de validação por teste rápido, e exemplos de nomeação para as Lições 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Lição Anterior" agora aponta para a Lição 17 (antes Lição 15), fechando o encadeamento.
- **Referências aos modelos padronizadas para modelos não descontinuados.** Substituídas todas as referências `gpt-4o` / `gpt-4o-mini` por todo o curso (docs, `.env.example`, notebooks Python/.NET e exemplos) para `gpt-4.1-mini` — `gpt-4o` (todas as versões) será aposentado em 2026. O exemplo de roteamento de modelos da Lição 16 mantém um contraste pequeno/grande usando `gpt-4.1-mini` (pequeno) e `gpt-4.1` (grande). Notebooks Python agora selecionam o modelo a partir das variáveis de ambiente (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) em vez de codificar o nome do modelo.

### Observações e limitações conhecidas

- **Não executado contra Azure ao vivo.** Os notebooks das novas lições são exemplos educacionais; execute e valide-os contra a sua própria instalação Microsoft Foundry / Foundry Local. O workflow de teste rápido requer que você implante o agente da lição e configure segredos Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) com o papel **Azure AI User** no escopo do projeto Foundry.
- **Lição 17 é somente local.** Não possui endpoint Foundry Responses, então a ação de teste rápido não se aplica; valide-a executando o notebook em sua estação de trabalho.

## [Lançado] — 2026-07-06

Esta versão migra o curso para a **Azure OpenAI Responses API**, padroniza a nomenclatura do produto para **Microsoft Foundry** e o **Microsoft Agent Framework (MAF)**, aposenta GitHub Models, atualiza versões de SDK e adiciona novo conteúdo sobre modelos locais e hospedagem de outras frameworks no Foundry.

### Adições

- **Skill de migração** — Instalado a Skill do Agente [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (do repositório [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) sob `.agents/skills/`, incluindo suas referências e script de varredura.
- **Foundry Local (executar modelos no dispositivo)** — Nova seção "Provedor Alternativo: Foundry Local" em [00-course-setup/README.md](./00-course-setup/README.md) cobrindo instalação (`winget` / `brew`), `foundry model run`, o `foundry-local-sdk` e a conexão do `FoundryLocalManager` ao Microsoft Agent Framework via `OpenAIChatClient`.
- **Hospedando agentes LangChain / LangGraph no Microsoft Foundry** — Nova seção em [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) além de exemplo executável [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) usando `langchain-azure-ai[hosting]` e `ResponsesHostServer` (protocolo `/responses`), com base no [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nova seção "Exemplo do Mundo Real: Microsoft Project Opal" em [15-browser-use/README.md](./15-browser-use/README.md) enquadrando Opal como um agente empresarial de uso do computador e relacionando-o aos conceitos do curso (intervenção humana, confiabilidade/segurança, planejamento, Skills).
- **Segundo exemplo Python da Lição 02** — Adicionado [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (ver "Alterações" — migrado do notebook anterior Semantic Kernel) e linkado no README da lição.
- **Seção Modelos e Provedores** adicionada a [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Alterações

- **Chat Completions → Responses API (Python).** Exemplos que chamavam o modelo diretamente foram migrados de Chat Completions para a Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), usando o cliente `OpenAI` contra o endpoint estável Azure OpenAI `/openai/v1/` (sem `api_version`). Exemplos afetados incluem:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — o walkthrough completo de chamadas de função (esquema da ferramenta convertido ao formato Responses, resultados das ferramentas retornados como `function_call_output`, `max_output_tokens`, etc.).

- **Modelos GitHub → Azure OpenAI.** Modelos GitHub está obsoleto (descontinuado **julho de 2026**) e não suporta a API de Respostas. Todos os caminhos de código dos Modelos GitHub foram convertidos para Azure OpenAI / Microsoft Foundry em exemplos Python e .NET:
  - Python: notebooks do fluxo de trabalho da Lições 08 (`01`–`03`), Lição 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + documentação complementar `.md`, e os notebooks/`.md` do fluxo de trabalho dotNET da Lição 08 (`01`–`03`) agora usam `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` com `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** O antigo `02-semantic-kernel.ipynb` foi reescrito para usar o Microsoft Agent Framework com Azure OpenAI (API de Respostas) e renomeado para `02-python-agent-framework-azure-openai.ipynb`.
- **Padronizado em `FoundryChatClient` + `as_agent`.** README e código dos notebooks que referenciavam `AzureAIProjectAgentProvider` foram padronizados no padrão canônico usado pela Lição 01 e pelos próprios exemplos do framework: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` com `provider.as_agent(...)`. Atualizado nas READMEs e notebooks da Lição 02–14 (exemplo, memória da Lição 13, todos os notebooks da Lição 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Nome do produto.** Renomeado em todo o conteúdo em inglês:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Inalterado: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" e nomes de variáveis de ambiente.)
- **Dependências** ([requirements.txt](../../requirements.txt)):
  - Fixados `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Fixado `openai>=1.108.1` (mínimo para a API de Respostas).
  - Removido `azure-ai-inference` (usado apenas pelos exemplos migrados dos Modelos GitHub).
- **Configuração do ambiente** ([.env.example](../../.env.example)): removidas as variáveis dos Modelos GitHub (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); adicionadas `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` e opcional `AZURE_OPENAI_API_KEY`; atualizada a nomenclatura para Microsoft Foundry.
- **Documentação** — Atualizados [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) e [STUDY_GUIDE.md](./STUDY_GUIDE.md) para o acima (configuração de variáveis de ambiente, trecho de verificação, orientação de provider, nomenclatura).

### Removido

- Etapas de onboarding dos Modelos GitHub e variáveis de ambiente dos docs de configuração (substituídos por Azure OpenAI / Microsoft Foundry).

### Segurança / Privacidade (limpeza para compartilhamento público)

- Limpadas saídas de execução dos notebooks Jupyter que vazaram um real **ID de assinatura Azure**, nomes de grupos de recursos / recursos e ID de conexão Bing, além de **caminhos locais e nomes de usuário** do desenvolvedor, em:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Verificado que não restam chaves de API, tokens, IDs de assinatura ou caminhos pessoais no conteúdo inglês rastreado (as referências ao `GITHUB_TOKEN` restantes são o token do GitHub Actions nos workflows e o PAT do servidor GitHub MCP na configuração da Lição 11 — ambos legítimos e não relacionados aos Modelos GitHub).

### Notas e limitações conhecidas

- **Não executados/compilados.** Esses são exemplos educacionais atualizados para correção de API/nomenclatura; não foram executados contra recursos ativos no Azure, e os exemplos .NET não foram compilados neste ambiente. Valide contra seu próprio deployment Microsoft Foundry / Azure OpenAI.
- **O deployment do modelo deve suportar a API de Respostas.** Use um deployment como `gpt-4.1-mini`, `gpt-4.1` ou um modelo `gpt-5.x`. Modelos mais antigos suportam a funcionalidade básica de Respostas, mas não todos os recursos.
- **Versão do agent-framework.** Os exemplos são voltados para a última versão do MAF (`>=1.10.0`). A chamada canônica para criação de agente é `client.as_agent(...)`; as APIs foram validadas contra a documentação publicada e uma build instalada do framework. Se fixar uma versão diferente, confirme a disponibilidade do método (`as_agent` vs `create_agent`).
- **Notebook do fluxo de trabalho da Lição 08, exemplo 04** intencionalmente mantém `AzureAIAgentClient` (de `agent-framework-azure-ai`) porque usa ferramentas hospedadas do Microsoft Foundry Agent Service (fundamentação Bing, interpretador de código); já está baseado em Respostas.
- **Deployment padrão do .NET.** Dois exemplos do fluxo de trabalho dotNET da Lição 08 tinham hardcoded um modelo específico; agora usam por padrão `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Se um exemplo depende de entrada multimodal/visão, defina `AZURE_OPENAI_DEPLOYMENT` para um modelo adequado.
- **Foundry Local** expõe um endpoint compatível com OpenAI para **Chat Completions** e se destina a desenvolvimento local; use Azure OpenAI / Microsoft Foundry para o conjunto completo de recursos da API de Respostas.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->