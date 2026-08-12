# Changelog

Todas as alterações notáveis ao curso **Agentes de IA para Iniciantes** estão documentadas neste ficheiro.

## [Lançado] — 2026-07-14

Esta versão descontinua o curso em dois modelos recentemente desaprovados, migra os Cadernos das Lições restantes para a API estável do Microsoft Agent Framework, e valida os cadernos Python contra uma implementação em direto da Microsoft Foundry.

### Alterações

- **Mudança para fora de modelos desaprovados (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Os modelos `gpt-4.1` e `gpt-4.1-mini` estão agora desaprovados (data de descontinuação publicada **14 de outubro de 2026**). Substituíram-se todas as referências do curso (documentação, `.env.example`, cadernos Python/.NET e exemplos) pelo modelo não desaprovado `gpt-5-mini`. O exemplo de encaminhamento de modelo da Lição 16 mantém um contraste pequeno/grande usando `gpt-5-nano` (pequeno) e `gpt-5-mini` (grande). Os ficheiros fornecidos de terceiros ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), texto histórico do GitHub Models, e as notas de capacidades da skill `azure-openai-to-responses` permaneceram intencionalmente inalterados.
- **Caderno da Lição 14 de entrega migrado para a API estável.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) usa agora `agent_framework.orchestrations.HandoffBuilder` com `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, streaming baseado em `event.type`, e `FoundryChatClient` (substituindo os símbolos removidos pré-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Caderno da Lição 14 de intervenção humana migrado para a API estável.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) pausa agora usando `ctx.request_info(...)` + `@response_handler` (substituindo o removido `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), constrói com `WorkflowBuilder(start_executor=..., output_executors=[...])`, conduz saída estruturada via `default_options={"response_format": ...}`, e usa uma resposta predefinida para que o caderno funcione sem intervenção (sem bloqueio com `input()`).
- **Configuração do ambiente** ([.env.example](../../.env.example)): alterados os nomes das implantações dos modelos para `gpt-5-mini`; adicionados `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (encaminhamento na Lição 16) e o anteriormente em falta `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (uso no navegador da Lição 15).
- **Dependências** ([requirements.txt](../../requirements.txt)): fixadas as versões de `agent-framework`, `agent-framework-foundry` e `agent-framework-openai` para `~=1.10.0` para um conjunto auto-consistente e validado (a versão 1.11.0 traz mudanças experimentais que quebram as superfícies usadas nestas lições).

### Notas e limitações conhecidas

- **Validado contra Microsoft Foundry em direto.** Os cadernos Python foram executados sem interface com `nbconvert` contra um projeto Microsoft Foundry usando `gpt-5-mini` (e `gpt-5-nano` para o encaminhamento na Lição 16). Implemente modelos equivalentes não desaprovados no seu próprio projeto; os cadernos leem o nome da implantação de `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Ainda requer recursos adicionais para algumas lições.** A Lição 05 necessita do Azure AI Search; o fluxo de trabalho da Lição 08 com Bing-grounding (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) necessita de ligação ao Bing e ferramentas hospedadas do Microsoft Foundry Agent Service; as Lições 13 (Cognee) e 17 (Foundry Local) requerem os seus próprios ambientes de execução.

## [Lançado] — 2026-07-13

Esta versão acrescenta duas novas lições que completam o arco de implementação — dimensionando agentes até o Microsoft Foundry e recuando para uma única estação de trabalho — mais um pipeline de teste rápido, navegação do curso atualizada, novas competências para o aluno e identidade visual atualizada.

### Adicionado

- **Lição 16 — Implementação de Agentes Escaláveis com Microsoft Foundry.** Nova lição [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) e caderno executável [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) construindo um agente de suporte ao cliente de produção (ferramentas, RAG, memória, encaminhamento de modelo, cache de respostas, aprovação humana, portão de avaliação, e rastreamento OpenTelemetry), com diagramas Mermaid de desenvolvimento/implementação/corrida, verificação de conhecimento, tarefa e desafio.
- **Lição 17 — Criação de Agentes de IA Locais com Foundry Local e Qwen.** Nova lição [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) e caderno [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) construindo um assistente de engenharia totalmente local (chamada de função Qwen via Foundry Local, ferramentas de ficheiros sandboxed, RAG local com Chroma, MCP local opcional), com diagramas local-só / local-RAG / chamada de ferramentas, verificação de conhecimento, tarefa e desafio.
- **Pipeline de teste rápido.** Novo fluxo de trabalho [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) mais catálogos por lição sob [tests/](./tests/README.md) para os agentes implementáveis nas Lições 01, 04, 05 e 16, com um README índice a mapear cada catálogo para a lição e nome do agente hospedado. A Lição 16 ganha a secção "Validando um Agente Implementado com Testes de Fumaça"; as Lições 01/04/05 ganham uma indicação opcional para teste de fumaça.
- **Competências do aluno.** Novas Competências de Agente sob `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (embalando as orientações das Lições 16 e 17), e [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (como validar os exemplos dos cadernos contra uma configuração real Microsoft Foundry / Azure OpenAI).
- **Validador de cadernos.** Novo [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) que executa cada caderno Python headlessly com `nbconvert` e imprime uma matriz PASSAR/FALHAR (mais `results.json`). Detecta automaticamente a raiz do repositório e Python, exclui por defeito cadernos fora do curso (`.venv`, `site-packages`, `translations`, ativos de templates de skills) e cadernos `.NET`, e suporta `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, e `-Python`.
- **Navegação do curso.** Adicionados links Anterior/Seguinte nas Lições 11–15 (antes ausentes) para encadear todo o curso de 00 → 18 em ambos os sentidos.
- **Novas miniaturas.** Miniaturas para as Lições 16 e 17, mais imagem social do repositório atualizada [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (agora a publicitar as duas novas lições e a URL `aka.ms/ai-agents-beginners`).
- **Dependências** ([requirements.txt](../../requirements.txt)): adicionados `foundry-local-sdk` e `chromadb` para a Lição 17.

### Alterações

- **Tabela principal das lições em [README.md](./README.md)**: as Lições 16 e 17 agora ligam para os seus conteúdos (antes "Em Breve"); imagem do repositório actualizada para `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: adicionadas as Lições 16 e 17 ao guia lição-a-lição e percursos de aprendizagem, e uma seção "Validando Agentes Implementados com Testes de Fumaça".
- **[AGENTS.md](./AGENTS.md)**: atualizada a contagem/descrição das lições (00–18), adicionada a secção de validação com testes de fumaça, e adicionados exemplos de nomeação para amostras das Lições 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Lição Anterior" agora aponta para a Lição 17 (antes Lição 15), encerrando a cadeia.
- **Referências aos modelos padronizadas em modelos não desaprovados.** Substituídas todas as referências `gpt-4o` / `gpt-4o-mini` no curso (documentação, `.env.example`, cadernos Python/.NET e exemplos) por `gpt-4.1-mini` — `gpt-4o` (todas versões) será descontinuado em 2026. O exemplo de encaminhamento de modelo da Lição 16 mantém o contraste pequeno/grande usando `gpt-4.1-mini` (pequeno) e `gpt-4.1` (grande). Os cadernos Python agora selecionam o modelo via variáveis de ambiente (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) em vez de codificar diretamente o nome do modelo.

### Notas e limitações conhecidas

- **Não executado contra Azure em direto.** Os novos cadernos das lições são amostras educativas; execute-os e valide-os na sua própria instalação do Microsoft Foundry / Foundry Local. O fluxo de trabalho dos testes de fumaça exige que implemente o agente da lição e configure os segredos Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) com o papel **Usuário Azure AI** ao nível do projeto Foundry.
- **A Lição 17 é apenas local.** Não tem ponto de extremidade Foundry Responses, pelo que a ação de teste de fumaça não se aplica; valide-a executando o caderno na sua estação de trabalho.

## [Lançado] — 2026-07-06

Esta versão migra o curso para a **API Azure OpenAI Responses**, padroniza a nomenclatura dos produtos em **Microsoft Foundry** e **Microsoft Agent Framework (MAF)**, descontinua GitHub Models, atualiza versões de SDK, e adiciona novo conteúdo sobre modelos locais e alojar outros frameworks no Foundry.

### Adicionado

- **Skill de migração** — Instalado o Agent Skill [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (do repositório [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) sob `.agents/skills/`, incluindo as suas referências e script de scanner.
- **Foundry Local (execução de modelos no dispositivo)** — Nova secção "Fornecedor Alternativo: Foundry Local" em [00-course-setup/README.md](./00-course-setup/README.md) cobrindo instalação (`winget` / `brew`), `foundry model run`, o `foundry-local-sdk`, e ligação do `FoundryLocalManager` ao Microsoft Agent Framework via `OpenAIChatClient`.
- **Alojamento de agentes LangChain / LangGraph no Microsoft Foundry** — Nova secção em [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) mais um exemplo executável [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) usando `langchain-azure-ai[hosting]` e `ResponsesHostServer` (o protocolo `/responses`), baseado em [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Projeto Microsoft Opal** — Nova secção "Exemplo no Mundo Real: Projeto Microsoft Opal" em [15-browser-use/README.md](./15-browser-use/README.md) a enquadrar o Opal como agente empresarial para utilização informática e a mapear os seus conceitos ao curso (intervenção humana, confiança/segurança, planeamento, Skills).
- **Segundo exemplo Python da Lição 02** — Adicionado [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (ver "Alterado" — migrado do antigo caderno Semantic Kernel) e ligado no README da lição.
- **Secção de Modelos e Fornecedores** adicionada a [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Alterações

- **Chat Completions → Responses API (Python).** Exemplos que chamavam diretamente o modelo foram migrados de Chat Completions para a Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), usando o cliente `OpenAI` contra o endpoint estável do Azure OpenAI `/openai/v1/` (sem `api_version`). Exemplos afetados incluem:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — o percurso completo de chamada de função (esquema da ferramenta convertido para o formato Responses, resultados das ferramentas retornados como `function_call_output`, `max_output_tokens`, etc.).

- **Modelos GitHub → Azure OpenAI.** Os modelos GitHub estão descontinuados (fim em **julho de 2026**) e não suportam a API de Respostas. Todos os caminhos de código dos modelos GitHub foram convertidos para Azure OpenAI / Microsoft Foundry em exemplos Python e .NET:
  - Python: cadernos do fluxo de trabalho da Lição 08 (`01`–`03`), Lição 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + documentação `.md` acompanhante, e os cadernos/`.md` do fluxo de trabalho dotNET da Lição 08 (`01`–`03`) usam agora `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` com `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** O antigo `02-semantic-kernel.ipynb` foi reescrito para usar o Microsoft Agent Framework com Azure OpenAI (API de Respostas) e renomeado para `02-python-agent-framework-azure-openai.ipynb`.
- **Padronização em `FoundryChatClient` + `as_agent`.** O README e código dos cadernos que referenciavam `AzureAIProjectAgentProvider` foram padronizados segundo o padrão canónico utilizado pela Lição 01 e pelos próprios exemplos do framework: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` com `provider.as_agent(...)`. Atualizado nos READMEs e cadernos das Lições 02–14 (ex., memória na Lição 13, todos os cadernos da Lição 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Naming de produto.** Renomeado em todo o conteúdo em inglês:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Inalterado: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" e nomes de variáveis de ambiente.)
- **Dependências** ([requirements.txt](../../requirements.txt)):
  - Travados `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Travado `openai>=1.108.1` (mínimo para a API de Respostas).
  - Removido `azure-ai-inference` (usado apenas pelos exemplos GitHub Models migrados).
- **Configuração de ambiente** ([.env.example](../../.env.example)): removidas variáveis GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); adicionadas `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` e opcional `AZURE_OPENAI_API_KEY`; nomenclatura atualizada para Microsoft Foundry.
- **Documentação** — Atualizado [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) e [STUDY_GUIDE.md](./STUDY_GUIDE.md) para o acima (configuração de variáveis de ambiente, trecho de verificação, orientação para providers, nomenclatura).

### Removido

- Passos de onboarding de modelos GitHub e variáveis de ambiente dos documentos de configuração (substituídos por Azure OpenAI / Microsoft Foundry).

### Segurança / Privacidade (limpeza para partilha pública)

- Limpeza das saídas de execução dos cadernos Jupyter que continham um verdadeiro **ID de subscrição Azure**, nomes de grupo/recurso e ID de ligação Bing, além de nomes de utilizador e caminhos locais dos programadores, em:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Verificação de que não permanecem chaves API, tokens, IDs de subscrição ou caminhos pessoais no conteúdo rastreado em inglês (as referências a `GITHUB_TOKEN` que permanecem são o token GitHub Actions nos workflows e o PAT do servidor GitHub MCP na configuração da Lição 11 — ambos legítimos e não relacionados com modelos GitHub).

### Notas e limitações conhecidas

- **Não executados/compilados.** Estes são exemplos educativos atualizados para correção de API/nomeação; não foram executados contra recursos Azure reais, e os exemplos .NET não foram compilados neste ambiente. Valide com a sua própria implantação Microsoft Foundry / Azure OpenAI.
- **Desdobramento de modelo deve suportar a API de Respostas.** Use um desdobramento como `gpt-4.1-mini`, `gpt-4.1` ou um modelo `gpt-5.x`. Modelos antigos suportam funcionalidade básica da API de Respostas mas não todas as funcionalidades.
- **Versão do agent-framework.** Os exemplos visam o MAF mais recente (`>=1.10.0`). A chamada canónica para criação do agente é `client.as_agent(...)`; APIs foram validadas contra a documentação publicada do framework e numa build instalada. Se usar uma versão travada diferente, confirme a disponibilidade do método (`as_agent` vs `create_agent`).
- **O caderno do fluxo de trabalho da Lição 08 04** mantém intencionalmente `AzureAIAgentClient` (do `agent-framework-azure-ai`) porque usa ferramentas alojadas Microsoft Foundry Agent Service (ancoragem Bing, interpretador de código); já é baseado em Respostas.
- **Desdobramento padrão .NET.** Dois exemplos de fluxo de trabalho dotNET da Lição 08 codificavam anteriormente um modelo específico; agora usam por padrão `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Se um exemplo necessita entrada multimodal/visão, defina `AZURE_OPENAI_DEPLOYMENT` para um modelo adequado.
- **Foundry Local** expõe um endpoint de **Chat Completions** compatível com OpenAI e destina-se a desenvolvimento local; use Azure OpenAI / Microsoft Foundry para o conjunto completo de funcionalidades da API de Respostas.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->